from dbrecon import *

def test_state_db():
    assert state_fips('ak')=='02'
    assert state_fips('AK')=='02'
    assert state_fips('02')=='02'
    assert state_fips('ar')=='05'
