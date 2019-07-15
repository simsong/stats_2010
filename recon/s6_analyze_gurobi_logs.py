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
from ctools.schema.table import Table


if __name__=="__main__":
    from argparse import ArgumentParser,ArgumentDefaultsHelpFormatter
    parser = ArgumentParser( formatter_class = ArgumentDefaultsHelpFormatter,
                             description="Analyze Gurobi logs. " )
    dbrecon.argparse_add_logging(parser)
    parser.add_argument("--ingest", help="Ingest the logfiles that haven't been ingested yet", action='store_true')
    parser.add_argument("--clear",  help="delete the database table and remake it", action='store_true')
    parser.add_argument("--report", help="Report what's in the database", action='store_true')
    parser.add_argument("roots", help="directories to scan for logfiles", nargs="*")

    args       = parser.parse_args()

    if args.clear:
        glog = GurobiLogfileParser("tests/model_04001944300.log")
        print(glog.sql_insert(table='glog'))
        exit(0)
        print(glog.sql_schema())
        DB.csfr("drop table glog")
        DB.csfr(glog.sql_schema())

    for root in args.roots:
        scan_root(root)
    
    

    print("glob:",glog.dict)

