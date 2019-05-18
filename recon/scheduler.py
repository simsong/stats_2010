#!/usr/bin/env python3
#
"""
scheduler.py:

Synthesize the LP files and run Gurobi on a tract-by-tract basis. 
"""

from dbrecon import dopen,dmakedirs,dsystem
import dbrecon
from dfxml.python.dfxml.writer import DFXMLWriter
from math import floor
import csv
import time
import itertools
import sys
import os
import dbrecon
import gc
import logging
import os.path
import pandas as pd
import numpy as np
import psutil
import xml.etree.ElementTree as ET

from collections import defaultdict

sys.path.append( os.path.join(os.path.dirname(__file__),".."))

import ctools.dbfile as dbfile

import glob, time, os, sys
import csv

DBFILE=os.path.join( os.path.dirname(__file__), "dbfile.sqlite3" )

SCHEMA="""
CREATE TABLE IF NOT EXISTS tracts (
    rowid INTEGER PRIMARY KEY,
    state varchar(2) NOT NULL,
    county varchar(3) NOT NULL,
    tract varchar(6) NOT NULL,
    has_csv varchar(1) default 'N' NOT NULL,
    has_lp varchar(1) default 'N' NOT NULL,
    has_sol varchar(1) default 'N NOT NULL'
);

CREATE UNIQUE INDEX IF NOT EXISTS t_geoid ON tracts(state,county,tract);
CREATE INDEX IF NOT EXISTS t_csv ON tracts(has_csv);
CREATE INDEX IF NOT EXISTS t_lp ON tracts(has_lp);
CREATE INDEX IF NOT EXISTS t_sol ON tracts(has_sol);

"""

                
class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
	    self.memo[args] = self.fn(*args)
        return self.memo[args]


@Memoize
def county_csv_exists(*,state_abbr,county):
    return os.path.exists(dbrecon.COUNTY_CSV_FILENAME(state_abbr=state_abbr, county=county))

def process_dfxml(dfxml):
    root = ET.parse(dfxml)
    start_time = root.find(".//start_time").text[0:19].replace("T"," ")
    command_line = " ".join(root.find("//command_line").text.split()[1:])
    maxrss = 0
    for e in root.findall("//rusage/maxrss"):
        maxrss += int(e.text)
    print(start_time,command_line,maxrss)

def init_sct(c,state_abbr,county,tract):
    has_csv = county_csv_exists(state_abbr,county)
    has_lp  = os.path.exists( dbrecon.tracts_with_files(state_abbr, county, 'lp') )
    has_sol = os.path.exists( dbrecon.tracts_with_files(state_abbr, county, 'sol') )
    c.execute("INSERT INTO TRACTS (state,county,tract,has_csv,has_lp,has_sol) values ",
              (state_abbr,county,tract,has_csv,has_lp,has_sol))

def init():
    try:
        os.unlink(DBFILE)
    except FileNotFoundError:
        pass
    with dbfile.DBSQL(fname=DBFILE) as db:
        db.create_schema(SCHEMA)

        c = db.cursor()
        for state_abbr in dbrecon.all_state_abbrs():
            for county in dbrecon.counties_for_state(state_abbr()):
                for tract in dbrecon.tracts_for_state_county(state_abbr,county):
                    init_sct(c,state_abbr,county,tract)
        db.commit()

if __name__=="__main__":
    from argparse import ArgumentParser,ArgumentDefaultsHelpFormatter
    parser = ArgumentParser( formatter_class = ArgumentDefaultsHelpFormatter,
                             description="Maintains a database of reconstruction and schedule next work if the CPU load and memory use is not too high." )
    dbrecon.argparse_add_logging(parser)
    parser.add_argument("--init",   help="Clear database and learn the current configuration", action='store_true')
    parser.add_argument("--dbfile", help="database file", default=DBFILE)
    parser.add_argument("--config", help="config file")
    
    args   = parser.parse_args()
    config = dbrecon.get_config(filename=args.config)

    if args.init:
        init()
