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

from dbrecon import dopen,dpath_expand,dmakedirs,DB
from ctools.timer import Timer

GEO_LAYOUT_FILENAME="$SRC/layouts/geo_layout.txt"

def fields_str(field_count,record_count=1):
    fields = "(" + ",".join(['%s']*field_count) + ")"
    fields_str = ",".join([fields] * record_count)
    return fields_str

def make_county_list(state_abbr:str):
    """Given a state abbreviation, find the geo file, extract information, and store in the CSV files
    and in the SQL database."""

    print(f"make_county_list({state_abbr})")

    # Input files
    state_code       = dbrecon.state_fips(state_abbr)
    sf1_zipfilename  = dbrecon.dpath_expand("$SF1_DIST/{state_abbr}2010.sf1.zip").format(state_abbr=state_abbr)
    sf1_geofile      = dbrecon.dpath_expand("$SF1_DIST/{state_abbr}geo2010.sf1").format(state_abbr=state_abbr)
    sf1file          = dopen(sf1_geofile, zipfilename=sf1_zipfilename, encoding='latin1')

    # Input Reader --- Get layout for geofile. This uses the hard-coded information in the geo_layout.txt file.
    names    = []
    colspecs = []
    for g in csv.DictReader(dopen(GEO_LAYOUT_FILENAME,'r', encoding='latin1'), delimiter=' '):
        names.append(g['field_name'])
        colspecs.append((int(g['start_pos'])-1, int(g['start_pos'])+int(g['length'])-1))

    # CSV output
    if args.csv:
        # Output files
        geofile_csv_filename       = f"$ROOT/{state_abbr}/geofile_{state_abbr}.csv"
        state_county_list_filename = f'$ROOT/{state_abbr}/state_county_list_{state_code}.csv'

        # If the output files exist, return
        if dbrecon.dpath_exists(geofile_csv_filename) and dbrecon.dpath_exists(state_county_list_filename):
            logging.warning(f"{geofile_csv_filename} exists; {state_county_list_filename} exists; will not overwrite")
            return

        logging.info(f"Creating {geofile_csv_filename}")
        dbrecon.dmakedirs(f"$ROOT/{state_abbr}") # make sure we can create the output file

        csvfile = dopen(geofile_csv_filename, 'w')
        writer  = csv.DictWriter(csvfile, fieldnames=names)
        writer.writeheader()
        f       = dopen(state_county_list_filename,'w')
        writer2 = csv.writer(f)

    # Database output
    db = DB()
    db.connect()
    c = db.cursor()
    c.execute("delete from geo where STUSAB=%s",(state_abbr,))

    # extract fields from the geofile and write them to the geofile_csv_file and/or the database
    # We do this because the geofile is position-specified and it was harder to use that.
    # We also extract the county list

    DB_FIELDS="STUSAB,SUMLEV,LOGRECNO,STATE,COUNTY,TRACT,BLOCK,NAME,POP100"
    DB_FIELDS_ARRAY = DB_FIELDS.split(",")

    vals = []
    count = 0
    for line in sf1file:
        # convert the column-specified line to a dict
        dataline = collections.OrderedDict(list(zip(names,[line[c[0]:c[1]] for c in colspecs])))

        # Write to CSV file
        if args.csv:
            writer.writerow(dataline)
            if dataline['SUMLEV']=='050':
                row = [dataline['STATE'], dataline['COUNTY'],state_abbr]
                writer2.writerow(row)

        # Write to database specific geolevels
        if (dataline['SUMLEV'] in ['040', '050', '140', '750', '101']) and (dataline['GEOCOMP']=='00'):
            vals   += [dataline[field].strip() for field in DB_FIELDS_ARRAY]
            count  += 1
            if count == 20:
                c.execute("INSERT INTO geo (" + DB_FIELDS + ") VALUES " + fields_str(len(DB_FIELDS_ARRAY),count), vals)
                vals = []
                count = 0

    # Finish up database transaction
    c.execute("INSERT INTO geo (" + DB_FIELDS + ") VALUES " + fields_str(len(DB_FIELDS_ARRAY),count), vals)
    db.commit()
    sf1file.close()
    if args.csv:
        csvfile.close()
        f.close()


if __name__=="__main__":
    from argparse import ArgumentParser,ArgumentDefaultsHelpFormatter
    parser = ArgumentParser( formatter_class = ArgumentDefaultsHelpFormatter,
                             description="Read SF1 geography files and creates the counties geography file. "
                             "This is pretty fast and DB heavy, so it is not parallelized" )
    parser.add_argument("--showcounties", 
                        help="Display all counties for state from files that were created", action='store_true')
    parser.add_argument("--nocsv", help="Do not make the CSV files", action='store_true')
    parser.add_argument("state_abbr", help="States to process. Say 'all' for all", nargs='*')
    dbrecon.argparse_add_logging(parser)
    args     = parser.parse_args()
    config   = dbrecon.setup_logging_and_get_config(args,prefix="01mak")

    args.csv = not args.nocsv

    # Verify that all of the input files that are needed exist and that we can read them
    for fn in [GEO_LAYOUT_FILENAME,
               "$SRC/layouts/layouts.json",
               "$SRC/layouts/sf1_vars_race_binaries.csv"]:
        if not dbrecon.dpath_exists(fn):
            raise FileNotFoundError(fn)

    if args.state_abbr==[] or args.state_abbr[0]=='all':
        states = dbrecon.all_state_abbrs()
    else:
        states = args.state_abbr
              
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
