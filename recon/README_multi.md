This directory contains tools for running the database reconstruction software on the DAS EMR clusters.

(Note that the stats_2010 carries its own copies of ctools, dfxml and census_etl. Don't try to make it use what's in das-vm-config, as the stats_2010 package needs to exist without das-vm-config.)

AWS EMR monitors the free memory on every instance and kills the instance if it runs out of memory. This works great under Spark, which simply starts a new cluster. It's lousy here. And if the MASTER or one of the 2 CORE nodes dies, the cluster becomes unstable and the entire cluster gets killed. So in general, we try to do all of the heavy-living on TASK nodes, because we can kill all of the task nodes and not damage the cluster.

You can control the cluster size with the ./dbrtool.py --resize command. It will only resize the TASK nodes:

```
urial-ITE-MASTER:hadoop@/mnt/users/garfi303/recon $ ./dbrtool.py --clus
CORE: ip-10-252-44-156.ite.ti.census.gov 4 days, 1:32, 0 users, load average: 0.00, 0.01, 0.00
CORE: ip-10-252-47-50.ite.ti.census.gov 14 days, 5:07, 0 users, load average: 0.02, 0.02, 0.00
urial-ITE-MASTER:hadoop@/mnt/users/garfi303/recon $ ./dbrtool.py --resize 10
Resize cluster to 10 nodes?yes
clusterId: j-2KI6WGJLYONB9
DASTaskInstanceGroup  requested: 10  running: 0
DASEMRDriverGroup  requested: 1  running: 1
DASEMRCoreGroup  requested: 2  running: 2
RESIZING
urial-ITE-MASTER:hadoop@/mnt/users/garfi303/recon $
```


There are two-workflows for using EMR clusters.

1. Each instance in the cluster is runs its own independent copy of scheduler and they coordinate through the database. This is the method that the original reconstruction was done, and it works, but it may be less efficient.)

2. The entire reconstruction is run through Spark. This shoudl give better overall utilization, and restart when there are crashes, but we don't have it working properly yet.

This file discusses workflow #1, each cluster running stand-alone. The Spark workflow is described in the file README_spark.md.


Sharding
========
The Database reconstruction package uses the MySQL database to keep track of the progress of the reconstruction. In the original reconstruction, there was only one reconstruction per database. In this version, a single database can hold multiple reconstructions. Each one has a unique reconstruction experiment identifier, called a REIDENT. The geography is stored in a table called {reident}_geo, the tracts are stored in a table called {reident}_tracts.

Each 2010 reconstruction experiment is given a unique RE identifier,
here called `REIDENT`.

1. SF1s are received and stored under the prefix `$DAS_S3ROOT/2010-re/REIDENT/zips/`

2. The RE identifier is registered using the dbtool.py program:

```
dbrtool.py --register REIDENT
```

Because the s used as the database prefix, must therefore begin with a
letter and contain only letters, numbers, and underbars.

All of the database reconstruction tools in stats_2010/recon have been modified so that they read REIDENT from the Unix environment and then use this as a prefix on every SQL table.

Database registration creates and initializes the `REIDENT_tracts`
table from original `tracts` table.

  - (step0 - downloads from the WWW server. This only needs to be done once, and doesn't need to be run in our EMR environment. In fact, this command doesn't work in the EMR environment.)

These can be run on either the DRIVER or a single WORKER node:

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


Examples
=========

Status all nodes:
-------------

```
urial-ITE-MASTER:hadoop@/mnt/users/garfi303/recon $ ./dbrtool.py --cluster
CORE: ip-10-252-44-156.ite.ti.census.gov 2 days, 19:09, 0 users, load average: 0.00, 0.00, 0.00
CORE: ip-10-252-47-50.ite.ti.census.gov 12 days, 22:43, 0 users, load average: 0.14, 0.07, 0.06
idle: ip-10-252-44-147.ite.ti.census.gov 1 day, 15:36, 0 users, load average: 0.08, 0.06, 0.01
idle: ip-10-252-44-170.ite.ti.census.gov 1 day, 15:36, 0 users, load average: 0.00, 0.03, 0.02
idle: ip-10-252-44-197.ite.ti.census.gov 1 day, 15:36, 0 users, load average: 0.01, 0.05, 0.02
idle: ip-10-252-44-59.ite.ti.census.gov 1 day, 15:36, 1 user, load average: 0.27, 0.15, 0.07
idle: ip-10-252-45-106.ite.ti.census.gov 1 day, 15:36, 0 users, load average: 0.00, 0.00, 0.00
idle: ip-10-252-45-143.ite.ti.census.gov 1 day, 15:36, 0 users, load average: 0.00, 0.02, 0.05
idle: ip-10-252-45-235.ite.ti.census.gov 1 day, 15:36, 0 users, load average: 0.00, 0.00, 0.00
idle: ip-10-252-47-12.ite.ti.census.gov 1 day, 15:36, 0 users, load average: 0.02, 0.01, 0.00
idle: ip-10-252-47-202.ite.ti.census.gov 1 day, 15:36, 0 users, load average: 0.00, 0.00, 0.01
in use: ip-10-252-45-251.ite.ti.census.gov 1 day, 15:36, 4 users, load average: 0.07, 0.10, 0.03
```

Launch on all available nodes:
--------------------------------

```
urial-ITE-MASTER:hadoop@/mnt/users/garfi303/recon $ ./dbrtool.py --launch_all --reident orig
Launch:  ip-10-252-44-197.ite.ti.census.gov
Launch:  ip-10-252-44-170.ite.ti.census.gov
Launch:  ip-10-252-47-12.ite.ti.census.gov
Launch:  ip-10-252-45-106.ite.ti.census.gov
Launch:  ip-10-252-45-235.ite.ti.census.gov
Launch:  ip-10-252-44-147.ite.ti.census.gov
Launch:  ip-10-252-47-202.ite.ti.census.gov
Launch:  ip-10-252-44-59.ite.ti.census.gov
Launch:  ip-10-252-45-143.ite.ti.census.gov
urial-ITE-MASTER:hadoop@/mnt/users/garfi303/recon $
```

This:
1. Logs into the idle nodes.
2. Does a new checkout of `stats_2010`
3. Runs scheduler.py for `--reident orig` and `--step3` and `--step4`, which kills any running stragglers.

Add `--force` to go after all nodes.


After a few minutes, you should see this:
```
urial-ITE-MASTER:hadoop@/mnt/users/garfi303/recon $ ./dbrtool.py --cluster
CORE: ip-10-252-44-156.ite.ti.census.gov 2 days, 19:22, 0 users, load average: 0.01, 0.04, 0.01
CORE: ip-10-252-47-50.ite.ti.census.gov 12 days, 22:56, 0 users, load average: 0.00, 0.00, 0.00
in use: ip-10-252-44-147.ite.ti.census.gov 1 day, 15:49, 0 users, load average: 50.89, 50.28, 29.26
in use: ip-10-252-44-170.ite.ti.census.gov 1 day, 15:49, 0 users, load average: 51.79, 48.62, 28.14
in use: ip-10-252-44-197.ite.ti.census.gov 1 day, 15:49, 0 users, load average: 57.27, 52.17, 30.20
in use: ip-10-252-44-59.ite.ti.census.gov 1 day, 15:49, 1 user, load average: 52.77, 50.11, 29.08
in use: ip-10-252-45-106.ite.ti.census.gov 1 day, 15:49, 0 users, load average: 49.90, 48.73, 28.50
in use: ip-10-252-45-143.ite.ti.census.gov 1 day, 15:49, 0 users, load average: 57.96, 50.30, 29.10
in use: ip-10-252-45-235.ite.ti.census.gov 1 day, 15:49, 0 users, load average: 51.72, 49.80, 29.09
in use: ip-10-252-45-251.ite.ti.census.gov 1 day, 15:49, 4 users, load average: 0.00, 0.01, 0.00
in use: ip-10-252-47-12.ite.ti.census.gov 1 day, 15:49, 0 users, load average: 49.76, 49.12, 28.67
in use: ip-10-252-47-202.ite.ti.census.gov 1 day, 15:49, 0 users, load average: 54.14, 49.67, 28.95
```



Monitoring
==========

To get a quick check of the cluster status, use:

```
./drbtool.py --cluster
```

To see what still needs to be done, try:
```
./drbtool.py --status --reident s005080090050030'
```

You can combine these with `watch`, like this:

```
watch './dbrtool.py --cluster;./dbrtool.py --status --reident s005080090050030'
```

Diagnosing crashes
==================
Eventaully the schedulers die:

```
Every 2.0s: ./dbrtool.py --cluster ; ./dbrtool.py --status --reident s005080090050030                                        Wed Apr  7 19:51:29 2021

CORE: ip-10-252-44-156.ite.ti.census.gov 4 days, 5:35, 0 users, load average: 0.01, 0.04, 0.04
CORE: ip-10-252-47-50.ite.ti.census.gov 14 days, 9:09, 0 users, load average: 0.12, 0.11, 0.04
idle: ip-10-252-46-199.ite.ti.census.gov 4:01, 0 users, load average: 0.06, 0.08, 0.15
idle: ip-10-252-47-191.ite.ti.census.gov 4:01, 0 users, load average: 0.00, 0.00, 0.00
Current Time
   now(): 2021-04-07 19:51:32
----------------------
Completed States:
----------------------
Files created and remaining
   lp_created: 72368
   lp_remaining: 163
   lp_in_process: 0
   lp_hostlocked: 0
   sol_created: 72124
   sol_remaining: 407
   sol_ready: 244
   csv_completed: 0
   csv_remaining: 72531

----------------------
LP files in progress
----------------------
SOLs in progress
----------------------
Number of LP files created in past hour:
----------------------
Number of SOL files created in past hour:
----------------------

```

If you launched with `--launch` or `--launch_all`, you can log into the machine and look for the 'output*' directory:
```
urial-ITE-MASTER:hadoop@/mnt/users/garfi303/recon $ ssh hadoop@10.252.46.199
...
CORE:hadoop@ip-10-252-46-199$ ls -l
total 4
drwxr-xr-x 25 hadoop hadoop 4096 Apr  7 16:52 das-vm-config
lrwxrwxrwx  1 hadoop hadoop   38 Apr  7 16:52 recon -> das-vm-config/dbrecon/stats_2010/recon
CORE:hadoop@ip-10-252-46-199$ pwd
/home/hadoop
CORE:hadoop@ip-10-252-46-199$ cd recon/
CORE:hadoop@ip-10-252-46-199$ ls -alt
total 436
-rw-r--r--  1 hadoop hadoop 27497 Apr  7 19:28 output-2021-04-07T19:28:19-0400
drwxr-xr-x  2 hadoop hadoop  8192 Apr  7 19:28 logs
drwxr-xr-x  7 hadoop hadoop  4096 Apr  7 19:28 .
-rw-r--r--  1 hadoop hadoop  7576 Apr  7 19:28 s1_make_geo_files.py
-rw-r--r--  1 hadoop hadoop 27442 Apr  7 16:56 output-2021-04-07T16:55:31-0400
drwxr-xr-x  2 hadoop hadoop    83 Apr  7 16:55 __pycache__
-rw-r--r--  1 hadoop hadoop 41632 Apr  7 16:55 dbrecon.py
-rwxr-xr-x  1 hadoop hadoop 29880 Apr  7 16:55 dbrtool.py
-rw-r--r--  1 hadoop hadoop   103 Apr  7 16:55 .gitignore
...
```
Look at the top file to try to figure out what happened. In this case, it is becasue there was a bug in s4_run_gurobi.py:
```
2021-04-07 19:28:21,378 dbrecon.py:806 (log_error) PID40493: DBMySQL.csfr called with auth=fl
Traceback (most recent call last):
  File "s4_run_gurobi.py", line 319, in <module>
    run_gurobi_for_county(stusab, county, tracts)
  File "s4_run_gurobi.py", line 283, in run_gurobi_for_county
    dbrecon.db_lock(stusab, county, tract)
  File "/mnt/home/hadoop/das-vm-config/dbrecon/stats_2010/recon/dbrecon.py", line 308, in db_lock
    DBMySQL.csfr(auth, cmd, args)
  File "/mnt/home/hadoop/das-vm-config/dbrecon/stats_2010/recon/ctools/dbfile.py", line 413, in csfr
    raise ValueError(f"DBMySQL.csfr called with auth={auth}")
ValueError: DBMySQL.csfr called with auth=fl
2021-04-07 19:28:22,370 dbrecon.py:811 (logging_exit) PID40676: DBMySQL.csfr called with auth=fl
2021-04-07 19:28:22,371 dbrecon.py:812 (logging_exit) ['s4_run_gurobi.py', '--exit1', '--j1', '1', '--j2', '32', 'fl', '103', '026500']
/usr/local/lib/python3.6/site-packages/pymysql/cursors.py:170: Warning: (1265, "Data truncated for column 'file' at row 1")
  result = self._query(query)
```


TODO
====
One of the fundamental mistakes in this project was to use the `datetime` filed in the MySQL database rather than storing Unix timestamps.
That's because datetime does not include timezone information. It turns out that dbrecon.csfr had this code:

```
L291:
        self.dbs.cursor().execute('SET @@session.time_zone = "+00:00"') # UTC please
```

and dbfile.py had this code:

```
L374:
        # Census standard TZ is America/New_York
        try:
            self.cursor().execute('SET @@session.time_zone = "America/New_York"')
        except self.internalError as e:
            pass
```

It's also a problem that the internal errors were simply ignored.
THis is just bad, sloppy programming all around. We should have stored everything as a time_t.

Fortunately, lp_end and sol_end are basically used as booleans, and
all of the code is being rewritten to use dbfile exclusively. However,
this shouldn't be allowed to continue, and it shouldn't be allowed for future projects.
