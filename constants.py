import os

ROOT_DIR = os.path.dirname(__file__)
DOC_DIR  = os.path.join(ROOT_DIR, "doc")
MAX_SEGMENT = 47                # segment numbers go 1..MAX_SEGMENT

WWW_SERVER='http://www2.census.gov/census_2010'

DOWNLOAD_URLS = {'pl94':WWW_SERVER+'/01-Redistricting_File--PL_94-171/{state_name}/{state}2010.pl.zip',
                 'sf1' :WWW_SERVER+'/04-Summary_File_1/{state_name}/{state}2010.sf1.zip',
                 'sf2' :WWW_SERVER+'/05-Summary_File_2/{state_name}/{state}2010.sf2.zip'}

PL94_ZIPFILE_NAME    = os.path.join(ROOT_DIR,'pl94/dist/{state}2010.pl.zip')
SF1_ZIPFILE_NAME    = os.path.join(ROOT_DIR,'sf1/dist/{state}2010.sf1.zip')
SF2_ZIPFILE_NAME    = os.path.join(ROOT_DIR,'sf2/dist/{state}2010.sf2.zip')

SF1_GEO_PREFIX="SF1ST "
SF1_DATA_PREFIX="SF1ST,"

# This is chapter6 exported as a CSV using Adobe Acrobat
# Chapter 6 is the data dictionary

PL94_CHAPTER6_CSV = DOC_DIR + "/" + "pl94_chapter6.csv"
SF1_CHAPTER6_CSV = DOC_DIR + "/" + "sf1_chapter6.csv"
SF2_CHAPTER6_CSV = DOC_DIR + "/" + "sf2_chapter6.csv"

STATE_DB="""Alaska/ak
Arizona/az
Arkansas/ar
California/ca
Colorado/co
Connecticut/ct
Delaware/de
District_of_Columbia/dc
Alabama/al
Florida/fl
Georgia/ga
Hawaii/hi
Idaho/id
Illinois/il
Indiana/in
Iowa/ia
Kansas/ks
Kentucky/ky
Louisiana/la
Maine/me
Maryland/md
Massachusetts/ma
Michigan/mi
Minnesota/mn
Mississippi/ms
Missouri/mo
Montana/mt
Nebraska/ne
Nevada/nv
New_Hampshire/nh
New_Jersey/nj
New_Mexico/nm
New_York/ny
North_Carolina/nc
North_Dakota/nd
Ohio/oh
Oklahoma/ok
Oregon/or
Pennsylvania/pa
Rhode_Island/ri
South_Carolina/sc
South_Dakota/sd
Tennessee/tn
Texas/tx
Utah/ut
Vermont/vt
Virginia/va
Washington/wa
West_Virginia/wv
Wisconsin/wi
Wyoming/wy"""


