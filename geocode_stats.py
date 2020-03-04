#!/usr/bin/env python3
"""
Goals of this program:

- We are interested in building a tree of geounits. For each geounit, we want to measure fanout. 

- We want to be able to experiment with different partitioning functions, and to explore partitioning functions that are based on the data

- We want to consider all geographies, inhabited 2010 geographies, and 2010 geographies with housing units or GQ facilities.
"""

import os
import sys

import dbload_pl94

class GeocodeStats:
    def __init__(self,db):
        self.conn = dbload_pl94.db_connection(db)
        
    def cursor(self):
        return self.conn.cursor()

    def prefixinfo(self,prefix,span):
        c = self.cursor()
        pl = len(prefix)
        cmd = f"select substr(geocode,1,{pl+span}),count(*) from blocks where substr(geocode,1,{pl})=? group by substr(geocode,1,{pl+span})"
        print(cmd)
        c.execute(cmd,[prefix])
        res = c.fetchall()
        for (code,count) in res:
            print(code,count)
        print(f"Count: {len(res)}")


if __name__=="__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Report statistics about geocode prefixes',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--prefix", help="Report about a prefix")
    parser.add_argument("--span", type=int, help="Specify number of characters for span")
    parser.add_argument("--db", help="Specify database location", default=dbload_pl94.DBFILE)
    args = parser.parse_args()
    gs = GeocodeStats(args.db)
    if args.prefix and args.span:
        print(gs.prefixinfo(args.prefix,args.span))
