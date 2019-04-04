#
# make sure that we can read the sf1 file

from constants import *

from sf1_doc_decoder import *

def test_part_matrix_columns():
    cols = part_matrix_columns(3)
    for line in sf1_file_from_zip('ak',3):
        fields = line.strip().split(",")
        break
    assert len(cols) == len(fields)
