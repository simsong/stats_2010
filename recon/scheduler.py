#!/usr/bin/env python3
#
"""scheduler.py:

The two time-consuming parts of the reconstruction are building and
solving the LP files. This schedules the jobs on multiple machines
using a MySQL database for coordination.

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
import fcntl

sys.path.append( os.path.join(os.path.dirname(__file__),".."))

from dbrecon import dopen,dmakedirs,dsystem
from dfxml.python.dfxml.writer import DFXMLWriter
from dbrecon import DB,LP,SOL,MB,GB,MiB,GiB,get_config_int,REIDENT

HOSTNAME = dbrecon.hostname()

# Tuning parameters

SCHEMA_FILENAME="schema.sql"
PYTHON_START_TIME = 1
MIN_LP_WAIT  = 60
MIN_SOL_WAIT  = 60

# Failsafes: don't start an LP or SOL unless we have this much free
MIN_FREE_MEM_FOR_LP  = 100*GiB
MIN_FREE_MEM_FOR_SOL = 100*GiB

MIN_FREE_MEM_FOR_KILLER = 5*GiB  # if less than this, start killing processes

REPORT_FREQUENCY = 60           # report this often into sysload table

PROCESS_DIE_TIME = 5            # how long to wait for a process to die
LONG_SLEEP= 300          # sleep for this long (seconds) when there are no resources
PS_LIST_FREQUENCY = 60   #

S3_SYNTH = 's3_pandas_synth_lp_files.py'
S4_RUN   = 's4_run_gurobi.py'
LP_J1    = 1                    # let this program schedule

################################################################
## These are Memoized because they are only used for init() and rescan()

def rescan():
    stusabs = [args.stusab] if args.stusab else dbrecon.all_stusabs()
    for stusab in stusabs:
        counties = [args.county] if args.county else dbrecon.counties_for_state(stusab=stusab)
        for county in counties:
            print(f"RESCAN {stusab} {county}")
            for tract in dbrecon.tracts_for_state_county(stusab=stusab,county=county):
                dbrecon.rescan_files(stusab,county,tract,quiet=False)
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
                (stusab,county,tract) = m
                what = "sol" if "sol" in path else "lp"
                DB.csfr(f"UPDATE {REIDENT}tracts SET {what}_start=NULL,{what}_end=NULL "
                        "where stusab=%s and county=%s and tract=%s",
                        (stusab, county, tract))
                os.unlink(path)


class SCT:
    def __init__(self,stusab,county,tract):
        self.stusab = stusab
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
    return p


def get_free_mem():
    return psutil.virtual_memory().available

last_report = 0
def report_load_memory():
    """Report and print the load and free memory; return free memory"""
    global last_report
    free_mem = get_free_mem()

    # print current tasks
    total_seconds = (time.time() - dbrecon.start_time)
    hours    = int(total_seconds // 3600)
    mins     = int((total_seconds % 3600) // 60)
    secs     = int(total_seconds % 60)
    if time.time() > last_report + REPORT_FREQUENCY:
        dbrecon.DB.csfr(
            """
            INSERT INTO sysload (t, host, min1, min5, min15, freegb)
            VALUES (NOW(), %s, %s, %s, %s, %s) ON DUPLICATE KEY update min1=min1
            """,
            [HOSTNAME] + list(os.getloadavg()) + [get_free_mem()//GiB])
        last_report = time.time()
    return free_mem


def pcmd(p):
    """Return a process command"""
    return " ".join(p.args)

def kill_tree(p):
    print("PID{} KILL TREE {} ".format(p.pid,pcmd(p)))
    for child in p.children(recursive=True):
        try:
            print("   killing",child,end='')
            child.kill()
            print("   waiting...", end='')
            child.wait()
        except psutil.NoSuchProcess as e:
            pass
        finally:
            print("")
    p.kill()
    return p.wait()

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

    def ps_list(self):
        for p in sorted(self.plist, key=lambda p:p.pid):
            try:
                print("PID{}: {:,} MiB {} children {} ".format(
                    p.pid, int(self.total_rss(p)/MiB), len(p.children(recursive=True)), pcmd(p)))
                subprocess.call(f"ps wwx -o uname,pid,ppid,pcpu,etimes,vsz,rss,command --sort=-pcpu --ppid={p.pid}".split())
            except psutil.NoSuchProcess as e:
                continue

    def youngest(self):
        return sorted(self.plist, key=lambda p:self.total_user_time(p))[0]


#
# Note: change running() into a dictionary where the start time is the key
# Then report for each job how long it has been running.
# Modify this to track the total number of bytes by all child processes

def run():
    os.set_blocking(sys.stdin.fileno(), False)
    running     = set()
    last_ps_list     = 0
    quiet       = True
    last_lp_launch = 0
    last_sol_launch = 0

    def running_lp():
        """Return a list of the runn LP makers"""
        return [p for p in running if p.args[1]==S3_SYNTH]

    stop_requested = False
    while True:
        command = sys.stdin.read(256).strip().lower()
        if command!='':
            print("COMMAND:",command)
            if command=="halt":
                # Halt is like stop, except we kill the jobs first
                [kill_tree(p) for p in running]
                stop_requested = True
            elif command=='stop':
                stop_requested = True
            elif command.startswith('ps'):
                subprocess.call("ps ww -o uname,pid,ppid,pcpu,etimes,vsz,rss,command --sort=-pcpu".split())
            elif command=='list':
                last_ps_list = 0
            elif command=='uptime':
                subprocess.call(['uptime'])
            elif command=='noisy':
                quiet = False
                dbrecon.DB.quiet = False
            elif command=='quiet':
                quiet = True
                dbrecon.DB.quiet = True
            else:
                print(f"UNKNOWN COMMAND: '{command}'.  TRY HALT, STOP, PS, LIST, UPTIME, NOISY, QUIET")

        # Clean database if necessary
        dbrecon.db_clean()

        # Report system usage if necessary
        dbrecon.GetConfig().config_reload()
        free_mem = report_load_memory()

        # Are we done yet?
        remain = dbrecon.DB.csfr(f"SELECT count(*) from {REIDENT}tracts where sol_end is null",quiet=True)
        if remain[0][0]==0:
            print("All done!")
            break

        # See if any of the processes have finished
        for p in copy.copy(running):
            if p.poll() is not None:
                logging.info(f"PID{p.pid}: EXITED {pcmd(p)} code: {p.returncode}")
                if p.returncode!=0:
                    logging.error(f"ERROR: Process {p.pid} did not exit cleanly. retcode={p.returncode} mypid={os.getpid()} ")
                    exit(1)     # hard fail
                running.remove(p)

        SHOW_PS = False
        with PSTree(running) as ps:
            from unicodedata import lookup
            if ((time.time() > last_ps_list + PS_LIST_FREQUENCY) and SHOW_PS) or (last_ps_list==0):
                print("")
                print(lookup('BLACK DOWN-POINTING TRIANGLE')*64)
                print("{}: {} Free Memory: {} GiB  {}% Load: {}".format(
                    HOSTNAME,
                    time.asctime(), free_mem//GiB, psutil.virtual_memory().percent, os.getloadavg()))
                print("")
                ps.ps_list()
                print(lookup('BLACK UP-POINTING TRIANGLE')*64+"\n")
                last_ps_list = time.time()

            if free_mem < MIN_FREE_MEM_FOR_KILLER:
                logging.error("%%%")
                logging.error("%%% Free memory down to {:,} -- will start killing processes.".format(get_free_mem()))
                logging.error("%%%")
                subprocess.call(['./pps.sh'])
                if len(running)==0:
                    logging.error("No more processes to kill. Waiting for %s seconds and restarting",
                                  LONG_SLEEP)
                    time.sleep(LONG_SLEEP)
                    continue
                p = ps.youngest()
                logging.warning("KILL "+pcmd(p))
                dbrecon.DB.csfr(f"INSERT INTO errors (host,file,error) VALUES (%s,%s,%s)",
                                (HOSTNAME,__file__,"Free memory down to {}".format(get_free_mem())))
                kill_tree(p)
                running.remove(p)
                continue

        if stop_requested:
            print("STOP REQUESTED")
            if len(running)==0:
                print("NONE LEFT. STOPPING.")
                break;
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
        if (get_free_mem()>MIN_FREE_MEM_FOR_LP) and (needed_lp>0) and (last_lp_launch + MIN_LP_WAIT < time.time()):
            # For now, only start one lp at a time
            if last_lp_launch + MIN_LP_WAIT > time.time():
                continue
            lp_limit = 1
            make_lps = DB.csfr(
                f"""
                SELECT stusab,county,count(*)
                FROM {REIDENT}tracts
                WHERE (lp_end IS NULL) AND (hostlock IS NULL)
                GROUP BY state,county
                ORDER BY RAND() DESC LIMIT %s
                """, (lp_limit,))
            if (len(make_lps)==0 and needed_lp>0) or not quiet:
                logging.warning(f"needed_lp: {needed_lp} but search produced 0. NO MORE LPS FOR NOW...")
                last_lp_launch = time.time()
            for (stusab,county,tract_count) in make_lps:
                # If the load average is too high, don't do it
                lp_j2 = get_config_int('run','lp_j2')
                print("WILL MAKE LP",S3_SYNTH, stusab,county,"TRACTS:",tract_count)

                stusab = stusab.lower()
                p = prun([sys.executable,'s3_pandas_synth_lp_files.py', '--j1', str(LP_J1), '--j2', str(lp_j2), stusab, county])
                running.add(p)
                last_lp_launch = time.time()

        ## Evaluate Launching SOLs

        if args.nosol:
            needed_sol = 0
        else:
            max_sol    = get_config_int('run','max_sol')
            max_jobs   = get_config_int('run','max_jobs')
            needed_sol = max_jobs-len(running)
            if not quiet:
                print(f"1: max_sol={max_sol} needed_sol={needed_sol} max_jobs={max_jobs} running={len(running)} ")
            if needed_sol > max_sol:
                needed_sol = max_sol
        if get_free_mem()>MIN_FREE_MEM_FOR_SOL and needed_sol>0:
            # Run any solvers that we have room for
            # For now, only launch one solver at a time
            max_sol_launch = get_config_int('run','max_sol_launch')
            limit_sol = max(needed_sol, max_sol_launch)
            if last_sol_launch + MIN_SOL_WAIT > time.time():
                continue
            solve_lps = DB.csfr(
                f"""
                SELECT stusab,county,tract FROM {REIDENT}tracts
                WHERE (sol_end IS NULL) AND (lp_end IS NOT NULL) AND (hostlock IS NULL)
                ORDER BY RAND() LIMIT %s
                """,(limit_sol,))
            if (len(solve_lps)==0 and needed_sol>0) or not quiet:
                print(f"2: needed_sol={needed_sol} len(solve_lps)={len(solve_lps)}")
            for (ct,(stusab,county,tract)) in enumerate(solve_lps,1):
                print("WILL SOLVE {} {} {} ({}/{}) {}".format(stusab,county,tract,ct,len(solve_lps),time.asctime()))
                gurobi_threads = get_config_int('gurobi','threads')
                dbrecon.db_lock(stusab,county,tract)
                stusab = stusab.lower()
                p = prun([sys.executable,S4_RUN,'--exit1','--j1','1','--j2',str(gurobi_threads),stusab,county,tract])
                running.add(p)
                time.sleep(PYTHON_START_TIME)
                last_sol_launch = time.time()

        time.sleep( get_config_int('run', 'sleep_time' ) )
        # and repeat
    # Should never get here

def none_running(hostname=None):
    hostlock = '' if hostname is None else f" AND (hostlock = '{hostname}') "
    print("LP in progress:")
    for (stusab,county,tract) in  DB.csfr(
            f"""
            SELECT stusab,county,tract
            FROM {REIDENT}tracts
            WHERE lp_start IS NOT NULL AND lp_end IS NULL
            """ + hostlock):
        print(stusab,county,tract)
    DB.csfr(
        f"""
        UPDATE {REIDENT}tracts
        SET lp_start=NULL
        WHERE lp_start IS NOT NULL AND lp_end IS NULL
        """ + hostlock)

    print("SOL in progress:")
    for (stusab,county,tract) in DB.csfr(
            f"""
            SELECT stusab,county,tract
            FROM {REIDENT}tracts
            WHERE sol_start IS NOT NULL AND sol_end IS NULL
            """ + hostlock):
        print(stusab,county,tract)
    DB.csfr(
        f"""
        UPDATE {REIDENT}tracts
        SET sol_start=NULL
        WHERE sol_start IS NOT NULL AND sol_end IS NULL
        """ + hostlock)
    print("Resume...")

def get_lock():
    """This version of get_lock() assumes a shared file system, so we can't lock __file__"""
    lockfile = f"/tmp/lockfile_{HOSTNAME}"
    if not os.path.exists(lockfile):
        with open(lockfile,"w") as lf:
            lf.write("lock")
    try:
        fd = os.open( lockfile, os.O_RDONLY )
        if fd>0:
            # non-blocking
            fcntl.flock(fd, fcntl.LOCK_EX|fcntl.LOCK_NB)
            return
    except IOError:
        pass
    logging.error("Could not acquire lock. Another copy of %s must be running",(__file__))
    raise RuntimeError("Could not acquire lock")

def scan_s3_s4():
    """Look for any running instances of s3 or s4. If they are found, print and abort"""
    found = 0
    for p in psutil.process_iter():
        cmd = p.cmdline()
        if (len(cmd) > 2) and cmd[0]==sys.executable and cmd[1] in (S3_SYNTH, S4_RUN):
            found += 1
            if found==1:
                print("Killing Running S3 and S4 Processes:")
            print("KILL PID{} {}".format(p.pid, " ".join(cmd)))
            p.kill()
            p.wait()

if __name__=="__main__":
    from argparse import ArgumentParser,ArgumentDefaultsHelpFormatter
    parser = ArgumentParser( formatter_class = ArgumentDefaultsHelpFormatter,
                             description="Maintains a database of reconstruction and schedule "
                             "next work if the CPU load and memory use is not too high." )
    dbrecon.argparse_add_logging(parser)
    parser.add_argument("--testdb",  help="test database connection", action='store_true')
    parser.add_argument("--rescan", help="scan all of the files and update the database if we find any missing LP or Solution files",
                        action='store_true')
    parser.add_argument("--clean",   help="Look for .lp and .sol files that are too slow and delete them, then remove them from the database", action='store_true')
    parser.add_argument("--nosol",   help="Do not run the solver", action='store_true')
    parser.add_argument("--nolp",    help="Do not run the LP maker", action='store_true')
    parser.add_argument("--none_running", help="Run if there are no outstanding LP files being built or Solutions being solved; clears them from database",
                        action='store_true')
    parser.add_argument("--none_running-anywhere", help="Run if there are no outstanding LP files being built or Solutions being solved anywhere.",
                        action='store_true')
    parser.add_argument("--dry_run", help="Just report what the next thing to run would be, then quit", action='store_true')
    parser.add_argument("--stusab", help="stusab for rescanning")
    parser.add_argument("--county", help="county for rescanning")

    args   = parser.parse_args()
    config = dbrecon.setup_logging_and_get_config(args=args,prefix='sch_')
    DB.quiet = True

    if args.testdb:
        print("Tables:")
        rows = DB.csfr(f"show tables")
        for row in rows:
            print(row)
    elif args.rescan:
        rescan()
    elif args.clean:
        clean()
    elif args.none_running:
        get_lock()
        none_running(HOSTNAME)
    elif args.none_running_anywhere:
        get_lock()
        none_running()
    else:
        get_lock()
        scan_s3_s4()
        none_running(HOSTNAME)
        run()
