#!/usr/bin/env python3
#
# print info about the SF1

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

FILEID='FILEID'
STUSAB='STUSAB'
SUMLEV='SUMLEV'
STATE='STATE'
COUNTY='COUNTY'
TRACT='TRACT'
BLOCK='BLOCK'


class SF1:
    GEO_FIELDS={}               # mapping of fields in geo header to location in the file... name:(start,end,desc)

    def __init__(self,args):
        self.args = args
        self.stats = 0
        self.stats_per_line = 0

    def read_sas_geo(self,fname):
        geo_line_re = re.compile(r'@(\d+) (\w+) [$](\d+)[.] [/][*](.*)[*][/]')
        # Sample line:
        # @1 FILEID $6. /*File Identification*/
        # @1 = Starting column
        # FILEID = Name of field
        # $6 = Width of field
        # /* human-readable name*
        with open(fname,"r") as f:
            for line in f:
                m = geo_line_re.search(line)
                if(m):
                    # the geo header file assumes that the first character is position 1
                    # python assumes that the first is position 0
                    start = int(m.group(1)) - 1 
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
        assert self.ex_geo_field(line,'FILEID')=='SF1ST '
        geo_level = self.ex_geo_field(line,'SUMLEV')
        def ex(field):
            return self.ex_geo_field(line,field)
        def exi(field):
            try:
                return int(ex(field))
            except ValueError:
                return 0
        if self.args.debug:
            for fieldname in self.GEO_FIELDS.keys():
                print(fieldname, self.ex_geo_field(line, fieldname), self.GEO_FIELDS[fieldname][2])
            print("")
            args.dump -= 1
            return
        geo_tuple=(ex(STUSAB), exi(COUNTY), exi(TRACT), exi(BLOCK), exi(SUMLEV))

    def decode_table_line(self,line):
        fields = line.split(",")
        try:
            (table,state,county,tract,block) = fields[0:5]
        except ValueError as r:
            print("Bad line: ",line)
            raise r
        self.stats_per_line = len(fields[5:])
        return

    def load_file(self,f, decode_func):
        # don't know what it currently is
        self.stats_per_line = 0 
        t0 = time.time()
        for (ll,line) in enumerate(f):
            if self.stats_per_line==0:
                decode_func(line)
            self.stats += self.stats_per_line
            if args.interval and (ll % args.interval==0):
                print("{}...".format(ll),end='')
                sys.stdout.flush()
        t1 = time.time()
        #print("Finished {}; {:,.0f} lines/sec".format(f.name,ll/(t1-t0)))

    def process_zipfile(self,zipfilename):
        (path,name) = os.path.split(zipfilename)
        zf = zipfile.ZipFile(zipfilename)
        for zn in zf.namelist():
            if zn.endswith("packinglist.txt"):
                pass
            elif zn[2:5]=='geo':
                #self.load_file(io.TextIOWrapper(zf.open(zn), encoding='latin1'), self.decode_geo_line)
                pass
            else:
                self.load_file(io.TextIOWrapper(zf.open(zn), encoding='latin1'), self.decode_table_line)
        print("{},{}".format(name[0:2],self.stats))
        sys.stdout.flush()
        self.stats = 0
        


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Compute file changes',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--db",   help="db file",default='sf1.shelf')
    parser.add_argument("--debug", action='store_true')
    parser.add_argument("--interval", help="Frequency of notification", type=int, default=0)
    parser.add_argument("zipfiles", help="Files to ingest. ZIP file", nargs="*")
    args = parser.parse_args()

    # open database and give me a big cache
    g = SF1(args)
    g.read_sas_geo("sf1/pl_geohd_2010.sas")
    for fname in args.zipfiles:
        g.process_zipfile(fname)
