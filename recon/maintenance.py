#!/usr/bin/env python3
# -*- mode: python -*-
#
"""
summarize.py:

summarize das_sysload into das_sysload_summary and das_tokens into das_tokens_summary

"""

import os
import argparse
import sys
import subprocess
import re

import ctools
import ctools.lock
import ctools.env as env
import ctools.dbfile as dbfile


if __name__=="__main__":
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--debug",action="store_true")
    args   = parser.parse_args()

    # Be sure only one copy is running
    ctools.lock.lock_script()

    env.get_census_env()
    env.get_env( os.path.join(env.get_home(), "dbwriter.bash") )

    auth = dbfile.DBMySQLAuth(host=os.environ['MYSQL_HOST'],
                              database=os.environ['MYSQL_DATABASE'],
                              user=os.environ['MYSQL_USER'],
                              password=os.environ['MYSQL_PASSWORD'])
                              
    dbfile.DBMySQL.csfr(auth,"""INSERT INTO das_sysload_summary
    (t,host,ipaddr,min1_min,min1_avg,min1_max,freegb_min,freegb_avg,freegb_max,n)
    SELECT t,host,ipaddr,min1_min,min1_avg,min1_max,freegb_min,freegb_avg,freegb_max,n
    FROM (select dayhour as t,
            host, ipaddr,
            min(min1) as min1_min,
            avg(min1) as min1_avg,
            max(min1) as min1_max,
            min(freegb) as freegb_min,
            avg(freegb) as freegb_avg,
            max(freegb) as freegb_max,
            count(*) as n
     FROM (select from_unixtime(unix_timestamp(date(t))+3600*hour(t)) AS dayhour,host,ipaddr,min1,freegb FROM das_sysload)
           as cte GROUP BY dayhour,host,ipaddr) AS nums ON DUPLICATE KEY UPDATE das_sysload_summary.t=das_sysload_summary.t""")
           
     dbfile.DBMySQL.csfr(auth,"""DELETE FROM das_sysload where timestampdiff(day,t,now())>7""")
