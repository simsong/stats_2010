#!/usr/bin/env python3
#
"""
pl94_mysql_dbload.py: Loads data from the PL94 into a MySQL database.
This is designed for spot-checks and information about geographies. 
Data loaded includes:
  STATE | COUNTY | TRACT | BLOCK | LOGRECNO | POP | HOUSES | OCCUPIED

Datasources:
  STATE|COUNTY|TRACT|BLOCK => LOGRECNO  -- Geography file
  POP --- File 12010
  HOUSES|OCCUPIED --- File 22010
"""

__version__ = '0.0.1'
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

from sql import SLGSQL

DBFILE="pl94.sqlite3"

CACHE_SIZE = -1024              # negative nubmer = multiple of 1024. So this is a 1MB cache.
SQL_SET_CACHE = "PRAGMA cache_size = {};".format(CACHE_SIZE)

SQL_SCHEMA="""
CREATE TABLE IF NOT EXISTS blocks (state VARCHAR(2), county INTEGER, tract INTEGER, block INTEGER, logrecno INTEGER, pop INTEGER, houses INTEGER, occupied INTEGER);
CREATE UNIQUE INDEX IF NOT EXISTS blocks_idx0 ON blocks(state,logrecno);
CREATE UNIQUE INDEX IF NOT EXISTS blocks_idx2 ON blocks(state,county,tract,block);
CREATE INDEX IF NOT EXISTS blocks_idx3 ON blocks(tract);
CREATE INDEX IF NOT EXISTS blocks_idx4 ON blocks(pop);
CREATE INDEX IF NOT EXISTS blocks_idx5 ON blocks(houses);
"""

# Define the fileds in the GEO Header. See Figure 2-5 of SF1 publication
#
GEO_FILEID=(1,6)
GEO_STUSAB=(7,2)
GEO_SUMLEV=(9,3)
GEO_LOGRECNO=(19,7)
GEO_COUNTY=(30,3)
GEO_PLACE=(46,5)            
GEO_TRACT=(55,6)            
GEO_BLKGRP=(61,1)
GEO_BLOCK=(62,4)        # first digit of block is blockgroup

DEBUG_BLOCK=None


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

def decode_geo_line(conn,c,line):
    """Decode the hiearchical geography lines. These must be done before the other files are read
    to get the logrecno."""
    def ex(desc):
        return line[desc[0]-1:desc[0]+desc[1]-1]
    def exi(desc):
        return int(ex(desc))
    if exi(GEO_SUMLEV) in [750]:
        try:
            if DEBUG_BLOCK and exi(GEO_BLOCK)==DEBUG_BLOCK:
                print("INSERT INTO blocks (stusab,county,tract,block,logrecno) values ({},{},{},{},{})".format(
                    ex(GEO_STUSAB), exi(GEO_COUNTY), exi(GEO_TRACT), exi(GEO_BLOCK), exi(GEO_LOGRECNO)))
            c.execute("INSERT INTO blocks (stusab,county,tract,block,logrecno) values (?,?,?,?,?)",
                      (ex(GEO_STUSAB), exi(GEO_COUNTY), exi(GEO_TRACT), exi(GEO_BLOCK), exi(GEO_LOGRECNO)))
        except sqlite3.IntegrityError as e:
            conn.commit()          # save where we are
            print("INSERT INTO blocks (stusab,county,tract,block,logrecno) values ({},{},{},{},{})".format(
                ex(GEO_STUSAB), exi(GEO_COUNTY), exi(GEO_TRACT), exi(GEO_BLOCK), exi(GEO_LOGRECNO)))
            raise e
            
def decode_12010(conn,c,line):
    """Update the database for a line. Note that the logical record number may not be in the DB, because this line may not be for a block"""
    fields = line.split(",")
    (fileid,stusab,chariter,cifsn,logrecno,p0010001) = fields[0:6]
    assert fileid=='PLST'
    c.execute("UPDATE blocks set pop=? where stusab=? and logrecno=?",
              (p0010001,stusab,logrecno))

def decode_22010(conn,c,line):
    """Update the database for a line. Note that the logical record number may not be in the DB, because this line may not be for a block"""
    fields = line.split(",")
    (fileid,stusab,chariter,cifsn,logrecno) = fields[0:5]
    (h0010001,h0010002,h0010003) = fields[-3:]
    assert fileid=='PLST'
    c.execute("UPDATE blocks set houses=?,occupied=? where stusab=? and logrecno=?",
              (h0010001,h0010002,stusab,logrecno))

def load_file(conn,f,func):
    t0 = time.time()
    c = conn.cursor()
    for (ll,line) in enumerate(f,1):
        try:
            func(conn,c,line)
        except ValueError as e:
            raise ValueError("bad line {}: {}".format(ll,line))
        if ll%10000==0:
            print("{}...".format(ll),end='')
            sys.stdout.flush()
    conn.commit()
    t1 = time.time()
    print("Finished {}; {:,.0f} lines/sec".format(f.name,ll/(t1-t0)))

def process_name(conn,f,name):
    if name[2:]=='geo2010.pl':
        load_file(conn,f,decode_geo_line)
    elif name[2:]=='000012010.pl':
        load_file(conn,f,decode_12010)
    elif name[2:]=='000022010.pl':
        load_file(conn,f,decode_22010)
    else:
        raise RuntimeError("Unknown file type: {}".format(fname))

def process_file(conn,fname):
    (path,name) = os.path.split(fname)
    print(f"process_file{name}")
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
    parser.add_argument("files", help="Files to ingest. May be XX000012010.pl XX000022010.pl or a ZIP file. For best results, use the ZIP file", 
                        nargs="*")
    args = parser.parse_args()

    # open database and give me a big cache
    conn = db_connection(args.db)
    make_database(conn)
    for fname in args.files:
        process_file(conn,fname)
