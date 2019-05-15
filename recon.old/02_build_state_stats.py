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

from dfxml.python.dfxml.writer import DFXMLWriter
from dbrecon import *
import dbrecon

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

#
# Read in an ordered dict -- keeps all the elements in order for use later
#
def orderedDictReader(csv_in, **kwargs):
    with open(csv_in) as csvfile:
        if 'keys' in kwargs:
            keys=kwargs['keys']
        else :
            reader = csv.DictReader(csvfile)
            keys = reader.fieldnames
        r = csv.reader(csvfile)
        return [OrderedDict(list(zip(keys, row))) for row in r]

def process_state(state_abbr):
    logging.info(f"{state_abbr}: building data frame with all SF1 measurements")
    t0 = time.time()
    state_code = dbrecon.state_fips(state_abbr)

    # Verify that all of the files that are needed exist and that we can read them
    dopen(f"$SRC/layouts/layouts.json","r").close()
    dopen(f"$SRC/layouts/DATA_FIELD_DESCRIPTORS_classified.csv").close()

    sf1_zipfilename  = dbrecon.dpath_expand("$SF1_DIST/{state_abbr}2010.sf1.zip").format(state_abbr=state_abbr)
    geo_filename     = f"$ROOT/{state_abbr}/geofile_{state_abbr}.csv"
    done_filename    = f"$ROOT/{state_abbr}/completed_{state_abbr}_02"

    # If there are no county directories, delete the done file.
    for county in counties_for_state(state_abbr):
        if not dpath_exists(STATE_COUNTY_DIR(state_abbr=state_abbr,county=county)) and dpath_exists(done_filename):
            dpath_unlink(done_filename)

    if dpath_exists(done_filename):
        print(f"{state_abbr} already exists")
        return

    # Read in layouts -- they are json created from xsd from the access database
    # on the website.  Note -- the xsd had to be modified to undo the file
    # mods due to access limitations.  It's read as a ordered dict to preserve
    # the order of the layout to read the csv.

    layout=json.load(dopen('$SRC/layouts/layouts.json'), object_pairs_hook=OrderedDict)


    # The eventual sf1 dictionary -- everything is put in here in a json-like format
    # so we can run national stuff once and dump to json with metadata (column descriptions,
    # universe labels, etc)

    sf1={}

    # Get Geo file in -- contains one record per logrecno (the structure used by
    # the public use files

    f = dopen(geo_filename.format(state_abbr=state_abbr))
    geo_df=pd.read_csv(f,
                       dtype={'STATE': object, 'COUNTY': object, 'TRACT': object,
                              'BLOCK': object, 'BLKGRP': object,
                              'SUMLEV': object, 'LOGRECNO': object},
                       low_memory=False)

    geo_df['geoid'] = (geo_df['STATE'].str.strip()
                       +geo_df['COUNTY'].str.strip()
                       +geo_df['TRACT'].str.strip()
                       +geo_df['BLOCK'].str.strip())

    geo_df['geoid'].astype('str')

    geo_df1 = geo_df[geo_df['SUMLEV'].isin(['050','140','101'])]
    geo_df2 = geo_df1[['STATE','COUNTY','TRACT','BLOCK','BLKGRP','SUMLEV','LOGRECNO','geoid']]

    # Table definitions -- from the access database, with some sort-of-value-added
    # information from me.

    dd          = csv.DictReader(dopen('$SRC/layouts/DATA_FIELD_DESCRIPTORS_classified.csv'))
    cell_names  = {}
    row_headers = {}

    for d in dd:
        if d['Title Row']=='1': row_headers[d['TABLE NUMBER']]=d
        if d['Title Row']=='0': cell_names[d['FIELD CODE']]=[d['FIELD NAME'],d['TABLE NUMBER']]

    # make header record for csv later
    h=['STATE','COUNTY','TRACT','BLOCK_GRP','BLOCK','SUMLEV','LOGRECNO']

    # Loop through the layout to read in each table within each state's sf1 file.  
    # Each sf1 file is put into a pandas dataframe and stored in list_
    # Keep only the real files (the mod and PT are artifacts of the access processing
    # They are all then reduced with the common LOGRECNO key 
    # Because the files have the entire state, we process them all at once, but then we
    # save them out county-by-county.
    # This is slow and memory-intensive. It would be faster with Spark
    frame = None
    for c,l in enumerate(layout,1):

        mem = psutil.Process(os.getpid()).memory_info().rss
        logging.info(f"{state_abbr}: processing layout {c} of {len(layout)}. Total memory used: {mem:,}")

        if l[:3]=='SF1' and l[9:-4]!='mod' and l[10:-5]!='PT':

            # add all the field names in order to header record.
            names = layout[l]
            extra = l[4:-4]
            fname = f'$ROOT/{state_abbr}/sf1/{state_abbr}{extra}2010.sf1'
            # Specify the dtypes
            dtypes = {'LOGRECNO': object}
            for name in names:
                if name in MEDIANS or name in AVERAGES:
                    dtypes[name] = np.float64 # avoids roundoff error
                elif name[0]=='P' or name[0]=='H':
                    dtypes[name] = np.int32

            try:
                logging.info(f"{state_abbr}: read_csv")
                # Setting low_memory=False causes a crash on what follows when reading CA
                df = pd.read_csv(dopen(fname, zipfilename=sf1_zipfilename), names=names, dtype=dtypes, low_memory=True)
                logging.info(f"{state_abbr}: read_csv one")
            except ValueError as e:
                # If one of the dtypes specifies an int, and a float is found, a ValueError is raised.
                # The column number is provided. The code below prints all of the column numbers.
                # this was used to find the values that could not be expressed as an int or float
                for i in range(len(names)):
                    print("names[{}]={}".format(i,names[i]))
                raise e
            # Here we incrementally merge the frames together. Special logic for the first
            # Note type(frame) == type(None) cannot be readily simplified. Sorry!
            if type(frame) == type(None):
                frame = df
            else:
                logging.info(f"{state_abbr}: starting merge")
                frame = pd.merge(frame, df, on='LOGRECNO', how='left')
                logging.info(f"{state_abbr}: done merge")
                del df
                gc.collect()    # because pandas has memory leaks

    logging.info(f"{state_abbr}: part2: merging and grouping by county")
    all_counties=pd.merge(frame, geo_df2, on='LOGRECNO').groupby('COUNTY')

    logging.info(f"{state_abbr}: part3: making county dirs and files. county count: {len(all_counties)}")
    for (county_code, df) in all_counties:
        logging.info(f"{state_abbr}: making {county_code} ")
        countydir = f'$ROOT/{state_abbr}/{state_code}{county_code}'
        dmakedirs(countydir)

        filename = f'{countydir}/sf1_county_{state_code}{county_code}.csv'
        df[df['SUMLEV'].isin(['050'])].to_csv(dopen(filename,'w'))

        filename = f'{countydir}/sf1_block_{state_code}{county_code}.csv'
        df[df['SUMLEV'].isin(['101'])].to_csv(dopen(filename,'w'))

        filename = f'{countydir}/sf1_tract_{state_code}{county_code}.csv' 
        df[df['SUMLEV'].isin(['140'])].to_csv(dopen(filename,'w'))

    t1 = time.time()
    print(f"{state_abbr}: Done. Processed summary files in {t1-t0:,.0f} seconds")
    with dopen(done_filename,"w") as f:
        f.write(time.asctime())

if __name__=="__main__":
    from argparse import ArgumentParser,ArgumentDefaultsHelpFormatter
    parser = ArgumentParser( formatter_class = ArgumentDefaultsHelpFormatter,
                             description="Create per-county county, block and tract count files." )
    dbrecon.argparse_add_logging(parser)
    parser.add_argument("--config", help="config file")
    parser.add_argument("state_abbrs",nargs="*",help='Specify states to process')
    parser.add_argument("--all",action='store_true',help='All states')
    parser.add_argument("--threads", '--j', type=int, help='Each state is run single-threaded')

    args =    parser.parse_args()
    config   = dbrecon.get_config(filename=args.config)
    dbrecon.setup_logging(config=config,loglevel=args.loglevel,prefix="02red")
    logfname = logging.getLogger().handlers[0].baseFilename
    dfxml    =   DFXMLWriter(logger=logging.info, filename=logfname.replace(".log",".dfxml"), prettyprint=True)

    states = []
    if args.all:
        states = dbrecon.all_state_abbrs()
    else:
        states = [dbrecon.state_abbr(st).lower() for st in args.state_abbrs]

    if not states:
        print("Specify states to download or --all")
        exit(1)

    if not args.threads:
        args.threads=config['run'].getint('threads',1)

    logging.info("Running with {} threads".format(args.threads))
    with multiprocessing.Pool(args.threads) as p:
        p.map(process_state, states)
