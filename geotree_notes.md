Nomenclature
============
US = "resident population of the United States of America"
PR = "resident population of the territory of Puerto Rico"

Geounit -

Geolevel

Geotree - the tree that contains all of the geounits arranged in all of the geolevels.

Geography Schemas
 This project has created five geography schemas; this numbering is used for reports:

v1 - Six levels: Geographical hiearchy used for the 2010 Demonstration Data products.
v2 - Five levels: Initial proposal incorporating AIANNH and Minor Civil Divisions.
v3 - Four levels: v2 proposal with a synthetic LEVEL3 connecting COUNTY/MCD to BLOCK.
v4 - Corrected v2.1 Revised MCD and AIAN-aware geography
v5 - v4 geography with bypass-to-block for populations < 1000



Partition - At each geolevel, each geounit is partitioned, and these partitions are used to create the next level down. This is how the tree is formed.

Each partition level is given a name (P0 .. P6). We store the value of (P0,P1,P2,P3,P4,P5,P6) as a unique tuple for each block. 

We name the levels as:

P0 - The root of the tree.

P1 - The first partition, includes the states (v1) and the state AIANNH areas (v2+)

P2 - The first sub-state partition.
   v1 - this is the counties.
   v4 - For tribal areas of a state, this is the AIANHH code.
      - For non-tribal areas, the partitioning depends upon the state type, and is reflected in the first letter of the P2
  A - AIANHH/tribal area of a state
  N - New England State (non-tribal area)
  P - Puerto Rico
  M - States with "strong" municipal civil divisions (MCDs) at the county level other than New England States. (non-tribal areas)
  P - States that lack "strong" municipal civil divisions; the tree for these states is organized County->Place
  Q - States that lack "strong" municipal civil divisions but have many places; these states are organized (COUNTY,COUSUB)->PLACE (non-tribal areas)


P3 -
   v1 - This is the tract groups

P4 -
   v1 - This is the tracts

P5 -
   v1 - This is the block groups, which is the first digit of the block identifier. Thus, in V1 geography, there may be up to 1000 blocks in a block group.
   
   v4 - This is the first 2 digits of the block identifier. In V4 geography, there may be only 100 blocks in a block2 group.

P6 - The block level



