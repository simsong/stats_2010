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
import time
import argparse
import csv
import zipfile
import io
import glob
import sys
import atexit
import re
import socket
import pickle
import xml.etree.ElementTree as ET

sys.path.append( os.path.join(os.path.dirname(__file__),".."))

import ctools.s3 as s3
import ctools.clogging as clogging
from total_size import total_size


##
## Functions that return paths.
## These cannot be constants because they do substituion, and f-strings don't work as macros
###
SF1_DIR           = '$ROOT/{state_abbr}/{state_code}{county}'
SF1_RACE_BINARIES = '$SRC/layouts/sf1_vars_race_binaries.csv'


global dfxml_writer
dfxml_writer = None
t0 = time.time()


def SF1_ZIP_FILE(*,state_abbr):
    return f"$SF1_DIST/{state_abbr}2010.sf1.zip".format(state_abbr=state_abbr)

def STEP02_DONE_FILE(*,state_abbr):
    return f'$ROOT/{state_abbr}/completed_{state_abbr}_02'

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
        if not os.path.exists(pathname):
            raise FileNotFoundError(pathname)
        config_file = ConfigParser()
        config_file.read(pathname)
        # Add our source directory to the paths
        config_file[SECTION_PATHS][OPTION_SRC] = SRC_DIRECTORY 
    return config_file

def state_rec(key):
    """Return the record in the state database for a key, where key is the state name, abbreviation, or FIPS code."""
    assert isinstance(key,str)
    for rec in STATES:
        if (key.lower()==rec['state_name'].lower()
            or key.lower()==rec['state_abbr'].lower()
            or key==rec['fips_state']):
                return rec
    raise ValueError(f"{key}: not a valid state name, abbreviation, or FIPS code")

def state_fips(key):
    """Convert state name or abbreviation to FIPS code"""
    assert isinstance(key,str)
    return state_rec(key)['fips_state']

def state_abbr(key):
    """Convert state FIPS code to the appreviation"""
    assert isinstance(key,str)
    return state_rec(key)['state_abbr']

def all_state_abbrs():
    # Return a list of all the states 
    return [rec['state_abbr'].lower() for rec in STATES]

def parse_state_abbrs(statelist):
    # Turn a comman-separated list of states into an array of all state abbreviations.
    # also accepts state numbers
    assert isinstance(statelist,str)
    return [state_rec(key)['state_abbr'].lower() for key in statelist.split(",")]
    
def counties_for_state(state_abbr):
    assert isinstance(state_abbr,str)
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
    """Read the state geofile to determine the number of tracts that are
    in a given county. The state geofile is cached, because it takes a
    while to read. the actual results are also cached in the CACHE_DIR"""
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
    assert isinstance(state_abbr, str)
    assert isinstance(county, str)
    assert isinstance(filetype, str)
    
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

def valid_state_code(code):
    assert isinstance(code,str)
    return len(state)==2 and all(ch.isdigit() for ch in code)

def valid_county_code(code):
    assert isinstance(code,str)
    return len(code)==3 and all(ch.isdigit() for ch in code)

def state_county_tract_has_file(state_abbr, county_code, tract_code, filetype='lp'):
    assert isinstance(state_abbr,str)
    assert isinstance(county_code,str)
    assert isinstance(tract_code,str)
    state_code = state_fips(state_abbr)
    files = dlistdir(f'$ROOT/{state_abbr}/{state_code}{county_code}/{filetype}/')
    return f"model_{state_code}{county_code}{tract_code}.{filetype}" in files

def state_county_has_any_files(state_abbr, county_code, filetype='lp'):
    assert isinstance(state_abbr,str)
    assert isinstance(county_code,str)
    state_code = state_fips(state_abbr)
    files = dlistdir(f'$ROOT/{state_abbr}/{state_code}{county_code}/{filetype}/')
    return any([fn.endswith("."+filetype) for fn in files])

def state_has_any_files(state_abbr, county_code, filetype='lp'):
    assert isinstance(state_abbr,str)
    assert isinstance(county_code,str)
    state_code = state_fips(state_abbr)
    counties   = counties_for_state(state_abbr)
    for county_code in counties:
        if state_county_has_any_files(state_abbr, county_code, filetype=filetype):
            return True


################################################################
### Logging. Much of this was moved to ctools.clogging

# Our generic setup routine
# https://stackoverflow.com/questions/8632354/python-argparse-custom-actions-with-additional-arguments-passed
def argparse_add_logging(parser):
    clogging.add_argument(parser)
    parser.add_argument("--stdout", help="Also log to stdout", action='store_true')
    parser.add_argument("--logmem", action='store_true',
                        help="enable memory debugging. Print memory usage. "
                        "Write output to temp file and compare with correct file.")


def setup_logging(*,config,loglevel=logging.INFO,logdir="logs",prefix='dbrecon',stdout=None,args=None):
    if not prefix:
        prefix = config[SECTION_RUN][OPTION_NAME]

    if args and args.loglevel:
        loglevel = args.loglevel
    if args and args.stdout:
        stdout = args.stdout
    if args and args.logmem:
        stdout = True

    logfname = "{}/{}-{}-{:06}.log".format(logdir,prefix,datetime.datetime.now().isoformat()[0:19],os.getpid())
    if not os.path.exists(logdir):
        os.mkdir(logdir)

    clogging.setup(level=loglevel, filename=logfname)
    logger = logging.getLogger()

    # Log to stdout if requested
    if stdout:
        print("Logging to stdout ")
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.getLevelName(loglevel))
        handler.setFormatter(  logging.Formatter(clogging.LOG_FORMAT) )
        logger.addHandler(handler)

    # Log warnings to stderr
    warning_handler = logging.StreamHandler(sys.stderr)
    warning_handler.setLevel(logging.WARNING)
    warning_handler.setFormatter( logging.Formatter(clogging.LOG_FORMAT) )
    logger.addHandler(warning_handler)

    # Log errors to stderr
    error_handler = logging.StreamHandler(sys.stderr)
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter( logging.Formatter(clogging.LOG_FORMAT) )
    logger.addHandler(error_handler)

    # Log to DFXML
    from dfxml.python.dfxml.writer import DFXMLWriter
    dfxml_writer    = DFXMLWriter(filename=logfname.replace(".log",".dfxml"), prettyprint=True)
    dfxml_handler   = dfxml_writer.logHandler()
    logger.addHandler(dfxml_handler)

    # Log exit codes
    atexit.register(logging_exit)

    # Finally, indicate that we have started up
    logging.info("START %s %s  log level: %s (%s)",sys.executable, " ".join(sys.argv), loglevel,loglevel)
        
def add_dfxml_tag(tag,text=None,attrs={}):
    e = ET.SubElement(dfxml_writer.doc, tag, attrs)
    if text:
        e.text = text


def logging_exit():
    if hasattr(sys,'last_value'):
        logging.error(sys.last_value)


def setup_logging_and_get_config(args,*,prefix=''):
    config = get_config(filename=args.config)
    setup_logging(config=config,prefix=prefix,args=args)
    return 

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
    logging.info("  dopen(path={},mode={},encoding={})".format(path,mode,encoding))
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
            zip_file  = zipfile.ZipFile(dpath_expand(zipfilename))
            zf        = zip_file.open(filename, 'r')
            logging.info("  ZIP: {} found in {}".format(filename,zipfilename))
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

################################################################
##
## memory profiling tools
##

def print_maxrss():
    import resource
    for who in ['RUSAGE_SELF','RUSAGE_CHILDREN']:
        rusage = resource.getrusage(getattr(resource,who))
        print(who,'utime:',rusage[0],'stime:',rusage[1],'maxrss:',rusage[2])

def mem_info(what,df,dump=True):
    import pandas as pd
    print(f'mem_info {what} ({type(df)}):')
    if type(df)!=pd.core.frame.DataFrame:
        print("Total {} memory usage: {:}".format(what,total_size(df)))
    else:
        if dump:
            pd.options.display.max_columns  = 240
            pd.options.display.max_rows     = 5
            pd.options.display.max_colwidth = 240
            print(df)
        for dtype in ['float','int','object']: 
            selected_dtype = df.select_dtypes(include=[dtype])
            mean_usage_b = selected_dtype.memory_usage(deep=True).mean()
            mean_usage_mb = mean_usage_b / 1024 ** 2
            print("Average {} memory usage for {} columns: {:03.2f} MB".format(what,dtype,mean_usage_mb))
        for dt in ['object','int64']:
            for c in df.columns:
                try:
                    if df[c].dtype==dt:
                        print(f"{dt} column: {c}")
                except AttributeError:
                    pass
        df.info(verbose=False,max_cols=160,memory_usage='deep',null_counts=True)
    print("elapsed time at {}: {:.2f}".format(what,time.time() - t0))
    print("==============================")
