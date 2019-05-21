#!/usr/bin/env /home/simsong/anaconda3/bin/python3
# -*- coding: utf-8 -*-

import re
import cgitb
import os
import sys
import datetime
cgitb.enable()

import dbrecon

queries = [
    ("Total states in database:", "select count(distinct state) from tracts"),
    ("Total counties in database:", "select count(distinct state,county) from tracts"),
    ("Total tracts in database:", "select count(*) from tracts"),
    ("Tracts with completed LP files:", "SELECT COUNT(*) FROM tracts WHERE  lp_end IS NOT NULL"),
    ("Tracts with completed SOL files:", "SELECT COUNT(*) FROM tracts WHERE  sol_end IS NOT NULL"),
    ("Last 5 completed LP files:", "SELECT state,county,tract,lp_end from tracts where lp_end IS NOT NULL order by lp_end DESC limit 5"),
    ("Last 5 completed SOL files:", "SELECT state,county,tract,lp_end from tracts where lp_end IS NOT NULL order by sol_end DESC limit 5"),
    ]

db_re = re.compile("export (.*)=(.*)")
def get_pw():
    with open( os.path.join('/home/simsong', 'dbrecon.bash')) as f:
        for line in f:
            m = db_re.search(line.strip())
            if m:
                os.environ[m.group(1)] = m.group(2)

def fmt(r):
    if isinstance(r,int):
        return "{:,}".format(r)
    if isinstance(r,datetime.datetime):
        return r.isoformat()
    return str(r)

if __name__=="__main__":
    print("Content-Type: text/plain;charset=utf-8")
    print()
    print("Hello World!")
    get_pw()
    config = dbrecon.get_config("config.ini")
    db = dbrecon.DB()
    c = db.cursor()
    print("Queries:")

    for (desc,query) in queries:
        c.execute(query)
        for row in c.fetchall():
            print(desc," ".join([fmt(r) for r in row]))
            desc = '     '

    
    
   
