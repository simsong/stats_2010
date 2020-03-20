#!/usr/bin/env python3
#
# geotree report tools
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

# https://htmlcolorcodes.com/

BOLD        = Font(bold=True)
CENTERED    = Alignment(horizontal='center')
YELLOW_FILL = PatternFill(fill_type='solid', start_color=colors.YELLOW, end_color=colors.YELLOW)
PINK_FILL   = PatternFill(fill_type='solid', start_color='ffb6c1', end_color='ffb6c1')
LIGHT_GREEN_FILL  = PatternFill(fill_type='solid', start_color='EAFAF1', end_color='EAF8F1')

#PR_FILL = PatternFill(fill_type='solid', start_color='F4D03F', end_color='F4D03F')       # yellow
PR_FILL     = PatternFill(fill_type='solid', start_color='F4D03F')       # yellow
STATE1_FILL = PatternFill(fill_type='solid', start_color='F2F4F4')   # silver
STATE2_FILL = PatternFill(fill_type='solid', start_color='A9CCE3') # blue

def darker(openpyxl_fill):
    rgb = openpyxl_fill.start_color.rgb
    (r,g,b) = [int(s,16) for s in [rgb[0:2],rgb[2:4],rgb[4:6]]]
    r = max(r-1,0)
    g = max(g-1,0)
    b = max(b-1,0)
    color = f"{r:02X}{g:02X}{b:02X}"
    return PatternFill(fill_type='solid', start_color=color)
               
class RingBuffer:
    from collections import deque
    def __init__(self, data):
        self.data = deque(data)

    def append(self, x):
        self.data.append(x)

    def rotate(self):
        self.data.append( self.data.popleft())

    def next(self):
        value = self.data.popleft()
        self.data.append(value)
        return value

class EasyWorkbook(Workbook):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    def clean(self):
        """Remove default 'Sheet' if exists"""
        if 'Sheet' in self:
            del self['Sheet']
        
    def format_rows(self,ws,*,min_row,max_row,column=None,skip_blank=True,min_col,max_col,fills=None,value_fills=None,stripe=False):
        """Apply colors to each row when column changes. If column is not specified, change every row."""
        if fills:
            fills = RingBuffer(fills)
            fill  = fills.next()
        prev_value = None
        make_darker = False
        for cellrow in ws.iter_rows(min_row=min_row, max_row=max_row, min_col=min_col, max_col=max_col):
            column_value = cellrow[column-min_col if column is not None else 0].value
            if skip_blank and column_value=='': 
                continue

            make_darker  = not make_darker

            if not column_value:
                fill = None
            elif value_fills is not None and column_value in value_fills:
                fill = value_fills[column_value]
            elif column_value == prev_value:
                continue        #  don't change
            else:
                fill = fills.next()
                prev_value = column_value
                make_darker = False

            #if make_darker and stripe:
            #    fill = darker(fill)

            for cell in cellrow:
                if fill:
                    cell.fill = fill

    def set_cell(ws,*,row,column,**kwargs):
        cell = ws.cell(row=row, column=column)
        for (key,value) in kwargs.items():
            setattr(cell, key, value)

# 
def wb_setup_overview(ws):
    """Set up the root of the spreadsheet, adding notes and other information"""
    ws.column_dimensions['A'].width=20
    ws.column_dimensions['C'].width=20
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

WIDTH_9_DIGITS_COMMAS=12
def ws_setup_level(ws,sheet_title):
    ws.cell(row=2, column=1).value = 'STUSAB' # A2
    ws.cell(row=2, column=2).value = 'Prefix' # B2
    ws.cell(row=2, column=3).value = 'Name'   # C2
    ws.column_dimensions['C'].width=20
    for ch in 'DEFGHIJKLMNOPQ':
        ws.column_dimensions[ch].width=WIDTH_9_DIGITS_COMMAS

    ws.cell(row=1,column=4).value = sheet_title
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

def ws_add_notes(ws,*,row,column,data):
    for line in data:
        ws.cell(row=row, column=column).value = line.strip()
        row += 1
            
def ws_add_metadata(wb):
    ws = wb.create_sheet("Notes")
    ws.cell(row=1, column=1).value = "Command Line"
    ws.cell(row=1, column=2).value = " ".join([sys.executable] + sys.argv)


