#!/usr/bin/env python3
#
# Read the processed SF1 dat and syntheize the LP file that will be input to the optimizer.
#
# When all solutions are present, creates the CSV file

import atexit
import csv
import dbrecon
import gc
import glob
import logging
import multiprocessing
import os
import os.path
import subprocess
import sys
import time

from os.path import dirname,basename,abspath

import botocore
import gurobipy

import dbrecon
from dbrecon import DBMySQL,dopen,dmakedirs,dsystem,dpath_exists,GB,dgetsize,dpath_expand,MY_DIR,dpath_unlink,S3ZPUT,S3ZCAT,REIDENT,ZCAT,GZIP,GZIP_OPT,SOL

from ctools.dbfile import DBMySQL,DBMySQLAuth

class InfeasibleError(RuntimeError):
    pass

# Details on Gurobi output:
# http://www.gurobi.com/documentation/8.1/refman/mip_logging.html

# How many threads to use
GUROBI_THREADS_DEFAULT=16
# The model variables we track
MODEL_ATTRS="NumVars,NumConstrs,NumNZs,NumIntVars,Runtime,IterCount,BarIterCount,isMIP".split(",")
# Previously had MIPGap but it was sometimes inf

"""Run gurobi with a given LP file.
Note: automatically handles the case where lpfile is compressed by decompressing
and giving the Gurobi optimizer device to read from.
"""

def run_gurobi(auth, stusab, county, tract, lpgz_filename, dry_run):
    logging.info(f'RunGurobi({stusab},{county},{tract})')

    config           = dbrecon.GetConfig().get_config()
    state_code       = dbrecon.state_fips(stusab)
    geoid_tract      = state_code + county + tract
    lpgz_filename    = dbrecon.dpath_expand(lpgz_filename)
    ilp_filename     = dbrecon.ILPFILENAME(stusab=stusab, county=county, tract=geoid_tract)
    sol_filename     = dbrecon.SOLFILENAME(stusab=stusab, county=county, tract=tract)
    solgz_filename   = dbrecon.SOLFILENAMEGZ(stusab=stusab, county=county, tract=tract)
    log_filename     = os.path.splitext(sol_filename)[0]+".log" # where final log gets written to
    tmp_log_filename = '/tmp/' + log_filename.replace('/','_').replace(".gz","") # were the temp log gets written

    env            = None # Guorbi environment
    p              = None # subprocess for decompressor
    tempname       = None # symlink that points to decompressed model file

    # make sure input file exists and is valid
    if dpath_exists(lpgz_filename) and dgetsize(lpgz_filename) < dbrecon.MIN_LP_SIZE:
        logging.warning("File {} is too small ({}). Removing and updating database.".format(lpgz_filename,os.path.getsize(lpgz_filename)))
        dbrecon.remove_lpfile(auth, stusab, county, tract)
        return

    if not dpath_exists(lpgz_filename):
        logging.warning("File does not exist: {}. Updating database.".format(lpgz_filename))
        dbrecon.remove_lpfile(auth, stusab, county, tract)
        return

    # Make sure output does not exist. If it exists, delete it, otherwise give an error
    for fn in [sol_filename,solgz_filename]:
        if dbrecon.dpath_exists(fn):
            try:
                logging.warning(f"File {fn} exists. size={dbrecon.dgetsize(fn)} Removing.")
            except FileNotFoundError as e:
                pass
            try:
                dbrecon.dpath_unlink(fn)
            except FileNotFoundError as e:
                pass


    # make sure output directory exists
    dbrecon.dmakedirs( dirname( sol_filename))
    dbrecon.db_start( auth, SOL, stusab, county, tract)

    try:
        customer     = dbrecon.get_config_str('gurobi','customer')
        appname      = dbrecon.get_config_str('gurobi','appname')
    except KeyError:
        customer = ''
        appname = ''

    if customer=='':
        env = gurobipy.Env( tmp_log_filename )
    else:
        env = gurobipy.Env.OtherEnv( tmp_log_filename, customer, appname, 0, "")

    env.setParam("LogToConsole",0)

    # Gurobi determines what kind of file it is reading by its extension.
    # So if we are reading from a .lp.gz file, we create a symlink with the
    # correct extension to a pipe
    if lpgz_filename.endswith(".lp"):
        model = gurobipy.read(lpgz_filename, env=env)
    elif lpgz_filename.endswith(".lp.gz"):
        # Make /tmp/stdin.lp a symlink to /dev/stdin, and then read that
        # so Gurobi can end a file ending with .lp
        if lpgz_filename.startswith('s3://'):
            cmd = S3ZCAT
        else:
            cmd = ZCAT
        p = subprocess.Popen([cmd,lpgz_filename],stdout=subprocess.PIPE)
        tempname = f"/tmp/stdin-{p.pid}-"+(lpgz_filename.replace("/","_"))+".lp"
        if os.path.exists(tempname):
            raise RuntimeError(f"File should not exist: {tempname}")
        os.symlink(f"/dev/fd/{p.stdout.fileno()}",tempname)
        model = gurobipy.read(tempname, env=env)
    else:
        raise RuntimeError("Don't know how to read model from {}".format(lpgz_filename))

    model.setParam("Threads",args.j2)

    if dry_run:
        print(f"MODEL FOR {stusab} {county} {tract} ")
        model.printStats()
    else:
        logging.info(f"Starting optimizer. pid={os.getpid()}")
        start_time = time.time()
        model.optimize()
        end_time = time.time()
        sol_time = round(end_time-start_time,4)

        vars = []
        vals = []

        # Model is optimal. If sol_filename is on s3, write to a tempoary file and copy it up there
        if sol_filename.startswith('s3://'):
            s3_sol_filename = sol_filename
            sol_filename = f'/mnt/tmp/sol-{stusab}{county}{tract}.sol'
        else:
            s3_sol_filename = None

        #
        if model.status == 2:
            logging.info(f'Model {geoid_tract} is optimal. Solve time: {sol_time}s. Writing solution to {sol_filename}')
            model.write(sol_filename)
        # Model is infeasible. This should not happen
        elif model.status == 3:
            logging.info(f'Model {geoid_tract} is infeasible. Elapsed time: {sol_time}s. Writing ILP to {ilp_filename}')
            dbrecon.dmakedirs( dirname( ilp_filename)) # make sure output directory exists
            model.computeIIS()
            model.write(dbrecon.dpath_expand(ilp_filename))
            raise InfeasibleError();
        else:
            logging.error(f"Unknown model status code: {model.status}")

        # Compress the output file in place, or while writing to s3
        if s3_sol_filename:
            cmd = [ S3ZPUT, sol_filename, s3_sol_filename+'.gz' ]
        else:
            cmd = [ GZIP, GZIP_OPT, sol_filename]
        subprocess.check_call(cmd)

        dbrecon.db_done(auth, SOL, stusab, county, tract) # indicate we have a solution

        # Save model information in the database
        for name in MODEL_ATTRS:
            try:
                vals.append(model.getAttr(name))
                vars.append(name)
            except AttributeError:
                pass

        # Get the final pop. Becuase the key may not exist immediately (it happened to us!)
        # retry if we get the boto3 error.
        # It would be nice to have a higher-level retry interface for this.
        for retry_count in range(1,11):
            try:
                final_pop = dbrecon.get_final_pop_from_sol(auth,stusab,county,tract,delete=False);
                break           # exit for loop
            except botocore.errorfactory.NoSuchKey as e:
                if retry_count==10:
                    logging.error(f"retry {retry_count} get_final_pop_from_sol. Retry count exceeded.")
                    raise
                logging.warning(f"retry {retry_count} get_final_pop_from_sol {e}")
                time.sleep(1)   # wait a second

        if final_pop==0:
            raise RuntimeError("final pop cannot be 0")
        vars.append("final_pop")
        vals.append(final_pop)

        # Get the sol_gb
        vars.append("sol_gb")
        vals.append(dbrecon.maxrss() // GB)

        cmd = f"UPDATE {REIDENT}tracts set " + ",".join([var+'=%s' for var in vars]) + " where stusab=%s and county=%s and tract=%s"
        DBMySQL.csfr(auth,cmd, vals+[stusab,county,tract])
    del env                     # free the memory and release the Gurobi token

    # save the logfile locally or uploaded in compressed form.
    if log_filename.startswith('s3://'):
        subprocess.check_call([ S3ZPUT, tmp_log_filename, log_filename+'.gz'])
    else:
        subprocess.check_call([ GZIP, GZIP_OPT], stdin=open(tmp_log_filename,'rb'), stdout=open(log_filename+'.gz','wb'))
    os.unlink(tmp_log_filename)
    if tempname is not None:
        os.unlink(tempname)



def run_gurobi_for_county_tract(stusab, county, tract):
    """Single-threaded function that runs gurobi for a specific state, county, tract."""

    auth = dbrecon.auth()
    assert len(stusab)==2
    assert len(county)==3
    assert len(tract)==6
    lpgz_filename  = dbrecon.LPFILENAMEGZ(stusab=stusab,county=county,tract=tract)
    if dbrecon.dpath_exists(lpgz_filename) is None:
        logging.warning(f"lpgz_filename does not exist. Waiting for 10 seconds for S3 to stabalize")
        time.sleep(10)

    if dbrecon.dpath_exists(lpgz_filename) is None:
        logging.error(f"lpgz_filename still does not exist. updating database")
        dbrecon.remove_lpfile(auth, stusab, county, tract)
        return

    sol_filename= dbrecon.SOLFILENAME(stusab=stusab, county=county, tract=tract)
    solgz_filename= sol_filename+".gz"
    if dbrecon.is_db_done(auth, SOL,stusab, county, tract) and dbrecon.dpath_exists(solgz_filename):
        logging.warning(f"SOL exists in database and sol file exists: {stusab}{county}{tract}; will not solve")
        return

    try:
        run_gurobi(auth, stusab, county, tract, lpgz_filename, args.dry_run)

    except FileExistsError as e:
        logging.warning(f"solution file exists for {stusab}{county}{tract}?")
        return

    except FileNotFoundError as e:
        logging.error(f"LP file not found for {stusab}{county}{tract}. Updating database")
        dbrecon.remove_lpfile(auth, stusab, county, tract)
        return

    except gurobipy.GurobiError as e:
        logging.error(f"GurobiError '{e}' in {stusab} {county} {tract}")
        dbrecon.log_error(error=str(e), filename=__file__)
        if str(e)=='Unable to read model':
            dbrecon.log_error("Unable to read model. Deleting lp file", filename=__file__)
            dbrecon.remove_lpfile(auth, stusab, county, tract)
            return
        else:
            DBMySQL.csfr(auth,
                         f'INSERT INTO errors (error,stusab,county,tract) values (%s,%s,%s,%s)',
                         (str(e),stusab,county,tract))
            raise e;
    except InfeasibleError as e:
        logging.error(f"Infeasible in {stusab} {county} {tract}")
        DBMySQL(auth,f'INSERT INTO errors (error,stusab,county,tract) values (%s,%s,%s,%s)',
                (str(e),stusab,county,tract))

    logging.info(f"Ran Gurobi for {stusab} {county} {tract}")
    if args.exit1:
        logging.info("clean exit")
        exit(0)

def run_gurobi_tuple(tt):
    """Run gurobi on a tract tuple.
    This cannot be made a local function inside run_gurobi_for_county because then it won't work with map.
    """
    run_gurobi_for_county_tract(tt[0], tt[1], tt[2])

def run_gurobi_for_county(stusab, county, tracts):
    logging.info(f"run_gurobi_for_county({stusab},{county})")
    assert stusab is not None
    assert county is not None
    auth = dbrecon.auth()       # will not be used in subprocesses
    if (tracts==[]) or (tracts==['all']):
        tracts = dbrecon.tracts_in_county_ready_to_solve(auth, stusab, county)
        logging.info(f"Tracts require solving in {stusab} {county}: {tracts}")
        if tracts==[]:
            # No tracts. Report if there are tracts in county missing LP files
            needed = dbrecon.get_tracts_needing_lp_files(auth, stusab, county)
            if needed:
                logging.warning(f"run_gurobi_for_county({stusab},{county}): {len(needed)} tracts do not have LP files")
            return

    for tract in tracts:
        dbrecon.db_lock(auth, stusab, county, tract)
    tracttuples = [(stusab, county, tract) for tract in tracts]
    if args.j1>1:
        with multiprocessing.Pool(args.j1) as p:
            p.map(run_gurobi_tuple, tracttuples)
    else:
        for tt in tracttuples:
            run_gurobi_tuple(tt)

if __name__=="__main__":
    from argparse import ArgumentParser,ArgumentDefaultsHelpFormatter
    parser = ArgumentParser( formatter_class = ArgumentDefaultsHelpFormatter,
                             description="Run Gurobi on one or all off the tracts in a given state/county." )
    dbrecon.argparse_add_logging(parser)
    parser.add_argument("stusab", help="2-character state abbreviation")
    parser.add_argument("county", help="3-digit county code; can be 'all' for all counties")
    parser.add_argument("tracts", help="4-digit tract code[s]; can be 'all'",nargs="*")
    parser.add_argument("--j1", help="Specify number of tracts to solve at once (presolve doesn't parallelize)", default=1, type=int)
    parser.add_argument("--j2", help="Specify number of threads for gurobi to use", default=GUROBI_THREADS_DEFAULT, type=int)
    parser.add_argument("--dry-run", help="do not run gurobi; just print model stats", action="store_true")
    parser.add_argument("--exit1", help="Exit Gurobi after the first execution", action='store_true')

    if 'GUROBI_HOME' not in os.environ:
        raise RuntimeError("GUROBI_HOME not in environment")

    args       = parser.parse_args()
    config     = dbrecon.setup_logging_and_get_config(args=args,prefix="04run")
    stusab     = dbrecon.stusab(args.stusab).lower()
    tracts     = args.tracts

    if args.county=='all':
        counties = dbrecon.counties_for_state(stusab)
    else:
        counties = [args.county]

    for county in counties:
        run_gurobi_for_county(stusab, county, tracts)
