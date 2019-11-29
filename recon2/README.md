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

The new coding format creates multiple variables for each person. The coding method using the above is:

    P02198_000300_1010_xxxx   - a unique identifier for each person on the block. xxxx is a hexadecimal number ranging from 0000 to ffff, allowing for up to 65,536 people per block.

For each person, there are 

    P02198_000300_1010_xxxx_A - person abcd's Age  [0..110]
    P02198_000300_1010_xxxx_R - person abcd's Race # [0..63]
    P02198_000300_1010_xxxx_H - person abcd's Hispanic code [0,1]
    P02198_000300_1010_xxxx_S - person abcd's sex code [0,1]
    
Race coding:  This reconstruction treats race as a bitfield. This is NOT the standard census coding, but that it allows for significantly more efficient representations. Our coding is:

     0x01 - White (WHITE)
     0x02 - Black or African American (BLACK)
     0x04 - American Indian or Alaksa Native (AIAN)
     0x08 - Asian (ASIAN)
     0x10 - Native Hawaiian or Other Pacific Islander (NHOPI)
     0x20 - Some Other Race (SOR)         

Database reconstruction can be performed almost entirely with block-level data (most of the relevant tabels are published at the block level). However, single-year age is only published at the tract level. Thus, the solution approach is to construct constraints for every block in the tract and for the tract as a whole, and then to solve tract-by-tract.

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

     (ite (and (and (>= P02198_000300_1010_00a_A 22) (<= P02198_000300_1010_00a_A 24) 
                    (= P02198_000300_1010_00a_S MALE)))
          1 0)

Which is simplifed to:
(ite (and (>= P02198_000300_1010_00a_A 22)
          (<= P02198_000300_1010_00a_A 24) 
          (=  P02198_000300_1010_00a_S MALE))
     1 0)

If we replace 00a with {pnum} (person number) then the and if the value of P0120010 for 02198_00300_1010 is 10, and if there are 30 people on the block, then assert statement is:

y = [f"""(ite (and (>= P02198_000300_1010_{hex4(pnum)}_A 22)
            (<= P02198_000300_1010_{hex4(pnum)}_A 24) 
             (=  P02198_000300_1010_{hex4(pnum)}_S MALE))
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

