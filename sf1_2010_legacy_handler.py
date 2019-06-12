<<<<<<< HEAD:sf1_decoder.py
#!/usr/bin/env python3
"""
decode the information in SF1
"""

import os
import os.path
import re
import zipfile
import io

CHAPTER6_CSV = os.path.join(os.path.dirname(__file__), "doc/{publication}_chapter6.csv")

FILE_START_RE = re.compile("^File (\d\d)")
VAR_RE = re.compile("(FILEID)|(STUSAB)|(CHARITER)|(CIFSN)|(LOGRECNO)|((H|P|PCT)[0-9A-O]{6,14})")
=======
>>>>>>> ee95b6ef7a6bbe01c6da3cb86d3e76a9bf01d91e:sf1_2010_legacy_handler.py

def part_matrix_columns(publication,fileno):
    """Given a SF1 part number, return the columns based on an analysis of Chapter 6."""
    assert 1<=fileno<=47
    infile = None
    cols = []
<<<<<<< HEAD:sf1_decoder.py
    with open( CHAPTER6_CSV.format(publication=publication), "r", encoding='latin1') as f:
=======
    with open( fileno, "r", encoding='latin1') as f:
>>>>>>> ee95b6ef7a6bbe01c6da3cb86d3e76a9bf01d91e:sf1_2010_legacy_handler.py
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
            for word in re.split("[ ,]",line):
                if len(word) > 3:
                    m = VAR_RE.search(word)
                    if m:
                        cols.append(word)
    return cols

                    

<<<<<<< HEAD:sf1_decoder.py
    
def pl94_file_from_zip(state,part):
    state = state.lower()
    zipfilename = f'/data/pl94/{state}2010.pl.zip'
    if part=='geo':
        partname = f'{state}{part}2010.pl'
    else:
        partname    = f'{state}{part:05}2010.pl'
    zip_file = zipfile.ZipFile(zipfilename)
    zf       = zip_file.open(partname, 'r')
    return io.TextIOWrapper(zf, encoding='latin1')

    
=======
>>>>>>> ee95b6ef7a6bbe01c6da3cb86d3e76a9bf01d91e:sf1_2010_legacy_handler.py


################################################################
### LEGACY HANDLING OF 2010 SF1 GEO HEADER
# Define the fileds in the GEO Header. See Figure 2-5 of SF1 publication
<<<<<<< HEAD:sf1_decoder.py
# Check these - PL94 and SF1 appear to have different geo headers.
=======
# These were extracted by hand. Sorry!
>>>>>>> ee95b6ef7a6bbe01c6da3cb86d3e76a9bf01d91e:sf1_2010_legacy_handler.py
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

