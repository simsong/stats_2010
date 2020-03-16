__version__ = '0.2.0'
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
from collections import deque

from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Alignment, PatternFill, Border, Side, Protection, Font, Fill, Color
from openpyxl.styles.borders import Border, Side, BORDER_THIN, BORDER_THICK
from openpyxl.comments import Comment
import openpyxl.styles.colors as colors


thin_border = Border(
    left=Side(border_style=BORDER_THIN, color='00000000'),
    right=Side(border_style=BORDER_THIN, color='00000000'),
    top=Side(border_style=BORDER_THIN, color='00000000'),
    bottom=Side(border_style=BORDER_THIN, color='00000000')
)

top_thick_border = Border( top=Side(border_style=BORDER_THICK, color='0000FF') )
top_border = Border( top=Side(border_style=BORDER_THIN, color='00000000') )
right_border = Border( right=Side(border_style=BORDER_THIN, color='00000000') )
right_thick_border = Border( right=Side(border_style=BORDER_THICK, color='00000000') )
bottom_border = Border( bottom=Side(border_style=BORDER_THIN, color='00000000') )
bottom_thick_border = Border( bottom=Side(border_style=BORDER_THICK, color='00007F') )

BOLD     = Font(bold=True)
CENTERED = Alignment(horizontal='center')
YELLOW_FILL   = PatternFill(fill_type='solid', start_color=colors.YELLOW, end_color=colors.YELLOW)
PINK_FILL   = PatternFill(fill_type='solid', start_color='ffb6c1', end_color='ffb6c1')

import pl94_dbload
import ctools.dbfile
import ctools.clogging
import constants
from constants import *

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

#                                 P1               P2                                       P3                                 P4         P5      P6
GEOTREE={'v1':{'names':['NATION','STATE',          'COUNTY',                                'TGROUP',                         'TRACT',   'BGROUP','BLOCK']},
         'v2':{'names':['NATION','DC•STATE•ASTATE','SLDU•AIANNH_COUNTY•COUSUB•COUNTY_PLACE', 'TRACT',                         'BLKGRP2', 'BLOCK', '']}
}

# 
def wb_setup_overview(ws):
    """Set up the root of the spreadsheet"""
    ws.cell(row=2, column=1).value = 'Level'
    ws.cell(row=2, column=2).value = '# Levels'
    ws.cell(row=2, column=3).value = 'Sublevel'
    ws.cell(row=2, column=4).value = '# Sublevels'

    ws.cell(row=1, column=5).value     = 'sublevel fanouts (interpolation=min)'
    ws.cell(row=1, column=5).alignment = CENTERED
    ws.cell(row=1, column=5).fill      = YELLOW_FILL
    ws.merge_cells(start_row=1, end_row=1, start_column=5, end_column=15)
    ws.cell(row=2, column=5).value = 'min'
    for n in range(1,10):
        ws.cell(row=2, column=5+n).value = f"{n*10}th pct."
    ws.cell(row=2, column=15).value = 'max'
    for col in range(5,16):
        ws.cell(row=2, column=col).alignment = CENTERED
        ws.cell(row=2, column=col).fill = YELLOW_FILL

    ws.cell(row=1, column=16).value     = 'sublevel populations (interpolation=min)'
    ws.cell(row=1, column=16).alignment = CENTERED
    ws.cell(row=1, column=16).fill      = PINK_FILL
    ws.merge_cells(start_row=1, end_row=1, start_column=16, end_column=26)
    ws.cell(row=2, column=16).value = 'min'
    for n in range(1,10):
        ws.cell(row=2, column=16+n).value = f"{n*10}th pct."
    ws.cell(row=2, column=26).value = 'max'
    for col in range(16,27):
        ws.cell(row=2, column=col).alignment = CENTERED
        ws.cell(row=2, column=col).fill = PINK_FILL
    return 3                    # next row

def ws_setup_level(ws,level,fanout_level):
    ws.cell(row=2, column=1).value = 'STUSAB' # A2
    ws.cell(row=2, column=2).value = 'Prefix' # B2
    ws.cell(row=2, column=3).value = 'Level'   # C2
    ws.column_dimensions['C'].width=20
    for ch in 'DEFGHIJKLMNOPQ':
        ws.column_dimensions[ch].width=10

    ws.cell(row=1,column=4).value = f"fanout to {fanout_level}"
    ws.cell(row=1,column=4).alignment = CENTERED
    ws.merge_cells(start_row=1,end_row=1,start_column=4,end_column=7+10)
    ws.cell(row=1,column=6+9).border = right_border
    ws.cell(row=2,column=4).value='fanout'
    ws.cell(row=2,column=5).value='pop_tot'
    ws.cell(row=2,column=6).value='pop_avg'
    ws.cell(row=2,column=7).value='min pop'
    for n in range(1,10):
        ws.cell(row=2,column=7+n).value = f"{n*10}th pct."
    ws.cell(row=2,column=17).value='max pop'
    for col in range(4,7+10+1):
        ws.cell(row=2,column=col).alignment = CENTERED
    ws.cell(row=2,column=4).border = right_border
    ws.cell(row=2,column=6).border = right_thick_border
    ws.cell(row=2,column=7+10).border = right_border

STRONG_MCD_STATES=[9,11,23,25,26,27,33,34,36,42,44,50,55]
DC_FIPS=11
EXCLUDE_STATE_RECOGNIZED_TRIBES=True
def include_aiannh(code):
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

def geocode3(gh):
    """The revised geocode that takes into account AIANNH. Levels are:
    0 - Nation
    1 - Non-AIANNH part-of-state                  | AIANNH part-of-State 
    2 - COUNTY in non-strong MCD states           | ignored in AIANNH
    3 - PLACE in 38 strong-MCD states, SLDU in DC | AIANNH in AIANNH states
    4 - TRACT or 3-digit TG or 4-digit TG         | TRACT
    5 - BLKGRP first 1 or 2 digits of block       | BLKGRP
    6 - BLOCK                                     | BLOCK
    """
    block  = f"{gh['block']:04}"
    blkgrp2 = block[0:2]         # note 2-digit block groups
    if gh['state']==DC_FIPS:
        # Washington DC
        return (f"{DC_FIPS:02}D",    f"____{int(gh['sldu']):05}",            f"___{gh['tract']:06}",               blkgrp2, block, None )
    elif include_aiannh(gh['AIANNH']):
        # AIANNH portion of 38-states with AIANNH
        return (f"{gh['state']:02}A", f"{gh['aiannh']:05}{gh['county']:03}", f"___{gh['tract']:06}",               blkgrp2, block, None )
    elif gh['STATE'] in STRONG_MCD_STATES:
        # Non-AIAN area in 12 state with strong MCD.
        # County is included in tract to make it unique, but cousubs do not cross counties.
        return (f"{gh['state']:02}X", f"___{gh['cousub']:05}",               f"{gh['county']:03}{gh['tract']:06}", blkgrp2, block, None  )
    else:
        # Non-AIAN area and 38 states not strong MCD
        return (f"{gh['state']:02}X", f"{gh['county']:03}{gh['place']:05}",  f"___{gh['tract']:06}",               blkgrp2, block, None  )
    return "".join(code)


class GeoTree:
    def __init__(self,db,name,scheme):
        self.db   = db
        self.name = name        # which table we are using
        self.scheme = scheme
        self.gt     = GEOTREE[scheme]

    def create(self):
        if self.scheme=='v1':
            self.db.create_schema(CREATE_GEOTREE_SQL.replace("%TABLE%",self.name),debug=True)
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
            self.db.execute(cmd,debug=True)
            self.db.commit()
        elif self.scheme=='v2':
            # This could be made a LOT faster. Right now we just go row-by-row
            self.db.create_schema(CREATE_GEOTREE_SQL.replace("%TABLE%",self.name),debug=True)
            c = self.db.execute("SELECT * from blocks")
            for block in c:
                try:
                    p = geocode3(block)
                except KeyError as e:
                    print("block:",block,file=sys.stderr)
                    print(e,file=sys.stderr)
                    exit(1)
                self.db.execute(f"INSERT INTO {self.name} (state,logrecno,p1,p2,p3,p4,p5,p6) values (?,?,?,?,?,?,?,?)",
                                (block['STATE'],block['LOGRECNO'],p[0],p[1],p[2],p[3],p[4],p[5]))
            self.db.commit()
        else:
            raise RuntimeError(f"Unknown scheme: {self.scheme}")

    def dump(self):
        cmd = f"""select a.state,a.logrecno,a.p1,a.p2,a.p3,a.p4,a.p5,a.p6,b.geocode,b.pop 
        from {self.name} a left join blocks b on a.state=b.state and a.logrecno=b.logrecno"""
        c = self.db.execute(cmd)
        for row in c:
            print(",".join([str(x) for x in row]))

    def get_geounits(self,ct):
        """ When ct=0, overview is nation, state page is being constructed, state rows need to be counties"""
        reporting_prefix = "||' '||".join(["''"] + [f"p{n}" for n in range(1,ct+2)])
        plevel1 = ",".join([f"p{n}" for n in range(1,ct+2)])   # if ct=0, this is P1
        plevel2 = ",".join([f"p{n}" for n in range(1,ct+3)])  # if ct=0, this is P1,P2
        plevel3 = ",".join([f"p{n}" for n in range(1,ct+4)])  # if ct=0, this is P1,P2,P3
        plevel4 = ",".join([f"p{n}" for n in range(1,ct+5)])  # if ct=0, this is P1,P2,P3,P4
        print(f"ct:{ct} plevel1:{plevel1}")

        old_cmd = f"""SELECT state,{reporting_prefix} as reporting_prefix,{plevel2},COUNT(*),SUM(pop) as population FROM 
        (SELECT a.state AS state,{plevel2},SUM(b.pop) as pop FROM {self.name} a LEFT JOIN blocks b ON a.state=b.state AND a.logrecno=b.logrecno GROUP BY {plevel2})
        GROUP BY {plevel2}"""

        cmd = f"""SELECT a.state,{reporting_prefix} as reporting_prefix,{plevel2},COUNT(*),SUM(pop) as population FROM 
        {self.name} a LEFT JOIN blocks b ON a.state=b.state AND a.logrecno=b.logrecno GROUP BY {plevel2}"""
        c = self.db.execute(cmd)
        t0 = time.time()
        res = c.fetchall()
        t1 = time.time()
        print(f"time: {t1-t0}",file=sys.stderr)
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
        fnamebase = f"reports/report-{vintage}"
        wb = Workbook()
        ws_overview = wb.create_sheet("Overview")
        if 'Sheet' in wb:
            del wb['Sheet']
        overview_row = wb_setup_overview(ws_overview)
        for (ct,overview_name) in enumerate(self.gt['names'][0:-1]):
            fanout_name = self.gt['names'][ct+1]
            next_level = self.gt['names'][ct+2]
            ws_level = wb.create_sheet(fanout_name.replace("/"," "))
            ws_setup_level(ws_level,fanout_name,next_level)
            geounits = self.get_geounits(ct)
            logging.info(f"ct: {ct} len(geounits)={len(geounits)}")

            # Turn the geounits into a queue for rapid access
            geounits = deque(geounits)
            # Now find all of the fanout groups
            level_stats = []
            row         = 3
            state       = None
            print_count = 0

            # Crunch through the returned geounits, dividing between each state, and summarizing on each row.
            while geounits:
                res = {}
                fanout_populations = []
                reporting_prefix = geounits[0]['reporting_prefix']
                while geounits and (reporting_prefix == geounits[0]['reporting_prefix']):
                    d0 = geounits.popleft()
                    if print_count < 10:
                        print(dict(d0))
                        print_count += 1
                    fanout_populations.append(d0['population'])

                if state!=d0['state']:
                    # New state!
                    if state is not None:
                        # End the last state
                        self.end_state(ws_level,state_start_row,row-1)
                    state           = d0['state']
                    if ct>0:
                        row += 1
                    state_start_row = row

                res['fanout_populations'] = fanout_populations
                res['fanout_count']       = len(fanout_populations)
                level_stats.append(res)

                # Populate the per-level information with the last d0 data and info for this res
                if ct==0:
                    ws_level.cell(row=row,column=1).value = constants.STATE_TO_STUSAB[d0['state']]
                else:
                    ws_level.cell(row=row,column=1).value = constants.STATE_TO_STUSAB[d0['state']]
                ws_level.cell(row=row,column=2).value = "_"+d0['reporting_prefix']
                if args.names:
                    if self.args.geocode3 and len(reporting_prefix)<12:
                        ws_level.cell(row=row,column=3).value = gs.geocode3_name(reporting_prefix)
                    else:
                        ws_level.cell(row=row,column=3).value = gs.county_name(state, county)
                ws_level.cell( row=row,column=4).value = len(fanout_populations)
                ws_level.cell( row=row,column=5).value = sum(fanout_populations)
                ws_level.cell( row=row,column=6).value = int(statistics.mean(fanout_populations))
                for cellrow in ws_level.iter_rows(min_row=row, max_row=row,min_col=3,max_col=6):
                    for cell in cellrow:
                        cell.border = right_border
                ws_level.cell( row=row,column=6).border = right_thick_border
                for cellrow in ws_level.iter_rows(min_row=row, max_row=row,min_col=7,max_col=17):
                    for(cell,value) in zip(cellrow, deciles(fanout_populations)):
                        cell.value = value
                        cell.number_format = '#,##0'
                ws_level.cell( row=row,column=17).border = right_thick_border
                row += 1
            self.end_state(ws_level, state_start_row, row-1) # and end the last state
            # Increase Spreadsheet usability
            ws_level.freeze_panes    = 'A3'
            ws_level.auto_filter.ref = f'A2:Q{row-1}'

            # Now put in the high-level
            ws_overview.cell(row=overview_row, column=1).value = self.gt['names'][ct+1]
            ws_overview.cell(row=overview_row, column=2).value = len(level_stats)
            ws_overview.cell(row=overview_row, column=3).value = self.gt['names'][ct+2]
            ws_overview.cell(row=overview_row, column=4).value = sum([res['fanout_count'] for res in level_stats])

            fanouts = [res['fanout_count'] for res in level_stats]
            fanout_deciles = deciles(fanouts)
            for cellrow in ws_overview.iter_rows(min_row = overview_row, max_row=overview_row, min_col=5, max_col = 15):
                for (cell,value) in zip(cellrow,fanout_deciles):
                    cell.value = value
                    cell.fill = YELLOW_FILL
                    cell.border = thin_border

            all_fanout_populations = [res['fanout_populations'] for res in level_stats]
            all_fanout_populations = list(flatmap( lambda a:a, all_fanout_populations))
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
            wb.save(fname)
            if ct+1==args.levels:
                break
        subprocess.call(['open',fname])


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Ingest the PL94 block-level population counts',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--db", help="Specify database location", default=pl94_dbload.DBFILE)
    parser.add_argument("--create", action='store_true', help='create the schema')
    parser.add_argument("--delete", action='store_true', help='delete the schema')
    parser.add_argument("--dump",   action='store_true', help='print the blocks')
    parser.add_argument("--scheme" , help='specify partitioning scheme')
    parser.add_argument("--report", action='store_true', help="Create a report")
    parser.add_argument("--names", action='store_true', help='display names')
    parser.add_argument("--levels", type=int, help="how many levels")
    parser.add_argument("name", help="Name of the schema table")
    ctools.clogging.add_argument(parser)
    args = parser.parse_args()
    ctools.clogging.setup(level=args.loglevel)

    db   = ctools.dbfile.DBSqlite3(args.db,dicts=True,debug=False)
    db.set_cache_bytes(4*1024*1024*1024)

    gt = GeoTree(db,args.name,args.scheme)

    # open database and give me a big cache
    if args.delete:
        db.execute(f"DROP TABLE IF EXISTS {args.name}",debug=True)
        db.execute(f"DROP INDEX IF EXISTS {args.name}_logrecno",debug=True)
        db.execute(f"DROP INDEX IF EXISTS {args.name}_p",debug=True)

    if args.create:
        gt.create()
                         
    if args.dump:
        gt.dump()

    if args.report:
        gt.report()
