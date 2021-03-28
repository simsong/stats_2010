#!/usr/bin/env python3
# -*- mode: python -*-
#
"""
maintenance.py

Just a little script for doing maintenance on the databse. It shouldn't be necessary to use this program.

"""

import os
import argparse
import sys
import subprocess
import re

sys.path.append( os.path.join(os.path.dirname(__file__),".."))

import dbrecon
import ctools
import ctools.lock
import ctools.env as env
import ctools.dbfile as dbfile
from dbrecon import REIDENT,DB


def fix_states(auth):
    db = dbrecon.DB()
    db.connect()
    c = db.cursor()
    c.execute("show tables")
    print("tables: ")
    for row in c:
        print(row[0])
    for sa in dbrecon.all_stusabs():
        fips = dbrecon.state_fips(sa)
        print(sa,fips)
        c = db.cursor()
        c.execute(
            f"""
            UPDATE {REIDENT}tracts
            SET state=%s
            WHERE stusab=%s
            """,(fips,sa))
        print("Changed:",c.rowcount)
        db.commit()

def summarize(auth):
    dbfile.DBMySQL.csfr(auth,f"""INSERT INTO das_sysload_summary
    (t,host,ipaddr,min1_min,min1_avg,min1_max,freegb_min,freegb_avg,freegb_max,n)
    SELECT t,host,ipaddr,min1_min,min1_avg,min1_max,freegb_min,freegb_avg,freegb_max,n
    FROM (SELECT dayhour as t,
            host, ipaddr,
            min(min1) as min1_min,
            avg(min1) as min1_avg,
            max(min1) as min1_max,
            min(freegb) as freegb_min,
            avg(freegb) as freegb_avg,
            max(freegb) as freegb_max,
            count(*) as n
     FROM (SELECT from_unixtime(unix_timestamp(date(t))+3600*hour(t)) AS dayhour,host,ipaddr,min1,freegb FROM das_sysload)
           as cte GROUP BY dayhour,host,ipaddr) AS nums ON DUPLICATE KEY UPDATE das_sysload_summary.t=das_sysload_summary.t""")

    dbfile.DBMySQL.csfr(auth,f"""DELETE FROM das_sysload where timestampdiff(day,t,now())>7""")

if __name__=="__main__":
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter, description='perform a maintneance task')
    dbrecon.argparse_add_logging(parser)
    parser.add_argument("--debug",action="store_true")
    parser.add_argument("--fix", action='store_true')
    args   = parser.parse_args()
    config = dbrecon.setup_logging_and_get_config(args=args,prefix="s9report")
    auth = dbrecon.auth()

    if args.fix:
        fix_states(auth)
        exit(0)
    summarize(auth)
