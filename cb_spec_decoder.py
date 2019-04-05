#!/usr/bin/env python3
"""
decode the information in SF1 files. Uses CHAPTER6 converted into CSV format.
SF1 is distributed as a set of 52 ZIP files. Each file contains:
- Geoheader, which maps every LOGRECNO to a Geography.
- files {state}00001{year}.sf1 through {state}00047{year}.sf1 where
  {state} is the 2- character abreviation and {year} is 2010.
  00001 through 00047 are the segment numbers. We pass them as an integer

The .sf1 files are all linked together by LOGRECNO. Each is a CSV file, without a header. The column headings are given by the Chapter6 pdf. 

See README.md for a description of the file formats.

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


SF1_GEOHEADER_NAME='{state}{part}2010.sf1'
SF1_PART_NAME='{state}{part:05}2010.sf1'

FILE_START_RE = re.compile(r"^File (\d\d)")
VAR_RE       = re.compile(r"^((FILEID)|(STUSAB)|(CHARITER)|(CIFSN)|(LOGRECNO)|"
                           r"([PH]\d{7,8})|"
                           r"(PCO\d{7})|"
                           r"(PCT\d{7,8})|"
                           r"(PCT\d{3}[A-Z]\d{3})|"
                           r"(H\d{3}[A-Z]\d{4})|"
                           r"(P\d{3}[A-Z]\d{3}))$")

INTERVAL=10

# Typo in SF1 specification. This varialble appears twice
DUPLICATE_VARIABLES = ['PCT0200001']

def part_matrix_columns(fileno):
    """Given a SF1 part number, return the columns based on an analysis of Chapter 6."""
    assert 1<=fileno<=47
    infile = None
    cols = []
    with open( fileno, "r", encoding='latin1') as f:
        for line in f:
            line = line.strip()
            line = re.sub(r",+", ",", line) # replace repeated commas with a single comma
            line = re.sub(r" +", " ", line) # replace repeated spaces with a single space
            if line[0]==',':
                line = line[1:]
            m = FILE_START_RE.search(line)
            if m:
                infile = int(m.group(1))
                continue
            if infile != fileno:
                continue
            print(line)
            for word in re.split("[ ,]",line):
                if len(word) > 3:
                    m = VAR_RE.search(word)
                    if m:
                        cols.append(word)
                        print(len(cols),m,word,":",line)
    return cols
                    
def sf1_file_from_zip(state,part):
    """Return an IO object that reads from the specified ZIP file in Unicode."""
    zipfilename = SF1_ZIPFILE_NAME.format(state=state)
    if part=='geo':
        partname = SF1_GEOHEADER_NAME.format(state=state,part=part)
    else:
        partname    = SF1_PART_NAME.format(state=state,part=part)
    zip_file = zipfile.ZipFile(zipfilename)
    zf       = zip_file.open(partname, 'r')
    return io.TextIOWrapper(zf, encoding='latin1')

    
# Define the fileds in the GEO Header. See Figure 2-5 of SF1 publication
# These were extracted by hand. Sorry!
GEO_FILEID=(1,6)
GEO_STUSAB=(7,2)
GEO_STATE=(28,2)
GEO_SUMLEV=(9,3)
GEO_LOGRECNO=(19,7)
GEO_COUNTY=(30,3)
GEO_PLACE=(46,5)            
GEO_TRACT=(55,6)            
GEO_BLKGRP=(61,1)
GEO_BLOCK=(62,4)        # first digit of block is blockgroup

# Using the constants above, extract a string from a line, and extract an integer.
def ex(line,what):
    """Given a line and a tuple defining the field (START,COUNT), extract the characters."""
    return line[what[0]-1:what[0]+what[1]-1]

def exi(line,what):
    """Same as ex(), but convert to a string."""
    return int(ex(what))

def geocode_for_line(geoline):
    """Given a geoline, extract and return a dictionary of the fields. Currently we only extract the ones listed above"""
    return "".join([ex(line,level) for level in [GEO_STATE, GEO_COUNTY, GEO_TRACT, GEO_BLKGRP, GEO_BLOCK]])

def logrecno_for_sumlev(state,sumlev):
    """Return a dictionary of the logrecnos for a state and the corresponding geocode for each"""
    logrecnos = dict()
    for geoline in sf1_file_from_zip(state,'geo'):
        if ex(geoline,GEO_SUMLEV)==sumlev:
            assert ex(geoline,GEO_FILEID)=='SF1ST'
            assert ex(geoline,GEO_STUSAB)==state
            print(ex(geoline, GEO_LOGRECNO), geocode_for_line(geoline))
            logrecnos[ ex(geoline, GEO_LOGRECNO) ] = geocode_for_line(geoline)
    return logrecnos

table_re = re.compile(r"(?P<table>(P|H|PCT)\d{1,2}[A-Z]?)[.]\s+(?P<title>[A-Z ]+)")
def is_table_name_line(line):
    """If @fields describes a table, return (table_number,table_description)"""
    m = table_re.search(line)
    if m:
        return m.group('table','title')
    return None

def is_variable_name(name):
    m = VAR_RE.search(name)
    if m:
        return True
    return False

def parse_variable_desc(line):
    """If @fields describes a variable, return data dictionary
    reference name, desc, segment, and maxsize. Assumes 
    that lines that describe variables are formualted as:
    <text> <variable-name> <segment> <maxsize>
    """

    fields = line.split()
    if len(fields)>=4:
        (desc,name,segment,maxsize) = (" ".join(fields[0:-4]),
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

def chapter6_prepare_line(line):
        line = line.replace('"',' ').replace(',',' ').strip()
        b = line.find('[')            # Remove the [
        if b>0:
            line = line[0:b]
        return " ".join([word for word in line.split() if len(word)>0])

def chapter6_lines(fname):
    """Given a chapter6 file, return each line as a an array of fields, cleaned"""
    with open(fname,"r",encoding='latin1') as f:
        for line in f:
            yield chapter6_prepare_line(line)
    


def tables_in_file(fname):
    tables = {}
    for line in chapter6_lines(fname):
        tn = is_table_name_line(line)
        if tn is not None:
            tables[tn[0]] = tn[1]
    return tables

def schema_for_spec(chapter6_filename,segment=True):
    """Given a Chapter6 file and an optional segment number, parse Chapter6 and
    return a schema object for that segment number
    """
    from census_etl.schema import Range,Variable,Table,Recode,Schema,TYPE_INTEGER
    schema = Schema()
    current_table = None
    tables = {}
    for line in chapter6_lines(chapter6_filename):
        tn = is_table_name_line(line)
        if tn:
            tables[tn[0]] = tn[1]
            current_table = tn[0]
            continue
        # if we are not in a table, return
        if not current_table:
            continue
        
        # Can we parse variables?
        vars = parse_variable_desc(line)
        if not vars:
            continue
        
        # Is this in one of the segments that we care about?
        (var_name, var_desc, var_segment, var_maxsize) = vars
    
        if (segment is True) or (var_segment == segment):
            # Add this variable, and optionally the table, to the schema
            table = schema.get_table(current_table, create=True)
            if var_name in table.vardict:
                if var_name in DUPLICATE_VARIABLES:
                    continue
                else:
                    raise KeyError("duplicate variable name: {}".format(var_name))
            table.add_variable( Variable(name   = var_name, desc=var_desc, field=len(table.vardict)+1, 
                                         attrib = {'segment':var_segment},
                                         vtype=TYPE_INTEGER) )

    return schema

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Extract the schema from the SF1 Chapter 6 and show what you can do with it.',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--all",action='store_true', help="dump for all segments")
    parser.add_argument("segment",nargs='?',help="dump for just this segment",type=int)
    args = parser.parse_args()
    if args.all:
        schema = schema_for_spec(SF1_CHAPTER6_CSV)
    else:
        schema = schema_for_spec(SF1_CHAPTER6_CSV,args.segment)
    


