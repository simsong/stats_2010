#!/usr/bin/env python3
"""
List all of the available datasets

"""

import os
import sys

import constants as c

import cb_spec_decoder
import cb_spark
import ctools.cspark as cspark
import ctools.s3     as s3
import ctools.tydoc  as tydoc

if __name__=="__main__":
    import argparse

    parser = argparse.ArgumentParser(description='List all available datasets',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--year",  type=int, help=f"Only do this year (default {c.YEARS})")
    parser.add_argument("--product", type=str, help=f"Only do this product (default {c.PRODUCTS})")
    parser.add_argument("--debug", action='store_true')
    args = parser.parse_args()

    # Get a schema object associated with the SF1 for 2010
    years = c.YEARS if not args.year else [args.year]
    products = c.PRODUCTS if not args.product else [args.product]

    root = os.path.dirname(__file__)
    for year in years:
        for product in products:

            try:
                df = cb_spark.DecennialDF(root=root, year=year, product=product, debug=args.debug)
            except FileNotFoundError as e:
                print(f"Not found: f{year} {product}")
                continue
            except RuntimeError as e:
                print(f"Internal constency error reading f{year} {product}:")
                print(e)
                print("")
                continue
            print(f"{year} {product}:")
            for table in df.schema.tables():
                print(f"   table {table.name:8}  {len(table.vars()):3} vars")
            print()
