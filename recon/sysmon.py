#!/usr/bin/env python3
#
"""
sysmon.py:

Report load every 5 minutes
"""

import dbrecon
import time, os, sys, os.path
import datetime
import psutil

sys.path.append( os.path.join(os.path.dirname(__file__),".."))

if __name__=="__main__":
    from argparse import ArgumentParser,ArgumentDefaultsHelpFormatter
    parser = ArgumentParser( formatter_class = ArgumentDefaultsHelpFormatter,
                             description="Report the load every 5 minutes." ) 
    parser.add_argument("--config", help="config file")
    
    args   = parser.parse_args()
    config = dbrecon.get_config(filename=args.config)

    db = dbrecon.DB(config)
    c = db.cursor()
    while True:
        DB().select_and_fetchall("insert into sysload (t, min1, min5, min15) values (now(), %s, %s, %s)",
                                 os.getloadavg())
        DB().commit()
        time.sleep(600)
