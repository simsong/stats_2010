import sys,os,os.path

sys.path.append( os.path.join( os.path.dirname(__file__), ".."))

import constants

def test_STATE_ABBR_TO_FIPS():
    assert constants.STATE_ABBR_TO_FIPS['WY'] == '56'
