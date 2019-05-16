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

from total_size import total_size
import dbrecon
from dbrecon import dopen
from ctools.timer import Timer

def sf1_zipfilename(state_abbr):
    return dbrecon.dpath_expand(f"$SF1_DIST/{state_abbr}2010.sf1.zip")

def open_segment(state_abbr,segment):
    """ Given a state abbreviation and a segment number, open it"""
    sf1_input_file = f"{state_abbr}{segment:05d}2010.sf1"
    return dopen(sf1_input_file, zipfilename=sf1_zipfilename(state_abbr), encoding='latin1')

def process_state(state_abbr):
    logging.info(f"{state_abbr}: building data frame with all SF1 measurements")
    with Timer() as timer:

        # Read in layouts -- they are json created from xsd from the access database
        # on the website.  Note -- the xsd had to be modified to undo the file
        # mods due to access limitations.  It's read as a ordered dict to preserve
        # the order of the layouts to read the csv.

        state_abbr_upper = state_abbr.upper()
        layouts           = json.load(dopen('$SRC/layouts/layouts.json'), object_pairs_hook=OrderedDict)
        geo_filename     = f"$ROOT/{state_abbr}/geofile_{state_abbr}.csv"
        done_filename    = f"$ROOT/{state_abbr}/completed_{state_abbr}_02"

        # done_filename is created when files are generated
        # If there are no county directories, delete the done file.
        for county in dbrecon.counties_for_state(state_abbr):
            if ( (not dbrecon.dpath_exists(dbrecon.STATE_COUNTY_DIR(state_abbr=state_abbr,county=county) ) )
                 and dbrecon.dpath_exists(done_filename)):
                dbrecon.dpath_unlink(done_filename)

        # If done_file exists, we don't need to run.
        # This would be better done by checking all of the county files.

        if dbrecon.dpath_exists(done_filename):
            print(f"{state_abbr} already exists")
            return

        # Generate the CSV header that the original code used
        # This looks weird, but we are trying to match the original files exactly.
        field_names = ['']
        xy = 'x'
        segment_numbers = []
        for i in range(1,48):
            try:
                heads = layouts[f"SF1_{i:05d}.xsd"]
                [field_names.append(head+"_"+xy) for head in heads[0:4]]
                if i==1:
                    assert heads[4]=='LOGRECNO'
                    field_names.append(heads[4])
                [field_names.append(head) for head in heads[5:]]
                xy = 'y' if xy=='x' else 'x'
                segment_numbers.append(i) # we are using these segments only
            except KeyError as e:
                pass
        JOIN_FIELDS = "STATE,COUNTY,TRACT,BLOCK,BLKGRP,SUMLEV".split(",")
        [field_names.append(field) for field in JOIN_FIELDS]
        field_names.append("geoid")

        # The SF1 directory consists of 47 or 48 segments. The first columns are defined below:
        # Summary levels at https://factfinder.census.gov/help/en/summary_level_code_list.htm
        SUMLEV_COUNTY = '050' # State-County
        SUMLEV_TRACT  = '140' # State-County-Census Tract
        SUMLEV_BLOCK  = '101' # State-County-County Sub∀division-Place/Remainder-Census Tract∀-Block Group-Block
        SF1_LINKAGE_VARIABLES = ['FILEID','STUSAB','CHARITER','CIFSN','LOGRECNO']

        geo_fields = {a[1]:a[0] for a in enumerate(layouts['GEO_HEADER_SF1.xsd'])}
        assert geo_fields['FILEID']==0 and geo_fields['STUSAB']==1

        GEO_SUMLEV_FIELD  = geo_fields['SUMLEV']
        GEO_LOGRECNO_FIELD= geo_fields['LOGRECNO']
        GEO_STATE_FIELD   = geo_fields['STATE']
        GEO_COUNTY_FIELD  = geo_fields['COUNTY']
        GEO_TRACT_FIELD  = geo_fields['TRACT']
        GEO_BLOCK_FIELD  = geo_fields['BLOCK']

        # Track the logical record for the join (we really don't need the whole field)
        logrecs = {}
        from collections import defaultdict
        counts = defaultdict(int)

        with dopen(geo_filename,"r") as f:
            ct = 0
            for line in f:
                geo_data = line.split(",")
                sumlev   = geo_data[GEO_SUMLEV_FIELD]
                if sumlev in [SUMLEV_COUNTY,SUMLEV_TRACT,SUMLEV_BLOCK]:
                    logrecno = geo_data[GEO_LOGRECNO_FIELD]
                    county   = geo_data[GEO_COUNTY_FIELD]
                    geocode  = "".join(geo_data[f] for f in
                                       [GEO_STATE_FIELD,GEO_COUNTY_FIELD,GEO_TRACT_FIELD,GEO_BLOCK_FIELD])
                    logrecs[logrecno] = (sumlev, ct, county,
                                         [geo_data[ geo_fields[ field ] ] for field in JOIN_FIELDS],
                                         geocode )
                    counts[sumlev] += 1
                    ct += 1
                
        print("{} geography file processed. counties:{}  tracts:{}  blocks:{}  mem:{:,}".format(
            state_abbr, counts[SUMLEV_COUNTY], counts[SUMLEV_TRACT], counts[SUMLEV_BLOCK],
            total_size(logrecs)))

        # Open the geofile and find all of the LOGRECNOs for the summary summary levels we care about
        # We are splitting on the entire line, which is a waste. But most of the data we are collecting is at the
        # block level, so most of the time we aren't wasting the work
        open_segment_files = [open_segment(state_abbr,segment) for segment in segment_numbers]

        # Open the block, tract, and county files for every county
        # and write the first line
        output_files = {}
        state_code = dbrecon.state_fips(state_abbr)
        for county_code in dbrecon.counties_for_state(state_abbr):
            countydir = f'$ROOT/{state_abbr}/{state_code}{county_code}'
            dbrecon.dmakedirs(countydir)
            output_files[county_code] = {
                SUMLEV_COUNTY: dopen(f'{countydir}/sf1_county_{state_code}{county_code}.csv','w') ,
                SUMLEV_BLOCK: dopen(f'{countydir}/sf1_block_{state_code}{county_code}.csv','w') ,
                SUMLEV_TRACT: dopen(f'{countydir}/sf1_tract_{state_code}{county_code}.csv','w') }
            for f in output_files[county_code].values():
                f.write(",".join(field_names))
                f.write("\n")

        # Now, for each segment, grab the fields, join, and stuff...

        def line_to_fields(line):
            """Transform a line from the SF1 file to the what the original code did (frequently incorrectly)
            with pandas."""
            TK**

        while True:
            line = ",".join([f.readline().strip() for f in open_segment_files])
            fields = line.split(",")
            if fields[0]=='':   # end of file!
                break
            if fields[0]!='SF1ST' or fields[1]!=state_abbr_upper:
                raise RuntimeError(f"bad fields in line {ct}: {fields}")
            logrecno = fields[4]
            if logrecno in logrecs:
                (sumlev,ct,county,joinfields,geocode) = logrecs[logrecno]
                outline = str(ct)+","+(",".join(fields+joinfields)) + "," + geocode + "\n"
                output_files[county][sumlev].write(outline)




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

