#!/usr/bin/env python3
"""
Program to download all of the PL94/SF1/SF2 files from the Census server.
"""

import os.path
import os
import sys
import subprocess

from constants import *

# https://developers.whatismybrowser.com/useragents/explore/operating_system_name/mac-os-x/
USER_AGENT="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7"

if __name__=="__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Compute file changes',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("products", help="Specifies what you wish to download. Should be pl94 sf1 sf2 or any combination thereof.",
                        nargs="*")
    parser.add_argument("--state", help="Just download this state.")

    args = parser.parse_args()
    for product in args.products:

        for statename_abbrev in STATE_DB.split("\n"):
            (state_name,state) = statename_abbrev.split("/")

            zipfilename = {'pl94':PL94_ZIPFILE_NAME,
                           'sf1' :SF1_ZIPFILE_NAME,
                           'sf2' :SF2_ZIPFILE_NAME}[product].format(state_name=state_name,state=state)
            zipdir = os.path.dirname(zipfilename)

            if not os.path.exists( zipdir ):
                os.makedirs( zipdir )

            if args.state and args.state.lower() != state.lower():
                continue

            url = DOWNLOAD_URLS[product].format(state_name=state_name,state=state)
            if os.path.basename(url) != os.path.basename(zipfilename):
                raise RuntimeError("{} != {}".format(os.path.basename(url),os.path.basename(zipfilename)))

            if os.path.exists(zipfilename):
                print("{} exists".format(zipfilename))
                if os.access(zipfilename, os.R_OK) & os.R_OK:
                    print("File is read-only, so it must be good")
                    continue
                # Test the archive
                r = subprocess.call(['unzip','-t',zipfilename])
                if r==0:
                    os.chmod(zipfilename,0o444)
                    print(os.path.basename(url),os.path.basename(zipfilename))
                    continue
                print("{} does not check. Will continue the downloading.".format(zipfilename))
            cmd = ['wget','-U',USER_AGENT,'-c',url,'-O',zipfilename]
            print("$ {}".format(" ".join(cmd)))
            subprocess.check_call(cmd)
