# Run a DAS job with:
# [output=outputfile] bash run_stats_2010_cluster.sh
#
# This uses all resources

echo Running DAS on `date` $config

#zip the code
ZIPFILE=../stats_2010.zip
export ZIPFILE
zip -r -q $ZIPFILE . -i '*.py' '*.sh' '*.ini'

CONFIG_DIR=configs
DEFAULT_CONFIG=test_RA_config_cluster.ini

DEFAULT_OUTPUT=das_output.out

#output=$1
if [ x$output = x ]; then
  output="$DEFAULT_OUTPUT"
fi

export TERM=xterm

## This program runs the DAS framework driver with the config file specified.
echo starting at `date`
echo $PWD

export PATH=$PATH:$PWD

echo PID $$ starting at `date`

nohup 2>&1 spark-submit --py-files $ZIPFILE --driver-memory 5g --num-executors 360 --executor-memory 5g --executor-cores 4 --driver-cores 10  --conf spark.driver.maxResultSize=0g --conf spark.executor.memoryOverhead=5g --conf spark.local.dir="/mnt/tmp/" --conf spark.eventLog.enabled=true --conf spark.eventLog.dir="/mnt/tmp/logs/" --master yarn --conf spark.submit.deployMode=client --conf spark.network.timeout=3000 cb_spark_demo.py &> $output &

echo PID $$ done at `date`
