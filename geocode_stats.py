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

import sqlite3
import pl94_dbload
import statistics
import numpy as np
import constants

from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Alignment
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
        c.execute(f"PRAGMA cache_size = {-1024*1024}") # 1GiB cache
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
        c = self.cursor()
        try:
            c.execute(query)
        except sqlite3.OperationalError as e:
            print(query,file=sys.stderr)
            print(e)
            exit(1)
        res = c.fetchone()
        if res is None:
            if gc[6:11]=='99999' or gc[6:11]=='00000':
                return "(none)"
            print(f"Query for {gc} returned no values: {query}",file=sys.stderr)
            return ""
        res = res[0]
        if append:
            res += " " + append
        if len(gc) > 11:
            res += "TRACT " + gc[11:17]
        if len(gc) > 17:
            res += "BLKGRP " + gc[17:18]
        if len(gc) > 18:
            res += "BLOCK " + gc[18:]
        return res

    def fanout_name(self,child_prefix_span):
        if self.args.geocode2:
            ary = [ ('state',2), ('county',3), ('cousub',5), ('tract',4), ('block',4)]
        elif self.args.geocode3:
            ary = [ ('AIAN state',3), ('county',3), ('place',5), ('tract',6), ('blkgrp',1), ('block',4)]
        else:
            ary = [ ('state',2), ('county',3), ('tract',4), ('block',4)]
            
        msg = 'Fanout to '
        while child_prefix_span > 0:
            s = min(child_prefix_span,ary[0][1])
            msg += f"[{ary[0][0]}:{s}]"
            child_prefix_span -= s
            ary.pop(0)
        return msg

    def add_span_report(self,wb,report_len,child_len):
        """Create a report for a given report_len and child_len. A span=2 is by state, a span=5 is state and county."""
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
        total_tracts = 0
        row = 3
        data = gs.group_blocks_by_prefix(report_len,child_len)
        total_population = 0

        details = []

        while data:
            reporting_prefix = data[0]['prefix'][0:report_len]
            details.append((reporting_prefix,""))
            state = data[0]['state']
            county = data[0]['county']
            populations = []
            # Get all of the populations for this prefix
            while data and (reporting_prefix == data[0]['prefix'][0:report_len]):
                d = data.pop(0)
                details.append((d['prefix'],d['population']))
                group_population = d['population']
                total_population += group_population
                if not isinstance(group_population,int):
                    raise RuntimeError(str(dict(data[0])))
                populations.append( group_population )
            ws[f'A{row}'] = constants.STATE_TO_STUSAB[state]
            ws[f'B{row}'] = reporting_prefix
            if self.args.geocode3:
                ws[f'C{row}'] = gs.geocode3_name(reporting_prefix)
            else:
                ws[f'C{row}'] = gs.county_name(state, county)
            ws.cell(column=4, row=row).value = len(populations)
            ws.cell(column=4, row=row).border = right_border

            ws.cell(column=5, row=row).value = sum(populations)
            ws.cell(column=6, row=row).value = int(statistics.mean(populations))
            ws.cell(column=6, row=row).border = right_border
            d = deciles(populations)
            for n in range(11):
                ws.cell(column=7+n,row=row).value = d[n]
            ws.cell(column=7+10,row=row).border = right_border
            details.append(("",""))
            if self.args.debug:
                print("=============")
                print(f"reporting_prefix: {reporting_prefix}")
                print("populations:",populations[1:10],"...")
                print("deciles:",d)
            row += 1
        ws.freeze_panes = 'A3'
        ws.auto_filter.ref = f'A2:Q{row-1}'
        row += 1
        ws.cell(column=3, row=row).value = "Total population:"
        ws.cell(column=5, row=row).value = total_population
        row += 2
        ws.cell(column=3, row=row).value = "Details:"
        row += 1
        for (a,b) in details:
            ws.cell(column=3, row=row).value=a
            ws.cell(column=4, row=row).value=b
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
    parser.add_argument("--report", help="Generate a report for one or more prefix:child_len,prefix:child_len sets.")
    parser.add_argument("--debug", action='store_true')
    args = parser.parse_args()
    gs = GeocodeStats(args)

    if args.report:
        wb = Workbook()
        for (ct,report_desc) in enumerate(args.report.split(",")):
            (prefix_len,child_len) = [int(x) for x in report_desc.split(":")]
            gs.add_span_report(wb,prefix_len,child_len)
            fname = f"report-{ct:02}.xlsx"
            print("Saving",fname)
            wb.save(fname)
            
        
