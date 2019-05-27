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

import gurobipy as gu
import dbrecon
from dbrecon import DB
from dbrecon import dopen,dmakedirs,dsystem,dpath_exists

# Details on Gurobi output:
# http://www.gurobi.com/documentation/8.1/refman/mip_logging.html
GUROBI_THREADS_DEFAULT=16
MODEL_ATTRS="NumVars,NumConstrs,NumNZs,NumIntVars,MIPGap,Runtime,IterCount,BarIterCount,isMIP".split(",")

"""Run gurobi with a given LP file. 
Note: automatically handles the case where lpfile is compressed by decompressing
and giving the Gurobi optimizer device to read from.
"""
def run_gurobi(state_abbr, county, tract, lp_filename, dry_run):
    logging.info(f'RunGurobi({state_abbr},{county},{tract})')
    print(f'RunGurobi({state_abbr},{county},{tract})')
    config      = dbrecon.get_config()
    state_abbr  = state_abbr
    county      = county
    tract       = tract
    state_code  = dbrecon.state_fips(state_abbr)
    geoid_tract = state_code + county + tract
    lp_filename = dbrecon.dpath_expand(lp_filename)
    ilp_filename= dbrecon.ILPFILENAME(state_abbr=state_abbr, county=county, geo_id=geoid_tract)
    sol_filename= dbrecon.SOLFILENAME(state_abbr=state_abbr, county=county, tract=tract)
    env         = None # Guorbi environment
    p           = None # subprocess for decompressor
    tempname    = None # symlink that points to decompressed model file


    if lp_filename.startswith("s3:"):
        raise RuntimeError("This must be modified to allow Gurobi to read files from S3 using the stdin hack.")

    if dbrecon.dpath_exists(sol_filename):
        raise FileExistsError(sol_filename)

    if not os.path.exists(lp_filename):
        raise FileNotFoundError("File does not exist: {}".format(lp_filename))

    if os.path.getsize(lp_filename) < dbrecon.MIN_LP_SIZE:
        # lp file is too small. Delete it and remove it from the database
        raise FileNotFoundError("File {} is too small ({})".format(lp_filename,os.path.getsize(lp_filename)))

    customer     = config['gurobi']['customer']
    appname      = config['gurobi']['appname']
    log_filename = os.path.splitext(sol_filename)[0]+".log"
    sol_time     = None
    
    # make sure output directory exists
    dbrecon.dmakedirs( os.path.dirname( sol_filename)) 
    env = gu.Env.OtherEnv( log_filename, customer, appname, 0, "")
    if lp_filename.endswith(".lp"):
        model = gu.read(lp_filename, env=env)
    elif lp_filename.endswith(".lp.gz"):
        p = subprocess.Popen(['zcat',lp_filename],stdout=subprocess.PIPE)
        # Because Gurobin must read from a file that ends with a .lp, 
        # make /tmp/stdin.lp a symlink to /dev/stdin, and
        # then read that
        tempname = f"/tmp/stdin-{p.pid}-{os.getpid()}-{time.time()}.lp"
        if os.path.exists(tempname):
            raise RuntimeError(f"File should not exist: {tempname}")
        os.symlink(f"/dev/fd/{p.stdout.fileno()}",tempname)
        model = gu.read(tempname, env=env)
    else:
        raise RuntimeError("Don't know how to read model from {}".format(lp_filename))

    model.setParam("Threads",args.j2)
    model.setParam("LogToConsole",0)

    if dry_run:
        print(f"MODEL FOR {state_abbr} {county} {tract} ")
        model.printStats()
    else:
        logging.info(f"Starting optimizer. pid={os.getpid()}")
        start_time = time.time()
        model.optimize()
        end_time = time.time()
        sol_time = round(end_time-start_time,4)
        sol_mtime = sol_time*1000

        vars = []
        vals = []

        # Model is optimal
        if model.status == 2:
            logging.info(f'Model {geoid_tract} is optimal. Solve time: {sol_mtime}ms. Writing solution to {sol_filename}')
            model.write(sol_filename)
            dbrecon.db_done('sol', state_abbr, county, tract, sol_time)
        # Model is infeasible. This should not happen
        elif model.status == 3:
            logging.info(f'Model {geoid_tract} is infeasible. Elapsed time: {sol_mtime}ms. Writing ILP to {ilp_filename}')
            dbrecon.dmakedirs( os.path.dirname( ilp_filename)) # make sure output directory exists
            model.computeIIS()
            model.write(dbrecon.dpath_expand(ilp_filename))
        else:
            logging.error(f"Unknown model status code: {model.status}")

        # Save model information in the database
        for name in MODEL_ATTRS:
            try:
                vals.append(model.getAttr(name))
                vars.append(name)
            except AttributeError:
                pass
        # Get the final pop
        vars.append("final_pop")
        vals.append(dbrecon.final_pop(state_abbr,county,tract))
        cmd = "UPDATE tracts set " + ",".join([var+'=%s' for var in vars]) + " where state=%s and county=%s and tract=%s"
        dbrecon.DB().select_and_fetchall(cmd, vals+[state_abbr,county,tract])
    del env


def run_gurobi_for_county_tract(state_abbr, county, tract):
    assert len(state_abbr)==2
    assert len(county)==3
    assert len(tract)==6
    lp_filename  = dbrecon.find_lp_filename(state_abbr=state_abbr,county=county,tract=tract)
    if not lp_filename:
        logging.info(f"no LP file for {state_abbr} {county} {tract}")
        return

    if dbrecon.is_db_done('sol',state_abbr, county, tract):
        logging.warning(f"SOL exists in database: {state_abbr}{county}{tract}; will not solve")
        return

    dbrecon.db_start('sol', state_abbr, county, tract)
    try:
        run_gurobi(state_abbr, county, tract, lp_filename, args.dry_run)
    except FileExistsError as e:
        logging.warning(f"solution file exists for {state_abbr}{county}{tract}; updating database")
        dbrecon.refresh_db(state_abbr, county,tract)
        return

    if args.exit1:
        print("exit1")
        exit(0)



def run_gurobi_tuple(tt):
    """Run gurobi on a tract tuple. 
    This cannot be made a local function inside run_gurobi_for_county because then it won't work with map.
    """
    run_gurobi_for_county_tract(tt[0], tt[1], tt[2])

def run_gurobi_for_county(state_abbr, county, tracts):
    logging.info(f"run_gurobi_for_county({state_abbr},{county})")
    if tracts==['all']:
        db = dbrecon.DB()
        tracts = [row[0] for row in db.select_and_fetchall("select tract from tracts where (lp_end is not null) and (sol_end is null) and state=%s and county=%s",
                                                           (state_abbr, county))]

        if tracts==[]:
            # No tracts. Report if there are unsolved counties
            rows = db.select_and_fetchall("select tract from tracts where (lp_end is null) and state=%s and county=%s",(state_abbr,county))
            if rows:
                logging.warning(f"run_gurobi_for_county({state_abbr},{county}): {len(rows)} tracts do not have LP files")
                return

    tracttuples = [(state_abbr, county, tract) for tract in tracts]
    if args.j1>1:
        from multiprocessing import Pool
        with Pool(args.j1) as p:
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
    parser.add_argument("--config", help="config file")
    parser.add_argument("--dry-run", help="do not run gurobi; just print model stats", action="store_true")
    parser.add_argument("--csv",   help="Make the CSV file from the solutions", action='store_true')
    parser.add_argument("--exit1", help="Exit Gurobi after the first execution", action='store_true')

    if 'GUROBI_HOME' not in os.environ:
        raise RuntimeError("GUROBI_HOME not in environment")

    args       = parser.parse_args()
    config     = dbrecon.setup_logging_and_get_config(args,prefix="04run")
    state_abbr = dbrecon.state_abbr(args.state_abbr).lower()
    tracts     = args.tracts
    
    if tracts==[]:
        tracts=['all']

    if args.county=='all':
        counties = dbrecon.counties_for_state(state_abbr)
    else:
        counties = [args.county]

    for county in counties:
        run_gurobi_for_county(state_abbr, county, tracts)


    # Create the state-level CSV files
    if args.csv:
        make_csv_file(state_abbr, county)

    print(f"{__file__}: Finished {state_abbr} {county}")
