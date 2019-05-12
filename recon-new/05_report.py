#!/usr/bin/env python3
#
# Generate a report about the current state of the reconstruction
#

from dbrecon import dopen,dmakedirs,dsystem
import dbrecon
from dfxml.python.dfxml.writer import DFXMLWriter
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
import xml.etree.ElementTree as ET

from collections import defaultdict

SF1_DIR = "$ROOT/{state_abbr}/{state_code}{county_code}"

import gurobipy as gu
import glob, time, os, sys
import csv




####Get input parameters

                
def report_state(state_abbr):
    if args.county_code:
        counties = [args.county_code]
    else:
        counties = dbrecon.counties_for_state(state_abbr)
    
    for county in counties:
        if args.tracts:
            tracts = args.tracts
        else:
            tracts = dbrecon.tracts_for_state_county(state_abbr=state_abbr,county=county)

        tracts_with_lp_files = dbrecon.tracts_with_files(state_abbr, county, 'lp')
        tracts_with_sol_files = dbrecon.tracts_with_files(state_abbr, county, 'sol')
        county_csv_filename = dbrecon.COUNTY_CSV_FILENAME(state_abbr=state_abbr, county=county)
        county_csv_filename_done = county_csv_filename+"-done"
        flag = 'DONE' if dbrecon.dpath_exists(county_csv_filename_done) else ''
        print("{} {}  tracts: {:4}  lp files: {:4}  solutions: {:4} {}".format(
            state_abbr,county,len(tracts),len(tracts_with_lp_files),len(tracts_with_sol_files),flag))

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
                             description="Run Gurobi and convert the output to the CSV file." )
    dbrecon.argparse_add_logging(parser)
    parser.add_argument("state_abbr", help="2-character state abbreviation", nargs="?")
    parser.add_argument("county_code", help="3-digit county code", nargs="?")
    parser.add_argument("tracts", help="4-digit tract code[s]; can be 'all'",nargs="*")
    parser.add_argument("--config", help="config file")
    parser.add_argument("--dfxml", help="analyze all files as dfxml", nargs="*")
    
    args = parser.parse_args()

    if args.dfxml:
        for filename in args.dfxml:
            process_dfxml(filename)
        exit(0)

    config = dbrecon.get_config(filename=args.config)


    states = [args.state_abbr] if args.state_abbr else dbrecon.all_state_abbrs()
    for state in states:
        report_state(state)
