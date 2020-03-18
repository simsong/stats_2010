# Automatically generated on Wed Mar 18 10:05:27 2020 by /Users/simsong/gits/stats_2010/ctools/schema/table.py

def leftpad(x,width):
    return ' '*(width-len(str(x)))+str(x)

def between(a,b,c,width):
    return leftpad(a,width) <= leftpad(b,width) <= leftpad(c,width)

def safe_int(i):
    try:
        return int(i)
    except (TypeError, ValueError) as e:
        return None

def safe_float(i):
    try:
        return float(i)
    except (TypeError, ValueError) as e:
        return None

def safe_str(i):
    try:
        return str(i)
    except (TypeError, ValueError) as e:
        return None


class geo_validator:
    @classmethod
    def is_valid_SLDU(self,x):
        """"""
        return True
    @classmethod
    def is_valid_SLDL(self,x):
        """"""
        return True
    @classmethod
    def is_valid_PUMA(self,x):
        """"""
        return True
    @classmethod
    def is_valid_PLACE(self,x):
        """"""
        return True
    @classmethod
    def is_valid_FILEID(self,x):
        """File Identification1"""
        return True
    @classmethod
    def is_valid_STUSAB(self,x):
        """State/U.S. Abbreviation (USPS)"""
        return True
    @classmethod
    def is_valid_SUMLEV(self,x):
        """Summary Level2"""
        return True
    @classmethod
    def is_valid_GEOCOMP(self,x):
        """Geographic Component3"""
        return True
    @classmethod
    def is_valid_CHARITER(self,x):
        """Characteristic Iteration4"""
        return True
    @classmethod
    def is_valid_CIFSN(self,x):
        """Characteristic Iteration File Sequence Number5"""
        return True
    @classmethod
    def is_valid_LOGRECNO(self,x):
        """Logical Record Number6"""
        return True
    @classmethod
    def is_valid_REGION(self,x):
        """Region7"""
        return True
    @classmethod
    def is_valid_DIVISION(self,x):
        """Division7"""
        return True
    @classmethod
    def is_valid_STATE(self,x):
        """State (FIPS)7 8"""
        return True
    @classmethod
    def is_valid_COUNTY(self,x):
        """County7 8"""
        return True
    @classmethod
    def is_valid_COUNTYCC(self,x):
        """FIPS County Class Code8"""
        return True
    @classmethod
    def is_valid_COUNTYSC(self,x):
        """County Size Code9"""
        return True
    @classmethod
    def is_valid_COUSUB(self,x):
        """County Subdivision (FIPS)7 8"""
        return True
    @classmethod
    def is_valid_COUSUBCC(self,x):
        """FIPS County Subdivision Class Code8"""
        return True
    @classmethod
    def is_valid_COUSUBSC(self,x):
        """County Subdivision Size Code9"""
        return True
    @classmethod
    def is_valid_PLACECC(self,x):
        """FIPS Place Class Code8"""
        return True
    @classmethod
    def is_valid_PLACESC(self,x):
        """Place Size Code9"""
        return True
    @classmethod
    def is_valid_TRACT(self,x):
        """Census Tract7"""
        return True
    @classmethod
    def is_valid_BLKGRP(self,x):
        """Block Group7"""
        return True
    @classmethod
    def is_valid_BLOCK(self,x):
        """Block7"""
        return True
    @classmethod
    def is_valid_IUC(self,x):
        """Internal Use Code10"""
        return True
    @classmethod
    def is_valid_CONCIT(self,x):
        """Consolidated City (FIPS)7 8"""
        return True
    @classmethod
    def is_valid_CONCITCC(self,x):
        """C3 Consolidated city"""
        return True
    @classmethod
    def is_valid_CONCITSC(self,x):
        """Consolidated City Size Code9"""
        return True
    @classmethod
    def is_valid_AIANHH(self,x):
        """American Indian Area/Alaska Native Area/ Hawaiian Home Land (Census)7"""
        return True
    @classmethod
    def is_valid_AIANHHFP(self,x):
        """Hawaiian Home Land (FIPS)7 8 11"""
        return True
    @classmethod
    def is_valid_AIANHHCC(self,x):
        """Hawaiian Home Land Class Code8"""
        return True
    @classmethod
    def is_valid_AIHHTLI(self,x):
        """Land Indicator"""
        return True
    @classmethod
    def is_valid_AITSCE(self,x):
        """American Indian Tribal Subdivision (Census)7"""
        return True
    @classmethod
    def is_valid_AITSCC(self,x):
        """Class Code8"""
        return True
    @classmethod
    def is_valid_TTRACT(self,x):
        """Tribal Census Tract"""
        return True
    @classmethod
    def is_valid_TBLKGRP(self,x):
        """Tribal Block Group"""
        return True
    @classmethod
    def is_valid_ANRC(self,x):
        """Alaska Native Regional Corporation (FIPS)7 8"""
        return True
    @classmethod
    def is_valid_ANRCCC(self,x):
        """Class Code8"""
        return True
    @classmethod
    def is_valid_CBSA(self,x):
        """Statistical Area7 8"""
        return True
    @classmethod
    def is_valid_CBSASC(self,x):
        """Statistical Area Size Code9"""
        return True
    @classmethod
    def is_valid_METDIV(self,x):
        """Metropolitan Division7 8"""
        return True
    @classmethod
    def is_valid_CSA(self,x):
        """Combined Statistical Area7 8"""
        return True
    @classmethod
    def is_valid_NECTA(self,x):
        """New England City and Town Area7 8"""
        return True
    @classmethod
    def is_valid_NECTASC(self,x):
        """New England City and Town Area Size Code9"""
        return True
    @classmethod
    def is_valid_NECTADIV(self,x):
        """New England City and Town Area Division7 8"""
        return True
    @classmethod
    def is_valid_CNECTA(self,x):
        """Combined New England City and Town Area7 8"""
        return True
    @classmethod
    def is_valid_CBSAPCI(self,x):
        """Statistical Area Principal City Indicator7"""
        return True
    @classmethod
    def is_valid_NECTAPCI(self,x):
        """Indicator7"""
        return True
    @classmethod
    def is_valid_UA(self,x):
        """Urban Area7 12"""
        return True
    @classmethod
    def is_valid_UASC(self,x):
        """Urban Area Size Code9 12"""
        return True
    @classmethod
    def is_valid_UATYPE(self,x):
        """Urban Area Type7 12"""
        return True
    @classmethod
    def is_valid_UR(self,x):
        """Urban/Rural7 12"""
        return True
    @classmethod
    def is_valid_CD(self,x):
        """Congressional District (111th)7 8 13"""
        return True
    @classmethod
    def is_valid_VTD(self,x):
        """Voting District7 15"""
        return True
    @classmethod
    def is_valid_VTDI(self,x):
        """Voting District Indicator7"""
        return True
    @classmethod
    def is_valid_ZCTA5(self,x):
        """ZIP Code Tabulation Area (5-digit)7 12"""
        return True
    @classmethod
    def is_valid_SUBMCD(self,x):
        """Subminor Civil Division (FIPS)7 8"""
        return True
    @classmethod
    def is_valid_SUBMCDCC(self,x):
        """FIPS Subminor Civil Division Class Code8"""
        return True
    @classmethod
    def is_valid_SDELM(self,x):
        """School District (Elementary)7"""
        return True
    @classmethod
    def is_valid_SDSEC(self,x):
        """School District (Secondary)7"""
        return True
    @classmethod
    def is_valid_SDUNI(self,x):
        """School District (Unified)7"""
        return True
    @classmethod
    def is_valid_AREALAND(self,x):
        """Area (Land)16"""
        return True
    @classmethod
    def is_valid_AREAWATR(self,x):
        """Area (Water)17"""
        return True
    @classmethod
    def is_valid_NAME(self,x):
        """Area Name-Legal/Statistical Area Description (LSAD) Term-Part Indicator18"""
        return True
    @classmethod
    def is_valid_FUNCSTAT(self,x):
        """Functional Status Code"""
        return True
    @classmethod
    def is_valid_GCUNI(self,x):
        """Geographic Change User Note Indicator"""
        return True
    @classmethod
    def is_valid_INTPTLAT(self,x):
        """Internal Point (Latitude)21"""
        return True
    @classmethod
    def is_valid_INTPTLON(self,x):
        """Internal Point (Longitude)22"""
        return True
    @classmethod
    def is_valid_LSADC(self,x):
        """Legal/Statistical Area Description Code"""
        return True
    @classmethod
    def is_valid_PARTFLAG(self,x):
        """Special Area Codes"""
        return True
    @classmethod
    def is_valid_UGA(self,x):
        """Urban Growth Area7"""
        return True
    @classmethod
    def is_valid_STATENS(self,x):
        """State (ANSI)8"""
        return True
    @classmethod
    def is_valid_COUNTYNS(self,x):
        """County (ANSI)8"""
        return True
    @classmethod
    def is_valid_COUSUBNS(self,x):
        """County Subdivision (ANSI)8"""
        return True
    @classmethod
    def is_valid_PLACENS(self,x):
        """Place (ANSI)8"""
        return True
    @classmethod
    def is_valid_CONCITNS(self,x):
        """Consolidated City (ANSI)8"""
        return True
    @classmethod
    def is_valid_AIANHHNS(self,x):
        """Hawaiian Home Land (ANSI)8"""
        return True
    @classmethod
    def is_valid_AITSNS(self,x):
        """American Indian Tribal Subdivision (ANSI)8"""
        return True
    @classmethod
    def is_valid_ANRCNS(self,x):
        """Alaska Native Regional Corporation (ANSI)8"""
        return True
    @classmethod
    def is_valid_SUBMCDNS(self,x):
        """Subminor Civil Division (ANSI)8"""
        return True
    @classmethod
    def is_valid_AIANHHSC(self,x):
        """Hawaiian Home Land Size Code9"""
        return True
    @classmethod
    def is_valid_CSASC(self,x):
        """Combined Statistical Area Size Code9"""
        return True
    @classmethod
    def is_valid_CNECTASC(self,x):
        """Combined NECTA Size Code9"""
        return True
    @classmethod
    def is_valid_MEMI(self,x):
        """Metropolitan/Micropolitan Indicator"""
        return True
    @classmethod
    def is_valid_NMEMI(self,x):
        """NECTA Metropolitan/Micropolitan Indicator"""
        return True
    @classmethod
    def is_valid_RESERVED(self,x):
        """Reserved"""
        return True

    @classmethod
    def validate_pipe_delimited(self,x):
        fields = x.split('|')
        if len(fields)!=87: return False
        if is_valid_SLDU(fields[1]) == False: return False
        if is_valid_SLDL(fields[2]) == False: return False
        if is_valid_PUMA(fields[3]) == False: return False
        if is_valid_PLACE(fields[4]) == False: return False
        if is_valid_FILEID(fields[5]) == False: return False
        if is_valid_STUSAB(fields[6]) == False: return False
        if is_valid_SUMLEV(fields[7]) == False: return False
        if is_valid_GEOCOMP(fields[8]) == False: return False
        if is_valid_CHARITER(fields[9]) == False: return False
        if is_valid_CIFSN(fields[10]) == False: return False
        if is_valid_LOGRECNO(fields[11]) == False: return False
        if is_valid_REGION(fields[12]) == False: return False
        if is_valid_DIVISION(fields[13]) == False: return False
        if is_valid_STATE(fields[14]) == False: return False
        if is_valid_COUNTY(fields[15]) == False: return False
        if is_valid_COUNTYCC(fields[16]) == False: return False
        if is_valid_COUNTYSC(fields[17]) == False: return False
        if is_valid_COUSUB(fields[18]) == False: return False
        if is_valid_COUSUBCC(fields[19]) == False: return False
        if is_valid_COUSUBSC(fields[20]) == False: return False
        if is_valid_PLACECC(fields[21]) == False: return False
        if is_valid_PLACESC(fields[22]) == False: return False
        if is_valid_TRACT(fields[23]) == False: return False
        if is_valid_BLKGRP(fields[24]) == False: return False
        if is_valid_BLOCK(fields[25]) == False: return False
        if is_valid_IUC(fields[26]) == False: return False
        if is_valid_CONCIT(fields[27]) == False: return False
        if is_valid_CONCITCC(fields[28]) == False: return False
        if is_valid_CONCITSC(fields[29]) == False: return False
        if is_valid_AIANHH(fields[30]) == False: return False
        if is_valid_AIANHHFP(fields[31]) == False: return False
        if is_valid_AIANHHCC(fields[32]) == False: return False
        if is_valid_AIHHTLI(fields[33]) == False: return False
        if is_valid_AITSCE(fields[34]) == False: return False
        if is_valid_AITSCC(fields[35]) == False: return False
        if is_valid_TTRACT(fields[36]) == False: return False
        if is_valid_TBLKGRP(fields[37]) == False: return False
        if is_valid_ANRC(fields[38]) == False: return False
        if is_valid_ANRCCC(fields[39]) == False: return False
        if is_valid_CBSA(fields[40]) == False: return False
        if is_valid_CBSASC(fields[41]) == False: return False
        if is_valid_METDIV(fields[42]) == False: return False
        if is_valid_CSA(fields[43]) == False: return False
        if is_valid_NECTA(fields[44]) == False: return False
        if is_valid_NECTASC(fields[45]) == False: return False
        if is_valid_NECTADIV(fields[46]) == False: return False
        if is_valid_CNECTA(fields[47]) == False: return False
        if is_valid_CBSAPCI(fields[48]) == False: return False
        if is_valid_NECTAPCI(fields[49]) == False: return False
        if is_valid_UA(fields[50]) == False: return False
        if is_valid_UASC(fields[51]) == False: return False
        if is_valid_UATYPE(fields[52]) == False: return False
        if is_valid_UR(fields[53]) == False: return False
        if is_valid_CD(fields[54]) == False: return False
        if is_valid_VTD(fields[55]) == False: return False
        if is_valid_VTDI(fields[56]) == False: return False
        if is_valid_ZCTA5(fields[57]) == False: return False
        if is_valid_SUBMCD(fields[58]) == False: return False
        if is_valid_SUBMCDCC(fields[59]) == False: return False
        if is_valid_SDELM(fields[60]) == False: return False
        if is_valid_SDSEC(fields[61]) == False: return False
        if is_valid_SDUNI(fields[62]) == False: return False
        if is_valid_AREALAND(fields[63]) == False: return False
        if is_valid_AREAWATR(fields[64]) == False: return False
        if is_valid_NAME(fields[65]) == False: return False
        if is_valid_FUNCSTAT(fields[66]) == False: return False
        if is_valid_GCUNI(fields[67]) == False: return False
        if is_valid_INTPTLAT(fields[68]) == False: return False
        if is_valid_INTPTLON(fields[69]) == False: return False
        if is_valid_LSADC(fields[70]) == False: return False
        if is_valid_PARTFLAG(fields[71]) == False: return False
        if is_valid_UGA(fields[72]) == False: return False
        if is_valid_STATENS(fields[73]) == False: return False
        if is_valid_COUNTYNS(fields[74]) == False: return False
        if is_valid_COUSUBNS(fields[75]) == False: return False
        if is_valid_PLACENS(fields[76]) == False: return False
        if is_valid_CONCITNS(fields[77]) == False: return False
        if is_valid_AIANHHNS(fields[78]) == False: return False
        if is_valid_AITSNS(fields[79]) == False: return False
        if is_valid_ANRCNS(fields[80]) == False: return False
        if is_valid_SUBMCDNS(fields[81]) == False: return False
        if is_valid_AIANHHSC(fields[82]) == False: return False
        if is_valid_CSASC(fields[83]) == False: return False
        if is_valid_CNECTASC(fields[84]) == False: return False
        if is_valid_MEMI(fields[85]) == False: return False
        if is_valid_NMEMI(fields[86]) == False: return False
        if is_valid_RESERVED(fields[87]) == False: return False
        return True

class geo:
    __slots__ = ['SLDU', 'SLDL', 'PUMA', 'PLACE', 'FILEID', 'STUSAB', 'SUMLEV', 'GEOCOMP', 'CHARITER', 'CIFSN', 'LOGRECNO', 'REGION', 'DIVISION', 'STATE', 'COUNTY', 'COUNTYCC', 'COUNTYSC', 'COUSUB', 'COUSUBCC', 'COUSUBSC', 'PLACECC', 'PLACESC', 'TRACT', 'BLKGRP', 'BLOCK', 'IUC', 'CONCIT', 'CONCITCC', 'CONCITSC', 'AIANHH', 'AIANHHFP', 'AIANHHCC', 'AIHHTLI', 'AITSCE', 'AITSCC', 'TTRACT', 'TBLKGRP', 'ANRC', 'ANRCCC', 'CBSA', 'CBSASC', 'METDIV', 'CSA', 'NECTA', 'NECTASC', 'NECTADIV', 'CNECTA', 'CBSAPCI', 'NECTAPCI', 'UA', 'UASC', 'UATYPE', 'UR', 'CD', 'VTD', 'VTDI', 'ZCTA5', 'SUBMCD', 'SUBMCDCC', 'SDELM', 'SDSEC', 'SDUNI', 'AREALAND', 'AREAWATR', 'NAME', 'FUNCSTAT', 'GCUNI', 'INTPTLAT', 'INTPTLON', 'LSADC', 'PARTFLAG', 'UGA', 'STATENS', 'COUNTYNS', 'COUSUBNS', 'PLACENS', 'CONCITNS', 'AIANHHNS', 'AITSNS', 'ANRCNS', 'SUBMCDNS', 'AIANHHSC', 'CSASC', 'CNECTASC', 'MEMI', 'NMEMI', 'RESERVED']
    def __repr__(self):
        return 'geo<SLDU:{},SLDL:{},PUMA:{},PLACE:{},FILEID:{},STUSAB:{},SUMLEV:{},GEOCOMP:{},CHARITER:{},CIFSN:{},LOGRECNO:{},REGION:{},DIVISION:{},STATE:{},COUNTY:{},COUNTYCC:{},COUNTYSC:{},COUSUB:{},COUSUBCC:{},COUSUBSC:{},PLACECC:{},PLACESC:{},TRACT:{},BLKGRP:{},BLOCK:{},IUC:{},CONCIT:{},CONCITCC:{},CONCITSC:{},AIANHH:{},AIANHHFP:{},AIANHHCC:{},AIHHTLI:{},AITSCE:{},AITSCC:{},TTRACT:{},TBLKGRP:{},ANRC:{},ANRCCC:{},CBSA:{},CBSASC:{},METDIV:{},CSA:{},NECTA:{},NECTASC:{},NECTADIV:{},CNECTA:{},CBSAPCI:{},NECTAPCI:{},UA:{},UASC:{},UATYPE:{},UR:{},CD:{},VTD:{},VTDI:{},ZCTA5:{},SUBMCD:{},SUBMCDCC:{},SDELM:{},SDSEC:{},SDUNI:{},AREALAND:{},AREAWATR:{},NAME:{},FUNCSTAT:{},GCUNI:{},INTPTLAT:{},INTPTLON:{},LSADC:{},PARTFLAG:{},UGA:{},STATENS:{},COUNTYNS:{},COUSUBNS:{},PLACENS:{},CONCITNS:{},AIANHHNS:{},AITSNS:{},ANRCNS:{},SUBMCDNS:{},AIANHHSC:{},CSASC:{},CNECTASC:{},MEMI:{},NMEMI:{},RESERVED:{}>'.format(self.SLDU,self.SLDL,self.PUMA,self.PLACE,self.FILEID,self.STUSAB,self.SUMLEV,self.GEOCOMP,self.CHARITER,self.CIFSN,self.LOGRECNO,self.REGION,self.DIVISION,self.STATE,self.COUNTY,self.COUNTYCC,self.COUNTYSC,self.COUSUB,self.COUSUBCC,self.COUSUBSC,self.PLACECC,self.PLACESC,self.TRACT,self.BLKGRP,self.BLOCK,self.IUC,self.CONCIT,self.CONCITCC,self.CONCITSC,self.AIANHH,self.AIANHHFP,self.AIANHHCC,self.AIHHTLI,self.AITSCE,self.AITSCC,self.TTRACT,self.TBLKGRP,self.ANRC,self.ANRCCC,self.CBSA,self.CBSASC,self.METDIV,self.CSA,self.NECTA,self.NECTASC,self.NECTADIV,self.CNECTA,self.CBSAPCI,self.NECTAPCI,self.UA,self.UASC,self.UATYPE,self.UR,self.CD,self.VTD,self.VTDI,self.ZCTA5,self.SUBMCD,self.SUBMCDCC,self.SDELM,self.SDSEC,self.SDUNI,self.AREALAND,self.AREAWATR,self.NAME,self.FUNCSTAT,self.GCUNI,self.INTPTLAT,self.INTPTLON,self.LSADC,self.PARTFLAG,self.UGA,self.STATENS,self.COUNTYNS,self.COUSUBNS,self.PLACENS,self.CONCITNS,self.AIANHHNS,self.AITSNS,self.ANRCNS,self.SUBMCDNS,self.AIANHHSC,self.CSASC,self.CNECTASC,self.MEMI,self.NMEMI,self.RESERVED)
    def __init__(self,line=None):
        if line: 
            if '|' in line: 
                self.parse_pipe_delimited(line)
            else:
                self.parse_column_specified(line)
    @classmethod
    def name(self):
        return 'geo'

    def parse_pipe_delimited(self,line):
        fields = line.split('|')
        if len(fields)!=87:
            raise ValueError(f'expected 87 fields, found {len(fields)}')
        self.SLDU            = fields[0]  # 
        self.SLDL            = fields[1]  # 
        self.PUMA            = fields[2]  # 
        self.PLACE           = fields[3]  # 
        self.FILEID          = fields[4]  # File Identification1
        self.STUSAB          = fields[5]  # State/U.S. Abbreviation (USPS)
        self.SUMLEV          = fields[6]  # Summary Level2
        self.GEOCOMP         = fields[7]  # Geographic Component3
        self.CHARITER        = fields[8]  # Characteristic Iteration4
        self.CIFSN           = fields[9]  # Characteristic Iteration File Sequence Number5
        self.LOGRECNO        = fields[10]  # Logical Record Number6
        self.REGION          = fields[11]  # Region7
        self.DIVISION        = fields[12]  # Division7
        self.STATE           = fields[13]  # State (FIPS)7 8
        self.COUNTY          = fields[14]  # County7 8
        self.COUNTYCC        = fields[15]  # FIPS County Class Code8
        self.COUNTYSC        = fields[16]  # County Size Code9
        self.COUSUB          = fields[17]  # County Subdivision (FIPS)7 8
        self.COUSUBCC        = fields[18]  # FIPS County Subdivision Class Code8
        self.COUSUBSC        = fields[19]  # County Subdivision Size Code9
        self.PLACECC         = fields[20]  # FIPS Place Class Code8
        self.PLACESC         = fields[21]  # Place Size Code9
        self.TRACT           = fields[22]  # Census Tract7
        self.BLKGRP          = fields[23]  # Block Group7
        self.BLOCK           = fields[24]  # Block7
        self.IUC             = fields[25]  # Internal Use Code10
        self.CONCIT          = fields[26]  # Consolidated City (FIPS)7 8
        self.CONCITCC        = fields[27]  # C3 Consolidated city
        self.CONCITSC        = fields[28]  # Consolidated City Size Code9
        self.AIANHH          = fields[29]  # American Indian Area/Alaska Native Area/ Hawaiian Home Land (Census)7
        self.AIANHHFP        = fields[30]  # Hawaiian Home Land (FIPS)7 8 11
        self.AIANHHCC        = fields[31]  # Hawaiian Home Land Class Code8
        self.AIHHTLI         = fields[32]  # Land Indicator
        self.AITSCE          = fields[33]  # American Indian Tribal Subdivision (Census)7
        self.AITSCC          = fields[34]  # Class Code8
        self.TTRACT          = fields[35]  # Tribal Census Tract
        self.TBLKGRP         = fields[36]  # Tribal Block Group
        self.ANRC            = fields[37]  # Alaska Native Regional Corporation (FIPS)7 8
        self.ANRCCC          = fields[38]  # Class Code8
        self.CBSA            = fields[39]  # Statistical Area7 8
        self.CBSASC          = fields[40]  # Statistical Area Size Code9
        self.METDIV          = fields[41]  # Metropolitan Division7 8
        self.CSA             = fields[42]  # Combined Statistical Area7 8
        self.NECTA           = fields[43]  # New England City and Town Area7 8
        self.NECTASC         = fields[44]  # New England City and Town Area Size Code9
        self.NECTADIV        = fields[45]  # New England City and Town Area Division7 8
        self.CNECTA          = fields[46]  # Combined New England City and Town Area7 8
        self.CBSAPCI         = fields[47]  # Statistical Area Principal City Indicator7
        self.NECTAPCI        = fields[48]  # Indicator7
        self.UA              = fields[49]  # Urban Area7 12
        self.UASC            = fields[50]  # Urban Area Size Code9 12
        self.UATYPE          = fields[51]  # Urban Area Type7 12
        self.UR              = fields[52]  # Urban/Rural7 12
        self.CD              = fields[53]  # Congressional District (111th)7 8 13
        self.VTD             = fields[54]  # Voting District7 15
        self.VTDI            = fields[55]  # Voting District Indicator7
        self.ZCTA5           = fields[56]  # ZIP Code Tabulation Area (5-digit)7 12
        self.SUBMCD          = fields[57]  # Subminor Civil Division (FIPS)7 8
        self.SUBMCDCC        = fields[58]  # FIPS Subminor Civil Division Class Code8
        self.SDELM           = fields[59]  # School District (Elementary)7
        self.SDSEC           = fields[60]  # School District (Secondary)7
        self.SDUNI           = fields[61]  # School District (Unified)7
        self.AREALAND        = fields[62]  # Area (Land)16
        self.AREAWATR        = fields[63]  # Area (Water)17
        self.NAME            = fields[64]  # Area Name-Legal/Statistical Area Description (LSAD) Term-Part Indicator18
        self.FUNCSTAT        = fields[65]  # Functional Status Code
        self.GCUNI           = fields[66]  # Geographic Change User Note Indicator
        self.INTPTLAT        = fields[67]  # Internal Point (Latitude)21
        self.INTPTLON        = fields[68]  # Internal Point (Longitude)22
        self.LSADC           = fields[69]  # Legal/Statistical Area Description Code
        self.PARTFLAG        = fields[70]  # Special Area Codes
        self.UGA             = fields[71]  # Urban Growth Area7
        self.STATENS         = fields[72]  # State (ANSI)8
        self.COUNTYNS        = fields[73]  # County (ANSI)8
        self.COUSUBNS        = fields[74]  # County Subdivision (ANSI)8
        self.PLACENS         = fields[75]  # Place (ANSI)8
        self.CONCITNS        = fields[76]  # Consolidated City (ANSI)8
        self.AIANHHNS        = fields[77]  # Hawaiian Home Land (ANSI)8
        self.AITSNS          = fields[78]  # American Indian Tribal Subdivision (ANSI)8
        self.ANRCNS          = fields[79]  # Alaska Native Regional Corporation (ANSI)8
        self.SUBMCDNS        = fields[80]  # Subminor Civil Division (ANSI)8
        self.AIANHHSC        = fields[81]  # Hawaiian Home Land Size Code9
        self.CSASC           = fields[82]  # Combined Statistical Area Size Code9
        self.CNECTASC        = fields[83]  # Combined NECTA Size Code9
        self.MEMI            = fields[84]  # Metropolitan/Micropolitan Indicator
        self.NMEMI           = fields[85]  # NECTA Metropolitan/Micropolitan Indicator
        self.RESERVED        = fields[86]  # Reserved

    def parse_column_specified(self,line):
        self.SLDU            = line[155:158] # 
        self.SLDL            = line[158:161] # 
        self.PUMA            = line[477:482] # 
        self.PLACE           = line[45:50] # 
        self.FILEID          = line[0:6] # File Identification1
        self.STUSAB          = line[6:8] # State/U.S. Abbreviation (USPS)
        self.SUMLEV          = line[8:11] # Summary Level2
        self.GEOCOMP         = line[11:13] # Geographic Component3
        self.CHARITER        = line[13:16] # Characteristic Iteration4
        self.CIFSN           = line[16:18] # Characteristic Iteration File Sequence Number5
        self.LOGRECNO        = line[18:25] # Logical Record Number6
        self.REGION          = line[25:26] # Region7
        self.DIVISION        = line[26:27] # Division7
        self.STATE           = line[27:29] # State (FIPS)7 8
        self.COUNTY          = line[29:32] # County7 8
        self.COUNTYCC        = line[32:34] # FIPS County Class Code8
        self.COUNTYSC        = line[34:36] # County Size Code9
        self.COUSUB          = line[36:41] # County Subdivision (FIPS)7 8
        self.COUSUBCC        = line[41:43] # FIPS County Subdivision Class Code8
        self.COUSUBSC        = line[43:45] # County Subdivision Size Code9
        self.PLACECC         = line[50:52] # FIPS Place Class Code8
        self.PLACESC         = line[52:54] # Place Size Code9
        self.TRACT           = line[54:60] # Census Tract7
        self.BLKGRP          = line[60:61] # Block Group7
        self.BLOCK           = line[61:65] # Block7
        self.IUC             = line[65:67] # Internal Use Code10
        self.CONCIT          = line[67:72] # Consolidated City (FIPS)7 8
        self.CONCITCC        = line[72:74] # C3 Consolidated city
        self.CONCITSC        = line[74:76] # Consolidated City Size Code9
        self.AIANHH          = line[76:80] # American Indian Area/Alaska Native Area/ Hawaiian Home Land (Census)7
        self.AIANHHFP        = line[80:85] # Hawaiian Home Land (FIPS)7 8 11
        self.AIANHHCC        = line[85:87] # Hawaiian Home Land Class Code8
        self.AIHHTLI         = line[87:88] # Land Indicator
        self.AITSCE          = line[88:91] # American Indian Tribal Subdivision (Census)7
        self.AITSCC          = line[96:98] # Class Code8
        self.TTRACT          = line[98:104] # Tribal Census Tract
        self.TBLKGRP         = line[104:105] # Tribal Block Group
        self.ANRC            = line[105:110] # Alaska Native Regional Corporation (FIPS)7 8
        self.ANRCCC          = line[110:112] # Class Code8
        self.CBSA            = line[112:117] # Statistical Area7 8
        self.CBSASC          = line[117:119] # Statistical Area Size Code9
        self.METDIV          = line[119:124] # Metropolitan Division7 8
        self.CSA             = line[124:127] # Combined Statistical Area7 8
        self.NECTA           = line[127:132] # New England City and Town Area7 8
        self.NECTASC         = line[132:134] # New England City and Town Area Size Code9
        self.NECTADIV        = line[134:139] # New England City and Town Area Division7 8
        self.CNECTA          = line[139:142] # Combined New England City and Town Area7 8
        self.CBSAPCI         = line[142:143] # Statistical Area Principal City Indicator7
        self.NECTAPCI        = line[143:144] # Indicator7
        self.UA              = line[144:149] # Urban Area7 12
        self.UASC            = line[149:151] # Urban Area Size Code9 12
        self.UATYPE          = line[151:152] # Urban Area Type7 12
        self.UR              = line[152:153] # Urban/Rural7 12
        self.CD              = line[153:155] # Congressional District (111th)7 8 13
        self.VTD             = line[161:167] # Voting District7 15
        self.VTDI            = line[167:168] # Voting District Indicator7
        self.ZCTA5           = line[171:176] # ZIP Code Tabulation Area (5-digit)7 12
        self.SUBMCD          = line[176:181] # Subminor Civil Division (FIPS)7 8
        self.SUBMCDCC        = line[181:183] # FIPS Subminor Civil Division Class Code8
        self.SDELM           = line[183:188] # School District (Elementary)7
        self.SDSEC           = line[188:193] # School District (Secondary)7
        self.SDUNI           = line[193:198] # School District (Unified)7
        self.AREALAND        = line[198:212] # Area (Land)16
        self.AREAWATR        = line[212:226] # Area (Water)17
        self.NAME            = line[226:316] # Area Name-Legal/Statistical Area Description (LSAD) Term-Part Indicator18
        self.FUNCSTAT        = line[316:317] # Functional Status Code
        self.GCUNI           = line[317:318] # Geographic Change User Note Indicator
        self.INTPTLAT        = line[336:347] # Internal Point (Latitude)21
        self.INTPTLON        = line[347:359] # Internal Point (Longitude)22
        self.LSADC           = line[359:361] # Legal/Statistical Area Description Code
        self.PARTFLAG        = line[361:362] # Special Area Codes
        self.UGA             = line[368:373] # Urban Growth Area7
        self.STATENS         = line[373:381] # State (ANSI)8
        self.COUNTYNS        = line[381:389] # County (ANSI)8
        self.COUSUBNS        = line[389:397] # County Subdivision (ANSI)8
        self.PLACENS         = line[397:405] # Place (ANSI)8
        self.CONCITNS        = line[405:413] # Consolidated City (ANSI)8
        self.AIANHHNS        = line[413:421] # Hawaiian Home Land (ANSI)8
        self.AITSNS          = line[421:429] # American Indian Tribal Subdivision (ANSI)8
        self.ANRCNS          = line[429:437] # Alaska Native Regional Corporation (ANSI)8
        self.SUBMCDNS        = line[437:445] # Subminor Civil Division (ANSI)8
        self.AIANHHSC        = line[469:471] # Hawaiian Home Land Size Code9
        self.CSASC           = line[471:473] # Combined Statistical Area Size Code9
        self.CNECTASC        = line[473:475] # Combined NECTA Size Code9
        self.MEMI            = line[475:476] # Metropolitan/Micropolitan Indicator
        self.NMEMI           = line[476:477] # NECTA Metropolitan/Micropolitan Indicator
        self.RESERVED        = line[482:500] # Reserved

    def validate(self):
        """Return True if the object data validates"""
        if not geo_validator.is_valid_SLDU(self.SLDU): return False
        if not geo_validator.is_valid_SLDL(self.SLDL): return False
        if not geo_validator.is_valid_PUMA(self.PUMA): return False
        if not geo_validator.is_valid_PLACE(self.PLACE): return False
        if not geo_validator.is_valid_FILEID(self.FILEID): return False
        if not geo_validator.is_valid_STUSAB(self.STUSAB): return False
        if not geo_validator.is_valid_SUMLEV(self.SUMLEV): return False
        if not geo_validator.is_valid_GEOCOMP(self.GEOCOMP): return False
        if not geo_validator.is_valid_CHARITER(self.CHARITER): return False
        if not geo_validator.is_valid_CIFSN(self.CIFSN): return False
        if not geo_validator.is_valid_LOGRECNO(self.LOGRECNO): return False
        if not geo_validator.is_valid_REGION(self.REGION): return False
        if not geo_validator.is_valid_DIVISION(self.DIVISION): return False
        if not geo_validator.is_valid_STATE(self.STATE): return False
        if not geo_validator.is_valid_COUNTY(self.COUNTY): return False
        if not geo_validator.is_valid_COUNTYCC(self.COUNTYCC): return False
        if not geo_validator.is_valid_COUNTYSC(self.COUNTYSC): return False
        if not geo_validator.is_valid_COUSUB(self.COUSUB): return False
        if not geo_validator.is_valid_COUSUBCC(self.COUSUBCC): return False
        if not geo_validator.is_valid_COUSUBSC(self.COUSUBSC): return False
        if not geo_validator.is_valid_PLACECC(self.PLACECC): return False
        if not geo_validator.is_valid_PLACESC(self.PLACESC): return False
        if not geo_validator.is_valid_TRACT(self.TRACT): return False
        if not geo_validator.is_valid_BLKGRP(self.BLKGRP): return False
        if not geo_validator.is_valid_BLOCK(self.BLOCK): return False
        if not geo_validator.is_valid_IUC(self.IUC): return False
        if not geo_validator.is_valid_CONCIT(self.CONCIT): return False
        if not geo_validator.is_valid_CONCITCC(self.CONCITCC): return False
        if not geo_validator.is_valid_CONCITSC(self.CONCITSC): return False
        if not geo_validator.is_valid_AIANHH(self.AIANHH): return False
        if not geo_validator.is_valid_AIANHHFP(self.AIANHHFP): return False
        if not geo_validator.is_valid_AIANHHCC(self.AIANHHCC): return False
        if not geo_validator.is_valid_AIHHTLI(self.AIHHTLI): return False
        if not geo_validator.is_valid_AITSCE(self.AITSCE): return False
        if not geo_validator.is_valid_AITSCC(self.AITSCC): return False
        if not geo_validator.is_valid_TTRACT(self.TTRACT): return False
        if not geo_validator.is_valid_TBLKGRP(self.TBLKGRP): return False
        if not geo_validator.is_valid_ANRC(self.ANRC): return False
        if not geo_validator.is_valid_ANRCCC(self.ANRCCC): return False
        if not geo_validator.is_valid_CBSA(self.CBSA): return False
        if not geo_validator.is_valid_CBSASC(self.CBSASC): return False
        if not geo_validator.is_valid_METDIV(self.METDIV): return False
        if not geo_validator.is_valid_CSA(self.CSA): return False
        if not geo_validator.is_valid_NECTA(self.NECTA): return False
        if not geo_validator.is_valid_NECTASC(self.NECTASC): return False
        if not geo_validator.is_valid_NECTADIV(self.NECTADIV): return False
        if not geo_validator.is_valid_CNECTA(self.CNECTA): return False
        if not geo_validator.is_valid_CBSAPCI(self.CBSAPCI): return False
        if not geo_validator.is_valid_NECTAPCI(self.NECTAPCI): return False
        if not geo_validator.is_valid_UA(self.UA): return False
        if not geo_validator.is_valid_UASC(self.UASC): return False
        if not geo_validator.is_valid_UATYPE(self.UATYPE): return False
        if not geo_validator.is_valid_UR(self.UR): return False
        if not geo_validator.is_valid_CD(self.CD): return False
        if not geo_validator.is_valid_VTD(self.VTD): return False
        if not geo_validator.is_valid_VTDI(self.VTDI): return False
        if not geo_validator.is_valid_ZCTA5(self.ZCTA5): return False
        if not geo_validator.is_valid_SUBMCD(self.SUBMCD): return False
        if not geo_validator.is_valid_SUBMCDCC(self.SUBMCDCC): return False
        if not geo_validator.is_valid_SDELM(self.SDELM): return False
        if not geo_validator.is_valid_SDSEC(self.SDSEC): return False
        if not geo_validator.is_valid_SDUNI(self.SDUNI): return False
        if not geo_validator.is_valid_AREALAND(self.AREALAND): return False
        if not geo_validator.is_valid_AREAWATR(self.AREAWATR): return False
        if not geo_validator.is_valid_NAME(self.NAME): return False
        if not geo_validator.is_valid_FUNCSTAT(self.FUNCSTAT): return False
        if not geo_validator.is_valid_GCUNI(self.GCUNI): return False
        if not geo_validator.is_valid_INTPTLAT(self.INTPTLAT): return False
        if not geo_validator.is_valid_INTPTLON(self.INTPTLON): return False
        if not geo_validator.is_valid_LSADC(self.LSADC): return False
        if not geo_validator.is_valid_PARTFLAG(self.PARTFLAG): return False
        if not geo_validator.is_valid_UGA(self.UGA): return False
        if not geo_validator.is_valid_STATENS(self.STATENS): return False
        if not geo_validator.is_valid_COUNTYNS(self.COUNTYNS): return False
        if not geo_validator.is_valid_COUSUBNS(self.COUSUBNS): return False
        if not geo_validator.is_valid_PLACENS(self.PLACENS): return False
        if not geo_validator.is_valid_CONCITNS(self.CONCITNS): return False
        if not geo_validator.is_valid_AIANHHNS(self.AIANHHNS): return False
        if not geo_validator.is_valid_AITSNS(self.AITSNS): return False
        if not geo_validator.is_valid_ANRCNS(self.ANRCNS): return False
        if not geo_validator.is_valid_SUBMCDNS(self.SUBMCDNS): return False
        if not geo_validator.is_valid_AIANHHSC(self.AIANHHSC): return False
        if not geo_validator.is_valid_CSASC(self.CSASC): return False
        if not geo_validator.is_valid_CNECTASC(self.CNECTASC): return False
        if not geo_validator.is_valid_MEMI(self.MEMI): return False
        if not geo_validator.is_valid_NMEMI(self.NMEMI): return False
        if not geo_validator.is_valid_RESERVED(self.RESERVED): return False
        return True

    def validate_reason(self):
        reason=[]
        if not geo_validator.is_valid_SLDU(self.SLDU): reason.append('SLDU ('+str(self.SLDU)+') out of range ()')
        if not geo_validator.is_valid_SLDL(self.SLDL): reason.append('SLDL ('+str(self.SLDL)+') out of range ()')
        if not geo_validator.is_valid_PUMA(self.PUMA): reason.append('PUMA ('+str(self.PUMA)+') out of range ()')
        if not geo_validator.is_valid_PLACE(self.PLACE): reason.append('PLACE ('+str(self.PLACE)+') out of range ()')
        if not geo_validator.is_valid_FILEID(self.FILEID): reason.append('FILEID ('+str(self.FILEID)+') out of range ()')
        if not geo_validator.is_valid_STUSAB(self.STUSAB): reason.append('STUSAB ('+str(self.STUSAB)+') out of range ()')
        if not geo_validator.is_valid_SUMLEV(self.SUMLEV): reason.append('SUMLEV ('+str(self.SUMLEV)+') out of range ()')
        if not geo_validator.is_valid_GEOCOMP(self.GEOCOMP): reason.append('GEOCOMP ('+str(self.GEOCOMP)+') out of range ()')
        if not geo_validator.is_valid_CHARITER(self.CHARITER): reason.append('CHARITER ('+str(self.CHARITER)+') out of range ()')
        if not geo_validator.is_valid_CIFSN(self.CIFSN): reason.append('CIFSN ('+str(self.CIFSN)+') out of range ()')
        if not geo_validator.is_valid_LOGRECNO(self.LOGRECNO): reason.append('LOGRECNO ('+str(self.LOGRECNO)+') out of range ()')
        if not geo_validator.is_valid_REGION(self.REGION): reason.append('REGION ('+str(self.REGION)+') out of range ()')
        if not geo_validator.is_valid_DIVISION(self.DIVISION): reason.append('DIVISION ('+str(self.DIVISION)+') out of range ()')
        if not geo_validator.is_valid_STATE(self.STATE): reason.append('STATE ('+str(self.STATE)+') out of range ()')
        if not geo_validator.is_valid_COUNTY(self.COUNTY): reason.append('COUNTY ('+str(self.COUNTY)+') out of range ()')
        if not geo_validator.is_valid_COUNTYCC(self.COUNTYCC): reason.append('COUNTYCC ('+str(self.COUNTYCC)+') out of range ()')
        if not geo_validator.is_valid_COUNTYSC(self.COUNTYSC): reason.append('COUNTYSC ('+str(self.COUNTYSC)+') out of range ()')
        if not geo_validator.is_valid_COUSUB(self.COUSUB): reason.append('COUSUB ('+str(self.COUSUB)+') out of range ()')
        if not geo_validator.is_valid_COUSUBCC(self.COUSUBCC): reason.append('COUSUBCC ('+str(self.COUSUBCC)+') out of range ()')
        if not geo_validator.is_valid_COUSUBSC(self.COUSUBSC): reason.append('COUSUBSC ('+str(self.COUSUBSC)+') out of range ()')
        if not geo_validator.is_valid_PLACECC(self.PLACECC): reason.append('PLACECC ('+str(self.PLACECC)+') out of range ()')
        if not geo_validator.is_valid_PLACESC(self.PLACESC): reason.append('PLACESC ('+str(self.PLACESC)+') out of range ()')
        if not geo_validator.is_valid_TRACT(self.TRACT): reason.append('TRACT ('+str(self.TRACT)+') out of range ()')
        if not geo_validator.is_valid_BLKGRP(self.BLKGRP): reason.append('BLKGRP ('+str(self.BLKGRP)+') out of range ()')
        if not geo_validator.is_valid_BLOCK(self.BLOCK): reason.append('BLOCK ('+str(self.BLOCK)+') out of range ()')
        if not geo_validator.is_valid_IUC(self.IUC): reason.append('IUC ('+str(self.IUC)+') out of range ()')
        if not geo_validator.is_valid_CONCIT(self.CONCIT): reason.append('CONCIT ('+str(self.CONCIT)+') out of range ()')
        if not geo_validator.is_valid_CONCITCC(self.CONCITCC): reason.append('CONCITCC ('+str(self.CONCITCC)+') out of range ()')
        if not geo_validator.is_valid_CONCITSC(self.CONCITSC): reason.append('CONCITSC ('+str(self.CONCITSC)+') out of range ()')
        if not geo_validator.is_valid_AIANHH(self.AIANHH): reason.append('AIANHH ('+str(self.AIANHH)+') out of range ()')
        if not geo_validator.is_valid_AIANHHFP(self.AIANHHFP): reason.append('AIANHHFP ('+str(self.AIANHHFP)+') out of range ()')
        if not geo_validator.is_valid_AIANHHCC(self.AIANHHCC): reason.append('AIANHHCC ('+str(self.AIANHHCC)+') out of range ()')
        if not geo_validator.is_valid_AIHHTLI(self.AIHHTLI): reason.append('AIHHTLI ('+str(self.AIHHTLI)+') out of range ()')
        if not geo_validator.is_valid_AITSCE(self.AITSCE): reason.append('AITSCE ('+str(self.AITSCE)+') out of range ()')
        if not geo_validator.is_valid_AITSCC(self.AITSCC): reason.append('AITSCC ('+str(self.AITSCC)+') out of range ()')
        if not geo_validator.is_valid_TTRACT(self.TTRACT): reason.append('TTRACT ('+str(self.TTRACT)+') out of range ()')
        if not geo_validator.is_valid_TBLKGRP(self.TBLKGRP): reason.append('TBLKGRP ('+str(self.TBLKGRP)+') out of range ()')
        if not geo_validator.is_valid_ANRC(self.ANRC): reason.append('ANRC ('+str(self.ANRC)+') out of range ()')
        if not geo_validator.is_valid_ANRCCC(self.ANRCCC): reason.append('ANRCCC ('+str(self.ANRCCC)+') out of range ()')
        if not geo_validator.is_valid_CBSA(self.CBSA): reason.append('CBSA ('+str(self.CBSA)+') out of range ()')
        if not geo_validator.is_valid_CBSASC(self.CBSASC): reason.append('CBSASC ('+str(self.CBSASC)+') out of range ()')
        if not geo_validator.is_valid_METDIV(self.METDIV): reason.append('METDIV ('+str(self.METDIV)+') out of range ()')
        if not geo_validator.is_valid_CSA(self.CSA): reason.append('CSA ('+str(self.CSA)+') out of range ()')
        if not geo_validator.is_valid_NECTA(self.NECTA): reason.append('NECTA ('+str(self.NECTA)+') out of range ()')
        if not geo_validator.is_valid_NECTASC(self.NECTASC): reason.append('NECTASC ('+str(self.NECTASC)+') out of range ()')
        if not geo_validator.is_valid_NECTADIV(self.NECTADIV): reason.append('NECTADIV ('+str(self.NECTADIV)+') out of range ()')
        if not geo_validator.is_valid_CNECTA(self.CNECTA): reason.append('CNECTA ('+str(self.CNECTA)+') out of range ()')
        if not geo_validator.is_valid_CBSAPCI(self.CBSAPCI): reason.append('CBSAPCI ('+str(self.CBSAPCI)+') out of range ()')
        if not geo_validator.is_valid_NECTAPCI(self.NECTAPCI): reason.append('NECTAPCI ('+str(self.NECTAPCI)+') out of range ()')
        if not geo_validator.is_valid_UA(self.UA): reason.append('UA ('+str(self.UA)+') out of range ()')
        if not geo_validator.is_valid_UASC(self.UASC): reason.append('UASC ('+str(self.UASC)+') out of range ()')
        if not geo_validator.is_valid_UATYPE(self.UATYPE): reason.append('UATYPE ('+str(self.UATYPE)+') out of range ()')
        if not geo_validator.is_valid_UR(self.UR): reason.append('UR ('+str(self.UR)+') out of range ()')
        if not geo_validator.is_valid_CD(self.CD): reason.append('CD ('+str(self.CD)+') out of range ()')
        if not geo_validator.is_valid_VTD(self.VTD): reason.append('VTD ('+str(self.VTD)+') out of range ()')
        if not geo_validator.is_valid_VTDI(self.VTDI): reason.append('VTDI ('+str(self.VTDI)+') out of range ()')
        if not geo_validator.is_valid_ZCTA5(self.ZCTA5): reason.append('ZCTA5 ('+str(self.ZCTA5)+') out of range ()')
        if not geo_validator.is_valid_SUBMCD(self.SUBMCD): reason.append('SUBMCD ('+str(self.SUBMCD)+') out of range ()')
        if not geo_validator.is_valid_SUBMCDCC(self.SUBMCDCC): reason.append('SUBMCDCC ('+str(self.SUBMCDCC)+') out of range ()')
        if not geo_validator.is_valid_SDELM(self.SDELM): reason.append('SDELM ('+str(self.SDELM)+') out of range ()')
        if not geo_validator.is_valid_SDSEC(self.SDSEC): reason.append('SDSEC ('+str(self.SDSEC)+') out of range ()')
        if not geo_validator.is_valid_SDUNI(self.SDUNI): reason.append('SDUNI ('+str(self.SDUNI)+') out of range ()')
        if not geo_validator.is_valid_AREALAND(self.AREALAND): reason.append('AREALAND ('+str(self.AREALAND)+') out of range ()')
        if not geo_validator.is_valid_AREAWATR(self.AREAWATR): reason.append('AREAWATR ('+str(self.AREAWATR)+') out of range ()')
        if not geo_validator.is_valid_NAME(self.NAME): reason.append('NAME ('+str(self.NAME)+') out of range ()')
        if not geo_validator.is_valid_FUNCSTAT(self.FUNCSTAT): reason.append('FUNCSTAT ('+str(self.FUNCSTAT)+') out of range ()')
        if not geo_validator.is_valid_GCUNI(self.GCUNI): reason.append('GCUNI ('+str(self.GCUNI)+') out of range ()')
        if not geo_validator.is_valid_INTPTLAT(self.INTPTLAT): reason.append('INTPTLAT ('+str(self.INTPTLAT)+') out of range ()')
        if not geo_validator.is_valid_INTPTLON(self.INTPTLON): reason.append('INTPTLON ('+str(self.INTPTLON)+') out of range ()')
        if not geo_validator.is_valid_LSADC(self.LSADC): reason.append('LSADC ('+str(self.LSADC)+') out of range ()')
        if not geo_validator.is_valid_PARTFLAG(self.PARTFLAG): reason.append('PARTFLAG ('+str(self.PARTFLAG)+') out of range ()')
        if not geo_validator.is_valid_UGA(self.UGA): reason.append('UGA ('+str(self.UGA)+') out of range ()')
        if not geo_validator.is_valid_STATENS(self.STATENS): reason.append('STATENS ('+str(self.STATENS)+') out of range ()')
        if not geo_validator.is_valid_COUNTYNS(self.COUNTYNS): reason.append('COUNTYNS ('+str(self.COUNTYNS)+') out of range ()')
        if not geo_validator.is_valid_COUSUBNS(self.COUSUBNS): reason.append('COUSUBNS ('+str(self.COUSUBNS)+') out of range ()')
        if not geo_validator.is_valid_PLACENS(self.PLACENS): reason.append('PLACENS ('+str(self.PLACENS)+') out of range ()')
        if not geo_validator.is_valid_CONCITNS(self.CONCITNS): reason.append('CONCITNS ('+str(self.CONCITNS)+') out of range ()')
        if not geo_validator.is_valid_AIANHHNS(self.AIANHHNS): reason.append('AIANHHNS ('+str(self.AIANHHNS)+') out of range ()')
        if not geo_validator.is_valid_AITSNS(self.AITSNS): reason.append('AITSNS ('+str(self.AITSNS)+') out of range ()')
        if not geo_validator.is_valid_ANRCNS(self.ANRCNS): reason.append('ANRCNS ('+str(self.ANRCNS)+') out of range ()')
        if not geo_validator.is_valid_SUBMCDNS(self.SUBMCDNS): reason.append('SUBMCDNS ('+str(self.SUBMCDNS)+') out of range ()')
        if not geo_validator.is_valid_AIANHHSC(self.AIANHHSC): reason.append('AIANHHSC ('+str(self.AIANHHSC)+') out of range ()')
        if not geo_validator.is_valid_CSASC(self.CSASC): reason.append('CSASC ('+str(self.CSASC)+') out of range ()')
        if not geo_validator.is_valid_CNECTASC(self.CNECTASC): reason.append('CNECTASC ('+str(self.CNECTASC)+') out of range ()')
        if not geo_validator.is_valid_MEMI(self.MEMI): reason.append('MEMI ('+str(self.MEMI)+') out of range ()')
        if not geo_validator.is_valid_NMEMI(self.NMEMI): reason.append('NMEMI ('+str(self.NMEMI)+') out of range ()')
        if not geo_validator.is_valid_RESERVED(self.RESERVED): reason.append('RESERVED ('+str(self.RESERVED)+') out of range ()')
        return ', '.join(reason)

    def SparkSQLRow(self):
        """Return a SparkSQL Row object for this object."""
        from pyspark.sql import Row
        return Row(
            sldu=safe_str(self.SLDU),
            sldl=safe_str(self.SLDL),
            puma=safe_str(self.PUMA),
            place=safe_str(self.PLACE),
            fileid=safe_str(self.FILEID),
            stusab=safe_str(self.STUSAB),
            sumlev=safe_str(self.SUMLEV),
            geocomp=safe_str(self.GEOCOMP),
            chariter=safe_str(self.CHARITER),
            cifsn=safe_str(self.CIFSN),
            logrecno=safe_str(self.LOGRECNO),
            region=safe_str(self.REGION),
            division=safe_str(self.DIVISION),
            state=safe_str(self.STATE),
            county=safe_str(self.COUNTY),
            countycc=safe_str(self.COUNTYCC),
            countysc=safe_str(self.COUNTYSC),
            cousub=safe_str(self.COUSUB),
            cousubcc=safe_str(self.COUSUBCC),
            cousubsc=safe_str(self.COUSUBSC),
            placecc=safe_str(self.PLACECC),
            placesc=safe_str(self.PLACESC),
            tract=safe_str(self.TRACT),
            blkgrp=safe_str(self.BLKGRP),
            block=safe_str(self.BLOCK),
            iuc=safe_str(self.IUC),
            concit=safe_str(self.CONCIT),
            concitcc=safe_str(self.CONCITCC),
            concitsc=safe_str(self.CONCITSC),
            aianhh=safe_str(self.AIANHH),
            aianhhfp=safe_str(self.AIANHHFP),
            aianhhcc=safe_str(self.AIANHHCC),
            aihhtli=safe_str(self.AIHHTLI),
            aitsce=safe_str(self.AITSCE),
            aitscc=safe_str(self.AITSCC),
            ttract=safe_str(self.TTRACT),
            tblkgrp=safe_str(self.TBLKGRP),
            anrc=safe_str(self.ANRC),
            anrccc=safe_str(self.ANRCCC),
            cbsa=safe_str(self.CBSA),
            cbsasc=safe_str(self.CBSASC),
            metdiv=safe_str(self.METDIV),
            csa=safe_str(self.CSA),
            necta=safe_str(self.NECTA),
            nectasc=safe_str(self.NECTASC),
            nectadiv=safe_str(self.NECTADIV),
            cnecta=safe_str(self.CNECTA),
            cbsapci=safe_str(self.CBSAPCI),
            nectapci=safe_str(self.NECTAPCI),
            ua=safe_str(self.UA),
            uasc=safe_str(self.UASC),
            uatype=safe_str(self.UATYPE),
            ur=safe_str(self.UR),
            cd=safe_str(self.CD),
            vtd=safe_str(self.VTD),
            vtdi=safe_str(self.VTDI),
            zcta5=safe_str(self.ZCTA5),
            submcd=safe_str(self.SUBMCD),
            submcdcc=safe_str(self.SUBMCDCC),
            sdelm=safe_str(self.SDELM),
            sdsec=safe_str(self.SDSEC),
            sduni=safe_str(self.SDUNI),
            arealand=safe_str(self.AREALAND),
            areawatr=safe_str(self.AREAWATR),
            name=safe_str(self.NAME),
            funcstat=safe_str(self.FUNCSTAT),
            gcuni=safe_str(self.GCUNI),
            intptlat=safe_str(self.INTPTLAT),
            intptlon=safe_str(self.INTPTLON),
            lsadc=safe_str(self.LSADC),
            partflag=safe_str(self.PARTFLAG),
            uga=safe_str(self.UGA),
            statens=safe_str(self.STATENS),
            countyns=safe_str(self.COUNTYNS),
            cousubns=safe_str(self.COUSUBNS),
            placens=safe_str(self.PLACENS),
            concitns=safe_str(self.CONCITNS),
            aianhhns=safe_str(self.AIANHHNS),
            aitsns=safe_str(self.AITSNS),
            anrcns=safe_str(self.ANRCNS),
            submcdns=safe_str(self.SUBMCDNS),
            aianhhsc=safe_str(self.AIANHHSC),
            csasc=safe_str(self.CSASC),
            cnectasc=safe_str(self.CNECTASC),
            memi=safe_str(self.MEMI),
            nmemi=safe_str(self.NMEMI),
            reserved=safe_str(self.RESERVED),
        )

