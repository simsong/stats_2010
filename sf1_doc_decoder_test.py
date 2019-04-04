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
