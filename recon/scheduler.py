#!/usr/bin/env python3
#
"""scheduler.py:

The two time-consuming parts of the reconstruction are building and
solving the LP files. This schedules the jobs on multiple machines
using a MySQL database for coordination.

This is a simple scheduler for a single system. But you can run it on multiple systems at the same time. They coordinate through the database


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
import multiprocessing
import operator
import uuid
import datetime
from os.path import dirname,basename,abspath

# Set up path, among other things
import dbrecon

from dbrecon import dopen,dmakedirs,dsystem
from dfxml.writer import DFXMLWriter
from dbrecon import DB,LP,SOL,MB,GB,MiB,GiB,get_config_int,REIDENT
from ctools.dbfile import DBMySQL,DBMySQLAuth

import ctools.cspark as cspark
import ctools.lock

HELP="""
Try one of the following commands:

HALT - Immediately halt the jobs and the scheduler.
STOP - Clean shutdown of the scheduler at the end of the current.
PS   - Show the current processes
LIST - Show the current tasks
UPTIME - Show system load
DEBUG  - enable/disable debugging
SQL    - show/hide SQL
"""


HOSTNAME = dbrecon.hostname()

# Tuning parameters

SCHEMA_FILENAME="schema.sql"
PYTHON_START_TIME = 1
MIN_LP_WAIT   = 120             # wait two minutes between launches
MIN_SOL_WAIT  = 60              # wait one minute between launch

# Failsafes: don't start an LP or SOL unless we have this much free
MIN_FREE_MEM_FOR_LP  = 400*GiB  # we've seen LP generation take up to 350GiB
MIN_FREE_MEM_FOR_SOL = 20*GiB

MIN_FREE_MEM_FOR_KILLER = 5*GiB  # if less than this, start killing processes

REPORT_FREQUENCY = 60           # report this often into sysload table

PROCESS_DIE_TIME = 5            # how long to wait for a process to die
LONG_SLEEP= 300          # sleep for this long (seconds) when there are no resources
PS_LIST_FREQUENCY = 30   # big status report every 30 seconds

S3_SYNTH = 's3_pandas_synth_lp_files.py'
S4_RUN   = 's4_run_gurobi.py'
LP_J1    = 1                    # let this program schedule

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
    #lines = subprocess.check_output(['free','-b'],encoding='utf-8').split('\n')
    #return int(lines[1].split()[3])

last_report = 0
def report_load_memory(auth):
    """Report and print the load and free memory; return free memory"""
    global last_report
    free_mem = get_free_mem()

    # print current tasks
    total_seconds = (time.time() - dbrecon.start_time)
    hours    = int(total_seconds // 3600)
    mins     = int((total_seconds % 3600) // 60)
    secs     = int(total_seconds % 60)
    if time.time() > last_report + REPORT_FREQUENCY:
        DBMySQL.csfr(auth,
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
    # Don't wait anymore.

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
        """ps_list shows all of the processes that we are running."""
        print("PIDs in use: ",[p.pid for p in self.plist])
        print("")
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

def run(auth, debug=False):
    os.set_blocking(sys.stdin.fileno(), False)
    running         = set()
    last_ps_list    = 0
    last_lp_launch  = 0
    last_sol_launch = 0
    halting         = False

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
                print("Killing existing...")
                [kill_tree(p) for p in running]
                stop_requested = True
                halt           = True
            elif command=='stop':
                stop_requested = True
            elif command.startswith('ps'):
                subprocess.call("ps ww -o uname,pid,ppid,pcpu,etimes,vsz,rss,command --sort=-pcpu".split())
            elif command=='list':
                last_ps_list = 0
            elif command=='uptime':
                subprocess.call(['uptime'])
            elif command=='debug':
                debug = not debug
            elif command=='sql':
                auth.debug = not auth.debug
            else:
                if command!='help':
                    print(f"UNKNOWN COMMAND: '{command}'.")
                print(HELP)

        # Clean database if necessary
        dbrecon.db_clean(auth)

        # Report system usage if necessary
        dbrecon.GetConfig().config_reload()
        free_mem = report_load_memory(auth)

        # Are we done yet?
        remain = {}
        for what in ['lp','sol']:
            remain[what]  = DBMySQL.csfr(auth,
                                   f""" SELECT count(*) from {REIDENT}tracts WHERE {what}_end is null and pop100>0 """)[0][0]

        if remain['sol']==0:
            print("All done!")
            return

        # See if any of the processes have finished
        # Hard fail if any of them did not exit cleanly so we can diagnose the problem.
        for p in copy.copy(running):
            if p.poll() is not None:
                logging.info(f"PID{p.pid}: EXITED {pcmd(p)} code: {p.returncode}")
                if debug:
                    print("PID{p.pid} {p.args} completed")
                if p.returncode!=0 and not halting:
                    logging.error(f"ERROR: Process {p.pid} did not exit cleanly. retcode={p.returncode} mypid={os.getpid()} ")
                    logging.error(f"***************************************************************************************")
                    exit(1)
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
                print(f"Remaining LP: {remain['lp']} Remaining SOL: {remain['sol']}")
                print("Running processes:")
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
                DBMySQL.csfr(auth,f"INSERT INTO errors (host,file,error) VALUES (%s,%s,%s)",
                                (HOSTNAME,__file__,"Free memory down to {}".format(get_free_mem())))
                kill_tree(p)
                running.remove(p)
                continue

        if stop_requested:
            print("STOP REQUESTED  (type 'halt' to abort)")
            if len(running)==0:
                print("NONE LEFT. STOPPING.")
                break;
            else:
                print(f"Waiting for {len(running)} processes to stop...")
                time.sleep(PROCESS_DIE_TIME)
                continue

        # See if we can create another process.
        # For stability, we create a max of one LP and one SOL each time through.

        # Figure out how many we need to launch
        #
        if args.nolp:
            needed_lp = 0
        else:
            needed_lp =  min(get_config_int('run','max_lp'),args.maxlp) - len(running_lp())

        if debug:
            print(f"needed_lp: {needed_lp}")

        # If we can run another launch in, do it.
        if (get_free_mem()>MIN_FREE_MEM_FOR_LP) and (needed_lp>0) and (last_lp_launch + MIN_LP_WAIT < time.time()):

            # We only launch one LP at a time because they take a few minutes to eat up a lot of memory.
            # We make the entire county at a time
            if last_lp_launch + MIN_LP_WAIT > time.time():
                continue
            direction = 'DESC' if args.desc else ''
            cmd = f"""
                SELECT t.stusab,t.county,count(*) as tracts,sum(t.pop100) as pop
                FROM {REIDENT}tracts t
                WHERE (t.lp_end IS NULL) AND (t.hostlock IS NULL) AND (t.pop100>0)
                GROUP BY t.state,t.county
                ORDER BY pop {direction} LIMIT 1
                """.format()
            make_lps = DBMySQL.csfr(auth, cmd)
            if (len(make_lps)==0 and needed_lp>0) or debug:
                logging.warning(f"needed_lp: {needed_lp} but search produced 0. NO MORE LPS FOR NOW...")
                last_lp_launch = time.time()
            for (stusab,county,tract_count,pop) in make_lps:
                # If the load average is too high, don't do it
                lp_j2 = get_config_int('run','lp_j2')
                stusab = stusab.lower()
                print(f"\nLAUNCHING LP {S3_SYNTH} {stusab} {county} TRACTS: {tract_count:,} POP: {pop:,}")
                cmd = [sys.executable,'s3_pandas_synth_lp_files.py', '--j1', str(LP_J1), '--j2', str(lp_j2), stusab, county]
                print("$ " + " ".join(cmd))
                p = prun(cmd)
                running.add(p)
                last_lp_launch = time.time()

        ## Evaluate Launching SOLs.
        ## Only evaluate solutions where we have a LP file

        max_sol    = get_config_int('run','max_sol')
        max_jobs   = get_config_int('run','max_jobs')
        max_sol_launch = get_config_int('run','max_sol_launch')
        if args.nosol:
            needed_sol = 0
        else:
            needed_sol = max_jobs-len(running)
            if needed_sol > max_sol:
                needed_sol = max_sol

        if debug:
            print(f"max_sol={max_sol} needed_sol={needed_sol} max_jobs={max_jobs} running={len(running)} get_free_mem()={get_free_mem()} ")

        if get_free_mem()>MIN_FREE_MEM_FOR_SOL and needed_sol>0:
            # Run any solvers that we have room for
            # As before, we only launch one at a time
            # Solve the biggest first, because they take the most time


            if last_sol_launch + MIN_SOL_WAIT > time.time():
                print(f"Can't launch again for {last_sol_launch+MIN_SOL_WAIT-time.time()} seconds")
            else:
                cmd = f"""
                SELECT stusab,county,tract FROM {REIDENT}tracts
                WHERE (sol_end IS NULL) AND (lp_end IS NOT NULL) AND (hostlock IS NULL)
                ORDER BY pop100 desc LIMIT %s
                """
                solve_lps = DBMySQL.csfr(auth,cmd,(max_sol_launch,))
                if (len(solve_lps)==0 and needed_sol>0) or debug:
                    print(f"2: needed_sol={needed_sol} len(solve_lps)={len(solve_lps)}")

                for (ct,(stusab,county,tract)) in enumerate(solve_lps,1):
                    print("LAUNCHING SOLVE {} {} {} ({}/{}) {}".format(stusab,county,tract,ct,len(solve_lps),time.asctime()))
                    gurobi_threads = get_config_int('gurobi','threads')
                    dbrecon.db_lock(stusab,county,tract)
                    stusab         = stusab.lower()
                    cmd = [sys.executable,S4_RUN,'--exit1','--j1','1','--j2',str(gurobi_threads),stusab,county,tract]
                    print("$ "+" ".join(cmd))
                    p = prun(cmd)
                    running.add(p)
                    time.sleep(PYTHON_START_TIME)
                    last_sol_launch = time.time()

        time.sleep( get_config_int('run', 'sleep_time' ) )
        # and repeat
    # Should never get here

################################################################
## killer stuff follows

SHOW_RUNNING=False
def set_none_running(auth, hostname):
    """Tell the database that there are no processes running, either on this host or on all hosts"""

    hostlock = '' if hostname is None else f" AND (hostlock = '{hostname}') "

    if SHOW_RUNNING:
        for (stusab,county,tract) in  DBMySQL.csfr(auth,
                f"""
                SELECT stusab,county,tract
                FROM {REIDENT}tracts
                WHERE lp_start IS NOT NULL AND lp_end IS NULL
                """ + hostlock):
            print("CLEARINING LP MAKING ",stusab,county,tract)
    DBMySQL.csfr(auth,
        f"""
        UPDATE {REIDENT}tracts
        SET lp_start=NULL
        WHERE lp_start IS NOT NULL AND lp_end IS NULL
        """ + hostlock)

    if SHOW_RUNNING:
        for (stusab,county,tract) in DBMySQL.csfr(auth,
                f"""
                SELECT stusab,county,tract
                FROM {REIDENT}tracts
                WHERE sol_start IS NOT NULL AND sol_end IS NULL
                """ + hostlock):
            print("CLEARING SOL MAKING",stusab,county,tract)
    DBMySQL.csfr(auth,
        f"""
        UPDATE {REIDENT}tracts
        SET sol_start=NULL
        WHERE sol_start IS NOT NULL AND sol_end IS NULL
        """ + hostlock)
    print("Resume...")

def kill_running_s3_s4():
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

################################################################
## rescan stuff follows


def rescan_row(config_row):
    """Designed to be called from multiprocessing. Validate that the files referenced in the database row are present. If they are not, update the database.
    If they are present, validate them. If they do not validate, update the database.
    """
    (config,row) = config_row
    dbrecon.GetConfig().set_config(config)
    dbrecon.set_reident(config['paths']['reident'])
    for var in config['environment']['vars'].split(','):
        os.environ[var] = config['environment'][var]

    row['stusab'] = row['stusab'].lower()
    logging.info(f"rescan_row {row}")
    lpfilenamegz  = dbrecon.LPFILENAMEGZ(stusab=row['stusab'],county=row['county'],tract=row['tract'])
    solfilenamegz = dbrecon.SOLFILENAMEGZ(stusab=row['stusab'],county=row['county'],tract=row['tract'])

    ret = []
    auth = dbrecon.auth()
    if row['sol_end'] and dbrecon.dgetsize(solfilenamegz) < dbrecon.MIN_SOL_SIZE:
        logging.warning(f"{solfilenamegz} not existing or too small. Removing.")
        dbrecon.remove_solfile(auth, row['stusab'], row['county'], row['tract'])
        ret.append(solfilenamegz)

    if row['lp_end'] and not dbrecon.lpfile_properly_terminated(lpfilenamegz):
        logging.warning(f"{lpfilenamegz} is not properly terminated. Removing")
        dbrecon.remove_lpfile(auth, row['stusab'], row['county'], row['tract'])
        ret.append(lpfilenamegz)

    del auth                    # be sure its disconnected
    return ret

def rescan(auth, args):
    """Get a list of the tracts that require scanning and check each one."""
    stusab = args.stusab
    county = args.county

    if args.spark:
        if not cspark.spark_running():
            raise RuntimeError("--spark provided but not running under spark")
        # pylint: disable=E0401
        from pyspark.sql import SparkSession
        spark = SparkSession.builder.getOrCreate()
        sc    = spark.sparkContext

        print("================================================================")
        print("================================================================")
        print("================================================================")
        print("================================================================")

        print("Checking spark to see if it's working...")
        d = sc.parallelize(range(10000))
        val = d.reduce(operator.add)
        if val != 49995000:
            raise RuntimeError(f"spark not operational (got {val} wanted 49995000)")

    # Figure out what needs to be processed

    restrict = "AND ((lp_end IS NOT NULL) or (sol_end IS NOT NULL)) "
    cmd = f"SELECT * from {REIDENT}tracts where (pop100>0) {restrict} "
    sqlargs = []
    if stusab:
        cmd += " and (stusab = %s)"
        sqlargs.append(stusab)
        if county:
            cmd += " and (county=%s)"
            sqlargs.append(county)
    rows = DBMySQL.csfr(auth, cmd, sqlargs, asDicts='True')

    # This idea borrowed from DAS. Put in the config file all of the information that the worker will need.
    # Move over environment variables in a special section called [environment]
    config = dbrecon.GetConfig().config

    config['paths']['reident'] = REIDENT
    for var in config['environment']['vars'].split(','):
        config['environment'][var] = os.getenv(var)
    config_rows = [ (config, row) for row in rows]

    print(f"*** Tracts requiring rescanning: {len(config_rows)}")
    cmd=cmd.replace("stusab,county,tract","count(*)").replace(restrict,"")
    r2  = DBMySQL.csfr(auth, cmd, sqlargs)[0][0]
    print(f"*** Total tracts: {r2}.")

    if not args.spark:
        print(f"Processing locally with {args.j1} threads. Expected completion in {len(config_rows)*3/10000} hours")
        with multiprocessing.Pool(args.j1) as p:
            p.map(rescan_row, config_rows)
        return

    print("*** Processing with spark...")
    output_path = os.path.join(os.getenv('DAS_S3ROOT'), '2010-re/{reident}/spark/' + datetime.datetime.now().isoformat()[0:19] + '-rescan')
    output_path_txt = output_path+".txt"
    print("*** Will write to",output_path)

    # Create an RDD that has all of the rows, and partition it so that there are roughly 5 rows per partition.
    rows_rdd = sc.parallelize(config_rows).repartition( len(config_rows)//10 )

    # Run the mapper
    results_rdd = rows_rdd.flatMap( rescan_row )

    # Save the results to S3 first

    results_rdd.saveAsTextFile(output_path)
    print("Combining to a single file and saving again")
    results_1partition = results_rdd.coalesce(1)
    results_1partition.saveAsTextFile(output_path_txt)

    # This would save the results on S3:
    print("\n\n\n\n")
    print("================================================================")
    print("================================================================")
    print("================================================================")

def clean(auth):
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
                DBMySQL.csfr(auth,f"UPDATE {REIDENT}tracts SET {what}_start=NULL,{what}_end=NULL "
                        "where stusab=%s and county=%s and tract=%s",
                        (stusab, county, tract))
                os.unlink(path)




if __name__=="__main__":
    from argparse import ArgumentParser,ArgumentDefaultsHelpFormatter
    parser = ArgumentParser( formatter_class = ArgumentDefaultsHelpFormatter,
                             description="Maintains a database of reconstruction and schedule "
                             "next work if the CPU load and memory use is not too high." )
    dbrecon.argparse_add_logging(parser)
    parser.add_argument("--testdb",  help="test database connection", action='store_true')
    parser.add_argument("--clean",   help="Look for .lp and .sol files that are too slow and delete them, then remove them from the database", action='store_true')
    parser.add_argument("--nosol",   help="Do not run the solver", action='store_true')

    parser.add_argument("--maxlp",   help="Never run more than this many LP makers", type=int, default=999)
    parser.add_argument("--rescan",  help="validate and update the database contents against files in the file system. Uses --j1 when not run under spark. SPARK ENABLED.", action='store_true')
    parser.add_argument("--nolp",    help="Do not run the LP maker", action='store_true')
    parser.add_argument("--set_none_running", help="Update database to indicate there are no outstanding LP files being built or Solutions being solved on this machine.",
                        action='store_true')
    parser.add_argument("--set_none_running-anywhere", help="Run if there are no outstanding LP files being built or solutions being solved on any machine.",
                        action='store_true')
    parser.add_argument("--dry_run", help="Just report what the next thing to run would be, then quit", action='store_true')
    parser.add_argument("--stusab", help="stusab for rescanning")
    parser.add_argument("--county", help="county for rescanning")
    parser.add_argument("--desc", action='store_true', help="Run most populus tracts first, otherwise do least populus tracts first")
    parser.add_argument("--debug", action='store_true', help="debug mode")
    parser.add_argument("--j1", help="number of threads for rescan", type=int, default=10)
    parser.add_argument("--spark", help="run under spark", action='store_true')
    args   = parser.parse_args()


    config = dbrecon.setup_logging_and_get_config(args=args,prefix='sch_')
    auth = dbrecon.auth()

    if args.j1>50:
        print("Experience has shown that --j1>50 is not useful on a machine with 96 cores. Setting --j1 to 50")
        args.j1 = 50


    args   = parser.parse_args()
    config = dbrecon.setup_logging_and_get_config(args=args,prefix='sch_')
    auth   = dbrecon.auth()

    if args.testdb:
        print("Tables:")
        rows = DBMySQL.csfr(auth,f"show tables")
        for row in rows:
            print(row)
        exit(0)

    ctools.lock.lock_script( abspath(__file__))

    if args.rescan:
        rescan(auth, args)
    elif args.clean:
        clean(auth)
    elif args.set_none_running:
        set_none_running(auth,HOSTNAME)
    elif args.set_none_running_anywhere:
        set_none_running(auth, None)
    else:
        kill_running_s3_s4()
        set_none_running(auth,HOSTNAME)
        run(auth, args.debug)
