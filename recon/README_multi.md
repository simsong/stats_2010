This directory contains tools for running the database reconstruction software on the DAS EMR clusters.

Note: Even though we are using the EMR clusters, we are not using Spark for the reconstruction or for job management. We're just using EMR so that we can bring up new nodes as required.

The Database reconstruction package uses the MySQL database to keep track of the progress of the reconstruction.

Note that the stats_2010 carries its own copies of ctools, dfxml and census_etl. Don't try to make it use what's in das-vm-config, as the stats_2010 package needs to exist without das-vm-config

Workflow
========
Each 2010 reconstruction experiment is given a unique RE identifier,
here called `REIDENT`.

1. SF1s are received and stored under the prefix `$DAS_S3ROOT/2010-re/REIDENT/zips/`

2. The RE identifier is registered using the dbtool.py program:

```
dbrtool.py --register REIDENT
```

All of the database reconstructions operate within the same MySQL
database. REIDENT is used as the database prefix. It must therefore
begin with a letter and contain only letters, numbers, and underbars.

All of the database reconstruction tools in stats_2010/recon have been modified so that they read REIDENT from the Unix environment and then use this as a prefix on every SQL table.

Database registration creates and initializes the `REIDENT_tracts`
table from original `tracts` table.

  - (step0 - downloads from the WWW server. This only needs to be done once, and doesn't need to be run in our EMR environment.)

These can be run on either the DRIVER or the WORKER node:

  - step1 - makes the geofiles underneath the prefix. We make a separate set of geofiles for every REIDENT, because it might change. When run from dbrtool, it takes 1.5 hours. It would go faster if the database server were faster.

  - step2 - outputs the CSV files for each county with block-level measurements. Basically, this combines all of the segments and selects out the LOGRECNOs corresponding to block and tract measurements. It took 1 hour, 5 minutes to run.


3. A scheduler.py process is started on the EMR WORKER nodes. The scheduler can be provided with a specific REIDENT to work, or it can work on any REIDENT that has work to do.

  - The scheduler.py is run with the dbrtool.py, which uses the das-vm-config/bin/every command to launch scheduler.py on each worker. If scheduler.py is already running, the interlock prevents a second from starting up.

  - The scheduler.py system is supposed to detect dead processes and restart them, but some of the county-by-county interlocks are a bit crufty. Another way to schedule this would be to use SQS and have scheduler.py read the next county to work on from the queue, rather than figuring it out from the MySQL database.

4. When all of the work units for a county has been finished, the scheduler will automatically run STEP 5 for that county and make the microdata file.  Note: this may require a (minor modificat)[https://github.ti.census.gov/CB-DAS/stats_2010/issues/9] to scheduler.py.

5. Reconstruction will be monitored on the DAS dashboard at https://dasexperimental.ite.ti.census.gov/re-recon.html, a JavaScript/JQuery app that gets its statistics from the api https://dasexperimental.ite.ti.census.gov/api/re-recon



Data Storage
============
All data for the reconstruction is stored in AWS S3, since that is the
only permanent storage that we have.  (It would have been better to
use AWS EFS, but that was not an option at the start of this project.)


|Prefix|Purpose|
|------|-------|
|`$DAS_S3ROOT/2010-re/`|Root prefix for the 2010 database reconstruction project |
|`$DAS_S3ROOT/2010-re/REIDENT/`|Prefix for each REIDENT|
|`$DAS_S3ROOT/2010-re/REIDENT/dist/`|Prefix for the SF1 zip files|
|`$DAS_S3ROOT/2010-re/REIDENT/work/{ST}/`|Prefix for the state ST data|
|`$DAS_S3ROOT/2010-re/REIDENT/work/{ST}/{SS}{CCC}`|Prefix for the state ST county CCC data|
|`$DAS_S3ROOT/2010-re/REIDENT/work/{ST}/{SS}{CCC}/lp/model_{SS}{CCC}{TRACT}.lp.gz`|Prefix for each lp files forthe STATE COUNTY|
|`$DAS_S3ROOT/2010-re/REIDENT/work/{ST}/{SS}{CCC}/sol/model_{SS}{CCC}{TRACT}.sol.gz`|Prefix for each solution files for each STATE|
|`$DAS_S3ROOT/2010-re/REIDENT/work/{ST}/{SS}{CCC}/synth_out_SSCCC.csv`|Prefix for synthetic data output|

Where:

|Abbrev|Meaning
|-----|-------|
|`{ST}`   | STUSAB  (2-character postal code)|
|`{SS}`   | STATE   (2-digit Census state code)|
|`{CCC}`  | COUNTY  (3-digit Census county code)|
|`{TRACT}`|TRACT (6-digit Census tract code)|


This is in line with [2010_stats/recon/README.md](https://github.ti.census.gov/CB-DAS/stats_2010/blob/master/recon/README.md) with `$ROOT` becoming `$DAS_S3ROOT/2010-re/REIDENT`.


All of the reconstruction programs should open files for reading and writing with sopen(), which should automatically work for both local files and s3 files.


Configuration
=============


Database Configuration
----------------
The database reconstruction is coordinated through a MySQL
database. The database contains tables for the 2010 geography and a
separate table `tracts_REIDENT` that keeps track of each reconstruction.

Database secrets (e.g. username, password, etc.) are stored in the
file `dbrecon_config_encrypted.json.ITE` which is decrypted with
$DAS_ROOT/bin/kms.py.



Tools for Database Reconstruction
================================

dbtool.py - manipulates the database reconstruction databases.



Open Issues
===========
Right now we engage in two file operations that do not work well on S3:
- Rename files.
- Incremental write (especially of compressed files)

Most of this is handled with the dbrecon `dopen()` facility, although some also uses the ctools.gzfile.

Since writing this code in 2018/2019, I've learned how to write compressed files directly to S3, but the knowledge of how to do that isn't embedded into these functions. So the fastest way to get going is:

1. Keep all of the source files in S3.
2. Build all of the state-and-county level files in S3.
3. Perform each tract reconstruction (building the LP files and solving them) in the local file system of a given instance.
4. Generate the microdata and save it back to S3.

However, this is super-gross, so I think that we're probably going to just fix everything to use S3 exclusively.

This will require modificaitons to the scheduler so that each tract can be assigned to a specific instance.

However, it's probably going to be easier to use each instance for a different state. It would be nice to break up CA and TX, though. So let's make it so the scheduler can run either for a specific state or a specific county
