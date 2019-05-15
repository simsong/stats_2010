#!/usr/bin/env python3
#
"""dbrecon.py

Common code and constants for the database reconstruction.
"""

import urllib.parse 
from configparser import ConfigParser
import os
import os.path
import logging
import logging.handlers
import datetime
import argparse
import csv
import zipfile
import io
import glob
import sys
import atexit
import re
import socket
import s3
import pickle


##
## Functions that return paths.
## These cannot be constants because they do substituion, and f-strings don't work as macros
###
SF1_DIR           = "$SF1DATA_ROOT/{state_abbr}/{state_code}{county}"
SF1_RACE_BINARIES = '$SRC/layouts/sf1_vars_race_binaries.csv'


def SF1_BLOCK_DATA_FILE(*,state_abbr,county):
    state_code = state_fips(state_abbr)
    sf1_dir    = SF1_DIR.format(state_code=state_code,county=county,state_abbr=state_abbr)
    return f'{sf1_dir}/sf1_block_{state_code}{county}.csv'

def SF1_TRACT_DATA_FILE(*,state_abbr,county):
    state_code = state_fips(state_abbr)
    sf1_dir        = SF1_DIR.format(state_code=state_code,county=county,state_abbr=state_abbr)
    return f'{sf1_dir}/sf1_tract_{state_code}{county}.csv'

def STATE_COUNTY_LIST(*,root='$ROOT',state_abbr,fips):
    return f"{root}/{state_abbr}/state_county_list_{fips}.csv"

def STATE_COUNTY_DIR(*,root='$ROOT',state_abbr,county):
    fips = state_fips(state_abbr)
    return f"{root}/{state_abbr}/{fips}{county}"

def LPDIR(*,state_abbr,county):
    """Returns the directory where LP files for a particular state and county are stored"""
    fips = state_fips(state_abbr)
    return f'$LPROOT/{state_abbr}/{fips}{county}/lp'

def SOLDIR(*,state_abbr,county):
    """Returns the directory where LP files for a particular state and county are stored"""
    fips = state_fips(state_abbr)
    return f'$LPROOT/{state_abbr}/{fips}{county}/sol'

def LPFILENAME(*,state_abbr,county,geo_id):
    lpdir = LPDIR(state_abbr=state_abbr,county=county)
    return f'{lpdir}/model_{geo_id}.lp'
    
def ILPFILENAME(*,state_abbr,county,geo_id):
    lpdir = LPDIR(state_abbr=state_abbr,county=county)
    return f'{lpdir}/model_{geo_id}.ilp'
    
def SOLFILENAME(*,state_abbr,county,tract):
    soldir = SOLDIR(state_abbr=state_abbr,county=county)
    fips = state_fips(state_abbr)
    return f'{soldir}/model_{fips}{county}{tract}.sol'
    
def COUNTY_CSV_FILENAME(*,state_abbr,county):
    csvdir = STATE_COUNTY_DIR(root='$LPROOT',state_abbr=state_abbr,county=county)
    geo_id = state_fips(state_abbr) + county
    return f'{csvdir}/synth_out_{geo_id}.csv'
    

def find_lp_filename(*,state_abbr,county,tract):
    geoid = state_fips(state_abbr)+county+tract
    lpdir = LPDIR(state_abbr=state_abbr,county=county)
    for key in dlistdir(lpdir):
        if geoid in key and (key.endswith(".lp") or key.endswith(".lp.gz")):
            return os.path.join(lpdir,key)
    return None

##
## For parsing the config file
##
SECTION_PATHS='paths'
SECTION_RUN='run'
OPTION_NAME='NAME'
OPTION_SRC='SRC'                # the $SRC is added to the [paths] section of the config file

SRC_DIRECTORY = os.path.dirname(__file__)

# For handling the config file
CONFIG_FILENAME = "config.ini"
CONFIG_PATHAME  = os.path.join(SRC_DIRECTORY, CONFIG_FILENAME)    # can be changed
config_file     = None              # will become a ConfiParser object

STATE_DATA=[
    "Alabama,AL,01",
    "Alaska,AK,02",
    "Arizona,AZ,04",
    "Arkansas,AR,05",
    "California,CA,06",
    "Colorado,CO,08",
    "Connecticut,CT,09",
    "Delaware,DE,10",
    "District_of_Columbia,DC,11",
    "Florida,FL,12",
    "Georgia,GA,13",
    "Hawaii,HI,15",
    "Idaho,ID,16",
    "Illinois,IL,17",
    "Indiana,IN,18",
    "Iowa,IA,19",
    "Kansas,KS,20",
    "Kentucky,KY,21",
    "Louisiana,LA,22",
    "Maine,ME,23",
    "Maryland,MD,24",
    "Massachusetts,MA,25",
    "Michigan,MI,26",
    "Minnesota,MN,27",
    "Mississippi,MS,28",
    "Missouri,MO,29",
    "Montana,MT,30",
    "Nebraska,NE,31",
    "Nevada,NV,32",
    "New_Hampshire,NH,33",
    "New_Jersey,NJ,34",
    "New_Mexico,NM,35",
    "New_York,NY,36",
    "North_Carolina,NC,37",
    "North_Dakota,ND,38",
    "Ohio,OH,39",
    "Oklahoma,OK,40",
    "Oregon,OR,41",
    "Pennsylvania,PA,42",
    "Rhode_Island,RI,44",
    "South_Carolina,SC,45",
    "South_Dakota,SD,46",
    "Tennessee,TN,47",
    "Texas,TX,48",
    "Utah,UT,49",
    "Vermont,VT,50",
    "Virginia,VA,51",
    "Washington,WA,53",
    "West_Virginia,WV,54",
    "Wisconsin,WI,55",
    "Wyoming,WY,56" ]
STATES=[dict(zip("state_name,state_abbr,fips_state".split(","),line.split(","))) for line in STATE_DATA]

# For now, assume that config.ini is in the same directory as the running script
def get_config(pathname=None,filename=None):
    global config_file
    if not config_file:
        if pathname and filename:
            raise RuntimeError("Cannot specify both pathname and filename")
        if not pathname:
            if not filename:
                filename = CONFIG_FILENAME
            pathname = os.path.join(SRC_DIRECTORY, filename ) 
        assert os.path.exists(pathname)
        config_file = ConfigParser()
        config_file.read(pathname)
        # Add our source directory to the paths
        config_file[SECTION_PATHS][OPTION_SRC] = SRC_DIRECTORY 
    return config_file

def state_rec(key):
    """Return the record in the state database for a key, where key is the state name, abbreviation, or FIPS code."""
    for rec in STATES:
        if (key.lower()==rec['state_name'].lower()
            or key.lower()==rec['state_abbr'].lower()
            or key==rec['fips_state']):
                return rec
    raise ValueError(f"{key}: not a valid state name, abbreviation, or FIPS code")

def state_fips(key):
    """Convert state name or abbreviation to FIPS code"""
    return state_rec(key)['fips_state']

def state_abbr(key):
    """Convert state FIPS code to the appreviation"""
    return state_rec(key)['state_abbr'].lower()

def all_state_abbrs():
    # Return a list of all the states 
    return [rec['state_abbr'].lower() for rec in STATES]

def parse_state_abbrs(statelist):
    # Turn a list of states into an array of all state abbreviations.
    # also accepts state numbers
    return [state_rec(key)['state_abbr'].lower() for key in statelist.split(",")]
    
def counties_for_state(state_abbr):
    fips = state_fips(state_abbr)
    counties = []
    with dopen(STATE_COUNTY_LIST(state_abbr=state_abbr,fips=fips)) as f:
        for line in f:
            (st1,county,st2) = line.strip().split(",")
            assert st1==fips
            assert st2==state_abbr
            counties.append(county)
    return counties

geofile_cache = {}
def tracts_for_state_county(*,state_abbr,county):
    """Read the state geofile to determine the number of tracts that are in a given county. The state geofile is cached, because it takes a while to read. the actual results are also cached in the CACHE_DIR"""
    global geofile_cache
    import pandas as pd

    dmakedirs("$CACHE_DIR")       # make sure that the cache directory exists
    state_county_tracts_fname = f"$CACHE_DIR/{state_abbr}_{county}_tracts.pickle"
    if not dpath_exists(state_county_tracts_fname):
        if state_abbr not in geofile_cache:
            with dopen(f"$ROOT/{state_abbr}/geofile_{state_abbr}.csv") as f:
                df = pd.read_csv(f,
                           dtype={'STATE': object, 'COUNTY': object, 'TRACT': object,
                                  'BLOCK': object, 'BLKGRP': object,
                                  'SUMLEV': object, 'LOGRECNO': object},
                             low_memory=False)
                geofile_cache[state_abbr] = df
        df = geofile_cache[state_abbr]
        tracts = df[df['SUMLEV'].isin(['140'])]
        tracts_in_county = tracts[tracts['COUNTY'].isin([county])]
        with dopen(state_county_tracts_fname,'wb') as f:
            pickle.dump(tracts_in_county['TRACT'].tolist(), f)
    with dopen(state_county_tracts_fname,'rb') as f:
        return pickle.load(f)


################################################################
### Output Products
################################################################
def tracts_with_files(state_abbr,county, filetype='lp'):
    ret = []
    state_code = state_fips(state_abbr)
    if filetype=='lp':
        dirfunc = LPDIR
    elif filetype=='sol':
        dirfunc = SOLDIR
    else:
        raise RuntimeError("only filetype lp and sol supported at the moment")
    for s in dlistdir(dirfunc(state_abbr=state_abbr, county=county)):
        if s.endswith(filetype):
            geo_id = state_code + county
            tract = os.path.basename(s).replace(f"model_{geo_id}","").replace(filetype,"")
            ret.append(tract)
    return ret

def state_county_tract_has_file(state, county_code, tract_code, filetype='lp'):
    sabbr = state_abbr(state)
    scode = state_fips(state)
    path = f'$LPROOT/{sabbr}/{scode}{county_code}/{filetype}/'
    files = list(dlistdir(path))
    return f"model_{scode}{county_code}{tract_code}.{filetype}" in files

def state_county_has_any_files(state, county_code, filetype='lp'):
    sabbr = state_abbr(state)
    scode = state_fips(state)
    path = f'$LPROOT/{sabbr}/{scode}{county_code}/{filetype}/'
    files = dlistdir(path)
    return any([fn.endswith("."+filetype) for fn in files])

def state_has_any_files(state, county_code, filetype='lp'):
    sabbr = state_abbr(state)
    scode = state_fips(state)
    counties   = counties_for_state(state)
    for county_code in counties:
        if state_county_has_any_files(state, county_code, filetype=filetype):
            return True


# Our generic setup routine
# https://stackoverflow.com/questions/8632354/python-argparse-custom-actions-with-additional-arguments-passed
def argparse_add_logging(parser):
    parser.add_argument('--loglevel', help='Set logging level',
                        choices=['CRITICAL','ERROR','WARNING','INFO','DEBUG'],
                        default='INFO')    
    parser.add_argument("--stdout", help="Also log to stdout", action='store_true')


def setup_logging(*,config,loglevel=None,logdir="logs",prefix=None,stdout=None,args=None):
    if not prefix:
        prefix = config[SECTION_RUN][OPTION_NAME]

    if args:
        if not loglevel:
            loglevel = args.loglevel
        if not stdout:
            stdout = args.stdout
        
    logfname = "{}/{}-{}-{:06}.log".format(logdir,prefix,datetime.datetime.now().isoformat()[0:19],os.getpid())
    if not os.path.exists(os.path.dirname(logfname)):
        os.mkdir(os.path.dirname(logfname))

    FORMAT="%(asctime)s %(filename)s:%(lineno)d (%(funcName)s) %(message)s"
    formatter = logging.Formatter(FORMAT)
    logging.basicConfig(filename=logfname, 
                        format=FORMAT,
                        datefmt='%Y-%m-%dT%H:%M:%S',
                        level=logging.getLevelName(loglevel))
    # Make a second handler that logs to syslog
    handler=logging.handlers.SysLogHandler(address="/dev/log",
                                           facility=logging.handlers.SysLogHandler.LOG_LOCAL1)

    logging.getLogger().addHandler(handler)

    # Log to stdout if requested
    if stdout:
        print("will also log to stdout")
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.getLevelName(loglevel))
        handler.setFormatter(formatter)
        logging.getLogger().addHandler(handler)

    # Log errors to stderr
    ehandler = logging.StreamHandler(sys.stderr)
    ehandler.setLevel(logging.ERROR)
    ehandler.setFormatter(formatter)
    logging.getLogger().addHandler(ehandler)

    logging.info("START %s %s  log level: %s (%s)",sys.executable, " ".join(sys.argv), loglevel,loglevel)
    atexit.register(logging_exit)
        
def logging_exit():
    if hasattr(sys,'last_value'):
        logging.error(sys.last_value)


var_re = re.compile(r"(\$[A-Z_][A-Z_0-9]*)")
def dpath_expand(path):
    """dpath_expand is the main path expansion function. It substitutes $VAR for variables in the [path] section of the config
    file. It handles VAR@HOST and expands host automatically. It is called by dopen() to do the expansion.
    """

    # Find and replace all of the dollar variables with those in the config file
    config_file = get_config()
    while True:
        m = var_re.search(path)
        if not m:
            break
        varname  = m.group(1)[1:]
        varname_hostname = varname + "@" + socket.gethostname()
        # See if the variable with my hostname is present. If so, use that one
        if varname_hostname in config_file[SECTION_PATHS]:
            varname = varname_hostname

        if varname in config_file[SECTION_PATHS]:
            val = config_file[SECTION_PATHS][varname]
        elif varname in os.environ:
            val = os.environ[varname]
        else:
            raise KeyError(f"'{varname}' not in [path] of config file and not in global environment")
        path = path.replace(m.group(1), val)
    return path

def dpath_exists(path):
    path = dpath_expand(path)
    if path[0:5]=='s3://':
        ret = s3.s3exists(path)
    else:
        ret = os.path.exists(path)
    logging.info(f"dpath_exists({path})={ret}")
    return ret


def dpath_unlink(path):
    path = dpath_expand(path)
    if path[0:5]=='s3://':
        raise RuntimeError("dpath_unlink doesn't work with s3 paths yet")
    return os.unlink(path)


def dlistdir(path):
    path = dpath_expand(path)
    url = urllib.parse.urlparse(path)
    if url.scheme=='s3':
        bucket = url.netloc
        prefix = url.path[1:]
        if not prefix.endswith('/'):
            prefix += '/'
        logging.info("listing objects in %s",path)
        for d in s3.list_objects(bucket,prefix):
            logging.info(d['Key'])
            yield d['Key']
        return 
    try:
        logging.info("listing files at %s",path)
        for d in os.listdir(path):
            yield d
    except FileNotFoundError as e:
        return []

def dopen(path, mode='r', encoding='utf-8',*, zipfilename=None):
    """An open function that can open from S3 and from inside of zipfiles"""
    logging.info("dopen: path:{} mode:{} encoding:{}".format(path,mode,encoding))
    path = dpath_expand(path)

    if path[0:5]=='s3://':
        return s3.s3open(path, mode=mode, encoding=encoding)

    if 'b' in mode:
        encoding=None

    # Check for full path name
    logging.info("=>open(path={},mode={},encoding={})".format(path,mode,encoding))

    # If opening mode==r, and the file does not exist, see if it is present in the provided ZIP file
    # If a zipfile is not provided, see if we can find one in the directory
    if "r" in mode and (not os.path.exists(path)):
        # path does not exist; see if there is a single zip file in the directory
        # If there is, see if the zipfile has the requested file in it
        (dirname,filename) = os.path.split(path)
        if not zipfilename:
            zipnames = glob.glob(os.path.join(dirname,"*.zip"))
            if len(zipnames)==1:
                zipfilename = zipnames[0]
        if zipfilename:
            zip_file  = zipfile.ZipFile(zipfilename)
            zf        = zip_file.open(filename, 'r')
            logging.info("  ({} found in {})".format(filename,zipfilename))
            if encoding==None and ("b" not in mode):
                encoding='utf-8'
            return io.TextIOWrapper(zf , encoding=encoding)
    if encoding==None:
        return open(path,mode=mode)
    else:
        return open(path,mode=mode,encoding=encoding)

def dmakedirs(dpath):
    """Like os.makedirs, but just returns for s3"""
    path = dpath_expand(dpath)

    # Can't make directories on S3
    if path[0:5]=='s3://':
        return
    logging.info("mkdirs({})".format(path))
    os.makedirs(path,exist_ok=True)


def dgetsize(dpath):
    path = dpath_expand(dpath)
    assert path.startswith("s3://")==False
    return os.path.getsize(path)

def dsystem(x):
    logging.info("system({})".format(x))
    print("$ {}".format(x))
    r = os.system(x)
    if r!=0:
        raise RuntimeError("{} RETURNED {}".format(x,r))
    return r

def print_maxrss():
    import resource
    for who in ['RUSAGE_SELF','RUSAGE_CHILDREN']:
        rusage = resource.getrusage(getattr(resource,who))
        print(who,'utime:',rusage[0],'stime:',rusage[1],'maxrss:',rusage[2])
