#!/usr/bin/env python3
"""
This is a program to generate ad hoc reports on the 2010 SF1
"""

HELP="""
Generate ad hoc reports on the 2010 SF1
"""


import geocode
import decennial_df
from constants import *




def custom_report_42(ddf):
    "State FIPS | County FIPS | Tract | Block group | Block | total group quarters population (first table item)"

    geo = ddf.get_table('geo')
    print("Geo first 10 available variables")
    for v in list(geo.vars())[0:10]:
        print(v.name, v.desc)
    print()

    p42 = ddf.get_table('P42')
    print("P42 available variables:")
    for v in p42.vars():
        print(v.name, v.desc)

    # Now get a dataframe for both, merge them, and print
    # pylint: disable=E0401
    from pyspark.sql import SparkSession
    from pyspark.sql.functions import col
    spark = SparkSession.builder.getOrCreate()
    geo_df = ddf.get_df(tableName='geo', sqlName='geo')
    p42_df = ddf.get_df(tableName='P42', sqlName='p42')
    spark.sql('SELECT state,count(*) from geo GROPU BY state order by 1').show(n=100)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=HELP,
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--cr42",action='store_true', help="custom report from Table P42")
    parser.add_argument("--cr44",action='store_true', help="custom report from Table P44")
    parser.add_argument("--tables",action='store_true', help='show tables')
    args = parser.parse_args()
    ddf = decennial_df.DecennialDF(year=2010, product=SF1)

    if args.tables:
        print("available tables:")
        for table in ddf.schema.tables():
            print(table)


    if args.cr42:
        custom_report_42(ddf)
