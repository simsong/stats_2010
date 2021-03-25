#!/usr/bin/env python3
"""
Tools for accessing the decennial data from Spark. Creates a data
frame with all of the decennial data that you can then process with
SQL.

"""

import os
import sys
import re

from constants import *
import cb_spec_decoder
import ctools.cspark as cspark
import ctools.s3     as s3
import ctools.tydoc  as tydoc

DECENNIAL_ROOT='DECENNIAL_ROOT'

# Hard-code where the DAS keeps its PL94 and SF1 data
DAS_S3ROOT='DAS_S3ROOT'
DAS_ROOTS=  ["$DAS_S3ROOT/2000/pl94",
             "$DAS_S3ROOT/2000/sf1",
             "$DAS_S3ROOT/2010/pl94",
             "$DAS_S3ROOT/2010/sf1"]

files = list()                  # database of files
registered_paths = set()        # paths that have been registered
def find_files():
    """Returns an iterator of all files under SF1_ROOT. Allows multiple paths if separated by semicolons"""

    if DAS_S3ROOT in os.environ:
        roots=DAS_ROOTS
    else:
        try:
            roots=os.environ[DECENNIAL_ROOT].split(';')
        except KeyError:
            raise RuntimeError("Environment variable DECENNIAL_ROOT must be defined with location of unzipped Decennial data files")
    for root in roots:
        root = os.path.expandvars(root) # expand dollar signs
        (bucket,prefix)  =  s3.get_bucket_key(root)
        print("Searching for published data in ",root)
        if root.startswith('s3:'):
            for obj in s3.list_objects(root):
                yield f's3://{bucket}/{obj[s3._Key]}'
        elif root.startswith('hdfs:'):
            raise RuntimeError('hdfs SF1_ROOT not implemented')
        else:
            for (dirpath,dirnames,filenames) in os.walk(root):
                for filename in filenames:
                    yield os.path.join(dirpath,filename)

def register_files(verbose=False):
    for path in find_files():
        register_file(path,verbose=verbose)

def unique_selector(selector):
    """Return the unique values for a given selector"""
    return set( [obj[selector] for obj in files] )


# Regular expressions for data products
RE='re'
FILEPATS=[ {YEAR:2000,PRODUCT:PL94,CIFSN_GEO:True,  RE:re.compile(r'(?P<state>[a-z][a-z])geo[.]upl')},
           {YEAR:2000,PRODUCT:PL94,CIFSN_GEO:False, RE:re.compile(r'(?P<state>[a-z][a-z])(?P<cifsn>\d{5})[.]upl')},

           {YEAR:2000,PRODUCT:SF1, CIFSN_GEO:True,  RE:re.compile(r'(?P<state>[a-z][a-z])geo[.]uf1')},
           {YEAR:2000,PRODUCT:SF1, CIFSN_GEO:False, RE:re.compile(r'(?P<state>[a-z][a-z])(?P<cifsn>\d{5})[.]uf1')},

           {YEAR:2010,PRODUCT:PL94,CIFSN_GEO:True,  RE:re.compile(r'(?P<state>[a-z][a-z])geo2010[.]pl')},
           {YEAR:2010,PRODUCT:PL94,CIFSN_GEO:False, RE:re.compile(r'(?P<state>[a-z][a-z])(?P<cifsn>\d{5})2010[.]pl')},

           {YEAR:2010,PRODUCT:SF1, CIFSN_GEO:True,  RE:re.compile(r'(?P<state>[a-z][a-z])geo2010[.]sf1')},
           {YEAR:2010,PRODUCT:SF1, CIFSN_GEO:False, RE:re.compile(r'(?P<state>[a-z][a-z])(?P<cifsn>\d{5})2010[.]sf1')},
       ]


PATH='path'
IGNORE_EXTENSIONS=['.csv','.zip']
def register_file(path, verbose=False):
    """Files have a pattern:  {state}{section}{year}.{product}"""
    if path in registered_paths:
        return
    if os.path.splitext(path)[1] in IGNORE_EXTENSIONS:
        return
    filename = os.path.basename(path)

    for pat in FILEPATS:
        m = pat[RE].search(filename)
        if m:
            if pat[CIFSN_GEO]==True:
                cifsn = CIFSN_GEO
            else:
                cifsn = int(m.group('cifsn'))
            obj = {PATH:path,
                   STATE:m.group('state'),
                   CIFSN:cifsn,
                   YEAR:pat[YEAR],
                   PRODUCT:pat[PRODUCT]}
            if verbose:
                print(obj)
            files.append(obj)
            registered_paths.add(path)
            return
    if verbose:
        print("Unrecognized filename:",filename)

# pylint: disable=E0401
class DecennialDF:
    """Create a set of dataframes associated with a decennial product."""
    def __init__(self,*,year,product):
        """Inventory the files and return an SF1 object."""

        self.year = year
        self.product = product

        # Validate parameters
        if year not in YEARS:
            raise RuntimeError(f"year must be in {YEARS}")

        if product not in PRODUCTS:
            raise RuntimeError(f"product must be in {PRODUCTS}")


        # Validate schema
        ch6file = CHAPTER6_CSV_FILE.format(year=year,product=product)
        if not os.path.exists(ch6file):
            raise FileNotFoundError(f"Requires {ch6file}")
        self.schema = cb_spec_decoder.schema_for_spec(ch6file, year=self.year, product=self.product )

        # Find the data files
        register_files()
        if len(files)==0:
            raise RuntimeError("No product files found")


    def get_table(self,tableName):
        return self.schema.get_table(tableName)

    def get_df(self,*, tableName, sqlName):
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
        paths = [ obj[PATH] for obj in files if
                  (obj[YEAR]==self.year and obj[PRODUCT]==self.product) and obj[CIFSN]==cifsn]
        for p in paths:
            print("path:",p)

        if len(paths)==0:
            print("No file found. Available data files:")
            for obj in files:
                print(obj)
            raise RuntimeError(f"No files found looking for year:{self.year} product:{self.product} CIFSN:{cifsn}")

        from pyspark.sql import SparkSession
        spark = SparkSession.builder.getOrCreate()

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
        """Print the legend for the columns in the dataframe. Takes advantage
        of the fact that all column names are unique with the Census
        Bureau."""
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
