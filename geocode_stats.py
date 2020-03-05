#!/usr/bin/env python3
"""
Goals of this program:

- We are interested in building a tree of geounits. For each geounit, we want to measure fanout. 

- We want to be able to experiment with different partitioning functions, and to explore partitioning functions that are based on the data

- We want to consider all geographies, inhabited 2010 geographies, and 2010 geographies with housing units or GQ facilities.
"""

import os
import sys

import sqlite3
import dbload_pl94
import statistics
import numpy as np
import constants

from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Alignment
from openpyxl.styles.borders import Border, Side, BORDER_THIN
thin_border = Border(
    left=Side(border_style=BORDER_THIN, color='00000000'),
    right=Side(border_style=BORDER_THIN, color='00000000'),
    top=Side(border_style=BORDER_THIN, color='00000000'),
    bottom=Side(border_style=BORDER_THIN, color='00000000')
)

WY_ONLY = False

right_border = Border(
    right=Side(border_style=BORDER_THIN, color='00000000')
)

CENTERED = Alignment(horizontal='center')

def deciles(ary):
    return np.percentile(ary, np.arange(0,100,10), interpolation='linear')

class GeocodeStats:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.conn.row_factory = sqlite3.Row # give me dicts

        c = self.cursor()
        c.execute(f"PRAGMA cache_size = {-1024*1024}") # 1GiB cache
        c.execute("SELECT state,county,name FROM counties") 
        self.counties = {(row['state'],row['county']):row['name'] for row in c.fetchall()}

    def cursor(self):
        return self.conn.cursor()

    def county_name(self,state,county):
        return self.counties[(state,county)]

    def prefixinfo(self,prefix,child_prefix_span):
        """For a given prefix and a span of characters for the child's prefix, 
        return a list of the children, and for each the number of blocks and number of people.
        The fanout is the size of the list.
        """
        c = self.cursor()
        pl = len(prefix)
        cmd = f"""SELECT substr(geocode,1,{pl+child_prefix_span}) AS prefix,
                  SUM(1) AS block_count,
                  SUM( CASE WHEN pop>0 THEN 1 ELSE 0 END) as pop_block_count,
                  SUM(pop) AS pop 
                  FROM blocks 
                  WHERE SUBSTR(geocode,1,{pl})=?
                  GROUP BY SUBSTR(geocode,1,{pl+child_prefix_span})"""
        print(cmd)
        c.execute(cmd,[prefix])
        return c.fetchall()

    def county_prefix_report(self,child_prefix_span,limit=None):
        """For every county, report the number of children, the blocks in each child, 
        the number of populated blocks in each child, and the population. 
        if child_prefix_span=6, then it is a tract-by-tract report.
        """
        assert isinstance(child_prefix_span,int)
        c = self.cursor()
        cmd = f"""SELECT substr(geocode,1,5+?) AS prefix,
                  state,
                  county,
                  SUM(1) AS block_count,
                  SUM( CASE WHEN pop>0 THEN 1 ELSE 0 END) as pop_block_count,
                  SUM(pop) AS pop 
                  FROM blocks"""
        if WY_ONLY:
            cmd += " WHERE state='WY' "

        cmd += """
                  GROUP BY SUBSTR(geocode,1,5+?)
                  ORDER BY 1
        """
        args = [child_prefix_span,child_prefix_span]
        if limit:
            cmd+= " LIMIT ?"
            args.append(limit)
        print(cmd,args)
        c.execute(cmd,args)
        return c.fetchall()

    def add_span_report(self,wb,span):
        ws = wb.create_sheet(f'span={span}')
        try:
            wb.remove_sheet(wb.get_sheet_by_name('Sheet'))
        except KeyError as e:
            pass

        ws['A2']='State'
        ws['B2']='County'
        ws['C2']='Name'
        ws.column_dimensions['C'].width=20
        for ch in 'DEFGHIJKLMNOPQ':
            ws.column_dimensions[ch].width=10

        ws.cell(column=4,row=1).value=f'Grouping by [state][county][{span} digits]'
        ws.cell(column=4,row=1).alignment = CENTERED
        ws.merge_cells(start_row=1,end_row=1,start_column=4,end_column=7+10)
        ws.cell(column=6+9,row=1).border = right_border
        ws.cell(column=4,row=2).value='#'
        ws.cell(column=5,row=2).value='pop_tot'
        ws.cell(column=6,row=2).value='pop_avg'
        ws.cell(column=7,row=2).value='min'
        for n in range(1,10):
            ws.cell(column=7+n,row=2).value = f"{n*10}th pct."
        ws.cell(column=7+10,row=2).value = f"max"
        for col in range(4,7+10+1):
            ws.cell(column=col,row=2).alignment = CENTERED
        ws.cell(column=4,   row=2).border = right_border
        ws.cell(column=6,   row=2).border = right_border
        ws.cell(column=7+10,row=2).border = right_border

        # First get a report of all the tracts in the US and iterate through it
        # to populate the base spreadsheet
        total_tracts = 0
        row = 3
        counties = gs.county_prefix_report(child_prefix_span=span)
        last = (None,None)

        while counties:
            (state,county) = (counties[0]['state'],counties[0]['county'])
            pops = []
            # Get all of the pops for this county...
            while counties and (state == counties[0]['state']) and (county == counties[0]['county']):
                pops.append( counties[0]['pop'] )
                counties.pop(0)
            ws[f'A{row}'] = state
            ws[f'B{row}'] = f"{constants.stusab_to_state(state):2}{county:03}_"
            ws[f'C{row}'] = gs.county_name(state, county)
            ws.cell(column=4, row=row).value = len(pops)
            ws.cell(column=4, row=row).border = right_border
            ws.cell(column=5, row=row).value = sum(pops)
            ws.cell(column=6, row=row).value = int(statistics.mean(pops))
            ws.cell(column=6, row=row).border = right_border
            d = deciles(pops)
            for n in range(10):
                ws.cell(column=7+n,row=row).value = d[n]
            ws.cell(column=7+10,row=row).value = max(pops)
            ws.cell(column=7+10,row=row).border = right_border
            row += 1
        ws.freeze_panes = 'A3'

if __name__=="__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Report statistics about geocode prefixes',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--prefix", help="Report about a prefix")
    parser.add_argument("--span", type=int, help="Specify number of characters for span")
    parser.add_argument("--db", help="Specify database location", default=dbload_pl94.DBFILE)
    parser.add_argument("--allcounties", help="Report by counties", action='store_true')
    parser.add_argument("--limit", type=int, help="Return only this many")
    parser.add_argument("--report", type=int, help="Give report from span 1 to report (max=12)")
    args = parser.parse_args()
    gs = GeocodeStats(args.db)
    if args.prefix and args.span:
        count = 0
        for row in gs.prefixinfo(args.prefix,args.span):
            count += 1
            print(dict(row))
        print("Count: ",count)
    if args.allcounties:
        for row in gs.county_prefix_report(args.span,limit=args.limit):
            print(dict(row))
        
    if args.report:
        args.report = min(args.report, 12)
        print("making report")
        wb = Workbook()
        for i in range(1,args.report+1):
            gs.add_span_report(wb,i)
            wb.save(f"report{i}.xlsx")
        
