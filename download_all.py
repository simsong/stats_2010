import os.path
import os
import sys
import subprocess

# https://developers.whatismybrowser.com/useragents/explore/operating_system_name/mac-os-x/
USER_AGENT="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7"

states="""Alaska/ak
Arizona/az
Arkansas/ar
California/ca
Colorado/co
Connecticut/ct
Delaware/de
District_of_Columbia/dc
Alabama/al
Florida/fl
Georgia/ga
Hawaii/hi
Idaho/id
Illinois/il
Indiana/in
Iowa/ia
Kansas/ks
Kentucky/ky
Louisiana/la
Maine/me
Maryland/md
Massachusetts/ma
Michigan/mi
Minnesota/mn
Mississippi/ms
Missouri/mo
Montana/mt
Nebraska/ne
Nevada/nv
New_Hampshire/nh
New_Jersey/nj
New_Mexico/nm
New_York/ny
North_Carolina/nc
North_Dakota/nd
Ohio/oh
Oklahoma/ok
Oregon/or
Pennsylvania/pa
Rhode_Island/ri
South_Carolina/sc
South_Dakota/sd
Tennessee/tn
Texas/tx
Utah/ut
Vermont/vt
Virginia/va
Washington/wa
West_Virginia/wv
Wisconsin/wi
Wyoming/wy"""

URLS = {'pl94':'https://www2.census.gov/census_2010/redistricting_file--pl_94-171/{st}2010.pl.zip',
        'sf1':'https://www2.census.gov/census_2010/04-Summary_File_1/{st}2010.sf1.zip',
        'sf2':'https://www2.census.gov/census_2010/05-Summary_File_2/{st}2010.sf2.zip'}
BASEDIR = os.path.dirname(__file__)

if __name__=="__main__":
    products = ['pl94']
    for product in products:
        download_dir = os.path.abspath(os.path.join(BASEDIR, product))
        print(f"download_dir: {download_dir}")
        if not os.path.exists(download_dir):
            os.mkdir( download_dir )
        print(download_dir)
        for state in states.split("\n"):
            url = URLS[product].format(st=state)
            fname = os.path.basename(url)
            if os.path.exists(fname):
                print("{} exists")
                goodfile = ".good" + fname
                if os.path.exists(goodfile):
                    continue
                # Test the archive
                r = subprocess.call(['unzip','-t',fname])
                if r==0:
                    open(".good" + fname,"w").close()
                    continue
                print("{} does not check. Will continue the downloading.".format(fname))
            cmd = ['wget','-U',USER_AGENT,'-c',url,'-O',os.path.join(download_dir,fname)]
            print("$ {}".format(" ".join(cmd)))
            subprocess.check_call(cmd)
