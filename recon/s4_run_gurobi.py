#!/usr/bin/env python3
#
# Read the processed SF1 dat and syntheize the LP file that will be input to the optimizer.
#
# When all solutions are present, creates the CSV file

from dbrecon import dopen,dmakedirs,dsystem,dpath_exists
import dbrecon
from math import floor
import csv
import time
import itertools
import sys
import os
import dbrecon
import gc
import logging
import os.path
import pandas as pd
import numpy as np
import psutil
import subprocess
import tempfile


from collections import defaultdict

import gurobipy as gu
import glob, time, os, sys
import csv

# https://www.gurobi.com/documentation/8.1/refman/optimization_status_codes.html#sec:StatusCodes
GUROBI_STATUS_CODES={2:"optimal", 3:"infeasible"}

# Details on Gurobi output:
# http://www.gurobi.com/documentation/8.1/refman/mip_logging.html
GUROBI_THREADS=16


##function for timing later
def millis():
    return int(round(time.time() * 1000))

class RunGurobi:
    def __init__(self,state_abbr, county, tract_code, lp_filename):
        logging.info(f'RunGurobi({state_abbr},{county},{tract_code})')
        self.state_abbr = state_abbr
        self.county = county
        self.tract_code = tract_code
        self.state_code = dbrecon.state_fips(state_abbr)
        self.geoid_tract = self.state_code + self.county + self.tract_code

        self.lp_filename   = lp_filename
        self.ilp_filename  = dbrecon.ILPFILENAME(state_abbr=state_abbr, county=county, geo_id=self.geoid_tract)
        self.p = None

    def sol_filename(self):
        return dbrecon.dpath_expand(dbrecon.SOLFILENAME(state_abbr=state_abbr, county=county, tract=self.tract_code))

    def get_model(self):
        if not dbrecon.dpath_exists(self.lp_filename):
            raise RuntimeError("File does not exist: {}".format(self.lp_filename))

        if self.lp_filename.startswith("s3:"):
            raise RuntimeError("This must be modified to allow Gurobi to read files from S3 using the stdin hack.")

        e = gu.Env.OtherEnv("gurobi.log", "Census", "DAS", 0, "")
        if self.lp_filename.endswith(".lp"):
            self.model = gu.read(dbrecon.dpath_expand(self.lp_filename), env=e)
        elif self.lp_filename.endswith(".lp.gz"):
            self.p = subprocess.Popen(['gunzip'],stdin=dopen(self.lp_filename,'rb'),stdout=subprocess.PIPE)
            os.close(0)         # close stdin
            os.dup2(self.p.stdout.fileno(), 0) # copy to sedin
            e = gu.Env.OtherEnv("gurobi.log", "Census", "DAS", 0, "")
            # Because Gurobin must read from a file that ends with a .lp, 
            # make /tmp/stdin.lp a symlink to /dev/stdin, and
            # then read that
            if not os.path.exists("/tmp/stdin.lp"):
                os.symlink("/dev/stdin","/tmp/stdin.lp")
            self.model = gu.read("/tmp/stdin.lp", env=e)
        else:
            raise RuntimeError("Don't know how to read model from {}".format(self.lp_filename))

    def run_model(self):
        with tempfile.NamedTemporaryFile(suffix='.log',encoding='utf-8') as tf:
            self.model.setParam("Threads",GUROBI_THREADS)
            print("tf.name:",tf.name,type(tf.name))
            self.model.setParam("LogFile",tf.name)

            start_time = millis()
            self.model.optimize()
            end_time = millis()

            mode = GUROBI_STATUS_CODES[self.model.status]

            logging.info(f"geoid_tract: {self.geoid_tract} Solve Time: {end_time-start_time}ms model {mode}")

            # Model is optimal
            dbrecon.dmakedirs( os.path.dirname( self.sol_filename())) # make sure output directory exists
            if self.model.status == 2:
                print('Model is optimal. Writing solution to {}'.format(self.sol_filename()))
                self.model.write(self.sol_filename())

            # Model is infeasible
            if self.model.status == 3:
                print('')
                self.model.computeIIS()
                print('Model is infeasible. Writing ILP to {}'.format(self.ilp_filename))
                self.model.write(dbrecon.dpath_expand(self.ilp_filename))
            
            # Save the results of the log 
            tf.seek(0)
            for line in tf:
                logging.info(line)
            tf.seek(0)
            
                

def run_gurobi_for_county_tract(state_abbr, county, tract):
    assert len(state_abbr)==2
    assert len(county)==3
    assert len(tract)==6
    lp_filename = dbrecon.find_lp_filename(state_abbr=state_abbr,county=county,tract=tract)
    if not lp_filename:
        logging.info(f"no LP file for {state_abbr} {county} {tract}")
        return

    r = RunGurobi(state_abbr, county, tract, lp_filename)
    r.get_model()
    if args.dry_run:
        print(f"MODEL FOR {state_abbr} {county} {tract} ")
        r.model.printStats()
        print("======================================================")
    else:
        r.run_model()
    del r

def run_gurobi_for_county(state_abbr, county):
    logging.info(f"run_gurobi_for_county({state_abbr},{county})")
    if not args.tracts or args.tracts==['all']:
        tracts = dbrecon.tracts_for_state_county(state_abbr=state_abbr, county=county)
    else:
        tracts = args.tracts

    def run_gurobi_tuple(tt):
        run_gurobi_for_county_tract(tt[0], tt[1], tt[2])

    tracttuples = [(state_abbr, county, tract) for tract in tracts]
    if args.j>1:
        from multiprocessing import Pool
        with Pool(args.j) as p:
            p.map(run_gurobi_tuple, tracttuples)
    else:
        for tt in tracttuples:
            run_gurobi_tuple(tt)

def make_csv_file(state_abbr, county):
    # Make sure we have a solution file for every tract
    state_code = dbrecon.state_fips(state_abbr)
    tracts     = dbrecon.tracts_for_state_county(state_abbr=state_abbr, county=county)
    missing = 0
    for tract_code in tracts:
        solfile = dbrecon.SOLFILENAME(state_abbr=state_abbr, county=county, tract=tract_code)
        if not dpath_exists(solfile):
            logging.error("No solution file for: {}".format(solfile))
            missing += 1
    if missing:
        raise RuntimeError("Missing tracts. Stop")

    county_csv_filename = dbrecon.COUNTY_CSV_FILENAME(state_abbr=state_abbr, county=county)
    county_csv_filename_done = county_csv_filename+"-done"
    if dpath_exists(county_csv_filename_done):
        logging.info(f"{county_csv_filename_done} already exists")
        return

    with dopen(county_csv_filename,"w") as outfile:
        w = csv.writer(outfile)
        w.writerow(['geoid_tract','geoid_block','sex','age','white','black','aian','asian','nhopi','sor','hisp'])
        for tract_code in tracts:
            logging.info("Starting tract "+tract_code)
            with dopen(dbrecon.SOLFILENAME(state_abbr=state_abbr, county=county, tract=tract_code),"r") as infile:
                for line in infile:
                    if line[0:2]=='C_': # oldstyle variable
                        (var,count) = line.strip().split(" ")

                        # don't count the zeros
                        if count=="0":
                            continue 
                        c = var.split("_")
                        tract = c[1][5:11]
                        if tract_code != tract:
                            raise RuntimeError(f"{infile.name}: Expecting tract {tract_code} read {tract}")
                        geoid_tract = state_code + county + tract
                        w.writerow([geoid_tract, c[1], c[5], c[6], c[7], c[8], c[9], c[10], c[11], c[12], c[13]])
            logging.info("Ending tract "+tract_code)
    with dopen(county_csv_filename_done,"w") as outfile:
        outfile.write(time.asctime()+"\n")



if __name__=="__main__":
    from argparse import ArgumentParser,ArgumentDefaultsHelpFormatter
    parser = ArgumentParser( formatter_class = ArgumentDefaultsHelpFormatter,
                             description="Run Gurobi and convert the output to the CSV file." )
    dbrecon.argparse_add_logging(parser)
    parser.add_argument("state_abbr", help="2-character state abbreviation")
    parser.add_argument("county", help="3-digit county code")
    parser.add_argument("tracts", help="4-digit tract code[s]; can be 'all'",nargs="*")
    parser.add_argument("--j", help="Specify number of threads", default=1, type=int)
    parser.add_argument("--config", help="config file")
    parser.add_argument("--dry-run", help="do not run gurobi; just print model stats", action="store_true")
    parser.add_argument("--justcsv", help="Just make the CSV file from the solutions", action='store_true')

    
    args       = parser.parse_args()
    config     = dbrecon.setup_logging_and_get_config(args,prefix="02bld")

    state_abbr = dbrecon.state_abbr(args.state_abbr).lower()
    county     = args.county

    if not args.justcsv:
        if 'GUROBI_HOME' not in os.environ:
            raise RuntimeError("GUROBI_HOME not in environment")

        if county=='all':
            logging.info(f"Process all counties in {state_abbr}")
            for county in dbrecon.counties_for_state(state_abbr):
                logging.info(f"county {county}")
                run_gurobi_for_county(state_abbr, county)
        elif county=='next':
            for county in dbrecon.counties_for_state(state_abbr):
                if not state_county_has_any_files(state_abbr, county, filetype='sol'):
                    run_gurobi_for_county(state_abbr, county)
                    break
        else:
            run_gurobi_for_county(state_abbr, county)

    # Create the state-level CSV files
    make_csv_file(state_abbr, county)

    print(f"Logfile: {logfname}")
