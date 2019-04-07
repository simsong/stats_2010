#!/usr/bin/env python3
"""
Demo of accessing sf1 from spark.
Set up your files like this:

SF1_ROOT = location of SF1. 
   If you are running under spark on EMR, this should be a s3:// or hdfs://
   If you are running under spark stand-alone, this should be just a regular directory.

You can arrange the files any way that you want inside SF1. We scan the directory and find all the files.
"""

import os

from constants import *
import cb_spec_decoder
import ctools.cspark as cspark
import ctools.s3     as s3

debug = False

SF1_ROOT='SF1_ROOT'

class DecennialDF:
    def __init__(self,*,year,product):
        """Inventory the files and return an SF1 object."""
        try:
            self.root = os.environ[SF1_ROOT]
        except KeyError:
            raise RuntimeError("Environment variable SF1_ROOT must be defined with location of SF1 files")

        self.files = []
        self.find_files()
        ch6file = CHAPTER6_CSV_FILES.format(year=year,product=product)
        self.schema = cb_spec_decoder.schema_for_spec(ch6file)

    def find_files(self):
        if self.root.startswith('s3:'):
            for obj in s3.list_objects(self.root):
                self.register_file(obj[s3._Key])
        elif self.root.startswith('hdfs:'):
            raise RuntimeError('hdfs SF1_ROOT not implemented')
        else:
            for (dirpath,dirnames,filenames) in os.walk(self.root):
                for filename in filenames:
                    self.register_file(os.path.join(dirpath,filename))

    def register_file(self,path):
        """Files have a pattern:  {state}{section}{year}.{product}"""
        filename = os.path.basename(path)
        if filename.endswith(".sf1"):
            state = filename[0:2]
            try:
                if len(filename)==13 and filename[2:5]=='geo':
                    self.files.append({'path':path,
                                       STATE:state,
                                       CIFSN:CIFSN_GEO,
                                       YEAR:int(filename[5:9]),
                                       PRODUCT:SF1})
                if len(filename)==15:
                    self.files.append({'path':path,
                                       STATE:state,
                                       CIFSN:int(filename[2:7]),
                                       YEAR:int(filename[7:11]),
                                       PRODUCT:SF1})
            except ValueError as e:
                if debug:
                    print("bad filename:",path)
            
    def unique_selector(self,selector):
        """Return the unique values for a given selector"""
        return set( [obj[selector] for obj in self.files] )
    
    def get_df(self,*,tableName,sqlName):
        """Get a dataframe where the tables are specified by a selector. Things to try:
        year=2010  (currently required, but defaults to 2010)
        table=tabname (you must specify a table),
        product=product (you must specify a product)
        """
        # Get a list of all the matching files
        table = self.schema.get_table(tableName)
        if table==GEO_TABLE:
            cifsn = CIFSN_GEO
        else:
            cifsn = table.attrib[CIFSN]

        # Find the files
        paths = [ obj['path'] for obj in self.files if
                  (obj['year']==year and obj['product']==product) and obj[CIFSN]==cifsn]
        if len(paths)==0:
            print("No file found. Available data files:")
            for obj in self.files:
                print(obj)
            raise RuntimeError(f"No files found looking for year:{year} product:{product} CIFSN:{cifsn}")
            
        print("paths:\n","\n".join(paths))
        rdds = [spark.sparkContext.textFile(path) for path in paths]
        # rdd  = spark.sparkContext.union(rdds=rdds)
        # Just use the first for now
        print("rdds=",rdds)
        rdd = rdds[0]
        df   = spark.createDataFrame( rdd.map( table.parse_line_to_SparkSQLRow ), samplingRatio=1.0 )
        df.registerTempTable( sqlName )
        return df
            

if __name__=="__main__":
    import argparse

    spark  = cspark.spark_session()

    parser = argparse.ArgumentParser(description='Tool for using SF1 with Spark',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--list", help="List available files", action='store_true')
    args = parser.parse_args()

    year = 2010
    product = SF1
    sf1_2010 = DecennialDF(year=year,product=product)
    if args.list:
        print(f"Year: {year} product: {product}")
        print("Available files: ",len(s.files))
        print("Available states: "," ".join(s.unique_selector('state')))
        print("Available products: ", " ".join(s.unique_selector('product')))
        print("Available years: ", " ".join(s.unique_selector('year')))
        print("Available segments: ", " ".join([str(i) for i in s.unique_selector('segment')]))
        print("Available tables: "," ".join([t.name for t in schema.tables()]))


    # Demonstrate a simple count of the number of people
    print("Table P3 just has counts:")
    sf1_2010.get_df(tableName="P3", sqlName='P3_2010')
    spark.sql("SELECT * FROM P3_2010 LIMIT 10").show()


    print("Table P22 has decimal numbers:")
    sf1_2010.get_df(tableName="P22", sqlName='P22_2010')
    spark.sql("SELECT * FROM P22_2010 LIMIT 10").show()

    
    print("We have geographies!")
    sf1_2010.get_df(tableName = GEO_TABLE, sqlName='GEO_2010')
    spark.sql("SELECT FILEID,STUSAB,LOGRECNO,STATE,COUNTYCC,TRACT,BLKGRP,BLOCK,FROM GEO_2010 LIMIT 10").show()
