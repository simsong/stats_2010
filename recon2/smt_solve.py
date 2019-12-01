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

DBFILE="pl94.sqlite3"

CACHE_SIZE = -1024*16           # negative nubmer = multiple of 1024. So this is a 16MB cache.
SQL_SET_CACHE = "PRAGMA cache_size = {};".format(CACHE_SIZE)
VAR_SUFFIXES = 'AHSwbisho'

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
        else:
            tquals.append(f"(= {p(block,i,q)} {quals[q]})")
    if tquals == []:
        return "1"              # no qualification, always count
    return "(ite (and " + " ".join(tquals) + ") 1 0)\n"
        
class ConstraintBuilder:
    def __init__(self,conn,state,county,tract,onlytables=[]):
        # Get all of the data fields

        self.state = state
        self.county = county
        self.tract  = tract
        self.block_constraints = 0
        self.tract_constraints = 0
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

    def setup(self,outfile):
        self.f = open(outfile,"w")
        self.f.write("(define-fun Male () Bool true)\n")
        self.f.write("(define-fun Female () Bool false)\n")
        self.f.write("(define-fun Hispanic () Bool true)\n")
        # Create the variables for each person on each block
        for LOGRECNO in self.blockpops:
            block = self.block_for_LOGRECNO(LOGRECNO)
            pop   = self.pop_for_LOGRECNO(LOGRECNO)
            self.f.write(f"; block: {block} pop: {pop}\n")
            for i in range(pop):
                _ = p(block,i)  # variable prefix
                for ch in VAR_SUFFIXES:
                    vname = _ + ch
                    if ch=='A':
                        # age is between 0 and 115
                        self.f.write(f"(declare-const {vname} Int) (assert (and (>= {_}A 0) (<= {_}A 115)))\n")
                    else:
                        # the remainder are Booleans
                        self.f.write(f"(declare-const {vname} Bool) \n")
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
        return quals

    def add_constraints(self, LOGRECNO, census_variable, sf1var, count):
        pop = self.pop_for_LOGRECNO(LOGRECNO)
        if pop==0:              # if pop=0, there are no population variables
            return
        quals = self.get_quals(sf1var)

        self.table_constraint_count[sf1var['table_number']] += 1
        sexp = []
        sexp.append(f'(assert (= {count} (+ \n')
        if sf1var['level']=='block':
            block = self.block_for_LOGRECNO(LOGRECNO)
            self.f.write(f";LOGRECNO {LOGRECNO} {census_variable} = {count}  (block {block} pop={pop})\n")
            sexp.append("  "+"  ".join([pcount(block,i,quals) for i in range(pop)]))
            self.block_constraints += 1
        elif sf1var['level']=='tract':
            self.f.write(f";LOGRECNO {LOGRECNO} {census_variable} = {count}  (tract {self.tract_logrecno} tractpop={self.tract_pop})\n")
            for block in self.blocks():
                pop = self.pop_for_block(block)
                if pop>0:
                    sexp.append(f"     ; LOGRECNO {LOGRECNO} {census_variable} = {count}  (tract {self.tract} block {block} pop={pop})\n")
                    sexp.append("  "+"  ".join([pcount(block,i,quals) for i in range(pop)]))
            self.tract_constraints += 1
        else:
            raise RuntimeError("Unknown level in: {}".format(sf1var)) 
        sexp.append(")))\n\n")
        self.f.write("".join(sexp))


    def done(self):
        self.f.write("(check-sat)\n")
        self.f.write("(get-value (" + " ".join(self.vars) + "))\n")
        self.f.close()
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
    parser.add_argument("--max", type=int, default=47, help="Only process this many SF1 files")
    parser.add_argument("--segments", type=str, help="specify the segments you wish, seperated by commas")
    parser.add_argument("--onlytables", help="Only use these tables")
    args = parser.parse_args()

    logging.getLogger().setLevel(logging.INFO)

    # open database and give me a big cache
    conn = sqlite3.connect(args.db)
    c = ConstraintBuilder(conn,args.state,args.county,args.tract,onlytables=args.onlytables.split(","))
    c.setup( f"solve_{args.state}{args.county:03}{args.tract:06}.smt")
    if args.segments:
        segments = [int(x) for x in args.segments.split(",")]
    else:
        segments = range(1, args.max)
    for seg in segments:
        fname = f"../data/2010_sf1/ak000{seg:02}2010.sf1"
        logging.info("Adding %s",fname)
        c.add_sf1file(fname)
    c.done()
