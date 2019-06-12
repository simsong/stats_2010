#!/usr/bin/env python3
"""
diffcol.py: 
   report differences of two files column-by-column.
"""

import csv
import os
import sys


def just(fname):
    with open(fname) as f:
        r = csv.reader(f)
        count1 = len( next( r ))
        count2 = len( next( r ))
        try:
            count3 = len( next( r ))
        except StopIteration:
            count3 = 'n/a'
        print(f"{fname}  cols1: {count1}  cols2: {count2}  cols3: {count3}")

def same(a,b):
    try:
        if float(a)==float(b):
            return True
    except ValueError:
        return a==b

def compare(file1,file2,all=False,col=None):
    ll = 1
    names = []
    with open(file1) as f1:
        with open(file2) as f2:
            r1 = csv.reader(f1)
            r2 = csv.reader(f2)
            while True:
                try:
                    data1 = next(r1)
                    data2 = next(r2)
                except StopIteration:
                    break
                print(f"== line {ll} ==")
                if len(data1)!=len(data2):
                    print(f"cols1:{len(data1)}  cols2:{len(data2)}")
                diff = 0
                for i in range(len(data1)):
                    if ll==1:
                        names.append(data1[i])
                    if same(data1[i],data2[i]):
                        ch = ''
                    else:
                        ch = '*'
                        diff += 1
                    if ch or (i==col) or (all):
                        print("{} {} '{}' '{}' {}".format(i,names[i],data1[i],data2[i],ch))
                if diff>0:
                    print(f"Line {ll} Total Columns different: {diff}")
                ll += 1
    print(f"Total lines checked: {ll}")
            

if __name__=="__main__":
    from argparse import ArgumentParser,ArgumentDefaultsHelpFormatter
    parser = ArgumentParser( formatter_class = ArgumentDefaultsHelpFormatter,
                             description="Compare two files column-by-column" )
    parser.add_argument("files",nargs="+")
    parser.add_argument("--all","--a",action='store_true',help="show all fields")
    parser.add_argument("--col","--c",type=int,help="always show this field as well")
    parser.add_argument("--just",action="store_true",help="just report the number of cols for the first 2 lines")

    args     = parser.parse_args()
    if args.just:
        for f in args.files:
            just(f)
        exit(0)
                        
    compare(args.files[0], args.files[1], all=args.all, col=args.col)
    
