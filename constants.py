import os

"""This file describes the naming convention for the 2000 and the 2010 decennial censuses.
This file concerns the data products PL94, SF1 and SF2.
The data products were distributed as sets of files per state.
  - state-names are used on the WWW server
  - state-abbreviations are used on both the WWW server and within the files themselves.
Each year/product/state consists of:
  - A geoheader file, which contains all of the tabulation geographies for the year.
  - Two or more table files, each of which contains one or more tables.

The first 5 columns of each file are linkage variables, for linking the tables to the geoheader.

Unfortunately, naming schemes were not consistent within 2000 and were changed from 2000 to 2010.
This file attempts to provide a simple interface for downloading, unpacking, and processing all of
the files. 

The documentation is internally inconsitent, in that sometimes the
multiple files for each state are called "segments" and sometimes they
are called "files". 

We try to consistently use the term:
  - "file_number" to describe the numbers that go from 1..N. 
  - segment to describe the name "geo" and the zero-filed representation of the file_number, 
    which seems to be numbers 00000 through {N:05d}
"""

ROOT_DIR = os.path.dirname(__file__)
DOC_DIR  = os.path.join(ROOT_DIR, "doc")

# years
YEAR = 'year'
YEARS = [2000,2010]

# products. Note that it is called the PL94 in places and te 
PRODUCT = 'product'
PL94 = 'pl94'
SF1  = 'sf1'
SF2  = 'sf2'
AIAN = 'aian'
PRODUCTS = [PL94, SF1, SF2, AIAN]

PRODUCT_EXTS = {2010: { PL94:'pl',
                        SF1:'sf1',
                        SF2:'sf2' }}
                    
# Number of files per data product
FILES_FOR_YEAR_PRODUCT = {2000: {PL94: 2,
                                 SF1 : 39},
                          2010: {PL94: 2,
                                 SF1 : 47} }

MAX_CIFSN = 47                # highest anywhere

# For self-check, each year/product has a prefix at the beginning of each line
FILE_LINE_PREFIXES = {2000 : {SF1: "uSF1,"},
                      2010 : {SF1: "SF1ST"}}

# This is chapter6 exported as a CSV using Adobe Acrobat
# Chapter 6 is the data dictionary. In some cases, we have just it

SPEC_CSV_FILES     = DOC_DIR + "/{year}/{product}.csv"
CHAPTER6_CSV_FILES = DOC_DIR + "/{year}/{product}_chapter6.csv"



#
# States. Note that for consistency, we use the phrase 'state' to refer to a 2-letter code
# and the phrase 'state_name' to refer to the spelled out, capitalized state name.
#
STATE = 'state'
STATE_DB="""Alaska/ak Arizona/az Arkansas/ar California/ca Colorado/co Connecticut/ct Delaware/de
District_of_Columbia/dc Alabama/al Florida/fl Georgia/ga Hawaii/hi Idaho/id Illinois/il Indiana/in
Iowa/ia Kansas/ks Kentucky/ky Louisiana/la Maine/me Maryland/md Massachusetts/ma Michigan/mi
Minnesota/mn Mississippi/ms Missouri/mo Montana/mt Nebraska/ne Nevada/nv New_Hampshire/nh
New_Jersey/nj New_Mexico/nm New_York/ny North_Carolina/nc North_Dakota/nd Ohio/oh Oklahoma/ok
Oregon/or Pennsylvania/pa Rhode_Island/ri South_Carolina/sc South_Dakota/sd Tennessee/tn
Texas/tx Utah/ut Vermont/vt Virginia/va Washington/wa West_Virginia/wv Wisconsin/wi Wyoming/wy"""

STATES_AND_ABBREVS = STATE_DB.split()
STATES             = [saa.split("/")[1] for saa in STATES_AND_ABBREVS]

# map states to state_names:
STATE_NAMES        = {saa.split("/")[1]:saa.split("/")[0] for saa in STATES_AND_ABBREVS}

SEGMENT_FORMAT="{segment_number:05d}"
GEO="geo"
GEO_TABLE='geo'

FILENAME_2000_SF2 = "{state}{characteristic_iteration}{file_number}_uf2.zip"
"""
Naming convention for SF2 data files is ssiiiyy_uf2.zip. 
iii is the characteristic iteration (total population, race groups, American Indian and Alaska 
Native tribes, and Hispanic/Latino groups)
Characteristic iteration codes are in the Appendix H of the technical documentation, 
which is available at http://www.census.gov/prod/cen2000/docs/sf2.pdf - page=278.	
yy is the number of the file
   Valid codes are 01 through 04.  See below for distribution of tables across files.
"""

# Download URLS.
# Key differences between 2000 and 2010:
# - Different URL formats
# - In 2000, each ZIP file contains a single segment
# - In 2010, each ZIP file contains *all* of the state's segments.

WWW_SERVER_2000 = "https://www2.census.gov/census_2000/datasets/"
URL_2000_PL94   = WWW_SERVER_2000 + "redistricting_file--pl_94-171/{state_name}/{state}{segment}.upl.zip"
URL_2000_SF1    = WWW_SERVER_2000 + "Summary_File_1/{state_name}/{state}{segment}_uf1.zip"
URL_2000_SF2    = WWW_SERVER_2000 + "Summary_File_2/{state_name}/{state}{segment}_uf2.zip"
                      
WWW_SERVER_2010='https://www2.census.gov/census_2010'
URL_2010_PL94 = WWW_SERVER_2010+'/01-Redistricting_File--PL_94-171/{state_name}/{state}2010.pl.zip'
URL_2010_SF1  = WWW_SERVER_2010+'/04-Summary_File_1/{state_name}/{state}2010.sf1.zip'
URL_2010_SF2  = WWW_SERVER_2010+'/05-Summary_File_2/{state_name}/{state}2010.sf2.zip'

ONE_SEGMENT_PER_ZIPFILE = {2000:True, 2010:False}

SEGMENTS_PER_PRODUCT = {2000: {PL94: 3,
                               SF1 : 40},
                        2010: {PL94: 3,
                               SF1 : 48}}



# SEGMENTS_PER_PRODUCT includes the 'geo' segment, so add 1 to the largest segment number
DOWNLOAD_SEGMENTS_PER_PRODUCT = {2000: {PL94: 3,
                                        SF1 : 40},
                                 2010: {PL94: 1,
                                        SF1 : 1}}


                        

DOWNLOAD_URLS = {2000:{PL94 : URL_2000_PL94,
                       SF1  : URL_2000_SF1,
                       SF2  : URL_2000_SF2},
                 2010:{PL94 : URL_2010_PL94,
                       SF1  : URL_2010_SF1,
                       SF2  : URL_2010_SF2 } } 
                 
# Specifies directory where a zip file is downloaded. The filename is kept from the original download URL
DEST_ZIPFILE_DIR    = {2000:ROOT_DIR+'/data/{year}_{product}/dist/{state}',
                       2010:ROOT_DIR+'/data/{year}_{product}/dist'}

# linkage variables
FILEID='FILEID'
STUSAB='STUSAB'
CHARITER='CHARITER'
CIFSN='CIFSN'
LOGRECNO='LOGRECNO'
LINKAGE_VARIABLES = [FILEID, STUSAB, CHARITER, CIFSN, LOGRECNO]

# We use the CIFSN 0 for the geo segment
CIFSN_GEO=0

class YPSS:
    __slots__=('year','product','state','segment','chariter')
    def __init__(self,year,product,state,segment,chariter=0):
        assert year in YEARS
        assert product in PRODUCTS
        assert state in STATES
        self.year     = year
        self.product  = product
        self.state    = state
        if type(segment)==str:
            self.segment = segment
        elif type(segment)==int:
            self.segment = "{:02d}".format(segment)
        else:
            raise ValueError("unknown type: {}".format(type(segment)))
        if type(segment)==str:
            self.chariter = chariter
        elif type(chariter)==int:
            self.chariter = "{:03d}".format(chariter)
        else:
            raise ValueError("unknown type: {}".format(type(segment)))
    def __repr__(self):
        return f"YPSS<{self.year}:{self.product}:{self.state}:{self.chariter}:{self.segment}>"
        
        
def download_url(ypss):
    return DOWNLOAD_URLS[ypss.year][ypss.product].format(year=ypss.year,product=ypss.product,
                                                         state_name = STATE_NAMES[ypss.state],
                                                         state=ypss.state,
                                                         chariter=ypss.chariter,
                                                         segment=ypss.segment)
                                                         
def zipfile_dir(ypss):
    return DEST_ZIPFILE_DIR[ypss.year].format(year=ypss.year,
                                              product=ypss.product,
                                              state=ypss.state,
                                              chariter=ypss.chariter,
                                              segment=ypss.segment)

def zipfile_name(ypss):
    return os.path.join( zipfile_dir(ypss), os.path.basename( download_url( ypss )))

def segmentfile_name(ypss):
    """The name within the zipfile of the requested segment"""
    ext = PRODUCT_EXTS[ypss.year][ypss.product]
    return "{state:2}{chariter:03}{segment:02}{year:04}.{ext}".format(
        state=ypss.state,
        chariter=int(ypss.chariter),
        segment=int(ypss.segment),
        year=int(ypss.year),
        ext = ext)

