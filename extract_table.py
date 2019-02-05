#!/usr/bin/env python3

import sf1_decoder
import os
import sys

"""Produce P1 and P2 tables for Robert"""

import dbload
import geo_info

def extract_table(state,sumlev,table):
    # First get all of the LOGRECNOs for the state and geography
    logrecs = sf1_decoder.logrecno_for_sumlev(state,sumlev)

#PL94 file2:
# 0 - FILEID
# 1 - STUSAB
# 2 - CHARITER
# 3 - CIFSN
# 4 - LOGRECNO


if __name__=='__main__':
    conn = dbload.db_connection()
    for state in geo_info.all_state_abbrs():
        fips = int(geo_info.state_fips(state))
        # Get the block LOGRECNOS
        c = conn.cursor()
        c.execute("SELECT min(tract),max(tract) FROM blocks where STATE=?",(state.upper(),))
        (a,b) = c.fetchall()[0]
        print("Minimum tract: {}  maximum tract: {}".format(a,b))
        c.execute("SELECT logrecno,county,tract,block FROM blocks where STATE=?",(state.upper(),))
        block_geocodes = {row[0]:"{state_fips:02d}{county:03d}{tract:05d}{block:04d}".format(state_fips=fips,county=row[1],tract=row[2],block=row[3])
                          for row in c.fetchall()}
        print(f" {state} number of blocks: {len(block_geocodes)}")
        for part in [1,2]:
            count = 0
            outfile = open(f"pl94_geocoded_{state}_{part}.csv","w")
            cols = sf1_decoder.part_matrix_columns('pl94',part)
            assert cols[4]=='LOGRECNO'
            newcols = ['GEOCODE'] + cols[4:]
            print(",".join(newcols),file=outfile)
            file=outfile
            for line in sf1_decoder.pl94_file_from_zip(state,part):
                line = line.strip()
                fields = line.split(",")
                assert len(cols) == len(fields)
                try:
                    logrecno = int(fields[4])
                    geocode = block_geocodes[logrecno]
                    print(",".join([geocode] + fields[4:]), file=outfile)
                    count += 1
                except KeyError:
                    pass
            outfile.close()
            print(f"  finished part {part}. count={count}")

    

