#!/usr/bin/env python3
"""
decode the information in SF1 files. 
  - Uses PDF converted into CSV format by Adobe Acrobat and Microsoft Excel.

2000 SF1 is distributed as a set of 39 x 52 = 2028 ZIP file, one for each segment, and one for the geoheader.

2010 SF1 is distributed as a set of 52 ZIP files, with each state's segments all in one file.

Once you have all of the files unpacked, they contain:
- Geoheader, which maps every LOGRECNO to a Geography.
  - Note that the geoheader formats are not consistent between products. 

- Segments (sometimes called file #s), which contains the 5 linkage fields and one or more "tables" arranged
  as a subset of the columsn.
- So:
   - The first 3 columns of every file in every state are the same. 
   - Column #4 is the Characteristic Iteration File Sequence Number (CIFSN)
   - Column #5 is the Logical Record Number

File naming conventions were inconsistent in 2000 and changed in 2010. The rules are a mess
and are contained within the Python file constants.py.

The files within a state are all linked together by LOGRECNO. 

Each is a CSV file, without a header. 
It is surprising that these CSV files were distributed without any headers.
The column headings are given by the data dictionary.
The purpose of this program is to parse the PDF files and recover the headers for every column.

"""

import os
import os.path
import re
import zipfile
import io
import sys
import copy
import logging

# File locations

from urllib.parse import urlparse
import constants as C

import ctools
import ctools.tydoc as tydoc
import ctools.s3 as s3
from ctools.schema.schema import Schema
from ctools.schema.variable import Variable
from ctools.schema import TYPE_INTEGER,TYPE_VARCHAR,TYPE_NUMBER,TYPE_DECIMAL

debug = False

"""
These regular expressions are used to parse the structure of Chapter 6 of the data product specification.
Fortunately, the format of Chapter 6 was consistent across 2000 and 2010, and between all data products.
Also consistent were the variable names.
"""

# Regular expressions for parsing geoheader
# Currently we don't parse them all due to inconsistencies in the PDF
# Generate an error if REQUIED_GEO_VARS are not present
# Note that we have several dashes below
GEO_VAR_RE   = re.compile(r"^(?P<desc>[A-Z][\-\–\—A-Za-z0-9 ()/.]+) "
                          r"(?P<name>[A-Z]{1,13}5?) (?P<width>\d{1,2}) (?P<column>\d{1,3}) (?P<datatype>(A|A/N|N))$")

REQUIRED_GEO_VARS =  ['FILEID', 'STUSAB', 'SUMLEV', 'LOGRECNO', 'STATE', 'COUNTY', 'PLACE', 'TRACT', 'BLKGRP', 'BLOCK' ]


# Regular expression for parsing file section
CHAPTER_RE    = re.compile(r"^Chapter (\d+)\.")
DATA_DICTIONARY_RE = re.compile(r"^Data.Dictionary")
SEGMENT_START_RE = re.compile(r"^File (\d+)")
TABLE_RE      = re.compile(r"(?P<table>(P|PL|H|PCT|PCO|HCT)\d{1,2}[A-Z]?)[.]\s+(?P<title>[A-Z()0-9 ]+)")
VAR_RE        = re.compile(r"^("
                           r"(FILEID)|(STUSAB)|(CHARITER)|(CIFSN)|(LOGRECNO)|"
                           r"([PH]\d{6,8})|"
                           r"(PCO\d{6,7})|"
                           r"(PCT\d{6,8})|"
                           r"(PCT\d{3}[A-Z]\d{3})|"
                           r"(H\d{3}[A-Z]\d{3,4})|"
                           r"(P\d{3}[A-Z]\d{3})|"
                           r"(HCT\d{3}\d{4})"
                           r")$")

VAR_FIELDS_RE = re.compile(r"^(?P<prefix>[A-Z]+)(?P<tablenumber>\d{1,3})(?P<sequence>[A-Z]?)(?P<number>\d+)$")
VAR_PREFIX_RE = re.compile(r"^(?P<prefix>[A-Z]+)")

# Regular expression for extracting table name from a variable

### TYPOS and OCR errors
## Typo in 2010 SF1 specification. A few variables are mentioned twice; ignore it the second time.
DUPLICATE_VARIABLES = set(['P027E003',   # 2000 SF1
                           'PCT0200001', # 2010 SF1
                           ])

# These tables don't parse correctly yet
BAD_TABLES=set(['P35F1'])

## Missing Geovariables. Typically because the file didn't OCR properly
## Note that column starts with 0 in this file, but starts with 1 in the PDF, so we subtract 1.
place_var = Variable(name = 'PLACE', column = (46-1), width=5, vtype=TYPE_VARCHAR)
chariter_var = Variable(name = 'CHARITER', column = (14-1), width=3, vtype=TYPE_INTEGER)
sldu_var     = Variable(name = 'SLDU', column=(156-1), width=3, vtype=TYPE_VARCHAR)
sldl_var     = Variable(name = 'SLDL', column=(159-1), width=3, vtype=TYPE_VARCHAR)
puma_var     = Variable(name = 'PUMA', column=(478-1), width=5, vtype=TYPE_VARCHAR)
MISSING_GEOVARIABLES = [{C.YEAR:2000, C.PRODUCT: C.PL94, C.VARIABLE: place_var},
                        {C.YEAR:2000, C.PRODUCT: C.PL94, C.VARIABLE: chariter_var},
                        {C.YEAR:2010, C.PRODUCT: C.PL94, C.VARIABLE: place_var},
                        {C.YEAR:2010, C.PRODUCT: C.PL94, C.VARIABLE: sldu_var},
                        {C.YEAR:2010, C.PRODUCT: C.PL94, C.VARIABLE: sldl_var},
                        {C.YEAR:2010, C.PRODUCT: C.PL94, C.VARIABLE: puma_var},
                        {C.YEAR:2010, C.PRODUCT: C.SF1,  C.VARIABLE: sldu_var},
                        {C.YEAR:2010, C.PRODUCT: C.SF1,  C.VARIABLE: sldl_var},
                        {C.YEAR:2010, C.PRODUCT: C.SF1,  C.VARIABLE: puma_var},
                        {C.YEAR:2010, C.PRODUCT: C.SF1,  C.VARIABLE: place_var}]
                        

## If there are tables that start a segment but there are no corresponding segment starts, put them here.
MISSING_SEGMENT_STARTS = []

## If there are tables for which the variables indicate they are in the wrong segment number, put them here.
WRONG_CIFSN = [{C.YEAR:2010, C.PRODUCT: C.SF1, C.TABLE: 'PCT23', C.CIFSN:47},
               {C.YEAR:2010, C.PRODUCT: C.SF1, C.TABLE: 'PCT24', C.CIFSN:47}]

## These tables are in the spec, but only in the UR1. Delete them from the SF1 schema.
MISSING_TABLES = [{C.YEAR:2010, C.PRODUCT: C.SF1, C.TABLE: 'PCT23'},
                  {C.YEAR:2010, C.PRODUCT: C.SF1, C.TABLE: 'PCT24'}]

# 2010 SF1: OCR puts the table definition for PCT12G at the bottom of page 6-213
MISSING_TABLE_STARTS   = [{C.YEAR:2010, C.PRODUCT: C.SF1, C.VARIABLE:'PCT012G001', C.TABLE:'PCT12G', C.DESC: "SEX BY AGE (TWO OR MORE RACES)"}]


def open_decennial(ypss):
    """Return an IO object that reads from the specified ZIP file in Unicode.
    This avoids the need to unzip the files.
    """

    with zipfile.ZipFile( C.zipfile_name( ypss ) ) as zip_file:
        # Note: You cannot use a with() on the one below:
        try:
            zf = zip_file.open( C.segmentfile_name( ypss ), 'r')
            return io.TextIOWrapper(zf, encoding='latin1')
        except KeyError as f:
            print(str(f))
        raise FileNotFoundError(f"segment {C.segmentfile_name( ypss )} not in file {C.zipfile_name(ypss)}")
        

def is_chapter_line(line):
    return CHAPTER_RE.search(line) and True

def is_data_dictionary_line(line):
    return DATA_DICTIONARY_RE.search(line) and True

def is_variable_name(name):
    m = VAR_RE.search(name)
    if m:
        return True
    return False

def variable_prefix(name):
    m = VAR_PREFIX_RE.search(name)
    return m.group('prefix')

def parse_table_name(line):
    """If line describes a table, return (table_number,table_description)"""
    # ignore continuation lines
    if line.endswith("Con."):
        return (None, None)
    m = TABLE_RE.search( line )
    if m:
        (table,title) = m.group('table','title')
        table = table.strip()
        title = title.strip()
        return (table, title)
    return (None, None)

def parse_linkage_desc(line):
    """If @line describes a linkage field, return
    return <name>, <desc>, True, <maxsize>"""
    fields = line.split()
    if len(fields)>=3:
        (desc,name,maxsize,a_n) = (" ".join(fields[0:-4]), fields[-3],fields[-2],fields[-1])
        if not is_variable_name(name):
            return False
        try:
            maxsize = int(maxsize)
        except ValueError as e:
            return False

        return (name,desc,True,maxsize)
    return None

def parse_variable_desc(line):
    """If @line describes a variable, return data dictionary
    reference <name>, <desc>, <segment>, and <maxsize>. Assumes 
    that lines that describe variables are formualted as:
    <text> <variable-name> <segment> <maxsize>
    """
    fields = line.split()
    if len(fields)>=4:
        (desc,name,segment,maxsize) = (" ".join(fields[0:-3]),
                                       fields[-3],fields[-2],fields[-1])
        if not is_variable_name(name):
            return False
        try:
            segment = int(segment)
            maxsize = int(maxsize)
        except ValueError as e:
            return False

        if (1 <= segment <= C.MAX_CIFSN) and (1 <= maxsize <= 9):
            if desc[-1:]==':':
                desc = desc[0:-1]
            return (name,desc,segment,maxsize)
    return False

FOOTNOTE_RE = re.compile(r'\[\d+\]')
def csvspec_prepare_csv_line(line):
    # Remove BOM if present
    line = line.replace(u"\uFEFF","")

    # Replace Unicode hard spaces with regular spaces
    line = line.replace(u"\u00A0"," ")

    # Remove the quotes
    line = line.replace('"',' ').replace(',',' ').strip()

    # Remove a foonote, if present
    m = FOOTNOTE_RE.search(line)
    if m:
        line = line[:m.span()[0]] + line[m.span()[1]:]

    # If there is still a '[', remove everything after it
    for ch in '[]':
        bracket = line.find(ch)
        if bracket != -1:
            line = line[:bracket]

    # Remove the space between words
    line = " ".join([word for word in line.split() if len(word)>0])


    # Make sure there are none of the bad characters
    for ch in '[,]':
        if ch in line:
            raise RuntimeError(f"line: {line} contains: {ch}")
    return line

def csvspec_lines(fname):
    """Given a data dictionary converted to a CSV file by Adobe Acrobat and Microsoft Excel,
    return each line as a an array of fields, cleaned. Note that
    """
    with open(fname,"r",encoding='utf-8') as f:
        for line in f:
            yield csvspec_prepare_csv_line(line)
    
def add_named_table(schema, table_name, table_desc, linkage_vars, cifsn):
    """Add the named table to the schema, and add the linkage variables to the table. """
    if not schema.has_table(table_name):
        # New table! Create it and add the linkage variables if we have any

        if debug:
            print(f"Creating table {table_name} in file number {cifsn}")
        table = schema.add_table_named(name=table_name, 
                                       desc=table_desc,
                                       delimiter=',',
                                       attrib = {C.CIFSN:cifsn} )

        # Add any memorized linkage variables. 
        for var in linkage_vars:
            if debug:
                print(f"Adding saved linkage variable {var.name} to table {table_name}")
            table.add_variable(var)
        return table
    else:
        return schema.get_table(table_name)

TABLE_FROM_VAR_RE = re.compile(r"([A-Z]+(000[0-9]|00[1-9]|0[1-9][0-9])[A-Z]*)")
PAT = re.compile(r"[A-Z]+(0+)(\d+)")
def table_name_from_variable(varname):
    m = TABLE_FROM_VAR_RE.search(varname)
    if m:
        table_name = m.group(1)
        # Remove the leading 0 if there is a number
        m = PAT.search(table_name)
        if m:
            old = m.group(1)+m.group(2)
            new = m.group(2)
            table_name = table_name.replace(old,new)
        return table_name
    return None




def schema_for_spec(csv_filename, *, year, product, debug=False):
    """Take the Census-provided PDF of the spec. Convert it to an Excel Spreadsheet with Adobe Acrobat, then save it as a CSV file.
    If you cannot convert the entire file, try converting just the Data Dictionary chapter. 
    Parse the data dictionary and return a schema object for that segment number. 
    year and product are provided so that patches can be applied.
    """
    schema          = Schema()
    linkage_vars    = []
    cifsn           = False
    prev_var_m      = None      # previous variable match
    geo_columns     = set()     # track the columns we have used
    table           = None
    in_data_dictionary = False
    last_line       = ""
    #debug = True

    print(f"csv filename: {csv_filename}")
    ### UR1 and SF1 use the same spec
    if product==C.UR1:
        product = C.SF1

    ### Read the geography header specification

    geotable        = schema.add_table_named( name=C.GEO_TABLE, attrib = {C.CIFSN:C.CIFSN_GEO} )

    ### Patch geo specification necessary
    for mgv in MISSING_GEOVARIABLES:
        if mgv[C.YEAR]==year and mgv[C.PRODUCT]==product:
            geotable.add_variable( mgv[C.VARIABLE] )


    for (ll,line) in enumerate(csvspec_lines(csv_filename),1):
        if not in_data_dictionary:
            # Look for the data dictionary chapter
            if is_data_dictionary_line(line) and is_chapter_line(last_line):
                in_data_dictionary = True
                continue
            last_line = line
            continue
            
        m = SEGMENT_START_RE.search(line)
        if m:
            # New segment. Note the segment number we are in and copy
            # over the linkage variables if we have any.  Make sure
            # that the segment number increased.  Tables do not cross
            # segments, so reset the current table and field number
            # 
            new_cifsn     = int(m.group(1))
            if new_cifsn == 1:
                segment_field_number = 0
            else:
                assert cifsn + 1 == new_cifsn
                # use memorized linkage variables
                segment_field_number = len(linkage_vars)    
            cifsn  = new_cifsn
            table  = None
            continue
       
        #print(f"Debug is {debug}; cifsn is {cifsn}") 
        # If not yet in a file, check for geoheader line
        if cifsn is False:
            m = GEO_VAR_RE.search(line)
            if m:
                (desc,name,width,column,datatype) = m.group('desc','name','width','column','datatype')
                width  = int(width)
                column = int(column) - 1 # we start with column 0, Census starts with column 1
                v = Variable( name = name,
                              desc = desc,
                              column = column, 
                              width = width,
                              vtype = TYPE_VARCHAR) 
                if debug:
                    print(f"Adding variable {v} to geotable {geotable}")
                geotable.add_variable( v )

                # Add these columns from the set of geo column we are using
                for i in range(column,column+width):
                    if i in geo_columns:
                        raise RuntimeError(f"Column {i} is used in multiple columns")
            continue

        # If this is the first segment, learn the linkage variables from the it
        if cifsn == 1:
            lnk = parse_linkage_desc(line)
            if lnk and lnk[0] in C.LINKAGE_VARIABLE_NAMES:
                (lnk_name, lnk_desc, lnk_cifsn, lnk_maxsize) = lnk
                if debug:
                    print(f"Discovered linkage variable {lnk_name}")
                linkage_vars.append( Variable(name  = lnk_name, 
                                              desc  = lnk_desc, 
                                              field = segment_field_number,
                                              width = lnk_maxsize,
                                              vtype = TYPE_VARCHAR) )
                segment_field_number += 1
                continue

        # Check for start of a new table, as indicated by table name.
        (new_table_name,new_table_desc) = parse_table_name(line)

        #if not new_table_name:
        #    print(f"Not new. Table was: {table}")
        if new_table_name:
            print(f"Discovered new table {table}")
            ### Patch as necessary for missing segment starts
            for mss in MISSING_SEGMENT_STARTS:
                if mss[C.YEAR]==year and mss[C.PRODUCT] == product and mss[C.TABLE] == new_table_name:
                    cifsn = mss[C.SEGMENT]
                    segment_field_number   = len(linkage_vars)
                    table          = None

            ### If this is the PL94 for 2000, manually add the linkage variables
            if year==2000 and product==C.PL94 and len(linkage_vars)==0:
                for varname in C.LINKAGE_VARIABLE_NAMES:
                    try:
                        var = copy.deepcopy(geotable.get_variable( varname ))
                        var.field = segment_field_number
                        segment_field_number += 1
                        linkage_vars.append( var )
                    except KeyError:
                        print("geotable:")
                        geotable.dump()
                        raise RuntimeError(f"Cannot find {varname}")
                    

            ### End patching

            table = add_named_table(schema, new_table_name, new_table_desc, linkage_vars, cifsn)

        # Can we parse variables?
        var = parse_variable_desc(line)
        if not var or var[0] in C.LINKAGE_VARIABLE_NAMES:
            continue
        
        # We found a variable that we can process. 
        (var_name, var_desc, var_cifsn, var_maxsize) = var
        # Compute the table name from the variable
        tnfv = table_name_from_variable(var_name)

        ###
        ### HANDLE ERRORS IN PDF AND OCR
        ###

        #print(f"At mts in missing, table was {table}")
        for mts in MISSING_TABLE_STARTS:
            if mts[C.YEAR]==year and mts[C.PRODUCT] == product and mts[C.VARIABLE] == var_name:
                table = add_named_table(schema, mts[C.TABLE], mts[C.DESC], linkage_vars, cifsn)

        for wc in WRONG_CIFSN:
            if wc[C.YEAR]==year and wc[C.PRODUCT] == product and wc[C.TABLE] == table.name:
                var_cifsn = wc[C.CIFSN]
                
        ###
        ### VALIDATE THE VARIABLE. (THIS ALSO VALIDATES OUR PARSING)
        ###

        if table is None:
            raise RuntimeError(f"Line {ll} we should have a table description. var: {var}")

        # Make sure variable is for the correct segment
        if cifsn != var_cifsn:
            raise RuntimeError(f"segment number mismatch: {cifsn} != {var_cifsn} for variable {var_name} in '{line}'")

        # Check for duplicate variable name (ignoring errors we know of)
        if var_name in table.varnames():
            if var_name in DUPLICATE_VARIABLES:
                continue            # Known erros
            raise KeyError("duplicate variable name: {}".format(var_name))

        # Make sure that all the variables in the table have the same prefix.
        var_prefix = variable_prefix(var_name)
        if 'variable_prefix' in table.attrib:
            assert table.attrib['variable_prefix'] == var_prefix
        else:
            table.attrib['variable_prefix'] = var_prefix
            
        # Validate this variable in relationship to the previous variable.
        m = VAR_FIELDS_RE.search(var_name)
        if m and prev_var_m:
            # if vsn=1 and the vtable hasn't changed, make sure that the vseries has increased
            num = m.group('number')
            if ( prev_var_m.group('tablenumber') == m.group('tablenumber') and num==1 ):
                expected_sequence = chr(ord(prev_var.m.group('sequence'))+1)
                if expected_sequence != m.group('sequence'):
                    raise ValueError(f"line {ll}: found VSERIES {vseries} for variable {var_name}; "
                                     f"expected {expected}.")

            # Make sure that the varilable sequence number increased from previous one or is 001
            if num>1:
                last_num = int(last_var_m.group('number'))
                if num != last_num+1:
                    raise ValueError(f"line {ll}: found VSN {num} for variable {var_name}; "
                                     f"expected {last_num+1}")
        last_var_m   = m

        ###
        ### END OF PDF ERROR HANDLER
        ###

        if 'AVERAGE' in table.desc:
            vtype = TYPE_DECIMAL
        else:
            vtype = TYPE_NUMBER

        v = Variable(name   = var_name,
                     desc   = var_desc,
                     field  = segment_field_number,
                     width  = var_maxsize,
                     vtype  = vtype)

        # OCR ERROR: table definition for table P35G before variable definition for P35F001
        if (year==2010) and (product==C.SF1) and (tnfv=='P35F'):
            schema.get_table('P35F').add_variable( v )

        else:
            if tnfv is not None:
                # SPEC ERROR: Year 2000 PL94 tables all start PL but the variables all start P
                if year==2000 and product==C.PL94 and tnfv[0]=='P':
                    tnfv = tnfv.replace("P","PL")
                if table.name != tnfv:
                    logging.warning(f"Extracted table name {tnfv} from variable {var_name} but current table is {table.name}. Adding anyway")
                    table = schema.get_table(tnfv).add_variable(v)
                    continue

            if debug:
                print(f"Adding variable {var_name} to {table}")
            table.add_variable( v )

        segment_field_number += 1        # Go to the next field

    ###
    ### delete any missing tables
    ###
    for mt in MISSING_TABLES:
        if mt[C.YEAR]==year and mt[C.PRODUCT]==product:
            schema.del_table_named(mt[C.TABLE])

    ###
    ### Validate the learned schema
    ###

    if in_data_dictionary==False:
        raise RuntimeError(f"Parser did not find the data dictionary")
        
    for varname in REQUIRED_GEO_VARS:
        if varname not in geotable.varnames():
            raise RuntimeError(f"Parser did not find geovariable {varname} in geoheader for {year} {product}")

    for table in schema.tables():
        if table in BAD_TABLES:
            print(f"Ignoring table {table}")
            continue
        if len(table.vars()) <= len(linkage_vars):
            print(f"detected table vars: {table.varnames()}")
            print(f"and linkage_vars {str(linkage_vars)}")
            raise RuntimeError(f"{year} {product} Table {table.name} does not have enough variables (has {len(table.vars())}, vs # expected links {len(linkage_vars)})")

    if debug:
        print("The following geo columns were not parsed:")
        for i in range(0,max(geo_columns)):
            if i not in geo_columns:
                print(i,end=' ')
        print()
    return schema

def get_cvsspec(*,year,product):
    # Note: SF1 and UR1 use the same specification
    if product==C.UR1:
        product = C.SF1
    checked = []
    for filename_fmt in C.SPEC_FILES:
        filename = filename_fmt.format(year=year, product=product)
        if os.path.exists(filename):
            return filename
        checked.append(filename)
    raise FileNotFoundError(f"Cannot find CSV spec for {year} {product}. Reviewed: " + (" ".join(checked)))
        
class DecennialData:
    def __init__(self,*, dataroot, year, product, debug=False):
        """Inventory the files and return an SF1 object.
        Note that if UR1 is requested, schema_for_spec() will get the spec for the SF1,
        but this class will still return the _data_ for UR1.
        """

        self.year      = int(year)
        self.product   = product
        self.debug = debug

        ### Get the schema

        self.specfile = get_cvsspec(year=year, product=product)
        self.schema = schema_for_spec( self.specfile, year=year, product=product, debug=debug)

        ### Get the data files
        if dataroot=="":
            raise RuntimeError(f"dataroot is ''")

        # files is an array of dictionaries which list every file under the dataroot
        self.files     = []
        for path in dataroot.split(";"):
            self.find_files(path)
        if len(self.files)==0:
            raise FileNotFoundError(f"No data files found in dataroot: {dataroot}")


    def get_table(self,tableName):
        return self.schema.get_table(tableName)

    def find_files(self, dataroot):
        p = urlparse(dataroot)
        if p.scheme=='s3':
            for obj in s3.list_objects(dataroot):
                self.register_file( 's3://' + p.netloc + '/' + obj[s3._Key])
        elif dataroot.startswith('hdfs:'):
            raise RuntimeError('hdfs SF1_ROOT not implemented')
        else:
            # Must be a file in the file system
            for (dirpath,dirnames,filenames) in os.walk(dataroot):
                for filename in filenames:
                    self.register_file(os.path.join(dirpath,filename))

    def register_file(self,path):
        """Files have a pattern:  {state}{section}{year}.{product}"""
        filename = os.path.basename(path)
        if filename.endswith(".sf1"):
            state = filename[0:2]
            try:
                if len(filename)==13 and filename[2:5]=='geo':
                    self.files.append({'path':path,
                                       C.STATE:state,
                                       C.CIFSN:C.CIFSN_GEO,
                                       C.YEAR:int(filename[5:9]),
                                       C.PRODUCT:C.SF1})
                if len(filename)==15:
                    self.files.append({'path':path,
                                       C.STATE:state,
                                       C.CIFSN:int(filename[2:7]),
                                       C.YEAR:int(filename[7:11]),
                                       C.PRODUCT:C.SF1})
            except ValueError as e:
                if debug:
                    print("bad filename:",path)
        elif filename.endswith(".uf1"):
            state = filename[0:2]
            try:
                if len(filename)==9 and filename[2:5]=='geo':
                    print(f"Found len 9 file {filename} ending with .uf1 & path {path}")
                    self.files.append({'path':path,
                                       C.STATE:state,
                                       C.CIFSN:C.CIFSN_GEO,
                                       C.YEAR:2000,         # Hacky hard-code..
                                       C.PRODUCT:C.SF1})    # Product seems to be u/r update to sf1. Not sure if this will work
                if len(filename)==11:
                    print(f"Found len 11 file {filename} ending with .uf1 & path {path}")
                    self.files.append({'path':path,
                                       C.STATE:state,
                                       C.CIFSN:int(filename[2:7]),
                                       C.YEAR:2000,
                                       C.PRODUCT:C.SF1})
            except ValueError as e:
                if debug:
                    print("bad filename:",path)
           
    def unique_selector(self,selector):
        """Return the unique values for a given selector"""
        return set( [obj[selector] for obj in self.files] )
    
    def get_df(self,*, tableName, sqlName):
        """Get a dataframe where the tables are specified by a selector.
        """
        # Get a list of all the matching files
        table = self.schema.get_table(tableName)
        if tableName == C.GEO_TABLE:
            cifsn = C.CIFSN_GEO
        else:
            cifsn = table.attrib[C.CIFSN]

        # Find the files
        paths = [ obj['path'] for obj in self.files if
                  (obj['year']==self.year and obj['product']==self.product) and obj[C.CIFSN]==cifsn]

        if len(paths)==0:
            print("No file found. Available data files:")
            for obj in self.files:
                print(obj)
            raise RuntimeError(f"No files found looking for year:{self.year} product:{self.product} CIFSN:{cifsn}")
            
        # Create an RDD for each text file
        from pyspark.sql import SparkSession
        spark = SparkSession.builder.getOrCreate()
        rdds = [spark.sparkContext.textFile(path) for path in paths]

        # Combine them into a single file
        rdd  = spark.sparkContext.union(rdds)

        # Convert it to a dataframe
        df   = spark.createDataFrame( rdd.map( table.parse_line_to_SparkSQLRow ), samplingRatio=1.0 )
        df.registerTempTable( sqlName )
        return df
            
    def find_variable_by_name(self,name):
        """Scans all tables in the schema until a variable name is found. Returns it"""
        for table in self.schema.tables():
            try:
                return (table, table.get_variable(name))
            except KeyError:
                pass
        raise KeyError(f"variable {name} not found in any table in schema")

    def print_legend(self,df,*,printHeading=True,file=sys.stdout):
        """Print the legend for the columns in the dataframe. 
        Takes advantage of the fact that all column names are unique with the Census Bureau."""

        if printHeading:
            print("Legend:")
        rows = []
        for varName in df.columns:
            if "." in varName:
                varName = varName.split(".")[-1] # take the last name
            rows.append( self.find_variable_by_name(varName) )
        #rows.sort()
        old_table = None
        for (table, var) in rows:
            if table!= old_table:
                print(f"Table {table.name}   {table.desc}")
                old_table = table
            print("  ", var.name, var.desc)
        print("")


def year_product_iterator():
    for year in C.SEGMENTS_FOR_YEAR_PRODUCT.keys():
        for product in C.SEGMENTS_FOR_YEAR_PRODUCT[year].keys():
            yield (year,product)


def build_relationship_table(path, sql_name, app_name):
    from pyspark.sql import SparkSession
    spark = SparkSession.builder.appName(app_name).getOrCreate()
    df = spark.read.csv(path, header=True)
    df.registerTempTable(sql_name)
    print(df)
    return df


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="""Test program:
    Extract the schema from the SF1 Chapter 6 and dump the schema. 
    Normally this module will be used to generate a Schema object for a specific data dictionary specification.""",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--geodump", help='Using the schema, dump the geo information for the provided file')
    parser.add_argument("--year",    type=int, help="Use statistics from this year" ,default=2010)
    parser.add_argument("--product", type=str, default=C.SF1)
    parser.add_argument("--segment", help="dump the tables just this segment",type=int)
    parser.add_argument("--limit", help="limit output to this many records. Specify 0 for no limit", type=int, default=50)
    parser.add_argument("--sumlev", help="Just print this summary level")
    parser.add_argument("--debug",   action='store_true')
    args = parser.parse_args()


    specfile = get_cvsspec(year=args.year,product=args.product)
    schema   = schema_for_spec(specfile, year=args.year, product=args.product, debug=args.debug)

    if args.geodump:
        geotable = schema.get_table(C.GEO_TABLE)
        tt = tydoc.tytable()
        tt.add_head(['LOGRECNO','SUMLEV','STATE','COUNTY','TRACT','BLOCK'])
        rows = 0
        for line in open(args.geodump,'r',encoding='latin1'):
            d = geotable.parse_line_to_dict(line)
            if args.sumlev is not None:
                if args.sumlev!=d['SUMLEV']:
                    continue
            tt.add_data( [d['LOGRECNO'], d['SUMLEV'], d['STATE'], d['COUNTY'], d['TRACT'], d['BLOCK']] )
            rows += 1
            if (rows==args.limit) and args.limit>0:
                break
        tt.render(sys.stdout, format='md')
        exit(0)
            

    if args.segment:
        for table in schema.tables():
            if table.attrib[C.CIFSN]==args.segment:
                table.dump()
    else:
        # If args.segment is not provided, then dump the entire schema
        schema.dump()
    


