Outstanding Errors
^^^^^^^^^^^^^
```
2021-03-25 21:21:46,669 scheduler.py:267 (run) %%%
2021-03-25 21:21:46,669 scheduler.py:268 (run) %%% Free memory down to 3,513,581,568 -- will start killing processes.
2021-03-25 21:21:46,669 scheduler.py:269 (run) %%%
Traceback (most recent call last):
  File "scheduler.py", line 476, in <module>
    run()
  File "scheduler.py", line 270, in run
    subprocess.call(['./pps'])
  File "/usr/lib64/python3.7/subprocess.py", line 339, in call
    with Popen(*popenargs, **kwargs) as p:
  File "/usr/lib64/python3.7/subprocess.py", line 800, in __init__
    restore_signals, start_new_session)
  File "/usr/lib64/python3.7/subprocess.py", line 1551, in _execute_child
    raise child_exception_type(errno_num, err_msg, err_filename)
FileNotFoundError: [Errno 2] No such file or directory: './pps': './pps'
2021-03-25 21:21:46,704 dbrecon.py:746 (logging_exit) PID59386: [Errno 2] No such file or directory: './pps': './pps'
PID65963: cmd:
                UPDATE orig_tracts set hostlock=NULL,lp_start=NULL,lp_end=NULL
                WHERE stusab=%s and county=%s and tract=%s"
                 vals:('ks', '145', '970200')
2021-03-25 21:21:53,306 dbrecon.py:233 (csfr)  cmd:
                UPDATE orig_tracts set hostlock=NULL,lp_start=NULL,lp_end=NULL
                WHERE stusab=%s and county=%s and tract=%s"

2021-03-25 21:21:53,306 dbrecon.py:234 (csfr) vals: ('ks', '145', '970200')
2021-03-25 21:21:53,306 dbrecon.py:235 (csfr) (1064, 'You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near \'"\' at line 2')
/usr/local/lib/python3.7/site-packages/pymysql/cursors.py:170: Warning: (1265, "Data truncated for column 'file' at row 1")
  result = self._query(query)
LOG ERROR: PID59386: [Errno 2] No such file or directory: './pps': './pps'
PID68565: cmd:
                UPDATE orig_tracts set hostlock=NULL,lp_start=NULL,lp_end=NULL
                WHERE stusab=%s and county=%s and tract=%s"
                 vals:('oh', '167', '021300')
2021-03-25 21:21:55,816 dbrecon.py:233 (csfr)  cmd:
                UPDATE orig_tracts set hostlock=NULL,lp_start=NULL,lp_end=NULL
                WHERE stusab=%s and county=%s and tract=%s"

2021-03-25 21:21:55,817 dbrecon.py:234 (csfr) vals: ('oh', '167', '021300')
2021-03-25 21:21:55,817 dbrecon.py:235 (csfr) (1064, 'You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near \'"\' at line 2')
Traceback (most recent call last):
  File "./dbrtool.py", line 383, in <module>
    run(cmd)
  File "./dbrtool.py", line 215, in run
    subprocess.run(cmd, cwd=RECON_DIR, check=True)
  File "/usr/lib64/python3.7/subprocess.py", line 512, in run
    output=stdout, stderr=stderr)
subprocess.CalledProcessError: Command '['/usr/bin/python3', 'scheduler.py', '--stusab', 'all']' returned non-zero exit status 1.
./dbrtool.py --step1 --reident orig --run  1659.62s user 192.29s system 283% cpu 10:53.10 total
-ITE-MASTER:hadoop@/mnt/users/garfi303/das-vm-config/dbrecon/stats_2010/recon $ PID71425: cmd:UPDATE orig_tracts set lp_end=now(),lp_host=%s,hostlock=NULL,pid=NULL where stusab=%s and county=%s and tract=%s vals:('ip-10-252-46-201', 'mo', '219', '820201')

...
PID65964: cmd:UPDATE orig_tracts set lp_end=now(),lp_host=%s,hostlock=NULL,pid=NULL where stusab=%s and county=%s and tract=%s vals:('ip-10-252-46-201', 'ks', '145', '970300')
PID65964: cmd:UPDATE orig_tracts set lp_gb=%s,hostlock=NULL where stusab=%s and county=%s and tract=%s vals:(68, 'ks', '145', '970300')
multiprocessing.pool.RemoteTraceback:
"""
Traceback (most recent call last):
  File "s3_pandas_synth_lp_files.py", line 486, in build_tract_lp_tuple
    lptb.build_tract_lp()
  File "s3_pandas_synth_lp_files.py", line 423, in build_tract_lp
    n_con = update_constraints(f, 'block', n_con, block_summary_nums,geo_id)
  File "s3_pandas_synth_lp_files.py", line 146, in update_constraints
    make_attributes_categories(con_frame)
  File "s3_pandas_synth_lp_files.py", line 93, in make_attributes_categories
    df[a] = df[a].astype('category')
  File "/usr/local/lib64/python3.7/site-packages/pandas/core/frame.py", line 3163, in __setitem__
    self._set_item(key, value)
  File "/usr/local/lib64/python3.7/site-packages/pandas/core/frame.py", line 3240, in _set_item
    NDFrame._set_item(self, key, value)
  File "/usr/local/lib64/python3.7/site-packages/pandas/core/generic.py", line 3829, in _set_item
    NDFrame._iset_item(self, loc, value)
  File "/usr/local/lib64/python3.7/site-packages/pandas/core/generic.py", line 3818, in _iset_item
    self._mgr.iset(loc, value)
  File "/usr/local/lib64/python3.7/site-packages/pandas/core/internals/managers.py", line 1119, in iset
    blk.delete(blk_locs)
  File "/usr/local/lib64/python3.7/site-packages/pandas/core/internals/blocks.py", line 369, in delete
    self.values = np.delete(self.values, loc, 0)
  File "<__array_function__ internals>", line 6, in delete
  File "/mnt/das_python/numpy/lib/function_base.py", line 4409, in delete
    new = arr[tuple(slobj)]
MemoryError: Unable to allocate 8.54 GiB for an array with shape (10, 114622772) and data type object

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/lib64/python3.7/multiprocessing/pool.py", line 121, in worker
    result = (True, func(*args, **kwds))
  File "/usr/lib64/python3.7/multiprocessing/pool.py", line 44, in mapstar
    return list(map(*args))
  File "s3_pandas_synth_lp_files.py", line 494, in build_tract_lp_tuple
    (stusab, county, tract))
  File "/mnt/users/garfi303/das-vm-config/dbrecon/stats_2010/recon/dbrecon.py", line 236, in csfr
    raise e
  File "/mnt/users/garfi303/das-vm-config/dbrecon/stats_2010/recon/dbrecon.py", line 229, in csfr
    c.execute(cmd,vals)
  File "/usr/local/lib/python3.7/site-packages/pymysql/cursors.py", line 170, in execute
    result = self._query(query)
  File "/usr/local/lib/python3.7/site-packages/pymysql/cursors.py", line 328, in _query
    conn.query(q)
  File "/usr/local/lib/python3.7/site-packages/pymysql/connections.py", line 517, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
  File "/usr/local/lib/python3.7/site-packages/pymysql/connections.py", line 732, in _read_query_result
    result.read()
  File "/usr/local/lib/python3.7/site-packages/pymysql/connections.py", line 1075, in read
    first_packet = self.connection._read_packet()
  File "/usr/local/lib/python3.7/site-packages/pymysql/connections.py", line 684, in _read_packet
    packet.check_error()
  File "/usr/local/lib/python3.7/site-packages/pymysql/protocol.py", line 220, in check_error
    err.raise_mysql_exception(self._data)
  File "/usr/local/lib/python3.7/site-packages/pymysql/err.py", line 109, in raise_mysql_exception
    raise errorclass(errno, errval)
pymysql.err.ProgrammingError: (1064, 'You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near \'"\' at line 2')
```
The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "s3_pandas_synth_lp_files.py", line 744, in <module>
    make_state_county_files(args.state, args.county)
  File "s3_pandas_synth_lp_files.py", line 694, in make_state_county_files
    p.map(build_tract_lp_tuple, tracttuples)
  File "/usr/lib64/python3.7/multiprocessing/pool.py", line 268, in map
    return self._map_async(func, iterable, mapstar, chunksize).get()
  File "/usr/lib64/python3.7/multiprocessing/pool.py", line 657, in get
    raise self._value
pymysql.err.ProgrammingError: (1064, 'You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near \'"\' at line 2')
2021-03-25 21:28:01,737 dbrecon.py:746 (logging_exit) PID65048: (1064, 'You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near \'"\' at line 2')
/usr/local/lib/python3.7/site-packages/pymysql/cursors.py:170: Warning: (1265, "Data truncated for column 'file' at row 1")
  result = self._query(query)
LOG ERROR: PID65048: (1064, 'You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near \'"\' at line 2')
PID64785: cmd:UPDATE orig_tracts set lp_end=now(),lp_host=%s,hostlock=NULL,pid=NULL where stusab=%s and county=%s and tract=%s vals:('ip-10-252-46-201', 'ar', '091', '020900')
PID64785: cmd:UPDATE orig_tracts set lp_gb=%s,hostlock=NULL where stusab=%s and county=%s and tract=%s vals:(56, 'ar', '091', '020900')
PID68559: cmd:UPDATE orig_tracts set lp_end=now(),lp_host=%s,hostlock=NULL,pid=NULL where stusab=%s and county=%s and tract=%s vals:('ip-10-252-46-201', 'oh', '167', '021200')
PID68559: cmd:UPDATE orig_tracts set lp_gb=%s,hostlock=NULL where stusab=%s and county=%s and tract=%s vals:(50, 'oh', '167', '021200')
PID71422: cmd:UPDATE orig_tracts set lp_end=now(),lp_host=%s,hostlock=NULL,pid=NULL where stusab=%s and county=%s and tract=%s vals:('ip-10-252-46-201', 'mo', '219', '820103')
PID71422: cmd:UPDATE orig_tracts set lp_gb=%s,hostlock=NULL where stusab=%s and county=%s and tract=%s vals:(40, 'mo', '219', '820103')
PID71417: cmd:UPDATE orig_tracts set lp_end=now(),lp_host=%s,hostlock=NULL,pid=NULL where stusab=%s and county=%s and tract=%s vals:('ip-10-252-46-201', 'mo', '219', '820101')
PID71417: cmd:UPDATE orig_tracts set lp_gb=%s,hostlock=NULL where stusab=%s and county=%s and tract=%s vals:(35, 'mo', '219', '820101')
multiprocessing.pool.RemoteTraceback:
"""
Traceback (most recent call last):
  File "s3_pandas_synth_lp_files.py", line 486, in build_tract_lp_tuple
    lptb.build_tract_lp()
  File "s3_pandas_synth_lp_files.py", line 423, in build_tract_lp
    n_con = update_constraints(f, 'block', n_con, block_summary_nums,geo_id)
  File "s3_pandas_synth_lp_files.py", line 146, in update_constraints
    make_attributes_categories(con_frame)
  File "s3_pandas_synth_lp_files.py", line 93, in make_attributes_categories
    df[a] = df[a].astype('category')
  File "/usr/local/lib64/python3.7/site-packages/pandas/core/frame.py", line 3163, in __setitem__
    self._set_item(key, value)
  File "/usr/local/lib64/python3.7/site-packages/pandas/core/frame.py", line 3240, in _set_item
    NDFrame._set_item(self, key, value)
  File "/usr/local/lib64/python3.7/site-packages/pandas/core/generic.py", line 3829, in _set_item
    NDFrame._iset_item(self, loc, value)
  File "/usr/local/lib64/python3.7/site-packages/pandas/core/generic.py", line 3818, in _iset_item
    self._mgr.iset(loc, value)
  File "/usr/local/lib64/python3.7/site-packages/pandas/core/internals/managers.py", line 1119, in iset
    blk.delete(blk_locs)
  File "/usr/local/lib64/python3.7/site-packages/pandas/core/internals/blocks.py", line 369, in delete
    self.values = np.delete(self.values, loc, 0)
  File "<__array_function__ internals>", line 6, in delete
  File "/mnt/das_python/numpy/lib/function_base.py", line 4409, in delete
    new = arr[tuple(slobj)]
MemoryError: Unable to allocate 6.28 GiB for an array with shape (10, 84281450) and data type object

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/lib64/python3.7/multiprocessing/pool.py", line 121, in worker
    result = (True, func(*args, **kwds))
  File "/usr/lib64/python3.7/multiprocessing/pool.py", line 44, in mapstar
    return list(map(*args))
  File "s3_pandas_synth_lp_files.py", line 494, in build_tract_lp_tuple
    (stusab, county, tract))
  File "/mnt/users/garfi303/das-vm-config/dbrecon/stats_2010/recon/dbrecon.py", line 236, in csfr
    raise e
  File "/mnt/users/garfi303/das-vm-config/dbrecon/stats_2010/recon/dbrecon.py", line 229, in csfr
    c.execute(cmd,vals)
  File "/usr/local/lib/python3.7/site-packages/pymysql/cursors.py", line 170, in execute
    result = self._query(query)
  File "/usr/local/lib/python3.7/site-packages/pymysql/cursors.py", line 328, in _query
    conn.query(q)
  File "/usr/local/lib/python3.7/site-packages/pymysql/connections.py", line 517, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
  File "/usr/local/lib/python3.7/site-packages/pymysql/connections.py", line 732, in _read_query_result
    result.read()
  File "/usr/local/lib/python3.7/site-packages/pymysql/connections.py", line 1075, in read
    first_packet = self.connection._read_packet()
  File "/usr/local/lib/python3.7/site-packages/pymysql/connections.py", line 684, in _read_packet
    packet.check_error()
  File "/usr/local/lib/python3.7/site-packages/pymysql/protocol.py", line 220, in check_error
    err.raise_mysql_exception(self._data)
  File "/usr/local/lib/python3.7/site-packages/pymysql/err.py", line 109, in raise_mysql_exception
    raise errorclass(errno, errval)
pymysql.err.ProgrammingError: (1064, 'You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near \'"\' at line 2')
"""

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "s3_pandas_synth_lp_files.py", line 744, in <module>
    make_state_county_files(args.state, args.county)
  File "s3_pandas_synth_lp_files.py", line 694, in make_state_county_files
    p.map(build_tract_lp_tuple, tracttuples)
  File "/usr/lib64/python3.7/multiprocessing/pool.py", line 268, in map
    return self._map_async(func, iterable, mapstar, chunksize).get()
  File "/usr/lib64/python3.7/multiprocessing/pool.py", line 657, in get
    raise self._value
pymysql.err.ProgrammingError: (1064, 'You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near \'"\' at line 2')
2021-03-25 21:28:47,077 dbrecon.py:746 (logging_exit) PID66677: (1064, 'You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near \'"\' at line 2')
/usr/local/lib/python3.7/site-packages/pymysql/cursors.py:170: Warning: (1265, "Data truncated for column 'file' at row 1")
  result = self._query(query)
LOG ERROR: PID66677: (1064, 'You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near \'"\' at line 2')
PID71419: cmd:UPDATE orig_tracts set lp_end=now(),lp_host=%s,hostlock=NULL,pid=NULL where stusab=%s and county=%s and tract=%s vals:('ip-10-252-46-201', 'mo', '219', '820102')
PID71419: cmd:UPDATE orig_tracts set lp_gb=%s,hostlock=NULL where stusab=%s and county=%s and tract=%s vals:(42, 'mo', '219', '820102')
PID73890: cmd:UPDATE orig_tracts set lp_end=now(),lp_host=%s,hostlock=NULL,pid=NULL where stusab=%s and county=%s and tract=%s vals:('ip-10-252-46-201', 'mo', '107', '090100')
PID73890: cmd:UPDATE orig_tracts set lp_gb=%s,hostlock=NULL where stusab=%s and county=%s and tract=%s vals:(50, 'mo', '107', '090100')
PID71426: cmd:UPDATE orig_tracts set lp_end=now(),lp_host=%s,hostlock=NULL,pid=NULL where stusab=%s and county=%s and tract=%s vals:('ip-10-252-46-201', 'mo', '219', '820202')
PID71426: cmd:UPDATE orig_tracts set lp_gb=%s,hostlock=NULL where stusab=%s and county=%s and tract=%s vals:(55, 'mo', '219', '820202')
PID73894: cmd:UPDATE orig_tracts set lp_end=now(),lp_host=%s,hostlock=NULL,pid=NULL where stusab=%s and county=%s and tract=%s vals:('ip-10-252-46-201', 'mo', '107', '090200')
PID73894: cmd:UPDATE orig_tracts set lp_gb=%s,hostlock=NULL where stusab=%s and county=%s and tract=%s vals:(54, 'mo', '107', '090200')
PID73899: cmd:UPDATE orig_tracts set lp_end=now(),lp_host=%s,hostlock=NULL,pid=NULL where stusab=%s and county=%s and tract=%s vals:('ip-10-252-46-201', 'mo', '107', '090400')
PID73899: cmd:UPDATE orig_tracts set lp_gb=%s,hostlock=NULL where stusab=%s and county=%s and tract=%s vals:(76, 'mo', '107', '090400')



```
