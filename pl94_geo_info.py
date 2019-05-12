#!/usr/bin/env python3
#
"""
geo_info.py print info about a geography file
Note that each state has its own geography file.
"""

__version__ = '0.0.1'

import datetime
import json
import os
import os.path
import re
import sqlite3
import sys
import time
import zipfile
import io

INTERVAL = 10000

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
STATES=[dict(zip("state_name,state_abbr,fips_state".split(","),line.split(","))) for line in STATE_DATA]


def state_rec(key):
    """Return the record in the state database for a key, where key is the state name, abbreviation, or FIPS code."""
    for rec in STATES:
        if (key.lower()==rec['state_name'].lower()
            or key.lower()==rec['state_abbr'].lower()
            or key==rec['fips_state']):
                return rec
    raise ValueError(f"{key}: not a valid state name, abbreviation, or FIPS code")

def state_fips(key):
    """Convert state name or abbreviation to FIPS code"""
    return state_rec(key)['fips_state']

def state_abbr(key):
    """Convert state FIPS code to the appreviation"""
    return state_rec(key)['state_abbr'].lower()

def all_state_abbrs():
    # Return a list of all the states 
    return [rec['state_abbr'].lower() for rec in STATES]

def parse_state_abbrs(statelist):
    # Turn a list of states into an array of all state abbreviations.
    # also accepts state numbers
    return [state_rec(key)['state_abbr'].lower() for key in statelist.split(",")]
    

class GeoDecoder:
    GEO_FIELDS={}               # name:(start,end,desc)

    def __init__(self,args):
        self.args = args

    def read_sas_geo(self,fname):
        geo_line_re = re.compile(r'@(\d+) (\w+) [$](\d+)[.] [/][*](.*)[*][/]')
        with open(fname,"r") as f:
            for line in f:
                m = geo_line_re.search(line)
                if(m):
                    start = int(m.group(1)) - 1 #  because we start with 0
                    end = int(m.group(3)) + start
                    self.GEO_FIELDS[m.group(2)] = (start, end, m.group(4))

    def ex_geo_field(self,line,fieldname):
        """Extract a field from the geo file"""
        g = self.GEO_FIELDS[fieldname]
        return line[ g[0]:g[1] ]

    def exi_geo_field(self,line,fieldname):
        """Extract an integer field from the geo file"""
        return int( self.ex_geo_field(line,fieldname))

    def decode_geo_line(self,line):
        """Decode the hiearchical geography lines. These must be done before the other files are read
        to get the logrecno."""
        assert self.ex_geo_field(line,'FILEID')=='PLST  '
        geo_level = self.ex_geo_field(line,'SUMLEV')
        if geo_level == args.level and args.dump:
            for fieldname in self.GEO_FIELDS.keys():
                print(fieldname, self.ex_geo_field(line, fieldname), self.GEO_FIELDS[fieldname][2])
            print("")
            args.dump -= 1
        return
        if exi(GEO_SUMLEV) in [750]:
            try:
                if DEBUG_BLOCK and exi(GEO_BLOCK)==DEBUG_BLOCK:
                    print("INSERT INTO blocks (state,county,tract,block,logrecno) values ({},{},{},{},{})".format(
                        ex(GEO_STUSAB), exi(GEO_COUNTY), exi(GEO_TRACT), exi(GEO_BLOCK), exi(GEO_LOGRECNO)))
                c.execute("INSERT INTO blocks (state,county,tract,block,logrecno) values (?,?,?,?,?)",
                          (ex(GEO_STUSAB), exi(GEO_COUNTY), exi(GEO_TRACT), exi(GEO_BLOCK), exi(GEO_LOGRECNO)))
            except sqlite3.IntegrityError as e:
                conn.commit()          # save where we are
                print("INSERT INTO blocks (state,county,tract,block,logrecno) values ({},{},{},{},{})".format(
                    ex(GEO_STUSAB), exi(GEO_COUNTY), exi(GEO_TRACT), exi(GEO_BLOCK), exi(GEO_LOGRECNO)))
                raise e


    def load_file(self,f,decode_func):
        t0 = time.time()
        for (ll,line) in enumerate(f):
            decode_func(line)
            if ll%INTERVAL==0:
                print("{}...".format(ll),end='')
                sys.stdout.flush()
        t1 = time.time()
        print("Finished {}; {:,.0f} lines/sec".format(fname,ll/(t1-t0)))

    def process_name(self,f,name):
        if name[2:]=='geo2010.pl':
            self.load_file(f,self.decode_geo_line)
        elif name[2:]=='000012010.pl':
            print("Not processing 000012010 files")
        elif name[2:]=='000022010.pl':
            print("Not processing 000022010 files")
        else:
            raise RuntimeError("Unknown file type: {}".format(fname))

    def process_file(self,fname):
        (path,name) = os.path.split(fname)
        print(name)
        if name.lower().endswith(".zip"):
            zf = zipfile.ZipFile(fname)
            for zn in zf.namelist():
                if zn.endswith(".pl"):
                    self.process_name( io.TextIOWrapper(zf.open(zn), encoding='latin1'), zn)
            return
        self.process_name(open(fname, encoding='latin1'), name)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Compute file changes',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--level", help="Info about this geolevel")
    parser.add_argument("--dump",  help="Dump this many records", type=int, default=0)
    parser.add_argument("files", help="Files to ingest. May be XXgeo2010.pl or a ZIP file", nargs="*")
    args = parser.parse_args()

    # open database and give me a big cache
    g = GeoDecoder(args)
    g.read_sas_geo("pl_geohd_2010.sas")
    for fname in args.files:
        g.process_file(fname)
