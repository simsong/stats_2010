#!/usr/bin/env python3
"""
Demo of accessing sf1 from spark.
Set up your files like this:

SF1_ROOT = location of SF1. 
   If you are running under spark on EMR, this should be a s3:// or hdfs://
   If you are running under spark stand-alone, this should be just a regular directory.

You can arrange the files any way that you want inside SF1. We scan the directory and find all the files.
"""

import os
import sys

from constants import *
import cb_spec_decoder
import ctools.cspark as cspark
import ctools.s3     as s3
import ctools.tydoc  as tydoc

debug = False

SF1_ROOT='SF1_ROOT'

if __name__=="__main__":
    import argparse

    spark  = cspark.spark_session(logLevel='ERROR')

    parser = argparse.ArgumentParser(description='Tool for using SF1 with Spark',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--list", help="List available files", action='store_true')
    args = parser.parse_args()

    # Get a schema object associated with the SF1 for 2010
    year = 2010
    product = SF1

    try:
        root = os.environ[SF1_ROOT]
    except KeyError:
        raise RuntimeError("Environment variable SF1_ROOT must be defined with location of SF1 files")

    sf1_2010 =  cb_spec_decoder.DecennialData(root=root,year=year,product=product)
    if args.list:
        print(f"Year: {year} product: {product}")
        print("Available files: ",len(s.files))
        print("Available states: "," ".join(s.unique_selector('state')))
        print("Available products: ", " ".join(s.unique_selector('product')))
        print("Available years: ", " ".join(s.unique_selector('year')))
        print("Available segments: ", " ".join([str(i) for i in s.unique_selector('segment')]))
        print("Available tables: "," ".join([t.name for t in schema.tables()]))


    print("Geolevels by state and summary level:")
    sf1_2010.get_df(tableName = GEO_TABLE, sqlName='GEO_2010')
    #print(spark.sql("SELECT * from GEO_2010 LIMIT 10").collect())
    #spark.sql("SELECT FILEID,STUSAB,LOGRECNO,STATE,COUNTYCC,TRACT,BLKGRP,BLOCK,FROM GEO_2010 LIMIT 10").show()
    tt = tydoc.tytable()
    tt.add_head(['State','Summary Level','Count'])
    for row in spark.sql("SELECT STUSAB,SUMLEV,COUNT(*) FROM GEO_2010 GROUP BY STUSAB,SUMLEV ORDER BY 1,2").collect():
        tt.add_data(row)
    tt.render(sys.stdout, format='md')

    print("Test; Print the names of 20 distinct names in the file (unformatted printing)")
    d0 = spark.sql("SELECT DISTINCT LOGRECNO,STUSAB,STATE,SUMLEV,NAME FROM GEO_2010 LIMIT 20")
    sf1_2010.print_legend(d0)
    for row in d0.collect():
        print(row)


    print("Table P2 just has counts. Here we dump the first 10 records:")
    sf1_2010.get_df(tableName="P2", sqlName='P2_2010')
    d1 = spark.sql("SELECT * FROM P2_2010 LIMIT 10")
    d1.show()
    sf1_2010.print_legend(d1)


    print("Table P17 has decimal numbers; they are represented as decimal numbers. Here are the first 10 rows:")
    sf1_2010.get_df(tableName="P17", sqlName='P17_2010')
    d2 = spark.sql("SELECT * FROM P17_2010 LIMIT 10")
    d2.show()
    sf1_2010.print_legend(d2)

    print("Table P2 counts by state and county:")
    res = spark.sql("SELECT GEO_2010.STUSAB,GEO_2010.COUNTY,GEO_2010.NAME,P0020001,P0020002,P0020003,P0020004,P0020005,P0020006 FROM GEO_2010 "
                    "INNER JOIN P2_2010 ON GEO_2010.STUSAB=P2_2010.STUSAB and GEO_2010.LOGRECNO=P2_2010.LOGRECNO "
                    "WHERE GEO_2010.SUMLEV='050' ORDER BY STUSAB,COUNTYCC")

    tt = tydoc.tytable()
    tt.add_head( res.columns )
    for row in res.collect():
        tt.add_data(row)
    tt.render(sys.stdout, format='md')
    sf1_2010.print_legend(res)

    # Compute counts by 
