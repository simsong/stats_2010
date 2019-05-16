#!/usr/bin/env python3
"""
diffcol.py: 
   report differences of two files column-by-column.
"""

import csv
import os
import sys


def compare(file1,file2):
    ll = 1
    with open(file1) as f1:
        with open(file2) as f2:
            while True:
                data1 = f1.readline().split(",")
                data2 = f2.readline().split(",")
                if not data1:
                    return
                print(f"== line {ll} ==")
                for i in range(len(data1)):
                    if data1[i] != data2[i]:
                        print(i,data1[i],data2[i])
                ll += 1
            

if __name__=="__main__":
    from argparse import ArgumentParser,ArgumentDefaultsHelpFormatter
    parser = ArgumentParser( formatter_class = ArgumentDefaultsHelpFormatter,
                             description="Compare two files column-by-column" )
    parser.add_argument("file1")
    parser.add_argument("file2")
    args     = parser.parse_args()
    compare(args.file1, args.file2)
    
