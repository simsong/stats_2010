#!/usr/bin/env python3
#
"""
s6_main.py:

Various maintenance functions. Feel free to add your own.
"""

import dbrecon
from dbrecon import DB,GB,MB
import glob
import logging
import os
import os.path
import subprocess
import sys
import time
import atexit

sys.path.append( os.path.join(os.path.dirname(__file__),".."))

import dbrecon
from dbrecon import DB
from dbrecon import dopen,dmakedirs,dsystem,dpath_exists,GB

from gurobi_logfile_parser import GurobiLogfileParser

import re

MFRE=re.compile("model_(\d\d)(\d\d\d)(\d\d\d\d\d\d)[.]log")
def model_filename_to_sct(fname):
    m = MFRE.search(fname)
    (state,county,tract) = m.group(1,2,3)
    return {'state':dbrecon.state_abbr(state), 'county':county, 'tract':tract}
    

def glog_scan_root(rootdir):
    for root, dirs, files in os.walk(rootdir):
        print(root)
        for fname in files:
            if fname.startswith("model") and fname.endswith(".log"):
                extra = model_filename_to_sct(fname)
                glog = GurobiLogfileParser(os.path.join(root,fname))
                try:
                    (cmd, vals) = glog.sql_insert(name='glog', dialect='mysql', extra=extra)
                except KeyError as e:
                    print("key error. glog:",glog.dict,"extra=",extra)
                    print(fname)
                    print(e)
                    exit(1)
                DB.csfr(cmd=cmd, vals=vals, quiet=True)
                print(fname)

def final_pop_scan():
    rows = DB.csfr("SELECT stusab, county, tract from tracts where final_pop is null")
    for (stusab,county,tract) in rows:
        try:
            final_pop = dbrecon.get_final_pop_from_sol(stusab, county, tract)
        except FileNotFoundError:
            print(f"{stusab} {county} {tract} has no solution. Removing")
            DB.csfr("UPDATE tracts set sol_start=NULL, sol_end=NULL where stusab=%s and county=%s and tract=%s",(stusab,county,tract))
        else:
            DB.csfr("UPDATE tracts set final_pop=%s where stusab=%s and county=%s and tract=%s",(final_pop,stusab,county,tract))

if __name__=="__main__":
    from argparse import ArgumentParser,ArgumentDefaultsHelpFormatter
    parser = ArgumentParser( formatter_class = ArgumentDefaultsHelpFormatter,
                             description="Analyze Gurobi logs. " )
    dbrecon.argparse_add_logging(parser)
    parser.add_argument("--schema",  help="drop the glog table and recreate it", action='store_true')
    parser.add_argument("--clear",  help="delete the records in the glog database table", action='store_true')
    parser.add_argument("--glog", help="Look for gurobi logfiles and import them into the glog database", action='store_true')
    parser.add_argument("roots", help="directories to scan for logfiles", nargs="*")
    parser.add_argument("--final_pop", help="Update final_pop in the tracts database for every tract that doesn't have final pop set", action='store_true')
    parser.add_argument("--validate", help="Show those tracts where final_pop != pop100", action='store_true')
    parser.add_argument("--rm", help="Remove the bad ones", action='store_true')

    args       = parser.parse_args()
    config     = dbrecon.setup_logging_and_get_config(args=args,prefix="06analyze")

    if args.clear or args.schema:
        glog = GurobiLogfileParser("tests/model_04001944300.log")
        if args.schema:
            DB.csfr("DROP TABLE IF EXISTS glog")
            DB.csfr(glog.sql_schema())
        if args.clear:
            DB.csfr("delete from glog")

    if args.final_pop:
        final_pop_scan()
        exit(0)

    if args.validate:
        bad = DB.csfr("SELECT t.stusab,t.county,t.tract,t.final_pop,g.pop100 FROM tracts t LEFT JOIN geo g "
                      "ON t.state=g.state AND t.county=g.county AND t.tract=g.tract WHERE g.sumlev=140 AND t.final_pop != g.pop100")
        for (stusab,county,tract,final_pop,pop100) in bad:
            print(f"{stusab} {county} {tract} {final_pop} != {pop100}")
            if args.rm:
                DB.csfr("UPDATE tracts set lp_start=Null,lp_end=null,sol_start=null,sol_end=null,hostlock=null where stusab=%s and county=%s and tract=%s",
                        (stusab,county,tract))
                dbrecon.dpath_unlink(LPFILENAMEGZ(state_abbr=stusab,county=county,tract=tract))
                dbrecon.dpath_unlink(SOLFILENAMEGZ(state_abbr=stusab,county=county,tract=tract))

    if args.glog:
        for root in args.roots:
            glog_scan_root(root)
    
