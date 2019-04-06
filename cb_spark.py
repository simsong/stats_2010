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
import sf1_doc_decoder
import ctools.cspark as cspark
import ctools.s3     as s3

debug = False

SF1_ROOT='SF1_ROOT'

class SF1:
    def __init__(self):
        """Inventory the files and return an SF1 object."""
        try:
            self.root = os.environ[SF1_ROOT]
        except KeyError:
            raise RuntimeError("Environment variable SF1_ROOT must be defined with location of SF1 files")

        self.files = []
        self.find_files()
        self.schema = sf1_doc_decoder.schema_for_sf1()

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
        if len(filename)==15 and filename[11]=='.':
            try:
                self.files.append({'path':path,
                                   'state':filename[0:2],
                                   'segment':int(filename[2:7]),
                                   'year':filename[7:11],
                                   'product':filename[13:16]})
            except ValueError as e:
                if debug:
                    print("bad file format:",path)
            
    def unique_selector(self,selector):
        """Return the unique values for a given selector"""
        return set( [obj[selector] for obj in self.files] )
    
    def get_df(self,*,year=2010,tableName,product=SF1,**kwargs):
        """Get a dataframe where the tables are specified by a selector. Things to try:
        year=2010  (currently required, but defaults to 2010)
        table=tabname (you must specify a table),
        product=product (you must specify a product)
        """
        # Get a list of all the matching files
        table = self.schema.get_table(table)
        paths = [ obj['path'] for obj in self.files where 
                  obj['year']==year and obj['table']==tableName obj['product']==product]
        rdds = [spark.sparkContext.textFile(path) for path in paths]
        rdd  = spark.sparkContext.union(*rdds)
        df   = spark.createDataFrame( rdd.map( table.parse_line_to_SparkSQLRow ), samplingRatio=1.0 )
        df.registerTempTable( f"{tableName}_{year}" )
        return df
            

if __name__=="__main__":
    import argparse

    # spark = spark_session()

    parser = argparse.ArgumentParser(description='Tool for using SF1 with Spark',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--list", help="List available files", action='store_true')
    args = parser.parse_args()

    s = SF1()
    if args.list:
        print("Available files: ",len(s.files))
        print("Available states: "," ".join(s.unique_selector('state')))
        print("Available products: ", " ".join(s.unique_selector('product')))
        print("Available years: ", " ".join(s.unique_selector('year')))
        print("Available segments: ", " ".join([str(i) for i in s.unique_selector('segment')]))
        print("Available tables: "," ".join([t.name for t in schema.tables()]))

    # Demonstrate a simple count of the number of people
    df = s.get_df(year=2010, product=SF1, table="P22")
    spark.sql("SELECT * FROM P22 LIMIT 10").show()
    
