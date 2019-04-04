#
# make sure that we can read the sf1 file

from constants import *

from sf1_doc_decoder import *

#def test_part_matrix_columns():
#    cols = part_matrix_columns(3)
#    for line in sf1_file_from_zip('ak',3):
#        fields = line.strip().split(",")
#        break
#    assert len(cols) == len(fields)

SF1_H22_LINE='H22.,,,,"ALLOCATION OF TENURE [3]'

SF1_FIPS_LINE='FIPS Place Class Code8                                                                 PLACECC,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,2,,,,,,51,,,,,,,,A/N,'

def test_line_to_fields():
    fields = line_to_fields(SF1_H22_LINE)
    assert fields[0]=='H22.'
    assert fields[1]=='ALLOCATION OF TENURE'
    
def test_H22_LINE_parses_chapter6():
    for line in open(SF1_CHAPTER6_CSV,"r",encoding='latin1'):
        if line.strip()==SF1_H22_LINE:
            # I have the line. Make sure we find the tables in it.
            fields = line_to_fields(line)
            tn = is_table_name(fields)
            assert tn[0]=='H22'
            assert tn[1]=='ALLOCATION OF TENURE'
            return True
    raise RuntimeError("SF1_H22_LINE not found in SF1_CHAPTER6_CSV")
    
def test_line_to_fields():
    fields = line_to_fields(SF1_FIPS_LINE)
    assert len(fields)==4
    #assert fields[0]=='FIPS Place Class Code8 PLACECC'
    assert fields[1]=='2'
    assert fields[2]=='51'
    assert fields[3]=='A/N'
    m = VAR_RE.search(fields[0])

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
