#!/usr/bin/env python3
#
"""
sysmon.py:

Report load and free memory every 5 minutes
"""

import datetime
import os
import os.path
import psutil
import sys
import time

import dbrecon
import scheduler

sys.path.append( os.path.join(os.path.dirname(__file__),".."))

if __name__=="__main__":
    from argparse import ArgumentParser,ArgumentDefaultsHelpFormatter
    parser = ArgumentParser( formatter_class = ArgumentDefaultsHelpFormatter,
                             description="Report the load every 5 minutes." ) 
    parser.add_argument("--config", help="config file")
    parser.add_argument("--noisy", action='store_true')
    
    args   = parser.parse_args()
    config = dbrecon.get_config(filename=args.config)

    while True:
        scheduler.report_load_memory(quiet=not args.noisy)
        time.sleep(600)
