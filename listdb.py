#!/usr/bin/env python3
"""
List datasets and other information

"""

import os
import sys

import constants as C

import cb_spec_decoder
import cb_spark_demo
import ctools.cspark as cspark
import ctools.s3     as s3
import ctools.tydoc  as tydoc

if __name__=="__main__":
    import argparse

    parser = argparse.ArgumentParser(description='List available datasets and other specified information.',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--year",  type=int, help=f"Only list specified year (default {C.YEARS})")
    parser.add_argument("--product", type=str, help=f"Only list specified data product (default {C.PRODUCTS})")
    parser.add_argument("--table", type=str,  help='Only show specified table; default is all tables.')
    parser.add_argument("--showtables", help="Show all the tables", action='store_true')
    parser.add_argument("--showvars", help="Show all the variables", action='store_true')
    parser.add_argument("--dump",  action='store_true', help='dump every table')
    parser.add_argument("--debug", action='store_true')
    args = parser.parse_args()

    for year in C.FILES_FOR_YEAR_PRODUCT.keys():
        for product in C.FILES_FOR_YEAR_PRODUCT[year].keys():
            if args.year and year!=args.year:
                continue
            if args.product and product!=args.product:
                continue
            try:
                df = cb_spec_decoder.DecennialData(dataroot=cb_spark_demo.DATAROOT, year=year, 
                                                   product=product, debug=args.debug)
            except FileNotFoundError as e:
                if args.debug:
                    print("DEBUG:",str(e))
                print(f"Not found: {year} {product}")
                continue
            except RuntimeError as e:
                print(f"Internal consistency error reading {year} {product}:")
                print(e)
                print("")
                continue
            tables = df.schema.tables() if not args.table else [df.schema.get_table(args.table)]
            print(f"{year} {product}:   {len(tables)} tables")
            if args.showtables:
                for table in tables:
                    print(f"   table {table.name:8}  {len(table.vars()):3} vars")
                    if args.showvars:
                        for variable in table.varnames():
                            printf(f"        {variable}")
            print()
