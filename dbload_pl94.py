#!/usr/bin/env python3
#
"""
dbload_pl94.py: create an SQLite3 database from PL94 data for blocks and tracts. Data loaded includes:
Blocks:   STATE | COUNTY | TRACT | BLOCK | LOGRECNO | POP | HOUSES | OCCUPIED 
Tracts:   STATE | COUNTY | TRACT | LOGRECNO  
Counties: STATE | COUNTY | NAME

PL94 Datasources:
  STATE|COUNTY|TRACT|BLOCK => LOGRECNO  -- Geography file
  POP --- File 012010
  HOUSES|OCCUPIED --- File 022010

SF1 Datasources:

NOTES: 
 * LOGRECNO is not consistent between the PL94 and SF1 files
 * HOUSES and OCCUPIED do not include GROUP QUARTERS

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
import logging

import constants
from constants import *

DBFILE="pl94.sqlite3"

CACHE_SIZE = -1024*16           # negative nubmer = multiple of 1024. So this is a 16MB cache.
SQL_SET_CACHE = "PRAGMA cache_size = {};".format(CACHE_SIZE)

SQL_SCHEMA="""
CREATE TABLE IF NOT EXISTS blocks (geocode VARCHAR(15), state INTEGER, county INTEGER, tract INTEGER, block INTEGER, logrecno INTEGER, pop INTEGER, houses INTEGER, occupied INTEGER);
CREATE UNIQUE INDEX IF NOT EXISTS geocode_idx ON blocks(geocode);
CREATE UNIQUE INDEX IF NOT EXISTS blocks_idx0 ON blocks(state,logrecno);
CREATE UNIQUE INDEX IF NOT EXISTS blocks_idx1 ON blocks(state,county,tract,block);
CREATE INDEX IF NOT EXISTS blocks_idx10 ON blocks(tract);
CREATE INDEX IF NOT EXISTS blocks_idx11 ON blocks(pop);
CREATE INDEX IF NOT EXISTS blocks_idx12 ON blocks(houses);

CREATE TABLE IF NOT EXISTS tracts (state INTEGER, county INTEGER, tract INTEGER, logrecno INTEGER, pop INTEGER, houses INTEGER, occupied INTEGER);
CREATE UNIQUE INDEX IF NOT EXISTS tracts_idx0 ON tracts(state,logrecno);
CREATE UNIQUE INDEX IF NOT EXISTS tracts_idx1 ON tracts(state,county,tract);
CREATE INDEX IF NOT EXISTS tracts_idx10 ON tracts(tract);
CREATE INDEX IF NOT EXISTS tracts_idx11 ON tracts(pop);
CREATE INDEX IF NOT EXISTS tracts_idx12 ON tracts(houses);

CREATE TABLE IF NOT EXISTS counties (stusab VARCHAR(2),state INTEGER, county INTEGER, name VARCHAR(90));
CREATE UNIQUE INDEX IF NOT EXISTS counties_idx0 ON counties(state,county);
CREATE UNIQUE INDEX IF NOT EXISTS counties_idx1 ON counties(stusab,county);

"""

# Define the fileds in the GEO Header. See Figure 2-5 of PL94 & SF1 publications
# These fields are consistent for both publications
# This could be rewritten to use the learned schema...
# THe fields appear exactly as they appear in the specification, which is (FIELD WIDTH, FIELD START)
GEO_FILEID=(6,1)
GEO_STUSAB=(2,7)
GEO_SUMLEV=(3,9)
GEO_LOGRECNO=(7,19)
GEO_STATE=(2,28)
GEO_COUNTY=(3,30)
GEO_PLACE=(5,46)        # Incorporated place or census designated place
GEO_PLACECC=(2,51)
GEO_TRACT=(6,55)            
GEO_BLKGRP=(1,61)
GEO_BLOCK=(4,62)        # first digit of block is blockgroup
GEO_CONCIT=(5,68)       # Consolidated City (FIPS)
GEO_AIANHH=(4,77)
GEO_NAME=(90,227)       # in Latin1 for 2000 and 2010

FIPS_PLACE_CLASS_CODE={
    "C1":"An active incorporated place that does not serve as a county subdivision equivalent",
    "C2":"An active incorporated place that is legally coextensive with a county subdivision but treated as independent of any county subdivision (an independent place)",
    "C5":"An active incorporated place that is independent of any county subdivision and serves as a county subdivision equivalent (an independent place)",
    "C6":"An active incorporated place that is partially independent of any county subdivision and partially dependent within a legal county subdivision (exists in Iowa and Ohio only)",
    "C7":"An incorporated place that is independent of any county (an independent city)",
    "C8":"The balance of a consolidated city excluding the separately incorporated place(s) within that consolidated government",
    "C9":"An inactive or nonfunctioning incorporated place",
    "M2":"A census designated place (CDP) defined within a military or Coast Guard installation",
    "U1":"A census designated place (CDP) with a name officially recognized by the U.S. Board on Geographic Names for a populated place",
    "U2":"A census designated place (CDP) with a name not officially recognized by the U.S. Board on Geographic Names for a populated place"}

FIPS_CONSOLIDATED_CITY={
    "03436":"Athens-Clarke County, Georgia",
    "04200":"Augusta-Richmond County, Georgia",
    "11390":"Butte-Silver Bow, Montana",
    "36000":"Indianapolis, Indiana",
    "47500":"Milford, Connecticut",
    "48003":"Louisville/Jefferson County, Kentucky",
    "52004":"Nashville-Davidson, Tennessee"}

DEBUG_BLOCK=None

class SLGSQL:
    def iso_now():
        """Report current time in ISO-8601 format"""
        return datetime.datetime.now().isoformat()[0:19]

    def create_schema(conn,schema):
        """Create the schema if it doesn't exist."""
        c = conn.cursor()
        for line in schema.split(";"):
            try:
                c.execute(line)
            except sqlite3.OperationalError as e:
                print("line:",line,file=sys.stderr)
                print(e)
                exit(1)

    def execselect(conn, sql, vals=()):
        """Execute a SQL query and return the first line"""
        c = conn.cursor()
        c.execute(sql, vals)
        return c.fetchone()

def make_database(conn):
    conn.row_factory = sqlite3.Row
    conn.cursor().execute(SQL_SET_CACHE)
    SLGSQL.create_schema(conn,SQL_SCHEMA)

def info_geo_line(conn,c,line):
    """Just print information about a geography line"""
    def ex(which):
        return line[which[1]-1:which[1]+which[0]-1]
    print(ex(GEO_STUSAB),ex(GEO_SUMLEV),ex(GEO_LOGRECNO),ex(GEO_STATE),ex(GEO_COUNTY),ex(GEO_PLACE),ex(GEO_PLACECC),ex(GEO_TRACT),ex(GEO_BLKGRP),ex(GEO_BLOCK),ex(GEO_CONCIT),ex(GEO_AIANHH),ex(GEO_NAME).strip())

def decode_geo_line(conn,c,line):
    """Decode the hiearchical geography lines. These must be done before the other files are read
    to get the logrecno."""
    def ex(which):
        return line[which[1]-1:which[1]+which[0]-1]
    def exi(which):
        return int(ex(which))
    assert ex(GEO_FILEID) in ('PLST  ','SF1ST ')
    sumlev = ex(GEO_SUMLEV)

    if (args.sumlev is not None) and (args.sumlev!=sumlev):
        return

    if sumlev in (SUMLEV_SF1_BLOCK,SUMLEV_PL94_BLOCK):
        geocode = "".join([ex(GEO_STATE), ex(GEO_COUNTY), ex(GEO_TRACT), ex(GEO_BLOCK)])
        c.execute("INSERT INTO blocks (geocode,state,county,tract,block,logrecno) values (?,?,?,?,?,?)",
                  (geocode, exi(GEO_STATE), exi(GEO_COUNTY), exi(GEO_TRACT), exi(GEO_BLOCK), exi(GEO_LOGRECNO)))
            
    elif sumlev == SUMLEV_TRACT:
        c.execute("INSERT INTO tracts (state,county,tract,logrecno) values (?,?,?,?)",
                  (exi(GEO_STATE), exi(GEO_COUNTY), exi(GEO_TRACT), exi(GEO_LOGRECNO)))
            
    elif sumlev == SUMLEV_COUNTY:
        c.execute("INSERT INTO counties (stusab,state,county,name) values (?,?,?,?)",
                  (ex(GEO_STUSAB), exi(GEO_STATE), exi(GEO_COUNTY), ex(GEO_NAME)))
        

def decode_012010(conn,c,line):
    """Update the database for a line in segemtn 1 of the 2010 PL94 or SF1 files. 
    Note that the logical record number may not be in the DB, because this line may not be for a block or tract.
    P0010001 = Total Population
    """
    fields = line.split(",")
    (fileid,stusab,chariter,cifsn,logrecno,P0010001) = fields[0:6]
    state = constants.STUSAB_TO_STATE[stusab]
    assert fileid in ('PLST','SF1ST')
    c.execute("UPDATE blocks set pop=? where stusab=? and logrecno=?", (P0010001,stusab,logrecno))
    c.execute("UPDATE tracts set pop=? where stusab=? and logrecno=?", (P0010001,stusab,logrecno))

def decode_pl94_022010(conn,c,line):
    """Update the database for a line. Note that the logical record number may not be in the DB, 
    because this line may not be for a block
    H0010001 = Total Housing Units
    H0010002 = Occupied Housing Units
    H0010003 = Vacant Housing Units
    """
    fields = line.split(",")
    (fileid,stusab,chariter,cifsn,logrecno) = fields[0:5]
    (H0010001,H0010002,H0010003) = fields[-3:]
    assert fileid=='PLST'
    c.execute("UPDATE blocks set houses=?,occupied=? where stusab=? and logrecno=?", (H0010001,H0010002,stusab,logrecno))
    c.execute("UPDATE tracts set houses=?,occupied=? where stusab=? and logrecno=?", (H0010001,H0010002,stusab,logrecno))

def load_file(conn,f,func):
    t0 = time.time()
    c = conn.cursor()
    for (ll,line) in enumerate(f,1):
        try:
            func(conn,c,line)
        except ValueError as e:
            raise ValueError("bad line {}: {}".format(ll,line))
        if ll%10000==0:
            print("{}...".format(ll),end='',file=sys.stderr)
    conn.commit()
    t1 = time.time()
    print("Finished {}; {:,.0f} lines/sec".format(f.name,ll/(t1-t0)))

def process_name(conn,f,name):
    if name[2:] in ['geo2010.pl','geo2010.sf1']:
        if args.geoinfo:
            load_file(conn,f,info_geo_line)
        else:
            load_file(conn,f,decode_geo_line)
        return
    if name[2:] in ['000012010.pl','000012010.sf1']:
        load_file(conn,f,decode_012010)
    elif name[2:]=='000022010.pl':
        load_file(conn,f,decode_pl94_022010)
    else:
        raise RuntimeError("Unknown file type: {}".format(fname))

def process_file(conn,fname):
    (path,name) = os.path.split(fname)
    print(f"process_file {name}")
    if name.lower().endswith(".zip"):
        zf = zipfile.ZipFile(fname)
        for zn in zf.namelist():
            if zn.endswith(".pl"):
                process_name( conn, io.TextIOWrapper(zf.open(zn), encoding='latin1'), zn)
        return
    process_name(conn, open(fname, encoding='latin1'), name)



def db_connection(filename=DBFILE):
    return sqlite3.connect(filename)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Ingest the PL94 block-level population counts',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--db", help="Specify database location", default=DBFILE)
    parser.add_argument("--wipe", help="Erase the DB file first", action='store_true')
    parser.add_argument("files", help="Files to ingest. May be XX000012010.pl XX000022010.pl or a ZIP file."
                        " For best results, use the ZIP file", 
                        nargs="*")
    parser.add_argument("--sumlev", help="Only do this summary level")
    parser.add_argument("--geoinfo", help="Provide geography information only.", action='store_true')
    args = parser.parse_args()

    if args.wipe and os.path.exists(args.db):
        os.unlink(args.db)

    # open database and give me a big cache
    conn = db_connection(args.db)
    make_database(conn)
    for fname in args.files:
        process_file(conn,fname)
