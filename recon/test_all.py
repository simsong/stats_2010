#!/usr/bin/env python3
"""Test the entire system with a reconstruction of Alaska (ak) county 013"""

import pytest
from subprocess import PIPE,run,Popen
from dbrecon import *
import shutil

@pytest.fixture(scope='session')
def setup():
    """Make sure that the GOLD_ROOT exists and prepare TEST_ROOT"""

    config    = get_config()
    ROOTDIR   = dpath_expand("$ROOT")
    TEST_ROOT = dpath_expand("$TEST_ROOT")
    GOLD_ROOT = dpath_expand("$GOLD_ROOT")

    TESTMODE=os.environ.get('TESTMODE','small')

    if TESTMODE=='small':
        (STATE,ST,COUNTY,TRACT) = ('ak', '02', '013', '000100') # small
    elif TESTMODE=='medium':
        (STATE,ST,COUNTY,TRACT) = ('de', '10', '001', '040100') # medium
    elif TESTMODE=='large':
        (STATE,ST,COUNTY,TRACT) = ('ca', '06', '037', '239202') # large

    assert ROOTDIR != TEST_ROOT
    assert ROOTDIR != GOLD_ROOT
    assert len(TEST_ROOT)>1

    # We do not yet handle S3 for testing
    assert GOLD_ROOT.startswith("s3://")==False
    assert TEST_ROOT.startswith("s3://")==False

    # Make sure that the test root exists
    if not os.path.exists(TEST_ROOT):
        os.mkdir(TEST_ROOT)

    if not os.path.exists(f'{TEST_ROOT}/{STATE}'):
        os.mkdir(f'{TEST_ROOT}/{STATE}')

    # Create a test config file in the test root
    TEST_CONFIG_FILE = f"{TEST_ROOT}/test_config.ini"
    config[SECTION_PATHS]["ROOT"] = TEST_ROOT
    config[SECTION_PATHS]["LPROOT"] = TEST_ROOT
    config[SECTION_PATHS]["SF1DATA_ROOT"] = TEST_ROOT
    with open(TEST_CONFIG_FILE,'w') as configfile:
        config.write(configfile)


    # Copy over the SF1 data if it does not exist
    assert os.path.exists(f'{GOLD_ROOT}/{STATE}/{STATE}2010.sf1.zip')
    if not os.path.exists(f'{TEST_ROOT}/{STATE}/{STATE}2010.sf1.zip'):
        shutil.copyfile(f'{GOLD_ROOT}/{STATE}/{STATE}2010.sf1.zip',
                        f'{TEST_ROOT}/{STATE}/{STATE}2010.sf1.zip')

    assert os.path.exists(TEST_CONFIG_FILE)
    assert os.path.exists(f"{GOLD_ROOT}/{STATE}")

    return {'GOLD_ROOT':GOLD_ROOT,
            'TEST_ROOT':TEST_ROOT,
            'TEST_CONFIG_FILE':TEST_CONFIG_FILE,
            'STATE':STATE,
            'ST':ST,
            'COUNTY':COUNTY,
            'TRACT':TRACT
    }

def verify(file_list):
    for fname in file_list:
        t1 = dpath_expand( f"$TEST_ROOT/{fname}")
        t2 = dpath_expand( f"$GOLD_ROOT/{fname}")
        for fn in [t1,t2]:
            if not os.path.exists( fn ):
                raise RuntimeError("{} does not exist".format(fn))
        dsystem(f'cmp {t1} {t2}')
    

def test_01(setup):
    # Run step 01
    STATE = setup['STATE']
    ST    = setup['ST']
    COUNTY= setup['COUNTY']
    TRACT = setup['TRACT']
    TEST_CONFIG_FILE = setup['TEST_CONFIG_FILE']

    dsystem(f'python3 01_make_geo_files.py --config {TEST_CONFIG_FILE} {STATE}')
    verify([f'{STATE}/geofile_{STATE}.csv',
            f'{STATE}/state_county_list_{ST}.csv'])

def test_02(setup):
    # Run step 02
    STATE = setup['STATE']
    ST    = setup['ST']
    COUNTY= setup['COUNTY']
    TRACT = setup['TRACT']
    TEST_CONFIG_FILE = setup['TEST_CONFIG_FILE']

    dsystem(f'python3 02_build_state_stats.py --config {TEST_CONFIG_FILE} {STATE}')
    verify([f'{STATE}/{ST}{COUNTY}/sf1_block_{ST}{COUNTY}.csv',
            f'{STATE}/{ST}{COUNTY}/sf1_tract_{ST}{COUNTY}.csv',
            f'{STATE}/{ST}{COUNTY}/sf1_county_{ST}{COUNTY}.csv'])

def test_03(setup):
    # Run step 03
    STATE = setup['STATE']
    ST    = setup['ST']
    COUNTY= setup['COUNTY']
    TRACT = setup['TRACT']
    TEST_CONFIG_FILE = setup['TEST_CONFIG_FILE']

    dsystem(f'python 03_synth_lp_files.py --config {TEST_CONFIG_FILE} {STATE} {COUNTY} {TRACT}')
    verify([f'{STATE}/{ST}{COUNTY}/lp/model_{ST}{COUNTY}{TRACT}.lp'])

def test_04(setup):
    # Run step 04
    STATE = setup['STATE']
    ST    = setup['ST']
    COUNTY= setup['COUNTY']
    TRACT = setup['TRACT']
    TEST_CONFIG_FILE = setup['TEST_CONFIG_FILE']

    dsystem(f'python3 04_run_gurobi.py --config {TEST_CONFIG_FILE} {STATE} {COUNTY} {TRACT}')
    verify([f'{STATE}/{ST}{COUNTY}/sol/model_{ST}{COUNTY}{TRACT}.sol'])


if __name__=="__main__":
    test_directory_and_files()
    test_01()
    test_02()
    test_03()
    test_04()

    
    
