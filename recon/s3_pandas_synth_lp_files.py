#!/usr/bin/env python3
#
"""
Read the processed SF1 dat and syntheize the LP file that will be input to the optimizer.
This is currently done with pandas and by buffering much in memory, both of which are quite memory intensive.

I tried to simplify this, but I was never able to figure out what it was actually doing.
"""

from collections import defaultdict
import xml.etree.ElementTree as ET
import math
import csv
import gc
import itertools
import json
import logging
import multiprocessing
import os
import os.path
import pandas as pd
import sys
import time
import tempfile
import subprocess
import atexit

import dbrecon

from total_size import total_size
from dbrecon import DB,GB,MB
from dbrecon import lpfile_properly_terminated,LPFILENAMEGZ,dopen,dpath_expand,dmakedirs,LPDIR,dpath_exists,dpath_unlink,mem_info,dgetsize,remove_lpfile,REIDENT
from ctools.dbfile import DBMySQL,DBMySQLAuth

assert pd.__version__ > '0.19'

MAX_SF1_ERRORS = 10             # some files may have errors
MISSING  = 'missing'
HISPANIC = 'hispanic'
DEFAULT_J1 = 1
DEFAULT_J2 = 8

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

def update_constraints(f, level, n_con, summary_nums, geo_id):
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
    if args.debug:
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
    if args.debug:
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

    def __init__(self,stusab, county, tract, sf1_tract_data, sf1_block_data):
        self.master_tuple_list=[]
        self.stusab = stusab
        self.county     = county
        self.tract      = tract
        self.sf1_tract_data = sf1_tract_data
        self.sf1_block_data = sf1_block_data
        self.auth       = dbrecon.auth()

    def db_fail(self):
        # remove from the database that we started. This is used to clean up the database if the program terminates improperly
        if not args.debug:
            DBMySQL.csfr(self.auth,
                         f"UPDATE {REIDENT}tracts SET lp_start=NULL where stusab=%s and county=%s and tract=%s",
                         (self.stusab,self.county,self.tract),rowcount=1)

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
        if args.debug:
            logging.info("get_constraint_summary  level: {} p01_data: {:,}B "
                         "data_dict: {:,}B summary_nums: {:,}B".
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

                    # This is where the variables are created!

                    if level=='block':
                        for i in s_tuple_list:
                            row = i + ['C_'+'_'.join(map(str, i))] + [s[GEOID]]
                            summary_nums[s[GEOID]]['tuple_list'].append(row)
                            self.master_tuple_list.append(row)
        ###
        ### END OF get_constraint_summary() ###
        ###

    def build_tract_lp(self):
        """Main entry point for building a new tract LP file.
        Modified to write gzipped LP files because the LP files are so large
        """

        state_code    = dbrecon.state_fips(self.stusab)
        geo_id        = self.sf1_tract_data[0][GEOID]
        lpfilenamegz  = LPFILENAMEGZ(stusab=self.stusab,county=self.county,tract=self.tract)
        use_s3        = lpfilenamegz.startswith("s3://")
        tmpgzfilename = lpfilenamegz.replace(".gz",".tmp.gz")
        if args.output:
            outfilename = args.output
        else:
            outfilename   = tmpgzfilename
            lpfileexists  = dbrecon.dpath_exists(lpfilenamegz)

            if dbrecon.is_db_done('lp',self.stusab, self.county, self.tract):
                logging.warning(f"note: LP file exists in database: {self.stusab}{self.county}{self.tract}  exists in file system: {lpfileexists}; "
                                "will not create another one.")
                return
            lpdir      = LPDIR(stusab=self.stusab,county=self.county)
            dmakedirs(lpdir)

            # file exists and it is good. Note that in the database
            try:
                if dbrecon.lpfile_properly_terminated(lpfilenamegz):
                    logging.info(f"{lpfilenamegz} at {state_code}{self.county}{self.tract} is properly terminated.")
                    dbrecon.db_done('lp',self.stusab, self.county, self.tract)
                    return
            except FileNotFoundError as e:
                # Intentional fall through
                pass


        t0         = time.time()
        logging.info(f"{state_code}{self.county}{self.tract} tract_data_size:{sys.getsizeof(self.sf1_tract_data):,} ; "
                     "block_data_size:{sys.getsizeof(self.sf1_block_data):,} ")

        if not args.debug:
            dbrecon.db_start('lp', self.stusab, self.county, self.tract)
            atexit.register(self.db_fail)

        if args.dry_run:
            logging.warning(f"DRY RUN: Will not create {outfilename}")
            return

        # Block constraint building
        # loop through blocks to get block constraints and the master tuple list

        # TODO - Move update_p01 inside get_constraint_summary function.
        # Pass in sf1_block_dict and sf1 tract dict
        #
        # Get the constraints from the block dict for all the blocks in the tract
        block_summary_nums = {}
        for block in self.sf1_block_data:
            self.get_constraint_summary('block', self.sf1_block_data, self.sf1_block_data[block],
                                        block_summary_nums)
        logging.info(f"{self.stusab} {self.county} {self.tract}: done getting block summary constraints")

        #
        # Create the output LP file and write header
        #
        f = dopen(outfilename,'w')
        f.write("\* DB Recon *\ \n")
        f.write("Minimize \n")
        f.write("Arbitrary_Objective_Function: __dummy \n")
        f.write("Subject To \n")

        # Loop through the block constraints and write them to the file
        n_con = 1 # initial connection
        n_con = update_constraints(f, 'block', n_con, block_summary_nums,geo_id)

        # loop through blocks in the tract to get block constraints and the master tuple list
        logging.info(f"block_summary_nums: {total_size(block_summary_nums):,}")
        if args.debug:
            logging.warning(f"block_summary_nums: {total_size(block_summary_nums):,}")

        del block_summary_nums

        tract_summary_nums = {}
        self.get_constraint_summary('tract', self.sf1_tract_data, self.sf1_tract_data, tract_summary_nums)
        logging.info(f"{self.stusab} {self.county} {self.tract}: done with tract summary")

        # for tracts, need to add the master_tuple_list just once
        for i in self.master_tuple_list:
            tract_summary_nums[geo_id]['tuple_list'].append(i)

        # Loop through the tract constraints to write to file.
        n_con = update_constraints(f, 'tract', n_con, tract_summary_nums,geo_id)
        logging.info(f"tract_summary_nums: {total_size(tract_summary_nums):,}")
        logging.info(f"master_tuple_list: {total_size(self.master_tuple_list):,}")
        if args.debug:
            logging.info(f"tract_summary_nums: {total_size(tract_summary_nums):,}")
            logging.info(f"master_tuple_list: {total_size(self.master_tuple_list):,}")
        del tract_summary_nums

        # Write the collected variable names to the file, since they are all binaries
        f.write("Bounds\n  __dummy = 0 \n Binaries \n")
        for t in self.master_tuple_list:
            f.write(t[10])
            f.write('\n')
        f.write('End\n')
        f.close()
        if not args.debug:
            dbrecon.db_done('lp',self.stusab, self.county, self.tract)
            DBMySQL.csfr(self.auth,
                         f"UPDATE {REIDENT}tracts SET lp_gb=%s,hostlock=NULL WHERE stusab=%s AND county=%s AND tract=%s",
                         (dbrecon.maxrss()//GB,self.stusab, self.county, self.tract), rowcount=1)
            atexit.unregister(self.db_fail)

        if args.debug:
            logging.info("debug completed.")
            logging.info("Elapsed seconds: {}".format(int(time.time()-t0)))
            dbrecon.print_maxrss()
            dbrecon.add_dfxml_tag('synth_lp_files','', {'success':'1'})
            exit(0)

        # Rename the temp file to the gzfile
        # If running on S3, make sure the object exists
        dbrecon.dwait_exists(outfilename)
        dbrecon.drename(outfilename, lpfilenamegz)
        # And wait for the lpfilenamegz to exist
        try:
            dbrecon.dwait_exists(lpfilenamegz)
        except RuntimeError as e:
            print(e)
            logging.warning("Will not fix database. Let s4_ discover the lp file isn't there.")


# Make the tract LP files.
#
# This cannot be a local functions because it is called from the
# multiprocessing map, and the multiprocessing system can't call local
# functions.
#
def build_tract_lp_tuple(tracttuple):
    (stusab, county, tract, sf1_tract_data, sf1_block_data) = tracttuple

    try:
        lptb = LPTractBuilder(stusab, county, tract, sf1_tract_data, sf1_block_data)
        lptb.build_tract_lp()
    except MemoryError as e:
        if not args.debug:
            print("MEMORY ERROR!!!")
            print(e)
            cmd = f"""
            UPDATE {REIDENT}tracts SET hostlock=NULL,lp_start=NULL,lp_end=NULL
            WHERE stusab=%s and county=%s and tract=%s
            """
            print(cmd)
            auth = DBMySQLAuth.FromConfig(os.environ)
            DBMySQL.csfr(auth,cmd, (stusab, county, tract), debug=1)
        logging.error(f"MEMORY ERROR in {stusab} {county} {tract}: {e}")

"""Support for multi-threading. tracttuple contains the stusab, county, tract, and sf1_tract_dict"""
def make_state_county_files(auth, stusab, county, tractgen='all'):
    """
    Reads the data files for the state and county, then call build_tract_lp to build the LP files for each tract.
    All of the tract LP files are built from the same data model, so they can be built in parallel with shared memory.
    Consults the database to see which files need to be rebuilt, and only builds those files.
    """
    assert (stusab[0].isalpha()) and (len(stusab)==2)
    assert (county[0].isdigit()) and (len(county)==3)
    logging.info(f"make_state_county_files({stusab},{county},{tractgen})")

    # Find the tracts in this county that do not yet have LP files
    if args.force:
        tracts = [tractgen]
    else:
        rows = DBMySQL.csfr(auth,
                            f"""
                            SELECT t.tract FROM {REIDENT}tracts t LEFT JOIN {REIDENT}geo g ON (t.stusab=g.stusab and t.county=g.county and t.tract=g.tract)
                            WHERE (t.stusab=%s) AND (t.county=%s) AND (t.lp_end IS NULL) AND (g.sumlev='140') AND (g.pop100>0)
                            """,(stusab,county))
        tracts_needing_lp_files = [row[0] for row in rows]
        logging.info("tracts_needing_lp_files: %s",tracts_needing_lp_files)
        if tractgen=='all':
            if len(tracts_needing_lp_files)==0:
                logging.warning(f"make_state_county_files({stusab},{county},{tractgen}) "
                                f"- No more tracts need LP files")
                return
            tracts = tracts_needing_lp_files
        else:
            if tractgen not in tracts_needing_lp_files:
                # Check to see if the tract file is large enough
                lpgz_filename = dbrecon.LPFILENAMEGZ(stusab=stusab,county=county,tract=tractgen)
                if dpath_exists(lpgz_filename) and dgetsize(lpgz_filename) < dbrecon.MIN_LP_SIZE:
                    logging.warning(f"{lpgz_filename} exists but is too small ({dgetsize(lpgz_filename)}); deleting")
                    remove_lpfile(stusab=stusab,county=county,tract=tractgen)
                else:
                    logging.warning(f"make_state_county_files({stusab},{county},{tractgen}) "
                                    f"- tract {tractgen} not in {tracts_needing_lp_files}")
                    return
            tracts = [tractgen]

    state_code = dbrecon.state_fips(stusab)

    ### Has the variables and the collapsing values we want (e.g, to collapse race, etc)
    ### These data frames are all quite small
    sf1_vars       = pd.read_csv(dopen(dbrecon.SF1_RACE_BINARIES), quoting=2)

    assert len(sf1_vars) > 0

    make_attributes_categories(sf1_vars)

    sf1_vars_block = sf1_vars[(sf1_vars['level']=='block')]
    sf1_vars_tract = sf1_vars[(sf1_vars['level']=='tract')]

    ### Read the actual data -- reformatted sf1.
    ### These files are not that large

    try:
        sf1_block_data_file = dpath_expand( dbrecon.SF1_BLOCK_DATA_FILE(stusab=stusab,county=county) )
        sf1_block_reader = csv.DictReader(dopen( sf1_block_data_file,'r'))
    except FileNotFoundError as e:
        print(e)
        logging.error(f"ERROR. NO BLOCK DATA FILE {sf1_block_data_file} for {stusab} {county} ")
        return

    try:
        sf1_tract_data_file = dpath_expand( dbrecon.SF1_TRACT_DATA_FILE(stusab=stusab,county=county) )
        sf1_tract_reader = csv.DictReader(dopen( sf1_tract_data_file,'r'))
    except FileNotFoundError as e:
        print(e)
        logging.error(f"ERROR. NO TRACT DATA FILE {sf1_tract_data_file} for {stusab} {county} ")
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
    logging.info("building sf1_block_list for %s %s",stusab,county)
    sf1_block_list = []
    for s in sf1_block_reader:
        temp_list = []
        if s['STATE'][:1].isdigit() and int(s['P0010001'])>0:
            geo_id=str(s['STATE'])+str(s['COUNTY']).zfill(3)+str(s['TRACT']).zfill(6)+str(s['BLOCK'])
            for k,v in list(s.items()):
                if k[:1]=='P' and geo_id[:1]!='S' and v.strip()!='':
                    sf1_block_list.append([geo_id,k,float(v)])

    assert len(sf1_block_list) > 0
    sf1_block     = pd.DataFrame.from_records(sf1_block_list, columns=[GEOID,TABLEVAR,'value'])
    assert len(sf1_block)>0

    make_attributes_categories(sf1_block)

    sf1_block_all = pd.merge(sf1_block, sf1_vars_block, how='inner',
                             left_on=[TABLEVAR], right_on=[CELL_NUMBER])

    #print(f"sf1_block:\n{sf1_block}")
    #print(f"sf1_vars_block:\n{sf1_vars_block}")
    #print(f"sf1_block_all:\n{sf1_block_all}")

    sf1_block_all['value'].fillna(0)

    ## make sf1_block_dict.
    ## This is a dictionary of dictionaries of lists where:
    ## sf1_block_dict[tract][block] = list of sf1_block rows from the SF1 data that match each block

    logging.info("collecting tract and block data for %s %s",stusab,county)
    sf1_block_records = sf1_block_all.to_dict(orient='records')
    assert len(sf1_block_records) > 0

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

    logging.info("getting tract data for %s %s",stusab,county)
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
                        logging.error(f"state:{stusab} county:{county} geo_id:{geo_id} k:{k} v:{v}")
                        error_count += 1
                        if error_count>MAX_SF1_ERRORS:
                            return

    sf1_tract = pd.DataFrame.from_records(sf1_tract_list, columns=[GEOID,TABLEVAR,'value'])
    make_attributes_categories(sf1_tract)

    # merge data with var definitions
    sf1_tract_all = pd.merge(sf1_tract, sf1_vars_tract, how='inner',
                             left_on=[TABLEVAR], right_on=[CELL_NUMBER])
    sf1_tract_all['value'].fillna(0)

    sf1_tract_records = sf1_tract_all.to_dict(orient='records')

    # Try to reclaim the memory
    del sf1_tract_all
    gc.collect()

    sf1_tract_dict=defaultdict(list)
    for d in sf1_tract_records:
        tract=d[GEOID][5:]
        sf1_tract_dict[tract].append(d)
    logging.info("%s %s total_size(sf1_block_dict)=%s total_size(sf1_tract_dict)=%s",
                 stusab,county,total_size(sf1_block_dict),total_size(sf1_tract_dict))
    if args.debug:
        logging.info("sf1_block_dict total memory: {:,} bytes".format(total_size(sf1_block_dict)))
        logging.info("sf1_tract_dict has data for {} tracts.".format(len(sf1_tract_dict)))
        logging.info("sf1_tract_dict total memory: {:,} bytes".format(total_size(sf1_tract_dict)))


    ################################################################
    ###
    ### We have now made the data for this county.
    ### We now make LP files for a specific set of tracts, or all the tracts.

    ### 2021-03-25 patch:
    ### Remove tracts not in the sf1_tract_dict and in the sf1_block_dict.
    ### This was a problem for the water tracts, although we now do not pull them into the 'tracts' list from the SQL.

    tracttuples = [(stusab, county, tract, sf1_tract_dict[tract], sf1_block_dict[tract])
                   for tract in tracts
                   if (tract in sf1_tract_dict) and (tract in sf1_block_dict)]

    if args.j2>1:
        with multiprocessing.Pool( args.j2 ) as p:
            p.map(build_tract_lp_tuple, tracttuples)
    else:
        list(map(build_tract_lp_tuple, tracttuples))

if __name__=="__main__":
    from argparse import ArgumentParser,ArgumentDefaultsHelpFormatter
    parser = ArgumentParser( formatter_class = ArgumentDefaultsHelpFormatter,
                             description="Synthesize LP files for all of the tracts in the given state and county." )
    dbrecon.argparse_add_logging(parser)
    parser.add_argument("--j1",
                        help="Specifies number of threads for state-county parallelism. "
                        "These threads do not share memory. Specify 1 to disable parallelism.",
                        type=int,default=DEFAULT_J1)
    parser.add_argument("--j2",
                        help="Specifies number of threads for tract-level parallelism. "
                        "These threads share tract and block statistics. Specify 1 to disable parallelism.",
                        type=int,default=DEFAULT_J2)
    parser.add_argument("--dry_run", help="don't actually write out the LP files",action='store_true')
    parser.add_argument("--debug", help="Run in debug mode. Do not update database and write output to file specified by --output",action='store_true')
    parser.add_argument("--output", help="Specify output file. Requires that a single state/county/tract be specified")
    parser.add_argument("--force", help="Generate all tract files, even if they exist", action='store_true')

    parser.add_argument("state",  help="2-character state abbreviation.")
    parser.add_argument("county", help="3-digit county code")
    parser.add_argument("tract",  help="If provided, just synthesize for this specific 6-digit tract code. Otherwise do all in the county",nargs="?")

    DB.quiet = True
    args     = parser.parse_args()
    config   = dbrecon.setup_logging_and_get_config(args=args,prefix="03pan")
    args.state = args.state.lower()

    assert dbrecon.dfxml_writer is not None

    if args.debug:
        root = logging.getLogger()
        root.setLevel(logging.DEBUG)
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        root.addHandler(handler)        
        logging.info("Info logging")
        logging.debug("Debug logging")

    if args.output or args.debug:
        logging.info("Memory debugging mode. Setting j1=1 and j2=1")
        args.j1 = 1
        args.j2 = 1

    auth = DBMySQLAuth.FromConfig(os.environ)

    # If we are doing a specific tract
    if args.tract:
        if not args.debug:
            dbrecon.db_lock(args.state, args.county, args.tract)
        make_state_county_files(auth, args.state, args.county, args.tract)

    else:
        # We are doing a single state/county pair. We may do each tract multithreaded. Lock the tracts...
        DBMySQL.csfr(auth,f"UPDATE {REIDENT}tracts set hostlock=%s,pid=%s where stusab=%s and county=%s and lp_end IS NULL",
                (dbrecon.hostname(),os.getpid(),args.state,args.county))
        make_state_county_files(auth, args.state, args.county)
