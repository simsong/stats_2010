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
import ctools.dbfile
import pl94_geofile

import constants
from constants import *

DBFILE="pl94.sqlite3"
DEBUG_AIAN = None

CACHE_SIZE = -1024*16           # negative nubmer = multiple of 1024. So this is a 16MB cache.
SQL_SET_CACHE = "PRAGMA cache_size = {};".format(CACHE_SIZE)

SQL_BLOCKS_SCHEMA="""
CREATE TABLE IF NOT EXISTS blocks (state INTEGER, county INTEGER, tract INTEGER, block INTEGER, 
                                   cousub INTEGER, aianhh INTEGER, sldu INTEGER, place INTEGER,
                                   logrecno INTEGER, pop INTEGER, houses INTEGER, occupied INTEGER);
CREATE UNIQUE INDEX IF NOT EXISTS blocks_idx0 ON blocks(state,logrecno);
CREATE UNIQUE INDEX IF NOT EXISTS blocks_idx1 ON blocks(state,county,tract,block);
CREATE INDEX IF NOT EXISTS blocks_tract  ON blocks(tract);
CREATE INDEX IF NOT EXISTS blocks_pop    ON blocks(pop);
CREATE INDEX IF NOT EXISTS blocks_houses ON blocks(houses);
CREATE INDEX IF NOT EXISTS blocks_cousub  ON blocks(cousub);
CREATE INDEX IF NOT EXISTS blocks_aianhh ON blocks(aianhh);
"""

DEBUG_BLOCK=None
INSERT_GROUP_COUNT=10

from geocode import GEO_HEADER,strip_str,extractall_typed

class Loader:
    """Class to load the blocks and geo tables"""
    def __init__(self, args):
        self.args = args
        self.db   = ctools.dbfile.DBSqlite3(self.args.db)
        self.conn = self.db.conn
        self.conn.row_factory = sqlite3.Row
        self.c    = self.db.conn.cursor()
        self.db.execute(SQL_SET_CACHE)
        if args.replace == False:
            self.db.create_schema(SQL_BLOCKS_SCHEMA)
            self.add_geo_schema_new()
        self.insert = None
        self.value_template = None
        self.value_count = 0
        self.values   = []

    def insert_add(self,values):
        self.value_count += 1
        self.values.extend(values)

    def insert_execute(self):
        if self.value_count > 0:
            cmd = self.insert + " VALUES " + ",".join([self.value_template] * self.value_count)
            self.c.execute( cmd, self.values )
            self.value_count = 0
            self.values = []

    def add_geo_schema_legacy(self):
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
        self.c.execute(f.getvalue())
        for gh in GEO_HEADER:
            self.c.execute(f"CREATE INDEX IF NOT EXISTS geo_{gh.lower()} ON geo({gh.lower()})")
        
    def add_geo_schema_new(self):
        self.c.execute( open("pl94_geofile.sql","r").read())
        # Add indexes for fields we care about
        for gh in GEO_HEADER:
            self.c.execute(f"CREATE INDEX IF NOT EXISTS geo_{gh.lower()} ON geo({gh.lower()})")
        
    def decode_geo_line_new(self, line):
        """Use the compiled geocode decoder to create a dictionary, then insert it into the database"""
        from geocode import nint
        gh = pl94_geofile.geo()
        gh.parse_column_specified(line)

        # Linkage variables
        if not gh.validate():
            raise RuntimeError( gh.validate_reason())

        if "990000" <= gh.TRACT <= "990099":
            # Ignore water tracts
            return

        values = [getattr(gh,slot) for slot in gh.__slots__]
        self.insert_add(values)
        if self.value_count > INSERT_GROUP_COUNT:
            self.insert_execute()

    def decode_012010(self, line):
        """Update the database for a line in segmetn 1 of the 2010 PL94 or SF1 files. 
        Note that the logical record number may not be in the DB, because this line may not be for a block or tract.
        P0010001 = Total Population
        """
        fields = line.split(",")
        (fileid,stusab,chariter,cifsn,logrecno,P0010001) = fields[0:6]
        state = constants.STUSAB_TO_STATE[stusab]
        assert fileid in ('PLST','SF1ST')
        # Update the blocks. If LOGRECNO is not in database, nothing is updated
        # because of referential integrity, LOGRECNO can only be in the database once
        self.c.execute("UPDATE blocks SET pop=? WHERE state=? AND logrecno=?", (P0010001,state,logrecno))

    def decode_pl94_022010(self, line):
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

        assert fileid=='PLST'
        self.c.execute("UPDATE blocks set houses=?,occupied=? where state=? and logrecno=?",
                  (H0010001,H0010002,state,logrecno))

    def load_file(self, f, func):
        t0 = time.time()
        self.c = self.conn.cursor()
        for (ll,line) in enumerate(f,1):
            try:
                func(line)
            except ValueError as e:
                raise ValueError("bad line {}: {}".format(ll,line))
            if ll%10000==0:
                print("{}...".format(ll),end='',file=sys.stderr,flush=True)
        self.insert_execute()   # finish the insert
        self.conn.commit()
        t1 = time.time()
        print(f"\n",file=sys.stderr)
        print(f"Finished {f.name}; {ll} lines, {ll/(t1-t0):,.0f} lines/sec",file=sys.stderr)

    def process_file_name(self, f, name):
        state = constants.STUSAB_TO_STATE[name[0:2].upper()]
        if name[2:] in ['geo2010.pl','geo2010.sf1']:
            # load the geo table
            if args.replace:
                self.conn.execute("DELETE FROM geo where STATE=?",(state,))

            gh = pl94_geofile.geo()
            self.insert = "INSERT INTO geo (" + ",".join(gh.__slots__) + ")"
            self.value_template = "(" + ",".join(["?"]*len(gh.__slots__)) + ")"


            self.load_file(f, self.decode_geo_line_new)
            # copy to the blocks table (really unnecessary; we should just copy over the logrecno, but this makes things easier)
            self.conn.execute("""
            INSERT INTO blocks (state, county, tract, block, cousub, aianhh, sldu, place, logrecno)
            SELECT cast(state as integer), 
                   cast(county as integer), 
                   cast(tract as integer), 
                   cast(block as integer), 
                   cast(cousub as integer), 
                   cast(aianhh as integer), 
                   cast(sldu as integer), 
                   cast(place as integer), 
                   cast(logrecno  as integer)
            FROM geo WHERE cast(state as integer)=? AND cast(sumlev as integer) IN (101,750)""",(state,)) 
            return
        if name[2:] in ['000012010.pl','000012010.sf1']:
            if args.replace:
                self.conn.execute("UPDATE blocks set pop=0 where STATE=?",(state,))
            self.load_file(f, self.decode_012010)
        elif name[2:]=='000022010.pl':
            if args.replace:
                self.conn.execute("UPDATE blocks set houses=0, occupied=0 where STATE=?",(state,))
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
    parser.add_argument("--replace", help='replace data for the state', action='store_true')
    parser.add_argument("--wipe", help="Erase the DB file first", action='store_true')
    parser.add_argument("files", help="Files to ingest. May be XX000012010.pl XX000022010.pl or a ZIP file."
                        " For best results, use the ZIP file", 
                        nargs="*")
    parser.add_argument("--sumlev", help="Only do this summary level")
    parser.add_argument("--aianhh", help="Print everything we know about an AIANHH")
    parser.add_argument("--debuglogrecno", help="logrecno for debugging", type=int)
    args = parser.parse_args()

    if args.wipe and os.path.exists(args.db):
        os.unlink(args.db)

    # open database and give me a big cache
    ld = Loader(args)
    for fname in args.files:
        ld.process_file_or_zip(fname)
