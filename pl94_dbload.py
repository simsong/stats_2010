#!/usr/bin/env python3
#
"""
pl94_dbload.py: create an SQLite3 database from PL94 data for blocks and tracts. Data loaded includes:
Blocks:   STATE  | COUNTY | TRACT | BLOCK | LOGRECNO | POP | HOUSES | OCCUPIED 
Geo:      (all fields we record from the GeoHeader)

PL94 Datasources:
  STATE|COUNTY|TRACT|BLOCK => LOGRECNO  -- Geography file
  POP --- File 012010
  HOUSES|OCCUPIED --- File 022010

SF1 Datasources:

NOTES: 
 * LOGRECNO is not consistent between the PL94 and SF1 files
 * HOUSES and OCCUPIED do not include GROUP QUARTERS
 * geocode  - basic geocode.      STATE/COUNTY/TRACT/BLOCK
 * geocode3 - combined version.
"""

__version__ = '0.2.0'
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
DEBUG_AIAN = None

CACHE_SIZE = -1024*16           # negative nubmer = multiple of 1024. So this is a 16MB cache.
SQL_SET_CACHE = "PRAGMA cache_size = {};".format(CACHE_SIZE)

SQL_BLOCKS_SCHEMA="""
CREATE TABLE IF NOT EXISTS blocks (geocode VARCHAR(15), geocode3 VARCHAR(26),
                                   state INTEGER, county INTEGER, tract INTEGER, block INTEGER, 
                                   cousub INTEGER, aiannh INTEGER, 
                                   logrecno INTEGER, pop INTEGER, houses INTEGER, occupied INTEGER);
CREATE UNIQUE INDEX IF NOT EXISTS geocode_idx ON blocks(geocode);
CREATE UNIQUE INDEX IF NOT EXISTS geocode3_idx ON blocks(geocode3);
CREATE UNIQUE INDEX IF NOT EXISTS blocks_idx0 ON blocks(state,logrecno);
CREATE UNIQUE INDEX IF NOT EXISTS blocks_idx1 ON blocks(state,county,tract,block);
CREATE INDEX IF NOT EXISTS blocks_tract  ON blocks(tract);
CREATE INDEX IF NOT EXISTS blocks_pop    ON blocks(pop);
CREATE INDEX IF NOT EXISTS blocks_houses ON blocks(houses);
CREATE INDEX IF NOT EXISTS blocks_cousub  ON blocks(cousub);
CREATE INDEX IF NOT EXISTS blocks_aiannh ON blocks(aiannh);
"""

DEBUG_BLOCK=None

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

from geocode import geo_geocode,geo_geocode3,GEO_HEADER,strip_str,extractall_typed

class Loader:
    """Class to load the blocks and geo tables"""
    def __init__(self, args):
        self.args = args
        self.db   = ctools.dbfile.DBSqlite3(self.args.db)
        self.conn = self.db.conn
        self.db.execute(SQL_SET_CACHE)
        self.conn.row_factory = sqlite3.Row
        self.db.create_schema(SQL_BLOCKS_SCHEMA)
        self.add_geo_schema()

    def add_geo_schema(self):
        c = self.conn.cursor()
        f = io.StringIO()
        f.write("CREATE TABLE IF NOT EXISTS geo (")
        for (ct,gh) in enumerate(GEO_HEADER):
            if ct>0:
                f.write(",")
            f.write(gh.lower())
            if GEO_HEADER[gh][2] in (str,strip_str):
                f.write(f" VARCHAR({GEO_HEADER[gh][0]}) ")
            else:
                f.write(f" INTEGER ")
        f.write(");")
        c.execute(f.getvalue())
        for gh in GEO_HEADER:
            c.execute(f"CREATE INDEX IF NOT EXISTS geo_{gh.lower()} ON geo({gh.lower()})")
        
    def decode_geo_line(self, c, line):
        """Decode the hiearchical geography lines. These must be done before the other files are read
        to get the logrecno."""

        gh = extractall_typed(line)
        if gh['LOGRECNO']==self.args.debuglogrecno:
            print("\n",gh)
        assert gh['FILEID'] in ('PLST','SF1ST')

        if gh['TRACT'] and gh['TRACT'] >= 990000 and gh['TRACT'] <=990099:
            # Ignore water tracts
            return

        # Extract the fields
        sumlev = gh['SUMLEV']

        if (self.args.sumlev is not None) and (self.args.sumlev!=sumlev):
            return

        if sumlev in (SUMLEV_SF1_BLOCK, SUMLEV_PL94_BLOCK):
            geocode  = geo_geocode(line)
            geocode3 = geo_geocode3(gh)
            if gh['LOGRECNO']==self.args.debuglogrecno:
                print("geocode:",geocode)
                print("geocode3:",geocode3)
            try:
                c.execute("INSERT INTO blocks "
                          "(geocode, geocode3, state, county,tract,block,cousub,aiannh,logrecno) values (?,?,?,?,?,?,?,?,?,?)",
                          (geocode, geocode3, gh['STATE'], gh['COUNTY'], gh['TRACT'], gh['BLOCK'], gh['COUSUB'],
                           gh['AIANNH'], gh['LOGRECNO']))
            except sqlite3.IntegrityError as e:
                print(e,sys.stderr)
                print(f"geocode: {geocode} geocode3: {geocode3}\n{gh}",file=sys.stderr)
                self.conn.commit()
                c.execute("SELECT * from blocks where geocode3=?",(geocode3,))
                r = c.fetchone()
                print(dict(r))
                exit(1)

        cmd = "INSERT INTO geo (" + ",".join(GEO_HEADER.keys()) + ") values (" + ",".join(["?"]*len(GEO_HEADER)) + ")"
        data = extractall_typed(line)
        args = [data[gh] for gh in GEO_HEADER]
        c.execute(cmd,args)

    def decode_012010(self, c, line):
        """Update the database for a line in segemtn 1 of the 2010 PL94 or SF1 files. 
        Note that the logical record number may not be in the DB, because this line may not be for a block or tract.
        P0010001 = Total Population
        """
        fields = line.split(",")
        (fileid,stusab,chariter,cifsn,logrecno,P0010001) = fields[0:6]
        state = constants.STUSAB_TO_STATE[stusab]
        assert fileid in ('PLST','SF1ST')
        if int(logrecno)==self.args.debuglogrecno:
            print("\n",line)
            print("UPDATE blocks set pop={} WHERE state={} and logrecno={}".format(P0010001,state,logrecno))
        # Update the blocks. If LOGRECNO is not in database, nothing is updated
        # because of referential integrity, LOGRECNO can only be in the database once
        c.execute("UPDATE blocks SET pop=? WHERE state=? AND logrecno=?", (P0010001,state,logrecno))

    def decode_pl94_022010(self, c, line):
        """Update the database for a line. Note that the logical record number may not be in the DB, 
        because this line may not be for a block
        H0010001 = Total Housing Units
        H0010002 = Occupied Housing Units
        H0010003 = Vacant Housing Units
        """
        fields = line.split(",")
        (fileid,stusab,chariter,cifsn,logrecno) = fields[0:5]
        state = constants.STUSAB_TO_STATE[stusab]
        (H0010001,H0010002,H0010003) = fields[-3:]

        if int(logrecno)==self.args.debuglogrecno:
            print("\n",line)

        assert fileid=='PLST'
        c.execute("UPDATE blocks set houses=?,occupied=? where state=? and logrecno=?", (H0010001,H0010002,state,logrecno))

    def load_file(self, f, func):
        t0 = time.time()
        c = self.conn.cursor()
        for (ll,line) in enumerate(f,1):
            try:
                func(c, line)
            except ValueError as e:
                raise ValueError("bad line {}: {}".format(ll,line))
            if ll%10000==0:
                print("{}...".format(ll),end='',file=sys.stderr,flush=True)
        self.conn.commit()
        t1 = time.time()
        print(f"\n",file=sys.stderr)
        print(f"Finished {f.name}; {ll} lines, {ll/(t1-t0):,.0f} lines/sec",file=sys.stderr)

    def process_file_name(self, f, name):
        if name[2:] in ['geo2010.pl','geo2010.sf1']:
            if args.geoinfo:
                self.load_file(f, self.info_geo_line)
            else:
                self.load_file(f, self.decode_geo_line)
            return
        if name[2:] in ['000012010.pl','000012010.sf1']:
            self.load_file(f, self.decode_012010)
        elif name[2:]=='000022010.pl':
            self.load_file(f, self.decode_pl94_022010)
        else:
            raise RuntimeError("Unknown file type: {}".format(fname))

    def process_file_or_zip(self, fname):
        (path,name) = os.path.split(fname)
        print(f"process_file {name}")
        if name.lower().endswith(".zip"):
            zf = zipfile.ZipFile(fname)
            for zn in zf.namelist():
                if zn.endswith(".pl"):
                    self.process_file_name( io.TextIOWrapper(zf.open(zn), encoding='latin1'), zn)
            return
        self.process_file_name(open(fname, encoding='latin1'), name)


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
    parser.add_argument("--aiannh", help="Print everything we know about an AIANNH")
    parser.add_argument("--debuglogrecno", help="logrecno for debugging", type=int)
    args = parser.parse_args()

    if args.wipe and os.path.exists(args.db):
        os.unlink(args.db)

    # open database and give me a big cache
    ld = Loader(args)
    for fname in args.files:
        ld.process_file_or_zip(fname)
