#!/usr/bin/env python3
#
"""
s6_analyze_gurobi_logs:

Ingest the gurobi logs into a database. 
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
    

def scan_root(root):
    for root, dirs, files in os.walk( dbrecon.dpath_expand("$ROOT") ):
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
                DB.csfr(cmd=cmd, vals=vals)

if __name__=="__main__":
    from argparse import ArgumentParser,ArgumentDefaultsHelpFormatter
    parser = ArgumentParser( formatter_class = ArgumentDefaultsHelpFormatter,
                             description="Analyze Gurobi logs. " )
    dbrecon.argparse_add_logging(parser)
    parser.add_argument("--ingest", help="Ingest the logfiles that haven't been ingested yet",
                            action='store_true')
    parser.add_argument("--schema",  help="drop the table and recreate it", action='store_true')
    parser.add_argument("--clear",  help="delete the records in the database table", action='store_true')
    parser.add_argument("--report", help="Report what's in the database", action='store_true')
    parser.add_argument("roots", help="directories to scan for logfiles", nargs="*")

    args       = parser.parse_args()
    config     = dbrecon.setup_logging_and_get_config(args,prefix="06analyze")

    if args.clear or args.schema:
        glog = GurobiLogfileParser("tests/model_04001944300.log")
        if args.schema:
            DB.csfr("DROP TABLE IF EXISTS glog")
            DB.csfr(glog.sql_schema())
        if args.clear:
            DB.csfr("delete from table glog")

    for root in args.roots:
        scan_root(root)
    
