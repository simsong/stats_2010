Notes on Spark
==============
UI was at: https://ip-10-252-44-48.ite.ti.census.gov:4440


For making this run on Spark, we make lots of RDDs and combine them with the union operator.

Spark is complex to tune. We allow specifying the spark parameters:

--num_executors - We started with 50, but soon it increased the numbers:

21/03/31 19:13:41 INFO ExecutorMonitor: New executor 453 has registered (new total is 408)

Looks like it has determined it needs 1.3M tasks, and 196K have completed:

21/03/31 19:25:59 INFO TaskSetManager: Finished task 196258.0 in stage 1.0 (TID 196261) in 3289 ms on ip-10-252-46-204.ite.ti.census.gov (executor 231) (195842/1372624)

--executor_memory


spark.dynamicAllocation.executorIdleTimeout - to prevent timeouts?
