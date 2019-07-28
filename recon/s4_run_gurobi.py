#!/usr/bin/env python3
#
# Read the processed SF1 dat and syntheize the LP file that will be input to the optimizer.
#
# When all solutions are present, creates the CSV file

import csv
import dbrecon
import gc
import glob
import logging
import os
import os.path
import subprocess
import sys
import time
import atexit
import multiprocessing 

import gurobipy
import dbrecon
from dbrecon import DB
from dbrecon import dopen,dmakedirs,dsystem,dpath_exists,GB

def db_fail(state_abbr, county, tract):
    DB.csfr("UPDATE tracts SET lp_start=NULL where stusab=%s and county=%s and tract=%s",(state_abbr,county,tract))


class InfeasibleError(RuntimeError):
    pass

# Details on Gurobi output:
# http://www.gurobi.com/documentation/8.1/refman/mip_logging.html
GUROBI_THREADS_DEFAULT=16
MODEL_ATTRS="NumVars,NumConstrs,NumNZs,NumIntVars,MIPGap,Runtime,IterCount,BarIterCount,isMIP".split(",")

"""Run gurobi with a given LP file. 
Note: automatically handles the case where lpfile is compressed by decompressing
and giving the Gurobi optimizer device to read from.
"""
def run_gurobi(state_abbr, county, tract, lpgz_filename, dry_run):
    logging.info(f'RunGurobi({state_abbr},{county},{tract})')
    config      = dbrecon.get_config()
    state_abbr  = state_abbr
    county      = county
    tract       = tract
    state_code  = dbrecon.state_fips(state_abbr)
    geoid_tract = state_code + county + tract
    lpgz_filename = dbrecon.dpath_expand(lpgz_filename)
    ilp_filename= dbrecon.ILPFILENAME(state_abbr=state_abbr, county=county, tract=geoid_tract)
    sol_filename= dbrecon.SOLFILENAME(state_abbr=state_abbr, county=county, tract=tract)
    solgz_filename= sol_filename+".gz"
    env         = None # Guorbi environment
    p           = None # subprocess for decompressor
    tempname    = None # symlink that points to decompressed model file

    if lpgz_filename.startswith("s3:"):
        raise RuntimeError("This must be modified to allow Gurobi to read files from S3 using the stdin hack.")

    # make sure input file exists and is valid
    if not os.path.exists(lpgz_filename) or dbrecon.dgetsize(lpgz_filename) < dbrecon.MIN_LP_SIZE:
        if os.path.exists(lpgz_filename):
            logging.warning("File {} is too small ({}). Removing and updating database.".format(lpgz_filename,os.path.getsize(lpgz_filename)))
            os.unlink(lpgz_filename)
        else:
            logging.warning("File does not exist: {}. Updating database.".format(lpgz_filename))
        dbrecon.DB.csfr('UPDATE tracts SET lp_start=NULL,lp_end=NULL,hostlock=NULL,error=NULL where stusab=%s and county=%s and tract=%s',
                        (state_abbr,county,tract))
        return

    # Make sure output does not exist. If it exists, delete it, otherwise give an error
    for fn in [sol_filename,solgz_filename]:
        if dbrecon.dpath_exists(fn):
            logging.warning("File {} exists but is too small ({}). Removing.".format(fn,dbrecon.dgetsize(fn)))
            dbrecon.dpath_unlink(fn)

    # make sure output directory exists
    dbrecon.dmakedirs( os.path.dirname( sol_filename)) 
    dbrecon.db_start('sol', state_abbr, county, tract)
    atexit.register(db_fail, state_abbr, county, tract)

    try:
        customer     = dbrecon.get_config_str('gurobi','customer')
        appname      = dbrecon.get_config_str('gurobi','appname')
    except KeyError:
        customer = ''
        appname = ''
    log_filename = os.path.splitext(sol_filename)[0]+".log"
    
    if customer=='':
        env = gurobipy.Env( log_filename )
    else:
        env = gurobipy.Env.OtherEnv( log_filename, customer, appname, 0, "")

    env.setParam("LogToConsole",0)
    if lpgz_filename.endswith(".lp"):
        model = gurobipy.read(lpgz_filename, env=env)
        tempname = None
    elif lpgz_filename.endswith(".lp.gz"):
        p = subprocess.Popen(['zcat',lpgz_filename],stdout=subprocess.PIPE)
        # Because Gurobin must read from a file that ends with a .lp, 
        # make /tmp/stdin.lp a symlink to /dev/stdin, and
        # then read that
        tempname = f"/tmp/stdin-{p.pid}-"+(lpgz_filename.replace("/","_"))+".lp"
        if os.path.exists(tempname):
            raise RuntimeError(f"File should not exist: {tempname}")
        os.symlink(f"/dev/fd/{p.stdout.fileno()}",tempname)
        model = gurobipy.read(tempname, env=env)
    else:
        raise RuntimeError("Don't know how to read model from {}".format(lpgz_filename))

    model.setParam("Threads",args.j2)

    if dry_run:
        print(f"MODEL FOR {state_abbr} {county} {tract} ")
        model.printStats()
    else:
        logging.info(f"Starting optimizer. pid={os.getpid()}")
        start_time = time.time()
        model.optimize()
        end_time = time.time()
        sol_time = round(end_time-start_time,4)

        vars = []
        vals = []

        # Model is optimal
        if model.status == 2:
            logging.info(f'Model {geoid_tract} is optimal. Solve time: {sol_time}s. Writing solution to {sol_filename}')
            model.write(sol_filename)
        # Model is infeasible. This should not happen
        elif model.status == 3:
            logging.info(f'Model {geoid_tract} is infeasible. Elapsed time: {sol_time}s. Writing ILP to {ilp_filename}')
            dbrecon.dmakedirs( os.path.dirname( ilp_filename)) # make sure output directory exists
            model.computeIIS()
            model.write(dbrecon.dpath_expand(ilp_filename))
            raise InfeasibleError();
        else:
            logging.error(f"Unknown model status code: {model.status}")

        # Compress the output file
        cmd = ['gzip','-1f',sol_filename]
        subprocess.check_call(cmd)
        dbrecon.db_done('sol', state_abbr, county, tract) # indicate we have a solution

        # Save model information in the database
        for name in MODEL_ATTRS:
            try:
                vals.append(model.getAttr(name))
                vars.append(name)
            except AttributeError:
                pass

        # Get the final pop
        vars.append("final_pop")
        vals.append(dbrecon.get_final_pop_from_sol(state_abbr,county,tract))

        # Get the sol_gb
        vars.append("sol_gb")
        vals.append(dbrecon.maxrss() // GB)

        cmd = "UPDATE tracts set " + ",".join([var+'=%s' for var in vars]) + " where stusab=%s and county=%s and tract=%s"
        dbrecon.DB.csfr(cmd, vals+[state_abbr,county,tract])
    del env
    if tempname is not None:
        os.unlink(tempname)
    atexit.unregister(db_fail)


def run_gurobi_for_county_tract(state_abbr, county, tract):
    assert len(state_abbr)==2
    assert len(county)==3
    assert len(tract)==6
    lpgz_filename  = dbrecon.LPFILENAMEGZ(state_abbr=state_abbr,county=county,tract=tract)
    if dbrecon.dpath_exists(lpgz_filename) is None:
        logging.info(f"lpgz_filename does not exist")
        dbrecon.rescan_files(state_abbr, county, tract)
        return

    if dbrecon.is_db_done('sol',state_abbr, county, tract):
        logging.warning(f"SOL exists in database: {state_abbr}{county}{tract}; will not solve")
        return

    try:
        run_gurobi(state_abbr, county, tract, lpgz_filename, args.dry_run)
    except FileExistsError as e:
        logging.warning(f"solution file exists for {state_abbr}{county}{tract}; rescan_files 1")
        dbrecon.rescan_files(state_abbr, county,tract)
    except FileNotFoundError as e:
        logging.warning(f"LP file not found for {state_abbr}{county}{tract}; rescan_files 2")
        dbrecon.rescan_files(state_abbr, county,tract)
    except gurobipy.GurobiError as e:
        logging.error(f"GurobiError in {state_abbr} {county} {tract}")
        dbrecon.log_error(error=str(e), filename=__file__)
        if str(e)=='Unable to read model':
            logging.error("Unable to read model. Deleting lp file")
            dbrecon.dpath_unlink(lpgz_filename)
            dbrecon.rescan_files(state_abbr, county, tract)
        else:
            dbrecon.DB.csfr('UPDATE tracts set error=%s where stusab=%s and county=%s and tract=%s',
                            (str(e),state_abbr,county,tract))
    except InfeasibleError as e:
        logging.error(f"Infeasible in {state_abbr} {county} {tract}")
        dbrecon.DB.csfr('UPDATE tracts set error="infeasible" where stusab=%s and county=%s and tract=%s',
                        (str(e),state_abbr,county,tract))
    except Exception as e:
        logging.error(f"Unknown error: {e}")
        
    if args.exit1:
        logging.info("clean exit")
        exit(0)

def run_gurobi_tuple(tt):
    """Run gurobi on a tract tuple. 
    This cannot be made a local function inside run_gurobi_for_county because then it won't work with map.
    """
    run_gurobi_for_county_tract(tt[0], tt[1], tt[2])

def run_gurobi_for_county(state_abbr, county, tracts):
    logging.info(f"run_gurobi_for_county({state_abbr},{county})")
    if (tracts==[]) or (tracts==['all']):
        tracts = [row[0] for row in DB.csfr("SELECT tract FROM tracts WHERE (lp_end IS NOT NULL) AND (sol_end IS NULL) AND stusab=%s AND county=%s",
                                            (state_abbr, county))]

        logging.info(f"Tracts require solving in {state_abbr} {county}: {tracts}")
        if tracts==[]:
            # No tracts. Report if there are tracts in county missing LP files
            rows = DB.csfr("SELECT tract FROM tracts WHERE (lp_end IS NULL) AND stusab=%s AND county=%s",(state_abbr,county))
            if rows:
                logging.warning(f"run_gurobi_for_county({state_abbr},{county}): {len(rows)} tracts do not have LP files")
            return

    tracttuples = [(state_abbr, county, tract) for tract in tracts]
    if args.j1>1:
        with multiprocessing.Pool(args.j1) as p:
            p.map(run_gurobi_tuple, tracttuples)
    else:
        for tt in tracttuples:
            run_gurobi_tuple(tt)

def make_csv_file(state_abbr, county):
    # Make sure we have a solution file for every tract
    county_csv_filename = dbrecon.COUNTY_CSV_FILENAME(state_abbr=state_abbr, county=county)
    state_code = dbrecon.state_fips(state_abbr)
    tracts     = dbrecon.tracts_for_state_county(state_abbr=state_abbr, county=county)
    missing = 0
    for tract in tracts:
        solfile = dbrecon.SOLFILENAME(state_abbr=state_abbr, county=county, tract=tract)
        if not dpath_exists(solfile):
            logging.error("No solution file for: {}".format(solfile))
            missing += 1
    if missing:
        logging.warning("Missing tracts. Will not make CSV file")
        return

    with dopen(county_csv_filename,"w") as outfile:
        w = csv.writer(outfile)
        w.writerow(['geoid_tract','geoid_block','sex','age','white','black','aian','asian','nhopi','sor','hisp'])
        for tract in tracts:
            logging.info("Starting tract "+tract)
            with dopen(dbrecon.SOLFILENAME(state_abbr=state_abbr, county=county, tract=tract),"r") as infile:
                for line in infile:
                    if line[0:2]=='C_': # oldstyle variable
                        (var,count) = line.strip().split(" ")

                        # don't count the zeros
                        if count=="0":
                            continue 
                        c = var.split("_")
                        tract_ = c[1][5:11]
                        if tract != tract_:
                            raise RuntimeError(f"{infile.name}: Expecting tract {tract} read {tract_}")
                        geoid_tract = state_code + county + tract
                        w.writerow([geoid_tract, c[1], c[5], c[6], c[7], c[8], c[9], c[10], c[11], c[12], c[13]])
            logging.info("Ending tract "+tract)

if __name__=="__main__":
    from argparse import ArgumentParser,ArgumentDefaultsHelpFormatter
    parser = ArgumentParser( formatter_class = ArgumentDefaultsHelpFormatter,
                             description="Run Gurobi on one or all off the tracts in a given state/county and convert the output to a single CSV file for the county." )
    dbrecon.argparse_add_logging(parser)
    parser.add_argument("state_abbr", help="2-character state abbreviation")
    parser.add_argument("county", help="3-digit county code; can be 'all' for all counties")
    parser.add_argument("tracts", help="4-digit tract code[s]; can be 'all'",nargs="*")
    parser.add_argument("--j1", help="Specify number of tracts to solve at once (presolve doesn't parallelize)", default=1, type=int)
    parser.add_argument("--j2", help="Specify number of threads for gurobi to use", default=GUROBI_THREADS_DEFAULT, type=int)
    parser.add_argument("--dry-run", help="do not run gurobi; just print model stats", action="store_true")
    parser.add_argument("--csv",   help="Make the CSV file from the solutions", action='store_true')
    parser.add_argument("--exit1", help="Exit Gurobi after the first execution", action='store_true')

    if 'GUROBI_HOME' not in os.environ:
        raise RuntimeError("GUROBI_HOME not in environment")

    args       = parser.parse_args()
    t0         = time.time()
    config     = dbrecon.setup_logging_and_get_config(args=args,prefix="04run")
    state_abbr = dbrecon.state_abbr(args.state_abbr).lower()
    tracts     = args.tracts
    
    DB.quiet = True

    if args.county=='all':
        counties = dbrecon.counties_for_state(state_abbr)
    else:
        counties = [args.county]

    for county in counties:
        run_gurobi_for_county(state_abbr, county, tracts)
        td = round(time.time() - t0,2)
        print(f"{__file__}: Finished {state_abbr} {county} {tracts} in {td} seconds")

    # Create the state-level CSV files
    if args.csv:
        make_csv_file(state_abbr, county)

