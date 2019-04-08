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
import sys

from constants import *
import cb_spec_decoder
import ctools.cspark as cspark
import ctools.s3     as s3
import ctools.tydoc  as tydoc

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

    def get_table(self,tableName):
        return self.schema.get_table(tableName)

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
        if tableName == GEO_TABLE:
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
            
        # Create an RDD for each text file
        rdds = [spark.sparkContext.textFile(path) for path in paths]
        # Combine them into a single file
        rdd  = spark.sparkContext.union(rdds)
        # Convert it to a dataframe
        df   = spark.createDataFrame( rdd.map( table.parse_line_to_SparkSQLRow ), samplingRatio=1.0 )
        df.registerTempTable( sqlName )
        return df
            
    def find_variable_by_name(self,name):
        """Scans all tables in the schema until a variable name is found. Returns it"""
        for table in self.schema.tables():
            try:
                return (table, table.get_variable(name))
            except KeyError:
                pass
        raise KeyError(f"variable {name} not found in any table in schema")

    def print_legend(self,df,*,printHeading=True,file=sys.stdout):
        """Print the legend for the columns in the dataframe. Takes advantage of the fact that all column names are unique with the Census Bureau."""
        if printHeading:
            print("Legend:")
        rows = []
        for varName in df.columns:
            if "." in varName:
                varName = varName.split(".")[-1] # take the last name
            rows.append( self.find_variable_by_name(varName) )
        rows.sort()
        old_table = None
        for (table, var) in rows:
            if table!= old_table:
                print(f"Table {table.name}   {table.desc}")
                old_table = table
            print("  ", var.name, var.desc)
        print("")

if __name__=="__main__":
    import argparse

    spark  = cspark.spark_session(logLevel='ERROR')

    parser = argparse.ArgumentParser(description='Tool for using SF1 with Spark',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--list", help="List available files", action='store_true')
    args = parser.parse_args()

    # Get a schema object associated with the SF1 for 2010
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


    print("Geolevels by state and summary level:")
    sf1_2010.get_df(tableName = GEO_TABLE, sqlName='GEO_2010')
    #print(spark.sql("SELECT * from GEO_2010 LIMIT 10").collect())
    #spark.sql("SELECT FILEID,STUSAB,LOGRECNO,STATE,COUNTYCC,TRACT,BLKGRP,BLOCK,FROM GEO_2010 LIMIT 10").show()
    tt = tydoc.tytable()
    tt.add_head(['State','Summary Level','Count'])
    for row in spark.sql("SELECT STUSAB,SUMLEV,COUNT(*) FROM GEO_2010 GROUP BY STUSAB,SUMLEV ORDER BY 1,2").collect():
        tt.add_data(row)
    tt.render(sys.stdout, format='md')

    print("Test; Print the names of 20 distinct names in the file (unformatted printing)")
    d0 = spark.sql("SELECT DISTINCT LOGRECNO,STUSAB,STATE,SUMLEV,NAME FROM GEO_2010 LIMIT 20")
    sf1_2010.print_legend(d0)
    for row in d0.collect():
        print(row)


    print("Table P2 just has counts. Here we dump the first 10 records:")
    sf1_2010.get_df(tableName="P2", sqlName='P2_2010')
    d1 = spark.sql("SELECT * FROM P2_2010 LIMIT 10")
    d1.show()
    sf1_2010.print_legend(d1)


    print("Table P17 has decimal numbers; they are represented as decimal numbers. Here are the first 10 rows:")
    sf1_2010.get_df(tableName="P17", sqlName='P17_2010')
    d2 = spark.sql("SELECT * FROM P17_2010 LIMIT 10")
    d2.show()
    sf1_2010.print_legend(d2)

    print("Table P2 counts by state and county:")
    res = spark.sql("SELECT GEO_2010.STUSAB,GEO_2010.COUNTY,GEO_2010.NAME,P0020001,P0020002,P0020003,P0020004,P0020005,P0020006 FROM GEO_2010 "
                    "INNER JOIN P2_2010 ON GEO_2010.STUSAB=P2_2010.STUSAB and GEO_2010.LOGRECNO=P2_2010.LOGRECNO "
                    "WHERE GEO_2010.SUMLEV='050' ORDER BY STUSAB,COUNTYCC")

    tt = tydoc.tytable()
    tt.add_head( res.columns )
    for row in res.collect():
        tt.add_data(row)
    tt.render(sys.stdout, format='md')
    sf1_2010.print_legend(res)

    # Compute counts by 
