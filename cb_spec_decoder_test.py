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

def test_parsed_spec_fields_correct():
    """For the each of the years and products, look at the ak files and make sure that we can account for every column.
    Eventually we will want to verify that a line read with the spec scanner from various files match as well.
    """
    for year in [2010]:
        for product in [SF1]:
            if product==SF1:
                chariter = '000'
            ch6file = CHAPTER6_CSV_FILES.format(year=year,product=product)
            assert os.path.exists(ch6file)
            schema = schema_for_spec(ch6file)
            for file_number in range(1,FILES_FOR_YEAR_PRODUCT[year][product]+1):
                state = 'ak'
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
                        print(f"Found {len(fields)} fields; expected {total_fields}")
                        print(line)
                        # Make a list of all the variables I think I have, and the value I found
                        table_vars = []
                        for (ct,table) in enumerate(tables_in_this_file):
                            for var in table.vars():
                                if ct==0 or var.name not in LINKAGE_VARIABLES:
                                    table_vars.append(var)
                        while len(table_vars) < len(fields):
                            table_vars.append("n/a")
                        while len(table_vars) > len(fields):
                            fields.append("n/a")

                        for i in range(len(table_vars)):
                            print(f"file {file_number} field {i+1}  {table_vars[i]}   {fields[i]}")
                    # Only look at the first line:
                    break
    raise RuntimeError("look at output")
                
            
        
    
