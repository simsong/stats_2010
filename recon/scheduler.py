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
from dbrecon import DB,LP,SOL,MB,GB,MiB,GiB,get_config_int


# Tuning parameters

SCHEMA_FILENAME="schema.sql"                
SLEEP_TIME   = 5
MAX_LOAD     = 32
MAX_CHILDREN = 10
PYTHON_START_TIME = 5
MIN_FREE_MEM_FOR_LP  = 240*GiB
MIN_FREE_MEM_FOR_SOL = 100*GiB
MIN_FREE_MEM_FOR_KILLER = 5*GiB  # if less than this, start killing processes
REPORT_FREQUENCY = 60           # report this often
PROCESS_DIE_TIME = 5
LONG_SLEEP_MINUTES = 5

S3_SYNTH = 's3_pandas_synth_lp_files.py'
S4_RUN   = 's4_run_gurobi.py'

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

def rescan():
    states = [args.state] if args.state else dbrecon.all_state_abbrs()
    for state_abbr in states:
        counties = [args.county] if args.county else dbrecon.counties_for_state(state_abbr=state_abbr)
        for county in counties:
            print(f"RESCAN {state_abbr} {county}")
            for tract in dbrecon.tracts_for_state_county(state_abbr=state_abbr,county=county):
                dbrecon.rescan_files(state_abbr,county,tract)
        print()

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
    p = psutil.Popen(cmd)
    info = f"PID{p.pid}: LAUNCH {' '.join(cmd)}"
    logging.info(info)
    print(info)
    return p


def get_free_mem():
    return psutil.virtual_memory().available

last_report = 0
def report_load_memory(quiet=True):
    """Report and print the load and free memory; return free memory"""
    global last_report
    free_mem = get_free_mem()

    # print current tasks
    total_seconds = (time.time() - dbrecon.start_time)
    hours    = int(total_seconds // 3600)
    mins     = int((total_seconds % 3600) // 60)
    secs     = int(total_seconds % 60)
    print("Time: {} Running time: {}:{:02}:{:02} load: {}  free_GiB: {}".
          format(time.asctime(),hours,mins,secs,load(),round(get_free_mem()/GiB,2)))
    if last_report < time.time() + REPORT_FREQUENCY:
        dbrecon.DB.csfr("insert into sysload (t, host, min1, min5, min15, freegb) "
                        "values (now(), %s, %s, %s, %s, %s) ON DUPLICATE KEY update min1=min1", 
                        [socket.gethostname().partition('.')[0]] + list(os.getloadavg()) + [get_free_mem()//GiB],
                        quiet=quiet)
        last_report = time.time()
    return free_mem
    

def pcmd(p):
    """Return a process command"""
    return " ".join(p.args)

class PSTree():
    """Service class. Given a set of processes (or all of them), find parents that meet certain requirements."""
    def __init__(self,plist=psutil.process_iter()):
        self.plist = [(psutil.Process(p) if isinstance(p,int) else p) for p in plist]

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return

    def total_rss(self,p):
        """Return the total rss for the process and all of its children."""
        return (p.memory_info().rss +
                sum([child.memory_info().rss for child in p.children(recursive=True)]))

    def total_user_time(self,p):
        return (p.cpu_times().user + 
                sum([child.cpu_times().user for child in p.children(recursive=True)]))

    def ps_aux(self):
        for p in sorted(self.plist, key=lambda p:p.pid):
            print("PID{}: {:,} MiB {} children {} ".format(
                p.pid, int(self.total_rss(p)/MiB), len(p.children(recursive=True)), pcmd(p)))

    def youngest(self):
        return sorted(self.plist, key=lambda p:self.total_user_time(p))[0]

#
# Note: change running() into a dictionary where the start time is the key
# Then report for each job how long it has been running.
# Modify this to track the total number of bytes by all child processes

def run():
    running     = set()

    def running_lp():
        """Return a list of the runn LP makers"""
        return [p for p in running if p.args[1]==S3_SYNTH]

    while True:
        # Report system usage if necessary
        dbrecon.config_reload()
        free_mem = report_load_memory()

        # See if any of the processes have finished
        for p in copy.copy(running):
            if p.poll() is not None:
                logging.info(f"PID{p.pid}: EXITED {pcmd(p)} code: {p.returncode}")
                if p.returncode!=0:
                    logging.error(f"ERROR: Process {p.pid} did not exit cleanly. retcode={p.returncode} mypid={os.getpid()} ")
                    exit(1)     # hard fail
                running.remove(p)

        with PSTree(running) as ps:
            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n")
            ps.ps_aux()
            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n")

            if free_mem < MIN_FREE_MEM_FOR_KILLER:
                logging.error("%%%")
                logging.error("%%% Free memory down to {:,} -- will start killing processes.".format(get_free_mem()))
                logging.error("%%%")
                subprocess.call(['ps','auxww'])
                if len(running)==0:
                    logging.error("No more processes to kill. Waiting for {} minutes and restarting".format(LONG_SLEEP_MINUTES))
                    time.sleep(LONG_SLEEP_MINUTES*60)
                    continue
                p = ps.youngest()
                logging.warning("KILL "+pcmd(p))
                p.kill()
                time.sleep(PROCESS_DIE_TIME) # give process a few moments to adjust
                p.poll()                     # clear the exit code
                running.remote()
                continue
            
        if dbrecon.should_stop():
            if len(running)==0:
                dbrecon.check_stop()
            else:
                print("Waiting for stop...")
                time.sleep(PROCESS_DIE_TIME)
                continue

        # See if we can create another process. 
        # For stability, we create a max of one LP and one SOL each time through.

        # The LP makers take a lot of memory, so if we aren't running less than two, run up to two.
        # Order by lp_start to make it least likely to start where there is another process running
        if args.nolp:
            needed_lp = 0
        else:
            needed_lp =  get_config_int('run','max_lp') - len(running_lp())
        if (get_free_mem()>MIN_FREE_MEM_FOR_LP) and needed_lp>0:
            needed_lp = 1
            make_lps = DB.csfr("SELECT state,county,count(*) FROM tracts "
                               "WHERE (lp_end IS NULL) and (hostlock IS NULL) and (error IS NULL) GROUP BY state,county "
                               "order BY RAND() DESC LIMIT %s", (needed_lp,))
            for (state,county,tract_count) in make_lps:
                # If the load average is too high, don't do it
                lp_j1 = get_config_int('run','lp_j1')
                lp_j2 = get_config_int('run','lp_j2')
                print("WILL MAKE LP",S3_SYNTH,
                      state,county,"TRACTS:",tract_count)
                p = prun([sys.executable,'s3_pandas_synth_lp_files.py',
                          '--j1', str(lp_j1), '--j2', str(lp_j2), state, county])
                running.add(p)
                time.sleep(PYTHON_START_TIME) # give load 5 seconds to adjust

        if args.nosol:
            needed_sol = 0
        else:
            needed_sol = get_config_int('run','max_jobs')-len(running)
        if get_free_mem()>MIN_FREE_MEM_FOR_SOL and needed_sol>0:
            # Run any solvers that we have room for
            needed_sol = 1
            gurobi_threads = get_config_int('gurobi','threads')
            solve_lps = DB.csfr("SELECT state,county,tract FROM tracts "
                                "WHERE (sol_end IS NULL) AND (lp_end IS NOT NULL) AND (hostlock IS NULL) and (error IS NULL) "
                                "ORDER BY sol_start,RAND() LIMIT %s",(needed_sol,))
            for (state,county,tract) in solve_lps:
                print("WILL SOLVE ",state,county,tract)
                p = prun([sys.executable,S4_RUN,'--j1','1','--j2',str(gurobi_threads),state,county,tract])
                running.add(p)
                time.sleep(PYTHON_START_TIME)

        print("="*64)
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
    parser.add_argument("--rescan", help="scan all of the files and update the database if we find any missing LP or Solution files",
                        action='store_true')
    parser.add_argument("--clean",   help="Look for .lp and .sol files that are too slow and delete them, then remove them from the database", action='store_true')
    parser.add_argument("--nosol",   help="Do not run the solver", action='store_true')
    parser.add_argument("--nolp",    help="Do not run the LP maker", action='store_true')
    parser.add_argument("--none_running", help="Run if there are no outstanding LP files being built or Solutions being solved; clears them from database", action='store_true')
    parser.add_argument("--dry_run", help="Just report what the next thing to run would be, then quit", action='store_true')
    parser.add_argument("--state", help="state for rescanning")
    parser.add_argument("--county", help="county for rescanning")
    
    args   = parser.parse_args()
    args.stdout = True          # for now, always log to stdout
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

    elif args.rescan:
        rescan()

    elif args.clean:
        clean()

    elif args.none_running:
        non_running()
    else:
        run()
