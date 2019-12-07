#!/usr/bin/python
#
# run_sugar.py:
#
# run the sugar with the specified input file and optionally print all possible results

import os
import sys
import re
from subprocess import Popen,PIPE,call
from collections import defaultdict
import time

SUGAR_PERL = './sugar-v2-3-3/bin/sugar'
SUGAR_JAR  = './sugar-v2-3-3/bin/sugar-v2-3-3.jar'
PICOSAT_SOLVER = '/opt/local/bin/picosat'
GLUCOSE_SOLVER = './glucose_static'
DEFAULT_SOLVER = PICOSAT_SOLVER

# Our encodings
SEXMAP = {"1":"M", "0":"F"}
RACEMAP = {"1":"W", "0":"B"}
MARRIAGEMAP = {"0":"S", "1":"M"}
VARMAP = {"S":SEXMAP,
          "R":RACEMAP,
          "M":MARRIAGEMAP}
DEFAULT_ALL_VARS = 'all_solutions.tex'

class Hashabledict(dict):
    def __hash__(self):
        return hash(frozenset(self))
    def __lt__(self,a):
        for key in sorted(self.keys()):
            if key not in a:
                return True
            if self[key] < a[key]:
                return True
            if self[key] > a[key]:
                return False
        return False
        
        

### Check files
for fn in [SUGAR_PERL,SUGAR_JAR]:
    if not os.path.exists(fn):
        raise FileNotFoundError(f"Cannot find sugar {fn}; download it from http://bach.istc.kobe-u.ac.jp/sugar/")

if not os.path.exists(PICOSAT_SOLVER):
    raise FileNotFoundError(f"Cannot find {PICOSAT_SOLVER}")


################################################################
###
### SAT SOLVER SUPPORT
###
################################################################


def is_cnf_file(fname):
    with open(fname,"r") as f:
        return f.read(6)=="p cnf "

def is_satisfied(fname):
    with open(fname,"r") as f:
        for line in f:
            if "s SATISFIABLE" in line:
                return True
        return False

def tally_dimacs_file(dimacs_file):
    assert is_cnf_file(dimacs_file)
    with open(dimacs_file,"r") as f:
        for line in f:
            if line[0]=='c': continue
            fields = line.strip().split(" ")
            assert fields[0]=='p'
            assert fields[1]=='cnf'
            return (int(fields[2]),int(fields[3]))

def run_solver(*,solver,cnffile,outfile):
    assert os.path.exists(cnffile)
    assert not os.path.exists(outfile)
    if "picosat" in solver:
        cmd = [solver,cnffile,'-o',outfile]
    elif "glucose" in solver:
        cmd = [solver,cnffile,outfile]
    else:
        raise RuntimeError("Unknown solver: {}".format(solver))
    print(" ".join(cmd))
    p = Popen(cmd,stdout=PIPE,stderr=PIPE)
    (out,err) = p.communicate()
    assert os.path.exists(cnffile)
    assert os.path.exists(outfile)
    if is_satisfied(outfile):
        return 
    solver_out = out.decode('utf-8'); del out
    solver_err = err.decode('utf-8'); del err
    raise RuntimeError("solver failed. ret={} out='{}' err='{}'".
                       format(p.returncode,solver_out,solver_err))


################################################################
###
### SUGAR SUPPORT
###
################################################################


def sugar_encode_csp(*,cspfile,cnffile,mapfile):
    """Run sugar to make an output file"""
    assert os.path.exists(cspfile)
    assert not os.path.exists(cnffile)
    assert not os.path.exists(mapfile)
    cmd = ['java','-cp',SUGAR_JAR,'jp.kobe_u.sugar.SugarMain','-v', '-encode', cspfile, cnffile, mapfile]
    print(" ".join(cmd))
    p = Popen(cmd,stdout=PIPE,stderr=PIPE)
    (out,err) = p.communicate()
    sugar_out = out.decode('utf-8'); del out
    sugar_err = err.decode('utf-8'); del err
    if p.returncode!=0:
        raise RuntimeError("sugar returned {}. out='{}' err='{}'".format(p.returncode,sugar_out,sugar_err))
        exit(1)
    assert os.path.exists(cnffile)
    assert os.path.exists(mapfile)
    
def sugar_decode_picosat_out(outdata,mapfile):
    cmd = ['java','-cp',SUGAR_JAR,'jp.kobe_u.sugar.SugarMain','-decode','/dev/stdin',mapfile]
    print(" ".join(cmd))
    (out,err) = Popen(cmd,stdin=PIPE,stdout=PIPE,stderr=PIPE).communicate(outdata.encode('utf-8'))
    out = out.decode('utf-8')
    err = err.decode('utf-8')
    if err:
        raise RuntimeError("sugar decode error: "+err)
    return out

def get_mapvars(mapfile):
    """Read the sugar .map file and return a dictionary
    where the key is the variable name and the value is the (start,r0,r1)
    where r0 is the first ordinal and r1 is the last. Sugar uses uniary encoding."""
    mapvars = {}
    with open(mapfile,"r") as f:
        for line in f:
            (var,name,start,_) = line.strip().split(" ")
            if var=="int":
                if ".." in _:
                    (r0,r1) = _.split("..")
                else:
                    (r0,r1) = int(_),int(_)
            else:
                raise RuntimeError("Only variables of type {} are supported".format(var))
            start = int(start)
            r0 = int(r0)
            r1 = int(r1)
            mapvars[name] = (start,r0,r1)
    return mapvars

def extract_vars_from_solver_output(*,solver_output_lines,mapfile,mapvars=None):
    """Read the output from a SAT solver and a map file and return the variable assignments 
    and a set of coeficients to add the dimacs file to prevent this solution."""

    assert len(solver_output_lines) > 10
    satvars    = {}                # extracted variables
    if mapvars==None:
        mapvars = get_mapvars(mapfile)
    # Compute the highest possible variable
    highest = max(v[0]+v[2]-v[1] for v in mapvars.values())
    # Now read the boolean variables and map them back
    coefs = set()               # each variable is positive or negative
    for line in solver_output_lines:
        # For each line in the DIMACS output file
        # read the numbers and add each to the coefficients set. 
        # stop when the first line is higher than the higest variable that we care about
        if line[0]!='v': continue
        vals = [int(v) for v in line[2:].split(" ")]
        if abs(vals[0]) > highest:
            break               # no need to read any more
        coefs.update(vals)

    # Now for each variable, check all of the booleans that make it up
    # to find the value of the variable. Also create the counter example.
    counter = set()
    for var in mapvars:
        (start,r0,r1) = mapvars[var]
        found = False           # we found the state change.
        for i in range(r1-r0):
            x = start+i
            if x in coefs:      # check for positive
                if not found:   # must be the transition from negative to positive
                    satvars[var] = str(r0+i)
                    found = True
                coefs.add(-x)
            else:
                coefs.add(x)
        if not found:
            satvars[var] = str(r0+1)
    print("satvars=",satvars)
    return (mapvars,satvars,counter)

################################################################
def latex_def(name,value):
    return "\\newcommand\\{}{{\\xspace{:,d}\\xspace}}\n".format(name,value)

def lines_iter(data):
    """Returns the lines without a newline"""
    return (x.group(0) for x in re.finditer(".*", data) if x.group(0))

def linecount(fname,filter_func):
    return len(list(filter(filter_func,open(fname,"r").read().split("\n"))))

def unmap(satvars,var):
    # Given a variable that is to be unmapped (e.g. A2)
    # transform it to text
    try:
        rvar = satvars[var]        # rvar is what we are returning
    except KeyError:
        return var
    try:
        return VARMAP[var[0]][rvar]
    except KeyError:
        return rvar

def extract_vars_from_sugar_decode(outdata):
    """Extract the variables from the sugar output. Returns a dictionary
    with the key the variable name and the value being the variable
    value"""
    # vars[] is the mapping of the sugar variable to the solution
    vars = Hashabledict()
    for line in outdata.split("\n"):
        line = line.strip()
        if len(line)==0: continue
        if line[0]=='s' and line!='s SATISFIABLE':
            print(outdata)
            raise RuntimeError("Constraints not satisfied; line={}".format(line))
        if line[0]=='a' and "\t" in line:
            (var,val) = line[2:].split("\t")
            vars[var] = val
    return vars


def sugar_decode_picostat_and_extract_satvars(lines,mapfile):
    return extract_vars_from_sugar_decode( sugar_decode_picosat_out( "\n".join(lines), mapfile))

def picosat_get_next_solution(path):
    """Read the picosat solution file and return each solution"""
    lines = []
    with open(path,"r") as f:
        for line in f:
            if line.startswith('c'):
                continue
            if line=="s SATISFIABLE\n":
                if lines:
                    yield lines
                    lines = []
            if line.startswith('s SOLUTIONS'):
                continue
            lines.append(line)
        if lines:
            yield(lines)
            

def parse_picosat_all_file(path):
    print("parsing picosat all file {}".format(path))
    total_solutions = 0
    distinct_solutions = 0
    seen = set()
    ctr = 0
    for lines in picosat_get_next_solution(path):
        total_solutions += 1
        # Our version worked, but we seem to have a bug, so use the sugar code here.
        #(mapvars,satvars,counter) = extract_vars_from_solver_output(solver_output_lines=lines,mapfile=args.map)
        satvars = sugar_decode_picostat_and_extract_satvars(lines,args.map)
        seen.add(satvars)

    for (ct,satvars) in enumerate(sorted(seen),1):
        print(f"sugar solution {ct} / {total_solutions}: {satvars}")



if __name__=="__main__":
    from argparse import ArgumentParser,ArgumentDefaultsHelpFormatter
    parser = ArgumentParser( formatter_class = ArgumentDefaultsHelpFormatter,
                             description="Runs sugar with picosat and parse the results into LaTeX")
    parser.add_argument("--cnf",default="constraints.cnf",help="specify cnf file")
    parser.add_argument("--parseout",
                        help="Parse the variables out of an .out file. A map file must be specified")
    parser.add_argument("--parseall",help='Evaluate output file of the picosat --all')
    parser.add_argument("--solver",default="picosat")
    parser.add_argument("--picosat_out",help='picosat output file',default='constraints.out')
    parser.add_argument("--map",help="Specify map file",default='constraints.map')
    parser.add_argument("--all",help="Compute all possible solutions; store results in ALL")
    parser.add_argument("--decode",help="test the decode function")
    parser.add_argument("--define",help="specify a #define to CPP")
    parser.add_argument("--sugar_output",help="specify sugar output",default='constraints.sugar.out')
    parser.add_argument("--csp", help="CSP File")
    parser.add_argument("problem",default="hhtype.csp",help="specify the problem CSP")
    args = parser.parse_args()

    if not args.csp:
        args.csp = args.problem+".tmp"

    if args.parseout:
        out = open(args.parseout,"r").read()
        (mapvars,satvars,counter) = extract_vars_from_solver_output( solver_output_lines=out.split("\n"), 
                                                                     mapfile=args.map) 
        print(parse_vars_to_printable(satvars))
        exit(1)

    if args.parseall:
        parse_picosat_all_file(args.parseall)
        exit(0)

    if args.decode:
        decode(open(args.decode,"r").read())
        exit(0)


    # Run the pre-processor and remove the files that begin with a '#'
    cmd = ['cpp',args.problem]
    (out,err) = Popen(cmd,stdout=PIPE).communicate()
    with open( args.csp,"w") as f:
        for line in out.decode('utf-8').split("\n"):
            if line.startswith('#'):
                continue
            f.write(line)
            f.write("\n")

    # Run sugar, which runs the solver
    if args.all:
        args.solver += " --all"
    tmp = args.cnf.replace(".cnf","")

    # Here is what the Java looks like
    # java  -cp './sugar-v2-3-3/bin/sugar-v2-3-3.jar' jp.kobe_u.sugar.SugarMain -vv  -encode 'constraints.csp' 'constraints.cnf' 'constraints.map'

    cmd = ['perl',SUGAR_PERL,
           '-jar',SUGAR_JAR,
           '-vv',
           '-solver',args.solver,'-keep','-tmp','constraints',
           '-output',args.picosat_out]

    cmd += [args.csp]
    print(" ".join(cmd))
    t0 = time.time()
    p = Popen(cmd,stdout=PIPE,stderr=PIPE,encoding='utf-8')
    (sugar_out,sugar_err) = p.communicate()
    t1 = time.time()
    if p.returncode!=0:
        raise RuntimeError("sugar returned {}. out='{}' err='{}'".
                           format(p.returncode,sugar_out,sugar_err))
        exit(1)
    print("sugar run time: {:.4} sec".format(t1-t0))
    print(sugar_out)
    print(sugar_err)

    if args.all:
        parse_picosat_all_file(args.picosat_out)
        exit(0)

    # keep a copy of the sugar output
    # Not strictly necessary, but useful for debugging
    with open(args.sugar_output,'w') as f:
        f.write(sugar_out)

    # Now constraints.out has the output from picosat

    if "ERROR" in sugar_out:
        print("Error in running sugar:")
        print(sugar_out)
        exit(1)
    
    satvars = extract_vars_from_sugar_decode(sugar_out)
    results = satvars_to_codes(satvars)

    # Print information about reconstruction, sorted
    for (age,desc) in sorted(results):
        print(desc)
        
