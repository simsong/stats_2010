#!/usr/bin/env python3
#
"""dbrecon.py

Common code and constants for the database reconstruction.
"""

import argparse
import atexit
import csv
import datetime
import glob
import io
import json
import resource
import logging
import logging.handlers
import os
import os.path
import pickle
import re
import socket
import sys
import time
import urllib.parse 
import xml.etree.ElementTree as ET
import zipfile
import psutil
from configparser import ConfigParser

sys.path.append( os.path.join(os.path.dirname(__file__),".."))

import ctools.s3 as s3
import ctools.clogging as clogging
import ctools.dbfile as dbfile
from ctools.gzfile import GZFile
from total_size import total_size

RETRIES = 10
DEFAULT_QUIET=True
STOP_FILE='/tmp/stop.txt'
# For handling the config file
SRC_DIRECTORY   = os.path.dirname(__file__)
CONFIG_FILENAME = "config.ini"
config_path     = os.path.join(SRC_DIRECTORY, CONFIG_FILENAME)    # can be changed
config_file     = None              # will become a ConfiParser object

##
## Functions that return paths.
## These cannot be constants because they do substituion, and f-strings don't work as macros
###
SF1_DIR           = '$ROOT/{state_abbr}/{state_code}{county}'
SF1_RACE_BINARIES = '$SRC/layouts/sf1_vars_race_binaries.csv'

global dfxml_writer
dfxml_writer = None
start_time = time.time()

MB=1000*1000
GB=1000*1000*1000
MiB=1024*1024
GiB=1024*1024*1024
LP='lp'
SOL='sol'
CSV='csv'

################################################################
### Utility Functions ##########################################
################################################################

class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]

def hostname():
    """Hostname without domain"""
    return socket.gethostname().partition('.')[0]

def filename_mtime(fname):
    """Return a file's mtime as a unix time_t"""
    if fname is None:
        return None
    try:
        return datetime.datetime.fromtimestamp(int(os.stat(fname).st_mtime))
    except FileNotFoundError:
        return None

################################################################
### Database management functions ##############################
################################################################

                                                           
db_re = re.compile("export (.*)=(.*)")
def get_pw():
    import pwd
    home = pwd.getpwuid(os.getuid()).pw_dir
    with open( os.path.join( home, 'dbrecon.bash')) as f:
        for line in f:
            m = db_re.search(line.strip())
            if m:
                os.environ[m.group(1)] = m.group(2)

class DB:
    """DB class with singleton pattern"""
    @staticmethod
    def csfr(cmd,vals=None,quiet=False,rowcount=None):
        """Connect, select, fetchall, and retry as necessary"""
        import mysql.connector.errors
        for i in range(1,RETRIES):
            try:
                db = DB()
                db.connect()
                result = None
                c = db.cursor()
                try:
                    logging.info(f"PID{os.getpid()}: {cmd} {vals}")
                    if quiet==False:
                        try:
                            print(f"PID{os.getpid()}: cmd:{cmd} vals:{vals}")
                        except BlockingIOError as e:
                            pass
                    c.execute(cmd,vals)
                    if (rowcount is not None) and ( c.rowcount!=rowcount):
                        logging.error(f"{cmd} {vals} expected rowcount={rowcount} != {c.rowcount}")
                except mysql.connector.errors.ProgrammingError as e:
                    logging.error("cmd: "+str(cmd))
                    logging.error("vals: "+str(vals))
                    logging.error(str(e))
                    raise e
                if cmd.upper().startswith("SELECT"):
                    result = c.fetchall()
                c.close()       # close the cursor
                db.close() # close the connection
                return result
            except mysql.connector.errors.InterfaceError as e:
                logging.error(e)
                logging.error(f"PID{os.getpid()}: NO RESULT SET??? RETRYING {i}/{RETRIES}: {cmd} {vals} ")
                pass
            except mysql.connector.errors.OperationalError as e:
                logging.error(e)
                logging.error(f"PID{os.getpid()}: OPERATIONAL ERROR??? RETRYING {i}/{RETRIES}: {cmd} {vals} ")
                pass
            time.sleep(RETRY_DELAY_TIME)
        raise e

    def cursor(self):
        return self.dbs.cursor()

    def commit(self):
        return self.dbs.commit()

    def create_schema(self,schema):
        return self.dbs.create_schema(schema)

    def connect(self):
        from ctools.dbfile import DBMySQLAuth,DBMySQL
        global config_file
        mysql_section = config_file['mysql']
        auth = DBMySQLAuth(host=os.path.expandvars(mysql_section['host']),
                               database=os.path.expandvars(mysql_section['database']),
                               user=os.path.expandvars(mysql_section['user']),
                               password=os.path.expandvars(mysql_section['password']))
        self.dbs       = DBMySQL(auth)
        self.dbs.cursor().execute('SET @@session.time_zone = "+00:00"') # UTC please
        self.dbs.cursor().execute('SET autocommit = 1') # autocommit

    def close(self):
        return self.dbs.close()

################################################################
### Understanding LP and SOL files #############################
################################################################

def get_final_pop_for_gzfile(sol_filenamegz, requireInt=False):
    count = 0
    errors = 0
    with dopen(sol_filenamegz) as f:
        for (num,line) in enumerate(f,1):
            if line.startswith('C'):
                line = line.strip()
                if line.endswith(" 1"):
                    count += 1
                elif line.endswith(" 0"):
                    pass
                else:
                    if errors==0:
                        logging.error("non-integer solutions in file "+sol_filenamegz)
                    logging.error("line {}: {}".format(num,line))
                    count += round(float(line.split()[1]))
                    errors += 1
    if errors>0 and requireInt:
        raise RuntimeError(f"errors: {errors}")
    return count

def get_final_pop_from_sol(state_abbr,county,tract,delete=True):
    sol_filenamegz = SOLFILENAMEGZ(state_abbr=state_abbr,county=county,tract=tract)
    count = get_final_pop_for_gzfile(sol_filenamegz)
    if count==0 or count>100000:
        logging.warning(f"{sol_filenamegz} has a final pop of {count}. This is invalid, so deleting")
        if delete:
            dpath_unlink(sol_filenamegz)
        DB.csfr("UPDATE tracts set sol_start=null, sol_end=null where stusab=%s and county=%s and tract=%s",
                (state_abbr,county,tract))
        return None
    return count

def db_lock(state_abbr, county, tract):
    DB.csfr("UPDATE tracts set hostlock=%s,pid=%s where stusab=%s and county=%s and tract=%s",
            (hostname(),os.getpid(),state_abbr,county,tract),
            rowcount=1 )
    logging.info(f"db_lock: {hostname()} {sys.argv[0]} {state_abbr} {county} {tract} ")

def db_unlock(state_abbr, county, tract):
    DB.csfr("UPDATE tracts set hostlock=NULL,pid=NULL where stusab=%s and county=%s and tract=%s",
            (state_abbr,county,tract),
            rowcount = 1 )

def db_start(what,state_abbr, county, tract):
    assert what in [LP, SOL, CSV]
    DB.csfr(f"UPDATE tracts set {what}_start=now(),{what}_host=%s,hostlock=%s,pid=%s where stusab=%s and county=%s and tract=%s",
            (hostname(),hostname(),os.getpid(),state_abbr,county,tract),
            rowcount=1 )
    logging.info(f"db_start: {hostname()} {sys.argv[0]} {what} {state_abbr} {county} {tract} ")
    
def db_done(what, state_abbr, county, tract):
    assert what in [LP,SOL, CSV]
    DB.csfr(f"UPDATE tracts set {what}_end=now(),{what}_host=%s,hostlock=NULL,pid=NULL where stusab=%s and county=%s and tract=%s",
            (hostname(),state_abbr,county,tract),rowcount=1)
    logging.info(f"db_done: {what} {state_abbr} {county} {tract} ")
    
def is_db_done(what, state_abbr, county, tract):
    assert what in [LP,SOL, CSV]
    row = DB.csfr(f"SELECT {what}_end FROM tracts WHERE stusab=%s AND county=%s AND tract=%s and {what}_end IS NOT NULL LIMIT 1", 
                  (state_abbr,county,tract))
    return len(row)==1

def db_clean():
    """Clear hostlock if PID is gone"""
    rows = DB.csfr("SELECT pid,stusab,county,tract FROM tracts WHERE hostlock=%s",(hostname(),),quiet=True)
    for (pid,stusab,country,tract) in rows:
        if not pid:
            db_unlock(stusab,county,tract)
            continue
        try:
            p = psutil.Process(pid)
        except psutil.NoSuchProcess:
            db_unlock(stusab,county,tract)

def rescan_files(state_abbr, county, tract, check_final_pop=False, quiet=True):
    raise RuntimeError("don't do at the moment")
    logging.info(f"rescanning {state_abbr} {county} {tract} in database.")
    lpfilenamegz  = LPFILENAMEGZ(state_abbr=state_abbr,county=county,tract=tract)
    solfilenamegz = SOLFILENAMEGZ(state_abbr=state_abbr,county=county, tract=tract)
    
    rows = DB.csfr("SELECT lp_start,lp_end,sol_start,sol_end,final_pop "
                       "FROM tracts where stusab=%s and county=%s and tract=%s LIMIT 1",
                       (state_abbr,county,tract),quiet=quiet)
    if len(rows)!=1:
        raise RuntimeError(f"{state_abbr} {county} {tract} is not in database")
    
    (lp_start,lp_end,sol_start,sol_end,final_pop_db) = rows[0]
    logging.info(f"lp_start={lp_start} lp_end={lp_end} sol_start={sol_start} sol_end={sol_end} final_pop_db={final_pop_db}")
    if dpath_exists(lpfilenamegz):
        if not quiet:
            print(f"{lpfilenamegz} exists")
        if lp_end is None:
            logging.warning(f"{lpfilenamegz} exists but is not in database. Adding")
            DB.csfr("UPDATE tracts set lp_end=%s where stusab=%s and county=%s and tract=%s",
                    (filename_mtime(lpfilenamegz).isoformat()[0:19],state_abbr,county,tract),quiet=quiet)
    else:
        if not quiet:
            print(f"{lpfilenamegz} does not exist")
        if (lp_start is not None) or (lp_end is not None):
            logging.warning(f"{lpfilenamegz} does not exist, but the database says it does. Deleting")
            DB.csfr("UPDATE tracts set lp_start=NULL,lp_end=NULL "
                        "WHERE stusab=%s and county=%s and tract=%s",
                        (state_abbr,county,tract),quiet=quiet)
            
    if dpath_exists(solfilenamegz):
        if sol_end is None:
            logging.warning(f"{solfilenamegz} exists but is not in database. Adding")
            DB.csfr("UPDATE tracts set sol_end=%s where stusab=%s and county=%s and tract=%s",
                    (filename_mtime(solfilenamegz).isoformat()[0:19],state_abbr,county,tract))

        if check_final_pop:
            final_pop_file = get_final_pop_from_sol(state_abbr,county,tract)
            if final_pop_db!=final_pop_file:
                logging.warning(f"final pop in database {final_pop_db} != {final_pop_file} "
                                f"for {state_abbr} {county} {tract}. Correcting")
                DB.csfr("UPDATE tracts set final_pop=%s where stusab=%s and county=%s and tract=%s",
                        (final_pop_file,state_abbr,county,tract))
    else:
        if sol_end is not None:
            logging.warning(f"{solfilenamegz} exists but database says it does not. Removing.")
            DB.csfr("UPDATE tracts set sol_start=NULL,sol_end=NULL,final_pop=NULL where stusab=%s and county=%s and tract=%s",
                    (state,county,tract),quiet=quiet)

################################################################
def should_stop():
    return os.path.exists(STOP_FILE)

def check_stop():
    if should_stop():
        logging.warning("Clean exit")
        os.unlink(STOP_FILE)
        exit(0)

def request_stop():
    with open(STOP_FILE,"w") as f:
        f.write("stop")
        

################################################################
### functions that return directories. dpath_expand is not called on these.

def STATE_COUNTY_DIR(*,root='$ROOT',state_abbr,county):
    fips = state_fips(state_abbr)
    return f"{root}/{state_abbr}/{fips}{county}"

def LPDIR(*,state_abbr,county):
    """Returns the directory where LP files for a particular state and county are stored.
    dpath_expand() is not called because we may search this directory for files."""
    fips = state_fips(state_abbr)
    return f'$ROOT/{state_abbr}/{fips}{county}/lp'

def SOLDIR(*,state_abbr,county):
    """Returns the directory where LP files for a particular state and county are stored.
    dpath_expand() is not called because we may search this directory for files.
    """
    fips = state_fips(state_abbr)
    return f'$ROOT/{state_abbr}/{fips}{county}/sol'

################################################################


def SF1_ZIP_FILE(*,state_abbr):
    return dpath_expand(f"$SF1_DIST/{state_abbr}2010.sf1.zip".format(state_abbr=state_abbr))

def STEP02_DONE_FILE(*,state_abbr):
    return dpath_expand(f'$ROOT/{state_abbr}/completed_{state_abbr}_02')

def SF1_BLOCK_DATA_FILE(*,state_abbr,county):
    state_code = state_fips(state_abbr)
    sf1_dir    = SF1_DIR.format(state_code=state_code,county=county,state_abbr=state_abbr)
    return dpath_expand(f'{sf1_dir}/sf1_block_{state_code}{county}.csv')

def SF1_TRACT_DATA_FILE(*,state_abbr,county):
    state_code = state_fips(state_abbr)
    sf1_dir    = SF1_DIR.format(state_code=state_code,county=county,state_abbr=state_abbr)
    return dpath_expand(f'{sf1_dir}/sf1_tract_{state_code}{county}.csv')

def STATE_COUNTY_LIST(*,root='$ROOT',state_abbr,fips):
    return dpath_expand(f"{root}/{state_abbr}/state_county_list_{fips}.csv")

def LPFILENAMEGZ(*,state_abbr,county,tract):
    geo_id = state_fips(state_abbr)+county+tract
    lpdir  = LPDIR(state_abbr=state_abbr,county=county)
    return dpath_expand(f'{lpdir}/model_{geo_id}.lp.gz')
    
def ILPFILENAME(*,state_abbr,county,tract):
    geo_id = state_fips(state_abbr)+county+tract
    lpdir = LPDIR(state_abbr=state_abbr,county=county)
    return dpath_expand(f'{lpdir}/model_{geo_id}.ilp')
    
def SOLFILENAME(*,state_abbr,county,tract):
    soldir = SOLDIR(state_abbr=state_abbr,county=county)
    fips = state_fips(state_abbr)
    return dpath_expand(f'{soldir}/model_{fips}{county}{tract}.sol')
    
def SOLFILENAMEGZ(*,state_abbr,county,tract):
    return SOLFILENAME(state_abbr=state_abbr,county=county,tract=tract)+".gz"

    
def COUNTY_CSV_FILENAME(*,state_abbr,county):
    csvdir = STATE_COUNTY_DIR(root='$ROOT',state_abbr=state_abbr,county=county)
    geo_id = state_fips(state_abbr) + county
    return dpath_expand(f'{csvdir}/synth_out_{geo_id}.csv')
    
SET_RE = re.compile(r"[^0-9](?P<state>\d\d)(?P<county>\d\d\d)(?P<tract>\d\d\d\d\d\d)[^0-9]")
def extract_state_county_tract(fname):
    m = SET_RE.search(fname)
    if m:
        return( state_abbr(m.group('state')), m.group('county'), m.group('tract'))
    return None

##
## For parsing the config file
##
SECTION_PATHS='paths'
SECTION_RUN='run'
OPTION_NAME='NAME'
OPTION_SRC='SRC'                # the $SRC is added to the [paths] section of the config file


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
def config_reload():
    global config_file,config_path
    config_file = ConfigParser()
    config_file.read(config_path)
    # Add our source directory to the paths
    if SECTION_PATHS not in config_file:
        config_file.add_section(SECTION_PATHS)
    config_file[SECTION_PATHS][OPTION_SRC] = SRC_DIRECTORY 
    return config_file

def get_config(*,filename=None):
    global config_file,config_path
    if config_file is not None:
        return config_file
    if filename is not None:
        config_path = filename
    return config_reload()

def get_config_str(section,name):
    """Like config[section][name], but looks for [name@hostname] first"""
    global config_file
    name_hostname = name + '@' + socket.gethostname()
    if name_hostname in config_file[section]:
        name = name_hostname
    return config_file[section][name]

def get_config_int(section,name):
    return int(get_config_str(section,name))

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
    return state_rec(key)['state_abbr'].lower()

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

def tracts_for_state_county(*,state_abbr,county):
    """Accessing the database, return the tracts for a given state/county"""
    rows = DB.csfr("select tract from tracts where stusab=%s and county=%s",(state_abbr,county))
    return [row[0] for row in rows]

################################################################
### LPFile Manipulation
################################################################

MIN_LP_SIZE = 100        # smaller than this, the file must be invalid
MIN_SOL_SIZE = 1000      # smaller than this, the file is invalid
def lpfile_properly_terminated(fname):
    #
    # Small files are not valid LP files
    if dgetsize(fname) < MIN_LP_SIZE:
        return False
    # If the lpfile is not on S3 and not compressed, we can tell if it is properly terminated
    # by reading the last 3 bytes and seeing if they have an End. This is fast
    if (not fname.startswith("s3:")) and (fname.endswith('.lp')):
        with dopen(fname,"rb") as f:
            f.seek(-4,2)
            last4 = f.read(4)
            return last4 in (b'End\n',b'\nEnd')
    # Otherwise, scan the file
    with dopen(fname,'rb') as f:
        lastline = ''
        for line in f:
            lastline = line
        return b'End' in lastline
    return True

################################################################
### Output Products
################################################################
def tracts_with_files(state_abbr,county, filetype=LP):
    assert isinstance(state_abbr, str)
    assert isinstance(county, str)
    assert isinstance(filetype, str)
    
    ret = []
    state_code = state_fips(state_abbr)
    if filetype==LP or filetype=='lp.gz':
        dirfunc = LPDIR
    elif filetype==SOL or filetype=='sol.gz':
        dirfunc = SOLDIR
    else:
        raise RuntimeError("only filetype lp and sol supported at the moment")
    for s in dlistdir(dirfunc(state_abbr=state_abbr, county=county)):
        if s.endswith(filetype):
            geo_id = state_code + county
            tract = os.path.basename(s).replace(f"model_{geo_id}","")
            dpos = tract.find('.')
            if dpos>0:
                tract = tract[0:dpos]
            ret.append(tract)
    return ret

def valid_state_code(code):
    assert isinstance(code,str)
    return len(state)==2 and all(ch.isdigit() for ch in code)

def valid_county_code(code):
    assert isinstance(code,str)
    return len(code)==3 and all(ch.isdigit() for ch in code)

def state_county_tract_has_file(state_abbr, county_code, tract_code, filetype=LP):
    assert isinstance(state_abbr,str)
    assert isinstance(county_code,str)
    assert isinstance(tract_code,str)
    state_code = state_fips(state_abbr)
    files = dlistdir(f'$ROOT/{state_abbr}/{state_code}{county_code}/{filetype}/')
    return f"model_{state_code}{county_code}{tract_code}.{filetype}" in files

def state_county_has_any_files(state_abbr, county_code, filetype=LP):
    assert isinstance(state_abbr,str)
    assert isinstance(county_code,str)
    state_code = state_fips(state_abbr)
    files = dlistdir(f'$ROOT/{state_abbr}/{state_code}{county_code}/{filetype}/')
    return any([fn.endswith("."+filetype) for fn in files])

def state_has_any_files(state_abbr, county_code, filetype=LP):
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
    parser.add_argument("--config", help="config file")
    parser.add_argument("--stdout", help="Also log to stdout", action='store_true')
    parser.add_argument("--logmem", action='store_true',
                        help="enable memory debugging. Print memory usage. "
                        "Write output to temp file and compare with correct file.")


def setup_logging(*,config,loglevel=logging.INFO,logdir="logs",prefix='dbrecon',stdout=None,args=None,error_alert=True):
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

    if error_alert:
        # Log exit codes
        atexit.register(logging_exit)

    # Finally, indicate that we have started up
    logging.info(f"START {hostname()} {sys.executable} {' '.join(sys.argv)} log level: {loglevel}")
        
def setup_logging_and_get_config(*,args,**kwargs):
    config = get_config(filename=args.config)
    setup_logging(config=config,**kwargs)
    return 

def add_dfxml_tag(tag,text=None,attrs={}):
    e = ET.SubElement(dfxml_writer.doc, tag, attrs)
    if text:
        e.text = text

def log_error(*,error=None, filename=None, last_value=None):
    DB.csfr("INSERT INTO errors (host,error,argv0,file,last_value) VALUES (%s,%s,%s,%s,%s)", (hostname(), error, sys.argv[0], filename, last_value), quiet=True)
    print("LOG ERROR:",error,file=sys.stderr)

def logging_exit():
    if hasattr(sys,'last_value'):
        msg = f'PID{os.getpid()}: {sys.last_value}'
        logging.error(msg)
        log_error(error=msg, filename=__file__, last_value=str(sys.last_value))


var_re = re.compile(r"(\$[A-Z_][A-Z_0-9]*)")
def dpath_expand(path):
    """dpath_expand is the main path expansion function. It substitutes $VAR for variables in the [path] section of the config
    file. It handles VAR@HOST and expands host automatically. It is called by dopen() to do the expansion.
    """

    # Find and replace all of the dollar variables with those in the config file
    global config_file
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
    """An open function that can open from S3 and from inside of zipfiles.
    Don't use this for new projects; use ctools.dconfig.dopen instead"""
    logging.info("  dopen('{}','{}','{}', zipfilename={})".format(path,mode,encoding,zipfilename))
    path = dpath_expand(path)

    if path[0:5]=='s3://':
        return s3.s3open(path, mode=mode, encoding=encoding)

    if 'b' in mode:
        encoding=None

    # Check for full path name
    logging.info("=>open(path={},mode={},encoding={})".format(path,mode,encoding))

    # if opening mode==r and the file does not exist, see if there is a file ending filename.gz,
    # and if it does, open through a pipe with a decompressor.

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

    if path.endswith(".gz"):
        logging.info(f"  passing {path} to GZFile for automatic compress/decompress")
        return GZFile(path,mode=mode,encoding=encoding)
    return open(path,mode=mode,encoding=encoding)

def drename(src,dst):
    logging.info('drename({},{})'.format(src,dst))
    if src.startswith('s3://') or dst.startswith('s3://'):
        raise RuntimeError('drename does not yet implement s3')
    return os.rename( dpath_expand(src), dpath_expand(dst) )

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

def maxrss():
    """Return maxrss in bytes, not KB"""
    return resource.getrusage(resource.RUSAGE_SELF)[2]*1024 

def print_maxrss():
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
    print("elapsed time at {}: {:.2f}".format(what,time.time() - start_time))
    print("==============================")


if __name__=="__main__":
    final_pop = get_final_pop_for_gzfile(sys.argv[1])
    print(sys.argv[1],':',final_pop)

