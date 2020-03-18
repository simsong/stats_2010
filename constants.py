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
  - "cifsn" to describe the numbers that go from 1..N. 
  - segment to describe the name "geo" and the zero-filed representation of the cifsn, 
    which seems to be numbers 00000 through {N:05d}
"""

ROOT_DIR = os.path.dirname(__file__)
DOC_DIR  = os.path.join(ROOT_DIR, "doc")

if not os.path.exists(DOC_DIR):
    raise FileNotFoundError(DOC_DIR)

# years
YEAR = 'year'
YEARS = [2000,2010]

# products. Note that it is called the PL94 in places and te 
PRODUCT = 'product'
PL94 = 'pl94'
SF1  = 'sf1'
SF2  = 'sf2'
SF3  = 'sf3'
SF4  = 'sf4'
RELATIONSHIP = 'relationship'
AIANSF = 'aiansf'
UR1  = 'ur1'
SEGMENT_FORMAT="{segment_number:05d}"
PRODUCTS = [PL94, SF1, SF2, SF3, SF4, AIANSF, UR1]

SUMLEV_TRACT = 140
SUMLEV_PL94_BLOCK = 750
SUMLEV_SF1_BLOCK = 101
SUMLEV_COUNTY = 50

PRODUCT_EXTS = { PL94:'pl',
                 SF1:'sf1',
                 SF2:'sf2',
                 SF3:'sf3',
                 SF4:'sf4',
                 UR1:'ur1' }
                    
# Number of files per data product
SEGMENTS_FOR_YEAR_PRODUCT = {2000:
                             {PL94: 2,
                              SF1 : 39,
                              SF2 : -1, 
                              SF3 : -1,
                              SF4 : -1,
                              AIANSF: -1 },
                             2010:
                             {PL94: 2,
                              SF1 : 47,
                              UR1 : 48,
                              SF2 : -1, 
                              AIANSF: -1 } }

MAX_CIFSN = 49                # highest anywhere

# For self-check, each year/product has a prefix at the beginning of each line
FILE_LINE_PREFIXES = {2000 : {PL94: "uPL",
                              SF1: "uSF1,"},
                      2010 : {PL94: "PLST",
                              SF1: "SF1ST",
                              SF2: "SF2ST",
                              AIANSF: "AIANSF",
                              UR1: "UR1" }}

# This is chapter6 exported as a CSV using Adobe Acrobat
# Chapter 6 is the data dictionary. In some cases, we have just it

GEO="geo"
GEO_TABLE='geo'
SPEC_CSV_FILE     = DOC_DIR + "/{year}/{product}_philManualEdits.csv"
CHAPTER6_CSV_FILE = DOC_DIR + "/{year}/{product}_chapter6.csv"
CHAPTER7_CSV_FILE = DOC_DIR + "/{year}/{product}_chapter7.csv"
SPEC_FILES = [SPEC_CSV_FILE,
              CHAPTER6_CSV_FILE,
              CHAPTER7_CSV_FILE]

#
# States. Note that for consistency, we use the phrase 'state' to refer to a 2-letter code
# and the phrase 'state_name' to refer to the spelled out, capitalized state name.
# Easy-to-read list at https://en.wikipedia.org/wiki/Federal_Information_Processing_Standard_state_code
# 
STATE = 'state'

# newstyle database; we need to transition to this.
STATE_DATA=[
    "Alabama,AL,01",
    "Alaska,AK,02",
    "Arizona,AZ,04",
    "Arkansas,AR,05",
    "California,CA,06",
    "Colorado,CO,08",
    "Connecticut,CT,09",
    "Delaware,DE,10",
    "District_of_Columbia,DC,11",
    "Florida,FL,12",
    "Georgia,GA,13",
    "Hawaii,HI,15",
    "Idaho,ID,16",
    "Illinois,IL,17",
    "Indiana,IN,18",
    "Iowa,IA,19",
    "Kansas,KS,20",
    "Kentucky,KY,21",
    "Louisiana,LA,22",
    "Maine,ME,23",
    "Maryland,MD,24",
    "Massachusetts,MA,25",
    "Michigan,MI,26",
    "Minnesota,MN,27",
    "Mississippi,MS,28",
    "Missouri,MO,29",
    "Montana,MT,30",
    "Nebraska,NE,31",
    "Nevada,NV,32",
    "New_Hampshire,NH,33",
    "New_Jersey,NJ,34",
    "New_Mexico,NM,35",
    "New_York,NY,36",
    "North_Carolina,NC,37",
    "North_Dakota,ND,38",
    "Ohio,OH,39",
    "Oklahoma,OK,40",
    "Oregon,OR,41",
    "Pennsylvania,PA,42",
    "Puerto_Rico,PR,72",        # note not 43!
    "Rhode_Island,RI,44",
    "South_Carolina,SC,45",
    "South_Dakota,SD,46",
    "Tennessee,TN,47",
    "Texas,TX,48",
    "Utah,UT,49",
    "Vermont,VT,50",
    "Virginia,VA,51",
    "Washington,WA,53",
    "West_Virginia,WV,54",
    "Wisconsin,WI,55",
    "Wyoming,WY,56" ]

"""
STATE_DICTS is a list of stat dictionaries, where each dict has the format:
{'state_name': 'Alabama', 'stusab': 'AL', 'state': '01'}
"""
STATE_DICTS=[dict(zip("state_name,stusab,state".split(","),line.split(","))) for line in STATE_DATA]

# Create some cuts through the data
STATE_NAMES             = [state['state_name'] for state in STATE_DICTS]



FILENAME_2000_SF2 = "{state}{characteristic_iteration}{cifsn}_uf2.zip"
"""
Naming convention for SF2 data files is ssiiiyy_uf2.zip. 
iii is the characteristic iteration (total population, race groups, American Indian and Alaska 
Native tribes, and Hispanic/Latino groups)
Characteristic iteration codes are in the Appendix H of the technical documentation, 
which is available at http://www.census.gov/prod/cen2000/docs/sf2.pdf - page=278.	
yy is the number of the file
   Valid codes are 01 through 04.  See below for distribution of tables across files.
"""

FIPS_PLACE_CLASS_CODE={
    "C1":"An active incorporated place that does not serve as a county subdivision equivalent",
    "C2":"An active incorporated place that is legally coextensive with a county subdivision but treated as independent of any county subdivision (an independent place)",
    "C5":"An active incorporated place that is independent of any county subdivision and serves as a county subdivision equivalent (an independent place)",
    "C6":"An active incorporated place that is partially independent of any county subdivision and partially dependent within a legal county subdivision (exists in Iowa and Ohio only)",
    "C7":"An incorporated place that is independent of any county (an independent city)",
    "C8":"The balance of a consolidated city excluding the separately incorporated place(s) within that consolidated government",
    "C9":"An inactive or nonfunctioning incorporated place",
    "M2":"A census designated place (CDP) defined within a military or Coast Guard installation",
    "U1":"A census designated place (CDP) with a name officially recognized by the U.S. Board on Geographic Names for a populated place",
    "U2":"A census designated place (CDP) with a name not officially recognized by the U.S. Board on Geographic Names for a populated place"}

FIPS_PLACE_CLASS_CODE={
    "C1":"An active incorporated place that does not serve as a county subdivision equivalent",
    "C2":"An active incorporated place that is legally coextensive with a county subdivision but treated as independent of any county subdivision (an independent place)",
    "C5":"An active incorporated place that is independent of any county subdivision and serves as a county subdivision equivalent (an independent place)",
    "C6":"An active incorporated place that is partially independent of any county subdivision and partially dependent within a legal county subdivision (exists in Iowa and Ohio only)",
    "C7":"An incorporated place that is independent of any county (an independent city)",
    "C8":"The balance of a consolidated city excluding the separately incorporated place(s) within that consolidated government",
    "C9":"An inactive or nonfunctioning incorporated place",
    "M2":"A census designated place (CDP) defined within a military or Coast Guard installation",
    "U1":"A census designated place (CDP) with a name officially recognized by the U.S. Board on Geographic Names for a populated place",
    "U2":"A census designated place (CDP) with a name not officially recognized by the U.S. Board on Geographic Names for a populated place"
}

FIPS_CONSOLIDATED_CITY={
    "03436":"Athens-Clarke County, Georgia",
    "04200":"Augusta-Richmond County, Georgia",
    "11390":"Butte-Silver Bow, Montana",
    "36000":"Indianapolis, Indiana",
    "47500":"Milford, Connecticut",
    "48003":"Louisville/Jefferson County, Kentucky",
    "52004":"Nashville-Davidson, Tennessee"
}



# Download URLS.
# Key differences between 2000 and 2010:
# - Different URL formats
# - In 2000, each ZIP file contains a single segment
# - In 2010, each ZIP file contains *all* of the state's segments.

WWW_SERVER_2000 = "https://www2.census.gov/census_2000/datasets/"
URL_2000_PL94   = WWW_SERVER_2000 + "redistricting_file--pl_94-171/{state_name}/{state}000{segment}.upl.zip"
URL_2000_SF1    = WWW_SERVER_2000 + "Summary_File_1/{state_name}/{state}{segment}_uf1.zip"
URL_2000_SF2    = WWW_SERVER_2000 + "Summary_File_2/{state_name}/{state}{segment}_uf2.zip"

WWW_SERVER_2000_RELATIONSHIP = "https://www2.census.gov/geo/docs/maps-data/data/rel/"
URL_2000_RELATIONSHIP = WWW_SERVER_2000_RELATIONSHIP + "t00t10/TAB2000_TAB2010_ST_{state_fips}_v2.zip"
                      
WWW_SERVER_2010='https://www2.census.gov/census_2010'
URL_2010_PL94 = WWW_SERVER_2010+'/01-Redistricting_File--PL_94-171/{state_name}/{state}2010.pl.zip'
URL_2010_SF1  = WWW_SERVER_2010+'/04-Summary_File_1/{state_name}/{state}2010.sf1.zip'
URL_2010_UR1  = WWW_SERVER_2010+'/04-Summary_File_1/Urban_Rural_Update/{state_name}/{state}2010.ur1.zip'
URL_2010_SF2  = WWW_SERVER_2010+'/05-Summary_File_2/{state_name}/{state}2010.sf2.zip'

ONE_SEGMENT_PER_ZIPFILE = {2000:True, 2010:False}

# Census 2000 and 2010 packaged differently
DOWNLOAD_SEGMENTS_PER_PRODUCT = {2000: {PL94: 3,
                                        SF1 : 40},
                                 2010: {PL94: 1,
                                        SF1 : 1,
                                        UR1 : 1 }}


DOWNLOAD_URLS = {2000:{PL94 : URL_2000_PL94,
                       SF1  : URL_2000_SF1,
                       SF2  : URL_2000_SF2,
                       RELATIONSHIP: URL_2000_RELATIONSHIP},
                 2010:{PL94 : URL_2010_PL94,
                       SF1  : URL_2010_SF1,
                       UR1  : URL_2010_UR1,
                       SF2  : URL_2010_SF2 } } 
                 
# Specifies directory where a zip file is downloaded. The filename is kept from the original download URL
DEST_ZIPFILE_DIR    = {2000:ROOT_DIR+'/data/{year}_{product}/dist/{state}',
                       2010:ROOT_DIR+'/data/{year}_{product}/dist'}

TABLE='TABLE'
VARIABLE='VARIABLE'
DESC='DESC'
SEGMENT='SEGMENT'

# linkage variables
FILEID='FILEID'
STUSAB='STUSAB'
CHARITER='CHARITER'
CIFSN='CIFSN'
LOGRECNO='LOGRECNO'
LINKAGE_VARIABLE_NAMES = [FILEID, STUSAB, CHARITER, CIFSN, LOGRECNO]

# We use the CIFSN 0 for the geo segment
CIFSN_GEO=0

# Create an array that maps state abbrev to state code.
# The theory is that it's faster to do a dictonary lookup than a function call and a dictionary lookup

STUSAB_TO_STATE = {sd['stusab']:int(sd['state']) for sd in STATE_DICTS}
STATE_TO_STUSAB = {int(sd['state']):sd['stusab'] for sd in STATE_DICTS}
    


class YPSS:
    """A Class that defines the Year, Product, State, Segment and Characteristic Iteration, 
       which is the way that each file in the PL94/SF1/SF2 are named."""
    __slots__=('year','product','state','segment','chariter')
    def __init__(self,year,product,state,segment,chariter=0):
        assert year in YEARS
        assert product in PRODUCTS
        assert state in STATE_NAMES
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
    if ypss.year==2000 and ypss.product==PL94:
        return "{state:2}000{segment:02}.upl".format(state=ypss.state,
                                                     segment=int(ypss.segment))
    if ypss.year==2010:
        ext = PRODUCT_EXTS[ypss.product]
        return "{state:2}{chariter:03}{segment:02}{year:04}.{ext}".format(
            state=ypss.state,
            chariter=int(ypss.chariter),
            segment=int(ypss.segment),
            year=int(ypss.year),
            ext = ext)



if __name__=="__main__":
    print("SDICTS:",SDICTS)
