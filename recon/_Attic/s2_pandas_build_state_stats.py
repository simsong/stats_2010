#!/usr/bin/env python3
#
# 02_build_state_stats.py:
# Reads the SF1 files and outputs statistics for the state, county, and every census tract.
#
# This is a slow process because so many of the datasets use strings instead of numbers.
#
# Currently this takes 160GB for California and nearly 30,000 seconds. Other states take less.
# This is parallelized with multiprocessing, to run each state in its own thread. As long
# as you have enough RAM to run both TX and CA at the same time, you should be okay.

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
import tempfile
import subprocess


from dfxml.python.dfxml.writer import DFXMLWriter
from dbrecon import *
from total_size import total_size
from compare_csv_files import compare_csv_files
import dbrecon

# Constants used in public use files and data frames
STATE = 'STATE'                 # Integer with leading zeros, so VARCHAR(2)
COUNTY = 'COUNTY'               # Integer with leading zeros, so VARCHAR(3)
TRACT = 'TRACT'                 # Integer with leading zeros, so VARCHAR(6)
BLKGRP = 'BLKGRP'               # Integer 0-9.
BLOCK = 'BLOCK'                 # Integer with leading zeros, so VARCHAR(4)
SUMLEV = 'SUMLEV'               # Integer with leading zeros, so VARCHAR(3)
LOGRECNO = 'LOGRECNO'           # Integer with leading zeros, so VARCHAR(7)

# Note that because strings are coded as Python objects, which take 80 bytes in memory
# it is almost always better to use a category for a string, unless every row has a different
# value for that string

GEOID = 'geoid'                 # We create it. STATE+COUNTY+TRACT+BLOCK
CHARITER = 'CHARITER'           # Characteristic Iteration with leading zeros. VARCHAR(3)
CIFSN = 'CIFSN'                 # Characteristic Iteration File Sequence Number with leading zeros. VARCHAR(2)
FILEID = 'FILEID'               # "SF1" 
STUSAB = 'STUSAB'               # State US abbreviation VARCHAR(2)


# Bug in original programmer's code: CHARITER and CIFSN were coded as integers, losing the leading zeros.
# That's okay, because they are not used. But they are read, so we try to read them efficiently
# Note that CHARITER and CIFSN must be coded as np.float32 because they have NA values.

STARTING_DTYPES = {LOGRECNO: object, STATE: object, COUNTY: object,
                   TRACT: object, BLOCK: object, BLKGRP: object, SUMLEV:
                   object, FILEID: object, STUSAB: object, CHARITER:np.float32, CIFSN:np.float32}

NA_VALUES = ['', ' ', '  ', '   ', 'NA', 'NULL']



# Bug in pandas: if we tell it to read something as a category, it may read it as an number
# and then convert. This is a problem for things with leading zeros. Really annoying. So we will read them
# as objects and then convert them to categories, to preserve the leading zeros.

CATEGORY_DTYPES = [STATE, COUNTY, TRACT, BLOCK, BLKGRP, SUMLEV, FILEID, STUSAB ]

# Describe the variables that contain MEDIANS and AVERAGES.
# This is hard-coded; it would be better to read from specifications. 
# TO minimize memory consumption, these are declared as floats, the rest as integers.
#
MEDIANS = set()
AVERAGES = set()
for prefix in '0ABCDEFGHI':
    for tbl in ['001','002','003']:
        MEDIANS.add("P013{}{}".format(prefix,tbl))
        AVERAGES.add("P017{}{}".format(prefix,tbl))
        AVERAGES.add("P037{}{}".format(prefix,tbl))
        AVERAGES.add("H012{}{}".format(prefix,tbl)) # average household tenure
        AVERAGES.add("H012{}0{}".format(prefix,tbl))

def sf1_dtypes(names):
    """Return an array of the DTYPES for the SF1 variables """
    # makes a shallow copy of the category DTYPES, per PEP448,
    # as we will be adding additional types to the array
    dtypes = {**STARTING_DTYPES} 
    for name in names:
        if name in MEDIANS or name in AVERAGES:
            dtypes[name] = np.float32 
        elif name[0]=='P' or name[0]=='H':
            dtypes[name] = np.int32

    for category in CATEGORY_DTYPES:
        dtypes[category] = object # see above
    
    return dtypes

def fix_df(df):
    """set specific fields to be categories that are read as objects"""
    pass

def verify_state_county(trt, state_abbr, county_code):
    logging.info(f"trt={trt} state_abbr={state_abbr} county_code={county_code}")
    state_code = dbrecon.state_fips(state_abbr)
    errors = 0
    for level in ['county', 'tract', 'block']:
        name1 = dpath_expand(f'$ROOT/{state_abbr}/{state_code}{county_code}/sf1_{level}_{state_code}{county_code}.csv')
        name2 = dpath_expand(f'{trt}/{state_abbr}/{state_code}{county_code}/sf1_{level}_{state_code}{county_code}.csv')
        if not os.path.exists(name1):
            logging.error("Cannot find reference file: "+name1)
            continue
        if not os.path.exists(name2):
            raise FileNotFoundError("Cannot find file that was just created: "+name2)
        errors += compare_csv_files(name1,name2)
        logging.info(f"{name1} {name2} errors: {errors}")
    return errors


def write_county_files(rac):
    (ROOT, state_code, county_code, df) = rac
    state_abbr = dbrecon.state_abbr(state_code)
    county_code = county_code.strip()
    if county_code=='':         # phantom from merge with missing data, apparently
        return
    if not dbrecon.valid_county_code(county_code):
        logging.error("Invalid county code: '{}'".format(county_code))
        return 3

    logging.info(f"{state_abbr}: writing {county_code} ")
    countydir = f'{ROOT}/{state_abbr}/{state_code}{county_code}'
    dmakedirs(countydir)

    filename = f'{countydir}/sf1_county_{state_code}{county_code}.csv'
    df[df[SUMLEV].isin(['050'])].to_csv(dopen(filename,'w'))

    filename = f'{countydir}/sf1_block_{state_code}{county_code}.csv'
    df[df[SUMLEV].isin(['101'])].to_csv(dopen(filename,'w'))

    filename = f'{countydir}/sf1_tract_{state_code}{county_code}.csv' 
    df[df[SUMLEV].isin(['140'])].to_csv(dopen(filename,'w'))

    errors = 0
    if args.mem:
        try:
            errors += verify_state_county(ROOT, state_abbr, county_code)
        except RuntimeError as e:
            print(e)
            errors += 1
    return errors


def process_state(state_abbr):
    """Create the sf1_county_XXXXX.csv, sf1_tract_XXXXX.csv, and sf1_block_XXXXX.csv files 
    for each census tract in a given state. Create the done file when the state is done."""

    logging.info(f"{state_abbr}: building county, tract and block files with all SF1 measurements")
    t0 = time.time()
    state_code = dbrecon.state_fips(state_abbr)

    # Verify that all of the files that are needed exist and that we can read them
    if not dpath_exists(f"$SRC/layouts/layouts.json"):
        raise FileNotFoundError("Cannot access layouts.json")
    if not dpath_exists(f"$SRC/layouts/DATA_FIELD_DESCRIPTORS_classified.csv"):
        raise FileNotFoundError("Cannot access $SRC/layouts/DATA_FIELD_DESCRIPTORS_classified.csv")

    sf1_zipfilename  = SF1_ZIP_FILE(state_abbr=state_abbr)
    geo_filename     = f"$ROOT/{state_abbr}/geofile_{state_abbr}.csv"
    done_filename    = STEP02_DONE_FILE(state_abbr=state_abbr)

    # If there are no county directories, delete the done file.
    for county in counties_for_state(state_abbr):
        if not dpath_exists(STATE_COUNTY_DIR(state_abbr=state_abbr,county=county)) and dpath_exists(done_filename):
            dpath_unlink(done_filename)

    if dpath_exists(done_filename) and not args.mem:
        logging.info(f"{state_abbr} already exists")
        return

    # Read in layouts -- they are json created from xsd from the access database
    # on the website.  Note -- the xsd had to be modified to undo the file
    # mods due to access limitations.  It's read as a ordered dict to preserve
    # the order of the layout to read the csv.

    layout=json.load(dopen('$SRC/layouts/layouts.json'), object_pairs_hook=OrderedDict)

    # Get Geo file in -- contains one record per logrecno (the structure used by
    # the public use files.) There is a logrecno for each entity at each geographic level.
    # This will get big, so we turn it to categories early on.

    f = dopen(geo_filename.format(state_abbr=state_abbr))
    geo_df = pd.read_csv(f, dtype=STARTING_DTYPES, na_values=NA_VALUES, low_memory=False)

    # Need to turn to categories *after* geoid is made
    geo_df[GEOID] = (geo_df[STATE].str.strip()
                       +geo_df[COUNTY].str.strip()
                       +geo_df[TRACT].str.strip()
                       +geo_df[BLOCK].str.strip())

    for name in CATEGORY_DTYPES:
        if name in geo_df:
            geo_df[name] = geo_df[name].astype('category')

    if args.mem:
        mem_info('geo_df part2',geo_df,dump=False)


    # Select just summary levels 050, 140 and 101, and just the 8 columns:
    geo_df1 = geo_df[geo_df[SUMLEV].isin(['050','140','101'])]
    geo_df2 = geo_df1[[STATE,COUNTY,TRACT,BLOCK,BLKGRP,SUMLEV,LOGRECNO,GEOID]]

    if args.mem:
        mem_info('geo_df1',geo_df1,dump=False)
        mem_info('geo_df2',geo_df2,dump=False)

    del geo_df,geo_df1


    # Table definitions -- from the access database, with some sort-of-value-added
    # information from me.

    dd          = csv.DictReader(dopen('$SRC/layouts/DATA_FIELD_DESCRIPTORS_classified.csv'))
    cell_names  = {}
    row_headers = {}

    for d in dd:
        if d['Title Row']=='1': row_headers[d['TABLE NUMBER']]=d
        if d['Title Row']=='0': cell_names[d['FIELD CODE']]=[d['FIELD NAME'],d['TABLE NUMBER']]

    # make header record for csv later
    # Unfortunately, the original programmer used a different expansion for blockgroup here, so we maintain it for now.
    # TODO: Change from 'BLOCK_GRP' to BLKGRP

    h=[STATE,COUNTY,TRACT,'BLOCK_GRP',BLOCK,SUMLEV,LOGRECNO]

    # Loop through the layout to read in each table within each state's sf1 file.  
    # Each sf1 file is put into a pandas dataframe and stored in list_
    # Keep only the real files (the mod and PT are artifacts of the access processing
    # They are all then reduced with the common LOGRECNO key 
    # Because the files have the entire state, we process them all at once, but then we
    # save them out county-by-county.
    # This is slow and memory-intensive. It would be faster with Spark

    logging.info(f"{state_abbr}: part1: Building state-wide frame of all tracts and blocks")
    frame = None
    for c,l in enumerate(layout,1):
        if l[:3]=='SF1' and l[9:-4]!='mod' and l[10:-5]!='PT':
            # add all the field names in order to header record.
            names = layout[l]
            extra = l[4:-4]
            fname = f'$ROOT/{state_abbr}/sf1/{state_abbr}{extra}2010.sf1'
            # Specify the dtypes

            dtypes = sf1_dtypes(names)

            try:
                # Setting low_memory=False causes a crash on what follows when reading CA
                df = pd.read_csv(dopen(fname, zipfilename=sf1_zipfilename), names=names,
                                 dtype=dtypes, na_values=NA_VALUES, low_memory=True)
                logging.info(f"{state_abbr}: read_csv read {df.shape}")
            except ValueError as e:
                # This code is left over from the development phase, when we were trying to figure out 
                # which of the dtypes were int and which were float.
                #
                # If one of the dtypes specified is an int, and a float is found, a ValueError is raised.
                # 
                # The code below prints an error message that allows the programmer to determine the error and correct.
                # This was used to develop the MEDIANS and AVERAGES variable lists.
                for i in range(len(names)):
                    logger.error("Bad data type found in layout: names[{}]={}".format(i,names[i]))
                raise e

            # For these columns, if we found them, convert them to a category
            for name in CATEGORY_DTYPES:
                if name in df:
                    df[name] = df[name].astype('category')

            # Here we incrementally merge the frames together. Special logic for the first
            if type(frame) == type(None):
                frame = df
            else:
                frame = pd.merge(frame, df, on=LOGRECNO, how='left')
                logging.info(f"{state_abbr}: done merge")
                del df 

            # Note: the merge will produce float64 types. Due to precision in some large (e.g. CA and TX) counties,
            # we cannot change these to float32 because we need both precision and accuracy.
            # We cannot use int32 because numpy's integer type cannot handle missing data.
            # 
            if args.mem:
                mem_info('frame',frame,dump=False)

        logging.info("{}: processed layout {} of {}. Total memory used: {:,} memory for frame: {:,}".
                     format(state_abbr,c,len(layout),psutil.Process(os.getpid()).memory_info().rss, total_size(frame)))
        gc.collect()    # because pandas has memory leaks

    logging.info(f"{state_abbr}: part2: grouping by county")
    all_counties=pd.merge(frame, geo_df2, on=LOGRECNO).groupby(COUNTY)

    logging.info(f"{state_abbr}: part3: making county dirs and files. county count: {len(all_counties)-1}")

    ROOT = '$ROOT'
    errors = 0
    if args.mem:
        ROOT = tempfile.mkdtemp()

    root_all_counties = [(ROOT,state_code,cd[0],cd[1]) for cd in all_counties]
    logging.info("all counties: {}".format([row[2] for row in root_all_counties]))
    if args.j2==1:
        errors = []
        for rac in root_all_counties:
            errors.append(write_county_files(rac))
    else:
        with multiprocessing.Pool(args.j2) as p:
            errors = p.map(write_county_files, root_all_counties)

    t1 = time.time()
    logging.info(f"{state_abbr}: Done. Processed summary files in {t1-t0:,.0f} seconds. errors: {errors}")
    if args.mem:
        logging.error("Total Verification Errors: {}".format(errors))
        if errors:
            exit(1)
        else:
            logging.info("Memory run completed.")
            exit(0)

    with dopen(done_filename,"w") as f:
        f.write(time.asctime())

if __name__=="__main__":
    from argparse import ArgumentParser,ArgumentDefaultsHelpFormatter
    parser = ArgumentParser( formatter_class = ArgumentDefaultsHelpFormatter,
                             description="Create per-county county, block and tract count files." )
    dbrecon.argparse_add_logging(parser)
    parser.add_argument("--all",action='store_true',help='All states')
    parser.add_argument('--j1', type=int, help='Number of states to run in parallel (states do not share memory)',default=1)
    parser.add_argument('--j2', type=int, help='Number of counties to output in parallel (counties share memory)',default=16)
    parser.add_argument("state_abbrs",nargs="?",help='Specify states to process, separated by commas. Use "all" for all states ')

    args     = parser.parse_args()
    config   = dbrecon.setup_logging_and_get_config(args,prefix="02bld")
    if args.mem:
        print("Memory debugging mode. Setting j=1")
        args.j1 = 1


    states = []
    if args.all or args.state_abbrs=='all':
        states = dbrecon.all_state_abbrs()
    else:
        states = [dbrecon.state_abbr(st).lower() for st in args.state_abbrs.split(',')]

    if not states:
        print("Specify states to download or --all")
        exit(1)

    logging.info("Running with {} threads".format(args.j1))
    if args.j1==1:
        for state in states:
            process_state(state)
    else:
        with multiprocessing.Pool(args.j1) as p:
            p.map(process_state, states)
