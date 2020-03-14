#!/usr/bin/env python3
"""
geocode.py:

Functions for working with geocodes.
A geocode is a text string that encodes the full geography.
This module contains logic to create geocodes from the PL94 and SF1 geography files.

We actually have three geocodes:

v1 geocode:  STATE(2)|COUNTY(3)|TRACT(6)|BLOCK(4)

v2 geocode:  STATE(2)|COUNTY(3)|COUSUB(4)|TRACT(6)|BLOCK(4)

v3 geocode:
 WASHINGTON DC(3) | PADDED-SLDU(8)       | PADDED-TRACT(9) | BLKGRP(2) | BLOCK(4)
 STATE-AIANNH (3) | PADDED-AIANNH(8)     | COUNTY-TRACT(9) | BLKGRP(2) | BLOCK(4)
 STATE(3)         | PADDED-COUSUB(8)     | COUNTY-TRACT(9) | BLKGRP(2) | BLOCK(4)
 STATE(3)         | COUNTY(3) | PLACE(5) | PADDED-TRACT(9) | BLKGRP(2) | BLOCK(4)
"""

STRONG_MCD_STATES=[9,11,23,25,26,27,33,34,36,42,44,50,55]
DC_FIPS=11

EXCLUDE_STATE_RECOGNIZED_TRIBES=True
def include_aiannh(code):
    if 1 <= code <= 4999:
        return "Federally recognized American Indian Reservations and Off-Reservation Trust Lands"
    elif 5000 <= code  <=5999:
        return "Hawaiian Home Lands"
    elif 6000 <= code <= 7999:
        return "Alaska Native Village Statistical Areas"
    elif 9000 <= code <= 9499:
        if EXCLUDE_STATE_RECOGNIZED_TRIBES:
            return False
        else:
            return "State recognized American Indian Reservations"
    else:
        return False


def nint(val):
    """Return an integer or None"""
    try:
        return int(val)
    except ValueError as e:
        if val.strip()=="":
            return None
        raise e

def strip_str(val):
    """Return a stripped string."""
    return str(val).strip()


# Define the fileds in the GEO Header. See Figure 2-5 of PL94 & SF1 publications
# These fields are consistent for both publications
# This could be rewritten to use the learned schema...
# The fields appear exactly as they appear in the specification, which is (FIELD WIDTH, FIELD START)
GEO_HEADER = {
    "FILEID" : (6,1, str),
    "STUSAB" : (2,7, str),
    "SUMLEV" : (3,9, nint),
    "LOGRECNO" : (7,19, nint),
    "STATE" :  (2,28, nint),
    "COUNTY" : (3, 30, nint),
    "COUSUB" : (5, 37, nint),
    "PLACE"  : (5, 46, nint),        # Incorporated place or census designated place,
    "PLACECC": (2,51, str),
    "TRACT"  :  (6,55, nint),            
    "BLKGRP" : (1,61, nint),       # first digit of block is blockgroup,
    "BLOCK"  :  (4,62, nint),        
    "CONCIT": (5, 68, nint),
    "AIANNH" : (4,77, nint),
    "AITSCE" : (3, 89, nint),
    "SLDU"   : (3, 156, str),
    "NAME"   : (90,227, strip_str)       # in Latin1 for 2000 and 2010,
}

def extract(field,line):
    """Extract just the field from the GEO file"""
    return line[GEO_HEADER[field][1]-1:GEO_HEADER[field][1]-1+GEO_HEADER[field][0]]

def extractall_typed(line):
    """Extract all the values as a typed dictionary"""
    try:
        return { gh : GEO_HEADER[gh][2]( extract(gh, line).strip()) for gh in GEO_HEADER}
    except ValueError:
        print("line:",line,file=sys.stderr)
        for gh in GEO_HEADER:
            print(gh,extract(gh,line),end='',file=sys.stderr)
            print(GEO_HEADER[gh][2]( extract(gh,line) ),file=sys.stderr )

def info_geo_line(conn, c, line):
    """Just print information about a geography line"""
    print( geo_geocode(line),extractall_typed( line ))

def geo_geocode(line):
    """The original geocode used for the DAS"""
    return "".join( [ extract(gh, line) for gh in ['STATE','COUNTY','TRACT', 'BLOCK']] )

def geo_geocode3(gh):
    """The revised geocode that takes into account AIANNH. Levels are:
    0 - Nation
    1 - Non-AIANNH part-of-state                  | AIANNH part-of-State 
    2 - COUNTY in non-strong MCD states           | ignored in AIANNH
    3 - PLACE in 38 strong-MCD states, SLDU in DC | AIANNH in AIANNH states
    4 - TRACT or 3-digit TG or 4-digit TG         | TRACT
    5 - BLKGRP first 1 or 2 digits of block       | BLKGRP
    6 - BLOCK                                     | BLOCK
    """
    code = []
    block  = f"{gh['BLOCK']:04}"
    blkgrp2 = block[0:2]         # note 2-digit block groups
    if gh['STATE']==DC_FIPS:
        # Washington DC
        code.append(f"{gh['STATE']:02}X")    # STATE  (3)
        code.append(f"XXX")                  # COUNTY (3);  Washington DC has no COUNTY level
        code.append(f"{int(gh['SLDU']):05}") # PLACE  (5) in the district of columbia
        code.append(f"___{gh['TRACT']:06}")  # TRACT  (9)
        code.append( blkgrp2 )               # BLKGRP (2)
        code.append( block   )               # BLOCK  (4)
    elif include_aiannh(gh['AIANNH']):
        # AIANNH portion of 38-states with AIANNH
        code.append(f"{gh['STATE']:02}A") # STATE; 3 characters
        code.append(f"IAN")               # COUNTY; 3 characters (ignored in AIANNH regions)
        code.append(f"{gh['AIANNH']:05}") # PLACE; 5 characters
        code.append(f"{gh['COUNTY']:03}{gh['TRACT']:06}")  # COUNTY + TRACT; 9 characters (for uniqueness)
        code.append( blkgrp2 ) # BLKGRP 2 character
        code.append( block )  # BLOCK 4 characters
    elif gh['STATE'] in STRONG_MCD_STATES:
        # Non-AIAN area in 12 state with strong MCD
        code.append(f"{gh['STATE']:02}X") # STATE; 3 characters
        code.append(f"XXX")               # COUNTY; 3 characters (ignored with strong MCD)
        code.append(f"{gh['COUSUB']:05}")  # PLACE; COUSUB in 12 strong-MCD states
        code.append(f"{gh['COUNTY']:03}{gh['TRACT']:06}")  # COUNTY + TRACT; 9 characters (for uniqueness)
        code.append( blkgrp2 ) # BLKGRP 2
        code.append( block  )  # BLOCK
    else:
        # Non-AIAN area and 38 states not strong MCD
        code.append(f"{gh['STATE']:02}X") # STATE; 3 characters
        code.append(f"{gh['COUNTY']:03}") # COUNTY; 3 characters
        code.append(f"{gh['PLACE']:05}")  # PLACE in 38 states with strong MCD
        code.append(f"___{gh['TRACT']:06}")  # TRACT 
        code.append( blkgrp2 ) # BLKGRP 2
        code.append( block  )  # BLOCK
    return "".join(code)



class GeoCode:
    """A class for representing v1 geocodes."""
    def __init__(self, state_code, county_code, tract_code, blk_code, area_land=None):
        self.state_code = state_code
        self.county_code = county_code
        self.tract_code = tract_code
        self.blk_code = blk_code
        self.area_land = area_land
        self.area_land_percentage = None

    def __str__(self):
        return self.state_code + self.county_code + self.tract_code + self.blk_code

    def __hash__(self):
        return hash((self.state_code, self.county_code, self.tract_code, self.blk_code, self.area_land))

    def __eq__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return self.state_code == other.state_code and self.county_code == other.county_code \
            and self.tract_code == other.tract_code and self.blk_code == other.blk_code \
            and self.area_land == self.area_land
