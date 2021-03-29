#!/usr/bin/env python3
#
"""dbrecon.py

Common code and constants for the database reconstruction.
Note: much of this has been moved to ctools.dbfile.
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
import boto3
import botocore
import subprocess
import inspect
from configparser import ConfigParser
from os.path import dirname,basename,abspath

# Make sure we can read ctools, which is in ..

MY_DIR      = dirname(abspath(__file__))
PARENT_DIR = dirname(MY_DIR)
if PARENT_DIR not in sys.path:
    sys.path.append( PARENT_DIR )

import ctools.s3 as s3
import ctools.clogging as clogging
from ctools.dbfile import DBMySQLAuth,DBMySQL
from ctools.gzfile import GZFile
from total_size import total_size

from dfxml.python.dfxml.writer import DFXMLWriter

REIDENT = os.getenv('REIDENT')

DB_RETRIES = 10
RETRY_DELAY_TIME = 10
DEFAULT_QUIET=True
# For handling the config file
SRC_DIRECTORY   = os.path.dirname( os.path.abspath(__file__))
CONFIG_FILENAME = "config.ini"
CONFIG_PATH     = os.path.join(SRC_DIRECTORY, CONFIG_FILENAME)    # can be changed

S3ZPUT  = os.path.join(MY_DIR, 's3zput') # script that uploads a file to s3 with compression
S3ZCAT  = os.path.join( MY_DIR, 's3zcat') # script that downloads and decompresses a file from s3


def set_reident(reident):
    global REIDENT
    import dbrecon
    dbrecon.REIDENT = REIDENT = os.environ['REIDENT'] = reident + "_"
    os.environ['REIDENT_NO_SEP'] = reident

##
## Functions that return paths.
## These cannot be constants because they do substituion, and f-strings don't work as macros
###
SF1_DIR                        = '$ROOT/work/{stusab}/{state_code}{county}'
SF1_RACE_BINARIES              = '$SRC/layouts/sf1_vars_race_binaries.csv'
GEOFILE_FILENAME_TEMPLATE      = "$ROOT/work/{stusab}/geofile_{stusab}.csv"
STATE_COUNTY_FILENAME_TEMPLATE = '$ROOT/work/{stusab}/state_county_list_{state_code}.csv'


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
### Summary Levels #############################################
################################################################

SUMLEVS = {
    "State": '040',
    "County": '050',
    "Census Tract-Block": '101',
    "Census Tract": '140'
}

SUMLEV_STATE = '040'

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
STATES=[dict(zip("state_name,stusab,fips_state".split(","),line.split(","))) for line in STATE_DATA]

##
## For parsing the config file
##
SECTION_PATHS='paths'
SECTION_RUN='run'
OPTION_NAME='NAME'
OPTION_SRC='SRC'                # the $SRC is added to the [paths] section of the config file

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
    """DB class connection class. Note that this is now in ctools.dbfile and should be removed."""

    @staticmethod
    def csfr(cmd,vals=None,quiet=False,rowcount=None):
        """Connect, select, fetchall, and retry as necessary"""
        try:
            from mysql.connector.errors import ProgrammingError,InterfaceError,OperationalError
        except ImportError as e:
            from pymysql.err import ProgrammingError,InterfaceError,OperationalError

        for i in range(1,DB_RETRIES):
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
                except ProgrammingError as e:
                    logging.error(f" cmd: {cmd}")
                    logging.error(f"vals: {vals}")
                    logging.error(str(e))
                    raise e
                if cmd.strip().upper().startswith("SELECT"):
                    result = c.fetchall()
                c.close()       # close the cursor
                db.close() # close the connection
                return result
            except InterfaceError as e:
                logging.error(e)
                logging.error(f"PID{os.getpid()}: NO RESULT SET??? RETRYING {i}/{DB_RETRIES}: {cmd} {vals} ")
                pass
            except OperationalError as e:
                logging.error(e)
                logging.error(f"PID{os.getpid()}: OPERATIONAL ERROR??? RETRYING {i}/{DB_RETRIES}: {cmd} {vals} ")
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
        config = GetConfig().get_config()
        try:
            mysql_section = config['mysql']
        except KeyError as e:
            print(e,file=sys.stderr)
            print("config:",file=sys.stderr)
            print(config,file=sys.stderr)
            exit(1)
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
### The USA Geography object.
### tracks geographies. We should have created this originally.
################################################################
class USAG:
    __slots__ = ['stusab','state','county','tract']
    def __init__(self, stusab, county, tract, block=None):
        self.stusab = stusab(stusab)
        self.state = state_fips(stusab)
        self.county = county
        self.tract  = tract
        self.block  = block
    def __repr__(self):
        v = " "+self.block if self.block is not None else ""
        return f"<{self.self} {self.stusab} {self.county} {self.tract}{v}>"
    def __eq__(self,a):
        return (self.stusab == a.stusab) and (self.county==a.county) and (self.tract == a.tract) and (self.block==a.block)


################################################################
### Understanding LP and SOL files #############################
################################################################

def get_final_pop_for_gzfile(sol_filenamegz, requireInt=False):
    count = 0
    errors = 0
    with dopen(sol_filenamegz,'r') as f:
        for (num,line) in enumerate(f,1):
            if line.startswith('C'):
                line = line.strip()
                if line.endswith(" 1"):
                    count += 1
                elif line.endswith(" 0"):
                    pass
                else:
                    if errors==0:
                        logging.error("Invalid pop count variables in "+sol_filenamegz)
                    logging.error("line {}: {}".format(num,line))
                    count += round(float(line.split()[1]))
                    errors += 1
    if errors>0 and requireInt:
        raise RuntimeError(f"errors: {errors}")
    return count

def get_final_pop_from_sol(stusab, county, tract, delete=True):
    sol_filenamegz = SOLFILENAMEGZ(stusab=stusab,county=county,tract=tract)
    count = get_final_pop_for_gzfile(sol_filenamegz)
    if count==0 or count>100000:
        logging.warning(f"{sol_filenamegz} has a final pop of {count}. This is invalid, so deleting")
        if delete:
            dpath_unlink(sol_filenamegz)
        DB.csfr(f"UPDATE {REIDENT}tracts set sol_start=null, sol_end=null where stusab=%s and county=%s and tract=%s",
                (stusab,county,tract))
        return None
    return count

################################################################
##
## This implements the hostlock system.
## The hostlock is used by the scheduler to make sure that the same LP or SOL isn't scheduled
## simulatenously on two different nodes.


def db_lock(stusab, county, tract):
    DB.csfr(f"UPDATE {REIDENT}tracts set hostlock=%s,pid=%s where stusab=%s and county=%s and tract=%s",
            (hostname(),os.getpid(),stusab,county,tract),
            rowcount=1)
    logging.info(f"db_lock: {hostname()} {sys.argv[0]} {stusab} {county} {tract} ")

def db_unlock(auth,stusab, county, tract):
    DBMySQL.csfr(auth,f"UPDATE {REIDENT}tracts set hostlock=NULL,pid=NULL where stusab=%s and county=%s and tract=%s",
            (stusab,county,tract),
            rowcount = 1)

def db_start(what,stusab, county, tract):
    assert what in [LP, SOL, CSV]
    DB.csfr(f"UPDATE {REIDENT}tracts set {what}_start=now(),{what}_host=%s,hostlock=%s,pid=%s where stusab=%s and county=%s and tract=%s",
            (hostname(),hostname(),os.getpid(),stusab,county,tract),
            rowcount=1 )
    logging.info(f"db_start: {hostname()} {sys.argv[0]} {what} {stusab} {county} {tract} ")

def db_done(what, stusab, county, tract):
    assert what in [LP,SOL, CSV]
    DB.csfr(f"UPDATE {REIDENT}tracts set {what}_end=now(),{what}_host=%s,hostlock=NULL,pid=NULL where stusab=%s and county=%s and tract=%s",
            (hostname(),stusab,county,tract),rowcount=1)
    logging.info(f"db_done: {what} {stusab} {county} {tract} ")

def is_db_done(what, stusab, county, tract):
    assert what in [LP,SOL, CSV]
    row = DB.csfr(
        f"""
        SELECT {what}_end FROM {REIDENT}tracts t LEFT JOIN {REIDENT}geo g ON (t.stusab=g.stusab and t.county=g.county and t.tract=g.tract)
        WHERE (t.stusab=%s) AND (t.county=%s) AND (t.tract=%s) and ({what}_end IS NOT NULL) AND (g.sumlev='140') AND (g.pop100>0) LIMIT 1
        """,
                  (stusab,county,tract))
    return len(row)==1

def db_clean(auth):
    """Clear hostlock if PID is gone. PID is the PID of the scheduler"""
    rows = DBMySQL.csfr(auth,f"SELECT pid,stusab,county,tract FROM {REIDENT}tracts WHERE hostlock=%s",(hostname(),),quiet=True)
    for (pid,stusab,county,tract) in rows:
        if not pid:
            db_unlock(auth,stusab,county,tract)
            continue
        try:
            p = psutil.Process(pid)
        except psutil.NoSuchProcess:
            db_unlock(auth,stusab,county,tract)

def rescan_files(stusab, county, tract, check_final_pop=False, quiet=True):
    raise RuntimeError("don't do at the moment. The database is more accurate than the file system.")
    logging.info(f"rescanning {stusab} {county} {tract} in database.")
    lpfilenamegz  = LPFILENAMEGZ(stusab=stusab,county=county,tract=tract)
    solfilenamegz = SOLFILENAMEGZ(stusab=stusab,county=county, tract=tract)

    rows = DB.csfr(f"SELECT lp_start,lp_end,sol_start,sol_end,final_pop "
                       "FROM {REIDENT}tracts where stusab=%s and county=%s and tract=%s LIMIT 1",
                       (stusab,county,tract),quiet=quiet)
    if len(rows)!=1:
        raise RuntimeError(f"{stusab} {county} {tract} is not in database")

    (lp_start,lp_end,sol_start,sol_end,final_pop_db) = rows[0]
    logging.info(f"lp_start={lp_start} lp_end={lp_end} sol_start={sol_start} "
                 f"sol_end={sol_end} final_pop_db={final_pop_db}")
    if dpath_exists(lpfilenamegz):
        if not quiet:
            print(f"{lpfilenamegz} exists")
        if lp_end is None:
            logging.warning(f"{lpfilenamegz} exists but is not in database. Adding")
            DB.csfr(f"UPDATE {REIDENT}tracts set lp_end=%s where stusab=%s and county=%s and tract=%s",
                    (filename_mtime(lpfilenamegz).isoformat()[0:19],stusab,county,tract),quiet=quiet)
    else:
        if not quiet:
            print(f"{lpfilenamegz} does not exist")
        if (lp_start is not None) or (lp_end is not None):
            logging.warning(f"{lpfilenamegz} does not exist, but the database says it does. Deleting")
            DB.csfr(f"""
            UPDATE {REIDENT}tracts set lp_start=NULL,lp_end=NULL
            WHERE stusab=%s and county=%s and tract=%s
            """,
                    (stusab,county,tract),quiet=quiet)

    if dpath_exists(solfilenamegz):
        if sol_end is None:
            logging.warning(f"{solfilenamegz} exists but is not in database. Adding")
            DB.csfr(f"UPDATE {REIDENT}tracts set sol_end=%s where stusab=%s and county=%s and tract=%s",
                    (filename_mtime(solfilenamegz).isoformat()[0:19],stusab,county,tract))

        if check_final_pop:
            final_pop_file = get_final_pop_from_sol(stusab,county,tract)
            if final_pop_db!=final_pop_file:
                logging.warning(f"final pop in database {final_pop_db} != {final_pop_file} "
                                f"for {stusab} {county} {tract}. Correcting")
                DB.csfr(f"UPDATE {REIDENT}tracts set final_pop=%s where stusab=%s and county=%s and tract=%s",
                        (final_pop_file,stusab,county,tract))
    else:
        if sol_end is not None:
            logging.warning(f"{solfilenamegz} exists but database says it does not. Removing.")
            DB.csfr(f"UPDATE {REIDENT}tracts SET sol_start=NULL,sol_end=NULL,final_pop=NULL "
                    "WHERE stusab=%s AND county=%s AND tract=%s",
                    (stusab,county,tract),quiet=quiet)

################################################################
### functions that return directory and file locations  ########
################################################################

def STATE_COUNTY_DIR(*,root='$ROOT',stusab,county):
    fips = state_fips(stusab)
    return f"{root}/work/{stusab}/{fips}{county}"

def LPDIR(*,stusab,county):
    """Returns the directory where LP files for a particular state and county are stored.
    dpath_expand() is not called because we may search this directory for files."""
    fips = state_fips(stusab)
    return f'$ROOT/work/{stusab}/{fips}{county}/lp'

def SOLDIR(*,stusab,county):
    """Returns the directory where LP files for a particular state and county are stored.
    dpath_expand() is not called because we may search this directory for files.
    """
    fips = state_fips(stusab)
    return f'$ROOT/work/{stusab}/{fips}{county}/sol'

def SF1_ZIP_FILE(*,stusab):
    return dpath_expand(f"$SF1_DIST/{stusab}2010.sf1.zip".format(stusab=stusab))

def SF1_COUNTY_DATA_FILE(*,stusab,county):
    state_code = state_fips(stusab)
    sf1_dir    = SF1_DIR.format(state_code=state_code,county=county,stusab=stusab)
    return dpath_expand(f'{sf1_dir}/sf1_county_{state_code}{county}.csv')

def SF1_BLOCK_DATA_FILE(*,stusab,county):
    state_code = state_fips(stusab)
    sf1_dir    = SF1_DIR.format(state_code=state_code,county=county,stusab=stusab)
    return dpath_expand(f'{sf1_dir}/sf1_block_{state_code}{county}.csv')

def SF1_TRACT_DATA_FILE(*,stusab,county):
    state_code = state_fips(stusab)
    sf1_dir    = SF1_DIR.format(state_code=state_code,county=county,stusab=stusab)
    return dpath_expand(f'{sf1_dir}/sf1_tract_{state_code}{county}.csv')

def LPFILENAMEGZ(*,stusab,county,tract):
    geo_id = state_fips(stusab)+county+tract
    lpdir  = LPDIR(stusab=stusab,county=county)
    return dpath_expand(f'{lpdir}/model_{geo_id}.lp.gz')

def ILPFILENAME(*,stusab,county,tract):
    geo_id = state_fips(stusab)+county+tract
    lpdir = LPDIR(stusab=stusab,county=county)
    return dpath_expand(f'{lpdir}/model_{geo_id}.ilp')

def SOLFILENAME(*,stusab,county,tract):
    soldir = SOLDIR(stusab=stusab,county=county)
    fips = state_fips(stusab)
    return dpath_expand(f'{soldir}/model_{fips}{county}{tract}.sol')

def SOLFILENAMEGZ(*,stusab,county,tract):
    return SOLFILENAME(stusab=stusab,county=county,tract=tract)+".gz"

def COUNTY_CSV_FILENAME(*,stusab,county):
    csvdir = STATE_COUNTY_DIR(root='$ROOT',stusab=stusab,county=county)
    geo_id = state_fips(stusab) + county
    return dpath_expand(f'{csvdir}/synth_out_{geo_id}.csv')

SET_RE = re.compile(r"[^0-9](?P<state>\d\d)(?P<county>\d\d\d)(?P<tract>\d\d\d\d\d\d)[^0-9]")
def extract_state_county_tract(fname):
    m = SET_RE.search(fname)
    if m:
        return( stusab(m.group('state')), m.group('county'), m.group('tract'))
    return None

def sf1_zipfilename(stusab):
    """If the SF1 is on S3, download it to a known location and work from there.
    This has a race condition if it is run in two different processs. Howeve, it's only done in steps1 and step2,
    and they are threaded on state, not on county.
    """
    sf1_path = dpath_expand(f"$SF1_DIST/{stusab}2010.sf1.zip")
    if sf1_path.startswith("s3://"):
        local_path = "/tmp/" + sf1_path.replace("/","_")

        # if the file doesn't exist or if it exists and is the wrong size, download it
        (bucket,key) = s3.get_bucket_key(sf1_path)
        if not os.path.exists(local_path) or s3.getsize(bucket,key)!=os.path.getsize(local_path):
            logging.warning(f"Downloading {sf1_path} to {local_path}")
            try:
                os.unlink(local_path)
            except FileNotFoundError:
                pass
            s3.get_object(bucket, key, local_path)
        return local_path
    return sf1_path


def auth():
    return DBMySQLAuth.FromConfig(os.environ)


# https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class GetConfig(metaclass=Singleton):
    def __init__(self):
        self.config = None

    def config_reload(self, path=CONFIG_PATH):
        self.config = ConfigParser()
        self.config.read(path)

        # Add our source directory to the paths
        if SECTION_PATHS not in self.config:
            raise RuntimeError(f"No [{SECTION_PATHS}] section in config file {path}")
        self.config[SECTION_PATHS][OPTION_SRC] = SRC_DIRECTORY
        return self.config

    def get_config(self, *, path=CONFIG_PATH):
        if self.config is None:
            self.config_reload(path=path)
        return self.config

def get_config_str(section,name):
    """Like config[section][name], but looks for [name@hostname] first"""
    config = GetConfig().get_config()
    name_hostname = name + '@' + socket.gethostname()
    if name_hostname in config[section]:
        name = name_hostname
    return config[section][name]

def get_config_int(section,name):
    return int(get_config_str(section,name))

def state_rec(key):
    """Return the record in the state database for a key, where key is the state name, abbreviation, or FIPS code."""
    assert isinstance(key,str)
    for rec in STATES:
        if (key.lower()==rec['state_name'].lower()
            or key.lower()==rec['stusab'].lower()
            or key==rec['fips_state']):
                return rec
    raise ValueError(f"{key}: not a valid state name, abbreviation, or FIPS code")

def state_fips(key):
    """Convert state name or abbreviation to FIPS code"""
    assert isinstance(key,str)
    return state_rec(key)['fips_state']

def stusab(key):
    """Convert state FIPS code to the appreviation"""
    assert isinstance(key,str)
    return state_rec(key)['stusab'].lower()

def all_stusabs():
    # Return a list of all the states
    return [rec['stusab'].lower() for rec in STATES]

def parse_stusabs(statelist):
    # Turn a comman-separated list of states into an array of all state abbreviations.
    # also accepts state numbers
    assert isinstance(statelist,str)
    return [state_rec(key)['stusab'].lower() for key in statelist.split(",")]

def counties_for_state(stusab):
    """Return a list of the the county codes (as strings) for the counties in stusab"""
    rows = DB.csfr(f"SELECT county FROM {REIDENT}geo WHERE stusab=%s and sumlev='050'",(stusab,))
    return [row[0] for row in rows]

def tracts_for_state_county(*,stusab,county):
    """Accessing the database, return the tracts for a given state/county.
    Only return tracts with non-zero population
    """
    rows = DB.csfr(
        f"""
        SELECT tract from {REIDENT}tracts t LEFT JOIN {REIDENT}geo g ON (t.stusab=g.stusab AND t.county=g.county AND t.tract=g.tract)
        WHERE (t.stusab=%s) and (t.county=%s) AND (g.sumlev='140') AND (g.pop100>0)
        """,(stusab,county))
    return [row[0] for row in rows]

################################################################
### LPFile Manipulation
################################################################

MIN_LP_SIZE  =  100      # smaller than this, the file must be invalid
MIN_SOL_SIZE = 1000      # smaller than this, the file is invalid
def lpfile_properly_terminated(fname):
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
    try:
        with dopen(fname,'rb') as f:
            lastline = ''
            for line in f:
                lastline = line
            return b'End' in lastline
    except AttributeError as e:
        logging.error("e=%s",e)
        return False
    return True

def remove_lpfile(*,stusab,county,tract):
    lpgz_filename = LPFILENAMEGZ(stusab=stusab,county=county,tract=tract)
    dpath_unlink(lpgz_filename)
    DB.csfr(f"UPDATE {REIDENT}tracts SET lp_start=NULL, lp_end=NULL, lp_gb=NULL, lp_host=NULL WHERE stusab=%s AND county=%s AND tract=%s",
            (stusab,county,tract))


def remove_solfile(*,stusab,county,tract):
    solgz_filename = SOLFILENAMEGZ(stusab=stusab,county=county,tract=tract)
    dpath_unlink(solgz_filename)
    DB.csfr(f"UPDATE {REIDENT}tracts SET sol_start=NULL, sol_end=NULL, sol_gb=NULL, sol_host=NULL WHERE stusab=%s AND county=%s AND tract=%s",
            (stusab,county,tract))

def remove_csvfile(*,stusab,county,tract):
    csv_filename = COUNTY_CSV_FILENAME(stusab=stusab,county=county)
    for fn in [csv_filename, csv_filename+'.tmp']:
        try:
            dpath_unlink(fn)
        except FileNotFoundError as e:
            pass
    DB.csfr(f"UPDATE {REIDENT}tracts SET csv_start=NULL, csv_end=NULL, csv_host=NULL WHERE stusab=%s AND county=%s",
            (stusab,county))



################################################################
### Output Products
################################################################
def valid_state_code(code):
    assert isinstance(code,str)
    return len(code)==2 and all(ch.isdigit() for ch in code)

def valid_county_code(code):
    assert isinstance(code,str)
    return len(code)==3 and all(ch.isdigit() for ch in code)

def state_county_tract_has_file(stusab, county_code, tract_code, filetype=LP):
    assert isinstance(stusab,str)
    assert isinstance(county_code,str)
    assert isinstance(tract_code,str)
    state_code = state_fips(stusab)
    files = dlistdir(f'$ROOT/{stusab}/{state_code}{county_code}/{filetype}/')
    return f"model_{state_code}{county_code}{tract_code}.{filetype}" in files

def state_county_has_any_files(stusab, county_code, filetype=LP):
    assert isinstance(stusab,str)
    assert isinstance(county_code,str)
    state_code = state_fips(stusab)
    files = dlistdir(f'$ROOT/{stusab}/{state_code}{county_code}/{filetype}/')
    return any([fn.endswith("."+filetype) for fn in files])

def state_has_any_files(stusab, county_code, filetype=LP):
    assert isinstance(stusab,str)
    assert isinstance(county_code,str)
    state_code = state_fips(stusab)
    counties   = counties_for_state(stusab)
    for county_code in counties:
        if state_county_has_any_files(stusab, county_code, filetype=filetype):
            return True


################################################################
### Logging. Much of this was moved to ctools.clogging

# Our generic setup routine
# https://stackoverflow.com/questions/8632354/python-argparse-custom-actions-with-additional-arguments-passed
def argparse_add_logging(parser):
    clogging.add_argument(parser)
    parser.add_argument("--config", help="config file")
    parser.add_argument("--reident", help='set reident at command line')
    parser.add_argument("--stdout", help="Also log to stdout", action='store_true')
    parser.add_argument("--logmem", action='store_true',
                        help="enable memory debugging. Print memory usage. "
                        "Write output to temp file and compare with correct file.")


def setup_logging(*,config,loglevel=logging.INFO,logdir="logs",prefix='dbrecon',
                  stdout=None,args=None,error_alert=True):
    global dfxml_writer
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

    # Log to DFXML
    dfxml_writer    = DFXMLWriter(filename=logfname.replace(".log",".dfxml"), prettyprint=True)
    dfxml_handler   = dfxml_writer.logHandler()
    logger.addHandler(dfxml_handler)

    if error_alert:
        # Log exit codes
        atexit.register(logging_exit)

    # Finally, indicate that we have started up
    logging.info(f"START {hostname()} {sys.executable} {' '.join(sys.argv)} log level: {loglevel}")

def setup_logging_and_get_config(*,args,**kwargs):
    if args.reident:
        set_reident(args.reident)
        inspect.stack()[1].frame.f_globals['REIDENT']=os.getenv('REIDENT')
    config = GetConfig().get_config()
    setup_logging(config=config,**kwargs)
    return config

def add_dfxml_tag(tag,text=None,attrs={}):
    e = ET.SubElement(dfxml_writer.doc, tag, attrs)
    if text:
        e.text = text

def log_error(*,error=None, filename=None, last_value=None):
    reident = os.getenv('REIDENT').replace('_','')
    DB.csfr(f"INSERT INTO errors (`host`,`error`,`argv0`,`reident`,`file`,`last_value`) VALUES (%s,%s,%s,%s,%s,%s)",
            (hostname(), error, sys.argv[0], reident, filename, last_value), quiet=True)
    print("LOG ERROR:",error,file=sys.stderr)

def logging_exit():
    if hasattr(sys,'last_value'):
        msg = f'PID{os.getpid()}: {sys.last_value}'
        logging.error(msg)
        log_error(error=msg, filename=__file__, last_value=str(sys.last_value))


var_re = re.compile(r"(\$[A-Z_][A-Z_0-9]*)")
def dpath_expand(path):
    """dpath_expand is the main path expansion function. It substitutes
    $VAR for variables in the [path] section of the config file. It
    handles VAR@HOST and expands host automatically. It is called by
    dopen() to do the expansion.
    """

    # Find and replace all of the dollar variables with those in the config file
    config = GetConfig().get_config()
    while True:
        m = var_re.search(path)
        if not m:
            break
        varname  = m.group(1)[1:]
        varname_hostname = varname + "@" + socket.gethostname()
        # See if the variable with my hostname is present. If so, use that one
        if varname_hostname in config[SECTION_PATHS]:
            varname = varname_hostname

        if varname in config[SECTION_PATHS]:
            val = config[SECTION_PATHS][varname]
        elif varname in os.environ:
            val = os.environ[varname]
        else:
            logging.error("varname: %s",varname)
            logging.error("path: %s",path)
            logging.error("keys in [%s]: %s",SECTION_PATHS,list(config[SECTION_PATHS].keys()))
            raise KeyError(f"'{varname}' not in [{SECTION_PATHS}] of config file and not in global environment")
        path = path[0:m.start(1)] + val + path[m.end(1):]
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
    if path.startswith('s3://'):
        (bucket,key) = s3.get_bucket_key(path)
        r = boto3.client('s3').delete_object(Bucket=bucket, Key=key)
        print("delete",bucket,key,r)
    else:
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

    # immediate passthrough if zipfilename is None and s3 is requested
    if path[0:5]=='s3://' and zipfilename is None:
        if mode.startswith('r') and not s3.s3exists(path):
            raise FileNotFoundError(path)
        if mode=='rb':
            return s3.S3File(path, mode=mode)
        if mode.startswith('w') and path.endswith('.gz'):
            p = subprocess.Popen([ S3ZPUT, '/dev/stdin', path], stdin=subprocess.PIPE, encoding=encoding)
            return p.stdin
        if mode.startswith('r') and path.endswith('.gz'):
            p = subprocess.Popen([ S3ZCAT, path], stdout=subprocess.PIPE, encoding=encoding)
            return p.stdout
        return s3.s3open(path, mode=mode, encoding=encoding)

    if 'b' in mode:
        encoding=None

    # immediate passthrough if zipfilename  is provided
    if zipfilename:
        assert mode.startswith('r') # can only read from zipfiles
        filename = os.path.basename(path)
        zip_file = zipfile.ZipFile(dopen(zipfilename, mode='rb'))
        zf       = zip_file.open(filename, 'r')
        if encoding==None and ("b" not in mode):
            encoding='utf-8'
        logging.info("zipfilename bypass: zipfilename=%s filename=%s  mode=%s encoding=%s",zipfilename,filename,mode,encoding)
        return io.TextIOWrapper(io.BufferedReader(zf, buffer_size=1024*1024) , encoding=encoding) # big buffer please


    # Legacy code follow
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
            zip_file  = zipfile.ZipFile(dopen(zipfilename, mode='rb'))
            zf        = zip_file.open(filename, 'r')
            logging.info("  ZIP: {} found in {}".format(filename,zipfilename))
            if encoding==None and ("b" not in mode):
                encoding='utf-8'
            return io.TextIOWrapper(zf , encoding=encoding)

    if path.endswith(".gz"):
        logging.info(f"  passing {path} to GZFile for automatic compress/decompress")
        return GZFile(path,mode=mode,encoding=encoding)
    return open(path,mode=mode,encoding=encoding)

def dwait_exists(src):
    """When writing to S3, objects may not exist immediately. You can call this to wait until they do."""
    if src.startswith('s3://'):
        (bucket,key) = s3.get_bucket_key(src)
        cmd=['wait','object-exists','--bucket',bucket,'--key',key]
        logging.info(' '.join(cmd))
        try:
            s3.aws_s3api(cmd)
        except RuntimeError as e:
            raise FileNotFoundError(src)
        logging.info('dwait_exists %s returning',src)
    else:
        if os.path.exists(src):
            return
        raise RuntimeError("not implemented yet to wait for unix files")

def drename(src,dst):
    logging.info('drename({},{})'.format(src,dst))
    if src.startswith('s3://') and dst.startswith('s3://'):
        try:
            (src_bucket, src_key) = s3.get_bucket_key(src)
            (dst_bucket, dst_key) = s3.get_bucket_key(dst)
            s3r = boto3.resource('s3')
            s3r.Object(dst_bucket,dst_key).copy_from(CopySource=src_bucket + '/' + src_key)
            s3r.Object(src_bucket, src_key).delete()
            return
        except botocore.errorfactory.NoSuchKey as e:
            raise FileNotFoundError(src)

    if src.startswith('s3://') or dst.startswith('s3://'):
        raise RuntimeError('drename does not implement renaming local file to S3')
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
    if path.startswith("s3://"):
        (bucket,key) = s3.get_bucket_key(path)
        try:
            return boto3.resource('s3').Object(bucket,key).content_length
        except botocore.exceptions.ClientError as err:
            if err.response['Error']['Code']=='404':
                raise FileNotFoundError(path) from err
            raise
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
    from argparse import ArgumentParser,ArgumentDefaultsHelpFormatter
    parser = ArgumentParser( formatter_class = ArgumentDefaultsHelpFormatter,
                             description="Get the count for SOL.GZ files" )
    parser.add_argument("gzfile",nargs="*")
    args     = parser.parse_args()
