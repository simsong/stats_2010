#!/usr/bin/env python3
"""
decode the information in SF1 files. Uses CHAPTER6 converted into CSV format.
"""

import os
import os.path
import re
import zipfile
import io

# File locations

from constants import *

SF1_GEOHEADER_NAME='{state}{part}2010.sf1'
SF1_PART_NAME='{state}{part:05}2010.sf1'

FILE_START_RE = re.compile(r"^File (\d\d)")
VAR_RE = re.compile(r"(FILEID)|(STUSAB)|(CHARITER)|(CIFSN)|(LOGRECNO)|((H|P|PCT)[0-9A-O]{6,14})")

def part_matrix_columns(fileno):
    """Given a SF1 part number, return the columns based on an analysis of Chapter 6."""
    assert 1<=fileno<=47
    infile = None
    cols = []
    with open( CHAPTER6_CSV, "r", encoding='latin1') as f:
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
    """Return a dictionary of the logrecnos for a state and the corresponding geocode"""
    logrecnos = dict()
    for geoline in sf1_file_from_zip(state,'geo'):
        print(ex(geoline,GEO_SUMLEV), sumlev)
        if ex(geoline,GEO_SUMLEV)==sumlev:
            assert ex(geoline,GEO_FILEID)=='SF1ST'
            assert ex(geoline,GEO_STUSAB)==state
            print(ex(geoline, GEO_LOGRECNO), geocode_for_line(geoline))
            logrecnos[ ex(geoline, GEO_LOGRECNO) ] = geocode_for_line(geoline)
    return logrecnos


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Extract the schema from the SF1 Chapter 6 and produce readers for all of the file types',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--state",help="specify state to work with",default='ak')
    args = parser.parse_args()
    
    print(logrecno_for_sumlev(args.state,'750'))

