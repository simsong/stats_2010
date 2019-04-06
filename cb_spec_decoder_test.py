#
# make sure that we can read the sf1 file

from constants import *

from cb_spec_decoder import *

#def test_part_matrix_columns():
#    cols = part_matrix_columns(3)
#    for line in sf1_file_from_zip('ak',3):
#        fields = line.strip().split(",")
#        break
#    assert len(cols) == len(fields)

SF1_P6_LINE='other races                                                                              P0060007              03          9,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,'
SF1_P0090058='Race                                                                          P0090058              03          9,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,'
SF1_H22_LINE='H22.,,,,"ALLOCATION OF TENURE [3]'

SF1_FIPS_LINE='FIPS Place Class Code8                                                                 PLACECC,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,2,,,,,,51,,,,,,,,A/N,'

def test_chapter6_prepare_line():
    assert chapter6_prepare_line(SF1_H22_LINE)=="H22. ALLOCATION OF TENURE"

def test_is_table_name_line():
    assert is_table_name_line(chapter6_prepare_line(SF1_H22_LINE))

def test_H22_LINE_parses_chapter6():
    for line in chapter6_lines(SF1_CHAPTER6_CSV):
        if line.strip().startswith("H22."):
            # I have the line. Make sure we find the tables in it.
            tn = is_table_name_line(line)
            assert tn[0]=='H22'
            assert tn[1]=='ALLOCATION OF TENURE'
            return True
    raise RuntimeError("SF1_H22_LINE not found in SF1_CHAPTER6_CSV")
    
def test_P0090058_parser():
    (name,desc,segment,maxsize) = parse_variable_desc(chapter6_prepare_line(SF1_P0090058))
    assert name=='P0090058'
    assert desc=='Race'
    assert segment==3
    assert maxsize==9

def test_tables_in_sf1():
    tables = tables_in_file(SF1_CHAPTER6_CSV)
    for table in sorted(tables):
        print(table,tables[table])
    for p in range(1,50):
        assert f"P{p}" in tables
    for pct in range(1,24):
        assert f"PCT{pct}" in tables
    for i in range(ord('A'),ord('O')+1):
        ch = chr(i)
        assert f"PCT12{ch}" in tables
    for h in range(1,23):
        assert f"H{h}" in tables
    for i in range(ord('A'),ord('I')+1):
        ch = chr(i)
        assert f"H11{ch}" in tables

def test_schema_segment3():
    schema = schema_for_spec(SF1_CHAPTER6_CSV,3)
    # format is table #, max variable number
    ptables = [(3,8),
               (4,3),
               (5,17),
               (6,7),
               (7,15),
               (8,71),
               (9,73)]
    for (table,maxvars) in ptables:
        tablename = f'P{table}'
        assert tablename in schema.tabledict
        t = schema.get_table(tablename)
        for v in range(1,maxvars+1):
            varname = f'P{table:03}{v:04}'
            assert varname in t.vardict

def test_spec_

def test_spec_parsing():
    # for the each of the products, look at the ak files and make sure that we have the correct
    # number of columns
    
