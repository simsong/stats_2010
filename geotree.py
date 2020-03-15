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
from collections import deque

from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Alignment, PatternFill, Border, Side, Protection, Font, Fill, Color
from openpyxl.styles.borders import Border, Side, BORDER_THIN
from openpyxl.comments import Comment
import openpyxl.styles.colors as colors

thin_border = Border(
    left=Side(border_style=BORDER_THIN, color='00000000'),
    right=Side(border_style=BORDER_THIN, color='00000000'),
    top=Side(border_style=BORDER_THIN, color='00000000'),
    bottom=Side(border_style=BORDER_THIN, color='00000000')
)

right_border = Border(
    right=Side(border_style=BORDER_THIN, color='00000000')
)
BOLD     = Font(bold=True)
CENTERED = Alignment(horizontal='center')
YELLOW_FILL   = PatternFill(fill_type='solid', start_color=colors.YELLOW, end_color=colors.YELLOW)
PINK_FILL   = PatternFill(fill_type='solid', start_color='ffb6c1', end_color='ffb6c1')

import pl94_dbload
import ctools.dbfile
import ctools.clogging
import constants
from constants import *

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

GEOTREE={'v1':{'names':['STATE','COUNTY','TGROUP','TRACT','BGROUP','BLOCK']}}

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

def ws_setup_level(ws,name):
    ws.cell(row=2, column=1).value = 'STUSAB' # A2
    ws.cell(row=2, column=2).value = 'Prefix' # B2
    ws.cell(row=2, column=3).value = 'Name'   # C2
    ws.column_dimensions['C'].width=20
    for ch in 'DEFGHIJKLMNOPQ':
        ws.column_dimensions[ch].width=10

    ws.cell(row=1,column=4).value = f"fanout to {name}"
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
    ws.cell(row=2,column=6).border = right_border
    ws.cell(row=2,column=7+10).border = right_border



class GeoTree:
    def __init__(self,db,name,scheme):
        self.db   = db
        self.name = name        # which table we are using
        self.scheme = scheme
        self.gt     = GEOTREE[scheme]

    def create(self):
        if self.scheme=='v1':
            self.db.create_schema(CREATE_GEOTREE_SQL.replace("%TABLE%",self.name),debug=True)
            cmd = f"""INSERT INTO {name} 
            SELECT state AS state,
            logrecno AS logrecno,
            printf("%02d",state) as p1,
            printf("%03d",county) as p2,
            substr(printf("%05d",tract),1,2) as p3,
            printf("%05d",tract) as p4,
            substr(printf("%04d",block),1,1) as p5,
            printf("%04d",block) as p6
            FROM blocks"""
            db.execute(cmd,debug=True)
            db.commit()
        else:
            raise RuntimeError(f"Unknown scheme: {self.scheme}")

    def dump(self):
        cmd = f"""select a.state,a.logrecno,a.p1,a.p2,a.p3,a.p4,a.p5,a.p6,b.geocode,b.pop 
        from {self.name} a left join blocks b on a.state=b.state and a.logrecno=b.logrecno"""
        c = self.db.execute(cmd)
        for row in c:
            print(",".join([str(x) for x in row]))

    def get_geounits(self,ct):
        reporting_prefix = "||".join(["''"] + [f"a.p{n}" for n in range(1,ct)])
        plevels = ",".join([f"p{n}" for n in range(1,ct+1)])
        plevels2 = ",".join([f"p{n}" for n in range(1,ct+2)])

        cmd = f"""SELECT state,{reporting_prefix} as reporting_prefix,{plevels},COUNT(*),SUM(pop) as population FROM 
        (SELECT a.state AS state,{plevels},SUM(b.pop) as pop FROM {self.name} a LEFT JOIN blocks b ON a.state=b.state AND a.logrecno=b.logrecno GROUP BY {plevels2})
        GROUP BY {plevels}"""
        c = self.db.execute(cmd)
        return c.fetchall()

    def report(self):
        """Generate a geotree report into a spreadsheet. 
        Sheet overview      - report of all summary levels
        Sheet FANLEV    - report of fanout to that level.
        """
        vintage   = time.strftime("%Y-%m-%d %H%M%S")
        fnamebase = f"reports/report-{vintage}"
        wb = Workbook()
        ws_overview = wb.create_sheet("Overview")
        if 'Sheet' in wb:
            del wb['Sheet']
        overview_row = wb_setup_overview(ws_overview)
        for (ct,fanout_name) in enumerate(self.gt['names'],1):
            ws_level = wb.create_sheet(fanout_name)
            ws_setup_level(ws_level,fanout_name)
            geounits = self.get_geounits(ct)
            logging.info(f"ct: {ct} len(geounits)={len(geounits)}")

            # Turn the geounits into a queue for rapid access
            geounits = deque(geounits)
            # Now find all of the fanout groups
            level_stats = []
            while geounits:
                res = {}
                fanout_populations = []
                reporting_prefix = geounits[0]['reporting_prefix']
                while geounits and (reporting_prefix == geounits[0]['reporting_prefix']):
                    d0 = geounits.popleft()
                    print(dict(d0))
                    fanout_populations.append(d0['population'])
                res['fanout_populations'] = fanout_populations
                res['fanout_count']       = len(fanout_populations)
                level_stats.append(res)

            # Now put in the high-level
            ws.cell(row=overview_row, column=1).value = fanout_name
            ws.cell(row=overview_row, column=2).value = len(level_stats)
            ws.cell(row=overview_row, column=3).value = self.gt['names'][ct]
            ws.cell(row=overview_row, column=4).value = sum([res['sublevel_count'] for res in level_stats])

            fname = f"{fnamebase} {ct}.xlsx"
            logging.info("Saving %s",fname)
            wb.save(fname)
            print("stop")
            exit(0)


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
    parser.add_argument("name", help="Name of the schema table")
    ctools.clogging.add_argument(parser)
    args = parser.parse_args()
    ctools.clogging.setup(level=args.loglevel)

    db   = ctools.dbfile.DBSqlite3(args.db,dicts=True,debug=True)
    db.set_cache_bytes(4*1024*1024*1024)

    gt = GeoTree(db,args.name,args.scheme)

    # open database and give me a big cache
    if args.delete:
        db.execute(f"DROP TABLE IF EXISTS {args.name}",debug=True)
        db.execute(f"DROP INDEX IF EXISTS {args.name}_logrecno",debug=True)
        db.execute(f"DROP INDEX IF EXISTS {args.name}_p",debug=True)

    if args.create:
        db.create()
                         
    if args.dump:
        gt.dump()

    if args.report:
        gt.report()
