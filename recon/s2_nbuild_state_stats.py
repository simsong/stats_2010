#!/usr/bin/env python3
#
# 02_build_state_stats.py:
# Reads the SF1 files, filter on geolevels 050, 140 and 101,  join the segment files into a single line,
# and output statistics. 
#
# This is a complete rewrite of 02_build_state_stats.py to process the files syntactically instead of semantically.
#

import json
import csv
import sys
import os
import pandas as pd
import numpy as np
import psutil
from collections import OrderedDict
from functools import reduce
import gc
import time
import logging
import multiprocessing

sys.path.append( os.path.join(os.path.dirname(__file__),".."))

import dbrecon
from ctools.timer import Timer

def open_segment(state_abbr,segment):
    """ Given a state abbreviation and a segment number, open it"""


def process_state(state_abbr):
    logging.info(f"{state_abbr}: building data frame with all SF1 measurements")
    with Timer() as timer:

        # Read in layouts -- they are json created from xsd from the access database
        # on the website.  Note -- the xsd had to be modified to undo the file
        # mods due to access limitations.  It's read as a ordered dict to preserve
        # the order of the layout to read the csv.

        layout           = json.load(dbrecon.dopen('$SRC/layouts/layouts.json'), object_pairs_hook=OrderedDict)
        sf1_zipfilename  = dbrecon.dpath_expand("$SF1_DIST/{state_abbr}2010.sf1.zip").format(state_abbr=state_abbr)
        geo_filename     = f"$ROOT/{state_abbr}/geofile_{state_abbr}.csv"
        done_filename    = f"$ROOT/{state_abbr}/completed_{state_abbr}_02"

        # done_filename is created when files are generated
        # If there are no county directories, delete the done file.
        for county in dbrecon.counties_for_state(state_abbr):
            if ( (not dbrecon.dpath_exists(dbrecon.STATE_COUNTY_DIR(state_abbr=state_abbr,county=county) ) )
                 and dbrecon.dpath_exists(done_filename)):
                dbrecon.dpath_unlink(done_filename)

        # If done_file exists, we don't need to run. This would be better done by checking all of the county files.
        if dbrecon.dpath_exists(done_filename):
            print(f"{state_abbr} already exists")
            return

        # The SF1 directory consists of 47 or 48 segments. The first columns are defined below:
        # Summary levels at https://factfinder.census.gov/help/en/summary_level_code_list.htm
        SUMLEV_COUNTY = '050' # State-County
        SUMLEV_TRACT  = '140' # State-County-Census Tract
        SUMLEV_BLOCK  = '101' # State-County-County Sub∀division-Place/Remainder-Census Tract∀-Block Group-Block
        SF1_SUMMARY_LEVELS    = set([SUMLEV_COUNTY,SUMLEV_TRACT,SUMLEV_BLOCK])
        SF1_LINKAGE_VARIABLES = ['FILEID','STUSAB','CHARITER','CIFSN','LOGRECNO']

        # Open the geofile and find all of the LOGRECNOs for the summary summary levels we care about
        with dbrecon.dopen(geo_filename,"r") as f:
            for line in f:
                print(line)



if __name__=="__main__":
    from argparse import ArgumentParser,ArgumentDefaultsHelpFormatter
    parser = ArgumentParser( formatter_class = ArgumentDefaultsHelpFormatter,
                             description="Create per-county county, block and tract count files from the state-level SF1 files." )
    dbrecon.argparse_add_logging(parser)
    parser.add_argument("--config", help="config file")
    parser.add_argument("state_abbrs",nargs="*",help='Specify states to process')
    parser.add_argument("--all",action='store_true',help='All states')
    parser.add_argument("--threads", '--j1', type=int, help='Number of states to run at once (defaults to thread count in config file).')

    args     = parser.parse_args()
    config   = dbrecon.get_config(filename=args.config)
    dbrecon.setup_logging(config=config,loglevel=args.loglevel,prefix="02red")
    logfname = logging.getLogger().handlers[0].baseFilename

    if not dbrecon.dpath_exists(f"$SRC/layouts/layouts.json"):
        raise FileNotFoundError("Cannot find $SRC/layouts/layouts.json")
    
    if not dbrecon.dpath_exists(f"$SRC/layouts/DATA_FIELD_DESCRIPTORS_classified.csv"):
        raise FileNotFoundError("$SRC/layouts/DATA_FIELD_DESCRIPTORS_classified.csv")


    from dfxml.python.dfxml.writer import DFXMLWriter
    dfxml    = DFXMLWriter(filename=logfname.replace(".log",".dfxml"), prettyprint=True)

    states = []
    if args.all:
        states = dbrecon.all_state_abbrs()
    else:
        states = [dbrecon.state_abbr(st).lower() for st in args.state_abbrs]


    if not states:
        print("Specify states to process or --all")
        exit(1)

    if not args.threads:
        args.threads=config['run'].getint('threads',1)

    logging.info("Running with {} threads".format(args.threads))
    if args.threads==1:
        [process_state(state) for state in states]
    else:
        with multiprocessing.Pool(args.threads) as p:
            p.map(process_state, states)

