#!/usr/bin/env python3
"""
geodump: dump variables from the geofiles for making crosswalks
"""

import os
import os.path
import re
import zipfile
import io
import sys
import copy
import logging
from collections import defaultdict

# File locations

from urllib.parse import urlparse
import constants as C

import ctools
import ctools.tydoc as tydoc
import ctools.s3 as s3
import ctools.dconfig as dconfig
from ctools.schema.schema import Schema
from ctools.schema.variable import Variable
from ctools.schema import TYPE_INTEGER,TYPE_VARCHAR,TYPE_NUMBER,TYPE_DECIMAL

SUMLEV_DEFAULT='750 for PL94, 101 for SF1, and 100 for UR1'

debug = False

"""
These regular expressions are used to parse the structure of Chapter 6 of the data product specification.
Fortunately, the format of Chapter 6 was consistent across 2000 and 2010, and between all data products.
Also consistent were the variable names.
"""

import cb_spec_decoder
from geolevels import GEOLEVELS

FIELDS = ['GEOID','LOGRECNO','SUMLEV','STATE','COUNTY','TRACT','BLOCK',
          'ZCTA5', # ZIP Code Tabulation Area (5-digit)
          'SDELM', # School District (Elementary),
          'SDSEC', # School District (Secondary),
          'SDUNI', # School District (Unified),
          'CD',    # Congressional District (111th),
          'SLDU',  # State Legislative District (Upper Chamber) (Year 1)
          'SLDL',  # State Legislative District (Lower Chamber) (Year 1)
          'VTD',   # Voting District,
          'COUSUB',# County Subdivision (FIPS)
          'SUBMCD',# Subminor Civil Division (FIPS)
          'UA', # Urban Areas,
          'CBSA', # Metropolitan Statistical Area,
          'METDIV', # Metrpolitan Division
          'CSA',    # Combined Statistical Area,
          'UGA',    # Urban Growth Area,
          'PUMA',   # Public Use Microdata Area
          'PLACE']   # Place (FIPS)

def make_crosswalk(geotable,geofile,args):
    tt = tydoc.tytable()
    tt.add_head(FIELDS)
    rows = 0
    try:
        for line in geofile:
            d = geotable.parse_line_to_dict(line)
            if args.debug:
                print(args.sumlev,d['SUMLEV'],args.sumlev==d['SUMLEV'])
            if (args.sumlev==d['SUMLEV']) or (args.sumlev=='any'):
                d['GEOID'] = d['STATE']+d['COUNTY']+d['TRACT']+d['BLOCK'][0]+d['BLOCK']
                tt.add_data( [d[field] for field in FIELDS])
                rows += 1
                if rows==args.limit:
                    break
    except KeyboardInterrupt as e:
        print(f"*** only read {rows} rows ***")
    tt.render(sys.stdout, format=args.format)


def make_counts(geotable,geofile,args):
    counts = defaultdict(int)
    for line in geofile:
        d = geotable.parse_line_to_dict(line)
        counts[d['SUMLEV']] += 1
    tt = tydoc.tytable()
    tt.add_head(['Summary Level','Count','Description'])
    for key in sorted(counts.keys()):
        tt.add_data([key,counts[key],GEOLEVELS.get(key,'???')])
    tt.render(sys.stdout, format=args.format)

def make_distinct(geotable,geofile,args):
    counts = defaultdict(set)
    for line in geofile:
        d = geotable.parse_line_to_dict(line)
        if d['SUMLEV']==args.sumlev or args.sumlev=='all':
            for field in FIELDS:
                if field in d:
                    counts[field].add(d[field])
    tt = tydoc.tytable()
    tt.add_head(['Variable','Distinct Values'])
    for (field,items) in sorted(counts.items()):
        tt.add_data([field,len(items)])
    tt.render(sys.stdout, format=args.format)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="""Geodump: using the parsed schema, dump information from the geography file for crosswalks.""",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--year",    type=int, help="Use statistics from this year" ,default=2010)
    parser.add_argument("--product", type=str, help="Specify the product", default=C.SF1)
    parser.add_argument("--limit",   help="limit output to this many records. Specify 0 for no limit", type=int, default=10)
    parser.add_argument("--sumlev",  help="Only print this summary leve. Specify 'any' for all.", default=SUMLEV_DEFAULT)
    parser.add_argument("--debug",   action='store_true')
    parser.add_argument("--format",  help="Specify format of output. Can be md,html,latex,csv", default='md')
    parser.add_argument("geofile", help="Specify the geofile to dump")
    parser.add_argument("--counts",  action='store_true',
                        help="Generate a histogram of how many counts there are at each summary level")
    parser.add_argument("--distinct",  action='store_true',
                        help="Generate a report of the number of distinct values of the critical fields for a specific summary level")
    
    args = parser.parse_args()

    if args.sumlev==SUMLEV_DEFAULT:
        args.sumlev = {C.PL94:'750',
                       C.SF1:'101',
                       C.UR1:'100'}[args.product]

    specfile = cb_spec_decoder.get_cvsspec(year=args.year,product=args.product)
    schema   = cb_spec_decoder.schema_for_spec(specfile, year=args.year, product=args.product)
    geotable = schema.get_table(C.GEO_TABLE)
    geofile  = dconfig.dopen(args.geofile,'r',encoding='latin1')

    if args.counts:
        make_counts(geotable,geofile,args)
        exit(0)

    if args.distinct:
        make_distinct(geotable,geofile,args)
        exit(0)

    make_crosswalk(geotable,geofile,args)
