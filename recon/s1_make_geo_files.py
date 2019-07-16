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
    """Given a state abbreviation, find the geo file, extract information, and store in the CSV files
    and in the SQL database."""

    # Input files
    state_code       = dbrecon.state_fips(state_abbr)
    sf1_zipfilename  = dbrecon.dpath_expand("$SF1_DIST/{state_abbr}2010.sf1.zip").format(state_abbr=state_abbr)
    sf1_geofile      = dbrecon.dpath_expand("$SF1_DIST/{state_abbr}geo2010.sf1").format(state_abbr=state_abbr)

    # Output files
    geofile_csv_filename               = f"$ROOT/{state_abbr}/geofile_{state_abbr}.csv"
    state_county_list_filename = f'$ROOT/{state_abbr}/state_county_list_{state_code}.csv'

    # If the output files exist, return
    if dbrecon.dpath_exists(geofile_csv_filename) and dbrecon.dpath_exists(state_county_list_filename):
        logging.warning(f"{geofile_csv_filename} exists; {state_county_list_filename} exists; will not overwrite")
        return

    logging.info(f"Creating {geofile_csv_filename}")
    dbrecon.dmakedirs(f"$ROOT/{state_abbr}") # make sure we can create the output file

    # Get layout for geofile. This uses the hard-coded information in the geo_layout.txt file.
    # TODO: move to the learned schema from the PDF
    names    = []
    colspecs = []

    for g in csv.DictReader(dopen(GEO_LAYOUT_FILENAME,'r', encoding='latin1'), delimiter=' '):
        names.append(g['field_name'])
        colspecs.append((int(g['start_pos'])-1, int(g['start_pos'])+int(g['length'])-1))

    # We use dopen() to open the geography file. It's either in the ZIP archive or its been extracted.
    # dopen handles it either way.
    #
    # extract fields from the geofile and write them to the geofile_csv_file.
    # We do this because the geofile is position-specified and it was harder to use that.
    # We also extract the county list

    sf1file = dopen(sf1_geofile, zipfilename=sf1_zipfilename, encoding='latin1')
    csvfile = dopen(geofile_csv_filename, 'w')
    writer  = csv.DictWriter(csvfile, fieldnames=names)
    writer.writeheader()
    f       = dopen(state_county_list_filename,'w')
    writer2 = csv.writer(f)
    for line in sf1file:
        columns = (colspecs)
        dataline = collections.OrderedDict(list(zip(names,[line[c[0]:c[1]] for c in colspecs])))
        writer.writerow(dataline)

        if dataline['SUMLEV']=='050':
            row = [dataline['STATE'], dataline['COUNTY'],state_abbr]
            writer2.writerow(row)
    sf1file.close()
    csvfile.close()
    f.close()


if __name__=="__main__":
    from argparse import ArgumentParser,ArgumentDefaultsHelpFormatter
    parser = ArgumentParser( formatter_class = ArgumentDefaultsHelpFormatter,
                             description="Read SF1 geography files and creates the counties geography file. This is pretty fast, so it is not parallelized" )
    parser.add_argument("--showcounties", 
                        help="Display all counties for state from files that were created", action='store_true')
    parser.add_argument("state_abbr", help="States to process", nargs='*')
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
              
    # Are we just printing status reports?
    if args.showcounties:
        for state_abbr in states:
            print(dbrecon.counties_for_state(state_abbr))
        exit(0)

    # Generate the CSV files. This may be parallelized in the future
    for state_abbr in states:
        with Timer() as timer:
            make_county_list(state_abbr)

    print("Made geofiles for: {}".format(" ".join(states)))
