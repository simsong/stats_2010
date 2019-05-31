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
import psutil
import socket

sys.path.append( os.path.join(os.path.dirname(__file__),".."))

from dbrecon import dopen,dmakedirs,dsystem
from dfxml.python.dfxml.writer import DFXMLWriter
from dbrecon import DB

CLEANEXIT_FILE='cleanexit.txt'

# Tuning parameters

SCHEMA_FILENAME="schema.sql"                
SLEEP_TIME   = 5
MAX_LOAD     = 32
MAX_LP       = 1
MAX_CHILDREN = 10
PYTHON_START_TIME = 5
MB          = 1024*1024
GB          = MB * 1024
MIN_FREE_MEM_FOR_LP  = 240*GB
MIN_FREE_MEM_FOR_SOL = 100*GB
REPORT_FREQUENCY = 60          # report this often

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
    DB.csfr("INSERT INTO tracts (state,county,tract,lp_end,sol_end,final_pop) values (%s,%s,%s,%s,%s,%s)",
            (state_abbr,county,tract,lptime,soltime, final_pop(state_abbr,county,tract)))

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
                DB.csfr(f"UPDATE tracts SET {what}_start=NULL,{what}_end=NULL "
                        "where state=%s and county=%s and tract=%s",
                        (state_abbr, county, tract))
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
        
# This is a simple scheduler for a single system. A distributed scheduler would be easier: we would just schedule everything.
def load():
    return os.getloadavg()[0]

def prun(cmd):
    """Run Popen unless we are in debug mode"""
    if args.dry_run:
        print(" ".join(cmd))
        exit(1)
    return subprocess.Popen(cmd)


def freemem():
    return psutil.virtual_memory().available

last_report = 0
def report_load_memory(quiet=True):
    global last_report
    if last_report < time.time() + REPORT_FREQUENCY:
        dbrecon.DB.csfr("insert into sysload (t, host, min1, min5, min15, freegb) values (now(), %s, %s, %s, %s, %s) ON DUPLICATE KEY IGNORE", 
                        [socket.gethostname().partition('.')[0]] + list(os.getloadavg()) + [freemem()//GB],
                        quiet=quiet)
        last_report = time.time()
    
def run():
    running     = set()
    running_lp  = set()
    while True:
        # Report system usage if necessary
        report_load_memory()

        # See if any of the processes have finished
        for p in copy.copy(running):
            if p.poll() is not None:
                print(f"PROCESS {p.pid} FINISHED: {','.join(p.args)} code: {p.returncode}")
                if p.returncode!=0:
                    logging.error(f"Process {p.pid} did not exit cleanly ")
                running.remove(p)
                if p in running_lp:
                    running_lp.remove(p)

        # print current tasks
        print("{}: load: {}  free_gb: {}".format(time.asctime(),load(),round(freemem()/GB,2)))
        for p in sorted(running, key=lambda p:p.args):
            print(" ".join(p.args))
        print("---")

        clean_exit = os.path.exists(CLEANEXIT_FILE)
        if clean_exit and len(running)==0:
            print("Clean exit")
            os.unlink(CLEANEXIT_FILE)
            return

        # See if we can create another process. 
        # For stability, we create a max of one LP and one SOL each time through.

        # The LP makers take a lot of memory, so if we aren't running less than two, run up to two.
        # Order by lp_start to make it least likely to start where there is another process running
        needed_lp =  MAX_LP - len(running_lp) 
        print(f"needed_lp: {needed_lp}")
        if (not args.nolp) and (freemem()>MIN_FREE_MEM_FOR_LP) and needed_lp>0 and (not clean_exit):
            needed_lp = 1
            make_lps = DB.csfr("SELECT state,county,count(*) FROM tracts "
                               "WHERE lp_end IS NULL GROUP BY state,county "
                               "order BY RAND() DESC LIMIT %s", (needed_lp,))
            for (state,county,tract_count) in make_lps:
                # If the load average is too high, don't do it
                print("WILL MAKE LP",'s3_pandas_synth_lp_files.py',state,county,"TRACTS:",tract_count)
                p = prun([sys.executable,'s3_pandas_synth_lp_files.py',state,county,'--j1','1'])
                running.add(p)
                running_lp.add(p)
                time.sleep(PYTHON_START_TIME) # give load 5 seconds to adjust

        needed_sol = MAX_CHILDREN-len(running)
        print(f"needed_sol: {needed_sol}")
        if (not args.nosol) and freemem()>MIN_FREE_MEM_FOR_SOL and needed_sol>0 and (not clean_exit):
            # Run any solvers that we have room for
            needed_sol = 1
            solve_lps = DB.csfr("SELECT state,county,tract FROM tracts "
                                "WHERE sol_end IS NULL AND lp_end IS NOT NULL "
                                "ORDER BY sol_start,RAND() LIMIT %s",(needed_sol,))
            for (state,county,tract) in solve_lps:
                print("WILL SOLVE ",state,county,tract)
                p = prun([sys.executable,'s4_run_gurobi.py',state,county,tract])
                running.add(p)
                time.sleep(PYTHON_START_TIME)

        print("------")
        time.sleep(SLEEP_TIME)
        # and repeat
    # Should never get here

def non_running():
    print("LP in progress:")
    for (state,county,tract) in  DB.csfr("SELECT state,county,tract FROM tracts WHERE lp_start IS NOT NULL AND lp_end IS NULL"):
        print(state,county,tract)
    DB.csfr("UPDATE tracts set lp_start=NULL WHERE lp_start IS NOT NULL and lp_end is NULL")
        
    print("SOL in progress:")
    for (state,county,tract) in  DB.csfr("SELECT state,county,tract FROM tracts WHERE sol_start IS NOT NULL AND sol_end IS NULL"):
        print(state,county,tract)
    DB.csfr("UPDATE tracts set sol_start=NULL WHERE sol_start IS NOT NULL AND sol_end IS NULL")



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
    parser.add_argument("--none_running", help="Run if there are no outstanding LP files being built or Solutions being solved; clears them from database", action='store_true')
    parser.add_argument("--dry_run", help="Just report what the next thing to run would be, then quit", action='store_true')
    
    args   = parser.parse_args()
    config = dbrecon.setup_logging_and_get_config(args,prefix='sch_')

    if args.testdb:
        db = dbrecon.DB(config)
        c = db.cursor()
        print("Tables:")
        rows = db.csfr("show tables")
        for row in rows:
            print(row)


    elif args.init:
        init()

    elif args.refresh:
        refresh()

    elif args.clean:
        clean()

    elif args.none_running:
        non_running()
    else:
        run()
