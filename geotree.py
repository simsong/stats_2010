import datetime
import json
import os
import os.path
import re
import sqlite3
import sys
import time
import zipfile
import io
import logging
import numpy as np
import itertools
import statistics
import subprocess
import gc
import math
from collections import deque

__version__ = '0.2.0'

#                       P0        P1                  P2                   P3          P4         P5      P6
GEOTREE={'v1':{'names':['US',    'DC•STATE',          'COUNTY',           'TGROUP',   'TRACT',   'BGROUP','BLOCK'],
               'name':'Geography used for 2010 Demonstration Data Products' },

         'v2':{'names':['US•PR' ,'DC•STATE•ASTATE•PR','SLDU•COUNTY•PLACE','TRACT',    'BLKGRP2', 'BLOCK', None],
               'name':'Revised MCD and AIAN-aware geography v2' },

         'v3':{'names':['US•PR' ,'DC•STATE•ASTATE•PR','SLDU•COUNTY•PLACE','LEVEL3',   'BLOCK',  None, None],
               'name':'Revised MCD and AIAN-aware geography v3 with synthetic LEVEL3'},

         'v4':{'names':['US•PR' ,'DC•STATE•ASTATE•PR','SLDU•COUNTY•COUSUB','PLACE•TRACT2', 'TRACT', 'BLKGRP2', 'BLOCK', None],
               'name':'Corrected v2 Revised MCD and AIAN-aware geography' },
         }


import pl94_geofile
import pl94_dbload
import ctools.dbfile
import ctools.clogging
import ctools.timer
import constants
from constants import *

from geotree_report import *

def deciles(ary):
    return np.percentile(ary, np.arange(0,101,10), interpolation='lower')

def flatmap(func, *iterable):
    return itertools.chain.from_iterable(map(func, *iterable))

###
### Create geotree schema
###
CREATE_GEOTREE_SQL="""
CREATE TABLE %TABLE% (state INTEGER,
                      logrecno INTEGER,
                      p1 VARCHAR(16),
                      p2 VARCHAR(16),
                      p3 VARCHAR(16),
                      p4 VARCHAR(16),
                      p5 VARCHAR(16),
                      p6 VARCHAR(16));
CREATE UNIQUE INDEX %TABLE%_logrecno ON %TABLE%(state,logrecno);
CREATE UNIQUE INDEX %TABLE%_p ON %TABLE%(p1,p2,p3,p4,p5,p6);
"""

def include_aianhh(code):
    code = int(code)
    if 1 <= code <= 4999:
        return "Federally recognized American Indian Reservations and Off-Reservation Trust Lands"
    elif 5000 <= code  <=5999:
        return "Hawaiian Home Lands"
    elif 6000 <= code <= 7999:
        return "Alaska Native Village Statistical Areas"
    elif 9000 <= code <= 9499:
        if EXCLUDE_STATE_RECOGNIZED_TRIBES:
            return False
        else:
            return "State recognized American Indian Reservations"
    else:
        return False

"""
MCD (Minor Civil Divisions) are a type of COUNTY subdivision. They are the legal type.
We typically have legal types and their statistical counterpart. They exist in 1/2 the states.
We have a stastistical counterpart which is Census County Division which exist in the other states.
They are both types of county sub-divisions. They appear in the COUSUB (County Subdivision)

PLACE is the Incorporated place or census designated place (CDP). We need to do that for 
These are  municipalities  e.g., cities, towns, burroughs. 

We put them under COUNTY for the states that are not strong MCD states. 

PLACE:
For states that are strong MCD, we ignore PLACE, because the the same entity appears in the COUNTY subdivision field.
We don't use PLACE because the towns and townships are not considered places.  

If you are Massachusetts, the city of Boston, and the town of framingham, are equally municipalities under state code, 
but Framingham town is not considered a place inthe census bureau definition.

sumlev 60 - towns and some cities. 
summary level 71 - county subdivision

"""

# New england states:
NEW_ENGLAND_STUSAB      = "CT,MA,ME,NH,VT,RI".split(",")
NEW_ENGLAND_STATES      = set([STUSAB_TO_STATE[stusab] for stusab in NEW_ENGLAND_STUSAB])

# V2 Strong MCDs we do not use county for P2.
STRONG_MCD_STUSAB       = NEW_ENGLAND_STUSAB + "NJ,NY,PA,MI,WI,MN".split(",")
STRONG_MCD_STATES       = set([STUSAB_TO_STATE[stusab] for stusab in STRONG_MCD_STUSAB])
# P1 - State/State-AIAINHH
# P2 - COUSUB.  (error! Should have been  (COUNTY,COUSUB)
# P3 - PLACE
#

# V4:
# We had several problems with the V2 this approach:
HIGH_FANOUT_STATES = "NJ,NY,PA,MI,MN,WI"
# 1 - The HIGH_FANOUT_STATES (which turned out to be the STRONG_MCD_STATES that were not the NEW_ENGLAND_STATES)
# 2 - Other states without strong MCDs (e.g. CA) didn't have enough fanout
#     (CA only 59 distinct COUNTY, 456 distinct COUNTY,COUSUB)
# 
# 3 - COUSUB is not a proper partition of STATE! It really should be (COUNTY,COUSUB)

# New approach:
# New England States we go straight to (COUNTY,COUSUB)
#       STATE -> (COUNTY,COUSUB) -> TRACT -> BLOCK

# The outher strong MCDs have too much fanout.
# They need to go STATE -> COUNTY -> COUSUB -> TRACT -> BLOCK

# The states non-MCD, non-New England that don't have strong COUSBU need to go:
#      STATE->COUNTY->PLACE->TRACT->BLOCK  (alt. a)
# But these states could alternatively go: 
#      STATE->COUSUB->PLACE->TRACT->BLOCK  (alt. b)
# Because the COUSUB partition is a proper superset of the COUNTY partition.
# We decide whether to go with a or b depending on which gives us a geometric mean closer to 4th root of 11M blocks.

# State codes for V2 to use COUSUB

EXCLUDE_STATE_RECOGNIZED_TRIBES=True
DC_STATE = STUSAB_TO_STATE['DC']
PR_STATE = STUSAB_TO_STATE['PR']

def info():
    print(f"""
NEW ENGLAND STUSAB:    {sorted(NEW_ENGLAND_STUSAB)}
V2 STRONG MCD STUSAB: {sorted(V2_STRONG_MCD_STUSAB)}
V2 STRONG MCD STATES: {sorted(V2_STRONG_MCD_STATES)}
""")


SS_DC='DC'
SS_NEW_ENGLAND='New England STATE'
SS_STRONG_MCD='STRONG MCD (not NE)'
SS_COUNTY_PLACE='COUNTY->PLACE'
SS_COUNTY_COUSUB_PLACE='(COUNTY,COUSUB)->PLACE'

from memoize import Memoize

@Memoize
def state_scheme(state):
    """Given a state, return which scheme we are going to use"""
    if state == DC_STATE:
        return SS_DC

    if state in NEW_ENGLAND_STATES:
        return SS_NEW_ENGLAND

    if state in STRONG_MCD_STATES:
        return SS_STRONG_MCD
        print(f"{stusab}:   New England State. Will use P2=COUNTY,COUSUB ({dcc}); P3=TRACT ({dct}); P4=BLKGRP2; P5=BLOCK")

    if state in STRONG_MCD_STATES:
        print(f"{stusab}:   Strong MCD State (high-fanout). Will use P2=COUNTY ({dc}); P3=COUSUB ({dcc}); P4=TRACT ({dct}); P5=BLOCK")

    dc  = db.execselect("SELECT COUNT(*) FROM (SELECT DISTINCT county FROM blocks where state=?)",(state,))[0]
    dcp = db.execselect("SELECT COUNT(*) FROM (SELECT DISTINCT COUNTY,PLACE FROM blocks where state=?)",(state,))[0]
    dcc = db.execselect("SELECT COUNT(*) FROM (SELECT DISTINCT county,cousub FROM blocks where state=?)",(state,))[0]

    # too many cousubs; go with county
    if dcc > dcp:
        return SS_COUNTY_PLACE  

    # case 1: p2=county, p3=place
    # dc  = number of distinct (county)
    # dcc = number of distinct (county,cousub)
    # dp  = number of distinct (county,place)
    d1 = math.sqrt(dc**2 + (math.sqrt(dcp) - dc)**2)
    # case 2: p2=(county,cousub) p3=place
    d2 = math.sqrt(dc**2 + (math.sqrt(dcc) - dc)**2)
    if d1<d2:
        return SS_COUNTY_PLACE
    else:
        return SS_COUNTY_COUSUB_PLACE

class MinMax:
    """Remember an object associated with a min and the object associated with the max."""
    def __int__(self,func):
        self.func = func
        self.the_min  = None
        self.the_max  = None
    def add(self,obj):
        val = func(obj)

V4_PREFIXES_EXPLAINED="""
Prefixes for state names:

A - AIANHH/tribal area of a state
N - New England State (non-tribal area)
P - Puerto Rico
M - States with "strong" municipal civil divisions (MCDs) at the county level other than New England States. (non-tribal areas)
P - States that lack "strong" municipal civil divisions; the tree for these states is organized County->Place
Q - States that lack "strong" municipal civil divisions but have many places; these states are organized (COUNTY,COUSUB)->PLACE (non-tribal areas)
"""

class GeoTree:
    def __init__(self,db,scheme,name,xpr):
        self.db   = db
        self.name = name        # which table we are using
        self.scheme = scheme
        self.gt     = GEOTREE[scheme]
        self.xpr    = xpr       # do not include PR

    def geocode_v2(self,gh):
        """The revised geocode that takes into account AIANHH. Levels are:
        0 - US or PR
        1 - Non-AIANHH part-of-state or PR            | AIANHH part-of-State 
        2 - COUNTY in non-strong MCD states           | ignored in AIANHH
        3 - PLACE in 38 strong-MCD states, SLDU in DC | AIANHH in AIANHH states
        4 - TRACT or 3-digit TG or 4-digit TG         | TRACT
        5 - BLKGRP first 1 or 2 digits of block       | BLKGRP
        6 - BLOCK                                     | BLOCK
        """
        block  = f"{gh['block']:04}"
        blkgrp2 = block[0:2]         # note 2-digit block groups
        if gh['state']==DC_STATE:
            # Washington DC
            return (f"{DC_STATE:02}D",    f"____{int(gh['sldu']):05}",            f"___{gh['tract']:06}",               blkgrp2, block, None )
        elif gh['state']==PR_STATE:
            # Puerto Rico
            return (f"{PR_STATE:02}P",    f"{gh['county']:03}{gh['place']:05}",   f"___{gh['tract']:06}",               blkgrp2, block, None )
        elif include_aianhh(gh['aianhh']):
            # AIANHH portion of 38-states with AIANHH
            return (f"{gh['state']:02}A", f"{gh['aianhh']:05}{gh['county']:03}", f"___{gh['tract']:06}",                blkgrp2, block, None )
        elif gh['concit'] in (3436,4200,11390,36000,47500,48003,52004):
            # Regions with a Consolidated City
            return (f"{gh['state']:02}A", f"CIT{gh['concit']:05}",                f"{gh['county']:03}{gh['tract']:06}",  blkgrp2, block, None  )
        elif gh['state'] in V2_STRONG_MCD_STATES:
            # Non-AIAN area in 12 state with strong MCD.
            # County is included in tract to make it unique, but cousubs do not cross counties.
            return (f"{gh['state']:02}X", f"___{gh['cousub']:05}",               f"{gh['county']:03}{gh['tract']:06}", blkgrp2, block, None  )
        else:
            # Non-AIAN area in states without strong MCD (or too many MCDs)
            return (f"{gh['state']:02}X", f"{gh['county']:03}{gh['place']:05}",  f"___{gh['tract']:06}",               blkgrp2, block, None  )

    def geocode_v4(self,gh):
        """The revised geocode that takes into account AIANHH and fanout issues."""
        tract   = gh['tract']
        block   = gh['block']
        blkgrp2 = block[0:2]         # note 2-digit block groups
        ss      = state_scheme(gh['state'])
        if ss == SS_DC:
            # Washington DC
            return (gh['state']+"D",  gh['sldu'],                    tract[0:2], tract,     blkgrp2,  block )

        if gh['state']==PR_STATE:
            # Puerto Rico
            return ("P"+gh['state'], gh['county']+gh['place'],       tract[0:2], tract,    blkgrp2,  block )

        if include_aianhh(gh['aianhh']):
            # AIANHH portion of 38-states with AIANHH
            return ("A"+gh['state'], gh['aianhh']+"_"+gh['county'], tract[0:2], tract,  blkgrp2,  block, None )

        if ss == SS_NEW_ENGLAND:
            return ("N"+gh['state'], gh['county']+"_"+gh['cousub'], tract[0:2],  tract,  blkgrp2,  block, None  )

        if ss == SS_STRONG_MCD:
            return ("M"+gh['state'], gh['county'],                  tract[0:2],  tract,  blkgrp2,  block, None  )

        if ss == SS_COUNTY_PLACE:
            return ("P"+gh['state'], gh['county'],                  gh['place'], tract,  blkgrp2, block, None  )

        if ss == SS_COUNTY_COUSUB_PLACE:
            return ("Q"+gh['state'], gh['county']+"_"+gh['cousub'], gh['place'], tract, blkgrp2, block, None  )

        raise ValueError(f"Unknown ss:{ss}")

    def create(self):
        logging.info("create %s started",self.scheme)
        self.db.create_schema(CREATE_GEOTREE_SQL.replace("%TABLE%",self.name))
        if self.scheme=='v1':
            cmd = f"""INSERT INTO {self.name} 
            SELECT state AS state,
            logrecno AS logrecno,
            printf("%02d",state) as p1,
            printf("%03d",county) as p2,
            substr(printf("%05d",tract),1,2) as p3,
            printf("%06d",tract) as p4,
            substr(printf("%04d",block),1,1) as p5,
            printf("%04d",block) as p6
            FROM blocks"""
            self.db.execute(cmd)
        elif self.scheme=='v2':
            # This could be made a LOT faster. Right now we just go row-by-row
            # It takes about 5 minutes.
            c = self.db.execute("SELECT * from geo where sumlev=750")
            for (ct,gh) in enumerate(c):
                if ct % 100_000==0:
                    logging.info(f"block {ct:,}")
                p = self.geocode_v2(gh)
                self.db.execute(f"INSERT INTO {self.name} (state,logrecno,p1,p2,p3,p4,p5,p6) values (?,?,?,?,?,?,?,?)",
                                (int(gh['state']),int(gh['logrecno']),p[0],p[1],p[2],p[3],p[4],p[5]))
        elif self.scheme=='v3':
            # V2 is the v2 geography for p1 and P2, but an adaptive algorithm for P3 and P4. There is no P5.
            # 
            v2tablename = "table2"
            c = self.db.execute(f"SELECT state,p1,p2,count(*) as count from {v2tablename} group by state,p1,p2")

            for row in c:
                state   = row['state']
                fanout1 = int(math.sqrt(row['count']))
                p1 = row['p1']
                p2 = row['p2']
                p3 = p4 = 1
                d = self.db.execute(f"SELECT logrecno from {v2tablename} where state=? and p1=? and p2=?",
                                    (row['state'],p1,p2))
                for row2 in d:
                    self.db.execute(f"INSERT into {self.name} (state,logrecno,p1,p2,p3,p4) values (?,?,?,?,?,?)",
                                    (state,row2['logrecno'],p1,p2,format(p3,"04"),format(p4,"04")))
                    p4 += 1
                    if p4 >= fanout1:
                        p3 += 1
                        p4 = 1
                logging.info("Completed %s %s %s",state,p1,p2)
        elif self.scheme=='v4':
            c = self.db.execute("SELECT * from geo where sumlev=750")
            for (ct,gh) in enumerate(c):
                if ct % 100_000==0:
                    logging.info(f"block {ct:,}")
                p = self.geocode_v4(gh)
                self.db.execute(f"INSERT INTO {self.name} (state,logrecno,p1,p2,p3,p4,p5,p6) values (?,?,?,?,?,?,?,?)",
                                (int(gh['state']),int(gh['logrecno']),p[0],p[1],p[2],p[3],p[4],p[5]))
        else:
            raise RuntimeError(f"Unknown scheme: {self.scheme}")
        self.db.commit()
        logging.info("create %s finished",self.scheme)

    def dump(self):
        cmd = f"""select a.state,a.logrecno,a.p1,a.p2,a.p3,a.p4,a.p5,a.p6,b.geocode,b.pop 
        from {self.name} a left join blocks b on a.state=b.state and a.logrecno=b.logrecno"""
        c = self.db.execute(cmd)
        for row in c:
            print(",".join([str(x) for x in row]))

    def get_geounits(self,ct):
        """ 
        When ct=0, nation page is constructed, single nation row goes to subpops.
        When ct=1, state page is being constructed, state rows need to be counties"""
        reporting_prefix = "||' '||".join(["''"] + [f"p{n}" for n in range(1,ct+1)])
        plevel1 = ",".join([f"p{n}" for n in range(1,ct+1)])  # if ct=0, this is P1
        plevel2 = ",".join([f"p{n}" for n in range(1,ct+2)])  # if ct=0, this is P1,P2
        plevel3 = ",".join([f"p{n}" for n in range(1,ct+3)])  # if ct=0, this is P1,P2,P3
        plevel4 = ",".join([f"p{n}" for n in range(1,ct+4)])  # if ct=0, this is P1,P2,P3,P4
        logging.info(f"ct:{ct} plevel1:{plevel1}")

        if self.xpr:
            where = f'WHERE a.state!={PR_STATE} and b.state!={PR_STATE}'
        else:
            where = ''
        cmd = f"""SELECT a.state,{reporting_prefix} as reporting_prefix,{plevel2},COUNT(*) as count,SUM(pop) as population FROM 
        {self.name} a LEFT JOIN blocks b ON a.state=b.state AND a.logrecno=b.logrecno {where} GROUP BY {plevel2}"""
        c = self.db.execute(cmd)
        t0 = time.time()
        res = c.fetchall()
        t1 = time.time()
        logging.info(f"Query Time: {t1-t0}")
        return res

    def end_state(self,ws,start_row,end_row):
        if start_row + 1 > end_row:
            return
        for cellrow in ws.iter_rows(min_row=start_row, max_row=start_row, min_col=1, max_col=17):
            for cell in cellrow:
                cell.border = top_thick_border
        #  don't do grouping; it is confusing
        #ws.row_dimensions.group(start_row,end_row-1,hidden=True)

    def report(self):
        """Generate a geotree report into a spreadsheet. 
        Sheet overview      - report of all summary levels
        Sheet FANLEV    - report of fanout to that level.
        When ct=0, we are doing NATION on the overview and STATES on the tab.
        """

        vintage   = time.strftime("%Y-%m-%d %H%M%S")
        fnamebase = f"reports/{args.scheme}{args.stusab} report-{vintage}"
        wb = EasyWorkbook()
        ws_overview = wb.create_sheet("Overview")
        wb.clean()
        overview_row = wb_setup_overview(ws_overview)
        for (ct,overview_name) in enumerate(self.gt['names'][0:-1]):
            t0 = time.time()
            fanout_name     = self.gt['names'][ct]
            next_level_name = self.gt['names'][ct+1]
            if next_level_name is None:
                break
            if self.xpr:
                fanout_name     = fanout_name.replace("•PR","")
                next_level_name = next_level_name.replace("•PR","")

            assert len(fanout_name) < 31
            ws_level = wb.create_sheet(fanout_name.replace("/"," "))
            sheet_title = f"{self.gt['name']}: fanout from {self.gt['names'][ct]} to {self.gt['names'][ct+1]}"
            ws_setup_level(ws_level,sheet_title)
            geounits = self.get_geounits(ct)
            logging.info(f"ct: {ct} len(geounits)={len(geounits)} t={time.time()-t0}")

            # Turn the geounits into a queue for rapid access
            geounits = deque(geounits)
            # Now find all of the fanout groups
            level_stats = []
            row         = 3
            state       = None
            print_count = 0

            # Crunch through the returned geounits, dividing between each state, and summarizing on each row.
            all_fanout_populations = []
            while geounits:
                res = {}
                fanout_populations = []
                reporting_prefix = geounits[0]['reporting_prefix']
                while geounits and (reporting_prefix == geounits[0]['reporting_prefix']):
                    d0 = geounits.popleft()
                    if print_count < 10:
                        logging.info(dict(d0))
                        print_count += 1
                    fanout_populations.append(d0['population'])
                    all_fanout_populations.append(d0['population'])

                if state!=d0['state']:
                    # New state!
                    state           = d0['state']
                    # If page is below P1, add a space between each state
                    if ct>1:    
                        row += 1

                res['fanout_populations'] = fanout_populations
                res['fanout_count']       = len(fanout_populations)
                level_stats.append(res)

                # Populate the per-level information with the last d0 data and info for this res
                if ct==0:
                    column1_label = 'US'
                else:
                    column1_label = constants.STATE_TO_STUSAB[d0['state']]
                    if d0['reporting_prefix'][3:4]=='A':
                        column1_label += '-AIANHH'
                ws_level.cell(row=row,column=1).value = column1_label
                ws_level.cell(row=row,column=2).value = d0['reporting_prefix']
                if args.names:
                    ws_level.cell(row=row,column=3).value = gs.county_name(state, county)
                ws_level.cell( row=row,column=4).value = len(fanout_populations)
                ws_level.cell( row=row,column=5).value = sum(fanout_populations)
                ws_level.cell( row=row,column=6).value = int(statistics.mean(fanout_populations))
                for cellrow in ws_level.iter_rows(min_row=row, max_row=row,min_col=3,max_col=6):
                    for cell in cellrow:
                        cell.border = right_border
                ws_level.cell( row=row,column=6).border = right_thick_border

                # add commas to pop_tot and pop_avg
                for cellrow in ws_level.iter_rows(min_row=row, max_row=row,min_col=5,max_col=6):
                    for cell in cellrow:
                        cell.number_format = '#,##0'
                # layout and format deciles
                for cellrow in ws_level.iter_rows(min_row=row, max_row=row,min_col=7,max_col=17):
                    for(cell,value) in zip(cellrow, deciles(fanout_populations)):
                        cell.value = value
                        cell.number_format = '#,##0'
                ws_level.cell( row=row,column=17).border = right_thick_border
                row += 1

                if row % 10_000==0:
                    logging.info(f"written [{fanout_name}] {row:,}")

            logging.info("total rows=%s t=%s",row,time.time()-t0)
            # Finalize the Sheet
            ws_level.freeze_panes    = 'A3'
            ws_level.auto_filter.ref = f'A2:Q{row-1}'
            wb.format_rows(ws_level, min_row=3, max_row=row-1, min_col=1, max_col=17, column=1,
                           stripe = (ct>1),
                           fills=[STATE1_FILL, STATE2_FILL], value_fills = {'PR':PR_FILL})

            # Now fill out the Overview Sheet
            ws_overview.cell(row=overview_row, column=1).value = fanout_name
            ws_overview.cell(row=overview_row, column=2).value = len(level_stats)
            ws_overview.cell(row=overview_row, column=3).value = next_level_name
            ws_overview.cell(row=overview_row, column=4).value = sum([res['fanout_count'] for res in level_stats])
            logging.info("fanout_name=%s next_level_name=%s",fanout_name,next_level_name)

            fanouts = [res['fanout_count'] for res in level_stats]
            fanout_deciles = deciles(fanouts)
            for cellrow in ws_overview.iter_rows(min_row = overview_row, max_row=overview_row, min_col=5, max_col = 15):
                for (cell,value) in zip(cellrow,fanout_deciles):
                    cell.value = value
                    cell.fill = YELLOW_FILL
                    cell.border = thin_border

            fanout_population_deciles = deciles(all_fanout_populations)
            for cellrow in ws_overview.iter_rows(min_row = overview_row, max_row=overview_row, min_col=16, max_col = 26):
                for (cell,value) in zip(cellrow,fanout_population_deciles):
                    cell.value = value
                    cell.number_format = "#,##0"
                    cell.fill = PINK_FILL
                    cell.border = thin_border
            overview_row += 1
            # Save this level

            fname = f"{fnamebase} {ct}.xlsx"
            logging.info("Saving %s",fname)
            with ctools.timer.Timer(notifier=logging.info):
                wb.save(fname)
            if ct+1==args.levels:
                break
        ws_add_notes(ws_overview,          row=overview_row+2, column=2, data=open("geotree_notes.md"))
        ws_add_notes(wb[wb.sheetnames[2]], row=4,              column=2, data=io.StringIO(V4_PREFIXES_EXPLAINED))
        ws_add_metadata(wb)
        fname = f"{fnamebase}.xlsx"
        logging.info("Saving %s",fname)
        with ctools.timer.Timer(notifier=logging.info):
            wb.save(fname)
        subprocess.call(['open',fname])

MAGIC=225
def mean_report(db):
    """This doesn't have very clever SQL"""
    for state in STATE_STATES:
        ss = state_scheme(state)
        stusab   = STATE_TO_STUSAB[state]
        print()
        ds = db.execselect("SELECT COUNT(*) FROM (SELECT DISTINCT sldu FROM blocks where state=?)",(state,))[0]
        dc = db.execselect("SELECT COUNT(*) FROM (SELECT DISTINCT county FROM blocks where state=?)",(state,))[0]
        dcc = db.execselect("SELECT COUNT(*) FROM (SELECT DISTINCT county,cousub FROM blocks where state=?)",(state,))[0]
        dcp = db.execselect("SELECT COUNT(*) FROM (SELECT DISTINCT county,place FROM blocks where state=?)",(state,))[0]
        dct = db.execselect("SELECT COUNT(*) FROM (SELECT DISTINCT county,tract FROM blocks where state=?)",(state,))[0]
        if ss == SS_DC:
            print(f"{stusab}:   Washington DC. Will use P2=SLDU ({ds}); P3=TRACT ({dct}); P4=BLKGRP2; P5=BLOCK")            
        elif ss == SS_NEW_ENGLAND:
            print(f"{stusab}:   New England State. Will use P2=COUNTY,COUSUB ({dcc}); P3=TRACT ({dct}); P4=BLKGRP2; P5=BLOCK")
        elif ss == SS_STRONG_MCD:
            print(f"{stusab}:   Strong MCD State (high-fanout). Will use P2=COUNTY ({dc}); P3=COUSUB ({dcc}) P4=TRACT ({dct}); P5=BLOCK")
        elif ss == SS_COUNTY_PLACE:
            print(f"{stusab}: Not strong MCD with P2=COUNTY ({dc}) P3=PLACE ({dcp}) P4=TRACT ({dct}) P5=BLOCK  --avoided COUNTY,COUSUB ({dcc})")
        elif ss == SS_COUNTY_COUSUB_PLACE:
            print(f"{stusab}: Not strong MCD with P2=COUNTY,COUSUB ({dcc})  P3=PLACE({dcp}) P4=TRACT ({dct}) P5=BLOCK --avoided COUNTY ({dc})")
    exit(0)
        


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Ingest the PL94 block-level population counts',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--db", help="Specify database location", default=pl94_dbload.DBFILE)
    parser.add_argument("--create", action='store_true', help='create the schema')
    parser.add_argument("--drop", action='store_true', help='drop the schema')
    parser.add_argument("--dumpblocks",   action='store_true', help='print the blocksblocks')
    parser.add_argument("--info",    help="print info", action='store_true')
    parser.add_argument("--scheme" , help='specify partitioning scheme')
    parser.add_argument("--report", action='store_true', help="Create a report")
    parser.add_argument("--names", action='store_true', help='display names')
    parser.add_argument("--levels", type=int, help="how many levels")
    parser.add_argument("--xpr",     action='store_true', help='remove PR from reports')
    parser.add_argument("--state",  help='Only process state STATE (specified by name or number)')
    parser.add_argument("--mean_report", help="Print geometric mean report", action='store_true')
    ctools.clogging.add_argument(parser)
    args = parser.parse_args()

    ctools.clogging.setup(level=args.loglevel)
    gc.enable()
    db   = ctools.dbfile.DBSqlite3(args.db,dicts=True,debug=False)
    db.set_cache_bytes(4*1024*1024*1024)

    if args.state:
        try:
            args.state  = int(args.state)
            args.stusab = STATE_TO_STUSAB[args.state]
        except ValueError:
            args.stusab = args.state.upper()
            args.state = STUSAB_TO_STATE[args.stusab]
    else:
        args.stusab = ""

    if args.mean_report:
        mean_report(db)

    if args.info:
        info()
        exit(0)

    if not args.scheme:
        parser.print_help()
        exit(1)

    name = 'table' + args.scheme[1:].replace(".","")
    if args.stusab:
        name += "_" + args.stusab

    gt = GeoTree(db,args.scheme,name,args.xpr)

    # open database and give me a big cache
    if args.drop:
        db.execute(f"DROP TABLE IF EXISTS {name}",debug=True)
        db.execute(f"DROP INDEX IF EXISTS {name}_logrecno",debug=True)
        db.execute(f"DROP INDEX IF EXISTS {name}_p",debug=True)

    if args.create:
        gt.create()
                         
    if args.dumpblocks:
        gt.dumpblocks()

    if args.report:
        gt.report()
