#!/usr/bin/env python3
#
"""
z3solve.py: Given a state, county and tract, construct and solve the database reconstruction problem using Z3.

"""

__version__ = '0.1.0'
import datetime
import json
import os
import os.path
import re
import sqlite3
import sys
import time
import zipfile
import io
import csv
import logging
from collections import defaultdict

# Database loading
DBFILE="sf1.sqlite3"
CACHE_SIZE = -1024*16           # negative nubmer = multiple of 1024. So this is a 16MB cache.
SQL_SET_CACHE = "PRAGMA cache_size = {};".format(CACHE_SIZE)


################
## SF1 problem encoding
VAR_SUFFIXES = 'AHSwbisho'
RACES='wbisho'

COL_TO_SUFFIX_MAP = {'hispanic':'H',
                     'sex':'S',
                     'white':'w',
                     'black':'b',
                     'aian':'i',
                     'asian':'s',
                     'nhopi':'h',
                     'sor':'o'}
COL_VAL_MAPPING = {'Y':'true',
                   'N':'false',
                   'male':'Male',
                   'female':'Female',
                   'hispanic':'Hispanic'}

data_field_descriptions = [row for row in csv.DictReader(open("layouts/DATA_FIELD_DESCRIPTORS_classified.csv","r"))]
sf1_vars_race_binaries  = [row for row in csv.DictReader(open("layouts/sf1_vars_race_binaries.csv","r"))]
layouts                 = json.loads(open("layouts/layouts.json").read())
TABLES  = set([sf1var['table_number'] for sf1var in sf1_vars_race_binaries])
VARS    = set([sf1var['cell_number'] for sf1var in sf1_vars_race_binaries])

def p(block,i,suffix=None):
    """Return the variable for person i on block block"""
    if suffix is None:
        suffix = ""
    else:
        assert suffix in VAR_SUFFIXES
    return f"P{block}_{i}{suffix}"

def pcount(block,i,quals):
    """Return a counter for person i on block with the qualifiers"""
    tquals = []
    for q in quals.keys():
        if q=='start_age':
            tquals.append(f"(>= {p(block,i,'A')} {quals['start_age']})")
        elif q=='end_age':
            tquals.append(f"(<= {p(block,i,'A')} {quals['end_age']})")
        elif q=='two' and quals['two']==True:
            tquals.append("(<= 2 (+ " + " ".join([f"(ite {p(block,i,race)} 1 0) " for race in RACES]) + "))")
        else:
            tquals.append(f"(= {p(block,i,q)} {quals[q]})")
    if tquals == []:
        return "1"              # no qualification, always count
    return "(ite (and " + " ".join(tquals) + ") 1 0)\n"
        
class ConstraintWriter:
    # Writes out the constraints in a requested format.
    FMT_Z3 = 'z3'
    FMT_YICES = 'yices'
    FMT_SUGAR = 'sugar'
    FMT_CVC4 = 'cvc4'
    def __init__(self,filename,fmt):
        if fmt not in [FMT_Z3,FMT_YICES,FMT_SUGAR]:
            raise ValueError(f"Unknown format '{fmt}'")
        self.fmt = fmt
        self.f   = open(filename,"w")
        self.vars = []

    def declare_const(self,name,val):
        if type(val)==int:
            self.f.write({FMT_Z3    : f"(declare-fun {name} () Int {val})\n",
                     FMT_SUGAR : f"#define {name} {val}\n"}[self.fmt])
        elif type(val)==bool:
            self.f.write({FMT_Z3    : f"(declare-fun {name} () Bool {val})\n",
                     FMT_SUGAR : f"#define {name} {val}\n"}[self.fmt])
        else:
            raise ValueError(f"Unsupported type")

    def declare_int(self,name,imin,imax):
        self.vars.append(name)
        self.f.write({FMT_Z3 : f"(define-const {name} Int) (assert (and (>= {name} {imin}) (<= {name} {imax})))\n"}[self.fmt])
        
    def declare_bool(self,name):
        self.vars.append(name)
        self.f.write({FMT_Z3 : f"(define-const {name} Bool)\n"}[self.fmt])

    def assert_sexp(self,sexp):
        self.f.write({FMT_Z3 : f"(assert {sexp})\n"}[self.fmt])

    def comment(self,c):
        self.f.write({FMT_Z3    : f";; {c}\n",
                      FMT_SUGAR : f";; {c}\n"}[self.fmt])


    def dump_vars(self):
        self.f.write({FMT_Z3    : f"(check-sat)\n(get-unsat-core)\n(get-value (" + " ".join(self.vars) + "))\n",
                      FMT_SUGAR : f"\n"}[self.fmt])

    def clos(self):
        self.f.close()
        

class ConstraintBuilder:
    """Creates a set of constraints for a given state,county,tract, and optionally a specific block or set of tables.
    Can output the constraints in a variety of formats.
    """
    def __init__(self,conn,state,county,tract,onlyblock=None,onlytables=[]):
        # Get all of the data fields

        self.state = state
        self.county = county
        self.tract  = tract
        self.block_constraints = 0
        self.tract_constraints = 0
        self.onlyblock         = onlyblock
        self.onlytables = onlytables
        c = conn.cursor()
        c.execute("SELECT logrecno,block,pop from blocks where state=? and county=? and tract=?",(state,county,tract))
        rows = c.fetchall()
        if len(rows)==0:
            raise RuntimeError(f"No database entry for state {state} county {county} tract {tract}")
        for row in rows:
            if row[1] is None or row[2] is None:
                print(f"Missing block ({row[1]}) or population ({row[2]}) for logrecno {row[0]}:")
                raise RuntimeError
        self.blockpops = {row[0]:{'block':row[1],'pop':row[2]} for row in rows}

        c.execute("SELECT logrecno,pop from tracts where state=? and county=? and tract=?",(state,county,tract))
        try:
            (self.tract_logrecno, self.tract_pop) = c.fetchone()
        except TypeError as e:
            raise ValueError(f"Could not find logrecno for state {state} county {county} tract {tract}")

        self.vars = []                       # vars in the solutions
        self.table_constraint_count = defaultdict(int)

    def pop_for_block(self,block):
        for LOGRECNO in self.blockpops:
            if self.blockpops[LOGRECNO]['block']==block:
                return self.blockpops[LOGRECNO]['pop']

    def pop_for_tract(self):
        return sum([self.blockpops[LOGRECNO]['pop'] for LOGRECNO in self.blockpops])

    def pop_for_LOGRECNO(self,LOGRECNO):
        if self.tract_logrecno == LOGRECNO:
            return self.tract_pop
        return self.blockpops[LOGRECNO]['pop']

    def block_for_LOGRECNO(self,LOGRECNO):
        return self.blockpops[LOGRECNO]['block']

    def blocks(self):
        return [self.blockpops[int(LOGRECNO)]['block'] for LOGRECNO in self.blockpops]

    def setup(self,outfile,fmt):
        self.w = ConstraintWriter(outfile,fmt)
        self.w.declare_const("Male",True)
        self.w.declare_const("Female",False)
        self.w.declare_const("Hispanic",True)
        # Create the variables for each person on each block
        for LOGRECNO in self.blockpops:
            block = self.block_for_LOGRECNO(LOGRECNO)
            if self.onlyblock and block!=self.onlyblock:
                continue
            pop   = self.pop_for_LOGRECNO(LOGRECNO)
            self.f.write(f"; block: {block} pop: {pop}\n")
            for i in range(pop):
                _ = p(block,i)  # variable prefix
                for ch in VAR_SUFFIXES:
                    vname = _ + ch
                    if ch=='A':
                        # age is between 0 and 115
                        self.w.declare_int(vname,0,115)
                    else:
                        # the remainder are Booleans
                        self.w.declare_bool(vname)
                    self.vars.append(vname)
                self.f.write("\n")

    def add_sf1file(self,fn):
        layout_name = "SF1_" + os.path.basename(fn)[2:7] + ".xsd"
        try:
            cols = layouts[layout_name]
        except KeyError:
            return              # we don't care about this layout

        # See if any of the cols are in the vars that we use. If not, just return
        used_vars = VARS.intersection(set(cols))
        print(f"{fn} provides {len(used_vars)} vars")
        if not used_vars:
            return

        for row in csv.DictReader(open(fn,'r'),fieldnames=cols):
            assert(row['FILEID']=='SF1ST')
            LOGRECNO = int(row['LOGRECNO'])
            if (LOGRECNO!=self.tract_logrecno) and (int(LOGRECNO) not in self.blockpops):
                # LOGRECNO not in the tract being reconstructed
                continue

            for sf1var in sf1_vars_race_binaries:
                # If this variable is block level and we have a tract-level logrecno, ignore it
                if self.onlytables and sf1var['table_number'] not in self.onlytables:
                    continue
                if sf1var['level']=='block' and LOGRECNO==self.tract_logrecno:
                    continue
                census_variable = sf1var['cell_number']
                try:
                    count = row[census_variable]
                except KeyError:
                    # Variable not in file
                    continue
                else:
                    self.add_constraints(LOGRECNO, census_variable, sf1var, count)

    def get_quals(self,sf1var):
        quals = {}
        for (a,b) in COL_TO_SUFFIX_MAP.items():
            if sf1var[a] in COL_VAL_MAPPING:
                quals[b] = COL_VAL_MAPPING[sf1var[a]]
        if sf1var['start_age']!='missing':
            quals['start_age'] = sf1var['start_age']
        if sf1var['end_age']!='missing':
            quals['end_age'] = sf1var['end_age']
        if sf1var['two']!='missing':
            quals['two'] = True
        return quals

    def add_constraints(self, LOGRECNO, census_variable, sf1var, count):
        pop = self.pop_for_LOGRECNO(LOGRECNO)
        if pop==0:              # if pop=0, there are no population variables
            return
        quals = self.get_quals(sf1var)

        self.table_constraint_count[sf1var['table_number']] += 1
        sexp = []
        sexp.append(f'(= {count} (+ \n')
        if sf1var['level']=='block':
            # block-level constraints
            block = self.block_for_LOGRECNO(LOGRECNO)
            if self.onlyblock and block!=self.onlyblock:
                return
            self.w.comment(f";LOGRECNO {LOGRECNO} {census_variable} = {count}  (block {block} pop={pop})\n")
            self.w.comment(f";{sf1var['title']}\n")
            sexp.append("  "+"  ".join([pcount(block,i,quals) for i in range(pop)]))
            self.block_constraints += 1

        elif sf1var['level']=='tract':
            # tract-level constraints
            if self.onlyblock:
                return
            self.w.comment(f";LOGRECNO {LOGRECNO} {census_variable} = {count}  (tract {self.tract_logrecno} tractpop={self.tract_pop})\n")
            self.w.comment(f";{sf1var['title']}\n")
            for block in self.blocks():
                pop = self.pop_for_block(block)
                if pop>0:
                    sexp.append(f"     ; LOGRECNO {LOGRECNO} {census_variable} = {count}  (tract {self.tract} block {block} pop={pop})\n")
                    sexp.append("  "+"  ".join([pcount(block,i,quals) for i in range(pop)]))
            self.tract_constraints += 1
        else:
            raise RuntimeError("Unknown level in: {}".format(sf1var)) 
        sexp.append("))\n\n")
        self.w.assert_sexp("".join(sexp))

    def done(self):
        self.w.dump_vars()
        self.w.close()
        print("Constraints per table:")
        for (k,v) in self.table_constraint_count.items():
            print(k,v)
        print(f"Tract level constraints: {self.tract_constraints}")
        print(f"Block level constraints: {self.block_constraints}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Ingest the PL94 block-level population counts',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--db", help="Specify database location", default=DBFILE)
    parser.add_argument("--state", default='AK')
    parser.add_argument("--county", default=105, type=int)
    parser.add_argument("--tract", default=200, type=int)
    parser.add_argument("--maxsegments", type=int, default=47, help="Only process this many SF1 files")
    parser.add_argument("--onlysegments", type=str, help="specify the segments you wish, seperated by commas")
    parser.add_argument("--onlytables", help="Only use these tables (for debugging)")
    parser.add_argument("--onlyblock", type=int, help="Only use this block (for debugging)")
    parser.add_argument("--outfile", help="output file")
    args = parser.parse_args()

    logging.getLogger().setLevel(logging.INFO)

    # open database and give me a big cache
    conn = sqlite3.connect(args.db)
    onlytables = args.onlytables.split(",") if args.onlytables else None
    c = ConstraintBuilder(conn,args.state,args.county,args.tract,
                          onlyblock=args.onlyblock,
                          onlytables=onlytables)
    outfile = args.outfile if args.outfile else f"solve_{args.state}{args.county:03}{args.tract:06}.smt"
    c.setup(outfile )
    if args.onlysegments:
        segments = [int(x) for x in args.onlysegments.split(",")]
    else:
        segments = range(1, args.maxsegments)
    for seg in segments:
        fname = f"../data/2010_sf1/ak000{seg:02}2010.sf1"
        logging.info("Adding %s",fname)
        c.add_sf1file(fname)
    c.done()
