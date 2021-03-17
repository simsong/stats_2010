#!/usr/bin/env python3
#
"""
Make the microdata on a county-by-county basis.
"""

import csv
import dbrecon
import gc
import glob
import logging
import os
import os.path
import subprocess
import sys
import time
import atexit
import multiprocessing

import dbrecon
from dbrecon import DB
from dbrecon import dopen,dmakedirs,dsystem,dpath_exists,GB

REIDENT = os.getenv('REIDENT')


def make_csv_file( pair ):
    # Make sure we have a solution file for every tract
    (state_abbr, county, overwrite) = pair
    county_csv_filename = dbrecon.COUNTY_CSV_FILENAME(state_abbr=state_abbr, county=county)
    county_csv_filename_tmp = county_csv_filename+".tmp"

    if dbrecon.dpath_exists(county_csv_filename):
        if overwrite:
            logging.info(f"{county_csv_filename} exists --- overwriting")
        else:
            logging.info(f"{county_csv_filename} exists --- will not overwrite")
            return
    if dbrecon.dpath_exists(county_csv_filename_tmp):
        logging.warning(f"{county_csv_filename_tmp} exists --- another process is running?")
        return

    state_code = dbrecon.state_fips(state_abbr)
    tracts     = dbrecon.tracts_for_state_county(state_abbr=state_abbr, county=county)
    missing = 0
    for tract in tracts:
        solfile = dbrecon.SOLFILENAMEGZ(state_abbr=state_abbr, county=county, tract=tract)
        if not dpath_exists(solfile):
            logging.error("No solution file: {}".format(solfile))
            missing += 1
    if missing>0:
        logging.error(f"Will not make {state_abbr} {state_code}{county} CSV file; missing tracts: {missing}")
        return

    with dopen(county_csv_filename_tmp,"w") as outfile:
        w = csv.writer(outfile)
        w.writerow(['geoid_tract','geoid_block','sex','age','white','black','aian','asian','nhopi','sor','hisp'])
        county_total = 0
        for tract in tracts:
            tract_total = 0
            logging.info(f"Starting tract {state_code}{county}{tract}")
            dbrecon.db_start('csv', state_abbr, county, tract)
            with dopen(dbrecon.SOLFILENAMEGZ(state_abbr=state_abbr, county=county, tract=tract),"r") as infile:
                for line in infile:
                    if line[0:2]=='C_': # oldstyle variable
                        (var,count) = line.strip().split()
                        count = round(float(count)) # some of the solutions are not precisely equal to 0 or 1
                        # don't count the zeros
                        if count==0:
                            continue
                        elif count==1:
                            c = var.split("_")
                            tract_ = c[1][5:11]
                            if tract != tract_:
                                raise RuntimeError(f"{infile.name}: Expecting tract {tract} read {tract_}")
                            geoid_tract = state_code + county + tract
                            w.writerow([geoid_tract, c[1], c[5], c[6], c[7], c[8], c[9], c[10], c[11], c[12], c[13]])
                            tract_total += 1
                            county_total += 1
                        else:
                            raise ValueError(f"invalid count={count} in line: {line}")
                logging.info(f"Ending {state_code}{county}{tract} tract pop: {tract_total}")
            # done with this tract
            dbrecon.db_done('csv', state_abbr, county, tract)
        # done with all tracts
    dbrecon.drename(county_csv_filename_tmp, county_csv_filename)
    logging.info(f"Ending {state_code}{county} county pop: {county_total}")
    print(f"{__file__} {state_code}{county} county pop: {county_total}")

if __name__=="__main__":
    from argparse import ArgumentParser,ArgumentDefaultsHelpFormatter
    parser = ArgumentParser( formatter_class = ArgumentDefaultsHelpFormatter,
                             description="Create the microdata file from all of the solutions for each tract in a given county.." )
    dbrecon.argparse_add_logging(parser)
    parser.add_argument("state_abbr", help="2-character state abbreviation; can be 'all' for all states.")
    parser.add_argument("county", help="3-digit county code; can be 'all' for all counties; must be 'all' if all states are specified")
    parser.add_argument("--j1", help="Specify number of counties to create CSV files at once", default=64, type=int)
    parser.add_argument("--overwrite", help="Overwrite the output files even if they exist", action='store_true')

    args       = parser.parse_args()
    config     = dbrecon.setup_logging_and_get_config(args=args,prefix="05micro")

    # Get a list of the state/county pairs to make
    pairs = []
    if args.state_abbr=='all':
        if args.county!='all':
            raise ValueError("'all' states requires 'all' counties")
        state_abbrs = dbrecon.all_state_abbrs()
    else:
        state_abbrs = [dbrecon.state_abbr(args.state_abbr).lower()]

    for state_abbr in state_abbrs:
        if args.county=='all':
            for county in dbrecon.counties_for_state(state_abbr):
                pairs.append( (state_abbr, county, args.overwrite) )
        else:
            pairs.append( (state_abbr, args.county, args.overwrite) )

    print(f"{__file__}: requested {len(pairs)} state/county pairs")
    with multiprocessing.Pool(args.j1) as p:
        p.map(make_csv_file, pairs)
