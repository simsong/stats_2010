#!/usr/bin/env /home/simsong/anaconda3/bin/python3
# -*- coding: utf-8 -*-

import re
import cgitb
import os
import sys
import datetime
cgitb.enable()

sys.path.append( os.path.join(os.path.dirname(__file__),".."))

import dbrecon
import ctools.tydoc as tydoc

queries = [
    ("Total states in database:", "select count(distinct state) from tracts"),
    ("Total counties in database:", "select count(distinct state,county) from tracts"),
    ("Total tracts in database:", "select count(*) from tracts"),
    ("Tracts with completed LP files:", "SELECT COUNT(*) FROM tracts WHERE  lp_end IS NOT NULL"),
    ("Tracts with completed SOL files:", "SELECT COUNT(*) FROM tracts WHERE  sol_end IS NOT NULL"),
    ("Last 5 completed LP files:", "SELECT state,county,tract,lp_end from tracts where lp_end IS NOT NULL order by lp_end DESC limit 5"),
    ("Last 5 completed SOL files:", "SELECT state,county,tract,lp_end from tracts where lp_end IS NOT NULL order by sol_end DESC limit 5"),
    (None,None),
    ("Last 5 system load","select t,min1,min5,min15 from sysload order by t desc limit 5"),
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
        timestr = (r - datetime.timedelta(hours=4)).isoformat()
        timestr = timestr.replace("T"," ")
    return str(r)

if __name__=="__main__":
    print("Content-Type: text/html;charset=utf-8\r\n\r\n")
    get_pw()
    config = dbrecon.get_config("config.ini")
    db = dbrecon.DB()
    c = db.cursor()

    doc = tydoc.tydoc()
    doc.head.add_tag('meta',attrib={'http-equiv':'refresh','content':'30'})
    doc.body.add_tag_text('p',"Report on reconstruction. All times in GMT.")

    table = tydoc.tytable()
    doc.body.append(table)
    for (desc,query) in queries:
        if desc is None:
            table = tydoc.tytable()
            doc.body.append(table)
            continue
            
        c.execute(query)
        for row in c.fetchall():
            table.add_data([desc] + [fmt(r) for r in row])
            desc = ''
    doc.render(sys.stdout , format='html')

    
    
   
