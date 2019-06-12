# Decoding the SF1 2010

This file records notes of understanding the PL94 and SF1 tables.
Note that PL94 is a subset of SF1.

PL94 - Contains per-block counts used solely for redistricting
SF1  - Contains tables at the block, tract and county level.
SF2  - Contains the detailed race tables, at a tract level


Use the following columns from PL94:

STATE/US-Abbreviation (USPS) STUSAB     2
State (FIPS)                 STATE      2
County                       COUNTY     3
Census Tract                 TRACT      6
Block Group                  BLKGRP     1
Block                        BLOCK      4

P1 - P0010001 - Total Population
H1 - H0010002 - Occupied Housing Units

We do our testing with Alaska
Tracts: https://www.census.gov/geo/maps-data/maps/2010ref/st02_tract.html
Summary levels: https://factfinder.census.gov/help/en/summary_level_code_list.htm

FIPS County Class Codes: https://factfinder.census.gov/help/en/fips_class_code.htm

We want summary level 750 
750 - State-County-Voting District/Remainder-County Subdivision-Place/Remainder-Census Tract-Block Group-Block


Here is what the first line of ak000012010.pl (FILEID,STUSAB,CHARITER,CIFSN,LOGRECNO,P0010001,...):
```
PLST,AK,000,01,0000001,710231,658356,473576,23263,104871,38135,7409,11102,51875,47286,4685,26127,6915,1095,2211,1777,530,213,409,1200,431,429,782,368,114,4181,1415,252,85,68,1103,177,233,529,67,13,50,17,47,30,5,3,60,14,3,10,361,153,21,33,24,13,1,79,14,1,12,5,4,0,0,1,47,39,8,0,0,0,0,0,0,710231,39249,670982,625614,455320,21949,102556,37459,7219,1111,45368,41711,4155,24741,6498,1028,284,1643,484,174,118,1119,395,115,730,193,34,3387,1219,217,75,18,975,164,61,448,26,6,48,17,20,25,1,2,56,3,1,5,234,117,16,11,13,2,0,65,2,0,1,5,2,0,0,0,36,36,0,0,0,0,0,0,0
```

First line of ak000022010.pl (FILEID,STUSAB,CHARITER,CIFSN,LOGRECNO,...H0010001,H0010002,H0010003,...):

```
PLST,AK,000,02,0000001,522853,497328,368895,16904,70630,28312,4599,7988,25525,23913,1418,14709,3010,488,1179,712,219,60,197,717,150,237,515,238,64,1471,489,58,16,27,382,45,90,238,27,5,12,3,25,11,3,2,26,4,1,7,120,50,2,11,8,5,1,28,5,1,6,1,2,0,0,0,21,20,1,0,0,0,0,0,0,522853,24437,498416,475596,356987,16129,69383,27883,4496,718,22820,21511,1277,14156,2868,470,198,671,207,52,65,669,142,79,487,150,20,1215,420,49,14,15,341,43,34,211,15,2,11,3,13,10,1,2,24,1,1,5,77,37,1,6,5,1,0,21,2,0,1,1,2,0,0,0,17,17,0,0,0,0,0,0,0,306967,258058,48909
```

SF1 is similar to PL94, except all of the fields are different. 

Here are the first 3 lines of AK000012010.sf1:

```
SF1ST,AK,000,01,0000001,710231
SF1ST,AK,000,01,0000002,1460
SF1ST,AK,000,01,0000003,0
```

Segment 02 is a bit more complex. Here are the first 3 lines of it:

```
SF1ST,AK,000,02,0000001,710231,0,0,0,0,710231
SF1ST,AK,000,02,0000002,1460,0,0,0,0,1460
SF1ST,AK,000,02,0000003,0,0,0,0,0,0
```

Here is the first line of  ak000032010.sf1 contained within the zip file ak2010.sf1.zip:

```
SF1ST,AK,000,03,0000001,710231,473576,23263,104871,38135,7409,11102,51875,710231,670982,39249,710231,670982,455320,21949,102556,37459,7219,1111,45368,39249,18256,1314,2315,676,190,9991,6507,767150,518949,33150,138312,50402,11154,15183,767150,720313,495498,30367,133387,48530,10515,2016,46837,23451,2783,4925,1872,639,13167,710231,658356,473576,23263,104871,38135,7409,11102,51875,47286,4685,26127,6915,1095,2211,1777,530,213,409,1200,431,429,782,368,114,4181,1415,252,85,68,1103,177,233,529,67,13,50,17,47,30,5,3,60,14,3,10,361,153,21,33,24,13,1,79,14,1,12,5,4,0,0,1,47,39,8,0,0,0,0,0,0,710231,39249,670982,625614,455320,21949,102556,37459,7219,1111,45368,41711,4155,24741,6498,1028,284,1643,484,174,118,1119,395,115,730,193,34,3387,1219,217,75,18,975,164,61,448,26,6,48,17,20,25,1,2,56,3,1,5,234,117,16,11,13,2,0,65,2,0,1,5,2,0,0,0,36,36,0,0,0,0,0,0,0
```

"When using Figure 2-2, you must take into consideration that the first 5 fields of the data file contain
identification information (FILEID, STUSAB, CHARITER, CIFSN, and LOGRECNO) which makes some segments
have more than 255 fields. These segments are shown in bold. Some manipulation of the files will be
required for software with a field limit of 255." (p. 2-3)


|Field |  Name  |
|------|--------|
|1     | FILEID |
|2     | STUSAB |
|3     | SUMLEV |
|4     | COUNTY |

Where are the others?


Geo coding:
```
@1 FILEID $6. /*File Identification*/
@7 STUSAB $2. /*State/US-Abbreviation (USPS)*/
@9 SUMLEV $3. /*Summary Level*/
@12 GEOCOMP $2. /*Geographic Component*/
@28 STATE $2. /*State (FIPS)*/
@30 COUNTY $3. /*County*/
@55 TRACT $6. /*Census Tract*/
@61 BLKGRP $1. /*Block Group*/
@62 BLOCK $4. /*Block*/
@66 IUC $2. /*Internal Use Code*/
```

BLOCKGROUP is the first digit of BLOCK

akgeo2010.pl:
```
PLST  AK04000000  00000014902                                                                                                                                                                          1477953211577  245383480336Alaska                                                                                    A!   710231   306967+63.3461910-152.837067900            01785533
```

# Understanding SF1
Start with [2010 Census Summary File 1](doc/sf1.pdf). This is a 730-page document. Key things to read:

## Abstract, pp. 1-1 through.
Key points:
* 177 population tables ("P") and 58 housing tables ("H") down to the block level.
* 82 population tables ("PCT") and 4 housing tables ("HCT") down to Census Tract.
* 10 populations ("PCO") down to county level, for a total of 331 tables.
* 2 urban/rural update PCT tables
* Total number of tables: 333

Tables with major race and Hispanic or Latino groups:
* 14 population tables and 4 housing tables to the block level.
* 5 population tables down to census tract.

Supported geographic levels:
* State (including DC & PR)
* County 
* County subdivision5
* Place (or place part)
* Census tract
* Block group
* Block

The SF1 uses the FIPS 55 Code Series to the American National Standards Institute (ANSI) Code Series to define each place. 

"It is easiest to think of the file set as a logical file. However, this logical file consists of 48 physical files:
the geographic header record file and file01 through file47 (or file48). This file design is comparable to
that used in Census 2000."

"A unique logical record number (LOGRECNO in the geographic header) is assigned to all files for a specific
geographic entity. This is done so all records for that specific entity can be linked together across files.
Besides the logical record number, other identifying fields also are carried over from the geographic header
file to the table file. These are file identification (FILEID), state/U.S. abbreviation (STUSAB), characteristic
iteration (CHARITER), and characteristic iteration file sequence number (CIFSN). See Figure 2-1 on the next
page for an example."

Figure 2-2 (p. 2-5) defines the mapping between Data file segment number and the tables.


## Chapter 3 Subject Locator
Suffixes are used on variables to indicate race codes.
"For example, PCT13, when repeated for the White alone population, is labeled PCT13A."

The suffixes are:
White alone                                        A suffix
Black or African American alone                    B suffix
American Indian and Alaska Native alone		   C suffix
Asian alone 	    	   	  	           D suffix
Native Hawaiian and Other Pacific Islander alone   E suffix
Some Other Race alone 	  	  	   	   F suffix
Two or More Races 				   G suffix
Hispanic or Latino 				   H suffix
White alone, not Hispanic or Latino 		   I suffix

One matrix, PCT12, is repeated not only for the above nine groups but also for the following:

Black or African American alone, not Hispanic or Latino                    J suffix
American Indian and Alaska Native alone, not Hispanic or Latino 	   K suffix
Asian alone, not Hispanic or Latino 	     	      	 		   L suffix
Native Hawaiian and Other Pacific Islander alone, not Hispanic or Latino   M suffix
Some Other Race alone, not Hispanic or Latino 	      	       	  	   N suffix
Two or More Races, not Hispanic or Latino 				   O suffix


What is wanted:

block x cenrace x hispanic
SF1 P8 and P9

According to the documentation:

p. 3-6:
Hispanic or Latino, and Not Hispanic or Latino
  Population 18 Years and Over, by Race: P11
  Total Population, by Race:             P9

p. 310
Race (also see asterisks throughout index)
  Total Population:     P3, P8, PCT23

# Chapter 5:

P8 RACE - Universe: Total Population ... 71 data cells
   Universe: Total population
P9 Hispanic or Latino, And not Hispanic or Latino by Race .. 73 data cells
   Universe: Total population

# Chapter 6: Data Dictionary
Chapter pages 6-1 through 6-349
PDF pages 163-512


The data is viewed as a single Matrix split into multiple files. 
Each line of each file contains the first 5 fields:
     1. FILEID - File ID, should be ST1ST (State file).
     2. STUSAB - State/U.S. Abbreviation (USPS)
     3. SUMLEV - Summary Level
     4. CHARITER - Characteristic Iteration. (000 means not an iteration)
     5. CIFSN    - Charistic Iteration File Sequence Number
     5. LOGRECNO - Logical Record Number

Notes:
FILEID - A unique, six-character identifier for each file series.
GEOCOMP - Geographic Component - Ignore this.
CHARITER - Ignore this. ("These iteration fields apply to Summary File 2 (SF 2) and the American Indian and Alaska Native Summary File only.")
CIFSN - The sequence number of the table file within the set of physical files for the state (i.e., the geographic
header record file and one or more table files).
LOGRECNO - The logical record is the complete record for a geographic entity defined by the summary level, but
exclusive of the characteristic iteration. A logical record may have one or more parts (or segments).
Each logical record has an assigned sequential integer number within the file.


The Matrix files begin:
File 01 --- File Linking Fields (comma delimited)
     1. FILEID - File ID, should be ST1ST (State file).
     2. STUSAB - State/U.S. Abbreviation (USPS)
     3. CHARITER - Characteristic Iteration. (000 means not an iteration)
     4. CIFSN    - Charistic Iteration File Sequence Number
     5. LOGRECNO - Logical Record Number
P1:
     6. P0010001 - Total population (universe: Total Population)

File 02 --- File Linking Fields
     1. FILEID - File ID, should be ST1ST (State file).
     2. STUSAB - State/U.S. Abbreviation (USPS)
     3. CHARITER - Characteristic Iteration. (000 means not an iteration)
     4. CIFSN    - Charistic Iteration File Sequence Number
     5. LOGRECNO - Logical Record Number
P2:
     6. P2

File 03 --- File Linking Fields
     1. FILEID - File ID, should be ST1ST (State file).
     2. STUSAB - State/U.S. Abbreviation (USPS)
     3. CHARITER - Characteristic Iteration. (000 means not an iteration)
     4. CIFSN    - Charistic Iteration File Sequence Number
     5. LOGRECNO - Logical Record Number
P3:
P4
P5
P6
P7

All of the files are then combined into a single huge matrix.

So it looks like we do the following:
1. Scan the geofile for all of the LOGRECNOs in a particular summary level.
2. Scan file 3. For each line, if we have a matching LOGRECNO, decode the line.
   To decode the line, we need to parse the PDF for Section 6, the data dictionary.

So it looks like we need to get the summary level for the LOGRECNO from the identification section.



p. 6-24 defines the P8 data dictionary:
Values P0080001 through P0080071  (Segment 3, Max Size 9)

p. 6-27 defines the P9 data dictionary:
Values P0090001 through P0090073  (Segment 3, Max Size 9)

The contents of File 3 are defined in the PDF, pages 6-22 through 6-29.
I have extracted these in the doc/ directory:

Robert wants:
* Each file has a header describing what the columns are
* CSV file
* Each row has a geocode as a column
