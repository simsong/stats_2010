This is the rewrite of the database reconstruction code.

__Please read this file through to the end before starting.__

# Census 2010 Database Reconstruction v2

This code builds upon the ideas in the (v1 database reconstruction)[../recon] and in the article Simson Garfinkel, John M. Abowd, and Christian Martindale. 2018, (Understanding Database Reconstruction Attacks on Public Data)[https://dl.acm.org/citation.cfm?id=3295691].

In the v1 database reconstruction, every potential person was represented by a variable that encoded the geocode, the sex, person number, and race categories. For example:

    C_021980003001010_male_15.0_0_male_17_N_Y_N_N_N_N_N 1

(This example does not use actual data.)

This is encoded as:

    02 - state
    198 - county
    000300 - tract
    1010   - block
    male   - sex
    15     - start_age
    17     - age
    N_Y_N_N_N_N_N - White_Black_AIAN_ASIAN_NH_SOR_HISP
    1      - Indicates that there is 1 person with these characteristics

This coding form resulted in very sparse problems and huge LP files. The LP files were also very hard to audit and to map to specific tables, which made it difficult to map the methodology to other problem regimes.

The new coding format creates multiple variables for each person. The coding starts by assuming that we are solving tract-by-tract, so the variables do not encode state, county or tract information. Instead, the variable looks like this:

    P1010_x   - a unique identifier for each person on block 1010. x is a decimal number ranging from 0 to the maximum number of people on the block.

For each person, there are 

    P1010_xA - person x's Age  [0..110]
    P1010_xH - person x's Hispanic code [0,1]
    P1010_xS - person x's sex code [0,1]
    P1010_xw - person x's is White [0,1]
    P1010_xb - person x's is Black or African American [0,1]
    P1010_xi - person x's is American Indian or Alaska Native [0,1]
    P1010_xs - person x's is Asian [0,1]
    P1010_xh - person x's is Native Hawaiian or Other Pacific Islander [0,1]
    P1010_xo - person x's is Some Other Race [0,1]
        
Database reconstruction can be performed almost entirely with block-level data (most of the relevant tabels are published at the block level). However, single-year age is only published at the tract level. Thus, the solution approach is to construct constraints for every block in the tract and for the tract as a whole, and then to solve tract-by-tract.

We are now using an SMT solver. There are several to choose from:
* Microsoft's Z3
* VeriT - https://verit.loria.fr
* Yices - https://yices.csl.sri.com
* http://optimathsat.disi.unitn.it/

Solution approach is as follows.

1. The geography file is scanned and loaded into a database, so that the geocode for every LOGREC is known.

2. The P1 (total population) table in PL94 is scanned and loaded into the database. We now have the population for each block. We start creating the SMT-LIB file for each census Tract with the list of variables for all of the blocks in the track.

3. For each remaing table, we expand each cell into a constraint. Each cell is a sum over variables that match a specific set of filters, so we just iterate over the cells that match the filter and add them into the constraint.

That is, each cell becomes and assertion such that:

     ASSERT (cell count) = (SUM (All matching people))

(All matching people) is a SUM over:
     - all relevant geographies (either the block or all of the blocks in the tract)
     - the age range of the matching people (each cell has a specified age range)
     - the sex of the matching people (either 0, 1, or both)
     - the race of the matching people (a specific value, or all)
     - the ethnicity of the matching people (either 0, 1, or both)

NOTE: We are currently not reconstructing household, but we trivially could do so using the approach described herein.


For example, if we are processing table P12 (Sex by Age), variable P0120010 (Male, 22 to 24 years old) is described by:

    (and 
     (and (>= AGE 22) (<= AGE 24))
     (= (SEX MALE)))

Continuing the above example, for person 000a in 02198_000300_1010, the expansion would be:

     (ite (and (and (>= P1010_00a_A 22) (<= P1010_00a_A 24) 
                    (= P1010_00a_S MALE)))
          1 0)

Which is simplifed to:
(ite (and (>= P1010_00a_A 22)
          (<= P1010_00a_A 24) 
          (=  P1010_00a_S MALE))
     1 0)

If we replace 00a with {pnum} (person number) then the and if the value of P0120010 for 02198_00300_1010 is 10, and if there are 30 people on the block, then assert statement is:

y = [f"""(ite (and (>= P1010_{hex4(pnum)}_A 22)
            (<= P1010_{hex4(pnum)}_A 24) 
             (=  P1010_{hex4(pnum)}_S MALE))
          1 0)""" for pnum in range(0,30)]

f"(assert (= 10) (sum {y}))"

Or, with some more parameterization:

y = [f"""(ite (and (>= P{geocode}_{p4}_A 22)
            (<= P{geocode}_{p4}_A 24) 
            (=  P{geocode}_{p4}_S MALE))
          1 0)""" for pnum in range(0,30)]

f"(assert (= 10) (sum {y}))"

This is then parameterized with a generator function that takes as arguments:
    * number of people in the cell
    * restrictions on the cell (age, sex, race & ethnicity).

Because the tables seem to have a lot of arbitrary coding, we create all of the generators in python. In a future version we will compile them from the PDF.

NOTE: reconv1 had most of the layouts encoded in the file (layouts.json)[../recon/layouts/layouts.json] and (sf1_vars_race_binaries.csv)[../recon/sf1_vars_race_binaries.csv].

File layouts.json indicates that the variable P0120010 maps to the file SF1_0004.sf1 and file sf1_vars_race_binaries.csv has this line for P0120010:

    22 to 24 years,P12,P0120010,block,missing,missing,missing,missing,missing,missing,missing,missing,missing,male,22,24,missing

Meaning:
    title:         22 to 24 years
    table_number:  P12
    cell_number:   P0120010
    level:         block
    total:         missing
    white:         missing
    black:         missing
    aian:          missing
    asian:         missing
    nhopi:         missing
    sor:           missing
    two:           missing
    hispanic:      missing
    sex:           male
    start_age:     22
    end_age:       24
    median_age     missing

The origin of this file sf1_vars_race_binaries.csv is unclear, but we may try to use it to infer the relationships.

# Solving
V1 uses Gurobi.

For V2, we tried to encode each tract problem as a (SMT-LIB)[http://smtlib.cs.uiowa.edu/index.shtml] problem.

# Developing

This was developed using Alaska (AK) county 105, tract 000200, which is the smallest tract. It contains just 12 blocks with a total of 95 people:

```
sqlite> select * from blocks where state='AK' and county=105 and tract=200;
AK|105|200|1000|24728|2||
AK|105|200|1001|24729|3||
AK|105|200|1002|24730|9||
AK|105|200|1003|24731|20||
AK|105|200|1004|24732|15||
AK|105|200|1005|24733|5||
AK|105|200|1006|24734|29||
AK|105|200|1007|24735|0||
AK|105|200|1008|24736|0||
AK|105|200|1009|24737|0||
AK|105|200|1010|24738|0||
AK|105|200|1011|24739|12||
sqlite> select sum(pop) from blocks where state='AK' and county=105 and tract=200;
95
sqlite>
```
AK|105|200|12

(It turns out that county 198, tract 000300 only has 87 people, but it has 27 blocks.)


# Changes from v1

V1 only used the following tables:

```
% awk -F, '{print $2}' sf1_vars_race_binaries.csv | sort | uniq | grep -v table_number
P1
P11
P12
P12A
P12B
P12C
P12D
P12E
P12F
P12G
P12H
P12I
P14
P6
P7
P9
PCT12
PCT12A
PCT12B
PCT12C
PCT12D
PCT12E
PCT12F
PCT12G
PCT12H
PCT12I
PCT12J
PCT12K
PCT12L
PCT12M
PCT12N
PCT12O
```