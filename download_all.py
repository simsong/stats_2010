#!/usr/bin/env python3
"""
Program to download all of the PL94/SF1/SF2 files from the Census server.
"""

import os.path
import os
import sys
import subprocess
import random
import zipfile

from constants import *

# https://developers.whatismybrowser.com/useragents/explore/operating_system_name/mac-os-x/
# A user agent that can be parameterized with two random numbers
USER_AGENT="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/{r1}.7.7 (KHTML, like Gecko) Version/{r2}.1.2 Safari/601.7.7"

def check_zip(zipfilename):
    """Check the file fname. If it is not writable, just return. 
    If it is a valid zip, then make it not writable. Return true if it checks"""
    if os.access(zipfilename, os.R_OK) & os.R_OK:
        return True
    # Test the archive
    try:
        with zipfile.ZipFile( zipfilename ) as zip_file:
            # Zipfile is good!
            os.chmod(zipfilename,0o444)
            return True
    except zipfile.BadZipFile as e:
        # zipfile is bad
        return False


def download(url,zipdir):
    if not os.path.exists( zipdir ):
        os.makedirs( zipdir )

    # Make sure format is the same
    zipfilename = os.path.join(zipdir, os.path.basename(url))
    if os.path.exists(zipfilename):
        if check_zip(zipfilename):
            return

    print(f"{url} -> {zipfilename}")
    if args.dry_run:
        return

    cmd = ['wget',
           '-U',USER_AGENT.format(r1=random.randint(1,1000),r2=random.randint(1,1000)),
           '-c',url,'-O',zipfilename]
    print("$ {}".format(" ".join(cmd)))
    subprocess.check_call(cmd)
    check_zip(zipfilename)

if __name__=="__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Compute file changes',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("products",
                        help="Specifies what you wish to download. "
                        "Should be pl94 sf1 sf2 ur1 or any combination thereof.",
                        nargs="*")
    parser.add_argument("--year",  help="Specify year",default=2010, type=int)
    parser.add_argument("--state", help="Just download this state (specify 2-letter abbreviation).")
    parser.add_argument("--dry_run", help="Don't actually download", action='store_true')

    args = parser.parse_args()
    year = args.year
    count = 0
    for product in args.products:
        # Loop through all states
        if product.lower() == "sf1" or product.lower() == "sf2" or product.lower() == "pl94"  or product.lower() == "ur1":
            for statename_abbrev in STATE_DB.split():
                try:
                    (state_name,state) = statename_abbrev.split("/")
                except ValueError as e:
                    print("Invalid atabase entry: {}".format(statename_abbrev))
                    raise e
                print(f"{year} {product} {state}")
                if args.state and args.state.lower() != state.lower():
                    continue

                for segment_number in range(0, DOWNLOAD_SEGMENTS_PER_PRODUCT[year][product]):
                    if segment_number==0:
                        segment = 'geo'
                    else:
                        segment = '{:05d}'.format(segment_number)
                    url = DOWNLOAD_URLS[year][product].format(state_name=state_name,state=state,segment=segment)
                    zipdir = DEST_ZIPFILE_DIR[year].format(year=year, product=product, state=state)
                    download(url,zipdir)
                    count += 1
        if product.lower() == "relationship":
            for state_info in STATES_FIPS_DICT:
                try:
                    print(f'Downloading {state_info["fips_state"]}')
                    url = DOWNLOAD_URLS[year][product].format(state_fips=state_info['fips_state'])
                    download(url, os.path.join(os.path.dirname(__file__), "relationship"))
                    count += 1
                except Exception as error:
                    print(f'Error downloading {state_info["fips_state"]}', error)
    if count==0:
        print("Nothing downloaded")
        parser.print_help()
