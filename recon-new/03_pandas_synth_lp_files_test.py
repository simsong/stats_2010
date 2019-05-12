#!/usr/bin/env python3

from subprocess import check_call,call
import sys
import hashlib
import os
import os.path

TEST_CONFIG_FILE="config_test.ini"

# We test the system by remaking the files for a county in alaska (ak)

SMALL_STATE='al'
SMALL_COUNTY='003'
SMALL_TRACT='011408'
SMALL_TRACT_LP_FILE='/data/sf1/recon_test/al/01003/lp/model_01003011408.lp'
SMALL_TRACT_LP_FILE_SHA1='ef2dbae86ed73be36de45e5015c6c96ce3225c5f'

def test_build_tract_lp():
    # delete the LP files and make sure other files are present for AL
    call(['find','/data/sf1/recon_test/al','-name','*.lp','-erase'])
    check_call(['rsync','--exclude=*.lp','--archive','/data/sf1/recon/al','/data/sf1/recon_test/'])

    assert not os.path.exists(SMALL_TRACT_LP_FILE)

    # Now run for AL
    check_call([sys.executable,'03_synth_lp_files.py','--config',TEST_CONFIG_FILE,
          SMALL_STATE,SMALL_COUNTY,SMALL_TRACT])
    # Now check the results
    assert os.path.exists(SMALL_TRACT_LP_FILE)
    
    digest = hashlib.sha1(open(SMALL_TRACT_LP_FILE,"rb").read()).hexdigest()
    assert digest == SMALL_TRACT_LP_FILE_SHA1



if __name__=="__main__":
    test_all()
