#!/usr/bin/env python3
"""
Goals of this program:

- We are interested in building a tree of geounits. For each geounit, we want to measure fanout. 

- We want to be able to experiment with different partitioning functions, and to explore partitioning functions that are based on the data

- We want to consider all geographies, inhabited 2010 geographies, and 2010 geographies with housing units or GQ facilities.


https://openpyxl.readthedocs.io/en/stable/filters.html - add filters
"""

import os
import sys
import time

import sqlite3
import pl94_dbload
import statistics
import numpy as np
import constants
import ctools.clogging
import logging

from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Alignment, PatternFill, Border, Side, Protection, Font
from openpyxl.styles.borders import Border, Side, BORDER_THIN
from openpyxl.comments import Comment
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

def deciles(ary):
    return np.percentile(ary, np.arange(0,101,10), interpolation='linear')

class GeocodeStats:
    def __init__(self,args):
        self.args = args
        self.conn = sqlite3.connect(args.db)
        self.conn.row_factory = sqlite3.Row # give me dicts
        if self.args.geocode2:
            self.geocode = 'geocode2'
        elif self.args.geocode3:
            self.geocode = 'geocode3'
        else:
            self.geocode = 'geocode'

        c = self.cursor()
        c.execute(f"PRAGMA cache_size = {-1024*1024*16}")  # 1GiB cache
        c.execute("SELECT state,county,name FROM geo where sumlev=50") 
        self.counties = {(row['state'],row['county']):row['name'] for row in c.fetchall()}

    def cursor(self):
        return self.conn.cursor()

    def county_name(self,state,county):
        return self.counties[(state,county)]

    def group_blocks_by_prefix(self,report_len,child_len):
        """Group all of the blocks by a given prefix and return aggregate statistics. 
        They then get re-arregated at a higher level by the caller"""
        grouper  = f"SUBSTR({self.geocode},1,{report_len+child_len}) "
        c = self.cursor()
        cmd = f"""SELECT {grouper} AS prefix, state, county, aiannh,
                  SUM(1) AS block_count,
                  SUM( CASE WHEN pop>0 THEN 1 ELSE 0 END) as populated_block_count,
                  SUM(pop) AS population
                  FROM blocks """
        cmd += f"""GROUP BY {grouper} ORDER BY 1 """
        if self.args.debug:
            print(cmd)
        c.execute(cmd)
        return c.fetchall()

    def geocode3_name(self,gc):
        """Decode the GEOCODE3 name"""
        append = ""
        if len(gc)>=11:
            # PLACE
            if gc[0:6]=='11XXXX':
                query=f"SELECT name FROM GEO WHERE state=11        AND '{gc[8:11]}'=sldu AND sumlev=610" # DC wards
            elif gc[2]=='X' and gc[3].isdigit():
                # not strong MCD states
                query=f"SELECT name FROM GEO WHERE {gc[0:2]}=state AND {gc[6:11]}=place AND sumlev=160"
            elif gc[2]=='X':
                # Strong MCD states
                query=f"SELECT name FROM GEO WHERE {gc[0:2]}=state AND {gc[6:11]}=cousub AND sumlev=521"
            else:
                # AIANNH
                query=f"SELECT name FROM GEO WHERE {gc[0:2]}=state AND {gc[6:11]}=aiannh AND sumlev=280"
        elif len(gc)>=6:       
            # COUNTY
            if gc[0:6]=='11XXXX':
                query=f"SELECT 'Washington DC'"
            elif gc[2]=='X' and gc[3].isdigit():
                # not strong MCD states
                query=f"SELECT NAME from geo WHERE state={gc[0:2]} AND county={gc[3:6]}"
            else:
                query=f"SELECT 'COUNTY IGNORED'"
        elif len(gc)>=3:       
            # STATE
            query=f"SELECT name FROM GEO WHERE state={gc[0:2]} AND sumlev=40"
            if gc[2]=='A':
                append=" (AIAN AREAS)"
        else:
            query="SELECT 'USA'"
        query += " LIMIT 1"
        c = self.cursor()
        try:
            c.execute(query)
        except sqlite3.OperationalError as e:
            print(query,file=sys.stderr)
            print(e)
            assert(0)
        res = c.fetchone()
        if res is None:
            if gc[6:11]=='99999' or gc[6:11]=='00000':
                return "(none)"
            print(f"Query for {gc} returned no values: {query}",file=sys.stderr)
            return ""
        res = res[0]
        if append:
            res += " " + append
        if len(gc) > 14:
            res += "TRACT " + gc[14:20]
        if len(gc) > 20:
            res += "BLKGRP " + gc[20:22]
        if len(gc) > 22:
            res += "BLOCK " + gc[22:26]
        return res

    def fanout_name(self,child_prefix_span):
        if self.args.geocode2:
            ary = [ ('state',2), ('county',3), ('cousub',5), ('tract',4), ('block',4)]
        elif self.args.geocode3:
            ary = [ ('AIAN state',3), ('county',3), ('place',5), ('tract',9), ('blkgrp',2), ('block',4)]
        else:
            ary = [ ('state',2), ('county',3), ('tract',4), ('block',4)]
            
        msg = 'Fanout to '
        try:
            while child_prefix_span > 0:
                s = min(child_prefix_span,ary[0][1])
                msg += f"[{ary[0][0]}:{s}]"
                child_prefix_span -= s
                ary.pop(0)
        except IndexError:
            msg + f"... {child_prefix_span}"
        return msg

    def add_geocode_report(self,wb,report_len,child_len):
        """Create a report for a given report_len and child_len. A span=2 is by state, a span=5 is state and county."""

        # First generate the data
        data         = gs.group_blocks_by_prefix(report_len,child_len)
        total_tracts = 0
        total_population = 0

        # Now find all of the fanout groups. Each fanout group will become a line in the report.
        fanout_groups = []
        while data:
            details = []
            res = {}
            res['reporting_prefix'] = data[0]['prefix'][0:report_len]
            res['state']  = state  = data[0]['state']
            res['county'] = county = data[0]['county']
            populations = []
            while data and (res['reporting_prefix'] == data[0]['prefix'][0:report_len]):
                d0 = data.pop(0)
                if args.details:
                    details.append((d0['prefix'],d0['population']))
                group_population = d0['population']
                if not isinstance(group_population,int):
                    raise RuntimeError(str(dict(data[0])))
                total_population += group_population
                populations.append( group_population )
            res['deciles'] = deciles(populations)
            res['details'] = details
            fanout_groups.append(res)

        logging.info("Data have been computed. Now laying out spreadsheet")

        child_prefix_span = report_len + child_len
        ws = wb.create_sheet(f'S {child_prefix_span}')
        if 'Sheet' in wb:
            del wb['Sheet']
        ws['A2']='STUSAB'
        ws['B2']='Prefix'
        ws['C2']='Name'
        ws.column_dimensions['C'].width=20
        for ch in 'DEFGHIJKLMNOPQ':
            ws.column_dimensions[ch].width=10

        ws.cell(column=4,row=1).value = self.fanout_name(child_prefix_span)
        ws.cell(column=4,row=1).alignment = CENTERED
        ws.merge_cells(start_row=1,end_row=1,start_column=4,end_column=7+10)
        ws.cell(column=6+9,row=1).border = right_border
        ws.cell(column=4,row=2).value='fanout'
        ws.cell(column=5,row=2).value='pop_tot'
        ws.cell(column=6,row=2).value='pop_avg'
        ws.cell(column=7,row=2).value='min pop'
        for n in range(1,10):
            ws.cell(column=7+n,row=2).value = f"{n*10}th pct."
        ws.cell(column=17,row=2).value='max pop'
        for col in range(4,7+10+1):
            ws.cell(column=col,row=2).alignment = CENTERED
        ws.cell(column=4,   row=2).border = right_border
        ws.cell(column=6,   row=2).border = right_border
        ws.cell(column=7+10,row=2).border = right_border

        # Using the grouper that we have specified for children, get the report
        row = 3
        logging.info(f"report_len: {report_len} len(data): {len(data)}")
        for res in fanout_groups:
            state  = res['state']
            county = res['county']
            reporting_prefix = res['reporting_prefix']

            ws[f'A{row}'] = constants.STATE_TO_STUSAB[state]
            ws[f'B{row}'] = res['reporting_prefix']
            if self.args.geocode3 and len(reporting_prefix)<12:
                ws[f'C{row}'] = gs.geocode3_name(reporting_prefix)
            else:
                ws[f'C{row}'] = gs.county_name(state, county)
            ws.cell(column=4, row=row).value = len(populations)
            ws.cell(column=5, row=row).value = sum(populations)
            ws.cell(column=6, row=row).value = int(statistics.mean(populations))
            for n in range(11):
                ws.cell(column=7+n,row=row).value = res['deciles'][n]
            row += 1

        logging.info("now adding borders")
        for cellrow in ws.iter_rows(min_row=2, max_row=row-1, min_col=1, max_col=17):
            cellrow[3].border = right_border
            cellrow[5].border = right_border
            cellrow[16].border = right_border

        logging.info("now freezing")
        # Increase Spreadsheet usability
        ws.freeze_panes = 'A3'
        ws.auto_filter.ref = f'A2:Q{row-1}'
        row += 1

        ws.cell(column=3, row=row).value = "Total population:"
        ws.cell(column=5, row=row).value = total_population
        row += 2

        if args.details:
            # Provide details
            logging.info("adding details")
            ws.cell(column=3, row=row).value = "Details:"
            row += 1
            for res in fanout_groups:
                cell       = ws.cell(column=3, row=row)
                cell.value = res['reporting_prefix']
                cell.font  = BOLD
                row += 1
                for (a,b) in res['details']:
                    ws.cell(column=3, row=row).value=a
                    ws.cell(column=4, row=row).value=b
                    row += 1
                row += 1


if __name__=="__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Report statistics about geocode prefixes',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--prefix", help="Report about a prefix")
    parser.add_argument("--child_prefix_span", type=int, help="Specify number of characters for child_prefix_span")
    parser.add_argument("--db", help="Specify database location", default=pl94_dbload.DBFILE)
    parser.add_argument("--limit", type=int, help="Return only this many")
    parser.add_argument("--geocode2", action='store_true', help="Use geocode2, not geocode")
    parser.add_argument("--geocode3", action='store_true', help="Use geocode3, not geocode")
    parser.add_argument("--geocode_report", help="Generate a fanout report by geocode", action='store_true')
    parser.add_argument("--geolevel_report", help="Generate a fanout report by geolevel", action='store_true')
    parser.add_argument("--prefixset", help="specify the sets of prefixes to use, in the form prefix:child_len,prefix:child_len")
    parser.add_argument("--debug", action='store_true')
    parser.add_argument("--details", action='store_true', help='Provide details for each fanout')
    ctools.clogging.add_argument(parser)
    args = parser.parse_args()
    ctools.clogging.setup(level = args.loglevel)
    gs = GeocodeStats(args)

    if args.geocode_report or args.geolevel_report:
        wb = Workbook()
        if args.geocode_report:
            vintage = "report geocode "
        if args.geolevel_report:
            vintage = "report geolevel "
        vintage += time.strftime("%Y-%m-%d %H%M%S")
        for (ct,report_desc) in enumerate(args.prefixset.split(",")):
            (prefix_len,child_len) = [int(x) for x in report_desc.split(":")]
            gs.add_geocode_report(wb,prefix_len,child_len)
            fname = f"{vintage} {ct:02}.xlsx"
            logging.info("Saving %s",fname)
            wb.save(fname)
            
        
