-- SQLite3/MySQL compatiable schema generated Wed Mar 18 09:29:59 2020 by /Users/simsong/gits/stats_2010/ctools/schema/table.py
CREATE TABLE geo (
   SLDU VARCHAR(3),  
   SLDL VARCHAR(3),  
   PUMA VARCHAR(5),  
   PLACE VARCHAR(5),  
   FILEID VARCHAR(6), -- File Identification1
   STUSAB VARCHAR(2), -- State/U.S. Abbreviation (USPS)
   SUMLEV VARCHAR(3), -- Summary Level2
   GEOCOMP VARCHAR(2), -- Geographic Component3
   CHARITER VARCHAR(3), -- Characteristic Iteration4
   CIFSN VARCHAR(2), -- Characteristic Iteration File Sequence Number5
   LOGRECNO VARCHAR(7), -- Logical Record Number6
   REGION VARCHAR(1), -- Region7
   DIVISION VARCHAR(1), -- Division7
   STATE VARCHAR(2), -- State (FIPS)7 8
   COUNTY VARCHAR(3), -- County7 8
   COUNTYCC VARCHAR(2), -- FIPS County Class Code8
   COUNTYSC VARCHAR(2), -- County Size Code9
   COUSUB VARCHAR(5), -- County Subdivision (FIPS)7 8
   COUSUBCC VARCHAR(2), -- FIPS County Subdivision Class Code8
   COUSUBSC VARCHAR(2), -- County Subdivision Size Code9
   PLACECC VARCHAR(2), -- FIPS Place Class Code8
   PLACESC VARCHAR(2), -- Place Size Code9
   TRACT VARCHAR(6), -- Census Tract7
   BLKGRP VARCHAR(1), -- Block Group7
   BLOCK VARCHAR(4), -- Block7
   IUC VARCHAR(2), -- Internal Use Code10
   CONCIT VARCHAR(5), -- Consolidated City (FIPS)7 8
   CONCITCC VARCHAR(2), -- C3 Consolidated city
   CONCITSC VARCHAR(2), -- Consolidated City Size Code9
   AIANHH VARCHAR(4), -- American Indian Area/Alaska Native Area/ Hawaiian Home Land (Census)7
   AIANHHFP VARCHAR(5), -- Hawaiian Home Land (FIPS)7 8 11
   AIANHHCC VARCHAR(2), -- Hawaiian Home Land Class Code8
   AIHHTLI VARCHAR(1), -- Land Indicator
   AITSCE VARCHAR(3), -- American Indian Tribal Subdivision (Census)7
   AITSCC VARCHAR(2), -- Class Code8
   TTRACT VARCHAR(6), -- Tribal Census Tract
   TBLKGRP VARCHAR(1), -- Tribal Block Group
   ANRC VARCHAR(5), -- Alaska Native Regional Corporation (FIPS)7 8
   ANRCCC VARCHAR(2), -- Class Code8
   CBSA VARCHAR(5), -- Statistical Area7 8
   CBSASC VARCHAR(2), -- Statistical Area Size Code9
   METDIV VARCHAR(5), -- Metropolitan Division7 8
   CSA VARCHAR(3), -- Combined Statistical Area7 8
   NECTA VARCHAR(5), -- New England City and Town Area7 8
   NECTASC VARCHAR(2), -- New England City and Town Area Size Code9
   NECTADIV VARCHAR(5), -- New England City and Town Area Division7 8
   CNECTA VARCHAR(3), -- Combined New England City and Town Area7 8
   CBSAPCI VARCHAR(1), -- Statistical Area Principal City Indicator7
   NECTAPCI VARCHAR(1), -- Indicator7
   UA VARCHAR(5), -- Urban Area7 12
   UASC VARCHAR(2), -- Urban Area Size Code9 12
   UATYPE VARCHAR(1), -- Urban Area Type7 12
   UR VARCHAR(1), -- Urban/Rural7 12
   CD VARCHAR(2), -- Congressional District (111th)7 8 13
   VTD VARCHAR(6), -- Voting District7 15
   VTDI VARCHAR(1), -- Voting District Indicator7
   ZCTA5 VARCHAR(5), -- ZIP Code Tabulation Area (5-digit)7 12
   SUBMCD VARCHAR(5), -- Subminor Civil Division (FIPS)7 8
   SUBMCDCC VARCHAR(2), -- FIPS Subminor Civil Division Class Code8
   SDELM VARCHAR(5), -- School District (Elementary)7
   SDSEC VARCHAR(5), -- School District (Secondary)7
   SDUNI VARCHAR(5), -- School District (Unified)7
   AREALAND VARCHAR(14), -- Area (Land)16
   AREAWATR VARCHAR(14), -- Area (Water)17
   NAME VARCHAR(90), -- Area Name-Legal/Statistical Area Description (LSAD) Term-Part Indicator18
   FUNCSTAT VARCHAR(1), -- Functional Status Code
   GCUNI VARCHAR(1), -- Geographic Change User Note Indicator
   INTPTLAT VARCHAR(11), -- Internal Point (Latitude)21
   INTPTLON VARCHAR(12), -- Internal Point (Longitude)22
   LSADC VARCHAR(2), -- Legal/Statistical Area Description Code
   PARTFLAG VARCHAR(1), -- Special Area Codes
   UGA VARCHAR(5), -- Urban Growth Area7
   STATENS VARCHAR(8), -- State (ANSI)8
   COUNTYNS VARCHAR(8), -- County (ANSI)8
   COUSUBNS VARCHAR(8), -- County Subdivision (ANSI)8
   PLACENS VARCHAR(8), -- Place (ANSI)8
   CONCITNS VARCHAR(8), -- Consolidated City (ANSI)8
   AIANHHNS VARCHAR(8), -- Hawaiian Home Land (ANSI)8
   AITSNS VARCHAR(8), -- American Indian Tribal Subdivision (ANSI)8
   ANRCNS VARCHAR(8), -- Alaska Native Regional Corporation (ANSI)8
   SUBMCDNS VARCHAR(8), -- Subminor Civil Division (ANSI)8
   AIANHHSC VARCHAR(2), -- Hawaiian Home Land Size Code9
   CSASC VARCHAR(2), -- Combined Statistical Area Size Code9
   CNECTASC VARCHAR(2), -- Combined NECTA Size Code9
   MEMI VARCHAR(1), -- Metropolitan/Micropolitan Indicator
   NMEMI VARCHAR(1), -- NECTA Metropolitan/Micropolitan Indicator
   RESERVED VARCHAR(18) -- Reserved
);
