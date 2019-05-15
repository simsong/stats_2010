This is the clean rewrite of the existing database reconstruction code.

**Please read this file through to the end before starting.**

The purpose of this code is to perform a database reconstruction
attack on the published statistics in the Census SF1. All global
parameters, including path names, are stored in the file
(config.ini)[config.ini]. In this document, config variables are
indicated **in bold**.

Currently this system is semi-automated, but it becomes a bit more
automated every time it is run!

Note that this system is designed to work equally well using Amazon
S3's storage system or using local storage.  We handle this with the
`dopen` function that is defined in (dbrecon.py)[dbrecon.py]. There is
a better-developed version of `dopen` in the Census `ctools` package,
but we do not include it here for brevity. For more information, see [dbrecon_README.md](dbrecon_README.md).

Before you start, look at (config.ini)[config.ini] and make sure that
all of the paths are good for your system! Then follow these steps:

   STEP 0 - Download the files
   STEP 1 - Extract the Geography information from the SF files (state CSVs)
   STEP 2 - Create CSV files associated with each state (county CSVs)
   STEP 3 - Create the LP files associated with each Census tract
   STEP 4 - Solve the LP files and produce the microdata


0. Download the SF1 data from the Census Bureau's website
http://www2.census.gov/ using the program `00_download_data.py`. This
program does not parallelize, but it does check to see if the file you
are trying to download has already been downloaded.

    python3 00_download_data.py --all

1. Extract and lightly process the geography information from each SF1
file. (It's not clear why we don't use the the original geography
files, but we don't. This may be changed before the final public
release.) This is fast, so it is not parallelized.

    python3 01_make_geo_files.py --all

2. Extract the summary level for STATE, COUNTY, TRACT, BLOCK_GRP,
BLOCK, SUMLEVEL and LOGRECNO and a data frame with all of the SF1
measurements. 

The time and memory that this process requires is proportional to the number of census tracts and blocks. We have provided two implementations:

Pandas Implementation --- 02_pandas_build_state_stats.py.  This implementation is single-threaded. It requires roughly 59GB of RAM to process TX and 49GB of RAM to process CA; other states take less. Time on our high-performance server is

The file `$ROOT/{state_abbr}/completed_{state_abbr}_02` is created when each
state is completed. (This would take less memory, and be faster, if a
single data frame was not created for all of the counties in each
state.) On our machine the Deleware completed in just 630 seconds (10
minutes), but CA took 14844.2 seconds (4.12 hours)

    python3 02_build_state_stats.py --all

3. Create the LP files. There is 1 LP file for every census tract. The
LP files are very large. The model to create the tract-level files are
created by reading the summary files created in step #2. So we can
parallelize at the (state,county) level, and we can then parallelize
within each (state,count) tuple at the tract level. The first set of
parallelization do not share memory, but the second step do. To handle
this, we use the 03_synth_lp_files.py program. It has two
parallelization parameters: --j1, which specifies how many
(state,county) pairs to run at once, and --j2, which says how many
tracts to run at once for each (state,county) pair. The default for
each of these is 8.

To give you an idea of how long this takes, know that synthsizing AK 110 (Juno), population 31,275, with 6 census tracts, requires 1183 seconds of CPU and 43GB of RAM with --j2==1.  With --j2=8 it requires 284 seconds of CPU and the same amount of RAM (because the RAM is shared).

    python3 03_synth_lp_files.py all all 


4. Run the Gurobi on the LP files.

5. Generate the final report


# Design
Requirements:
* A place to store all of the data that's persistent.  Options: 
  * backed up file systems; 
  * Amazon S3. 
* A way to distribute the load among many processes. 
  
Goals: 
1. consistent maming scheme for data files
2. Make as few changes to the structure of original code as possible
3. All programs are testable and generate provenance for output

Changes:
1. All encodings changed to UTF-8 (previously UTF-8859-1 was hard-coded in several places). 
2. Variables replaced with descriptive names. E.g. "string" becomes "line"
3. The file sf1_vars_race_binaries.csv specifies the mapping from the published tables to the various tabulations. Previously it used Y to indicate a value was present in a tabulation and a N to indicate it was not, and "missing" to indicate that it was missing. This caused memory issues with pandas. We have changed this according to:  "missing" -> -1, "N" -> 0, "Y" -> 1. This lets the columns be represented as integers rather than objects.

## File Layout

Source Code Hiearchy:
    $SRC/config.ini             - Master configuration file for database reconstruction
    $SRC/layouts/               - Data files used in the processing.
    $SRC/layouts/geo_layout.txt - geography layout file. This was made by hand, apprently.
    $SRC/layouts/layouts.json   - A JSON file created from the access database on the website

Where:
   $SRC   = Root of Python source tree  (dopen expands this automatically)


Data Hiearchy:
    ROOT         - Root of reconstructed and re-identified files files
S3://BUCKET/ROOT - Root of files on file server

ROOT could be on S3...

Original layout:

$ROOT/ST/sf1/                         - directory for unpacking SF1
$ROOT/ST/sf1/STnnnnnnnnn.sf1          - SF1 table files
$ROOT/ST/sf1/ST2010.sf1.prd.packinglist.txt - SF1 packing list
$ROOT/ST/sf1/ST2010.sf1.zip           - SF1 ZIP file
$ROOT/ST/sf1/STgeo.sf1.zip            - SF1 geo ZIP file
$ROOT/ST/sf1/state_county_list_SN.csv - state and county info
$ROOT/ST/ST_geofile.csv               - unzipped SF1 geo file


$ROOT/ST/SNCOUNT/
$ROOT/ST/SNCOUNT/sf1_block_COUNTY.csv  - county-level data from SF1
$ROOT/ST/SNCOUNT/sf1_county_COUNTY.csv - county-level data from SF1
$ROOT/ST/SNCOUNT/sf1_tract_COUNTY.csv  - tract level data from SF1
$ROOT/ST/SNCOUNT/lp/                   - directory for LP files
$ROOT/ST/SNCOUNT/lp/model/model_params_GEOID.lp - the LP files
$ROOT/ST/SNCOUNT/lp/sol/model_STATE*TRACT.sol - the LP solution files

Where:
  $ROOT   = Root of reconstructed data on local file systme.
  ST      = 2 character state abbreviation  (04 is Arizona)
  SNCOUNT = 2 digit state ANSI code + 3 digita county abbreviation (04001 is Apache County, AZ)
  GEOID  = GeoID code = STATE*TRACT  (e.g. 02013000100 = State 02 (AK), County 013, Tract 0001.00)
  *TRACT = 6 digit character tract


# Operation
## New program:

`driver.py` is main driver for the reconstruction program. 

Options:
  --download - Download all the data
  --

## Changes:
read_geo_file.py - rewritten to read and write a line at a time. Slowed it down, but took dramatically less memory

## Old code sequence

1. `download_data.py` - downloads the SF1 zip files from census.gov and unzips the ZIP files in ROOT/{state_name}
2. `read_geo_file.py` - uses `geo_layout.txt` and the state geography file in the ZIP to produce a `geofile_xx.csv`. 
3. `read_files_allstate.py` reads the SF1 tables and unpacks each county into its own directory.
4. `make_state_list.py` - creates the metadata file `state_county_list_xx.csv`
5. `synth.py` - for a particular state and county, creates the LP file `model_params_{geo_id}.lp`
6. `run_gurobi.py` - runs gurobi for a particular state and county. 


## Validation

This information is for those of us at the Census Bureau. It largely
tracks how we validated that the new code ran as was as the original,
development code. 

# Cleaning up the bad blocks
The directory `bad/` contains the blocks that did not properly reconstruct.

The file `bad/stats.py` prints stats about these bad blocks.

The original reconstruction is stored in:

$S3ROOT/title13_reid_cleanup/solution_variability/{state_name}/{state_code}{county_code}/

(Ignore the title13 prefix, as the data are not actually title13)


# Tests
For testing, we have two additional directories, which must be specified in config.ini:

    GOLD_ROOT - where the good files are kept
    TEST_ROOT - Where the the programs under test will write their results


When py.test is run, the config.ini file is copied into TEST_ROOT/test_config.ini, with the value of ROOT in the test config file being replaced with the value of TEST_ROOT from the config.ini file.

