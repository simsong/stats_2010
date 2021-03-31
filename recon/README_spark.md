Notes on Spark
==============

For making this run on Spark, we make lots of RDDs and combine them with the union operator.
This allows each to be evaluated separately.
```
In [25]: a=sc.parallelize(range(0,10))

In [26]: b=sc.parallelize(range(100,110))

In [27]: c=sc.parallelize(range(200,210))

In [28]: sc.union([a,b,c]).collect()
Out[28]:
[0,
 1,
 2,
 3,
 4,
 5,
 6,
 7,
 8,
 9,
 100,
 101,
 102,
 103,
 104,
 105,
 106,
 107,
 108,
 109,
 200,
 201,
 202,
 203,
 204,
 205,
 206,
 207,
 208,
 209]

In [29]:
```
