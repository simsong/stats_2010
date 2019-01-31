#!/usr/bin/env python3

import sf1_decoder
import os
import sys


def extract_table(state,sumlev,table):
    # First get all of the LOGRECNOs for the state and geography
    logrecs = sf1_decoder.logrecno_for_sumlev(state,sumlev)


if __name__=='__main__':
    extract_table('ak','750','P8')
