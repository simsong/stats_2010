import py.test
import sys
import os

sys.path.append("..")


from s2_nbuild_state_stats import *

def test_open_segment():
    print("First five lines of segment 1 of AZ:")
    f = open_segment("az",1)
    for i in range(5):
        print(f.readline())
        
    
