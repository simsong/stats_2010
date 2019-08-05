#!/usr/bin/env python3

from subprocess import check_call,call
import sys
import hashlib
import os
import os.path

TEST_CONFIG_FILE="config_test.ini"

# We test by remaking the smallest of all the LP files

SMALL_STUSAB='mo'
SMALL_STATE='29'
SMALL_COUNTY='183'
SMALL_TRACT='980000'

def test_build_tract_lp():
    return 

if __name__=="__main__":
    call([sys.executable,'s3_pandas_synth_lp_files.py','--debug','--output','/tmp/model_29183980000.lp.gz',SMALL_STUSAB,SMALL_COUNTY,SMALL_TRACT,'--stdout'])

