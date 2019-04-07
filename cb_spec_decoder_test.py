#
# make sure that we can read the sf1 file

from constants import *

from cb_spec_decoder import *
from decimal import Decimal

SF1_CHAPTER6_CSV = CHAPTER6_CSV_FILES.format(year=2010,product=SF1)
SF1_P6_LINE='other races                                                                              P0060007              03          9,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,'
SF1_P0090058='Race                                                                          P0090058              03          9,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,'
SF1_H22_LINE='H22.,,,,"ALLOCATION OF TENURE [3]'

SF1_FIPS_LINE='FIPS Place Class Code8                                                                 PLACECC,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,2,,,,,,51,,,,,,,,A/N,'

SF1_LINE_7837="PCT12G.   SEX BY AGE (TWO OR MORE RACES) [209]\227Con.,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,"


def test_chapter6_prepare_csv_line():
    assert chapter6_prepare_csv_line(SF1_H22_LINE)=="H22. ALLOCATION OF TENURE"

def test_line_7837():
    tn = parse_table_name( chapter6_prepare_csv_line( SF1_LINE_7837 ))
    assert tn[0]=='PCT12G'
    assert tn[1]=='SEX BY AGE (TWO OR MORE RACES)'

def test_parse_table_name():
    assert parse_table_name(chapter6_prepare_csv_line(SF1_H22_LINE))

def test_H22_LINE_parses_chapter6():
    for line in chapter6_lines(SF1_CHAPTER6_CSV):
        if line.strip().startswith("H22."):
            # I have the line. Make sure we find the tables in it.
            tn = parse_table_name(line)
            assert tn[0]=='H22'
            assert tn[1]=='ALLOCATION OF TENURE'
            return True
    raise RuntimeError(f"SF1_H22_LINE not found in {SF1_CHAPTER6_CSV}")
    
def test_P0090058_parser():
    (name,desc,segment,maxsize) = parse_variable_desc(chapter6_prepare_csv_line(SF1_P0090058))
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
    schema = schema_for_spec(SF1_CHAPTER6_CSV)
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
        if tablename not in schema.tabledict:
            raise RuntimeError(f"table {tablename} not in {schema.tabledict.keys()}")
        t = schema.get_table(tablename)
        for v in range(1,maxvars+1):
            varname = f'P{table:03}{v:04}'
            assert varname in t.vardict

def test_spottest_2010_sf1():
    year = 2010
    product = SF1
    state  = 'ak'
    ch6file = CHAPTER6_CSV_FILES.format(year=year,product=product)
    assert os.path.exists(ch6file)
    schema = schema_for_spec(ch6file)

    p3 = schema.get_table('P3')
    ypss = YPSS(year, product, state, p3.attrib[CIFSN])
    for line in open_decennial( ypss ):
        first_line = line
        break
    p3.dump()
    print("first line of ",ypss)
    print(first_line)
    d3 = p3.parse_line_to_dict(first_line)
    assert d3[FILEID]   == 'SF1ST'
    assert d3[STUSAB]   == 'AK'
    assert d3[CHARITER] == '000'
    assert d3[CIFSN]    == '03'
    assert d3[LOGRECNO] == '0000001'
    assert d3['P0030001'] == 710231
    assert d3['P0030002'] == 473576
    assert d3['P0030003'] == 23263
    assert d3['P0030004'] == 104871
    assert d3['P0030005'] == 38135
    assert d3['P0030006'] == 7409
    assert d3['P0030007'] == 11102
    assert d3['P0030008'] == 51875
    
    # Make sure the second table in a fiel works
    p4 = schema.get_table('P4')
    d4 = p4.parse_line_to_dict(first_line)
    assert d4[FILEID]   == 'SF1ST'
    assert d4[STUSAB]   == 'AK'
    assert d4[CHARITER] == '000'
    assert d4[CIFSN]    == '03'
    assert d4[LOGRECNO] == '0000001'
    assert d4['P0040001'] == 710231
    assert d4['P0040002'] == 670982
    assert d4['P0040003'] == 39249

    # Let's make sure decimal works!
    p17 = schema.get_table('P17')
    p17.dump()
    ypss = YPSS(year, product, state, p17.attrib[CIFSN])
    for line in open_decennial( ypss ):
        first_line = line
        break
    print("first line of ",ypss)
    print(first_line)
    d17 = p17.parse_line_to_dict(first_line)
    assert d17[FILEID]   == 'SF1ST'
    assert d17[STUSAB]   == 'AK'
    assert d17[CHARITER] == '000'
    assert d17[CIFSN]    == '05'
    assert d17[LOGRECNO] == '0000001'
    assert d17['P0170001'] == Decimal('2.65')
    assert d17['P0170002'] == Decimal('0.72')
    assert d17['P0170003'] == Decimal('1.93')

    
    

TEST_STATE = 'de'
IGNORE_FILE_NUMBERS = [12]
def test_parsed_spec_fields_correct():
    """For the each of the years and products, look at the ak files and make sure that we can account for every column.
    Eventually we will want to verify that a line read with the spec scanner from various files match as well.
    """
    errors = 0
    for year in [2010]:
        for product in [SF1]:
            if product==SF1:
                chariter = '000'
            ch6file = CHAPTER6_CSV_FILES.format(year=year,product=product)
            assert os.path.exists(ch6file)
            schema = schema_for_spec(ch6file)
            for file_number in range(1,FILES_FOR_YEAR_PRODUCT[year][product]+1):
                if file_number in IGNORE_FILE_NUMBERS:
                    continue
                state = TEST_STATE
                ypss = YPSS(year, product, state, file_number)
                for line in open_decennial( ypss ):
                    fields = line.split(",")
                    assert fields[0] == FILE_LINE_PREFIXES[year][product] # FILEID
                    assert fields[1].lower() == state                     # STUSAB
                    assert fields[2] == chariter                          # CHARITER
                    assert int(fields[3]) == file_number                  # CIFSN
                    assert int(fields[4]) == 1                            # LOGRECNO

                    # make sure that the total number of fields matches those for our spec.
                    # do this by finding all of the tables that have this 
                    # print the line
                    total_fields = 0
                    tables_in_this_file = []
                    for table in schema.tables():
                        if table.attrib['CIFSN']==file_number:
                            tables_in_this_file.append(table)
                            if total_fields==0:
                                total_fields += len(table.vars())
                            else:
                                total_fields += len(table.vars()) - 5 # we only have these five fields on the first table
                    if len(fields) != total_fields:
                        print(f"File {file_number} Found {len(fields)} values in the file; expected {total_fields}")
                        print(f"Tables found:")
                        for table in tables_in_this_file:
                            print(f"{table.name} has {len(table.varnames())} variables according to the specification.")
                        print()
                        print(f"First line of {TEST_STATE} file part {file_number}:")
                        print(line)
                        # Make a list of all the variables I think I have, and the value I found
                        file_vars = []
                        for (ct,table) in enumerate(tables_in_this_file):
                            for var in table.vars():
                                if ct==0 or var.name not in LINKAGE_VARIABLES:
                                    file_vars.append(var.name)
                        while len(file_vars) < len(fields):
                            file_vars.append("n/a")
                        while len(file_vars) > len(fields):
                            fields.append("n/a")

                        for (i,(a,b)) in enumerate(zip(file_vars,fields),1):
                            if a[-3:]=='001':
                                print()
                            print(f"file {file_number} field {i}  {a}   {b}")
                        errors += 1
                    # Only look at the first line:
                    break
    if errors>0:
        raise RuntimeError("Errors found")
                
            
        
    
