#!/usr/bin/env python3
"""
decode the information in SF1 files. 
  - Uses CHAPTER6 PDF converted into CSV format by Adobe Acrobat.

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
The column headings are given by the Chapter6 pdf. 
The purpose of this program is to parse the PDF files and recover the headers for every column.

"""

import os
import os.path
import re
import zipfile
import io
import sys

# File locations

from constants import *
import census_etl
from census_etl.schema import Range,Variable,Table,Recode,Schema,TYPE_INTEGER,TYPE_VARCHAR,TYPE_NUMBER,TYPE_DECIMAL
import ctools
import ctools.tydoc  as tydoc

debug = False

"""
These regular expressions are used to parse the structure of Chapter 6 of the data product specification.
Fortunately, the format of Chapter 6 was consistent across 2000 and 2010, and between all data products.
Also consistent were the variable names.
"""

# Regular expressions for parsing geoheader
# Currently we don't parse them all due to inconsistencies in the PDF
# Generate an error if REQUIED_GEO_VARS are not present
GEO_VAR_RE   = re.compile(r"^(?P<desc>[A-Z][-A-Za-z0-9 ()/.]+) (?P<name>[A-Z]{1,13}) (?P<width>\d{1,2}) (?P<column>\d{1,3}) (?P<datatype>(A|A/N|N))$")
REQUIRED_GEO_VARS =  ['FILEID', 'STUSAB', 'SUMLEV', 'LOGRECNO', 'STATE', 'COUNTY', 'PLACE', 'TRACT', 'BLKGRP', 'BLOCK' ]


# Regular expression for parsing file section
FILE_START_RE = re.compile(r"^File (\d\d)")
TABLE_RE      = re.compile(r"(?P<table>(P|H|PCT|PCO|HCT)\d{1,2}[A-Z]?)[.]\s+(?P<title>[A-Z()0-9 ]+)")
VAR_RE        = re.compile(r"^("
                           r"(FILEID)|(STUSAB)|(CHARITER)|(CIFSN)|(LOGRECNO)|"
                           r"([PH]\d{7,8})|"
                           r"(PCO\d{7})|"
                           r"(PCT\d{7,8})|"
                           r"(PCT\d{3}[A-Z]\d{3})|"
                           r"(H\d{3}[A-Z]\d{4})|"
                           r"(P\d{3}[A-Z]\d{3})|"
                           r"(HCT\d{3}\d{4})"
                           r")$")

VAR_FIELDS_RE = re.compile(r"^(?P<prefix>[A-Z]+)(?P<tablenumber>\d{1,3})(?P<sequence>[A-Z]?)(?P<number>\d+)$")
VAR_PREFIX_RE = re.compile(r"^(?P<prefix>[A-Z]+)")

# Typo in 2010 SF1 specification. This varialble appears twice; ignore it the second time.
DUPLICATE_VARIABLES = ['PCT0200001']

def open_decennial(ypss):
    """Return an IO object that reads from the specified ZIP file in Unicode.
    This avoids the need to unzip the files.
    """

    with zipfile.ZipFile( zipfile_name( ypss ) ) as zip_file:
        # Note: You cannot use a with() on the one below:
        try:
            zf = zip_file.open( segmentfile_name( ypss ), 'r')
            return io.TextIOWrapper(zf, encoding='latin1')
        except KeyError as f:
            print(str(f))
        raise FileNotFoundError(f"segment {segmentfile_name( ypss )} not in file {zipfile_name(ypss)}")
        

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
    m = TABLE_RE.search( line )
    if m:
        (table,title) = m.group('table','title')
        return (table.strip(), title.strip())
    return None

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

        if (1 <= segment <= MAX_CIFSN) and (1 <= maxsize <= 9):
            return (name,desc,segment,maxsize)
    return None

FOOTNOTE_RE = re.compile(r'\[\d+\]')
def chapter6_prepare_csv_line(line):
    # Remove the quotes
    line = line.replace('"',' ').replace(',',' ').strip()

    # Remove a foonote, if present
    m = FOOTNOTE_RE.search(line)
    if m:
        line = line[:m.span()[0]] + line[m.span()[1]:]

    # Remove the space between words
    line = " ".join([word for word in line.split() if len(word)>0])

    # Make sure there are none of the bad characters
    assert ',' not in line
    assert '[' not in line
    assert ']' not in line
    return line

def chapter6_lines(fname):
    """Given a chapter6 PDF converted to a CSV file by Adobe Acrobat,
    return each line as a an array of fields, cleaned.
    """
    with open(fname,"r",encoding='latin1') as f:
        for line in f:
            yield chapter6_prepare_csv_line(line)
    
def tables_in_file(fname):
    """Give a chapter6 CSV file, return all of the tables in it."""
    tables = {}
    for line in chapter6_lines(fname):
        tn = parse_table_name(line)
        if tn is not None:
            tables[tn[0]] = tn[1]
    return tables

def process_tn(schema, tn, linkage_vars, file_number):
    """Process the tn and return the table"""
    (table_name, table_desc) = tn
    if not schema.has_table(table_name):
        # New table! Create it and add the linkage variables if we have any

        if debug:
            print(f"Creating table {table_name} in file number {file_number}")
        table = Table(name=table_name, 
                      desc=table_desc,
                      delimiter=',',
                      attrib = {CIFSN:file_number} )
        schema.add_table(table)

        # Add any memorized linkage variables. 
        for var in linkage_vars:
            if debug:
                print(f"Adding saved linkage variable {var.name} to table {table_name}")
            table.add_variable(var)
        return table
    else:
        return schema.get_table(table_name)
    

def schema_for_spec(chapter6_filename):
    """Given a Chapter6 file and an optional segment number, parse Chapter6 and
    return a schema object for that segment number
    """
    schema          = Schema()
    geotable        = Table( name = GEO_TABLE, attrib = {CIFSN:CIFSN_GEO} )
    schema.add_table(geotable)

    ## Due to a PDF issue, we hard-code the PLACE
    ## Note that we start with column 0, so we subtract 1 from place
    geotable.add_variable( Variable(name = 'PLACE', column = (46-1), width=5, vtype=TYPE_VARCHAR))


    linkage_vars    = []
    file_number     = False
    prev_var_m      = None      # previous variable match
    geo_columns     = set(range(0,500))

    for (ll,line) in enumerate(chapter6_lines(chapter6_filename),1):
        m = FILE_START_RE.search(line)
        if m:
            # New file. Note the file number we are in and copy over the linkage variables if we have any.
            # Make sure that the file number increased. 
            # Tables do not cross files, so reset the current table and field number
            # 
            old_file_number = file_number
            file_number     = int(m.group(1))
            if file_number == 1:
                field_number = 0
            else:
                assert old_file_number + 1 == file_number
                # use memorized linkage variables
                field_number = len(linkage_vars)    
            table           = None
            table_name      = None
            continue
        
        # If not yet in a file, check for geoheader line
        if file_number is False:
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
                geotable.add_variable( v )

                # Remove these columns from the set of geo column
                for i in range(column,column+width):
                    geo_columns.remove(i)
            continue

        # Check for linkage variables in the first file.
        if file_number == 1:
            lnk = parse_linkage_desc(line)
            if lnk and lnk[0] in LINKAGE_VARIABLES:
                (lnk_name, lnk_desc, lnk_cifsn, lnk_maxsize) = lnk
                if debug:
                    print(f"Discovered linkage variable {lnk_name}")
                linkage_vars.append( Variable(name  = lnk_name, 
                                              desc  = lnk_desc, 
                                              field = field_number,
                                              width = lnk_maxsize,
                                              vtype = TYPE_VARCHAR) )
                field_number += 1
                continue

        # Check for start of a new table, as indicated by table name.
        tn = parse_table_name(line)
        if tn:
            table = process_tn(schema, tn, linkage_vars, file_number)

        # Can we parse variables?
        var = parse_variable_desc(line)
        if not var or var[0] in LINKAGE_VARIABLES:
            continue
        
        # We found a variable that we can process. 
        (var_name, var_desc, var_cifsn, var_maxsize) = var

        # Make sure variable is for the correct file
        assert file_number == var_cifsn

        ###
        ### HANDLE ERRORS IN PDF AND OCR
        ###

        # 2010 SF1: OCR puts the table definition for PCT12G at the bottom of page 6-213
        if var_name=='PCT012G001':
            table = process_tn(schema, ["PCT12G","SEX BY AGE (TWO OR MORE RACES)"], linkage_vars, file_number)


        ###
        ### VALIDATE THE VARIABLE. (THIS ALSO VALIDATES OUR PARSING)
        ###

        if table is None:
            raise RuntimeError(f"Line {ll} we should have a table description. var: {var}")

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



        # Everything looks good: add the variable and increment the field number
        if debug:
            print(f"Adding variable {var_name} to table {table_name}")

        if 'AVERAGE' in table.desc:
            vtype = TYPE_DECIMAL
        else:
            vtype = TYPE_NUMBER

        table.add_variable( Variable(name   = var_name,
                                     desc   = var_desc,
                                     field  = field_number,
                                     width  = var_maxsize,
                                     vtype  = vtype) )
        # Go to the next field
        field_number += 1



        # If VSN is 001 and the first 
        
    for varname in REQUIRED_GEO_VARS:
        if varname not in geotable.varnames():
            raise RuntimeError(f"Parser did not find geovariable {varname} in geoheader")

    if debug:
        print("The following geo columns were not parsed:")
        print(sorted(geo_columns))
    return schema


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="""Test program:
    Extract the schema from the SF1 Chapter 6 and dump the schema. 
    Normally this module will be used to generate a Schema object for a specific Chapter6 spec.""",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--geodump", help='Using the schema, dump the geo information for the provided file')
    parser.add_argument("--year",    type=int, default=2010)
    parser.add_argument("--product", type=str, default=SF1)
    parser.add_argument("--segment", help="dump the tables just this segment",type=int)
    parser.add_argument("--limit", help="limit output to this many records", type=int, default=50)
    parser.add_argument("--sumlev", help="Just print this summary level")
    args = parser.parse_args()


    ch6file = CHAPTER6_CSV_FILES.format(year=args.year,product=args.product)

    schema  = schema_for_spec(ch6file)
    schema.dump()

    if args.geodump:
        geotable = schema.get_table(GEO_TABLE)
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
            if rows==args.limit:
                break
        tt.render(sys.stdout, format='md')
        exit(0)
            

    if args.segment:
        for table in schema.tables():
            if table.attrib[CIFSN]==args.segment:
                table.dump()
    else:
        schema.dump()
    


