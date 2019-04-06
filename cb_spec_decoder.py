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
- So the first 5 columns of every file in every state are the same. 

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

# File locations

from constants import *
import census_etl
import ctools

"""
These regular expressions are used to parse the structure of Chapter 6 of the data product specification.
Fortunately, the format of Chapter 6 was consistent across 2000 and 2010, and between all data products.
Also consistent were the variable names.
"""

FILE_START_RE = re.compile(r"^File (\d\d)")
TABLE_RE      = re.compile(r"(?P<table>(P|H|PCT)\d{1,2}[A-Z]?)[.]\s+(?P<title>[A-Z ]+)")
VAR_RE        = re.compile(r"^((FILEID)|(STUSAB)|(CHARITER)|(CIFSN)|(LOGRECNO)|"
                           r"([PH]\d{7,8})|"
                           r"(PCO\d{7})|"
                           r"(PCT\d{7,8})|"
                           r"(PCT\d{3}[A-Z]\d{3})|"
                           r"(H\d{3}[A-Z]\d{4})|"
                           r"(P\d{3}[A-Z]\d{3}))$")

# Typo in 2010 SF1 specification. This varialble appears twice; ignore it the second time.
DUPLICATE_VARIABLES = ['PCT0200001']



def open_decennial(ypss):
    """Return an IO object that reads from the specified ZIP file in Unicode.
    This avoids the need to unzip the files.
    """

    with zipfile.ZipFile( zipfile_name( ypss ) ) as zip_file:
        # Note: You cannot use a with() on the one below:
        zf = zip_file.open( segmentfile_name( ypss ), 'r')
        return io.TextIOWrapper(zf, encoding='latin1')

    
def is_variable_name(name):
    m = VAR_RE.search(name)
    if m:
        return True
    return False

def parse_table_name(line):
    """If line describes a table, return (table_number,table_description)"""
    m = TABLE_RE.search(line)
    if m:
        return m.group('table','title')
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

        if (1 <= segment <= MAX_SEGMENT) and (1 <= maxsize <= 9):
            return (name,desc,segment,maxsize)
    return None

def chapter6_prepare_csv_line(line):
    line = line.replace('"',' ').replace(',',' ').strip()
    b = line.find('[')            # Remove the [
    if b>0:
        line = line[0:b]
    line = " ".join([word for word in line.split() if len(word)>0])
    assert ',' not in line
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

def schema_for_spec(chapter6_filename,segment=True):
    """Given a Chapter6 file and an optional segment number, parse Chapter6 and
    return a schema object for that segment number
    """
    from census_etl.schema import Range,Variable,Table,Recode,Schema,TYPE_INTEGER,TYPE_VARCHAR
    schema = Schema()
    current_table = None
    tables = {}
    linkage_vars = []
    infile = False
    got_all_linkage = False
    field_number = 0
    for line in chapter6_lines(chapter6_filename):
        m = FILE_START_RE.search(line)
        if m:
            infile = int(m.group(1))
            if got_all_linkage:
                field_number = len(linkage_vars)
            continue
        
        # If not in a file, return
        if infile is False:
            continue

        # Check for linkage variables
        lnk = parse_linkage_desc(line)
        if lnk and (got_all_linkage is False):
            (lnk_name, lnk_desc, lnk_segment, lnk_maxsize) = lnk
            linkage_vars.append( Variable(name  = lnk_name, 
                                          desc  = lnk_desc, 
                                          field = field_number,
                                          width = lnk_maxsize,
                                          vtype = TYPE_VARCHAR) )
            field_number += 1
            continue

        # Check for table name
        tn = parse_table_name(line)
        if tn:
            if (segment is True) or (infile == segment):
                tables[tn[0]] = tn[1]
                current_table = tn[0]
                table         = schema.get_table(current_table, create=True)
                # Add the linkage variables if we don't have them
                if len(table.vardict)==0:
                    for var in linkage_vars:
                        table.add_variable(var)
            else:
                current_table = None
                table         = None

            got_all_linkage = True
            continue

        # if we are not in a table, return
        if not current_table:
            continue
        
        # Can we parse variables?
        var = parse_variable_desc(line)
        if not var:
            continue
        
        # Process
        (var_name, var_desc, var_segment, var_maxsize) = var
        # Add this variable, and optionally the table, to the schema
        if var_name in table.vardict:
            if var_name in DUPLICATE_VARIABLES:
                continue
            else:
                raise KeyError("duplicate variable name: {}".format(var_name))
        table.add_variable( Variable(name   = var_name,
                                     desc   = var_desc,
                                     field  = field_number,
                                     width  = var_maxsize,
                                     attrib = {'segment':var_segment},
                                     vtype  = TYPE_INTEGER) )
        field_number += 1

    return schema

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="""Test program:
    Extract the schema from the SF1 Chapter 6 and dump the schema. 
    Normally this module will be used to generate a Schema object for a specific Chapter6 spec.""",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--all",  action='store_true', help="dump for all segments")
    parser.add_argument("--year", type=int, default=2010)
    parser.add_argument("--product", type=str, default=SF1)
    
    parser.add_argument("segment",nargs='?',help="dump for just this segment",type=int)
    args = parser.parse_args()
    ch6file = CHAPTER6_CSV_FILES.format(year=args.year,product=args.product)
    if args.all:
        args.segment = True
    schema = schema_for_spec(ch6file, args.segment)
    schema.dump()
    


