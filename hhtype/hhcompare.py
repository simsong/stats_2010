#!/usr/bin/env python3
"""
Compare hhtype.md with hh_syntheiszed.txt
"""

import re
brackets_re = re.compile(r"(\{.*\})")
hh_re = re.compile(r"\* (\d+) = (Size.*)")

import json


if __name__=="__main__":
    # First read and remember hh_syntheiszed.txt
    hh_synth = []
    for line in open("hh_synthesized.txt"):
        m = brackets_re.search(line)
        if m:
            x = m.group(1).replace("'", '"')
            if ':' in x:
                hh_synth.append(json.loads(x))
    print(f"Read {len(hh_synth)} definitions")

    xfer = {'Size 1, ': {'SIZE':1},
            'Size 2, ': {'SIZE':2},
            'Size 3, ': {'SIZE':3},
            'Size 4, ': {'SIZE':4},
            'Size 5, ': {'SIZE':5},
            'Size 6, ': {'SIZE':6},
            'Size 7+, ': {'SIZE':7},
            'no multig, ': {'MULTIG':0},
            'multig, ': {'MULTIG':1},
            'married opposite-sex ': {'MARRIED_OPPOSITE_SEX':1,
                                      'MARRIED_SAME_SEX':0},
            'married same-sex ': {'MARRIED_SAME_SEX':1,
                                  'MARRIED_OPPOSITE_SEX':0}
    }

    # Now read each of Williams' definitions and see what we can do with them
    for line in open("hhtype.md","r"):
        m = hh_re.search(line)
        if m:
            prop = {}
            s = m.group(2)
            for (p,attr) in xfer.items():
                if p in s:
                    prop = {**prop, **attr}
                    s=s.replace(p,"")
            print("s=",s,"prop=",prop)
                
            
