#!/usr/bin/env python3
#
"""
Test program to use Z3 to synthesize all possible HHTYPES given our constraints.
"""

# https://stackoverflow.com/questions/13395391/z3-finding-all-satisfying-models

"""
Using the python API, find a dozen Pythagorean triples.
"""

import z3

hhtype = DeclareSort('hhtype')

a = z3.Int('a')
b = z3.Int('b')
c = z3.Int('c')
s = z3.Solver()
s.add( a*a + b*b == c*c)
s.add( a>0)
s.add( b>0)
s.add( c>0)

for i in range(25):
    if s.check() == z3.sat:
        print(s.model())
        # add this model as an impossibility
        print("a=",s.model()[a])
        print("b=",s.model()[b])
        s.add(z3.Not(  z3.And(a == s.model()[a], b == s.model()[b]) ) )
    else:
        print("No more solutions")
        break
