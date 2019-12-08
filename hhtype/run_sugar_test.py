from run_sugar import *
import tempfile

### This is what the mapfile looks like
MAPFILE="""
int SIZE 1 1..7
int MARRIED 7 0..1
int MARRIED_SAME_SEX 8 0..1
int MARRIED_OPPOSITE_SEX 9 0..1
int MULTIG 10 0..1
int CHILD_UNDER_18 11 0..1
int OWN_CHILD_UNDER_6_ONLY 12 0..1
int OWN_CHILD_BETWEEN_6_AND_17 13 0..1
int OWN_CHILD_IN_BOTH_RANGES 14 0..1
int OWN_CHILD_UNDER_18 15 0..1
"""

PYTHON_MAP_VARS = {'SIZE': ('int', 1, 1, 7),
                   'MARRIED': ('int', 7, 0, 1),
                   'MARRIED_SAME_SEX': ('int', 8, 0, 1),
                   'MARRIED_OPPOSITE_SEX': ('int', 9, 0, 1),
                   'MULTIG': ('int', 10, 0, 1),
                   'CHILD_UNDER_18': ('int', 11, 0, 1),
                   'OWN_CHILD_UNDER_6_ONLY': ('int', 12, 0, 1),
                   'OWN_CHILD_BETWEEN_6_AND_17': ('int', 13, 0, 1),
                   'OWN_CHILD_IN_BOTH_RANGES': ('int', 14, 0, 1),
                   'OWN_CHILD_UNDER_18': ('int', 15, 0, 1)}

### This is what the picosat output looks like
PICOSAT_OUT="""
s SATISFIABLE
v -1 -2 -3 -4 -5 -6 7 8 9 -10 -11 -12 -13 14 15 0
"""

### This is what sugar thinks of the above
SUGAR_OUT="""s SATISFIABLE
a SIZE	7
a MARRIED	0
a MARRIED_SAME_SEX	0
a MARRIED_OPPOSITE_SEX	0
a MULTIG	1
a CHILD_UNDER_18	1
a OWN_CHILD_UNDER_6_ONLY	1
a OWN_CHILD_BETWEEN_6_AND_17	1
a OWN_CHILD_IN_BOTH_RANGES	0
a OWN_CHILD_UNDER_18	0
a
"""

SUGAR_VARS = {'SIZE': 7, 'MARRIED': 0, 'MARRIED_SAME_SEX': 0, 'MARRIED_OPPOSITE_SEX': 0, 'MULTIG': 1, 'CHILD_UNDER_18': 1, 'OWN_CHILD_UNDER_6_ONLY': 1, 'OWN_CHILD_BETWEEN_6_AND_17': 1, 'OWN_CHILD_IN_BOTH_RANGES': 0, 'OWN_CHILD_UNDER_18': 0}

def test_sugar_decoders():
    with tempfile.NamedTemporaryFile(mode='w') as f:
        f.write(MAPFILE)
        f.flush()
        outdata = sugar_decode_picosat_out(PICOSAT_OUT,f.name)
    assert outdata==SUGAR_OUT
    vars = extract_vars_from_sugar_decode(outdata)
    assert vars==SUGAR_VARS

def test_python_decoders():
    with tempfile.NamedTemporaryFile(mode='w') as f:
        f.write(MAPFILE)
        f.flush()
        mapvars = python_get_mapvars(f.name)
        print(mapvars)
        assert mapvars==PYTHON_MAP_VARS
        
        satvars = python_decode_picosat_and_extract_satvars(solver_output_lines=PICOSAT_OUT.split("\n"), mapvars=mapvars)
        logging.error("satvars: %s",satvars)
        logging.error("SUGARSA: %s",SUGAR_VARS)
        assert satvars==SUGAR_VARS

if __name__=="__main__":
    test_sugar_decoders()
    test_python_decoders()
