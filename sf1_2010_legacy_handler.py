
def part_matrix_columns(fileno):
    """Given a SF1 part number, return the columns based on an analysis of Chapter 6."""
    assert 1<=fileno<=47
    infile = None
    cols = []
    with open( fileno, "r", encoding='latin1') as f:
        for line in f:
            line = line.strip()
            line = re.sub(r",+", ",", line) # replace repeated commas with a single comma
            line = re.sub(r" +", " ", line) # replace repeated spaces with a single space
            if line[0]==',':
                line = line[1:]
            m = FILE_START_RE.search(line)
            if m:
                infile = int(m.group(1))
                continue
            if infile != fileno:
                continue
            print(line)
            for word in re.split("[ ,]",line):
                if len(word) > 3:
                    m = VAR_RE.search(word)
                    if m:
                        cols.append(word)
                        print(len(cols),m,word,":",line)
    return cols

                    



################################################################
### LEGACY HANDLING OF 2010 SF1 GEO HEADER
# Define the fileds in the GEO Header. See Figure 2-5 of SF1 publication
# These were extracted by hand. Sorry!
GEO_FILEID=(1,6)
GEO_STUSAB=(7,2)
GEO_STATE=(28,2)
GEO_SUMLEV=(9,3)
GEO_LOGRECNO=(19,7)
GEO_COUNTY=(30,3)
GEO_PLACE=(46,5)            
GEO_TRACT=(55,6)            
GEO_BLKGRP=(61,1)
GEO_BLOCK=(62,4)        # first digit of block is blockgroup

# Using the constants above, extract a string from a line, and extract an integer.
def ex(line,what):
    """Given a line and a tuple defining the field (START,COUNT), extract the characters."""
    return line[what[0]-1:what[0]+what[1]-1]

def exi(line,what):
    """Same as ex(), but convert to a string."""
    return int(ex(what))

def geocode_for_line(geoline):
    """Given a geoline, extract and return a dictionary of the fields. Currently we only extract the ones listed above"""
    return "".join([ex(line,level) for level in [GEO_STATE, GEO_COUNTY, GEO_TRACT, GEO_BLKGRP, GEO_BLOCK]])

def logrecno_for_sumlev(state,sumlev):
    """Return a dictionary of the logrecnos for a state and the corresponding geocode for each"""
    logrecnos = dict()
    for geoline in sf1_file_from_zip(state,'geo'):
        if ex(geoline,GEO_SUMLEV)==sumlev:
            assert ex(geoline,GEO_FILEID)=='SF1ST'
            assert ex(geoline,GEO_STUSAB)==state
            print(ex(geoline, GEO_LOGRECNO), geocode_for_line(geoline))
            logrecnos[ ex(geoline, GEO_LOGRECNO) ] = geocode_for_line(geoline)
    return logrecnos

