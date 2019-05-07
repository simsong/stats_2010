#!/usr/bin/env python3
"""
List datasets and other information

"""

import os
import sys

import constants as c

import cb_spec_decoder
import ctools.cspark as cspark
import ctools.s3     as s3
import ctools.tydoc  as tydoc

if __name__=="__main__":
    import argparse

    parser = argparse.ArgumentParser(description='List available datasets and other specified information.',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--year",  type=int, help=f"Only list specified year (default {c.YEARS})")
    parser.add_argument("--product", type=str, help=f"Only list specified data product (default {c.PRODUCTS})")
    parser.add_argument("--table", type=str,  help='Only show specified table; default is all tables.')
    parser.add_argument("--dump",  action='store_true', help='dump every table')
    parser.add_argument("--debug", action='store_true')
    args = parser.parse_args()

    # Get a schema object associated with the SF1 for 2010
    years = c.YEARS if not args.year else [args.year]
    products = c.PRODUCTS if not args.product else [args.product]

    dataroot = os.path.dirname(__file__)
    for year in years:
        for product in products:
            try:
                df = cb_spec_decoder.DecennialData(dataroot=dataroot, year=year, product=product, debug=args.debug)
            except FileNotFoundError as e:
                if args.debug:
                    print("DEBUG:",str(e))
                print(f"Not found: {year} {product}")
                continue
            except RuntimeError as e:
                print(f"Internal constency error reading f{year} {product}:")
                print(e)
                print("")
                continue
            print(f"{year} {product}:")
            tables = df.schema.tables() if not args.table else [df.schema.get_table(args.table)]
            for table in tables:
                print(f"   table {table.name:8}  {len(table.vars()):3} vars")
                if args.dump:
                    table.dump()
            print()
