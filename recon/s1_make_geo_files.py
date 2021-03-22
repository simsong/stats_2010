#!/usr/bin/env python3
#
"""
read_geo_file.py:
Inputs: SF1 ZIPFILES
Outputs: SF1 geofile as a CSV with a file header and list of counties in the state
Output location: $ROOT/{state_abbr}/
"""

import json
import csv
import collections
import sys
import dbrecon
import logging
import time
import os
import io
import multiprocessing
import zipfile

sys.path.append( os.path.join(os.path.dirname(__file__),".."))

import ctools.s3
from ctools.timer import Timer

from dbrecon import dopen,dpath_expand,dmakedirs,DB,GEOFILE_FILENAME_TEMPLATE,STATE_COUNTY_FILENAME_TEMPLATE



REIDENT = os.getenv('REIDENT')
GEO_LAYOUT_FILENAME="$SRC/layouts/geo_layout.txt"

TRANSACTION_RECORDS = 20

def fields_str(field_count,record_count=1):
    fields = "(" + ",".join(['%s']*field_count) + ")"
    fields_str = ",".join([fields] * record_count)
    return fields_str

def make_county_list(state_abbr:str):
    """Given a state abbreviation, find the geo file, extract information, and store in the CSV files
    and in the SQL database."""

    print(f"make_county_list({state_abbr})")

    state_code       = dbrecon.state_fips(state_abbr)

    # Input files

    sf1_zipfilename  = dbrecon.dpath_expand(f"$SF1_DIST/{state_abbr}2010.sf1.zip")
    sf1_geofilename  = f"{state_abbr}geo2010.sf1"

    # Open the SF1 zipfile
    if sf1_zipfilename.startswith("s3://"):
        zf = zipfile.ZipFile(ctools.s3.S3File(sf1_zipfilename))
    else:
        zf = zipfile.ZipFile(sf1_zipfilename)
    sf1_geofile = io.TextIOWrapper(zf.open(sf1_geofilename))


    # Input Reader --- Get layout for geofile. This uses the hard-coded information in the geo_layout.txt file.
    names    = []
    colspecs = []
    for g in csv.DictReader(dopen(GEO_LAYOUT_FILENAME,'r', encoding='latin1'), delimiter=' '):
        names.append(g['field_name'])
        colspecs.append((int(g['start_pos'])-1, int(g['start_pos'])+int(g['length'])-1))

    # CSV output. We make this by default. In the future  we should be able to run it entirely out of the database
    if args.csv:
        # Output files
        geofile_csv_filename       = GEOFILE_FILENAME_TEMPLATE.format(state_abbr=state_abbr)
        state_county_list_filename = STATE_COUNTY_FILENAME_TEMPLATE.format(state_abbr=state_abbr, state_code=state_code)

        logging.info(f"Creating {geofile_csv_filename}")
        dbrecon.dmakedirs( os.path.dirname(geofile_csv_filename) ) # make sure we can create the output file

        csvfile = dopen(geofile_csv_filename, 'w')
        writer  = csv.DictWriter(csvfile, fieldnames=names)
        writer.writeheader()
        f       = dopen(state_county_list_filename,'w')
        writer2 = csv.writer(f)

    # Get our own database connection
    db = DB()
    db.connect()
    c = db.cursor()
    c.execute(f"DELETE from {REIDENT}geo where STUSAB=%s",(state_abbr,))

    # extract fields from the geofile and write them to the geofile_csv_file and/or the database
    # We do this because the geofile is position-specified and it was harder to use that.
    # We also extract the county list

    DB_FIELDS="STUSAB,SUMLEV,LOGRECNO,STATE,COUNTY,TRACT,BLOCK,NAME,POP100"
    DB_FIELDS_ARRAY = DB_FIELDS.split(",")

    vals = []
    count = 0
    total_count = 0

    for line in sf1_geofile:
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
            total_count += 1
            if count >= TRANSACTION_RECORDS:
                c.execute(f"INSERT INTO {REIDENT}geo (" + DB_FIELDS + ") VALUES " + fields_str(len(DB_FIELDS_ARRAY),count), vals)
                vals = []
                count = 0

    # Finish up database transaction
    if count>0:
        c.execute(f"INSERT INTO {REIDENT}geo (" + DB_FIELDS + ") VALUES " + fields_str(len(DB_FIELDS_ARRAY),count), vals)
        total_count += count
    db.commit()
    print("Total: {}".format(total_count))
    assert total_count>0
    sf1_geofile.close()

    # Select georecords into the tracts
    c.execute(f"INSERT INTO {REIDENT}tracts (stusab,state,county,tract) SELECT stusab,state,county,tract from {REIDENT}geo where sumlev=140")
    db.commit()

    if args.csv:
        csvfile.close()
        f.close()


if __name__=="__main__":
    from argparse import ArgumentParser,ArgumentDefaultsHelpFormatter
    parser = ArgumentParser( formatter_class = ArgumentDefaultsHelpFormatter,
                             description="Read SF1 geography files, creates the counties geography files, and loads the MySQL database."
                             "This is pretty fast and DB heavy, so it is not parallelized" )
    parser.add_argument("--showcounties",
                        help="Display all counties for state from files that were created", action='store_true')
    parser.add_argument("--nocsv", help="Do not make the CSV files", action='store_true')
    parser.add_argument("state_abbr", help="States to process. Say 'all' for all", nargs='*')
    dbrecon.argparse_add_logging(parser)
    args     = parser.parse_args()
    config   = dbrecon.setup_logging_and_get_config(args=args,prefix="01mak")

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

    # Generate the CSV files. Do this in parallel
    with multiprocessing.Pool(10) as p:
        p.map(make_county_list, states)

    print("Made geofiles for: {}".format(" ".join(states)))
