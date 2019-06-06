#!/usr/bin/env /home/simsong/anaconda3/bin/python3
# -*- coding: utf-8 -*-

import re
import cgitb
import os
import sys
import datetime
import time
cgitb.enable()

sys.path.append( os.path.join(os.path.dirname(__file__),".."))

import dbrecon
import ctools.tydoc as tydoc

queries = [
    ('z','Current Time', 'select now()'),
    ('a',"Total states in database:",   "select count(distinct state) from tracts"),
    ('b',"Total counties in database:", "select count(distinct state,county) from tracts"),
    ('c',"Total tracts in database:",   "select count(*) from tracts"),
    ('d',"Number of LP files created in past hour:", "select count(*) from tracts where unix_timestamp() - unix_timestamp(lp_end) < 3600"),
    ('e',"Number of SOL files created in past hour:", "select count(*) from tracts where unix_timestamp() - unix_timestamp(sol_end) < 3600"),
    ('g',"LP Files created",             "SELECT sum(if(lp_end is not Null,1,0)) FROM tracts"),
    ('gg',"LP Files needed",             "SELECT sum(if(lp_end is Null,1,0)) FROM tracts"),
    ('h',"Solutions created",            "SELECT sum(if(sol_end is not Null,1,0)) FROM tracts"),
    ('hh',"Solutions Needed",            "SELECT sum(if(sol_end is Null,1,0)) FROM tracts"),
    (None, "LP files ready to solve",    "SELECT count(*) from tracts where lp_end is not null and sol_start is null"),
    (None,None,None),
    (None,"Current system load",
         "select sysload.host,sysload.t,unix_timestamp(now())-unix_timestamp(sysload.t),"
         "freegb,min1,min5,min15 from sysload inner join (select max(t) as t,host from sysload group by host) tops on sysload.t=tops.t and sysload.host=tops.host"),
    (None,"Completion of LP files at current rate:", "time.asctime(time.localtime(time.time()+int(3600*vals['gg']/vals['d']))) if vals['d']>0 else 'n/a'"),
    (None,"Completion of solutions at current rate:", "time.asctime(time.localtime(time.time()+int(3600*vals['hh']/vals['e']))) if vals['e']>0 else 'n/a'"),
    ('f',"Total completed LP and SOL files per state","select state,count(distinct county),count(*),sum(if(lp_end is not null,1,0)),sum(if(sol_end is not null,1,0)) from tracts group by state"),
    ('i',"Last 5 completed LP files:",  "SELECT state,county,tract,lp_end,now()-modified_at,lp_end-lp_start from tracts where lp_end IS NOT NULL order by lp_end DESC limit 5"),
    ('j',"Last 5 completed SOL files:", "SELECT state,county,tract,sol_end,now()-modified_at,sol_time from tracts where lp_end IS NOT NULL order by sol_end DESC limit 5"),
    (None,None,None),
    (None,"SOLs in progress",     "SELECT state,county,tract,sol_start from tracts where sol_start is not null and sol_end is null order by sol_start"),
    (None,"LP files in progress", "SELECT state,county,tract,lp_start from tracts where lp_start is not null and lp_end is null order by lp_start"),
    (None,None,None),
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
    config = dbrecon.get_config(filename="config.ini")

    doc = tydoc.tydoc()
    doc.head.add_tag('meta',attrib={'http-equiv':'refresh','content':'30'})
    doc.body.add_tag_text('p',"Report on reconstruction. All times in GMT.")

    table = tydoc.tytable()
    doc.body.append(table)
    vals = {}
    db = dbrecon.DB()
    db.connect()
    c = db.cursor()
    for (label,desc,query) in queries:
        if desc is None:
            table = tydoc.tytable()
            doc.body.append(table)
            continue
            
        if not query.upper().startswith('SELECT'):
            table.add_data([desc,str(eval(query))])
            continue
        c.execute(query)
        rows = c.fetchall()
        for row in rows:
            if desc: # Beginning of a new query
                d = desc
                desc = None
                if len(c.description)==1 and len(rows)==1:
                    v = row[0]
                    vals[label] = v
                    table.add_data([d]+[fmt(v)])
                    continue
                else:
                    table.add_data([d])   #should span
                    table.add_data([r[0] for r in c.description])
            table.add_data([fmt(r) for r in row])
    doc.render(sys.stdout , format='html')

    
    
   
