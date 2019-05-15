import py.test
import sys
import os

sys.path.append( os.path.join( os.path.dirname(__file__), ".."))

from s2_nbuild_state_stats import *

def test_open_segment():
    print("First five lines of segment 1 of AZ:")
    f = open_segment("az",1)
    for i in range(5):
        print(f.readline())
    assert(0)
    
