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

debug = False

"""
These regular expressions are used to parse the structure of Chapter 6 of the data product specification.
Fortunately, the format of Chapter 6 was consistent across 2000 and 2010, and between all data products.
Also consistent were the variable names.
"""

import cb_spec_decoder

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="""Geodump: using the parsed schema, dump information from the geography file for crosswalks.""",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--year",    type=int, help="Use statistics from this year" ,default=2010)
    parser.add_argument("--product", type=str, help="Specify the product", default=C.SF1)
    parser.add_argument("--limit",   help="limit output to this many records. Specify 0 for no limit", type=int, default=10)
    parser.add_argument("--sumlev",  help="Only print this summary leve. Specify 'any' for all ", default='750')
    parser.add_argument("--debug",   action='store_true')
    parser.add_argument("--format",  help="Specify format of output. Can be md,html,latex,csv", default='md')
    parser.add_argument("geofile", help="Specify the geofile to dump")
    args = parser.parse_args()


    specfile = cb_spec_decoder.get_cvsspec(year=args.year,product=args.product)
    schema   = cb_spec_decoder.schema_for_spec(specfile, year=args.year, product=args.product, debug=args.debug)

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

    geotable = schema.get_table(C.GEO_TABLE)
    tt = tydoc.tytable()
    tt.add_head(FIELDS)
    rows = 0
    try:
        for line in dconfig.dopen(args.geofile,'r',encoding='latin1'):
            d = geotable.parse_line_to_dict(line)
            if (args.sumlev==d['SUMLEV']) or (args.sumlev=='any'):
                d['GEOID'] = d['STATE']+d['COUNTY']+d['TRACT']+d['BLOCK'][0]+d['BLOCK']
                tt.add_data( [d[field] for field in FIELDS])
                rows += 1
                if rows==args.limit:
                    break
    except KeyboardInterrupt as e:
        print(f"*** only read {rows} rows ***")
    tt.render(sys.stdout, format=args.format)
