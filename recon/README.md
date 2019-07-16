This is the clean rewrite of the existing database reconstruction code.

**Please read this file through to the end before starting.**

The purpose of this code is to perform a database reconstruction
attack on the published statistics in the Census SF1. All global
parameters, including path names, are stored in the file
(config.ini)[config.ini]. In this document, config variables are
indicated **in bold**.

This system is semi-automated, but it becomes a bit more automated
every time it is run!

Note that this system is designed to work equally well using Amazon
S3's storage system or using local storage.  We handle this with the
`dopen` function that is defined in (dbrecon.py)[dbrecon.py]. There is
a better-developed version of `dopen` in the Census `ctools` package,
but we do not include it here for brevity and isolation. 

Before you start, look at (config.ini)[config.ini] and make sure that
all of the paths are good for your system! Then follow these steps:

* STEP 0 - Download the files. 
* STEP 1 - Extract the geography information from the SF files and create the state-level CSVs
* STEP 2 - Combines the segments of the each state's SF1 and outputs a set of CSV files for each county that contain the block-level measurements, the tract level measurements, and the county-level measurements. `s2_pandas_build_state_stats.py` was the original version of this program and it was very slow and very memory intensive. `s2_nbuild_state_stats.py` is the rewrite, which is neither slow nor memory intensive. Instead of using pandas, it uses a hand-tuned join and group by written in pure python. It can do the entire state of califronia in 4 hours in a single Python thread and with less than 2 GiB of RAM. 
* STEP 3 - Create the `.lp.gz` files associated with each Census tract. This is still very memory intensive. We store the LP files compressed because they are quite large (many more than a gigabyte) and highly compressible (typically 20:1). 
* STEP 4 - Solve the `.lp.gz` files to produce the `.sol.gz` files. Each LP file typically solves in 1-10 seconds. Gurobi won't write out compressed files, so we write them out as `.sol` files and then compress them, which gives us a good way of knowing that the file is complete.
* STEP 5 - Produce the population files. This step makes the microdata!

Steps 3 and 4 can be run concurrently using the `scheduler.py` program. If you are not using `scheduler.py`, you are wasting machine resources. That's because the CPU and memory requirements of steps 3 and 4 are unpredictable, so the scheduler just launches jobs until some (but not all) of the CPU cores and RAM are in use. If more RAM is needed, it will kill the most recently launched jobs. It's pretty good at following things, but it crashes every now and then and must be manually restarted.

## Configuration Information
Configuration information is kept in the file config.ini. The following sections are present:

* `[run]` --- configuration information for the scheduler.py program. 
* `[urls]` --- download URLs.
* `[paths]` --- file paths.
* `[gurobi]` --- configuration informaton for the Gurobi optimizer
* `[mysql]` --- configuration information for the database used to track progress of steps 3 (`.lp.gz` file creation) and 4 (`.sol.gz` creation).

The configuration file is used by every python program. The `scheduler.py` program re-reads the config file each time through the main event loop, so you can actually change configuration parameters on the fly, without interrupting and restarting the program.

We've made substantial modification to the normal Python procedure for reading configuration files. Specifically:

1. Each configuration variable can include multiple versions which are used on different hosts. For exmaple, if you have 10 machines in your cluster, with `workera` having 64 cores, `workerb` having 32 cores, and the remaining having 16 cores, you might set up your Gurobi section so that Gurobi can use as many threads as there are cores, which is typically the right thing to do. Most runs of Gurobi will use just 1 or 2 threads, so you would run up to to look like this:

    [run]
    max_sol = 32
    max_sol@workera: 64
    max_sol@workerb: 32                    
    
    [gurobi]
    threads: 2
    threads@workera: 8
    threads@workerb: 8

This will allow some over-provisioning, but should keep loads under control. Of course, you might want to tune these variables for your systems, and you can tune them while `scheduler.py` is running and they will take effect each time a new step 4 solver is launched.


## Logging

Each run of each program creates two log files, a text-based `.log` file and a `.dfxml` file that captures more detailed information.

Each run of the Gurobi optimizer also creates a Gurobi log file. We will be creating software to analyze these files. 

## Paralleism and scheduling

Reconstructing the microdata of the entire United States ia a massive operation and must be parallelized if you want it to complete within a reasonable amount of time.

Originally parallelism was provided by building it directly into step
3 and step 4. This level of parallelism is sufficient if you have a
single cluster and with to reconstruct a single state. However, for
large jobs, even this level of control over the parallelism was
insufficient. For these situations, we created a scheduler that
oversees step 3 and step 4.

There are many opportunities for parallelism that are realized in the current code:

* Machine-level parallelism. Run `scheduler.py` on every machine. Every machine should have access to a shared file system that is defined in `config.ini`. This file system is best done with NSF, or with lustre, or with Amazon S3, in that order. 

* Non-shared memory parallelism. This parallelism refers to building multiple county LP files at once, or simultaneous level invocations of Gurobi. This parallelism is specified by the `--j1` parameter if you are relying on the parallelism coming directly from the Python step 2 or step 3 programs, but it's better handled by the `scheduler.py` program, since `scheduler.py` will automatically launch new jobs as needed and kill jobs if too many are running. 

* Shared-memory parallelism. Building the LP files can be parallelized, because the data is read in county-by-county, but we build an LP file for each tract. Solving the LP files can also be parallelized, because Gurobi supports multiple threads. Shared-memory parallelism is specified by the `--j2` parameter or by the `[run].lp_j2` and `[guroobi].threads` parameters in the config files. 


# Making it all run

## Step 0 - Download the files

Download the SF1 data from the Census Bureau's website
http://www2.census.gov/ using the program `s0_download_data.py`. This
program does not parallelize, but it does check to see if the file you
are trying to download has already been downloaded.

    python3 s0_download_data.py --all

## Step 1 - Extract the geography information

Extract and lightly process the geography information from each SF1
file. (It's not clear why we don't use the the original geography
files, but we don't. This may be changed before the final public
release.) This is fast, so it is not parallelized.

    python3 s1_make_geo_files.py --all

## Step 2 - Create CSV files associated with each state

This step extracts the summary level for STATE, COUNTY, TRACT,
BLOCK_GRP, BLOCK, SUMLEVEL and LOGRECNO from all of the SF1 files and
outputs a two-dimensional table for each county.

The original implementation of this used pandas and was quite memory
heavy, especially for the larger states. (CA takes 100GB). You will
find this implementation in `s2_pandas_build_state_stats.py` and it
isn included for historical reference only.

The rewrite of this performs a purely semantic merging of the
files. It's much more efficient in both speed and memory. The program
starts by reading the entire geography file and storing the records in
memory that hold the block, tract, or county-level records. The
program then opens 39 input files (1 for each SF1 segment) and an
output file for every county. It then reads the SF1 records one record
(39 files), performs a join with the appropriate record in the
geography file, and writes the output to the appropriate county file.

 The direct implementation is complicated by the fact that not every
 logical record is in every segment file. So we create a reader that,
 when given a logical record request, returns either blank logical
 records or the records from the requested file. 

The file `$ROOT/{state_abbr}/completed_{state_abbr}_02` is created when each
state is completed. (This would take less memory, and be faster, if a
single data frame was not created for all of the counties in each
state.) On our machine the Deleware completed in just 630 seconds (10
minutes), but CA took 14844.2 seconds (4.12 hours)

    python3 02_build_state_stats.py --all

## Step 3 --- Create the .lp.gz files

The database reconstruct works by creating linear program (LP) files
that are delivered to the Guorbi optimizer. The structure of these LP
files makes them quite large---typically between 50MB and
1GB. However, these files are quite compressible, so we write them as
compressed files and then (in Step 4) we convince Guorbi to read the
compressed files. 

There is 1 .lp.gz file for every census tract. The model to create the
tract-level files are created by reading the summary files created in
step #2. So we can parallelize at the (state,county) level, and we can
then parallelize within each (state,county) tuple at the tract
level. The first set of parallelization do not share memory, but the
second step do. To handle this, we use the 03_synth_lp_files.py
program. It has two parallelization parameters: --j1, which specifies
how many (state,county) pairs to run at once, and --j2, which says how
many tracts to run at once for each (state,county) pair. The default
for each of these is 8.

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


