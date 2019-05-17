#!/usr/bin/env python3
#
# 02_build_state_stats.py:
# Reads the SF1 files, filter on geolevels 050, 140 and 101,  join the segment files into a single line,
# and output statistics. 
#
# This is a complete rewrite of 02_build_state_stats.py to process the files syntactically instead of semantically.
#

import json
import csv
import sys
import os
import pandas as pd
import numpy as np
import psutil
from collections import OrderedDict
from functools import reduce
import gc
import time
import logging
import multiprocessing

sys.path.append( os.path.join(os.path.dirname(__file__),".."))

from total_size import total_size
import dbrecon
from dbrecon import dopen
from ctools.timer import Timer

# The linkage variables, in the order they appear in the file
SF1_LINKAGE_VARIABLES = ['FILEID','STUSAB','CHARITER','CIFSN','LOGRECNO']

def sf1_zipfilename(state_abbr):
    return dbrecon.dpath_expand(f"$SF1_DIST/{state_abbr}2010.sf1.zip")

ANY="any"
class ReaderException(Exception):
    pass

class SF1SegmentReader():
    def __init__(self,*,state_abbr,segment_filename,names,xy,cifsn):
        """ Given a state abbreviation and a segment number, open it"""
        self.infile = dopen(segment_filename, zipfilename=sf1_zipfilename(state_abbr), encoding='latin1')
        self.fields = None       # the last line read
        self.names  = names      # names of the fields
        self.cifsn  = cifsn
        # process the names as pandas would
        for i in range(0,4):
            self.names[i] = self.names[i]+"_"+xy
        if self.cifsn>1:
            del self.names[4]   #  don't include
        
    def getfields(self,*,logrecno):
        """ Reads a line, looking for logrecno. If not found, return a line of fields """
        if self.fields is None:
            line = self.infile.readline().strip()
            if line=="":
                # End of this segment. Segment 1 has all the logrecs. Otherwise, this just doesn't go to the end
                if self.cifsn==1:
                    raise ReaderException(f"Reached end of CIFSN {self.cifsn} while looking for {logrecno}")
                else:
                    return ['' for name in self.names]
            self.fields   = line.split(",")
            self.logrecno = self.fields[4]

            # Undo the broken transformations
            # Delete LOGRECNO in all but the CIFSN 1
            if self.cifsn>1:
                del self.fields[4] 
            # These two fields were improperly formatted as floats...
            self.fields[2] = format(int(self.fields[2]),'.1f') # CHARITER
            self.fields[3] = format(int(self.fields[3]),'.1f') # CIFSN
            assert len(self.fields) == len(self.names)

        if (self.logrecno == logrecno) or (logrecno==ANY):
            # Map the fields we have to the broken fields that are reported
            def refmt(nv):
                (name,val) = nv
                if name=='PCT012A001':
                    print(name,val,format(float(val),'.1f'))
                if (name in ['CHARITER','CIFSN'] 
                    or name.startswith('PCT') 
                    or name.startswith('HCT') 
                    or name.startswith('PCT012')):
                    return format(float(val),'.1f')

                if '.' in val and len(val)>3:
                    if val[-3]=='.':
                        if val[-1]=='0':
                            return val[0:-1]
                        return val


                return val
            
            fields = ([self.fields[0],        # FILEID
                       self.fields[1],        # STUSAB
                       refmt(('CHARITER',self.fields[2])), # CHARITER
                       refmt(('CIFSN',self.fields[3])), # CIFSN
                       self.fields[4]] +      # LOGRECNO
                      [refmt(nv) for nv in zip(self.names[5:],self.fields[5:]) ])
            
            self.fields = None
            return fields
        return ['' for name in self.names]

def process_state(state_abbr):
    logging.info(f"{state_abbr}: building data frame with all SF1 measurements")
    with Timer() as timer:

        # Read in layouts -- they are json created from xsd from the access database
        # on the website.  Note -- the xsd had to be modified to undo the file
        # mods due to access limitations.  It's read as a ordered dict to preserve
        # the order of the layouts to read the csv.

        state_abbr_upper = state_abbr.upper()
        layouts          = json.load(dopen('$SRC/layouts/layouts.json'), object_pairs_hook=OrderedDict)
        geo_filename     = f"$ROOT/{state_abbr}/geofile_{state_abbr}.csv"
        done_filename    = f"$ROOT/{state_abbr}/completed_{state_abbr}_02"

        # done_filename is created when files are generated
        # If there are no county directories, delete the done file.
        for county in dbrecon.counties_for_state(state_abbr):
            if ( (not dbrecon.dpath_exists(dbrecon.STATE_COUNTY_DIR(state_abbr=state_abbr,county=county) ) )
                 and dbrecon.dpath_exists(done_filename)):
                dbrecon.dpath_unlink(done_filename)

        # If done_file exists, we don't need to run.
        # This would be better done by checking all of the county files.

        if dbrecon.dpath_exists(done_filename):
            print(f"{state_abbr} already exists")
            return

        # Generate the CSV header that the original code used
        # This looks weird, but we are trying to match the original files exactly.
        # while we are here, open the segment files
        field_names = ['']      # PANDASID
        xy = 'x'
        open_segments = []
        for (c,l) in enumerate(layouts,1):
            if l[:3]=='SF1' and l[9:-4]!='mod' and l[10:-5]!='PT':
                cifsn = int(l[4:-4])
                names = layouts[l]
                extra = l[4:-4]
                fname = f'$ROOT/{state_abbr}/sf1/{state_abbr}{extra}2010.sf1'
                segreader = SF1SegmentReader(state_abbr=state_abbr,
                                             segment_filename=fname,
                                             names = names,
                                             xy = xy,
                                             cifsn = cifsn )
                xy = 'y' if xy=='x' else 'x'
                open_segments.append(segreader)

                # add all the field names in order to header record, with pandas-style renaming
                field_names.extend( segreader.names )

        # Add the geoid fields
        JOIN_FIELDS = "STATE,COUNTY,TRACT,BLOCK,BLKGRP,SUMLEV".split(",")
        [field_names.append(field) for field in JOIN_FIELDS]
        field_names.append("geoid")


        ################################################################
        
        # The SF1 directory consists of 47 or 48 segments. The first columns are defined below:
        # Summary levels at https://factfinder.census.gov/help/en/summary_level_code_list.htm
        SUMLEV_COUNTY = '050' # State-County
        SUMLEV_TRACT  = '140' # State-County-Census Tract
        SUMLEV_BLOCK  = '101' # State-County-County Sub∀division-Place/Remainder-Census Tract∀-Block Group-Block

        geo_fields = {a[1]:a[0] for a in enumerate(layouts['GEO_HEADER_SF1.xsd'])}
        assert geo_fields['FILEID']==0 and geo_fields['STUSAB']==1

        GEO_SUMLEV_FIELD  = geo_fields['SUMLEV']
        GEO_LOGRECNO_FIELD= geo_fields['LOGRECNO']
        GEO_STATE_FIELD   = geo_fields['STATE']
        GEO_COUNTY_FIELD  = geo_fields['COUNTY']
        GEO_TRACT_FIELD  = geo_fields['TRACT']
        GEO_BLOCK_FIELD  = geo_fields['BLOCK']

        # Track the logical record for the join (we really don't need the whole field)
        logrecs = {}
        from collections import defaultdict
        counts = defaultdict(int)

        with dopen(geo_filename,"r") as f:
            ct = 0
            for line in f:
                geo_data = line.split(",")
                sumlev   = geo_data[GEO_SUMLEV_FIELD]
                if sumlev in [SUMLEV_COUNTY,SUMLEV_TRACT,SUMLEV_BLOCK]:
                    logrecno = geo_data[GEO_LOGRECNO_FIELD]
                    county   = geo_data[GEO_COUNTY_FIELD]
                    geoid  = "".join(geo_data[f] for f in
                                       [GEO_STATE_FIELD,GEO_COUNTY_FIELD,GEO_TRACT_FIELD,GEO_BLOCK_FIELD])
                    logrecs[logrecno] = (sumlev, ct, county,
                                         [geo_data[ geo_fields[ field ] ] for field in JOIN_FIELDS],
                                         geoid.strip() )
                    counts[sumlev] += 1
                    ct += 1
                
        print("{} geography file processed. counties:{}  tracts:{}  blocks:{}  mem:{:,}".format(
            state_abbr, counts[SUMLEV_COUNTY], counts[SUMLEV_TRACT], counts[SUMLEV_BLOCK],
            total_size(logrecs)))

        # Open the geofile and find all of the LOGRECNOs for the
        # summary summary levels we care about We are splitting on the
        # entire line, which is a waste. But most of the data we are
        # collecting is at the block level, so most of the time we
        # aren't wasting the work


        # Open the block, tract, and county files for every county
        # and write the first line
        output_files = {}
        state_code = dbrecon.state_fips(state_abbr)
        for county_code in dbrecon.counties_for_state(state_abbr):
            countydir = f'$ROOT/{state_abbr}/{state_code}{county_code}'
            dbrecon.dmakedirs(countydir)
            output_files[county_code] = {
                SUMLEV_COUNTY: dopen(f'{countydir}/sf1_county_{state_code}{county_code}.csv','w') ,
                SUMLEV_BLOCK:  dopen(f'{countydir}/sf1_block_{state_code}{county_code}.csv','w') ,
                SUMLEV_TRACT:  dopen(f'{countydir}/sf1_tract_{state_code}{county_code}.csv','w') }
            for f in output_files[county_code].values():
                f.write(",".join(field_names))
                f.write("\n")

        import operator
        count = 0
        while True:
            count += 1
            try:
                fields = open_segments[0].getfields(logrecno=ANY)
            except ReaderException as e:
                break;
            logrecno = fields[4]
            for osr in open_segments[1:]:
                fields.extend(osr.getfields(logrecno=logrecno))
            if fields[0]=='':   # end of file!
                break

            if logrecno in logrecs:
                (sumlev,ct,county,joinfields,geoid) = logrecs[logrecno]

                fields.insert(0,str(ct)) # insert the pandasID
                fields.extend(joinfields) # add the fields that we join
                fields.append(geoid)

                # Check the SF1ST fields. Everyplace we have a SF1ST should be a FILEID
                errors = 0
                for i in range(len(fields)):
                    if fields[i]=='SF1ST' and not field_names[i].startswith('FILEID'):
                        print(f"fields[{i}]={fields[i]}  (should be FILEID field)")
                        errors += 1
                if len(fields) != len(field_names):
                    print(f"Expected {len(field_names)} fields, got {len(fields)}")
                    errors += 1
                if errors>0:
                    for i in range(len(fields)):
                        print(i,field_names[i],fields[i])
                    raise RuntimeError(f"errors: {errors}")

                outline = ",".join(fields) + "\n"
                output_files[county][sumlev].write(outline)




if __name__=="__main__":
    from argparse import ArgumentParser,ArgumentDefaultsHelpFormatter
    parser = ArgumentParser( formatter_class = ArgumentDefaultsHelpFormatter,
                             description="Create per-county county, block and tract count files from the state-level SF1 files." )
    dbrecon.argparse_add_logging(parser)
    parser.add_argument("--config", help="config file")
    parser.add_argument("state_abbrs",nargs="*",help='Specify states to process')
    parser.add_argument("--all",action='store_true',help='All states')
    parser.add_argument("--threads", '--j1', type=int, help='Number of states to run at once (defaults to thread count in config file).')

    args     = parser.parse_args()
    config   = dbrecon.get_config(filename=args.config)
    dbrecon.setup_logging(config=config,loglevel=args.loglevel,prefix="02red")
    logfname = logging.getLogger().handlers[0].baseFilename

    if not dbrecon.dpath_exists(f"$SRC/layouts/layouts.json"):
        raise FileNotFoundError("Cannot find $SRC/layouts/layouts.json")
    
    if not dbrecon.dpath_exists(f"$SRC/layouts/DATA_FIELD_DESCRIPTORS_classified.csv"):
        raise FileNotFoundError("$SRC/layouts/DATA_FIELD_DESCRIPTORS_classified.csv")


    from dfxml.python.dfxml.writer import DFXMLWriter
    dfxml    = DFXMLWriter(filename=logfname.replace(".log",".dfxml"), prettyprint=True)

    states = []
    if args.all:
        states = dbrecon.all_state_abbrs()
    else:
        states = [dbrecon.state_abbr(st).lower() for st in args.state_abbrs]

    if not states:
        print("Specify states to process or --all")
        exit(1)

    if not args.threads:
        args.threads=config['run'].getint('threads',1)

    logging.info("Running with {} threads".format(args.threads))
    if args.threads==1:
        [process_state(state) for state in states]
    else:
        with multiprocessing.Pool(args.threads) as p:
            p.map(process_state, states)
