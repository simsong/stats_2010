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
#from decennial_df import DecennialDF,files,register_files,unique_selector

import cb_spec_decoder
import ctools.cspark as cspark
import ctools.s3     as s3
import ctools.tydoc  as tydoc

if 'DAS_S3ROOT' in os.environ:
    DATAROOT = f"{os.environ['DAS_S3ROOT']}/2000/;{os.environ['DAS_S3ROOT']}/2010/"
else:
    DATAROOT = os.path.join( os.path.dirname(__file__), 'data')

def smallCellStructure_PersonsSF2000():
    # From a list of tables with integer counts, find those with small counts in 2000 SF1
    # See Ch. 6 of https://www.census.gov/prod/cen2000/doc/sf1.pdf
    from string import ascii_uppercase
    import re
    tables =    [  
                    "P3",       # Race                          [[[Block level tables begin]]]
                    "P4",       # HISP x Race
                    "P5",       # Race for Pop 18+
                    "P6",       # HISP x Race for Pop 18+
                    "P12",      # Sex by Age (2-5 year buckets)
                    "P14",      # Sex by Age for Pop <20
                    "P16",      # Pop in HHs
                    # P27-P30, P32, P36; REL not yet in schema
                    "P37",      # Pop in GQs
                    "P38"       # Pop in GQs by Sex by Age                
                ]
    # Sex by Age (Major Race Alone)
    tables +=   [f"P12{letter}" for letter in ascii_uppercase[:6]] # A-F
    tables +=   [
                    "P12G",     # Sex by Age (2+ races)
                    "P12H",     # Sex by Age (HISP)
                    "P12I",     # Sex by Age (White Alone, Not HISP)
                    # P27A-P30I, P32A-I; REL not yet in schema
                    "PCT12",    # Sex by Age (1 year buckets)   [[[Tract level tables begin]]]
                    "PCT13"     # Sex by Age, Pop in HHs
                    # PCT16-PCT17; 3-digit GQs not yet in schema
                ]
    # Sex by Age (Major Race Alone)
    tables +=   [f"PCT12{letter}" for letter in ascii_uppercase[:6]] # A-F
    tables +=   [
                    "PCT12G",   # Sex by Age (2+ races)
                    "PCT12H",   # Sex by Age (HISP)
                ]
    # Sex by Age (Major Race Alone, Not HISP)
    tables +=   [f"PCT12" for letter in ascii_uppercase[8:8+6]] # I-N 
    tables +=   ["PCT12O"]      # Sex by Age (2+ races, Not HISP)
    # Sex by Age (Major Race Alone), Pop in HHs
    tables +=   [f"PCT13{letter}" for letter in ascii_uppercase[:9]] # A-I
    tables +=   [
                    "PCT13G",   # Sex by Age (2+ races), Pop in HHs
                    "PCT13H",   # Sex by Age (HISP), Pop in HHs
                    "PCT13I"    # Sex by Age (White Alone, Not HISP), Pop in HHs
                    # PCT17A-I; 3-digit GQs not yet in schema
                ]

    year = 2000
    product = SF1
    sf1_2000 = cb_spec_decoder.DecennialData(dataroot=DATAROOT, year=year, product=product)

    print("Geolevels by state and summary level:")
    sf1_2000.get_df(tableName = GEO_TABLE, sqlName='GEO_2000')
    
    #Loop the variables in the tables. This is slower then doing a single query with all the variables but I want to be able to view
    #the output with the tytable which has problems if you have alot of variables.
    for table in tables:
        #Just wanted to break after first loop to stop for testing.
        if table == "P4":
            break
        print(f'Current Table: {table}')
        sf1_2000.get_df(tableName=f"{table}", sqlName=f"{table}_2000")
        regex = re.compile(r'^[P]')
        current_table_var_names = list( filter(regex.search, list(sf1_2000.get_table(table).varnames())) )
        current_table_var_names = list(filter(filterIds, current_table_var_names))
        current_table_var_string = ",".join(current_table_var_names)
        current_info = {}
        print(f'Current Table: {table}.')
        result_temp_table = spark.sql(f"SELECT GEO_2000.LOGRECNO, GEO_2000.STUSAB, GEO_2000.STATE, GEO_2000.SUMLEV, GEO_2000.GEOCOMP, GEO_2000.NAME, {current_table_var_string} FROM GEO_2000 "
                f"INNER JOIN {table}_2000 ON GEO_2000.LOGRECNO={table}_2000.LOGRECNO AND GEO_2000.STUSAB={table}_2000.STUSAB "
                f"WHERE GEO_2000.SUMLEV='040' AND GEO_2000.GEOCOMP='00' ORDER BY GEO_2000.STUSAB")
        result_temp_table.registerTempTable( "temp_table" )
        print_table(result_temp_table)
        sf1_2000.print_legend(result_temp_table)

        #Loop the variables in the tables. This is slower then doing a single query with all the variables but I want to be able to view
        #the output with the tytable which has problems if you have alot of variables.
        current_table_var_names = ["P003031"]
        for current_var in current_table_var_names:
            result = spark.sql(f"SELECT LOGRECNO, STUSAB, STATE, SUMLEV, GEOCOMP, NAME, {current_var} FROM temp_table "
                    f"WHERE {current_var}=0")
            print_table(result)
            sf1_2000.print_legend(result)


        

def print_table(result):
    tt = tydoc.tytable()
    tt.add_head( result.columns )
    for row in result.collect():
        tt.add_data(row)
    tt.render(sys.stdout, format='md')
    

def filterIds(ids):
    # This includes all of the none leaf ids of the tables proposed by Philip. 
    # This is currently on P3, P4, and P5.
    # I wish but could not find a automatic way to tell what where totals and what where leafs.
    total_table_reference = ["P003001","P003002","P003009","P003010","P003026","P003047",
                             "P003063","P003070","P004001","P004003","P004004","P004011",
                             "P004012","P004028","P004049","P004065","P004072","P005001",
                             "P005002","P005009","P005010","P005026","P005047","P005063",
                             "P005070"]
    if(ids in total_table_reference):
        return False
    else:
        return True

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
                    for cifsn in range(SEGMENTS_FOR_YEAR_PRODUCT[year][product]):
                        objs = [obj for obj in ypfiles if obj[STATE]==state and obj[CIFSN]==cifsn]
                        if len(objs)==0:
                            print(f"** error. no files for {product} {year} {state} cifsn {cifsn}")
                        elif len(objs)>1:
                            print(f"** error. too many files for {product} {year} {state} cifsn {cifsn}:")
                            for obj in objs:
                                print(obj)
                            
        print("Validation done")
        exit(0)

    # Note that getting spark here causes the arguments to be reparsed under spark-submit
    # Normally that's not a problem
    spark  = cspark.spark_session(logLevel='ERROR', pydirs=['.','ctools','ctools/schema'])
    #demo()
    smallCellStructure_PersonsSF2000()

