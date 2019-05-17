#!/usr/bin/env python3
#
"""
Read the processed SF1 dat and syntheize the LP file that will be input to the optimizer.

"""

from collections import defaultdict
from dbrecon import *
import xml.etree.ElementTree as ET
import math
import csv
import dbrecon
import gc
import itertools
import json
import logging
import multiprocessing
import numpy as np
import os
import os.path
import pandas as pd
import psutil
import sys
import time
import tempfile
import subprocess

from total_size import total_size

assert pd.__version__ > '0.19'


MIN_LP_SIZE = 1000              # smaller than this, the file must be invalid
MAX_SF1_ERRORS = 10             # some files may have errors


MISSING = 'missing'
HISPANIC = 'hispanic'

Y = 'Y'
N = 'N'
MALE     = 'male'
FEMALE   = 'female'
BOTH     = 'both'

SEX = 'sex'
AGE = 'age'
WHITE = 'white'
BLACK = 'black'
AIAN  = 'aian'
ASIAN = 'asian'
NH    = 'nh'
SOR   = 'sor'
HISP  = 'hisp'

GEOID = 'geoid'
TABLE_NUM = 'table_num'
CELL_NUMBER = 'cell_number'
TABLEVAR = 'tablevar'           

# geo_table is a column that has cell_number and geoid concatenated
# do not make it a category, as it appears that the column is distinct
# in each row of the tables that use it
GEO_TABLE = 'geo_table'

#
# These are all of the possible values that each attribute can take on:
#

SEX_RANGE      = [MALE, FEMALE]
AGE_RANGE      = list(range(0, 111))
WHITE_RANGE    = [Y, N]
BLACK_RANGE    = [Y, N]
AIAN_RANGE     = [Y, N]
ASIAN_RANGE    = [Y, N]
HAWAIIAN_RANGE = [Y, N]
SOR_RANGE      = [Y, N]
HISPANIC_RANGE = [Y, N]

ATTRIBUTES = [SEX, AGE, WHITE, BLACK, AIAN, ASIAN, NH, SOR, HISP]

#
# These are the kinds of column names that should be turned into pandas categories
#
CATEGORIES = ATTRIBUTES + [GEOID, TABLE_NUM, CELL_NUMBER, TABLEVAR]

def make_attributes_categories(df):
    """Change attributes that are objects to categories"""
    for a in CATEGORIES:
        if (a in df) and (df[a].dtype=='object'):
            df[a] = df[a].astype('category')
    return df

def lpfile_properly_terminated(fname):
    # Note that we need to open in binary mode to allow seeking from end of file
    if dbrecon.dgetsize(fname) < MIN_LP_SIZE:
        return False
    with dopen(fname,"rb") as f:
        f.seek(-3,2)
        last3 = f.read(3)
        return last3==b'End'
    

################################################################
## 
## code to build the LP files
##
################################################################

# Function to get p01_counts list for an entity (block or tract)
#
def get_p01_counts( level, data_dict):
    p01_counts = {}
    for s in data_dict:
        if level=='block': 
            q1=data_dict[s]
        elif level=='tract': 
            q1=data_dict
        else:
            raise RuntimeError("invalid level: {}".format(level))
        for q in q1:
            if q['table_number'] == 'P1':
                p01_counts[q[GEOID]] = q['value']
    return p01_counts

def update_constraints(f, level, n_con, summary_nums, geo_id, state_code, county, state_abbr):
    tuple_list=[]
    constraint_list=[]

    for s in summary_nums:
        tuple_list.extend(summary_nums[s]['tuple_list'])
        constraint_list.extend(summary_nums[s]['constraints'])
    summary_nums={}
    tuple_frame=pd.DataFrame(tuple_list, columns=['TID'] + ATTRIBUTES + ['print_val', GEOID])
    make_attributes_categories(tuple_frame)
    del tuple_list

    con_frame_list=[]
    for c in constraint_list:
        c2=list(itertools.product(*c[1:10]))
        for c3 in c2:
            #value, table number, geoid
            x=[c[0]]
            x.extend(c3)
            x.append(c[10])
            x.append(c[11])
            x.append(c[12])
            con_frame_list.append(x)
    del constraint_list
    gc.collect()
    con_frame = pd.DataFrame(con_frame_list, columns=['value'] + ATTRIBUTES + [TABLE_NUM,GEOID,CELL_NUMBER])
    con_frame[GEO_TABLE] = con_frame[CELL_NUMBER] + '_' + con_frame[GEOID]
    make_attributes_categories(con_frame) 
    
    ## Note: we must make con_frame into categories *after* GEO_TABLE is added, because you cannot add categories


    if level=='block':
        merge_list=[GEOID] + ATTRIBUTES
    else:
        merge_list=ATTRIBUTES

    # lp is the largest data frame that is made. Before the move to
    # categories, it would routinely exceed 50GB. Now it is a merge of
    # two other dataframes that use categories. So it is typically
    # 1GB-10GB.

    lp = pd.merge(tuple_frame, con_frame, how='inner', on=merge_list, copy=False)
    if args.mem:
        mem_info("tuple_frame",tuple_frame)
        mem_info("con_frame",con_frame)
        mem_info('lp',lp)
    del tuple_frame
    del con_frame
    gc.collect()

    lp_short = lp[[GEO_TABLE, 'value','print_val']]
    del lp
    gc.collect()

    lp_df    = lp_short.groupby([GEO_TABLE, 'value']).agg(lambda x: ' + '.join(x))
    if args.mem:
        mem_info("lp_short",lp_short)
        mem_info("lp_df",lp_df)
    del lp_short
    gc.collect()

    for index, row in lp_df.iterrows():
        f.write("_C_{geo_table}_{n_con}: {group} = {n} \n".
                format(geo_table=index[0],n_con=n_con, group=row['print_val'], n=index[1]))
        n_con += 1
    del lp_df
    gc.collect()
    return n_con




class LPTractBuilder:
    """Build the LP files for a given tract"""

    def __init__(self):
        self.master_tuple_list=[]

        pass

    def get_constraint_summary(self, level, p01_data, data_dict, summary_nums):
        """
        Function to get the summary dict to create constraints
        @param summary_nums - dictionary with summary numbers that is updated.
          summary_nums[geoid] = {}        --- a dictionary of summary numbers for each GEOID.
             {'n_people' : '0'}           --- (why is this number a string?)
             {'constraints' : []}         --- The constraints for this GEOID
             {'tuple_list'  : []}         --- all of the tuples for this geoid
           - erased by update_constraints
        The tuples consist of:
        tuple=(pid,sex,age,wh,bl,aian,asian,nh,sor,hisp,VARIABLE_NAME,GEO_ID)
          p = person ID f"{geoid}_{sex}_{start_age}_{age}"
          s = sex
          a,wh,bl,aian,nh,sor,hisp = race attributes
         master_tuple_list usage:
           - extended by get_constraint_summary() when level='block'
           - then each tuple is appended to summary_nums[geo_id]['tuple_list']
           - t[10] for each tuple is written to the LP file; this defines all of the variables as binaries.
           - TODO: make the variable list a list of generators and expanding on writing

        @param summary_nums updated.
        @param master_tuple_list - updated
        """
        if args.mem:
            print("get_constraint_summary  level: {} p01_data: {:,}B data_dict: {:,}B summary_nums: {:,}B".
                  format(level,total_size(p01_data,verbose=False),total_size(data_dict,verbose=False),
                         total_size(summary_nums,verbose=False)))

        p01_counts = get_p01_counts(level, p01_data)

        ###Loops through the data to create the constraints and the value that it should be output to.
        # for example, if it is female, hispanic, age 10-14, then it will create a list for each of the
        # sex/race/age combos to be used later.
        # I don't have medians in here.  working on it...they are weird because of the fractional
        # medians provided in the sf files
        # creates a block level dictionary with the associated constraints
        # Also creates a list of table P12 (sex*age for a block) to be used to instantiate people

        ###Initial values of sex and race and origin

        for s in data_dict:
            if s[GEOID] not in summary_nums:
                summary_nums[s[GEOID]] = {'n_people': '0', 'constraints': [], 'tuple_list': []}
            if s['table_number'] == 'P1':
                summary_nums[s[GEOID]]['n_people'] = s['value']

            constraint_value = s['value']

            ## Initialize all constraint values to the default values, which is all possible values
            ## Then see if there are any restrictions in the table currently being processed
            S     = SEX_RANGE
            A     = AGE_RANGE
            Wh    = WHITE_RANGE
            Bl    = BLACK_RANGE
            Aian  = AIAN_RANGE
            Asian = ASIAN_RANGE
            NH    = HAWAIIAN_RANGE
            Sor   = SOR_RANGE
            Hisp  = HISPANIC_RANGE

            ### This creates the set of possible values for the people who were responsible
            ### for the counts in the table.
            ### use race and origin binaries and the two or more races

            if s['white']  != MISSING: Wh = [s['white']]
            if s['black']  != MISSING: Bl = [s['black']]
            if s['aian']   != MISSING: Aian = [s['aian']]
            if s['asian']  != MISSING: Asian = [s['asian']]
            if s['nhopi']  != MISSING: NH  = [s['nhopi']]
            if s['sor']    != MISSING: Sor = [s['sor']]
            if s[HISPANIC] != MISSING:
                if s[HISPANIC]==HISPANIC:
                    Hisp=['Y']
                else: Hisp = [s[HISPANIC]]

            if s['sex'] == MISSING:
                pass
            elif s['sex'] == BOTH:
                S = SEX_RANGE
            elif s['sex'] == MALE:
                S = [MALE]
            elif s['sex'] == FEMALE:
                S = [FEMALE]
            else:
                raise RuntimeError('invalid sex: ',s['sex'])

            if s['start_age'] != MISSING:
                A = [x for x in range(int(s['start_age']), int(s['end_age']) + 1)]

            if s['median_age'] != MISSING:
                if s['start_age'] == MISSING:
                    ##constrain to missing age start_age and media
                    A = [x for x in range(int(0), int(math.floor(constraint_value)) + 1)]
                    constraint_value = math.floor(p01_counts[s[GEOID]] / 2)
                else:
                    ##constrain to a given start age and median
                    A = [x for x in range(int(s['start_age']), int(math.floor(constraint_value)) + 1)]
                    constraint_value = math.floor(p01_counts[s[GEOID]] / 2)

            if s['two']!='two':
                constraint = [constraint_value, S, A, Wh, Bl, Aian, Asian, NH, Sor, Hisp, s['table_number'], s[GEOID], s[CELL_NUMBER]]
                summary_nums[s[GEOID]]['constraints'].append(constraint)

                if s['table_number'] == 'P12' and not (s['start_age'] == 0 and s['end_age'] == 110) and constraint_value > 0:
                    s_tuple_list = []

                    #
                    # format of tuple=(p,s,a,wh,bl,aian,asian,nh,sor,hisp) where the person number is s_a_number
                    # Note -- the person number is made against table P12, which is sex by age.  It ensures that there
                    # are fewer records to enter the optimization to speed it up.
                    #
                    # Previously this was done with list comprehension; it was changed to a generator.
                    #

                    s_tuple_list = (['{}_{}_{}_{}'.format(s[GEOID], s['sex'], s['start_age'], p), 
                                    s['sex'], age, wh, bl, AI, As, nh, so, hisp]
                                    for p in range(0, int(s['value']))
                                    for wh in Wh
                                    for bl in Bl
                                    for AI in Aian
                                    for As in Asian
                                    for nh in NH
                                    for so in Sor
                                    for hisp in Hisp
                                    for age in [x for x in range(int(s['start_age']), int(s['end_age']) + 1)])
                    
                    #
                    # Now we use the generator create the master_tuple_list.
                    # This is the slow operation because we are evaluating the generator that we created above.
                    #
                    # The master_tuple_list is used twice in build_tract_lp():
                    # Once to make the tract_summary_nums, and then it is written to the LP file.
                    # So we won't save anything by making it a generator.
                    #

                    if level=='block':
                        for i in s_tuple_list:
                            row = i + ['C_'+'_'.join(map(str, i))] + [s[GEOID]]
                            summary_nums[s[GEOID]]['tuple_list'].append(row)
                            self.master_tuple_list.append(row)
        ###
        ### END OF get_constraint_summary() ###

    def build_tract_lp(self,state_abbr, county, tract, sf1_tract_data, sf1_block_data):
        t0         = time.time()
        state_code = dbrecon.state_fips(state_abbr)
        geo_id     = sf1_tract_data[0][GEOID]
        lpdir      = LPDIR(state_abbr=state_abbr,county=county)
        lpfilename = LPFILENAME(state_abbr=state_abbr,county=county,geo_id=geo_id)
        logging.info(f"{state_code}{county}{tract} tract_data_size:{sys.getsizeof(sf1_tract_data):,} ; "
                     "block_data_size:{sys.getsizeof(sf1_block_data):,} ")

        if args.dry_run:
            print(f"DRY RUN: Will not create {lpfilename}")
            return

        if args.mem:
            tf = tempfile.NamedTemporaryFile(delete=False)
            lpfilename_hold = lpfilename
            lpfilename = tf.name
            print(f"MEMORY COUNTING. Will not create {lpfilename}. Tempfile written to {tf.name}")

        # assure that the directory exists
        dmakedirs(lpdir)  

        # If the LP files for this state/county/tract already exist, and they are properly terminated, just return

        if dpath_exists(lpfilename) and not args.mem:
            if lpfile_properly_terminated(lpfilename):
                logging.info(f"{state_abbr} {county} {tract}: {lpfilename} already exists")
                return
            logging.info(f"{state_abbr} {county} {tract}: {lpfilename} exists but not properly terminated. Deleting.")
            dpath_unlink(lpfilename)

        #
        # Create the output LP file and write header
        #
        f = dopen(lpfilename,'w')
        f.write("\* DB Recon *\ \n")
        f.write("Minimize \n")
        f.write("Arbitrary_Objective_Function: __dummy \n")
        f.write("Subject To \n")

        # Block constraint building
        # loop through blocks to get block constraints and the master tuple list

        # TODO - Move update_p01 inside get_constraint_summary function.
        # Pass in sf1_block_dict and sf1 tract dict
        #
        # Get the constraints from the block dict for all the blocks in the tract
        block_summary_nums = {}
        for block in sf1_block_data:
            self.get_constraint_summary('block', sf1_block_data, sf1_block_data[block], block_summary_nums)
        logging.info(f"{state_abbr} {county} {tract}: done getting block summary constraints")

        # Initial constraint number counter
        n_con  = 1                  
        # Loop through the block constraints and write them to the file
        n_con = update_constraints(f, 'block', n_con, block_summary_nums,geo_id,state_code,county,state_abbr)

        # loop through blocks in the tract to get block constraints and the master tuple list
        if args.mem:
            print(f"block_summary_nums: {total_size(block_summary_nums):,}")

        del block_summary_nums

        tract_summary_nums = {}
        self.get_constraint_summary('tract', sf1_tract_data, sf1_tract_data, tract_summary_nums)
        logging.info(f"{state_abbr} {county} {tract}: done with tract summary")

        # for tracts, need to add the master_tuple_list just once
        for i in self.master_tuple_list: 
            tract_summary_nums[geo_id]['tuple_list'].append(i)

        # Loop through the tract constraints to write to file.
        n_con = update_constraints(f, 'tract', n_con, tract_summary_nums,geo_id,state_code,county,state_abbr,)
        if args.mem:
            print(f"tract_summary_nums: {total_size(tract_summary_nums):,}")
            print(f"master_tuple_list: {total_size(self.master_tuple_list):,}")
        del tract_summary_nums

        # Write the collected variable names to the file, since they are all binaries
        f.write("Bounds\n  __dummy = 0 \n Binaries \n")
        for t in self.master_tuple_list:
            f.write(t[10])
            f.write('\n')
        f.write(' End')
        f.close()

        if args.mem:
            if dpath_exists(lpfilename):
                print(f"Comparing {lpfilename} and {lpfilename_hold}")
                subprocess.check_call(['cmp',dbrecon.dpath_expand(lpfilename),dbrecon.dpath_expand(lpfilename_hold)])
            print("memory round completed. File validates")
            print("Elapsed seconds: {}".format(int(time.time()-t0)))
            dbrecon.print_maxrss()
            dbrecon.add_dfxml_tag('synth_lp_files','', {'success':1})
            exit(0)


# Make the tract LP files. This cannot be a local functions
def build_tract_lp_tuple(tracttuple):
    (state_abbr, county, tract, sf1_tract_data, sf1_block_data) = tracttuple
    
    lptb = LPTractBuilder()
    lptb.build_tract_lp(state_abbr, county, tract, sf1_tract_data, sf1_block_data)

"""Support for multi-threading. tracttuple contains the state_abbr, county, tract, and sf1_tract_dict"""
def make_state_county_files(state_abbr, county, tractgen='all'):
    """
    Reads the data files for the state and county, then call build_tract_lp to build the LP files for each tract.
    All of the LP files are built from the same data model. This can be done in parallel.
    """
    assert state_abbr[0].isalpha()
    assert county[0].isdigit()
    logging.info(f"make_state_county_files({state_abbr},{county},{tractgen})")

    state_code = dbrecon.state_fips(state_abbr)

    ### Has the variables and the collapsing values we want (e.g, to collapse race, etc)
    ### These data frames are all quite small
    sf1_vars       = pd.read_csv(dopen(SF1_RACE_BINARIES), quoting=2)
    make_attributes_categories(sf1_vars)

    sf1_vars_block = sf1_vars[(sf1_vars['level']=='block')]
    sf1_vars_tract = sf1_vars[(sf1_vars['level']=='tract')]

    ### Read the actual data -- reformatted sf1.
    ### These files are not that large

    try:
        sf1_block_reader = csv.DictReader(dopen(SF1_BLOCK_DATA_FILE(state_abbr=state_abbr,county=county),'r'))
        sf1_tract_reader = csv.DictReader(dopen(SF1_TRACT_DATA_FILE(state_abbr=state_abbr,county=county),'r'))
    except FileNotFoundError as e:
        print(e)
        logging.error(f"ERROR. NO BLOCK DATA FILE for {state_abbr} {county} ")
        return

    ## make sf1_block_list, looks like this:
    ##                   geoid  tablevar  value
    ## 0       020130001001363  P0010001   24.0
    ## 1       020130001001363  P0020001   24.0
    ## ...                 ...       ...    ...
    ## 121903  020130001003156  P039I019    0.0
    ## 121904  020130001003156  P039I020    0.0
    ##       
    ## This is the cartesian product of all of the blocks and all of
    ## the tablevars in the tables that cover these blocks.  'value'
    ## is the value for that variable for that geoid, as read from the
    ## SF1 files.
    ##
    ## This table is large because the geoids are strings (80 bytes)
    ## instead of integers (which would require encoding the leading
    ## 0), and because the tablevars are strings (80 bytes). But it's
    ## not that large, since the records are by blocks.  In the 2010
    ## Census geography file, the tract with the most blocks is Idaho
    ## 015, which has 3449.  The county with the most blocks is
    ## California 37, which has 109582.
    ##
    ## TODO: Improve this by turning the geoids and tablevars into categories.
    ##
    logging.info("building sf1_block_list for %s %s",state_abbr,county)
    sf1_block_list=[]
    for s in sf1_block_reader:
        temp_list=[]
        if s['STATE'][:1].isdigit() and int(s['P0010001'])>0:
            geo_id=str(s['STATE'])+str(s['COUNTY']).zfill(3)+str(s['TRACT']).zfill(6)+str(s['BLOCK'])
            for k,v in list(s.items()):
                if k[:1]=='P' and geo_id[:1]!='S' and v.strip()!='': 
                    sf1_block_list.append([geo_id,k,float(v)])

    sf1_block     = pd.DataFrame.from_records(sf1_block_list, columns=[GEOID,TABLEVAR,'value'])
    make_attributes_categories(sf1_block)

    sf1_block_all = pd.merge(sf1_block, sf1_vars_block, how='inner', left_on=[TABLEVAR], right_on=[CELL_NUMBER])
    sf1_block_all['value'].fillna(0)

    ## make sf1_block_dict.
    ## This is a dictionary of dictionaries of lists where:
    ## sf1_block_dict[tract][block] = list of sf1_block rows from the SF1 data that match each block

    logging.info("collecting tract and block data for %s %s",state_abbr,county)
    sf1_block_records = sf1_block_all.to_dict(orient='records')
    sf1_block_dict = {}
    for d in sf1_block_records:
        tract=d[GEOID][5:11]  # tracts are six digits
        block=d[GEOID][11:15] # blocks are 4 digits (the first digit is the block group)
        if tract not in sf1_block_dict:
            sf1_block_dict[tract]={}
        if block not in sf1_block_dict[tract]:
            sf1_block_dict[tract][block]=[]
        sf1_block_dict[tract][block].append(d)

    ## To clean up, delete all of the temporary dataframes
    del sf1_block,sf1_block_all,sf1_block_records,tract,block
    gc.collect()

    ## make sf1_tract_dict.
    ## This is a dictionary of lists where
    ## sf1_block_dict[tract] = list of sf1_tract rows from the SF1 data that match each tract

    logging.info("getting tract data for %s %s",state_abbr,county)
    sf1_tract_list=[]
    error_count = 0
    for s in sf1_tract_reader:
        if s['STATE'][:1].isdigit() and int(s['P0010001'])>0:
            geo_id=str(s['STATE'])+str(s['COUNTY']).zfill(3)+str(s['TRACT']).zfill(6)
            for k,v in list(s.items()):
                if k[:3]=='PCT' and geo_id[:1]!='S':
                    try:
                        sf1_tract_list.append([geo_id,k,float(v)])
                    except ValueError as e:
                        logging.error(f"state:{state_abbr} county:{county} geo_id:{geo_id} k:{k} v:{v}")
                        error_count += 1
                        if error_count>MAX_SF1_ERRORS:
                            return

    sf1_tract = pd.DataFrame.from_records(sf1_tract_list, columns=[GEOID,TABLEVAR,'value'])
    make_attributes_categories(sf1_tract)

    # merge data with var definitions
    sf1_tract_all = pd.merge(sf1_tract, sf1_vars_tract, how='inner', left_on=[TABLEVAR], right_on=[CELL_NUMBER])
    sf1_tract_all['value'].fillna(0)

    sf1_tract_records = sf1_tract_all.to_dict(orient='records')
    del sf1_tract_all
    gc.collect()

    sf1_tract_dict=defaultdict(list)
    for d in sf1_tract_records:
        tract=d[GEOID][5:]
        sf1_tract_dict[tract].append(d)
    logging.info("%s %s total_size(sf1_block_dict)=%s total_size(sf1_tract_dict)=%s",
                 state_abbr,county,total_size(sf1_block_dict),total_size(sf1_tract_dict))
    if args.mem:
        print("sf1_block_dict total memory: {:,} bytes".format(total_size(sf1_block_dict)))
        print("sf1_tract_dict has data for {} tracts.".format(len(sf1_tract_dict)))
        print("sf1_tract_dict total memory: {:,} bytes".format(total_size(sf1_tract_dict)))
    
    ################################################################
    ### 
    ### We have now made the data for this county.
    ### We now make LP files for a specific set of tracts, or all the tracts.

    if tractgen!='all':
        tracts = [tractgen]
        logging.info(f"Only processing tract {tractgen}")
    else:
        tracts = sf1_tract_dict.keys()
        logging.info(f"Number of tracts in {state_abbr} {county}: {len(tracts)}")

    tracttuples = [(state_abbr, county, tract, sf1_tract_dict[tract], sf1_block_dict[tract]) for tract in tracts]

    if args.j2>1:
        with multiprocessing.Pool(args.j2) as p:
            p.map(build_tract_lp_tuple, tracttuples)
    else:
        list(map(build_tract_lp_tuple, tracttuples))

if __name__=="__main__":
    from argparse import ArgumentParser,ArgumentDefaultsHelpFormatter
    parser = ArgumentParser( formatter_class = ArgumentDefaultsHelpFormatter,
                             description="Synthesize LP files for all of the tracts in the given state and county." )
    dbrecon.argparse_add_logging(parser)
    parser.add_argument("--config", help="config file", default='config.ini')
    parser.add_argument("--j1", 
                        help="Specifies number of threads for state-county parallelism. "
                        "These threads do not share memory. Specify 1 to disable parallelism.",
                        type=int,default=4)
    parser.add_argument("--j2",
                        help="Specifies number of threads for tract-level parallelism. "
                        "These threads share tract and block statistics. Specify 1 to disable parallelism.",
                        type=int,default=16)
    parser.add_argument("--dry_run", help="don't actually write out the LP files",action='store_true')
    parser.add_argument("--mem",
                        help="enable memory debugging. Print memory usage. "
                        "Write output to temp file and compare with correct file.", action='store_true')

    parser.add_argument("state", help="2-character state abbreviation; all for all. Multiple states may be separated by commas.")
    parser.add_argument("county", help="3-digit county code; specify next for next; all for all. Multiple counties may be separated by commas")
    parser.add_argument("tract", help="Just synthesize for this specific 4-digit tract code",nargs="?")
    
    args     = parser.parse_args()
    config   = dbrecon.setup_logging_and_get_config(args,prefix="03syn")
    

    if args.mem:
        print("Memory debugging mode. Setting j1=1 and j2=1")
        args.j1 = 1
        args.j2 = 1

    if args.state=='all':
        state_abbrs = dbrecon.all_state_abbrs()
    else:
        state_abbrs = dbrecon.parse_state_abbrs(args.state)

    if len(state_abbrs)>1 and args.county!='all':
        print("if more than one state_abbr is specified, then county must be all",file=sys.stderr)
        exit(1)
    
    # If we are doing a specific tract
    if args.tract:
        if len(state_abbrs)!=1:
            logging.error("Can only specify a single, specific state if a tract is specified.")
            exit(1)
        if args.county=='all':
            logging.error("May not specify all county codes if you are specifying a tract")
            exit(1)
        make_state_county_files(state_abbrs[0], args.county, args.tract)
        exit(0)

    # If we are doing multiple states, spin off a different thread for each state/county code combination.
    # This lets us get multiprocessing here and in the per-tract multiprocessing
    if args.county=='all':
        def recall(pair):
            from subprocess import check_call
            (state_abbr,county) = pair
            cmd = [sys.executable,__file__,'--config',args.config,state_abbr,county,'all','--j2',str(args.j2)]
            if args.dry_run:
                cmd.append("--dry_run")
            if args.stdout:
                cmd.append("--stdout")
            logging.info(" ".join(cmd))
            check_call(cmd)

        state_abbr_county_pairs = []
        for state_abbr in state_abbrs:
            state_abbr_county_pairs.extend([(state_abbr,county) 
                                            for county in dbrecon.counties_for_state(state_abbr)])
        with multiprocessing.Pool(args.j1) as p:
            p.map(recall, state_abbr_county_pairs)
        exit(0)

    # We are doing a single state/county pair. We may do each tract multithreaded.
    assert args.county!='all'
    make_state_county_files(state_abbrs[0], args.county)
    print(f"Logfile: {logfname}")

