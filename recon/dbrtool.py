#!/usr/bin/env python3

"""
Program to maniuplate the databsae for the database reconstruciton system.
"""

HELP="""
Manipulate the reconstruction database. Database authenticaiton
credentials come from KMS if they are not in the environment.

Use --env to generate bash statements to put them in your environment. This is
easily done with:

$(./drbtool.py --env)
"""


import os
from os.path import abspath,dirname
import sys
import json
import io
import re
import logging
import subprocess


try:
    import pymysql
except ImportError:
    print("""
    You are running on a cluster that hasn't been updated to include pymysql.
    Execute this command:

    (cd /mnt/gits/das-vm-config && git checkout master && git pull && bash DAS-Bootstrap3-setup-python.sh)

    """,file=sys.stderr)
    exit(1)

DAS_ROOT   = dirname(dirname(dirname(dirname(abspath(__file__)))))
if DAS_ROOT not in sys.path:
    sys.path.append(DAS_ROOT)

BIN_DIR=os.path.join(DAS_ROOT,'bin')
if BIN_DIR not in sys.path:
    sys.path.append(BIN_DIR)

MY_DIR=dirname(abspath(__file__))
if MY_DIR not in sys.path:
    sys.path.append(MY_DIR)

# Import ssh_remote if we can get it. If we cannot, we won't be able to run commands on remote host
try:
    import ssh_remote
    import kms as kms
except ImportError:
    logging.warning("ssh_remote and kms not available")



import dbrecon
import constants

import ctools.s3
import ctools.dbfile as dbfile
from ctools.dbfile import DBMySQL

# Step1 Parallelism
S1_J1 = '50'

# Step2 Parallelism
S2_J1 = '50'

# Step3 parallelism
S3_J1 = "1"
S3_J2 = "32"

# Step4 parallelism
S4_J1 = "16"
S4_J2 = "32"

# Step5 parallelism
S5_J1 = "1"

FAST=True

ENCRYPTED_CONFIG = os.path.join(DAS_ROOT,'dbrecon/dbrecon_config_encrypted.json.ITE')

RECON_DIR    = dirname(abspath(__file__))
RECON_CONFIG = os.path.join(RECON_DIR, 'config.ini')
RECON_SCHEMA = os.path.join(RECON_DIR, 'schema.sql')

# REIDENT separator character.
SEP = '_'
SEP_TRACTS = '_tracts'


def states():
    return [state.lower() for state in constants.STATE_STUSAB if state.lower()!='pr']

def sf1_zipfile_name(reident, stusab):
    return os.path.join(os.environ['DAS_S3ROOT'],f'2010-re/{reident}/dist/{stusab.lower()}2010.sf1.zip')

def get_mysql_env():
    """Return a dictionary of the encrypted MySQL information in the dbrecon_config_encrypted.json.ITE file"""
    # pylint: disable=E0401
    return kms.get_encrypted_json_file( os.path.join( dirname(__file__), ENCRYPTED_CONFIG))[os.getenv('DAS_ENVIRONMENT')]

def put_mysql_env():
    """Put the Mysql authentication variables into the environment"""
    for (key,val) in get_mysql_env().items():
        os.environ[key] = val

def get_auth():
    """Returns a dbfile authentication token from the encrypted file"""
    if 'MYSQL_PASSWORD' in os.environ:
        env = {'MYSQL_USER':os.environ['MYSQL_USER'],
               'MYSQL_PASSWORD':os.environ['MYSQL_PASSWORD'],
               'MYSQL_HOST':os.environ['MYSQL_HOST'],
               'MYSQL_DATABASE':os.environ['MYSQL_DATABASE']}
    else:
        env = get_mysql_env()
    return dbfile.DBMySQLAuth.FromConfig(env)


def do_mysql():
    """Give the user an interactive MySQL shell."""
    env = get_mysql_env()
    cmd = ['mysql','mysql',
           '--user='+env['MYSQL_USER'], '--password='+env['MYSQL_PASSWORD'],
           '--host='+env['MYSQL_HOST'],env['MYSQL_DATABASE']]
    os.execlp(*cmd)

QUERIES = [
    ('Current Time', 'select now()'),
    ("LP and SOL Files created (out of 73507)",
     """SELECT * FROM
             (SELECT COUNT(*) as lp_created from {reident}tracts WHERE lp_end IS NOT NULL) a
              LEFT JOIN
             (select count(*) as sol_created from {reident}tracts WHERE sol_end IS NOT NULL) b
         ON 1=1"""),

    ("LP files in progress",
     """SELECT t.state,t.county,t.tract,t.lp_start,t.lp_host,unix_timestamp() - unix_timestamp(t.lp_start) as age,t.hostlock
     FROM {reident}tracts t LEFT JOIN {reident}geo g ON t.stusab=g.stusab AND t.county=g.county AND t.tract=g.tract
                                       AND g.sumlev='140' and g.pop100>0
     WHERE lp_start IS NOT NULL and LP_END IS NULL ORDER BY hostlock,lp_start"""),

    ("SOLs in progress",
     """SELECT t.state,t.county,t.tract,t.sol_start,t.sol_host,unix_timestamp() - unix_timestamp(t.sol_start) as age,hostlock
     FROM {reident}tracts t LEFT JOIN {reident}geo g ON t.stusab=g.stusab AND t.county=g.county AND t.tract=g.tract
                                       AND g.sumlev='140' and g.pop100>0
     WHERE t.sol_start IS NOT NULL and SOL_END IS NULL ORDER BY t.sol_start"""),

    ("Number of LP files created in past hour:",
     """select count(*) as `count`,lp_host from {reident}tracts
     WHERE unix_timestamp() - unix_timestamp(lp_end) < 3600
     GROUP BY lp_host
     """),

    ("Number of SOL files created in past hour:",
     """select count(*) as `count`,sol_host FROM {reident}tracts
     WHERE unix_timestamp() - unix_timestamp(sol_end) < 3600
     GROUP BY sol_host"""),

    ]



def get_recon_status(auth, reident=None):
    """Perform database queries regarding the current state of the reconstruction and return results as a JSON file.
    this is used for the dashboard API but can be run from the command line as well.
    :param auth: authentication token.
    :return: a dictionary with queries.
          'tables' - all of the tables in the database.
          'reidents' - all of the reidents
    """
    ret = {}
    ret['tables'] =   [row[0] for row in dbfile.DBMySQL.csfr(auth, "SHOW TABLES")]
    ret['queries'] = []
    ret['reidents'] = [table.replace(SEP_TRACTS,"") for table in ret['tables'] if table.endswith(SEP_TRACTS)]
    for reident in get_reidents(auth):
        tables = []
        for(name,query) in QUERIES:
            column_names = []
            rows = DBMySQL.csfr(auth, query.replace("{reident}",reident+"_"), (), asDicts=True,debug=True)
            tables.append((name,rows))
        ret['queries'].append((reident,tables))
    return ret

def api(auth):
    return json.dumps(get_recon_status(auth),default=str);

def get_reidents(auth):
    """Return the reidents.
    :param auth: authentication token.
    :return: a list of the reidents, which is taken to be the prefix of every table with a suffix of `_errors.`
    """
    return [row[0].replace("_tracts","") for row in dbfile.DBMySQL.csfr(auth, f"SHOW TABLES LIKE '%{SEP_TRACTS}'") ]


def do_register(auth, reident):
    """Create a new database with reident as a prefix."""
    db = dbfile.DBMySQL(auth)
    tables = db.execselect(f"SHOW TABLES LIKE '{reident}{SEP_TRACTS}'")
    if tables:
        raise ValueError(f"{reident} already exists")

    # Make sure the zip files exist
    if not FAST:
        print(f"Verifying REIDENT={reident} distribution files")
        for stusab in states():
            path = sf1_zipfile_name(reident, stusab)
            print("\r",path,"...       ",end='')
            if not ctools.s3.s3exists(path):
                raise FileNotFoundError(path)
        print("\n\nSF1 ZIPs present")

    # Now get the schema and transform it for reident by renaming every table
    # and view to {reident}_{name}
    new_schema = io.StringIO()
    create_table_re = re.compile("CREATE TABLE `?([a-z0-9_]+)`?",re.I)
    create_view_re = re.compile("CREATE VIEW `?([a-z0-9_]+)`?",re.I)
    from_re = re.compile("FROM `?([a-z0-9_]+)`?",re.I)

    # This is for rewriting the view:
    # I wasn't able to get the view stuff to work, so we just drop the views
    table_column_re = re.compile("`([a-zA-Z_]+)`[.]`([a-zA-Z_0-9]+)`")
    incomment = False
    for line in open(RECON_SCHEMA):
        # remove all the DROPS for safety!
        if incomment:
            if line.strip().endswith("*/;"):
                incomment = False
            continue
        if " VIEW " in line:
            if not line.strip().endswith("*/;"):
                incomment = True
            continue
        if "CREATE ALGORITHM=UNDEFINED" in line:
            continue

        # Rename tables as necessary

        oline = line
        if "DROP" in line:
            continue
        # fix column in VIEWS. We have to do this in reverse because we keep making the line longer with each substitution.
        if "VIEW" in line:
            for m in reversed(list(table_column_re.finditer(line))):
                line = line[:m.start(1)] + reident + SEP + line[m.start(1):]
        # fix name prefixes
        for r in [create_table_re, create_view_re, from_re]:
            m = r.search(line)
            if m:
                line = line[:m.start(1)] + reident + SEP + line[m.start(1):]
        if oline!=line:
            logging.debug("oline: %s",oline)
            logging.debug("line: %s",line)
            logging.debug("")

        new_schema.write(line)
    print(f"Creating tables with {reident} prefix")
    db.create_schema(new_schema.getvalue())


def run(cmd):
    print()
    print("$ " + " ".join(cmd))
    subprocess.run(cmd, cwd=RECON_DIR, check=True)

def do_step1(auth, reident, state, *, force=False):
    print(f"Step 1 - s1_make_geo_files.py")
    cmd = [sys.executable, 's1_make_geo_files.py', '--j1', S1_J1, '--config', RECON_CONFIG]
    if force:
        cmd.append("--force")
    cmd.append(state)
    run(cmd)

def do_step2(auth, reident, state):
    print(f"Step 2 - s2_nbuild_state_stats.py")
    run([sys.executable, 's2_nbuild_state_stats.py', '--j1', S2_J1, '--config', RECON_CONFIG, state])

def do_step3(auth, reident, state, county, tract):
    print(f"Step 3 - s3_pandas_synth_lp_files.py")
    cmd = [sys.executable, 's3_pandas_synth_lp_files.py', '--config', RECON_CONFIG, '--j1', S3_J1, '--j2', S3_J2, state, county]
    if tract:
        cmd.append(tract)
    run(cmd)

def do_step4(auth, reident, state, county, tracts):
    print(f"Step 4 - s4_run_gurobi.py")
    cmd = [sys.executable, 's4_run_gurobi.py', '--config', RECON_CONFIG, '--j1', S4_J1, '--j2', S4_J2, state, county]+tracts
    run(cmd)

def do_step5(auth, reident, state, county):
    print(f"Step 5 - s5_make_microdata.py")
    cmd = [sys.executable, 's5_make_microdata.py', '--config', RECON_CONFIG, '--j1', S5_J1, state, county]
    run(cmd)


def list_counties(auth, stusab):
    logging.error("A county must be specified. Try one of these:")
    rows = dbfile.DBMySQL.csfr(auth,f"SELECT DISTINCT county FROM {REIDENT}geo where stusab=%s and sumlev='050'",
                               (stusab,))
    for row in rows:
        logging.error("\t%s",row[0])


def list_tracts(auth,stusab, county):
    logging.error("One or more tracts must be specified. Try one of these (or type 'all'):")
    rows = dbfile.DBMySQL.csfr(auth,f"SELECT DISTINCT tract FROM {REIDENT}geo where stusab=%s and county=%s and sumlev='101'",
                               (stusab,county))
    for row in rows:
        logging.error("\t%s",row[0])

def do_drop(auth,reident):
    """Create a new database with reident as a prefix.
    :param auth: authentication token.
    :param reident: reident to use.
    """
    # note that _ is a special character and must be escaped.
    drop_tables = [row[0] for row in dbfile.DBMySQL.csfr(auth,f"SHOW TABLES LIKE '{reident}\\_%%'")]
    if not drop_tables:
        logging.error(f"{reident} is not an active REIDENT")
        exit(1)
    print("Will delete the following tables:")
    print("\n".join(drop_tables))
    print("")
    confirm = input(f"Type '{reident}' to confirm: ").strip()
    if confirm!=reident:
        logging.error("drop tables not confirmed")
        exit(1)
    for table in drop_tables:
        cmd = f"DROP TABLE IF EXISTS {table}"
        print(cmd)
        dbfile.DBMySQL.csfr(auth,cmd)
        cmd = f"DROP VIEW IF EXISTS {table}"
        print(cmd)
        dbfile.DBMySQL.csfr(auth,cmd)


def do_info(path):
    if path.endswith(".sol") or path.endswith(".sol.gz"):
        print(f"{path}:")
        final_pop = dbrecon.get_final_pop_for_gzfile(path)
        print(f"Final pop: {final_pop}")
    else:
        print(f"Don't know how to info: {path}",file=sys.stderr)
        exit(1)

def all_hosts():
    pat = re.compile("(ip-[^ :]+)")
    ret = []
    for line in subprocess.check_output(['yarn','node','--list'],
                                        stderr=open('/dev/null','w'),encoding='utf-8').split('\n'):
            m = pat.search(line)
            if m:
                ret.append(m.group(1))
    return ret



def do_setup(host):
    print("setup ",host)
    p = ssh_remote.run_command_on_host(
        host,
        'cd /mnt/gits/das-vm-config && git checkout master && git pull && bash DAS-Bootstrap3-setup-python.sh; '
        'cd $HOME;'
        'git clone --recursive https://github.ti.census.gov/CB-DAS/das-vm-config.git ; '
        'ln -s das-vm-config/dbrecon/stats_2010/recon;'
        'cd das-vm-config/dbrecon/stats_2010/recon; git pull ; ls -l ; pwd',
        pipeerror=True)
    print(p)


def host_status(host,*, idle_message=""):
    """Print the status of host and return True if it is ready to run"""
    lines = ssh_remote.run_command_on_host(host, 'grep instanceRole /emr/instance-controller/lib/info/extraInstanceData.json;ps ux')
    if "TASK" in lines:
        if "scheduler.py" not in lines:
            print("idle:",host, idle_message)
            return True
        else:
            print("\tin use:", host)
    else:
        print("\tCORE:",host)
    return False


def do_launch(host, *, debug=False, desc=False, reident):
    print(">launch ",host)
    cmd=(
        'git clone https://github.ti.census.gov/CB-DAS/das-vm-config.git --recursive;'
        'cd das-vm-config;'
        'bash DAS-Bootstrap3-setup-python.sh;'
        'source /etc/profile.d/census_dash.sh;'
        'cd dbrecon/stats_2010/recon;'
        'git fetch --all; git checkout master ; git pull; git submodule update;'
        'export DAS_S3ROOT=s3://uscb-decennial-ite-das;'
        'export BCC_HTTPS_PROXY=https://proxy.ti.census.gov:3128;'
        'export BCC_HTTP_PROXY=http://proxy.ti.census.gov:3128;'
        'export AWS_DEFAULT_REGION=us-gov-west-1;'
        'export DAS_ENVIRONMENT=ITE;'
        'export GUROBI_HOME=/usr/local/lib64/python3.6/site-packages/gurobipy;'
        'export GRB_APP_NAME=DAS;'
        'export GRB_LICENSE_FILE=/usr/local/lib64/python3.6/site-packages/gurobipy/gurobi_client.lic;'
        'export GRB_ISV_NAME=Census;'
        "kill $(ps auxww | grep drbtool.py | grep -v grep | awk '{print $2;}');"
        '$(./dbrtool.py --env);'
        f'(./dbrtool.py --run --reident {reident} > output-$(date -Iseconds) 2>&1 </dev/null &)')
    if desc:
        cmd = cmd.replace("--run","--run --desc ")
    out = ssh_remote.run_command_on_host(host, cmd, pipeerror=True)
    if debug:
        print(out)



if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=HELP,
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    g = parser.add_mutually_exclusive_group()
    g.add_argument("--env", action='store_true', help='Generate export functions to put MySQL authentication into your environment')
    g.add_argument("--mysql", action='store_true', help='Provide a MySQL command line')
    g.add_argument("--status", action='store_true', help='Print stats about the current runs')
    g.add_argument("--register", action='store_true', help="register a new REIDENT for database reconstruction.")
    g.add_argument("--drop", action='store_true', help="drop a REIDENT from database")
    g.add_argument("--show", action='store_true', help="Show all reidents in database")
    g.add_argument("--info", help="Provide info on a file")
    g.add_argument("--ls", action='store_true',help="Show the files")
    g.add_argument("--run", help="Run the scheduler",action='store_true')
    g.add_argument("--setup", help="Setup a driver machine to run recon")
    g.add_argument("--setup_all", help="Setup all driver machines to run recon",action='store_true')
    g.add_argument("--uptime_all", help="Run uptime on all machines",action='store_true')
    g.add_argument("--launch", help="Run --run on a specific machine(s) (sep by comma)")
    g.add_argument("--launch_all", help="Run --run on every Task that is not running a scheduler", action='store_true')
    g.add_argument("--status_all", help="report each machine status", action='store_true')

    parser.add_argument("--step1", help="Run step 1 - make the county list. Defaults to all states unless state is specified. Only needs to be run once per state", action='store_true')
    parser.add_argument("--step2", help="Run step 2. Defaults to all states unless state is specified", action='store_true')
    parser.add_argument("--step3", help="manually run Step 3 and make LP files. Normally run this through the controller. This is for testing", action='store_true')
    parser.add_argument("--step4", help="manually run Step 4 and make SOL files. Normally run this through the controller. This is for testing", action='store_true')
    parser.add_argument("--step5", help="manually run Step 5 and make microdata. Normall run this through the controller. This is for testing", action='store_true')
    parser.add_argument("--reident", help="specify the reconstruction identification")
    parser.add_argument("--stusab", help="which stusab to process", default='all')
    parser.add_argument("--county", help="required for step3 and step4")
    parser.add_argument("--tract",  help="required for step 4. Specify multiple tracts with commas between them")
    parser.add_argument('--debug', action='store_true', help='debug all SQL')
    parser.add_argument('--force', action='store_true', help='delete output files if they exist, and force launching on all clusters')
    parser.add_argument('--nodes', help='Show YARN nodes', action='store_true')
    parser.add_argument('--prep', help='Log into each node and prep it for the dbrecon', action='store_true')
    parser.add_argument('--limit', type=int, default=100, help='When launching, launch no more than this.')
    parser.add_argument("--desc", help="Run the scheduler, largest tracts first",action='store_true')
    args = parser.parse_args()

    if args.env:
        for(k,v) in get_mysql_env().items():
            print(f"export {k}={v}")
        exit(0)

    if args.info:
        do_info(args.info)
        exit(0)

    if args.nodes:
        run(['yarn','node','--list'])
        exit(0)

    if args.setup:
        do_setup(args.setup)
        exit(0)

    if args.setup_all:
        for host in all_hosts():
            do_setup( host )
        exit(0)

    if args.uptime_all:
        for host in all_hosts():
            lines = ssh_remote.run_command_on_host(host,'uptime', pipeerror=True).split('\n')
            uptime = [line for line in lines if 'load average' in line]
            if uptime:
                print(host, uptime[0])
            else:
                print(host, "NO OBVIOUS UPTIME")
        exit(0)

    if args.launch:
        if not args.reident:
            print("--launch requires --reident",file=sys.stderr)
            exit(1)
        for host in args.launch.split(','):
            do_launch(args.launch, debug=True, desc=args.desc, reident=args.reident)
        exit(0)

    if args.launch_all:
        if not args.reident:
            print("--launch requires --reident",file=sys.stderr)
            exit(1)
        for host in all_hosts():
            if host_status(host,idle_message='LAUNCHING') or args.force:
                do_launch(host, desc=args.desc, reident=args.reident)
                args.limit -= 1
                if args.limit==0:
                    print("limit reached.")
                    break
        exit(0)

    if args.status_all:
        for host in all_hosts():
            host_status(host)
        exit(0)

    ################################################################
    # Everything after here needs mysql

    if 'MYSQL_HOST' not in os.environ:
        logging.warning('MYSQL_HOST is not in your environment!')
        logging.warning('Next time, please  run $(./dbrtool.py --env) to create the environment variables')
        logging.warning('starting sub-shell with environment variables set')
        for(k,v) in get_mysql_env().items():
            os.environ[k] = v
        os.execlp(os.getenv('SHELL'),os.getenv('SHELL'))


    if args.mysql:
        do_mysql()

    auth = get_auth()
    if args.debug:
        auth.debug = True
        logging.getLogger().setLevel(logging.INFO)

    if args.show:
        print("\n".join(get_reidents(auth)))
        exit(0)
    if args.status:
        ret = get_recon_status(auth, args.reident)
        print(json.dumps(ret,default=str,indent=4))
        exit(0)

    ################################################################
    # Everything after here needs reident
    if args.reident:
        # Pass to subprocesses
        os.environ['REIDENT_NO_SEP'] = args.reident
        dbrecon.REIDENT = os.environ['REIDENT'] = REIDENT = args.reident+"_"
    else:
        print("Please specify --reident\n",file=sys.stderr)
        parser.print_help()
        exit(1)

    if args.register:
        do_register(auth, args.reident)
        print(f"\n{args.reident} registered")
        exit(0)
    elif args.drop:
        do_drop(auth, args.reident)
        print(f"\n{args.reident} dropped")
        exit(0)
    elif args.ls:
        root = os.path.join(os.getenv('DAS_S3ROOT'),'2010-re',args.reident,'work',args.stusab)
        run(['aws','s3','ls','--recursive',root])
    elif args.run:
        cmd = [sys.executable,'scheduler.py']
        if args.stusab:
            cmd.extend(['--stusab',args.stusab])
        if args.county:
            cmd.extend(['--county',args.county])
        if args.desc:
            cmd.extend(['--desc','--maxlp','1','--nosol'])
        run(cmd)


    ################################################################
    # We can run multiple steps if we want! For testing, of course
    if args.step3 or args.step4 or args.step5:
        if args.stusab=='all':
            logging.error("cannot run step3, step4 or step5 on all stusabs; use the scheduler.")
            exit(1)
        if not args.county:
            list_counties(auth, args.stusab)
            exit(1)

    if args.step4:
        if not args.tract or (len(args.tract)!=6 and args.tract!='all'):
            list_tracts(auth, args.stusab, args.county)
            exit(1)

    if args.step1:
        do_step1(auth, args.reident, args.stusab, force=args.force)

    if args.step2:
        do_step2(auth, args.reident, args.stusab)

    if args.step3:
        if args.force:
            dbrecon.remove_lpfile(stusab=args.stusab, county=args.county, tract=args.tract)
        do_step3(auth, args.reident, args.stusab, args.county, args.tract)

    if args.step4:
        if args.force:
            dbrecon.remove_solfile(stusab=args.stusab, county=args.county, tract=args.tract)
        do_step4(auth, args.reident, args.stusab, args.county, args.tract.split(","))

    if args.step5:
        if args.force:
            dbrecon.remove_csvfile(stusab=args.stusab, county=args.county, tract=args.tract)
        do_step5(auth, args.reident, args.stusab, args.county)
