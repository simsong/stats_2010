import py.test
import os
import os.path
from os.path import abspath,dirname,basename
import sys

MY_DIR     = dirname(abspath(__file__))
PARENT_DIR = dirname(MY_DIR)
if PARENT_DIR not in sys.path:
    sys.path.append(PARENT_DIR)

S3_TESTFILE = '$DAS_S3ROOT/2010-re/unittests/testfile.txt.gz'
S3_TESTFILE_CONTENTS='Hello World.\nThis is a test.\n'

# this shouldn't be necessary
#pylint: disable=E0401
import dbrecon

def test_lpfile_properly_termianted():
    assert dbrecon.lpfile_properly_terminated( os.path.join(MY_DIR, "shortfile_bad.lp")) == False
    assert dbrecon.lpfile_properly_terminated( os.path.join(MY_DIR, "shortfile_bad.lp.gz")) == False
    assert dbrecon.lpfile_properly_terminated( os.path.join(MY_DIR, "model_29183980000.lp.gz")) == True

def test_s3gateway():
    v1 = dbrecon.dopen(S3_TESTFILE, 'r', download=False).read()
    assert v1 == S3_TESTFILE_CONTENTS
    v2 = dbrecon.dopen(S3_TESTFILE, 'r', download=True).read()
    assert v2 == S3_TESTFILE_CONTENTS
