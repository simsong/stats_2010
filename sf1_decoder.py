#!/usr/bin/env python3
"""
decode the information in SF1
"""

import os
import os.path
import re

CHAPTER6_CSV = os.path.join(os.path.dirname(__file__), "doc/sf1_chapter6.csv")

FILE_START_RE = re.compile("^File (\d\d)")
VAR_RE = re.compile("(FILEID)|(STUSAB)|(CHARITTER)|(CIFSN)|(LOGRECNO)|((H|P|PCT)[0-9A-O]{6,14})")

def part_matrix_columns(fileno):
    """Given a SF1 part number, return the columns based on an analysis of Chapter 6."""
    assert 1<=fileno<=47
    infile = None
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
            for word in re.split("[ ,]",line):
                if len(word) > 5:
                    m = VAR_RE.search(word)
                    if m:
                        print(m,word,":",line)
                    


if __name__=="__main__":
    part_matrix_columns(3)
