#!/usr/bin/env python3
#
"""
scheduler.py:

Synthesize the LP files and run Gurobi on a tract-by-tract basis. 
"""

import copy
import dbrecon
import logging
import os
import os.path
import subprocess
import sys
import time
import xml.etree.ElementTree as ET

sys.path.append( os.path.join(os.path.dirname(__file__),".."))

from dbrecon import dopen,dmakedirs,dsystem
from dfxml.python.dfxml.writer import DFXMLWriter
from dbrecon import DB

SCHEMA_FILENAME="schema.sql"                
SLEEP_TIME=60

################################################################
## These are Memoized because they are only used for init() and rescan()
@dbrecon.Memoize
def county_csv_exists(state_abbr,county):
    return dbrecon.COUNTY_CSV_FILENAME(state_abbr=state_abbr, county=county)

@dbrecon.Memoize
def tracts_with_files(s, c, w):
    return dbrecon.tracts_with_files(s, c, w)

from dbrecon import filename_mtime,final_pop
def init_sct(c,state_abbr,county,tract):
    lpfilename = dbrecon.find_lp_filename(state_abbr=state_abbr,county=county,tract=tract)
    lptime = filename_mtime( lpfilename )
    soltime = filename_mtime( dbrecon.SOLFILENAME(state_abbr=state_abbr,county=county, tract=tract) )
    DB().select_and_fetchall("INSERT INTO tracts (state,county,tract,lp_end,sol_end,final_pop) values (%s,%s,%s,%s,%s,%s)",
                             (state_abbr,county,tract,lptime,soltime,
                              final_pop(state_abbr,county,tract)))
    DB().commit()

def refresh():
    for state_abbr in dbrecon.all_state_abbrs():
        print(state_abbr)
        for county in dbrecon.counties_for_state(state_abbr=state_abbr):
            print(county," ",end='')
            for tract in dbrecon.tracts_for_state_county(state_abbr=state_abbr,county=county):
                dbrecon.refresh_db(state_abbr,county,tract)

def clean():
    db = dbrecon.DB()
    c  = db.cursor()
    for root, dirs, files in os.walk( dbrecon.dpath_expand("$ROOT") ):
        for fname in files:
            # Do not clean the CSVs
            path = os.path.join(root, fname)
            sz   = os.path.getsize(path)
            if path.endswith(".csv"):
                continue
            if path.endswith(".csv-done"):
                continue
            if sz < 100:
                print(path,sz)
                m = dbrecon.extract_state_county_tract(fname)
                if m is None:
                    continue
                (state_abbr,county,tract) = m
                what = "sol" if "sol" in path else "lp"
                DB().select_and_fetchall(f"UPDATE tracts SET {what}_start=NULL,{what}_end=NULL "
                                         "where state=%s and county=%s and tract=%s",
                                         (state_abbr, county, tract))
                DB().commit()
                os.unlink(path)


def init():
    raise RuntimeError("Don't run init anymore")
    db = dbrecon.DB()
    db.create_schema(open(SCHEMA_FILENAME).read())
    print("schema loaded")
    for state_abbr in dbrecon.all_state_abbrs():
        for county in dbrecon.counties_for_state(state_abbr=state_abbr):
            for tract in dbrecon.tracts_for_state_county(state_abbr=state_abbr,county=county):
                init_sct(c,state_abbr,county,tract)
        db.commit()

                      
LP='lp'
SOL='sol'
class SCT:
    def __init__(self,state,county,tract):
        self.state = state
        self.county = county
        self.tract  = tract
        


MAX_LOAD     = 50
MAX_LP       = 2
MAX_CHILDREN = 10
# This is a simple scheduler for a single system. A distributed scheduler would be easier: we would just schedule everything.
def run():
    running = set()
    running_lp = set()
    while True:
        # See if any of the processes have finished
        for p in copy.copy(running):
            if p.poll() is not None:
                print("PROCESS FINISHED: "," ".join(p.args))
                running.remove(p)
                if p in running_lp:
                    running_lp.remove(p)

        # See if we need to create more processes
        while len(running) < MAX_CHILDREN:
            # The LP makers take a lot of memory, so if we aren't running less than two, run up to two.
            # Order by lp_start to make it least likely to start where there is another process running
            load = os.getloadavg()[0]
            if load>MAX_LOAD:
                logging.info(f"Load {load} to high.")
            else:
                if not args.nolp:
                    needed =  MAX_LP - len(running_lp) 
                    make_lps = DB().select_and_fetchall("SELECT state,county,count(*) FROM tracts WHERE lp_end IS NULL GROUP BY state,county order BY lp_start,3 DESC LIMIT %s",(needed,))
                    for (state,county,tract_count) in make_lps:
                        # If the load average is too high, don't do it
                        print("WILL MAKE LP",'s3_pandas_synth_lp_files.py',state,county,"TRACTS:",tract_count)
                        cmd = [sys.executable,'s3_pandas_synth_lp_files.py',state,county,'--j1','1']
                        if args.dry_run:
                            print(" ".join(cmd))
                            exit(1)
                        p = subprocess.Popen(cmd)
                        running.add(p)
                        running_lp.add(p)

                if not args.nosol:
                    # Run any solvers that we have room for
                    needed = MAX_CHILDREN-len(running)
                    solve_lps = DB().select_and_fetchall("select state,county,tract from tracts where sol_end is NULL and lp_end IS NOT NULL ORDER BY sol_start LIMIT %s",(needed,))
                    for (state,county,tract) in solve_lps:
                        print("WILL SOLVE ",state,county,tract)
                        cmd=[sys.executable,'s4_run_gurobi.py',state,county,tract]
                        if args.dry_run:
                            print(" ".join(cmd))
                            exit(1)
                        p = subprocess.Popen(cmd)
                        running.add(p)
            # print current tasks
            print(f"Load: {load}")
            for p in running:
                print(" ".join(p.args))
            print("----------")
            time.sleep(SLEEP_TIME)
            # and repeat 


def process_dfxml(dfxml):
    root = ET.parse(dfxml)
    start_time = root.find(".//start_time").text[0:19].replace("T"," ")
    command_line = " ".join(root.find("//command_line").text.split()[1:])
    maxrss = 0
    for e in root.findall("//rusage/maxrss"):
        maxrss += int(e.text)
    print(start_time,command_line,maxrss)

if __name__=="__main__":
    from argparse import ArgumentParser,ArgumentDefaultsHelpFormatter
    parser = ArgumentParser( formatter_class = ArgumentDefaultsHelpFormatter,
                             description="Maintains a database of reconstruction and schedule "
                             "next work if the CPU load and memory use is not too high." ) 
    dbrecon.argparse_add_logging(parser)
    parser.add_argument("--init",    help="Clear database and learn the current configuration", action='store_true')
    parser.add_argument("--config",  help="config file")
    parser.add_argument("--testdb",  help="test database connection", action='store_true')
    parser.add_argument("--refresh", help="scan all of the files and update the database if we find any missing LP or Solution files",
                        action='store_true')
    parser.add_argument("--clean",   help="Look for .lp and .sol files that are too slow and delete them, then remove them from the database", action='store_true')
    parser.add_argument("--nosol",   help="Do not run the solver", action='store_true')
    parser.add_argument("--nolp",    help="Do not run the LP maker", action='store_true')
    parser.add_argument("--dry_run", help="Just report what the next thing to run would be, then quit", action='store_true')
    
    args   = parser.parse_args()
    config = dbrecon.setup_logging_and_get_config(args,prefix='sch_')

    if args.testdb:
        db = dbrecon.DB(config)
        c = db.cursor()
        print("Tables:")
        rows = DB().select_and_fetchall("show tables")
        for row in rows:
            print(row)
        exit(0)

    if args.init:
        init()

    if args.refresh:
        refresh()

    if args.clean:
        clean()

    run()
