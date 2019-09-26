import ctools.cspark as cspark
import pprint
import cb_spec_decoder
import os
from collections import defaultdict
from ctools.s3 import list_objects
from constants import *
from string import ascii_uppercase
import sf1_info as info
import re
import shutil
from geocode import GeoCode
from copy import deepcopy
import pprint


if 'DAS_S3ROOT' in os.environ:
    DATAROOT = f"{os.environ['DAS_S3ROOT']}/2000/;{os.environ['DAS_S3ROOT']}/2010/"
else:
    DATAROOT = os.path.join( os.path.dirname(__file__), 'data')

SUMMARY_LEVEL_MAP = {
    'STATE' : '040',
    'COUNTY' : '050',
    'BLOCK' : '101'
}

SQL_STRINGS ={
    'BLOCK': "(STATE={state_code} AND COUNTY={county_code} AND TRACT={tract_code} AND BLOCK={block_code})"
}


def smallcell_structure_persons_sf_2000(summary_level, threshold):
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
    sf1_year = 2000
    current_product = SF1
    sf1_2000 = cb_spec_decoder.DecennialData(dataroot=DATAROOT, year=sf1_year, product=current_product)

    block_map = build_block_level_map()

    print("Geolevels by state and summary level:")
    sf1_2000.get_df(tableName=GEO_TABLE, sqlName='GEO_2000')
    multi_index_list = []
    tables = ["P3"]
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
            result_temp_table = spark.sql(f"SELECT GEO_2000.LOGRECNO, GEO_2000.STUSAB, GEO_2000.STATE, GEO_2000.COUNTY,"
                                          f" GEO_2000.TRACT, GEO_2000.BLOCK, GEO_2000.SUMLEV, GEO_2000.GEOCOMP, GEO_2000.NAME,"
                                          f" {current_table_var_string}"
                                          f" FROM GEO_2000 INNER JOIN {table}_2000 ON GEO_2000.LOGRECNO={table}_2000.LOGRECNO"
                                          f" AND GEO_2000.STUSAB={table}_2000.STUSAB WHERE"
                                          f" GEO_2000.SUMLEV='{SUMMARY_LEVEL_MAP[summary_level]}'{filter_state_query}AND GEO_2000.GEOCOMP='00'"
                                          f" ORDER BY GEO_2000.STUSAB")
            result_temp_table.registerTempTable("temp_table")
            print(f"Size of Dict {len(block_map.keys())}")
            percentage_map = {key: {str(k): v for k, v in value.items()} for key, value in block_map.items()}
            table_results = {row['STATE'] + row['COUNTY'] + row['TRACT'] + row['BLOCK']: row for row in result_temp_table.collect()}

        except Exception as e:
            print("Error", e)
        print(f"Length {len(multi_index_list)}")
        # print(multi_index_list)
        # pp = pprint.PrettyPrinter(indent=4)
        # pp.pprint(multi_index_list)


def build_block_level_map():
    block_map = defaultdict(dict)
    s3_file_list = []
    file_location = os.path.join(os.getenv('DAS_S3ROOT'), os.getenv("JBID", default=""), "relationship/")
    print(f"Loading file at {file_location}")

    # Grab and create file path to the S3 prefix that has the relationship file in it.
    for j in list_objects(file_location):
        s3_file_list.append(os.path.join(os.getenv('DAS_S3ROOT'), j['Key']))

    print("Starting to build relationship table")
    cb_spec_decoder.build_relationship_table(s3_file_list, "relationship")
    print("Done building relationship table.")

    relationship_results = spark.sql(f"SELECT STATE_2000, COUNTY_2000, TRACT_2000, BLK_2000, STATE_2010, COUNTY_2010, "
                                     f"TRACT_2010, BLK_2010, AREALAND_INT, AREALAND_2010 FROM relationship")

    print("Start processing results")
    for result in relationship_results.collect():
        if int(result['AREALAND_2010']) == 0:
            continue
        geocode_2000 = GeoCode(result['STATE_2000'], result['COUNTY_2000'], result['TRACT_2000'], result['BLK_2000'], result['AREALAND_INT'])
        geocode_2010 = GeoCode(result['STATE_2010'], result['COUNTY_2010'], result['TRACT_2010'], result['BLK_2010'], result['AREALAND_2010'])
        block_map[geocode_2010][geocode_2000] = int(geocode_2000.area_land) / int(geocode_2010.area_land)
    print("Result dict built")

    return block_map


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


def test_block_consistency(block_map):
    count_cons = 0
    count_incons = 0
    for k, v in block_map.items():
        contribution_total_2000 = 0
        for item in v:
            contribution_total_2000 += float(item[1])
        if contribution_total_2000 != float(k[1]):
            print(f"Found inconsistency for {k[0]}")
            count_incons += 1
        else:
            count_cons += 1
    print(f"Size of inconsistency {count_incons}")
    print(f"Size of consistant {count_cons}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Tool for converting from 2000 SF1 to 2010',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--type", help="housing or person")
    parser.add_argument("--sumlevel", help="Valid summary levels include STATE, COUNTY", required=True,
                        choices=['BLOCK'])
    parser.add_argument("--threshold", help="Threshold to be include in multi list", required=True, type=float)
    parser.add_argument("--filterstate", help="The fips state code", type=int)
    args = parser.parse_args()

    spark = cspark.spark_session(logLevel='ERROR', pydirs=['.', 'ctools', 'ctools/schema'])
    if args.filterstate:
        filter_state_query = f" AND GEO_2000.STATE='{args.filterstate}' "
    else:
        filter_state_query = ''
    if args.type:
        print(f'Threshold = {float(args.threshold)}')
        if args.type == 'housing':
            # smallCellStructure_HouseholdsSF2000(args.sumlevel, args.threshold)
            pass
        elif args.type == 'person':
            smallcell_structure_persons_sf_2000(args.sumlevel, args.threshold)
        shutil.rmtree("temp", ignore_errors=True)
