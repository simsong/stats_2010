#!/usr/bin/env python3
#
# print info about a geography file

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
