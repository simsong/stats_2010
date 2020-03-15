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

import pl94_dbload

import ctools.dbfile

import constants
from constants import *


###
### Create geotree schema
###
CREATE_GEOTREE_SQL="""
CREATE TABLE %TABLE% (state INTEGER,
                      logrecno INTEGER,
                      p1 VARCHAR(16),
                      p2 VARCHAR(16),
                      p3 VARCHAR(16),
                      p4 VARCHAR(16),
                      p5 VARCHAR(16),
                      p6 VARCHAR(16));
CREATE UNIQUE INDEX %TABLE%_logrecno ON %TABLE%(state,logrecno);
CREATE UNIQUE INDEX %TABLE%_p ON %TABLE%(p1,p2,p3,p4,p5,p6);
"""

def create_v1(db,name):
    cmd = f"""INSERT INTO {name} 
    SELECT state AS state,
    logrecno AS logrecno,
    printf("%02d",state) as p1,
    printf("%03d",county) as p2,
    substr(printf("%05d",tract),1,2) as p3,
    printf("%05d",tract) as p4,
    substr(printf("%04d",block),1,1) as p5,
    printf("%04d",block) as p6
    FROM blocks"""
    db.execute(cmd,debug=True)
    db.commit()
                                         
def geotree_print(db,name):
    cmd = f"""select a.state,a.logrecno,a.p1,a.p2,a.p3,a.p4,a.p5,a.p6,b.geocode,b.pop 
    from {name} a left join blocks b on a.state=b.state and a.logrecno=b.logrecno where a.state<70"""
    c = db.execute(cmd)
    for row in c:
        print(",".join([str(x) for x in row]))


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Ingest the PL94 block-level population counts',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--db", help="Specify database location", default=pl94_dbload.DBFILE)
    parser.add_argument("--create", action='store_true', help='create the schema')
    parser.add_argument("--delete", action='store_true', help='delete the schema')
    parser.add_argument("--print", action='store_true', help='print the blocks')
    parser.add_argument("--v1" , action='store_true', help='create v1 geotree')
    parser.add_argument("name", help="Name of the schema tree")
    args = parser.parse_args()
    db   = ctools.dbfile.DBSqlite3(args.db)
    db.set_cache_bytes(4*1024*1024*1024)

    # open database and give me a big cache
    if args.delete:
        db.execute(f"DROP TABLE IF EXISTS {args.name}",debug=True)
        db.execute(f"DROP INDEX IF EXISTS {args.name}_logrecno",debug=True)
        db.execute(f"DROP INDEX IF EXISTS {args.name}_p",debug=True)
    if args.create:
        db.create_schema(CREATE_GEOTREE_SQL.replace("%TABLE%",args.name),debug=True)
                         
    if args.v1:
        create_v1(db,args.name)

    if args.print:
        geotree_print(db,args.name)
