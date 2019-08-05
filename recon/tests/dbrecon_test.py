import py.test
import os
import os.path
import sys

sys.path.append( os.path.join(os.path.dirname(__file__),  ".."))
sys.path.append( os.path.join(os.path.dirname(__file__),  "../.."))

from dbrecon import *

def test_lpfile_properly_termianted():
    here = os.path.dirname(__file__)
    assert lpfile_properly_terminated( os.path.join(here, "shortfile_bad.lp")) == False
    assert lpfile_properly_terminated( os.path.join(here, "shortfile_bad.lp.gz")) == False
    assert lpfile_properly_terminated( os.path.join(here, "model_29183980000.lp.gz")) == True

