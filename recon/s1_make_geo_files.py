#!/usr/bin/env python3
#
# read_geo_file.py:
# Inputs: SF1 ZIPFILES
# Outputs: SF1 geofile as a CSV with a file header and list of counties in the state
# Output location: $ROOT/{state_abbr}/

import json
import csv
import collections
import sys
import dbrecon
import logging
import time
import os

sys.path.append( os.path.join(os.path.dirname(__file__),".."))

from dbrecon import dopen,dpath_expand,dmakedirs
from ctools.timer import Timer

GEO_LAYOUT_FILENAME="$SRC/layouts/geo_layout.txt"

def make_county_list(state_abbr:str):

    # Find our input files

    state_code       = dbrecon.state_fips(state_abbr)
    sf1_zipfilename  = dbrecon.dpath_expand("$SF1_DIST/{state_abbr}2010.sf1.zip").format(state_abbr=state_abbr)
    sf1_input_file   = dbrecon.dpath_expand("$SF1_DIST/{state_abbr}geo2010.sf1").format(state_abbr=state_abbr)

    # Get output files
    geo_filename               = f"$ROOT/{state_abbr}/geofile_{state_abbr}.csv"
    state_county_list_filename = f'$ROOT/{state_abbr}/state_county_list_{state_code}.csv'

    # If the output files exist, return
    if dbrecon.dpath_exists(geo_filename) and dbrecon.dpath_exists(state_county_list_filename):
        logging.warning(f"{geo_filename} exists; {state_county_list_filename} exists; will not overwrite")
        return

    logging.info(f"Creating {geo_filename}")
    dbrecon.dmakedirs(f"$ROOT/{state_abbr}") # make sure we can create the output file

    with Timer() as timer:

        # Get layout for geofile. This uses the hard-coded information in the geo_layout.txt file
        # move to the learned schema from the PDF
        names=[]
        col_starts=[]
        col_ends=[]
        colspecs=[]

        for g in csv.DictReader(dopen(GEO_LAYOUT_FILENAME,'r', encoding='latin1'), delimiter=' '):
            names.append(g['field_name'])
            col_starts.append(int(g['start_pos'])-1)
            col_ends.append(int(g['start_pos'])+int(g['length'])-2)
            colspecs.append((int(g['start_pos'])-1, int(g['start_pos'])+int(g['length'])-1))

        # We use dopen() to open the geography file. It's either in the ZIP archive or its been extracted.
        # dopen handles it either way.
        #
        # Below is cleaned up from original code, but still converting
        # line into a dictionary and then writing it out with the
        # DictWriter.  Presumably this is done to reorder the columns

        with dopen(sf1_input_file, zipfilename=sf1_zipfilename, encoding='latin1') as sf1file:
            with dopen(geo_filename, 'w') as csvfile:
                writer = None       # will set later
                for line in sf1file:
                    columns = (colspecs)
                    dataline = collections.OrderedDict(list(zip(names,[line[c[0]:c[1]] for c in colspecs])))

                    if not writer:       # we want a header on the output file
                        row_head = list(dataline.keys())
                        writer   = csv.DictWriter(csvfile, fieldnames=row_head)
                        writer.writeheader()
                    writer.writerow(dataline)


        print(f"Creating {state_county_list_filename}")
        geo = csv.DictReader(dopen(geo_filename, 'r', encoding='latin1'))
        state_abbr_dict={}
        for s in dbrecon.STATES:
            state_abbr_dict[s['fips_state']]=s['state_abbr'].lower()

        # Extract Summary Level 050 (state county)
        with dopen(state_county_list_filename,'w') as f:
            writer = csv.writer(f)
            for g in geo:
                if g['SUMLEV']=='050':
                    row = [g['STATE'], g['COUNTY'],state_abbr_dict[g['STATE']]]
                    writer.writerow(row)


if __name__=="__main__":
    from argparse import ArgumentParser,ArgumentDefaultsHelpFormatter
    parser = ArgumentParser( formatter_class = ArgumentDefaultsHelpFormatter,
                             description="Read SF1 geography files and creates the counties geography file. This is pretty fast, so it is not parallelized" )
    parser.add_argument("--showcounties", help="Display all counties for state frmo files that were created", action='store_true')
    parser.add_argument("state_abbr", nargs='*')
    dbrecon.argparse_add_logging(parser)
    args     = parser.parse_args()
    config   = dbrecon.setup_logging_and_get_config(args,prefix="01mak")

    # Verify that all of the input files that are needed exist and that we can read them
    for fn in [GEO_LAYOUT_FILENAME,
               "$SRC/layouts/layouts.json",
               "$SRC/layouts/sf1_vars_race_binaries.csv"]:
        if not dbrecon.dpath_exists(fn):
            raise FileNotFoundError(fn)

    if args.state_abbr:
        states = args.state_abbr
    else:
        states = dbrecon.all_state_abbrs()
              
    # Make sure the output directory for the layouts exists

    for state_abbr in states:
        if args.showcounties:
            print(dbrecon.counties_for_state(state_abbr))
        else:
            make_county_list(state_abbr)

    print("Made geofiles for: {}".format(" ".join(states)))
