import ctools.cspark as cspark
import cb_spec_decoder
from collections import defaultdict
from ctools.s3 import list_objects
from constants import *
from string import ascii_uppercase
import sf1_info as info
import re
import shutil
from geocode import GeoCode
import uuid
import time
import sf1_info_house as info_house

if 'DAS_S3ROOT' in os.environ:
    DATAROOT = f"{os.environ['DAS_S3ROOT']}/2000/;{os.environ['DAS_S3ROOT']}/2010/"
else:
    DATAROOT = os.path.join( os.path.dirname(__file__), 'data')

relationship_dict = {
    "BLOCK": {
        "sql_name": "relationship_block",
        "sql_query": f"SELECT STATE_2000, COUNTY_2000, TRACT_2000, BLK_2000, STATE_2010, COUNTY_2010,"
                    f" TRACT_2010, BLK_2010, AREALAND_INT, AREALAND_2010, AREALAND_2000"
                    f" FROM relationship_block",
        "s3_folder_name": os.path.join(os.getenv('DAS_S3ROOT'), os.getenv("JBID", default=""), "relationship/"),
        "aggregate_from": "BLOCK",
        "app_name": "relationship_block_app"
    },
    "TRACT": {
        "sql_name": "relationship_tract",
        "sql_query": f"SELECT STATE00, COUNTY00, TRACT00, STATE10, COUNTY10, TRACT10, AREAPCT00PT FROM relationship_tract",
        "s3_folder_name": os.path.join(os.getenv('DAS_S3ROOT'), os.getenv("JBID", default=""), "relationship_tract/"),
        "aggregate_from": "TRACT",
        "app_name": "relationship_tract_app"
    }
}


def smallcell_structure_housing_sf_2000(summary_level, threshold):
    tables = [
        "P15",  # Total Households              [[[Block level tables begin]]]
        "P18",  # HHSIZE x HHTYPE x PRES_OWN_CHILD
        "P19",  # PRES_UNDER_18 x HHTYPE
        "P20",  # HHAGE x HHTYPE x PRES_OWN_CHILD
        "P21",  # HHTYPE x HHAGE
        "P22",  # PRES_>60 x HHSIZE x HHTYPE
        "P23",  # PRES_>65 x HHSIZE x HHTYPE
        "P24",  # PRES_>75 x HHSIZE x HHTYPE
        "P26",  # HHSIZE
        "P31",  # FAMILIES
        "P34",  # FAM_TYPE x PRES_OWN_CHILD x AGE_OWN_CHILD
    ]
    # HHs by Major Race Alone / HISP of Householder
    tables += [f"P15{letter}" for letter in ascii_uppercase[:9]]  # A-I
    # HHs by HHSIZE by Major Race Alone / HISP of Householder
    tables += [f"P26{letter}" for letter in ascii_uppercase[:9]]  # A-I
    # Families by HHSIZE by Major Race Alone / HISP of Householder
    tables += [f"P31{letter}" for letter in ascii_uppercase[:9]]  # A-I
    # Family Type x PRES_OWN_CHILD x AGE_OWN_CHILD by Major Race Alone / HISP of Householder
    # Very weird error on this table tables +=   [f"P34{letter}" for letter in ascii_uppercase[:9]] # A-I
    # Family Type x PRES_REL_CHILD x AGE_REL_CHILD by Major Race Alone / HISP of Householder #### Irrelevant to histogram?
    tables += [
        "PCT14"  # Unmarried-Partner HHs by Sex of Partners #### Can determine from HHTYPE+HHSEX in our histogram
    ]
    # Skipping some tables we eventually want but which current histogram doesn't support: H3, H4, H5
    tables += [
        "H6",  # HHRACE
        "H7",  # HHRACE x HHHISP
        # "H8", Not sure how to do Tallied   # HHRACEs Tallied (this one is a bit weird but I think works with current histogram)
        # "H9", Not sure how to do Tallied  # HHRACEs Tallied x HHHISP
        "H13"  # HHSIZE
    ]
    start_time = time.time()
    print('smallCellStructure_HouseholdsSF2000')

    blocks_to_tract_map = build_old_geo_to_new_geo_map(summary_level, **relationship_dict["BLOCK"])
    tract_to_tract_map = build_old_geo_to_new_geo_map(summary_level, **relationship_dict["TRACT"])

    sf1_year = 2000
    current_product = SF1
    sf1_2000 = cb_spec_decoder.DecennialData(dataroot=DATAROOT, year=sf1_year, product=current_product)
    print("Geolevels by state and summary level:")
    sf1_2000.get_df(tableName=GEO_TABLE, sqlName='GEO_2000')
    start_time_multi = time.time()
    query = "SELECT * FROM GEO_2000 " \
            "INNER JOIN {table}_2000 ON GEO_2000.LOGRECNO={table}_2000.LOGRECNO AND "\
            "GEO_2000.STUSAB={table}_2000.STUSAB "\
            "WHERE GEO_2000.SUMLEV='{SUMMARY_LEVEL_MAP[summary_level]}'{filter_state_query}AND " \
            "GEO_2000.GEOCOMP='00' ORDER BY GEO_2000.STUSAB"

    for table in tables:
        sf1_2000.get_df(tableName=f"{table}", sqlName=f"{table}_2000")
        table_info = info_house.get_correct_house_builder(table)
        rdd = load_data_from_table(table=table, sf1_2000=sf1_2000, summary_level=summary_level,
                                   threshold=threshold, blocks_to_tract_map=blocks_to_tract_map,
                                   tract_to_tract_map=tract_to_tract_map, rdd=rdd, table_info=table_info,
                                   current_table_var_string=None, query=query)

    print(f'TIme to extend list {time.time() - start_time_multi}')

    print(f"Length Before expanded {rdd.count()}")
    print(f'Time to run tables {time.time() - start_time}')
    rdd = rdd.map(lambda x: cartesian_iterative(x.histogram))
    rdd = rdd.flatMap(lambda item: item).cache()
    print(f"Length After expanded {rdd.count()}")
    df = rdd.toDF(['geoid', 'hhgq', 'sex', 'age', 'hisp', 'cenrace', 'citizen'])
    print(f"Length After df_convert {df.count()}")

    start_time = time.time()
    save_dataframe(df, summary_level, threshold)
    print(f'Time to save data {time.time() - start_time}')


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
    start_time = time.time()
    # sf1_year = 2000
    # current_product = SF1
    # sf1_2000 = cb_spec_decoder.DecennialData(dataroot=DATAROOT, year=sf1_year, product=current_product)

    blocks_to_tract_map = build_old_geo_to_new_geo_map(summary_level, **relationship_dict["BLOCK"])
    tract_to_tract_map = build_old_geo_to_new_geo_map(summary_level, **relationship_dict["TRACT"])

    print("Geolevels by state and summary level:")
    sf1_year = 2000
    current_product = SF1
    sf1_2000 = cb_spec_decoder.DecennialData(dataroot=DATAROOT, year=sf1_year, product=current_product)
    sf1_2000.get_df(tableName=GEO_TABLE, sqlName='GEO_2000')

    print(f"Starting table process")
    start_time_multi = time.time()
    query = "SELECT GEO_2000.LOGRECNO, GEO_2000.STUSAB, GEO_2000.STATE, GEO_2000.COUNTY," \
        " GEO_2000.TRACT, GEO_2000.BLOCK, GEO_2000.SUMLEV, GEO_2000.GEOCOMP, GEO_2000.NAME," \
        " {current_table_var_string}" \
        " FROM GEO_2000 INNER JOIN {table}_2000 ON GEO_2000.LOGRECNO={table}_2000.LOGRECNO" \
        " AND GEO_2000.STUSAB={table}_2000.STUSAB WHERE" \
        " GEO_2000.SUMLEV='{sum_level_to_use}' AND GEO_2000.GEOCOMP='00'" \
        " ORDER BY GEO_2000.STUSAB"
    rdd = None
    for table in tables:
        print(f'Loading Table: {table}')
        sf1_2000.get_df(tableName=f"{table}", sqlName=f"{table}_2000")
        regex = re.compile(r'^[P]')
        all_var_names = sf1_2000.get_table(table).varnames()
        current_table_var_names = list(filter(filter_ids_persons, list(filter(regex.search, list(all_var_names)))))
        current_table_var_string = ",".join(current_table_var_names)
        table_info = info.get_correct_builder(table, current_table_var_names)

        rdd = load_data_from_table(table=table, sf1_2000=sf1_2000, summary_level=summary_level,
                                   threshold=threshold, blocks_to_tract_map=blocks_to_tract_map,
                                   tract_to_tract_map=tract_to_tract_map, rdd=rdd,
                                   current_table_var_string=current_table_var_string, table_info=table_info,
                                   query=query)
    print(f'TIme to extend list {time.time() - start_time_multi}')

    print(f"Length Before expanded {rdd.count()}")
    print(f'Time to run tables {time.time() - start_time}')
    rdd = rdd.map(lambda x: cartesian_iterative(x.histogram))
    rdd = rdd.flatMap(lambda item: item).cache()
    print(f"Length After expanded {rdd.count()}")
    df = rdd.toDF(['geoid', 'hhgq', 'sex', 'age', 'hisp', 'cenrace', 'citizen'])
    print(f"Length After df_convert {df.count()}")

    start_time = time.time()
    save_dataframe(df, summary_level, threshold)
    print(f'Time to save data {time.time() - start_time}')


def cartesian_iterative(pools):
    result = [()]
    for pool in pools:
        result = [x + (y,) for x in result for y in pool]
    return result


def save_dataframe(df, summary_level, threshold):
    uuid_str = str(uuid.uuid4())[:5]
    print(f"UUID of Run {uuid_str}")
    location = os.path.join(os.getenv('DAS_S3ROOT'), "users", os.getenv("JBID", default=""), "smallcell", args.type,
                            summary_level, uuid_str + "_threshold_" + str(threshold))

    df.write.format("csv").save(location)


def load_data_from_table(table, sf1_2000, summary_level, threshold, blocks_to_tract_map, tract_to_tract_map, rdd,
                         current_table_var_string, table_info, query):
    try:
        map_to_send = blocks_to_tract_map if table[:3] != "PCT" else tract_to_tract_map
        sum_level_to_use = '101' if table[:3] != "PCT" else '080'
        query = eval(f'f"""{query}"""')
        print(query)
        result_temp_table = spark.sql(query)
        result_temp_table.registerTempTable("temp_table")
        print(f"Size of Dict {len(map_to_send.keys())}")
        table_results = {row['STATE'] + row['COUNTY'] + row['TRACT'] + row['BLOCK']: row for row in
                         result_temp_table.collect()}
        # to_return.extend(table_info.rdd_approach(map_to_send, table_results, summary_level, threshold, table))
        rdd_to_return = table_info.rdd_approach(map_to_send, table_results, summary_level, threshold, table, rdd)
    except Exception as e:
        import traceback
        traceback.print_exc()
    return rdd_to_return


def build_old_geo_to_new_geo_map(summary_level, sql_name, sql_query, s3_folder_name, app_name, aggregate_from=None):
    geo_id_info = {
        'STATE': 2,
        'COUNTY': 5,
        'TRACT': 11,
        'BLOCK': 15
    }

    s3_file_list = []
    print(f"Loading file at {s3_folder_name}")

    # Grab and create file path to the S3 prefix that has the relationship file in it.
    print(f"{aggregate_from}")
    for s3_file_path in list_objects(s3_folder_name):
        s3_file_list.append(os.path.join(os.getenv('DAS_S3ROOT'), s3_file_path['Key']))
    print(s3_file_list)

    print("Starting to build relationship table")
    cb_spec_decoder.build_relationship_table(path=s3_file_list, sql_name=sql_name,
                                             app_name=app_name)

    print("Done building relationship table.")
    relationship_results = spark.sql(sql_query)

    if args.filterstate:
        print(f"State: {args.filterstate}")
    print("Start processing results")
    if aggregate_from == "BLOCK":
        return handle_block_results(relationship_results, geo_id_info, summary_level)
    elif aggregate_from == "TRACT":
        return handle_tract_results(relationship_results, geo_id_info, summary_level)
    return NotImplemented("Have to provide aggregate_from")


def handle_tract_results(relationship_results, geo_id_info, summary_level):
    print("Handle Tract Results")
    block_map = defaultdict(dict)
    for result in relationship_results.collect():
        if args.filterstate and str(args.filterstate) != str(result['STATE10']):
            continue
        geocode_2000 = GeoCode(result['STATE00'], result['COUNTY00'], result['TRACT00'])
        geocode_2010 = GeoCode(result['STATE10'], result['COUNTY10'], result['TRACT10'])
        block_map[str(geocode_2010)[:geo_id_info[summary_level]]][str(geocode_2000)] = float(result['AREAPCT00PT'])
    return block_map


def handle_block_results(relationship_results, geo_id_info, summary_level):
    print("Handle Block Results")
    block_map = defaultdict(dict)
    for result in relationship_results.collect():
        if int(result['AREALAND_2000']) == 0:
            continue
        if args.filterstate and str(args.filterstate) != str(result['STATE_2010']):
            continue
        geocode_2000 = GeoCode(result['STATE_2000'], result['COUNTY_2000'], result['TRACT_2000'], result['BLK_2000'],
                               result['AREALAND_INT'])
        geocode_2010 = GeoCode(result['STATE_2010'], result['COUNTY_2010'], result['TRACT_2010'], result['BLK_2010'],
                               result['AREALAND_2010'])
        block_map[str(geocode_2010)[:geo_id_info[summary_level]]][str(geocode_2000)] = \
            int(geocode_2000.area_land) / int(result['AREALAND_2000'])
    return block_map


def filter_ids_persons(ids):
    # This will include all of the none leaf ids of the tables proposed by Philip.
    # I wish I could find a automatic way to tell what where totals and what where leafs.
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


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Tool for converting from 2000 SF1 to 2010',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--type", help="housing or person")
    parser.add_argument("--sumlevel", help="Valid summary levels include STATE, COUNTY", required=True,
                        choices=['TRACT', 'COUNTY'])
    parser.add_argument("--threshold", help="Threshold to be include in multi list", required=True, type=float)
    parser.add_argument("--filterstate", help="The fips state code", type=str)
    args = parser.parse_args()

    spark = cspark.spark_session(logLevel='ERROR', pydirs=['.', 'ctools', 'ctools/schema'])
    if args.type:
        print(f'Threshold = {float(args.threshold)}')
        if args.type == 'housing':
            smallcell_structure_housing_sf_2000(args.sumlevel, args.threshold)
            pass
        elif args.type == 'person':
            smallcell_structure_persons_sf_2000(args.sumlevel, args.threshold)
        shutil.rmtree("temp", ignore_errors=True)
