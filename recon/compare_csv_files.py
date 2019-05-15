#!/usr/bin/env python3

import sys

def equal(v1,v2):
    try:
        return float(v1)==float(v2)
    except ValueError:
        return v1.strip() == v2.strip()

def compare_csv_files(fname1,fname2):
    f1 = open(fname1,"r")
    f2 = open(fname2,"r")
    linenumber = 0
    fieldnames = []
    errors = 0
    while True:
        linenumber += 1
        line1 = f1.readline()
        line2 = f2.readline()
        if linenumber==1:
            fieldnames = line1.split(",")
        if not line1:
            break
        fields1 = line1.split(",")
        fields2 = line2.split(",")
        if len(fields1)!=len(fields2):
            print(f"line {linenumber}: file1 fields {len(fields1)}  file2 fields: {line(fields2)}")
            errors += 1
            continue
        for i in range(len(fields1)):
            if not equal(fields1[i],fields2[i]):
                print(f"line {linenumber} field {fieldnames[i]}/{i}:  file1:{fields1[i]} file2:{fields2[i]}")
                errors += 1
    if errors:
        print(f"Total errors: {errors}")
    return errors

if __name__=="__main__":
    compare_csv_files(sys.argv[1],sys.argv[2])
