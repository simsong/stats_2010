#!/usr/bin/env python3
#
# 00_download_data.py:
# Downloads all of the files

import urllib
import csv
import sys
import os
import os.path
import dbrecon
import logging
import requests
import time    
import zipfile
import glob

from dbrecon import dmakedirs
from dbrecon import dopen,dpath_exists

####Get input parameters

def download(state_abbr, sf1_dest_dir):
    config = dbrecon.get_config()
    state_abbr = state_abbr.lower()
    rec        = dbrecon.state_rec(state_abbr)
    state_code = dbrecon.state_fips(state_abbr)

    ### check for file and if does not exist, download it
    url      = config['urls']['SF1_URL_TEMPLATE'].format(state_name=rec['state_name'], state_abbr=state_abbr)
    sf1_dist = dbrecon.dpath_expand("$SF1_DIST")
    filename = sf1_dist+"/"+os.path.basename(url)
    print(f"Downloading {url} -> {filename}")
    if dpath_exists(filename):
        print("  exists")
        return                  # downloaded

    bytes = 0
    t0 = time.time()
    r = requests.get(url,stream=True)

    with dopen(filename,"wb") as f:
        for chunk in r.iter_content(1024*1024):
            if bytes==0 and chunk[0:2]!=b'PK':
                print("ERROR: {} is not a zip file".format(url))
                os.unlink(filename)
                return
            f.write(chunk)
            bytes += len(chunk)
    t1 = time.time()
    print("   Downloaded {:,} bytes in {:.1f} seconds for {:.0f} Kbytes/sec".format(bytes,t1-t0, bytes/(t1-t0)/1000))



def validate(sf1_dist_dir):
    for zipfilename in glob.glob(os.path.join(sf1_dist_dir,"*.zip")):
        print(zipfilename,"...",end='')
        try:
            with zipfile.ZipFile(zipfilename) as zf:
                print("")
                continue
        except zipfile.BadZipfile as e:
            print("BadZipfile")
            continue



if __name__=="__main__":
    config = dbrecon.get_config()
    from argparse import ArgumentParser,ArgumentDefaultsHelpFormatter
    parser = ArgumentParser( formatter_class = ArgumentDefaultsHelpFormatter,
                             description="Data Migration Tool" )
    dbrecon.argparse_add_logging(parser)
    parser.add_argument("--all",action='store_true',help='All states')
    parser.add_argument("state_abbrs",nargs="*",help='Specify states to download on')
    parser.add_argument("--config", help="config file")
    parser.add_argument("--validate",action='store_true',help='Validate the ZIP files and delete those that are incomplete')
    args = parser.parse_args()

    config = dbrecon.get_config(filename=args.config)

    ## Make sure we have a directory for the state
    sf1_dist_dir = dbrecon.dpath_expand("$SF1_DIST")

    print(f"Downloading to {sf1_dist_dir}")
    dmakedirs(sf1_dist_dir)

    if args.validate:
        validate(sf1_dist_dir)
        exit(0)

    states = []
    if args.all:
        states = dbrecon.all_state_abbrs()
    else:
        states = args.state_abbrs

    if not states:
        print("Specify states to download or --all")
        exit(1)


    for state in states:
        download(state, sf1_dist_dir)
