#!/usr/bin/env python3
"""
Demo of accessing sf1 from spark.
Set up your files like this:

SF1_ROOT = location of SF1. 
   If you are running under spark on EMR, this should be a s3:// or hdfs://
   If you are running under spark stand-alone, this should be just a regular directory.

"""



from constants import *
from copy import deepcopy
from string import ascii_uppercase
from string import ascii_uppercase
import cb_spec_decoder
import ctools.cspark as cspark
import ctools.tydoc  as tydoc
import json
import logging
import os
import re
import sf1_info as info
import sf1_info_house as info_house
import sys
from collections import defaultdict
from ctools.s3 import put_object, get_bucket_key
import shutil
import pathlib
import time
import pprint
import glob
import uuid

if 'DAS_S3ROOT' in os.environ:
    DATAROOT = f"{os.environ['DAS_S3ROOT']}/2000/;{os.environ['DAS_S3ROOT']}/2010/"
else:
    DATAROOT = os.path.join( os.path.dirname(__file__), 'data')

SUMMARY_LEVEL_MAP = {
    'NATION': '010',
    'STATE' : '040',
    'COUNTY' : '050'
}

def smallCellStructure_HouseholdsSF2000(summary_level, threshold):
    # From a list of tables with integer counts, find those with small counts in 2000 SF1, for Households
    # See Ch. 6 of https://www.census.gov/prod/cen2000/doc/sf1.pdf
    # Tables chosen from that document to get small-cell counts corresponding to histogram at:
    #   https://github.ti.census.gov/CB-DAS/das_decennial/blob/master/programs/schema/schemas/Schema_Household2010.py
    tables =    [
                    "P15",      # Total Households              [[[Block level tables begin]]]
                    "P18",      # HHSIZE x HHTYPE x PRES_OWN_CHILD
                    "P19",      # PRES_UNDER_18 x HHTYPE
                    "P20",      # HHAGE x HHTYPE x PRES_OWN_CHILD
                    "P21",      # HHTYPE x HHAGE
                    "P22",      # PRES_>60 x HHSIZE x HHTYPE
                    "P23",      # PRES_>65 x HHSIZE x HHTYPE
                    "P24",      # PRES_>75 x HHSIZE x HHTYPE
                    "P26",       # HHSIZE
                    "P31",      # FAMILIES
                    "P34",      # FAM_TYPE x PRES_OWN_CHILD x AGE_OWN_CHILD
                ]
    # HHs by Major Race Alone / HISP of Householder
    tables +=   [f"P15{letter}" for letter in ascii_uppercase[:9]] # A-I
    # HHs by HHSIZE by Major Race Alone / HISP of Householder
    tables +=   [f"P26{letter}" for letter in ascii_uppercase[:9]] # A-I
    # Families by HHSIZE by Major Race Alone / HISP of Householder
    tables +=   [f"P31{letter}" for letter in ascii_uppercase[:9]] # A-I
    # Family Type x PRES_OWN_CHILD x AGE_OWN_CHILD by Major Race Alone / HISP of Householder
    # Very weird error on this table tables +=   [f"P34{letter}" for letter in ascii_uppercase[:9]] # A-I
    # Family Type x PRES_REL_CHILD x AGE_REL_CHILD by Major Race Alone / HISP of Householder #### Irrelevant to histogram?
    tables +=   [
                    "PCT14"    # Unmarried-Partner HHs by Sex of Partners #### Can determine from HHTYPE+HHSEX in our histogram
                ]
    # Skipping some tables we eventually want but which current histogram doesn't support: H3, H4, H5
    tables +=   [
                    "H6",   # HHRACE
                    "H7",   # HHRACE x HHHISP
                    # "H8", Not sure how to do Tallied   # HHRACEs Tallied (this one is a bit weird but I think works with current histogram)
                    # "H9", Not sure how to do Tallied  # HHRACEs Tallied x HHHISP
                    "H13"   # HHSIZE
                    # H14   # TENURE x HHRACE (do want eventually but not in scope of current histogram)
                    # H15   # TENURE x HHSIZE (do want eventually but not in scope of current histogram)
                    # H16   # TENURE x HHAGE (do want eventually but not in scope of current histogram)
                    # H17   # TENURE x HHTYPE x HHAGE (do want eventually but not in scope of current histogram)
                ]
    # TENURE x HHSIZE x Major Race Alone / HISP of Householder
    #tables +=   [f"H15{letter}" for letter in ascii_uppercase[:9]] # A-I # Not yet in scope of histogram
    # H16A-I # Not yet in scope
    print('smallCellStructure_HouseholdsSF2000')
    sf1_year = 2000
    current_product = SF1
    sf1_2000 = cb_spec_decoder.DecennialData(dataroot=DATAROOT, year=sf1_year, product=current_product)
    print("Geolevels by state and summary level:")
    sf1_2000.get_df(tableName=GEO_TABLE, sqlName='GEO_2000')
    multi_index_list = []
    for table in tables:
        try:
            print(f'Loading Table: {table}')
            sf1_2000.get_df(tableName=f"{table}", sqlName=f"{table}_2000")
            result_temp_table = spark.sql(f"SELECT * FROM GEO_2000 "
                f"INNER JOIN {table}_2000 ON GEO_2000.LOGRECNO={table}_2000.LOGRECNO AND "
                f"GEO_2000.STUSAB={table}_2000.STUSAB "
                f"WHERE GEO_2000.SUMLEV='{SUMMARY_LEVEL_MAP[summary_level]}'{filter_state_query}AND GEO_2000.GEOCOMP='00' ORDER BY GEO_2000.STUSAB")
            table_info = info_house.get_correct_house_builder(table)
            result_temp_table.registerTempTable("temp_table")
            print_table(result_temp_table)
            sf1_2000.print_legend(result_temp_table)
            multi_index_list = deepcopy(multi_index_list) + deepcopy(table_info.process_results(summary_level, result_temp_table, table, threshold))
        except ValueError as error:
            print(error)
            break

    start_time = time.time()
    state_dict = build_state_level(multi_index_list=multi_index_list)
    uuid_str = str(uuid.uuid4())[:5]
    for v, k in state_dict.items():
        save_data(summary_level, v, k, threshold, uuid_str)
    end_time = time.time()
    print(f'Save data in {end_time - start_time}')


def smallCellStructure_PersonsSF2000(summary_level, threshold):
    # From a list of tables with integer counts, find those with small counts in 2000 SF1, for Persons
    # See Ch. 6 of https://www.census.gov/prod/cen2000/doc/sf1.pdf
    # Tables chosen from that document to get small-cell counts corresponding to histogram at:
    #   https://github.ti.census.gov/CB-DAS/das_decennial/blob/master/programs/schema/schemas/Schema_DHCP_HHGQ.py
    tables =    [  
                    "P3",       # Race                          [[[Block level tables begin]]]
                    "P4",       # HISP x Race
                    "P5",       # Race for Pop 18+
                    "P6",       # HISP x Race for Pop 18+
                    "P12",      # Sex by Age (2-5 year buckets)
                    "P14",      # Sex by Age for Pop <20
                    "P16",      # Pop in HHs
                    # P27-P30, P32, P36; REL not yet in schema
                    "P37"      # Pop in GQs
                    # "P38"       # Pop in GQs by Sex by Age                
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
    tables +=   [f"PCT12{letter}" for letter in ascii_uppercase[8:8+6]] # I-N
    tables +=   ["PCT12O"]      # Sex by Age (2+ races, Not HISP)
    # Sex by Age (Major Race Alone), Pop in HHs
    tables +=   [f"PCT13{letter}" for letter in ascii_uppercase[:9]] # A-I
    tables +=   [
                    "PCT13G",   # Sex by Age (2+ races), Pop in HHs
                    "PCT13H",   # Sex by Age (HISP), Pop in HHs
                    "PCT13I"    # Sex by Age (White Alone, Not HISP), Pop in HHs
                    # PCT17A-I; 3-digit GQs not yet in schema
                ]
    start_time = time.time()
    sf1_year = 2000
    current_product = SF1
    sf1_2000 = cb_spec_decoder.DecennialData(dataroot=DATAROOT, year=sf1_year, product=current_product)

    print("Geolevels by state and summary level:")
    sf1_2000.get_df(tableName=GEO_TABLE, sqlName='GEO_2000')
    multi_index_list = []
    for table in tables:
        try:
            # Just wanted to break after first loop to stop for testing.
            print(f'Loading Table: {table}')
            sf1_2000.get_df(tableName=f"{table}", sqlName=f"{table}_2000")
            regex = re.compile(r'^[P]')
            all_var_names = sf1_2000.get_table(table).varnames()
            print(f"Length of all vars {len(all_var_names)}")
            current_table_var_names = list(filter(filter_ids_persons, list(filter(regex.search, list(all_var_names)))))
            print(f"Length of filtered vars {len(current_table_var_names)}")
            current_table_var_string = ",".join(current_table_var_names)
            table_info = info.get_correct_builder(table, current_table_var_names)
            # This sql does the join for the GEO_2000 table with the current table and then registers the new dataframe
            # as a temp table.
            # This is so we can use the already joined table to find the zeros. 
            print(f'Building temp table for {table}')
            result_temp_table = spark.sql(f"SELECT GEO_2000.LOGRECNO, GEO_2000.STUSAB, GEO_2000.STATE, GEO_2000.COUNTY, GEO_2000.SUMLEV, GEO_2000.GEOCOMP, GEO_2000.NAME, {current_table_var_string} FROM GEO_2000 "
                    f"INNER JOIN {table}_2000 ON GEO_2000.LOGRECNO={table}_2000.LOGRECNO AND GEO_2000.STUSAB={table}_2000.STUSAB "
                    f"WHERE GEO_2000.SUMLEV='{SUMMARY_LEVEL_MAP[summary_level]}'{filter_state_query}AND GEO_2000.GEOCOMP='00' ORDER BY GEO_2000.STUSAB")
            result_temp_table.registerTempTable("temp_table")
            print_table(result_temp_table)
            sf1_2000.print_legend(result_temp_table)
            multi_index_list = deepcopy(multi_index_list) + deepcopy(table_info.process_results(summary_level, result_temp_table, table, threshold))
        except ValueError as error:
            print(error)
            break
    end_time = time.time()
    print(f'Got data in {end_time - start_time}')

    start_time = time.time()
    state_dict = build_state_level(multi_index_list=multi_index_list)
    uuid_str = str(uuid.uuid4())[:5]
    for v, k in state_dict.items():
        save_data(summary_level, v, k, threshold, uuid_str)
    end_time = time.time()
    print(f'Save data in {end_time - start_time}')


def build_state_level(multi_index_list):
    histogram_state = defaultdict(list)
    for item in multi_index_list:
        histogram_state[item.geo_code_parts['STATE']].append(item)
    return histogram_state


def build_tract_compare_relationship_file():
    check_dupe = []
    tract_map = defaultdict(list)
    file_location = os.path.join(os.getenv('DAS_S3ROOT'), os.getenv("JBID", default=""), "relationship", "us2010trf_headers.csv")
    print(f"Loading file at {file_location}")
    cb_spec_decoder.build_relationship_table(file_location, "relationship")

    relationship_results = spark.sql(f"SELECT GEOID00, GEOID10 FROM relationship")

    for relationship_row in relationship_results.collect():
        tract_map[relationship_row['GEOID00']].append(relationship_row['GEOID10'])
        check_dupe.append(relationship_row['GEOID10'])

    check_set = set(check_dupe)
    print(f"Length of list {len(check_dupe)}")
    print(f"Length of set {len(check_set)}")

    printer = pprint.PrettyPrinter(indent=4)
    printer.pprint(tract_map)


def save_data(summary_level, state_id, index_list, threshold, uuid_str):
    location = os.path.join("users", os.getenv("JBID", default=""), "smallcell", args.type,
                            summary_level, uuid_str + "_threshold_" + str(threshold), state_id)
    output_dict = defaultdict(list)
    for item in index_list:
        store_location = os.path.join(location, f'{item.full_geo_code}_threshold_{threshold}.json')
        local_temp_store = os.path.join("temp", store_location)
        item.generate_expanded_histogram()
        path = pathlib.Path(local_temp_store)
        path.parent.mkdir(parents=True, exist_ok=True)
        output_dict[local_temp_store].extend(item.generate_expanded_histogram())
    for local_file_location, histogram in output_dict.items():
        with open(local_file_location, "w+") as filehandler:
            json.dump(histogram, filehandler)
    folder_location = os.path.join("temp", location, "*")
    files = [f for f in glob.glob(folder_location)]
    for file in files:
        (bucket, key) = get_bucket_key(os.path.join(os.getenv('DAS_S3ROOT'), file))
        key = key.split("temp/")[1]
        put_object(bucket, key, file)
        print(f"Upload: {file} s3://{bucket}/{key}")
        

def print_table(result):
    tt = tydoc.tytable()
    tt.add_head( result.columns )
    for row in result.collect():
        tt.add_data(row)
    tt.render(sys.stdout, format='md')
    

def filter_ids_persons(ids):
    # This will include all of the none leaf ids of the tables proposed by Philip.
    # I wish I could not find a automatic way to tell what where totals and what where leafs.
    total_table_reference = ["P003001","P003002","P003009","P003010","P003026","P003047",
                             "P003063","P003070","P004001","P004003","P004004","P004011",
                             "P004012","P004028","P004049","P004065","P004072","P005001",
                             "P005002","P005009","P005010","P005026","P005047","P005063",
                             "P005070","P006001","P006003","P006004","P006011","P006012",
                             "P006028","P006049","P006065","P006072","P012001","P012002",
                             "P012026","P014001","P014002","P014023","P037001","P037002",
                             "P037006"]
    [total_table_reference.extend([f"P012{letter}001", f"P012{letter}002", f"P012{letter}026"]) for letter in ascii_uppercase[:9]]
    [total_table_reference.extend([f"PCT012{letter}001", f"PCT012{letter}002", f"PCT012{letter}106"]) for letter in ascii_uppercase[:15]]
    total_table_reference += ["PCT012001", "PCT012002", "PCT012106"]
    [total_table_reference.extend([f"PCT013{letter}001", f"PCT013{letter}002", f"PCT013{letter}026"]) for letter in ascii_uppercase[:12]]
    total_table_reference += ["PCT013001", "PCT013002", "PCT013026"]
    return filter_based_on_list(ids=ids, total_table_reference=total_table_reference)


def filter_based_on_list(ids, total_table_reference):
    if ids in total_table_reference:
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
    parser.add_argument("--type", help="housing or person")
    parser.add_argument("--sumlevel", help="Valid summary levels include STATE, COUNTY", required=True, choices=['NATION', 'STATE', 'COUNTY'])
    parser.add_argument("--threshold", help="Threshold to be include in multi list", required=True, type=float)
    parser.add_argument("--filterstate", help="The fips state code", type=int)
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
    spark  = cspark.spark_session(logLevel='ERROR', pydirs=['.','ctools','ctools/schema'], appName="cb_spark_demo")
    if args.filterstate:
        filter_state_query = f" AND GEO_2000.STATE='{args.filterstate}' "
    else:
        filter_state_query = ''
    if args.type:
        print(f'Threshold = {float(args.threshold)}')
        if args.type == 'housing':
            smallCellStructure_HouseholdsSF2000(args.sumlevel, args.threshold)
        elif args.type == 'person':
            smallCellStructure_PersonsSF2000(args.sumlevel, args.threshold)
        elif args.type == 'tract_compare':
            build_tract_compare_relationship_file()
        shutil.rmtree("temp", ignore_errors=True)

