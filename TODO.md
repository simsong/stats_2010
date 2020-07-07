Create an intermediate file describign the tables. Use that to make the schema.

## Table language
For each table, define:
 - page number in PDF
 - variable name/description/type
 - variable set including:
   - variable name template
   - variable name range
   - variable name descriptions
   - how to permuate variable names.

## Recon1
- Try to process existing .LP files with GLPK

## Recon2
- Produce .LP files to solve as MIPs.
- Explore using https://pythonhosted.org/PuLP/CaseStudies/a_sudoku_problem.html to produce the .LP files

## Geography:
- modify the SQL database so that we have a new table for experimenting with geotrees:

GeotreeN:
ID | LOGRECNO | P1 | P2 | P3 | P4 | P5

P1 - state/AIAN
P2 - county/MCD
P3 - tract group
P4 - tract
P5 - block group
P6 - block

pl94_dbload - loads tables and Geocode 1 & Geocode3 remain as is.
geotree.py - add code for creating and managing the geotree tables.

Plan forward:
- Create a geotree table for the v1 and v3 geocodes
- Modify geocode_stats.py to be able to report on any geotree
- Create a geotree for the v4 geotree (where there are three levels under COUNTY/MCD which are adaptively chosen)

