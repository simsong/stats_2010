Outstanding Errors
^^^^^^^^^^^^^
2021-03-25 23:16:36,846 s4_run_gurobi.py:223 (run_gurobi_for_county_tract) LP file not found for ny085020100; rescan_files 2
Traceback (most recent call last):
  File "/mnt/users/garfi303/das-vm-config/dbrecon/stats_2010/recon/dbrecon.py", line 921, in dgetsize
    return boto3.resource('s3').Object(bucket,key).content_length
  File "/usr/local/lib/python3.7/site-packages/boto3/resources/factory.py", line 339, in property_loader
    self.load()
  File "/usr/local/lib/python3.7/site-packages/boto3/resources/factory.py", line 505, in do_action
    response = action(self, *args, **kwargs)
  File "/usr/local/lib/python3.7/site-packages/boto3/resources/action.py", line 83, in __call__
    response = getattr(parent.meta.client, operation_name)(*args, **params)
  File "/usr/local/lib/python3.7/site-packages/botocore/client.py", line 357, in _api_call
    return self._make_api_call(operation_name, kwargs)
  File "/usr/local/lib/python3.7/site-packages/botocore/client.py", line 676, in _make_api_call
    raise error_class(parsed_response, operation_name)
botocore.exceptions.ClientError: An error occurred (404) when calling the HeadObject operation: Not Found

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "s4_run_gurobi.py", line 218, in run_gurobi_for_county_tract
    run_gurobi(stusab, county, tract, lpgz_filename, args.dry_run)
  File "s4_run_gurobi.py", line 83, in run_gurobi
    logging.warning("File {} exists. Removing.".format(fn,dbrecon.dgetsize(fn)))
  File "/mnt/users/garfi303/das-vm-config/dbrecon/stats_2010/recon/dbrecon.py", line 924, in dgetsize
    raise FileNotFoundError(path) from err
FileNotFoundError: s3://uscb-decennial-ite-das/2010-re/orig/work/ny/36085/sol/model_36085020100.sol

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "s4_run_gurobi.py", line 312, in <module>
    run_gurobi_for_county(stusab, county, tracts)
  File "s4_run_gurobi.py", line 281, in run_gurobi_for_county
    run_gurobi_tuple(tt)
  File "s4_run_gurobi.py", line 253, in run_gurobi_tuple
    run_gurobi_for_county_tract(tt[0], tt[1], tt[2])
  File "s4_run_gurobi.py", line 224, in run_gurobi_for_county_tract
    dbrecon.rescan_files(stusab, county,tract)
  File "/mnt/users/garfi303/das-vm-config/dbrecon/stats_2010/recon/dbrecon.py", line 370, in rescan_files
    raise RuntimeError("don't do at the moment. The database is more accurate than the file system.")
RuntimeError: don't do at the moment. The database is more accurate than the file system.
2021-03-25 23:16:36,989 dbrecon.py:746 (logging_exit) PID74181: don't do at the moment. The database is more accurate than the file system.
/usr/local/lib/python3.7/site-packages/pymysql/cursors.py:170: Warning: (1265, "Data truncated for column 'file' at row 1")
  result = self._query(query)
LOG ERROR: PID74181: don't do at the moment. The database is more accurate than the file system.
