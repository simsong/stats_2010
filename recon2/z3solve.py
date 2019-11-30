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

DBFILE="pl94.sqlite3"

CACHE_SIZE = -1024*16           # negative nubmer = multiple of 1024. So this is a 16MB cache.
SQL_SET_CACHE = "PRAGMA cache_size = {};".format(CACHE_SIZE)

VAR_SUFFIXES = 'AHSwbisho'

class SLGSQL:
    def iso_now():
        """Report current time in ISO-8601 format"""
        return datetime.datetime.now().isoformat()[0:19]

    def create_schema(conn,schema):
        """Create the schema if it doesn't exist."""
        c = conn.cursor()
        for line in schema.split(";"):
            c.execute(line)

    def execselect(conn, sql, vals=()):
        """Execute a SQL query and return the first line"""
        c = conn.cursor()
        c.execute(sql, vals)
        return c.fetchone()

def make_database(conn):
    conn.row_factory = sqlite3.Row
    conn.cursor().execute(SQL_SET_CACHE)
    SLGSQL.create_schema(conn,SQL_SCHEMA)

def db_connection(filename=DBFILE):
    return sqlite3.connect(filename)

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
        
def process(conn,state,county,tract):
    # Get all of the data fields
    data_field_descriptions = [row for row in csv.DictReader(open("layouts/DATA_FIELD_DESCRIPTORS_classified.csv","r"))]
    sf1_vars_race_binaries  = [row for row in csv.DictReader(open("layouts/sf1_vars_race_binaries.csv","r"))]
    layouts                 = json.loads(open("layouts/layouts.json").read())

    c = conn.cursor()
    c.execute("SELECT logrecno,block,pop from blocks where state=? and county=? and tract=?",(state,county,tract))
    blockpops = {row[0]:{'block':row[1],'pop':row[2]} for row in c.fetchall()}

    # Get the relevant SF1 records

    vars = []
    with open("solve.z3","w") as f:
        f.write("(define-fun Male () Bool true)\n")
        f.write("(define-fun Female () Bool false)\n")
        block_pop = {}
        for LOGRECNO in blockpops:
            block = blockpops[LOGRECNO]['block']
            pop = blockpops[LOGRECNO]['pop']
            f.write(f"; block: {block} pop: {pop}\n")
            for i in range(pop):
                _ = p(block,i)  # variable prefix
                for ch in VAR_SUFFIXES:
                    if ch=='A':
                        # age is between 0 and 115
                        f.write(f"(declare-const {_}A Int) (assert (and (>= {_}A 0) (<= {_}A 115)))\n")
                    else:
                        # the remainder are Booleans
                        f.write(f"(declare-const {_}{ch} Bool) \n")
                f.write("\n")
                vars.extend([_+ch for ch in "AHSwbisho"])

        # P10: RACE FOR THE POPULATION 18 YEARS AND OVER [71]
        # P11: HISPANIC OR LATINO, AND NOT HISPANIC OR LATINO BY RACE FOR THE POPULATION 18 YEARS AND OVER [73]
        # Because P11 includes all of P10, just process P11
        # Find the file
        fn = "../data/2010_sf1/ak000042010.sf1"
        cols = layouts['SF1_00004.xsd']
        for row in csv.DictReader(open(fn,'r'),fieldnames=cols):
            assert(row['FILEID']=='SF1ST')
            LOGRECNO = row['LOGRECNO']
            if int(LOGRECNO) not in blockpops:
                #print(row['LOGRECNO']," not in ",logrecs)
                continue
            
            block = blockpops[int(LOGRECNO)]['block']
            pop = blockpops[int(LOGRECNO)]['pop']

            for sf1var in sf1_vars_race_binaries:
                census_variable = sf1var['cell_number']
                if census_variable in row:
                    count = row[census_variable]
                    f.write(f";LOGRECNO {LOGRECNO} {census_variable} = {count}  (block {block} pop={pop})\n")
                    if pop==0:
                        continue
                    quals = {}
                    for (a,b) in [('hispanic','H'),
                                  ('sex','S'),
                                  ('white','w'),
                                  ('black','b'),
                                  ('aian','i'),
                                  ('asian','s'),
                                  ('nhopi','h'),
                                  ('sor','o')]:
                        MAPPING = {'Y':'true',
                                   'N':'false',
                                   'male':'Male',
                                   'female':'Female',
                                   'hispanic':'Hispanic'}
                        if sf1var[a] in MAPPING:
                            quals[b] = MAPPING[sf1var[a]]
                    if sf1var['start_age']!='missing':
                        quals['start_age'] = sf1var['start_age']
                    if sf1var['end_age']!='missing':
                        quals['end_age'] = sf1var['end_age']
                    f.write(f"(assert (= {count} (+ \n")
                    f.write("  "+"  ".join([pcount(block,i,quals) for i in range(pop)]))
                    f.write(")))\n\n")

        # PCT12 is the single-digit year track-level statistics by race. Add them.
        #with open("layouts/sf1_vars_race_binaries.csv") as vrb:
        #    for row in csv.DictReader(vrb):
        #        print(row)

        f.write("(check-sat)\n")
        f.write("(get-value (" + " ".join(vars) + "))\n")
        exit(0)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Ingest the PL94 block-level population counts',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--db", help="Specify database location", default=DBFILE)
    parser.add_argument("--state", default='AK')
    parser.add_argument("--county", default=105, type=int)
    parser.add_argument("--tract", default=200, type=int)
    args = parser.parse_args()

    # open database and give me a big cache
    conn = db_connection(args.db)
    process(conn,args.state,args.county,args.tract)
