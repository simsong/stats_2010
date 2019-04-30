#!/usr/bin/env python3
"""
Demo of accessing sf1 from spark.
Set up your files like this:

SF1_ROOT = location of SF1. 
   If you are running under spark on EMR, this should be a s3:// or hdfs://
   If you are running under spark stand-alone, this should be just a regular directory.

"""

import os
import sys

from constants import *
from decennial_df import DecennialDF,files,register_files,unique_selector

import cb_spec_decoder
import ctools.cspark as cspark
import ctools.s3     as s3
import ctools.tydoc  as tydoc

if 'DAS_S3ROOT' in os.environ:
    DATAROOT = f"{os.environ['DAS_S3ROOT']}/2000/;{os.environ['DAS_S3ROOT']}/2010/"
else:
    DATAROOT = os.path.join( os.path.dirname(__file__), 'data')

def demo():
    # Get a schema object associated with the SF1 for 2010

    year = 2010
    product = SF1
    sf1_2010 = cb_spec_decoder.DecennialData(dataroot=DATAROOT, year=year,product=product)

    print("Geolevels by state and summary level:")
    sf1_2010.get_df(tableName = GEO_TABLE, sqlName='GEO_2010')

    print("10 records from GEO_2010:")
    for _ in spark.sql("SELECT * from GEO_2010 LIMIT 10").collect():
        print(_)
    #spark.sql("SELECT FILEID,STUSAB,LOGRECNO,STATE,COUNTYCC,TRACT,BLKGRP,BLOCK FROM GEO_2010 LIMIT 10").show()


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


if __name__=="__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Tool for using SF1 with Spark',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--validate", help="Validate all data files", action='store_true')
    args = parser.parse_args()

    if args.validate:
        for year in years:
            for product in products:
                print(f"Year: {year} product: {product}")

                ypfiles   = [obj for obj in files if obj[YEAR]==year and obj[PRODUCT]==product]
                states    = set([obj[STATE] for obj in ypfiles])
                print(f"Available states: {len(states)}")

                print("Validating states...")
                #for obj in ypfiles:
                #    print(obj)
                for state in STATES:
                    for file_number in range(SEGMENTS_PER_PRODUCT[year][product]):
                        objs = [obj for obj in ypfiles if obj[STATE]==state and obj[CIFSN]==file_number]
                        if len(objs)==0:
                            print(f"** error. no files for {product} {year} {state} file number {file_number}")
                        elif len(objs)>1:
                            print(f"** error. too many files for {product} {year} {state} file number {file_number}:")
                            for obj in objs:
                                print(obj)
                            
        print("Validation done")
        exit(0)

    # Note that getting spark here causes the arguments to be reparsed under spark-submit
    # Normally that's not a problem
    spark  = cspark.spark_session(logLevel='ERROR', pydirs=['.','ctools','ctools/schema'])
    demo()
