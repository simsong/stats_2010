#!/usr/bin/env python3
"""
Goals of this program:

- We are interested in building a tree of geounits. For each geounit, we want to measure fanout. 

- We want to be able to experiment with different partitioning functions, and to explore partitioning functions that are based on the data

- We want to consider all geographies, inhabited 2010 geographies, and 2010 geographies with housing units or GQ facilities.
"""

import os
import sys

import sqlite3
import dbload_pl94

class GeocodeStats:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.conn.row_factory = sqlite3.Row # give me dicts
        
    def cursor(self):
        return self.conn.cursor()

    def prefixinfo(self,prefix,child_prefix_span,minpop=0):
        """For a given prefix and a span of characters for the child's prefix, 
        return a list of the children, and for each the number of blocks and number of people.
        The fanout is the size of the list.
        """
        c = self.cursor()
        pl = len(prefix)
        cmd = f"""SELECT substr(geocode,1,{pl+child_prefix_span}) AS prefix,
                  COUNT(*) AS count,
                  SUM(pop) AS pop 
                  FROM blocks 
                  WHERE SUBSTR(geocode,1,{pl})=? AND pop>=?
                  GROUP BY SUBSTR(geocode,1,{pl+child_prefix_span})"""
        print(cmd)
        c.execute(cmd,[prefix,minpop])
        res = c.fetchall()
        for row in res:
            print(dict(row))
        return res


    def prefixinfo(self,prefix,child_prefix_span,minpop=0):
        """For a given prefix and a span of characters for the child's prefix, 
        return a list of the children, and for each the number of blocks and number of people.
        The fanout is the size of the list.
        """
        c = self.cursor()
        pl = len(prefix)
        cmd = f"""SELECT substr(geocode,1,{pl+child_prefix_span}) AS prefix,
                  COUNT(*) AS count,
                  SUM(pop) AS pop 
                  FROM blocks 
                  WHERE SUBSTR(geocode,1,{pl})=? AND pop>=?
                  GROUP BY SUBSTR(geocode,1,{pl+child_prefix_span})"""
        print(cmd)
        c.execute(cmd,[prefix,minpop])
        return c.fetchall()

    def county_prefix_report(self,child_prefix_span,limit=10):
        """For every county, report the number of children, the blocks, and the population, 
        for child prefixes of a given size.
        """
        assert isinstance(child_prefix_span,int)
        c = self.cursor()
        cmd = f"""SELECT substr(geocode,1,5+?) AS prefix,
                  SUM(1) AS block_count,
                  SUM( CASE WHEN pop>0 THEN 1 ELSE 0 END) as pop_block_count,
                  SUM(pop) AS pop 
                  FROM blocks 
                  GROUP BY state,county,SUBSTR(geocode,6,?) LIMIT ?"""
        print(cmd)
        c.execute(cmd,[child_prefix_span,child_prefix_span,limit])
        return c.fetchall()

if __name__=="__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Report statistics about geocode prefixes',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--prefix", help="Report about a prefix")
    parser.add_argument("--span", type=int, help="Specify number of characters for span")
    parser.add_argument("--db", help="Specify database location", default=dbload_pl94.DBFILE)
    parser.add_argument("--allcounties", help="Report by counties", action='store_true')
    args = parser.parse_args()
    gs = GeocodeStats(args.db)
    if args.prefix and args.span:
        for row in gs.prefixinfo(args.prefix,args.span,minpop=1):
            print(dict(row))
    if args.allcounties:
        for row in gs.county_prefix_report(args.span,limit=10):
            print(dict(row))
        
