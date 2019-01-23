
DATA <sas-data-set-name>    ;
       infile "<path>\<filename>.csv" delimiter = ',' MISSOVER DSD lrecl=32767 firstobs=2 ;      
	   informat FILEID $6. ;			
       informat STUSAB $2. ;			
       informat SUMLEV $3. ;			
       informat GEOCOMP $2. ;			
       informat CHARITER $3. ;			
       informat CIFSN $2. ;			
       informat LOGRECNO best32. ;			
       informat REGION $1. ;			
       informat DIVISION $1. ;			
       informat STATE $2. ;			
       informat COUNTY $3. ;			
       informat COUNTYCC $2. ;			
       informat COUNTYSC $2. ;			
       informat COUSUB $5. ;			
       informat COUSUBCC $2. ;			
       informat COUSUBSC $2. ;			
       informat PLACE $5. ;			
       informat PLACECC $2. ;			
       informat PLACESC $2. ;			
       informat TRACT $6. ;			
       informat BLKGRP $1. ;			
       informat BLOCK $4. ;			
       informat IUC $2. ;			
       informat CONCIT $5. ;			
       informat CONCITCC $2. ;			
       informat CONCITSC $2. ;			
       informat AIANHH $4. ;			
       informat AIANHHFP $5. ;			
       informat AIANHHCC $2. ;			
       informat AIHHTLI $1. ;			
       informat AITSCE $3. ;			
       informat AITS $5. ;			
       informat AITSCC $2. ;			
       informat TTRACT $6. ;			
       informat TBLKGRP $1. ;			
       informat ANRC $5. ;			
       informat ANRCCC $2. ;			
       informat CBSA $5. ;			
       informat CBSASC $2. ;			
       informat METDIV $5. ;			
       informat CSA $3. ;			
       informat NECTA $5. ;			
       informat NECTASC $2. ;			
       informat NECTADIV $5. ;			
       informat CNECTA $3. ;			
       informat CBSAPCI $1. ;			
       informat NECTAPCI $1. ;			
       informat UA $5. ;			
       informat UASC $2. ;			
       informat UATYPE $1. ;			
       informat UR $1. ;			
       informat CD $2. ;			
       informat SLDU $3. ;			
       informat SLDL $3. ;			
       informat VTD $6. ;			
       informat VTDI $1. ;			
       informat RESERVE2 $3. ;			
       informat ZCTA5 $5. ;			
       informat SUBMCD $5. ;			
       informat SUBMCDCC $2. ;			
       informat SDELEM $5. ;			
       informat SDSEC $5. ;			
       informat SDUNI $5. ;			
       informat AREALAND $14. ;			
       informat AREAWATR $14. ;			
       informat NAME $90. ;			
       informat FUNCSTAT $1. ;			
       informat GCUNI $1. ;			
       informat POP100 best32. ;			
       informat HU100 best32. ;			
       informat INTPTLAT $11. ;			
       informat INTPTLON $12. ;			
       informat LSADC $2. ;			
       informat PARTFLAG $1. ;			
       informat RESERVE3 $6. ;			
       informat UGA $5. ;			
       informat STATENS $8. ;			
       informat COUNTYNS $8. ;			
       informat COUSUBNS $8. ;			
       informat PLACENS $8. ;			
       informat CONCITNS $8. ;			
       informat AIANHHNS $8. ;			
       informat AITSNS $8. ;			
       informat ANRCNS $8. ;			
       informat SUBMCDNS $8. ;			
       informat CD113 $2. ;			
       informat CD114 $2. ;			
       informat CD115 $2. ;			
       informat SLDU2 $3. ;			
       informat SLDU3 $3. ;			
       informat SLDU4 $3. ;			
       informat SLDL2 $3. ;			
       informat SLDL3 $3. ;			
       informat SLDL4 $3. ;			
       informat AIANHHSC $2. ;			
       informat CSASC $2. ;			
       informat CNECTASC $2. ;			
       informat MEMI $1. ;			
       informat NMEMI $1. ;			
       informat PUMA $5. ;			
       informat RESERVED $18. ;			
       informat P0010001 best32. ;			
       informat P0020001 best32. ;			
       informat P0020002 best32. ;			
       informat P0020003 best32. ;			
       informat P0020004 best32. ;			
       informat P0020005 best32. ;			
       informat P0020006 best32. ;			
       informat P0030001 best32. ;			
       informat P0030002 best32. ;			
       informat P0030003 best32. ;			
       informat P0030004 best32. ;			
       informat P0030005 best32. ;			
       informat P0030006 best32. ;			
       informat P0030007 best32. ;			
       informat P0030008 best32. ;			
       informat P0040001 best32. ;			
       informat P0040002 best32. ;			
       informat P0040003 best32. ;			
       informat P0050001 best32. ;			
       informat P0050002 best32. ;			
       informat P0050003 best32. ;			
       informat P0050004 best32. ;			
       informat P0050005 best32. ;			
       informat P0050006 best32. ;			
       informat P0050007 best32. ;			
       informat P0050008 best32. ;			
       informat P0050009 best32. ;			
       informat P0050010 best32. ;			
       informat P0050011 best32. ;			
       informat P0050012 best32. ;			
       informat P0050013 best32. ;			
       informat P0050014 best32. ;			
       informat P0050015 best32. ;			
       informat P0050016 best32. ;			
       informat P0050017 best32. ;			
       informat P0060001 best32. ;			
       informat P0060002 best32. ;			
       informat P0060003 best32. ;			
       informat P0060004 best32. ;			
       informat P0060005 best32. ;			
       informat P0060006 best32. ;			
       informat P0060007 best32. ;			
       informat P0070001 best32. ;			
       informat P0070002 best32. ;			
       informat P0070003 best32. ;			
       informat P0070004 best32. ;			
       informat P0070005 best32. ;			
       informat P0070006 best32. ;			
       informat P0070007 best32. ;			
       informat P0070008 best32. ;			
       informat P0070009 best32. ;			
       informat P0070010 best32. ;			
       informat P0070011 best32. ;			
       informat P0070012 best32. ;			
       informat P0070013 best32. ;			
       informat P0070014 best32. ;			
       informat P0070015 best32. ;			
       informat P0080001 best32. ;			
       informat P0080002 best32. ;			
       informat P0080003 best32. ;			
       informat P0080004 best32. ;			
       informat P0080005 best32. ;			
       informat P0080006 best32. ;			
       informat P0080007 best32. ;			
       informat P0080008 best32. ;			
       informat P0080009 best32. ;			
       informat P0080010 best32. ;			
       informat P0080011 best32. ;			
       informat P0080012 best32. ;			
       informat P0080013 best32. ;			
       informat P0080014 best32. ;			
       informat P0080015 best32. ;			
       informat P0080016 best32. ;			
       informat P0080017 best32. ;			
       informat P0080018 best32. ;			
       informat P0080019 best32. ;			
       informat P0080020 best32. ;			
       informat P0080021 best32. ;			
       informat P0080022 best32. ;			
       informat P0080023 best32. ;			
       informat P0080024 best32. ;			
       informat P0080025 best32. ;			
       informat P0080026 best32. ;			
       informat P0080027 best32. ;			
       informat P0080028 best32. ;			
       informat P0080029 best32. ;			
       informat P0080030 best32. ;			
       informat P0080031 best32. ;			
       informat P0080032 best32. ;			
       informat P0080033 best32. ;			
       informat P0080034 best32. ;			
       informat P0080035 best32. ;			
       informat P0080036 best32. ;			
       informat P0080037 best32. ;			
       informat P0080038 best32. ;			
       informat P0080039 best32. ;			
       informat P0080040 best32. ;			
       informat P0080041 best32. ;			
       informat P0080042 best32. ;			
       informat P0080043 best32. ;			
       informat P0080044 best32. ;			
       informat P0080045 best32. ;			
       informat P0080046 best32. ;			
       informat P0080047 best32. ;			
       informat P0080048 best32. ;			
       informat P0080049 best32. ;			
       informat P0080050 best32. ;			
       informat P0080051 best32. ;			
       informat P0080052 best32. ;			
       informat P0080053 best32. ;			
       informat P0080054 best32. ;			
       informat P0080055 best32. ;			
       informat P0080056 best32. ;			
       informat P0080057 best32. ;			
       informat P0080058 best32. ;			
       informat P0080059 best32. ;			
       informat P0080060 best32. ;			
       informat P0080061 best32. ;			
       informat P0080062 best32. ;			
       informat P0080063 best32. ;			
       informat P0080064 best32. ;			
       informat P0080065 best32. ;			
       informat P0080066 best32. ;			
       informat P0080067 best32. ;			
       informat P0080068 best32. ;			
       informat P0080069 best32. ;			
       informat P0080070 best32. ;			
       informat P0080071 best32. ;			
       informat P0090001 best32. ;			
       informat P0090002 best32. ;			
       informat P0090003 best32. ;			
       informat P0090004 best32. ;			
       informat P0090005 best32. ;			
       informat P0090006 best32. ;			
       informat P0090007 best32. ;			
       informat P0090008 best32. ;			
       informat P0090009 best32. ;			
       informat P0090010 best32. ;			
       informat P0090011 best32. ;			
       informat P0090012 best32. ;			
       informat P0090013 best32. ;			
       informat P0090014 best32. ;			
       informat P0090015 best32. ;			
       informat P0090016 best32. ;			
       informat P0090017 best32. ;			
       informat P0090018 best32. ;			
       informat P0090019 best32. ;			
       informat P0090020 best32. ;			
       informat P0090021 best32. ;			
       informat P0090022 best32. ;			
       informat P0090023 best32. ;			
       informat P0090024 best32. ;			
       informat P0090025 best32. ;			
       informat P0090026 best32. ;			
       informat P0090027 best32. ;			
       informat P0090028 best32. ;			
       informat P0090029 best32. ;			
       informat P0090030 best32. ;			
       informat P0090031 best32. ;			
       informat P0090032 best32. ;			
       informat P0090033 best32. ;			
       informat P0090034 best32. ;			
       informat P0090035 best32. ;			
       informat P0090036 best32. ;			
       informat P0090037 best32. ;			
       informat P0090038 best32. ;			
       informat P0090039 best32. ;			
       informat P0090040 best32. ;			
       informat P0090041 best32. ;			
       informat P0090042 best32. ;			
       informat P0090043 best32. ;			
       informat P0090044 best32. ;			
       informat P0090045 best32. ;			
       informat P0090046 best32. ;			
       informat P0090047 best32. ;			
       informat P0090048 best32. ;			
       informat P0090049 best32. ;			
       informat P0090050 best32. ;			
       informat P0090051 best32. ;			
       informat P0090052 best32. ;			
       informat P0090053 best32. ;			
       informat P0090054 best32. ;			
       informat P0090055 best32. ;			
       informat P0090056 best32. ;			
       informat P0090057 best32. ;			
       informat P0090058 best32. ;			
       informat P0090059 best32. ;			
       informat P0090060 best32. ;			
       informat P0090061 best32. ;			
       informat P0090062 best32. ;			
       informat P0090063 best32. ;			
       informat P0090064 best32. ;			
       informat P0090065 best32. ;			
       informat P0090066 best32. ;			
       informat P0090067 best32. ;			
       informat P0090068 best32. ;			
       informat P0090069 best32. ;			
       informat P0090070 best32. ;			
       informat P0090071 best32. ;			
       informat P0090072 best32. ;			
       informat P0090073 best32. ;			
       informat P0100001 best32. ;			
       informat P0100002 best32. ;			
       informat P0100003 best32. ;			
       informat P0100004 best32. ;			
       informat P0100005 best32. ;			
       informat P0100006 best32. ;			
       informat P0100007 best32. ;			
       informat P0100008 best32. ;			
       informat P0100009 best32. ;			
       informat P0100010 best32. ;			
       informat P0100011 best32. ;			
       informat P0100012 best32. ;			
       informat P0100013 best32. ;			
       informat P0100014 best32. ;			
       informat P0100015 best32. ;			
       informat P0100016 best32. ;			
       informat P0100017 best32. ;			
       informat P0100018 best32. ;			
       informat P0100019 best32. ;			
       informat P0100020 best32. ;			
       informat P0100021 best32. ;			
       informat P0100022 best32. ;			
       informat P0100023 best32. ;			
       informat P0100024 best32. ;			
       informat P0100025 best32. ;			
       informat P0100026 best32. ;			
       informat P0100027 best32. ;			
       informat P0100028 best32. ;			
       informat P0100029 best32. ;			
       informat P0100030 best32. ;			
       informat P0100031 best32. ;			
       informat P0100032 best32. ;			
       informat P0100033 best32. ;			
       informat P0100034 best32. ;			
       informat P0100035 best32. ;			
       informat P0100036 best32. ;			
       informat P0100037 best32. ;			
       informat P0100038 best32. ;			
       informat P0100039 best32. ;			
       informat P0100040 best32. ;			
       informat P0100041 best32. ;			
       informat P0100042 best32. ;			
       informat P0100043 best32. ;			
       informat P0100044 best32. ;			
       informat P0100045 best32. ;			
       informat P0100046 best32. ;			
       informat P0100047 best32. ;			
       informat P0100048 best32. ;			
       informat P0100049 best32. ;			
       informat P0100050 best32. ;			
       informat P0100051 best32. ;			
       informat P0100052 best32. ;			
       informat P0100053 best32. ;			
       informat P0100054 best32. ;			
       informat P0100055 best32. ;			
       informat P0100056 best32. ;			
       informat P0100057 best32. ;			
       informat P0100058 best32. ;			
       informat P0100059 best32. ;			
       informat P0100060 best32. ;			
       informat P0100061 best32. ;			
       informat P0100062 best32. ;			
       informat P0100063 best32. ;			
       informat P0100064 best32. ;			
       informat P0100065 best32. ;			
       informat P0100066 best32. ;			
       informat P0100067 best32. ;			
       informat P0100068 best32. ;			
       informat P0100069 best32. ;			
       informat P0100070 best32. ;			
       informat P0100071 best32. ;			
       informat P0110001 best32. ;			
       informat P0110002 best32. ;			
       informat P0110003 best32. ;			
       informat P0110004 best32. ;			
       informat P0110005 best32. ;			
       informat P0110006 best32. ;			
       informat P0110007 best32. ;			
       informat P0110008 best32. ;			
       informat P0110009 best32. ;			
       informat P0110010 best32. ;			
       informat P0110011 best32. ;			
       informat P0110012 best32. ;			
       informat P0110013 best32. ;			
       informat P0110014 best32. ;			
       informat P0110015 best32. ;			
       informat P0110016 best32. ;			
       informat P0110017 best32. ;			
       informat P0110018 best32. ;			
       informat P0110019 best32. ;			
       informat P0110020 best32. ;			
       informat P0110021 best32. ;			
       informat P0110022 best32. ;			
       informat P0110023 best32. ;			
       informat P0110024 best32. ;			
       informat P0110025 best32. ;			
       informat P0110026 best32. ;			
       informat P0110027 best32. ;			
       informat P0110028 best32. ;			
       informat P0110029 best32. ;			
       informat P0110030 best32. ;			
       informat P0110031 best32. ;			
       informat P0110032 best32. ;			
       informat P0110033 best32. ;			
       informat P0110034 best32. ;			
       informat P0110035 best32. ;			
       informat P0110036 best32. ;			
       informat P0110037 best32. ;			
       informat P0110038 best32. ;			
       informat P0110039 best32. ;			
       informat P0110040 best32. ;			
       informat P0110041 best32. ;			
       informat P0110042 best32. ;			
       informat P0110043 best32. ;			
       informat P0110044 best32. ;			
       informat P0110045 best32. ;			
       informat P0110046 best32. ;			
       informat P0110047 best32. ;			
       informat P0110048 best32. ;			
       informat P0110049 best32. ;			
       informat P0110050 best32. ;			
       informat P0110051 best32. ;			
       informat P0110052 best32. ;			
       informat P0110053 best32. ;			
       informat P0110054 best32. ;			
       informat P0110055 best32. ;			
       informat P0110056 best32. ;			
       informat P0110057 best32. ;			
       informat P0110058 best32. ;			
       informat P0110059 best32. ;			
       informat P0110060 best32. ;			
       informat P0110061 best32. ;			
       informat P0110062 best32. ;			
       informat P0110063 best32. ;			
       informat P0110064 best32. ;			
       informat P0110065 best32. ;			
       informat P0110066 best32. ;			
       informat P0110067 best32. ;			
       informat P0110068 best32. ;			
       informat P0110069 best32. ;			
       informat P0110070 best32. ;			
       informat P0110071 best32. ;			
       informat P0110072 best32. ;			
       informat P0110073 best32. ;			
       informat P0120001 best32. ;			
       informat P0120002 best32. ;			
       informat P0120003 best32. ;			
       informat P0120004 best32. ;			
       informat P0120005 best32. ;			
       informat P0120006 best32. ;			
       informat P0120007 best32. ;			
       informat P0120008 best32. ;			
       informat P0120009 best32. ;			
       informat P0120010 best32. ;			
       informat P0120011 best32. ;			
       informat P0120012 best32. ;			
       informat P0120013 best32. ;			
       informat P0120014 best32. ;			
       informat P0120015 best32. ;			
       informat P0120016 best32. ;			
       informat P0120017 best32. ;			
       informat P0120018 best32. ;			
       informat P0120019 best32. ;			
       informat P0120020 best32. ;			
       informat P0120021 best32. ;			
       informat P0120022 best32. ;			
       informat P0120023 best32. ;			
       informat P0120024 best32. ;			
       informat P0120025 best32. ;			
       informat P0120026 best32. ;			
       informat P0120027 best32. ;			
       informat P0120028 best32. ;			
       informat P0120029 best32. ;			
       informat P0120030 best32. ;			
       informat P0120031 best32. ;			
       informat P0120032 best32. ;			
       informat P0120033 best32. ;			
       informat P0120034 best32. ;			
       informat P0120035 best32. ;			
       informat P0120036 best32. ;			
       informat P0120037 best32. ;			
       informat P0120038 best32. ;			
       informat P0120039 best32. ;			
       informat P0120040 best32. ;			
       informat P0120041 best32. ;			
       informat P0120042 best32. ;			
       informat P0120043 best32. ;			
       informat P0120044 best32. ;			
       informat P0120045 best32. ;			
       informat P0120046 best32. ;			
       informat P0120047 best32. ;			
       informat P0120048 best32. ;			
       informat P0120049 best32. ;			
       informat P0130001 best32. ;			
       informat P0130002 best32. ;			
       informat P0130003 best32. ;			
       informat P0140001 best32. ;			
       informat P0140002 best32. ;			
       informat P0140003 best32. ;			
       informat P0140004 best32. ;			
       informat P0140005 best32. ;			
       informat P0140006 best32. ;			
       informat P0140007 best32. ;			
       informat P0140008 best32. ;			
       informat P0140009 best32. ;			
       informat P0140010 best32. ;			
       informat P0140011 best32. ;			
       informat P0140012 best32. ;			
       informat P0140013 best32. ;			
       informat P0140014 best32. ;			
       informat P0140015 best32. ;			
       informat P0140016 best32. ;			
       informat P0140017 best32. ;			
       informat P0140018 best32. ;			
       informat P0140019 best32. ;			
       informat P0140020 best32. ;			
       informat P0140021 best32. ;			
       informat P0140022 best32. ;			
       informat P0140023 best32. ;			
       informat P0140024 best32. ;			
       informat P0140025 best32. ;			
       informat P0140026 best32. ;			
       informat P0140027 best32. ;			
       informat P0140028 best32. ;			
       informat P0140029 best32. ;			
       informat P0140030 best32. ;			
       informat P0140031 best32. ;			
       informat P0140032 best32. ;			
       informat P0140033 best32. ;			
       informat P0140034 best32. ;			
       informat P0140035 best32. ;			
       informat P0140036 best32. ;			
       informat P0140037 best32. ;			
       informat P0140038 best32. ;			
       informat P0140039 best32. ;			
       informat P0140040 best32. ;			
       informat P0140041 best32. ;			
       informat P0140042 best32. ;			
       informat P0140043 best32. ;			
       informat P0150001 best32. ;			
       informat P0150002 best32. ;			
       informat P0150003 best32. ;			
       informat P0150004 best32. ;			
       informat P0150005 best32. ;			
       informat P0150006 best32. ;			
       informat P0150007 best32. ;			
       informat P0150008 best32. ;			
       informat P0150009 best32. ;			
       informat P0150010 best32. ;			
       informat P0150011 best32. ;			
       informat P0150012 best32. ;			
       informat P0150013 best32. ;			
       informat P0150014 best32. ;			
       informat P0150015 best32. ;			
       informat P0150016 best32. ;			
       informat P0150017 best32. ;			
       informat P0160001 best32. ;			
       informat P0160002 best32. ;			
       informat P0160003 best32. ;			
       informat P0170001 best32. ;			
       informat P0170002 best32. ;			
       informat P0170003 best32. ;			
       informat P0180001 best32. ;			
       informat P0180002 best32. ;			
       informat P0180003 best32. ;			
       informat P0180004 best32. ;			
       informat P0180005 best32. ;			
       informat P0180006 best32. ;			
       informat P0180007 best32. ;			
       informat P0180008 best32. ;			
       informat P0180009 best32. ;			
       informat P0190001 best32. ;			
       informat P0190002 best32. ;			
       informat P0190003 best32. ;			
       informat P0190004 best32. ;			
       informat P0190005 best32. ;			
       informat P0190006 best32. ;			
       informat P0190007 best32. ;			
       informat P0190008 best32. ;			
       informat P0190009 best32. ;			
       informat P0190010 best32. ;			
       informat P0190011 best32. ;			
       informat P0190012 best32. ;			
       informat P0190013 best32. ;			
       informat P0190014 best32. ;			
       informat P0190015 best32. ;			
       informat P0190016 best32. ;			
       informat P0190017 best32. ;			
       informat P0190018 best32. ;			
       informat P0190019 best32. ;			
       informat P0200001 best32. ;			
       informat P0200002 best32. ;			
       informat P0200003 best32. ;			
       informat P0200004 best32. ;			
       informat P0200005 best32. ;			
       informat P0200006 best32. ;			
       informat P0200007 best32. ;			
       informat P0200008 best32. ;			
       informat P0200009 best32. ;			
       informat P0200010 best32. ;			
       informat P0200011 best32. ;			
       informat P0200012 best32. ;			
       informat P0200013 best32. ;			
       informat P0200014 best32. ;			
       informat P0200015 best32. ;			
       informat P0200016 best32. ;			
       informat P0200017 best32. ;			
       informat P0200018 best32. ;			
       informat P0200019 best32. ;			
       informat P0200020 best32. ;			
       informat P0200021 best32. ;			
       informat P0200022 best32. ;			
       informat P0200023 best32. ;			
       informat P0200024 best32. ;			
       informat P0200025 best32. ;			
       informat P0200026 best32. ;			
       informat P0200027 best32. ;			
       informat P0200028 best32. ;			
       informat P0200029 best32. ;			
       informat P0200030 best32. ;			
       informat P0200031 best32. ;			
       informat P0200032 best32. ;			
       informat P0200033 best32. ;			
       informat P0200034 best32. ;			
       informat P0210001 best32. ;			
       informat P0210002 best32. ;			
       informat P0210003 best32. ;			
       informat P0210004 best32. ;			
       informat P0210005 best32. ;			
       informat P0210006 best32. ;			
       informat P0210007 best32. ;			
       informat P0210008 best32. ;			
       informat P0210009 best32. ;			
       informat P0210010 best32. ;			
       informat P0210011 best32. ;			
       informat P0210012 best32. ;			
       informat P0210013 best32. ;			
       informat P0210014 best32. ;			
       informat P0210015 best32. ;			
       informat P0210016 best32. ;			
       informat P0210017 best32. ;			
       informat P0210018 best32. ;			
       informat P0210019 best32. ;			
       informat P0210020 best32. ;			
       informat P0210021 best32. ;			
       informat P0210022 best32. ;			
       informat P0210023 best32. ;			
       informat P0210024 best32. ;			
       informat P0210025 best32. ;			
       informat P0210026 best32. ;			
       informat P0210027 best32. ;			
       informat P0210028 best32. ;			
       informat P0210029 best32. ;			
       informat P0210030 best32. ;			
       informat P0210031 best32. ;			
       informat P0220001 best32. ;			
       informat P0220002 best32. ;			
       informat P0220003 best32. ;			
       informat P0220004 best32. ;			
       informat P0220005 best32. ;			
       informat P0220006 best32. ;			
       informat P0220007 best32. ;			
       informat P0220008 best32. ;			
       informat P0220009 best32. ;			
       informat P0220010 best32. ;			
       informat P0220011 best32. ;			
       informat P0220012 best32. ;			
       informat P0220013 best32. ;			
       informat P0220014 best32. ;			
       informat P0220015 best32. ;			
       informat P0220016 best32. ;			
       informat P0220017 best32. ;			
       informat P0220018 best32. ;			
       informat P0220019 best32. ;			
       informat P0220020 best32. ;			
       informat P0220021 best32. ;			
       informat P0230001 best32. ;			
       informat P0230002 best32. ;			
       informat P0230003 best32. ;			
       informat P0230004 best32. ;			
       informat P0230005 best32. ;			
       informat P0230006 best32. ;			
       informat P0230007 best32. ;			
       informat P0230008 best32. ;			
       informat P0230009 best32. ;			
       informat P0230010 best32. ;			
       informat P0230011 best32. ;			
       informat P0230012 best32. ;			
       informat P0230013 best32. ;			
       informat P0230014 best32. ;			
       informat P0230015 best32. ;			
       informat P0240001 best32. ;			
       informat P0240002 best32. ;			
       informat P0240003 best32. ;			
       informat P0240004 best32. ;			
       informat P0240005 best32. ;			
       informat P0240006 best32. ;			
       informat P0240007 best32. ;			
       informat P0240008 best32. ;			
       informat P0240009 best32. ;			
       informat P0240010 best32. ;			
       informat P0240011 best32. ;			
       informat P0250001 best32. ;			
       informat P0250002 best32. ;			
       informat P0250003 best32. ;			
       informat P0250004 best32. ;			
       informat P0250005 best32. ;			
       informat P0250006 best32. ;			
       informat P0250007 best32. ;			
       informat P0250008 best32. ;			
       informat P0250009 best32. ;			
       informat P0250010 best32. ;			
       informat P0250011 best32. ;			
       informat P0260001 best32. ;			
       informat P0260002 best32. ;			
       informat P0260003 best32. ;			
       informat P0260004 best32. ;			
       informat P0260005 best32. ;			
       informat P0260006 best32. ;			
       informat P0260007 best32. ;			
       informat P0260008 best32. ;			
       informat P0260009 best32. ;			
       informat P0260010 best32. ;			
       informat P0260011 best32. ;			
       informat P0270001 best32. ;			
       informat P0270002 best32. ;			
       informat P0270003 best32. ;			
       informat P0280001 best32. ;			
       informat P0280002 best32. ;			
       informat P0280003 best32. ;			
       informat P0280004 best32. ;			
       informat P0280005 best32. ;			
       informat P0280006 best32. ;			
       informat P0280007 best32. ;			
       informat P0280008 best32. ;			
       informat P0280009 best32. ;			
       informat P0280010 best32. ;			
       informat P0280011 best32. ;			
       informat P0280012 best32. ;			
       informat P0280013 best32. ;			
       informat P0280014 best32. ;			
       informat P0280015 best32. ;			
       informat P0280016 best32. ;			
       informat P0290001 best32. ;			
       informat P0290002 best32. ;			
       informat P0290003 best32. ;			
       informat P0290004 best32. ;			
       informat P0290005 best32. ;			
       informat P0290006 best32. ;			
       informat P0290007 best32. ;			
       informat P0290008 best32. ;			
       informat P0290009 best32. ;			
       informat P0290010 best32. ;			
       informat P0290011 best32. ;			
       informat P0290012 best32. ;			
       informat P0290013 best32. ;			
       informat P0290014 best32. ;			
       informat P0290015 best32. ;			
       informat P0290016 best32. ;			
       informat P0290017 best32. ;			
       informat P0290018 best32. ;			
       informat P0290019 best32. ;			
       informat P0290020 best32. ;			
       informat P0290021 best32. ;			
       informat P0290022 best32. ;			
       informat P0290023 best32. ;			
       informat P0290024 best32. ;			
       informat P0290025 best32. ;			
       informat P0290026 best32. ;			
       informat P0290027 best32. ;			
       informat P0290028 best32. ;			
       informat P0300001 best32. ;			
       informat P0300002 best32. ;			
       informat P0300003 best32. ;			
       informat P0300004 best32. ;			
       informat P0300005 best32. ;			
       informat P0300006 best32. ;			
       informat P0300007 best32. ;			
       informat P0300008 best32. ;			
       informat P0300009 best32. ;			
       informat P0300010 best32. ;			
       informat P0300011 best32. ;			
       informat P0300012 best32. ;			
       informat P0300013 best32. ;			
       informat P0310001 best32. ;			
       informat P0310002 best32. ;			
       informat P0310003 best32. ;			
       informat P0310004 best32. ;			
       informat P0310005 best32. ;			
       informat P0310006 best32. ;			
       informat P0310007 best32. ;			
       informat P0310008 best32. ;			
       informat P0310009 best32. ;			
       informat P0310010 best32. ;			
       informat P0310011 best32. ;			
       informat P0310012 best32. ;			
       informat P0310013 best32. ;			
       informat P0310014 best32. ;			
       informat P0310015 best32. ;			
       informat P0310016 best32. ;			
       informat P0320001 best32. ;			
       informat P0320002 best32. ;			
       informat P0320003 best32. ;			
       informat P0320004 best32. ;			
       informat P0320005 best32. ;			
       informat P0320006 best32. ;			
       informat P0320007 best32. ;			
       informat P0320008 best32. ;			
       informat P0320009 best32. ;			
       informat P0320010 best32. ;			
       informat P0320011 best32. ;			
       informat P0320012 best32. ;			
       informat P0320013 best32. ;			
       informat P0320014 best32. ;			
       informat P0320015 best32. ;			
       informat P0320016 best32. ;			
       informat P0320017 best32. ;			
       informat P0320018 best32. ;			
       informat P0320019 best32. ;			
       informat P0320020 best32. ;			
       informat P0320021 best32. ;			
       informat P0320022 best32. ;			
       informat P0320023 best32. ;			
       informat P0320024 best32. ;			
       informat P0320025 best32. ;			
       informat P0320026 best32. ;			
       informat P0320027 best32. ;			
       informat P0320028 best32. ;			
       informat P0320029 best32. ;			
       informat P0320030 best32. ;			
       informat P0320031 best32. ;			
       informat P0320032 best32. ;			
       informat P0320033 best32. ;			
       informat P0320034 best32. ;			
       informat P0320035 best32. ;			
       informat P0320036 best32. ;			
       informat P0320037 best32. ;			
       informat P0320038 best32. ;			
       informat P0320039 best32. ;			
       informat P0320040 best32. ;			
       informat P0320041 best32. ;			
       informat P0320042 best32. ;			
       informat P0320043 best32. ;			
       informat P0320044 best32. ;			
       informat P0320045 best32. ;			
       informat P0330001 best32. ;			
       informat P0330002 best32. ;			
       informat P0330003 best32. ;			
       informat P0330004 best32. ;			
       informat P0330005 best32. ;			
       informat P0330006 best32. ;			
       informat P0330007 best32. ;			
       informat P0340001 best32. ;			
       informat P0340002 best32. ;			
       informat P0340003 best32. ;			
       informat P0340004 best32. ;			
       informat P0340005 best32. ;			
       informat P0340006 best32. ;			
       informat P0340007 best32. ;			
       informat P0340008 best32. ;			
       informat P0340009 best32. ;			
       informat P0340010 best32. ;			
       informat P0340011 best32. ;			
       informat P0340012 best32. ;			
       informat P0340013 best32. ;			
       informat P0340014 best32. ;			
       informat P0340015 best32. ;			
       informat P0340016 best32. ;			
       informat P0340017 best32. ;			
       informat P0340018 best32. ;			
       informat P0340019 best32. ;			
       informat P0340020 best32. ;			
       informat P0340021 best32. ;			
       informat P0340022 best32. ;			
       informat P0350001 best32. ;			
       informat P0360001 best32. ;			
       informat P0360002 best32. ;			
       informat P0360003 best32. ;			
       informat P0370001 best32. ;			
       informat P0370002 best32. ;			
       informat P0370003 best32. ;			
       informat P0380001 best32. ;			
       informat P0380002 best32. ;			
       informat P0380003 best32. ;			
       informat P0380004 best32. ;			
       informat P0380005 best32. ;			
       informat P0380006 best32. ;			
       informat P0380007 best32. ;			
       informat P0380008 best32. ;			
       informat P0380009 best32. ;			
       informat P0380010 best32. ;			
       informat P0380011 best32. ;			
       informat P0380012 best32. ;			
       informat P0380013 best32. ;			
       informat P0380014 best32. ;			
       informat P0380015 best32. ;			
       informat P0380016 best32. ;			
       informat P0380017 best32. ;			
       informat P0380018 best32. ;			
       informat P0380019 best32. ;			
       informat P0380020 best32. ;			
       informat P0390001 best32. ;			
       informat P0390002 best32. ;			
       informat P0390003 best32. ;			
       informat P0390004 best32. ;			
       informat P0390005 best32. ;			
       informat P0390006 best32. ;			
       informat P0390007 best32. ;			
       informat P0390008 best32. ;			
       informat P0390009 best32. ;			
       informat P0390010 best32. ;			
       informat P0390011 best32. ;			
       informat P0390012 best32. ;			
       informat P0390013 best32. ;			
       informat P0390014 best32. ;			
       informat P0390015 best32. ;			
       informat P0390016 best32. ;			
       informat P0390017 best32. ;			
       informat P0390018 best32. ;			
       informat P0390019 best32. ;			
       informat P0390020 best32. ;			
       informat P0400001 best32. ;			
       informat P0400002 best32. ;			
       informat P0400003 best32. ;			
       informat P0400004 best32. ;			
       informat P0400005 best32. ;			
       informat P0400006 best32. ;			
       informat P0400007 best32. ;			
       informat P0400008 best32. ;			
       informat P0400009 best32. ;			
       informat P0400010 best32. ;			
       informat P0400011 best32. ;			
       informat P0400012 best32. ;			
       informat P0400013 best32. ;			
       informat P0400014 best32. ;			
       informat P0400015 best32. ;			
       informat P0400016 best32. ;			
       informat P0400017 best32. ;			
       informat P0400018 best32. ;			
       informat P0400019 best32. ;			
       informat P0400020 best32. ;			
       informat P0410001 best32. ;			
       informat P0410002 best32. ;			
       informat P0410003 best32. ;			
       informat P0410004 best32. ;			
       informat P0410005 best32. ;			
       informat P0410006 best32. ;			
       informat P0420001 best32. ;			
       informat P0420002 best32. ;			
       informat P0420003 best32. ;			
       informat P0420004 best32. ;			
       informat P0420005 best32. ;			
       informat P0420006 best32. ;			
       informat P0420007 best32. ;			
       informat P0420008 best32. ;			
       informat P0420009 best32. ;			
       informat P0420010 best32. ;			
       informat P0430001 best32. ;			
       informat P0430002 best32. ;			
       informat P0430003 best32. ;			
       informat P0430004 best32. ;			
       informat P0430005 best32. ;			
       informat P0430006 best32. ;			
       informat P0430007 best32. ;			
       informat P0430008 best32. ;			
       informat P0430009 best32. ;			
       informat P0430010 best32. ;			
       informat P0430011 best32. ;			
       informat P0430012 best32. ;			
       informat P0430013 best32. ;			
       informat P0430014 best32. ;			
       informat P0430015 best32. ;			
       informat P0430016 best32. ;			
       informat P0430017 best32. ;			
       informat P0430018 best32. ;			
       informat P0430019 best32. ;			
       informat P0430020 best32. ;			
       informat P0430021 best32. ;			
       informat P0430022 best32. ;			
       informat P0430023 best32. ;			
       informat P0430024 best32. ;			
       informat P0430025 best32. ;			
       informat P0430026 best32. ;			
       informat P0430027 best32. ;			
       informat P0430028 best32. ;			
       informat P0430029 best32. ;			
        informat P0430030 best32. ;			
        informat P0430031 best32. ;			
        informat P0430032 best32. ;			
        informat P0430033 best32. ;			
        informat P0430034 best32. ;			
        informat P0430035 best32. ;			
        informat P0430036 best32. ;			
        informat P0430037 best32. ;			
        informat P0430038 best32. ;			
        informat P0430039 best32. ;			
        informat P0430040 best32. ;			
        informat P0430041 best32. ;			
        informat P0430042 best32. ;			
        informat P0430043 best32. ;			
        informat P0430044 best32. ;			
        informat P0430045 best32. ;			
        informat P0430046 best32. ;			
        informat P0430047 best32. ;			
        informat P0430048 best32. ;			
        informat P0430049 best32. ;			
        informat P0430050 best32. ;			
        informat P0430051 best32. ;			
        informat P0430052 best32. ;			
        informat P0430053 best32. ;			
        informat P0430054 best32. ;			
        informat P0430055 best32. ;			
        informat P0430056 best32. ;			
        informat P0430057 best32. ;			
        informat P0430058 best32. ;			
        informat P0430059 best32. ;			
        informat P0430060 best32. ;			
        informat P0430061 best32. ;			
        informat P0430062 best32. ;			
        informat P0430063 best32. ;			
        informat P0440001 best32. ;			
        informat P0440002 best32. ;			
        informat P0440003 best32. ;			
        informat P0450001 best32. ;			
        informat P0450002 best32. ;			
        informat P0450003 best32. ;			
        informat P0460001 best32. ;			
        informat P0460002 best32. ;			
        informat P0460003 best32. ;			
        informat P0470001 best32. ;			
        informat P0470002 best32. ;			
        informat P0470003 best32. ;			
        informat P0480001 best32. ;			
        informat P0480002 best32. ;			
        informat P0480003 best32. ;			
        informat P0490001 best32. ;			
        informat P0490002 best32. ;			
        informat P0490003 best32. ;			
        informat P0500001 best32. ;			
        informat P0500002 best32. ;			
        informat P0500003 best32. ;			
        informat P0510001 best32. ;			
        informat P0510002 best32. ;			
        informat P0510003 best32. ;			
        informat P012A001 best32. ;			
        informat P012A002 best32. ;			
        informat P012A003 best32. ;			
        informat P012A004 best32. ;			
        informat P012A005 best32. ;			
        informat P012A006 best32. ;			
        informat P012A007 best32. ;			
        informat P012A008 best32. ;			
        informat P012A009 best32. ;			
        informat P012A010 best32. ;			
        informat P012A011 best32. ;			
        informat P012A012 best32. ;			
        informat P012A013 best32. ;			
        informat P012A014 best32. ;			
        informat P012A015 best32. ;			
        informat P012A016 best32. ;			
        informat P012A017 best32. ;			
        informat P012A018 best32. ;			
        informat P012A019 best32. ;			
        informat P012A020 best32. ;			
        informat P012A021 best32. ;			
        informat P012A022 best32. ;			
        informat P012A023 best32. ;			
        informat P012A024 best32. ;			
        informat P012A025 best32. ;			
        informat P012A026 best32. ;			
        informat P012A027 best32. ;			
        informat P012A028 best32. ;			
        informat P012A029 best32. ;			
        informat P012A030 best32. ;			
        informat P012A031 best32. ;			
        informat P012A032 best32. ;			
        informat P012A033 best32. ;			
        informat P012A034 best32. ;			
        informat P012A035 best32. ;			
        informat P012A036 best32. ;			
        informat P012A037 best32. ;			
        informat P012A038 best32. ;			
        informat P012A039 best32. ;			
        informat P012A040 best32. ;			
        informat P012A041 best32. ;			
        informat P012A042 best32. ;			
        informat P012A043 best32. ;			
        informat P012A044 best32. ;			
        informat P012A045 best32. ;			
        informat P012A046 best32. ;			
        informat P012A047 best32. ;			
        informat P012A048 best32. ;			
        informat P012A049 best32. ;			
        informat P012B001 best32. ;			
        informat P012B002 best32. ;			
        informat P012B003 best32. ;			
        informat P012B004 best32. ;			
        informat P012B005 best32. ;			
        informat P012B006 best32. ;			
        informat P012B007 best32. ;			
        informat P012B008 best32. ;			
        informat P012B009 best32. ;			
        informat P012B010 best32. ;			
        informat P012B011 best32. ;			
        informat P012B012 best32. ;			
        informat P012B013 best32. ;			
        informat P012B014 best32. ;			
        informat P012B015 best32. ;			
        informat P012B016 best32. ;			
        informat P012B017 best32. ;			
        informat P012B018 best32. ;			
        informat P012B019 best32. ;			
        informat P012B020 best32. ;			
        informat P012B021 best32. ;			
        informat P012B022 best32. ;			
        informat P012B023 best32. ;			
        informat P012B024 best32. ;			
        informat P012B025 best32. ;			
        informat P012B026 best32. ;			
        informat P012B027 best32. ;			
        informat P012B028 best32. ;			
        informat P012B029 best32. ;			
        informat P012B030 best32. ;			
        informat P012B031 best32. ;			
        informat P012B032 best32. ;			
        informat P012B033 best32. ;			
        informat P012B034 best32. ;			
        informat P012B035 best32. ;			
        informat P012B036 best32. ;			
        informat P012B037 best32. ;			
        informat P012B038 best32. ;			
        informat P012B039 best32. ;			
        informat P012B040 best32. ;			
        informat P012B041 best32. ;			
        informat P012B042 best32. ;			
        informat P012B043 best32. ;			
        informat P012B044 best32. ;			
        informat P012B045 best32. ;			
        informat P012B046 best32. ;			
        informat P012B047 best32. ;			
        informat P012B048 best32. ;			
        informat P012B049 best32. ;			
        informat P012C001 best32. ;			
        informat P012C002 best32. ;			
        informat P012C003 best32. ;			
        informat P012C004 best32. ;			
        informat P012C005 best32. ;			
        informat P012C006 best32. ;			
        informat P012C007 best32. ;			
        informat P012C008 best32. ;			
        informat P012C009 best32. ;			
        informat P012C010 best32. ;			
        informat P012C011 best32. ;			
        informat P012C012 best32. ;			
        informat P012C013 best32. ;			
        informat P012C014 best32. ;			
        informat P012C015 best32. ;			
        informat P012C016 best32. ;			
        informat P012C017 best32. ;			
        informat P012C018 best32. ;			
        informat P012C019 best32. ;			
        informat P012C020 best32. ;			
        informat P012C021 best32. ;			
        informat P012C022 best32. ;			
        informat P012C023 best32. ;			
        informat P012C024 best32. ;			
        informat P012C025 best32. ;			
        informat P012C026 best32. ;			
        informat P012C027 best32. ;			
        informat P012C028 best32. ;			
        informat P012C029 best32. ;			
        informat P012C030 best32. ;			
        informat P012C031 best32. ;			
        informat P012C032 best32. ;			
        informat P012C033 best32. ;			
        informat P012C034 best32. ;			
        informat P012C035 best32. ;			
        informat P012C036 best32. ;			
        informat P012C037 best32. ;			
        informat P012C038 best32. ;			
        informat P012C039 best32. ;			
        informat P012C040 best32. ;			
        informat P012C041 best32. ;			
        informat P012C042 best32. ;			
        informat P012C043 best32. ;			
        informat P012C044 best32. ;			
        informat P012C045 best32. ;			
        informat P012C046 best32. ;			
        informat P012C047 best32. ;			
        informat P012C048 best32. ;			
        informat P012C049 best32. ;			
        informat P012D001 best32. ;			
        informat P012D002 best32. ;			
        informat P012D003 best32. ;			
        informat P012D004 best32. ;			
        informat P012D005 best32. ;			
        informat P012D006 best32. ;			
        informat P012D007 best32. ;			
        informat P012D008 best32. ;			
        informat P012D009 best32. ;			
        informat P012D010 best32. ;			
        informat P012D011 best32. ;			
        informat P012D012 best32. ;			
        informat P012D013 best32. ;			
        informat P012D014 best32. ;			
        informat P012D015 best32. ;			
        informat P012D016 best32. ;			
        informat P012D017 best32. ;			
        informat P012D018 best32. ;			
        informat P012D019 best32. ;			
        informat P012D020 best32. ;			
        informat P012D021 best32. ;			
        informat P012D022 best32. ;			
        informat P012D023 best32. ;			
        informat P012D024 best32. ;			
        informat P012D025 best32. ;			
        informat P012D026 best32. ;			
        informat P012D027 best32. ;			
        informat P012D028 best32. ;			
        informat P012D029 best32. ;			
        informat P012D030 best32. ;			
        informat P012D031 best32. ;			
        informat P012D032 best32. ;			
        informat P012D033 best32. ;			
        informat P012D034 best32. ;			
        informat P012D035 best32. ;			
        informat P012D036 best32. ;			
        informat P012D037 best32. ;			
        informat P012D038 best32. ;			
        informat P012D039 best32. ;			
        informat P012D040 best32. ;			
        informat P012D041 best32. ;			
        informat P012D042 best32. ;			
        informat P012D043 best32. ;			
        informat P012D044 best32. ;			
        informat P012D045 best32. ;			
        informat P012D046 best32. ;			
        informat P012D047 best32. ;			
        informat P012D048 best32. ;			
        informat P012D049 best32. ;			
        informat P012E001 best32. ;			
        informat P012E002 best32. ;			
        informat P012E003 best32. ;			
        informat P012E004 best32. ;			
        informat P012E005 best32. ;			
        informat P012E006 best32. ;			
        informat P012E007 best32. ;			
        informat P012E008 best32. ;			
        informat P012E009 best32. ;			
        informat P012E010 best32. ;			
        informat P012E011 best32. ;			
        informat P012E012 best32. ;			
        informat P012E013 best32. ;			
        informat P012E014 best32. ;			
        informat P012E015 best32. ;			
        informat P012E016 best32. ;			
        informat P012E017 best32. ;			
        informat P012E018 best32. ;			
        informat P012E019 best32. ;			
        informat P012E020 best32. ;			
        informat P012E021 best32. ;			
        informat P012E022 best32. ;			
        informat P012E023 best32. ;			
        informat P012E024 best32. ;			
        informat P012E025 best32. ;			
        informat P012E026 best32. ;			
        informat P012E027 best32. ;			
        informat P012E028 best32. ;			
        informat P012E029 best32. ;			
        informat P012E030 best32. ;			
        informat P012E031 best32. ;			
        informat P012E032 best32. ;			
        informat P012E033 best32. ;			
        informat P012E034 best32. ;			
        informat P012E035 best32. ;			
        informat P012E036 best32. ;			
        informat P012E037 best32. ;			
        informat P012E038 best32. ;			
        informat P012E039 best32. ;			
        informat P012E040 best32. ;			
        informat P012E041 best32. ;			
        informat P012E042 best32. ;			
        informat P012E043 best32. ;			
        informat P012E044 best32. ;			
        informat P012E045 best32. ;			
        informat P012E046 best32. ;			
        informat P012E047 best32. ;			
        informat P012E048 best32. ;			
        informat P012E049 best32. ;			
        informat P012F001 best32. ;			
        informat P012F002 best32. ;			
        informat P012F003 best32. ;			
        informat P012F004 best32. ;			
        informat P012F005 best32. ;			
        informat P012F006 best32. ;			
        informat P012F007 best32. ;			
        informat P012F008 best32. ;			
        informat P012F009 best32. ;			
        informat P012F010 best32. ;			
        informat P012F011 best32. ;			
        informat P012F012 best32. ;			
        informat P012F013 best32. ;			
        informat P012F014 best32. ;			
        informat P012F015 best32. ;			
        informat P012F016 best32. ;			
        informat P012F017 best32. ;			
        informat P012F018 best32. ;			
        informat P012F019 best32. ;			
        informat P012F020 best32. ;			
        informat P012F021 best32. ;			
        informat P012F022 best32. ;			
        informat P012F023 best32. ;			
        informat P012F024 best32. ;			
        informat P012F025 best32. ;			
        informat P012F026 best32. ;			
        informat P012F027 best32. ;			
        informat P012F028 best32. ;			
        informat P012F029 best32. ;			
        informat P012F030 best32. ;			
        informat P012F031 best32. ;			
        informat P012F032 best32. ;			
        informat P012F033 best32. ;			
        informat P012F034 best32. ;			
        informat P012F035 best32. ;			
        informat P012F036 best32. ;			
        informat P012F037 best32. ;			
        informat P012F038 best32. ;			
        informat P012F039 best32. ;			
        informat P012F040 best32. ;			
        informat P012F041 best32. ;			
        informat P012F042 best32. ;			
        informat P012F043 best32. ;			
        informat P012F044 best32. ;			
        informat P012F045 best32. ;			
        informat P012F046 best32. ;			
        informat P012F047 best32. ;			
        informat P012F048 best32. ;			
        informat P012F049 best32. ;			
        informat P012G001 best32. ;			
        informat P012G002 best32. ;			
        informat P012G003 best32. ;			
        informat P012G004 best32. ;			
        informat P012G005 best32. ;			
        informat P012G006 best32. ;			
        informat P012G007 best32. ;			
        informat P012G008 best32. ;			
        informat P012G009 best32. ;			
        informat P012G010 best32. ;			
        informat P012G011 best32. ;			
        informat P012G012 best32. ;			
        informat P012G013 best32. ;			
        informat P012G014 best32. ;			
        informat P012G015 best32. ;			
        informat P012G016 best32. ;			
        informat P012G017 best32. ;			
        informat P012G018 best32. ;			
        informat P012G019 best32. ;			
        informat P012G020 best32. ;			
        informat P012G021 best32. ;			
        informat P012G022 best32. ;			
        informat P012G023 best32. ;			
        informat P012G024 best32. ;			
        informat P012G025 best32. ;			
        informat P012G026 best32. ;			
        informat P012G027 best32. ;			
        informat P012G028 best32. ;			
        informat P012G029 best32. ;			
        informat P012G030 best32. ;			
        informat P012G031 best32. ;			
        informat P012G032 best32. ;			
        informat P012G033 best32. ;			
        informat P012G034 best32. ;			
        informat P012G035 best32. ;			
        informat P012G036 best32. ;			
        informat P012G037 best32. ;			
        informat P012G038 best32. ;			
        informat P012G039 best32. ;			
        informat P012G040 best32. ;			
        informat P012G041 best32. ;			
        informat P012G042 best32. ;			
        informat P012G043 best32. ;			
        informat P012G044 best32. ;			
        informat P012G045 best32. ;			
        informat P012G046 best32. ;			
        informat P012G047 best32. ;			
        informat P012G048 best32. ;			
        informat P012G049 best32. ;			
        informat P012H001 best32. ;			
        informat P012H002 best32. ;			
        informat P012H003 best32. ;			
        informat P012H004 best32. ;			
        informat P012H005 best32. ;			
        informat P012H006 best32. ;			
        informat P012H007 best32. ;			
        informat P012H008 best32. ;			
        informat P012H009 best32. ;			
        informat P012H010 best32. ;			
        informat P012H011 best32. ;			
        informat P012H012 best32. ;			
        informat P012H013 best32. ;			
        informat P012H014 best32. ;			
        informat P012H015 best32. ;			
        informat P012H016 best32. ;			
        informat P012H017 best32. ;			
        informat P012H018 best32. ;			
        informat P012H019 best32. ;			
        informat P012H020 best32. ;			
        informat P012H021 best32. ;			
        informat P012H022 best32. ;			
        informat P012H023 best32. ;			
        informat P012H024 best32. ;			
        informat P012H025 best32. ;			
        informat P012H026 best32. ;			
        informat P012H027 best32. ;			
        informat P012H028 best32. ;			
        informat P012H029 best32. ;			
        informat P012H030 best32. ;			
        informat P012H031 best32. ;			
        informat P012H032 best32. ;			
        informat P012H033 best32. ;			
        informat P012H034 best32. ;			
        informat P012H035 best32. ;			
        informat P012H036 best32. ;			
        informat P012H037 best32. ;			
        informat P012H038 best32. ;			
        informat P012H039 best32. ;			
        informat P012H040 best32. ;			
        informat P012H041 best32. ;			
        informat P012H042 best32. ;			
        informat P012H043 best32. ;			
        informat P012H044 best32. ;			
        informat P012H045 best32. ;			
        informat P012H046 best32. ;			
        informat P012H047 best32. ;			
        informat P012H048 best32. ;			
        informat P012H049 best32. ;			
        informat P012I001 best32. ;			
        informat P012I002 best32. ;			
        informat P012I003 best32. ;			
        informat P012I004 best32. ;			
        informat P012I005 best32. ;			
        informat P012I006 best32. ;			
        informat P012I007 best32. ;			
        informat P012I008 best32. ;			
        informat P012I009 best32. ;			
        informat P012I010 best32. ;			
        informat P012I011 best32. ;			
        informat P012I012 best32. ;			
        informat P012I013 best32. ;			
        informat P012I014 best32. ;			
        informat P012I015 best32. ;			
        informat P012I016 best32. ;			
        informat P012I017 best32. ;			
        informat P012I018 best32. ;			
        informat P012I019 best32. ;			
        informat P012I020 best32. ;			
        informat P012I021 best32. ;			
        informat P012I022 best32. ;			
        informat P012I023 best32. ;			
        informat P012I024 best32. ;			
        informat P012I025 best32. ;			
        informat P012I026 best32. ;			
        informat P012I027 best32. ;			
        informat P012I028 best32. ;			
        informat P012I029 best32. ;			
        informat P012I030 best32. ;			
        informat P012I031 best32. ;			
        informat P012I032 best32. ;			
        informat P012I033 best32. ;			
        informat P012I034 best32. ;			
        informat P012I035 best32. ;			
        informat P012I036 best32. ;			
        informat P012I037 best32. ;			
        informat P012I038 best32. ;			
        informat P012I039 best32. ;			
        informat P012I040 best32. ;			
        informat P012I041 best32. ;			
        informat P012I042 best32. ;			
        informat P012I043 best32. ;			
        informat P012I044 best32. ;			
        informat P012I045 best32. ;			
        informat P012I046 best32. ;			
        informat P012I047 best32. ;			
        informat P012I048 best32. ;			
        informat P012I049 best32. ;			
        informat P013A001 best32. ;			
        informat P013A002 best32. ;			
        informat P013A003 best32. ;			
        informat P013B001 best32. ;			
        informat P013B002 best32. ;			
        informat P013B003 best32. ;			
        informat P013C001 best32. ;			
        informat P013C002 best32. ;			
        informat P013C003 best32. ;			
        informat P013D001 best32. ;			
        informat P013D002 best32. ;			
        informat P013D003 best32. ;			
        informat P013E001 best32. ;			
        informat P013E002 best32. ;			
        informat P013E003 best32. ;			
        informat P013F001 best32. ;			
        informat P013F002 best32. ;			
        informat P013F003 best32. ;			
        informat P013G001 best32. ;			
        informat P013G002 best32. ;			
        informat P013G003 best32. ;			
        informat P013H001 best32. ;			
        informat P013H002 best32. ;			
        informat P013H003 best32. ;			
        informat P013I001 best32. ;			
        informat P013I002 best32. ;			
        informat P013I003 best32. ;			
        informat P016A001 best32. ;			
        informat P016A002 best32. ;			
        informat P016A003 best32. ;			
        informat P016B001 best32. ;			
        informat P016B002 best32. ;			
        informat P016B003 best32. ;			
        informat P016C001 best32. ;			
        informat P016C002 best32. ;			
        informat P016C003 best32. ;			
        informat P016D001 best32. ;			
        informat P016D002 best32. ;			
        informat P016D003 best32. ;			
        informat P016E001 best32. ;			
        informat P016E002 best32. ;			
        informat P016E003 best32. ;			
        informat P016F001 best32. ;			
        informat P016F002 best32. ;			
        informat P016F003 best32. ;			
        informat P016G001 best32. ;			
        informat P016G002 best32. ;			
        informat P016G003 best32. ;			
        informat P016H001 best32. ;			
        informat P016H002 best32. ;			
        informat P016H003 best32. ;			
        informat P016I001 best32. ;			
        informat P016I002 best32. ;			
        informat P016I003 best32. ;			
        informat P017A001 best32. ;			
        informat P017A002 best32. ;			
        informat P017A003 best32. ;			
        informat P017B001 best32. ;			
        informat P017B002 best32. ;			
        informat P017B003 best32. ;			
        informat P017C001 best32. ;			
        informat P017C002 best32. ;			
        informat P017C003 best32. ;			
        informat P017D001 best32. ;			
        informat P017D002 best32. ;			
        informat P017D003 best32. ;			
        informat P017E001 best32. ;			
        informat P017E002 best32. ;			
        informat P017E003 best32. ;			
        informat P017F001 best32. ;			
        informat P017F002 best32. ;			
        informat P017F003 best32. ;			
        informat P017G001 best32. ;			
        informat P017G002 best32. ;			
        informat P017G003 best32. ;			
        informat P017H001 best32. ;			
        informat P017H002 best32. ;			
        informat P017H003 best32. ;			
        informat P017I001 best32. ;			
        informat P017I002 best32. ;			
        informat P017I003 best32. ;			
        informat P018A001 best32. ;			
        informat P018A002 best32. ;			
        informat P018A003 best32. ;			
        informat P018A004 best32. ;			
        informat P018A005 best32. ;			
        informat P018A006 best32. ;			
        informat P018A007 best32. ;			
        informat P018A008 best32. ;			
        informat P018A009 best32. ;			
        informat P018B001 best32. ;			
        informat P018B002 best32. ;			
        informat P018B003 best32. ;			
        informat P018B004 best32. ;			
        informat P018B005 best32. ;			
        informat P018B006 best32. ;			
        informat P018B007 best32. ;			
        informat P018B008 best32. ;			
        informat P018B009 best32. ;			
        informat P018C001 best32. ;			
        informat P018C002 best32. ;			
        informat P018C003 best32. ;			
        informat P018C004 best32. ;			
        informat P018C005 best32. ;			
        informat P018C006 best32. ;			
        informat P018C007 best32. ;			
        informat P018C008 best32. ;			
        informat P018C009 best32. ;			
        informat P018D001 best32. ;			
        informat P018D002 best32. ;			
        informat P018D003 best32. ;			
        informat P018D004 best32. ;			
        informat P018D005 best32. ;			
        informat P018D006 best32. ;			
        informat P018D007 best32. ;			
        informat P018D008 best32. ;			
        informat P018D009 best32. ;			
        informat P018E001 best32. ;			
        informat P018E002 best32. ;			
        informat P018E003 best32. ;			
        informat P018E004 best32. ;			
        informat P018E005 best32. ;			
        informat P018E006 best32. ;			
        informat P018E007 best32. ;			
        informat P018E008 best32. ;			
        informat P018E009 best32. ;			
        informat P018F001 best32. ;			
        informat P018F002 best32. ;			
        informat P018F003 best32. ;			
        informat P018F004 best32. ;			
        informat P018F005 best32. ;			
        informat P018F006 best32. ;			
        informat P018F007 best32. ;			
        informat P018F008 best32. ;			
        informat P018F009 best32. ;			
        informat P018G001 best32. ;			
        informat P018G002 best32. ;			
        informat P018G003 best32. ;			
        informat P018G004 best32. ;			
        informat P018G005 best32. ;			
        informat P018G006 best32. ;			
        informat P018G007 best32. ;			
        informat P018G008 best32. ;			
        informat P018G009 best32. ;			
        informat P018H001 best32. ;			
        informat P018H002 best32. ;			
        informat P018H003 best32. ;			
        informat P018H004 best32. ;			
        informat P018H005 best32. ;			
        informat P018H006 best32. ;			
        informat P018H007 best32. ;			
        informat P018H008 best32. ;			
        informat P018H009 best32. ;			
        informat P018I001 best32. ;			
        informat P018I002 best32. ;			
        informat P018I003 best32. ;			
        informat P018I004 best32. ;			
        informat P018I005 best32. ;			
        informat P018I006 best32. ;			
        informat P018I007 best32. ;			
        informat P018I008 best32. ;			
        informat P018I009 best32. ;			
        informat P028A001 best32. ;			
        informat P028A002 best32. ;			
        informat P028A003 best32. ;			
        informat P028A004 best32. ;			
        informat P028A005 best32. ;			
        informat P028A006 best32. ;			
        informat P028A007 best32. ;			
        informat P028A008 best32. ;			
        informat P028A009 best32. ;			
        informat P028A010 best32. ;			
        informat P028A011 best32. ;			
        informat P028A012 best32. ;			
        informat P028A013 best32. ;			
        informat P028A014 best32. ;			
        informat P028A015 best32. ;			
        informat P028A016 best32. ;			
        informat P028B001 best32. ;			
        informat P028B002 best32. ;			
        informat P028B003 best32. ;			
        informat P028B004 best32. ;			
        informat P028B005 best32. ;			
        informat P028B006 best32. ;			
        informat P028B007 best32. ;			
        informat P028B008 best32. ;			
        informat P028B009 best32. ;			
        informat P028B010 best32. ;			
        informat P028B011 best32. ;			
        informat P028B012 best32. ;			
        informat P028B013 best32. ;			
        informat P028B014 best32. ;			
        informat P028B015 best32. ;			
        informat P028B016 best32. ;			
        informat P028C001 best32. ;			
        informat P028C002 best32. ;			
        informat P028C003 best32. ;			
        informat P028C004 best32. ;			
        informat P028C005 best32. ;			
        informat P028C006 best32. ;			
        informat P028C007 best32. ;			
        informat P028C008 best32. ;			
        informat P028C009 best32. ;			
        informat P028C010 best32. ;			
        informat P028C011 best32. ;			
        informat P028C012 best32. ;			
        informat P028C013 best32. ;			
        informat P028C014 best32. ;			
        informat P028C015 best32. ;			
        informat P028C016 best32. ;			
        informat P028D001 best32. ;			
        informat P028D002 best32. ;			
        informat P028D003 best32. ;			
        informat P028D004 best32. ;			
        informat P028D005 best32. ;			
        informat P028D006 best32. ;			
        informat P028D007 best32. ;			
        informat P028D008 best32. ;			
        informat P028D009 best32. ;			
        informat P028D010 best32. ;			
        informat P028D011 best32. ;			
        informat P028D012 best32. ;			
        informat P028D013 best32. ;			
        informat P028D014 best32. ;			
        informat P028D015 best32. ;			
        informat P028D016 best32. ;			
        informat P028E001 best32. ;			
        informat P028E002 best32. ;			
        informat P028E003 best32. ;			
        informat P028E004 best32. ;			
        informat P028E005 best32. ;			
        informat P028E006 best32. ;			
        informat P028E007 best32. ;			
        informat P028E008 best32. ;			
        informat P028E009 best32. ;			
        informat P028E010 best32. ;			
        informat P028E011 best32. ;			
        informat P028E012 best32. ;			
        informat P028E013 best32. ;			
        informat P028E014 best32. ;			
        informat P028E015 best32. ;			
        informat P028E016 best32. ;			
        informat P028F001 best32. ;			
        informat P028F002 best32. ;			
        informat P028F003 best32. ;			
        informat P028F004 best32. ;			
        informat P028F005 best32. ;			
        informat P028F006 best32. ;			
        informat P028F007 best32. ;			
        informat P028F008 best32. ;			
        informat P028F009 best32. ;			
        informat P028F010 best32. ;			
        informat P028F011 best32. ;			
        informat P028F012 best32. ;			
        informat P028F013 best32. ;			
        informat P028F014 best32. ;			
        informat P028F015 best32. ;			
        informat P028F016 best32. ;			
        informat P028G001 best32. ;			
        informat P028G002 best32. ;			
        informat P028G003 best32. ;			
        informat P028G004 best32. ;			
        informat P028G005 best32. ;			
        informat P028G006 best32. ;			
        informat P028G007 best32. ;			
        informat P028G008 best32. ;			
        informat P028G009 best32. ;			
        informat P028G010 best32. ;			
        informat P028G011 best32. ;			
        informat P028G012 best32. ;			
        informat P028G013 best32. ;			
        informat P028G014 best32. ;			
        informat P028G015 best32. ;			
        informat P028G016 best32. ;			
        informat P028H001 best32. ;			
        informat P028H002 best32. ;			
        informat P028H003 best32. ;			
        informat P028H004 best32. ;			
        informat P028H005 best32. ;			
        informat P028H006 best32. ;			
        informat P028H007 best32. ;			
        informat P028H008 best32. ;			
        informat P028H009 best32. ;			
        informat P028H010 best32. ;			
        informat P028H011 best32. ;			
        informat P028H012 best32. ;			
        informat P028H013 best32. ;			
        informat P028H014 best32. ;			
        informat P028H015 best32. ;			
        informat P028H016 best32. ;			
        informat P028I001 best32. ;			
        informat P028I002 best32. ;			
        informat P028I003 best32. ;			
        informat P028I004 best32. ;			
        informat P028I005 best32. ;			
        informat P028I006 best32. ;			
        informat P028I007 best32. ;			
        informat P028I008 best32. ;			
        informat P028I009 best32. ;			
        informat P028I010 best32. ;			
        informat P028I011 best32. ;			
        informat P028I012 best32. ;			
        informat P028I013 best32. ;			
        informat P028I014 best32. ;			
        informat P028I015 best32. ;			
        informat P028I016 best32. ;			
        informat P029A001 best32. ;			
        informat P029A002 best32. ;			
        informat P029A003 best32. ;			
        informat P029A004 best32. ;			
        informat P029A005 best32. ;			
        informat P029A006 best32. ;			
        informat P029A007 best32. ;			
        informat P029A008 best32. ;			
        informat P029A009 best32. ;			
        informat P029A010 best32. ;			
        informat P029A011 best32. ;			
        informat P029A012 best32. ;			
        informat P029A013 best32. ;			
        informat P029A014 best32. ;			
        informat P029A015 best32. ;			
        informat P029A016 best32. ;			
        informat P029A017 best32. ;			
        informat P029A018 best32. ;			
        informat P029A019 best32. ;			
        informat P029A020 best32. ;			
        informat P029A021 best32. ;			
        informat P029A022 best32. ;			
        informat P029A023 best32. ;			
        informat P029A024 best32. ;			
        informat P029A025 best32. ;			
        informat P029A026 best32. ;			
        informat P029A027 best32. ;			
        informat P029A028 best32. ;			
        informat P029B001 best32. ;			
        informat P029B002 best32. ;			
        informat P029B003 best32. ;			
        informat P029B004 best32. ;			
        informat P029B005 best32. ;			
        informat P029B006 best32. ;			
        informat P029B007 best32. ;			
        informat P029B008 best32. ;			
        informat P029B009 best32. ;			
        informat P029B010 best32. ;			
        informat P029B011 best32. ;			
        informat P029B012 best32. ;			
        informat P029B013 best32. ;			
        informat P029B014 best32. ;			
        informat P029B015 best32. ;			
        informat P029B016 best32. ;			
        informat P029B017 best32. ;			
        informat P029B018 best32. ;			
        informat P029B019 best32. ;			
        informat P029B020 best32. ;			
        informat P029B021 best32. ;			
        informat P029B022 best32. ;			
        informat P029B023 best32. ;			
        informat P029B024 best32. ;			
        informat P029B025 best32. ;			
        informat P029B026 best32. ;			
        informat P029B027 best32. ;			
        informat P029B028 best32. ;			
        informat P029C001 best32. ;			
        informat P029C002 best32. ;			
        informat P029C003 best32. ;			
        informat P029C004 best32. ;			
        informat P029C005 best32. ;			
        informat P029C006 best32. ;			
        informat P029C007 best32. ;			
        informat P029C008 best32. ;			
        informat P029C009 best32. ;			
        informat P029C010 best32. ;			
        informat P029C011 best32. ;			
        informat P029C012 best32. ;			
        informat P029C013 best32. ;			
        informat P029C014 best32. ;			
        informat P029C015 best32. ;			
        informat P029C016 best32. ;			
        informat P029C017 best32. ;			
        informat P029C018 best32. ;			
        informat P029C019 best32. ;			
        informat P029C020 best32. ;			
        informat P029C021 best32. ;			
        informat P029C022 best32. ;			
        informat P029C023 best32. ;			
        informat P029C024 best32. ;			
        informat P029C025 best32. ;			
        informat P029C026 best32. ;			
        informat P029C027 best32. ;			
        informat P029C028 best32. ;			
        informat P029D001 best32. ;			
        informat P029D002 best32. ;			
        informat P029D003 best32. ;			
        informat P029D004 best32. ;			
        informat P029D005 best32. ;			
        informat P029D006 best32. ;			
        informat P029D007 best32. ;			
        informat P029D008 best32. ;			
        informat P029D009 best32. ;			
        informat P029D010 best32. ;			
        informat P029D011 best32. ;			
        informat P029D012 best32. ;			
        informat P029D013 best32. ;			
        informat P029D014 best32. ;			
        informat P029D015 best32. ;			
        informat P029D016 best32. ;			
        informat P029D017 best32. ;			
        informat P029D018 best32. ;			
        informat P029D019 best32. ;			
        informat P029D020 best32. ;			
        informat P029D021 best32. ;			
        informat P029D022 best32. ;			
        informat P029D023 best32. ;			
        informat P029D024 best32. ;			
        informat P029D025 best32. ;			
        informat P029D026 best32. ;			
        informat P029D027 best32. ;			
        informat P029D028 best32. ;			
        informat P029E001 best32. ;			
        informat P029E002 best32. ;			
        informat P029E003 best32. ;			
        informat P029E004 best32. ;			
        informat P029E005 best32. ;			
        informat P029E006 best32. ;			
        informat P029E007 best32. ;			
        informat P029E008 best32. ;			
        informat P029E009 best32. ;			
        informat P029E010 best32. ;			
        informat P029E011 best32. ;			
        informat P029E012 best32. ;			
        informat P029E013 best32. ;			
        informat P029E014 best32. ;			
        informat P029E015 best32. ;			
        informat P029E016 best32. ;			
        informat P029E017 best32. ;			
        informat P029E018 best32. ;			
        informat P029E019 best32. ;			
        informat P029E020 best32. ;			
        informat P029E021 best32. ;			
        informat P029E022 best32. ;			
        informat P029E023 best32. ;			
        informat P029E024 best32. ;			
        informat P029E025 best32. ;			
        informat P029E026 best32. ;			
        informat P029E027 best32. ;			
        informat P029E028 best32. ;			
        informat P029F001 best32. ;			
        informat P029F002 best32. ;			
        informat P029F003 best32. ;			
        informat P029F004 best32. ;			
        informat P029F005 best32. ;			
        informat P029F006 best32. ;			
        informat P029F007 best32. ;			
        informat P029F008 best32. ;			
        informat P029F009 best32. ;			
        informat P029F010 best32. ;			
        informat P029F011 best32. ;			
        informat P029F012 best32. ;			
        informat P029F013 best32. ;			
        informat P029F014 best32. ;			
        informat P029F015 best32. ;			
        informat P029F016 best32. ;			
        informat P029F017 best32. ;			
        informat P029F018 best32. ;			
        informat P029F019 best32. ;			
        informat P029F020 best32. ;			
        informat P029F021 best32. ;			
        informat P029F022 best32. ;			
        informat P029F023 best32. ;			
        informat P029F024 best32. ;			
        informat P029F025 best32. ;			
        informat P029F026 best32. ;			
        informat P029F027 best32. ;			
        informat P029F028 best32. ;			
        informat P029G001 best32. ;			
        informat P029G002 best32. ;			
        informat P029G003 best32. ;			
        informat P029G004 best32. ;			
        informat P029G005 best32. ;			
        informat P029G006 best32. ;			
        informat P029G007 best32. ;			
        informat P029G008 best32. ;			
        informat P029G009 best32. ;			
        informat P029G010 best32. ;			
        informat P029G011 best32. ;			
        informat P029G012 best32. ;			
        informat P029G013 best32. ;			
        informat P029G014 best32. ;			
        informat P029G015 best32. ;			
        informat P029G016 best32. ;			
        informat P029G017 best32. ;			
        informat P029G018 best32. ;			
        informat P029G019 best32. ;			
        informat P029G020 best32. ;			
        informat P029G021 best32. ;			
        informat P029G022 best32. ;			
        informat P029G023 best32. ;			
        informat P029G024 best32. ;			
        informat P029G025 best32. ;			
        informat P029G026 best32. ;			
        informat P029G027 best32. ;			
        informat P029G028 best32. ;			
        informat P029H001 best32. ;			
        informat P029H002 best32. ;			
        informat P029H003 best32. ;			
        informat P029H004 best32. ;			
        informat P029H005 best32. ;			
        informat P029H006 best32. ;			
        informat P029H007 best32. ;			
        informat P029H008 best32. ;			
        informat P029H009 best32. ;			
        informat P029H010 best32. ;			
        informat P029H011 best32. ;			
        informat P029H012 best32. ;			
        informat P029H013 best32. ;			
        informat P029H014 best32. ;			
        informat P029H015 best32. ;			
        informat P029H016 best32. ;			
        informat P029H017 best32. ;			
        informat P029H018 best32. ;			
        informat P029H019 best32. ;			
        informat P029H020 best32. ;			
        informat P029H021 best32. ;			
        informat P029H022 best32. ;			
        informat P029H023 best32. ;			
        informat P029H024 best32. ;			
        informat P029H025 best32. ;			
        informat P029H026 best32. ;			
        informat P029H027 best32. ;			
        informat P029H028 best32. ;			
        informat P029I001 best32. ;			
        informat P029I002 best32. ;			
        informat P029I003 best32. ;			
        informat P029I004 best32. ;			
        informat P029I005 best32. ;			
        informat P029I006 best32. ;			
        informat P029I007 best32. ;			
        informat P029I008 best32. ;			
        informat P029I009 best32. ;			
        informat P029I010 best32. ;			
        informat P029I011 best32. ;			
        informat P029I012 best32. ;			
        informat P029I013 best32. ;			
        informat P029I014 best32. ;			
        informat P029I015 best32. ;			
        informat P029I016 best32. ;			
        informat P029I017 best32. ;			
        informat P029I018 best32. ;			
        informat P029I019 best32. ;			
        informat P029I020 best32. ;			
        informat P029I021 best32. ;			
        informat P029I022 best32. ;			
        informat P029I023 best32. ;			
        informat P029I024 best32. ;			
        informat P029I025 best32. ;			
        informat P029I026 best32. ;			
        informat P029I027 best32. ;			
        informat P029I028 best32. ;			
        informat P031A001 best32. ;			
        informat P031A002 best32. ;			
        informat P031A003 best32. ;			
        informat P031A004 best32. ;			
        informat P031A005 best32. ;			
        informat P031A006 best32. ;			
        informat P031A007 best32. ;			
        informat P031A008 best32. ;			
        informat P031A009 best32. ;			
        informat P031A010 best32. ;			
        informat P031A011 best32. ;			
        informat P031A012 best32. ;			
        informat P031A013 best32. ;			
        informat P031A014 best32. ;			
        informat P031A015 best32. ;			
        informat P031A016 best32. ;			
        informat P031B001 best32. ;			
        informat P031B002 best32. ;			
        informat P031B003 best32. ;			
        informat P031B004 best32. ;			
        informat P031B005 best32. ;			
        informat P031B006 best32. ;			
        informat P031B007 best32. ;			
        informat P031B008 best32. ;			
        informat P031B009 best32. ;			
        informat P031B010 best32. ;			
        informat P031B011 best32. ;			
        informat P031B012 best32. ;			
        informat P031B013 best32. ;			
        informat P031B014 best32. ;			
        informat P031B015 best32. ;			
        informat P031B016 best32. ;			
        informat P031C001 best32. ;			
        informat P031C002 best32. ;			
        informat P031C003 best32. ;			
        informat P031C004 best32. ;			
        informat P031C005 best32. ;			
        informat P031C006 best32. ;			
        informat P031C007 best32. ;			
        informat P031C008 best32. ;			
        informat P031C009 best32. ;			
        informat P031C010 best32. ;			
        informat P031C011 best32. ;			
        informat P031C012 best32. ;			
        informat P031C013 best32. ;			
        informat P031C014 best32. ;			
        informat P031C015 best32. ;			
        informat P031C016 best32. ;			
        informat P031D001 best32. ;			
        informat P031D002 best32. ;			
        informat P031D003 best32. ;			
        informat P031D004 best32. ;			
        informat P031D005 best32. ;			
        informat P031D006 best32. ;			
        informat P031D007 best32. ;			
        informat P031D008 best32. ;			
        informat P031D009 best32. ;			
        informat P031D010 best32. ;			
        informat P031D011 best32. ;			
        informat P031D012 best32. ;			
        informat P031D013 best32. ;			
        informat P031D014 best32. ;			
        informat P031D015 best32. ;			
        informat P031D016 best32. ;			
        informat P031E001 best32. ;			
        informat P031E002 best32. ;			
        informat P031E003 best32. ;			
        informat P031E004 best32. ;			
        informat P031E005 best32. ;			
        informat P031E006 best32. ;			
        informat P031E007 best32. ;			
        informat P031E008 best32. ;			
        informat P031E009 best32. ;			
        informat P031E010 best32. ;			
        informat P031E011 best32. ;			
        informat P031E012 best32. ;			
        informat P031E013 best32. ;			
        informat P031E014 best32. ;			
        informat P031E015 best32. ;			
        informat P031E016 best32. ;			
        informat P031F001 best32. ;			
        informat P031F002 best32. ;			
        informat P031F003 best32. ;			
        informat P031F004 best32. ;			
        informat P031F005 best32. ;			
        informat P031F006 best32. ;			
        informat P031F007 best32. ;			
        informat P031F008 best32. ;			
        informat P031F009 best32. ;			
        informat P031F010 best32. ;			
        informat P031F011 best32. ;			
        informat P031F012 best32. ;			
        informat P031F013 best32. ;			
        informat P031F014 best32. ;			
        informat P031F015 best32. ;			
        informat P031F016 best32. ;			
        informat P031G001 best32. ;			
        informat P031G002 best32. ;			
        informat P031G003 best32. ;			
        informat P031G004 best32. ;			
        informat P031G005 best32. ;			
        informat P031G006 best32. ;			
        informat P031G007 best32. ;			
        informat P031G008 best32. ;			
        informat P031G009 best32. ;			
        informat P031G010 best32. ;			
        informat P031G011 best32. ;			
        informat P031G012 best32. ;			
        informat P031G013 best32. ;			
        informat P031G014 best32. ;			
        informat P031G015 best32. ;			
        informat P031G016 best32. ;			
        informat P031H001 best32. ;			
        informat P031H002 best32. ;			
        informat P031H003 best32. ;			
        informat P031H004 best32. ;			
        informat P031H005 best32. ;			
        informat P031H006 best32. ;			
        informat P031H007 best32. ;			
        informat P031H008 best32. ;			
        informat P031H009 best32. ;			
        informat P031H010 best32. ;			
        informat P031H011 best32. ;			
        informat P031H012 best32. ;			
        informat P031H013 best32. ;			
        informat P031H014 best32. ;			
        informat P031H015 best32. ;			
        informat P031H016 best32. ;			
        informat P031I001 best32. ;			
        informat P031I002 best32. ;			
        informat P031I003 best32. ;			
        informat P031I004 best32. ;			
        informat P031I005 best32. ;			
        informat P031I006 best32. ;			
        informat P031I007 best32. ;			
        informat P031I008 best32. ;			
        informat P031I009 best32. ;			
        informat P031I010 best32. ;			
        informat P031I011 best32. ;			
        informat P031I012 best32. ;			
        informat P031I013 best32. ;			
        informat P031I014 best32. ;			
        informat P031I015 best32. ;			
        informat P031I016 best32. ;			
        informat P034A001 best32. ;			
        informat P034A002 best32. ;			
        informat P034A003 best32. ;			
        informat P034A004 best32. ;			
        informat P034A005 best32. ;			
        informat P034A006 best32. ;			
        informat P034A007 best32. ;			
        informat P034A008 best32. ;			
        informat P034A009 best32. ;			
        informat P034A010 best32. ;			
        informat P034A011 best32. ;			
        informat P034A012 best32. ;			
        informat P034A013 best32. ;			
        informat P034A014 best32. ;			
        informat P034A015 best32. ;			
        informat P034A016 best32. ;			
        informat P034A017 best32. ;			
        informat P034A018 best32. ;			
        informat P034A019 best32. ;			
        informat P034A020 best32. ;			
        informat P034A021 best32. ;			
        informat P034A022 best32. ;			
        informat P034B001 best32. ;			
        informat P034B002 best32. ;			
        informat P034B003 best32. ;			
        informat P034B004 best32. ;			
        informat P034B005 best32. ;			
        informat P034B006 best32. ;			
        informat P034B007 best32. ;			
        informat P034B008 best32. ;			
        informat P034B009 best32. ;			
        informat P034B010 best32. ;			
        informat P034B011 best32. ;			
        informat P034B012 best32. ;			
        informat P034B013 best32. ;			
        informat P034B014 best32. ;			
        informat P034B015 best32. ;			
        informat P034B016 best32. ;			
        informat P034B017 best32. ;			
        informat P034B018 best32. ;			
        informat P034B019 best32. ;			
        informat P034B020 best32. ;			
        informat P034B021 best32. ;			
        informat P034B022 best32. ;			
        informat P034C001 best32. ;			
        informat P034C002 best32. ;			
        informat P034C003 best32. ;			
        informat P034C004 best32. ;			
        informat P034C005 best32. ;			
        informat P034C006 best32. ;			
        informat P034C007 best32. ;			
        informat P034C008 best32. ;			
        informat P034C009 best32. ;			
        informat P034C010 best32. ;			
        informat P034C011 best32. ;			
        informat P034C012 best32. ;			
        informat P034C013 best32. ;			
        informat P034C014 best32. ;			
        informat P034C015 best32. ;			
        informat P034C016 best32. ;			
        informat P034C017 best32. ;			
        informat P034C018 best32. ;			
        informat P034C019 best32. ;			
        informat P034C020 best32. ;			
        informat P034C021 best32. ;			
        informat P034C022 best32. ;			
        informat P034D001 best32. ;			
        informat P034D002 best32. ;			
        informat P034D003 best32. ;			
        informat P034D004 best32. ;			
        informat P034D005 best32. ;			
        informat P034D006 best32. ;			
        informat P034D007 best32. ;			
        informat P034D008 best32. ;			
        informat P034D009 best32. ;			
        informat P034D010 best32. ;			
        informat P034D011 best32. ;			
        informat P034D012 best32. ;			
        informat P034D013 best32. ;			
        informat P034D014 best32. ;			
        informat P034D015 best32. ;			
        informat P034D016 best32. ;			
        informat P034D017 best32. ;			
        informat P034D018 best32. ;			
        informat P034D019 best32. ;			
        informat P034D020 best32. ;			
        informat P034D021 best32. ;			
        informat P034D022 best32. ;			
        informat P034E001 best32. ;			
        informat P034E002 best32. ;			
        informat P034E003 best32. ;			
        informat P034E004 best32. ;			
        informat P034E005 best32. ;			
        informat P034E006 best32. ;			
        informat P034E007 best32. ;			
        informat P034E008 best32. ;			
        informat P034E009 best32. ;			
        informat P034E010 best32. ;			
        informat P034E011 best32. ;			
        informat P034E012 best32. ;			
        informat P034E013 best32. ;			
        informat P034E014 best32. ;			
        informat P034E015 best32. ;			
        informat P034E016 best32. ;			
        informat P034E017 best32. ;			
        informat P034E018 best32. ;			
        informat P034E019 best32. ;			
        informat P034E020 best32. ;			
        informat P034E021 best32. ;			
        informat P034E022 best32. ;			
        informat P034F001 best32. ;			
        informat P034F002 best32. ;			
        informat P034F003 best32. ;			
        informat P034F004 best32. ;			
        informat P034F005 best32. ;			
        informat P034F006 best32. ;			
        informat P034F007 best32. ;			
        informat P034F008 best32. ;			
        informat P034F009 best32. ;			
        informat P034F010 best32. ;			
        informat P034F011 best32. ;			
        informat P034F012 best32. ;			
        informat P034F013 best32. ;			
        informat P034F014 best32. ;			
        informat P034F015 best32. ;			
        informat P034F016 best32. ;			
        informat P034F017 best32. ;			
        informat P034F018 best32. ;			
        informat P034F019 best32. ;			
        informat P034F020 best32. ;			
        informat P034F021 best32. ;			
        informat P034F022 best32. ;			
        informat P034G001 best32. ;			
        informat P034G002 best32. ;			
        informat P034G003 best32. ;			
        informat P034G004 best32. ;			
        informat P034G005 best32. ;			
        informat P034G006 best32. ;			
        informat P034G007 best32. ;			
        informat P034G008 best32. ;			
        informat P034G009 best32. ;			
        informat P034G010 best32. ;			
        informat P034G011 best32. ;			
        informat P034G012 best32. ;			
        informat P034G013 best32. ;			
        informat P034G014 best32. ;			
        informat P034G015 best32. ;			
        informat P034G016 best32. ;			
        informat P034G017 best32. ;			
        informat P034G018 best32. ;			
        informat P034G019 best32. ;			
        informat P034G020 best32. ;			
        informat P034G021 best32. ;			
        informat P034G022 best32. ;			
        informat P034H001 best32. ;			
        informat P034H002 best32. ;			
        informat P034H003 best32. ;			
        informat P034H004 best32. ;			
        informat P034H005 best32. ;			
        informat P034H006 best32. ;			
        informat P034H007 best32. ;			
        informat P034H008 best32. ;			
        informat P034H009 best32. ;			
        informat P034H010 best32. ;			
        informat P034H011 best32. ;			
        informat P034H012 best32. ;			
        informat P034H013 best32. ;			
        informat P034H014 best32. ;			
        informat P034H015 best32. ;			
        informat P034H016 best32. ;			
        informat P034H017 best32. ;			
        informat P034H018 best32. ;			
        informat P034H019 best32. ;			
        informat P034H020 best32. ;			
        informat P034H021 best32. ;			
        informat P034H022 best32. ;			
        informat P034I001 best32. ;			
        informat P034I002 best32. ;			
        informat P034I003 best32. ;			
        informat P034I004 best32. ;			
        informat P034I005 best32. ;			
        informat P034I006 best32. ;			
        informat P034I007 best32. ;			
        informat P034I008 best32. ;			
        informat P034I009 best32. ;			
        informat P034I010 best32. ;			
        informat P034I011 best32. ;			
        informat P034I012 best32. ;			
        informat P034I013 best32. ;			
        informat P034I014 best32. ;			
        informat P034I015 best32. ;			
        informat P034I016 best32. ;			
        informat P034I017 best32. ;			
        informat P034I018 best32. ;			
        informat P034I019 best32. ;			
        informat P034I020 best32. ;			
        informat P034I021 best32. ;			
        informat P034I022 best32. ;			
        informat P035A001 best32. ;			
        informat P035B001 best32. ;			
        informat P035C001 best32. ;			
        informat P035D001 best32. ;			
        informat P035E001 best32. ;			
        informat P035F001 best32. ;			
        informat P035G001 best32. ;			
        informat P035H001 best32. ;			
        informat P035I001 best32. ;			
        informat P036A001 best32. ;			
        informat P036A002 best32. ;			
        informat P036A003 best32. ;			
        informat P036B001 best32. ;			
        informat P036B002 best32. ;			
        informat P036B003 best32. ;			
        informat P036C001 best32. ;			
        informat P036C002 best32. ;			
        informat P036C003 best32. ;			
        informat P036D001 best32. ;			
        informat P036D002 best32. ;			
        informat P036D003 best32. ;			
        informat P036E001 best32. ;			
        informat P036E002 best32. ;			
        informat P036E003 best32. ;			
        informat P036F001 best32. ;			
        informat P036F002 best32. ;			
        informat P036F003 best32. ;			
        informat P036G001 best32. ;			
        informat P036G002 best32. ;			
        informat P036G003 best32. ;			
        informat P036H001 best32. ;			
        informat P036H002 best32. ;			
        informat P036H003 best32. ;			
        informat P036I001 best32. ;			
        informat P036I002 best32. ;			
        informat P036I003 best32. ;			
        informat P037A001 best32. ;			
        informat P037A002 best32. ;			
        informat P037A003 best32. ;			
        informat P037B001 best32. ;			
        informat P037B002 best32. ;			
        informat P037B003 best32. ;			
        informat P037C001 best32. ;			
        informat P037C002 best32. ;			
        informat P037C003 best32. ;			
        informat P037D001 best32. ;			
        informat P037D002 best32. ;			
        informat P037D003 best32. ;			
        informat P037E001 best32. ;			
        informat P037E002 best32. ;			
        informat P037E003 best32. ;			
        informat P037F001 best32. ;			
        informat P037F002 best32. ;			
        informat P037F003 best32. ;			
        informat P037G001 best32. ;			
        informat P037G002 best32. ;			
        informat P037G003 best32. ;			
        informat P037H001 best32. ;			
        informat P037H002 best32. ;			
        informat P037H003 best32. ;			
        informat P037I001 best32. ;			
        informat P037I002 best32. ;			
        informat P037I003 best32. ;			
        informat P038A001 best32. ;			
        informat P038A002 best32. ;			
        informat P038A003 best32. ;			
        informat P038A004 best32. ;			
        informat P038A005 best32. ;			
        informat P038A006 best32. ;			
        informat P038A007 best32. ;			
        informat P038A008 best32. ;			
        informat P038A009 best32. ;			
        informat P038A010 best32. ;			
        informat P038A011 best32. ;			
        informat P038A012 best32. ;			
        informat P038A013 best32. ;			
        informat P038A014 best32. ;			
        informat P038A015 best32. ;			
        informat P038A016 best32. ;			
        informat P038A017 best32. ;			
        informat P038A018 best32. ;			
        informat P038A019 best32. ;			
        informat P038A020 best32. ;			
        informat P038B001 best32. ;			
        informat P038B002 best32. ;			
        informat P038B003 best32. ;			
        informat P038B004 best32. ;			
        informat P038B005 best32. ;			
        informat P038B006 best32. ;			
        informat P038B007 best32. ;			
        informat P038B008 best32. ;			
        informat P038B009 best32. ;			
        informat P038B010 best32. ;			
        informat P038B011 best32. ;			
        informat P038B012 best32. ;			
        informat P038B013 best32. ;			
        informat P038B014 best32. ;			
        informat P038B015 best32. ;			
        informat P038B016 best32. ;			
        informat P038B017 best32. ;			
        informat P038B018 best32. ;			
        informat P038B019 best32. ;			
        informat P038B020 best32. ;			
        informat P038C001 best32. ;			
        informat P038C002 best32. ;			
        informat P038C003 best32. ;			
        informat P038C004 best32. ;			
        informat P038C005 best32. ;			
        informat P038C006 best32. ;			
        informat P038C007 best32. ;			
        informat P038C008 best32. ;			
        informat P038C009 best32. ;			
        informat P038C010 best32. ;			
        informat P038C011 best32. ;			
        informat P038C012 best32. ;			
        informat P038C013 best32. ;			
        informat P038C014 best32. ;			
        informat P038C015 best32. ;			
        informat P038C016 best32. ;			
        informat P038C017 best32. ;			
        informat P038C018 best32. ;			
        informat P038C019 best32. ;			
        informat P038C020 best32. ;			
        informat P038D001 best32. ;			
        informat P038D002 best32. ;			
        informat P038D003 best32. ;			
        informat P038D004 best32. ;			
        informat P038D005 best32. ;			
        informat P038D006 best32. ;			
        informat P038D007 best32. ;			
        informat P038D008 best32. ;			
        informat P038D009 best32. ;			
        informat P038D010 best32. ;			
        informat P038D011 best32. ;			
        informat P038D012 best32. ;			
        informat P038D013 best32. ;			
        informat P038D014 best32. ;			
        informat P038D015 best32. ;			
        informat P038D016 best32. ;			
        informat P038D017 best32. ;			
        informat P038D018 best32. ;			
        informat P038D019 best32. ;			
        informat P038D020 best32. ;			
        informat P038E001 best32. ;			
        informat P038E002 best32. ;			
        informat P038E003 best32. ;			
        informat P038E004 best32. ;			
        informat P038E005 best32. ;			
        informat P038E006 best32. ;			
        informat P038E007 best32. ;			
        informat P038E008 best32. ;			
        informat P038E009 best32. ;			
        informat P038E010 best32. ;			
        informat P038E011 best32. ;			
        informat P038E012 best32. ;			
        informat P038E013 best32. ;			
        informat P038E014 best32. ;			
        informat P038E015 best32. ;			
        informat P038E016 best32. ;			
        informat P038E017 best32. ;			
        informat P038E018 best32. ;			
        informat P038E019 best32. ;			
        informat P038E020 best32. ;			
        informat P038F001 best32. ;			
        informat P038F002 best32. ;			
        informat P038F003 best32. ;			
        informat P038F004 best32. ;			
        informat P038F005 best32. ;			
        informat P038F006 best32. ;			
        informat P038F007 best32. ;			
        informat P038F008 best32. ;			
        informat P038F009 best32. ;			
        informat P038F010 best32. ;			
        informat P038F011 best32. ;			
        informat P038F012 best32. ;			
        informat P038F013 best32. ;			
        informat P038F014 best32. ;			
        informat P038F015 best32. ;			
        informat P038F016 best32. ;			
        informat P038F017 best32. ;			
        informat P038F018 best32. ;			
        informat P038F019 best32. ;			
        informat P038F020 best32. ;			
        informat P038G001 best32. ;			
        informat P038G002 best32. ;			
        informat P038G003 best32. ;			
        informat P038G004 best32. ;			
        informat P038G005 best32. ;			
        informat P038G006 best32. ;			
        informat P038G007 best32. ;			
        informat P038G008 best32. ;			
        informat P038G009 best32. ;			
        informat P038G010 best32. ;			
        informat P038G011 best32. ;			
        informat P038G012 best32. ;			
        informat P038G013 best32. ;			
        informat P038G014 best32. ;			
        informat P038G015 best32. ;			
        informat P038G016 best32. ;			
        informat P038G017 best32. ;			
        informat P038G018 best32. ;			
        informat P038G019 best32. ;			
        informat P038G020 best32. ;			
        informat P038H001 best32. ;			
        informat P038H002 best32. ;			
        informat P038H003 best32. ;			
        informat P038H004 best32. ;			
        informat P038H005 best32. ;			
        informat P038H006 best32. ;			
        informat P038H007 best32. ;			
        informat P038H008 best32. ;			
        informat P038H009 best32. ;			
        informat P038H010 best32. ;			
        informat P038H011 best32. ;			
        informat P038H012 best32. ;			
        informat P038H013 best32. ;			
        informat P038H014 best32. ;			
        informat P038H015 best32. ;			
        informat P038H016 best32. ;			
        informat P038H017 best32. ;			
        informat P038H018 best32. ;			
        informat P038H019 best32. ;			
        informat P038H020 best32. ;			
        informat P038I001 best32. ;			
        informat P038I002 best32. ;			
        informat P038I003 best32. ;			
        informat P038I004 best32. ;			
        informat P038I005 best32. ;			
        informat P038I006 best32. ;			
        informat P038I007 best32. ;			
        informat P038I008 best32. ;			
        informat P038I009 best32. ;			
        informat P038I010 best32. ;			
        informat P038I011 best32. ;			
        informat P038I012 best32. ;			
        informat P038I013 best32. ;			
        informat P038I014 best32. ;			
        informat P038I015 best32. ;			
        informat P038I016 best32. ;			
        informat P038I017 best32. ;			
        informat P038I018 best32. ;			
        informat P038I019 best32. ;			
        informat P038I020 best32. ;			
        informat P039A001 best32. ;			
        informat P039A002 best32. ;			
        informat P039A003 best32. ;			
        informat P039A004 best32. ;			
        informat P039A005 best32. ;			
        informat P039A006 best32. ;			
        informat P039A007 best32. ;			
        informat P039A008 best32. ;			
        informat P039A009 best32. ;			
        informat P039A010 best32. ;			
        informat P039A011 best32. ;			
        informat P039A012 best32. ;			
        informat P039A013 best32. ;			
        informat P039A014 best32. ;			
        informat P039A015 best32. ;			
        informat P039A016 best32. ;			
        informat P039A017 best32. ;			
        informat P039A018 best32. ;			
        informat P039A019 best32. ;			
        informat P039A020 best32. ;			
        informat P039B001 best32. ;			
        informat P039B002 best32. ;			
        informat P039B003 best32. ;			
        informat P039B004 best32. ;			
        informat P039B005 best32. ;			
        informat P039B006 best32. ;			
        informat P039B007 best32. ;			
        informat P039B008 best32. ;			
        informat P039B009 best32. ;			
        informat P039B010 best32. ;			
        informat P039B011 best32. ;			
        informat P039B012 best32. ;			
        informat P039B013 best32. ;			
        informat P039B014 best32. ;			
        informat P039B015 best32. ;			
        informat P039B016 best32. ;			
        informat P039B017 best32. ;			
        informat P039B018 best32. ;			
        informat P039B019 best32. ;			
        informat P039B020 best32. ;			
        informat P039C001 best32. ;			
        informat P039C002 best32. ;			
        informat P039C003 best32. ;			
        informat P039C004 best32. ;			
        informat P039C005 best32. ;			
        informat P039C006 best32. ;			
        informat P039C007 best32. ;			
        informat P039C008 best32. ;			
        informat P039C009 best32. ;			
        informat P039C010 best32. ;			
        informat P039C011 best32. ;			
        informat P039C012 best32. ;			
        informat P039C013 best32. ;			
        informat P039C014 best32. ;			
        informat P039C015 best32. ;			
        informat P039C016 best32. ;			
        informat P039C017 best32. ;			
        informat P039C018 best32. ;			
        informat P039C019 best32. ;			
        informat P039C020 best32. ;			
        informat P039D001 best32. ;			
        informat P039D002 best32. ;			
        informat P039D003 best32. ;			
        informat P039D004 best32. ;			
        informat P039D005 best32. ;			
        informat P039D006 best32. ;			
        informat P039D007 best32. ;			
        informat P039D008 best32. ;			
        informat P039D009 best32. ;			
        informat P039D010 best32. ;			
        informat P039D011 best32. ;			
        informat P039D012 best32. ;			
        informat P039D013 best32. ;			
        informat P039D014 best32. ;			
        informat P039D015 best32. ;			
        informat P039D016 best32. ;			
        informat P039D017 best32. ;			
        informat P039D018 best32. ;			
        informat P039D019 best32. ;			
        informat P039D020 best32. ;			
        informat P039E001 best32. ;			
        informat P039E002 best32. ;			
        informat P039E003 best32. ;			
        informat P039E004 best32. ;			
        informat P039E005 best32. ;			
        informat P039E006 best32. ;			
        informat P039E007 best32. ;			
        informat P039E008 best32. ;			
        informat P039E009 best32. ;			
        informat P039E010 best32. ;			
        informat P039E011 best32. ;			
        informat P039E012 best32. ;			
        informat P039E013 best32. ;			
        informat P039E014 best32. ;			
        informat P039E015 best32. ;			
        informat P039E016 best32. ;			
        informat P039E017 best32. ;			
        informat P039E018 best32. ;			
        informat P039E019 best32. ;			
        informat P039E020 best32. ;			
        informat P039F001 best32. ;			
        informat P039F002 best32. ;			
        informat P039F003 best32. ;			
        informat P039F004 best32. ;			
        informat P039F005 best32. ;			
        informat P039F006 best32. ;			
        informat P039F007 best32. ;			
        informat P039F008 best32. ;			
        informat P039F009 best32. ;			
        informat P039F010 best32. ;			
        informat P039F011 best32. ;			
        informat P039F012 best32. ;			
        informat P039F013 best32. ;			
        informat P039F014 best32. ;			
        informat P039F015 best32. ;			
        informat P039F016 best32. ;			
        informat P039F017 best32. ;			
        informat P039F018 best32. ;			
        informat P039F019 best32. ;			
        informat P039F020 best32. ;			
        informat P039G001 best32. ;			
        informat P039G002 best32. ;			
        informat P039G003 best32. ;			
        informat P039G004 best32. ;			
        informat P039G005 best32. ;			
        informat P039G006 best32. ;			
        informat P039G007 best32. ;			
        informat P039G008 best32. ;			
        informat P039G009 best32. ;			
        informat P039G010 best32. ;			
        informat P039G011 best32. ;			
        informat P039G012 best32. ;			
        informat P039G013 best32. ;			
        informat P039G014 best32. ;			
        informat P039G015 best32. ;			
        informat P039G016 best32. ;			
        informat P039G017 best32. ;			
        informat P039G018 best32. ;			
        informat P039G019 best32. ;			
        informat P039G020 best32. ;			
        informat P039H001 best32. ;			
        informat P039H002 best32. ;			
        informat P039H003 best32. ;			
        informat P039H004 best32. ;			
        informat P039H005 best32. ;			
        informat P039H006 best32. ;			
        informat P039H007 best32. ;			
        informat P039H008 best32. ;			
        informat P039H009 best32. ;			
        informat P039H010 best32. ;			
        informat P039H011 best32. ;			
        informat P039H012 best32. ;			
        informat P039H013 best32. ;			
        informat P039H014 best32. ;			
        informat P039H015 best32. ;			
        informat P039H016 best32. ;			
        informat P039H017 best32. ;			
        informat P039H018 best32. ;			
        informat P039H019 best32. ;			
        informat P039H020 best32. ;			
        informat P039I001 best32. ;			
        informat P039I002 best32. ;			
        informat P039I003 best32. ;			
        informat P039I004 best32. ;			
        informat P039I005 best32. ;			
        informat P039I006 best32. ;			
        informat P039I007 best32. ;			
        informat P039I008 best32. ;			
        informat P039I009 best32. ;			
        informat P039I010 best32. ;			
        informat P039I011 best32. ;			
        informat P039I012 best32. ;			
        informat P039I013 best32. ;			
        informat P039I014 best32. ;			
        informat P039I015 best32. ;			
        informat P039I016 best32. ;			
        informat P039I017 best32. ;			
        informat P039I018 best32. ;			
        informat P039I019 best32. ;			
        informat P039I020 best32. ;			
        informat PCT0010001 best32. ;			
        informat PCT0010002 best32. ;			
        informat PCT0010003 best32. ;			
        informat PCT0010004 best32. ;			
        informat PCT0010005 best32. ;			
        informat PCT0010006 best32. ;			
        informat PCT0010007 best32. ;			
        informat PCT0010008 best32. ;			
        informat PCT0010009 best32. ;			
        informat PCT0010010 best32. ;			
        informat PCT0010011 best32. ;			
        informat PCT0010012 best32. ;			
        informat PCT0010013 best32. ;			
        informat PCT0010014 best32. ;			
        informat PCT0010015 best32. ;			
        informat PCT0010016 best32. ;			
        informat PCT0010017 best32. ;			
        informat PCT0010018 best32. ;			
        informat PCT0010019 best32. ;			
        informat PCT0010020 best32. ;			
        informat PCT0010021 best32. ;			
        informat PCT0010022 best32. ;			
        informat PCT0010023 best32. ;			
        informat PCT0010024 best32. ;			
        informat PCT0010025 best32. ;			
        informat PCT0010026 best32. ;			
        informat PCT0010027 best32. ;			
        informat PCT0010028 best32. ;			
        informat PCT0010029 best32. ;			
        informat PCT0010030 best32. ;			
        informat PCT0010031 best32. ;			
        informat PCT0010032 best32. ;			
        informat PCT0010033 best32. ;			
        informat PCT0010034 best32. ;			
        informat PCT0010035 best32. ;			
        informat PCT0010036 best32. ;			
        informat PCT0010037 best32. ;			
        informat PCT0010038 best32. ;			
        informat PCT0010039 best32. ;			
        informat PCT0010040 best32. ;			
        informat PCT0010041 best32. ;			
        informat PCT0010042 best32. ;			
        informat PCT0010043 best32. ;			
        informat PCT0010044 best32. ;			
        informat PCT0010045 best32. ;			
        informat PCT0010046 best32. ;			
        informat PCT0010047 best32. ;			
        informat PCT0010048 best32. ;			
        informat PCT0010049 best32. ;			
        informat PCT0010050 best32. ;			
        informat PCT0010051 best32. ;			
        informat PCT0010052 best32. ;			
        informat PCT0010053 best32. ;			
        informat PCT0010054 best32. ;			
        informat PCT0020001 best32. ;			
        informat PCT0020002 best32. ;			
        informat PCT0020003 best32. ;			
        informat PCT0020004 best32. ;			
        informat PCT0020005 best32. ;			
        informat PCT0020006 best32. ;			
        informat PCT0020007 best32. ;			
        informat PCT0020008 best32. ;			
        informat PCT0020009 best32. ;			
        informat PCT0020010 best32. ;			
        informat PCT0020011 best32. ;			
        informat PCT0020012 best32. ;			
        informat PCT0020013 best32. ;			
        informat PCT0020014 best32. ;			
        informat PCT0020015 best32. ;			
        informat PCT0020016 best32. ;			
        informat PCT0020017 best32. ;			
        informat PCT0020018 best32. ;			
        informat PCT0020019 best32. ;			
        informat PCT0020020 best32. ;			
        informat PCT0020021 best32. ;			
        informat PCT0020022 best32. ;			
        informat PCT0020023 best32. ;			
        informat PCT0020024 best32. ;			
        informat PCT0020025 best32. ;			
        informat PCT0020026 best32. ;			
        informat PCT0020027 best32. ;			
        informat PCT0020028 best32. ;			
        informat PCT0020029 best32. ;			
        informat PCT0020030 best32. ;			
        informat PCT0020031 best32. ;			
        informat PCT0020032 best32. ;			
        informat PCT0020033 best32. ;			
        informat PCT0020034 best32. ;			
        informat PCT0020035 best32. ;			
        informat PCT0020036 best32. ;			
        informat PCT0020037 best32. ;			
        informat PCT0020038 best32. ;			
        informat PCT0020039 best32. ;			
        informat PCT0020040 best32. ;			
        informat PCT0020041 best32. ;			
        informat PCT0020042 best32. ;			
        informat PCT0020043 best32. ;			
        informat PCT0020044 best32. ;			
        informat PCT0020045 best32. ;			
        informat PCT0020046 best32. ;			
        informat PCT0020047 best32. ;			
        informat PCT0020048 best32. ;			
        informat PCT0020049 best32. ;			
        informat PCT0020050 best32. ;			
        informat PCT0020051 best32. ;			
        informat PCT0020052 best32. ;			
        informat PCT0020053 best32. ;			
        informat PCT0020054 best32. ;			
        informat PCT0030001 best32. ;			
        informat PCT0030002 best32. ;			
        informat PCT0030003 best32. ;			
        informat PCT0030004 best32. ;			
        informat PCT0030005 best32. ;			
        informat PCT0030006 best32. ;			
        informat PCT0030007 best32. ;			
        informat PCT0030008 best32. ;			
        informat PCT0030009 best32. ;			
        informat PCT0030010 best32. ;			
        informat PCT0030011 best32. ;			
        informat PCT0030012 best32. ;			
        informat PCT0030013 best32. ;			
        informat PCT0030014 best32. ;			
        informat PCT0030015 best32. ;			
        informat PCT0030016 best32. ;			
        informat PCT0030017 best32. ;			
        informat PCT0030018 best32. ;			
        informat PCT0030019 best32. ;			
        informat PCT0030020 best32. ;			
        informat PCT0030021 best32. ;			
        informat PCT0030022 best32. ;			
        informat PCT0030023 best32. ;			
        informat PCT0030024 best32. ;			
        informat PCT0030025 best32. ;			
        informat PCT0030026 best32. ;			
        informat PCT0030027 best32. ;			
        informat PCT0030028 best32. ;			
        informat PCT0030029 best32. ;			
        informat PCT0030030 best32. ;			
        informat PCT0030031 best32. ;			
        informat PCT0030032 best32. ;			
        informat PCT0030033 best32. ;			
        informat PCT0030034 best32. ;			
        informat PCT0030035 best32. ;			
        informat PCT0030036 best32. ;			
        informat PCT0030037 best32. ;			
        informat PCT0030038 best32. ;			
        informat PCT0030039 best32. ;			
        informat PCT0030040 best32. ;			
        informat PCT0030041 best32. ;			
        informat PCT0030042 best32. ;			
        informat PCT0030043 best32. ;			
        informat PCT0030044 best32. ;			
        informat PCT0030045 best32. ;			
        informat PCT0030046 best32. ;			
        informat PCT0030047 best32. ;			
        informat PCT0030048 best32. ;			
        informat PCT0030049 best32. ;			
        informat PCT0030050 best32. ;			
        informat	  PCT0030051	best32. ;	
        informat	  PCT0030052	best32. ;	
        informat	  PCT0030053	best32. ;	
        informat	  PCT0030054	best32. ;	
        informat	  PCT0040001	best32. ;	
        informat	  PCT0040002	best32. ;	
        informat	  PCT0040003	best32. ;	
        informat	  PCT0040004	best32. ;	
        informat	  PCT0040005	best32. ;	
        informat	  PCT0040006	best32. ;	
        informat	  PCT0040007	best32. ;	
        informat	  PCT0040008	best32. ;	
        informat	  PCT0040009	best32. ;	
        informat	  PCT0050001	best32. ;	
        informat	  PCT0050002	best32. ;	
        informat	  PCT0050003	best32. ;	
        informat	  PCT0050004	best32. ;	
        informat	  PCT0050005	best32. ;	
        informat	  PCT0050006	best32. ;	
        informat	  PCT0050007	best32. ;	
        informat	  PCT0050008	best32. ;	
        informat	  PCT0050009	best32. ;	
        informat	  PCT0050010	best32. ;	
        informat	  PCT0050011	best32. ;	
        informat	  PCT0050012	best32. ;	
        informat	  PCT0050013	best32. ;	
        informat	  PCT0050014	best32. ;	
        informat	  PCT0050015	best32. ;	
        informat	  PCT0050016	best32. ;	
        informat	  PCT0050017	best32. ;	
        informat	  PCT0050018	best32. ;	
        informat	  PCT0050019	best32. ;	
        informat	  PCT0050020	best32. ;	
        informat	  PCT0050021	best32. ;	
        informat	  PCT0050022	best32. ;	
        informat	  PCT0060001	best32. ;	
        informat	  PCT0060002	best32. ;	
        informat	  PCT0060003	best32. ;	
        informat	  PCT0060004	best32. ;	
        informat	  PCT0060005	best32. ;	
        informat	  PCT0060006	best32. ;	
        informat	  PCT0060007	best32. ;	
        informat	  PCT0060008	best32. ;	
        informat	  PCT0060009	best32. ;	
        informat	  PCT0060010	best32. ;	
        informat	  PCT0060011	best32. ;	
        informat	  PCT0060012	best32. ;	
        informat	  PCT0060013	best32. ;	
        informat	  PCT0060014	best32. ;	
        informat	  PCT0060015	best32. ;	
        informat	  PCT0060016	best32. ;	
        informat	  PCT0060017	best32. ;	
        informat	  PCT0060018	best32. ;	
        informat	  PCT0060019	best32. ;	
        informat	  PCT0060020	best32. ;	
        informat	  PCT0060021	best32. ;	
        informat	  PCT0060022	best32. ;	
        informat	  PCT0070001	best32. ;	
        informat	  PCT0070002	best32. ;	
        informat	  PCT0070003	best32. ;	
        informat	  PCT0070004	best32. ;	
        informat	  PCT0070005	best32. ;	
        informat	  PCT0070006	best32. ;	
        informat	  PCT0070007	best32. ;	
        informat	  PCT0070008	best32. ;	
        informat	  PCT0070009	best32. ;	
        informat	  PCT0070010	best32. ;	
        informat	  PCT0070011	best32. ;	
        informat	  PCT0070012	best32. ;	
        informat	  PCT0070013	best32. ;	
        informat	  PCT0070014	best32. ;	
        informat	  PCT0070015	best32. ;	
        informat	  PCT0070016	best32. ;	
        informat	  PCT0070017	best32. ;	
        informat	  PCT0070018	best32. ;	
        informat	  PCT0070019	best32. ;	
        informat	  PCT0070020	best32. ;	
        informat	  PCT0070021	best32. ;	
        informat	  PCT0070022	best32. ;	
        informat	  PCT0080001	best32. ;	
        informat	  PCT0080002	best32. ;	
        informat	  PCT0080003	best32. ;	
        informat	  PCT0080004	best32. ;	
        informat	  PCT0080005	best32. ;	
        informat	  PCT0080006	best32. ;	
        informat	  PCT0080007	best32. ;	
        informat	  PCT0080008	best32. ;	
        informat	  PCT0080009	best32. ;	
        informat	  PCT0080010	best32. ;	
        informat	  PCT0080011	best32. ;	
        informat	  PCT0080012	best32. ;	
        informat	  PCT0080013	best32. ;	
        informat	  PCT0080014	best32. ;	
        informat	  PCT0090001	best32. ;	
        informat	  PCT0090002	best32. ;	
        informat	  PCT0090003	best32. ;	
        informat	  PCT0090004	best32. ;	
        informat	  PCT0090005	best32. ;	
        informat	  PCT0090006	best32. ;	
        informat	  PCT0090007	best32. ;	
        informat	  PCT0090008	best32. ;	
        informat	  PCT0090009	best32. ;	
        informat	  PCT0090010	best32. ;	
        informat	  PCT0090011	best32. ;	
        informat	  PCT0090012	best32. ;	
        informat	  PCT0090013	best32. ;	
        informat	  PCT0090014	best32. ;	
        informat	  PCT0100001	best32. ;	
        informat	  PCT0100002	best32. ;	
        informat	  PCT0100003	best32. ;	
        informat	  PCT0100004	best32. ;	
        informat	  PCT0100005	best32. ;	
        informat	  PCT0100006	best32. ;	
        informat	  PCT0100007	best32. ;	
        informat	  PCT0100008	best32. ;	
        informat	  PCT0100009	best32. ;	
        informat	  PCT0100010	best32. ;	
        informat	  PCT0100011	best32. ;	
        informat	  PCT0100012	best32. ;	
        informat	  PCT0100013	best32. ;	
        informat	  PCT0100014	best32. ;	
        informat	  PCT0110001	best32. ;	
        informat	  PCT0110002	best32. ;	
        informat	  PCT0110003	best32. ;	
        informat	  PCT0110004	best32. ;	
        informat	  PCT0110005	best32. ;	
        informat	  PCT0110006	best32. ;	
        informat	  PCT0110007	best32. ;	
        informat	  PCT0110008	best32. ;	
        informat	  PCT0110009	best32. ;	
        informat	  PCT0110010	best32. ;	
        informat	  PCT0110011	best32. ;	
        informat	  PCT0110012	best32. ;	
        informat	  PCT0110013	best32. ;	
        informat	  PCT0110014	best32. ;	
        informat	  PCT0110015	best32. ;	
        informat	  PCT0110016	best32. ;	
        informat	  PCT0110017	best32. ;	
        informat	  PCT0110018	best32. ;	
        informat	  PCT0110019	best32. ;	
        informat	  PCT0110020	best32. ;	
        informat	  PCT0110021	best32. ;	
        informat	  PCT0110022	best32. ;	
        informat	  PCT0110023	best32. ;	
        informat	  PCT0110024	best32. ;	
        informat	  PCT0110025	best32. ;	
        informat	  PCT0110026	best32. ;	
        informat	  PCT0110027	best32. ;	
        informat	  PCT0110028	best32. ;	
        informat	  PCT0110029	best32. ;	
        informat	  PCT0110030	best32. ;	
        informat	  PCT0110031	best32. ;	
        informat	  PCT0120001	best32. ;	
        informat	  PCT0120002	best32. ;	
        informat	  PCT0120003	best32. ;	
        informat	  PCT0120004	best32. ;	
        informat	  PCT0120005	best32. ;	
        informat	  PCT0120006	best32. ;	
        informat	  PCT0120007	best32. ;	
        informat	  PCT0120008	best32. ;	
        informat	  PCT0120009	best32. ;	
        informat	  PCT0120010	best32. ;	
        informat	  PCT0120011	best32. ;	
        informat	  PCT0120012	best32. ;	
        informat	  PCT0120013	best32. ;	
        informat	  PCT0120014	best32. ;	
        informat	  PCT0120015	best32. ;	
        informat	  PCT0120016	best32. ;	
        informat	  PCT0120017	best32. ;	
        informat	  PCT0120018	best32. ;	
        informat	  PCT0120019	best32. ;	
        informat	  PCT0120020	best32. ;	
        informat	  PCT0120021	best32. ;	
        informat	  PCT0120022	best32. ;	
        informat	  PCT0120023	best32. ;	
        informat	  PCT0120024	best32. ;	
        informat	  PCT0120025	best32. ;	
        informat	  PCT0120026	best32. ;	
        informat	  PCT0120027	best32. ;	
        informat	  PCT0120028	best32. ;	
        informat	  PCT0120029	best32. ;	
        informat	  PCT0120030	best32. ;	
        informat	  PCT0120031	best32. ;	
        informat	  PCT0120032	best32. ;	
        informat	  PCT0120033	best32. ;	
        informat	  PCT0120034	best32. ;	
        informat	  PCT0120035	best32. ;	
        informat	  PCT0120036	best32. ;	
        informat	  PCT0120037	best32. ;	
        informat	  PCT0120038	best32. ;	
        informat	  PCT0120039	best32. ;	
        informat	  PCT0120040	best32. ;	
        informat	  PCT0120041	best32. ;	
        informat	  PCT0120042	best32. ;	
        informat	  PCT0120043	best32. ;	
        informat	  PCT0120044	best32. ;	
        informat	  PCT0120045	best32. ;	
        informat	  PCT0120046	best32. ;	
        informat	  PCT0120047	best32. ;	
        informat	  PCT0120048	best32. ;	
        informat	  PCT0120049	best32. ;	
        informat	  PCT0120050	best32. ;	
        informat	  PCT0120051	best32. ;	
        informat	  PCT0120052	best32. ;	
        informat	  PCT0120053	best32. ;	
        informat	  PCT0120054	best32. ;	
        informat	  PCT0120055	best32. ;	
        informat	  PCT0120056	best32. ;	
        informat	  PCT0120057	best32. ;	
        informat	  PCT0120058	best32. ;	
        informat	  PCT0120059	best32. ;	
        informat	  PCT0120060	best32. ;	
        informat	  PCT0120061	best32. ;	
        informat	  PCT0120062	best32. ;	
        informat	  PCT0120063	best32. ;	
        informat	  PCT0120064	best32. ;	
        informat	  PCT0120065	best32. ;	
        informat	  PCT0120066	best32. ;	
        informat	  PCT0120067	best32. ;	
        informat	  PCT0120068	best32. ;	
        informat	  PCT0120069	best32. ;	
        informat	  PCT0120070	best32. ;	
        informat	  PCT0120071	best32. ;	
        informat	  PCT0120072	best32. ;	
        informat	  PCT0120073	best32. ;	
        informat	  PCT0120074	best32. ;	
        informat	  PCT0120075	best32. ;	
        informat	  PCT0120076	best32. ;	
        informat	  PCT0120077	best32. ;	
        informat	  PCT0120078	best32. ;	
        informat	  PCT0120079	best32. ;	
        informat	  PCT0120080	best32. ;	
        informat	  PCT0120081	best32. ;	
        informat	  PCT0120082	best32. ;	
        informat	  PCT0120083	best32. ;	
        informat	  PCT0120084	best32. ;	
        informat	  PCT0120085	best32. ;	
        informat	  PCT0120086	best32. ;	
        informat	  PCT0120087	best32. ;	
        informat	  PCT0120088	best32. ;	
        informat	  PCT0120089	best32. ;	
        informat	  PCT0120090	best32. ;	
        informat	  PCT0120091	best32. ;	
        informat	  PCT0120092	best32. ;	
        informat	  PCT0120093	best32. ;	
        informat	  PCT0120094	best32. ;	
        informat	  PCT0120095	best32. ;	
        informat	  PCT0120096	best32. ;	
        informat	  PCT0120097	best32. ;	
        informat	  PCT0120098	best32. ;	
        informat	  PCT0120099	best32. ;	
        informat	  PCT0120100	best32. ;	
        informat	  PCT0120101	best32. ;	
        informat	  PCT0120102	best32. ;	
        informat	  PCT0120103	best32. ;	
        informat	  PCT0120104	best32. ;	
        informat	  PCT0120105	best32. ;	
        informat	  PCT0120106	best32. ;	
        informat	  PCT0120107	best32. ;	
        informat	  PCT0120108	best32. ;	
        informat	  PCT0120109	best32. ;	
        informat	  PCT0120110	best32. ;	
        informat	  PCT0120111	best32. ;	
        informat	  PCT0120112	best32. ;	
        informat	  PCT0120113	best32. ;	
        informat	  PCT0120114	best32. ;	
        informat	  PCT0120115	best32. ;	
        informat	  PCT0120116	best32. ;	
        informat	  PCT0120117	best32. ;	
        informat	  PCT0120118	best32. ;	
        informat	  PCT0120119	best32. ;	
        informat	  PCT0120120	best32. ;	
        informat	  PCT0120121	best32. ;	
        informat	  PCT0120122	best32. ;	
        informat	  PCT0120123	best32. ;	
        informat	  PCT0120124	best32. ;	
        informat	  PCT0120125	best32. ;	
        informat	  PCT0120126	best32. ;	
        informat	  PCT0120127	best32. ;	
        informat	  PCT0120128	best32. ;	
        informat	  PCT0120129	best32. ;	
        informat	  PCT0120130	best32. ;	
        informat	  PCT0120131	best32. ;	
        informat	  PCT0120132	best32. ;	
        informat	  PCT0120133	best32. ;	
        informat	  PCT0120134	best32. ;	
        informat	  PCT0120135	best32. ;	
        informat	  PCT0120136	best32. ;	
        informat	  PCT0120137	best32. ;	
        informat	  PCT0120138	best32. ;	
        informat	  PCT0120139	best32. ;	
        informat	  PCT0120140	best32. ;	
        informat	  PCT0120141	best32. ;	
        informat	  PCT0120142	best32. ;	
        informat	  PCT0120143	best32. ;	
        informat	  PCT0120144	best32. ;	
        informat	  PCT0120145	best32. ;	
        informat	  PCT0120146	best32. ;	
        informat	  PCT0120147	best32. ;	
        informat	  PCT0120148	best32. ;	
        informat	  PCT0120149	best32. ;	
        informat	  PCT0120150	best32. ;	
        informat	  PCT0120151	best32. ;	
        informat	  PCT0120152	best32. ;	
        informat	  PCT0120153	best32. ;	
        informat	  PCT0120154	best32. ;	
        informat	  PCT0120155	best32. ;	
        informat	  PCT0120156	best32. ;	
        informat	  PCT0120157	best32. ;	
        informat	  PCT0120158	best32. ;	
        informat	  PCT0120159	best32. ;	
        informat	  PCT0120160	best32. ;	
        informat	  PCT0120161	best32. ;	
        informat	  PCT0120162	best32. ;	
        informat	  PCT0120163	best32. ;	
        informat	  PCT0120164	best32. ;	
        informat	  PCT0120165	best32. ;	
        informat	  PCT0120166	best32. ;	
        informat	  PCT0120167	best32. ;	
        informat	  PCT0120168	best32. ;	
        informat	  PCT0120169	best32. ;	
        informat	  PCT0120170	best32. ;	
        informat	  PCT0120171	best32. ;	
        informat	  PCT0120172	best32. ;	
        informat	  PCT0120173	best32. ;	
        informat	  PCT0120174	best32. ;	
        informat	  PCT0120175	best32. ;	
        informat	  PCT0120176	best32. ;	
        informat	  PCT0120177	best32. ;	
        informat	  PCT0120178	best32. ;	
        informat	  PCT0120179	best32. ;	
        informat	  PCT0120180	best32. ;	
        informat	  PCT0120181	best32. ;	
        informat	  PCT0120182	best32. ;	
        informat	  PCT0120183	best32. ;	
        informat	  PCT0120184	best32. ;	
        informat	  PCT0120185	best32. ;	
        informat	  PCT0120186	best32. ;	
        informat	  PCT0120187	best32. ;	
        informat	  PCT0120188	best32. ;	
        informat	  PCT0120189	best32. ;	
        informat	  PCT0120190	best32. ;	
        informat	  PCT0120191	best32. ;	
        informat	  PCT0120192	best32. ;	
        informat	  PCT0120193	best32. ;	
        informat	  PCT0120194	best32. ;	
        informat	  PCT0120195	best32. ;	
        informat	  PCT0120196	best32. ;	
        informat	  PCT0120197	best32. ;	
        informat	  PCT0120198	best32. ;	
        informat	  PCT0120199	best32. ;	
        informat	  PCT0120200	best32. ;	
        informat	  PCT0120201	best32. ;	
        informat	  PCT0120202	best32. ;	
        informat	  PCT0120203	best32. ;	
        informat	  PCT0120204	best32. ;	
        informat	  PCT0120205	best32. ;	
        informat	  PCT0120206	best32. ;	
        informat	  PCT0120207	best32. ;	
        informat	  PCT0120208	best32. ;	
        informat	  PCT0120209	best32. ;	
        informat	  PCT0130001	best32. ;	
        informat	  PCT0130002	best32. ;	
        informat	  PCT0130003	best32. ;	
        informat	  PCT0130004	best32. ;	
        informat	  PCT0130005	best32. ;	
        informat	  PCT0130006	best32. ;	
        informat	  PCT0130007	best32. ;	
        informat	  PCT0130008	best32. ;	
        informat	  PCT0130009	best32. ;	
        informat	  PCT0130010	best32. ;	
        informat	  PCT0130011	best32. ;	
        informat	  PCT0130012	best32. ;	
        informat	  PCT0130013	best32. ;	
        informat	  PCT0130014	best32. ;	
        informat	  PCT0130015	best32. ;	
        informat	  PCT0130016	best32. ;	
        informat	  PCT0130017	best32. ;	
        informat	  PCT0130018	best32. ;	
        informat	  PCT0130019	best32. ;	
        informat	  PCT0130020	best32. ;	
        informat	  PCT0130021	best32. ;	
        informat	  PCT0130022	best32. ;	
        informat	  PCT0130023	best32. ;	
        informat	  PCT0130024	best32. ;	
        informat	  PCT0130025	best32. ;	
        informat	  PCT0130026	best32. ;	
        informat	  PCT0130027	best32. ;	
        informat	  PCT0130028	best32. ;	
        informat	  PCT0130029	best32. ;	
        informat	  PCT0130030	best32. ;	
        informat	  PCT0130031	best32. ;	
        informat	  PCT0130032	best32. ;	
        informat	  PCT0130033	best32. ;	
        informat	  PCT0130034	best32. ;	
        informat	  PCT0130035	best32. ;	
        informat	  PCT0130036	best32. ;	
        informat	  PCT0130037	best32. ;	
        informat	  PCT0130038	best32. ;	
        informat	  PCT0130039	best32. ;	
        informat	  PCT0130040	best32. ;	
        informat	  PCT0130041	best32. ;	
        informat	  PCT0130042	best32. ;	
        informat	  PCT0130043	best32. ;	
        informat	  PCT0130044	best32. ;	
        informat	  PCT0130045	best32. ;	
        informat	  PCT0130046	best32. ;	
        informat	  PCT0130047	best32. ;	
        informat	  PCT0130048	best32. ;	
        informat	  PCT0130049	best32. ;	
        informat	  PCT0140001	best32. ;	
        informat	  PCT0140002	best32. ;	
        informat	  PCT0140003	best32. ;	
        informat	  PCT0150001	best32. ;	
        informat	  PCT0150002	best32. ;	
        informat	  PCT0150003	best32. ;	
        informat	  PCT0150004	best32. ;	
        informat	  PCT0150005	best32. ;	
        informat	  PCT0150006	best32. ;	
        informat	  PCT0150007	best32. ;	
        informat	  PCT0150008	best32. ;	
        informat	  PCT0150009	best32. ;	
        informat	  PCT0150010	best32. ;	
        informat	  PCT0150011	best32. ;	
        informat	  PCT0150012	best32. ;	
        informat	  PCT0150013	best32. ;	
        informat	  PCT0150014	best32. ;	
        informat	  PCT0150015	best32. ;	
        informat	  PCT0150016	best32. ;	
        informat	  PCT0150017	best32. ;	
        informat	  PCT0150018	best32. ;	
        informat	  PCT0150019	best32. ;	
        informat	  PCT0150020	best32. ;	
        informat	  PCT0150021	best32. ;	
        informat	  PCT0150022	best32. ;	
        informat	  PCT0150023	best32. ;	
        informat	  PCT0150024	best32. ;	
        informat	  PCT0150025	best32. ;	
        informat	  PCT0150026	best32. ;	
        informat	  PCT0150027	best32. ;	
        informat	  PCT0150028	best32. ;	
        informat	  PCT0150029	best32. ;	
        informat	  PCT0150030	best32. ;	
        informat	  PCT0150031	best32. ;	
        informat	  PCT0150032	best32. ;	
        informat	  PCT0150033	best32. ;	
        informat	  PCT0150034	best32. ;	
        informat	  PCT0160001	best32. ;	
        informat	  PCT0160002	best32. ;	
        informat	  PCT0160003	best32. ;	
        informat	  PCT0160004	best32. ;	
        informat	  PCT0160005	best32. ;	
        informat	  PCT0160006	best32. ;	
        informat	  PCT0160007	best32. ;	
        informat	  PCT0160008	best32. ;	
        informat	  PCT0160009	best32. ;	
        informat	  PCT0160010	best32. ;	
        informat	  PCT0160011	best32. ;	
        informat	  PCT0160012	best32. ;	
        informat	  PCT0160013	best32. ;	
        informat	  PCT0160014	best32. ;	
        informat	  PCT0160015	best32. ;	
        informat	  PCT0160016	best32. ;	
        informat	  PCT0160017	best32. ;	
        informat	  PCT0160018	best32. ;	
        informat	  PCT0160019	best32. ;	
        informat	  PCT0160020	best32. ;	
        informat	  PCT0160021	best32. ;	
        informat	  PCT0160022	best32. ;	
        informat	  PCT0160023	best32. ;	
        informat	  PCT0160024	best32. ;	
        informat	  PCT0160025	best32. ;	
        informat	  PCT0160026	best32. ;	
        informat	  PCT0170001	best32. ;	
        informat	  PCT0170002	best32. ;	
        informat	  PCT0170003	best32. ;	
        informat	  PCT0170004	best32. ;	
        informat	  PCT0170005	best32. ;	
        informat	  PCT0170006	best32. ;	
        informat	  PCT0170007	best32. ;	
        informat	  PCT0170008	best32. ;	
        informat	  PCT0170009	best32. ;	
        informat	  PCT0170010	best32. ;	
        informat	  PCT0170011	best32. ;	
        informat	  PCT0170012	best32. ;	
        informat	  PCT0170013	best32. ;	
        informat	  PCT0170014	best32. ;	
        informat	  PCT0170015	best32. ;	
        informat	  PCT0170016	best32. ;	
        informat	  PCT0170017	best32. ;	
        informat	  PCT0170018	best32. ;	
        informat	  PCT0180001	best32. ;	
        informat	  PCT0180002	best32. ;	
        informat	  PCT0180003	best32. ;	
        informat	  PCT0180004	best32. ;	
        informat	  PCT0180005	best32. ;	
        informat	  PCT0180006	best32. ;	
        informat	  PCT0180007	best32. ;	
        informat	  PCT0180008	best32. ;	
        informat	  PCT0180009	best32. ;	
        informat	  PCT0180010	best32. ;	
        informat	  PCT0180011	best32. ;	
        informat	  PCT0180012	best32. ;	
        informat	  PCT0180013	best32. ;	
        informat	  PCT0180014	best32. ;	
        informat	  PCT0180015	best32. ;	
        informat	  PCT0190001	best32. ;	
        informat	  PCT0190002	best32. ;	
        informat	  PCT0190003	best32. ;	
        informat	  PCT0190004	best32. ;	
        informat	  PCT0190005	best32. ;	
        informat	  PCT0190006	best32. ;	
        informat	  PCT0190007	best32. ;	
        informat	  PCT0190008	best32. ;	
        informat	  PCT0190009	best32. ;	
        informat	  PCT0190010	best32. ;	
        informat	  PCT0190011	best32. ;	
        informat	  PCT0200001	best32. ;	
        informat	  PCT0200002	best32. ;	
        informat	  PCT0200003	best32. ;	
        informat	  PCT0200004	best32. ;	
        informat	  PCT0200005	best32. ;	
        informat	  PCT0200006	best32. ;	
        informat	  PCT0200007	best32. ;	
        informat	  PCT0200008	best32. ;	
        informat	  PCT0200009	best32. ;	
        informat	  PCT0200010	best32. ;	
        informat	  PCT0200011	best32. ;	
        informat	  PCT0200012	best32. ;	
        informat	  PCT0200013	best32. ;	
        informat	  PCT0200014	best32. ;	
        informat	  PCT0200015	best32. ;	
        informat	  PCT0200016	best32. ;	
        informat	  PCT0200017	best32. ;	
        informat	  PCT0200018	best32. ;	
        informat	  PCT0200019	best32. ;	
        informat	  PCT0200020	best32. ;	
        informat	  PCT0200021	best32. ;	
        informat	  PCT0200022	best32. ;	
        informat	  PCT0200023	best32. ;	
        informat	  PCT0200024	best32. ;	
        informat	  PCT0200025	best32. ;	
        informat	  PCT0200026	best32. ;	
        informat	  PCT0200027	best32. ;	
        informat	  PCT0200028	best32. ;	
        informat	  PCT0200029	best32. ;	
        informat	  PCT0200030	best32. ;	
        informat	  PCT0200031	best32. ;	
        informat	  PCT0200032	best32. ;	
        informat	  PCT0210001	best32. ;	
        informat	  PCT0210002	best32. ;	
        informat	  PCT0210003	best32. ;	
        informat	  PCT0210004	best32. ;	
        informat	  PCT0210005	best32. ;	
        informat	  PCT0210006	best32. ;	
        informat	  PCT0210007	best32. ;	
        informat	  PCT0210008	best32. ;	
        informat	  PCT0210009	best32. ;	
        informat	  PCT0210010	best32. ;	
        informat	  PCT0210011	best32. ;	
        informat	  PCT0210012	best32. ;	
        informat	  PCT0210013	best32. ;	
        informat	  PCT0210014	best32. ;	
        informat	  PCT0210015	best32. ;	
        informat	  PCT0210016	best32. ;	
        informat	  PCT0210017	best32. ;	
        informat	  PCT0210018	best32. ;	
        informat	  PCT0210019	best32. ;	
        informat	  PCT0210020	best32. ;	
        informat	  PCT0210021	best32. ;	
        informat	  PCT0210022	best32. ;	
        informat	  PCT0210023	best32. ;	
        informat	  PCT0210024	best32. ;	
        informat	  PCT0210025	best32. ;	
        informat	  PCT0210026	best32. ;	
        informat	  PCT0210027	best32. ;	
        informat	  PCT0210028	best32. ;	
        informat	  PCT0210029	best32. ;	
        informat	  PCT0210030	best32. ;	
        informat	  PCT0210031	best32. ;	
        informat	  PCT0210032	best32. ;	
        informat	  PCT0210033	best32. ;	
        informat	  PCT0210034	best32. ;	
        informat	  PCT0210035	best32. ;	
        informat	  PCT0210036	best32. ;	
        informat	  PCT0210037	best32. ;	
        informat	  PCT0210038	best32. ;	
        informat	  PCT0210039	best32. ;	
        informat	  PCT0210040	best32. ;	
        informat	  PCT0210041	best32. ;	
        informat	  PCT0210042	best32. ;	
        informat	  PCT0210043	best32. ;	
        informat	  PCT0210044	best32. ;	
        informat	  PCT0210045	best32. ;	
        informat	  PCT0210046	best32. ;	
        informat	  PCT0210047	best32. ;	
        informat	  PCT0210048	best32. ;	
        informat	  PCT0210049	best32. ;	
        informat	  PCT0210050	best32. ;	
        informat	  PCT0210051	best32. ;	
        informat	  PCT0210052	best32. ;	
        informat	  PCT0210053	best32. ;	
        informat	  PCT0210054	best32. ;	
        informat	  PCT0210055	best32. ;	
        informat	  PCT0210056	best32. ;	
        informat	  PCT0210057	best32. ;	
        informat	  PCT0210058	best32. ;	
        informat	  PCT0210059	best32. ;	
        informat	  PCT0210060	best32. ;	
        informat	  PCT0210061	best32. ;	
        informat	  PCT0210062	best32. ;	
        informat	  PCT0210063	best32. ;	
        informat	  PCT0210064	best32. ;	
        informat	  PCT0210065	best32. ;	
        informat	  PCT0210066	best32. ;	
        informat	  PCT0210067	best32. ;	
        informat	  PCT0210068	best32. ;	
        informat	  PCT0210069	best32. ;	
        informat	  PCT0210070	best32. ;	
        informat	  PCT0210071	best32. ;	
        informat	  PCT0210072	best32. ;	
        informat	  PCT0210073	best32. ;	
        informat	  PCT0210074	best32. ;	
        informat	  PCT0210075	best32. ;	
        informat	  PCT0210076	best32. ;	
        informat	  PCT0210077	best32. ;	
        informat	  PCT0210078	best32. ;	
        informat	  PCT0210079	best32. ;	
        informat	  PCT0210080	best32. ;	
        informat	  PCT0210081	best32. ;	
        informat	  PCT0210082	best32. ;	
        informat	  PCT0210083	best32. ;	
        informat	  PCT0210084	best32. ;	
        informat	  PCT0210085	best32. ;	
        informat	  PCT0210086	best32. ;	
        informat	  PCT0210087	best32. ;	
        informat	  PCT0210088	best32. ;	
        informat	  PCT0210089	best32. ;	
        informat	  PCT0210090	best32. ;	
        informat	  PCT0210091	best32. ;	
        informat	  PCT0210092	best32. ;	
        informat	  PCT0210093	best32. ;	
        informat	  PCT0210094	best32. ;	
        informat	  PCT0210095	best32. ;	
        informat	  PCT0210096	best32. ;	
        informat	  PCT0210097	best32. ;	
        informat	  PCT0210098	best32. ;	
        informat	  PCT0210099	best32. ;	
        informat	  PCT0210100	best32. ;	
        informat	  PCT0210101	best32. ;	
        informat	  PCT0210102	best32. ;	
        informat	  PCT0210103	best32. ;	
        informat	  PCT0210104	best32. ;	
        informat	  PCT0210105	best32. ;	
        informat	  PCT0210106	best32. ;	
        informat	  PCT0210107	best32. ;	
        informat	  PCT0210108	best32. ;	
        informat	  PCT0210109	best32. ;	
        informat	  PCT0210110	best32. ;	
        informat	  PCT0210111	best32. ;	
        informat	  PCT0210112	best32. ;	
        informat	  PCT0210113	best32. ;	
        informat	  PCT0210114	best32. ;	
        informat	  PCT0210115	best32. ;	
        informat	  PCT0210116	best32. ;	
        informat	  PCT0210117	best32. ;	
        informat	  PCT0210118	best32. ;	
        informat	  PCT0210119	best32. ;	
        informat	  PCT0210120	best32. ;	
        informat	  PCT0210121	best32. ;	
        informat	  PCT0210122	best32. ;	
        informat	  PCT0210123	best32. ;	
        informat	  PCT0210124	best32. ;	
        informat	  PCT0210125	best32. ;	
        informat	  PCT0210126	best32. ;	
        informat	  PCT0210127	best32. ;	
        informat	  PCT0210128	best32. ;	
        informat	  PCT0210129	best32. ;	
        informat	  PCT0210130	best32. ;	
        informat	  PCT0210131	best32. ;	
        informat	  PCT0210132	best32. ;	
        informat	  PCT0210133	best32. ;	
        informat	  PCT0210134	best32. ;	
        informat	  PCT0210135	best32. ;	
        informat	  PCT0210136	best32. ;	
        informat	  PCT0210137	best32. ;	
        informat	  PCT0210138	best32. ;	
        informat	  PCT0210139	best32. ;	
        informat	  PCT0210140	best32. ;	
        informat	  PCT0210141	best32. ;	
        informat	  PCT0210142	best32. ;	
        informat	  PCT0210143	best32. ;	
        informat	  PCT0210144	best32. ;	
        informat	  PCT0210145	best32. ;	
        informat	  PCT0210146	best32. ;	
        informat	  PCT0210147	best32. ;	
        informat	  PCT0210148	best32. ;	
        informat	  PCT0210149	best32. ;	
        informat	  PCT0210150	best32. ;	
        informat	  PCT0210151	best32. ;	
        informat	  PCT0210152	best32. ;	
        informat	  PCT0210153	best32. ;	
        informat	  PCT0210154	best32. ;	
        informat	  PCT0210155	best32. ;	
        informat	  PCT0210156	best32. ;	
        informat	  PCT0210157	best32. ;	
        informat	  PCT0210158	best32. ;	
        informat	  PCT0210159	best32. ;	
        informat	  PCT0210160	best32. ;	
        informat	  PCT0210161	best32. ;	
        informat	  PCT0210162	best32. ;	
        informat	  PCT0210163	best32. ;	
        informat	  PCT0210164	best32. ;	
        informat	  PCT0210165	best32. ;	
        informat	  PCT0210166	best32. ;	
        informat	  PCT0210167	best32. ;	
        informat	  PCT0210168	best32. ;	
        informat	  PCT0210169	best32. ;	
        informat	  PCT0210170	best32. ;	
        informat	  PCT0210171	best32. ;	
        informat	  PCT0210172	best32. ;	
        informat	  PCT0210173	best32. ;	
        informat	  PCT0210174	best32. ;	
        informat	  PCT0210175	best32. ;	
        informat	  PCT0210176	best32. ;	
        informat	  PCT0210177	best32. ;	
        informat	  PCT0210178	best32. ;	
        informat	  PCT0210179	best32. ;	
        informat	  PCT0210180	best32. ;	
        informat	  PCT0210181	best32. ;	
        informat	  PCT0210182	best32. ;	
        informat	  PCT0210183	best32. ;	
        informat	  PCT0210184	best32. ;	
        informat	  PCT0210185	best32. ;	
        informat	  PCT0210186	best32. ;	
        informat	  PCT0210187	best32. ;	
        informat	  PCT0210188	best32. ;	
        informat	  PCT0210189	best32. ;	
        informat	  PCT0210190	best32. ;	
        informat	  PCT0210191	best32. ;	
        informat	  PCT0210192	best32. ;	
        informat	  PCT0210193	best32. ;	
        informat	  PCT0210194	best32. ;	
        informat	  PCT0210195	best32. ;	
        informat	  PCT0220001	best32. ;	
        informat	  PCT0220002	best32. ;	
        informat	  PCT0220003	best32. ;	
        informat	  PCT0220004	best32. ;	
        informat	  PCT0220005	best32. ;	
        informat	  PCT0220006	best32. ;	
        informat	  PCT0220007	best32. ;	
        informat	  PCT0220008	best32. ;	
        informat	  PCT0220009	best32. ;	
        informat	  PCT0220010	best32. ;	
        informat	  PCT0220011	best32. ;	
        informat	  PCT0220012	best32. ;	
        informat	  PCT0220013	best32. ;	
        informat	  PCT0220014	best32. ;	
        informat	  PCT0220015	best32. ;	
        informat	  PCT0220016	best32. ;	
        informat	  PCT0220017	best32. ;	
        informat	  PCT0220018	best32. ;	
        informat	  PCT0220019	best32. ;	
        informat	  PCT0220020	best32. ;	
        informat	  PCT0220021	best32. ;	
        informat	  PCT012A001	best32. ;	
        informat	  PCT012A002	best32. ;	
        informat	  PCT012A003	best32. ;	
        informat	  PCT012A004	best32. ;	
        informat	  PCT012A005	best32. ;	
        informat	  PCT012A006	best32. ;	
        informat	  PCT012A007	best32. ;	
        informat	  PCT012A008	best32. ;	
        informat	  PCT012A009	best32. ;	
        informat	  PCT012A010	best32. ;	
        informat	  PCT012A011	best32. ;	
        informat	  PCT012A012	best32. ;	
        informat	  PCT012A013	best32. ;	
        informat	  PCT012A014	best32. ;	
        informat	  PCT012A015	best32. ;	
        informat	  PCT012A016	best32. ;	
        informat	  PCT012A017	best32. ;	
        informat	  PCT012A018	best32. ;	
        informat	  PCT012A019	best32. ;	
        informat	  PCT012A020	best32. ;	
        informat	  PCT012A021	best32. ;	
        informat	  PCT012A022	best32. ;	
        informat	  PCT012A023	best32. ;	
        informat	  PCT012A024	best32. ;	
        informat	  PCT012A025	best32. ;	
        informat	  PCT012A026	best32. ;	
        informat	  PCT012A027	best32. ;	
        informat	  PCT012A028	best32. ;	
        informat	  PCT012A029	best32. ;	
        informat	  PCT012A030	best32. ;	
        informat	  PCT012A031	best32. ;	
        informat	  PCT012A032	best32. ;	
        informat	  PCT012A033	best32. ;	
        informat	  PCT012A034	best32. ;	
        informat	  PCT012A035	best32. ;	
        informat	  PCT012A036	best32. ;	
        informat	  PCT012A037	best32. ;	
        informat	  PCT012A038	best32. ;	
        informat	  PCT012A039	best32. ;	
        informat	  PCT012A040	best32. ;	
        informat	  PCT012A041	best32. ;	
        informat	  PCT012A042	best32. ;	
        informat	  PCT012A043	best32. ;	
        informat	  PCT012A044	best32. ;	
        informat	  PCT012A045	best32. ;	
        informat	  PCT012A046	best32. ;	
        informat	  PCT012A047	best32. ;	
        informat	  PCT012A048	best32. ;	
        informat	  PCT012A049	best32. ;	
        informat	  PCT012A050	best32. ;	
        informat	  PCT012A051	best32. ;	
        informat	  PCT012A052	best32. ;	
        informat	  PCT012A053	best32. ;	
        informat	  PCT012A054	best32. ;	
        informat	  PCT012A055	best32. ;	
        informat	  PCT012A056	best32. ;	
        informat	  PCT012A057	best32. ;	
        informat	  PCT012A058	best32. ;	
        informat	  PCT012A059	best32. ;	
        informat	  PCT012A060	best32. ;	
        informat	  PCT012A061	best32. ;	
        informat	  PCT012A062	best32. ;	
        informat	  PCT012A063	best32. ;	
        informat	  PCT012A064	best32. ;	
        informat	  PCT012A065	best32. ;	
        informat	  PCT012A066	best32. ;	
        informat	  PCT012A067	best32. ;	
        informat	  PCT012A068	best32. ;	
        informat	  PCT012A069	best32. ;	
        informat	  PCT012A070	best32. ;	
        informat	  PCT012A071	best32. ;	
        informat	  PCT012A072	best32. ;	
        informat	  PCT012A073	best32. ;	
        informat	  PCT012A074	best32. ;	
        informat	  PCT012A075	best32. ;	
        informat	  PCT012A076	best32. ;	
        informat	  PCT012A077	best32. ;	
        informat	  PCT012A078	best32. ;	
        informat	  PCT012A079	best32. ;	
        informat	  PCT012A080	best32. ;	
        informat	  PCT012A081	best32. ;	
        informat	  PCT012A082	best32. ;	
        informat	  PCT012A083	best32. ;	
        informat	  PCT012A084	best32. ;	
        informat	  PCT012A085	best32. ;	
        informat	  PCT012A086	best32. ;	
        informat	  PCT012A087	best32. ;	
        informat	  PCT012A088	best32. ;	
        informat	  PCT012A089	best32. ;	
        informat	  PCT012A090	best32. ;	
        informat	  PCT012A091	best32. ;	
        informat	  PCT012A092	best32. ;	
        informat	  PCT012A093	best32. ;	
        informat	  PCT012A094	best32. ;	
        informat	  PCT012A095	best32. ;	
        informat	  PCT012A096	best32. ;	
        informat	  PCT012A097	best32. ;	
        informat	  PCT012A098	best32. ;	
        informat	  PCT012A099	best32. ;	
        informat	  PCT012A100	best32. ;	
        informat	  PCT012A101	best32. ;	
        informat	  PCT012A102	best32. ;	
        informat	  PCT012A103	best32. ;	
        informat	  PCT012A104	best32. ;	
        informat	  PCT012A105	best32. ;	
        informat	  PCT012A106	best32. ;	
        informat	  PCT012A107	best32. ;	
        informat	  PCT012A108	best32. ;	
        informat	  PCT012A109	best32. ;	
        informat	  PCT012A110	best32. ;	
        informat	  PCT012A111	best32. ;	
        informat	  PCT012A112	best32. ;	
        informat	  PCT012A113	best32. ;	
        informat	  PCT012A114	best32. ;	
        informat	  PCT012A115	best32. ;	
        informat	  PCT012A116	best32. ;	
        informat	  PCT012A117	best32. ;	
        informat	  PCT012A118	best32. ;	
        informat	  PCT012A119	best32. ;	
        informat	  PCT012A120	best32. ;	
        informat	  PCT012A121	best32. ;	
        informat	  PCT012A122	best32. ;	
        informat	  PCT012A123	best32. ;	
        informat	  PCT012A124	best32. ;	
        informat	  PCT012A125	best32. ;	
        informat	  PCT012A126	best32. ;	
        informat	  PCT012A127	best32. ;	
        informat	  PCT012A128	best32. ;	
        informat	  PCT012A129	best32. ;	
        informat	  PCT012A130	best32. ;	
        informat	  PCT012A131	best32. ;	
        informat	  PCT012A132	best32. ;	
        informat	  PCT012A133	best32. ;	
        informat	  PCT012A134	best32. ;	
        informat	  PCT012A135	best32. ;	
        informat	  PCT012A136	best32. ;	
        informat	  PCT012A137	best32. ;	
        informat	  PCT012A138	best32. ;	
        informat	  PCT012A139	best32. ;	
        informat	  PCT012A140	best32. ;	
        informat	  PCT012A141	best32. ;	
        informat	  PCT012A142	best32. ;	
        informat	  PCT012A143	best32. ;	
        informat	  PCT012A144	best32. ;	
        informat	  PCT012A145	best32. ;	
        informat	  PCT012A146	best32. ;	
        informat	  PCT012A147	best32. ;	
        informat	  PCT012A148	best32. ;	
        informat	  PCT012A149	best32. ;	
        informat	  PCT012A150	best32. ;	
        informat	  PCT012A151	best32. ;	
        informat	  PCT012A152	best32. ;	
        informat	  PCT012A153	best32. ;	
        informat	  PCT012A154	best32. ;	
        informat	  PCT012A155	best32. ;	
        informat	  PCT012A156	best32. ;	
        informat	  PCT012A157	best32. ;	
        informat	  PCT012A158	best32. ;	
        informat	  PCT012A159	best32. ;	
        informat	  PCT012A160	best32. ;	
        informat	  PCT012A161	best32. ;	
        informat	  PCT012A162	best32. ;	
        informat	  PCT012A163	best32. ;	
        informat	  PCT012A164	best32. ;	
        informat	  PCT012A165	best32. ;	
        informat	  PCT012A166	best32. ;	
        informat	  PCT012A167	best32. ;	
        informat	  PCT012A168	best32. ;	
        informat	  PCT012A169	best32. ;	
        informat	  PCT012A170	best32. ;	
        informat	  PCT012A171	best32. ;	
        informat	  PCT012A172	best32. ;	
        informat	  PCT012A173	best32. ;	
        informat	  PCT012A174	best32. ;	
        informat	  PCT012A175	best32. ;	
        informat	  PCT012A176	best32. ;	
        informat	  PCT012A177	best32. ;	
        informat	  PCT012A178	best32. ;	
        informat	  PCT012A179	best32. ;	
        informat	  PCT012A180	best32. ;	
        informat	  PCT012A181	best32. ;	
        informat	  PCT012A182	best32. ;	
        informat	  PCT012A183	best32. ;	
        informat	  PCT012A184	best32. ;	
        informat	  PCT012A185	best32. ;	
        informat	  PCT012A186	best32. ;	
        informat	  PCT012A187	best32. ;	
        informat	  PCT012A188	best32. ;	
        informat	  PCT012A189	best32. ;	
        informat	  PCT012A190	best32. ;	
        informat	  PCT012A191	best32. ;	
        informat	  PCT012A192	best32. ;	
        informat	  PCT012A193	best32. ;	
        informat	  PCT012A194	best32. ;	
        informat	  PCT012A195	best32. ;	
        informat	  PCT012A196	best32. ;	
        informat	  PCT012A197	best32. ;	
        informat	  PCT012A198	best32. ;	
        informat	  PCT012A199	best32. ;	
        informat	  PCT012A200	best32. ;	
        informat	  PCT012A201	best32. ;	
        informat	  PCT012A202	best32. ;	
        informat	  PCT012A203	best32. ;	
        informat	  PCT012A204	best32. ;	
        informat	  PCT012A205	best32. ;	
        informat	  PCT012A206	best32. ;	
        informat	  PCT012A207	best32. ;	
        informat	  PCT012A208	best32. ;	
        informat	  PCT012A209	best32. ;	
        informat	  PCT012B001	best32. ;	
        informat	  PCT012B002	best32. ;	
        informat	  PCT012B003	best32. ;	
        informat	  PCT012B004	best32. ;	
        informat	  PCT012B005	best32. ;	
        informat	  PCT012B006	best32. ;	
        informat	  PCT012B007	best32. ;	
        informat	  PCT012B008	best32. ;	
        informat	  PCT012B009	best32. ;	
        informat	  PCT012B010	best32. ;	
        informat	  PCT012B011	best32. ;	
        informat	  PCT012B012	best32. ;	
        informat	  PCT012B013	best32. ;	
        informat	  PCT012B014	best32. ;	
        informat	  PCT012B015	best32. ;	
        informat	  PCT012B016	best32. ;	
        informat	  PCT012B017	best32. ;	
        informat	  PCT012B018	best32. ;	
        informat	  PCT012B019	best32. ;	
        informat	  PCT012B020	best32. ;	
        informat	  PCT012B021	best32. ;	
        informat	  PCT012B022	best32. ;	
        informat	  PCT012B023	best32. ;	
        informat	  PCT012B024	best32. ;	
        informat	  PCT012B025	best32. ;	
        informat	  PCT012B026	best32. ;	
        informat	  PCT012B027	best32. ;	
        informat	  PCT012B028	best32. ;	
        informat	  PCT012B029	best32. ;	
        informat	  PCT012B030	best32. ;	
        informat	  PCT012B031	best32. ;	
        informat	  PCT012B032	best32. ;	
        informat	  PCT012B033	best32. ;	
        informat	  PCT012B034	best32. ;	
        informat	  PCT012B035	best32. ;	
        informat	  PCT012B036	best32. ;	
        informat	  PCT012B037	best32. ;	
        informat	  PCT012B038	best32. ;	
        informat	  PCT012B039	best32. ;	
        informat	  PCT012B040	best32. ;	
        informat	  PCT012B041	best32. ;	
        informat	  PCT012B042	best32. ;	
        informat	  PCT012B043	best32. ;	
        informat	  PCT012B044	best32. ;	
        informat	  PCT012B045	best32. ;	
        informat	  PCT012B046	best32. ;	
        informat	  PCT012B047	best32. ;	
        informat	  PCT012B048	best32. ;	
        informat	  PCT012B049	best32. ;	
        informat	  PCT012B050	best32. ;	
        informat	  PCT012B051	best32. ;	
        informat	  PCT012B052	best32. ;	
        informat	  PCT012B053	best32. ;	
        informat	  PCT012B054	best32. ;	
        informat	  PCT012B055	best32. ;	
        informat	  PCT012B056	best32. ;	
        informat	  PCT012B057	best32. ;	
        informat	  PCT012B058	best32. ;	
        informat	  PCT012B059	best32. ;	
        informat	  PCT012B060	best32. ;	
        informat	  PCT012B061	best32. ;	
        informat	  PCT012B062	best32. ;	
        informat	  PCT012B063	best32. ;	
        informat	  PCT012B064	best32. ;	
        informat	  PCT012B065	best32. ;	
        informat	  PCT012B066	best32. ;	
        informat	  PCT012B067	best32. ;	
        informat	  PCT012B068	best32. ;	
        informat	  PCT012B069	best32. ;	
        informat	  PCT012B070	best32. ;	
        informat	  PCT012B071	best32. ;	
        informat	  PCT012B072	best32. ;	
        informat	  PCT012B073	best32. ;	
        informat	  PCT012B074	best32. ;	
        informat	  PCT012B075	best32. ;	
        informat	  PCT012B076	best32. ;	
        informat	  PCT012B077	best32. ;	
        informat	  PCT012B078	best32. ;	
        informat	  PCT012B079	best32. ;	
        informat	  PCT012B080	best32. ;	
        informat	  PCT012B081	best32. ;	
        informat	  PCT012B082	best32. ;	
        informat	  PCT012B083	best32. ;	
        informat	  PCT012B084	best32. ;	
        informat	  PCT012B085	best32. ;	
        informat	  PCT012B086	best32. ;	
        informat	  PCT012B087	best32. ;	
        informat	  PCT012B088	best32. ;	
        informat	  PCT012B089	best32. ;	
        informat	  PCT012B090	best32. ;	
        informat	  PCT012B091	best32. ;	
        informat	  PCT012B092	best32. ;	
        informat	  PCT012B093	best32. ;	
        informat	  PCT012B094	best32. ;	
        informat	  PCT012B095	best32. ;	
        informat	  PCT012B096	best32. ;	
        informat	  PCT012B097	best32. ;	
        informat	  PCT012B098	best32. ;	
        informat	  PCT012B099	best32. ;	
        informat	  PCT012B100	best32. ;	
        informat	  PCT012B101	best32. ;	
        informat	  PCT012B102	best32. ;	
        informat	  PCT012B103	best32. ;	
        informat	  PCT012B104	best32. ;	
        informat	  PCT012B105	best32. ;	
        informat	  PCT012B106	best32. ;	
        informat	  PCT012B107	best32. ;	
        informat	  PCT012B108	best32. ;	
        informat	  PCT012B109	best32. ;	
        informat	  PCT012B110	best32. ;	
        informat	  PCT012B111	best32. ;	
        informat	  PCT012B112	best32. ;	
        informat	  PCT012B113	best32. ;	
        informat	  PCT012B114	best32. ;	
        informat	  PCT012B115	best32. ;	
        informat	  PCT012B116	best32. ;	
        informat	  PCT012B117	best32. ;	
        informat	  PCT012B118	best32. ;	
        informat	  PCT012B119	best32. ;	
        informat	  PCT012B120	best32. ;	
        informat	  PCT012B121	best32. ;	
        informat	  PCT012B122	best32. ;	
        informat	  PCT012B123	best32. ;	
        informat	  PCT012B124	best32. ;	
        informat	  PCT012B125	best32. ;	
        informat	  PCT012B126	best32. ;	
        informat	  PCT012B127	best32. ;	
        informat	  PCT012B128	best32. ;	
        informat	  PCT012B129	best32. ;	
        informat	  PCT012B130	best32. ;	
        informat	  PCT012B131	best32. ;	
        informat	  PCT012B132	best32. ;	
        informat	  PCT012B133	best32. ;	
        informat	  PCT012B134	best32. ;	
        informat	  PCT012B135	best32. ;	
        informat	  PCT012B136	best32. ;	
        informat	  PCT012B137	best32. ;	
        informat	  PCT012B138	best32. ;	
        informat	  PCT012B139	best32. ;	
        informat	  PCT012B140	best32. ;	
        informat	  PCT012B141	best32. ;	
        informat	  PCT012B142	best32. ;	
        informat	  PCT012B143	best32. ;	
        informat	  PCT012B144	best32. ;	
        informat	  PCT012B145	best32. ;	
        informat	  PCT012B146	best32. ;	
        informat	  PCT012B147	best32. ;	
        informat	  PCT012B148	best32. ;	
        informat	  PCT012B149	best32. ;	
        informat	  PCT012B150	best32. ;	
        informat	  PCT012B151	best32. ;	
        informat	  PCT012B152	best32. ;	
        informat	  PCT012B153	best32. ;	
        informat	  PCT012B154	best32. ;	
        informat	  PCT012B155	best32. ;	
        informat	  PCT012B156	best32. ;	
        informat	  PCT012B157	best32. ;	
        informat	  PCT012B158	best32. ;	
        informat	  PCT012B159	best32. ;	
        informat	  PCT012B160	best32. ;	
        informat	  PCT012B161	best32. ;	
        informat	  PCT012B162	best32. ;	
        informat	  PCT012B163	best32. ;	
        informat	  PCT012B164	best32. ;	
        informat	  PCT012B165	best32. ;	
        informat	  PCT012B166	best32. ;	
        informat	  PCT012B167	best32. ;	
        informat	  PCT012B168	best32. ;	
        informat	  PCT012B169	best32. ;	
        informat	  PCT012B170	best32. ;	
        informat	  PCT012B171	best32. ;	
        informat	  PCT012B172	best32. ;	
        informat	  PCT012B173	best32. ;	
        informat	  PCT012B174	best32. ;	
        informat	  PCT012B175	best32. ;	
        informat	  PCT012B176	best32. ;	
        informat	  PCT012B177	best32. ;	
        informat	  PCT012B178	best32. ;	
        informat	  PCT012B179	best32. ;	
        informat	  PCT012B180	best32. ;	
        informat	  PCT012B181	best32. ;	
        informat	  PCT012B182	best32. ;	
        informat	  PCT012B183	best32. ;	
        informat	  PCT012B184	best32. ;	
        informat	  PCT012B185	best32. ;	
        informat	  PCT012B186	best32. ;	
        informat	  PCT012B187	best32. ;	
        informat	  PCT012B188	best32. ;	
        informat	  PCT012B189	best32. ;	
        informat	  PCT012B190	best32. ;	
        informat	  PCT012B191	best32. ;	
        informat	  PCT012B192	best32. ;	
        informat	  PCT012B193	best32. ;	
        informat	  PCT012B194	best32. ;	
        informat	  PCT012B195	best32. ;	
        informat	  PCT012B196	best32. ;	
        informat	  PCT012B197	best32. ;	
        informat	  PCT012B198	best32. ;	
        informat	  PCT012B199	best32. ;	
        informat	  PCT012B200	best32. ;	
        informat	  PCT012B201	best32. ;	
        informat	  PCT012B202	best32. ;	
        informat	  PCT012B203	best32. ;	
        informat	  PCT012B204	best32. ;	
        informat	  PCT012B205	best32. ;	
        informat	  PCT012B206	best32. ;	
        informat	  PCT012B207	best32. ;	
        informat	  PCT012B208	best32. ;	
        informat	  PCT012B209	best32. ;	
        informat	  PCT012C001	best32. ;	
        informat	  PCT012C002	best32. ;	
        informat	  PCT012C003	best32. ;	
        informat	  PCT012C004	best32. ;	
        informat	  PCT012C005	best32. ;	
        informat	  PCT012C006	best32. ;	
        informat	  PCT012C007	best32. ;	
        informat	  PCT012C008	best32. ;	
        informat	  PCT012C009	best32. ;	
        informat	  PCT012C010	best32. ;	
        informat	  PCT012C011	best32. ;	
        informat	  PCT012C012	best32. ;	
        informat	  PCT012C013	best32. ;	
        informat	  PCT012C014	best32. ;	
        informat	  PCT012C015	best32. ;	
        informat	  PCT012C016	best32. ;	
        informat	  PCT012C017	best32. ;	
        informat	  PCT012C018	best32. ;	
        informat	  PCT012C019	best32. ;	
        informat	  PCT012C020	best32. ;	
        informat	  PCT012C021	best32. ;	
        informat	  PCT012C022	best32. ;	
        informat	  PCT012C023	best32. ;	
        informat	  PCT012C024	best32. ;	
        informat	  PCT012C025	best32. ;	
        informat	  PCT012C026	best32. ;	
        informat	  PCT012C027	best32. ;	
        informat	  PCT012C028	best32. ;	
        informat	  PCT012C029	best32. ;	
        informat	  PCT012C030	best32. ;	
        informat	  PCT012C031	best32. ;	
        informat	  PCT012C032	best32. ;	
        informat	  PCT012C033	best32. ;	
        informat	  PCT012C034	best32. ;	
        informat	  PCT012C035	best32. ;	
        informat	  PCT012C036	best32. ;	
        informat	  PCT012C037	best32. ;	
        informat	  PCT012C038	best32. ;	
        informat	  PCT012C039	best32. ;	
        informat	  PCT012C040	best32. ;	
        informat	  PCT012C041	best32. ;	
        informat	  PCT012C042	best32. ;	
        informat	  PCT012C043	best32. ;	
        informat	  PCT012C044	best32. ;	
        informat	  PCT012C045	best32. ;	
        informat	  PCT012C046	best32. ;	
        informat	  PCT012C047	best32. ;	
        informat	  PCT012C048	best32. ;	
        informat	  PCT012C049	best32. ;	
        informat	  PCT012C050	best32. ;	
        informat	  PCT012C051	best32. ;	
        informat	  PCT012C052	best32. ;	
        informat	  PCT012C053	best32. ;	
        informat	  PCT012C054	best32. ;	
        informat	  PCT012C055	best32. ;	
        informat	  PCT012C056	best32. ;	
        informat	  PCT012C057	best32. ;	
        informat	  PCT012C058	best32. ;	
        informat	  PCT012C059	best32. ;	
        informat	  PCT012C060	best32. ;	
        informat	  PCT012C061	best32. ;	
        informat	  PCT012C062	best32. ;	
        informat	  PCT012C063	best32. ;	
        informat	  PCT012C064	best32. ;	
        informat	  PCT012C065	best32. ;	
        informat	  PCT012C066	best32. ;	
        informat	  PCT012C067	best32. ;	
        informat	  PCT012C068	best32. ;	
        informat	  PCT012C069	best32. ;	
        informat	  PCT012C070	best32. ;	
        informat	  PCT012C071	best32. ;	
        informat	  PCT012C072	best32. ;	
        informat	  PCT012C073	best32. ;	
        informat	  PCT012C074	best32. ;	
        informat	  PCT012C075	best32. ;	
        informat	  PCT012C076	best32. ;	
        informat	  PCT012C077	best32. ;	
        informat	  PCT012C078	best32. ;	
        informat	  PCT012C079	best32. ;	
        informat	  PCT012C080	best32. ;	
        informat	  PCT012C081	best32. ;	
        informat	  PCT012C082	best32. ;	
        informat	  PCT012C083	best32. ;	
        informat	  PCT012C084	best32. ;	
        informat	  PCT012C085	best32. ;	
        informat	  PCT012C086	best32. ;	
        informat	  PCT012C087	best32. ;	
        informat	  PCT012C088	best32. ;	
        informat	  PCT012C089	best32. ;	
        informat	  PCT012C090	best32. ;	
        informat	  PCT012C091	best32. ;	
        informat	  PCT012C092	best32. ;	
        informat	  PCT012C093	best32. ;	
        informat	  PCT012C094	best32. ;	
        informat	  PCT012C095	best32. ;	
        informat	  PCT012C096	best32. ;	
        informat	  PCT012C097	best32. ;	
        informat	  PCT012C098	best32. ;	
        informat	  PCT012C099	best32. ;	
        informat	  PCT012C100	best32. ;	
        informat	  PCT012C101	best32. ;	
        informat	  PCT012C102	best32. ;	
        informat	  PCT012C103	best32. ;	
        informat	  PCT012C104	best32. ;	
        informat	  PCT012C105	best32. ;	
        informat	  PCT012C106	best32. ;	
        informat	  PCT012C107	best32. ;	
        informat	  PCT012C108	best32. ;	
        informat	  PCT012C109	best32. ;	
        informat	  PCT012C110	best32. ;	
        informat	  PCT012C111	best32. ;	
        informat	  PCT012C112	best32. ;	
        informat	  PCT012C113	best32. ;	
        informat	  PCT012C114	best32. ;	
        informat	  PCT012C115	best32. ;	
        informat	  PCT012C116	best32. ;	
        informat	  PCT012C117	best32. ;	
        informat	  PCT012C118	best32. ;	
        informat	  PCT012C119	best32. ;	
        informat	  PCT012C120	best32. ;	
        informat	  PCT012C121	best32. ;	
        informat	  PCT012C122	best32. ;	
        informat	  PCT012C123	best32. ;	
        informat	  PCT012C124	best32. ;	
        informat	  PCT012C125	best32. ;	
        informat	  PCT012C126	best32. ;	
        informat	  PCT012C127	best32. ;	
        informat	  PCT012C128	best32. ;	
        informat	  PCT012C129	best32. ;	
        informat	  PCT012C130	best32. ;	
        informat	  PCT012C131	best32. ;	
        informat	  PCT012C132	best32. ;	
        informat	  PCT012C133	best32. ;	
        informat	  PCT012C134	best32. ;	
        informat	  PCT012C135	best32. ;	
        informat	  PCT012C136	best32. ;	
        informat	  PCT012C137	best32. ;	
        informat	  PCT012C138	best32. ;	
        informat	  PCT012C139	best32. ;	
        informat	  PCT012C140	best32. ;	
        informat	  PCT012C141	best32. ;	
        informat	  PCT012C142	best32. ;	
        informat	  PCT012C143	best32. ;	
        informat	  PCT012C144	best32. ;	
        informat	  PCT012C145	best32. ;	
        informat	  PCT012C146	best32. ;	
        informat	  PCT012C147	best32. ;	
        informat	  PCT012C148	best32. ;	
        informat	  PCT012C149	best32. ;	
        informat	  PCT012C150	best32. ;	
        informat	  PCT012C151	best32. ;	
        informat	  PCT012C152	best32. ;	
        informat	  PCT012C153	best32. ;	
        informat	  PCT012C154	best32. ;	
        informat	  PCT012C155	best32. ;	
        informat	  PCT012C156	best32. ;	
        informat	  PCT012C157	best32. ;	
        informat	  PCT012C158	best32. ;	
        informat	  PCT012C159	best32. ;	
        informat	  PCT012C160	best32. ;	
        informat	  PCT012C161	best32. ;	
        informat	  PCT012C162	best32. ;	
        informat	  PCT012C163	best32. ;	
        informat	  PCT012C164	best32. ;	
        informat	  PCT012C165	best32. ;	
        informat	  PCT012C166	best32. ;	
        informat	  PCT012C167	best32. ;	
        informat	  PCT012C168	best32. ;	
        informat	  PCT012C169	best32. ;	
        informat	  PCT012C170	best32. ;	
        informat	  PCT012C171	best32. ;	
        informat	  PCT012C172	best32. ;	
        informat	  PCT012C173	best32. ;	
        informat	  PCT012C174	best32. ;	
        informat	  PCT012C175	best32. ;	
        informat	  PCT012C176	best32. ;	
        informat	  PCT012C177	best32. ;	
        informat	  PCT012C178	best32. ;	
        informat	  PCT012C179	best32. ;	
        informat	  PCT012C180	best32. ;	
        informat	  PCT012C181	best32. ;	
        informat	  PCT012C182	best32. ;	
        informat	  PCT012C183	best32. ;	
        informat	  PCT012C184	best32. ;	
        informat	  PCT012C185	best32. ;	
        informat	  PCT012C186	best32. ;	
        informat	  PCT012C187	best32. ;	
        informat	  PCT012C188	best32. ;	
        informat	  PCT012C189	best32. ;	
        informat	  PCT012C190	best32. ;	
        informat	  PCT012C191	best32. ;	
        informat	  PCT012C192	best32. ;	
        informat	  PCT012C193	best32. ;	
        informat	  PCT012C194	best32. ;	
        informat	  PCT012C195	best32. ;	
        informat	  PCT012C196	best32. ;	
        informat	  PCT012C197	best32. ;	
        informat	  PCT012C198	best32. ;	
        informat	  PCT012C199	best32. ;	
        informat	  PCT012C200	best32. ;	
        informat	  PCT012C201	best32. ;	
        informat	  PCT012C202	best32. ;	
        informat	  PCT012C203	best32. ;	
        informat	  PCT012C204	best32. ;	
        informat	  PCT012C205	best32. ;	
        informat	  PCT012C206	best32. ;	
        informat	  PCT012C207	best32. ;	
        informat	  PCT012C208	best32. ;	
        informat	  PCT012C209	best32. ;	
        informat	  PCT012D001	best32. ;	
        informat	  PCT012D002	best32. ;	
        informat	  PCT012D003	best32. ;	
        informat	  PCT012D004	best32. ;	
        informat	  PCT012D005	best32. ;	
        informat	  PCT012D006	best32. ;	
        informat	  PCT012D007	best32. ;	
        informat	  PCT012D008	best32. ;	
        informat	  PCT012D009	best32. ;	
        informat	  PCT012D010	best32. ;	
        informat	  PCT012D011	best32. ;	
        informat	  PCT012D012	best32. ;	
        informat	  PCT012D013	best32. ;	
        informat	  PCT012D014	best32. ;	
        informat	  PCT012D015	best32. ;	
        informat	  PCT012D016	best32. ;	
        informat	  PCT012D017	best32. ;	
        informat	  PCT012D018	best32. ;	
        informat	  PCT012D019	best32. ;	
        informat	  PCT012D020	best32. ;	
        informat	  PCT012D021	best32. ;	
        informat	  PCT012D022	best32. ;	
        informat	  PCT012D023	best32. ;	
        informat	  PCT012D024	best32. ;	
        informat	  PCT012D025	best32. ;	
        informat	  PCT012D026	best32. ;	
        informat	  PCT012D027	best32. ;	
        informat	  PCT012D028	best32. ;	
        informat	  PCT012D029	best32. ;	
        informat	  PCT012D030	best32. ;	
        informat	  PCT012D031	best32. ;	
        informat	  PCT012D032	best32. ;	
        informat	  PCT012D033	best32. ;	
        informat	  PCT012D034	best32. ;	
        informat	  PCT012D035	best32. ;	
        informat	  PCT012D036	best32. ;	
        informat	  PCT012D037	best32. ;	
        informat	  PCT012D038	best32. ;	
        informat	  PCT012D039	best32. ;	
        informat	  PCT012D040	best32. ;	
        informat	  PCT012D041	best32. ;	
        informat	  PCT012D042	best32. ;	
        informat	  PCT012D043	best32. ;	
        informat	  PCT012D044	best32. ;	
        informat	  PCT012D045	best32. ;	
        informat	  PCT012D046	best32. ;	
        informat	  PCT012D047	best32. ;	
        informat	  PCT012D048	best32. ;	
        informat	  PCT012D049	best32. ;	
        informat	  PCT012D050	best32. ;	
        informat	  PCT012D051	best32. ;	
        informat	  PCT012D052	best32. ;	
        informat	  PCT012D053	best32. ;	
        informat	  PCT012D054	best32. ;	
        informat	  PCT012D055	best32. ;	
        informat	  PCT012D056	best32. ;	
        informat	  PCT012D057	best32. ;	
        informat	  PCT012D058	best32. ;	
        informat	  PCT012D059	best32. ;	
        informat	  PCT012D060	best32. ;	
        informat	  PCT012D061	best32. ;	
        informat	  PCT012D062	best32. ;	
        informat	  PCT012D063	best32. ;	
        informat	  PCT012D064	best32. ;	
        informat	  PCT012D065	best32. ;	
        informat	  PCT012D066	best32. ;	
        informat	  PCT012D067	best32. ;	
        informat	  PCT012D068	best32. ;	
        informat	  PCT012D069	best32. ;	
        informat	  PCT012D070	best32. ;	
        informat	  PCT012D071	best32. ;	
        informat	  PCT012D072	best32. ;	
        informat	  PCT012D073	best32. ;	
        informat	  PCT012D074	best32. ;	
        informat	  PCT012D075	best32. ;	
        informat	  PCT012D076	best32. ;	
        informat	  PCT012D077	best32. ;	
        informat	  PCT012D078	best32. ;	
        informat	  PCT012D079	best32. ;	
        informat	  PCT012D080	best32. ;	
        informat	  PCT012D081	best32. ;	
        informat	  PCT012D082	best32. ;	
        informat	  PCT012D083	best32. ;	
        informat	  PCT012D084	best32. ;	
        informat	  PCT012D085	best32. ;	
        informat	  PCT012D086	best32. ;	
        informat	  PCT012D087	best32. ;	
        informat	  PCT012D088	best32. ;	
        informat	  PCT012D089	best32. ;	
        informat	  PCT012D090	best32. ;	
        informat	  PCT012D091	best32. ;	
        informat	  PCT012D092	best32. ;	
        informat	  PCT012D093	best32. ;	
        informat	  PCT012D094	best32. ;	
        informat	  PCT012D095	best32. ;	
        informat	  PCT012D096	best32. ;	
        informat	  PCT012D097	best32. ;	
        informat	  PCT012D098	best32. ;	
        informat	  PCT012D099	best32. ;	
        informat	  PCT012D100	best32. ;	
        informat	  PCT012D101	best32. ;	
        informat	  PCT012D102	best32. ;	
        informat	  PCT012D103	best32. ;	
        informat	  PCT012D104	best32. ;	
        informat	  PCT012D105	best32. ;	
        informat	  PCT012D106	best32. ;	
        informat	  PCT012D107	best32. ;	
        informat	  PCT012D108	best32. ;	
        informat	  PCT012D109	best32. ;	
        informat	  PCT012D110	best32. ;	
        informat	  PCT012D111	best32. ;	
        informat	  PCT012D112	best32. ;	
        informat	  PCT012D113	best32. ;	
        informat	  PCT012D114	best32. ;	
        informat	  PCT012D115	best32. ;	
        informat	  PCT012D116	best32. ;	
        informat	  PCT012D117	best32. ;	
        informat	  PCT012D118	best32. ;	
        informat	  PCT012D119	best32. ;	
        informat	  PCT012D120	best32. ;	
        informat	  PCT012D121	best32. ;	
        informat	  PCT012D122	best32. ;	
        informat	  PCT012D123	best32. ;	
        informat	  PCT012D124	best32. ;	
        informat	  PCT012D125	best32. ;	
        informat	  PCT012D126	best32. ;	
        informat	  PCT012D127	best32. ;	
        informat	  PCT012D128	best32. ;	
        informat	  PCT012D129	best32. ;	
        informat	  PCT012D130	best32. ;	
        informat	  PCT012D131	best32. ;	
        informat	  PCT012D132	best32. ;	
        informat	  PCT012D133	best32. ;	
        informat	  PCT012D134	best32. ;	
        informat	  PCT012D135	best32. ;	
        informat	  PCT012D136	best32. ;	
        informat	  PCT012D137	best32. ;	
        informat	  PCT012D138	best32. ;	
        informat	  PCT012D139	best32. ;	
        informat	  PCT012D140	best32. ;	
        informat	  PCT012D141	best32. ;	
        informat	  PCT012D142	best32. ;	
        informat	  PCT012D143	best32. ;	
        informat	  PCT012D144	best32. ;	
        informat	  PCT012D145	best32. ;	
        informat	  PCT012D146	best32. ;	
        informat	  PCT012D147	best32. ;	
        informat	  PCT012D148	best32. ;	
        informat	  PCT012D149	best32. ;	
        informat	  PCT012D150	best32. ;	
        informat	  PCT012D151	best32. ;	
        informat	  PCT012D152	best32. ;	
        informat	  PCT012D153	best32. ;	
        informat	  PCT012D154	best32. ;	
        informat	  PCT012D155	best32. ;	
        informat	  PCT012D156	best32. ;	
        informat	  PCT012D157	best32. ;	
        informat	  PCT012D158	best32. ;	
        informat	  PCT012D159	best32. ;	
        informat	  PCT012D160	best32. ;	
        informat	  PCT012D161	best32. ;	
        informat	  PCT012D162	best32. ;	
        informat	  PCT012D163	best32. ;	
        informat	  PCT012D164	best32. ;	
        informat	  PCT012D165	best32. ;	
        informat	  PCT012D166	best32. ;	
        informat	  PCT012D167	best32. ;	
        informat	  PCT012D168	best32. ;	
        informat	  PCT012D169	best32. ;	
        informat	  PCT012D170	best32. ;	
        informat	  PCT012D171	best32. ;	
        informat	  PCT012D172	best32. ;	
        informat	  PCT012D173	best32. ;	
        informat	  PCT012D174	best32. ;	
        informat	  PCT012D175	best32. ;	
        informat	  PCT012D176	best32. ;	
        informat	  PCT012D177	best32. ;	
        informat	  PCT012D178	best32. ;	
        informat	  PCT012D179	best32. ;	
        informat	  PCT012D180	best32. ;	
        informat	  PCT012D181	best32. ;	
        informat	  PCT012D182	best32. ;	
        informat	  PCT012D183	best32. ;	
        informat	  PCT012D184	best32. ;	
        informat	  PCT012D185	best32. ;	
        informat	  PCT012D186	best32. ;	
        informat	  PCT012D187	best32. ;	
        informat	  PCT012D188	best32. ;	
        informat	  PCT012D189	best32. ;	
        informat	  PCT012D190	best32. ;	
        informat	  PCT012D191	best32. ;	
        informat	  PCT012D192	best32. ;	
        informat	  PCT012D193	best32. ;	
        informat	  PCT012D194	best32. ;	
        informat	  PCT012D195	best32. ;	
        informat	  PCT012D196	best32. ;	
        informat	  PCT012D197	best32. ;	
        informat	  PCT012D198	best32. ;	
        informat	  PCT012D199	best32. ;	
        informat	  PCT012D200	best32. ;	
        informat	  PCT012D201	best32. ;	
        informat	  PCT012D202	best32. ;	
        informat	  PCT012D203	best32. ;	
        informat	  PCT012D204	best32. ;	
        informat	  PCT012D205	best32. ;	
        informat	  PCT012D206	best32. ;	
        informat	  PCT012D207	best32. ;	
        informat	  PCT012D208	best32. ;	
        informat	  PCT012D209	best32. ;	
        informat	  PCT012E001	best32. ;	
        informat	  PCT012E002	best32. ;	
        informat	  PCT012E003	best32. ;	
        informat	  PCT012E004	best32. ;	
        informat	  PCT012E005	best32. ;	
        informat	  PCT012E006	best32. ;	
        informat	  PCT012E007	best32. ;	
        informat	  PCT012E008	best32. ;	
        informat	  PCT012E009	best32. ;	
        informat	  PCT012E010	best32. ;	
        informat	  PCT012E011	best32. ;	
        informat	  PCT012E012	best32. ;	
        informat	  PCT012E013	best32. ;	
        informat	  PCT012E014	best32. ;	
        informat	  PCT012E015	best32. ;	
        informat	  PCT012E016	best32. ;	
        informat	  PCT012E017	best32. ;	
        informat	  PCT012E018	best32. ;	
        informat	  PCT012E019	best32. ;	
        informat	  PCT012E020	best32. ;	
        informat	  PCT012E021	best32. ;	
        informat	  PCT012E022	best32. ;	
        informat	  PCT012E023	best32. ;	
        informat	  PCT012E024	best32. ;	
        informat	  PCT012E025	best32. ;	
        informat	  PCT012E026	best32. ;	
        informat	  PCT012E027	best32. ;	
        informat	  PCT012E028	best32. ;	
        informat	  PCT012E029	best32. ;	
        informat	  PCT012E030	best32. ;	
        informat	  PCT012E031	best32. ;	
        informat	  PCT012E032	best32. ;	
        informat	  PCT012E033	best32. ;	
        informat	  PCT012E034	best32. ;	
        informat	  PCT012E035	best32. ;	
        informat	  PCT012E036	best32. ;	
        informat	  PCT012E037	best32. ;	
        informat	  PCT012E038	best32. ;	
        informat	  PCT012E039	best32. ;	
        informat	  PCT012E040	best32. ;	
        informat	  PCT012E041	best32. ;	
        informat	  PCT012E042	best32. ;	
        informat	  PCT012E043	best32. ;	
        informat	  PCT012E044	best32. ;	
        informat	  PCT012E045	best32. ;	
        informat	  PCT012E046	best32. ;	
        informat	  PCT012E047	best32. ;	
        informat	  PCT012E048	best32. ;	
        informat	  PCT012E049	best32. ;	
        informat	  PCT012E050	best32. ;	
        informat	  PCT012E051	best32. ;	
        informat	  PCT012E052	best32. ;	
        informat	  PCT012E053	best32. ;	
        informat	  PCT012E054	best32. ;	
        informat	  PCT012E055	best32. ;	
        informat	  PCT012E056	best32. ;	
        informat	  PCT012E057	best32. ;	
        informat	  PCT012E058	best32. ;	
        informat	  PCT012E059	best32. ;	
        informat	  PCT012E060	best32. ;	
        informat	  PCT012E061	best32. ;	
        informat	  PCT012E062	best32. ;	
        informat	  PCT012E063	best32. ;	
        informat	  PCT012E064	best32. ;	
        informat	  PCT012E065	best32. ;	
        informat	  PCT012E066	best32. ;	
        informat	  PCT012E067	best32. ;	
        informat	  PCT012E068	best32. ;	
        informat	  PCT012E069	best32. ;	
        informat	  PCT012E070	best32. ;	
        informat	  PCT012E071	best32. ;	
        informat	  PCT012E072	best32. ;	
        informat	  PCT012E073	best32. ;	
        informat	  PCT012E074	best32. ;	
        informat	  PCT012E075	best32. ;	
        informat	  PCT012E076	best32. ;	
        informat	  PCT012E077	best32. ;	
        informat	  PCT012E078	best32. ;	
        informat	  PCT012E079	best32. ;	
        informat	  PCT012E080	best32. ;	
        informat	  PCT012E081	best32. ;	
        informat	  PCT012E082	best32. ;	
        informat	  PCT012E083	best32. ;	
        informat	  PCT012E084	best32. ;	
        informat	  PCT012E085	best32. ;	
        informat	  PCT012E086	best32. ;	
        informat	  PCT012E087	best32. ;	
        informat	  PCT012E088	best32. ;	
        informat	  PCT012E089	best32. ;	
        informat	  PCT012E090	best32. ;	
        informat	  PCT012E091	best32. ;	
        informat	  PCT012E092	best32. ;	
        informat	  PCT012E093	best32. ;	
        informat	  PCT012E094	best32. ;	
        informat	  PCT012E095	best32. ;	
        informat	  PCT012E096	best32. ;	
        informat	  PCT012E097	best32. ;	
        informat	  PCT012E098	best32. ;	
        informat	  PCT012E099	best32. ;	
        informat	  PCT012E100	best32. ;	
        informat	  PCT012E101	best32. ;	
        informat	  PCT012E102	best32. ;	
        informat	  PCT012E103	best32. ;	
        informat	  PCT012E104	best32. ;	
        informat	  PCT012E105	best32. ;	
        informat	  PCT012E106	best32. ;	
        informat	  PCT012E107	best32. ;	
        informat	  PCT012E108	best32. ;	
        informat	  PCT012E109	best32. ;	
        informat	  PCT012E110	best32. ;	
        informat	  PCT012E111	best32. ;	
        informat	  PCT012E112	best32. ;	
        informat	  PCT012E113	best32. ;	
        informat	  PCT012E114	best32. ;	
        informat	  PCT012E115	best32. ;	
        informat	  PCT012E116	best32. ;	
        informat	  PCT012E117	best32. ;	
        informat	  PCT012E118	best32. ;	
        informat	  PCT012E119	best32. ;	
        informat	  PCT012E120	best32. ;	
        informat	  PCT012E121	best32. ;	
        informat	  PCT012E122	best32. ;	
        informat	  PCT012E123	best32. ;	
        informat	  PCT012E124	best32. ;	
        informat	  PCT012E125	best32. ;	
        informat	  PCT012E126	best32. ;	
        informat	  PCT012E127	best32. ;	
        informat	  PCT012E128	best32. ;	
        informat	  PCT012E129	best32. ;	
        informat	  PCT012E130	best32. ;	
        informat	  PCT012E131	best32. ;	
        informat	  PCT012E132	best32. ;	
        informat	  PCT012E133	best32. ;	
        informat	  PCT012E134	best32. ;	
        informat	  PCT012E135	best32. ;	
        informat	  PCT012E136	best32. ;	
        informat	  PCT012E137	best32. ;	
        informat	  PCT012E138	best32. ;	
        informat	  PCT012E139	best32. ;	
        informat	  PCT012E140	best32. ;	
        informat	  PCT012E141	best32. ;	
        informat	  PCT012E142	best32. ;	
        informat	  PCT012E143	best32. ;	
        informat	  PCT012E144	best32. ;	
        informat	  PCT012E145	best32. ;	
        informat	  PCT012E146	best32. ;	
        informat	  PCT012E147	best32. ;	
        informat	  PCT012E148	best32. ;	
        informat	  PCT012E149	best32. ;	
        informat	  PCT012E150	best32. ;	
        informat	  PCT012E151	best32. ;	
        informat	  PCT012E152	best32. ;	
        informat	  PCT012E153	best32. ;	
        informat	  PCT012E154	best32. ;	
        informat	  PCT012E155	best32. ;	
        informat	  PCT012E156	best32. ;	
        informat	  PCT012E157	best32. ;	
        informat	  PCT012E158	best32. ;	
        informat	  PCT012E159	best32. ;	
        informat	  PCT012E160	best32. ;	
        informat	  PCT012E161	best32. ;	
        informat	  PCT012E162	best32. ;	
        informat	  PCT012E163	best32. ;	
        informat	  PCT012E164	best32. ;	
        informat	  PCT012E165	best32. ;	
        informat	  PCT012E166	best32. ;	
        informat	  PCT012E167	best32. ;	
        informat	  PCT012E168	best32. ;	
        informat	  PCT012E169	best32. ;	
        informat	  PCT012E170	best32. ;	
        informat	  PCT012E171	best32. ;	
        informat	  PCT012E172	best32. ;	
        informat	  PCT012E173	best32. ;	
        informat	  PCT012E174	best32. ;	
        informat	  PCT012E175	best32. ;	
        informat	  PCT012E176	best32. ;	
        informat	  PCT012E177	best32. ;	
        informat	  PCT012E178	best32. ;	
        informat	  PCT012E179	best32. ;	
        informat	  PCT012E180	best32. ;	
        informat	  PCT012E181	best32. ;	
        informat	  PCT012E182	best32. ;	
        informat	  PCT012E183	best32. ;	
        informat	  PCT012E184	best32. ;	
        informat	  PCT012E185	best32. ;	
        informat	  PCT012E186	best32. ;	
        informat	  PCT012E187	best32. ;	
        informat	  PCT012E188	best32. ;	
        informat	  PCT012E189	best32. ;	
        informat	  PCT012E190	best32. ;	
        informat	  PCT012E191	best32. ;	
        informat	  PCT012E192	best32. ;	
        informat	  PCT012E193	best32. ;	
        informat	  PCT012E194	best32. ;	
        informat	  PCT012E195	best32. ;	
        informat	  PCT012E196	best32. ;	
        informat	  PCT012E197	best32. ;	
        informat	  PCT012E198	best32. ;	
        informat	  PCT012E199	best32. ;	
        informat	  PCT012E200	best32. ;	
        informat	  PCT012E201	best32. ;	
        informat	  PCT012E202	best32. ;	
        informat	  PCT012E203	best32. ;	
        informat	  PCT012E204	best32. ;	
        informat	  PCT012E205	best32. ;	
        informat	  PCT012E206	best32. ;	
        informat	  PCT012E207	best32. ;	
        informat	  PCT012E208	best32. ;	
        informat	  PCT012E209	best32. ;	
        informat	  PCT012F001	best32. ;	
        informat	  PCT012F002	best32. ;	
        informat	  PCT012F003	best32. ;	
        informat	  PCT012F004	best32. ;	
        informat	  PCT012F005	best32. ;	
        informat	  PCT012F006	best32. ;	
        informat	  PCT012F007	best32. ;	
        informat	  PCT012F008	best32. ;	
        informat	  PCT012F009	best32. ;	
        informat	  PCT012F010	best32. ;	
        informat	  PCT012F011	best32. ;	
        informat	  PCT012F012	best32. ;	
        informat	  PCT012F013	best32. ;	
        informat	  PCT012F014	best32. ;	
        informat	  PCT012F015	best32. ;	
        informat	  PCT012F016	best32. ;	
        informat	  PCT012F017	best32. ;	
        informat	  PCT012F018	best32. ;	
        informat	  PCT012F019	best32. ;	
        informat	  PCT012F020	best32. ;	
        informat	  PCT012F021	best32. ;	
        informat	  PCT012F022	best32. ;	
        informat	  PCT012F023	best32. ;	
        informat	  PCT012F024	best32. ;	
        informat	  PCT012F025	best32. ;	
        informat	  PCT012F026	best32. ;	
        informat	  PCT012F027	best32. ;	
        informat	  PCT012F028	best32. ;	
        informat	  PCT012F029	best32. ;	
        informat	  PCT012F030	best32. ;	
        informat	  PCT012F031	best32. ;	
        informat	  PCT012F032	best32. ;	
        informat	  PCT012F033	best32. ;	
        informat	  PCT012F034	best32. ;	
        informat	  PCT012F035	best32. ;	
        informat	  PCT012F036	best32. ;	
        informat	  PCT012F037	best32. ;	
        informat	  PCT012F038	best32. ;	
        informat	  PCT012F039	best32. ;	
        informat	  PCT012F040	best32. ;	
        informat	  PCT012F041	best32. ;	
        informat	  PCT012F042	best32. ;	
        informat	  PCT012F043	best32. ;	
        informat	  PCT012F044	best32. ;	
        informat	  PCT012F045	best32. ;	
        informat	  PCT012F046	best32. ;	
        informat	  PCT012F047	best32. ;	
        informat	  PCT012F048	best32. ;	
        informat	  PCT012F049	best32. ;	
        informat	  PCT012F050	best32. ;	
        informat	  PCT012F051	best32. ;	
        informat	  PCT012F052	best32. ;	
        informat	  PCT012F053	best32. ;	
        informat	  PCT012F054	best32. ;	
        informat	  PCT012F055	best32. ;	
        informat	  PCT012F056	best32. ;	
        informat	  PCT012F057	best32. ;	
        informat	  PCT012F058	best32. ;	
        informat	  PCT012F059	best32. ;	
        informat	  PCT012F060	best32. ;	
        informat	  PCT012F061	best32. ;	
        informat	  PCT012F062	best32. ;	
        informat	  PCT012F063	best32. ;	
        informat	  PCT012F064	best32. ;	
        informat	  PCT012F065	best32. ;	
        informat	  PCT012F066	best32. ;	
        informat	  PCT012F067	best32. ;	
        informat	  PCT012F068	best32. ;	
        informat	  PCT012F069	best32. ;	
        informat	  PCT012F070	best32. ;	
        informat	  PCT012F071	best32. ;	
        informat	  PCT012F072	best32. ;	
        informat	  PCT012F073	best32. ;	
        informat	  PCT012F074	best32. ;	
        informat	  PCT012F075	best32. ;	
        informat	  PCT012F076	best32. ;	
        informat	  PCT012F077	best32. ;	
        informat	  PCT012F078	best32. ;	
        informat	  PCT012F079	best32. ;	
        informat	  PCT012F080	best32. ;	
        informat	  PCT012F081	best32. ;	
        informat	  PCT012F082	best32. ;	
        informat	  PCT012F083	best32. ;	
        informat	  PCT012F084	best32. ;	
        informat	  PCT012F085	best32. ;	
        informat	  PCT012F086	best32. ;	
        informat	  PCT012F087	best32. ;	
        informat	  PCT012F088	best32. ;	
        informat	  PCT012F089	best32. ;	
        informat	  PCT012F090	best32. ;	
        informat	  PCT012F091	best32. ;	
        informat	  PCT012F092	best32. ;	
        informat	  PCT012F093	best32. ;	
        informat	  PCT012F094	best32. ;	
        informat	  PCT012F095	best32. ;	
        informat	  PCT012F096	best32. ;	
        informat	  PCT012F097	best32. ;	
        informat	  PCT012F098	best32. ;	
        informat	  PCT012F099	best32. ;	
        informat	  PCT012F100	best32. ;	
        informat	  PCT012F101	best32. ;	
        informat	  PCT012F102	best32. ;	
        informat	  PCT012F103	best32. ;	
        informat	  PCT012F104	best32. ;	
        informat	  PCT012F105	best32. ;	
        informat	  PCT012F106	best32. ;	
        informat	  PCT012F107	best32. ;	
        informat	  PCT012F108	best32. ;	
        informat	  PCT012F109	best32. ;	
        informat	  PCT012F110	best32. ;	
        informat	  PCT012F111	best32. ;	
        informat	  PCT012F112	best32. ;	
        informat	  PCT012F113	best32. ;	
        informat	  PCT012F114	best32. ;	
        informat	  PCT012F115	best32. ;	
        informat	  PCT012F116	best32. ;	
        informat	  PCT012F117	best32. ;	
        informat	  PCT012F118	best32. ;	
        informat	  PCT012F119	best32. ;	
        informat	  PCT012F120	best32. ;	
        informat	  PCT012F121	best32. ;	
        informat	  PCT012F122	best32. ;	
        informat	  PCT012F123	best32. ;	
        informat	  PCT012F124	best32. ;	
        informat	  PCT012F125	best32. ;	
        informat	  PCT012F126	best32. ;	
        informat	  PCT012F127	best32. ;	
        informat	  PCT012F128	best32. ;	
        informat	  PCT012F129	best32. ;	
        informat	  PCT012F130	best32. ;	
        informat	  PCT012F131	best32. ;	
        informat	  PCT012F132	best32. ;	
        informat	  PCT012F133	best32. ;	
        informat	  PCT012F134	best32. ;	
        informat	  PCT012F135	best32. ;	
        informat	  PCT012F136	best32. ;	
        informat	  PCT012F137	best32. ;	
        informat	  PCT012F138	best32. ;	
        informat	  PCT012F139	best32. ;	
        informat	  PCT012F140	best32. ;	
        informat	  PCT012F141	best32. ;	
        informat	  PCT012F142	best32. ;	
        informat	  PCT012F143	best32. ;	
        informat	  PCT012F144	best32. ;	
        informat	  PCT012F145	best32. ;	
        informat	  PCT012F146	best32. ;	
        informat	  PCT012F147	best32. ;	
        informat	  PCT012F148	best32. ;	
        informat	  PCT012F149	best32. ;	
        informat	  PCT012F150	best32. ;	
        informat	  PCT012F151	best32. ;	
        informat	  PCT012F152	best32. ;	
        informat	  PCT012F153	best32. ;	
        informat	  PCT012F154	best32. ;	
        informat	  PCT012F155	best32. ;	
        informat	  PCT012F156	best32. ;	
        informat	  PCT012F157	best32. ;	
        informat	  PCT012F158	best32. ;	
        informat	  PCT012F159	best32. ;	
        informat	  PCT012F160	best32. ;	
        informat	  PCT012F161	best32. ;	
        informat	  PCT012F162	best32. ;	
        informat	  PCT012F163	best32. ;	
        informat	  PCT012F164	best32. ;	
        informat	  PCT012F165	best32. ;	
        informat	  PCT012F166	best32. ;	
        informat	  PCT012F167	best32. ;	
        informat	  PCT012F168	best32. ;	
        informat	  PCT012F169	best32. ;	
        informat	  PCT012F170	best32. ;	
        informat	  PCT012F171	best32. ;	
        informat	  PCT012F172	best32. ;	
        informat	  PCT012F173	best32. ;	
        informat	  PCT012F174	best32. ;	
        informat	  PCT012F175	best32. ;	
        informat	  PCT012F176	best32. ;	
        informat	  PCT012F177	best32. ;	
        informat	  PCT012F178	best32. ;	
        informat	  PCT012F179	best32. ;	
        informat	  PCT012F180	best32. ;	
        informat	  PCT012F181	best32. ;	
        informat	  PCT012F182	best32. ;	
        informat	  PCT012F183	best32. ;	
        informat	  PCT012F184	best32. ;	
        informat	  PCT012F185	best32. ;	
        informat	  PCT012F186	best32. ;	
        informat	  PCT012F187	best32. ;	
        informat	  PCT012F188	best32. ;	
        informat	  PCT012F189	best32. ;	
        informat	  PCT012F190	best32. ;	
        informat	  PCT012F191	best32. ;	
        informat	  PCT012F192	best32. ;	
        informat	  PCT012F193	best32. ;	
        informat	  PCT012F194	best32. ;	
        informat	  PCT012F195	best32. ;	
        informat	  PCT012F196	best32. ;	
        informat	  PCT012F197	best32. ;	
        informat	  PCT012F198	best32. ;	
        informat	  PCT012F199	best32. ;	
        informat	  PCT012F200	best32. ;	
        informat	  PCT012F201	best32. ;	
        informat	  PCT012F202	best32. ;	
        informat	  PCT012F203	best32. ;	
        informat	  PCT012F204	best32. ;	
        informat	  PCT012F205	best32. ;	
        informat	  PCT012F206	best32. ;	
        informat	  PCT012F207	best32. ;	
        informat	  PCT012F208	best32. ;	
        informat	  PCT012F209	best32. ;	
        informat	  PCT012G001	best32. ;	
        informat	  PCT012G002	best32. ;	
        informat	  PCT012G003	best32. ;	
        informat	  PCT012G004	best32. ;	
        informat	  PCT012G005	best32. ;	
        informat	  PCT012G006	best32. ;	
        informat	  PCT012G007	best32. ;	
        informat	  PCT012G008	best32. ;	
        informat	  PCT012G009	best32. ;	
        informat	  PCT012G010	best32. ;	
        informat	  PCT012G011	best32. ;	
        informat	  PCT012G012	best32. ;	
        informat	  PCT012G013	best32. ;	
        informat	  PCT012G014	best32. ;	
        informat	  PCT012G015	best32. ;	
        informat	  PCT012G016	best32. ;	
        informat	  PCT012G017	best32. ;	
        informat	  PCT012G018	best32. ;	
        informat	  PCT012G019	best32. ;	
        informat	  PCT012G020	best32. ;	
        informat	  PCT012G021	best32. ;	
        informat	  PCT012G022	best32. ;	
        informat	  PCT012G023	best32. ;	
        informat	  PCT012G024	best32. ;	
        informat	  PCT012G025	best32. ;	
        informat	  PCT012G026	best32. ;	
        informat	  PCT012G027	best32. ;	
        informat	  PCT012G028	best32. ;	
        informat	  PCT012G029	best32. ;	
        informat	  PCT012G030	best32. ;	
        informat	  PCT012G031	best32. ;	
        informat	  PCT012G032	best32. ;	
        informat	  PCT012G033	best32. ;	
        informat	  PCT012G034	best32. ;	
        informat	  PCT012G035	best32. ;	
        informat	  PCT012G036	best32. ;	
        informat	  PCT012G037	best32. ;	
        informat	  PCT012G038	best32. ;	
        informat	  PCT012G039	best32. ;	
        informat	  PCT012G040	best32. ;	
        informat	  PCT012G041	best32. ;	
        informat	  PCT012G042	best32. ;	
        informat	  PCT012G043	best32. ;	
        informat	  PCT012G044	best32. ;	
        informat	  PCT012G045	best32. ;	
        informat	  PCT012G046	best32. ;	
        informat	  PCT012G047	best32. ;	
        informat	  PCT012G048	best32. ;	
        informat	  PCT012G049	best32. ;	
        informat	  PCT012G050	best32. ;	
        informat	  PCT012G051	best32. ;	
        informat	  PCT012G052	best32. ;	
        informat	  PCT012G053	best32. ;	
        informat	  PCT012G054	best32. ;	
        informat	  PCT012G055	best32. ;	
        informat	  PCT012G056	best32. ;	
        informat	  PCT012G057	best32. ;	
        informat	  PCT012G058	best32. ;	
        informat	  PCT012G059	best32. ;	
        informat	  PCT012G060	best32. ;	
        informat	  PCT012G061	best32. ;	
        informat	  PCT012G062	best32. ;	
        informat	  PCT012G063	best32. ;	
        informat	  PCT012G064	best32. ;	
        informat	  PCT012G065	best32. ;	
        informat	  PCT012G066	best32. ;	
        informat	  PCT012G067	best32. ;	
        informat	  PCT012G068	best32. ;	
        informat	  PCT012G069	best32. ;	
        informat	  PCT012G070	best32. ;	
        informat	  PCT012G071	best32. ;	
        informat	  PCT012G072	best32. ;	
        informat	  PCT012G073	best32. ;	
        informat	  PCT012G074	best32. ;	
        informat	  PCT012G075	best32. ;	
        informat	  PCT012G076	best32. ;	
        informat	  PCT012G077	best32. ;	
        informat	  PCT012G078	best32. ;	
        informat	  PCT012G079	best32. ;	
        informat	  PCT012G080	best32. ;	
        informat	  PCT012G081	best32. ;	
        informat	  PCT012G082	best32. ;	
        informat	  PCT012G083	best32. ;	
        informat	  PCT012G084	best32. ;	
        informat	  PCT012G085	best32. ;	
        informat	  PCT012G086	best32. ;	
        informat	  PCT012G087	best32. ;	
        informat	  PCT012G088	best32. ;	
        informat	  PCT012G089	best32. ;	
        informat	  PCT012G090	best32. ;	
        informat	  PCT012G091	best32. ;	
        informat	  PCT012G092	best32. ;	
        informat	  PCT012G093	best32. ;	
        informat	  PCT012G094	best32. ;	
        informat	  PCT012G095	best32. ;	
        informat	  PCT012G096	best32. ;	
        informat	  PCT012G097	best32. ;	
        informat	  PCT012G098	best32. ;	
        informat	  PCT012G099	best32. ;	
        informat	  PCT012G100	best32. ;	
        informat	  PCT012G101	best32. ;	
        informat	  PCT012G102	best32. ;	
        informat	  PCT012G103	best32. ;	
        informat	  PCT012G104	best32. ;	
        informat	  PCT012G105	best32. ;	
        informat	  PCT012G106	best32. ;	
        informat	  PCT012G107	best32. ;	
        informat	  PCT012G108	best32. ;	
        informat	  PCT012G109	best32. ;	
        informat	  PCT012G110	best32. ;	
        informat	  PCT012G111	best32. ;	
        informat	  PCT012G112	best32. ;	
        informat	  PCT012G113	best32. ;	
        informat	  PCT012G114	best32. ;	
        informat	  PCT012G115	best32. ;	
        informat	  PCT012G116	best32. ;	
        informat	  PCT012G117	best32. ;	
        informat	  PCT012G118	best32. ;	
        informat	  PCT012G119	best32. ;	
        informat	  PCT012G120	best32. ;	
        informat	  PCT012G121	best32. ;	
        informat	  PCT012G122	best32. ;	
        informat	  PCT012G123	best32. ;	
        informat	  PCT012G124	best32. ;	
        informat	  PCT012G125	best32. ;	
        informat	  PCT012G126	best32. ;	
        informat	  PCT012G127	best32. ;	
        informat	  PCT012G128	best32. ;	
        informat	  PCT012G129	best32. ;	
        informat	  PCT012G130	best32. ;	
        informat	  PCT012G131	best32. ;	
        informat	  PCT012G132	best32. ;	
        informat	  PCT012G133	best32. ;	
        informat	  PCT012G134	best32. ;	
        informat	  PCT012G135	best32. ;	
        informat	  PCT012G136	best32. ;	
        informat	  PCT012G137	best32. ;	
        informat	  PCT012G138	best32. ;	
        informat	  PCT012G139	best32. ;	
        informat	  PCT012G140	best32. ;	
        informat	  PCT012G141	best32. ;	
        informat	  PCT012G142	best32. ;	
        informat	  PCT012G143	best32. ;	
        informat	  PCT012G144	best32. ;	
        informat	  PCT012G145	best32. ;	
        informat	  PCT012G146	best32. ;	
        informat	  PCT012G147	best32. ;	
        informat	  PCT012G148	best32. ;	
        informat	  PCT012G149	best32. ;	
        informat	  PCT012G150	best32. ;	
        informat	  PCT012G151	best32. ;	
        informat	  PCT012G152	best32. ;	
        informat	  PCT012G153	best32. ;	
        informat	  PCT012G154	best32. ;	
        informat	  PCT012G155	best32. ;	
        informat	  PCT012G156	best32. ;	
        informat	  PCT012G157	best32. ;	
        informat	  PCT012G158	best32. ;	
        informat	  PCT012G159	best32. ;	
        informat	  PCT012G160	best32. ;	
        informat	  PCT012G161	best32. ;	
        informat	  PCT012G162	best32. ;	
        informat	  PCT012G163	best32. ;	
        informat	  PCT012G164	best32. ;	
        informat	  PCT012G165	best32. ;	
        informat	  PCT012G166	best32. ;	
        informat	  PCT012G167	best32. ;	
        informat	  PCT012G168	best32. ;	
        informat	  PCT012G169	best32. ;	
        informat	  PCT012G170	best32. ;	
        informat	  PCT012G171	best32. ;	
        informat	  PCT012G172	best32. ;	
        informat	  PCT012G173	best32. ;	
        informat	  PCT012G174	best32. ;	
        informat	  PCT012G175	best32. ;	
        informat	  PCT012G176	best32. ;	
        informat	  PCT012G177	best32. ;	
        informat	  PCT012G178	best32. ;	
        informat	  PCT012G179	best32. ;	
        informat	  PCT012G180	best32. ;	
        informat	  PCT012G181	best32. ;	
        informat	  PCT012G182	best32. ;	
        informat	  PCT012G183	best32. ;	
        informat	  PCT012G184	best32. ;	
        informat	  PCT012G185	best32. ;	
        informat	  PCT012G186	best32. ;	
        informat	  PCT012G187	best32. ;	
        informat	  PCT012G188	best32. ;	
        informat	  PCT012G189	best32. ;	
        informat	  PCT012G190	best32. ;	
        informat	  PCT012G191	best32. ;	
        informat	  PCT012G192	best32. ;	
        informat	  PCT012G193	best32. ;	
        informat	  PCT012G194	best32. ;	
        informat	  PCT012G195	best32. ;	
        informat	  PCT012G196	best32. ;	
        informat	  PCT012G197	best32. ;	
        informat	  PCT012G198	best32. ;	
        informat	  PCT012G199	best32. ;	
        informat	  PCT012G200	best32. ;	
        informat	  PCT012G201	best32. ;	
        informat	  PCT012G202	best32. ;	
        informat	  PCT012G203	best32. ;	
        informat	  PCT012G204	best32. ;	
        informat	  PCT012G205	best32. ;	
        informat	  PCT012G206	best32. ;	
        informat	  PCT012G207	best32. ;	
        informat	  PCT012G208	best32. ;	
        informat	  PCT012G209	best32. ;	
        informat	  PCT012H001	best32. ;	
        informat	  PCT012H002	best32. ;	
        informat	  PCT012H003	best32. ;	
        informat	  PCT012H004	best32. ;	
        informat	  PCT012H005	best32. ;	
        informat	  PCT012H006	best32. ;	
        informat	  PCT012H007	best32. ;	
        informat	  PCT012H008	best32. ;	
        informat	  PCT012H009	best32. ;	
        informat	  PCT012H010	best32. ;	
        informat	  PCT012H011	best32. ;	
        informat	  PCT012H012	best32. ;	
        informat	  PCT012H013	best32. ;	
        informat	  PCT012H014	best32. ;	
        informat	  PCT012H015	best32. ;	
        informat	  PCT012H016	best32. ;	
        informat	  PCT012H017	best32. ;	
        informat	  PCT012H018	best32. ;	
        informat	  PCT012H019	best32. ;	
        informat	  PCT012H020	best32. ;	
        informat	  PCT012H021	best32. ;	
        informat	  PCT012H022	best32. ;	
        informat	  PCT012H023	best32. ;	
        informat	  PCT012H024	best32. ;	
        informat	  PCT012H025	best32. ;	
        informat	  PCT012H026	best32. ;	
        informat	  PCT012H027	best32. ;	
        informat	  PCT012H028	best32. ;	
        informat	  PCT012H029	best32. ;	
        informat	  PCT012H030	best32. ;	
        informat	  PCT012H031	best32. ;	
        informat	  PCT012H032	best32. ;	
        informat	  PCT012H033	best32. ;	
        informat	  PCT012H034	best32. ;	
        informat	  PCT012H035	best32. ;	
        informat	  PCT012H036	best32. ;	
        informat	  PCT012H037	best32. ;	
        informat	  PCT012H038	best32. ;	
        informat	  PCT012H039	best32. ;	
        informat	  PCT012H040	best32. ;	
        informat	  PCT012H041	best32. ;	
        informat	  PCT012H042	best32. ;	
        informat	  PCT012H043	best32. ;	
        informat	  PCT012H044	best32. ;	
        informat	  PCT012H045	best32. ;	
        informat	  PCT012H046	best32. ;	
        informat	  PCT012H047	best32. ;	
        informat	  PCT012H048	best32. ;	
        informat	  PCT012H049	best32. ;	
        informat	  PCT012H050	best32. ;	
        informat	  PCT012H051	best32. ;	
        informat	  PCT012H052	best32. ;	
        informat	  PCT012H053	best32. ;	
        informat	  PCT012H054	best32. ;	
        informat	  PCT012H055	best32. ;	
        informat	  PCT012H056	best32. ;	
        informat	  PCT012H057	best32. ;	
        informat	  PCT012H058	best32. ;	
        informat	  PCT012H059	best32. ;	
        informat	  PCT012H060	best32. ;	
        informat	  PCT012H061	best32. ;	
        informat	  PCT012H062	best32. ;	
        informat	  PCT012H063	best32. ;	
        informat	  PCT012H064	best32. ;	
        informat	  PCT012H065	best32. ;	
        informat	  PCT012H066	best32. ;	
        informat	  PCT012H067	best32. ;	
        informat	  PCT012H068	best32. ;	
        informat	  PCT012H069	best32. ;	
        informat	  PCT012H070	best32. ;	
        informat	  PCT012H071	best32. ;	
        informat	  PCT012H072	best32. ;	
        informat	  PCT012H073	best32. ;	
        informat	  PCT012H074	best32. ;	
        informat	  PCT012H075	best32. ;	
        informat	  PCT012H076	best32. ;	
        informat	  PCT012H077	best32. ;	
        informat	  PCT012H078	best32. ;	
        informat	  PCT012H079	best32. ;	
        informat	  PCT012H080	best32. ;	
        informat	  PCT012H081	best32. ;	
        informat	  PCT012H082	best32. ;	
        informat	  PCT012H083	best32. ;	
        informat	  PCT012H084	best32. ;	
        informat	  PCT012H085	best32. ;	
        informat	  PCT012H086	best32. ;	
        informat	  PCT012H087	best32. ;	
        informat	  PCT012H088	best32. ;	
        informat	  PCT012H089	best32. ;	
        informat	  PCT012H090	best32. ;	
        informat	  PCT012H091	best32. ;	
        informat	  PCT012H092	best32. ;	
        informat	  PCT012H093	best32. ;	
        informat	  PCT012H094	best32. ;	
        informat	  PCT012H095	best32. ;	
        informat	  PCT012H096	best32. ;	
        informat	  PCT012H097	best32. ;	
        informat	  PCT012H098	best32. ;	
        informat	  PCT012H099	best32. ;	
        informat	  PCT012H100	best32. ;	
        informat	  PCT012H101	best32. ;	
        informat	  PCT012H102	best32. ;	
        informat	  PCT012H103	best32. ;	
        informat	  PCT012H104	best32. ;	
        informat	  PCT012H105	best32. ;	
        informat	  PCT012H106	best32. ;	
        informat	  PCT012H107	best32. ;	
        informat	  PCT012H108	best32. ;	
        informat	  PCT012H109	best32. ;	
        informat	  PCT012H110	best32. ;	
        informat	  PCT012H111	best32. ;	
        informat	  PCT012H112	best32. ;	
        informat	  PCT012H113	best32. ;	
        informat	  PCT012H114	best32. ;	
        informat	  PCT012H115	best32. ;	
        informat	  PCT012H116	best32. ;	
        informat	  PCT012H117	best32. ;	
        informat	  PCT012H118	best32. ;	
        informat	  PCT012H119	best32. ;	
        informat	  PCT012H120	best32. ;	
        informat	  PCT012H121	best32. ;	
        informat	  PCT012H122	best32. ;	
        informat	  PCT012H123	best32. ;	
        informat	  PCT012H124	best32. ;	
        informat	  PCT012H125	best32. ;	
        informat	  PCT012H126	best32. ;	
        informat	  PCT012H127	best32. ;	
        informat	  PCT012H128	best32. ;	
        informat	  PCT012H129	best32. ;	
        informat	  PCT012H130	best32. ;	
        informat	  PCT012H131	best32. ;	
        informat	  PCT012H132	best32. ;	
        informat	  PCT012H133	best32. ;	
        informat	  PCT012H134	best32. ;	
        informat	  PCT012H135	best32. ;	
        informat	  PCT012H136	best32. ;	
        informat	  PCT012H137	best32. ;	
        informat	  PCT012H138	best32. ;	
        informat	  PCT012H139	best32. ;	
        informat	  PCT012H140	best32. ;	
        informat	  PCT012H141	best32. ;	
        informat	  PCT012H142	best32. ;	
        informat	  PCT012H143	best32. ;	
        informat	  PCT012H144	best32. ;	
        informat	  PCT012H145	best32. ;	
        informat	  PCT012H146	best32. ;	
        informat	  PCT012H147	best32. ;	
        informat	  PCT012H148	best32. ;	
        informat	  PCT012H149	best32. ;	
        informat	  PCT012H150	best32. ;	
        informat	  PCT012H151	best32. ;	
        informat	  PCT012H152	best32. ;	
        informat	  PCT012H153	best32. ;	
        informat	  PCT012H154	best32. ;	
        informat	  PCT012H155	best32. ;	
        informat	  PCT012H156	best32. ;	
        informat	  PCT012H157	best32. ;	
        informat	  PCT012H158	best32. ;	
        informat	  PCT012H159	best32. ;	
        informat	  PCT012H160	best32. ;	
        informat	  PCT012H161	best32. ;	
        informat	  PCT012H162	best32. ;	
        informat	  PCT012H163	best32. ;	
        informat	  PCT012H164	best32. ;	
        informat	  PCT012H165	best32. ;	
        informat	  PCT012H166	best32. ;	
        informat	  PCT012H167	best32. ;	
        informat	  PCT012H168	best32. ;	
        informat	  PCT012H169	best32. ;	
        informat	  PCT012H170	best32. ;	
        informat	  PCT012H171	best32. ;	
        informat	  PCT012H172	best32. ;	
        informat	  PCT012H173	best32. ;	
        informat	  PCT012H174	best32. ;	
        informat	  PCT012H175	best32. ;	
        informat	  PCT012H176	best32. ;	
        informat	  PCT012H177	best32. ;	
        informat	  PCT012H178	best32. ;	
        informat	  PCT012H179	best32. ;	
        informat	  PCT012H180	best32. ;	
        informat	  PCT012H181	best32. ;	
        informat	  PCT012H182	best32. ;	
        informat	  PCT012H183	best32. ;	
        informat	  PCT012H184	best32. ;	
        informat	  PCT012H185	best32. ;	
        informat	  PCT012H186	best32. ;	
        informat	  PCT012H187	best32. ;	
        informat	  PCT012H188	best32. ;	
        informat	  PCT012H189	best32. ;	
        informat	  PCT012H190	best32. ;	
        informat	  PCT012H191	best32. ;	
        informat	  PCT012H192	best32. ;	
        informat	  PCT012H193	best32. ;	
        informat	  PCT012H194	best32. ;	
        informat	  PCT012H195	best32. ;	
        informat	  PCT012H196	best32. ;	
        informat	  PCT012H197	best32. ;	
        informat	  PCT012H198	best32. ;	
        informat	  PCT012H199	best32. ;	
        informat	  PCT012H200	best32. ;	
        informat	  PCT012H201	best32. ;	
        informat	  PCT012H202	best32. ;	
        informat	  PCT012H203	best32. ;	
        informat	  PCT012H204	best32. ;	
        informat	  PCT012H205	best32. ;	
        informat	  PCT012H206	best32. ;	
        informat	  PCT012H207	best32. ;	
        informat	  PCT012H208	best32. ;	
        informat	  PCT012H209	best32. ;	
        informat	  PCT012I001	best32. ;	
        informat	  PCT012I002	best32. ;	
        informat	  PCT012I003	best32. ;	
        informat	  PCT012I004	best32. ;	
        informat	  PCT012I005	best32. ;	
        informat	  PCT012I006	best32. ;	
        informat	  PCT012I007	best32. ;	
        informat	  PCT012I008	best32. ;	
        informat	  PCT012I009	best32. ;	
        informat	  PCT012I010	best32. ;	
        informat	  PCT012I011	best32. ;	
        informat	  PCT012I012	best32. ;	
        informat	  PCT012I013	best32. ;	
        informat	  PCT012I014	best32. ;	
        informat	  PCT012I015	best32. ;	
        informat	  PCT012I016	best32. ;	
        informat	  PCT012I017	best32. ;	
        informat	  PCT012I018	best32. ;	
        informat	  PCT012I019	best32. ;	
        informat	  PCT012I020	best32. ;	
        informat	  PCT012I021	best32. ;	
        informat	  PCT012I022	best32. ;	
        informat	  PCT012I023	best32. ;	
        informat	  PCT012I024	best32. ;	
        informat	  PCT012I025	best32. ;	
        informat	  PCT012I026	best32. ;	
        informat	  PCT012I027	best32. ;	
        informat	  PCT012I028	best32. ;	
        informat	  PCT012I029	best32. ;	
        informat	  PCT012I030	best32. ;	
        informat	  PCT012I031	best32. ;	
        informat	  PCT012I032	best32. ;	
        informat	  PCT012I033	best32. ;	
        informat	  PCT012I034	best32. ;	
        informat	  PCT012I035	best32. ;	
        informat	  PCT012I036	best32. ;	
        informat	  PCT012I037	best32. ;	
        informat	  PCT012I038	best32. ;	
        informat	  PCT012I039	best32. ;	
        informat	  PCT012I040	best32. ;	
        informat	  PCT012I041	best32. ;	
        informat	  PCT012I042	best32. ;	
        informat	  PCT012I043	best32. ;	
        informat	  PCT012I044	best32. ;	
        informat	  PCT012I045	best32. ;	
        informat	  PCT012I046	best32. ;	
        informat	  PCT012I047	best32. ;	
        informat	  PCT012I048	best32. ;	
        informat	  PCT012I049	best32. ;	
        informat	  PCT012I050	best32. ;	
        informat	  PCT012I051	best32. ;	
        informat	  PCT012I052	best32. ;	
        informat	  PCT012I053	best32. ;	
        informat	  PCT012I054	best32. ;	
        informat	  PCT012I055	best32. ;	
        informat	  PCT012I056	best32. ;	
        informat	  PCT012I057	best32. ;	
        informat	  PCT012I058	best32. ;	
        informat	  PCT012I059	best32. ;	
        informat	  PCT012I060	best32. ;	
        informat	  PCT012I061	best32. ;	
        informat	  PCT012I062	best32. ;	
        informat	  PCT012I063	best32. ;	
        informat	  PCT012I064	best32. ;	
        informat	  PCT012I065	best32. ;	
        informat	  PCT012I066	best32. ;	
        informat	  PCT012I067	best32. ;	
        informat	  PCT012I068	best32. ;	
        informat	  PCT012I069	best32. ;	
        informat	  PCT012I070	best32. ;	
        informat	  PCT012I071	best32. ;	
        informat	  PCT012I072	best32. ;	
        informat	  PCT012I073	best32. ;	
        informat	  PCT012I074	best32. ;	
        informat	  PCT012I075	best32. ;	
        informat	  PCT012I076	best32. ;	
        informat	  PCT012I077	best32. ;	
        informat	  PCT012I078	best32. ;	
        informat	  PCT012I079	best32. ;	
        informat	  PCT012I080	best32. ;	
        informat	  PCT012I081	best32. ;	
        informat	  PCT012I082	best32. ;	
        informat	  PCT012I083	best32. ;	
        informat	  PCT012I084	best32. ;	
        informat	  PCT012I085	best32. ;	
        informat	  PCT012I086	best32. ;	
        informat	  PCT012I087	best32. ;	
        informat	  PCT012I088	best32. ;	
        informat	  PCT012I089	best32. ;	
        informat	  PCT012I090	best32. ;	
        informat	  PCT012I091	best32. ;	
        informat	  PCT012I092	best32. ;	
        informat	  PCT012I093	best32. ;	
        informat	  PCT012I094	best32. ;	
        informat	  PCT012I095	best32. ;	
        informat	  PCT012I096	best32. ;	
        informat	  PCT012I097	best32. ;	
        informat	  PCT012I098	best32. ;	
        informat	  PCT012I099	best32. ;	
        informat	  PCT012I100	best32. ;	
        informat	  PCT012I101	best32. ;	
        informat	  PCT012I102	best32. ;	
        informat	  PCT012I103	best32. ;	
        informat	  PCT012I104	best32. ;	
        informat	  PCT012I105	best32. ;	
        informat	  PCT012I106	best32. ;	
        informat	  PCT012I107	best32. ;	
        informat	  PCT012I108	best32. ;	
        informat	  PCT012I109	best32. ;	
        informat	  PCT012I110	best32. ;	
        informat	  PCT012I111	best32. ;	
        informat	  PCT012I112	best32. ;	
        informat	  PCT012I113	best32. ;	
        informat	  PCT012I114	best32. ;	
        informat	  PCT012I115	best32. ;	
        informat	  PCT012I116	best32. ;	
        informat	  PCT012I117	best32. ;	
        informat	  PCT012I118	best32. ;	
        informat	  PCT012I119	best32. ;	
        informat	  PCT012I120	best32. ;	
        informat	  PCT012I121	best32. ;	
        informat	  PCT012I122	best32. ;	
        informat	  PCT012I123	best32. ;	
        informat	  PCT012I124	best32. ;	
        informat	  PCT012I125	best32. ;	
        informat	  PCT012I126	best32. ;	
        informat	  PCT012I127	best32. ;	
        informat	  PCT012I128	best32. ;	
        informat	  PCT012I129	best32. ;	
        informat	  PCT012I130	best32. ;	
        informat	  PCT012I131	best32. ;	
        informat	  PCT012I132	best32. ;	
        informat	  PCT012I133	best32. ;	
        informat	  PCT012I134	best32. ;	
        informat	  PCT012I135	best32. ;	
        informat	  PCT012I136	best32. ;	
        informat	  PCT012I137	best32. ;	
        informat	  PCT012I138	best32. ;	
        informat	  PCT012I139	best32. ;	
        informat	  PCT012I140	best32. ;	
        informat	  PCT012I141	best32. ;	
        informat	  PCT012I142	best32. ;	
        informat	  PCT012I143	best32. ;	
        informat	  PCT012I144	best32. ;	
        informat	  PCT012I145	best32. ;	
        informat	  PCT012I146	best32. ;	
        informat	  PCT012I147	best32. ;	
        informat	  PCT012I148	best32. ;	
        informat	  PCT012I149	best32. ;	
        informat	  PCT012I150	best32. ;	
        informat	  PCT012I151	best32. ;	
        informat	  PCT012I152	best32. ;	
        informat	  PCT012I153	best32. ;	
        informat	  PCT012I154	best32. ;	
        informat	  PCT012I155	best32. ;	
        informat	  PCT012I156	best32. ;	
        informat	  PCT012I157	best32. ;	
        informat	  PCT012I158	best32. ;	
        informat	  PCT012I159	best32. ;	
        informat	  PCT012I160	best32. ;	
        informat	  PCT012I161	best32. ;	
        informat	  PCT012I162	best32. ;	
        informat	  PCT012I163	best32. ;	
        informat	  PCT012I164	best32. ;	
        informat	  PCT012I165	best32. ;	
        informat	  PCT012I166	best32. ;	
        informat	  PCT012I167	best32. ;	
        informat	  PCT012I168	best32. ;	
        informat	  PCT012I169	best32. ;	
        informat	  PCT012I170	best32. ;	
        informat	  PCT012I171	best32. ;	
        informat	  PCT012I172	best32. ;	
        informat	  PCT012I173	best32. ;	
        informat	  PCT012I174	best32. ;	
        informat	  PCT012I175	best32. ;	
        informat	  PCT012I176	best32. ;	
        informat	  PCT012I177	best32. ;	
        informat	  PCT012I178	best32. ;	
        informat	  PCT012I179	best32. ;	
        informat	  PCT012I180	best32. ;	
        informat	  PCT012I181	best32. ;	
        informat	  PCT012I182	best32. ;	
        informat	  PCT012I183	best32. ;	
        informat	  PCT012I184	best32. ;	
        informat	  PCT012I185	best32. ;	
        informat	  PCT012I186	best32. ;	
        informat	  PCT012I187	best32. ;	
        informat	  PCT012I188	best32. ;	
        informat	  PCT012I189	best32. ;	
        informat	  PCT012I190	best32. ;	
        informat	  PCT012I191	best32. ;	
        informat	  PCT012I192	best32. ;	
        informat	  PCT012I193	best32. ;	
        informat	  PCT012I194	best32. ;	
        informat	  PCT012I195	best32. ;	
        informat	  PCT012I196	best32. ;	
        informat	  PCT012I197	best32. ;	
        informat	  PCT012I198	best32. ;	
        informat	  PCT012I199	best32. ;	
        informat	  PCT012I200	best32. ;	
        informat	  PCT012I201	best32. ;	
        informat	  PCT012I202	best32. ;	
        informat	  PCT012I203	best32. ;	
        informat	  PCT012I204	best32. ;	
        informat	  PCT012I205	best32. ;	
        informat	  PCT012I206	best32. ;	
        informat	  PCT012I207	best32. ;	
        informat	  PCT012I208	best32. ;	
        informat	  PCT012I209	best32. ;	
        informat	  PCT012J001	best32. ;	
        informat	  PCT012J002	best32. ;	
        informat	  PCT012J003	best32. ;	
        informat	  PCT012J004	best32. ;	
        informat	  PCT012J005	best32. ;	
        informat	  PCT012J006	best32. ;	
        informat	  PCT012J007	best32. ;	
        informat	  PCT012J008	best32. ;	
        informat	  PCT012J009	best32. ;	
        informat	  PCT012J010	best32. ;	
        informat	  PCT012J011	best32. ;	
        informat	  PCT012J012	best32. ;	
        informat	  PCT012J013	best32. ;	
        informat	  PCT012J014	best32. ;	
        informat	  PCT012J015	best32. ;	
        informat	  PCT012J016	best32. ;	
        informat	  PCT012J017	best32. ;	
        informat	  PCT012J018	best32. ;	
        informat	  PCT012J019	best32. ;	
        informat	  PCT012J020	best32. ;	
        informat	  PCT012J021	best32. ;	
        informat	  PCT012J022	best32. ;	
        informat	  PCT012J023	best32. ;	
        informat	  PCT012J024	best32. ;	
        informat	  PCT012J025	best32. ;	
        informat	  PCT012J026	best32. ;	
        informat	  PCT012J027	best32. ;	
        informat	  PCT012J028	best32. ;	
        informat	  PCT012J029	best32. ;	
        informat	  PCT012J030	best32. ;	
        informat	  PCT012J031	best32. ;	
        informat	  PCT012J032	best32. ;	
        informat	  PCT012J033	best32. ;	
        informat	  PCT012J034	best32. ;	
        informat	  PCT012J035	best32. ;	
        informat	  PCT012J036	best32. ;	
        informat	  PCT012J037	best32. ;	
        informat	  PCT012J038	best32. ;	
        informat	  PCT012J039	best32. ;	
        informat	  PCT012J040	best32. ;	
        informat	  PCT012J041	best32. ;	
        informat	  PCT012J042	best32. ;	
        informat	  PCT012J043	best32. ;	
        informat	  PCT012J044	best32. ;	
        informat	  PCT012J045	best32. ;	
        informat	  PCT012J046	best32. ;	
        informat	  PCT012J047	best32. ;	
        informat	  PCT012J048	best32. ;	
        informat	  PCT012J049	best32. ;	
        informat	  PCT012J050	best32. ;	
        informat	  PCT012J051	best32. ;	
        informat	  PCT012J052	best32. ;	
        informat	  PCT012J053	best32. ;	
        informat	  PCT012J054	best32. ;	
        informat	  PCT012J055	best32. ;	
        informat	  PCT012J056	best32. ;	
        informat	  PCT012J057	best32. ;	
        informat	  PCT012J058	best32. ;	
        informat	  PCT012J059	best32. ;	
        informat	  PCT012J060	best32. ;	
        informat	  PCT012J061	best32. ;	
        informat	  PCT012J062	best32. ;	
        informat	  PCT012J063	best32. ;	
        informat	  PCT012J064	best32. ;	
        informat	  PCT012J065	best32. ;	
        informat	  PCT012J066	best32. ;	
        informat	  PCT012J067	best32. ;	
        informat	  PCT012J068	best32. ;	
        informat	  PCT012J069	best32. ;	
        informat	  PCT012J070	best32. ;	
        informat	  PCT012J071	best32. ;	
        informat	  PCT012J072	best32. ;	
        informat	  PCT012J073	best32. ;	
        informat	  PCT012J074	best32. ;	
        informat	  PCT012J075	best32. ;	
        informat	  PCT012J076	best32. ;	
        informat	  PCT012J077	best32. ;	
        informat	  PCT012J078	best32. ;	
        informat	  PCT012J079	best32. ;	
        informat	  PCT012J080	best32. ;	
        informat	  PCT012J081	best32. ;	
        informat	  PCT012J082	best32. ;	
        informat	  PCT012J083	best32. ;	
        informat	  PCT012J084	best32. ;	
        informat	  PCT012J085	best32. ;	
        informat	  PCT012J086	best32. ;	
        informat	  PCT012J087	best32. ;	
        informat	  PCT012J088	best32. ;	
        informat	  PCT012J089	best32. ;	
        informat	  PCT012J090	best32. ;	
        informat	  PCT012J091	best32. ;	
        informat	  PCT012J092	best32. ;	
        informat	  PCT012J093	best32. ;	
        informat	  PCT012J094	best32. ;	
        informat	  PCT012J095	best32. ;	
        informat	  PCT012J096	best32. ;	
        informat	  PCT012J097	best32. ;	
        informat	  PCT012J098	best32. ;	
        informat	  PCT012J099	best32. ;	
        informat	  PCT012J100	best32. ;	
        informat	  PCT012J101	best32. ;	
        informat	  PCT012J102	best32. ;	
        informat	  PCT012J103	best32. ;	
        informat	  PCT012J104	best32. ;	
        informat	  PCT012J105	best32. ;	
        informat	  PCT012J106	best32. ;	
        informat	  PCT012J107	best32. ;	
        informat	  PCT012J108	best32. ;	
        informat	  PCT012J109	best32. ;	
        informat	  PCT012J110	best32. ;	
        informat	  PCT012J111	best32. ;	
        informat	  PCT012J112	best32. ;	
        informat	  PCT012J113	best32. ;	
        informat	  PCT012J114	best32. ;	
        informat	  PCT012J115	best32. ;	
        informat	  PCT012J116	best32. ;	
        informat	  PCT012J117	best32. ;	
        informat	  PCT012J118	best32. ;	
        informat	  PCT012J119	best32. ;	
        informat	  PCT012J120	best32. ;	
        informat	  PCT012J121	best32. ;	
        informat	  PCT012J122	best32. ;	
        informat	  PCT012J123	best32. ;	
        informat	  PCT012J124	best32. ;	
        informat	  PCT012J125	best32. ;	
        informat	  PCT012J126	best32. ;	
        informat	  PCT012J127	best32. ;	
        informat	  PCT012J128	best32. ;	
        informat	  PCT012J129	best32. ;	
        informat	  PCT012J130	best32. ;	
        informat	  PCT012J131	best32. ;	
        informat	  PCT012J132	best32. ;	
        informat	  PCT012J133	best32. ;	
        informat	  PCT012J134	best32. ;	
        informat	  PCT012J135	best32. ;	
        informat	  PCT012J136	best32. ;	
        informat	  PCT012J137	best32. ;	
        informat	  PCT012J138	best32. ;	
        informat	  PCT012J139	best32. ;	
        informat	  PCT012J140	best32. ;	
        informat	  PCT012J141	best32. ;	
        informat	  PCT012J142	best32. ;	
        informat	  PCT012J143	best32. ;	
        informat	  PCT012J144	best32. ;	
        informat	  PCT012J145	best32. ;	
        informat	  PCT012J146	best32. ;	
        informat	  PCT012J147	best32. ;	
        informat	  PCT012J148	best32. ;	
        informat	  PCT012J149	best32. ;	
        informat	  PCT012J150	best32. ;	
        informat	  PCT012J151	best32. ;	
        informat	  PCT012J152	best32. ;	
        informat	  PCT012J153	best32. ;	
        informat	  PCT012J154	best32. ;	
        informat	  PCT012J155	best32. ;	
        informat	  PCT012J156	best32. ;	
        informat	  PCT012J157	best32. ;	
        informat	  PCT012J158	best32. ;	
        informat	  PCT012J159	best32. ;	
        informat	  PCT012J160	best32. ;	
        informat	  PCT012J161	best32. ;	
        informat	  PCT012J162	best32. ;	
        informat	  PCT012J163	best32. ;	
        informat	  PCT012J164	best32. ;	
        informat	  PCT012J165	best32. ;	
        informat	  PCT012J166	best32. ;	
        informat	  PCT012J167	best32. ;	
        informat	  PCT012J168	best32. ;	
        informat	  PCT012J169	best32. ;	
        informat	  PCT012J170	best32. ;	
        informat	  PCT012J171	best32. ;	
        informat	  PCT012J172	best32. ;	
        informat	  PCT012J173	best32. ;	
        informat	  PCT012J174	best32. ;	
        informat	  PCT012J175	best32. ;	
        informat	  PCT012J176	best32. ;	
        informat	  PCT012J177	best32. ;	
        informat	  PCT012J178	best32. ;	
        informat	  PCT012J179	best32. ;	
        informat	  PCT012J180	best32. ;	
        informat	  PCT012J181	best32. ;	
        informat	  PCT012J182	best32. ;	
        informat	  PCT012J183	best32. ;	
        informat	  PCT012J184	best32. ;	
        informat	  PCT012J185	best32. ;	
        informat	  PCT012J186	best32. ;	
        informat	  PCT012J187	best32. ;	
        informat	  PCT012J188	best32. ;	
        informat	  PCT012J189	best32. ;	
        informat	  PCT012J190	best32. ;	
        informat	  PCT012J191	best32. ;	
        informat	  PCT012J192	best32. ;	
        informat	  PCT012J193	best32. ;	
        informat	  PCT012J194	best32. ;	
        informat	  PCT012J195	best32. ;	
        informat	  PCT012J196	best32. ;	
        informat	  PCT012J197	best32. ;	
        informat	  PCT012J198	best32. ;	
        informat	  PCT012J199	best32. ;	
        informat	  PCT012J200	best32. ;	
        informat	  PCT012J201	best32. ;	
        informat	  PCT012J202	best32. ;	
        informat	  PCT012J203	best32. ;	
        informat	  PCT012J204	best32. ;	
        informat	  PCT012J205	best32. ;	
        informat	  PCT012J206	best32. ;	
        informat	  PCT012J207	best32. ;	
        informat	  PCT012J208	best32. ;	
        informat	  PCT012J209	best32. ;	
        informat	  PCT012K001	best32. ;	
        informat	  PCT012K002	best32. ;	
        informat	  PCT012K003	best32. ;	
        informat	  PCT012K004	best32. ;	
        informat	  PCT012K005	best32. ;	
        informat	  PCT012K006	best32. ;	
        informat	  PCT012K007	best32. ;	
        informat	  PCT012K008	best32. ;	
        informat	  PCT012K009	best32. ;	
        informat	  PCT012K010	best32. ;	
        informat	  PCT012K011	best32. ;	
        informat	  PCT012K012	best32. ;	
        informat	  PCT012K013	best32. ;	
        informat	  PCT012K014	best32. ;	
        informat	  PCT012K015	best32. ;	
        informat	  PCT012K016	best32. ;	
        informat	  PCT012K017	best32. ;	
        informat	  PCT012K018	best32. ;	
        informat	  PCT012K019	best32. ;	
        informat	  PCT012K020	best32. ;	
        informat	  PCT012K021	best32. ;	
        informat	  PCT012K022	best32. ;	
        informat	  PCT012K023	best32. ;	
        informat	  PCT012K024	best32. ;	
        informat	  PCT012K025	best32. ;	
        informat	  PCT012K026	best32. ;	
        informat	  PCT012K027	best32. ;	
        informat	  PCT012K028	best32. ;	
        informat	  PCT012K029	best32. ;	
        informat	  PCT012K030	best32. ;	
        informat	  PCT012K031	best32. ;	
        informat	  PCT012K032	best32. ;	
        informat	  PCT012K033	best32. ;	
        informat	  PCT012K034	best32. ;	
        informat	  PCT012K035	best32. ;	
        informat	  PCT012K036	best32. ;	
        informat	  PCT012K037	best32. ;	
        informat	  PCT012K038	best32. ;	
        informat	  PCT012K039	best32. ;	
        informat	  PCT012K040	best32. ;	
        informat	  PCT012K041	best32. ;	
        informat	  PCT012K042	best32. ;	
        informat	  PCT012K043	best32. ;	
        informat	  PCT012K044	best32. ;	
        informat	  PCT012K045	best32. ;	
        informat	  PCT012K046	best32. ;	
        informat	  PCT012K047	best32. ;	
        informat	  PCT012K048	best32. ;	
        informat	  PCT012K049	best32. ;	
        informat	  PCT012K050	best32. ;	
        informat	  PCT012K051	best32. ;	
        informat	  PCT012K052	best32. ;	
        informat	  PCT012K053	best32. ;	
        informat	  PCT012K054	best32. ;	
        informat	  PCT012K055	best32. ;	
        informat	  PCT012K056	best32. ;	
        informat	  PCT012K057	best32. ;	
        informat	  PCT012K058	best32. ;	
        informat	  PCT012K059	best32. ;	
        informat	  PCT012K060	best32. ;	
        informat	  PCT012K061	best32. ;	
        informat	  PCT012K062	best32. ;	
        informat	  PCT012K063	best32. ;	
        informat	  PCT012K064	best32. ;	
        informat	  PCT012K065	best32. ;	
        informat	  PCT012K066	best32. ;	
        informat	  PCT012K067	best32. ;	
        informat	  PCT012K068	best32. ;	
        informat	  PCT012K069	best32. ;	
        informat	  PCT012K070	best32. ;	
        informat	  PCT012K071	best32. ;	
        informat	  PCT012K072	best32. ;	
        informat	  PCT012K073	best32. ;	
        informat	  PCT012K074	best32. ;	
        informat	  PCT012K075	best32. ;	
        informat	  PCT012K076	best32. ;	
        informat	  PCT012K077	best32. ;	
        informat	  PCT012K078	best32. ;	
        informat	  PCT012K079	best32. ;	
        informat	  PCT012K080	best32. ;	
        informat	  PCT012K081	best32. ;	
        informat	  PCT012K082	best32. ;	
        informat	  PCT012K083	best32. ;	
        informat	  PCT012K084	best32. ;	
        informat	  PCT012K085	best32. ;	
        informat	  PCT012K086	best32. ;	
        informat	  PCT012K087	best32. ;	
        informat	  PCT012K088	best32. ;	
        informat	  PCT012K089	best32. ;	
        informat	  PCT012K090	best32. ;	
        informat	  PCT012K091	best32. ;	
        informat	  PCT012K092	best32. ;	
        informat	  PCT012K093	best32. ;	
        informat	  PCT012K094	best32. ;	
        informat	  PCT012K095	best32. ;	
        informat	  PCT012K096	best32. ;	
        informat	  PCT012K097	best32. ;	
        informat	  PCT012K098	best32. ;	
        informat	  PCT012K099	best32. ;	
        informat	  PCT012K100	best32. ;	
        informat	  PCT012K101	best32. ;	
        informat	  PCT012K102	best32. ;	
        informat	  PCT012K103	best32. ;	
        informat	  PCT012K104	best32. ;	
        informat	  PCT012K105	best32. ;	
        informat	  PCT012K106	best32. ;	
        informat	  PCT012K107	best32. ;	
        informat	  PCT012K108	best32. ;	
        informat	  PCT012K109	best32. ;	
        informat	  PCT012K110	best32. ;	
        informat	  PCT012K111	best32. ;	
        informat	  PCT012K112	best32. ;	
        informat	  PCT012K113	best32. ;	
        informat	  PCT012K114	best32. ;	
        informat	  PCT012K115	best32. ;	
        informat	  PCT012K116	best32. ;	
        informat	  PCT012K117	best32. ;	
        informat	  PCT012K118	best32. ;	
        informat	  PCT012K119	best32. ;	
        informat	  PCT012K120	best32. ;	
        informat	  PCT012K121	best32. ;	
        informat	  PCT012K122	best32. ;	
        informat	  PCT012K123	best32. ;	
        informat	  PCT012K124	best32. ;	
        informat	  PCT012K125	best32. ;	
        informat	  PCT012K126	best32. ;	
        informat	  PCT012K127	best32. ;	
        informat	  PCT012K128	best32. ;	
        informat	  PCT012K129	best32. ;	
        informat	  PCT012K130	best32. ;	
        informat	  PCT012K131	best32. ;	
        informat	  PCT012K132	best32. ;	
        informat	  PCT012K133	best32. ;	
        informat	  PCT012K134	best32. ;	
        informat	  PCT012K135	best32. ;	
        informat	  PCT012K136	best32. ;	
        informat	  PCT012K137	best32. ;	
        informat	  PCT012K138	best32. ;	
        informat	  PCT012K139	best32. ;	
        informat	  PCT012K140	best32. ;	
        informat	  PCT012K141	best32. ;	
        informat	  PCT012K142	best32. ;	
        informat	  PCT012K143	best32. ;	
        informat	  PCT012K144	best32. ;	
        informat	  PCT012K145	best32. ;	
        informat	  PCT012K146	best32. ;	
        informat	  PCT012K147	best32. ;	
        informat	  PCT012K148	best32. ;	
        informat	  PCT012K149	best32. ;	
        informat	  PCT012K150	best32. ;	
        informat	  PCT012K151	best32. ;	
        informat	  PCT012K152	best32. ;	
        informat	  PCT012K153	best32. ;	
        informat	  PCT012K154	best32. ;	
        informat	  PCT012K155	best32. ;	
        informat	  PCT012K156	best32. ;	
        informat	  PCT012K157	best32. ;	
        informat	  PCT012K158	best32. ;	
        informat	  PCT012K159	best32. ;	
        informat	  PCT012K160	best32. ;	
        informat	  PCT012K161	best32. ;	
        informat	  PCT012K162	best32. ;	
        informat	  PCT012K163	best32. ;	
        informat	  PCT012K164	best32. ;	
        informat	  PCT012K165	best32. ;	
        informat	  PCT012K166	best32. ;	
        informat	  PCT012K167	best32. ;	
        informat	  PCT012K168	best32. ;	
        informat	  PCT012K169	best32. ;	
        informat	  PCT012K170	best32. ;	
        informat	  PCT012K171	best32. ;	
        informat	  PCT012K172	best32. ;	
        informat	  PCT012K173	best32. ;	
        informat	  PCT012K174	best32. ;	
        informat	  PCT012K175	best32. ;	
        informat	  PCT012K176	best32. ;	
        informat	  PCT012K177	best32. ;	
        informat	  PCT012K178	best32. ;	
        informat	  PCT012K179	best32. ;	
        informat	  PCT012K180	best32. ;	
        informat	  PCT012K181	best32. ;	
        informat	  PCT012K182	best32. ;	
        informat	  PCT012K183	best32. ;	
        informat	  PCT012K184	best32. ;	
        informat	  PCT012K185	best32. ;	
        informat	  PCT012K186	best32. ;	
        informat	  PCT012K187	best32. ;	
        informat	  PCT012K188	best32. ;	
        informat	  PCT012K189	best32. ;	
        informat	  PCT012K190	best32. ;	
        informat	  PCT012K191	best32. ;	
        informat	  PCT012K192	best32. ;	
        informat	  PCT012K193	best32. ;	
        informat	  PCT012K194	best32. ;	
        informat	  PCT012K195	best32. ;	
        informat	  PCT012K196	best32. ;	
        informat	  PCT012K197	best32. ;	
        informat	  PCT012K198	best32. ;	
        informat	  PCT012K199	best32. ;	
        informat	  PCT012K200	best32. ;	
        informat	  PCT012K201	best32. ;	
        informat	  PCT012K202	best32. ;	
        informat	  PCT012K203	best32. ;	
        informat	  PCT012K204	best32. ;	
        informat	  PCT012K205	best32. ;	
        informat	  PCT012K206	best32. ;	
        informat	  PCT012K207	best32. ;	
        informat	  PCT012K208	best32. ;	
        informat	  PCT012K209	best32. ;	
        informat	  PCT012L001	best32. ;	
        informat	  PCT012L002	best32. ;	
        informat	  PCT012L003	best32. ;	
        informat	  PCT012L004	best32. ;	
        informat	  PCT012L005	best32. ;	
        informat	  PCT012L006	best32. ;	
        informat	  PCT012L007	best32. ;	
        informat	  PCT012L008	best32. ;	
        informat	  PCT012L009	best32. ;	
        informat	  PCT012L010	best32. ;	
        informat	  PCT012L011	best32. ;	
        informat	  PCT012L012	best32. ;	
        informat	  PCT012L013	best32. ;	
        informat	  PCT012L014	best32. ;	
        informat	  PCT012L015	best32. ;	
        informat	  PCT012L016	best32. ;	
        informat	  PCT012L017	best32. ;	
        informat	  PCT012L018	best32. ;	
        informat	  PCT012L019	best32. ;	
        informat	  PCT012L020	best32. ;	
        informat	  PCT012L021	best32. ;	
        informat	  PCT012L022	best32. ;	
        informat	  PCT012L023	best32. ;	
        informat	  PCT012L024	best32. ;	
        informat	  PCT012L025	best32. ;	
        informat	  PCT012L026	best32. ;	
        informat	  PCT012L027	best32. ;	
        informat	  PCT012L028	best32. ;	
        informat	  PCT012L029	best32. ;	
        informat	  PCT012L030	best32. ;	
        informat	  PCT012L031	best32. ;	
        informat	  PCT012L032	best32. ;	
        informat	  PCT012L033	best32. ;	
        informat	  PCT012L034	best32. ;	
        informat	  PCT012L035	best32. ;	
        informat	  PCT012L036	best32. ;	
        informat	  PCT012L037	best32. ;	
        informat	  PCT012L038	best32. ;	
        informat	  PCT012L039	best32. ;	
        informat	  PCT012L040	best32. ;	
        informat	  PCT012L041	best32. ;	
        informat	  PCT012L042	best32. ;	
        informat	  PCT012L043	best32. ;	
        informat	  PCT012L044	best32. ;	
        informat	  PCT012L045	best32. ;	
        informat	  PCT012L046	best32. ;	
        informat	  PCT012L047	best32. ;	
        informat	  PCT012L048	best32. ;	
        informat	  PCT012L049	best32. ;	
        informat	  PCT012L050	best32. ;	
        informat	  PCT012L051	best32. ;	
        informat	  PCT012L052	best32. ;	
        informat	  PCT012L053	best32. ;	
        informat	  PCT012L054	best32. ;	
        informat	  PCT012L055	best32. ;	
        informat	  PCT012L056	best32. ;	
        informat	  PCT012L057	best32. ;	
        informat	  PCT012L058	best32. ;	
        informat	  PCT012L059	best32. ;	
        informat	  PCT012L060	best32. ;	
        informat	  PCT012L061	best32. ;	
        informat	  PCT012L062	best32. ;	
        informat	  PCT012L063	best32. ;	
        informat	  PCT012L064	best32. ;	
        informat	  PCT012L065	best32. ;	
        informat	  PCT012L066	best32. ;	
        informat	  PCT012L067	best32. ;	
        informat	  PCT012L068	best32. ;	
        informat	  PCT012L069	best32. ;	
        informat	  PCT012L070	best32. ;	
        informat	  PCT012L071	best32. ;	
        informat	  PCT012L072	best32. ;	
        informat	  PCT012L073	best32. ;	
        informat	  PCT012L074	best32. ;	
        informat	  PCT012L075	best32. ;	
        informat	  PCT012L076	best32. ;	
        informat	  PCT012L077	best32. ;	
        informat	  PCT012L078	best32. ;	
        informat	  PCT012L079	best32. ;	
        informat	  PCT012L080	best32. ;	
        informat	  PCT012L081	best32. ;	
        informat	  PCT012L082	best32. ;	
        informat	  PCT012L083	best32. ;	
        informat	  PCT012L084	best32. ;	
        informat	  PCT012L085	best32. ;	
        informat	  PCT012L086	best32. ;	
        informat	  PCT012L087	best32. ;	
        informat	  PCT012L088	best32. ;	
        informat	  PCT012L089	best32. ;	
        informat	  PCT012L090	best32. ;	
        informat	  PCT012L091	best32. ;	
        informat	  PCT012L092	best32. ;	
        informat	  PCT012L093	best32. ;	
        informat	  PCT012L094	best32. ;	
        informat	  PCT012L095	best32. ;	
        informat	  PCT012L096	best32. ;	
        informat	  PCT012L097	best32. ;	
        informat	  PCT012L098	best32. ;	
        informat	  PCT012L099	best32. ;	
        informat	  PCT012L100	best32. ;	
        informat	  PCT012L101	best32. ;	
        informat	  PCT012L102	best32. ;	
        informat	  PCT012L103	best32. ;	
        informat	  PCT012L104	best32. ;	
        informat	  PCT012L105	best32. ;	
        informat	  PCT012L106	best32. ;	
        informat	  PCT012L107	best32. ;	
        informat	  PCT012L108	best32. ;	
        informat	  PCT012L109	best32. ;	
        informat	  PCT012L110	best32. ;	
        informat	  PCT012L111	best32. ;	
        informat	  PCT012L112	best32. ;	
        informat	  PCT012L113	best32. ;	
        informat	  PCT012L114	best32. ;	
        informat	  PCT012L115	best32. ;	
        informat	  PCT012L116	best32. ;	
        informat	  PCT012L117	best32. ;	
        informat	  PCT012L118	best32. ;	
        informat	  PCT012L119	best32. ;	
        informat	  PCT012L120	best32. ;	
        informat	  PCT012L121	best32. ;	
        informat	  PCT012L122	best32. ;	
        informat	  PCT012L123	best32. ;	
        informat	  PCT012L124	best32. ;	
        informat	  PCT012L125	best32. ;	
        informat	  PCT012L126	best32. ;	
        informat	  PCT012L127	best32. ;	
        informat	  PCT012L128	best32. ;	
        informat	  PCT012L129	best32. ;	
        informat	  PCT012L130	best32. ;	
        informat	  PCT012L131	best32. ;	
        informat	  PCT012L132	best32. ;	
        informat	  PCT012L133	best32. ;	
        informat	  PCT012L134	best32. ;	
        informat	  PCT012L135	best32. ;	
        informat	  PCT012L136	best32. ;	
        informat	  PCT012L137	best32. ;	
        informat	  PCT012L138	best32. ;	
        informat	  PCT012L139	best32. ;	
        informat	  PCT012L140	best32. ;	
        informat	  PCT012L141	best32. ;	
        informat	  PCT012L142	best32. ;	
        informat	  PCT012L143	best32. ;	
        informat	  PCT012L144	best32. ;	
        informat	  PCT012L145	best32. ;	
        informat	  PCT012L146	best32. ;	
        informat	  PCT012L147	best32. ;	
        informat	  PCT012L148	best32. ;	
        informat	  PCT012L149	best32. ;	
        informat	  PCT012L150	best32. ;	
        informat	  PCT012L151	best32. ;	
        informat	  PCT012L152	best32. ;	
        informat	  PCT012L153	best32. ;	
        informat	  PCT012L154	best32. ;	
        informat	  PCT012L155	best32. ;	
        informat	  PCT012L156	best32. ;	
        informat	  PCT012L157	best32. ;	
        informat	  PCT012L158	best32. ;	
        informat	  PCT012L159	best32. ;	
        informat	  PCT012L160	best32. ;	
        informat	  PCT012L161	best32. ;	
        informat	  PCT012L162	best32. ;	
        informat	  PCT012L163	best32. ;	
        informat	  PCT012L164	best32. ;	
        informat	  PCT012L165	best32. ;	
        informat	  PCT012L166	best32. ;	
        informat	  PCT012L167	best32. ;	
        informat	  PCT012L168	best32. ;	
        informat	  PCT012L169	best32. ;	
        informat	  PCT012L170	best32. ;	
        informat	  PCT012L171	best32. ;	
        informat	  PCT012L172	best32. ;	
        informat	  PCT012L173	best32. ;	
        informat	  PCT012L174	best32. ;	
        informat	  PCT012L175	best32. ;	
        informat	  PCT012L176	best32. ;	
        informat	  PCT012L177	best32. ;	
        informat	  PCT012L178	best32. ;	
        informat	  PCT012L179	best32. ;	
        informat	  PCT012L180	best32. ;	
        informat	  PCT012L181	best32. ;	
        informat	  PCT012L182	best32. ;	
        informat	  PCT012L183	best32. ;	
        informat	  PCT012L184	best32. ;	
        informat	  PCT012L185	best32. ;	
        informat	  PCT012L186	best32. ;	
        informat	  PCT012L187	best32. ;	
        informat	  PCT012L188	best32. ;	
        informat	  PCT012L189	best32. ;	
        informat	  PCT012L190	best32. ;	
        informat	  PCT012L191	best32. ;	
        informat	  PCT012L192	best32. ;	
        informat	  PCT012L193	best32. ;	
        informat	  PCT012L194	best32. ;	
        informat	  PCT012L195	best32. ;	
        informat	  PCT012L196	best32. ;	
        informat	  PCT012L197	best32. ;	
        informat	  PCT012L198	best32. ;	
        informat	  PCT012L199	best32. ;	
        informat	  PCT012L200	best32. ;	
        informat	  PCT012L201	best32. ;	
        informat	  PCT012L202	best32. ;	
        informat	  PCT012L203	best32. ;	
        informat	  PCT012L204	best32. ;	
        informat	  PCT012L205	best32. ;	
        informat	  PCT012L206	best32. ;	
        informat	  PCT012L207	best32. ;	
        informat	  PCT012L208	best32. ;	
        informat	  PCT012L209	best32. ;	
        informat	  PCT012M001	best32. ;	
        informat	  PCT012M002	best32. ;	
        informat	  PCT012M003	best32. ;	
        informat	  PCT012M004	best32. ;	
        informat	  PCT012M005	best32. ;	
        informat	  PCT012M006	best32. ;	
        informat	  PCT012M007	best32. ;	
        informat	  PCT012M008	best32. ;	
        informat	  PCT012M009	best32. ;	
        informat	  PCT012M010	best32. ;	
        informat	  PCT012M011	best32. ;	
        informat	  PCT012M012	best32. ;	
        informat	  PCT012M013	best32. ;	
        informat	  PCT012M014	best32. ;	
        informat	  PCT012M015	best32. ;	
        informat	  PCT012M016	best32. ;	
        informat	  PCT012M017	best32. ;	
        informat	  PCT012M018	best32. ;	
        informat	  PCT012M019	best32. ;	
        informat	  PCT012M020	best32. ;	
        informat	  PCT012M021	best32. ;	
        informat	  PCT012M022	best32. ;	
        informat	  PCT012M023	best32. ;	
        informat	  PCT012M024	best32. ;	
        informat	  PCT012M025	best32. ;	
        informat	  PCT012M026	best32. ;	
        informat	  PCT012M027	best32. ;	
        informat	  PCT012M028	best32. ;	
        informat	  PCT012M029	best32. ;	
        informat	  PCT012M030	best32. ;	
        informat	  PCT012M031	best32. ;	
        informat	  PCT012M032	best32. ;	
        informat	  PCT012M033	best32. ;	
        informat	  PCT012M034	best32. ;	
        informat	  PCT012M035	best32. ;	
        informat	  PCT012M036	best32. ;	
        informat	  PCT012M037	best32. ;	
        informat	  PCT012M038	best32. ;	
        informat	  PCT012M039	best32. ;	
        informat	  PCT012M040	best32. ;	
        informat	  PCT012M041	best32. ;	
        informat	  PCT012M042	best32. ;	
        informat	  PCT012M043	best32. ;	
        informat	  PCT012M044	best32. ;	
        informat	  PCT012M045	best32. ;	
        informat	  PCT012M046	best32. ;	
        informat	  PCT012M047	best32. ;	
        informat	  PCT012M048	best32. ;	
        informat	  PCT012M049	best32. ;	
        informat	  PCT012M050	best32. ;	
        informat	  PCT012M051	best32. ;	
        informat	  PCT012M052	best32. ;	
        informat	  PCT012M053	best32. ;	
        informat	  PCT012M054	best32. ;	
        informat	  PCT012M055	best32. ;	
        informat	  PCT012M056	best32. ;	
        informat	  PCT012M057	best32. ;	
        informat	  PCT012M058	best32. ;	
        informat	  PCT012M059	best32. ;	
        informat	  PCT012M060	best32. ;	
        informat	  PCT012M061	best32. ;	
        informat	  PCT012M062	best32. ;	
        informat	  PCT012M063	best32. ;	
        informat	  PCT012M064	best32. ;	
        informat	  PCT012M065	best32. ;	
        informat	  PCT012M066	best32. ;	
        informat	  PCT012M067	best32. ;	
        informat	  PCT012M068	best32. ;	
        informat	  PCT012M069	best32. ;	
        informat	  PCT012M070	best32. ;	
        informat	  PCT012M071	best32. ;	
        informat	  PCT012M072	best32. ;	
        informat	  PCT012M073	best32. ;	
        informat	  PCT012M074	best32. ;	
        informat	  PCT012M075	best32. ;	
        informat	  PCT012M076	best32. ;	
        informat	  PCT012M077	best32. ;	
        informat	  PCT012M078	best32. ;	
        informat	  PCT012M079	best32. ;	
        informat	  PCT012M080	best32. ;	
        informat	  PCT012M081	best32. ;	
        informat	  PCT012M082	best32. ;	
        informat	  PCT012M083	best32. ;	
        informat	  PCT012M084	best32. ;	
        informat	  PCT012M085	best32. ;	
        informat	  PCT012M086	best32. ;	
        informat	  PCT012M087	best32. ;	
        informat	  PCT012M088	best32. ;	
        informat	  PCT012M089	best32. ;	
        informat	  PCT012M090	best32. ;	
        informat	  PCT012M091	best32. ;	
        informat	  PCT012M092	best32. ;	
        informat	  PCT012M093	best32. ;	
        informat	  PCT012M094	best32. ;	
        informat	  PCT012M095	best32. ;	
        informat	  PCT012M096	best32. ;	
        informat	  PCT012M097	best32. ;	
        informat	  PCT012M098	best32. ;	
        informat	  PCT012M099	best32. ;	
        informat	  PCT012M100	best32. ;	
        informat	  PCT012M101	best32. ;	
        informat	  PCT012M102	best32. ;	
        informat	  PCT012M103	best32. ;	
        informat	  PCT012M104	best32. ;	
        informat	  PCT012M105	best32. ;	
        informat	  PCT012M106	best32. ;	
        informat	  PCT012M107	best32. ;	
        informat	  PCT012M108	best32. ;	
        informat	  PCT012M109	best32. ;	
        informat	  PCT012M110	best32. ;	
        informat	  PCT012M111	best32. ;	
        informat	  PCT012M112	best32. ;	
        informat	  PCT012M113	best32. ;	
        informat	  PCT012M114	best32. ;	
        informat	  PCT012M115	best32. ;	
        informat	  PCT012M116	best32. ;	
        informat	  PCT012M117	best32. ;	
        informat	  PCT012M118	best32. ;	
        informat	  PCT012M119	best32. ;	
        informat	  PCT012M120	best32. ;	
        informat	  PCT012M121	best32. ;	
        informat	  PCT012M122	best32. ;	
        informat	  PCT012M123	best32. ;	
        informat	  PCT012M124	best32. ;	
        informat	  PCT012M125	best32. ;	
        informat	  PCT012M126	best32. ;	
        informat	  PCT012M127	best32. ;	
        informat	  PCT012M128	best32. ;	
        informat	  PCT012M129	best32. ;	
        informat	  PCT012M130	best32. ;	
        informat	  PCT012M131	best32. ;	
        informat	  PCT012M132	best32. ;	
        informat	  PCT012M133	best32. ;	
        informat	  PCT012M134	best32. ;	
        informat	  PCT012M135	best32. ;	
        informat	  PCT012M136	best32. ;	
        informat	  PCT012M137	best32. ;	
        informat	  PCT012M138	best32. ;	
        informat	  PCT012M139	best32. ;	
        informat	  PCT012M140	best32. ;	
        informat	  PCT012M141	best32. ;	
        informat	  PCT012M142	best32. ;	
        informat	  PCT012M143	best32. ;	
        informat	  PCT012M144	best32. ;	
        informat	  PCT012M145	best32. ;	
        informat	  PCT012M146	best32. ;	
        informat	  PCT012M147	best32. ;	
        informat	  PCT012M148	best32. ;	
        informat	  PCT012M149	best32. ;	
        informat	  PCT012M150	best32. ;	
        informat	  PCT012M151	best32. ;	
        informat	  PCT012M152	best32. ;	
        informat	  PCT012M153	best32. ;	
        informat	  PCT012M154	best32. ;	
        informat	  PCT012M155	best32. ;	
        informat	  PCT012M156	best32. ;	
        informat	  PCT012M157	best32. ;	
        informat	  PCT012M158	best32. ;	
        informat	  PCT012M159	best32. ;	
        informat	  PCT012M160	best32. ;	
        informat	  PCT012M161	best32. ;	
        informat	  PCT012M162	best32. ;	
        informat	  PCT012M163	best32. ;	
        informat	  PCT012M164	best32. ;	
        informat	  PCT012M165	best32. ;	
        informat	  PCT012M166	best32. ;	
        informat	  PCT012M167	best32. ;	
        informat	  PCT012M168	best32. ;	
        informat	  PCT012M169	best32. ;	
        informat	  PCT012M170	best32. ;	
        informat	  PCT012M171	best32. ;	
        informat	  PCT012M172	best32. ;	
        informat	  PCT012M173	best32. ;	
        informat	  PCT012M174	best32. ;	
        informat	  PCT012M175	best32. ;	
        informat	  PCT012M176	best32. ;	
        informat	  PCT012M177	best32. ;	
        informat	  PCT012M178	best32. ;	
        informat	  PCT012M179	best32. ;	
        informat	  PCT012M180	best32. ;	
        informat	  PCT012M181	best32. ;	
        informat	  PCT012M182	best32. ;	
        informat	  PCT012M183	best32. ;	
        informat	  PCT012M184	best32. ;	
        informat	  PCT012M185	best32. ;	
        informat	  PCT012M186	best32. ;	
        informat	  PCT012M187	best32. ;	
        informat	  PCT012M188	best32. ;	
        informat	  PCT012M189	best32. ;	
        informat	  PCT012M190	best32. ;	
        informat	  PCT012M191	best32. ;	
        informat	  PCT012M192	best32. ;	
        informat	  PCT012M193	best32. ;	
        informat	  PCT012M194	best32. ;	
        informat	  PCT012M195	best32. ;	
        informat	  PCT012M196	best32. ;	
        informat	  PCT012M197	best32. ;	
        informat	  PCT012M198	best32. ;	
        informat	  PCT012M199	best32. ;	
        informat	  PCT012M200	best32. ;	
        informat	  PCT012M201	best32. ;	
        informat	  PCT012M202	best32. ;	
        informat	  PCT012M203	best32. ;	
        informat	  PCT012M204	best32. ;	
        informat	  PCT012M205	best32. ;	
        informat	  PCT012M206	best32. ;	
        informat	  PCT012M207	best32. ;	
        informat	  PCT012M208	best32. ;	
        informat	  PCT012M209	best32. ;	
        informat	  PCT012N001	best32. ;	
        informat	  PCT012N002	best32. ;	
        informat	  PCT012N003	best32. ;	
        informat	  PCT012N004	best32. ;	
        informat	  PCT012N005	best32. ;	
        informat	  PCT012N006	best32. ;	
        informat	  PCT012N007	best32. ;	
        informat	  PCT012N008	best32. ;	
        informat	  PCT012N009	best32. ;	
        informat	  PCT012N010	best32. ;	
        informat	  PCT012N011	best32. ;	
        informat	  PCT012N012	best32. ;	
        informat	  PCT012N013	best32. ;	
        informat	  PCT012N014	best32. ;	
        informat	  PCT012N015	best32. ;	
        informat	  PCT012N016	best32. ;	
        informat	  PCT012N017	best32. ;	
        informat	  PCT012N018	best32. ;	
        informat	  PCT012N019	best32. ;	
        informat	  PCT012N020	best32. ;	
        informat	  PCT012N021	best32. ;	
        informat	  PCT012N022	best32. ;	
        informat	  PCT012N023	best32. ;	
        informat	  PCT012N024	best32. ;	
        informat	  PCT012N025	best32. ;	
        informat	  PCT012N026	best32. ;	
        informat	  PCT012N027	best32. ;	
        informat	  PCT012N028	best32. ;	
        informat	  PCT012N029	best32. ;	
        informat	  PCT012N030	best32. ;	
        informat	  PCT012N031	best32. ;	
        informat	  PCT012N032	best32. ;	
        informat	  PCT012N033	best32. ;	
        informat	  PCT012N034	best32. ;	
        informat	  PCT012N035	best32. ;	
        informat	  PCT012N036	best32. ;	
        informat	  PCT012N037	best32. ;	
        informat	  PCT012N038	best32. ;	
        informat	  PCT012N039	best32. ;	
        informat	  PCT012N040	best32. ;	
        informat	  PCT012N041	best32. ;	
        informat	  PCT012N042	best32. ;	
        informat	  PCT012N043	best32. ;	
        informat	  PCT012N044	best32. ;	
        informat	  PCT012N045	best32. ;	
        informat	  PCT012N046	best32. ;	
        informat	  PCT012N047	best32. ;	
        informat	  PCT012N048	best32. ;	
        informat	  PCT012N049	best32. ;	
        informat	  PCT012N050	best32. ;	
        informat	  PCT012N051	best32. ;	
        informat	  PCT012N052	best32. ;	
        informat	  PCT012N053	best32. ;	
        informat	  PCT012N054	best32. ;	
        informat	  PCT012N055	best32. ;	
        informat	  PCT012N056	best32. ;	
        informat	  PCT012N057	best32. ;	
        informat	  PCT012N058	best32. ;	
        informat	  PCT012N059	best32. ;	
        informat	  PCT012N060	best32. ;	
        informat	  PCT012N061	best32. ;	
        informat	  PCT012N062	best32. ;	
        informat	  PCT012N063	best32. ;	
        informat	  PCT012N064	best32. ;	
        informat	  PCT012N065	best32. ;	
        informat	  PCT012N066	best32. ;	
        informat	  PCT012N067	best32. ;	
        informat	  PCT012N068	best32. ;	
        informat	  PCT012N069	best32. ;	
        informat	  PCT012N070	best32. ;	
        informat	  PCT012N071	best32. ;	
        informat	  PCT012N072	best32. ;	
        informat	  PCT012N073	best32. ;	
        informat	  PCT012N074	best32. ;	
        informat	  PCT012N075	best32. ;	
        informat	  PCT012N076	best32. ;	
        informat	  PCT012N077	best32. ;	
        informat	  PCT012N078	best32. ;	
        informat	  PCT012N079	best32. ;	
        informat	  PCT012N080	best32. ;	
        informat	  PCT012N081	best32. ;	
        informat	  PCT012N082	best32. ;	
        informat	  PCT012N083	best32. ;	
        informat	  PCT012N084	best32. ;	
        informat	  PCT012N085	best32. ;	
        informat	  PCT012N086	best32. ;	
        informat	  PCT012N087	best32. ;	
        informat	  PCT012N088	best32. ;	
        informat	  PCT012N089	best32. ;	
        informat	  PCT012N090	best32. ;	
        informat	  PCT012N091	best32. ;	
        informat	  PCT012N092	best32. ;	
        informat	  PCT012N093	best32. ;	
        informat	  PCT012N094	best32. ;	
        informat	  PCT012N095	best32. ;	
        informat	  PCT012N096	best32. ;	
        informat	  PCT012N097	best32. ;	
        informat	  PCT012N098	best32. ;	
        informat	  PCT012N099	best32. ;	
        informat	  PCT012N100	best32. ;	
        informat	  PCT012N101	best32. ;	
        informat	  PCT012N102	best32. ;	
        informat	  PCT012N103	best32. ;	
        informat	  PCT012N104	best32. ;	
        informat	  PCT012N105	best32. ;	
        informat	  PCT012N106	best32. ;	
        informat	  PCT012N107	best32. ;	
        informat	  PCT012N108	best32. ;	
        informat	  PCT012N109	best32. ;	
        informat	  PCT012N110	best32. ;	
        informat	  PCT012N111	best32. ;	
        informat	  PCT012N112	best32. ;	
        informat	  PCT012N113	best32. ;	
        informat	  PCT012N114	best32. ;	
        informat	  PCT012N115	best32. ;	
        informat	  PCT012N116	best32. ;	
        informat	  PCT012N117	best32. ;	
        informat	  PCT012N118	best32. ;	
        informat	  PCT012N119	best32. ;	
        informat	  PCT012N120	best32. ;	
        informat	  PCT012N121	best32. ;	
        informat	  PCT012N122	best32. ;	
        informat	  PCT012N123	best32. ;	
        informat	  PCT012N124	best32. ;	
        informat	  PCT012N125	best32. ;	
        informat	  PCT012N126	best32. ;	
        informat	  PCT012N127	best32. ;	
        informat	  PCT012N128	best32. ;	
        informat	  PCT012N129	best32. ;	
        informat	  PCT012N130	best32. ;	
        informat	  PCT012N131	best32. ;	
        informat	  PCT012N132	best32. ;	
        informat	  PCT012N133	best32. ;	
        informat	  PCT012N134	best32. ;	
        informat	  PCT012N135	best32. ;	
        informat	  PCT012N136	best32. ;	
        informat	  PCT012N137	best32. ;	
        informat	  PCT012N138	best32. ;	
        informat	  PCT012N139	best32. ;	
        informat	  PCT012N140	best32. ;	
        informat	  PCT012N141	best32. ;	
        informat	  PCT012N142	best32. ;	
        informat	  PCT012N143	best32. ;	
        informat	  PCT012N144	best32. ;	
        informat	  PCT012N145	best32. ;	
        informat	  PCT012N146	best32. ;	
        informat	  PCT012N147	best32. ;	
        informat	  PCT012N148	best32. ;	
        informat	  PCT012N149	best32. ;	
        informat	  PCT012N150	best32. ;	
        informat	  PCT012N151	best32. ;	
        informat	  PCT012N152	best32. ;	
        informat	  PCT012N153	best32. ;	
        informat	  PCT012N154	best32. ;	
        informat	  PCT012N155	best32. ;	
        informat	  PCT012N156	best32. ;	
        informat	  PCT012N157	best32. ;	
        informat	  PCT012N158	best32. ;	
        informat	  PCT012N159	best32. ;	
        informat	  PCT012N160	best32. ;	
        informat	  PCT012N161	best32. ;	
        informat	  PCT012N162	best32. ;	
        informat	  PCT012N163	best32. ;	
        informat	  PCT012N164	best32. ;	
        informat	  PCT012N165	best32. ;	
        informat	  PCT012N166	best32. ;	
        informat	  PCT012N167	best32. ;	
        informat	  PCT012N168	best32. ;	
        informat	  PCT012N169	best32. ;	
        informat	  PCT012N170	best32. ;	
        informat	  PCT012N171	best32. ;	
        informat	  PCT012N172	best32. ;	
        informat	  PCT012N173	best32. ;	
        informat	  PCT012N174	best32. ;	
        informat	  PCT012N175	best32. ;	
        informat	  PCT012N176	best32. ;	
        informat	  PCT012N177	best32. ;	
        informat	  PCT012N178	best32. ;	
        informat	  PCT012N179	best32. ;	
        informat	  PCT012N180	best32. ;	
        informat	  PCT012N181	best32. ;	
        informat	  PCT012N182	best32. ;	
        informat	  PCT012N183	best32. ;	
        informat	  PCT012N184	best32. ;	
        informat	  PCT012N185	best32. ;	
        informat	  PCT012N186	best32. ;	
        informat	  PCT012N187	best32. ;	
        informat	  PCT012N188	best32. ;	
        informat	  PCT012N189	best32. ;	
        informat	  PCT012N190	best32. ;	
        informat	  PCT012N191	best32. ;	
        informat	  PCT012N192	best32. ;	
        informat	  PCT012N193	best32. ;	
        informat	  PCT012N194	best32. ;	
        informat	  PCT012N195	best32. ;	
        informat	  PCT012N196	best32. ;	
        informat	  PCT012N197	best32. ;	
        informat	  PCT012N198	best32. ;	
        informat	  PCT012N199	best32. ;	
        informat	  PCT012N200	best32. ;	
        informat	  PCT012N201	best32. ;	
        informat	  PCT012N202	best32. ;	
        informat	  PCT012N203	best32. ;	
        informat	  PCT012N204	best32. ;	
        informat	  PCT012N205	best32. ;	
        informat	  PCT012N206	best32. ;	
        informat	  PCT012N207	best32. ;	
        informat	  PCT012N208	best32. ;	
        informat	  PCT012N209	best32. ;	
        informat	  PCT012O001	best32. ;	
        informat	  PCT012O002	best32. ;	
        informat	  PCT012O003	best32. ;	
        informat	  PCT012O004	best32. ;	
        informat	  PCT012O005	best32. ;	
        informat	  PCT012O006	best32. ;	
        informat	  PCT012O007	best32. ;	
        informat	  PCT012O008	best32. ;	
        informat	  PCT012O009	best32. ;	
        informat	  PCT012O010	best32. ;	
        informat	  PCT012O011	best32. ;	
        informat	  PCT012O012	best32. ;	
        informat	  PCT012O013	best32. ;	
        informat	  PCT012O014	best32. ;	
        informat	  PCT012O015	best32. ;	
        informat	  PCT012O016	best32. ;	
        informat	  PCT012O017	best32. ;	
        informat	  PCT012O018	best32. ;	
        informat	  PCT012O019	best32. ;	
        informat	  PCT012O020	best32. ;	
        informat	  PCT012O021	best32. ;	
        informat	  PCT012O022	best32. ;	
        informat	  PCT012O023	best32. ;	
        informat	  PCT012O024	best32. ;	
        informat	  PCT012O025	best32. ;	
        informat	  PCT012O026	best32. ;	
        informat	  PCT012O027	best32. ;	
        informat	  PCT012O028	best32. ;	
        informat	  PCT012O029	best32. ;	
        informat	  PCT012O030	best32. ;	
        informat	  PCT012O031	best32. ;	
        informat	  PCT012O032	best32. ;	
        informat	  PCT012O033	best32. ;	
        informat	  PCT012O034	best32. ;	
        informat	  PCT012O035	best32. ;	
        informat	  PCT012O036	best32. ;	
        informat	  PCT012O037	best32. ;	
        informat	  PCT012O038	best32. ;	
        informat	  PCT012O039	best32. ;	
        informat	  PCT012O040	best32. ;	
        informat	  PCT012O041	best32. ;	
        informat	  PCT012O042	best32. ;	
        informat	  PCT012O043	best32. ;	
        informat	  PCT012O044	best32. ;	
        informat	  PCT012O045	best32. ;	
        informat	  PCT012O046	best32. ;	
        informat	  PCT012O047	best32. ;	
        informat	  PCT012O048	best32. ;	
        informat	  PCT012O049	best32. ;	
        informat	  PCT012O050	best32. ;	
        informat	  PCT012O051	best32. ;	
        informat	  PCT012O052	best32. ;	
        informat	  PCT012O053	best32. ;	
        informat	  PCT012O054	best32. ;	
        informat	  PCT012O055	best32. ;	
        informat	  PCT012O056	best32. ;	
        informat	  PCT012O057	best32. ;	
        informat	  PCT012O058	best32. ;	
        informat	  PCT012O059	best32. ;	
        informat	  PCT012O060	best32. ;	
        informat	  PCT012O061	best32. ;	
        informat	  PCT012O062	best32. ;	
        informat	  PCT012O063	best32. ;	
        informat	  PCT012O064	best32. ;	
        informat	  PCT012O065	best32. ;	
        informat	  PCT012O066	best32. ;	
        informat	  PCT012O067	best32. ;	
        informat	  PCT012O068	best32. ;	
        informat	  PCT012O069	best32. ;	
        informat	  PCT012O070	best32. ;	
        informat	  PCT012O071	best32. ;	
        informat	  PCT012O072	best32. ;	
        informat	  PCT012O073	best32. ;	
        informat	  PCT012O074	best32. ;	
        informat	  PCT012O075	best32. ;	
        informat	  PCT012O076	best32. ;	
        informat	  PCT012O077	best32. ;	
        informat	  PCT012O078	best32. ;	
        informat	  PCT012O079	best32. ;	
        informat	  PCT012O080	best32. ;	
        informat	  PCT012O081	best32. ;	
        informat	  PCT012O082	best32. ;	
        informat	  PCT012O083	best32. ;	
        informat	  PCT012O084	best32. ;	
        informat	  PCT012O085	best32. ;	
        informat	  PCT012O086	best32. ;	
        informat	  PCT012O087	best32. ;	
        informat	  PCT012O088	best32. ;	
        informat	  PCT012O089	best32. ;	
        informat	  PCT012O090	best32. ;	
        informat	  PCT012O091	best32. ;	
        informat	  PCT012O092	best32. ;	
        informat	  PCT012O093	best32. ;	
        informat	  PCT012O094	best32. ;	
        informat	  PCT012O095	best32. ;	
        informat	  PCT012O096	best32. ;	
        informat	  PCT012O097	best32. ;	
        informat	  PCT012O098	best32. ;	
        informat	  PCT012O099	best32. ;	
        informat	  PCT012O100	best32. ;	
        informat	  PCT012O101	best32. ;	
        informat	  PCT012O102	best32. ;	
        informat	  PCT012O103	best32. ;	
        informat	  PCT012O104	best32. ;	
        informat	  PCT012O105	best32. ;	
        informat	  PCT012O106	best32. ;	
        informat	  PCT012O107	best32. ;	
        informat	  PCT012O108	best32. ;	
        informat	  PCT012O109	best32. ;	
        informat	  PCT012O110	best32. ;	
        informat	  PCT012O111	best32. ;	
        informat	  PCT012O112	best32. ;	
        informat	  PCT012O113	best32. ;	
        informat	  PCT012O114	best32. ;	
        informat	  PCT012O115	best32. ;	
        informat	  PCT012O116	best32. ;	
        informat	  PCT012O117	best32. ;	
        informat	  PCT012O118	best32. ;	
        informat	  PCT012O119	best32. ;	
        informat	  PCT012O120	best32. ;	
        informat	  PCT012O121	best32. ;	
        informat	  PCT012O122	best32. ;	
        informat	  PCT012O123	best32. ;	
        informat	  PCT012O124	best32. ;	
        informat	  PCT012O125	best32. ;	
        informat	  PCT012O126	best32. ;	
        informat	  PCT012O127	best32. ;	
        informat	  PCT012O128	best32. ;	
        informat	  PCT012O129	best32. ;	
        informat	  PCT012O130	best32. ;	
        informat	  PCT012O131	best32. ;	
        informat	  PCT012O132	best32. ;	
        informat	  PCT012O133	best32. ;	
        informat	  PCT012O134	best32. ;	
        informat	  PCT012O135	best32. ;	
        informat	  PCT012O136	best32. ;	
        informat	  PCT012O137	best32. ;	
        informat	  PCT012O138	best32. ;	
        informat	  PCT012O139	best32. ;	
        informat	  PCT012O140	best32. ;	
        informat	  PCT012O141	best32. ;	
        informat	  PCT012O142	best32. ;	
        informat	  PCT012O143	best32. ;	
        informat	  PCT012O144	best32. ;	
        informat	  PCT012O145	best32. ;	
        informat	  PCT012O146	best32. ;	
        informat	  PCT012O147	best32. ;	
        informat	  PCT012O148	best32. ;	
        informat	  PCT012O149	best32. ;	
        informat	  PCT012O150	best32. ;	
        informat	  PCT012O151	best32. ;	
        informat	  PCT012O152	best32. ;	
        informat	  PCT012O153	best32. ;	
        informat	  PCT012O154	best32. ;	
        informat	  PCT012O155	best32. ;	
        informat	  PCT012O156	best32. ;	
        informat	  PCT012O157	best32. ;	
        informat	  PCT012O158	best32. ;	
        informat	  PCT012O159	best32. ;	
        informat	  PCT012O160	best32. ;	
        informat	  PCT012O161	best32. ;	
        informat	  PCT012O162	best32. ;	
        informat	  PCT012O163	best32. ;	
        informat	  PCT012O164	best32. ;	
        informat	  PCT012O165	best32. ;	
        informat	  PCT012O166	best32. ;	
        informat	  PCT012O167	best32. ;	
        informat	  PCT012O168	best32. ;	
        informat	  PCT012O169	best32. ;	
        informat	  PCT012O170	best32. ;	
        informat	  PCT012O171	best32. ;	
        informat	  PCT012O172	best32. ;	
        informat	  PCT012O173	best32. ;	
        informat	  PCT012O174	best32. ;	
        informat	  PCT012O175	best32. ;	
        informat	  PCT012O176	best32. ;	
        informat	  PCT012O177	best32. ;	
        informat	  PCT012O178	best32. ;	
        informat	  PCT012O179	best32. ;	
        informat	  PCT012O180	best32. ;	
        informat	  PCT012O181	best32. ;	
        informat	  PCT012O182	best32. ;	
        informat	  PCT012O183	best32. ;	
        informat	  PCT012O184	best32. ;	
        informat	  PCT012O185	best32. ;	
        informat	  PCT012O186	best32. ;	
        informat	  PCT012O187	best32. ;	
        informat	  PCT012O188	best32. ;	
        informat	  PCT012O189	best32. ;	
        informat	  PCT012O190	best32. ;	
        informat	  PCT012O191	best32. ;	
        informat	  PCT012O192	best32. ;	
        informat	  PCT012O193	best32. ;	
        informat	  PCT012O194	best32. ;	
        informat	  PCT012O195	best32. ;	
        informat	  PCT012O196	best32. ;	
        informat	  PCT012O197	best32. ;	
        informat	  PCT012O198	best32. ;	
        informat	  PCT012O199	best32. ;	
        informat	  PCT012O200	best32. ;	
        informat	  PCT012O201	best32. ;	
        informat	  PCT012O202	best32. ;	
        informat	  PCT012O203	best32. ;	
        informat	  PCT012O204	best32. ;	
        informat	  PCT012O205	best32. ;	
        informat	  PCT012O206	best32. ;	
        informat	  PCT012O207	best32. ;	
        informat	  PCT012O208	best32. ;	
        informat	  PCT012O209	best32. ;	
        informat	  PCT013A001	best32. ;	
        informat	  PCT013A002	best32. ;	
        informat	  PCT013A003	best32. ;	
        informat	  PCT013A004	best32. ;	
        informat	  PCT013A005	best32. ;	
        informat	  PCT013A006	best32. ;	
        informat	  PCT013A007	best32. ;	
        informat	  PCT013A008	best32. ;	
        informat	  PCT013A009	best32. ;	
        informat	  PCT013A010	best32. ;	
        informat	  PCT013A011	best32. ;	
        informat	  PCT013A012	best32. ;	
        informat	  PCT013A013	best32. ;	
        informat	  PCT013A014	best32. ;	
        informat	  PCT013A015	best32. ;	
        informat	  PCT013A016	best32. ;	
        informat	  PCT013A017	best32. ;	
        informat	  PCT013A018	best32. ;	
        informat	  PCT013A019	best32. ;	
        informat	  PCT013A020	best32. ;	
        informat	  PCT013A021	best32. ;	
        informat	  PCT013A022	best32. ;	
        informat	  PCT013A023	best32. ;	
        informat	  PCT013A024	best32. ;	
        informat	  PCT013A025	best32. ;	
        informat	  PCT013A026	best32. ;	
        informat	  PCT013A027	best32. ;	
        informat	  PCT013A028	best32. ;	
        informat	  PCT013A029	best32. ;	
        informat	  PCT013A030	best32. ;	
        informat	  PCT013A031	best32. ;	
        informat	  PCT013A032	best32. ;	
        informat	  PCT013A033	best32. ;	
        informat	  PCT013A034	best32. ;	
        informat	  PCT013A035	best32. ;	
        informat	  PCT013A036	best32. ;	
        informat	  PCT013A037	best32. ;	
        informat	  PCT013A038	best32. ;	
        informat	  PCT013A039	best32. ;	
        informat	  PCT013A040	best32. ;	
        informat	  PCT013A041	best32. ;	
        informat	  PCT013A042	best32. ;	
        informat	  PCT013A043	best32. ;	
        informat	  PCT013A044	best32. ;	
        informat	  PCT013A045	best32. ;	
        informat	  PCT013A046	best32. ;	
        informat	  PCT013A047	best32. ;	
        informat	  PCT013A048	best32. ;	
        informat	  PCT013A049	best32. ;	
        informat	  PCT013B001	best32. ;	
        informat	  PCT013B002	best32. ;	
        informat	  PCT013B003	best32. ;	
        informat	  PCT013B004	best32. ;	
        informat	  PCT013B005	best32. ;	
        informat	  PCT013B006	best32. ;	
        informat	  PCT013B007	best32. ;	
        informat	  PCT013B008	best32. ;	
        informat	  PCT013B009	best32. ;	
        informat	  PCT013B010	best32. ;	
        informat	  PCT013B011	best32. ;	
        informat	  PCT013B012	best32. ;	
        informat	  PCT013B013	best32. ;	
        informat	  PCT013B014	best32. ;	
        informat	  PCT013B015	best32. ;	
        informat	  PCT013B016	best32. ;	
        informat	  PCT013B017	best32. ;	
        informat	  PCT013B018	best32. ;	
        informat	  PCT013B019	best32. ;	
        informat	  PCT013B020	best32. ;	
        informat	  PCT013B021	best32. ;	
        informat	  PCT013B022	best32. ;	
        informat	  PCT013B023	best32. ;	
        informat	  PCT013B024	best32. ;	
        informat	  PCT013B025	best32. ;	
        informat	  PCT013B026	best32. ;	
        informat	  PCT013B027	best32. ;	
        informat	  PCT013B028	best32. ;	
        informat	  PCT013B029	best32. ;	
        informat	  PCT013B030	best32. ;	
        informat	  PCT013B031	best32. ;	
        informat	  PCT013B032	best32. ;	
        informat	  PCT013B033	best32. ;	
        informat	  PCT013B034	best32. ;	
        informat	  PCT013B035	best32. ;	
        informat	  PCT013B036	best32. ;	
        informat	  PCT013B037	best32. ;	
        informat	  PCT013B038	best32. ;	
        informat	  PCT013B039	best32. ;	
        informat	  PCT013B040	best32. ;	
        informat	  PCT013B041	best32. ;	
        informat	  PCT013B042	best32. ;	
        informat	  PCT013B043	best32. ;	
        informat	  PCT013B044	best32. ;	
        informat	  PCT013B045	best32. ;	
        informat	  PCT013B046	best32. ;	
        informat	  PCT013B047	best32. ;	
        informat	  PCT013B048	best32. ;	
        informat	  PCT013B049	best32. ;	
        informat	  PCT013C001	best32. ;	
        informat	  PCT013C002	best32. ;	
        informat	  PCT013C003	best32. ;	
        informat	  PCT013C004	best32. ;	
        informat	  PCT013C005	best32. ;	
        informat	  PCT013C006	best32. ;	
        informat	  PCT013C007	best32. ;	
        informat	  PCT013C008	best32. ;	
        informat	  PCT013C009	best32. ;	
        informat	  PCT013C010	best32. ;	
        informat	  PCT013C011	best32. ;	
        informat	  PCT013C012	best32. ;	
        informat	  PCT013C013	best32. ;	
        informat	  PCT013C014	best32. ;	
        informat	  PCT013C015	best32. ;	
        informat	  PCT013C016	best32. ;	
        informat	  PCT013C017	best32. ;	
        informat	  PCT013C018	best32. ;	
        informat	  PCT013C019	best32. ;	
        informat	  PCT013C020	best32. ;	
        informat	  PCT013C021	best32. ;	
        informat	  PCT013C022	best32. ;	
        informat	  PCT013C023	best32. ;	
        informat	  PCT013C024	best32. ;	
        informat	  PCT013C025	best32. ;	
        informat	  PCT013C026	best32. ;	
        informat	  PCT013C027	best32. ;	
        informat	  PCT013C028	best32. ;	
        informat	  PCT013C029	best32. ;	
        informat	  PCT013C030	best32. ;	
        informat	  PCT013C031	best32. ;	
        informat	  PCT013C032	best32. ;	
        informat	  PCT013C033	best32. ;	
        informat	  PCT013C034	best32. ;	
        informat	  PCT013C035	best32. ;	
        informat	  PCT013C036	best32. ;	
        informat	  PCT013C037	best32. ;	
        informat	  PCT013C038	best32. ;	
        informat	  PCT013C039	best32. ;	
        informat	  PCT013C040	best32. ;	
        informat	  PCT013C041	best32. ;	
        informat	  PCT013C042	best32. ;	
        informat	  PCT013C043	best32. ;	
        informat	  PCT013C044	best32. ;	
        informat	  PCT013C045	best32. ;	
        informat	  PCT013C046	best32. ;	
        informat	  PCT013C047	best32. ;	
        informat	  PCT013C048	best32. ;	
        informat	  PCT013C049	best32. ;	
        informat	  PCT013D001	best32. ;	
        informat	  PCT013D002	best32. ;	
        informat	  PCT013D003	best32. ;	
        informat	  PCT013D004	best32. ;	
        informat	  PCT013D005	best32. ;	
        informat	  PCT013D006	best32. ;	
        informat	  PCT013D007	best32. ;	
        informat	  PCT013D008	best32. ;	
        informat	  PCT013D009	best32. ;	
        informat	  PCT013D010	best32. ;	
        informat	  PCT013D011	best32. ;	
        informat	  PCT013D012	best32. ;	
        informat	  PCT013D013	best32. ;	
        informat	  PCT013D014	best32. ;	
        informat	  PCT013D015	best32. ;	
        informat	  PCT013D016	best32. ;	
        informat	  PCT013D017	best32. ;	
        informat	  PCT013D018	best32. ;	
        informat	  PCT013D019	best32. ;	
        informat	  PCT013D020	best32. ;	
        informat	  PCT013D021	best32. ;	
        informat	  PCT013D022	best32. ;	
        informat	  PCT013D023	best32. ;	
        informat	  PCT013D024	best32. ;	
        informat	  PCT013D025	best32. ;	
        informat	  PCT013D026	best32. ;	
        informat	  PCT013D027	best32. ;	
        informat	  PCT013D028	best32. ;	
        informat	  PCT013D029	best32. ;	
        informat	  PCT013D030	best32. ;	
        informat	  PCT013D031	best32. ;	
        informat	  PCT013D032	best32. ;	
        informat	  PCT013D033	best32. ;	
        informat	  PCT013D034	best32. ;	
        informat	  PCT013D035	best32. ;	
        informat	  PCT013D036	best32. ;	
        informat	  PCT013D037	best32. ;	
        informat	  PCT013D038	best32. ;	
        informat	  PCT013D039	best32. ;	
        informat	  PCT013D040	best32. ;	
        informat	  PCT013D041	best32. ;	
        informat	  PCT013D042	best32. ;	
        informat	  PCT013D043	best32. ;	
        informat	  PCT013D044	best32. ;	
        informat	  PCT013D045	best32. ;	
        informat	  PCT013D046	best32. ;	
        informat	  PCT013D047	best32. ;	
        informat	  PCT013D048	best32. ;	
        informat	  PCT013D049	best32. ;	
        informat	  PCT013E001	best32. ;	
        informat	  PCT013E002	best32. ;	
        informat	  PCT013E003	best32. ;	
        informat	  PCT013E004	best32. ;	
        informat	  PCT013E005	best32. ;	
        informat	  PCT013E006	best32. ;	
        informat	  PCT013E007	best32. ;	
        informat	  PCT013E008	best32. ;	
        informat	  PCT013E009	best32. ;	
        informat	  PCT013E010	best32. ;	
        informat	  PCT013E011	best32. ;	
        informat	  PCT013E012	best32. ;	
        informat	  PCT013E013	best32. ;	
        informat	  PCT013E014	best32. ;	
        informat	  PCT013E015	best32. ;	
        informat	  PCT013E016	best32. ;	
        informat	  PCT013E017	best32. ;	
        informat	  PCT013E018	best32. ;	
        informat	  PCT013E019	best32. ;	
        informat	  PCT013E020	best32. ;	
        informat	  PCT013E021	best32. ;	
        informat	  PCT013E022	best32. ;	
        informat	  PCT013E023	best32. ;	
        informat	  PCT013E024	best32. ;	
        informat	  PCT013E025	best32. ;	
        informat	  PCT013E026	best32. ;	
        informat	  PCT013E027	best32. ;	
        informat	  PCT013E028	best32. ;	
        informat	  PCT013E029	best32. ;	
        informat	  PCT013E030	best32. ;	
        informat	  PCT013E031	best32. ;	
        informat	  PCT013E032	best32. ;	
        informat	  PCT013E033	best32. ;	
        informat	  PCT013E034	best32. ;	
        informat	  PCT013E035	best32. ;	
        informat	  PCT013E036	best32. ;	
        informat	  PCT013E037	best32. ;	
        informat	  PCT013E038	best32. ;	
        informat	  PCT013E039	best32. ;	
        informat	  PCT013E040	best32. ;	
        informat	  PCT013E041	best32. ;	
        informat	  PCT013E042	best32. ;	
        informat	  PCT013E043	best32. ;	
        informat	  PCT013E044	best32. ;	
        informat	  PCT013E045	best32. ;	
        informat	  PCT013E046	best32. ;	
        informat	  PCT013E047	best32. ;	
        informat	  PCT013E048	best32. ;	
        informat	  PCT013E049	best32. ;	
        informat	  PCT013F001	best32. ;	
        informat	  PCT013F002	best32. ;	
        informat	  PCT013F003	best32. ;	
        informat	  PCT013F004	best32. ;	
        informat	  PCT013F005	best32. ;	
        informat	  PCT013F006	best32. ;	
        informat	  PCT013F007	best32. ;	
        informat	  PCT013F008	best32. ;	
        informat	  PCT013F009	best32. ;	
        informat	  PCT013F010	best32. ;	
        informat	  PCT013F011	best32. ;	
        informat	  PCT013F012	best32. ;	
        informat	  PCT013F013	best32. ;	
        informat	  PCT013F014	best32. ;	
        informat	  PCT013F015	best32. ;	
        informat	  PCT013F016	best32. ;	
        informat	  PCT013F017	best32. ;	
        informat	  PCT013F018	best32. ;	
        informat	  PCT013F019	best32. ;	
        informat	  PCT013F020	best32. ;	
        informat	  PCT013F021	best32. ;	
        informat	  PCT013F022	best32. ;	
        informat	  PCT013F023	best32. ;	
        informat	  PCT013F024	best32. ;	
        informat	  PCT013F025	best32. ;	
        informat	  PCT013F026	best32. ;	
        informat	  PCT013F027	best32. ;	
        informat	  PCT013F028	best32. ;	
        informat	  PCT013F029	best32. ;	
        informat	  PCT013F030	best32. ;	
        informat	  PCT013F031	best32. ;	
        informat	  PCT013F032	best32. ;	
        informat	  PCT013F033	best32. ;	
        informat	  PCT013F034	best32. ;	
        informat	  PCT013F035	best32. ;	
        informat	  PCT013F036	best32. ;	
        informat	  PCT013F037	best32. ;	
        informat	  PCT013F038	best32. ;	
        informat	  PCT013F039	best32. ;	
        informat	  PCT013F040	best32. ;	
        informat	  PCT013F041	best32. ;	
        informat	  PCT013F042	best32. ;	
        informat	  PCT013F043	best32. ;	
        informat	  PCT013F044	best32. ;	
        informat	  PCT013F045	best32. ;	
        informat	  PCT013F046	best32. ;	
        informat	  PCT013F047	best32. ;	
        informat	  PCT013F048	best32. ;	
        informat	  PCT013F049	best32. ;	
        informat	  PCT013G001	best32. ;	
        informat	  PCT013G002	best32. ;	
        informat	  PCT013G003	best32. ;	
        informat	  PCT013G004	best32. ;	
        informat	  PCT013G005	best32. ;	
        informat	  PCT013G006	best32. ;	
        informat	  PCT013G007	best32. ;	
        informat	  PCT013G008	best32. ;	
        informat	  PCT013G009	best32. ;	
        informat	  PCT013G010	best32. ;	
        informat	  PCT013G011	best32. ;	
        informat	  PCT013G012	best32. ;	
        informat	  PCT013G013	best32. ;	
        informat	  PCT013G014	best32. ;	
        informat	  PCT013G015	best32. ;	
        informat	  PCT013G016	best32. ;	
        informat	  PCT013G017	best32. ;	
        informat	  PCT013G018	best32. ;	
        informat	  PCT013G019	best32. ;	
        informat	  PCT013G020	best32. ;	
        informat	  PCT013G021	best32. ;	
        informat	  PCT013G022	best32. ;	
        informat	  PCT013G023	best32. ;	
        informat	  PCT013G024	best32. ;	
        informat	  PCT013G025	best32. ;	
        informat	  PCT013G026	best32. ;	
        informat	  PCT013G027	best32. ;	
        informat	  PCT013G028	best32. ;	
        informat	  PCT013G029	best32. ;	
        informat	  PCT013G030	best32. ;	
        informat	  PCT013G031	best32. ;	
        informat	  PCT013G032	best32. ;	
        informat	  PCT013G033	best32. ;	
        informat	  PCT013G034	best32. ;	
        informat	  PCT013G035	best32. ;	
        informat	  PCT013G036	best32. ;	
        informat	  PCT013G037	best32. ;	
        informat	  PCT013G038	best32. ;	
        informat	  PCT013G039	best32. ;	
        informat	  PCT013G040	best32. ;	
        informat	  PCT013G041	best32. ;	
        informat	  PCT013G042	best32. ;	
        informat	  PCT013G043	best32. ;	
        informat	  PCT013G044	best32. ;	
        informat	  PCT013G045	best32. ;	
        informat	  PCT013G046	best32. ;	
        informat	  PCT013G047	best32. ;	
        informat	  PCT013G048	best32. ;	
        informat	  PCT013G049	best32. ;	
        informat	  PCT013H001	best32. ;	
        informat	  PCT013H002	best32. ;	
        informat	  PCT013H003	best32. ;	
        informat	  PCT013H004	best32. ;	
        informat	  PCT013H005	best32. ;	
        informat	  PCT013H006	best32. ;	
        informat	  PCT013H007	best32. ;	
        informat	  PCT013H008	best32. ;	
        informat	  PCT013H009	best32. ;	
        informat	  PCT013H010	best32. ;	
        informat	  PCT013H011	best32. ;	
        informat	  PCT013H012	best32. ;	
        informat	  PCT013H013	best32. ;	
        informat	  PCT013H014	best32. ;	
        informat	  PCT013H015	best32. ;	
        informat	  PCT013H016	best32. ;	
        informat	  PCT013H017	best32. ;	
        informat	  PCT013H018	best32. ;	
        informat	  PCT013H019	best32. ;	
        informat	  PCT013H020	best32. ;	
        informat	  PCT013H021	best32. ;	
        informat	  PCT013H022	best32. ;	
        informat	  PCT013H023	best32. ;	
        informat	  PCT013H024	best32. ;	
        informat	  PCT013H025	best32. ;	
        informat	  PCT013H026	best32. ;	
        informat	  PCT013H027	best32. ;	
        informat	  PCT013H028	best32. ;	
        informat	  PCT013H029	best32. ;	
        informat	  PCT013H030	best32. ;	
        informat	  PCT013H031	best32. ;	
        informat	  PCT013H032	best32. ;	
        informat	  PCT013H033	best32. ;	
        informat	  PCT013H034	best32. ;	
        informat	  PCT013H035	best32. ;	
        informat	  PCT013H036	best32. ;	
        informat	  PCT013H037	best32. ;	
        informat	  PCT013H038	best32. ;	
        informat	  PCT013H039	best32. ;	
        informat	  PCT013H040	best32. ;	
        informat	  PCT013H041	best32. ;	
        informat	  PCT013H042	best32. ;	
        informat	  PCT013H043	best32. ;	
        informat	  PCT013H044	best32. ;	
        informat	  PCT013H045	best32. ;	
        informat	  PCT013H046	best32. ;	
        informat	  PCT013H047	best32. ;	
        informat	  PCT013H048	best32. ;	
        informat	  PCT013H049	best32. ;	
        informat	  PCT013I001	best32. ;	
        informat	  PCT013I002	best32. ;	
        informat	  PCT013I003	best32. ;	
        informat	  PCT013I004	best32. ;	
        informat	  PCT013I005	best32. ;	
        informat	  PCT013I006	best32. ;	
        informat	  PCT013I007	best32. ;	
        informat	  PCT013I008	best32. ;	
        informat	  PCT013I009	best32. ;	
        informat	  PCT013I010	best32. ;	
        informat	  PCT013I011	best32. ;	
        informat	  PCT013I012	best32. ;	
        informat	  PCT013I013	best32. ;	
        informat	  PCT013I014	best32. ;	
        informat	  PCT013I015	best32. ;	
        informat	  PCT013I016	best32. ;	
        informat	  PCT013I017	best32. ;	
        informat	  PCT013I018	best32. ;	
        informat	  PCT013I019	best32. ;	
        informat	  PCT013I020	best32. ;	
        informat	  PCT013I021	best32. ;	
        informat	  PCT013I022	best32. ;	
        informat	  PCT013I023	best32. ;	
        informat	  PCT013I024	best32. ;	
        informat	  PCT013I025	best32. ;	
        informat	  PCT013I026	best32. ;	
        informat	  PCT013I027	best32. ;	
        informat	  PCT013I028	best32. ;	
        informat	  PCT013I029	best32. ;	
        informat	  PCT013I030	best32. ;	
        informat	  PCT013I031	best32. ;	
        informat	  PCT013I032	best32. ;	
        informat	  PCT013I033	best32. ;	
        informat	  PCT013I034	best32. ;	
        informat	  PCT013I035	best32. ;	
        informat	  PCT013I036	best32. ;	
        informat	  PCT013I037	best32. ;	
        informat	  PCT013I038	best32. ;	
        informat	  PCT013I039	best32. ;	
        informat	  PCT013I040	best32. ;	
        informat	  PCT013I041	best32. ;	
        informat	  PCT013I042	best32. ;	
        informat	  PCT013I043	best32. ;	
        informat	  PCT013I044	best32. ;	
        informat	  PCT013I045	best32. ;	
        informat	  PCT013I046	best32. ;	
        informat	  PCT013I047	best32. ;	
        informat	  PCT013I048	best32. ;	
        informat	  PCT013I049	best32. ;	
        informat	  PCT014A001	best32. ;	
        informat	  PCT014A002	best32. ;	
        informat	  PCT014A003	best32. ;	
        informat	  PCT014B001	best32. ;	
        informat	  PCT014B002	best32. ;	
        informat	  PCT014B003	best32. ;	
        informat	  PCT014C001	best32. ;	
        informat	  PCT014C002	best32. ;	
        informat	  PCT014C003	best32. ;	
        informat	  PCT014D001	best32. ;	
        informat	  PCT014D002	best32. ;	
        informat	  PCT014D003	best32. ;	
        informat	  PCT014E001	best32. ;	
        informat	  PCT014E002	best32. ;	
        informat	  PCT014E003	best32. ;	
        informat	  PCT014F001	best32. ;	
        informat	  PCT014F002	best32. ;	
        informat	  PCT014F003	best32. ;	
        informat	  PCT014G001	best32. ;	
        informat	  PCT014G002	best32. ;	
        informat	  PCT014G003	best32. ;	
        informat	  PCT014H001	best32. ;	
        informat	  PCT014H002	best32. ;	
        informat	  PCT014H003	best32. ;	
        informat	  PCT014I001	best32. ;	
        informat	  PCT014I002	best32. ;	
        informat	  PCT014I003	best32. ;	
        informat	  PCT019A001	best32. ;	
        informat	  PCT019A002	best32. ;	
        informat	  PCT019A003	best32. ;	
        informat	  PCT019A004	best32. ;	
        informat	  PCT019A005	best32. ;	
        informat	  PCT019A006	best32. ;	
        informat	  PCT019A007	best32. ;	
        informat	  PCT019A008	best32. ;	
        informat	  PCT019A009	best32. ;	
        informat	  PCT019A010	best32. ;	
        informat	  PCT019A011	best32. ;	
        informat	  PCT019B001	best32. ;	
        informat	  PCT019B002	best32. ;	
        informat	  PCT019B003	best32. ;	
        informat	  PCT019B004	best32. ;	
        informat	  PCT019B005	best32. ;	
        informat	  PCT019B006	best32. ;	
        informat	  PCT019B007	best32. ;	
        informat	  PCT019B008	best32. ;	
        informat	  PCT019B009	best32. ;	
        informat	  PCT019B010	best32. ;	
        informat	  PCT019B011	best32. ;	
        informat	  PCT019C001	best32. ;	
        informat	  PCT019C002	best32. ;	
        informat	  PCT019C003	best32. ;	
        informat	  PCT019C004	best32. ;	
        informat	  PCT019C005	best32. ;	
        informat	  PCT019C006	best32. ;	
        informat	  PCT019C007	best32. ;	
        informat	  PCT019C008	best32. ;	
        informat	  PCT019C009	best32. ;	
        informat	  PCT019C010	best32. ;	
        informat	  PCT019C011	best32. ;	
        informat	  PCT019D001	best32. ;	
        informat	  PCT019D002	best32. ;	
        informat	  PCT019D003	best32. ;	
        informat	  PCT019D004	best32. ;	
        informat	  PCT019D005	best32. ;	
        informat	  PCT019D006	best32. ;	
        informat	  PCT019D007	best32. ;	
        informat	  PCT019D008	best32. ;	
        informat	  PCT019D009	best32. ;	
        informat	  PCT019D010	best32. ;	
        informat	  PCT019D011	best32. ;	
        informat	  PCT019E001	best32. ;	
        informat	  PCT019E002	best32. ;	
        informat	  PCT019E003	best32. ;	
        informat	  PCT019E004	best32. ;	
        informat	  PCT019E005	best32. ;	
        informat	  PCT019E006	best32. ;	
        informat	  PCT019E007	best32. ;	
        informat	  PCT019E008	best32. ;	
        informat	  PCT019E009	best32. ;	
        informat	  PCT019E010	best32. ;	
        informat	  PCT019E011	best32. ;	
        informat	  PCT019F001	best32. ;	
        informat	  PCT019F002	best32. ;	
        informat	  PCT019F003	best32. ;	
        informat	  PCT019F004	best32. ;	
        informat	  PCT019F005	best32. ;	
        informat	  PCT019F006	best32. ;	
        informat	  PCT019F007	best32. ;	
        informat	  PCT019F008	best32. ;	
        informat	  PCT019F009	best32. ;	
        informat	  PCT019F010	best32. ;	
        informat	  PCT019F011	best32. ;	
        informat	  PCT019G001	best32. ;	
        informat	  PCT019G002	best32. ;	
        informat	  PCT019G003	best32. ;	
        informat	  PCT019G004	best32. ;	
        informat	  PCT019G005	best32. ;	
        informat	  PCT019G006	best32. ;	
        informat	  PCT019G007	best32. ;	
        informat	  PCT019G008	best32. ;	
        informat	  PCT019G009	best32. ;	
        informat	  PCT019G010	best32. ;	
        informat	  PCT019G011	best32. ;	
        informat	  PCT019H001	best32. ;	
        informat	  PCT019H002	best32. ;	
        informat	  PCT019H003	best32. ;	
        informat	  PCT019H004	best32. ;	
        informat	  PCT019H005	best32. ;	
        informat	  PCT019H006	best32. ;	
        informat	  PCT019H007	best32. ;	
        informat	  PCT019H008	best32. ;	
        informat	  PCT019H009	best32. ;	
        informat	  PCT019H010	best32. ;	
        informat	  PCT019H011	best32. ;	
        informat	  PCT019I001	best32. ;	
        informat	  PCT019I002	best32. ;	
        informat	  PCT019I003	best32. ;	
        informat	  PCT019I004	best32. ;	
        informat	  PCT019I005	best32. ;	
        informat	  PCT019I006	best32. ;	
        informat	  PCT019I007	best32. ;	
        informat	  PCT019I008	best32. ;	
        informat	  PCT019I009	best32. ;	
        informat	  PCT019I010	best32. ;	
        informat	  PCT019I011	best32. ;	
        informat	  PCT020A001	best32. ;	
        informat	  PCT020A002	best32. ;	
        informat	  PCT020A003	best32. ;	
        informat	  PCT020A004	best32. ;	
        informat	  PCT020A005	best32. ;	
        informat	  PCT020A006	best32. ;	
        informat	  PCT020A007	best32. ;	
        informat	  PCT020A008	best32. ;	
        informat	  PCT020A009	best32. ;	
        informat	  PCT020A010	best32. ;	
        informat	  PCT020A011	best32. ;	
        informat	  PCT020A012	best32. ;	
        informat	  PCT020A013	best32. ;	
        informat	  PCT020A014	best32. ;	
        informat	  PCT020A015	best32. ;	
        informat	  PCT020A016	best32. ;	
        informat	  PCT020A017	best32. ;	
        informat	  PCT020A018	best32. ;	
        informat	  PCT020A019	best32. ;	
        informat	  PCT020A020	best32. ;	
        informat	  PCT020A021	best32. ;	
        informat	  PCT020A022	best32. ;	
        informat	  PCT020A023	best32. ;	
        informat	  PCT020A024	best32. ;	
        informat	  PCT020A025	best32. ;	
        informat	  PCT020A026	best32. ;	
        informat	  PCT020A027	best32. ;	
        informat	  PCT020A028	best32. ;	
        informat	  PCT020A029	best32. ;	
        informat	  PCT020A030	best32. ;	
        informat	  PCT020A031	best32. ;	
        informat	  PCT020A032	best32. ;	
        informat	  PCT020B001	best32. ;	
        informat	  PCT020B002	best32. ;	
        informat	  PCT020B003	best32. ;	
        informat	  PCT020B004	best32. ;	
        informat	  PCT020B005	best32. ;	
        informat	  PCT020B006	best32. ;	
        informat	  PCT020B007	best32. ;	
        informat	  PCT020B008	best32. ;	
        informat	  PCT020B009	best32. ;	
        informat	  PCT020B010	best32. ;	
        informat	  PCT020B011	best32. ;	
        informat	  PCT020B012	best32. ;	
        informat	  PCT020B013	best32. ;	
        informat	  PCT020B014	best32. ;	
        informat	  PCT020B015	best32. ;	
        informat	  PCT020B016	best32. ;	
        informat	  PCT020B017	best32. ;	
        informat	  PCT020B018	best32. ;	
        informat	  PCT020B019	best32. ;	
        informat	  PCT020B020	best32. ;	
        informat	  PCT020B021	best32. ;	
        informat	  PCT020B022	best32. ;	
        informat	  PCT020B023	best32. ;	
        informat	  PCT020B024	best32. ;	
        informat	  PCT020B025	best32. ;	
        informat	  PCT020B026	best32. ;	
        informat	  PCT020B027	best32. ;	
        informat	  PCT020B028	best32. ;	
        informat	  PCT020B029	best32. ;	
        informat	  PCT020B030	best32. ;	
        informat	  PCT020B031	best32. ;	
        informat	  PCT020B032	best32. ;	
        informat	  PCT020C001	best32. ;	
        informat	  PCT020C002	best32. ;	
        informat	  PCT020C003	best32. ;	
        informat	  PCT020C004	best32. ;	
        informat	  PCT020C005	best32. ;	
        informat	  PCT020C006	best32. ;	
        informat	  PCT020C007	best32. ;	
        informat	  PCT020C008	best32. ;	
        informat	  PCT020C009	best32. ;	
        informat	  PCT020C010	best32. ;	
        informat	  PCT020C011	best32. ;	
        informat	  PCT020C012	best32. ;	
        informat	  PCT020C013	best32. ;	
        informat	  PCT020C014	best32. ;	
        informat	  PCT020C015	best32. ;	
        informat	  PCT020C016	best32. ;	
        informat	  PCT020C017	best32. ;	
        informat	  PCT020C018	best32. ;	
        informat	  PCT020C019	best32. ;	
        informat	  PCT020C020	best32. ;	
        informat	  PCT020C021	best32. ;	
        informat	  PCT020C022	best32. ;	
        informat	  PCT020C023	best32. ;	
        informat	  PCT020C024	best32. ;	
        informat	  PCT020C025	best32. ;	
        informat	  PCT020C026	best32. ;	
        informat	  PCT020C027	best32. ;	
        informat	  PCT020C028	best32. ;	
        informat	  PCT020C029	best32. ;	
        informat	  PCT020C030	best32. ;	
        informat	  PCT020C031	best32. ;	
        informat	  PCT020C032	best32. ;	
        informat	  PCT020D001	best32. ;	
        informat	  PCT020D002	best32. ;	
        informat	  PCT020D003	best32. ;	
        informat	  PCT020D004	best32. ;	
        informat	  PCT020D005	best32. ;	
        informat	  PCT020D006	best32. ;	
        informat	  PCT020D007	best32. ;	
        informat	  PCT020D008	best32. ;	
        informat	  PCT020D009	best32. ;	
        informat	  PCT020D010	best32. ;	
        informat	  PCT020D011	best32. ;	
        informat	  PCT020D012	best32. ;	
        informat	  PCT020D013	best32. ;	
        informat	  PCT020D014	best32. ;	
        informat	  PCT020D015	best32. ;	
        informat	  PCT020D016	best32. ;	
        informat	  PCT020D017	best32. ;	
        informat	  PCT020D018	best32. ;	
        informat	  PCT020D019	best32. ;	
        informat	  PCT020D020	best32. ;	
        informat	  PCT020D021	best32. ;	
        informat	  PCT020D022	best32. ;	
        informat	  PCT020D023	best32. ;	
        informat	  PCT020D024	best32. ;	
        informat	  PCT020D025	best32. ;	
        informat	  PCT020D026	best32. ;	
        informat	  PCT020D027	best32. ;	
        informat	  PCT020D028	best32. ;	
        informat	  PCT020D029	best32. ;	
        informat	  PCT020D030	best32. ;	
        informat	  PCT020D031	best32. ;	
        informat	  PCT020D032	best32. ;	
        informat	  PCT020E001	best32. ;	
        informat	  PCT020E002	best32. ;	
        informat	  PCT020E003	best32. ;	
        informat	  PCT020E004	best32. ;	
        informat	  PCT020E005	best32. ;	
        informat	  PCT020E006	best32. ;	
        informat	  PCT020E007	best32. ;	
        informat	  PCT020E008	best32. ;	
        informat	  PCT020E009	best32. ;	
        informat	  PCT020E010	best32. ;	
        informat	  PCT020E011	best32. ;	
        informat	  PCT020E012	best32. ;	
        informat	  PCT020E013	best32. ;	
        informat	  PCT020E014	best32. ;	
        informat	  PCT020E015	best32. ;	
        informat	  PCT020E016	best32. ;	
        informat	  PCT020E017	best32. ;	
        informat	  PCT020E018	best32. ;	
        informat	  PCT020E019	best32. ;	
        informat	  PCT020E020	best32. ;	
        informat	  PCT020E021	best32. ;	
        informat	  PCT020E022	best32. ;	
        informat	  PCT020E023	best32. ;	
        informat	  PCT020E024	best32. ;	
        informat	  PCT020E025	best32. ;	
        informat	  PCT020E026	best32. ;	
        informat	  PCT020E027	best32. ;	
        informat	  PCT020E028	best32. ;	
        informat	  PCT020E029	best32. ;	
        informat	  PCT020E030	best32. ;	
        informat	  PCT020E031	best32. ;	
        informat	  PCT020E032	best32. ;	
        informat	  PCT020F001	best32. ;	
        informat	  PCT020F002	best32. ;	
        informat	  PCT020F003	best32. ;	
        informat	  PCT020F004	best32. ;	
        informat	  PCT020F005	best32. ;	
        informat	  PCT020F006	best32. ;	
        informat	  PCT020F007	best32. ;	
        informat	  PCT020F008	best32. ;	
        informat	  PCT020F009	best32. ;	
        informat	  PCT020F010	best32. ;	
        informat	  PCT020F011	best32. ;	
        informat	  PCT020F012	best32. ;	
        informat	  PCT020F013	best32. ;	
        informat	  PCT020F014	best32. ;	
        informat	  PCT020F015	best32. ;	
        informat	  PCT020F016	best32. ;	
        informat	  PCT020F017	best32. ;	
        informat	  PCT020F018	best32. ;	
        informat	  PCT020F019	best32. ;	
        informat	  PCT020F020	best32. ;	
        informat	  PCT020F021	best32. ;	
        informat	  PCT020F022	best32. ;	
        informat	  PCT020F023	best32. ;	
        informat	  PCT020F024	best32. ;	
        informat	  PCT020F025	best32. ;	
        informat	  PCT020F026	best32. ;	
        informat	  PCT020F027	best32. ;	
        informat	  PCT020F028	best32. ;	
        informat	  PCT020F029	best32. ;	
        informat	  PCT020F030	best32. ;	
        informat	  PCT020F031	best32. ;	
        informat	  PCT020F032	best32. ;	
        informat	  PCT020G001	best32. ;	
        informat	  PCT020G002	best32. ;	
        informat	  PCT020G003	best32. ;	
        informat	  PCT020G004	best32. ;	
        informat	  PCT020G005	best32. ;	
        informat	  PCT020G006	best32. ;	
        informat	  PCT020G007	best32. ;	
        informat	  PCT020G008	best32. ;	
        informat	  PCT020G009	best32. ;	
        informat	  PCT020G010	best32. ;	
        informat	  PCT020G011	best32. ;	
        informat	  PCT020G012	best32. ;	
        informat	  PCT020G013	best32. ;	
        informat	  PCT020G014	best32. ;	
        informat	  PCT020G015	best32. ;	
        informat	  PCT020G016	best32. ;	
        informat	  PCT020G017	best32. ;	
        informat	  PCT020G018	best32. ;	
        informat	  PCT020G019	best32. ;	
        informat	  PCT020G020	best32. ;	
        informat	  PCT020G021	best32. ;	
        informat	  PCT020G022	best32. ;	
        informat	  PCT020G023	best32. ;	
        informat	  PCT020G024	best32. ;	
        informat	  PCT020G025	best32. ;	
        informat	  PCT020G026	best32. ;	
        informat	  PCT020G027	best32. ;	
        informat	  PCT020G028	best32. ;	
        informat	  PCT020G029	best32. ;	
        informat	  PCT020G030	best32. ;	
        informat	  PCT020G031	best32. ;	
        informat	  PCT020G032	best32. ;	
        informat	  PCT020H001	best32. ;	
        informat	  PCT020H002	best32. ;	
        informat	  PCT020H003	best32. ;	
        informat	  PCT020H004	best32. ;	
        informat	  PCT020H005	best32. ;	
        informat	  PCT020H006	best32. ;	
        informat	  PCT020H007	best32. ;	
        informat	  PCT020H008	best32. ;	
        informat	  PCT020H009	best32. ;	
        informat	  PCT020H010	best32. ;	
        informat	  PCT020H011	best32. ;	
        informat	  PCT020H012	best32. ;	
        informat	  PCT020H013	best32. ;	
        informat	  PCT020H014	best32. ;	
        informat	  PCT020H015	best32. ;	
        informat	  PCT020H016	best32. ;	
        informat	  PCT020H017	best32. ;	
        informat	  PCT020H018	best32. ;	
        informat	  PCT020H019	best32. ;	
        informat	  PCT020H020	best32. ;	
        informat	  PCT020H021	best32. ;	
        informat	  PCT020H022	best32. ;	
        informat	  PCT020H023	best32. ;	
        informat	  PCT020H024	best32. ;	
        informat	  PCT020H025	best32. ;	
        informat	  PCT020H026	best32. ;	
        informat	  PCT020H027	best32. ;	
        informat	  PCT020H028	best32. ;	
        informat	  PCT020H029	best32. ;	
        informat	  PCT020H030	best32. ;	
        informat	  PCT020H031	best32. ;	
        informat	  PCT020H032	best32. ;	
        informat	  PCT020I001	best32. ;	
        informat	  PCT020I002	best32. ;	
        informat	  PCT020I003	best32. ;	
        informat	  PCT020I004	best32. ;	
        informat	  PCT020I005	best32. ;	
        informat	  PCT020I006	best32. ;	
        informat	  PCT020I007	best32. ;	
        informat	  PCT020I008	best32. ;	
        informat	  PCT020I009	best32. ;	
        informat	  PCT020I010	best32. ;	
        informat	  PCT020I011	best32. ;	
        informat	  PCT020I012	best32. ;	
        informat	  PCT020I013	best32. ;	
        informat	  PCT020I014	best32. ;	
        informat	  PCT020I015	best32. ;	
        informat	  PCT020I016	best32. ;	
        informat	  PCT020I017	best32. ;	
        informat	  PCT020I018	best32. ;	
        informat	  PCT020I019	best32. ;	
        informat	  PCT020I020	best32. ;	
        informat	  PCT020I021	best32. ;	
        informat	  PCT020I022	best32. ;	
        informat	  PCT020I023	best32. ;	
        informat	  PCT020I024	best32. ;	
        informat	  PCT020I025	best32. ;	
        informat	  PCT020I026	best32. ;	
        informat	  PCT020I027	best32. ;	
        informat	  PCT020I028	best32. ;	
        informat	  PCT020I029	best32. ;	
        informat	  PCT020I030	best32. ;	
        informat	  PCT020I031	best32. ;	
        informat	  PCT020I032	best32. ;	
        informat	  PCT022A001	best32. ;	
        informat	  PCT022A002	best32. ;	
        informat	  PCT022A003	best32. ;	
        informat	  PCT022A004	best32. ;	
        informat	  PCT022A005	best32. ;	
        informat	  PCT022A006	best32. ;	
        informat	  PCT022A007	best32. ;	
        informat	  PCT022A008	best32. ;	
        informat	  PCT022A009	best32. ;	
        informat	  PCT022A010	best32. ;	
        informat	  PCT022A011	best32. ;	
        informat	  PCT022A012	best32. ;	
        informat	  PCT022A013	best32. ;	
        informat	  PCT022A014	best32. ;	
        informat	  PCT022A015	best32. ;	
        informat	  PCT022A016	best32. ;	
        informat	  PCT022A017	best32. ;	
        informat	  PCT022A018	best32. ;	
        informat	  PCT022A019	best32. ;	
        informat	  PCT022A020	best32. ;	
        informat	  PCT022A021	best32. ;	
        informat	  PCT022B001	best32. ;	
        informat	  PCT022B002	best32. ;	
        informat	  PCT022B003	best32. ;	
        informat	  PCT022B004	best32. ;	
        informat	  PCT022B005	best32. ;	
        informat	  PCT022B006	best32. ;	
        informat	  PCT022B007	best32. ;	
        informat	  PCT022B008	best32. ;	
        informat	  PCT022B009	best32. ;	
        informat	  PCT022B010	best32. ;	
        informat	  PCT022B011	best32. ;	
        informat	  PCT022B012	best32. ;	
        informat	  PCT022B013	best32. ;	
        informat	  PCT022B014	best32. ;	
        informat	  PCT022B015	best32. ;	
        informat	  PCT022B016	best32. ;	
        informat	  PCT022B017	best32. ;	
        informat	  PCT022B018	best32. ;	
        informat	  PCT022B019	best32. ;	
        informat	  PCT022B020	best32. ;	
        informat	  PCT022B021	best32. ;	
        informat	  PCT022C001	best32. ;	
        informat	  PCT022C002	best32. ;	
        informat	  PCT022C003	best32. ;	
        informat	  PCT022C004	best32. ;	
        informat	  PCT022C005	best32. ;	
        informat	  PCT022C006	best32. ;	
        informat	  PCT022C007	best32. ;	
        informat	  PCT022C008	best32. ;	
        informat	  PCT022C009	best32. ;	
        informat	  PCT022C010	best32. ;	
        informat	  PCT022C011	best32. ;	
        informat	  PCT022C012	best32. ;	
        informat	  PCT022C013	best32. ;	
        informat	  PCT022C014	best32. ;	
        informat	  PCT022C015	best32. ;	
        informat	  PCT022C016	best32. ;	
        informat	  PCT022C017	best32. ;	
        informat	  PCT022C018	best32. ;	
        informat	  PCT022C019	best32. ;	
        informat	  PCT022C020	best32. ;	
        informat	  PCT022C021	best32. ;	
        informat	  PCT022D001	best32. ;	
        informat	  PCT022D002	best32. ;	
        informat	  PCT022D003	best32. ;	
        informat	  PCT022D004	best32. ;	
        informat	  PCT022D005	best32. ;	
        informat	  PCT022D006	best32. ;	
        informat	  PCT022D007	best32. ;	
        informat	  PCT022D008	best32. ;	
        informat	  PCT022D009	best32. ;	
        informat	  PCT022D010	best32. ;	
        informat	  PCT022D011	best32. ;	
        informat	  PCT022D012	best32. ;	
        informat	  PCT022D013	best32. ;	
        informat	  PCT022D014	best32. ;	
        informat	  PCT022D015	best32. ;	
        informat	  PCT022D016	best32. ;	
        informat	  PCT022D017	best32. ;	
        informat	  PCT022D018	best32. ;	
        informat	  PCT022D019	best32. ;	
        informat	  PCT022D020	best32. ;	
        informat	  PCT022D021	best32. ;	
        informat	  PCT022E001	best32. ;	
        informat	  PCT022E002	best32. ;	
        informat	  PCT022E003	best32. ;	
        informat	  PCT022E004	best32. ;	
        informat	  PCT022E005	best32. ;	
        informat	  PCT022E006	best32. ;	
        informat	  PCT022E007	best32. ;	
        informat	  PCT022E008	best32. ;	
        informat	  PCT022E009	best32. ;	
        informat	  PCT022E010	best32. ;	
        informat	  PCT022E011	best32. ;	
        informat	  PCT022E012	best32. ;	
        informat	  PCT022E013	best32. ;	
        informat	  PCT022E014	best32. ;	
        informat	  PCT022E015	best32. ;	
        informat	  PCT022E016	best32. ;	
        informat	  PCT022E017	best32. ;	
        informat	  PCT022E018	best32. ;	
        informat	  PCT022E019	best32. ;	
        informat	  PCT022E020	best32. ;	
        informat	  PCT022E021	best32. ;	
        informat	  PCT022F001	best32. ;	
        informat	  PCT022F002	best32. ;	
        informat	  PCT022F003	best32. ;	
        informat	  PCT022F004	best32. ;	
        informat	  PCT022F005	best32. ;	
        informat	  PCT022F006	best32. ;	
        informat	  PCT022F007	best32. ;	
        informat	  PCT022F008	best32. ;	
        informat	  PCT022F009	best32. ;	
        informat	  PCT022F010	best32. ;	
        informat	  PCT022F011	best32. ;	
        informat	  PCT022F012	best32. ;	
        informat	  PCT022F013	best32. ;	
        informat	  PCT022F014	best32. ;	
        informat	  PCT022F015	best32. ;	
        informat	  PCT022F016	best32. ;	
        informat	  PCT022F017	best32. ;	
        informat	  PCT022F018	best32. ;	
        informat	  PCT022F019	best32. ;	
        informat	  PCT022F020	best32. ;	
        informat	  PCT022F021	best32. ;	
        informat	  PCT022G001	best32. ;	
        informat	  PCT022G002	best32. ;	
        informat	  PCT022G003	best32. ;	
        informat	  PCT022G004	best32. ;	
        informat	  PCT022G005	best32. ;	
        informat	  PCT022G006	best32. ;	
        informat	  PCT022G007	best32. ;	
        informat	  PCT022G008	best32. ;	
        informat	  PCT022G009	best32. ;	
        informat	  PCT022G010	best32. ;	
        informat	  PCT022G011	best32. ;	
        informat	  PCT022G012	best32. ;	
        informat	  PCT022G013	best32. ;	
        informat	  PCT022G014	best32. ;	
        informat	  PCT022G015	best32. ;	
        informat	  PCT022G016	best32. ;	
        informat	  PCT022G017	best32. ;	
        informat	  PCT022G018	best32. ;	
        informat	  PCT022G019	best32. ;	
        informat	  PCT022G020	best32. ;	
        informat	  PCT022G021	best32. ;	
        informat	  PCT022H001	best32. ;	
        informat	  PCT022H002	best32. ;	
        informat	  PCT022H003	best32. ;	
        informat	  PCT022H004	best32. ;	
        informat	  PCT022H005	best32. ;	
        informat	  PCT022H006	best32. ;	
        informat	  PCT022H007	best32. ;	
        informat	  PCT022H008	best32. ;	
        informat	  PCT022H009	best32. ;	
        informat	  PCT022H010	best32. ;	
        informat	  PCT022H011	best32. ;	
        informat	  PCT022H012	best32. ;	
        informat	  PCT022H013	best32. ;	
        informat	  PCT022H014	best32. ;	
        informat	  PCT022H015	best32. ;	
        informat	  PCT022H016	best32. ;	
        informat	  PCT022H017	best32. ;	
        informat	  PCT022H018	best32. ;	
        informat	  PCT022H019	best32. ;	
        informat	  PCT022H020	best32. ;	
        informat	  PCT022H021	best32. ;	
        informat	  PCT022I001	best32. ;	
        informat	  PCT022I002	best32. ;	
        informat	  PCT022I003	best32. ;	
        informat	  PCT022I004	best32. ;	
        informat	  PCT022I005	best32. ;	
        informat	  PCT022I006	best32. ;	
        informat	  PCT022I007	best32. ;	
        informat	  PCT022I008	best32. ;	
        informat	  PCT022I009	best32. ;	
        informat	  PCT022I010	best32. ;	
        informat	  PCT022I011	best32. ;	
        informat	  PCT022I012	best32. ;	
        informat	  PCT022I013	best32. ;	
        informat	  PCT022I014	best32. ;	
        informat	  PCT022I015	best32. ;	
        informat	  PCT022I016	best32. ;	
        informat	  PCT022I017	best32. ;	
        informat	  PCT022I018	best32. ;	
        informat	  PCT022I019	best32. ;	
        informat	  PCT022I020	best32. ;	
        informat	  PCT022I021	best32. ;	
        informat	  PCO0010001	best32. ;	
        informat	  PCO0010002	best32. ;	
        informat	  PCO0010003	best32. ;	
        informat	  PCO0010004	best32. ;	
        informat	  PCO0010005	best32. ;	
        informat	  PCO0010006	best32. ;	
        informat	  PCO0010007	best32. ;	
        informat	  PCO0010008	best32. ;	
        informat	  PCO0010009	best32. ;	
        informat	  PCO0010010	best32. ;	
        informat	  PCO0010011	best32. ;	
        informat	  PCO0010012	best32. ;	
        informat	  PCO0010013	best32. ;	
        informat	  PCO0010014	best32. ;	
        informat	  PCO0010015	best32. ;	
        informat	  PCO0010016	best32. ;	
        informat	  PCO0010017	best32. ;	
        informat	  PCO0010018	best32. ;	
        informat	  PCO0010019	best32. ;	
        informat	  PCO0010020	best32. ;	
        informat	  PCO0010021	best32. ;	
        informat	  PCO0010022	best32. ;	
        informat	  PCO0010023	best32. ;	
        informat	  PCO0010024	best32. ;	
        informat	  PCO0010025	best32. ;	
        informat	  PCO0010026	best32. ;	
        informat	  PCO0010027	best32. ;	
        informat	  PCO0010028	best32. ;	
        informat	  PCO0010029	best32. ;	
        informat	  PCO0010030	best32. ;	
        informat	  PCO0010031	best32. ;	
        informat	  PCO0010032	best32. ;	
        informat	  PCO0010033	best32. ;	
        informat	  PCO0010034	best32. ;	
        informat	  PCO0010035	best32. ;	
        informat	  PCO0010036	best32. ;	
        informat	  PCO0010037	best32. ;	
        informat	  PCO0010038	best32. ;	
        informat	  PCO0010039	best32. ;	
        informat	  PCO0020001	best32. ;	
        informat	  PCO0020002	best32. ;	
        informat	  PCO0020003	best32. ;	
        informat	  PCO0020004	best32. ;	
        informat	  PCO0020005	best32. ;	
        informat	  PCO0020006	best32. ;	
        informat	  PCO0020007	best32. ;	
        informat	  PCO0020008	best32. ;	
        informat	  PCO0020009	best32. ;	
        informat	  PCO0020010	best32. ;	
        informat	  PCO0020011	best32. ;	
        informat	  PCO0020012	best32. ;	
        informat	  PCO0020013	best32. ;	
        informat	  PCO0020014	best32. ;	
        informat	  PCO0020015	best32. ;	
        informat	  PCO0020016	best32. ;	
        informat	  PCO0020017	best32. ;	
        informat	  PCO0020018	best32. ;	
        informat	  PCO0020019	best32. ;	
        informat	  PCO0020020	best32. ;	
        informat	  PCO0020021	best32. ;	
        informat	  PCO0020022	best32. ;	
        informat	  PCO0020023	best32. ;	
        informat	  PCO0020024	best32. ;	
        informat	  PCO0020025	best32. ;	
        informat	  PCO0020026	best32. ;	
        informat	  PCO0020027	best32. ;	
        informat	  PCO0020028	best32. ;	
        informat	  PCO0020029	best32. ;	
        informat	  PCO0020030	best32. ;	
        informat	  PCO0020031	best32. ;	
        informat	  PCO0020032	best32. ;	
        informat	  PCO0020033	best32. ;	
        informat	  PCO0020034	best32. ;	
        informat	  PCO0020035	best32. ;	
        informat	  PCO0020036	best32. ;	
        informat	  PCO0020037	best32. ;	
        informat	  PCO0020038	best32. ;	
        informat	  PCO0020039	best32. ;	
        informat	  PCO0030001	best32. ;	
        informat	  PCO0030002	best32. ;	
        informat	  PCO0030003	best32. ;	
        informat	  PCO0030004	best32. ;	
        informat	  PCO0030005	best32. ;	
        informat	  PCO0030006	best32. ;	
        informat	  PCO0030007	best32. ;	
        informat	  PCO0030008	best32. ;	
        informat	  PCO0030009	best32. ;	
        informat	  PCO0030010	best32. ;	
        informat	  PCO0030011	best32. ;	
        informat	  PCO0030012	best32. ;	
        informat	  PCO0030013	best32. ;	
        informat	  PCO0030014	best32. ;	
        informat	  PCO0030015	best32. ;	
        informat	  PCO0030016	best32. ;	
        informat	  PCO0030017	best32. ;	
        informat	  PCO0030018	best32. ;	
        informat	  PCO0030019	best32. ;	
        informat	  PCO0030020	best32. ;	
        informat	  PCO0030021	best32. ;	
        informat	  PCO0030022	best32. ;	
        informat	  PCO0030023	best32. ;	
        informat	  PCO0030024	best32. ;	
        informat	  PCO0030025	best32. ;	
        informat	  PCO0030026	best32. ;	
        informat	  PCO0030027	best32. ;	
        informat	  PCO0030028	best32. ;	
        informat	  PCO0030029	best32. ;	
        informat	  PCO0030030	best32. ;	
        informat	  PCO0030031	best32. ;	
        informat	  PCO0030032	best32. ;	
        informat	  PCO0030033	best32. ;	
        informat	  PCO0030034	best32. ;	
        informat	  PCO0030035	best32. ;	
        informat	  PCO0030036	best32. ;	
        informat	  PCO0030037	best32. ;	
        informat	  PCO0030038	best32. ;	
        informat	  PCO0030039	best32. ;	
        informat	  PCO0040001	best32. ;	
        informat	  PCO0040002	best32. ;	
        informat	  PCO0040003	best32. ;	
        informat	  PCO0040004	best32. ;	
        informat	  PCO0040005	best32. ;	
        informat	  PCO0040006	best32. ;	
        informat	  PCO0040007	best32. ;	
        informat	  PCO0040008	best32. ;	
        informat	  PCO0040009	best32. ;	
        informat	  PCO0040010	best32. ;	
        informat	  PCO0040011	best32. ;	
        informat	  PCO0040012	best32. ;	
        informat	  PCO0040013	best32. ;	
        informat	  PCO0040014	best32. ;	
        informat	  PCO0040015	best32. ;	
        informat	  PCO0040016	best32. ;	
        informat	  PCO0040017	best32. ;	
        informat	  PCO0040018	best32. ;	
        informat	  PCO0040019	best32. ;	
        informat	  PCO0040020	best32. ;	
        informat	  PCO0040021	best32. ;	
        informat	  PCO0040022	best32. ;	
        informat	  PCO0040023	best32. ;	
        informat	  PCO0040024	best32. ;	
        informat	  PCO0040025	best32. ;	
        informat	  PCO0040026	best32. ;	
        informat	  PCO0040027	best32. ;	
        informat	  PCO0040028	best32. ;	
        informat	  PCO0040029	best32. ;	
        informat	  PCO0040030	best32. ;	
        informat	  PCO0040031	best32. ;	
        informat	  PCO0040032	best32. ;	
        informat	  PCO0040033	best32. ;	
        informat	  PCO0040034	best32. ;	
        informat	  PCO0040035	best32. ;	
        informat	  PCO0040036	best32. ;	
        informat	  PCO0040037	best32. ;	
        informat	  PCO0040038	best32. ;	
        informat	  PCO0040039	best32. ;	
        informat	  PCO0050001	best32. ;	
        informat	  PCO0050002	best32. ;	
        informat	  PCO0050003	best32. ;	
        informat	  PCO0050004	best32. ;	
        informat	  PCO0050005	best32. ;	
        informat	  PCO0050006	best32. ;	
        informat	  PCO0050007	best32. ;	
        informat	  PCO0050008	best32. ;	
        informat	  PCO0050009	best32. ;	
        informat	  PCO0050010	best32. ;	
        informat	  PCO0050011	best32. ;	
        informat	  PCO0050012	best32. ;	
        informat	  PCO0050013	best32. ;	
        informat	  PCO0050014	best32. ;	
        informat	  PCO0050015	best32. ;	
        informat	  PCO0050016	best32. ;	
        informat	  PCO0050017	best32. ;	
        informat	  PCO0050018	best32. ;	
        informat	  PCO0050019	best32. ;	
        informat	  PCO0050020	best32. ;	
        informat	  PCO0050021	best32. ;	
        informat	  PCO0050022	best32. ;	
        informat	  PCO0050023	best32. ;	
        informat	  PCO0050024	best32. ;	
        informat	  PCO0050025	best32. ;	
        informat	  PCO0050026	best32. ;	
        informat	  PCO0050027	best32. ;	
        informat	  PCO0050028	best32. ;	
        informat	  PCO0050029	best32. ;	
        informat	  PCO0050030	best32. ;	
        informat	  PCO0050031	best32. ;	
        informat	  PCO0050032	best32. ;	
        informat	  PCO0050033	best32. ;	
        informat	  PCO0050034	best32. ;	
        informat	  PCO0050035	best32. ;	
        informat	  PCO0050036	best32. ;	
        informat	  PCO0050037	best32. ;	
        informat	  PCO0050038	best32. ;	
        informat	  PCO0050039	best32. ;	
        informat	  PCO0060001	best32. ;	
        informat	  PCO0060002	best32. ;	
        informat	  PCO0060003	best32. ;	
        informat	  PCO0060004	best32. ;	
        informat	  PCO0060005	best32. ;	
        informat	  PCO0060006	best32. ;	
        informat	  PCO0060007	best32. ;	
        informat	  PCO0060008	best32. ;	
        informat	  PCO0060009	best32. ;	
        informat	  PCO0060010	best32. ;	
        informat	  PCO0060011	best32. ;	
        informat	  PCO0060012	best32. ;	
        informat	  PCO0060013	best32. ;	
        informat	  PCO0060014	best32. ;	
        informat	  PCO0060015	best32. ;	
        informat	  PCO0060016	best32. ;	
        informat	  PCO0060017	best32. ;	
        informat	  PCO0060018	best32. ;	
        informat	  PCO0060019	best32. ;	
        informat	  PCO0060020	best32. ;	
        informat	  PCO0060021	best32. ;	
        informat	  PCO0060022	best32. ;	
        informat	  PCO0060023	best32. ;	
        informat	  PCO0060024	best32. ;	
        informat	  PCO0060025	best32. ;	
        informat	  PCO0060026	best32. ;	
        informat	  PCO0060027	best32. ;	
        informat	  PCO0060028	best32. ;	
        informat	  PCO0060029	best32. ;	
        informat	  PCO0060030	best32. ;	
        informat	  PCO0060031	best32. ;	
        informat	  PCO0060032	best32. ;	
        informat	  PCO0060033	best32. ;	
        informat	  PCO0060034	best32. ;	
        informat	  PCO0060035	best32. ;	
        informat	  PCO0060036	best32. ;	
        informat	  PCO0060037	best32. ;	
        informat	  PCO0060038	best32. ;	
        informat	  PCO0060039	best32. ;	
        informat	  PCO0070001	best32. ;	
        informat	  PCO0070002	best32. ;	
        informat	  PCO0070003	best32. ;	
        informat	  PCO0070004	best32. ;	
        informat	  PCO0070005	best32. ;	
        informat	  PCO0070006	best32. ;	
        informat	  PCO0070007	best32. ;	
        informat	  PCO0070008	best32. ;	
        informat	  PCO0070009	best32. ;	
        informat	  PCO0070010	best32. ;	
        informat	  PCO0070011	best32. ;	
        informat	  PCO0070012	best32. ;	
        informat	  PCO0070013	best32. ;	
        informat	  PCO0070014	best32. ;	
        informat	  PCO0070015	best32. ;	
        informat	  PCO0070016	best32. ;	
        informat	  PCO0070017	best32. ;	
        informat	  PCO0070018	best32. ;	
        informat	  PCO0070019	best32. ;	
        informat	  PCO0070020	best32. ;	
        informat	  PCO0070021	best32. ;	
        informat	  PCO0070022	best32. ;	
        informat	  PCO0070023	best32. ;	
        informat	  PCO0070024	best32. ;	
        informat	  PCO0070025	best32. ;	
        informat	  PCO0070026	best32. ;	
        informat	  PCO0070027	best32. ;	
        informat	  PCO0070028	best32. ;	
        informat	  PCO0070029	best32. ;	
        informat	  PCO0070030	best32. ;	
        informat	  PCO0070031	best32. ;	
        informat	  PCO0070032	best32. ;	
        informat	  PCO0070033	best32. ;	
        informat	  PCO0070034	best32. ;	
        informat	  PCO0070035	best32. ;	
        informat	  PCO0070036	best32. ;	
        informat	  PCO0070037	best32. ;	
        informat	  PCO0070038	best32. ;	
        informat	  PCO0070039	best32. ;	
        informat	  PCO0080001	best32. ;	
        informat	  PCO0080002	best32. ;	
        informat	  PCO0080003	best32. ;	
        informat	  PCO0080004	best32. ;	
        informat	  PCO0080005	best32. ;	
        informat	  PCO0080006	best32. ;	
        informat	  PCO0080007	best32. ;	
        informat	  PCO0080008	best32. ;	
        informat	  PCO0080009	best32. ;	
        informat	  PCO0080010	best32. ;	
        informat	  PCO0080011	best32. ;	
        informat	  PCO0080012	best32. ;	
        informat	  PCO0080013	best32. ;	
        informat	  PCO0080014	best32. ;	
        informat	  PCO0080015	best32. ;	
        informat	  PCO0080016	best32. ;	
        informat	  PCO0080017	best32. ;	
        informat	  PCO0080018	best32. ;	
        informat	  PCO0080019	best32. ;	
        informat	  PCO0080020	best32. ;	
        informat	  PCO0080021	best32. ;	
        informat	  PCO0080022	best32. ;	
        informat	  PCO0080023	best32. ;	
        informat	  PCO0080024	best32. ;	
        informat	  PCO0080025	best32. ;	
        informat	  PCO0080026	best32. ;	
        informat	  PCO0080027	best32. ;	
        informat	  PCO0080028	best32. ;	
        informat	  PCO0080029	best32. ;	
        informat	  PCO0080030	best32. ;	
        informat	  PCO0080031	best32. ;	
        informat	  PCO0080032	best32. ;	
        informat	  PCO0080033	best32. ;	
        informat	  PCO0080034	best32. ;	
        informat	  PCO0080035	best32. ;	
        informat	  PCO0080036	best32. ;	
        informat	  PCO0080037	best32. ;	
        informat	  PCO0080038	best32. ;	
        informat	  PCO0080039	best32. ;	
        informat	  PCO0090001	best32. ;	
        informat	  PCO0090002	best32. ;	
        informat	  PCO0090003	best32. ;	
        informat	  PCO0090004	best32. ;	
        informat	  PCO0090005	best32. ;	
        informat	  PCO0090006	best32. ;	
        informat	  PCO0090007	best32. ;	
        informat	  PCO0090008	best32. ;	
        informat	  PCO0090009	best32. ;	
        informat	  PCO0090010	best32. ;	
        informat	  PCO0090011	best32. ;	
        informat	  PCO0090012	best32. ;	
        informat	  PCO0090013	best32. ;	
        informat	  PCO0090014	best32. ;	
        informat	  PCO0090015	best32. ;	
        informat	  PCO0090016	best32. ;	
        informat	  PCO0090017	best32. ;	
        informat	  PCO0090018	best32. ;	
        informat	  PCO0090019	best32. ;	
        informat	  PCO0090020	best32. ;	
        informat	  PCO0090021	best32. ;	
        informat	  PCO0090022	best32. ;	
        informat	  PCO0090023	best32. ;	
        informat	  PCO0090024	best32. ;	
        informat	  PCO0090025	best32. ;	
        informat	  PCO0090026	best32. ;	
        informat	  PCO0090027	best32. ;	
        informat	  PCO0090028	best32. ;	
        informat	  PCO0090029	best32. ;	
        informat	  PCO0090030	best32. ;	
        informat	  PCO0090031	best32. ;	
        informat	  PCO0090032	best32. ;	
        informat	  PCO0090033	best32. ;	
        informat	  PCO0090034	best32. ;	
        informat	  PCO0090035	best32. ;	
        informat	  PCO0090036	best32. ;	
        informat	  PCO0090037	best32. ;	
        informat	  PCO0090038	best32. ;	
        informat	  PCO0090039	best32. ;	
        informat	  PCO0100001	best32. ;	
        informat	  PCO0100002	best32. ;	
        informat	  PCO0100003	best32. ;	
        informat	  PCO0100004	best32. ;	
        informat	  PCO0100005	best32. ;	
        informat	  PCO0100006	best32. ;	
        informat	  PCO0100007	best32. ;	
        informat	  PCO0100008	best32. ;	
        informat	  PCO0100009	best32. ;	
        informat	  PCO0100010	best32. ;	
        informat	  PCO0100011	best32. ;	
        informat	  PCO0100012	best32. ;	
        informat	  PCO0100013	best32. ;	
        informat	  PCO0100014	best32. ;	
        informat	  PCO0100015	best32. ;	
        informat	  PCO0100016	best32. ;	
        informat	  PCO0100017	best32. ;	
        informat	  PCO0100018	best32. ;	
        informat	  PCO0100019	best32. ;	
        informat	  PCO0100020	best32. ;	
        informat	  PCO0100021	best32. ;	
        informat	  PCO0100022	best32. ;	
        informat	  PCO0100023	best32. ;	
        informat	  PCO0100024	best32. ;	
        informat	  PCO0100025	best32. ;	
        informat	  PCO0100026	best32. ;	
        informat	  PCO0100027	best32. ;	
        informat	  PCO0100028	best32. ;	
        informat	  PCO0100029	best32. ;	
        informat	  PCO0100030	best32. ;	
        informat	  PCO0100031	best32. ;	
        informat	  PCO0100032	best32. ;	
        informat	  PCO0100033	best32. ;	
        informat	  PCO0100034	best32. ;	
        informat	  PCO0100035	best32. ;	
        informat	  PCO0100036	best32. ;	
        informat	  PCO0100037	best32. ;	
        informat	  PCO0100038	best32. ;	
        informat	  PCO0100039	best32. ;	
        informat	  H00010001 	best32. ;	
        informat	  H0020001 	best32. ;	
        informat	  H0020002 	best32. ;	
        informat	  H0020003 	best32. ;	
        informat	  H0020004 	best32. ;	
        informat	  H0020005 	best32. ;	
        informat	  H0020006 	best32. ;	
        informat	  H0030001 	best32. ;	
        informat	  H0030002 	best32. ;	
        informat	  H0030003 	best32. ;	
        informat	  H0040001 	best32. ;	
        informat	  H0040002 	best32. ;	
        informat	  H0040003 	best32. ;	
        informat	  H0040004 	best32. ;	
        informat	  H0050001 	best32. ;	
        informat	  H0050002 	best32. ;	
        informat	  H0050003 	best32. ;	
        informat	  H0050004 	best32. ;	
        informat	  H0050005 	best32. ;	
        informat	  H0050006 	best32. ;	
        informat	  H0050007 	best32. ;	
        informat	  H0050008 	best32. ;	
        informat	  H0060001 	best32. ;	
        informat	  H0060002 	best32. ;	
        informat	  H0060003 	best32. ;	
        informat	  H0060004 	best32. ;	
        informat	  H0060005 	best32. ;	
        informat	  H0060006 	best32. ;	
        informat	  H0060007 	best32. ;	
        informat	  H0060008 	best32. ;	
        informat	  H0070001 	best32. ;	
        informat	  H0070002 	best32. ;	
        informat	  H0070003 	best32. ;	
        informat	  H0070004 	best32. ;	
        informat	  H0070005 	best32. ;	
        informat	  H0070006 	best32. ;	
        informat	  H0070007 	best32. ;	
        informat	  H0070008 	best32. ;	
        informat	  H0070009 	best32. ;	
        informat	  H0070010 	best32. ;	
        informat	  H0070011 	best32. ;	
        informat	  H0070012 	best32. ;	
        informat	  H0070013 	best32. ;	
        informat	  H0070014 	best32. ;	
        informat	  H0070015 	best32. ;	
        informat	  H0070016 	best32. ;	
        informat	  H0070017 	best32. ;	
        informat	  H0080001 	best32. ;	
        informat	  H0080002 	best32. ;	
        informat	  H0080003 	best32. ;	
        informat	  H0080004 	best32. ;	
        informat	  H0080005 	best32. ;	
        informat	  H0080006 	best32. ;	
        informat	  H0080007 	best32. ;	
        informat	  H0090001 	best32. ;	
        informat	  H0090002 	best32. ;	
        informat	  H0090003 	best32. ;	
        informat	  H0090004 	best32. ;	
        informat	  H0090005 	best32. ;	
        informat	  H0090006 	best32. ;	
        informat	  H0090007 	best32. ;	
        informat	  H0090008 	best32. ;	
        informat	  H0090009 	best32. ;	
        informat	  H0090010 	best32. ;	
        informat	  H0090011 	best32. ;	
        informat	  H0090012 	best32. ;	
        informat	  H0090013 	best32. ;	
        informat	  H0090014 	best32. ;	
        informat	  H0090015 	best32. ;	
        informat	  H0100001 	best32. ;	
        informat	  H0110001 	best32. ;	
        informat	  H0110002 	best32. ;	
        informat	  H0110003 	best32. ;	
        informat	  H0110004 	best32. ;	
        informat	  H0120001 	best32. ;	
        informat	  H0120002 	best32. ;	
        informat	  H0120003 	best32. ;	
        informat	  H0130001 	best32. ;	
        informat	  H0130002 	best32. ;	
        informat	  H0130003 	best32. ;	
        informat	  H0130004 	best32. ;	
        informat	  H0130005 	best32. ;	
        informat	  H0130006 	best32. ;	
        informat	  H0130007 	best32. ;	
        informat	  H0130008 	best32. ;	
        informat	  H0140001 	best32. ;	
        informat	  H0140002 	best32. ;	
        informat	  H0140003 	best32. ;	
        informat	  H0140004 	best32. ;	
        informat	  H0140005 	best32. ;	
        informat	  H0140006 	best32. ;	
        informat	  H0140007 	best32. ;	
        informat	  H0140008 	best32. ;	
        informat	  H0140009 	best32. ;	
        informat	  H0140010 	best32. ;	
        informat	  H0140011 	best32. ;	
        informat	  H0140012 	best32. ;	
        informat	  H0140013 	best32. ;	
        informat	  H0140014 	best32. ;	
        informat	  H0140015 	best32. ;	
        informat	  H0140016 	best32. ;	
        informat	  H0140017 	best32. ;	
        informat	  H0150001 	best32. ;	
        informat	  H0150002 	best32. ;	
        informat	  H0150003 	best32. ;	
        informat	  H0150004 	best32. ;	
        informat	  H0150005 	best32. ;	
        informat	  H0150006 	best32. ;	
        informat	  H0150007 	best32. ;	
        informat	  H0160001 	best32. ;	
        informat	  H0160002 	best32. ;	
        informat	  H0160003 	best32. ;	
        informat	  H0160004 	best32. ;	
        informat	  H0160005 	best32. ;	
        informat	  H0160006 	best32. ;	
        informat	  H0160007 	best32. ;	
        informat	  H0160008 	best32. ;	
        informat	  H0160009 	best32. ;	
        informat	  H0160010 	best32. ;	
        informat	  H0160011 	best32. ;	
        informat	  H0160012 	best32. ;	
        informat	  H0160013 	best32. ;	
        informat	  H0160014 	best32. ;	
        informat	  H0160015 	best32. ;	
        informat	  H0160016 	best32. ;	
        informat	  H0160017 	best32. ;	
        informat	  H0170001 	best32. ;	
        informat	  H0170002 	best32. ;	
        informat	  H0170003 	best32. ;	
        informat	  H0170004 	best32. ;	
        informat	  H0170005 	best32. ;	
        informat	  H0170006 	best32. ;	
        informat	  H0170007 	best32. ;	
        informat	  H0170008 	best32. ;	
        informat	  H0170009 	best32. ;	
        informat	  H0170010 	best32. ;	
        informat	  H0170011 	best32. ;	
        informat	  H0170012 	best32. ;	
        informat	  H0170013 	best32. ;	
        informat	  H0170014 	best32. ;	
        informat	  H0170015 	best32. ;	
        informat	  H0170016 	best32. ;	
        informat	  H0170017 	best32. ;	
        informat	  H0170018 	best32. ;	
        informat	  H0170019 	best32. ;	
        informat	  H0170020 	best32. ;	
        informat	  H0170021 	best32. ;	
        informat	  H0180001 	best32. ;	
        informat	  H0180002 	best32. ;	
        informat	  H0180003 	best32. ;	
        informat	  H0180004 	best32. ;	
        informat	  H0180005 	best32. ;	
        informat	  H0180006 	best32. ;	
        informat	  H0180007 	best32. ;	
        informat	  H0180008 	best32. ;	
        informat	  H0180009 	best32. ;	
        informat	  H0180010 	best32. ;	
        informat	  H0180011 	best32. ;	
        informat	  H0180012 	best32. ;	
        informat	  H0180013 	best32. ;	
        informat	  H0180014 	best32. ;	
        informat	  H0180015 	best32. ;	
        informat	  H0180016 	best32. ;	
        informat	  H0180017 	best32. ;	
        informat	  H0180018 	best32. ;	
        informat	  H0180019 	best32. ;	
        informat	  H0180020 	best32. ;	
        informat	  H0180021 	best32. ;	
        informat	  H0180022 	best32. ;	
        informat	  H0180023 	best32. ;	
        informat	  H0180024 	best32. ;	
        informat	  H0180025 	best32. ;	
        informat	  H0180026 	best32. ;	
        informat	  H0180027 	best32. ;	
        informat	  H0180028 	best32. ;	
        informat	  H0180029 	best32. ;	
        informat	  H0180030 	best32. ;	
        informat	  H0180031 	best32. ;	
        informat	  H0180032 	best32. ;	
        informat	  H0180033 	best32. ;	
        informat	  H0180034 	best32. ;	
        informat	  H0180035 	best32. ;	
        informat	  H0180036 	best32. ;	
        informat	  H0180037 	best32. ;	
        informat	  H0180038 	best32. ;	
        informat	  H0180039 	best32. ;	
        informat	  H0180040 	best32. ;	
        informat	  H0180041 	best32. ;	
        informat	  H0180042 	best32. ;	
        informat	  H0180043 	best32. ;	
        informat	  H0180044 	best32. ;	
        informat	  H0180045 	best32. ;	
        informat	  H0180046 	best32. ;	
        informat	  H0180047 	best32. ;	
        informat	  H0180048 	best32. ;	
        informat	  H0180049 	best32. ;	
        informat	  H0180050 	best32. ;	
        informat	  H0180051 	best32. ;	
        informat	  H0180052 	best32. ;	
        informat	  H0180053 	best32. ;	
        informat	  H0180054 	best32. ;	
        informat	  H0180055 	best32. ;	
        informat	  H0180056 	best32. ;	
        informat	  H0180057 	best32. ;	
        informat	  H0180058 	best32. ;	
        informat	  H0180059 	best32. ;	
        informat	  H0180060 	best32. ;	
        informat	  H0180061 	best32. ;	
        informat	  H0180062 	best32. ;	
        informat	  H0180063 	best32. ;	
        informat	  H0180064 	best32. ;	
        informat	  H0180065 	best32. ;	
        informat	  H0180066 	best32. ;	
        informat	  H0180067 	best32. ;	
        informat	  H0180068 	best32. ;	
        informat	  H0180069 	best32. ;	
        informat	  H0190001 	best32. ;	
        informat	  H0190002 	best32. ;	
        informat	  H0190003 	best32. ;	
        informat	  H0190004 	best32. ;	
        informat	  H0190005 	best32. ;	
        informat	  H0190006 	best32. ;	
        informat	  H0190007 	best32. ;	
        informat	  H0200001 	best32. ;	
        informat	  H0200002 	best32. ;	
        informat	  H0200003 	best32. ;	
        informat	  H0210001 	best32. ;	
        informat	  H0210002 	best32. ;	
        informat	  H0210003 	best32. ;	
        informat	  H0220001 	best32. ;	
        informat	  H0220002 	best32. ;	
        informat	  H0220003 	best32. ;	
        informat	  H011A0001 	best32. ;	
        informat	  H011A0002 	best32. ;	
        informat	  H011A0003 	best32. ;	
        informat	  H011A0004 	best32. ;	
        informat	  H011B0001 	best32. ;	
        informat	  H011B0002 	best32. ;	
        informat	  H011B0003 	best32. ;	
        informat	  H011B0004 	best32. ;	
        informat	  H011C0001 	best32. ;	
        informat	  H011C0002 	best32. ;	
        informat	  H011C0003 	best32. ;	
        informat	  H011C0004 	best32. ;	
        informat	  H011D0001 	best32. ;	
        informat	  H011D0002 	best32. ;	
        informat	  H011D0003 	best32. ;	
        informat	  H011D0004 	best32. ;	
        informat	  H011E0001 	best32. ;	
        informat	  H011E0002 	best32. ;	
        informat	  H011E0003 	best32. ;	
        informat	  H011E0004 	best32. ;	
        informat	  H011F0001 	best32. ;	
        informat	  H011F0002 	best32. ;	
        informat	  H011F0003 	best32. ;	
        informat	  H011F0004 	best32. ;	
        informat	  H011G0001 	best32. ;	
        informat	  H011G0002 	best32. ;	
        informat	  H011G0003 	best32. ;	
        informat	  H011G0004 	best32. ;	
        informat	  H011H0001 	best32. ;	
        informat	  H011H0002 	best32. ;	
        informat	  H011H0003 	best32. ;	
        informat	  H011H0004 	best32. ;	
        informat	  H011I0001 	best32. ;	
        informat	  H011I0002 	best32. ;	
        informat	  H011I0003 	best32. ;	
        informat	  H011I0004 	best32. ;	
        informat	  H012A0001 	best32. ;	
        informat	  H012A0002 	best32. ;	
        informat	  H012A0003 	best32. ;	
        informat	  H012B0001 	best32. ;	
        informat	  H012B0002 	best32. ;	
        informat	  H012B0003 	best32. ;	
        informat	  H012C0001 	best32. ;	
        informat	  H012C0002 	best32. ;	
        informat	  H012C0003 	best32. ;	
        informat	  H012D0001 	best32. ;	
        informat	  H012D0002 	best32. ;	
        informat	  H012D0003 	best32. ;	
        informat	  H012E0001 	best32. ;	
        informat	  H012E0002 	best32. ;	
        informat	  H012E0003 	best32. ;	
        informat	  H012F0001 	best32. ;	
        informat	  H012F0002 	best32. ;	
        informat	  H012F0003 	best32. ;	
        informat	  H012G0001 	best32. ;	
        informat	  H012G0002 	best32. ;	
        informat	  H012G0003 	best32. ;	
        informat	  H012H0001 	best32. ;	
        informat	  H012H0002 	best32. ;	
        informat	  H012H0003 	best32. ;	
        informat	  H012I0001 	best32. ;	
        informat	  H012I0002 	best32. ;	
        informat	  H012I0003 	best32. ;	
        informat	  H016A0001 	best32. ;	
        informat	  H016A0002 	best32. ;	
        informat	  H016A0003 	best32. ;	
        informat	  H016A0004 	best32. ;	
        informat	  H016A0005 	best32. ;	
        informat	  H016A0006 	best32. ;	
        informat	  H016A0007 	best32. ;	
        informat	  H016A0008 	best32. ;	
        informat	  H016A0009 	best32. ;	
        informat	  H016A0010 	best32. ;	
        informat	  H016A0011 	best32. ;	
        informat	  H016A0012 	best32. ;	
        informat	  H016A0013 	best32. ;	
        informat	  H016A0014 	best32. ;	
        informat	  H016A0015 	best32. ;	
        informat	  H016A0016 	best32. ;	
        informat	  H016A0017 	best32. ;	
        informat	  H016B0001 	best32. ;	
        informat	  H016B0002 	best32. ;	
        informat	  H016B0003 	best32. ;	
        informat	  H016B0004 	best32. ;	
        informat	  H016B0005 	best32. ;	
        informat	  H016B0006 	best32. ;	
        informat	  H016B0007 	best32. ;	
        informat	  H016B0008 	best32. ;	
        informat	  H016B0009 	best32. ;	
        informat	  H016B0010 	best32. ;	
        informat	  H016B0011 	best32. ;	
        informat	  H016B0012 	best32. ;	
        informat	  H016B0013 	best32. ;	
        informat	  H016B0014 	best32. ;	
        informat	  H016B0015 	best32. ;	
        informat	  H016B0016 	best32. ;	
        informat	  H016B0017 	best32. ;	
        informat	  H016C0001 	best32. ;	
        informat	  H016C0002 	best32. ;	
        informat	  H016C0003 	best32. ;	
        informat	  H016C0004 	best32. ;	
        informat	  H016C0005 	best32. ;	
        informat	  H016C0006 	best32. ;	
        informat	  H016C0007 	best32. ;	
        informat	  H016C0008 	best32. ;	
        informat	  H016C0009 	best32. ;	
        informat	  H016C0010 	best32. ;	
        informat	  H016C0011 	best32. ;	
        informat	  H016C0012 	best32. ;	
        informat	  H016C0013 	best32. ;	
        informat	  H016C0014 	best32. ;	
        informat	  H016C0015 	best32. ;	
        informat	  H016C0016 	best32. ;	
        informat	  H016C0017 	best32. ;	
        informat	  H016D0001 	best32. ;	
        informat	  H016D0002 	best32. ;	
        informat	  H016D0003 	best32. ;	
        informat	  H016D0004 	best32. ;	
        informat	  H016D0005 	best32. ;	
        informat	  H016D0006 	best32. ;	
        informat	  H016D0007 	best32. ;	
        informat	  H016D0008 	best32. ;	
        informat	  H016D0009 	best32. ;	
        informat	  H016D0010 	best32. ;	
        informat	  H016D0011 	best32. ;	
        informat	  H016D0012 	best32. ;	
        informat	  H016D0013 	best32. ;	
        informat	  H016D0014 	best32. ;	
        informat	  H016D0015 	best32. ;	
        informat	  H016D0016 	best32. ;	
        informat	  H016D0017 	best32. ;	
        informat	  H016E0001 	best32. ;	
        informat	  H016E0002 	best32. ;	
        informat	  H016E0003 	best32. ;	
        informat	  H016E0004 	best32. ;	
        informat	  H016E0005 	best32. ;	
        informat	  H016E0006 	best32. ;	
        informat	  H016E0007 	best32. ;	
        informat	  H016E0008 	best32. ;	
        informat	  H016E0009 	best32. ;	
        informat	  H016E0010 	best32. ;	
        informat	  H016E0011 	best32. ;	
        informat	  H016E0012 	best32. ;	
        informat	  H016E0013 	best32. ;	
        informat	  H016E0014 	best32. ;	
        informat	  H016E0015 	best32. ;	
        informat	  H016E0016 	best32. ;	
        informat	  H016E0017 	best32. ;	
        informat	  H016F0001 	best32. ;	
        informat	  H016F0002 	best32. ;	
        informat	  H016F0003 	best32. ;	
        informat	  H016F0004 	best32. ;	
        informat	  H016F0005 	best32. ;	
        informat	  H016F0006 	best32. ;	
        informat	  H016F0007 	best32. ;	
        informat	  H016F0008 	best32. ;	
        informat	  H016F0009 	best32. ;	
        informat	  H016F0010 	best32. ;	
        informat	  H016F0011 	best32. ;	
        informat	  H016F0012 	best32. ;	
        informat	  H016F0013 	best32. ;	
        informat	  H016F0014 	best32. ;	
        informat	  H016F0015 	best32. ;	
        informat	  H016F0016 	best32. ;	
        informat	  H016F0017 	best32. ;	
        informat	  H016G0001 	best32. ;	
        informat	  H016G0002 	best32. ;	
        informat	  H016G0003 	best32. ;	
        informat	  H016G0004 	best32. ;	
        informat	  H016G0005 	best32. ;	
        informat	  H016G0006 	best32. ;	
        informat	  H016G0007 	best32. ;	
        informat	  H016G0008 	best32. ;	
        informat	  H016G0009 	best32. ;	
        informat	  H016G0010 	best32. ;	
        informat	  H016G0011 	best32. ;	
        informat	  H016G0012 	best32. ;	
        informat	  H016G0013 	best32. ;	
        informat	  H016G0014 	best32. ;	
        informat	  H016G0015 	best32. ;	
        informat	  H016G0016 	best32. ;	
        informat	  H016G0017 	best32. ;	
        informat	  H016H0001 	best32. ;	
        informat	  H016H0002 	best32. ;	
        informat	  H016H0003 	best32. ;	
        informat	  H016H0004 	best32. ;	
        informat	  H016H0005 	best32. ;	
        informat	  H016H0006 	best32. ;	
        informat	  H016H0007 	best32. ;	
        informat	  H016H0008 	best32. ;	
        informat	  H016H0009 	best32. ;	
        informat	  H016H0010 	best32. ;	
        informat	  H016H0011 	best32. ;	
        informat	  H016H0012 	best32. ;	
        informat	  H016H0013 	best32. ;	
        informat	  H016H0014 	best32. ;	
        informat	  H016H0015 	best32. ;	
        informat	  H016H0016 	best32. ;	
        informat	  H016H0017 	best32. ;	
        informat	  H016I0001 	best32. ;	
        informat	  H016I0002 	best32. ;	
        informat	  H016I0003 	best32. ;	
        informat	  H016I0004 	best32. ;	
        informat	  H016I0005 	best32. ;	
        informat	  H016I0006 	best32. ;	
        informat	  H016I0007 	best32. ;	
        informat	  H016I0008 	best32. ;	
        informat	  H016I0009 	best32. ;	
        informat	  H016I0010 	best32. ;	
        informat	  H016I0011 	best32. ;	
        informat	  H016I0012 	best32. ;	
        informat	  H016I0013 	best32. ;	
        informat	  H016I0014 	best32. ;	
        informat	  H016I0015 	best32. ;	
        informat	  H016I0016 	best32. ;	
        informat	  H016I0017 	best32. ;	
        informat	  H017A0001 	best32. ;	
        informat	  H017A0002 	best32. ;	
        informat	  H017A0003 	best32. ;	
        informat	  H017A0004 	best32. ;	
        informat	  H017A0005 	best32. ;	
        informat	  H017A0006 	best32. ;	
        informat	  H017A0007 	best32. ;	
        informat	  H017A0008 	best32. ;	
        informat	  H017A0009 	best32. ;	
        informat	  H017A0010 	best32. ;	
        informat	  H017A0011 	best32. ;	
        informat	  H017A0012 	best32. ;	
        informat	  H017A0013 	best32. ;	
        informat	  H017A0014 	best32. ;	
        informat	  H017A0015 	best32. ;	
        informat	  H017A0016 	best32. ;	
        informat	  H017A0017 	best32. ;	
        informat	  H017A0018 	best32. ;	
        informat	  H017A0019 	best32. ;	
        informat	  H017A0020 	best32. ;	
        informat	  H017A0021 	best32. ;	
        informat	  H017B0001 	best32. ;	
        informat	  H017B0002 	best32. ;	
        informat	  H017B0003 	best32. ;	
        informat	  H017B0004 	best32. ;	
        informat	  H017B0005 	best32. ;	
        informat	  H017B0006 	best32. ;	
        informat	  H017B0007 	best32. ;	
        informat	  H017B0008 	best32. ;	
        informat	  H017B0009 	best32. ;	
        informat	  H017B0010 	best32. ;	
        informat	  H017B0011 	best32. ;	
        informat	  H017B0012 	best32. ;	
        informat	  H017B0013 	best32. ;	
        informat	  H017B0014 	best32. ;	
        informat	  H017B0015 	best32. ;	
        informat	  H017B0016 	best32. ;	
        informat	  H017B0017 	best32. ;	
        informat	  H017B0018 	best32. ;	
        informat	  H017B0019 	best32. ;	
        informat	  H017B0020 	best32. ;	
        informat	  H017B0021 	best32. ;	
        informat	  H017C0001 	best32. ;	
        informat	  H017C0002 	best32. ;	
        informat	  H017C0003 	best32. ;	
        informat	  H017C0004 	best32. ;	
        informat	  H017C0005 	best32. ;	
        informat	  H017C0006 	best32. ;	
        informat	  H017C0007 	best32. ;	
        informat	  H017C0008 	best32. ;	
        informat	  H017C0009 	best32. ;	
        informat	  H017C0010 	best32. ;	
        informat	  H017C0011 	best32. ;	
        informat	  H017C0012 	best32. ;	
        informat	  H017C0013 	best32. ;	
        informat	  H017C0014 	best32. ;	
        informat	  H017C0015 	best32. ;	
        informat	  H017C0016 	best32. ;	
        informat	  H017C0017 	best32. ;	
        informat	  H017C0018 	best32. ;	
        informat	  H017C0019 	best32. ;	
        informat	  H017C0020 	best32. ;	
        informat	  H017C0021 	best32. ;	
        informat	  H017D0001 	best32. ;	
        informat	  H017D0002 	best32. ;	
        informat	  H017D0003 	best32. ;	
        informat	  H017D0004 	best32. ;	
        informat	  H017D0005 	best32. ;	
        informat	  H017D0006 	best32. ;	
        informat	  H017D0007 	best32. ;	
        informat	  H017D0008 	best32. ;	
        informat	  H017D0009 	best32. ;	
        informat	  H017D0010 	best32. ;	
        informat	  H017D0011 	best32. ;	
        informat	  H017D0012 	best32. ;	
        informat	  H017D0013 	best32. ;	
        informat	  H017D0014 	best32. ;	
        informat	  H017D0015 	best32. ;	
        informat	  H017D0016 	best32. ;	
        informat	  H017D0017 	best32. ;	
        informat	  H017D0018 	best32. ;	
        informat	  H017D0019 	best32. ;	
        informat	  H017D0020 	best32. ;	
        informat	  H017D0021 	best32. ;	
        informat	  H017E0001 	best32. ;	
        informat	  H017E0002 	best32. ;	
        informat	  H017E0003 	best32. ;	
        informat	  H017E0004 	best32. ;	
        informat	  H017E0005 	best32. ;	
        informat	  H017E0006 	best32. ;	
        informat	  H017E0007 	best32. ;	
        informat	  H017E0008 	best32. ;	
        informat	  H017E0009 	best32. ;	
        informat	  H017E0010 	best32. ;	
        informat	  H017E0011 	best32. ;	
        informat	  H017E0012 	best32. ;	
        informat	  H017E0013 	best32. ;	
        informat	  H017E0014 	best32. ;	
        informat	  H017E0015 	best32. ;	
        informat	  H017E0016 	best32. ;	
        informat	  H017E0017 	best32. ;	
        informat	  H017E0018 	best32. ;	
        informat	  H017E0019 	best32. ;	
        informat	  H017E0020 	best32. ;	
        informat	  H017E0021 	best32. ;	
        informat	  H017F0001 	best32. ;	
        informat	  H017F0002 	best32. ;	
        informat	  H017F0003 	best32. ;	
        informat	  H017F0004 	best32. ;	
        informat	  H017F0005 	best32. ;	
        informat	  H017F0006 	best32. ;	
        informat	  H017F0007 	best32. ;	
        informat	  H017F0008 	best32. ;	
        informat	  H017F0009 	best32. ;	
        informat	  H017F0010 	best32. ;	
        informat	  H017F0011 	best32. ;	
        informat	  H017F0012 	best32. ;	
        informat	  H017F0013 	best32. ;	
        informat	  H017F0014 	best32. ;	
        informat	  H017F0015 	best32. ;	
        informat	  H017F0016 	best32. ;	
        informat	  H017F0017 	best32. ;	
        informat	  H017F0018 	best32. ;	
        informat	  H017F0019 	best32. ;	
        informat	  H017F0020 	best32. ;	
        informat	  H017F0021 	best32. ;	
        informat	  H017G0001 	best32. ;	
        informat	  H017G0002 	best32. ;	
        informat	  H017G0003 	best32. ;	
        informat	  H017G0004 	best32. ;	
        informat	  H017G0005 	best32. ;	
        informat	  H017G0006 	best32. ;	
        informat	  H017G0007 	best32. ;	
        informat	  H017G0008 	best32. ;	
        informat	  H017G0009 	best32. ;	
        informat	  H017G0010 	best32. ;	
        informat	  H017G0011 	best32. ;	
        informat	  H017G0012 	best32. ;	
        informat	  H017G0013 	best32. ;	
        informat	  H017G0014 	best32. ;	
        informat	  H017G0015 	best32. ;	
        informat	  H017G0016 	best32. ;	
        informat	  H017G0017 	best32. ;	
        informat	  H017G0018 	best32. ;	
        informat	  H017G0019 	best32. ;	
        informat	  H017G0020 	best32. ;	
        informat	  H017G0021 	best32. ;	
        informat	  H017H0001 	best32. ;	
        informat	  H017H0002 	best32. ;	
        informat	  H017H0003 	best32. ;	
        informat	  H017H0004 	best32. ;	
        informat	  H017H0005 	best32. ;	
        informat	  H017H0006 	best32. ;	
        informat	  H017H0007 	best32. ;	
        informat	  H017H0008 	best32. ;	
        informat	  H017H0009 	best32. ;	
        informat	  H017H0010 	best32. ;	
        informat	  H017H0011 	best32. ;	
        informat	  H017H0012 	best32. ;	
        informat	  H017H0013 	best32. ;	
        informat	  H017H0014 	best32. ;	
        informat	  H017H0015 	best32. ;	
        informat	  H017H0016 	best32. ;	
        informat	  H017H0017 	best32. ;	
        informat	  H017H0018 	best32. ;	
        informat	  H017H0019 	best32. ;	
        informat	  H017H0020 	best32. ;	
        informat	  H017H0021 	best32. ;	
        informat	  H017I0001 	best32. ;	
        informat	  H017I0002 	best32. ;	
        informat	  H017I0003 	best32. ;	
        informat	  H017I0004 	best32. ;	
        informat	  H017I0005 	best32. ;	
        informat	  H017I0006 	best32. ;	
        informat	  H017I0007 	best32. ;	
        informat	  H017I0008 	best32. ;	
        informat	  H017I0009 	best32. ;	
        informat	  H017I0010 	best32. ;	
        informat	  H017I0011 	best32. ;	
        informat	  H017I0012 	best32. ;	
        informat	  H017I0013 	best32. ;	
        informat	  H017I0014 	best32. ;	
        informat	  H017I0015 	best32. ;	
        informat	  H017I0016 	best32. ;	
        informat	  H017I0017 	best32. ;	
        informat	  H017I0018 	best32. ;	
        informat	  H017I0019 	best32. ;	
        informat	  H017I0020 	best32. ;	
        informat	  H017I0021 	best32. ;	
        informat	  HCT0010001	best32. ;	
        informat	  HCT0010002	best32. ;	
        informat	  HCT0010003	best32. ;	
        informat	  HCT0010004	best32. ;	
        informat	  HCT0010005	best32. ;	
        informat	  HCT0010006	best32. ;	
        informat	  HCT0010007	best32. ;	
        informat	  HCT0010008	best32. ;	
        informat	  HCT0010009	best32. ;	
        informat	  HCT0010010	best32. ;	
        informat	  HCT0010011	best32. ;	
        informat	  HCT0010012	best32. ;	
        informat	  HCT0010013	best32. ;	
        informat	  HCT0010014	best32. ;	
        informat	  HCT0010015	best32. ;	
        informat	  HCT0010016	best32. ;	
        informat	  HCT0010017	best32. ;	
        informat	  HCT0010018	best32. ;	
        informat	  HCT0010019	best32. ;	
        informat	  HCT0010020	best32. ;	
        informat	  HCT0010021	best32. ;	
        informat	  HCT0010022	best32. ;	
        informat	  HCT0010023	best32. ;	
        informat	  HCT0010024	best32. ;	
        informat	  HCT0010025	best32. ;	
        informat	  HCT0010026	best32. ;	
        informat	  HCT0010027	best32. ;	
        informat	  HCT0010028	best32. ;	
        informat	  HCT0010029	best32. ;	
        informat	  HCT0010030	best32. ;	
        informat	  HCT0010031	best32. ;	
        informat	  HCT0010032	best32. ;	
        informat	  HCT0010033	best32. ;	
        informat	  HCT0010034	best32. ;	
        informat	  HCT0010035	best32. ;	
        informat	  HCT0020001	best32. ;	
        informat	  HCT0020002	best32. ;	
        informat	  HCT0020003	best32. ;	
        informat	  HCT0020004	best32. ;	
        informat	  HCT0020005	best32. ;	
        informat	  HCT0020006	best32. ;	
        informat	  HCT0020007	best32. ;	
        informat	  HCT0020008	best32. ;	
        informat	  HCT0020009	best32. ;	
        informat	  HCT0020010	best32. ;	
        informat	  HCT0020011	best32. ;	
        informat	  HCT0020012	best32. ;	
        informat	  HCT0020013	best32. ;	
        informat	  HCT0030001	best32. ;	
        informat	  HCT0030002	best32. ;	
        informat	  HCT0030003	best32. ;	
        informat	  HCT0030004	best32. ;	
        informat	  HCT0030005	best32. ;	
        informat	  HCT0030006	best32. ;	
        informat	  HCT0030007	best32. ;	
        informat	  HCT0030008	best32. ;	
        informat	  HCT0030009	best32. ;	
        informat	  HCT0030010	best32. ;	
        informat	  HCT0030011	best32. ;	
        informat	  HCT0030012	best32. ;	
        informat	  HCT0030013	best32. ;	
        informat	  HCT0040001	best32. ;	
        informat	  HCT0040002	best32. ;	
        informat	  HCT0040003	best32. ;	
        informat	  HCT0040004	best32. ;	
        informat	  HCT0040005	best32. ;	
        informat	  HCT0040006	best32. ;	
        informat	  HCT0040007	best32. ;	
        informat	  HCT0040008	best32. ;	
        informat	  HCT0040009	best32. ;	
        informat	  HCT0040010	best32. ;	
        informat	  HCT0040011	best32. ;	
        informat	  HCT0040012	best32. ;	
        informat	  HCT0040013	best32. ;	
        informat	  PCT0230001	best32. ;	
        informat	  PCT0230002	best32. ;	
        informat	  PCT0230003	best32. ;	
        informat	  PCT0230004	best32. ;	
        informat	  PCT0230005	best32. ;	
        informat	  PCT0230006	best32. ;	
        informat	  PCT0230007	best32. ;	
        informat	  PCT0230008	best32. ;	
        informat	  PCT0230009	best32. ;	
        informat	  PCT0230010	best32. ;	
        informat	  PCT0230011	best32. ;	
        informat	  PCT0230012	best32. ;	
        informat	  PCT0230013	best32. ;	
        informat	  PCT0230014	best32. ;	
        informat	  PCT0230015	best32. ;	
        informat	  PCT0230016	best32. ;	
        informat	  PCT0230017	best32. ;	
        informat	  PCT0230018	best32. ;	
        informat	  PCT0230019	best32. ;	
        informat	  PCT0230020	best32. ;	
        informat	  PCT0230021	best32. ;	
        informat	  PCT0230022	best32. ;	
        informat	  PCT0230023	best32. ;	
        informat	  PCT0230024	best32. ;	
        informat	  PCT0240001	best32. ;	
        informat	  PCT0240002	best32. ;	
        informat	  PCT0240003	best32. ;	
        informat	  PCT0240004	best32. ;	
        informat	  PCT0240005	best32. ;	
        informat	  PCT0240006	best32. ;	
        informat	  PCT0240007	best32. ;	
        informat	  PCT0240008	best32. ;	
        informat	  PCT0240009	best32. ;	
        informat	  PCT0240010	best32. ;	
        informat	  PCT0240011	best32. ;	
        informat	  PCT0240012	best32. ;	
        informat	  PCT0240013	best32. ;	
        informat	  PCT0240014	best32. ;	
        informat	  PCT0240015	best32. ;	
        informat	  PCT0240016	best32. ;	
        informat	  PCT0240017	best32. ;	
        informat	  PCT0240018	best32. ;	
        informat	  PCT0240019	best32. ;	
        informat	  PCT0240020	best32. ;	
        informat	  PCT0240021	best32. ;	
        informat	  PCT0240022	best32. ;	
        informat	  PCT0240023	best32. ;	
        format FILEID $6. ;			
        format STUSAB $2. ;			
        format SUMLEV $3. ;			
        format GEOCOMP $2. ;			
        format CHARITER $3. ;			
        format CIFSN $2. ;			
        format LOGRECNO best12. ;				
        format REGION $1. ;			
        format DIVISION $1. ;			
        format STATE $2. ;			
        format COUNTY $3. ;			
        format COUNTYCC $2. ;			
        format COUNTYSC $2. ;			
        format COUSUB $5. ;			
        format COUSUBCC $2. ;			
        format COUSUBSC $2. ;			
        format PLACE $5. ;			
        format PLACECC $2. ;			
        format PLACESC $2. ;			
        format TRACT $6. ;			
        format BLKGRP $1. ;			
        format BLOCK $4. ;			
        format IUC $2. ;			
        format CONCIT $5. ;			
        format CONCITCC $2. ;			
        format CONCITSC $2. ;			
        format AIANHH $4. ;			
        format AIANHHFP $5. ;			
        format AIANHHCC $2. ;			
        format AIHHTLI $1. ;			
        format AITSCE $3. ;			
        format AITS $5. ;			
        format AITSCC $2. ;			
        format TTRACT $6. ;			
        format TBLKGRP $1. ;			
        format ANRC $5. ;			
        format ANRCCC $2. ;			
        format CBSA $5. ;			
        format CBSASC $2. ;			
        format METDIV $5. ;			
        format CSA $3. ;			
        format NECTA $5. ;			
        format NECTASC $2. ;			
        format NECTADIV $5. ;			
        format CNECTA $3. ;			
        format CBSAPCI $1. ;			
        format NECTAPCI $1. ;			
        format UA $5. ;			
        format UASC $2. ;			
        format UATYPE $1. ;			
        format UR $1. ;			
        format CD $2. ;			
        format SLDU $3. ;			
        format SLDL $3. ;			
        format VTD $6. ;			
        format VTDI $1. ;			
        format RESERVE2 $3. ;			
        format ZCTA5 $5. ;			
        format SUBMCD $5. ;			
        format SUBMCDCC $2. ;			
        format SDELEM $5. ;			
        format SDSEC $5. ;			
        format SDUNI $5. ;			
        format AREALAND $14. ;			
        format AREAWATR $14. ;			
        format NAME $90. ;			
        format FUNCSTAT $1. ;			
        format GCUNI $1. ;			
        format POP100 best12. ;			
        format HU100 best12. ;			
        format INTPTLAT $11. ;			
        format INTPTLON $12. ;			
        format LSADC $2. ;			
        format PARTFLAG $1. ;			
        format RESERVE3 $6. ;			
        format UGA $5. ;			
        format STATENS $8. ;			
        format COUNTYNS $8. ;			
        format COUSUBNS $8. ;			
        format PLACENS $8. ;			
        format CONCITNS $8. ;			
        format AIANHHNS $8. ;			
        format AITSNS $8. ;			
        format ANRCNS $8. ;			
        format SUBMCDNS $8. ;			
        format CD113 $2. ;			
        format CD114 $2. ;			
        format CD115 $2. ;			
        format SLDU2 $3. ;			
        format SLDU3 $3. ;			
        format SLDU4 $3. ;			
        format SLDL2 $3. ;			
        format SLDL3 $3. ;			
        format SLDL4 $3. ;			
        format AIANHHSC $2. ;			
        format CSASC $2. ;			
        format CNECTASC $2. ;			
        format MEMI $1. ;			
        format NMEMI $1. ;			
        format PUMA $5. ;			
        format RESERVED $18. ;				
        format P0010001 best12. ;			
        format P0020001 best12. ;			
        format P0020002 best12. ;			
        format P0020003 best12. ;			
        format P0020004 best12. ;			
        format P0020005 best12. ;			
        format P0020006 best12. ;			
        format P0030001 best12. ;			
        format P0030002 best12. ;			
        format P0030003 best12. ;			
        format P0030004 best12. ;			
        format P0030005 best12. ;			
        format P0030006 best12. ;			
        format P0030007 best12. ;			
        format P0030008 best12. ;			
        format P0040001 best12. ;			
        format P0040002 best12. ;			
        format P0040003 best12. ;			
        format P0050001 best12. ;			
        format P0050002 best12. ;			
        format P0050003 best12. ;			
        format P0050004 best12. ;			
        format P0050005 best12. ;			
        format P0050006 best12. ;			
        format P0050007 best12. ;			
        format P0050008 best12. ;			
        format P0050009 best12. ;			
        format P0050010 best12. ;			
        format P0050011 best12. ;			
        format P0050012 best12. ;			
        format P0050013 best12. ;			
        format P0050014 best12. ;			
        format P0050015 best12. ;			
        format P0050016 best12. ;			
        format P0050017 best12. ;			
        format P0060001 best12. ;			
        format P0060002 best12. ;			
        format P0060003 best12. ;			
        format P0060004 best12. ;			
        format P0060005 best12. ;			
        format P0060006 best12. ;			
        format P0060007 best12. ;			
        format P0070001 best12. ;			
        format P0070002 best12. ;			
        format P0070003 best12. ;			
        format P0070004 best12. ;			
        format P0070005 best12. ;			
        format P0070006 best12. ;			
        format P0070007 best12. ;			
        format P0070008 best12. ;			
        format P0070009 best12. ;			
        format P0070010 best12. ;			
        format P0070011 best12. ;			
        format P0070012 best12. ;			
        format P0070013 best12. ;			
        format P0070014 best12. ;			
        format P0070015 best12. ;			
        format P0080001 best12. ;			
        format P0080002 best12. ;			
        format P0080003 best12. ;			
        format P0080004 best12. ;			
        format P0080005 best12. ;			
        format P0080006 best12. ;			
        format P0080007 best12. ;			
        format P0080008 best12. ;			
        format P0080009 best12. ;			
        format P0080010 best12. ;			
        format P0080011 best12. ;			
        format P0080012 best12. ;			
        format P0080013 best12. ;			
        format P0080014 best12. ;			
        format P0080015 best12. ;			
        format P0080016 best12. ;			
        format P0080017 best12. ;			
        format P0080018 best12. ;			
        format P0080019 best12. ;			
        format P0080020 best12. ;			
        format P0080021 best12. ;			
        format P0080022 best12. ;			
        format P0080023 best12. ;			
        format P0080024 best12. ;			
        format P0080025 best12. ;			
        format P0080026 best12. ;			
        format P0080027 best12. ;			
        format P0080028 best12. ;			
        format P0080029 best12. ;			
        format P0080030 best12. ;			
        format P0080031 best12. ;			
        format P0080032 best12. ;			
        format P0080033 best12. ;			
        format P0080034 best12. ;			
        format P0080035 best12. ;			
        format P0080036 best12. ;			
        format P0080037 best12. ;			
        format P0080038 best12. ;			
        format P0080039 best12. ;			
        format P0080040 best12. ;			
        format P0080041 best12. ;			
        format P0080042 best12. ;			
        format P0080043 best12. ;			
        format P0080044 best12. ;			
        format P0080045 best12. ;			
        format P0080046 best12. ;			
        format P0080047 best12. ;			
        format P0080048 best12. ;			
        format P0080049 best12. ;			
        format P0080050 best12. ;			
        format P0080051 best12. ;			
        format P0080052 best12. ;			
        format P0080053 best12. ;			
        format P0080054 best12. ;			
        format P0080055 best12. ;			
        format P0080056 best12. ;			
        format P0080057 best12. ;			
        format P0080058 best12. ;			
        format P0080059 best12. ;			
        format P0080060 best12. ;			
        format P0080061 best12. ;			
        format P0080062 best12. ;			
        format P0080063 best12. ;			
        format P0080064 best12. ;			
        format P0080065 best12. ;			
        format P0080066 best12. ;			
        format P0080067 best12. ;			
        format P0080068 best12. ;			
        format P0080069 best12. ;			
        format P0080070 best12. ;			
        format P0080071 best12. ;			
        format P0090001 best12. ;			
        format P0090002 best12. ;			
        format P0090003 best12. ;			
        format P0090004 best12. ;			
        format P0090005 best12. ;			
        format P0090006 best12. ;			
        format P0090007 best12. ;			
        format P0090008 best12. ;			
        format P0090009 best12. ;			
        format P0090010 best12. ;			
        format P0090011 best12. ;			
        format P0090012 best12. ;			
        format P0090013 best12. ;			
        format P0090014 best12. ;			
        format P0090015 best12. ;			
        format P0090016 best12. ;			
        format P0090017 best12. ;			
        format P0090018 best12. ;			
        format P0090019 best12. ;			
        format P0090020 best12. ;			
        format P0090021 best12. ;			
        format P0090022 best12. ;			
        format P0090023 best12. ;			
        format P0090024 best12. ;			
        format P0090025 best12. ;			
        format P0090026 best12. ;			
        format P0090027 best12. ;			
        format P0090028 best12. ;			
        format P0090029 best12. ;			
        format P0090030 best12. ;			
        format P0090031 best12. ;			
        format P0090032 best12. ;			
        format P0090033 best12. ;			
        format P0090034 best12. ;			
        format P0090035 best12. ;			
        format P0090036 best12. ;			
        format P0090037 best12. ;			
        format P0090038 best12. ;			
        format P0090039 best12. ;			
        format P0090040 best12. ;			
        format P0090041 best12. ;			
        format P0090042 best12. ;			
        format P0090043 best12. ;			
        format P0090044 best12. ;			
        format P0090045 best12. ;			
        format P0090046 best12. ;			
        format P0090047 best12. ;			
        format P0090048 best12. ;			
        format P0090049 best12. ;			
        format P0090050 best12. ;			
        format P0090051 best12. ;			
        format P0090052 best12. ;			
        format P0090053 best12. ;			
        format P0090054 best12. ;			
        format P0090055 best12. ;			
        format P0090056 best12. ;			
        format P0090057 best12. ;			
        format P0090058 best12. ;			
        format P0090059 best12. ;			
        format P0090060 best12. ;			
        format P0090061 best12. ;			
        format P0090062 best12. ;			
        format P0090063 best12. ;			
        format P0090064 best12. ;			
        format P0090065 best12. ;			
        format P0090066 best12. ;			
        format P0090067 best12. ;			
        format P0090068 best12. ;			
        format P0090069 best12. ;			
        format P0090070 best12. ;			
        format P0090071 best12. ;			
        format P0090072 best12. ;			
        format P0090073 best12. ;			
        format P0100001 best12. ;			
        format P0100002 best12. ;			
        format P0100003 best12. ;			
        format P0100004 best12. ;			
        format P0100005 best12. ;			
        format P0100006 best12. ;			
        format P0100007 best12. ;			
        format P0100008 best12. ;			
        format P0100009 best12. ;			
        format P0100010 best12. ;			
        format P0100011 best12. ;			
        format P0100012 best12. ;			
        format P0100013 best12. ;			
        format P0100014 best12. ;			
        format P0100015 best12. ;			
        format P0100016 best12. ;			
        format P0100017 best12. ;			
        format P0100018 best12. ;			
        format P0100019 best12. ;			
        format P0100020 best12. ;			
        format P0100021 best12. ;			
        format P0100022 best12. ;			
        format P0100023 best12. ;			
        format P0100024 best12. ;			
        format P0100025 best12. ;			
        format P0100026 best12. ;			
        format P0100027 best12. ;			
        format P0100028 best12. ;			
        format P0100029 best12. ;			
        format P0100030 best12. ;			
        format P0100031 best12. ;			
        format P0100032 best12. ;			
        format P0100033 best12. ;			
        format P0100034 best12. ;			
        format P0100035 best12. ;			
        format P0100036 best12. ;			
        format P0100037 best12. ;			
        format P0100038 best12. ;			
        format P0100039 best12. ;			
        format P0100040 best12. ;			
        format P0100041 best12. ;			
        format P0100042 best12. ;			
        format P0100043 best12. ;			
        format P0100044 best12. ;			
        format P0100045 best12. ;			
        format P0100046 best12. ;			
        format P0100047 best12. ;			
        format P0100048 best12. ;			
        format P0100049 best12. ;			
        format P0100050 best12. ;			
        format P0100051 best12. ;			
        format P0100052 best12. ;			
        format P0100053 best12. ;			
        format P0100054 best12. ;			
        format P0100055 best12. ;			
        format P0100056 best12. ;			
        format P0100057 best12. ;			
        format P0100058 best12. ;			
        format P0100059 best12. ;			
        format P0100060 best12. ;			
        format P0100061 best12. ;			
        format P0100062 best12. ;			
        format P0100063 best12. ;			
        format P0100064 best12. ;			
        format P0100065 best12. ;			
        format P0100066 best12. ;			
        format P0100067 best12. ;			
        format P0100068 best12. ;			
        format P0100069 best12. ;			
        format P0100070 best12. ;			
        format P0100071 best12. ;			
        format P0110001 best12. ;			
        format P0110002 best12. ;			
        format P0110003 best12. ;			
        format P0110004 best12. ;			
        format P0110005 best12. ;			
        format P0110006 best12. ;			
        format P0110007 best12. ;			
        format P0110008 best12. ;			
        format P0110009 best12. ;			
        format P0110010 best12. ;			
        format P0110011 best12. ;			
        format P0110012 best12. ;			
        format P0110013 best12. ;			
        format P0110014 best12. ;			
        format P0110015 best12. ;			
        format P0110016 best12. ;			
        format P0110017 best12. ;			
        format P0110018 best12. ;			
        format P0110019 best12. ;			
        format P0110020 best12. ;			
        format P0110021 best12. ;			
        format P0110022 best12. ;			
        format P0110023 best12. ;			
        format P0110024 best12. ;			
        format P0110025 best12. ;			
        format P0110026 best12. ;			
        format P0110027 best12. ;			
        format P0110028 best12. ;			
        format P0110029 best12. ;			
        format P0110030 best12. ;			
        format P0110031 best12. ;			
        format P0110032 best12. ;			
        format P0110033 best12. ;			
        format P0110034 best12. ;			
        format P0110035 best12. ;			
        format P0110036 best12. ;			
        format P0110037 best12. ;			
        format P0110038 best12. ;			
        format P0110039 best12. ;			
        format P0110040 best12. ;			
        format P0110041 best12. ;			
        format P0110042 best12. ;			
        format P0110043 best12. ;			
        format P0110044 best12. ;			
        format P0110045 best12. ;			
        format P0110046 best12. ;			
        format P0110047 best12. ;			
        format P0110048 best12. ;			
        format P0110049 best12. ;			
        format P0110050 best12. ;			
        format P0110051 best12. ;			
        format P0110052 best12. ;			
        format P0110053 best12. ;			
        format P0110054 best12. ;			
        format P0110055 best12. ;			
        format P0110056 best12. ;			
        format P0110057 best12. ;			
        format P0110058 best12. ;			
        format P0110059 best12. ;			
        format P0110060 best12. ;			
        format P0110061 best12. ;			
        format P0110062 best12. ;			
        format P0110063 best12. ;			
        format P0110064 best12. ;			
        format P0110065 best12. ;			
        format P0110066 best12. ;			
        format P0110067 best12. ;			
        format P0110068 best12. ;			
        format P0110069 best12. ;			
        format P0110070 best12. ;			
        format P0110071 best12. ;			
        format P0110072 best12. ;			
        format P0110073 best12. ;			
        format P0120001 best12. ;			
        format P0120002 best12. ;			
        format P0120003 best12. ;			
        format P0120004 best12. ;			
        format P0120005 best12. ;			
        format P0120006 best12. ;			
        format P0120007 best12. ;			
        format P0120008 best12. ;			
        format P0120009 best12. ;			
        format P0120010 best12. ;			
        format P0120011 best12. ;			
        format P0120012 best12. ;			
        format P0120013 best12. ;			
        format P0120014 best12. ;			
        format P0120015 best12. ;			
        format P0120016 best12. ;			
        format P0120017 best12. ;			
        format P0120018 best12. ;			
        format P0120019 best12. ;			
        format P0120020 best12. ;			
        format P0120021 best12. ;			
        format P0120022 best12. ;			
        format P0120023 best12. ;			
        format P0120024 best12. ;			
        format P0120025 best12. ;			
        format P0120026 best12. ;			
        format P0120027 best12. ;			
        format P0120028 best12. ;			
        format P0120029 best12. ;			
        format P0120030 best12. ;			
        format P0120031 best12. ;			
        format P0120032 best12. ;			
        format P0120033 best12. ;			
        format P0120034 best12. ;			
        format P0120035 best12. ;			
        format P0120036 best12. ;			
        format P0120037 best12. ;			
        format P0120038 best12. ;			
        format P0120039 best12. ;			
        format P0120040 best12. ;			
        format P0120041 best12. ;			
        format P0120042 best12. ;			
        format P0120043 best12. ;			
        format P0120044 best12. ;			
        format P0120045 best12. ;			
        format P0120046 best12. ;			
        format P0120047 best12. ;			
        format P0120048 best12. ;			
        format P0120049 best12. ;			
        format P0130001 best12. ;			
        format P0130002 best12. ;			
        format P0130003 best12. ;			
        format P0140001 best12. ;			
        format P0140002 best12. ;			
        format P0140003 best12. ;			
        format P0140004 best12. ;			
        format P0140005 best12. ;			
        format P0140006 best12. ;			
        format P0140007 best12. ;			
        format P0140008 best12. ;			
        format P0140009 best12. ;			
        format P0140010 best12. ;			
        format P0140011 best12. ;			
        format P0140012 best12. ;			
        format P0140013 best12. ;			
        format P0140014 best12. ;			
        format P0140015 best12. ;			
        format P0140016 best12. ;			
        format P0140017 best12. ;			
        format P0140018 best12. ;			
        format P0140019 best12. ;			
        format P0140020 best12. ;			
        format P0140021 best12. ;			
        format P0140022 best12. ;			
        format P0140023 best12. ;			
        format P0140024 best12. ;			
        format P0140025 best12. ;			
        format P0140026 best12. ;			
        format P0140027 best12. ;			
        format P0140028 best12. ;			
        format P0140029 best12. ;			
        format P0140030 best12. ;			
        format P0140031 best12. ;			
        format P0140032 best12. ;			
        format P0140033 best12. ;			
        format P0140034 best12. ;			
        format P0140035 best12. ;			
        format P0140036 best12. ;			
        format P0140037 best12. ;			
        format P0140038 best12. ;			
        format P0140039 best12. ;			
        format P0140040 best12. ;			
        format P0140041 best12. ;			
        format P0140042 best12. ;			
        format P0140043 best12. ;			
        format P0150001 best12. ;			
        format P0150002 best12. ;			
        format P0150003 best12. ;			
        format P0150004 best12. ;			
        format P0150005 best12. ;			
        format P0150006 best12. ;			
        format P0150007 best12. ;			
        format P0150008 best12. ;			
        format P0150009 best12. ;			
        format P0150010 best12. ;			
        format P0150011 best12. ;			
        format P0150012 best12. ;			
        format P0150013 best12. ;			
        format P0150014 best12. ;			
        format P0150015 best12. ;			
        format P0150016 best12. ;			
        format P0150017 best12. ;			
        format P0160001 best12. ;			
        format P0160002 best12. ;			
        format P0160003 best12. ;			
        format P0170001 best12. ;			
        format P0170002 best12. ;			
        format P0170003 best12. ;			
        format P0180001 best12. ;			
        format P0180002 best12. ;			
        format P0180003 best12. ;			
        format P0180004 best12. ;			
        format P0180005 best12. ;			
        format P0180006 best12. ;			
        format P0180007 best12. ;			
        format P0180008 best12. ;			
        format P0180009 best12. ;			
        format P0190001 best12. ;			
        format P0190002 best12. ;			
        format P0190003 best12. ;			
        format P0190004 best12. ;			
        format P0190005 best12. ;			
        format P0190006 best12. ;			
        format P0190007 best12. ;			
        format P0190008 best12. ;			
        format P0190009 best12. ;			
        format P0190010 best12. ;			
        format P0190011 best12. ;			
        format P0190012 best12. ;			
        format P0190013 best12. ;			
        format P0190014 best12. ;			
        format P0190015 best12. ;			
        format P0190016 best12. ;			
        format P0190017 best12. ;			
        format P0190018 best12. ;			
        format P0190019 best12. ;			
        format P0200001 best12. ;			
        format P0200002 best12. ;			
        format P0200003 best12. ;			
        format P0200004 best12. ;			
        format P0200005 best12. ;			
        format P0200006 best12. ;			
        format P0200007 best12. ;			
        format P0200008 best12. ;			
        format P0200009 best12. ;			
        format P0200010 best12. ;			
        format P0200011 best12. ;			
        format P0200012 best12. ;			
        format P0200013 best12. ;			
        format P0200014 best12. ;			
        format P0200015 best12. ;			
        format P0200016 best12. ;			
        format P0200017 best12. ;			
        format P0200018 best12. ;			
        format P0200019 best12. ;			
        format P0200020 best12. ;			
        format P0200021 best12. ;			
        format P0200022 best12. ;			
        format P0200023 best12. ;			
        format P0200024 best12. ;			
        format P0200025 best12. ;			
        format P0200026 best12. ;			
        format P0200027 best12. ;			
        format P0200028 best12. ;			
        format P0200029 best12. ;			
        format P0200030 best12. ;			
        format P0200031 best12. ;			
        format P0200032 best12. ;			
        format P0200033 best12. ;			
        format P0200034 best12. ;			
        format P0210001 best12. ;			
        format P0210002 best12. ;			
        format P0210003 best12. ;			
        format P0210004 best12. ;			
        format P0210005 best12. ;			
        format P0210006 best12. ;			
        format P0210007 best12. ;			
        format P0210008 best12. ;			
        format P0210009 best12. ;			
        format P0210010 best12. ;			
        format P0210011 best12. ;			
        format P0210012 best12. ;			
        format P0210013 best12. ;			
        format P0210014 best12. ;			
        format P0210015 best12. ;			
        format P0210016 best12. ;			
        format P0210017 best12. ;			
        format P0210018 best12. ;			
        format P0210019 best12. ;			
        format P0210020 best12. ;			
        format P0210021 best12. ;			
        format P0210022 best12. ;			
        format P0210023 best12. ;			
        format P0210024 best12. ;			
        format P0210025 best12. ;			
        format P0210026 best12. ;			
        format P0210027 best12. ;			
        format P0210028 best12. ;			
        format P0210029 best12. ;			
        format P0210030 best12. ;			
        format P0210031 best12. ;			
        format P0220001 best12. ;			
        format P0220002 best12. ;			
        format P0220003 best12. ;			
        format P0220004 best12. ;			
        format P0220005 best12. ;			
        format P0220006 best12. ;			
        format P0220007 best12. ;			
        format P0220008 best12. ;			
        format P0220009 best12. ;			
        format P0220010 best12. ;			
        format P0220011 best12. ;			
        format P0220012 best12. ;			
        format P0220013 best12. ;			
        format P0220014 best12. ;			
        format P0220015 best12. ;			
        format P0220016 best12. ;			
        format P0220017 best12. ;			
        format P0220018 best12. ;			
        format P0220019 best12. ;			
        format P0220020 best12. ;			
        format P0220021 best12. ;			
        format P0230001 best12. ;			
        format P0230002 best12. ;			
        format P0230003 best12. ;			
        format P0230004 best12. ;			
        format P0230005 best12. ;			
        format P0230006 best12. ;			
        format P0230007 best12. ;			
        format P0230008 best12. ;			
        format P0230009 best12. ;			
        format P0230010 best12. ;			
        format P0230011 best12. ;			
        format P0230012 best12. ;			
        format P0230013 best12. ;			
        format P0230014 best12. ;			
        format P0230015 best12. ;			
        format P0240001 best12. ;			
        format P0240002 best12. ;			
        format P0240003 best12. ;			
        format P0240004 best12. ;			
        format P0240005 best12. ;			
        format P0240006 best12. ;			
        format P0240007 best12. ;			
        format P0240008 best12. ;			
        format P0240009 best12. ;			
        format P0240010 best12. ;			
        format P0240011 best12. ;			
        format P0250001 best12. ;			
        format P0250002 best12. ;			
        format P0250003 best12. ;			
        format P0250004 best12. ;			
        format P0250005 best12. ;			
        format P0250006 best12. ;			
        format P0250007 best12. ;			
        format P0250008 best12. ;			
        format P0250009 best12. ;			
        format P0250010 best12. ;			
        format P0250011 best12. ;			
        format P0260001 best12. ;			
        format P0260002 best12. ;			
        format P0260003 best12. ;			
        format P0260004 best12. ;			
        format P0260005 best12. ;			
        format P0260006 best12. ;			
        format P0260007 best12. ;			
        format P0260008 best12. ;			
        format P0260009 best12. ;			
        format P0260010 best12. ;			
        format P0260011 best12. ;			
        format P0270001 best12. ;			
        format P0270002 best12. ;			
        format P0270003 best12. ;			
        format P0280001 best12. ;			
        format P0280002 best12. ;			
        format P0280003 best12. ;			
        format P0280004 best12. ;			
        format P0280005 best12. ;			
        format P0280006 best12. ;			
        format P0280007 best12. ;			
        format P0280008 best12. ;			
        format P0280009 best12. ;			
        format P0280010 best12. ;			
        format P0280011 best12. ;			
        format P0280012 best12. ;			
        format P0280013 best12. ;			
        format P0280014 best12. ;			
        format P0280015 best12. ;			
        format P0280016 best12. ;			
        format P0290001 best12. ;			
        format P0290002 best12. ;			
        format P0290003 best12. ;			
        format P0290004 best12. ;			
        format P0290005 best12. ;			
        format P0290006 best12. ;			
        format P0290007 best12. ;			
        format P0290008 best12. ;			
        format P0290009 best12. ;			
        format P0290010 best12. ;			
        format P0290011 best12. ;			
        format P0290012 best12. ;			
        format P0290013 best12. ;			
        format P0290014 best12. ;			
        format P0290015 best12. ;			
        format P0290016 best12. ;			
        format P0290017 best12. ;			
        format P0290018 best12. ;			
        format P0290019 best12. ;			
        format P0290020 best12. ;			
        format P0290021 best12. ;			
        format P0290022 best12. ;			
        format P0290023 best12. ;			
        format P0290024 best12. ;			
        format P0290025 best12. ;			
        format P0290026 best12. ;			
        format P0290027 best12. ;			
        format P0290028 best12. ;			
        format P0300001 best12. ;			
        format P0300002 best12. ;			
        format P0300003 best12. ;			
        format P0300004 best12. ;			
        format P0300005 best12. ;			
        format P0300006 best12. ;			
        format P0300007 best12. ;			
        format P0300008 best12. ;			
        format P0300009 best12. ;			
        format P0300010 best12. ;			
        format P0300011 best12. ;			
        format P0300012 best12. ;			
        format P0300013 best12. ;			
        format P0310001 best12. ;			
        format P0310002 best12. ;			
        format P0310003 best12. ;			
        format P0310004 best12. ;			
        format P0310005 best12. ;			
        format P0310006 best12. ;			
        format P0310007 best12. ;			
        format P0310008 best12. ;			
        format P0310009 best12. ;			
        format P0310010 best12. ;			
        format P0310011 best12. ;			
        format P0310012 best12. ;			
        format P0310013 best12. ;			
        format P0310014 best12. ;			
        format P0310015 best12. ;			
        format P0310016 best12. ;			
        format P0320001 best12. ;			
        format P0320002 best12. ;			
        format P0320003 best12. ;			
        format P0320004 best12. ;			
        format P0320005 best12. ;			
        format P0320006 best12. ;			
        format P0320007 best12. ;			
        format P0320008 best12. ;			
        format P0320009 best12. ;			
        format P0320010 best12. ;			
        format P0320011 best12. ;			
        format P0320012 best12. ;			
        format P0320013 best12. ;			
        format P0320014 best12. ;			
        format P0320015 best12. ;			
        format P0320016 best12. ;			
        format P0320017 best12. ;			
        format P0320018 best12. ;			
        format P0320019 best12. ;			
        format P0320020 best12. ;			
        format P0320021 best12. ;			
        format P0320022 best12. ;			
        format P0320023 best12. ;			
        format P0320024 best12. ;			
        format P0320025 best12. ;			
        format P0320026 best12. ;			
        format P0320027 best12. ;			
        format P0320028 best12. ;			
        format P0320029 best12. ;			
        format P0320030 best12. ;			
        format P0320031 best12. ;			
        format P0320032 best12. ;			
        format P0320033 best12. ;			
        format P0320034 best12. ;			
        format P0320035 best12. ;			
        format P0320036 best12. ;			
        format P0320037 best12. ;			
        format P0320038 best12. ;			
        format P0320039 best12. ;			
        format P0320040 best12. ;			
        format P0320041 best12. ;			
        format P0320042 best12. ;			
        format P0320043 best12. ;			
        format P0320044 best12. ;			
        format P0320045 best12. ;			
        format P0330001 best12. ;			
        format P0330002 best12. ;			
        format P0330003 best12. ;			
        format P0330004 best12. ;			
        format P0330005 best12. ;			
        format P0330006 best12. ;			
        format P0330007 best12. ;			
        format P0340001 best12. ;			
        format P0340002 best12. ;			
        format P0340003 best12. ;			
        format P0340004 best12. ;			
        format P0340005 best12. ;			
        format P0340006 best12. ;			
        format P0340007 best12. ;			
        format P0340008 best12. ;			
        format P0340009 best12. ;			
        format P0340010 best12. ;			
        format P0340011 best12. ;			
        format P0340012 best12. ;			
        format P0340013 best12. ;			
        format P0340014 best12. ;			
        format P0340015 best12. ;			
        format P0340016 best12. ;			
        format P0340017 best12. ;			
        format P0340018 best12. ;			
        format P0340019 best12. ;			
        format P0340020 best12. ;			
        format P0340021 best12. ;			
        format P0340022 best12. ;			
        format P0350001 best12. ;			
        format P0360001 best12. ;			
        format P0360002 best12. ;			
        format P0360003 best12. ;			
        format P0370001 best12. ;			
        format P0370002 best12. ;			
        format P0370003 best12. ;			
        format P0380001 best12. ;			
        format P0380002 best12. ;			
        format P0380003 best12. ;			
        format P0380004 best12. ;			
        format P0380005 best12. ;			
        format P0380006 best12. ;			
        format P0380007 best12. ;			
        format P0380008 best12. ;			
        format P0380009 best12. ;			
        format P0380010 best12. ;			
        format P0380011 best12. ;			
        format P0380012 best12. ;			
        format P0380013 best12. ;			
        format P0380014 best12. ;			
        format P0380015 best12. ;			
        format P0380016 best12. ;			
        format P0380017 best12. ;			
        format P0380018 best12. ;			
        format P0380019 best12. ;			
        format P0380020 best12. ;			
        format P0390001 best12. ;			
        format P0390002 best12. ;			
        format P0390003 best12. ;			
        format P0390004 best12. ;			
        format P0390005 best12. ;			
        format P0390006 best12. ;			
        format P0390007 best12. ;			
        format P0390008 best12. ;			
        format P0390009 best12. ;			
        format P0390010 best12. ;			
        format P0390011 best12. ;			
        format P0390012 best12. ;			
        format P0390013 best12. ;			
        format P0390014 best12. ;			
        format P0390015 best12. ;			
        format P0390016 best12. ;			
        format P0390017 best12. ;			
        format P0390018 best12. ;			
        format P0390019 best12. ;			
        format P0390020 best12. ;			
        format P0400001 best12. ;			
        format P0400002 best12. ;			
        format P0400003 best12. ;			
        format P0400004 best12. ;			
        format P0400005 best12. ;			
         format P0400006 best12. ;			
         format P0400007 best12. ;			
         format P0400008 best12. ;			
         format P0400009 best12. ;			
         format P0400010 best12. ;			
         format P0400011 best12. ;			
         format P0400012 best12. ;			
         format P0400013 best12. ;			
         format P0400014 best12. ;			
         format P0400015 best12. ;			
         format P0400016 best12. ;			
         format P0400017 best12. ;			
         format P0400018 best12. ;			
         format P0400019 best12. ;			
         format P0400020 best12. ;			
         format P0410001 best12. ;			
         format P0410002 best12. ;			
         format P0410003 best12. ;			
         format P0410004 best12. ;			
         format P0410005 best12. ;			
         format P0410006 best12. ;			
         format P0420001 best12. ;			
         format P0420002 best12. ;			
         format P0420003 best12. ;			
         format P0420004 best12. ;			
         format P0420005 best12. ;			
         format P0420006 best12. ;			
         format P0420007 best12. ;			
         format P0420008 best12. ;			
         format P0420009 best12. ;			
         format P0420010 best12. ;			
         format P0430001 best12. ;			
         format P0430002 best12. ;			
         format P0430003 best12. ;			
         format P0430004 best12. ;			
         format P0430005 best12. ;			
         format P0430006 best12. ;			
         format P0430007 best12. ;			
         format P0430008 best12. ;			
         format P0430009 best12. ;			
         format P0430010 best12. ;			
         format P0430011 best12. ;			
         format P0430012 best12. ;			
         format P0430013 best12. ;			
         format P0430014 best12. ;			
         format P0430015 best12. ;			
         format P0430016 best12. ;			
         format P0430017 best12. ;			
         format P0430018 best12. ;			
         format P0430019 best12. ;			
         format P0430020 best12. ;			
         format P0430021 best12. ;			
         format P0430022 best12. ;			
         format P0430023 best12. ;			
         format P0430024 best12. ;			
         format P0430025 best12. ;			
         format P0430026 best12. ;			
         format P0430027 best12. ;			
         format P0430028 best12. ;			
         format P0430029 best12. ;			
         format P0430030 best12. ;			
         format P0430031 best12. ;			
         format P0430032 best12. ;			
         format P0430033 best12. ;			
         format P0430034 best12. ;			
         format P0430035 best12. ;			
         format P0430036 best12. ;			
         format P0430037 best12. ;			
         format P0430038 best12. ;			
         format P0430039 best12. ;			
         format P0430040 best12. ;			
         format P0430041 best12. ;			
         format P0430042 best12. ;			
         format P0430043 best12. ;			
         format P0430044 best12. ;			
         format P0430045 best12. ;			
         format P0430046 best12. ;			
         format P0430047 best12. ;			
         format P0430048 best12. ;			
         format P0430049 best12. ;			
         format P0430050 best12. ;			
         format P0430051 best12. ;			
         format P0430052 best12. ;			
         format P0430053 best12. ;			
         format P0430054 best12. ;			
         format P0430055 best12. ;			
         format P0430056 best12. ;			
         format P0430057 best12. ;			
         format P0430058 best12. ;			
         format P0430059 best12. ;			
         format P0430060 best12. ;			
         format P0430061 best12. ;			
         format P0430062 best12. ;			
         format P0430063 best12. ;			
         format P0440001 best12. ;			
         format P0440002 best12. ;			
         format P0440003 best12. ;			
         format P0450001 best12. ;			
         format P0450002 best12. ;			
         format P0450003 best12. ;			
         format P0460001 best12. ;			
         format P0460002 best12. ;			
         format P0460003 best12. ;			
         format P0470001 best12. ;			
         format P0470002 best12. ;			
         format P0470003 best12. ;			
         format P0480001 best12. ;			
         format P0480002 best12. ;			
         format P0480003 best12. ;			
         format P0490001 best12. ;			
         format P0490002 best12. ;			
         format P0490003 best12. ;			
         format P0500001 best12. ;			
         format P0500002 best12. ;			
         format P0500003 best12. ;			
         format P0510001 best12. ;			
         format P0510002 best12. ;			
         format P0510003 best12. ;			
         format P012A001 best12. ;			
         format P012A002 best12. ;			
         format P012A003 best12. ;			
         format P012A004 best12. ;			
         format P012A005 best12. ;			
         format P012A006 best12. ;			
         format P012A007 best12. ;			
         format P012A008 best12. ;			
         format P012A009 best12. ;			
         format P012A010 best12. ;			
         format P012A011 best12. ;			
         format P012A012 best12. ;			
         format P012A013 best12. ;			
         format P012A014 best12. ;			
         format P012A015 best12. ;			
         format P012A016 best12. ;			
         format P012A017 best12. ;			
         format P012A018 best12. ;			
         format P012A019 best12. ;			
         format P012A020 best12. ;			
         format P012A021 best12. ;			
         format P012A022 best12. ;			
         format P012A023 best12. ;			
         format P012A024 best12. ;			
         format P012A025 best12. ;			
         format P012A026 best12. ;			
         format P012A027 best12. ;			
         format P012A028 best12. ;			
         format P012A029 best12. ;			
         format P012A030 best12. ;			
         format P012A031 best12. ;			
         format P012A032 best12. ;			
         format P012A033 best12. ;			
         format P012A034 best12. ;			
         format P012A035 best12. ;			
         format P012A036 best12. ;			
         format P012A037 best12. ;			
         format P012A038 best12. ;			
         format P012A039 best12. ;			
         format P012A040 best12. ;			
         format P012A041 best12. ;			
         format P012A042 best12. ;			
         format P012A043 best12. ;			
         format P012A044 best12. ;			
         format P012A045 best12. ;			
         format P012A046 best12. ;			
         format P012A047 best12. ;			
         format P012A048 best12. ;			
         format P012A049 best12. ;			
         format P012B001 best12. ;			
         format P012B002 best12. ;			
         format P012B003 best12. ;			
         format P012B004 best12. ;			
         format P012B005 best12. ;			
         format P012B006 best12. ;			
         format P012B007 best12. ;			
         format P012B008 best12. ;			
         format P012B009 best12. ;			
         format P012B010 best12. ;			
         format P012B011 best12. ;			
         format P012B012 best12. ;			
         format P012B013 best12. ;			
         format P012B014 best12. ;			
         format P012B015 best12. ;			
         format P012B016 best12. ;			
         format P012B017 best12. ;			
         format P012B018 best12. ;			
         format P012B019 best12. ;			
         format P012B020 best12. ;			
         format P012B021 best12. ;			
         format P012B022 best12. ;			
         format P012B023 best12. ;			
         format P012B024 best12. ;			
         format P012B025 best12. ;			
         format P012B026 best12. ;			
         format P012B027 best12. ;			
         format P012B028 best12. ;			
         format P012B029 best12. ;			
         format P012B030 best12. ;			
         format P012B031 best12. ;			
         format P012B032 best12. ;			
         format P012B033 best12. ;			
         format P012B034 best12. ;			
         format P012B035 best12. ;			
         format P012B036 best12. ;			
         format P012B037 best12. ;			
         format P012B038 best12. ;			
         format P012B039 best12. ;			
         format P012B040 best12. ;			
         format P012B041 best12. ;			
         format P012B042 best12. ;			
         format P012B043 best12. ;			
         format P012B044 best12. ;			
         format P012B045 best12. ;			
         format P012B046 best12. ;			
         format P012B047 best12. ;			
         format P012B048 best12. ;			
         format P012B049 best12. ;			
         format P012C001 best12. ;			
         format P012C002 best12. ;			
         format P012C003 best12. ;			
         format P012C004 best12. ;			
         format P012C005 best12. ;			
         format P012C006 best12. ;			
         format P012C007 best12. ;			
         format P012C008 best12. ;			
         format P012C009 best12. ;			
         format P012C010 best12. ;			
         format P012C011 best12. ;			
         format P012C012 best12. ;			
         format P012C013 best12. ;			
         format P012C014 best12. ;			
         format P012C015 best12. ;			
         format P012C016 best12. ;			
         format P012C017 best12. ;			
         format P012C018 best12. ;			
         format P012C019 best12. ;			
         format P012C020 best12. ;			
         format P012C021 best12. ;			
         format P012C022 best12. ;			
         format P012C023 best12. ;			
         format P012C024 best12. ;			
         format P012C025 best12. ;			
         format P012C026 best12. ;			
         format P012C027 best12. ;			
         format P012C028 best12. ;			
         format P012C029 best12. ;			
         format P012C030 best12. ;			
         format P012C031 best12. ;			
         format P012C032 best12. ;			
         format P012C033 best12. ;			
         format P012C034 best12. ;			
         format P012C035 best12. ;			
         format P012C036 best12. ;			
         format P012C037 best12. ;			
         format P012C038 best12. ;			
         format P012C039 best12. ;			
         format P012C040 best12. ;			
         format P012C041 best12. ;			
         format P012C042 best12. ;			
         format P012C043 best12. ;			
         format P012C044 best12. ;			
         format P012C045 best12. ;			
         format P012C046 best12. ;			
         format P012C047 best12. ;			
         format P012C048 best12. ;			
         format P012C049 best12. ;			
         format P012D001 best12. ;			
         format P012D002 best12. ;			
         format P012D003 best12. ;			
         format P012D004 best12. ;			
         format P012D005 best12. ;			
         format P012D006 best12. ;			
         format P012D007 best12. ;			
         format P012D008 best12. ;			
         format P012D009 best12. ;			
         format P012D010 best12. ;			
         format P012D011 best12. ;			
         format P012D012 best12. ;			
         format P012D013 best12. ;			
         format P012D014 best12. ;			
         format P012D015 best12. ;			
         format P012D016 best12. ;			
         format P012D017 best12. ;			
         format P012D018 best12. ;			
         format P012D019 best12. ;			
         format P012D020 best12. ;			
         format P012D021 best12. ;			
         format P012D022 best12. ;			
         format P012D023 best12. ;			
         format P012D024 best12. ;			
         format P012D025 best12. ;			
         format P012D026 best12. ;			
         format P012D027 best12. ;			
         format P012D028 best12. ;			
         format P012D029 best12. ;			
         format P012D030 best12. ;			
         format P012D031 best12. ;			
         format P012D032 best12. ;			
         format P012D033 best12. ;			
         format P012D034 best12. ;			
         format P012D035 best12. ;			
         format P012D036 best12. ;			
         format P012D037 best12. ;			
         format P012D038 best12. ;			
         format P012D039 best12. ;			
         format P012D040 best12. ;			
         format P012D041 best12. ;			
         format P012D042 best12. ;			
         format P012D043 best12. ;			
         format P012D044 best12. ;			
         format P012D045 best12. ;			
         format P012D046 best12. ;			
         format P012D047 best12. ;			
         format P012D048 best12. ;			
         format P012D049 best12. ;			
         format P012E001 best12. ;			
         format P012E002 best12. ;			
         format P012E003 best12. ;			
         format P012E004 best12. ;			
         format P012E005 best12. ;			
         format P012E006 best12. ;			
         format P012E007 best12. ;			
         format P012E008 best12. ;			
         format P012E009 best12. ;			
         format P012E010 best12. ;			
         format P012E011 best12. ;			
         format P012E012 best12. ;			
         format P012E013 best12. ;			
         format P012E014 best12. ;			
         format P012E015 best12. ;			
         format P012E016 best12. ;			
         format P012E017 best12. ;			
         format P012E018 best12. ;			
         format P012E019 best12. ;			
         format P012E020 best12. ;			
         format P012E021 best12. ;			
         format P012E022 best12. ;			
         format P012E023 best12. ;			
         format P012E024 best12. ;			
         format P012E025 best12. ;			
         format P012E026 best12. ;			
         format P012E027 best12. ;			
         format P012E028 best12. ;			
         format P012E029 best12. ;			
         format P012E030 best12. ;			
         format P012E031 best12. ;			
         format P012E032 best12. ;			
         format P012E033 best12. ;			
         format P012E034 best12. ;			
         format P012E035 best12. ;			
         format P012E036 best12. ;			
         format P012E037 best12. ;			
         format P012E038 best12. ;			
         format P012E039 best12. ;			
         format P012E040 best12. ;			
         format P012E041 best12. ;			
         format P012E042 best12. ;			
         format P012E043 best12. ;			
         format P012E044 best12. ;			
         format P012E045 best12. ;			
         format P012E046 best12. ;			
         format P012E047 best12. ;			
         format P012E048 best12. ;			
         format P012E049 best12. ;			
         format P012F001 best12. ;			
         format P012F002 best12. ;			
         format P012F003 best12. ;			
         format P012F004 best12. ;			
         format P012F005 best12. ;			
         format P012F006 best12. ;			
         format P012F007 best12. ;			
         format P012F008 best12. ;			
         format P012F009 best12. ;			
         format P012F010 best12. ;			
         format P012F011 best12. ;			
         format P012F012 best12. ;			
         format P012F013 best12. ;			
         format P012F014 best12. ;			
         format P012F015 best12. ;			
         format P012F016 best12. ;			
         format P012F017 best12. ;			
         format P012F018 best12. ;			
         format P012F019 best12. ;			
         format P012F020 best12. ;			
         format P012F021 best12. ;			
         format P012F022 best12. ;			
         format P012F023 best12. ;			
         format P012F024 best12. ;			
         format P012F025 best12. ;			
         format P012F026 best12. ;			
         format P012F027 best12. ;			
         format P012F028 best12. ;			
         format P012F029 best12. ;			
         format P012F030 best12. ;			
         format P012F031 best12. ;			
         format P012F032 best12. ;			
         format P012F033 best12. ;			
         format P012F034 best12. ;			
         format P012F035 best12. ;			
         format P012F036 best12. ;			
         format P012F037 best12. ;			
         format P012F038 best12. ;			
         format P012F039 best12. ;			
         format P012F040 best12. ;			
         format P012F041 best12. ;			
         format P012F042 best12. ;			
         format P012F043 best12. ;			
         format P012F044 best12. ;			
         format P012F045 best12. ;			
         format P012F046 best12. ;			
         format P012F047 best12. ;			
         format P012F048 best12. ;			
         format P012F049 best12. ;			
         format P012G001 best12. ;			
         format P012G002 best12. ;			
         format P012G003 best12. ;			
         format P012G004 best12. ;			
         format P012G005 best12. ;			
         format P012G006 best12. ;			
         format P012G007 best12. ;			
         format P012G008 best12. ;			
         format P012G009 best12. ;			
         format P012G010 best12. ;			
         format P012G011 best12. ;			
         format P012G012 best12. ;			
         format P012G013 best12. ;			
         format P012G014 best12. ;			
         format P012G015 best12. ;			
         format P012G016 best12. ;			
         format P012G017 best12. ;			
         format P012G018 best12. ;			
         format P012G019 best12. ;			
         format P012G020 best12. ;			
         format P012G021 best12. ;			
         format P012G022 best12. ;			
         format P012G023 best12. ;			
         format P012G024 best12. ;			
         format P012G025 best12. ;			
         format P012G026 best12. ;			
         format P012G027 best12. ;			
         format P012G028 best12. ;			
         format P012G029 best12. ;			
         format P012G030 best12. ;			
         format P012G031 best12. ;			
         format P012G032 best12. ;			
         format P012G033 best12. ;			
         format P012G034 best12. ;			
         format P012G035 best12. ;			
         format P012G036 best12. ;			
         format P012G037 best12. ;			
         format P012G038 best12. ;			
         format P012G039 best12. ;			
         format P012G040 best12. ;			
         format P012G041 best12. ;			
         format P012G042 best12. ;			
         format P012G043 best12. ;			
         format P012G044 best12. ;			
         format P012G045 best12. ;			
         format P012G046 best12. ;			
         format P012G047 best12. ;			
         format P012G048 best12. ;			
         format P012G049 best12. ;			
         format P012H001 best12. ;			
         format P012H002 best12. ;			
         format P012H003 best12. ;			
         format P012H004 best12. ;			
         format P012H005 best12. ;			
         format P012H006 best12. ;			
         format P012H007 best12. ;			
         format P012H008 best12. ;			
         format P012H009 best12. ;			
         format P012H010 best12. ;			
         format P012H011 best12. ;			
         format P012H012 best12. ;			
         format P012H013 best12. ;			
         format P012H014 best12. ;			
         format P012H015 best12. ;			
         format P012H016 best12. ;			
         format P012H017 best12. ;			
         format P012H018 best12. ;			
         format P012H019 best12. ;			
         format P012H020 best12. ;			
         format P012H021 best12. ;			
         format P012H022 best12. ;			
         format P012H023 best12. ;			
         format P012H024 best12. ;			
         format P012H025 best12. ;			
         format P012H026 best12. ;			
         format P012H027 best12. ;			
         format P012H028 best12. ;			
         format P012H029 best12. ;			
         format P012H030 best12. ;			
         format P012H031 best12. ;			
         format P012H032 best12. ;			
         format P012H033 best12. ;			
         format P012H034 best12. ;			
         format P012H035 best12. ;			
         format P012H036 best12. ;			
         format P012H037 best12. ;			
         format P012H038 best12. ;			
         format P012H039 best12. ;			
         format P012H040 best12. ;			
         format P012H041 best12. ;			
         format P012H042 best12. ;			
         format P012H043 best12. ;			
         format P012H044 best12. ;			
         format P012H045 best12. ;			
         format P012H046 best12. ;			
         format P012H047 best12. ;			
         format P012H048 best12. ;			
         format P012H049 best12. ;			
         format P012I001 best12. ;			
         format P012I002 best12. ;			
         format P012I003 best12. ;			
         format P012I004 best12. ;			
         format P012I005 best12. ;			
         format P012I006 best12. ;			
         format P012I007 best12. ;			
         format P012I008 best12. ;			
         format P012I009 best12. ;			
         format P012I010 best12. ;			
         format P012I011 best12. ;			
         format P012I012 best12. ;			
         format P012I013 best12. ;			
         format P012I014 best12. ;			
         format P012I015 best12. ;			
         format P012I016 best12. ;			
         format P012I017 best12. ;			
         format P012I018 best12. ;			
         format P012I019 best12. ;			
         format P012I020 best12. ;			
         format P012I021 best12. ;			
         format P012I022 best12. ;			
         format P012I023 best12. ;			
         format P012I024 best12. ;			
         format P012I025 best12. ;			
         format P012I026 best12. ;			
         format P012I027 best12. ;			
         format P012I028 best12. ;			
         format P012I029 best12. ;			
         format P012I030 best12. ;			
         format P012I031 best12. ;			
         format P012I032 best12. ;			
         format P012I033 best12. ;			
         format P012I034 best12. ;			
         format P012I035 best12. ;			
         format P012I036 best12. ;			
         format P012I037 best12. ;			
         format P012I038 best12. ;			
         format P012I039 best12. ;			
         format P012I040 best12. ;			
         format P012I041 best12. ;			
         format P012I042 best12. ;			
         format P012I043 best12. ;			
         format P012I044 best12. ;			
         format P012I045 best12. ;			
         format P012I046 best12. ;			
         format P012I047 best12. ;			
         format P012I048 best12. ;			
         format P012I049 best12. ;			
         format P013A001 best12. ;			
         format P013A002 best12. ;			
         format P013A003 best12. ;			
         format P013B001 best12. ;			
         format P013B002 best12. ;			
         format P013B003 best12. ;			
         format P013C001 best12. ;			
         format P013C002 best12. ;			
         format P013C003 best12. ;			
         format P013D001 best12. ;			
         format P013D002 best12. ;			
         format P013D003 best12. ;			
         format P013E001 best12. ;			
         format P013E002 best12. ;			
         format P013E003 best12. ;			
         format P013F001 best12. ;			
         format P013F002 best12. ;			
         format P013F003 best12. ;			
         format P013G001 best12. ;			
         format P013G002 best12. ;			
         format P013G003 best12. ;			
         format P013H001 best12. ;			
         format P013H002 best12. ;			
         format P013H003 best12. ;			
         format P013I001 best12. ;			
         format P013I002 best12. ;			
         format P013I003 best12. ;			
         format P016A001 best12. ;			
         format P016A002 best12. ;			
         format P016A003 best12. ;			
         format P016B001 best12. ;			
         format P016B002 best12. ;			
         format P016B003 best12. ;			
         format P016C001 best12. ;			
         format P016C002 best12. ;			
         format P016C003 best12. ;			
         format P016D001 best12. ;			
         format P016D002 best12. ;			
         format P016D003 best12. ;			
         format P016E001 best12. ;			
         format P016E002 best12. ;			
         format P016E003 best12. ;			
         format P016F001 best12. ;			
         format P016F002 best12. ;			
         format P016F003 best12. ;			
         format P016G001 best12. ;			
         format P016G002 best12. ;			
         format P016G003 best12. ;			
         format P016H001 best12. ;			
         format P016H002 best12. ;			
         format P016H003 best12. ;			
         format P016I001 best12. ;			
         format P016I002 best12. ;			
         format P016I003 best12. ;			
         format P017A001 best12. ;			
         format P017A002 best12. ;			
         format P017A003 best12. ;			
         format P017B001 best12. ;			
         format P017B002 best12. ;			
         format P017B003 best12. ;			
         format P017C001 best12. ;			
         format P017C002 best12. ;			
         format P017C003 best12. ;			
         format P017D001 best12. ;			
         format P017D002 best12. ;			
         format P017D003 best12. ;			
         format P017E001 best12. ;			
         format P017E002 best12. ;			
         format P017E003 best12. ;			
         format P017F001 best12. ;			
         format P017F002 best12. ;			
         format P017F003 best12. ;			
         format P017G001 best12. ;			
         format P017G002 best12. ;			
         format P017G003 best12. ;			
         format P017H001 best12. ;			
         format P017H002 best12. ;			
         format P017H003 best12. ;			
         format P017I001 best12. ;			
         format P017I002 best12. ;			
         format P017I003 best12. ;			
         format P018A001 best12. ;			
         format P018A002 best12. ;			
         format P018A003 best12. ;			
         format P018A004 best12. ;			
         format P018A005 best12. ;			
         format P018A006 best12. ;			
         format P018A007 best12. ;			
         format P018A008 best12. ;			
         format P018A009 best12. ;			
         format P018B001 best12. ;			
         format P018B002 best12. ;			
         format P018B003 best12. ;			
         format P018B004 best12. ;			
         format P018B005 best12. ;			
         format P018B006 best12. ;			
         format P018B007 best12. ;			
         format P018B008 best12. ;			
         format P018B009 best12. ;			
         format P018C001 best12. ;			
         format P018C002 best12. ;			
         format P018C003 best12. ;			
         format P018C004 best12. ;			
         format P018C005 best12. ;			
         format P018C006 best12. ;			
         format P018C007 best12. ;			
         format P018C008 best12. ;			
         format P018C009 best12. ;			
         format P018D001 best12. ;			
         format P018D002 best12. ;			
         format P018D003 best12. ;			
         format P018D004 best12. ;			
         format P018D005 best12. ;			
         format P018D006 best12. ;			
         format P018D007 best12. ;			
         format P018D008 best12. ;			
         format P018D009 best12. ;			
         format P018E001 best12. ;			
         format P018E002 best12. ;			
         format P018E003 best12. ;			
         format P018E004 best12. ;			
         format P018E005 best12. ;			
         format P018E006 best12. ;			
         format P018E007 best12. ;			
         format P018E008 best12. ;			
         format P018E009 best12. ;			
         format P018F001 best12. ;			
         format P018F002 best12. ;			
         format P018F003 best12. ;			
         format P018F004 best12. ;			
         format P018F005 best12. ;			
         format P018F006 best12. ;			
         format P018F007 best12. ;			
         format P018F008 best12. ;			
         format P018F009 best12. ;			
         format P018G001 best12. ;			
         format P018G002 best12. ;			
         format P018G003 best12. ;			
         format P018G004 best12. ;			
         format P018G005 best12. ;			
         format P018G006 best12. ;			
         format P018G007 best12. ;			
         format P018G008 best12. ;			
         format P018G009 best12. ;			
         format P018H001 best12. ;			
         format P018H002 best12. ;			
         format P018H003 best12. ;			
         format P018H004 best12. ;			
         format P018H005 best12. ;			
         format P018H006 best12. ;			
         format P018H007 best12. ;			
         format P018H008 best12. ;			
         format P018H009 best12. ;			
         format P018I001 best12. ;			
         format P018I002 best12. ;			
         format P018I003 best12. ;			
         format P018I004 best12. ;			
         format P018I005 best12. ;			
         format P018I006 best12. ;			
         format P018I007 best12. ;			
         format P018I008 best12. ;			
         format P018I009 best12. ;			
         format P028A001 best12. ;			
         format P028A002 best12. ;			
         format P028A003 best12. ;			
         format P028A004 best12. ;			
         format P028A005 best12. ;			
         format P028A006 best12. ;			
         format P028A007 best12. ;			
         format P028A008 best12. ;			
         format P028A009 best12. ;			
         format P028A010 best12. ;			
         format P028A011 best12. ;			
         format P028A012 best12. ;			
         format P028A013 best12. ;			
         format P028A014 best12. ;			
         format P028A015 best12. ;			
         format P028A016 best12. ;			
         format P028B001 best12. ;			
         format P028B002 best12. ;			
         format P028B003 best12. ;			
         format P028B004 best12. ;			
         format P028B005 best12. ;			
         format P028B006 best12. ;			
         format P028B007 best12. ;			
         format P028B008 best12. ;			
         format P028B009 best12. ;			
         format P028B010 best12. ;			
         format P028B011 best12. ;			
         format P028B012 best12. ;			
         format P028B013 best12. ;			
         format P028B014 best12. ;			
         format P028B015 best12. ;			
         format P028B016 best12. ;			
         format P028C001 best12. ;			
         format P028C002 best12. ;			
         format P028C003 best12. ;			
         format P028C004 best12. ;			
         format P028C005 best12. ;			
         format P028C006 best12. ;			
         format P028C007 best12. ;			
         format P028C008 best12. ;			
         format P028C009 best12. ;			
         format P028C010 best12. ;			
         format P028C011 best12. ;			
         format P028C012 best12. ;			
         format P028C013 best12. ;			
         format P028C014 best12. ;			
         format P028C015 best12. ;			
         format P028C016 best12. ;			
         format P028D001 best12. ;			
         format P028D002 best12. ;			
         format P028D003 best12. ;			
         format P028D004 best12. ;			
         format P028D005 best12. ;			
         format P028D006 best12. ;			
         format P028D007 best12. ;			
         format P028D008 best12. ;			
         format P028D009 best12. ;			
         format P028D010 best12. ;			
         format P028D011 best12. ;			
         format P028D012 best12. ;			
         format P028D013 best12. ;			
         format P028D014 best12. ;			
         format P028D015 best12. ;			
         format P028D016 best12. ;			
         format P028E001 best12. ;			
         format P028E002 best12. ;			
         format P028E003 best12. ;			
         format P028E004 best12. ;			
         format P028E005 best12. ;			
         format P028E006 best12. ;			
         format P028E007 best12. ;			
         format P028E008 best12. ;			
         format P028E009 best12. ;			
         format P028E010 best12. ;			
         format P028E011 best12. ;			
         format P028E012 best12. ;			
         format P028E013 best12. ;			
         format P028E014 best12. ;			
         format P028E015 best12. ;			
         format P028E016 best12. ;			
         format P028F001 best12. ;			
         format P028F002 best12. ;			
         format P028F003 best12. ;			
         format P028F004 best12. ;			
         format P028F005 best12. ;			
         format P028F006 best12. ;			
         format P028F007 best12. ;			
         format P028F008 best12. ;			
         format P028F009 best12. ;			
         format P028F010 best12. ;			
         format P028F011 best12. ;			
         format P028F012 best12. ;			
         format P028F013 best12. ;			
         format P028F014 best12. ;			
         format P028F015 best12. ;			
         format P028F016 best12. ;			
         format P028G001 best12. ;			
         format P028G002 best12. ;			
         format P028G003 best12. ;			
         format P028G004 best12. ;			
         format P028G005 best12. ;			
         format P028G006 best12. ;			
         format P028G007 best12. ;			
         format P028G008 best12. ;			
         format P028G009 best12. ;			
         format P028G010 best12. ;			
         format P028G011 best12. ;			
         format P028G012 best12. ;			
         format P028G013 best12. ;			
         format P028G014 best12. ;			
         format P028G015 best12. ;			
         format P028G016 best12. ;			
         format P028H001 best12. ;			
         format P028H002 best12. ;			
         format P028H003 best12. ;			
         format P028H004 best12. ;			
         format P028H005 best12. ;			
         format P028H006 best12. ;			
         format P028H007 best12. ;			
         format P028H008 best12. ;			
         format P028H009 best12. ;			
         format P028H010 best12. ;			
         format P028H011 best12. ;			
         format P028H012 best12. ;			
         format P028H013 best12. ;			
         format P028H014 best12. ;			
         format P028H015 best12. ;			
         format P028H016 best12. ;			
         format P028I001 best12. ;			
         format P028I002 best12. ;			
         format P028I003 best12. ;			
         format P028I004 best12. ;			
         format P028I005 best12. ;			
         format P028I006 best12. ;			
         format P028I007 best12. ;			
         format P028I008 best12. ;			
         format P028I009 best12. ;			
         format P028I010 best12. ;			
         format P028I011 best12. ;			
         format P028I012 best12. ;			
         format P028I013 best12. ;			
         format P028I014 best12. ;			
         format P028I015 best12. ;			
         format P028I016 best12. ;			
         format P029A001 best12. ;			
         format P029A002 best12. ;			
         format P029A003 best12. ;			
         format P029A004 best12. ;			
         format P029A005 best12. ;			
         format P029A006 best12. ;			
         format P029A007 best12. ;			
         format P029A008 best12. ;			
         format P029A009 best12. ;			
         format P029A010 best12. ;			
         format P029A011 best12. ;			
         format P029A012 best12. ;			
         format P029A013 best12. ;			
         format P029A014 best12. ;			
         format P029A015 best12. ;			
         format P029A016 best12. ;			
         format P029A017 best12. ;			
         format P029A018 best12. ;			
         format P029A019 best12. ;			
         format P029A020 best12. ;			
         format P029A021 best12. ;			
         format P029A022 best12. ;			
         format P029A023 best12. ;			
         format P029A024 best12. ;			
         format P029A025 best12. ;			
         format P029A026 best12. ;			
         format P029A027 best12. ;			
         format P029A028 best12. ;			
         format P029B001 best12. ;			
         format P029B002 best12. ;			
         format P029B003 best12. ;			
         format P029B004 best12. ;			
         format P029B005 best12. ;			
         format P029B006 best12. ;			
         format P029B007 best12. ;			
         format P029B008 best12. ;			
         format P029B009 best12. ;			
         format P029B010 best12. ;			
         format P029B011 best12. ;			
         format P029B012 best12. ;			
         format P029B013 best12. ;			
         format P029B014 best12. ;			
         format P029B015 best12. ;			
         format P029B016 best12. ;			
         format P029B017 best12. ;			
         format P029B018 best12. ;			
         format P029B019 best12. ;			
         format P029B020 best12. ;			
         format P029B021 best12. ;			
         format P029B022 best12. ;			
         format P029B023 best12. ;			
         format P029B024 best12. ;			
         format P029B025 best12. ;			
         format P029B026 best12. ;			
         format P029B027 best12. ;			
         format P029B028 best12. ;			
         format P029C001 best12. ;			
         format P029C002 best12. ;			
         format P029C003 best12. ;			
         format P029C004 best12. ;			
         format P029C005 best12. ;			
         format P029C006 best12. ;			
         format P029C007 best12. ;			
         format P029C008 best12. ;			
         format P029C009 best12. ;			
         format P029C010 best12. ;			
         format P029C011 best12. ;			
         format P029C012 best12. ;			
         format P029C013 best12. ;			
         format P029C014 best12. ;			
         format P029C015 best12. ;			
         format P029C016 best12. ;			
         format P029C017 best12. ;			
         format P029C018 best12. ;			
         format P029C019 best12. ;			
         format P029C020 best12. ;			
         format P029C021 best12. ;			
         format P029C022 best12. ;			
         format P029C023 best12. ;			
         format P029C024 best12. ;			
         format P029C025 best12. ;			
         format P029C026 best12. ;			
         format P029C027 best12. ;			
         format P029C028 best12. ;			
         format P029D001 best12. ;			
         format P029D002 best12. ;			
         format P029D003 best12. ;			
         format P029D004 best12. ;			
         format P029D005 best12. ;			
         format P029D006 best12. ;			
         format P029D007 best12. ;			
         format P029D008 best12. ;			
         format P029D009 best12. ;			
         format P029D010 best12. ;			
         format P029D011 best12. ;			
         format P029D012 best12. ;			
         format P029D013 best12. ;			
         format P029D014 best12. ;			
         format P029D015 best12. ;			
         format P029D016 best12. ;			
         format P029D017 best12. ;			
         format P029D018 best12. ;			
         format P029D019 best12. ;			
         format P029D020 best12. ;			
         format P029D021 best12. ;			
         format P029D022 best12. ;			
         format P029D023 best12. ;			
         format P029D024 best12. ;			
         format P029D025 best12. ;			
         format P029D026 best12. ;			
         format P029D027 best12. ;			
         format P029D028 best12. ;			
         format P029E001 best12. ;			
         format P029E002 best12. ;			
         format P029E003 best12. ;			
         format P029E004 best12. ;			
         format P029E005 best12. ;			
         format P029E006 best12. ;			
         format P029E007 best12. ;			
         format P029E008 best12. ;			
         format P029E009 best12. ;			
         format P029E010 best12. ;			
         format P029E011 best12. ;			
         format P029E012 best12. ;			
         format P029E013 best12. ;			
         format P029E014 best12. ;			
         format P029E015 best12. ;			
         format P029E016 best12. ;			
         format P029E017 best12. ;			
         format P029E018 best12. ;			
         format P029E019 best12. ;			
         format P029E020 best12. ;			
         format P029E021 best12. ;			
         format P029E022 best12. ;			
         format P029E023 best12. ;			
         format P029E024 best12. ;			
         format P029E025 best12. ;			
         format P029E026 best12. ;			
         format P029E027 best12. ;			
         format P029E028 best12. ;			
         format P029F001 best12. ;			
         format P029F002 best12. ;			
         format P029F003 best12. ;			
         format P029F004 best12. ;			
         format P029F005 best12. ;			
         format P029F006 best12. ;			
         format P029F007 best12. ;			
         format P029F008 best12. ;			
         format P029F009 best12. ;			
         format P029F010 best12. ;			
         format P029F011 best12. ;			
         format P029F012 best12. ;			
         format P029F013 best12. ;			
         format P029F014 best12. ;			
         format P029F015 best12. ;			
         format P029F016 best12. ;			
         format P029F017 best12. ;			
         format P029F018 best12. ;			
         format P029F019 best12. ;			
         format P029F020 best12. ;			
         format P029F021 best12. ;			
         format P029F022 best12. ;			
         format P029F023 best12. ;			
         format P029F024 best12. ;			
         format P029F025 best12. ;			
         format P029F026 best12. ;			
         format P029F027 best12. ;			
         format P029F028 best12. ;			
         format P029G001 best12. ;			
         format P029G002 best12. ;			
         format P029G003 best12. ;			
         format P029G004 best12. ;			
         format P029G005 best12. ;			
         format P029G006 best12. ;			
         format P029G007 best12. ;			
         format P029G008 best12. ;			
         format P029G009 best12. ;			
         format P029G010 best12. ;			
         format P029G011 best12. ;			
         format P029G012 best12. ;			
         format P029G013 best12. ;			
         format P029G014 best12. ;			
         format P029G015 best12. ;			
         format P029G016 best12. ;			
         format P029G017 best12. ;			
         format P029G018 best12. ;			
         format P029G019 best12. ;			
         format P029G020 best12. ;			
         format P029G021 best12. ;			
         format P029G022 best12. ;			
         format P029G023 best12. ;			
         format P029G024 best12. ;			
         format P029G025 best12. ;			
         format P029G026 best12. ;			
         format P029G027 best12. ;			
         format P029G028 best12. ;			
         format P029H001 best12. ;			
         format P029H002 best12. ;			
         format P029H003 best12. ;			
         format P029H004 best12. ;			
         format P029H005 best12. ;			
         format P029H006 best12. ;			
         format P029H007 best12. ;			
         format P029H008 best12. ;			
         format P029H009 best12. ;			
         format P029H010 best12. ;			
         format P029H011 best12. ;			
         format P029H012 best12. ;			
         format P029H013 best12. ;			
         format P029H014 best12. ;			
         format P029H015 best12. ;			
         format P029H016 best12. ;			
         format P029H017 best12. ;			
         format P029H018 best12. ;			
         format P029H019 best12. ;			
         format P029H020 best12. ;			
         format P029H021 best12. ;			
         format P029H022 best12. ;			
         format P029H023 best12. ;			
         format P029H024 best12. ;			
         format P029H025 best12. ;			
         format P029H026 best12. ;			
         format P029H027 best12. ;			
         format P029H028 best12. ;			
         format P029I001 best12. ;			
         format P029I002 best12. ;			
         format P029I003 best12. ;			
         format P029I004 best12. ;			
         format P029I005 best12. ;			
         format P029I006 best12. ;			
         format P029I007 best12. ;			
         format P029I008 best12. ;			
         format P029I009 best12. ;			
         format P029I010 best12. ;			
         format P029I011 best12. ;			
         format P029I012 best12. ;			
         format P029I013 best12. ;			
         format P029I014 best12. ;			
         format P029I015 best12. ;			
         format P029I016 best12. ;			
         format P029I017 best12. ;			
         format P029I018 best12. ;			
         format P029I019 best12. ;			
         format P029I020 best12. ;			
         format P029I021 best12. ;			
         format P029I022 best12. ;			
         format P029I023 best12. ;			
         format P029I024 best12. ;			
         format P029I025 best12. ;			
         format P029I026 best12. ;			
         format P029I027 best12. ;			
         format P029I028 best12. ;			
         format P031A001 best12. ;			
         format P031A002 best12. ;			
         format P031A003 best12. ;			
         format P031A004 best12. ;			
         format P031A005 best12. ;			
         format P031A006 best12. ;			
         format P031A007 best12. ;			
         format P031A008 best12. ;			
         format P031A009 best12. ;			
         format P031A010 best12. ;			
         format P031A011 best12. ;			
         format P031A012 best12. ;			
         format P031A013 best12. ;			
         format P031A014 best12. ;			
         format P031A015 best12. ;			
         format P031A016 best12. ;			
         format P031B001 best12. ;			
         format P031B002 best12. ;			
         format P031B003 best12. ;			
         format P031B004 best12. ;			
         format P031B005 best12. ;			
         format P031B006 best12. ;			
         format P031B007 best12. ;			
         format P031B008 best12. ;			
         format P031B009 best12. ;			
         format P031B010 best12. ;			
         format P031B011 best12. ;			
         format P031B012 best12. ;			
         format P031B013 best12. ;			
         format P031B014 best12. ;			
         format P031B015 best12. ;			
         format P031B016 best12. ;			
         format P031C001 best12. ;			
         format P031C002 best12. ;			
         format P031C003 best12. ;			
         format P031C004 best12. ;			
         format P031C005 best12. ;			
         format P031C006 best12. ;			
         format P031C007 best12. ;			
         format P031C008 best12. ;			
         format P031C009 best12. ;			
         format P031C010 best12. ;			
         format P031C011 best12. ;			
         format P031C012 best12. ;			
         format P031C013 best12. ;			
         format P031C014 best12. ;			
         format P031C015 best12. ;			
         format P031C016 best12. ;			
         format P031D001 best12. ;			
         format P031D002 best12. ;			
         format P031D003 best12. ;			
         format P031D004 best12. ;			
         format P031D005 best12. ;			
         format P031D006 best12. ;			
         format P031D007 best12. ;			
         format P031D008 best12. ;			
         format P031D009 best12. ;			
         format P031D010 best12. ;			
         format P031D011 best12. ;			
         format P031D012 best12. ;			
         format P031D013 best12. ;			
         format P031D014 best12. ;			
         format P031D015 best12. ;			
         format P031D016 best12. ;			
         format P031E001 best12. ;			
         format P031E002 best12. ;			
         format P031E003 best12. ;			
         format P031E004 best12. ;			
         format P031E005 best12. ;			
         format P031E006 best12. ;			
         format P031E007 best12. ;			
         format P031E008 best12. ;			
         format P031E009 best12. ;			
         format P031E010 best12. ;			
         format P031E011 best12. ;			
         format P031E012 best12. ;			
         format P031E013 best12. ;			
         format P031E014 best12. ;			
         format P031E015 best12. ;			
         format P031E016 best12. ;			
         format P031F001 best12. ;			
         format P031F002 best12. ;			
         format P031F003 best12. ;			
         format P031F004 best12. ;			
         format P031F005 best12. ;			
         format P031F006 best12. ;			
         format P031F007 best12. ;			
         format P031F008 best12. ;			
         format P031F009 best12. ;			
         format P031F010 best12. ;			
         format P031F011 best12. ;			
         format P031F012 best12. ;			
         format P031F013 best12. ;			
         format P031F014 best12. ;			
         format P031F015 best12. ;			
         format P031F016 best12. ;			
         format P031G001 best12. ;			
         format P031G002 best12. ;			
         format P031G003 best12. ;			
         format P031G004 best12. ;			
         format P031G005 best12. ;			
         format P031G006 best12. ;			
         format P031G007 best12. ;			
         format P031G008 best12. ;			
         format P031G009 best12. ;			
         format P031G010 best12. ;			
         format P031G011 best12. ;			
         format P031G012 best12. ;			
         format P031G013 best12. ;			
         format P031G014 best12. ;			
         format P031G015 best12. ;			
         format P031G016 best12. ;			
         format P031H001 best12. ;			
         format P031H002 best12. ;			
         format P031H003 best12. ;			
         format P031H004 best12. ;			
         format P031H005 best12. ;			
         format P031H006 best12. ;			
         format P031H007 best12. ;			
         format P031H008 best12. ;			
         format P031H009 best12. ;			
         format P031H010 best12. ;			
         format P031H011 best12. ;			
         format P031H012 best12. ;			
         format P031H013 best12. ;			
         format P031H014 best12. ;			
         format P031H015 best12. ;			
         format P031H016 best12. ;			
         format P031I001 best12. ;			
         format P031I002 best12. ;			
         format P031I003 best12. ;			
         format P031I004 best12. ;			
         format P031I005 best12. ;			
         format P031I006 best12. ;			
         format P031I007 best12. ;			
         format P031I008 best12. ;			
         format P031I009 best12. ;			
         format P031I010 best12. ;			
         format P031I011 best12. ;			
         format P031I012 best12. ;			
         format P031I013 best12. ;			
         format P031I014 best12. ;			
         format P031I015 best12. ;			
         format P031I016 best12. ;			
         format P034A001 best12. ;			
         format P034A002 best12. ;			
         format P034A003 best12. ;			
         format P034A004 best12. ;			
         format P034A005 best12. ;			
         format P034A006 best12. ;			
         format P034A007 best12. ;			
         format P034A008 best12. ;			
         format P034A009 best12. ;			
         format P034A010 best12. ;			
         format P034A011 best12. ;			
         format P034A012 best12. ;			
         format P034A013 best12. ;			
         format P034A014 best12. ;			
         format P034A015 best12. ;			
         format P034A016 best12. ;			
         format P034A017 best12. ;			
         format P034A018 best12. ;			
         format P034A019 best12. ;			
         format P034A020 best12. ;			
         format P034A021 best12. ;			
         format P034A022 best12. ;			
         format P034B001 best12. ;			
         format P034B002 best12. ;			
         format P034B003 best12. ;			
         format P034B004 best12. ;			
         format P034B005 best12. ;			
         format P034B006 best12. ;			
         format P034B007 best12. ;			
         format P034B008 best12. ;			
         format P034B009 best12. ;			
         format P034B010 best12. ;			
         format P034B011 best12. ;			
         format P034B012 best12. ;			
         format P034B013 best12. ;			
         format P034B014 best12. ;			
         format P034B015 best12. ;			
         format P034B016 best12. ;			
         format P034B017 best12. ;			
         format P034B018 best12. ;			
         format P034B019 best12. ;			
         format P034B020 best12. ;			
         format P034B021 best12. ;			
         format P034B022 best12. ;			
         format P034C001 best12. ;			
         format P034C002 best12. ;			
         format P034C003 best12. ;			
         format P034C004 best12. ;			
         format P034C005 best12. ;			
         format P034C006 best12. ;			
         format P034C007 best12. ;			
         format P034C008 best12. ;			
         format P034C009 best12. ;			
         format P034C010 best12. ;			
         format P034C011 best12. ;			
         format P034C012 best12. ;			
         format P034C013 best12. ;			
         format P034C014 best12. ;			
         format P034C015 best12. ;			
         format P034C016 best12. ;			
         format P034C017 best12. ;			
         format P034C018 best12. ;			
         format P034C019 best12. ;			
         format P034C020 best12. ;			
         format P034C021 best12. ;			
         format P034C022 best12. ;			
         format P034D001 best12. ;			
         format P034D002 best12. ;			
         format P034D003 best12. ;			
         format P034D004 best12. ;			
         format P034D005 best12. ;			
         format P034D006 best12. ;			
         format P034D007 best12. ;			
         format P034D008 best12. ;			
         format P034D009 best12. ;			
         format P034D010 best12. ;			
         format P034D011 best12. ;			
         format P034D012 best12. ;			
         format P034D013 best12. ;			
         format P034D014 best12. ;			
         format P034D015 best12. ;			
         format P034D016 best12. ;			
         format P034D017 best12. ;			
         format P034D018 best12. ;			
         format P034D019 best12. ;			
         format P034D020 best12. ;			
         format P034D021 best12. ;			
         format P034D022 best12. ;			
         format P034E001 best12. ;			
         format P034E002 best12. ;			
         format P034E003 best12. ;			
         format P034E004 best12. ;			
         format P034E005 best12. ;			
         format P034E006 best12. ;			
         format P034E007 best12. ;			
         format P034E008 best12. ;			
         format P034E009 best12. ;			
         format P034E010 best12. ;			
         format P034E011 best12. ;			
         format P034E012 best12. ;			
         format P034E013 best12. ;			
         format P034E014 best12. ;			
         format P034E015 best12. ;			
         format P034E016 best12. ;			
         format P034E017 best12. ;			
         format P034E018 best12. ;			
         format P034E019 best12. ;			
         format P034E020 best12. ;			
         format P034E021 best12. ;			
         format P034E022 best12. ;			
         format P034F001 best12. ;			
         format P034F002 best12. ;			
         format P034F003 best12. ;			
         format P034F004 best12. ;			
         format P034F005 best12. ;			
         format P034F006 best12. ;			
         format P034F007 best12. ;			
         format P034F008 best12. ;			
         format P034F009 best12. ;			
         format P034F010 best12. ;			
         format P034F011 best12. ;			
         format P034F012 best12. ;			
         format P034F013 best12. ;			
         format P034F014 best12. ;			
         format P034F015 best12. ;			
         format P034F016 best12. ;			
         format P034F017 best12. ;			
         format P034F018 best12. ;			
         format P034F019 best12. ;			
         format P034F020 best12. ;			
         format P034F021 best12. ;			
         format P034F022 best12. ;			
         format P034G001 best12. ;			
         format P034G002 best12. ;			
         format P034G003 best12. ;			
         format P034G004 best12. ;			
         format P034G005 best12. ;			
         format P034G006 best12. ;			
         format P034G007 best12. ;			
         format P034G008 best12. ;			
         format P034G009 best12. ;			
         format P034G010 best12. ;			
         format P034G011 best12. ;			
         format P034G012 best12. ;			
         format P034G013 best12. ;			
         format P034G014 best12. ;			
         format P034G015 best12. ;			
         format P034G016 best12. ;			
         format P034G017 best12. ;			
         format P034G018 best12. ;			
         format P034G019 best12. ;			
         format P034G020 best12. ;			
         format P034G021 best12. ;			
         format P034G022 best12. ;			
         format P034H001 best12. ;			
         format P034H002 best12. ;			
         format P034H003 best12. ;			
         format P034H004 best12. ;			
         format P034H005 best12. ;			
         format P034H006 best12. ;			
         format P034H007 best12. ;			
         format P034H008 best12. ;			
         format P034H009 best12. ;			
         format P034H010 best12. ;			
         format P034H011 best12. ;			
         format P034H012 best12. ;			
         format P034H013 best12. ;			
         format P034H014 best12. ;			
         format P034H015 best12. ;			
         format P034H016 best12. ;			
         format P034H017 best12. ;			
         format P034H018 best12. ;			
         format P034H019 best12. ;			
         format P034H020 best12. ;			
         format P034H021 best12. ;			
         format P034H022 best12. ;			
         format P034I001 best12. ;			
         format P034I002 best12. ;			
         format P034I003 best12. ;			
         format P034I004 best12. ;			
         format P034I005 best12. ;			
         format P034I006 best12. ;			
         format P034I007 best12. ;			
         format P034I008 best12. ;			
         format P034I009 best12. ;			
         format P034I010 best12. ;			
         format P034I011 best12. ;			
         format P034I012 best12. ;			
         format P034I013 best12. ;			
         format P034I014 best12. ;			
         format P034I015 best12. ;			
         format P034I016 best12. ;			
         format P034I017 best12. ;			
         format P034I018 best12. ;			
         format P034I019 best12. ;			
         format P034I020 best12. ;			
         format P034I021 best12. ;			
         format P034I022 best12. ;			
         format P035A001 best12. ;			
         format P035B001 best12. ;			
         format P035C001 best12. ;			
         format P035D001 best12. ;			
         format P035E001 best12. ;			
         format P035F001 best12. ;			
         format P035G001 best12. ;			
         format P035H001 best12. ;			
         format P035I001 best12. ;			
         format P036A001 best12. ;			
         format P036A002 best12. ;			
         format P036A003 best12. ;			
         format P036B001 best12. ;			
         format P036B002 best12. ;			
         format P036B003 best12. ;			
         format P036C001 best12. ;			
         format P036C002 best12. ;			
         format P036C003 best12. ;			
         format P036D001 best12. ;			
         format P036D002 best12. ;			
         format P036D003 best12. ;			
         format P036E001 best12. ;			
         format P036E002 best12. ;			
         format P036E003 best12. ;			
         format P036F001 best12. ;			
         format P036F002 best12. ;			
         format P036F003 best12. ;			
         format P036G001 best12. ;			
         format P036G002 best12. ;			
         format P036G003 best12. ;			
         format P036H001 best12. ;			
         format P036H002 best12. ;			
         format P036H003 best12. ;			
         format P036I001 best12. ;			
         format P036I002 best12. ;			
         format P036I003 best12. ;			
         format P037A001 best12. ;			
         format P037A002 best12. ;			
         format P037A003 best12. ;			
         format P037B001 best12. ;			
         format P037B002 best12. ;			
         format P037B003 best12. ;			
         format P037C001 best12. ;			
         format P037C002 best12. ;			
         format P037C003 best12. ;			
         format P037D001 best12. ;			
         format P037D002 best12. ;			
         format P037D003 best12. ;			
         format P037E001 best12. ;			
         format P037E002 best12. ;			
         format P037E003 best12. ;			
         format P037F001 best12. ;			
         format P037F002 best12. ;			
         format P037F003 best12. ;			
         format P037G001 best12. ;			
         format P037G002 best12. ;			
         format P037G003 best12. ;			
         format P037H001 best12. ;			
         format P037H002 best12. ;			
         format P037H003 best12. ;			
         format P037I001 best12. ;			
         format P037I002 best12. ;			
         format P037I003 best12. ;			
         format P038A001 best12. ;			
         format P038A002 best12. ;			
         format P038A003 best12. ;			
         format P038A004 best12. ;			
         format P038A005 best12. ;			
         format P038A006 best12. ;			
         format P038A007 best12. ;			
         format P038A008 best12. ;			
         format P038A009 best12. ;			
         format P038A010 best12. ;			
         format P038A011 best12. ;			
         format P038A012 best12. ;			
         format P038A013 best12. ;			
         format P038A014 best12. ;			
         format P038A015 best12. ;			
         format P038A016 best12. ;			
         format P038A017 best12. ;			
         format P038A018 best12. ;			
         format P038A019 best12. ;			
         format P038A020 best12. ;			
         format P038B001 best12. ;			
         format P038B002 best12. ;			
         format P038B003 best12. ;			
         format P038B004 best12. ;			
         format P038B005 best12. ;			
         format P038B006 best12. ;			
         format P038B007 best12. ;			
         format P038B008 best12. ;			
         format P038B009 best12. ;			
         format P038B010 best12. ;			
         format P038B011 best12. ;			
         format P038B012 best12. ;			
         format P038B013 best12. ;			
         format P038B014 best12. ;			
         format P038B015 best12. ;			
         format P038B016 best12. ;			
         format P038B017 best12. ;			
         format P038B018 best12. ;			
         format P038B019 best12. ;			
         format P038B020 best12. ;			
         format P038C001 best12. ;			
         format P038C002 best12. ;			
         format P038C003 best12. ;			
         format P038C004 best12. ;			
         format P038C005 best12. ;			
         format P038C006 best12. ;			
         format P038C007 best12. ;			
         format P038C008 best12. ;			
         format P038C009 best12. ;			
         format P038C010 best12. ;			
         format P038C011 best12. ;			
         format P038C012 best12. ;			
         format P038C013 best12. ;			
         format P038C014 best12. ;			
         format P038C015 best12. ;			
         format P038C016 best12. ;			
         format P038C017 best12. ;			
         format P038C018 best12. ;			
         format P038C019 best12. ;			
         format P038C020 best12. ;			
         format P038D001 best12. ;			
         format P038D002 best12. ;			
         format P038D003 best12. ;			
         format P038D004 best12. ;			
         format P038D005 best12. ;			
         format P038D006 best12. ;			
         format P038D007 best12. ;			
         format P038D008 best12. ;			
         format P038D009 best12. ;			
         format P038D010 best12. ;			
         format P038D011 best12. ;			
         format P038D012 best12. ;			
         format P038D013 best12. ;			
         format P038D014 best12. ;			
         format P038D015 best12. ;			
         format P038D016 best12. ;			
         format P038D017 best12. ;			
         format P038D018 best12. ;			
         format P038D019 best12. ;			
         format P038D020 best12. ;			
         format P038E001 best12. ;			
         format P038E002 best12. ;			
         format P038E003 best12. ;			
         format P038E004 best12. ;			
         format P038E005 best12. ;			
         format P038E006 best12. ;			
         format P038E007 best12. ;			
         format P038E008 best12. ;			
         format P038E009 best12. ;			
         format P038E010 best12. ;			
         format P038E011 best12. ;			
         format P038E012 best12. ;			
         format P038E013 best12. ;			
         format P038E014 best12. ;			
         format P038E015 best12. ;			
         format P038E016 best12. ;			
         format P038E017 best12. ;			
         format P038E018 best12. ;			
         format P038E019 best12. ;			
         format P038E020 best12. ;			
         format P038F001 best12. ;			
         format P038F002 best12. ;			
         format P038F003 best12. ;			
         format P038F004 best12. ;			
         format P038F005 best12. ;			
         format P038F006 best12. ;			
         format P038F007 best12. ;			
         format P038F008 best12. ;			
         format P038F009 best12. ;			
         format P038F010 best12. ;			
         format P038F011 best12. ;			
         format P038F012 best12. ;			
         format P038F013 best12. ;			
         format P038F014 best12. ;			
         format P038F015 best12. ;			
         format P038F016 best12. ;			
         format P038F017 best12. ;			
         format P038F018 best12. ;			
         format P038F019 best12. ;			
         format P038F020 best12. ;			
         format P038G001 best12. ;			
         format P038G002 best12. ;			
         format P038G003 best12. ;			
         format P038G004 best12. ;			
         format P038G005 best12. ;			
         format P038G006 best12. ;			
         format P038G007 best12. ;			
         format P038G008 best12. ;			
         format P038G009 best12. ;			
         format P038G010 best12. ;			
         format P038G011 best12. ;			
         format P038G012 best12. ;			
         format P038G013 best12. ;			
         format P038G014 best12. ;			
         format P038G015 best12. ;			
         format P038G016 best12. ;			
         format P038G017 best12. ;			
         format P038G018 best12. ;			
         format P038G019 best12. ;			
         format P038G020 best12. ;			
         format P038H001 best12. ;			
         format P038H002 best12. ;			
         format P038H003 best12. ;			
         format P038H004 best12. ;			
         format P038H005 best12. ;			
         format P038H006 best12. ;			
         format P038H007 best12. ;			
         format P038H008 best12. ;			
         format P038H009 best12. ;			
         format P038H010 best12. ;			
         format P038H011 best12. ;			
         format P038H012 best12. ;			
         format P038H013 best12. ;			
         format P038H014 best12. ;			
         format P038H015 best12. ;			
         format P038H016 best12. ;			
         format P038H017 best12. ;			
         format P038H018 best12. ;			
         format P038H019 best12. ;			
         format P038H020 best12. ;			
         format P038I001 best12. ;			
         format P038I002 best12. ;			
         format P038I003 best12. ;			
         format P038I004 best12. ;			
         format P038I005 best12. ;			
         format P038I006 best12. ;			
         format P038I007 best12. ;			
         format P038I008 best12. ;			
         format P038I009 best12. ;			
         format P038I010 best12. ;			
         format P038I011 best12. ;			
         format P038I012 best12. ;			
         format P038I013 best12. ;			
         format P038I014 best12. ;			
         format P038I015 best12. ;			
         format P038I016 best12. ;			
         format P038I017 best12. ;			
         format P038I018 best12. ;			
         format P038I019 best12. ;			
         format P038I020 best12. ;			
         format P039A001 best12. ;			
         format P039A002 best12. ;			
         format P039A003 best12. ;			
         format P039A004 best12. ;			
         format P039A005 best12. ;			
         format P039A006 best12. ;			
         format P039A007 best12. ;			
         format P039A008 best12. ;			
         format P039A009 best12. ;			
         format P039A010 best12. ;			
         format P039A011 best12. ;			
         format P039A012 best12. ;			
         format P039A013 best12. ;			
         format P039A014 best12. ;			
         format P039A015 best12. ;			
         format P039A016 best12. ;			
         format P039A017 best12. ;			
         format P039A018 best12. ;			
         format P039A019 best12. ;			
         format P039A020 best12. ;			
         format P039B001 best12. ;			
         format P039B002 best12. ;			
         format P039B003 best12. ;			
         format P039B004 best12. ;			
         format P039B005 best12. ;			
         format P039B006 best12. ;			
         format P039B007 best12. ;			
         format P039B008 best12. ;			
         format P039B009 best12. ;			
         format P039B010 best12. ;			
         format P039B011 best12. ;			
         format P039B012 best12. ;			
         format P039B013 best12. ;			
         format P039B014 best12. ;			
         format P039B015 best12. ;			
         format P039B016 best12. ;			
         format P039B017 best12. ;			
         format P039B018 best12. ;			
         format P039B019 best12. ;			
         format P039B020 best12. ;			
         format P039C001 best12. ;			
         format P039C002 best12. ;			
         format P039C003 best12. ;			
         format P039C004 best12. ;			
         format P039C005 best12. ;			
         format P039C006 best12. ;			
         format P039C007 best12. ;			
         format P039C008 best12. ;			
         format P039C009 best12. ;			
         format P039C010 best12. ;			
         format P039C011 best12. ;			
         format P039C012 best12. ;			
         format P039C013 best12. ;			
         format P039C014 best12. ;			
         format P039C015 best12. ;			
         format P039C016 best12. ;			
         format P039C017 best12. ;			
         format P039C018 best12. ;			
         format P039C019 best12. ;			
         format P039C020 best12. ;			
         format P039D001 best12. ;			
         format P039D002 best12. ;			
         format P039D003 best12. ;			
         format P039D004 best12. ;			
         format P039D005 best12. ;			
         format P039D006 best12. ;			
         format P039D007 best12. ;			
         format P039D008 best12. ;			
         format P039D009 best12. ;			
         format P039D010 best12. ;			
         format P039D011 best12. ;			
         format P039D012 best12. ;			
         format P039D013 best12. ;			
         format P039D014 best12. ;			
         format P039D015 best12. ;			
         format P039D016 best12. ;			
         format P039D017 best12. ;			
         format P039D018 best12. ;			
         format P039D019 best12. ;			
         format P039D020 best12. ;			
         format P039E001 best12. ;			
         format P039E002 best12. ;			
         format P039E003 best12. ;			
         format P039E004 best12. ;			
         format P039E005 best12. ;			
         format P039E006 best12. ;			
         format P039E007 best12. ;			
         format P039E008 best12. ;			
         format P039E009 best12. ;			
         format P039E010 best12. ;			
         format P039E011 best12. ;			
         format P039E012 best12. ;			
         format P039E013 best12. ;			
         format P039E014 best12. ;			
         format P039E015 best12. ;			
         format P039E016 best12. ;			
         format P039E017 best12. ;			
         format P039E018 best12. ;			
         format P039E019 best12. ;			
         format P039E020 best12. ;			
         format P039F001 best12. ;			
         format P039F002 best12. ;			
         format P039F003 best12. ;			
         format P039F004 best12. ;			
         format P039F005 best12. ;			
         format P039F006 best12. ;			
         format P039F007 best12. ;			
         format P039F008 best12. ;			
         format P039F009 best12. ;			
         format P039F010 best12. ;			
         format P039F011 best12. ;			
         format P039F012 best12. ;			
         format P039F013 best12. ;			
         format P039F014 best12. ;			
         format P039F015 best12. ;			
         format P039F016 best12. ;			
         format P039F017 best12. ;			
         format P039F018 best12. ;			
         format P039F019 best12. ;			
         format P039F020 best12. ;			
         format P039G001 best12. ;			
         format P039G002 best12. ;			
         format P039G003 best12. ;			
         format P039G004 best12. ;			
         format P039G005 best12. ;			
         format P039G006 best12. ;			
         format P039G007 best12. ;			
         format P039G008 best12. ;			
         format P039G009 best12. ;			
         format P039G010 best12. ;			
         format P039G011 best12. ;			
         format P039G012 best12. ;			
         format P039G013 best12. ;			
         format P039G014 best12. ;			
         format P039G015 best12. ;			
         format P039G016 best12. ;			
         format P039G017 best12. ;			
         format P039G018 best12. ;			
         format P039G019 best12. ;			
         format P039G020 best12. ;			
         format P039H001 best12. ;			
         format P039H002 best12. ;			
         format P039H003 best12. ;			
         format P039H004 best12. ;			
         format P039H005 best12. ;			
         format P039H006 best12. ;			
         format P039H007 best12. ;			
         format P039H008 best12. ;			
         format P039H009 best12. ;			
         format P039H010 best12. ;			
         format P039H011 best12. ;			
         format P039H012 best12. ;			
         format P039H013 best12. ;			
         format P039H014 best12. ;			
         format P039H015 best12. ;			
         format P039H016 best12. ;			
         format P039H017 best12. ;			
         format P039H018 best12. ;			
         format P039H019 best12. ;			
         format P039H020 best12. ;			
         format P039I001 best12. ;			
         format P039I002 best12. ;			
         format P039I003 best12. ;			
         format P039I004 best12. ;			
         format P039I005 best12. ;			
         format P039I006 best12. ;			
         format P039I007 best12. ;			
         format P039I008 best12. ;			
         format P039I009 best12. ;			
         format P039I010 best12. ;			
         format P039I011 best12. ;			
         format P039I012 best12. ;			
         format P039I013 best12. ;			
         format P039I014 best12. ;			
         format P039I015 best12. ;			
         format P039I016 best12. ;			
         format P039I017 best12. ;			
         format P039I018 best12. ;			
         format P039I019 best12. ;			
         format P039I020 best12. ;			
         format PCT0010001 best12. ;			
         format PCT0010002 best12. ;			
         format PCT0010003 best12. ;			
         format PCT0010004 best12. ;			
         format PCT0010005 best12. ;			
         format PCT0010006 best12. ;			
         format PCT0010007 best12. ;			
         format PCT0010008 best12. ;			
         format PCT0010009 best12. ;			
         format PCT0010010 best12. ;			
         format PCT0010011 best12. ;			
         format PCT0010012 best12. ;			
         format PCT0010013 best12. ;			
         format PCT0010014 best12. ;			
         format PCT0010015 best12. ;			
         format PCT0010016 best12. ;			
         format PCT0010017 best12. ;			
         format PCT0010018 best12. ;			
         format PCT0010019 best12. ;			
         format PCT0010020 best12. ;			
         format PCT0010021 best12. ;			
         format PCT0010022 best12. ;			
         format PCT0010023 best12. ;			
         format PCT0010024 best12. ;			
         format PCT0010025 best12. ;			
         format PCT0010026 best12. ;			
         format PCT0010027 best12. ;			
         format PCT0010028 best12. ;			
         format PCT0010029 best12. ;			
         format PCT0010030 best12. ;			
         format PCT0010031 best12. ;			
         format PCT0010032 best12. ;			
         format PCT0010033 best12. ;			
         format PCT0010034 best12. ;			
         format PCT0010035 best12. ;			
         format PCT0010036 best12. ;			
         format PCT0010037 best12. ;			
         format PCT0010038 best12. ;			
         format PCT0010039 best12. ;			
         format PCT0010040 best12. ;			
         format PCT0010041 best12. ;			
         format PCT0010042 best12. ;			
         format PCT0010043 best12. ;			
         format PCT0010044 best12. ;			
         format PCT0010045 best12. ;			
         format PCT0010046 best12. ;			
         format PCT0010047 best12. ;			
         format PCT0010048 best12. ;			
         format PCT0010049 best12. ;			
         format PCT0010050 best12. ;			
         format PCT0010051 best12. ;			
         format PCT0010052 best12. ;			
         format PCT0010053 best12. ;			
         format PCT0010054 best12. ;			
         format PCT0020001 best12. ;			
         format PCT0020002 best12. ;			
         format PCT0020003 best12. ;			
         format PCT0020004 best12. ;			
         format PCT0020005 best12. ;			
         format PCT0020006 best12. ;			
         format PCT0020007 best12. ;			
         format PCT0020008 best12. ;			
         format PCT0020009 best12. ;			
         format PCT0020010 best12. ;			
         format PCT0020011 best12. ;			
         format PCT0020012 best12. ;			
         format PCT0020013 best12. ;			
         format PCT0020014 best12. ;			
         format PCT0020015 best12. ;			
         format PCT0020016 best12. ;			
         format PCT0020017 best12. ;			
         format PCT0020018 best12. ;			
         format PCT0020019 best12. ;			
         format PCT0020020 best12. ;			
         format PCT0020021 best12. ;			
         format PCT0020022 best12. ;			
         format PCT0020023 best12. ;			
         format PCT0020024 best12. ;			
         format PCT0020025 best12. ;			
         format PCT0020026 best12. ;			
         format PCT0020027 best12. ;			
         format PCT0020028 best12. ;			
         format PCT0020029 best12. ;			
         format PCT0020030 best12. ;			
         format PCT0020031 best12. ;			
         format PCT0020032 best12. ;			
         format PCT0020033 best12. ;			
         format PCT0020034 best12. ;			
         format PCT0020035 best12. ;			
         format PCT0020036 best12. ;			
         format PCT0020037 best12. ;			
         format PCT0020038 best12. ;			
         format PCT0020039 best12. ;			
         format PCT0020040 best12. ;			
         format PCT0020041 best12. ;			
         format PCT0020042 best12. ;			
         format PCT0020043 best12. ;			
         format PCT0020044 best12. ;			
         format PCT0020045 best12. ;			
         format PCT0020046 best12. ;			
         format PCT0020047 best12. ;			
         format PCT0020048 best12. ;			
         format PCT0020049 best12. ;			
         format PCT0020050 best12. ;			
         format PCT0020051 best12. ;			
         format PCT0020052 best12. ;			
         format PCT0020053 best12. ;			
         format PCT0020054 best12. ;			
         format PCT0030001 best12. ;			
         format PCT0030002 best12. ;			
         format PCT0030003 best12. ;			
         format PCT0030004 best12. ;			
         format PCT0030005 best12. ;			
         format PCT0030006 best12. ;			
         format PCT0030007 best12. ;			
         format PCT0030008 best12. ;			
         format PCT0030009 best12. ;			
         format PCT0030010 best12. ;			
         format PCT0030011 best12. ;			
         format PCT0030012 best12. ;			
         format PCT0030013 best12. ;			
         format PCT0030014 best12. ;			
         format PCT0030015 best12. ;			
         format PCT0030016 best12. ;			
         format PCT0030017 best12. ;			
         format PCT0030018 best12. ;			
         format PCT0030019 best12. ;			
         format PCT0030020 best12. ;			
         format PCT0030021 best12. ;			
         format PCT0030022 best12. ;			
         format PCT0030023 best12. ;			
         format PCT0030024 best12. ;			
         format PCT0030025 best12. ;			
         format PCT0030026 best12. ;			
         format PCT0030027 best12. ;			
         format PCT0030028 best12. ;			
         format PCT0030029 best12. ;			
         format PCT0030030 best12. ;			
         format PCT0030031 best12. ;			
         format PCT0030032 best12. ;			
         format PCT0030033 best12. ;			
         format PCT0030034 best12. ;			
         format PCT0030035 best12. ;			
         format PCT0030036 best12. ;			
         format PCT0030037 best12. ;			
         format PCT0030038 best12. ;			
         format PCT0030039 best12. ;			
         format PCT0030040 best12. ;			
         format PCT0030041 best12. ;			
         format PCT0030042 best12. ;			
         format PCT0030043 best12. ;			
         format PCT0030044 best12. ;			
         format PCT0030045 best12. ;			
         format PCT0030046 best12. ;			
         format PCT0030047 best12. ;			
         format PCT0030048 best12. ;			
         format PCT0030049 best12. ;			
         format PCT0030050 best12. ;			
         format 	  PCT0030051	best12. ;	
         format 	  PCT0030052	best12. ;	
         format 	  PCT0030053	best12. ;	
         format 	  PCT0030054	best12. ;	
         format 	  PCT0040001	best12. ;	
         format 	  PCT0040002	best12. ;	
         format 	  PCT0040003	best12. ;	
         format 	  PCT0040004	best12. ;	
         format 	  PCT0040005	best12. ;	
         format 	  PCT0040006	best12. ;	
         format 	  PCT0040007	best12. ;	
         format 	  PCT0040008	best12. ;	
         format 	  PCT0040009	best12. ;	
         format 	  PCT0050001	best12. ;	
         format 	  PCT0050002	best12. ;	
         format 	  PCT0050003	best12. ;	
         format 	  PCT0050004	best12. ;	
         format 	  PCT0050005	best12. ;	
         format 	  PCT0050006	best12. ;	
         format 	  PCT0050007	best12. ;	
         format 	  PCT0050008	best12. ;	
         format 	  PCT0050009	best12. ;	
         format 	  PCT0050010	best12. ;	
         format 	  PCT0050011	best12. ;	
         format 	  PCT0050012	best12. ;	
         format 	  PCT0050013	best12. ;	
         format 	  PCT0050014	best12. ;	
         format 	  PCT0050015	best12. ;	
         format 	  PCT0050016	best12. ;	
         format 	  PCT0050017	best12. ;	
         format 	  PCT0050018	best12. ;	
         format 	  PCT0050019	best12. ;	
         format 	  PCT0050020	best12. ;	
         format 	  PCT0050021	best12. ;	
         format 	  PCT0050022	best12. ;	
         format 	  PCT0060001	best12. ;	
         format 	  PCT0060002	best12. ;	
         format 	  PCT0060003	best12. ;	
         format 	  PCT0060004	best12. ;	
         format 	  PCT0060005	best12. ;	
         format 	  PCT0060006	best12. ;	
         format 	  PCT0060007	best12. ;	
         format 	  PCT0060008	best12. ;	
         format 	  PCT0060009	best12. ;	
         format 	  PCT0060010	best12. ;	
         format 	  PCT0060011	best12. ;	
         format 	  PCT0060012	best12. ;	
         format 	  PCT0060013	best12. ;	
         format 	  PCT0060014	best12. ;	
         format 	  PCT0060015	best12. ;	
         format 	  PCT0060016	best12. ;	
         format 	  PCT0060017	best12. ;	
         format 	  PCT0060018	best12. ;	
         format 	  PCT0060019	best12. ;	
         format 	  PCT0060020	best12. ;	
         format 	  PCT0060021	best12. ;	
         format 	  PCT0060022	best12. ;	
         format 	  PCT0070001	best12. ;	
         format 	  PCT0070002	best12. ;	
         format 	  PCT0070003	best12. ;	
         format 	  PCT0070004	best12. ;	
         format 	  PCT0070005	best12. ;	
         format 	  PCT0070006	best12. ;	
         format 	  PCT0070007	best12. ;	
         format 	  PCT0070008	best12. ;	
         format 	  PCT0070009	best12. ;	
         format 	  PCT0070010	best12. ;	
         format 	  PCT0070011	best12. ;	
         format 	  PCT0070012	best12. ;	
         format 	  PCT0070013	best12. ;	
         format 	  PCT0070014	best12. ;	
         format 	  PCT0070015	best12. ;	
         format 	  PCT0070016	best12. ;	
         format 	  PCT0070017	best12. ;	
         format 	  PCT0070018	best12. ;	
         format 	  PCT0070019	best12. ;	
         format 	  PCT0070020	best12. ;	
         format 	  PCT0070021	best12. ;	
         format 	  PCT0070022	best12. ;	
         format 	  PCT0080001	best12. ;	
         format 	  PCT0080002	best12. ;	
         format 	  PCT0080003	best12. ;	
         format 	  PCT0080004	best12. ;	
         format 	  PCT0080005	best12. ;	
         format 	  PCT0080006	best12. ;	
         format 	  PCT0080007	best12. ;	
         format 	  PCT0080008	best12. ;	
         format 	  PCT0080009	best12. ;	
         format 	  PCT0080010	best12. ;	
         format 	  PCT0080011	best12. ;	
         format 	  PCT0080012	best12. ;	
         format 	  PCT0080013	best12. ;	
         format 	  PCT0080014	best12. ;	
         format 	  PCT0090001	best12. ;	
         format 	  PCT0090002	best12. ;	
         format 	  PCT0090003	best12. ;	
         format 	  PCT0090004	best12. ;	
         format 	  PCT0090005	best12. ;	
         format 	  PCT0090006	best12. ;	
         format 	  PCT0090007	best12. ;	
         format 	  PCT0090008	best12. ;	
         format 	  PCT0090009	best12. ;	
         format 	  PCT0090010	best12. ;	
         format 	  PCT0090011	best12. ;	
         format 	  PCT0090012	best12. ;	
         format 	  PCT0090013	best12. ;	
         format 	  PCT0090014	best12. ;	
         format 	  PCT0100001	best12. ;	
         format 	  PCT0100002	best12. ;	
         format 	  PCT0100003	best12. ;	
         format 	  PCT0100004	best12. ;	
         format 	  PCT0100005	best12. ;	
         format 	  PCT0100006	best12. ;	
         format 	  PCT0100007	best12. ;	
         format 	  PCT0100008	best12. ;	
         format 	  PCT0100009	best12. ;	
         format 	  PCT0100010	best12. ;	
         format 	  PCT0100011	best12. ;	
         format 	  PCT0100012	best12. ;	
         format 	  PCT0100013	best12. ;	
         format 	  PCT0100014	best12. ;	
         format 	  PCT0110001	best12. ;	
         format 	  PCT0110002	best12. ;	
         format 	  PCT0110003	best12. ;	
         format 	  PCT0110004	best12. ;	
         format 	  PCT0110005	best12. ;	
         format 	  PCT0110006	best12. ;	
         format 	  PCT0110007	best12. ;	
         format 	  PCT0110008	best12. ;	
         format 	  PCT0110009	best12. ;	
         format 	  PCT0110010	best12. ;	
         format 	  PCT0110011	best12. ;	
         format 	  PCT0110012	best12. ;	
         format 	  PCT0110013	best12. ;	
         format 	  PCT0110014	best12. ;	
         format 	  PCT0110015	best12. ;	
         format 	  PCT0110016	best12. ;	
         format 	  PCT0110017	best12. ;	
         format 	  PCT0110018	best12. ;	
         format 	  PCT0110019	best12. ;	
         format 	  PCT0110020	best12. ;	
         format 	  PCT0110021	best12. ;	
         format 	  PCT0110022	best12. ;	
         format 	  PCT0110023	best12. ;	
         format 	  PCT0110024	best12. ;	
         format 	  PCT0110025	best12. ;	
         format 	  PCT0110026	best12. ;	
         format 	  PCT0110027	best12. ;	
         format 	  PCT0110028	best12. ;	
         format 	  PCT0110029	best12. ;	
         format 	  PCT0110030	best12. ;	
         format 	  PCT0110031	best12. ;	
         format 	  PCT0120001	best12. ;	
         format 	  PCT0120002	best12. ;	
         format 	  PCT0120003	best12. ;	
         format 	  PCT0120004	best12. ;	
         format 	  PCT0120005	best12. ;	
         format 	  PCT0120006	best12. ;	
         format 	  PCT0120007	best12. ;	
         format 	  PCT0120008	best12. ;	
         format 	  PCT0120009	best12. ;	
         format 	  PCT0120010	best12. ;	
         format 	  PCT0120011	best12. ;	
         format 	  PCT0120012	best12. ;	
         format 	  PCT0120013	best12. ;	
         format 	  PCT0120014	best12. ;	
         format 	  PCT0120015	best12. ;	
         format 	  PCT0120016	best12. ;	
         format 	  PCT0120017	best12. ;	
         format 	  PCT0120018	best12. ;	
         format 	  PCT0120019	best12. ;	
         format 	  PCT0120020	best12. ;	
         format 	  PCT0120021	best12. ;	
         format 	  PCT0120022	best12. ;	
         format 	  PCT0120023	best12. ;	
         format 	  PCT0120024	best12. ;	
         format 	  PCT0120025	best12. ;	
         format 	  PCT0120026	best12. ;	
         format 	  PCT0120027	best12. ;	
         format 	  PCT0120028	best12. ;	
         format 	  PCT0120029	best12. ;	
         format 	  PCT0120030	best12. ;	
         format 	  PCT0120031	best12. ;	
         format 	  PCT0120032	best12. ;	
         format 	  PCT0120033	best12. ;	
         format 	  PCT0120034	best12. ;	
         format 	  PCT0120035	best12. ;	
         format 	  PCT0120036	best12. ;	
         format 	  PCT0120037	best12. ;	
         format 	  PCT0120038	best12. ;	
         format 	  PCT0120039	best12. ;	
         format 	  PCT0120040	best12. ;	
         format 	  PCT0120041	best12. ;	
         format 	  PCT0120042	best12. ;	
         format 	  PCT0120043	best12. ;	
         format 	  PCT0120044	best12. ;	
         format 	  PCT0120045	best12. ;	
         format 	  PCT0120046	best12. ;	
         format 	  PCT0120047	best12. ;	
         format 	  PCT0120048	best12. ;	
         format 	  PCT0120049	best12. ;	
         format 	  PCT0120050	best12. ;	
         format 	  PCT0120051	best12. ;	
         format 	  PCT0120052	best12. ;	
         format 	  PCT0120053	best12. ;	
         format 	  PCT0120054	best12. ;	
         format 	  PCT0120055	best12. ;	
         format 	  PCT0120056	best12. ;	
         format 	  PCT0120057	best12. ;	
         format 	  PCT0120058	best12. ;	
         format 	  PCT0120059	best12. ;	
         format 	  PCT0120060	best12. ;	
         format 	  PCT0120061	best12. ;	
         format 	  PCT0120062	best12. ;	
         format 	  PCT0120063	best12. ;	
         format 	  PCT0120064	best12. ;	
         format 	  PCT0120065	best12. ;	
         format 	  PCT0120066	best12. ;	
         format 	  PCT0120067	best12. ;	
         format 	  PCT0120068	best12. ;	
         format 	  PCT0120069	best12. ;	
         format 	  PCT0120070	best12. ;	
         format 	  PCT0120071	best12. ;	
         format 	  PCT0120072	best12. ;	
         format 	  PCT0120073	best12. ;	
         format 	  PCT0120074	best12. ;	
         format 	  PCT0120075	best12. ;	
         format 	  PCT0120076	best12. ;	
         format 	  PCT0120077	best12. ;	
         format 	  PCT0120078	best12. ;	
         format 	  PCT0120079	best12. ;	
         format 	  PCT0120080	best12. ;	
         format 	  PCT0120081	best12. ;	
         format 	  PCT0120082	best12. ;	
         format 	  PCT0120083	best12. ;	
         format 	  PCT0120084	best12. ;	
         format 	  PCT0120085	best12. ;	
         format 	  PCT0120086	best12. ;	
         format 	  PCT0120087	best12. ;	
         format 	  PCT0120088	best12. ;	
         format 	  PCT0120089	best12. ;	
         format 	  PCT0120090	best12. ;	
         format 	  PCT0120091	best12. ;	
         format 	  PCT0120092	best12. ;	
         format 	  PCT0120093	best12. ;	
         format 	  PCT0120094	best12. ;	
         format 	  PCT0120095	best12. ;	
         format 	  PCT0120096	best12. ;	
         format 	  PCT0120097	best12. ;	
         format 	  PCT0120098	best12. ;	
         format 	  PCT0120099	best12. ;	
         format 	  PCT0120100	best12. ;	
         format 	  PCT0120101	best12. ;	
         format 	  PCT0120102	best12. ;	
         format 	  PCT0120103	best12. ;	
         format 	  PCT0120104	best12. ;	
         format 	  PCT0120105	best12. ;	
         format 	  PCT0120106	best12. ;	
         format 	  PCT0120107	best12. ;	
         format 	  PCT0120108	best12. ;	
         format 	  PCT0120109	best12. ;	
         format 	  PCT0120110	best12. ;	
         format 	  PCT0120111	best12. ;	
         format 	  PCT0120112	best12. ;	
         format 	  PCT0120113	best12. ;	
         format 	  PCT0120114	best12. ;	
         format 	  PCT0120115	best12. ;	
         format 	  PCT0120116	best12. ;	
         format 	  PCT0120117	best12. ;	
         format 	  PCT0120118	best12. ;	
         format 	  PCT0120119	best12. ;	
         format 	  PCT0120120	best12. ;	
         format 	  PCT0120121	best12. ;	
         format 	  PCT0120122	best12. ;	
         format 	  PCT0120123	best12. ;	
         format 	  PCT0120124	best12. ;	
         format 	  PCT0120125	best12. ;	
         format 	  PCT0120126	best12. ;	
         format 	  PCT0120127	best12. ;	
         format 	  PCT0120128	best12. ;	
         format 	  PCT0120129	best12. ;	
         format 	  PCT0120130	best12. ;	
         format 	  PCT0120131	best12. ;	
         format 	  PCT0120132	best12. ;	
         format 	  PCT0120133	best12. ;	
         format 	  PCT0120134	best12. ;	
         format 	  PCT0120135	best12. ;	
         format 	  PCT0120136	best12. ;	
         format 	  PCT0120137	best12. ;	
         format 	  PCT0120138	best12. ;	
         format 	  PCT0120139	best12. ;	
         format 	  PCT0120140	best12. ;	
         format 	  PCT0120141	best12. ;	
         format 	  PCT0120142	best12. ;	
         format 	  PCT0120143	best12. ;	
         format 	  PCT0120144	best12. ;	
         format 	  PCT0120145	best12. ;	
         format 	  PCT0120146	best12. ;	
         format 	  PCT0120147	best12. ;	
         format 	  PCT0120148	best12. ;	
         format 	  PCT0120149	best12. ;	
         format 	  PCT0120150	best12. ;	
         format 	  PCT0120151	best12. ;	
         format 	  PCT0120152	best12. ;	
         format 	  PCT0120153	best12. ;	
         format 	  PCT0120154	best12. ;	
         format 	  PCT0120155	best12. ;	
         format 	  PCT0120156	best12. ;	
         format 	  PCT0120157	best12. ;	
         format 	  PCT0120158	best12. ;	
         format 	  PCT0120159	best12. ;	
         format 	  PCT0120160	best12. ;	
         format 	  PCT0120161	best12. ;	
         format 	  PCT0120162	best12. ;	
         format 	  PCT0120163	best12. ;	
         format 	  PCT0120164	best12. ;	
         format 	  PCT0120165	best12. ;	
         format 	  PCT0120166	best12. ;	
         format 	  PCT0120167	best12. ;	
         format 	  PCT0120168	best12. ;	
         format 	  PCT0120169	best12. ;	
         format 	  PCT0120170	best12. ;	
         format 	  PCT0120171	best12. ;	
         format 	  PCT0120172	best12. ;	
         format 	  PCT0120173	best12. ;	
         format 	  PCT0120174	best12. ;	
         format 	  PCT0120175	best12. ;	
         format 	  PCT0120176	best12. ;	
         format 	  PCT0120177	best12. ;	
         format 	  PCT0120178	best12. ;	
         format 	  PCT0120179	best12. ;	
         format 	  PCT0120180	best12. ;	
         format 	  PCT0120181	best12. ;	
         format 	  PCT0120182	best12. ;	
         format 	  PCT0120183	best12. ;	
         format 	  PCT0120184	best12. ;	
         format 	  PCT0120185	best12. ;	
         format 	  PCT0120186	best12. ;	
         format 	  PCT0120187	best12. ;	
         format 	  PCT0120188	best12. ;	
         format 	  PCT0120189	best12. ;	
         format 	  PCT0120190	best12. ;	
         format 	  PCT0120191	best12. ;	
         format 	  PCT0120192	best12. ;	
         format 	  PCT0120193	best12. ;	
         format 	  PCT0120194	best12. ;	
         format 	  PCT0120195	best12. ;	
         format 	  PCT0120196	best12. ;	
         format 	  PCT0120197	best12. ;	
         format 	  PCT0120198	best12. ;	
         format 	  PCT0120199	best12. ;	
         format 	  PCT0120200	best12. ;	
         format 	  PCT0120201	best12. ;	
         format 	  PCT0120202	best12. ;	
         format 	  PCT0120203	best12. ;	
         format 	  PCT0120204	best12. ;	
         format 	  PCT0120205	best12. ;	
         format 	  PCT0120206	best12. ;	
         format 	  PCT0120207	best12. ;	
         format 	  PCT0120208	best12. ;	
         format 	  PCT0120209	best12. ;	
         format 	  PCT0130001	best12. ;	
         format 	  PCT0130002	best12. ;	
         format 	  PCT0130003	best12. ;	
         format 	  PCT0130004	best12. ;	
         format 	  PCT0130005	best12. ;	
         format 	  PCT0130006	best12. ;	
         format 	  PCT0130007	best12. ;	
         format 	  PCT0130008	best12. ;	
         format 	  PCT0130009	best12. ;	
         format 	  PCT0130010	best12. ;	
         format 	  PCT0130011	best12. ;	
         format 	  PCT0130012	best12. ;	
         format 	  PCT0130013	best12. ;	
         format 	  PCT0130014	best12. ;	
         format 	  PCT0130015	best12. ;	
         format 	  PCT0130016	best12. ;	
         format 	  PCT0130017	best12. ;	
         format 	  PCT0130018	best12. ;	
         format 	  PCT0130019	best12. ;	
         format 	  PCT0130020	best12. ;	
         format 	  PCT0130021	best12. ;	
         format 	  PCT0130022	best12. ;	
         format 	  PCT0130023	best12. ;	
         format 	  PCT0130024	best12. ;	
         format 	  PCT0130025	best12. ;	
         format 	  PCT0130026	best12. ;	
         format 	  PCT0130027	best12. ;	
         format 	  PCT0130028	best12. ;	
         format 	  PCT0130029	best12. ;	
         format 	  PCT0130030	best12. ;	
         format 	  PCT0130031	best12. ;	
         format 	  PCT0130032	best12. ;	
         format 	  PCT0130033	best12. ;	
         format 	  PCT0130034	best12. ;	
         format 	  PCT0130035	best12. ;	
         format 	  PCT0130036	best12. ;	
         format 	  PCT0130037	best12. ;	
         format 	  PCT0130038	best12. ;	
         format 	  PCT0130039	best12. ;	
         format 	  PCT0130040	best12. ;	
         format 	  PCT0130041	best12. ;	
         format 	  PCT0130042	best12. ;	
         format 	  PCT0130043	best12. ;	
         format 	  PCT0130044	best12. ;	
         format 	  PCT0130045	best12. ;	
         format 	  PCT0130046	best12. ;	
         format 	  PCT0130047	best12. ;	
         format 	  PCT0130048	best12. ;	
         format 	  PCT0130049	best12. ;	
         format 	  PCT0140001	best12. ;	
         format 	  PCT0140002	best12. ;	
         format 	  PCT0140003	best12. ;	
         format 	  PCT0150001	best12. ;	
         format 	  PCT0150002	best12. ;	
         format 	  PCT0150003	best12. ;	
         format 	  PCT0150004	best12. ;	
         format 	  PCT0150005	best12. ;	
         format 	  PCT0150006	best12. ;	
         format 	  PCT0150007	best12. ;	
         format 	  PCT0150008	best12. ;	
         format 	  PCT0150009	best12. ;	
         format 	  PCT0150010	best12. ;	
         format 	  PCT0150011	best12. ;	
         format 	  PCT0150012	best12. ;	
         format 	  PCT0150013	best12. ;	
         format 	  PCT0150014	best12. ;	
         format 	  PCT0150015	best12. ;	
         format 	  PCT0150016	best12. ;	
         format 	  PCT0150017	best12. ;	
         format 	  PCT0150018	best12. ;	
         format 	  PCT0150019	best12. ;	
         format 	  PCT0150020	best12. ;	
         format 	  PCT0150021	best12. ;	
         format 	  PCT0150022	best12. ;	
         format 	  PCT0150023	best12. ;	
         format 	  PCT0150024	best12. ;	
         format 	  PCT0150025	best12. ;	
         format 	  PCT0150026	best12. ;	
         format 	  PCT0150027	best12. ;	
         format 	  PCT0150028	best12. ;	
         format 	  PCT0150029	best12. ;	
         format 	  PCT0150030	best12. ;	
         format 	  PCT0150031	best12. ;	
         format 	  PCT0150032	best12. ;	
         format 	  PCT0150033	best12. ;	
         format 	  PCT0150034	best12. ;	
         format 	  PCT0160001	best12. ;	
         format 	  PCT0160002	best12. ;	
         format 	  PCT0160003	best12. ;	
         format 	  PCT0160004	best12. ;	
         format 	  PCT0160005	best12. ;	
         format 	  PCT0160006	best12. ;	
         format 	  PCT0160007	best12. ;	
         format 	  PCT0160008	best12. ;	
         format 	  PCT0160009	best12. ;	
         format 	  PCT0160010	best12. ;	
         format 	  PCT0160011	best12. ;	
         format 	  PCT0160012	best12. ;	
         format 	  PCT0160013	best12. ;	
         format 	  PCT0160014	best12. ;	
         format 	  PCT0160015	best12. ;	
         format 	  PCT0160016	best12. ;	
         format 	  PCT0160017	best12. ;	
         format 	  PCT0160018	best12. ;	
         format 	  PCT0160019	best12. ;	
         format 	  PCT0160020	best12. ;	
         format 	  PCT0160021	best12. ;	
         format 	  PCT0160022	best12. ;	
         format 	  PCT0160023	best12. ;	
         format 	  PCT0160024	best12. ;	
         format 	  PCT0160025	best12. ;	
         format 	  PCT0160026	best12. ;	
         format 	  PCT0170001	best12. ;	
         format 	  PCT0170002	best12. ;	
         format 	  PCT0170003	best12. ;	
         format 	  PCT0170004	best12. ;	
         format 	  PCT0170005	best12. ;	
         format 	  PCT0170006	best12. ;	
         format 	  PCT0170007	best12. ;	
         format 	  PCT0170008	best12. ;	
         format 	  PCT0170009	best12. ;	
         format 	  PCT0170010	best12. ;	
         format 	  PCT0170011	best12. ;	
         format 	  PCT0170012	best12. ;	
         format 	  PCT0170013	best12. ;	
         format 	  PCT0170014	best12. ;	
         format 	  PCT0170015	best12. ;	
         format 	  PCT0170016	best12. ;	
         format 	  PCT0170017	best12. ;	
         format 	  PCT0170018	best12. ;	
         format 	  PCT0180001	best12. ;	
         format 	  PCT0180002	best12. ;	
         format 	  PCT0180003	best12. ;	
         format 	  PCT0180004	best12. ;	
         format 	  PCT0180005	best12. ;	
         format 	  PCT0180006	best12. ;	
         format 	  PCT0180007	best12. ;	
         format 	  PCT0180008	best12. ;	
         format 	  PCT0180009	best12. ;	
         format 	  PCT0180010	best12. ;	
         format 	  PCT0180011	best12. ;	
         format 	  PCT0180012	best12. ;	
         format 	  PCT0180013	best12. ;	
         format 	  PCT0180014	best12. ;	
         format 	  PCT0180015	best12. ;	
         format 	  PCT0190001	best12. ;	
         format 	  PCT0190002	best12. ;	
         format 	  PCT0190003	best12. ;	
         format 	  PCT0190004	best12. ;	
         format 	  PCT0190005	best12. ;	
         format 	  PCT0190006	best12. ;	
         format 	  PCT0190007	best12. ;	
         format 	  PCT0190008	best12. ;	
         format 	  PCT0190009	best12. ;	
         format 	  PCT0190010	best12. ;	
         format 	  PCT0190011	best12. ;	
         format 	  PCT0200001	best12. ;	
         format 	  PCT0200002	best12. ;	
         format 	  PCT0200003	best12. ;	
         format 	  PCT0200004	best12. ;	
         format 	  PCT0200005	best12. ;	
         format 	  PCT0200006	best12. ;	
         format 	  PCT0200007	best12. ;	
         format 	  PCT0200008	best12. ;	
         format 	  PCT0200009	best12. ;	
         format 	  PCT0200010	best12. ;	
         format 	  PCT0200011	best12. ;	
         format 	  PCT0200012	best12. ;	
         format 	  PCT0200013	best12. ;	
         format 	  PCT0200014	best12. ;	
         format 	  PCT0200015	best12. ;	
         format 	  PCT0200016	best12. ;	
         format 	  PCT0200017	best12. ;	
         format 	  PCT0200018	best12. ;	
         format 	  PCT0200019	best12. ;	
         format 	  PCT0200020	best12. ;	
         format 	  PCT0200021	best12. ;	
         format 	  PCT0200022	best12. ;	
         format 	  PCT0200023	best12. ;	
         format 	  PCT0200024	best12. ;	
         format 	  PCT0200025	best12. ;	
         format 	  PCT0200026	best12. ;	
         format 	  PCT0200027	best12. ;	
         format 	  PCT0200028	best12. ;	
         format 	  PCT0200029	best12. ;	
         format 	  PCT0200030	best12. ;	
         format 	  PCT0200031	best12. ;	
         format 	  PCT0200032	best12. ;	
         format 	  PCT0210001	best12. ;	
         format 	  PCT0210002	best12. ;	
         format 	  PCT0210003	best12. ;	
         format 	  PCT0210004	best12. ;	
         format 	  PCT0210005	best12. ;	
         format 	  PCT0210006	best12. ;	
         format 	  PCT0210007	best12. ;	
         format 	  PCT0210008	best12. ;	
         format 	  PCT0210009	best12. ;	
         format 	  PCT0210010	best12. ;	
         format 	  PCT0210011	best12. ;	
         format 	  PCT0210012	best12. ;	
         format 	  PCT0210013	best12. ;	
         format 	  PCT0210014	best12. ;	
         format 	  PCT0210015	best12. ;	
         format 	  PCT0210016	best12. ;	
         format 	  PCT0210017	best12. ;	
         format 	  PCT0210018	best12. ;	
         format 	  PCT0210019	best12. ;	
         format 	  PCT0210020	best12. ;	
         format 	  PCT0210021	best12. ;	
         format 	  PCT0210022	best12. ;	
         format 	  PCT0210023	best12. ;	
         format 	  PCT0210024	best12. ;	
         format 	  PCT0210025	best12. ;	
         format 	  PCT0210026	best12. ;	
         format 	  PCT0210027	best12. ;	
         format 	  PCT0210028	best12. ;	
         format 	  PCT0210029	best12. ;	
         format 	  PCT0210030	best12. ;	
         format 	  PCT0210031	best12. ;	
         format 	  PCT0210032	best12. ;	
         format 	  PCT0210033	best12. ;	
         format 	  PCT0210034	best12. ;	
         format 	  PCT0210035	best12. ;	
         format 	  PCT0210036	best12. ;	
         format 	  PCT0210037	best12. ;	
         format 	  PCT0210038	best12. ;	
         format 	  PCT0210039	best12. ;	
         format 	  PCT0210040	best12. ;	
         format 	  PCT0210041	best12. ;	
         format 	  PCT0210042	best12. ;	
         format 	  PCT0210043	best12. ;	
         format 	  PCT0210044	best12. ;	
         format 	  PCT0210045	best12. ;	
         format 	  PCT0210046	best12. ;	
         format 	  PCT0210047	best12. ;	
         format 	  PCT0210048	best12. ;	
         format 	  PCT0210049	best12. ;	
         format 	  PCT0210050	best12. ;	
         format 	  PCT0210051	best12. ;	
         format 	  PCT0210052	best12. ;	
         format 	  PCT0210053	best12. ;	
         format 	  PCT0210054	best12. ;	
         format 	  PCT0210055	best12. ;	
         format 	  PCT0210056	best12. ;	
         format 	  PCT0210057	best12. ;	
         format 	  PCT0210058	best12. ;	
         format 	  PCT0210059	best12. ;	
         format 	  PCT0210060	best12. ;	
         format 	  PCT0210061	best12. ;	
         format 	  PCT0210062	best12. ;	
         format 	  PCT0210063	best12. ;	
         format 	  PCT0210064	best12. ;	
         format 	  PCT0210065	best12. ;	
         format 	  PCT0210066	best12. ;	
         format 	  PCT0210067	best12. ;	
         format 	  PCT0210068	best12. ;	
         format 	  PCT0210069	best12. ;	
         format 	  PCT0210070	best12. ;	
         format 	  PCT0210071	best12. ;	
         format 	  PCT0210072	best12. ;	
         format 	  PCT0210073	best12. ;	
         format 	  PCT0210074	best12. ;	
         format 	  PCT0210075	best12. ;	
         format 	  PCT0210076	best12. ;	
         format 	  PCT0210077	best12. ;	
         format 	  PCT0210078	best12. ;	
         format 	  PCT0210079	best12. ;	
         format 	  PCT0210080	best12. ;	
         format 	  PCT0210081	best12. ;	
         format 	  PCT0210082	best12. ;	
         format 	  PCT0210083	best12. ;	
         format 	  PCT0210084	best12. ;	
         format 	  PCT0210085	best12. ;	
         format 	  PCT0210086	best12. ;	
         format 	  PCT0210087	best12. ;	
         format 	  PCT0210088	best12. ;	
         format 	  PCT0210089	best12. ;	
         format 	  PCT0210090	best12. ;	
         format 	  PCT0210091	best12. ;	
         format 	  PCT0210092	best12. ;	
         format 	  PCT0210093	best12. ;	
         format 	  PCT0210094	best12. ;	
         format 	  PCT0210095	best12. ;	
         format 	  PCT0210096	best12. ;	
         format 	  PCT0210097	best12. ;	
         format 	  PCT0210098	best12. ;	
         format 	  PCT0210099	best12. ;	
         format 	  PCT0210100	best12. ;	
         format 	  PCT0210101	best12. ;	
         format 	  PCT0210102	best12. ;	
         format 	  PCT0210103	best12. ;	
         format 	  PCT0210104	best12. ;	
         format 	  PCT0210105	best12. ;	
         format 	  PCT0210106	best12. ;	
         format 	  PCT0210107	best12. ;	
         format 	  PCT0210108	best12. ;	
         format 	  PCT0210109	best12. ;	
         format 	  PCT0210110	best12. ;	
         format 	  PCT0210111	best12. ;	
         format 	  PCT0210112	best12. ;	
         format 	  PCT0210113	best12. ;	
         format 	  PCT0210114	best12. ;	
         format 	  PCT0210115	best12. ;	
         format 	  PCT0210116	best12. ;	
         format 	  PCT0210117	best12. ;	
         format 	  PCT0210118	best12. ;	
         format 	  PCT0210119	best12. ;	
         format 	  PCT0210120	best12. ;	
         format 	  PCT0210121	best12. ;	
         format 	  PCT0210122	best12. ;	
         format 	  PCT0210123	best12. ;	
         format 	  PCT0210124	best12. ;	
         format 	  PCT0210125	best12. ;	
         format 	  PCT0210126	best12. ;	
         format 	  PCT0210127	best12. ;	
         format 	  PCT0210128	best12. ;	
         format 	  PCT0210129	best12. ;	
         format 	  PCT0210130	best12. ;	
         format 	  PCT0210131	best12. ;	
         format 	  PCT0210132	best12. ;	
         format 	  PCT0210133	best12. ;	
         format 	  PCT0210134	best12. ;	
         format 	  PCT0210135	best12. ;	
         format 	  PCT0210136	best12. ;	
         format 	  PCT0210137	best12. ;	
         format 	  PCT0210138	best12. ;	
         format 	  PCT0210139	best12. ;	
         format 	  PCT0210140	best12. ;	
         format 	  PCT0210141	best12. ;	
         format 	  PCT0210142	best12. ;	
         format 	  PCT0210143	best12. ;	
         format 	  PCT0210144	best12. ;	
         format 	  PCT0210145	best12. ;	
         format 	  PCT0210146	best12. ;	
         format 	  PCT0210147	best12. ;	
         format 	  PCT0210148	best12. ;	
         format 	  PCT0210149	best12. ;	
         format 	  PCT0210150	best12. ;	
         format 	  PCT0210151	best12. ;	
         format 	  PCT0210152	best12. ;	
         format 	  PCT0210153	best12. ;	
         format 	  PCT0210154	best12. ;	
         format 	  PCT0210155	best12. ;	
         format 	  PCT0210156	best12. ;	
         format 	  PCT0210157	best12. ;	
         format 	  PCT0210158	best12. ;	
         format 	  PCT0210159	best12. ;	
         format 	  PCT0210160	best12. ;	
         format 	  PCT0210161	best12. ;	
         format 	  PCT0210162	best12. ;	
         format 	  PCT0210163	best12. ;	
         format 	  PCT0210164	best12. ;	
         format 	  PCT0210165	best12. ;	
         format 	  PCT0210166	best12. ;	
         format 	  PCT0210167	best12. ;	
         format 	  PCT0210168	best12. ;	
         format 	  PCT0210169	best12. ;	
         format 	  PCT0210170	best12. ;	
         format 	  PCT0210171	best12. ;	
         format 	  PCT0210172	best12. ;	
         format 	  PCT0210173	best12. ;	
         format 	  PCT0210174	best12. ;	
         format 	  PCT0210175	best12. ;	
         format 	  PCT0210176	best12. ;	
         format 	  PCT0210177	best12. ;	
         format 	  PCT0210178	best12. ;	
         format 	  PCT0210179	best12. ;	
         format 	  PCT0210180	best12. ;	
         format 	  PCT0210181	best12. ;	
         format 	  PCT0210182	best12. ;	
         format 	  PCT0210183	best12. ;	
         format 	  PCT0210184	best12. ;	
         format 	  PCT0210185	best12. ;	
         format 	  PCT0210186	best12. ;	
         format 	  PCT0210187	best12. ;	
         format 	  PCT0210188	best12. ;	
         format 	  PCT0210189	best12. ;	
         format 	  PCT0210190	best12. ;	
         format 	  PCT0210191	best12. ;	
         format 	  PCT0210192	best12. ;	
         format 	  PCT0210193	best12. ;	
         format 	  PCT0210194	best12. ;	
         format 	  PCT0210195	best12. ;	
         format 	  PCT0220001	best12. ;	
         format 	  PCT0220002	best12. ;	
         format 	  PCT0220003	best12. ;	
         format 	  PCT0220004	best12. ;	
         format 	  PCT0220005	best12. ;	
         format 	  PCT0220006	best12. ;	
         format 	  PCT0220007	best12. ;	
         format 	  PCT0220008	best12. ;	
         format 	  PCT0220009	best12. ;	
         format 	  PCT0220010	best12. ;	
         format 	  PCT0220011	best12. ;	
         format 	  PCT0220012	best12. ;	
         format 	  PCT0220013	best12. ;	
         format 	  PCT0220014	best12. ;	
         format 	  PCT0220015	best12. ;	
         format 	  PCT0220016	best12. ;	
         format 	  PCT0220017	best12. ;	
         format 	  PCT0220018	best12. ;	
         format 	  PCT0220019	best12. ;	
         format 	  PCT0220020	best12. ;	
         format 	  PCT0220021	best12. ;	
         format 	  PCT012A001	best12. ;	
         format 	  PCT012A002	best12. ;	
         format 	  PCT012A003	best12. ;	
         format 	  PCT012A004	best12. ;	
         format 	  PCT012A005	best12. ;	
         format 	  PCT012A006	best12. ;	
         format 	  PCT012A007	best12. ;	
         format 	  PCT012A008	best12. ;	
         format 	  PCT012A009	best12. ;	
         format 	  PCT012A010	best12. ;	
         format 	  PCT012A011	best12. ;	
         format 	  PCT012A012	best12. ;	
         format 	  PCT012A013	best12. ;	
         format 	  PCT012A014	best12. ;	
         format 	  PCT012A015	best12. ;	
         format 	  PCT012A016	best12. ;	
         format 	  PCT012A017	best12. ;	
         format 	  PCT012A018	best12. ;	
         format 	  PCT012A019	best12. ;	
         format 	  PCT012A020	best12. ;	
         format 	  PCT012A021	best12. ;	
         format 	  PCT012A022	best12. ;	
         format 	  PCT012A023	best12. ;	
         format 	  PCT012A024	best12. ;	
         format 	  PCT012A025	best12. ;	
         format 	  PCT012A026	best12. ;	
         format 	  PCT012A027	best12. ;	
         format 	  PCT012A028	best12. ;	
         format 	  PCT012A029	best12. ;	
         format 	  PCT012A030	best12. ;	
         format 	  PCT012A031	best12. ;	
         format 	  PCT012A032	best12. ;	
         format 	  PCT012A033	best12. ;	
         format 	  PCT012A034	best12. ;	
         format 	  PCT012A035	best12. ;	
         format 	  PCT012A036	best12. ;	
         format 	  PCT012A037	best12. ;	
         format 	  PCT012A038	best12. ;	
         format 	  PCT012A039	best12. ;	
         format 	  PCT012A040	best12. ;	
         format 	  PCT012A041	best12. ;	
         format 	  PCT012A042	best12. ;	
         format 	  PCT012A043	best12. ;	
         format 	  PCT012A044	best12. ;	
         format 	  PCT012A045	best12. ;	
         format 	  PCT012A046	best12. ;	
         format 	  PCT012A047	best12. ;	
         format 	  PCT012A048	best12. ;	
         format 	  PCT012A049	best12. ;	
         format 	  PCT012A050	best12. ;	
         format 	  PCT012A051	best12. ;	
         format 	  PCT012A052	best12. ;	
         format 	  PCT012A053	best12. ;	
         format 	  PCT012A054	best12. ;	
         format 	  PCT012A055	best12. ;	
         format 	  PCT012A056	best12. ;	
         format 	  PCT012A057	best12. ;	
         format 	  PCT012A058	best12. ;	
         format 	  PCT012A059	best12. ;	
         format 	  PCT012A060	best12. ;	
         format 	  PCT012A061	best12. ;	
         format 	  PCT012A062	best12. ;	
         format 	  PCT012A063	best12. ;	
         format 	  PCT012A064	best12. ;	
         format 	  PCT012A065	best12. ;	
         format 	  PCT012A066	best12. ;	
         format 	  PCT012A067	best12. ;	
         format 	  PCT012A068	best12. ;	
         format 	  PCT012A069	best12. ;	
         format 	  PCT012A070	best12. ;	
         format 	  PCT012A071	best12. ;	
         format 	  PCT012A072	best12. ;	
         format 	  PCT012A073	best12. ;	
         format 	  PCT012A074	best12. ;	
         format 	  PCT012A075	best12. ;	
         format 	  PCT012A076	best12. ;	
         format 	  PCT012A077	best12. ;	
         format 	  PCT012A078	best12. ;	
         format 	  PCT012A079	best12. ;	
         format 	  PCT012A080	best12. ;	
         format 	  PCT012A081	best12. ;	
         format 	  PCT012A082	best12. ;	
         format 	  PCT012A083	best12. ;	
         format 	  PCT012A084	best12. ;	
         format 	  PCT012A085	best12. ;	
         format 	  PCT012A086	best12. ;	
         format 	  PCT012A087	best12. ;	
         format 	  PCT012A088	best12. ;	
         format 	  PCT012A089	best12. ;	
         format 	  PCT012A090	best12. ;	
         format 	  PCT012A091	best12. ;	
         format 	  PCT012A092	best12. ;	
         format 	  PCT012A093	best12. ;	
         format 	  PCT012A094	best12. ;	
         format 	  PCT012A095	best12. ;	
         format 	  PCT012A096	best12. ;	
         format 	  PCT012A097	best12. ;	
         format 	  PCT012A098	best12. ;	
         format 	  PCT012A099	best12. ;	
         format 	  PCT012A100	best12. ;	
         format 	  PCT012A101	best12. ;	
         format 	  PCT012A102	best12. ;	
         format 	  PCT012A103	best12. ;	
         format 	  PCT012A104	best12. ;	
         format 	  PCT012A105	best12. ;	
         format 	  PCT012A106	best12. ;	
         format 	  PCT012A107	best12. ;	
         format 	  PCT012A108	best12. ;	
         format 	  PCT012A109	best12. ;	
         format 	  PCT012A110	best12. ;	
         format 	  PCT012A111	best12. ;	
         format 	  PCT012A112	best12. ;	
         format 	  PCT012A113	best12. ;	
         format 	  PCT012A114	best12. ;	
         format 	  PCT012A115	best12. ;	
         format 	  PCT012A116	best12. ;	
         format 	  PCT012A117	best12. ;	
         format 	  PCT012A118	best12. ;	
         format 	  PCT012A119	best12. ;	
         format 	  PCT012A120	best12. ;	
         format 	  PCT012A121	best12. ;	
         format 	  PCT012A122	best12. ;	
         format 	  PCT012A123	best12. ;	
         format 	  PCT012A124	best12. ;	
         format 	  PCT012A125	best12. ;	
         format 	  PCT012A126	best12. ;	
         format 	  PCT012A127	best12. ;	
         format 	  PCT012A128	best12. ;	
         format 	  PCT012A129	best12. ;	
         format 	  PCT012A130	best12. ;	
         format 	  PCT012A131	best12. ;	
         format 	  PCT012A132	best12. ;	
         format 	  PCT012A133	best12. ;	
         format 	  PCT012A134	best12. ;	
         format 	  PCT012A135	best12. ;	
         format 	  PCT012A136	best12. ;	
         format 	  PCT012A137	best12. ;	
         format 	  PCT012A138	best12. ;	
         format 	  PCT012A139	best12. ;	
         format 	  PCT012A140	best12. ;	
         format 	  PCT012A141	best12. ;	
         format 	  PCT012A142	best12. ;	
         format 	  PCT012A143	best12. ;	
         format 	  PCT012A144	best12. ;	
         format 	  PCT012A145	best12. ;	
         format 	  PCT012A146	best12. ;	
         format 	  PCT012A147	best12. ;	
         format 	  PCT012A148	best12. ;	
         format 	  PCT012A149	best12. ;	
         format 	  PCT012A150	best12. ;	
         format 	  PCT012A151	best12. ;	
         format 	  PCT012A152	best12. ;	
         format 	  PCT012A153	best12. ;	
         format 	  PCT012A154	best12. ;	
         format 	  PCT012A155	best12. ;	
         format 	  PCT012A156	best12. ;	
         format 	  PCT012A157	best12. ;	
         format 	  PCT012A158	best12. ;	
         format 	  PCT012A159	best12. ;	
         format 	  PCT012A160	best12. ;	
         format 	  PCT012A161	best12. ;	
         format 	  PCT012A162	best12. ;	
         format 	  PCT012A163	best12. ;	
         format 	  PCT012A164	best12. ;	
         format 	  PCT012A165	best12. ;	
         format 	  PCT012A166	best12. ;	
         format 	  PCT012A167	best12. ;	
         format 	  PCT012A168	best12. ;	
         format 	  PCT012A169	best12. ;	
         format 	  PCT012A170	best12. ;	
         format 	  PCT012A171	best12. ;	
         format 	  PCT012A172	best12. ;	
         format 	  PCT012A173	best12. ;	
         format 	  PCT012A174	best12. ;	
         format 	  PCT012A175	best12. ;	
         format 	  PCT012A176	best12. ;	
         format 	  PCT012A177	best12. ;	
         format 	  PCT012A178	best12. ;	
         format 	  PCT012A179	best12. ;	
         format 	  PCT012A180	best12. ;	
         format 	  PCT012A181	best12. ;	
         format 	  PCT012A182	best12. ;	
         format 	  PCT012A183	best12. ;	
         format 	  PCT012A184	best12. ;	
         format 	  PCT012A185	best12. ;	
         format 	  PCT012A186	best12. ;	
         format 	  PCT012A187	best12. ;	
         format 	  PCT012A188	best12. ;	
         format 	  PCT012A189	best12. ;	
         format 	  PCT012A190	best12. ;	
         format 	  PCT012A191	best12. ;	
         format 	  PCT012A192	best12. ;	
         format 	  PCT012A193	best12. ;	
         format 	  PCT012A194	best12. ;	
         format 	  PCT012A195	best12. ;	
         format 	  PCT012A196	best12. ;	
         format 	  PCT012A197	best12. ;	
         format 	  PCT012A198	best12. ;	
         format 	  PCT012A199	best12. ;	
         format 	  PCT012A200	best12. ;	
         format 	  PCT012A201	best12. ;	
         format 	  PCT012A202	best12. ;	
         format 	  PCT012A203	best12. ;	
         format 	  PCT012A204	best12. ;	
         format 	  PCT012A205	best12. ;	
         format 	  PCT012A206	best12. ;	
         format 	  PCT012A207	best12. ;	
         format 	  PCT012A208	best12. ;	
         format 	  PCT012A209	best12. ;	
         format 	  PCT012B001	best12. ;	
         format 	  PCT012B002	best12. ;	
         format 	  PCT012B003	best12. ;	
         format 	  PCT012B004	best12. ;	
         format 	  PCT012B005	best12. ;	
         format 	  PCT012B006	best12. ;	
         format 	  PCT012B007	best12. ;	
         format 	  PCT012B008	best12. ;	
         format 	  PCT012B009	best12. ;	
         format 	  PCT012B010	best12. ;	
         format 	  PCT012B011	best12. ;	
         format 	  PCT012B012	best12. ;	
         format 	  PCT012B013	best12. ;	
         format 	  PCT012B014	best12. ;	
         format 	  PCT012B015	best12. ;	
         format 	  PCT012B016	best12. ;	
         format 	  PCT012B017	best12. ;	
         format 	  PCT012B018	best12. ;	
         format 	  PCT012B019	best12. ;	
         format 	  PCT012B020	best12. ;	
         format 	  PCT012B021	best12. ;	
         format 	  PCT012B022	best12. ;	
         format 	  PCT012B023	best12. ;	
         format 	  PCT012B024	best12. ;	
         format 	  PCT012B025	best12. ;	
         format 	  PCT012B026	best12. ;	
         format 	  PCT012B027	best12. ;	
         format 	  PCT012B028	best12. ;	
         format 	  PCT012B029	best12. ;	
         format 	  PCT012B030	best12. ;	
         format 	  PCT012B031	best12. ;	
         format 	  PCT012B032	best12. ;	
         format 	  PCT012B033	best12. ;	
         format 	  PCT012B034	best12. ;	
         format 	  PCT012B035	best12. ;	
         format 	  PCT012B036	best12. ;	
         format 	  PCT012B037	best12. ;	
         format 	  PCT012B038	best12. ;	
         format 	  PCT012B039	best12. ;	
         format 	  PCT012B040	best12. ;	
         format 	  PCT012B041	best12. ;	
         format 	  PCT012B042	best12. ;	
         format 	  PCT012B043	best12. ;	
         format 	  PCT012B044	best12. ;	
         format 	  PCT012B045	best12. ;	
         format 	  PCT012B046	best12. ;	
         format 	  PCT012B047	best12. ;	
         format 	  PCT012B048	best12. ;	
         format 	  PCT012B049	best12. ;	
         format 	  PCT012B050	best12. ;	
         format 	  PCT012B051	best12. ;	
         format 	  PCT012B052	best12. ;	
         format 	  PCT012B053	best12. ;	
         format 	  PCT012B054	best12. ;	
         format 	  PCT012B055	best12. ;	
         format 	  PCT012B056	best12. ;	
         format 	  PCT012B057	best12. ;	
         format 	  PCT012B058	best12. ;	
         format 	  PCT012B059	best12. ;	
         format 	  PCT012B060	best12. ;	
         format 	  PCT012B061	best12. ;	
         format 	  PCT012B062	best12. ;	
         format 	  PCT012B063	best12. ;	
         format 	  PCT012B064	best12. ;	
         format 	  PCT012B065	best12. ;	
         format 	  PCT012B066	best12. ;	
         format 	  PCT012B067	best12. ;	
         format 	  PCT012B068	best12. ;	
         format 	  PCT012B069	best12. ;	
         format 	  PCT012B070	best12. ;	
         format 	  PCT012B071	best12. ;	
         format 	  PCT012B072	best12. ;	
         format 	  PCT012B073	best12. ;	
         format 	  PCT012B074	best12. ;	
         format 	  PCT012B075	best12. ;	
         format 	  PCT012B076	best12. ;	
         format 	  PCT012B077	best12. ;	
         format 	  PCT012B078	best12. ;	
         format 	  PCT012B079	best12. ;	
         format 	  PCT012B080	best12. ;	
         format 	  PCT012B081	best12. ;	
         format 	  PCT012B082	best12. ;	
         format 	  PCT012B083	best12. ;	
         format 	  PCT012B084	best12. ;	
         format 	  PCT012B085	best12. ;	
         format 	  PCT012B086	best12. ;	
         format 	  PCT012B087	best12. ;	
         format 	  PCT012B088	best12. ;	
         format 	  PCT012B089	best12. ;	
         format 	  PCT012B090	best12. ;	
         format 	  PCT012B091	best12. ;	
         format 	  PCT012B092	best12. ;	
         format 	  PCT012B093	best12. ;	
         format 	  PCT012B094	best12. ;	
         format 	  PCT012B095	best12. ;	
         format 	  PCT012B096	best12. ;	
         format 	  PCT012B097	best12. ;	
         format 	  PCT012B098	best12. ;	
         format 	  PCT012B099	best12. ;	
         format 	  PCT012B100	best12. ;	
         format 	  PCT012B101	best12. ;	
         format 	  PCT012B102	best12. ;	
         format 	  PCT012B103	best12. ;	
         format 	  PCT012B104	best12. ;	
         format 	  PCT012B105	best12. ;	
         format 	  PCT012B106	best12. ;	
         format 	  PCT012B107	best12. ;	
         format 	  PCT012B108	best12. ;	
         format 	  PCT012B109	best12. ;	
         format 	  PCT012B110	best12. ;	
         format 	  PCT012B111	best12. ;	
         format 	  PCT012B112	best12. ;	
         format 	  PCT012B113	best12. ;	
         format 	  PCT012B114	best12. ;	
         format 	  PCT012B115	best12. ;	
         format 	  PCT012B116	best12. ;	
         format 	  PCT012B117	best12. ;	
         format 	  PCT012B118	best12. ;	
         format 	  PCT012B119	best12. ;	
         format 	  PCT012B120	best12. ;	
         format 	  PCT012B121	best12. ;	
         format 	  PCT012B122	best12. ;	
         format 	  PCT012B123	best12. ;	
         format 	  PCT012B124	best12. ;	
         format 	  PCT012B125	best12. ;	
         format 	  PCT012B126	best12. ;	
         format 	  PCT012B127	best12. ;	
         format 	  PCT012B128	best12. ;	
         format 	  PCT012B129	best12. ;	
         format 	  PCT012B130	best12. ;	
         format 	  PCT012B131	best12. ;	
         format 	  PCT012B132	best12. ;	
         format 	  PCT012B133	best12. ;	
         format 	  PCT012B134	best12. ;	
         format 	  PCT012B135	best12. ;	
         format 	  PCT012B136	best12. ;	
         format 	  PCT012B137	best12. ;	
         format 	  PCT012B138	best12. ;	
         format 	  PCT012B139	best12. ;	
         format 	  PCT012B140	best12. ;	
         format 	  PCT012B141	best12. ;	
         format 	  PCT012B142	best12. ;	
         format 	  PCT012B143	best12. ;	
         format 	  PCT012B144	best12. ;	
         format 	  PCT012B145	best12. ;	
         format 	  PCT012B146	best12. ;	
         format 	  PCT012B147	best12. ;	
         format 	  PCT012B148	best12. ;	
         format 	  PCT012B149	best12. ;	
         format 	  PCT012B150	best12. ;	
         format 	  PCT012B151	best12. ;	
         format 	  PCT012B152	best12. ;	
         format 	  PCT012B153	best12. ;	
         format 	  PCT012B154	best12. ;	
         format 	  PCT012B155	best12. ;	
         format 	  PCT012B156	best12. ;	
         format 	  PCT012B157	best12. ;	
         format 	  PCT012B158	best12. ;	
         format 	  PCT012B159	best12. ;	
         format 	  PCT012B160	best12. ;	
         format 	  PCT012B161	best12. ;	
         format 	  PCT012B162	best12. ;	
         format 	  PCT012B163	best12. ;	
         format 	  PCT012B164	best12. ;	
         format 	  PCT012B165	best12. ;	
         format 	  PCT012B166	best12. ;	
         format 	  PCT012B167	best12. ;	
         format 	  PCT012B168	best12. ;	
         format 	  PCT012B169	best12. ;	
         format 	  PCT012B170	best12. ;	
         format 	  PCT012B171	best12. ;	
         format 	  PCT012B172	best12. ;	
         format 	  PCT012B173	best12. ;	
         format 	  PCT012B174	best12. ;	
         format 	  PCT012B175	best12. ;	
         format 	  PCT012B176	best12. ;	
         format 	  PCT012B177	best12. ;	
         format 	  PCT012B178	best12. ;	
         format 	  PCT012B179	best12. ;	
         format 	  PCT012B180	best12. ;	
         format 	  PCT012B181	best12. ;	
         format 	  PCT012B182	best12. ;	
         format 	  PCT012B183	best12. ;	
         format 	  PCT012B184	best12. ;	
         format 	  PCT012B185	best12. ;	
         format 	  PCT012B186	best12. ;	
         format 	  PCT012B187	best12. ;	
         format 	  PCT012B188	best12. ;	
         format 	  PCT012B189	best12. ;	
         format 	  PCT012B190	best12. ;	
         format 	  PCT012B191	best12. ;	
         format 	  PCT012B192	best12. ;	
         format 	  PCT012B193	best12. ;	
         format 	  PCT012B194	best12. ;	
         format 	  PCT012B195	best12. ;	
         format 	  PCT012B196	best12. ;	
         format 	  PCT012B197	best12. ;	
         format 	  PCT012B198	best12. ;	
         format 	  PCT012B199	best12. ;	
         format 	  PCT012B200	best12. ;	
         format 	  PCT012B201	best12. ;	
         format 	  PCT012B202	best12. ;	
         format 	  PCT012B203	best12. ;	
         format 	  PCT012B204	best12. ;	
         format 	  PCT012B205	best12. ;	
         format 	  PCT012B206	best12. ;	
         format 	  PCT012B207	best12. ;	
         format 	  PCT012B208	best12. ;	
         format 	  PCT012B209	best12. ;	
         format 	  PCT012C001	best12. ;	
         format 	  PCT012C002	best12. ;	
         format 	  PCT012C003	best12. ;	
         format 	  PCT012C004	best12. ;	
         format 	  PCT012C005	best12. ;	
         format 	  PCT012C006	best12. ;	
         format 	  PCT012C007	best12. ;	
         format 	  PCT012C008	best12. ;	
         format 	  PCT012C009	best12. ;	
         format 	  PCT012C010	best12. ;	
         format 	  PCT012C011	best12. ;	
         format 	  PCT012C012	best12. ;	
         format 	  PCT012C013	best12. ;	
         format 	  PCT012C014	best12. ;	
         format 	  PCT012C015	best12. ;	
         format 	  PCT012C016	best12. ;	
         format 	  PCT012C017	best12. ;	
         format 	  PCT012C018	best12. ;	
         format 	  PCT012C019	best12. ;	
         format 	  PCT012C020	best12. ;	
         format 	  PCT012C021	best12. ;	
         format 	  PCT012C022	best12. ;	
         format 	  PCT012C023	best12. ;	
         format 	  PCT012C024	best12. ;	
         format 	  PCT012C025	best12. ;	
         format 	  PCT012C026	best12. ;	
         format 	  PCT012C027	best12. ;	
         format 	  PCT012C028	best12. ;	
         format 	  PCT012C029	best12. ;	
         format 	  PCT012C030	best12. ;	
         format 	  PCT012C031	best12. ;	
         format 	  PCT012C032	best12. ;	
         format 	  PCT012C033	best12. ;	
         format 	  PCT012C034	best12. ;	
         format 	  PCT012C035	best12. ;	
         format 	  PCT012C036	best12. ;	
         format 	  PCT012C037	best12. ;	
         format 	  PCT012C038	best12. ;	
         format 	  PCT012C039	best12. ;	
         format 	  PCT012C040	best12. ;	
         format 	  PCT012C041	best12. ;	
         format 	  PCT012C042	best12. ;	
         format 	  PCT012C043	best12. ;	
         format 	  PCT012C044	best12. ;	
         format 	  PCT012C045	best12. ;	
         format 	  PCT012C046	best12. ;	
         format 	  PCT012C047	best12. ;	
         format 	  PCT012C048	best12. ;	
         format 	  PCT012C049	best12. ;	
         format 	  PCT012C050	best12. ;	
         format 	  PCT012C051	best12. ;	
         format 	  PCT012C052	best12. ;	
         format 	  PCT012C053	best12. ;	
         format 	  PCT012C054	best12. ;	
         format 	  PCT012C055	best12. ;	
         format 	  PCT012C056	best12. ;	
         format 	  PCT012C057	best12. ;	
         format 	  PCT012C058	best12. ;	
         format 	  PCT012C059	best12. ;	
         format 	  PCT012C060	best12. ;	
         format 	  PCT012C061	best12. ;	
         format 	  PCT012C062	best12. ;	
         format 	  PCT012C063	best12. ;	
         format 	  PCT012C064	best12. ;	
         format 	  PCT012C065	best12. ;	
         format 	  PCT012C066	best12. ;	
         format 	  PCT012C067	best12. ;	
         format 	  PCT012C068	best12. ;	
         format 	  PCT012C069	best12. ;	
         format 	  PCT012C070	best12. ;	
         format 	  PCT012C071	best12. ;	
         format 	  PCT012C072	best12. ;	
         format 	  PCT012C073	best12. ;	
         format 	  PCT012C074	best12. ;	
         format 	  PCT012C075	best12. ;	
         format 	  PCT012C076	best12. ;	
         format 	  PCT012C077	best12. ;	
         format 	  PCT012C078	best12. ;	
         format 	  PCT012C079	best12. ;	
         format 	  PCT012C080	best12. ;	
         format 	  PCT012C081	best12. ;	
         format 	  PCT012C082	best12. ;	
         format 	  PCT012C083	best12. ;	
         format 	  PCT012C084	best12. ;	
         format 	  PCT012C085	best12. ;	
         format 	  PCT012C086	best12. ;	
         format 	  PCT012C087	best12. ;	
         format 	  PCT012C088	best12. ;	
         format 	  PCT012C089	best12. ;	
         format 	  PCT012C090	best12. ;	
         format 	  PCT012C091	best12. ;	
         format 	  PCT012C092	best12. ;	
         format 	  PCT012C093	best12. ;	
         format 	  PCT012C094	best12. ;	
         format 	  PCT012C095	best12. ;	
         format 	  PCT012C096	best12. ;	
         format 	  PCT012C097	best12. ;	
         format 	  PCT012C098	best12. ;	
         format 	  PCT012C099	best12. ;	
         format 	  PCT012C100	best12. ;	
         format 	  PCT012C101	best12. ;	
         format 	  PCT012C102	best12. ;	
         format 	  PCT012C103	best12. ;	
         format 	  PCT012C104	best12. ;	
         format 	  PCT012C105	best12. ;	
         format 	  PCT012C106	best12. ;	
         format 	  PCT012C107	best12. ;	
         format 	  PCT012C108	best12. ;	
         format 	  PCT012C109	best12. ;	
         format 	  PCT012C110	best12. ;	
         format 	  PCT012C111	best12. ;	
         format 	  PCT012C112	best12. ;	
         format 	  PCT012C113	best12. ;	
         format 	  PCT012C114	best12. ;	
         format 	  PCT012C115	best12. ;	
         format 	  PCT012C116	best12. ;	
         format 	  PCT012C117	best12. ;	
         format 	  PCT012C118	best12. ;	
         format 	  PCT012C119	best12. ;	
         format 	  PCT012C120	best12. ;	
         format 	  PCT012C121	best12. ;	
         format 	  PCT012C122	best12. ;	
         format 	  PCT012C123	best12. ;	
         format 	  PCT012C124	best12. ;	
         format 	  PCT012C125	best12. ;	
         format 	  PCT012C126	best12. ;	
         format 	  PCT012C127	best12. ;	
         format 	  PCT012C128	best12. ;	
         format 	  PCT012C129	best12. ;	
         format 	  PCT012C130	best12. ;	
         format 	  PCT012C131	best12. ;	
         format 	  PCT012C132	best12. ;	
         format 	  PCT012C133	best12. ;	
         format 	  PCT012C134	best12. ;	
         format 	  PCT012C135	best12. ;	
         format 	  PCT012C136	best12. ;	
         format 	  PCT012C137	best12. ;	
         format 	  PCT012C138	best12. ;	
         format 	  PCT012C139	best12. ;	
         format 	  PCT012C140	best12. ;	
         format 	  PCT012C141	best12. ;	
         format 	  PCT012C142	best12. ;	
         format 	  PCT012C143	best12. ;	
         format 	  PCT012C144	best12. ;	
         format 	  PCT012C145	best12. ;	
         format 	  PCT012C146	best12. ;	
         format 	  PCT012C147	best12. ;	
         format 	  PCT012C148	best12. ;	
         format 	  PCT012C149	best12. ;	
         format 	  PCT012C150	best12. ;	
         format 	  PCT012C151	best12. ;	
         format 	  PCT012C152	best12. ;	
         format 	  PCT012C153	best12. ;	
         format 	  PCT012C154	best12. ;	
         format 	  PCT012C155	best12. ;	
         format 	  PCT012C156	best12. ;	
         format 	  PCT012C157	best12. ;	
         format 	  PCT012C158	best12. ;	
         format 	  PCT012C159	best12. ;	
         format 	  PCT012C160	best12. ;	
         format 	  PCT012C161	best12. ;	
         format 	  PCT012C162	best12. ;	
         format 	  PCT012C163	best12. ;	
         format 	  PCT012C164	best12. ;	
         format 	  PCT012C165	best12. ;	
         format 	  PCT012C166	best12. ;	
         format 	  PCT012C167	best12. ;	
         format 	  PCT012C168	best12. ;	
         format 	  PCT012C169	best12. ;	
         format 	  PCT012C170	best12. ;	
         format 	  PCT012C171	best12. ;	
         format 	  PCT012C172	best12. ;	
         format 	  PCT012C173	best12. ;	
         format 	  PCT012C174	best12. ;	
         format 	  PCT012C175	best12. ;	
         format 	  PCT012C176	best12. ;	
         format 	  PCT012C177	best12. ;	
         format 	  PCT012C178	best12. ;	
         format 	  PCT012C179	best12. ;	
         format 	  PCT012C180	best12. ;	
         format 	  PCT012C181	best12. ;	
         format 	  PCT012C182	best12. ;	
         format 	  PCT012C183	best12. ;	
         format 	  PCT012C184	best12. ;	
         format 	  PCT012C185	best12. ;	
         format 	  PCT012C186	best12. ;	
         format 	  PCT012C187	best12. ;	
         format 	  PCT012C188	best12. ;	
         format 	  PCT012C189	best12. ;	
         format 	  PCT012C190	best12. ;	
         format 	  PCT012C191	best12. ;	
         format 	  PCT012C192	best12. ;	
         format 	  PCT012C193	best12. ;	
         format 	  PCT012C194	best12. ;	
         format 	  PCT012C195	best12. ;	
         format 	  PCT012C196	best12. ;	
         format 	  PCT012C197	best12. ;	
         format 	  PCT012C198	best12. ;	
         format 	  PCT012C199	best12. ;	
         format 	  PCT012C200	best12. ;	
         format 	  PCT012C201	best12. ;	
         format 	  PCT012C202	best12. ;	
         format 	  PCT012C203	best12. ;	
         format 	  PCT012C204	best12. ;	
         format 	  PCT012C205	best12. ;	
         format 	  PCT012C206	best12. ;	
         format 	  PCT012C207	best12. ;	
         format 	  PCT012C208	best12. ;	
         format 	  PCT012C209	best12. ;	
         format 	  PCT012D001	best12. ;	
         format 	  PCT012D002	best12. ;	
         format 	  PCT012D003	best12. ;	
         format 	  PCT012D004	best12. ;	
         format 	  PCT012D005	best12. ;	
         format 	  PCT012D006	best12. ;	
         format 	  PCT012D007	best12. ;	
         format 	  PCT012D008	best12. ;	
         format 	  PCT012D009	best12. ;	
         format 	  PCT012D010	best12. ;	
         format 	  PCT012D011	best12. ;	
         format 	  PCT012D012	best12. ;	
         format 	  PCT012D013	best12. ;	
         format 	  PCT012D014	best12. ;	
         format 	  PCT012D015	best12. ;	
         format 	  PCT012D016	best12. ;	
         format 	  PCT012D017	best12. ;	
         format 	  PCT012D018	best12. ;	
         format 	  PCT012D019	best12. ;	
         format 	  PCT012D020	best12. ;	
         format 	  PCT012D021	best12. ;	
         format 	  PCT012D022	best12. ;	
         format 	  PCT012D023	best12. ;	
         format 	  PCT012D024	best12. ;	
         format 	  PCT012D025	best12. ;	
         format 	  PCT012D026	best12. ;	
         format 	  PCT012D027	best12. ;	
         format 	  PCT012D028	best12. ;	
         format 	  PCT012D029	best12. ;	
         format 	  PCT012D030	best12. ;	
         format 	  PCT012D031	best12. ;	
         format 	  PCT012D032	best12. ;	
         format 	  PCT012D033	best12. ;	
         format 	  PCT012D034	best12. ;	
         format 	  PCT012D035	best12. ;	
         format 	  PCT012D036	best12. ;	
         format 	  PCT012D037	best12. ;	
         format 	  PCT012D038	best12. ;	
         format 	  PCT012D039	best12. ;	
         format 	  PCT012D040	best12. ;	
         format 	  PCT012D041	best12. ;	
         format 	  PCT012D042	best12. ;	
         format 	  PCT012D043	best12. ;	
         format 	  PCT012D044	best12. ;	
         format 	  PCT012D045	best12. ;	
         format 	  PCT012D046	best12. ;	
         format 	  PCT012D047	best12. ;	
         format 	  PCT012D048	best12. ;	
         format 	  PCT012D049	best12. ;	
         format 	  PCT012D050	best12. ;	
         format 	  PCT012D051	best12. ;	
         format 	  PCT012D052	best12. ;	
         format 	  PCT012D053	best12. ;	
         format 	  PCT012D054	best12. ;	
         format 	  PCT012D055	best12. ;	
         format 	  PCT012D056	best12. ;	
         format 	  PCT012D057	best12. ;	
         format 	  PCT012D058	best12. ;	
         format 	  PCT012D059	best12. ;	
         format 	  PCT012D060	best12. ;	
         format 	  PCT012D061	best12. ;	
         format 	  PCT012D062	best12. ;	
         format 	  PCT012D063	best12. ;	
         format 	  PCT012D064	best12. ;	
         format 	  PCT012D065	best12. ;	
         format 	  PCT012D066	best12. ;	
         format 	  PCT012D067	best12. ;	
         format 	  PCT012D068	best12. ;	
         format 	  PCT012D069	best12. ;	
         format 	  PCT012D070	best12. ;	
         format 	  PCT012D071	best12. ;	
         format 	  PCT012D072	best12. ;	
         format 	  PCT012D073	best12. ;	
         format 	  PCT012D074	best12. ;	
         format 	  PCT012D075	best12. ;	
         format 	  PCT012D076	best12. ;	
         format 	  PCT012D077	best12. ;	
         format 	  PCT012D078	best12. ;	
         format 	  PCT012D079	best12. ;	
         format 	  PCT012D080	best12. ;	
         format 	  PCT012D081	best12. ;	
         format 	  PCT012D082	best12. ;	
         format 	  PCT012D083	best12. ;	
         format 	  PCT012D084	best12. ;	
         format 	  PCT012D085	best12. ;	
         format 	  PCT012D086	best12. ;	
         format 	  PCT012D087	best12. ;	
         format 	  PCT012D088	best12. ;	
         format 	  PCT012D089	best12. ;	
         format 	  PCT012D090	best12. ;	
         format 	  PCT012D091	best12. ;	
         format 	  PCT012D092	best12. ;	
         format 	  PCT012D093	best12. ;	
         format 	  PCT012D094	best12. ;	
         format 	  PCT012D095	best12. ;	
         format 	  PCT012D096	best12. ;	
         format 	  PCT012D097	best12. ;	
         format 	  PCT012D098	best12. ;	
         format 	  PCT012D099	best12. ;	
         format 	  PCT012D100	best12. ;	
         format 	  PCT012D101	best12. ;	
         format 	  PCT012D102	best12. ;	
         format 	  PCT012D103	best12. ;	
         format 	  PCT012D104	best12. ;	
         format 	  PCT012D105	best12. ;	
         format 	  PCT012D106	best12. ;	
         format 	  PCT012D107	best12. ;	
         format 	  PCT012D108	best12. ;	
         format 	  PCT012D109	best12. ;	
         format 	  PCT012D110	best12. ;	
         format 	  PCT012D111	best12. ;	
         format 	  PCT012D112	best12. ;	
         format 	  PCT012D113	best12. ;	
         format 	  PCT012D114	best12. ;	
         format 	  PCT012D115	best12. ;	
         format 	  PCT012D116	best12. ;	
         format 	  PCT012D117	best12. ;	
         format 	  PCT012D118	best12. ;	
         format 	  PCT012D119	best12. ;	
         format 	  PCT012D120	best12. ;	
         format 	  PCT012D121	best12. ;	
         format 	  PCT012D122	best12. ;	
         format 	  PCT012D123	best12. ;	
         format 	  PCT012D124	best12. ;	
         format 	  PCT012D125	best12. ;	
         format 	  PCT012D126	best12. ;	
         format 	  PCT012D127	best12. ;	
         format 	  PCT012D128	best12. ;	
         format 	  PCT012D129	best12. ;	
         format 	  PCT012D130	best12. ;	
         format 	  PCT012D131	best12. ;	
         format 	  PCT012D132	best12. ;	
         format 	  PCT012D133	best12. ;	
         format 	  PCT012D134	best12. ;	
         format 	  PCT012D135	best12. ;	
         format 	  PCT012D136	best12. ;	
         format 	  PCT012D137	best12. ;	
         format 	  PCT012D138	best12. ;	
         format 	  PCT012D139	best12. ;	
         format 	  PCT012D140	best12. ;	
         format 	  PCT012D141	best12. ;	
         format 	  PCT012D142	best12. ;	
         format 	  PCT012D143	best12. ;	
         format 	  PCT012D144	best12. ;	
         format 	  PCT012D145	best12. ;	
         format 	  PCT012D146	best12. ;	
         format 	  PCT012D147	best12. ;	
         format 	  PCT012D148	best12. ;	
         format 	  PCT012D149	best12. ;	
         format 	  PCT012D150	best12. ;	
         format 	  PCT012D151	best12. ;	
         format 	  PCT012D152	best12. ;	
         format 	  PCT012D153	best12. ;	
         format 	  PCT012D154	best12. ;	
         format 	  PCT012D155	best12. ;	
         format 	  PCT012D156	best12. ;	
         format 	  PCT012D157	best12. ;	
         format 	  PCT012D158	best12. ;	
         format 	  PCT012D159	best12. ;	
         format 	  PCT012D160	best12. ;	
         format 	  PCT012D161	best12. ;	
         format 	  PCT012D162	best12. ;	
         format 	  PCT012D163	best12. ;	
         format 	  PCT012D164	best12. ;	
         format 	  PCT012D165	best12. ;	
         format 	  PCT012D166	best12. ;	
         format 	  PCT012D167	best12. ;	
         format 	  PCT012D168	best12. ;	
         format 	  PCT012D169	best12. ;	
         format 	  PCT012D170	best12. ;	
         format 	  PCT012D171	best12. ;	
         format 	  PCT012D172	best12. ;	
         format 	  PCT012D173	best12. ;	
         format 	  PCT012D174	best12. ;	
         format 	  PCT012D175	best12. ;	
         format 	  PCT012D176	best12. ;	
         format 	  PCT012D177	best12. ;	
         format 	  PCT012D178	best12. ;	
         format 	  PCT012D179	best12. ;	
         format 	  PCT012D180	best12. ;	
         format 	  PCT012D181	best12. ;	
         format 	  PCT012D182	best12. ;	
         format 	  PCT012D183	best12. ;	
         format 	  PCT012D184	best12. ;	
         format 	  PCT012D185	best12. ;	
         format 	  PCT012D186	best12. ;	
         format 	  PCT012D187	best12. ;	
         format 	  PCT012D188	best12. ;	
         format 	  PCT012D189	best12. ;	
         format 	  PCT012D190	best12. ;	
         format 	  PCT012D191	best12. ;	
         format 	  PCT012D192	best12. ;	
         format 	  PCT012D193	best12. ;	
         format 	  PCT012D194	best12. ;	
         format 	  PCT012D195	best12. ;	
         format 	  PCT012D196	best12. ;	
         format 	  PCT012D197	best12. ;	
         format 	  PCT012D198	best12. ;	
         format 	  PCT012D199	best12. ;	
         format 	  PCT012D200	best12. ;	
         format 	  PCT012D201	best12. ;	
         format 	  PCT012D202	best12. ;	
         format 	  PCT012D203	best12. ;	
         format 	  PCT012D204	best12. ;	
         format 	  PCT012D205	best12. ;	
         format 	  PCT012D206	best12. ;	
         format 	  PCT012D207	best12. ;	
         format 	  PCT012D208	best12. ;	
         format 	  PCT012D209	best12. ;	
         format 	  PCT012E001	best12. ;	
         format 	  PCT012E002	best12. ;	
         format 	  PCT012E003	best12. ;	
         format 	  PCT012E004	best12. ;	
         format 	  PCT012E005	best12. ;	
         format 	  PCT012E006	best12. ;	
         format 	  PCT012E007	best12. ;	
         format 	  PCT012E008	best12. ;	
         format 	  PCT012E009	best12. ;	
         format 	  PCT012E010	best12. ;	
         format 	  PCT012E011	best12. ;	
         format 	  PCT012E012	best12. ;	
         format 	  PCT012E013	best12. ;	
         format 	  PCT012E014	best12. ;	
         format 	  PCT012E015	best12. ;	
         format 	  PCT012E016	best12. ;	
         format 	  PCT012E017	best12. ;	
         format 	  PCT012E018	best12. ;	
         format 	  PCT012E019	best12. ;	
         format 	  PCT012E020	best12. ;	
         format 	  PCT012E021	best12. ;	
         format 	  PCT012E022	best12. ;	
         format 	  PCT012E023	best12. ;	
         format 	  PCT012E024	best12. ;	
         format 	  PCT012E025	best12. ;	
         format 	  PCT012E026	best12. ;	
         format 	  PCT012E027	best12. ;	
         format 	  PCT012E028	best12. ;	
         format 	  PCT012E029	best12. ;	
         format 	  PCT012E030	best12. ;	
         format 	  PCT012E031	best12. ;	
         format 	  PCT012E032	best12. ;	
         format 	  PCT012E033	best12. ;	
         format 	  PCT012E034	best12. ;	
         format 	  PCT012E035	best12. ;	
         format 	  PCT012E036	best12. ;	
         format 	  PCT012E037	best12. ;	
         format 	  PCT012E038	best12. ;	
         format 	  PCT012E039	best12. ;	
         format 	  PCT012E040	best12. ;	
         format 	  PCT012E041	best12. ;	
         format 	  PCT012E042	best12. ;	
         format 	  PCT012E043	best12. ;	
         format 	  PCT012E044	best12. ;	
         format 	  PCT012E045	best12. ;	
         format 	  PCT012E046	best12. ;	
         format 	  PCT012E047	best12. ;	
         format 	  PCT012E048	best12. ;	
         format 	  PCT012E049	best12. ;	
         format 	  PCT012E050	best12. ;	
         format 	  PCT012E051	best12. ;	
         format 	  PCT012E052	best12. ;	
         format 	  PCT012E053	best12. ;	
         format 	  PCT012E054	best12. ;	
         format 	  PCT012E055	best12. ;	
         format 	  PCT012E056	best12. ;	
         format 	  PCT012E057	best12. ;	
         format 	  PCT012E058	best12. ;	
         format 	  PCT012E059	best12. ;	
         format 	  PCT012E060	best12. ;	
         format 	  PCT012E061	best12. ;	
         format 	  PCT012E062	best12. ;	
         format 	  PCT012E063	best12. ;	
         format 	  PCT012E064	best12. ;	
         format 	  PCT012E065	best12. ;	
         format 	  PCT012E066	best12. ;	
         format 	  PCT012E067	best12. ;	
         format 	  PCT012E068	best12. ;	
         format 	  PCT012E069	best12. ;	
         format 	  PCT012E070	best12. ;	
         format 	  PCT012E071	best12. ;	
         format 	  PCT012E072	best12. ;	
         format 	  PCT012E073	best12. ;	
         format 	  PCT012E074	best12. ;	
         format 	  PCT012E075	best12. ;	
         format 	  PCT012E076	best12. ;	
         format 	  PCT012E077	best12. ;	
         format 	  PCT012E078	best12. ;	
         format 	  PCT012E079	best12. ;	
         format 	  PCT012E080	best12. ;	
         format 	  PCT012E081	best12. ;	
         format 	  PCT012E082	best12. ;	
         format 	  PCT012E083	best12. ;	
         format 	  PCT012E084	best12. ;	
         format 	  PCT012E085	best12. ;	
         format 	  PCT012E086	best12. ;	
         format 	  PCT012E087	best12. ;	
         format 	  PCT012E088	best12. ;	
         format 	  PCT012E089	best12. ;	
         format 	  PCT012E090	best12. ;	
         format 	  PCT012E091	best12. ;	
         format 	  PCT012E092	best12. ;	
         format 	  PCT012E093	best12. ;	
         format 	  PCT012E094	best12. ;	
         format 	  PCT012E095	best12. ;	
         format 	  PCT012E096	best12. ;	
         format 	  PCT012E097	best12. ;	
         format 	  PCT012E098	best12. ;	
         format 	  PCT012E099	best12. ;	
         format 	  PCT012E100	best12. ;	
         format 	  PCT012E101	best12. ;	
         format 	  PCT012E102	best12. ;	
         format 	  PCT012E103	best12. ;	
         format 	  PCT012E104	best12. ;	
         format 	  PCT012E105	best12. ;	
         format 	  PCT012E106	best12. ;	
         format 	  PCT012E107	best12. ;	
         format 	  PCT012E108	best12. ;	
         format 	  PCT012E109	best12. ;	
         format 	  PCT012E110	best12. ;	
         format 	  PCT012E111	best12. ;	
         format 	  PCT012E112	best12. ;	
         format 	  PCT012E113	best12. ;	
         format 	  PCT012E114	best12. ;	
         format 	  PCT012E115	best12. ;	
         format 	  PCT012E116	best12. ;	
         format 	  PCT012E117	best12. ;	
         format 	  PCT012E118	best12. ;	
         format 	  PCT012E119	best12. ;	
         format 	  PCT012E120	best12. ;	
         format 	  PCT012E121	best12. ;	
         format 	  PCT012E122	best12. ;	
         format 	  PCT012E123	best12. ;	
         format 	  PCT012E124	best12. ;	
         format 	  PCT012E125	best12. ;	
         format 	  PCT012E126	best12. ;	
         format 	  PCT012E127	best12. ;	
         format 	  PCT012E128	best12. ;	
         format 	  PCT012E129	best12. ;	
         format 	  PCT012E130	best12. ;	
         format 	  PCT012E131	best12. ;	
         format 	  PCT012E132	best12. ;	
         format 	  PCT012E133	best12. ;	
         format 	  PCT012E134	best12. ;	
         format 	  PCT012E135	best12. ;	
         format 	  PCT012E136	best12. ;	
         format 	  PCT012E137	best12. ;	
         format 	  PCT012E138	best12. ;	
         format 	  PCT012E139	best12. ;	
         format 	  PCT012E140	best12. ;	
         format 	  PCT012E141	best12. ;	
         format 	  PCT012E142	best12. ;	
         format 	  PCT012E143	best12. ;	
         format 	  PCT012E144	best12. ;	
         format 	  PCT012E145	best12. ;	
         format 	  PCT012E146	best12. ;	
         format 	  PCT012E147	best12. ;	
         format 	  PCT012E148	best12. ;	
         format 	  PCT012E149	best12. ;	
         format 	  PCT012E150	best12. ;	
         format 	  PCT012E151	best12. ;	
         format 	  PCT012E152	best12. ;	
         format 	  PCT012E153	best12. ;	
         format 	  PCT012E154	best12. ;	
         format 	  PCT012E155	best12. ;	
         format 	  PCT012E156	best12. ;	
         format 	  PCT012E157	best12. ;	
         format 	  PCT012E158	best12. ;	
         format 	  PCT012E159	best12. ;	
         format 	  PCT012E160	best12. ;	
         format 	  PCT012E161	best12. ;	
         format 	  PCT012E162	best12. ;	
         format 	  PCT012E163	best12. ;	
         format 	  PCT012E164	best12. ;	
         format 	  PCT012E165	best12. ;	
         format 	  PCT012E166	best12. ;	
         format 	  PCT012E167	best12. ;	
         format 	  PCT012E168	best12. ;	
         format 	  PCT012E169	best12. ;	
         format 	  PCT012E170	best12. ;	
         format 	  PCT012E171	best12. ;	
         format 	  PCT012E172	best12. ;	
         format 	  PCT012E173	best12. ;	
         format 	  PCT012E174	best12. ;	
         format 	  PCT012E175	best12. ;	
         format 	  PCT012E176	best12. ;	
         format 	  PCT012E177	best12. ;	
         format 	  PCT012E178	best12. ;	
         format 	  PCT012E179	best12. ;	
         format 	  PCT012E180	best12. ;	
         format 	  PCT012E181	best12. ;	
         format 	  PCT012E182	best12. ;	
         format 	  PCT012E183	best12. ;	
         format 	  PCT012E184	best12. ;	
         format 	  PCT012E185	best12. ;	
         format 	  PCT012E186	best12. ;	
         format 	  PCT012E187	best12. ;	
         format 	  PCT012E188	best12. ;	
         format 	  PCT012E189	best12. ;	
         format 	  PCT012E190	best12. ;	
         format 	  PCT012E191	best12. ;	
         format 	  PCT012E192	best12. ;	
         format 	  PCT012E193	best12. ;	
         format 	  PCT012E194	best12. ;	
         format 	  PCT012E195	best12. ;	
         format 	  PCT012E196	best12. ;	
         format 	  PCT012E197	best12. ;	
         format 	  PCT012E198	best12. ;	
         format 	  PCT012E199	best12. ;	
         format 	  PCT012E200	best12. ;	
         format 	  PCT012E201	best12. ;	
         format 	  PCT012E202	best12. ;	
         format 	  PCT012E203	best12. ;	
         format 	  PCT012E204	best12. ;	
         format 	  PCT012E205	best12. ;	
         format 	  PCT012E206	best12. ;	
         format 	  PCT012E207	best12. ;	
         format 	  PCT012E208	best12. ;	
         format 	  PCT012E209	best12. ;	
         format 	  PCT012F001	best12. ;	
         format 	  PCT012F002	best12. ;	
         format 	  PCT012F003	best12. ;	
         format 	  PCT012F004	best12. ;	
         format 	  PCT012F005	best12. ;	
         format 	  PCT012F006	best12. ;	
         format 	  PCT012F007	best12. ;	
         format 	  PCT012F008	best12. ;	
         format 	  PCT012F009	best12. ;	
         format 	  PCT012F010	best12. ;	
         format 	  PCT012F011	best12. ;	
         format 	  PCT012F012	best12. ;	
         format 	  PCT012F013	best12. ;	
         format 	  PCT012F014	best12. ;	
         format 	  PCT012F015	best12. ;	
         format 	  PCT012F016	best12. ;	
         format 	  PCT012F017	best12. ;	
         format 	  PCT012F018	best12. ;	
         format 	  PCT012F019	best12. ;	
         format 	  PCT012F020	best12. ;	
         format 	  PCT012F021	best12. ;	
         format 	  PCT012F022	best12. ;	
         format 	  PCT012F023	best12. ;	
         format 	  PCT012F024	best12. ;	
         format 	  PCT012F025	best12. ;	
         format 	  PCT012F026	best12. ;	
         format 	  PCT012F027	best12. ;	
         format 	  PCT012F028	best12. ;	
         format 	  PCT012F029	best12. ;	
         format 	  PCT012F030	best12. ;	
         format 	  PCT012F031	best12. ;	
         format 	  PCT012F032	best12. ;	
         format 	  PCT012F033	best12. ;	
         format 	  PCT012F034	best12. ;	
         format 	  PCT012F035	best12. ;	
         format 	  PCT012F036	best12. ;	
         format 	  PCT012F037	best12. ;	
         format 	  PCT012F038	best12. ;	
         format 	  PCT012F039	best12. ;	
         format 	  PCT012F040	best12. ;	
         format 	  PCT012F041	best12. ;	
         format 	  PCT012F042	best12. ;	
         format 	  PCT012F043	best12. ;	
         format 	  PCT012F044	best12. ;	
         format 	  PCT012F045	best12. ;	
         format 	  PCT012F046	best12. ;	
         format 	  PCT012F047	best12. ;	
         format 	  PCT012F048	best12. ;	
         format 	  PCT012F049	best12. ;	
         format 	  PCT012F050	best12. ;	
         format 	  PCT012F051	best12. ;	
         format 	  PCT012F052	best12. ;	
         format 	  PCT012F053	best12. ;	
         format 	  PCT012F054	best12. ;	
         format 	  PCT012F055	best12. ;	
         format 	  PCT012F056	best12. ;	
         format 	  PCT012F057	best12. ;	
         format 	  PCT012F058	best12. ;	
         format 	  PCT012F059	best12. ;	
         format 	  PCT012F060	best12. ;	
         format 	  PCT012F061	best12. ;	
         format 	  PCT012F062	best12. ;	
         format 	  PCT012F063	best12. ;	
         format 	  PCT012F064	best12. ;	
         format 	  PCT012F065	best12. ;	
         format 	  PCT012F066	best12. ;	
         format 	  PCT012F067	best12. ;	
         format 	  PCT012F068	best12. ;	
         format 	  PCT012F069	best12. ;	
         format 	  PCT012F070	best12. ;	
         format 	  PCT012F071	best12. ;	
         format 	  PCT012F072	best12. ;	
         format 	  PCT012F073	best12. ;	
         format 	  PCT012F074	best12. ;	
         format 	  PCT012F075	best12. ;	
         format 	  PCT012F076	best12. ;	
         format 	  PCT012F077	best12. ;	
         format 	  PCT012F078	best12. ;	
         format 	  PCT012F079	best12. ;	
         format 	  PCT012F080	best12. ;	
         format 	  PCT012F081	best12. ;	
         format 	  PCT012F082	best12. ;	
         format 	  PCT012F083	best12. ;	
         format 	  PCT012F084	best12. ;	
         format 	  PCT012F085	best12. ;	
         format 	  PCT012F086	best12. ;	
         format 	  PCT012F087	best12. ;	
         format 	  PCT012F088	best12. ;	
         format 	  PCT012F089	best12. ;	
         format 	  PCT012F090	best12. ;	
         format 	  PCT012F091	best12. ;	
         format 	  PCT012F092	best12. ;	
         format 	  PCT012F093	best12. ;	
         format 	  PCT012F094	best12. ;	
         format 	  PCT012F095	best12. ;	
         format 	  PCT012F096	best12. ;	
         format 	  PCT012F097	best12. ;	
         format 	  PCT012F098	best12. ;	
         format 	  PCT012F099	best12. ;	
         format 	  PCT012F100	best12. ;	
         format 	  PCT012F101	best12. ;	
         format 	  PCT012F102	best12. ;	
         format 	  PCT012F103	best12. ;	
         format 	  PCT012F104	best12. ;	
         format 	  PCT012F105	best12. ;	
         format 	  PCT012F106	best12. ;	
         format 	  PCT012F107	best12. ;	
         format 	  PCT012F108	best12. ;	
         format 	  PCT012F109	best12. ;	
         format 	  PCT012F110	best12. ;	
         format 	  PCT012F111	best12. ;	
         format 	  PCT012F112	best12. ;	
         format 	  PCT012F113	best12. ;	
         format 	  PCT012F114	best12. ;	
         format 	  PCT012F115	best12. ;	
         format 	  PCT012F116	best12. ;	
         format 	  PCT012F117	best12. ;	
         format 	  PCT012F118	best12. ;	
         format 	  PCT012F119	best12. ;	
         format 	  PCT012F120	best12. ;	
         format 	  PCT012F121	best12. ;	
         format 	  PCT012F122	best12. ;	
         format 	  PCT012F123	best12. ;	
         format 	  PCT012F124	best12. ;	
         format 	  PCT012F125	best12. ;	
         format 	  PCT012F126	best12. ;	
         format 	  PCT012F127	best12. ;	
         format 	  PCT012F128	best12. ;	
         format 	  PCT012F129	best12. ;	
         format 	  PCT012F130	best12. ;	
         format 	  PCT012F131	best12. ;	
         format 	  PCT012F132	best12. ;	
         format 	  PCT012F133	best12. ;	
         format 	  PCT012F134	best12. ;	
         format 	  PCT012F135	best12. ;	
         format 	  PCT012F136	best12. ;	
         format 	  PCT012F137	best12. ;	
         format 	  PCT012F138	best12. ;	
         format 	  PCT012F139	best12. ;	
         format 	  PCT012F140	best12. ;	
         format 	  PCT012F141	best12. ;	
         format 	  PCT012F142	best12. ;	
         format 	  PCT012F143	best12. ;	
         format 	  PCT012F144	best12. ;	
         format 	  PCT012F145	best12. ;	
         format 	  PCT012F146	best12. ;	
         format 	  PCT012F147	best12. ;	
         format 	  PCT012F148	best12. ;	
         format 	  PCT012F149	best12. ;	
         format 	  PCT012F150	best12. ;	
         format 	  PCT012F151	best12. ;	
         format 	  PCT012F152	best12. ;	
         format 	  PCT012F153	best12. ;	
         format 	  PCT012F154	best12. ;	
         format 	  PCT012F155	best12. ;	
         format 	  PCT012F156	best12. ;	
         format 	  PCT012F157	best12. ;	
         format 	  PCT012F158	best12. ;	
         format 	  PCT012F159	best12. ;	
         format 	  PCT012F160	best12. ;	
         format 	  PCT012F161	best12. ;	
         format 	  PCT012F162	best12. ;	
         format 	  PCT012F163	best12. ;	
         format 	  PCT012F164	best12. ;	
         format 	  PCT012F165	best12. ;	
         format 	  PCT012F166	best12. ;	
         format 	  PCT012F167	best12. ;	
         format 	  PCT012F168	best12. ;	
         format 	  PCT012F169	best12. ;	
         format 	  PCT012F170	best12. ;	
         format 	  PCT012F171	best12. ;	
         format 	  PCT012F172	best12. ;	
         format 	  PCT012F173	best12. ;	
         format 	  PCT012F174	best12. ;	
         format 	  PCT012F175	best12. ;	
         format 	  PCT012F176	best12. ;	
         format 	  PCT012F177	best12. ;	
         format 	  PCT012F178	best12. ;	
         format 	  PCT012F179	best12. ;	
         format 	  PCT012F180	best12. ;	
         format 	  PCT012F181	best12. ;	
         format 	  PCT012F182	best12. ;	
         format 	  PCT012F183	best12. ;	
         format 	  PCT012F184	best12. ;	
         format 	  PCT012F185	best12. ;	
         format 	  PCT012F186	best12. ;	
         format 	  PCT012F187	best12. ;	
         format 	  PCT012F188	best12. ;	
         format 	  PCT012F189	best12. ;	
         format 	  PCT012F190	best12. ;	
         format 	  PCT012F191	best12. ;	
         format 	  PCT012F192	best12. ;	
         format 	  PCT012F193	best12. ;	
         format 	  PCT012F194	best12. ;	
         format 	  PCT012F195	best12. ;	
         format 	  PCT012F196	best12. ;	
         format 	  PCT012F197	best12. ;	
         format 	  PCT012F198	best12. ;	
         format 	  PCT012F199	best12. ;	
         format 	  PCT012F200	best12. ;	
         format 	  PCT012F201	best12. ;	
         format 	  PCT012F202	best12. ;	
         format 	  PCT012F203	best12. ;	
         format 	  PCT012F204	best12. ;	
         format 	  PCT012F205	best12. ;	
         format 	  PCT012F206	best12. ;	
         format 	  PCT012F207	best12. ;	
         format 	  PCT012F208	best12. ;	
         format 	  PCT012F209	best12. ;	
         format 	  PCT012G001	best12. ;	
         format 	  PCT012G002	best12. ;	
         format 	  PCT012G003	best12. ;	
         format 	  PCT012G004	best12. ;	
         format 	  PCT012G005	best12. ;	
         format 	  PCT012G006	best12. ;	
         format 	  PCT012G007	best12. ;	
         format 	  PCT012G008	best12. ;	
         format 	  PCT012G009	best12. ;	
         format 	  PCT012G010	best12. ;	
         format 	  PCT012G011	best12. ;	
         format 	  PCT012G012	best12. ;	
         format 	  PCT012G013	best12. ;	
         format 	  PCT012G014	best12. ;	
         format 	  PCT012G015	best12. ;	
         format 	  PCT012G016	best12. ;	
         format 	  PCT012G017	best12. ;	
         format 	  PCT012G018	best12. ;	
         format 	  PCT012G019	best12. ;	
         format 	  PCT012G020	best12. ;	
         format 	  PCT012G021	best12. ;	
         format 	  PCT012G022	best12. ;	
         format 	  PCT012G023	best12. ;	
         format 	  PCT012G024	best12. ;	
         format 	  PCT012G025	best12. ;	
         format 	  PCT012G026	best12. ;	
         format 	  PCT012G027	best12. ;	
         format 	  PCT012G028	best12. ;	
         format 	  PCT012G029	best12. ;	
         format 	  PCT012G030	best12. ;	
         format 	  PCT012G031	best12. ;	
         format 	  PCT012G032	best12. ;	
         format 	  PCT012G033	best12. ;	
         format 	  PCT012G034	best12. ;	
         format 	  PCT012G035	best12. ;	
         format 	  PCT012G036	best12. ;	
         format 	  PCT012G037	best12. ;	
         format 	  PCT012G038	best12. ;	
         format 	  PCT012G039	best12. ;	
         format 	  PCT012G040	best12. ;	
         format 	  PCT012G041	best12. ;	
         format 	  PCT012G042	best12. ;	
         format 	  PCT012G043	best12. ;	
         format 	  PCT012G044	best12. ;	
         format 	  PCT012G045	best12. ;	
         format 	  PCT012G046	best12. ;	
         format 	  PCT012G047	best12. ;	
         format 	  PCT012G048	best12. ;	
         format 	  PCT012G049	best12. ;	
         format 	  PCT012G050	best12. ;	
         format 	  PCT012G051	best12. ;	
         format 	  PCT012G052	best12. ;	
         format 	  PCT012G053	best12. ;	
         format 	  PCT012G054	best12. ;	
         format 	  PCT012G055	best12. ;	
         format 	  PCT012G056	best12. ;	
         format 	  PCT012G057	best12. ;	
         format 	  PCT012G058	best12. ;	
         format 	  PCT012G059	best12. ;	
         format 	  PCT012G060	best12. ;	
         format 	  PCT012G061	best12. ;	
         format 	  PCT012G062	best12. ;	
         format 	  PCT012G063	best12. ;	
         format 	  PCT012G064	best12. ;	
         format 	  PCT012G065	best12. ;	
         format 	  PCT012G066	best12. ;	
         format 	  PCT012G067	best12. ;	
         format 	  PCT012G068	best12. ;	
         format 	  PCT012G069	best12. ;	
         format 	  PCT012G070	best12. ;	
         format 	  PCT012G071	best12. ;	
         format 	  PCT012G072	best12. ;	
         format 	  PCT012G073	best12. ;	
         format 	  PCT012G074	best12. ;	
         format 	  PCT012G075	best12. ;	
         format 	  PCT012G076	best12. ;	
         format 	  PCT012G077	best12. ;	
         format 	  PCT012G078	best12. ;	
         format 	  PCT012G079	best12. ;	
         format 	  PCT012G080	best12. ;	
         format 	  PCT012G081	best12. ;	
         format 	  PCT012G082	best12. ;	
         format 	  PCT012G083	best12. ;	
         format 	  PCT012G084	best12. ;	
         format 	  PCT012G085	best12. ;	
         format 	  PCT012G086	best12. ;	
         format 	  PCT012G087	best12. ;	
         format 	  PCT012G088	best12. ;	
         format 	  PCT012G089	best12. ;	
         format 	  PCT012G090	best12. ;	
         format 	  PCT012G091	best12. ;	
         format 	  PCT012G092	best12. ;	
         format 	  PCT012G093	best12. ;	
         format 	  PCT012G094	best12. ;	
         format 	  PCT012G095	best12. ;	
         format 	  PCT012G096	best12. ;	
         format 	  PCT012G097	best12. ;	
         format 	  PCT012G098	best12. ;	
         format 	  PCT012G099	best12. ;	
         format 	  PCT012G100	best12. ;	
         format 	  PCT012G101	best12. ;	
         format 	  PCT012G102	best12. ;	
         format 	  PCT012G103	best12. ;	
         format 	  PCT012G104	best12. ;	
         format 	  PCT012G105	best12. ;	
         format 	  PCT012G106	best12. ;	
         format 	  PCT012G107	best12. ;	
         format 	  PCT012G108	best12. ;	
         format 	  PCT012G109	best12. ;	
         format 	  PCT012G110	best12. ;	
         format 	  PCT012G111	best12. ;	
         format 	  PCT012G112	best12. ;	
         format 	  PCT012G113	best12. ;	
         format 	  PCT012G114	best12. ;	
         format 	  PCT012G115	best12. ;	
         format 	  PCT012G116	best12. ;	
         format 	  PCT012G117	best12. ;	
         format 	  PCT012G118	best12. ;	
         format 	  PCT012G119	best12. ;	
         format 	  PCT012G120	best12. ;	
         format 	  PCT012G121	best12. ;	
         format 	  PCT012G122	best12. ;	
         format 	  PCT012G123	best12. ;	
         format 	  PCT012G124	best12. ;	
         format 	  PCT012G125	best12. ;	
         format 	  PCT012G126	best12. ;	
         format 	  PCT012G127	best12. ;	
         format 	  PCT012G128	best12. ;	
         format 	  PCT012G129	best12. ;	
         format 	  PCT012G130	best12. ;	
         format 	  PCT012G131	best12. ;	
         format 	  PCT012G132	best12. ;	
         format 	  PCT012G133	best12. ;	
         format 	  PCT012G134	best12. ;	
         format 	  PCT012G135	best12. ;	
         format 	  PCT012G136	best12. ;	
         format 	  PCT012G137	best12. ;	
         format 	  PCT012G138	best12. ;	
         format 	  PCT012G139	best12. ;	
         format 	  PCT012G140	best12. ;	
         format 	  PCT012G141	best12. ;	
         format 	  PCT012G142	best12. ;	
         format 	  PCT012G143	best12. ;	
         format 	  PCT012G144	best12. ;	
         format 	  PCT012G145	best12. ;	
         format 	  PCT012G146	best12. ;	
         format 	  PCT012G147	best12. ;	
         format 	  PCT012G148	best12. ;	
         format 	  PCT012G149	best12. ;	
         format 	  PCT012G150	best12. ;	
         format 	  PCT012G151	best12. ;	
         format 	  PCT012G152	best12. ;	
         format 	  PCT012G153	best12. ;	
         format 	  PCT012G154	best12. ;	
         format 	  PCT012G155	best12. ;	
         format 	  PCT012G156	best12. ;	
         format 	  PCT012G157	best12. ;	
         format 	  PCT012G158	best12. ;	
         format 	  PCT012G159	best12. ;	
         format 	  PCT012G160	best12. ;	
         format 	  PCT012G161	best12. ;	
         format 	  PCT012G162	best12. ;	
         format 	  PCT012G163	best12. ;	
         format 	  PCT012G164	best12. ;	
         format 	  PCT012G165	best12. ;	
         format 	  PCT012G166	best12. ;	
         format 	  PCT012G167	best12. ;	
         format 	  PCT012G168	best12. ;	
         format 	  PCT012G169	best12. ;	
         format 	  PCT012G170	best12. ;	
         format 	  PCT012G171	best12. ;	
         format 	  PCT012G172	best12. ;	
         format 	  PCT012G173	best12. ;	
         format 	  PCT012G174	best12. ;	
         format 	  PCT012G175	best12. ;	
         format 	  PCT012G176	best12. ;	
         format 	  PCT012G177	best12. ;	
         format 	  PCT012G178	best12. ;	
         format 	  PCT012G179	best12. ;	
         format 	  PCT012G180	best12. ;	
         format 	  PCT012G181	best12. ;	
         format 	  PCT012G182	best12. ;	
         format 	  PCT012G183	best12. ;	
         format 	  PCT012G184	best12. ;	
         format 	  PCT012G185	best12. ;	
         format 	  PCT012G186	best12. ;	
         format 	  PCT012G187	best12. ;	
         format 	  PCT012G188	best12. ;	
         format 	  PCT012G189	best12. ;	
         format 	  PCT012G190	best12. ;	
         format 	  PCT012G191	best12. ;	
         format 	  PCT012G192	best12. ;	
         format 	  PCT012G193	best12. ;	
         format 	  PCT012G194	best12. ;	
         format 	  PCT012G195	best12. ;	
         format 	  PCT012G196	best12. ;	
         format 	  PCT012G197	best12. ;	
         format 	  PCT012G198	best12. ;	
         format 	  PCT012G199	best12. ;	
         format 	  PCT012G200	best12. ;	
         format 	  PCT012G201	best12. ;	
         format 	  PCT012G202	best12. ;	
         format 	  PCT012G203	best12. ;	
         format 	  PCT012G204	best12. ;	
         format 	  PCT012G205	best12. ;	
         format 	  PCT012G206	best12. ;	
         format 	  PCT012G207	best12. ;	
         format 	  PCT012G208	best12. ;	
         format 	  PCT012G209	best12. ;	
         format 	  PCT012H001	best12. ;	
         format 	  PCT012H002	best12. ;	
         format 	  PCT012H003	best12. ;	
         format 	  PCT012H004	best12. ;	
         format 	  PCT012H005	best12. ;	
         format 	  PCT012H006	best12. ;	
         format 	  PCT012H007	best12. ;	
         format 	  PCT012H008	best12. ;	
         format 	  PCT012H009	best12. ;	
         format 	  PCT012H010	best12. ;	
         format 	  PCT012H011	best12. ;	
         format 	  PCT012H012	best12. ;	
         format 	  PCT012H013	best12. ;	
         format 	  PCT012H014	best12. ;	
         format 	  PCT012H015	best12. ;	
         format 	  PCT012H016	best12. ;	
         format 	  PCT012H017	best12. ;	
         format 	  PCT012H018	best12. ;	
         format 	  PCT012H019	best12. ;	
         format 	  PCT012H020	best12. ;	
         format 	  PCT012H021	best12. ;	
         format 	  PCT012H022	best12. ;	
         format 	  PCT012H023	best12. ;	
         format 	  PCT012H024	best12. ;	
         format 	  PCT012H025	best12. ;	
         format 	  PCT012H026	best12. ;	
         format 	  PCT012H027	best12. ;	
         format 	  PCT012H028	best12. ;	
         format 	  PCT012H029	best12. ;	
         format 	  PCT012H030	best12. ;	
         format 	  PCT012H031	best12. ;	
         format 	  PCT012H032	best12. ;	
         format 	  PCT012H033	best12. ;	
         format 	  PCT012H034	best12. ;	
         format 	  PCT012H035	best12. ;	
         format 	  PCT012H036	best12. ;	
         format 	  PCT012H037	best12. ;	
         format 	  PCT012H038	best12. ;	
         format 	  PCT012H039	best12. ;	
         format 	  PCT012H040	best12. ;	
         format 	  PCT012H041	best12. ;	
         format 	  PCT012H042	best12. ;	
         format 	  PCT012H043	best12. ;	
         format 	  PCT012H044	best12. ;	
         format 	  PCT012H045	best12. ;	
         format 	  PCT012H046	best12. ;	
         format 	  PCT012H047	best12. ;	
         format 	  PCT012H048	best12. ;	
         format 	  PCT012H049	best12. ;	
         format 	  PCT012H050	best12. ;	
         format 	  PCT012H051	best12. ;	
         format 	  PCT012H052	best12. ;	
         format 	  PCT012H053	best12. ;	
         format 	  PCT012H054	best12. ;	
         format 	  PCT012H055	best12. ;	
         format 	  PCT012H056	best12. ;	
         format 	  PCT012H057	best12. ;	
         format 	  PCT012H058	best12. ;	
         format 	  PCT012H059	best12. ;	
         format 	  PCT012H060	best12. ;	
         format 	  PCT012H061	best12. ;	
         format 	  PCT012H062	best12. ;	
         format 	  PCT012H063	best12. ;	
         format 	  PCT012H064	best12. ;	
         format 	  PCT012H065	best12. ;	
         format 	  PCT012H066	best12. ;	
         format 	  PCT012H067	best12. ;	
         format 	  PCT012H068	best12. ;	
         format 	  PCT012H069	best12. ;	
         format 	  PCT012H070	best12. ;	
         format 	  PCT012H071	best12. ;	
         format 	  PCT012H072	best12. ;	
         format 	  PCT012H073	best12. ;	
         format 	  PCT012H074	best12. ;	
         format 	  PCT012H075	best12. ;	
         format 	  PCT012H076	best12. ;	
         format 	  PCT012H077	best12. ;	
         format 	  PCT012H078	best12. ;	
         format 	  PCT012H079	best12. ;	
         format 	  PCT012H080	best12. ;	
         format 	  PCT012H081	best12. ;	
         format 	  PCT012H082	best12. ;	
         format 	  PCT012H083	best12. ;	
         format 	  PCT012H084	best12. ;	
         format 	  PCT012H085	best12. ;	
         format 	  PCT012H086	best12. ;	
         format 	  PCT012H087	best12. ;	
         format 	  PCT012H088	best12. ;	
         format 	  PCT012H089	best12. ;	
         format 	  PCT012H090	best12. ;	
         format 	  PCT012H091	best12. ;	
         format 	  PCT012H092	best12. ;	
         format 	  PCT012H093	best12. ;	
         format 	  PCT012H094	best12. ;	
         format 	  PCT012H095	best12. ;	
         format 	  PCT012H096	best12. ;	
         format 	  PCT012H097	best12. ;	
         format 	  PCT012H098	best12. ;	
         format 	  PCT012H099	best12. ;	
         format 	  PCT012H100	best12. ;	
         format 	  PCT012H101	best12. ;	
         format 	  PCT012H102	best12. ;	
         format 	  PCT012H103	best12. ;	
         format 	  PCT012H104	best12. ;	
         format 	  PCT012H105	best12. ;	
         format 	  PCT012H106	best12. ;	
         format 	  PCT012H107	best12. ;	
         format 	  PCT012H108	best12. ;	
         format 	  PCT012H109	best12. ;	
         format 	  PCT012H110	best12. ;	
         format 	  PCT012H111	best12. ;	
         format 	  PCT012H112	best12. ;	
         format 	  PCT012H113	best12. ;	
         format 	  PCT012H114	best12. ;	
         format 	  PCT012H115	best12. ;	
         format 	  PCT012H116	best12. ;	
         format 	  PCT012H117	best12. ;	
         format 	  PCT012H118	best12. ;	
         format 	  PCT012H119	best12. ;	
         format 	  PCT012H120	best12. ;	
         format 	  PCT012H121	best12. ;	
         format 	  PCT012H122	best12. ;	
         format 	  PCT012H123	best12. ;	
         format 	  PCT012H124	best12. ;	
         format 	  PCT012H125	best12. ;	
         format 	  PCT012H126	best12. ;	
         format 	  PCT012H127	best12. ;	
         format 	  PCT012H128	best12. ;	
         format 	  PCT012H129	best12. ;	
         format 	  PCT012H130	best12. ;	
         format 	  PCT012H131	best12. ;	
         format 	  PCT012H132	best12. ;	
         format 	  PCT012H133	best12. ;	
         format 	  PCT012H134	best12. ;	
         format 	  PCT012H135	best12. ;	
         format 	  PCT012H136	best12. ;	
         format 	  PCT012H137	best12. ;	
         format 	  PCT012H138	best12. ;	
         format 	  PCT012H139	best12. ;	
         format 	  PCT012H140	best12. ;	
         format 	  PCT012H141	best12. ;	
         format 	  PCT012H142	best12. ;	
         format 	  PCT012H143	best12. ;	
         format 	  PCT012H144	best12. ;	
         format 	  PCT012H145	best12. ;	
         format 	  PCT012H146	best12. ;	
         format 	  PCT012H147	best12. ;	
         format 	  PCT012H148	best12. ;	
         format 	  PCT012H149	best12. ;	
         format 	  PCT012H150	best12. ;	
         format 	  PCT012H151	best12. ;	
         format 	  PCT012H152	best12. ;	
         format 	  PCT012H153	best12. ;	
         format 	  PCT012H154	best12. ;	
         format 	  PCT012H155	best12. ;	
         format 	  PCT012H156	best12. ;	
         format 	  PCT012H157	best12. ;	
         format 	  PCT012H158	best12. ;	
         format 	  PCT012H159	best12. ;	
         format 	  PCT012H160	best12. ;	
         format 	  PCT012H161	best12. ;	
         format 	  PCT012H162	best12. ;	
         format 	  PCT012H163	best12. ;	
         format 	  PCT012H164	best12. ;	
         format 	  PCT012H165	best12. ;	
         format 	  PCT012H166	best12. ;	
         format 	  PCT012H167	best12. ;	
         format 	  PCT012H168	best12. ;	
         format 	  PCT012H169	best12. ;	
         format 	  PCT012H170	best12. ;	
         format 	  PCT012H171	best12. ;	
         format 	  PCT012H172	best12. ;	
         format 	  PCT012H173	best12. ;	
         format 	  PCT012H174	best12. ;	
         format 	  PCT012H175	best12. ;	
         format 	  PCT012H176	best12. ;	
         format 	  PCT012H177	best12. ;	
         format 	  PCT012H178	best12. ;	
         format 	  PCT012H179	best12. ;	
         format 	  PCT012H180	best12. ;	
         format 	  PCT012H181	best12. ;	
         format 	  PCT012H182	best12. ;	
         format 	  PCT012H183	best12. ;	
         format 	  PCT012H184	best12. ;	
         format 	  PCT012H185	best12. ;	
         format 	  PCT012H186	best12. ;	
         format 	  PCT012H187	best12. ;	
         format 	  PCT012H188	best12. ;	
         format 	  PCT012H189	best12. ;	
         format 	  PCT012H190	best12. ;	
         format 	  PCT012H191	best12. ;	
         format 	  PCT012H192	best12. ;	
         format 	  PCT012H193	best12. ;	
         format 	  PCT012H194	best12. ;	
         format 	  PCT012H195	best12. ;	
         format 	  PCT012H196	best12. ;	
         format 	  PCT012H197	best12. ;	
         format 	  PCT012H198	best12. ;	
         format 	  PCT012H199	best12. ;	
         format 	  PCT012H200	best12. ;	
         format 	  PCT012H201	best12. ;	
         format 	  PCT012H202	best12. ;	
         format 	  PCT012H203	best12. ;	
         format 	  PCT012H204	best12. ;	
         format 	  PCT012H205	best12. ;	
         format 	  PCT012H206	best12. ;	
         format 	  PCT012H207	best12. ;	
         format 	  PCT012H208	best12. ;	
         format 	  PCT012H209	best12. ;	
         format 	  PCT012I001	best12. ;	
         format 	  PCT012I002	best12. ;	
         format 	  PCT012I003	best12. ;	
         format 	  PCT012I004	best12. ;	
         format 	  PCT012I005	best12. ;	
         format 	  PCT012I006	best12. ;	
         format 	  PCT012I007	best12. ;	
         format 	  PCT012I008	best12. ;	
         format 	  PCT012I009	best12. ;	
         format 	  PCT012I010	best12. ;	
         format 	  PCT012I011	best12. ;	
         format 	  PCT012I012	best12. ;	
         format 	  PCT012I013	best12. ;	
         format 	  PCT012I014	best12. ;	
         format 	  PCT012I015	best12. ;	
         format 	  PCT012I016	best12. ;	
         format 	  PCT012I017	best12. ;	
         format 	  PCT012I018	best12. ;	
         format 	  PCT012I019	best12. ;	
         format 	  PCT012I020	best12. ;	
         format 	  PCT012I021	best12. ;	
         format 	  PCT012I022	best12. ;	
         format 	  PCT012I023	best12. ;	
         format 	  PCT012I024	best12. ;	
         format 	  PCT012I025	best12. ;	
         format 	  PCT012I026	best12. ;	
         format 	  PCT012I027	best12. ;	
         format 	  PCT012I028	best12. ;	
         format 	  PCT012I029	best12. ;	
         format 	  PCT012I030	best12. ;	
         format 	  PCT012I031	best12. ;	
         format 	  PCT012I032	best12. ;	
         format 	  PCT012I033	best12. ;	
         format 	  PCT012I034	best12. ;	
         format 	  PCT012I035	best12. ;	
         format 	  PCT012I036	best12. ;	
         format 	  PCT012I037	best12. ;	
         format 	  PCT012I038	best12. ;	
         format 	  PCT012I039	best12. ;	
         format 	  PCT012I040	best12. ;	
         format 	  PCT012I041	best12. ;	
         format 	  PCT012I042	best12. ;	
         format 	  PCT012I043	best12. ;	
         format 	  PCT012I044	best12. ;	
         format 	  PCT012I045	best12. ;	
         format 	  PCT012I046	best12. ;	
         format 	  PCT012I047	best12. ;	
         format 	  PCT012I048	best12. ;	
         format 	  PCT012I049	best12. ;	
         format 	  PCT012I050	best12. ;	
         format 	  PCT012I051	best12. ;	
         format 	  PCT012I052	best12. ;	
         format 	  PCT012I053	best12. ;	
         format 	  PCT012I054	best12. ;	
         format 	  PCT012I055	best12. ;	
         format 	  PCT012I056	best12. ;	
         format 	  PCT012I057	best12. ;	
         format 	  PCT012I058	best12. ;	
         format 	  PCT012I059	best12. ;	
         format 	  PCT012I060	best12. ;	
         format 	  PCT012I061	best12. ;	
         format 	  PCT012I062	best12. ;	
         format 	  PCT012I063	best12. ;	
         format 	  PCT012I064	best12. ;	
         format 	  PCT012I065	best12. ;	
         format 	  PCT012I066	best12. ;	
         format 	  PCT012I067	best12. ;	
         format 	  PCT012I068	best12. ;	
         format 	  PCT012I069	best12. ;	
         format 	  PCT012I070	best12. ;	
         format 	  PCT012I071	best12. ;	
         format 	  PCT012I072	best12. ;	
         format 	  PCT012I073	best12. ;	
         format 	  PCT012I074	best12. ;	
         format 	  PCT012I075	best12. ;	
         format 	  PCT012I076	best12. ;	
         format 	  PCT012I077	best12. ;	
         format 	  PCT012I078	best12. ;	
         format 	  PCT012I079	best12. ;	
         format 	  PCT012I080	best12. ;	
         format 	  PCT012I081	best12. ;	
         format 	  PCT012I082	best12. ;	
         format 	  PCT012I083	best12. ;	
         format 	  PCT012I084	best12. ;	
         format 	  PCT012I085	best12. ;	
         format 	  PCT012I086	best12. ;	
         format 	  PCT012I087	best12. ;	
         format 	  PCT012I088	best12. ;	
         format 	  PCT012I089	best12. ;	
         format 	  PCT012I090	best12. ;	
         format 	  PCT012I091	best12. ;	
         format 	  PCT012I092	best12. ;	
         format 	  PCT012I093	best12. ;	
         format 	  PCT012I094	best12. ;	
         format 	  PCT012I095	best12. ;	
         format 	  PCT012I096	best12. ;	
         format 	  PCT012I097	best12. ;	
         format 	  PCT012I098	best12. ;	
         format 	  PCT012I099	best12. ;	
         format 	  PCT012I100	best12. ;	
         format 	  PCT012I101	best12. ;	
         format 	  PCT012I102	best12. ;	
         format 	  PCT012I103	best12. ;	
         format 	  PCT012I104	best12. ;	
         format 	  PCT012I105	best12. ;	
         format 	  PCT012I106	best12. ;	
         format 	  PCT012I107	best12. ;	
         format 	  PCT012I108	best12. ;	
         format 	  PCT012I109	best12. ;	
         format 	  PCT012I110	best12. ;	
         format 	  PCT012I111	best12. ;	
         format 	  PCT012I112	best12. ;	
         format 	  PCT012I113	best12. ;	
         format 	  PCT012I114	best12. ;	
         format 	  PCT012I115	best12. ;	
         format 	  PCT012I116	best12. ;	
         format 	  PCT012I117	best12. ;	
         format 	  PCT012I118	best12. ;	
         format 	  PCT012I119	best12. ;	
         format 	  PCT012I120	best12. ;	
         format 	  PCT012I121	best12. ;	
         format 	  PCT012I122	best12. ;	
         format 	  PCT012I123	best12. ;	
         format 	  PCT012I124	best12. ;	
         format 	  PCT012I125	best12. ;	
         format 	  PCT012I126	best12. ;	
         format 	  PCT012I127	best12. ;	
         format 	  PCT012I128	best12. ;	
         format 	  PCT012I129	best12. ;	
         format 	  PCT012I130	best12. ;	
         format 	  PCT012I131	best12. ;	
         format 	  PCT012I132	best12. ;	
         format 	  PCT012I133	best12. ;	
         format 	  PCT012I134	best12. ;	
         format 	  PCT012I135	best12. ;	
         format 	  PCT012I136	best12. ;	
         format 	  PCT012I137	best12. ;	
         format 	  PCT012I138	best12. ;	
         format 	  PCT012I139	best12. ;	
         format 	  PCT012I140	best12. ;	
         format 	  PCT012I141	best12. ;	
         format 	  PCT012I142	best12. ;	
         format 	  PCT012I143	best12. ;	
         format 	  PCT012I144	best12. ;	
         format 	  PCT012I145	best12. ;	
         format 	  PCT012I146	best12. ;	
         format 	  PCT012I147	best12. ;	
         format 	  PCT012I148	best12. ;	
         format 	  PCT012I149	best12. ;	
         format 	  PCT012I150	best12. ;	
         format 	  PCT012I151	best12. ;	
         format 	  PCT012I152	best12. ;	
         format 	  PCT012I153	best12. ;	
         format 	  PCT012I154	best12. ;	
         format 	  PCT012I155	best12. ;	
         format 	  PCT012I156	best12. ;	
         format 	  PCT012I157	best12. ;	
         format 	  PCT012I158	best12. ;	
         format 	  PCT012I159	best12. ;	
         format 	  PCT012I160	best12. ;	
         format 	  PCT012I161	best12. ;	
         format 	  PCT012I162	best12. ;	
         format 	  PCT012I163	best12. ;	
         format 	  PCT012I164	best12. ;	
         format 	  PCT012I165	best12. ;	
         format 	  PCT012I166	best12. ;	
         format 	  PCT012I167	best12. ;	
         format 	  PCT012I168	best12. ;	
         format 	  PCT012I169	best12. ;	
         format 	  PCT012I170	best12. ;	
         format 	  PCT012I171	best12. ;	
         format 	  PCT012I172	best12. ;	
         format 	  PCT012I173	best12. ;	
         format 	  PCT012I174	best12. ;	
         format 	  PCT012I175	best12. ;	
         format 	  PCT012I176	best12. ;	
         format 	  PCT012I177	best12. ;	
         format 	  PCT012I178	best12. ;	
         format 	  PCT012I179	best12. ;	
         format 	  PCT012I180	best12. ;	
         format 	  PCT012I181	best12. ;	
         format 	  PCT012I182	best12. ;	
         format 	  PCT012I183	best12. ;	
         format 	  PCT012I184	best12. ;	
         format 	  PCT012I185	best12. ;	
         format 	  PCT012I186	best12. ;	
         format 	  PCT012I187	best12. ;	
         format 	  PCT012I188	best12. ;	
         format 	  PCT012I189	best12. ;	
         format 	  PCT012I190	best12. ;	
         format 	  PCT012I191	best12. ;	
         format 	  PCT012I192	best12. ;	
         format 	  PCT012I193	best12. ;	
         format 	  PCT012I194	best12. ;	
         format 	  PCT012I195	best12. ;	
         format 	  PCT012I196	best12. ;	
         format 	  PCT012I197	best12. ;	
         format 	  PCT012I198	best12. ;	
         format 	  PCT012I199	best12. ;	
         format 	  PCT012I200	best12. ;	
         format 	  PCT012I201	best12. ;	
         format 	  PCT012I202	best12. ;	
         format 	  PCT012I203	best12. ;	
         format 	  PCT012I204	best12. ;	
         format 	  PCT012I205	best12. ;	
         format 	  PCT012I206	best12. ;	
         format 	  PCT012I207	best12. ;	
         format 	  PCT012I208	best12. ;	
         format 	  PCT012I209	best12. ;	
         format 	  PCT012J001	best12. ;	
         format 	  PCT012J002	best12. ;	
         format 	  PCT012J003	best12. ;	
         format 	  PCT012J004	best12. ;	
         format 	  PCT012J005	best12. ;	
         format 	  PCT012J006	best12. ;	
         format 	  PCT012J007	best12. ;	
         format 	  PCT012J008	best12. ;	
         format 	  PCT012J009	best12. ;	
         format 	  PCT012J010	best12. ;	
         format 	  PCT012J011	best12. ;	
         format 	  PCT012J012	best12. ;	
         format 	  PCT012J013	best12. ;	
         format 	  PCT012J014	best12. ;	
         format 	  PCT012J015	best12. ;	
         format 	  PCT012J016	best12. ;	
         format 	  PCT012J017	best12. ;	
         format 	  PCT012J018	best12. ;	
         format 	  PCT012J019	best12. ;	
         format 	  PCT012J020	best12. ;	
         format 	  PCT012J021	best12. ;	
         format 	  PCT012J022	best12. ;	
         format 	  PCT012J023	best12. ;	
         format 	  PCT012J024	best12. ;	
         format 	  PCT012J025	best12. ;	
         format 	  PCT012J026	best12. ;	
         format 	  PCT012J027	best12. ;	
         format 	  PCT012J028	best12. ;	
         format 	  PCT012J029	best12. ;	
         format 	  PCT012J030	best12. ;	
         format 	  PCT012J031	best12. ;	
         format 	  PCT012J032	best12. ;	
         format 	  PCT012J033	best12. ;	
         format 	  PCT012J034	best12. ;	
         format 	  PCT012J035	best12. ;	
         format 	  PCT012J036	best12. ;	
         format 	  PCT012J037	best12. ;	
         format 	  PCT012J038	best12. ;	
         format 	  PCT012J039	best12. ;	
         format 	  PCT012J040	best12. ;	
         format 	  PCT012J041	best12. ;	
         format 	  PCT012J042	best12. ;	
         format 	  PCT012J043	best12. ;	
         format 	  PCT012J044	best12. ;	
         format 	  PCT012J045	best12. ;	
         format 	  PCT012J046	best12. ;	
         format 	  PCT012J047	best12. ;	
         format 	  PCT012J048	best12. ;	
         format 	  PCT012J049	best12. ;	
         format 	  PCT012J050	best12. ;	
         format 	  PCT012J051	best12. ;	
         format 	  PCT012J052	best12. ;	
         format 	  PCT012J053	best12. ;	
         format 	  PCT012J054	best12. ;	
         format 	  PCT012J055	best12. ;	
         format 	  PCT012J056	best12. ;	
         format 	  PCT012J057	best12. ;	
         format 	  PCT012J058	best12. ;	
         format 	  PCT012J059	best12. ;	
         format 	  PCT012J060	best12. ;	
         format 	  PCT012J061	best12. ;	
         format 	  PCT012J062	best12. ;	
         format 	  PCT012J063	best12. ;	
         format 	  PCT012J064	best12. ;	
         format 	  PCT012J065	best12. ;	
         format 	  PCT012J066	best12. ;	
         format 	  PCT012J067	best12. ;	
         format 	  PCT012J068	best12. ;	
         format 	  PCT012J069	best12. ;	
         format 	  PCT012J070	best12. ;	
         format 	  PCT012J071	best12. ;	
         format 	  PCT012J072	best12. ;	
         format 	  PCT012J073	best12. ;	
         format 	  PCT012J074	best12. ;	
         format 	  PCT012J075	best12. ;	
         format 	  PCT012J076	best12. ;	
         format 	  PCT012J077	best12. ;	
         format 	  PCT012J078	best12. ;	
         format 	  PCT012J079	best12. ;	
         format 	  PCT012J080	best12. ;	
         format 	  PCT012J081	best12. ;	
         format 	  PCT012J082	best12. ;	
         format 	  PCT012J083	best12. ;	
         format 	  PCT012J084	best12. ;	
         format 	  PCT012J085	best12. ;	
         format 	  PCT012J086	best12. ;	
         format 	  PCT012J087	best12. ;	
         format 	  PCT012J088	best12. ;	
         format 	  PCT012J089	best12. ;	
         format 	  PCT012J090	best12. ;	
         format 	  PCT012J091	best12. ;	
         format 	  PCT012J092	best12. ;	
         format 	  PCT012J093	best12. ;	
         format 	  PCT012J094	best12. ;	
         format 	  PCT012J095	best12. ;	
         format 	  PCT012J096	best12. ;	
         format 	  PCT012J097	best12. ;	
         format 	  PCT012J098	best12. ;	
         format 	  PCT012J099	best12. ;	
         format 	  PCT012J100	best12. ;	
         format 	  PCT012J101	best12. ;	
         format 	  PCT012J102	best12. ;	
         format 	  PCT012J103	best12. ;	
         format 	  PCT012J104	best12. ;	
         format 	  PCT012J105	best12. ;	
         format 	  PCT012J106	best12. ;	
         format 	  PCT012J107	best12. ;	
         format 	  PCT012J108	best12. ;	
         format 	  PCT012J109	best12. ;	
         format 	  PCT012J110	best12. ;	
         format 	  PCT012J111	best12. ;	
         format 	  PCT012J112	best12. ;	
         format 	  PCT012J113	best12. ;	
         format 	  PCT012J114	best12. ;	
         format 	  PCT012J115	best12. ;	
         format 	  PCT012J116	best12. ;	
         format 	  PCT012J117	best12. ;	
         format 	  PCT012J118	best12. ;	
         format 	  PCT012J119	best12. ;	
         format 	  PCT012J120	best12. ;	
         format 	  PCT012J121	best12. ;	
         format 	  PCT012J122	best12. ;	
         format 	  PCT012J123	best12. ;	
         format 	  PCT012J124	best12. ;	
         format 	  PCT012J125	best12. ;	
         format 	  PCT012J126	best12. ;	
         format 	  PCT012J127	best12. ;	
         format 	  PCT012J128	best12. ;	
         format 	  PCT012J129	best12. ;	
         format 	  PCT012J130	best12. ;	
         format 	  PCT012J131	best12. ;	
         format 	  PCT012J132	best12. ;	
         format 	  PCT012J133	best12. ;	
         format 	  PCT012J134	best12. ;	
         format 	  PCT012J135	best12. ;	
         format 	  PCT012J136	best12. ;	
         format 	  PCT012J137	best12. ;	
         format 	  PCT012J138	best12. ;	
         format 	  PCT012J139	best12. ;	
         format 	  PCT012J140	best12. ;	
         format 	  PCT012J141	best12. ;	
         format 	  PCT012J142	best12. ;	
         format 	  PCT012J143	best12. ;	
         format 	  PCT012J144	best12. ;	
         format 	  PCT012J145	best12. ;	
         format 	  PCT012J146	best12. ;	
         format 	  PCT012J147	best12. ;	
         format 	  PCT012J148	best12. ;	
         format 	  PCT012J149	best12. ;	
         format 	  PCT012J150	best12. ;	
         format 	  PCT012J151	best12. ;	
         format 	  PCT012J152	best12. ;	
         format 	  PCT012J153	best12. ;	
         format 	  PCT012J154	best12. ;	
         format 	  PCT012J155	best12. ;	
         format 	  PCT012J156	best12. ;	
         format 	  PCT012J157	best12. ;	
         format 	  PCT012J158	best12. ;	
         format 	  PCT012J159	best12. ;	
         format 	  PCT012J160	best12. ;	
         format 	  PCT012J161	best12. ;	
         format 	  PCT012J162	best12. ;	
         format 	  PCT012J163	best12. ;	
         format 	  PCT012J164	best12. ;	
         format 	  PCT012J165	best12. ;	
         format 	  PCT012J166	best12. ;	
         format 	  PCT012J167	best12. ;	
         format 	  PCT012J168	best12. ;	
         format 	  PCT012J169	best12. ;	
         format 	  PCT012J170	best12. ;	
         format 	  PCT012J171	best12. ;	
         format 	  PCT012J172	best12. ;	
         format 	  PCT012J173	best12. ;	
         format 	  PCT012J174	best12. ;	
         format 	  PCT012J175	best12. ;	
         format 	  PCT012J176	best12. ;	
         format 	  PCT012J177	best12. ;	
         format 	  PCT012J178	best12. ;	
         format 	  PCT012J179	best12. ;	
         format 	  PCT012J180	best12. ;	
         format 	  PCT012J181	best12. ;	
         format 	  PCT012J182	best12. ;	
         format 	  PCT012J183	best12. ;	
         format 	  PCT012J184	best12. ;	
         format 	  PCT012J185	best12. ;	
         format 	  PCT012J186	best12. ;	
         format 	  PCT012J187	best12. ;	
         format 	  PCT012J188	best12. ;	
         format 	  PCT012J189	best12. ;	
         format 	  PCT012J190	best12. ;	
         format 	  PCT012J191	best12. ;	
         format 	  PCT012J192	best12. ;	
         format 	  PCT012J193	best12. ;	
         format 	  PCT012J194	best12. ;	
         format 	  PCT012J195	best12. ;	
         format 	  PCT012J196	best12. ;	
         format 	  PCT012J197	best12. ;	
         format 	  PCT012J198	best12. ;	
         format 	  PCT012J199	best12. ;	
         format 	  PCT012J200	best12. ;	
         format 	  PCT012J201	best12. ;	
         format 	  PCT012J202	best12. ;	
         format 	  PCT012J203	best12. ;	
         format 	  PCT012J204	best12. ;	
         format 	  PCT012J205	best12. ;	
         format 	  PCT012J206	best12. ;	
         format 	  PCT012J207	best12. ;	
         format 	  PCT012J208	best12. ;	
         format 	  PCT012J209	best12. ;	
         format 	  PCT012K001	best12. ;	
         format 	  PCT012K002	best12. ;	
         format 	  PCT012K003	best12. ;	
         format 	  PCT012K004	best12. ;	
         format 	  PCT012K005	best12. ;	
         format 	  PCT012K006	best12. ;	
         format 	  PCT012K007	best12. ;	
         format 	  PCT012K008	best12. ;	
         format 	  PCT012K009	best12. ;	
         format 	  PCT012K010	best12. ;	
         format 	  PCT012K011	best12. ;	
         format 	  PCT012K012	best12. ;	
         format 	  PCT012K013	best12. ;	
         format 	  PCT012K014	best12. ;	
         format 	  PCT012K015	best12. ;	
         format 	  PCT012K016	best12. ;	
         format 	  PCT012K017	best12. ;	
         format 	  PCT012K018	best12. ;	
         format 	  PCT012K019	best12. ;	
         format 	  PCT012K020	best12. ;	
         format 	  PCT012K021	best12. ;	
         format 	  PCT012K022	best12. ;	
         format 	  PCT012K023	best12. ;	
         format 	  PCT012K024	best12. ;	
         format 	  PCT012K025	best12. ;	
         format 	  PCT012K026	best12. ;	
         format 	  PCT012K027	best12. ;	
         format 	  PCT012K028	best12. ;	
         format 	  PCT012K029	best12. ;	
         format 	  PCT012K030	best12. ;	
         format 	  PCT012K031	best12. ;	
         format 	  PCT012K032	best12. ;	
         format 	  PCT012K033	best12. ;	
         format 	  PCT012K034	best12. ;	
         format 	  PCT012K035	best12. ;	
         format 	  PCT012K036	best12. ;	
         format 	  PCT012K037	best12. ;	
         format 	  PCT012K038	best12. ;	
         format 	  PCT012K039	best12. ;	
         format 	  PCT012K040	best12. ;	
         format 	  PCT012K041	best12. ;	
         format 	  PCT012K042	best12. ;	
         format 	  PCT012K043	best12. ;	
         format 	  PCT012K044	best12. ;	
         format 	  PCT012K045	best12. ;	
         format 	  PCT012K046	best12. ;	
         format 	  PCT012K047	best12. ;	
         format 	  PCT012K048	best12. ;	
         format 	  PCT012K049	best12. ;	
         format 	  PCT012K050	best12. ;	
         format 	  PCT012K051	best12. ;	
         format 	  PCT012K052	best12. ;	
         format 	  PCT012K053	best12. ;	
         format 	  PCT012K054	best12. ;	
         format 	  PCT012K055	best12. ;	
         format 	  PCT012K056	best12. ;	
         format 	  PCT012K057	best12. ;	
         format 	  PCT012K058	best12. ;	
         format 	  PCT012K059	best12. ;	
         format 	  PCT012K060	best12. ;	
         format 	  PCT012K061	best12. ;	
         format 	  PCT012K062	best12. ;	
         format 	  PCT012K063	best12. ;	
         format 	  PCT012K064	best12. ;	
         format 	  PCT012K065	best12. ;	
         format 	  PCT012K066	best12. ;	
         format 	  PCT012K067	best12. ;	
         format 	  PCT012K068	best12. ;	
         format 	  PCT012K069	best12. ;	
         format 	  PCT012K070	best12. ;	
         format 	  PCT012K071	best12. ;	
         format 	  PCT012K072	best12. ;	
         format 	  PCT012K073	best12. ;	
         format 	  PCT012K074	best12. ;	
         format 	  PCT012K075	best12. ;	
         format 	  PCT012K076	best12. ;	
         format 	  PCT012K077	best12. ;	
         format 	  PCT012K078	best12. ;	
         format 	  PCT012K079	best12. ;	
         format 	  PCT012K080	best12. ;	
         format 	  PCT012K081	best12. ;	
         format 	  PCT012K082	best12. ;	
         format 	  PCT012K083	best12. ;	
         format 	  PCT012K084	best12. ;	
         format 	  PCT012K085	best12. ;	
         format 	  PCT012K086	best12. ;	
         format 	  PCT012K087	best12. ;	
         format 	  PCT012K088	best12. ;	
         format 	  PCT012K089	best12. ;	
         format 	  PCT012K090	best12. ;	
         format 	  PCT012K091	best12. ;	
         format 	  PCT012K092	best12. ;	
         format 	  PCT012K093	best12. ;	
         format 	  PCT012K094	best12. ;	
         format 	  PCT012K095	best12. ;	
         format 	  PCT012K096	best12. ;	
         format 	  PCT012K097	best12. ;	
         format 	  PCT012K098	best12. ;	
         format 	  PCT012K099	best12. ;	
         format 	  PCT012K100	best12. ;	
         format 	  PCT012K101	best12. ;	
         format 	  PCT012K102	best12. ;	
         format 	  PCT012K103	best12. ;	
         format 	  PCT012K104	best12. ;	
         format 	  PCT012K105	best12. ;	
         format 	  PCT012K106	best12. ;	
         format 	  PCT012K107	best12. ;	
         format 	  PCT012K108	best12. ;	
         format 	  PCT012K109	best12. ;	
         format 	  PCT012K110	best12. ;	
         format 	  PCT012K111	best12. ;	
         format 	  PCT012K112	best12. ;	
         format 	  PCT012K113	best12. ;	
         format 	  PCT012K114	best12. ;	
         format 	  PCT012K115	best12. ;	
         format 	  PCT012K116	best12. ;	
         format 	  PCT012K117	best12. ;	
         format 	  PCT012K118	best12. ;	
         format 	  PCT012K119	best12. ;	
         format 	  PCT012K120	best12. ;	
         format 	  PCT012K121	best12. ;	
         format 	  PCT012K122	best12. ;	
         format 	  PCT012K123	best12. ;	
         format 	  PCT012K124	best12. ;	
         format 	  PCT012K125	best12. ;	
         format 	  PCT012K126	best12. ;	
         format 	  PCT012K127	best12. ;	
         format 	  PCT012K128	best12. ;	
         format 	  PCT012K129	best12. ;	
         format 	  PCT012K130	best12. ;	
         format 	  PCT012K131	best12. ;	
         format 	  PCT012K132	best12. ;	
         format 	  PCT012K133	best12. ;	
         format 	  PCT012K134	best12. ;	
         format 	  PCT012K135	best12. ;	
         format 	  PCT012K136	best12. ;	
         format 	  PCT012K137	best12. ;	
         format 	  PCT012K138	best12. ;	
         format 	  PCT012K139	best12. ;	
         format 	  PCT012K140	best12. ;	
         format 	  PCT012K141	best12. ;	
         format 	  PCT012K142	best12. ;	
         format 	  PCT012K143	best12. ;	
         format 	  PCT012K144	best12. ;	
         format 	  PCT012K145	best12. ;	
         format 	  PCT012K146	best12. ;	
         format 	  PCT012K147	best12. ;	
         format 	  PCT012K148	best12. ;	
         format 	  PCT012K149	best12. ;	
         format 	  PCT012K150	best12. ;	
         format 	  PCT012K151	best12. ;	
         format 	  PCT012K152	best12. ;	
         format 	  PCT012K153	best12. ;	
         format 	  PCT012K154	best12. ;	
         format 	  PCT012K155	best12. ;	
         format 	  PCT012K156	best12. ;	
         format 	  PCT012K157	best12. ;	
         format 	  PCT012K158	best12. ;	
         format 	  PCT012K159	best12. ;	
         format 	  PCT012K160	best12. ;	
         format 	  PCT012K161	best12. ;	
         format 	  PCT012K162	best12. ;	
         format 	  PCT012K163	best12. ;	
         format 	  PCT012K164	best12. ;	
         format 	  PCT012K165	best12. ;	
         format 	  PCT012K166	best12. ;	
         format 	  PCT012K167	best12. ;	
         format 	  PCT012K168	best12. ;	
         format 	  PCT012K169	best12. ;	
         format 	  PCT012K170	best12. ;	
         format 	  PCT012K171	best12. ;	
         format 	  PCT012K172	best12. ;	
         format 	  PCT012K173	best12. ;	
         format 	  PCT012K174	best12. ;	
         format 	  PCT012K175	best12. ;	
         format 	  PCT012K176	best12. ;	
         format 	  PCT012K177	best12. ;	
         format 	  PCT012K178	best12. ;	
         format 	  PCT012K179	best12. ;	
         format 	  PCT012K180	best12. ;	
         format 	  PCT012K181	best12. ;	
         format 	  PCT012K182	best12. ;	
         format 	  PCT012K183	best12. ;	
         format 	  PCT012K184	best12. ;	
         format 	  PCT012K185	best12. ;	
         format 	  PCT012K186	best12. ;	
         format 	  PCT012K187	best12. ;	
         format 	  PCT012K188	best12. ;	
         format 	  PCT012K189	best12. ;	
         format 	  PCT012K190	best12. ;	
         format 	  PCT012K191	best12. ;	
         format 	  PCT012K192	best12. ;	
         format 	  PCT012K193	best12. ;	
         format 	  PCT012K194	best12. ;	
         format 	  PCT012K195	best12. ;	
         format 	  PCT012K196	best12. ;	
         format 	  PCT012K197	best12. ;	
         format 	  PCT012K198	best12. ;	
         format 	  PCT012K199	best12. ;	
         format 	  PCT012K200	best12. ;	
         format 	  PCT012K201	best12. ;	
         format 	  PCT012K202	best12. ;	
         format 	  PCT012K203	best12. ;	
         format 	  PCT012K204	best12. ;	
         format 	  PCT012K205	best12. ;	
         format 	  PCT012K206	best12. ;	
         format 	  PCT012K207	best12. ;	
         format 	  PCT012K208	best12. ;	
         format 	  PCT012K209	best12. ;	
         format 	  PCT012L001	best12. ;	
         format 	  PCT012L002	best12. ;	
         format 	  PCT012L003	best12. ;	
         format 	  PCT012L004	best12. ;	
         format 	  PCT012L005	best12. ;	
         format 	  PCT012L006	best12. ;	
         format 	  PCT012L007	best12. ;	
         format 	  PCT012L008	best12. ;	
         format 	  PCT012L009	best12. ;	
         format 	  PCT012L010	best12. ;	
         format 	  PCT012L011	best12. ;	
         format 	  PCT012L012	best12. ;	
         format 	  PCT012L013	best12. ;	
         format 	  PCT012L014	best12. ;	
         format 	  PCT012L015	best12. ;	
         format 	  PCT012L016	best12. ;	
         format 	  PCT012L017	best12. ;	
         format 	  PCT012L018	best12. ;	
         format 	  PCT012L019	best12. ;	
         format 	  PCT012L020	best12. ;	
         format 	  PCT012L021	best12. ;	
         format 	  PCT012L022	best12. ;	
         format 	  PCT012L023	best12. ;	
         format 	  PCT012L024	best12. ;	
         format 	  PCT012L025	best12. ;	
         format 	  PCT012L026	best12. ;	
         format 	  PCT012L027	best12. ;	
         format 	  PCT012L028	best12. ;	
         format 	  PCT012L029	best12. ;	
         format 	  PCT012L030	best12. ;	
         format 	  PCT012L031	best12. ;	
         format 	  PCT012L032	best12. ;	
         format 	  PCT012L033	best12. ;	
         format 	  PCT012L034	best12. ;	
         format 	  PCT012L035	best12. ;	
         format 	  PCT012L036	best12. ;	
         format 	  PCT012L037	best12. ;	
         format 	  PCT012L038	best12. ;	
         format 	  PCT012L039	best12. ;	
         format 	  PCT012L040	best12. ;	
         format 	  PCT012L041	best12. ;	
         format 	  PCT012L042	best12. ;	
         format 	  PCT012L043	best12. ;	
         format 	  PCT012L044	best12. ;	
         format 	  PCT012L045	best12. ;	
         format 	  PCT012L046	best12. ;	
         format 	  PCT012L047	best12. ;	
         format 	  PCT012L048	best12. ;	
         format 	  PCT012L049	best12. ;	
         format 	  PCT012L050	best12. ;	
         format 	  PCT012L051	best12. ;	
         format 	  PCT012L052	best12. ;	
         format 	  PCT012L053	best12. ;	
         format 	  PCT012L054	best12. ;	
         format 	  PCT012L055	best12. ;	
         format 	  PCT012L056	best12. ;	
         format 	  PCT012L057	best12. ;	
         format 	  PCT012L058	best12. ;	
         format 	  PCT012L059	best12. ;	
         format 	  PCT012L060	best12. ;	
         format 	  PCT012L061	best12. ;	
         format 	  PCT012L062	best12. ;	
         format 	  PCT012L063	best12. ;	
         format 	  PCT012L064	best12. ;	
         format 	  PCT012L065	best12. ;	
         format 	  PCT012L066	best12. ;	
         format 	  PCT012L067	best12. ;	
         format 	  PCT012L068	best12. ;	
         format 	  PCT012L069	best12. ;	
         format 	  PCT012L070	best12. ;	
         format 	  PCT012L071	best12. ;	
         format 	  PCT012L072	best12. ;	
         format 	  PCT012L073	best12. ;	
         format 	  PCT012L074	best12. ;	
         format 	  PCT012L075	best12. ;	
         format 	  PCT012L076	best12. ;	
         format 	  PCT012L077	best12. ;	
         format 	  PCT012L078	best12. ;	
         format 	  PCT012L079	best12. ;	
         format 	  PCT012L080	best12. ;	
         format 	  PCT012L081	best12. ;	
         format 	  PCT012L082	best12. ;	
         format 	  PCT012L083	best12. ;	
         format 	  PCT012L084	best12. ;	
         format 	  PCT012L085	best12. ;	
         format 	  PCT012L086	best12. ;	
         format 	  PCT012L087	best12. ;	
         format 	  PCT012L088	best12. ;	
         format 	  PCT012L089	best12. ;	
         format 	  PCT012L090	best12. ;	
         format 	  PCT012L091	best12. ;	
         format 	  PCT012L092	best12. ;	
         format 	  PCT012L093	best12. ;	
         format 	  PCT012L094	best12. ;	
         format 	  PCT012L095	best12. ;	
         format 	  PCT012L096	best12. ;	
         format 	  PCT012L097	best12. ;	
         format 	  PCT012L098	best12. ;	
         format 	  PCT012L099	best12. ;	
         format 	  PCT012L100	best12. ;	
         format 	  PCT012L101	best12. ;	
         format 	  PCT012L102	best12. ;	
         format 	  PCT012L103	best12. ;	
         format 	  PCT012L104	best12. ;	
         format 	  PCT012L105	best12. ;	
         format 	  PCT012L106	best12. ;	
         format 	  PCT012L107	best12. ;	
         format 	  PCT012L108	best12. ;	
         format 	  PCT012L109	best12. ;	
         format 	  PCT012L110	best12. ;	
         format 	  PCT012L111	best12. ;	
         format 	  PCT012L112	best12. ;	
         format 	  PCT012L113	best12. ;	
         format 	  PCT012L114	best12. ;	
         format 	  PCT012L115	best12. ;	
         format 	  PCT012L116	best12. ;	
         format 	  PCT012L117	best12. ;	
         format 	  PCT012L118	best12. ;	
         format 	  PCT012L119	best12. ;	
         format 	  PCT012L120	best12. ;	
         format 	  PCT012L121	best12. ;	
         format 	  PCT012L122	best12. ;	
         format 	  PCT012L123	best12. ;	
         format 	  PCT012L124	best12. ;	
         format 	  PCT012L125	best12. ;	
         format 	  PCT012L126	best12. ;	
         format 	  PCT012L127	best12. ;	
         format 	  PCT012L128	best12. ;	
         format 	  PCT012L129	best12. ;	
         format 	  PCT012L130	best12. ;	
         format 	  PCT012L131	best12. ;	
         format 	  PCT012L132	best12. ;	
         format 	  PCT012L133	best12. ;	
         format 	  PCT012L134	best12. ;	
         format 	  PCT012L135	best12. ;	
         format 	  PCT012L136	best12. ;	
         format 	  PCT012L137	best12. ;	
         format 	  PCT012L138	best12. ;	
         format 	  PCT012L139	best12. ;	
         format 	  PCT012L140	best12. ;	
         format 	  PCT012L141	best12. ;	
         format 	  PCT012L142	best12. ;	
         format 	  PCT012L143	best12. ;	
         format 	  PCT012L144	best12. ;	
         format 	  PCT012L145	best12. ;	
         format 	  PCT012L146	best12. ;	
         format 	  PCT012L147	best12. ;	
         format 	  PCT012L148	best12. ;	
         format 	  PCT012L149	best12. ;	
         format 	  PCT012L150	best12. ;	
         format 	  PCT012L151	best12. ;	
         format 	  PCT012L152	best12. ;	
         format 	  PCT012L153	best12. ;	
         format 	  PCT012L154	best12. ;	
         format 	  PCT012L155	best12. ;	
         format 	  PCT012L156	best12. ;	
         format 	  PCT012L157	best12. ;	
         format 	  PCT012L158	best12. ;	
         format 	  PCT012L159	best12. ;	
         format 	  PCT012L160	best12. ;	
         format 	  PCT012L161	best12. ;	
         format 	  PCT012L162	best12. ;	
         format 	  PCT012L163	best12. ;	
         format 	  PCT012L164	best12. ;	
         format 	  PCT012L165	best12. ;	
         format 	  PCT012L166	best12. ;	
         format 	  PCT012L167	best12. ;	
         format 	  PCT012L168	best12. ;	
         format 	  PCT012L169	best12. ;	
         format 	  PCT012L170	best12. ;	
         format 	  PCT012L171	best12. ;	
         format 	  PCT012L172	best12. ;	
         format 	  PCT012L173	best12. ;	
         format 	  PCT012L174	best12. ;	
         format 	  PCT012L175	best12. ;	
         format 	  PCT012L176	best12. ;	
         format 	  PCT012L177	best12. ;	
         format 	  PCT012L178	best12. ;	
         format 	  PCT012L179	best12. ;	
         format 	  PCT012L180	best12. ;	
         format 	  PCT012L181	best12. ;	
         format 	  PCT012L182	best12. ;	
         format 	  PCT012L183	best12. ;	
         format 	  PCT012L184	best12. ;	
         format 	  PCT012L185	best12. ;	
         format 	  PCT012L186	best12. ;	
         format 	  PCT012L187	best12. ;	
         format 	  PCT012L188	best12. ;	
         format 	  PCT012L189	best12. ;	
         format 	  PCT012L190	best12. ;	
         format 	  PCT012L191	best12. ;	
         format 	  PCT012L192	best12. ;	
         format 	  PCT012L193	best12. ;	
         format 	  PCT012L194	best12. ;	
         format 	  PCT012L195	best12. ;	
         format 	  PCT012L196	best12. ;	
         format 	  PCT012L197	best12. ;	
         format 	  PCT012L198	best12. ;	
         format 	  PCT012L199	best12. ;	
         format 	  PCT012L200	best12. ;	
         format 	  PCT012L201	best12. ;	
         format 	  PCT012L202	best12. ;	
         format 	  PCT012L203	best12. ;	
         format 	  PCT012L204	best12. ;	
         format 	  PCT012L205	best12. ;	
         format 	  PCT012L206	best12. ;	
         format 	  PCT012L207	best12. ;	
         format 	  PCT012L208	best12. ;	
         format 	  PCT012L209	best12. ;	
         format 	  PCT012M001	best12. ;	
         format 	  PCT012M002	best12. ;	
         format 	  PCT012M003	best12. ;	
         format 	  PCT012M004	best12. ;	
         format 	  PCT012M005	best12. ;	
         format 	  PCT012M006	best12. ;	
         format 	  PCT012M007	best12. ;	
         format 	  PCT012M008	best12. ;	
         format 	  PCT012M009	best12. ;	
         format 	  PCT012M010	best12. ;	
         format 	  PCT012M011	best12. ;	
         format 	  PCT012M012	best12. ;	
         format 	  PCT012M013	best12. ;	
         format 	  PCT012M014	best12. ;	
         format 	  PCT012M015	best12. ;	
         format 	  PCT012M016	best12. ;	
         format 	  PCT012M017	best12. ;	
         format 	  PCT012M018	best12. ;	
         format 	  PCT012M019	best12. ;	
         format 	  PCT012M020	best12. ;	
         format 	  PCT012M021	best12. ;	
         format 	  PCT012M022	best12. ;	
         format 	  PCT012M023	best12. ;	
         format 	  PCT012M024	best12. ;	
         format 	  PCT012M025	best12. ;	
         format 	  PCT012M026	best12. ;	
         format 	  PCT012M027	best12. ;	
         format 	  PCT012M028	best12. ;	
         format 	  PCT012M029	best12. ;	
         format 	  PCT012M030	best12. ;	
         format 	  PCT012M031	best12. ;	
         format 	  PCT012M032	best12. ;	
         format 	  PCT012M033	best12. ;	
         format 	  PCT012M034	best12. ;	
         format 	  PCT012M035	best12. ;	
         format 	  PCT012M036	best12. ;	
         format 	  PCT012M037	best12. ;	
         format 	  PCT012M038	best12. ;	
         format 	  PCT012M039	best12. ;	
         format 	  PCT012M040	best12. ;	
         format 	  PCT012M041	best12. ;	
         format 	  PCT012M042	best12. ;	
         format 	  PCT012M043	best12. ;	
         format 	  PCT012M044	best12. ;	
         format 	  PCT012M045	best12. ;	
         format 	  PCT012M046	best12. ;	
         format 	  PCT012M047	best12. ;	
         format 	  PCT012M048	best12. ;	
         format 	  PCT012M049	best12. ;	
         format 	  PCT012M050	best12. ;	
         format 	  PCT012M051	best12. ;	
         format 	  PCT012M052	best12. ;	
         format 	  PCT012M053	best12. ;	
         format 	  PCT012M054	best12. ;	
         format 	  PCT012M055	best12. ;	
         format 	  PCT012M056	best12. ;	
         format 	  PCT012M057	best12. ;	
         format 	  PCT012M058	best12. ;	
         format 	  PCT012M059	best12. ;	
         format 	  PCT012M060	best12. ;	
         format 	  PCT012M061	best12. ;	
         format 	  PCT012M062	best12. ;	
         format 	  PCT012M063	best12. ;	
         format 	  PCT012M064	best12. ;	
         format 	  PCT012M065	best12. ;	
         format 	  PCT012M066	best12. ;	
         format 	  PCT012M067	best12. ;	
         format 	  PCT012M068	best12. ;	
         format 	  PCT012M069	best12. ;	
         format 	  PCT012M070	best12. ;	
         format 	  PCT012M071	best12. ;	
         format 	  PCT012M072	best12. ;	
         format 	  PCT012M073	best12. ;	
         format 	  PCT012M074	best12. ;	
         format 	  PCT012M075	best12. ;	
         format 	  PCT012M076	best12. ;	
         format 	  PCT012M077	best12. ;	
         format 	  PCT012M078	best12. ;	
         format 	  PCT012M079	best12. ;	
         format 	  PCT012M080	best12. ;	
         format 	  PCT012M081	best12. ;	
         format 	  PCT012M082	best12. ;	
         format 	  PCT012M083	best12. ;	
         format 	  PCT012M084	best12. ;	
         format 	  PCT012M085	best12. ;	
         format 	  PCT012M086	best12. ;	
         format 	  PCT012M087	best12. ;	
         format 	  PCT012M088	best12. ;	
         format 	  PCT012M089	best12. ;	
         format 	  PCT012M090	best12. ;	
         format 	  PCT012M091	best12. ;	
         format 	  PCT012M092	best12. ;	
         format 	  PCT012M093	best12. ;	
         format 	  PCT012M094	best12. ;	
         format 	  PCT012M095	best12. ;	
         format 	  PCT012M096	best12. ;	
         format 	  PCT012M097	best12. ;	
         format 	  PCT012M098	best12. ;	
         format 	  PCT012M099	best12. ;	
         format 	  PCT012M100	best12. ;	
         format 	  PCT012M101	best12. ;	
         format 	  PCT012M102	best12. ;	
         format 	  PCT012M103	best12. ;	
         format 	  PCT012M104	best12. ;	
         format 	  PCT012M105	best12. ;	
         format 	  PCT012M106	best12. ;	
         format 	  PCT012M107	best12. ;	
         format 	  PCT012M108	best12. ;	
         format 	  PCT012M109	best12. ;	
         format 	  PCT012M110	best12. ;	
         format 	  PCT012M111	best12. ;	
         format 	  PCT012M112	best12. ;	
         format 	  PCT012M113	best12. ;	
         format 	  PCT012M114	best12. ;	
         format 	  PCT012M115	best12. ;	
         format 	  PCT012M116	best12. ;	
         format 	  PCT012M117	best12. ;	
         format 	  PCT012M118	best12. ;	
         format 	  PCT012M119	best12. ;	
         format 	  PCT012M120	best12. ;	
         format 	  PCT012M121	best12. ;	
         format 	  PCT012M122	best12. ;	
         format 	  PCT012M123	best12. ;	
         format 	  PCT012M124	best12. ;	
         format 	  PCT012M125	best12. ;	
         format 	  PCT012M126	best12. ;	
         format 	  PCT012M127	best12. ;	
         format 	  PCT012M128	best12. ;	
         format 	  PCT012M129	best12. ;	
         format 	  PCT012M130	best12. ;	
         format 	  PCT012M131	best12. ;	
         format 	  PCT012M132	best12. ;	
         format 	  PCT012M133	best12. ;	
         format 	  PCT012M134	best12. ;	
         format 	  PCT012M135	best12. ;	
         format 	  PCT012M136	best12. ;	
         format 	  PCT012M137	best12. ;	
         format 	  PCT012M138	best12. ;	
         format 	  PCT012M139	best12. ;	
         format 	  PCT012M140	best12. ;	
         format 	  PCT012M141	best12. ;	
         format 	  PCT012M142	best12. ;	
         format 	  PCT012M143	best12. ;	
         format 	  PCT012M144	best12. ;	
         format 	  PCT012M145	best12. ;	
         format 	  PCT012M146	best12. ;	
         format 	  PCT012M147	best12. ;	
         format 	  PCT012M148	best12. ;	
         format 	  PCT012M149	best12. ;	
         format 	  PCT012M150	best12. ;	
         format 	  PCT012M151	best12. ;	
         format 	  PCT012M152	best12. ;	
         format 	  PCT012M153	best12. ;	
         format 	  PCT012M154	best12. ;	
         format 	  PCT012M155	best12. ;	
         format 	  PCT012M156	best12. ;	
         format 	  PCT012M157	best12. ;	
         format 	  PCT012M158	best12. ;	
         format 	  PCT012M159	best12. ;	
         format 	  PCT012M160	best12. ;	
         format 	  PCT012M161	best12. ;	
         format 	  PCT012M162	best12. ;	
         format 	  PCT012M163	best12. ;	
         format 	  PCT012M164	best12. ;	
         format 	  PCT012M165	best12. ;	
         format 	  PCT012M166	best12. ;	
         format 	  PCT012M167	best12. ;	
         format 	  PCT012M168	best12. ;	
         format 	  PCT012M169	best12. ;	
         format 	  PCT012M170	best12. ;	
         format 	  PCT012M171	best12. ;	
         format 	  PCT012M172	best12. ;	
         format 	  PCT012M173	best12. ;	
         format 	  PCT012M174	best12. ;	
         format 	  PCT012M175	best12. ;	
         format 	  PCT012M176	best12. ;	
         format 	  PCT012M177	best12. ;	
         format 	  PCT012M178	best12. ;	
         format 	  PCT012M179	best12. ;	
         format 	  PCT012M180	best12. ;	
         format 	  PCT012M181	best12. ;	
         format 	  PCT012M182	best12. ;	
         format 	  PCT012M183	best12. ;	
         format 	  PCT012M184	best12. ;	
         format 	  PCT012M185	best12. ;	
         format 	  PCT012M186	best12. ;	
         format 	  PCT012M187	best12. ;	
         format 	  PCT012M188	best12. ;	
         format 	  PCT012M189	best12. ;	
         format 	  PCT012M190	best12. ;	
         format 	  PCT012M191	best12. ;	
         format 	  PCT012M192	best12. ;	
         format 	  PCT012M193	best12. ;	
         format 	  PCT012M194	best12. ;	
         format 	  PCT012M195	best12. ;	
         format 	  PCT012M196	best12. ;	
         format 	  PCT012M197	best12. ;	
         format 	  PCT012M198	best12. ;	
         format 	  PCT012M199	best12. ;	
         format 	  PCT012M200	best12. ;	
         format 	  PCT012M201	best12. ;	
         format 	  PCT012M202	best12. ;	
         format 	  PCT012M203	best12. ;	
         format 	  PCT012M204	best12. ;	
         format 	  PCT012M205	best12. ;	
         format 	  PCT012M206	best12. ;	
         format 	  PCT012M207	best12. ;	
         format 	  PCT012M208	best12. ;	
         format 	  PCT012M209	best12. ;	
         format 	  PCT012N001	best12. ;	
         format 	  PCT012N002	best12. ;	
         format 	  PCT012N003	best12. ;	
         format 	  PCT012N004	best12. ;	
         format 	  PCT012N005	best12. ;	
         format 	  PCT012N006	best12. ;	
         format 	  PCT012N007	best12. ;	
         format 	  PCT012N008	best12. ;	
         format 	  PCT012N009	best12. ;	
         format 	  PCT012N010	best12. ;	
         format 	  PCT012N011	best12. ;	
         format 	  PCT012N012	best12. ;	
         format 	  PCT012N013	best12. ;	
         format 	  PCT012N014	best12. ;	
         format 	  PCT012N015	best12. ;	
         format 	  PCT012N016	best12. ;	
         format 	  PCT012N017	best12. ;	
         format 	  PCT012N018	best12. ;	
         format 	  PCT012N019	best12. ;	
         format 	  PCT012N020	best12. ;	
         format 	  PCT012N021	best12. ;	
         format 	  PCT012N022	best12. ;	
         format 	  PCT012N023	best12. ;	
         format 	  PCT012N024	best12. ;	
         format 	  PCT012N025	best12. ;	
         format 	  PCT012N026	best12. ;	
         format 	  PCT012N027	best12. ;	
         format 	  PCT012N028	best12. ;	
         format 	  PCT012N029	best12. ;	
         format 	  PCT012N030	best12. ;	
         format 	  PCT012N031	best12. ;	
         format 	  PCT012N032	best12. ;	
         format 	  PCT012N033	best12. ;	
         format 	  PCT012N034	best12. ;	
         format 	  PCT012N035	best12. ;	
         format 	  PCT012N036	best12. ;	
         format 	  PCT012N037	best12. ;	
         format 	  PCT012N038	best12. ;	
         format 	  PCT012N039	best12. ;	
         format 	  PCT012N040	best12. ;	
         format 	  PCT012N041	best12. ;	
         format 	  PCT012N042	best12. ;	
         format 	  PCT012N043	best12. ;	
         format 	  PCT012N044	best12. ;	
         format 	  PCT012N045	best12. ;	
         format 	  PCT012N046	best12. ;	
         format 	  PCT012N047	best12. ;	
         format 	  PCT012N048	best12. ;	
         format 	  PCT012N049	best12. ;	
         format 	  PCT012N050	best12. ;	
         format 	  PCT012N051	best12. ;	
         format 	  PCT012N052	best12. ;	
         format 	  PCT012N053	best12. ;	
         format 	  PCT012N054	best12. ;	
         format 	  PCT012N055	best12. ;	
         format 	  PCT012N056	best12. ;	
         format 	  PCT012N057	best12. ;	
         format 	  PCT012N058	best12. ;	
         format 	  PCT012N059	best12. ;	
         format 	  PCT012N060	best12. ;	
         format 	  PCT012N061	best12. ;	
         format 	  PCT012N062	best12. ;	
         format 	  PCT012N063	best12. ;	
         format 	  PCT012N064	best12. ;	
         format 	  PCT012N065	best12. ;	
         format 	  PCT012N066	best12. ;	
         format 	  PCT012N067	best12. ;	
         format 	  PCT012N068	best12. ;	
         format 	  PCT012N069	best12. ;	
         format 	  PCT012N070	best12. ;	
         format 	  PCT012N071	best12. ;	
         format 	  PCT012N072	best12. ;	
         format 	  PCT012N073	best12. ;	
         format 	  PCT012N074	best12. ;	
         format 	  PCT012N075	best12. ;	
         format 	  PCT012N076	best12. ;	
         format 	  PCT012N077	best12. ;	
         format 	  PCT012N078	best12. ;	
         format 	  PCT012N079	best12. ;	
         format 	  PCT012N080	best12. ;	
         format 	  PCT012N081	best12. ;	
         format 	  PCT012N082	best12. ;	
         format 	  PCT012N083	best12. ;	
         format 	  PCT012N084	best12. ;	
         format 	  PCT012N085	best12. ;	
         format 	  PCT012N086	best12. ;	
         format 	  PCT012N087	best12. ;	
         format 	  PCT012N088	best12. ;	
         format 	  PCT012N089	best12. ;	
         format 	  PCT012N090	best12. ;	
         format 	  PCT012N091	best12. ;	
         format 	  PCT012N092	best12. ;	
         format 	  PCT012N093	best12. ;	
         format 	  PCT012N094	best12. ;	
         format 	  PCT012N095	best12. ;	
         format 	  PCT012N096	best12. ;	
         format 	  PCT012N097	best12. ;	
         format 	  PCT012N098	best12. ;	
         format 	  PCT012N099	best12. ;	
         format 	  PCT012N100	best12. ;	
         format 	  PCT012N101	best12. ;	
         format 	  PCT012N102	best12. ;	
         format 	  PCT012N103	best12. ;	
         format 	  PCT012N104	best12. ;	
         format 	  PCT012N105	best12. ;	
         format 	  PCT012N106	best12. ;	
         format 	  PCT012N107	best12. ;	
         format 	  PCT012N108	best12. ;	
         format 	  PCT012N109	best12. ;	
         format 	  PCT012N110	best12. ;	
         format 	  PCT012N111	best12. ;	
         format 	  PCT012N112	best12. ;	
         format 	  PCT012N113	best12. ;	
         format 	  PCT012N114	best12. ;	
         format 	  PCT012N115	best12. ;	
         format 	  PCT012N116	best12. ;	
         format 	  PCT012N117	best12. ;	
         format 	  PCT012N118	best12. ;	
         format 	  PCT012N119	best12. ;	
         format 	  PCT012N120	best12. ;	
         format 	  PCT012N121	best12. ;	
         format 	  PCT012N122	best12. ;	
         format 	  PCT012N123	best12. ;	
         format 	  PCT012N124	best12. ;	
         format 	  PCT012N125	best12. ;	
         format 	  PCT012N126	best12. ;	
         format 	  PCT012N127	best12. ;	
         format 	  PCT012N128	best12. ;	
         format 	  PCT012N129	best12. ;	
         format 	  PCT012N130	best12. ;	
         format 	  PCT012N131	best12. ;	
         format 	  PCT012N132	best12. ;	
         format 	  PCT012N133	best12. ;	
         format 	  PCT012N134	best12. ;	
         format 	  PCT012N135	best12. ;	
         format 	  PCT012N136	best12. ;	
         format 	  PCT012N137	best12. ;	
         format 	  PCT012N138	best12. ;	
         format 	  PCT012N139	best12. ;	
         format 	  PCT012N140	best12. ;	
         format 	  PCT012N141	best12. ;	
         format 	  PCT012N142	best12. ;	
         format 	  PCT012N143	best12. ;	
         format 	  PCT012N144	best12. ;	
         format 	  PCT012N145	best12. ;	
         format 	  PCT012N146	best12. ;	
         format 	  PCT012N147	best12. ;	
         format 	  PCT012N148	best12. ;	
         format 	  PCT012N149	best12. ;	
         format 	  PCT012N150	best12. ;	
         format 	  PCT012N151	best12. ;	
         format 	  PCT012N152	best12. ;	
         format 	  PCT012N153	best12. ;	
         format 	  PCT012N154	best12. ;	
         format 	  PCT012N155	best12. ;	
         format 	  PCT012N156	best12. ;	
         format 	  PCT012N157	best12. ;	
         format 	  PCT012N158	best12. ;	
         format 	  PCT012N159	best12. ;	
         format 	  PCT012N160	best12. ;	
         format 	  PCT012N161	best12. ;	
         format 	  PCT012N162	best12. ;	
         format 	  PCT012N163	best12. ;	
         format 	  PCT012N164	best12. ;	
         format 	  PCT012N165	best12. ;	
         format 	  PCT012N166	best12. ;	
         format 	  PCT012N167	best12. ;	
         format 	  PCT012N168	best12. ;	
         format 	  PCT012N169	best12. ;	
         format 	  PCT012N170	best12. ;	
         format 	  PCT012N171	best12. ;	
         format 	  PCT012N172	best12. ;	
         format 	  PCT012N173	best12. ;	
         format 	  PCT012N174	best12. ;	
         format 	  PCT012N175	best12. ;	
         format 	  PCT012N176	best12. ;	
         format 	  PCT012N177	best12. ;	
         format 	  PCT012N178	best12. ;	
         format 	  PCT012N179	best12. ;	
         format 	  PCT012N180	best12. ;	
         format 	  PCT012N181	best12. ;	
         format 	  PCT012N182	best12. ;	
         format 	  PCT012N183	best12. ;	
         format 	  PCT012N184	best12. ;	
         format 	  PCT012N185	best12. ;	
         format 	  PCT012N186	best12. ;	
         format 	  PCT012N187	best12. ;	
         format 	  PCT012N188	best12. ;	
         format 	  PCT012N189	best12. ;	
         format 	  PCT012N190	best12. ;	
         format 	  PCT012N191	best12. ;	
         format 	  PCT012N192	best12. ;	
         format 	  PCT012N193	best12. ;	
         format 	  PCT012N194	best12. ;	
         format 	  PCT012N195	best12. ;	
         format 	  PCT012N196	best12. ;	
         format 	  PCT012N197	best12. ;	
         format 	  PCT012N198	best12. ;	
         format 	  PCT012N199	best12. ;	
         format 	  PCT012N200	best12. ;	
         format 	  PCT012N201	best12. ;	
         format 	  PCT012N202	best12. ;	
         format 	  PCT012N203	best12. ;	
         format 	  PCT012N204	best12. ;	
         format 	  PCT012N205	best12. ;	
         format 	  PCT012N206	best12. ;	
         format 	  PCT012N207	best12. ;	
         format 	  PCT012N208	best12. ;	
         format 	  PCT012N209	best12. ;	
         format 	  PCT012O001	best12. ;	
         format 	  PCT012O002	best12. ;	
         format 	  PCT012O003	best12. ;	
         format 	  PCT012O004	best12. ;	
         format 	  PCT012O005	best12. ;	
         format 	  PCT012O006	best12. ;	
         format 	  PCT012O007	best12. ;	
         format 	  PCT012O008	best12. ;	
         format 	  PCT012O009	best12. ;	
         format 	  PCT012O010	best12. ;	
         format 	  PCT012O011	best12. ;	
         format 	  PCT012O012	best12. ;	
         format 	  PCT012O013	best12. ;	
         format 	  PCT012O014	best12. ;	
         format 	  PCT012O015	best12. ;	
         format 	  PCT012O016	best12. ;	
         format 	  PCT012O017	best12. ;	
         format 	  PCT012O018	best12. ;	
         format 	  PCT012O019	best12. ;	
         format 	  PCT012O020	best12. ;	
         format 	  PCT012O021	best12. ;	
         format 	  PCT012O022	best12. ;	
         format 	  PCT012O023	best12. ;	
         format 	  PCT012O024	best12. ;	
         format 	  PCT012O025	best12. ;	
         format 	  PCT012O026	best12. ;	
         format 	  PCT012O027	best12. ;	
         format 	  PCT012O028	best12. ;	
         format 	  PCT012O029	best12. ;	
         format 	  PCT012O030	best12. ;	
         format 	  PCT012O031	best12. ;	
         format 	  PCT012O032	best12. ;	
         format 	  PCT012O033	best12. ;	
         format 	  PCT012O034	best12. ;	
         format 	  PCT012O035	best12. ;	
         format 	  PCT012O036	best12. ;	
         format 	  PCT012O037	best12. ;	
         format 	  PCT012O038	best12. ;	
         format 	  PCT012O039	best12. ;	
         format 	  PCT012O040	best12. ;	
         format 	  PCT012O041	best12. ;	
         format 	  PCT012O042	best12. ;	
         format 	  PCT012O043	best12. ;	
         format 	  PCT012O044	best12. ;	
         format 	  PCT012O045	best12. ;	
         format 	  PCT012O046	best12. ;	
         format 	  PCT012O047	best12. ;	
         format 	  PCT012O048	best12. ;	
         format 	  PCT012O049	best12. ;	
         format 	  PCT012O050	best12. ;	
         format 	  PCT012O051	best12. ;	
         format 	  PCT012O052	best12. ;	
         format 	  PCT012O053	best12. ;	
         format 	  PCT012O054	best12. ;	
         format 	  PCT012O055	best12. ;	
         format 	  PCT012O056	best12. ;	
         format 	  PCT012O057	best12. ;	
         format 	  PCT012O058	best12. ;	
         format 	  PCT012O059	best12. ;	
         format 	  PCT012O060	best12. ;	
         format 	  PCT012O061	best12. ;	
         format 	  PCT012O062	best12. ;	
         format 	  PCT012O063	best12. ;	
         format 	  PCT012O064	best12. ;	
         format 	  PCT012O065	best12. ;	
         format 	  PCT012O066	best12. ;	
         format 	  PCT012O067	best12. ;	
         format 	  PCT012O068	best12. ;	
         format 	  PCT012O069	best12. ;	
         format 	  PCT012O070	best12. ;	
         format 	  PCT012O071	best12. ;	
         format 	  PCT012O072	best12. ;	
         format 	  PCT012O073	best12. ;	
         format 	  PCT012O074	best12. ;	
         format 	  PCT012O075	best12. ;	
         format 	  PCT012O076	best12. ;	
         format 	  PCT012O077	best12. ;	
         format 	  PCT012O078	best12. ;	
         format 	  PCT012O079	best12. ;	
         format 	  PCT012O080	best12. ;	
         format 	  PCT012O081	best12. ;	
         format 	  PCT012O082	best12. ;	
         format 	  PCT012O083	best12. ;	
         format 	  PCT012O084	best12. ;	
         format 	  PCT012O085	best12. ;	
         format 	  PCT012O086	best12. ;	
         format 	  PCT012O087	best12. ;	
         format 	  PCT012O088	best12. ;	
         format 	  PCT012O089	best12. ;	
         format 	  PCT012O090	best12. ;	
         format 	  PCT012O091	best12. ;	
         format 	  PCT012O092	best12. ;	
         format 	  PCT012O093	best12. ;	
         format 	  PCT012O094	best12. ;	
         format 	  PCT012O095	best12. ;	
         format 	  PCT012O096	best12. ;	
         format 	  PCT012O097	best12. ;	
         format 	  PCT012O098	best12. ;	
         format 	  PCT012O099	best12. ;	
         format 	  PCT012O100	best12. ;	
         format 	  PCT012O101	best12. ;	
         format 	  PCT012O102	best12. ;	
         format 	  PCT012O103	best12. ;	
         format 	  PCT012O104	best12. ;	
         format 	  PCT012O105	best12. ;	
         format 	  PCT012O106	best12. ;	
         format 	  PCT012O107	best12. ;	
         format 	  PCT012O108	best12. ;	
         format 	  PCT012O109	best12. ;	
         format 	  PCT012O110	best12. ;	
         format 	  PCT012O111	best12. ;	
         format 	  PCT012O112	best12. ;	
         format 	  PCT012O113	best12. ;	
         format 	  PCT012O114	best12. ;	
         format 	  PCT012O115	best12. ;	
         format 	  PCT012O116	best12. ;	
         format 	  PCT012O117	best12. ;	
         format 	  PCT012O118	best12. ;	
         format 	  PCT012O119	best12. ;	
         format 	  PCT012O120	best12. ;	
         format 	  PCT012O121	best12. ;	
         format 	  PCT012O122	best12. ;	
         format 	  PCT012O123	best12. ;	
         format 	  PCT012O124	best12. ;	
         format 	  PCT012O125	best12. ;	
         format 	  PCT012O126	best12. ;	
         format 	  PCT012O127	best12. ;	
         format 	  PCT012O128	best12. ;	
         format 	  PCT012O129	best12. ;	
         format 	  PCT012O130	best12. ;	
         format 	  PCT012O131	best12. ;	
         format 	  PCT012O132	best12. ;	
         format 	  PCT012O133	best12. ;	
         format 	  PCT012O134	best12. ;	
         format 	  PCT012O135	best12. ;	
         format 	  PCT012O136	best12. ;	
         format 	  PCT012O137	best12. ;	
         format 	  PCT012O138	best12. ;	
         format 	  PCT012O139	best12. ;	
         format 	  PCT012O140	best12. ;	
         format 	  PCT012O141	best12. ;	
         format 	  PCT012O142	best12. ;	
         format 	  PCT012O143	best12. ;	
         format 	  PCT012O144	best12. ;	
         format 	  PCT012O145	best12. ;	
         format 	  PCT012O146	best12. ;	
         format 	  PCT012O147	best12. ;	
         format 	  PCT012O148	best12. ;	
         format 	  PCT012O149	best12. ;	
         format 	  PCT012O150	best12. ;	
         format 	  PCT012O151	best12. ;	
         format 	  PCT012O152	best12. ;	
         format 	  PCT012O153	best12. ;	
         format 	  PCT012O154	best12. ;	
         format 	  PCT012O155	best12. ;	
         format 	  PCT012O156	best12. ;	
         format 	  PCT012O157	best12. ;	
         format 	  PCT012O158	best12. ;	
         format 	  PCT012O159	best12. ;	
         format 	  PCT012O160	best12. ;	
         format 	  PCT012O161	best12. ;	
         format 	  PCT012O162	best12. ;	
         format 	  PCT012O163	best12. ;	
         format 	  PCT012O164	best12. ;	
         format 	  PCT012O165	best12. ;	
         format 	  PCT012O166	best12. ;	
         format 	  PCT012O167	best12. ;	
         format 	  PCT012O168	best12. ;	
         format 	  PCT012O169	best12. ;	
         format 	  PCT012O170	best12. ;	
         format 	  PCT012O171	best12. ;	
         format 	  PCT012O172	best12. ;	
         format 	  PCT012O173	best12. ;	
         format 	  PCT012O174	best12. ;	
         format 	  PCT012O175	best12. ;	
         format 	  PCT012O176	best12. ;	
         format 	  PCT012O177	best12. ;	
         format 	  PCT012O178	best12. ;	
         format 	  PCT012O179	best12. ;	
         format 	  PCT012O180	best12. ;	
         format 	  PCT012O181	best12. ;	
         format 	  PCT012O182	best12. ;	
         format 	  PCT012O183	best12. ;	
         format 	  PCT012O184	best12. ;	
         format 	  PCT012O185	best12. ;	
         format 	  PCT012O186	best12. ;	
         format 	  PCT012O187	best12. ;	
         format 	  PCT012O188	best12. ;	
         format 	  PCT012O189	best12. ;	
         format 	  PCT012O190	best12. ;	
         format 	  PCT012O191	best12. ;	
         format 	  PCT012O192	best12. ;	
         format 	  PCT012O193	best12. ;	
         format 	  PCT012O194	best12. ;	
         format 	  PCT012O195	best12. ;	
         format 	  PCT012O196	best12. ;	
         format 	  PCT012O197	best12. ;	
         format 	  PCT012O198	best12. ;	
         format 	  PCT012O199	best12. ;	
         format 	  PCT012O200	best12. ;	
         format 	  PCT012O201	best12. ;	
         format 	  PCT012O202	best12. ;	
         format 	  PCT012O203	best12. ;	
         format 	  PCT012O204	best12. ;	
         format 	  PCT012O205	best12. ;	
         format 	  PCT012O206	best12. ;	
         format 	  PCT012O207	best12. ;	
         format 	  PCT012O208	best12. ;	
         format 	  PCT012O209	best12. ;	
         format 	  PCT013A001	best12. ;	
         format 	  PCT013A002	best12. ;	
         format 	  PCT013A003	best12. ;	
         format 	  PCT013A004	best12. ;	
         format 	  PCT013A005	best12. ;	
         format 	  PCT013A006	best12. ;	
         format 	  PCT013A007	best12. ;	
         format 	  PCT013A008	best12. ;	
         format 	  PCT013A009	best12. ;	
         format 	  PCT013A010	best12. ;	
         format 	  PCT013A011	best12. ;	
         format 	  PCT013A012	best12. ;	
         format 	  PCT013A013	best12. ;	
         format 	  PCT013A014	best12. ;	
         format 	  PCT013A015	best12. ;	
         format 	  PCT013A016	best12. ;	
         format 	  PCT013A017	best12. ;	
         format 	  PCT013A018	best12. ;	
         format 	  PCT013A019	best12. ;	
         format 	  PCT013A020	best12. ;	
         format 	  PCT013A021	best12. ;	
         format 	  PCT013A022	best12. ;	
         format 	  PCT013A023	best12. ;	
         format 	  PCT013A024	best12. ;	
         format 	  PCT013A025	best12. ;	
         format 	  PCT013A026	best12. ;	
         format 	  PCT013A027	best12. ;	
         format 	  PCT013A028	best12. ;	
         format 	  PCT013A029	best12. ;	
         format 	  PCT013A030	best12. ;	
         format 	  PCT013A031	best12. ;	
         format 	  PCT013A032	best12. ;	
         format 	  PCT013A033	best12. ;	
         format 	  PCT013A034	best12. ;	
         format 	  PCT013A035	best12. ;	
         format 	  PCT013A036	best12. ;	
         format 	  PCT013A037	best12. ;	
         format 	  PCT013A038	best12. ;	
         format 	  PCT013A039	best12. ;	
         format 	  PCT013A040	best12. ;	
         format 	  PCT013A041	best12. ;	
         format 	  PCT013A042	best12. ;	
         format 	  PCT013A043	best12. ;	
         format 	  PCT013A044	best12. ;	
         format 	  PCT013A045	best12. ;	
         format 	  PCT013A046	best12. ;	
         format 	  PCT013A047	best12. ;	
         format 	  PCT013A048	best12. ;	
         format 	  PCT013A049	best12. ;	
         format 	  PCT013B001	best12. ;	
         format 	  PCT013B002	best12. ;	
         format 	  PCT013B003	best12. ;	
         format 	  PCT013B004	best12. ;	
         format 	  PCT013B005	best12. ;	
         format 	  PCT013B006	best12. ;	
         format 	  PCT013B007	best12. ;	
         format 	  PCT013B008	best12. ;	
         format 	  PCT013B009	best12. ;	
         format 	  PCT013B010	best12. ;	
         format 	  PCT013B011	best12. ;	
         format 	  PCT013B012	best12. ;	
         format 	  PCT013B013	best12. ;	
         format 	  PCT013B014	best12. ;	
         format 	  PCT013B015	best12. ;	
         format 	  PCT013B016	best12. ;	
         format 	  PCT013B017	best12. ;	
         format 	  PCT013B018	best12. ;	
         format 	  PCT013B019	best12. ;	
         format 	  PCT013B020	best12. ;	
         format 	  PCT013B021	best12. ;	
         format 	  PCT013B022	best12. ;	
         format 	  PCT013B023	best12. ;	
         format 	  PCT013B024	best12. ;	
         format 	  PCT013B025	best12. ;	
         format 	  PCT013B026	best12. ;	
         format 	  PCT013B027	best12. ;	
         format 	  PCT013B028	best12. ;	
         format 	  PCT013B029	best12. ;	
         format 	  PCT013B030	best12. ;	
         format 	  PCT013B031	best12. ;	
         format 	  PCT013B032	best12. ;	
         format 	  PCT013B033	best12. ;	
         format 	  PCT013B034	best12. ;	
         format 	  PCT013B035	best12. ;	
         format 	  PCT013B036	best12. ;	
         format 	  PCT013B037	best12. ;	
         format 	  PCT013B038	best12. ;	
         format 	  PCT013B039	best12. ;	
         format 	  PCT013B040	best12. ;	
         format 	  PCT013B041	best12. ;	
         format 	  PCT013B042	best12. ;	
         format 	  PCT013B043	best12. ;	
         format 	  PCT013B044	best12. ;	
         format 	  PCT013B045	best12. ;	
         format 	  PCT013B046	best12. ;	
         format 	  PCT013B047	best12. ;	
         format 	  PCT013B048	best12. ;	
         format 	  PCT013B049	best12. ;	
         format 	  PCT013C001	best12. ;	
         format 	  PCT013C002	best12. ;	
         format 	  PCT013C003	best12. ;	
         format 	  PCT013C004	best12. ;	
         format 	  PCT013C005	best12. ;	
         format 	  PCT013C006	best12. ;	
         format 	  PCT013C007	best12. ;	
         format 	  PCT013C008	best12. ;	
         format 	  PCT013C009	best12. ;	
         format 	  PCT013C010	best12. ;	
         format 	  PCT013C011	best12. ;	
         format 	  PCT013C012	best12. ;	
         format 	  PCT013C013	best12. ;	
         format 	  PCT013C014	best12. ;	
         format 	  PCT013C015	best12. ;	
         format 	  PCT013C016	best12. ;	
         format 	  PCT013C017	best12. ;	
         format 	  PCT013C018	best12. ;	
         format 	  PCT013C019	best12. ;	
         format 	  PCT013C020	best12. ;	
         format 	  PCT013C021	best12. ;	
         format 	  PCT013C022	best12. ;	
         format 	  PCT013C023	best12. ;	
         format 	  PCT013C024	best12. ;	
         format 	  PCT013C025	best12. ;	
         format 	  PCT013C026	best12. ;	
         format 	  PCT013C027	best12. ;	
         format 	  PCT013C028	best12. ;	
         format 	  PCT013C029	best12. ;	
         format 	  PCT013C030	best12. ;	
         format 	  PCT013C031	best12. ;	
         format 	  PCT013C032	best12. ;	
         format 	  PCT013C033	best12. ;	
         format 	  PCT013C034	best12. ;	
         format 	  PCT013C035	best12. ;	
         format 	  PCT013C036	best12. ;	
         format 	  PCT013C037	best12. ;	
         format 	  PCT013C038	best12. ;	
         format 	  PCT013C039	best12. ;	
         format 	  PCT013C040	best12. ;	
         format 	  PCT013C041	best12. ;	
         format 	  PCT013C042	best12. ;	
         format 	  PCT013C043	best12. ;	
         format 	  PCT013C044	best12. ;	
         format 	  PCT013C045	best12. ;	
         format 	  PCT013C046	best12. ;	
         format 	  PCT013C047	best12. ;	
         format 	  PCT013C048	best12. ;	
         format 	  PCT013C049	best12. ;	
         format 	  PCT013D001	best12. ;	
         format 	  PCT013D002	best12. ;	
         format 	  PCT013D003	best12. ;	
         format 	  PCT013D004	best12. ;	
         format 	  PCT013D005	best12. ;	
         format 	  PCT013D006	best12. ;	
         format 	  PCT013D007	best12. ;	
         format 	  PCT013D008	best12. ;	
         format 	  PCT013D009	best12. ;	
         format 	  PCT013D010	best12. ;	
         format 	  PCT013D011	best12. ;	
         format 	  PCT013D012	best12. ;	
         format 	  PCT013D013	best12. ;	
         format 	  PCT013D014	best12. ;	
         format 	  PCT013D015	best12. ;	
         format 	  PCT013D016	best12. ;	
         format 	  PCT013D017	best12. ;	
         format 	  PCT013D018	best12. ;	
         format 	  PCT013D019	best12. ;	
         format 	  PCT013D020	best12. ;	
         format 	  PCT013D021	best12. ;	
         format 	  PCT013D022	best12. ;	
         format 	  PCT013D023	best12. ;	
         format 	  PCT013D024	best12. ;	
         format 	  PCT013D025	best12. ;	
         format 	  PCT013D026	best12. ;	
         format 	  PCT013D027	best12. ;	
         format 	  PCT013D028	best12. ;	
         format 	  PCT013D029	best12. ;	
         format 	  PCT013D030	best12. ;	
         format 	  PCT013D031	best12. ;	
         format 	  PCT013D032	best12. ;	
         format 	  PCT013D033	best12. ;	
         format 	  PCT013D034	best12. ;	
         format 	  PCT013D035	best12. ;	
         format 	  PCT013D036	best12. ;	
         format 	  PCT013D037	best12. ;	
         format 	  PCT013D038	best12. ;	
         format 	  PCT013D039	best12. ;	
         format 	  PCT013D040	best12. ;	
         format 	  PCT013D041	best12. ;	
         format 	  PCT013D042	best12. ;	
         format 	  PCT013D043	best12. ;	
         format 	  PCT013D044	best12. ;	
         format 	  PCT013D045	best12. ;	
         format 	  PCT013D046	best12. ;	
         format 	  PCT013D047	best12. ;	
         format 	  PCT013D048	best12. ;	
         format 	  PCT013D049	best12. ;	
         format 	  PCT013E001	best12. ;	
         format 	  PCT013E002	best12. ;	
         format 	  PCT013E003	best12. ;	
         format 	  PCT013E004	best12. ;	
         format 	  PCT013E005	best12. ;	
         format 	  PCT013E006	best12. ;	
         format 	  PCT013E007	best12. ;	
         format 	  PCT013E008	best12. ;	
         format 	  PCT013E009	best12. ;	
         format 	  PCT013E010	best12. ;	
         format 	  PCT013E011	best12. ;	
         format 	  PCT013E012	best12. ;	
         format 	  PCT013E013	best12. ;	
         format 	  PCT013E014	best12. ;	
         format 	  PCT013E015	best12. ;	
         format 	  PCT013E016	best12. ;	
         format 	  PCT013E017	best12. ;	
         format 	  PCT013E018	best12. ;	
         format 	  PCT013E019	best12. ;	
         format 	  PCT013E020	best12. ;	
         format 	  PCT013E021	best12. ;	
         format 	  PCT013E022	best12. ;	
         format 	  PCT013E023	best12. ;	
         format 	  PCT013E024	best12. ;	
         format 	  PCT013E025	best12. ;	
         format 	  PCT013E026	best12. ;	
         format 	  PCT013E027	best12. ;	
         format 	  PCT013E028	best12. ;	
         format 	  PCT013E029	best12. ;	
         format 	  PCT013E030	best12. ;	
         format 	  PCT013E031	best12. ;	
         format 	  PCT013E032	best12. ;	
         format 	  PCT013E033	best12. ;	
         format 	  PCT013E034	best12. ;	
         format 	  PCT013E035	best12. ;	
         format 	  PCT013E036	best12. ;	
         format 	  PCT013E037	best12. ;	
         format 	  PCT013E038	best12. ;	
         format 	  PCT013E039	best12. ;	
         format 	  PCT013E040	best12. ;	
         format 	  PCT013E041	best12. ;	
         format 	  PCT013E042	best12. ;	
         format 	  PCT013E043	best12. ;	
         format 	  PCT013E044	best12. ;	
         format 	  PCT013E045	best12. ;	
         format 	  PCT013E046	best12. ;	
         format 	  PCT013E047	best12. ;	
         format 	  PCT013E048	best12. ;	
         format 	  PCT013E049	best12. ;	
         format 	  PCT013F001	best12. ;	
         format 	  PCT013F002	best12. ;	
         format 	  PCT013F003	best12. ;	
         format 	  PCT013F004	best12. ;	
         format 	  PCT013F005	best12. ;	
         format 	  PCT013F006	best12. ;	
         format 	  PCT013F007	best12. ;	
         format 	  PCT013F008	best12. ;	
         format 	  PCT013F009	best12. ;	
         format 	  PCT013F010	best12. ;	
         format 	  PCT013F011	best12. ;	
         format 	  PCT013F012	best12. ;	
         format 	  PCT013F013	best12. ;	
         format 	  PCT013F014	best12. ;	
         format 	  PCT013F015	best12. ;	
         format 	  PCT013F016	best12. ;	
         format 	  PCT013F017	best12. ;	
         format 	  PCT013F018	best12. ;	
         format 	  PCT013F019	best12. ;	
         format 	  PCT013F020	best12. ;	
         format 	  PCT013F021	best12. ;	
         format 	  PCT013F022	best12. ;	
         format 	  PCT013F023	best12. ;	
         format 	  PCT013F024	best12. ;	
         format 	  PCT013F025	best12. ;	
         format 	  PCT013F026	best12. ;	
         format 	  PCT013F027	best12. ;	
         format 	  PCT013F028	best12. ;	
         format 	  PCT013F029	best12. ;	
         format 	  PCT013F030	best12. ;	
         format 	  PCT013F031	best12. ;	
         format 	  PCT013F032	best12. ;	
         format 	  PCT013F033	best12. ;	
         format 	  PCT013F034	best12. ;	
         format 	  PCT013F035	best12. ;	
         format 	  PCT013F036	best12. ;	
         format 	  PCT013F037	best12. ;	
         format 	  PCT013F038	best12. ;	
         format 	  PCT013F039	best12. ;	
         format 	  PCT013F040	best12. ;	
         format 	  PCT013F041	best12. ;	
         format 	  PCT013F042	best12. ;	
         format 	  PCT013F043	best12. ;	
         format 	  PCT013F044	best12. ;	
         format 	  PCT013F045	best12. ;	
         format 	  PCT013F046	best12. ;	
         format 	  PCT013F047	best12. ;	
         format 	  PCT013F048	best12. ;	
         format 	  PCT013F049	best12. ;	
         format 	  PCT013G001	best12. ;	
         format 	  PCT013G002	best12. ;	
         format 	  PCT013G003	best12. ;	
         format 	  PCT013G004	best12. ;	
         format 	  PCT013G005	best12. ;	
         format 	  PCT013G006	best12. ;	
         format 	  PCT013G007	best12. ;	
         format 	  PCT013G008	best12. ;	
         format 	  PCT013G009	best12. ;	
         format 	  PCT013G010	best12. ;	
         format 	  PCT013G011	best12. ;	
         format 	  PCT013G012	best12. ;	
         format 	  PCT013G013	best12. ;	
         format 	  PCT013G014	best12. ;	
         format 	  PCT013G015	best12. ;	
         format 	  PCT013G016	best12. ;	
         format 	  PCT013G017	best12. ;	
         format 	  PCT013G018	best12. ;	
         format 	  PCT013G019	best12. ;	
         format 	  PCT013G020	best12. ;	
         format 	  PCT013G021	best12. ;	
         format 	  PCT013G022	best12. ;	
         format 	  PCT013G023	best12. ;	
         format 	  PCT013G024	best12. ;	
         format 	  PCT013G025	best12. ;	
         format 	  PCT013G026	best12. ;	
         format 	  PCT013G027	best12. ;	
         format 	  PCT013G028	best12. ;	
         format 	  PCT013G029	best12. ;	
         format 	  PCT013G030	best12. ;	
         format 	  PCT013G031	best12. ;	
         format 	  PCT013G032	best12. ;	
         format 	  PCT013G033	best12. ;	
         format 	  PCT013G034	best12. ;	
         format 	  PCT013G035	best12. ;	
         format 	  PCT013G036	best12. ;	
         format 	  PCT013G037	best12. ;	
         format 	  PCT013G038	best12. ;	
         format 	  PCT013G039	best12. ;	
         format 	  PCT013G040	best12. ;	
         format 	  PCT013G041	best12. ;	
         format 	  PCT013G042	best12. ;	
         format 	  PCT013G043	best12. ;	
         format 	  PCT013G044	best12. ;	
         format 	  PCT013G045	best12. ;	
         format 	  PCT013G046	best12. ;	
         format 	  PCT013G047	best12. ;	
         format 	  PCT013G048	best12. ;	
         format 	  PCT013G049	best12. ;	
         format 	  PCT013H001	best12. ;	
         format 	  PCT013H002	best12. ;	
         format 	  PCT013H003	best12. ;	
         format 	  PCT013H004	best12. ;	
         format 	  PCT013H005	best12. ;	
         format 	  PCT013H006	best12. ;	
         format 	  PCT013H007	best12. ;	
         format 	  PCT013H008	best12. ;	
         format 	  PCT013H009	best12. ;	
         format 	  PCT013H010	best12. ;	
         format 	  PCT013H011	best12. ;	
         format 	  PCT013H012	best12. ;	
         format 	  PCT013H013	best12. ;	
         format 	  PCT013H014	best12. ;	
         format 	  PCT013H015	best12. ;	
         format 	  PCT013H016	best12. ;	
         format 	  PCT013H017	best12. ;	
         format 	  PCT013H018	best12. ;	
         format 	  PCT013H019	best12. ;	
         format 	  PCT013H020	best12. ;	
         format 	  PCT013H021	best12. ;	
         format 	  PCT013H022	best12. ;	
         format 	  PCT013H023	best12. ;	
         format 	  PCT013H024	best12. ;	
         format 	  PCT013H025	best12. ;	
         format 	  PCT013H026	best12. ;	
         format 	  PCT013H027	best12. ;	
         format 	  PCT013H028	best12. ;	
         format 	  PCT013H029	best12. ;	
         format 	  PCT013H030	best12. ;	
         format 	  PCT013H031	best12. ;	
         format 	  PCT013H032	best12. ;	
         format 	  PCT013H033	best12. ;	
         format 	  PCT013H034	best12. ;	
         format 	  PCT013H035	best12. ;	
         format 	  PCT013H036	best12. ;	
         format 	  PCT013H037	best12. ;	
         format 	  PCT013H038	best12. ;	
         format 	  PCT013H039	best12. ;	
         format 	  PCT013H040	best12. ;	
         format 	  PCT013H041	best12. ;	
         format 	  PCT013H042	best12. ;	
         format 	  PCT013H043	best12. ;	
         format 	  PCT013H044	best12. ;	
         format 	  PCT013H045	best12. ;	
         format 	  PCT013H046	best12. ;	
         format 	  PCT013H047	best12. ;	
         format 	  PCT013H048	best12. ;	
         format 	  PCT013H049	best12. ;	
         format 	  PCT013I001	best12. ;	
         format 	  PCT013I002	best12. ;	
         format 	  PCT013I003	best12. ;	
         format 	  PCT013I004	best12. ;	
         format 	  PCT013I005	best12. ;	
         format 	  PCT013I006	best12. ;	
         format 	  PCT013I007	best12. ;	
         format 	  PCT013I008	best12. ;	
         format 	  PCT013I009	best12. ;	
         format 	  PCT013I010	best12. ;	
         format 	  PCT013I011	best12. ;	
         format 	  PCT013I012	best12. ;	
         format 	  PCT013I013	best12. ;	
         format 	  PCT013I014	best12. ;	
         format 	  PCT013I015	best12. ;	
         format 	  PCT013I016	best12. ;	
         format 	  PCT013I017	best12. ;	
         format 	  PCT013I018	best12. ;	
         format 	  PCT013I019	best12. ;	
         format 	  PCT013I020	best12. ;	
         format 	  PCT013I021	best12. ;	
         format 	  PCT013I022	best12. ;	
         format 	  PCT013I023	best12. ;	
         format 	  PCT013I024	best12. ;	
         format 	  PCT013I025	best12. ;	
         format 	  PCT013I026	best12. ;	
         format 	  PCT013I027	best12. ;	
         format 	  PCT013I028	best12. ;	
         format 	  PCT013I029	best12. ;	
         format 	  PCT013I030	best12. ;	
         format 	  PCT013I031	best12. ;	
         format 	  PCT013I032	best12. ;	
         format 	  PCT013I033	best12. ;	
         format 	  PCT013I034	best12. ;	
         format 	  PCT013I035	best12. ;	
         format 	  PCT013I036	best12. ;	
         format 	  PCT013I037	best12. ;	
         format 	  PCT013I038	best12. ;	
         format 	  PCT013I039	best12. ;	
         format 	  PCT013I040	best12. ;	
         format 	  PCT013I041	best12. ;	
         format 	  PCT013I042	best12. ;	
         format 	  PCT013I043	best12. ;	
         format 	  PCT013I044	best12. ;	
         format 	  PCT013I045	best12. ;	
         format 	  PCT013I046	best12. ;	
         format 	  PCT013I047	best12. ;	
         format 	  PCT013I048	best12. ;	
         format 	  PCT013I049	best12. ;	
         format 	  PCT014A001	best12. ;	
         format 	  PCT014A002	best12. ;	
         format 	  PCT014A003	best12. ;	
         format 	  PCT014B001	best12. ;	
         format 	  PCT014B002	best12. ;	
         format 	  PCT014B003	best12. ;	
         format 	  PCT014C001	best12. ;	
         format 	  PCT014C002	best12. ;	
         format 	  PCT014C003	best12. ;	
         format 	  PCT014D001	best12. ;	
         format 	  PCT014D002	best12. ;	
         format 	  PCT014D003	best12. ;	
         format 	  PCT014E001	best12. ;	
         format 	  PCT014E002	best12. ;	
         format 	  PCT014E003	best12. ;	
         format 	  PCT014F001	best12. ;	
         format 	  PCT014F002	best12. ;	
         format 	  PCT014F003	best12. ;	
         format 	  PCT014G001	best12. ;	
         format 	  PCT014G002	best12. ;	
         format 	  PCT014G003	best12. ;	
         format 	  PCT014H001	best12. ;	
         format 	  PCT014H002	best12. ;	
         format 	  PCT014H003	best12. ;	
         format 	  PCT014I001	best12. ;	
         format 	  PCT014I002	best12. ;	
         format 	  PCT014I003	best12. ;	
         format 	  PCT019A001	best12. ;	
         format 	  PCT019A002	best12. ;	
         format 	  PCT019A003	best12. ;	
         format 	  PCT019A004	best12. ;	
         format 	  PCT019A005	best12. ;	
         format 	  PCT019A006	best12. ;	
         format 	  PCT019A007	best12. ;	
         format 	  PCT019A008	best12. ;	
         format 	  PCT019A009	best12. ;	
         format 	  PCT019A010	best12. ;	
         format 	  PCT019A011	best12. ;	
         format 	  PCT019B001	best12. ;	
         format 	  PCT019B002	best12. ;	
         format 	  PCT019B003	best12. ;	
         format 	  PCT019B004	best12. ;	
         format 	  PCT019B005	best12. ;	
         format 	  PCT019B006	best12. ;	
         format 	  PCT019B007	best12. ;	
         format 	  PCT019B008	best12. ;	
         format 	  PCT019B009	best12. ;	
         format 	  PCT019B010	best12. ;	
         format 	  PCT019B011	best12. ;	
         format 	  PCT019C001	best12. ;	
         format 	  PCT019C002	best12. ;	
         format 	  PCT019C003	best12. ;	
         format 	  PCT019C004	best12. ;	
         format 	  PCT019C005	best12. ;	
         format 	  PCT019C006	best12. ;	
         format 	  PCT019C007	best12. ;	
         format 	  PCT019C008	best12. ;	
         format 	  PCT019C009	best12. ;	
         format 	  PCT019C010	best12. ;	
         format 	  PCT019C011	best12. ;	
         format 	  PCT019D001	best12. ;	
         format 	  PCT019D002	best12. ;	
         format 	  PCT019D003	best12. ;	
         format 	  PCT019D004	best12. ;	
         format 	  PCT019D005	best12. ;	
         format 	  PCT019D006	best12. ;	
         format 	  PCT019D007	best12. ;	
         format 	  PCT019D008	best12. ;	
         format 	  PCT019D009	best12. ;	
         format 	  PCT019D010	best12. ;	
         format 	  PCT019D011	best12. ;	
         format 	  PCT019E001	best12. ;	
         format 	  PCT019E002	best12. ;	
         format 	  PCT019E003	best12. ;	
         format 	  PCT019E004	best12. ;	
         format 	  PCT019E005	best12. ;	
         format 	  PCT019E006	best12. ;	
         format 	  PCT019E007	best12. ;	
         format 	  PCT019E008	best12. ;	
         format 	  PCT019E009	best12. ;	
         format 	  PCT019E010	best12. ;	
         format 	  PCT019E011	best12. ;	
         format 	  PCT019F001	best12. ;	
         format 	  PCT019F002	best12. ;	
         format 	  PCT019F003	best12. ;	
         format 	  PCT019F004	best12. ;	
         format 	  PCT019F005	best12. ;	
         format 	  PCT019F006	best12. ;	
         format 	  PCT019F007	best12. ;	
         format 	  PCT019F008	best12. ;	
         format 	  PCT019F009	best12. ;	
         format 	  PCT019F010	best12. ;	
         format 	  PCT019F011	best12. ;	
         format 	  PCT019G001	best12. ;	
         format 	  PCT019G002	best12. ;	
         format 	  PCT019G003	best12. ;	
         format 	  PCT019G004	best12. ;	
         format 	  PCT019G005	best12. ;	
         format 	  PCT019G006	best12. ;	
         format 	  PCT019G007	best12. ;	
         format 	  PCT019G008	best12. ;	
         format 	  PCT019G009	best12. ;	
         format 	  PCT019G010	best12. ;	
         format 	  PCT019G011	best12. ;	
         format 	  PCT019H001	best12. ;	
         format 	  PCT019H002	best12. ;	
         format 	  PCT019H003	best12. ;	
         format 	  PCT019H004	best12. ;	
         format 	  PCT019H005	best12. ;	
         format 	  PCT019H006	best12. ;	
         format 	  PCT019H007	best12. ;	
         format 	  PCT019H008	best12. ;	
         format 	  PCT019H009	best12. ;	
         format 	  PCT019H010	best12. ;	
         format 	  PCT019H011	best12. ;	
         format 	  PCT019I001	best12. ;	
         format 	  PCT019I002	best12. ;	
         format 	  PCT019I003	best12. ;	
         format 	  PCT019I004	best12. ;	
         format 	  PCT019I005	best12. ;	
         format 	  PCT019I006	best12. ;	
         format 	  PCT019I007	best12. ;	
         format 	  PCT019I008	best12. ;	
         format 	  PCT019I009	best12. ;	
         format 	  PCT019I010	best12. ;	
         format 	  PCT019I011	best12. ;	
         format 	  PCT020A001	best12. ;	
         format 	  PCT020A002	best12. ;	
         format 	  PCT020A003	best12. ;	
         format 	  PCT020A004	best12. ;	
         format 	  PCT020A005	best12. ;	
         format 	  PCT020A006	best12. ;	
         format 	  PCT020A007	best12. ;	
         format 	  PCT020A008	best12. ;	
         format 	  PCT020A009	best12. ;	
         format 	  PCT020A010	best12. ;	
         format 	  PCT020A011	best12. ;	
         format 	  PCT020A012	best12. ;	
         format 	  PCT020A013	best12. ;	
         format 	  PCT020A014	best12. ;	
         format 	  PCT020A015	best12. ;	
         format 	  PCT020A016	best12. ;	
         format 	  PCT020A017	best12. ;	
         format 	  PCT020A018	best12. ;	
         format 	  PCT020A019	best12. ;	
         format 	  PCT020A020	best12. ;	
         format 	  PCT020A021	best12. ;	
         format 	  PCT020A022	best12. ;	
         format 	  PCT020A023	best12. ;	
         format 	  PCT020A024	best12. ;	
         format 	  PCT020A025	best12. ;	
         format 	  PCT020A026	best12. ;	
         format 	  PCT020A027	best12. ;	
         format 	  PCT020A028	best12. ;	
         format 	  PCT020A029	best12. ;	
         format 	  PCT020A030	best12. ;	
         format 	  PCT020A031	best12. ;	
         format 	  PCT020A032	best12. ;	
         format 	  PCT020B001	best12. ;	
         format 	  PCT020B002	best12. ;	
         format 	  PCT020B003	best12. ;	
         format 	  PCT020B004	best12. ;	
         format 	  PCT020B005	best12. ;	
         format 	  PCT020B006	best12. ;	
         format 	  PCT020B007	best12. ;	
         format 	  PCT020B008	best12. ;	
         format 	  PCT020B009	best12. ;	
         format 	  PCT020B010	best12. ;	
         format 	  PCT020B011	best12. ;	
         format 	  PCT020B012	best12. ;	
         format 	  PCT020B013	best12. ;	
         format 	  PCT020B014	best12. ;	
         format 	  PCT020B015	best12. ;	
         format 	  PCT020B016	best12. ;	
         format 	  PCT020B017	best12. ;	
         format 	  PCT020B018	best12. ;	
         format 	  PCT020B019	best12. ;	
         format 	  PCT020B020	best12. ;	
         format 	  PCT020B021	best12. ;	
         format 	  PCT020B022	best12. ;	
         format 	  PCT020B023	best12. ;	
         format 	  PCT020B024	best12. ;	
         format 	  PCT020B025	best12. ;	
         format 	  PCT020B026	best12. ;	
         format 	  PCT020B027	best12. ;	
         format 	  PCT020B028	best12. ;	
         format 	  PCT020B029	best12. ;	
         format 	  PCT020B030	best12. ;	
         format 	  PCT020B031	best12. ;	
         format 	  PCT020B032	best12. ;	
         format 	  PCT020C001	best12. ;	
         format 	  PCT020C002	best12. ;	
         format 	  PCT020C003	best12. ;	
         format 	  PCT020C004	best12. ;	
         format 	  PCT020C005	best12. ;	
         format 	  PCT020C006	best12. ;	
         format 	  PCT020C007	best12. ;	
         format 	  PCT020C008	best12. ;	
         format 	  PCT020C009	best12. ;	
         format 	  PCT020C010	best12. ;	
         format 	  PCT020C011	best12. ;	
         format 	  PCT020C012	best12. ;	
         format 	  PCT020C013	best12. ;	
         format 	  PCT020C014	best12. ;	
         format 	  PCT020C015	best12. ;	
         format 	  PCT020C016	best12. ;	
         format 	  PCT020C017	best12. ;	
         format 	  PCT020C018	best12. ;	
         format 	  PCT020C019	best12. ;	
         format 	  PCT020C020	best12. ;	
         format 	  PCT020C021	best12. ;	
         format 	  PCT020C022	best12. ;	
         format 	  PCT020C023	best12. ;	
         format 	  PCT020C024	best12. ;	
         format 	  PCT020C025	best12. ;	
         format 	  PCT020C026	best12. ;	
         format 	  PCT020C027	best12. ;	
         format 	  PCT020C028	best12. ;	
         format 	  PCT020C029	best12. ;	
         format 	  PCT020C030	best12. ;	
         format 	  PCT020C031	best12. ;	
         format 	  PCT020C032	best12. ;	
         format 	  PCT020D001	best12. ;	
         format 	  PCT020D002	best12. ;	
         format 	  PCT020D003	best12. ;	
         format 	  PCT020D004	best12. ;	
         format 	  PCT020D005	best12. ;	
         format 	  PCT020D006	best12. ;	
         format 	  PCT020D007	best12. ;	
         format 	  PCT020D008	best12. ;	
         format 	  PCT020D009	best12. ;	
         format 	  PCT020D010	best12. ;	
         format 	  PCT020D011	best12. ;	
         format 	  PCT020D012	best12. ;	
         format 	  PCT020D013	best12. ;	
         format 	  PCT020D014	best12. ;	
         format 	  PCT020D015	best12. ;	
         format 	  PCT020D016	best12. ;	
         format 	  PCT020D017	best12. ;	
         format 	  PCT020D018	best12. ;	
         format 	  PCT020D019	best12. ;	
         format 	  PCT020D020	best12. ;	
         format 	  PCT020D021	best12. ;	
         format 	  PCT020D022	best12. ;	
         format 	  PCT020D023	best12. ;	
         format 	  PCT020D024	best12. ;	
         format 	  PCT020D025	best12. ;	
         format 	  PCT020D026	best12. ;	
         format 	  PCT020D027	best12. ;	
         format 	  PCT020D028	best12. ;	
         format 	  PCT020D029	best12. ;	
         format 	  PCT020D030	best12. ;	
         format 	  PCT020D031	best12. ;	
         format 	  PCT020D032	best12. ;	
         format 	  PCT020E001	best12. ;	
         format 	  PCT020E002	best12. ;	
         format 	  PCT020E003	best12. ;	
         format 	  PCT020E004	best12. ;	
         format 	  PCT020E005	best12. ;	
         format 	  PCT020E006	best12. ;	
         format 	  PCT020E007	best12. ;	
         format 	  PCT020E008	best12. ;	
         format 	  PCT020E009	best12. ;	
         format 	  PCT020E010	best12. ;	
         format 	  PCT020E011	best12. ;	
         format 	  PCT020E012	best12. ;	
         format 	  PCT020E013	best12. ;	
         format 	  PCT020E014	best12. ;	
         format 	  PCT020E015	best12. ;	
         format 	  PCT020E016	best12. ;	
         format 	  PCT020E017	best12. ;	
         format 	  PCT020E018	best12. ;	
         format 	  PCT020E019	best12. ;	
         format 	  PCT020E020	best12. ;	
         format 	  PCT020E021	best12. ;	
         format 	  PCT020E022	best12. ;	
         format 	  PCT020E023	best12. ;	
         format 	  PCT020E024	best12. ;	
         format 	  PCT020E025	best12. ;	
         format 	  PCT020E026	best12. ;	
         format 	  PCT020E027	best12. ;	
         format 	  PCT020E028	best12. ;	
         format 	  PCT020E029	best12. ;	
         format 	  PCT020E030	best12. ;	
         format 	  PCT020E031	best12. ;	
         format 	  PCT020E032	best12. ;	
         format 	  PCT020F001	best12. ;	
         format 	  PCT020F002	best12. ;	
         format 	  PCT020F003	best12. ;	
         format 	  PCT020F004	best12. ;	
         format 	  PCT020F005	best12. ;	
         format 	  PCT020F006	best12. ;	
         format 	  PCT020F007	best12. ;	
         format 	  PCT020F008	best12. ;	
         format 	  PCT020F009	best12. ;	
         format 	  PCT020F010	best12. ;	
         format 	  PCT020F011	best12. ;	
         format 	  PCT020F012	best12. ;	
         format 	  PCT020F013	best12. ;	
         format 	  PCT020F014	best12. ;	
         format 	  PCT020F015	best12. ;	
         format 	  PCT020F016	best12. ;	
         format 	  PCT020F017	best12. ;	
         format 	  PCT020F018	best12. ;	
         format 	  PCT020F019	best12. ;	
         format 	  PCT020F020	best12. ;	
         format 	  PCT020F021	best12. ;	
         format 	  PCT020F022	best12. ;	
         format 	  PCT020F023	best12. ;	
         format 	  PCT020F024	best12. ;	
         format 	  PCT020F025	best12. ;	
         format 	  PCT020F026	best12. ;	
         format 	  PCT020F027	best12. ;	
         format 	  PCT020F028	best12. ;	
         format 	  PCT020F029	best12. ;	
         format 	  PCT020F030	best12. ;	
         format 	  PCT020F031	best12. ;	
         format 	  PCT020F032	best12. ;	
         format 	  PCT020G001	best12. ;	
         format 	  PCT020G002	best12. ;	
         format 	  PCT020G003	best12. ;	
         format 	  PCT020G004	best12. ;	
         format 	  PCT020G005	best12. ;	
         format 	  PCT020G006	best12. ;	
         format 	  PCT020G007	best12. ;	
         format 	  PCT020G008	best12. ;	
         format 	  PCT020G009	best12. ;	
         format 	  PCT020G010	best12. ;	
         format 	  PCT020G011	best12. ;	
         format 	  PCT020G012	best12. ;	
         format 	  PCT020G013	best12. ;	
         format 	  PCT020G014	best12. ;	
         format 	  PCT020G015	best12. ;	
         format 	  PCT020G016	best12. ;	
         format 	  PCT020G017	best12. ;	
         format 	  PCT020G018	best12. ;	
         format 	  PCT020G019	best12. ;	
         format 	  PCT020G020	best12. ;	
         format 	  PCT020G021	best12. ;	
         format 	  PCT020G022	best12. ;	
         format 	  PCT020G023	best12. ;	
         format 	  PCT020G024	best12. ;	
         format 	  PCT020G025	best12. ;	
         format 	  PCT020G026	best12. ;	
         format 	  PCT020G027	best12. ;	
         format 	  PCT020G028	best12. ;	
         format 	  PCT020G029	best12. ;	
         format 	  PCT020G030	best12. ;	
         format 	  PCT020G031	best12. ;	
         format 	  PCT020G032	best12. ;	
         format 	  PCT020H001	best12. ;	
         format 	  PCT020H002	best12. ;	
         format 	  PCT020H003	best12. ;	
         format 	  PCT020H004	best12. ;	
         format 	  PCT020H005	best12. ;	
         format 	  PCT020H006	best12. ;	
         format 	  PCT020H007	best12. ;	
         format 	  PCT020H008	best12. ;	
         format 	  PCT020H009	best12. ;	
         format 	  PCT020H010	best12. ;	
         format 	  PCT020H011	best12. ;	
         format 	  PCT020H012	best12. ;	
         format 	  PCT020H013	best12. ;	
         format 	  PCT020H014	best12. ;	
         format 	  PCT020H015	best12. ;	
         format 	  PCT020H016	best12. ;	
         format 	  PCT020H017	best12. ;	
         format 	  PCT020H018	best12. ;	
         format 	  PCT020H019	best12. ;	
         format 	  PCT020H020	best12. ;	
         format 	  PCT020H021	best12. ;	
         format 	  PCT020H022	best12. ;	
         format 	  PCT020H023	best12. ;	
         format 	  PCT020H024	best12. ;	
         format 	  PCT020H025	best12. ;	
         format 	  PCT020H026	best12. ;	
         format 	  PCT020H027	best12. ;	
         format 	  PCT020H028	best12. ;	
         format 	  PCT020H029	best12. ;	
         format 	  PCT020H030	best12. ;	
         format 	  PCT020H031	best12. ;	
         format 	  PCT020H032	best12. ;	
         format 	  PCT020I001	best12. ;	
         format 	  PCT020I002	best12. ;	
         format 	  PCT020I003	best12. ;	
         format 	  PCT020I004	best12. ;	
         format 	  PCT020I005	best12. ;	
         format 	  PCT020I006	best12. ;	
         format 	  PCT020I007	best12. ;	
         format 	  PCT020I008	best12. ;	
         format 	  PCT020I009	best12. ;	
         format 	  PCT020I010	best12. ;	
         format 	  PCT020I011	best12. ;	
         format 	  PCT020I012	best12. ;	
         format 	  PCT020I013	best12. ;	
         format 	  PCT020I014	best12. ;	
         format 	  PCT020I015	best12. ;	
         format 	  PCT020I016	best12. ;	
         format 	  PCT020I017	best12. ;	
         format 	  PCT020I018	best12. ;	
         format 	  PCT020I019	best12. ;	
         format 	  PCT020I020	best12. ;	
         format 	  PCT020I021	best12. ;	
         format 	  PCT020I022	best12. ;	
         format 	  PCT020I023	best12. ;	
         format 	  PCT020I024	best12. ;	
         format 	  PCT020I025	best12. ;	
         format 	  PCT020I026	best12. ;	
         format 	  PCT020I027	best12. ;	
         format 	  PCT020I028	best12. ;	
         format 	  PCT020I029	best12. ;	
         format 	  PCT020I030	best12. ;	
         format 	  PCT020I031	best12. ;	
         format 	  PCT020I032	best12. ;	
         format 	  PCT022A001	best12. ;	
         format 	  PCT022A002	best12. ;	
         format 	  PCT022A003	best12. ;	
         format 	  PCT022A004	best12. ;	
         format 	  PCT022A005	best12. ;	
         format 	  PCT022A006	best12. ;	
         format 	  PCT022A007	best12. ;	
         format 	  PCT022A008	best12. ;	
         format 	  PCT022A009	best12. ;	
         format 	  PCT022A010	best12. ;	
         format 	  PCT022A011	best12. ;	
         format 	  PCT022A012	best12. ;	
         format 	  PCT022A013	best12. ;	
         format 	  PCT022A014	best12. ;	
         format 	  PCT022A015	best12. ;	
         format 	  PCT022A016	best12. ;	
         format 	  PCT022A017	best12. ;	
         format 	  PCT022A018	best12. ;	
         format 	  PCT022A019	best12. ;	
         format 	  PCT022A020	best12. ;	
         format 	  PCT022A021	best12. ;	
         format 	  PCT022B001	best12. ;	
         format 	  PCT022B002	best12. ;	
         format 	  PCT022B003	best12. ;	
         format 	  PCT022B004	best12. ;	
         format 	  PCT022B005	best12. ;	
         format 	  PCT022B006	best12. ;	
         format 	  PCT022B007	best12. ;	
         format 	  PCT022B008	best12. ;	
         format 	  PCT022B009	best12. ;	
         format 	  PCT022B010	best12. ;	
         format 	  PCT022B011	best12. ;	
         format 	  PCT022B012	best12. ;	
         format 	  PCT022B013	best12. ;	
         format 	  PCT022B014	best12. ;	
         format 	  PCT022B015	best12. ;	
         format 	  PCT022B016	best12. ;	
         format 	  PCT022B017	best12. ;	
         format 	  PCT022B018	best12. ;	
         format 	  PCT022B019	best12. ;	
         format 	  PCT022B020	best12. ;	
         format 	  PCT022B021	best12. ;	
         format 	  PCT022C001	best12. ;	
         format 	  PCT022C002	best12. ;	
         format 	  PCT022C003	best12. ;	
         format 	  PCT022C004	best12. ;	
         format 	  PCT022C005	best12. ;	
         format 	  PCT022C006	best12. ;	
         format 	  PCT022C007	best12. ;	
         format 	  PCT022C008	best12. ;	
         format 	  PCT022C009	best12. ;	
         format 	  PCT022C010	best12. ;	
         format 	  PCT022C011	best12. ;	
         format 	  PCT022C012	best12. ;	
         format 	  PCT022C013	best12. ;	
         format 	  PCT022C014	best12. ;	
         format 	  PCT022C015	best12. ;	
         format 	  PCT022C016	best12. ;	
         format 	  PCT022C017	best12. ;	
         format 	  PCT022C018	best12. ;	
         format 	  PCT022C019	best12. ;	
         format 	  PCT022C020	best12. ;	
         format 	  PCT022C021	best12. ;	
         format 	  PCT022D001	best12. ;	
         format 	  PCT022D002	best12. ;	
         format 	  PCT022D003	best12. ;	
         format 	  PCT022D004	best12. ;	
         format 	  PCT022D005	best12. ;	
         format 	  PCT022D006	best12. ;	
         format 	  PCT022D007	best12. ;	
         format 	  PCT022D008	best12. ;	
         format 	  PCT022D009	best12. ;	
         format 	  PCT022D010	best12. ;	
         format 	  PCT022D011	best12. ;	
         format 	  PCT022D012	best12. ;	
         format 	  PCT022D013	best12. ;	
         format 	  PCT022D014	best12. ;	
         format 	  PCT022D015	best12. ;	
         format 	  PCT022D016	best12. ;	
         format 	  PCT022D017	best12. ;	
         format 	  PCT022D018	best12. ;	
         format 	  PCT022D019	best12. ;	
         format 	  PCT022D020	best12. ;	
         format 	  PCT022D021	best12. ;	
         format 	  PCT022E001	best12. ;	
         format 	  PCT022E002	best12. ;	
         format 	  PCT022E003	best12. ;	
         format 	  PCT022E004	best12. ;	
         format 	  PCT022E005	best12. ;	
         format 	  PCT022E006	best12. ;	
         format 	  PCT022E007	best12. ;	
         format 	  PCT022E008	best12. ;	
         format 	  PCT022E009	best12. ;	
         format 	  PCT022E010	best12. ;	
         format 	  PCT022E011	best12. ;	
         format 	  PCT022E012	best12. ;	
         format 	  PCT022E013	best12. ;	
         format 	  PCT022E014	best12. ;	
         format 	  PCT022E015	best12. ;	
         format 	  PCT022E016	best12. ;	
         format 	  PCT022E017	best12. ;	
         format 	  PCT022E018	best12. ;	
         format 	  PCT022E019	best12. ;	
         format 	  PCT022E020	best12. ;	
         format 	  PCT022E021	best12. ;	
         format 	  PCT022F001	best12. ;	
         format 	  PCT022F002	best12. ;	
         format 	  PCT022F003	best12. ;	
         format 	  PCT022F004	best12. ;	
         format 	  PCT022F005	best12. ;	
         format 	  PCT022F006	best12. ;	
         format 	  PCT022F007	best12. ;	
         format 	  PCT022F008	best12. ;	
         format 	  PCT022F009	best12. ;	
         format 	  PCT022F010	best12. ;	
         format 	  PCT022F011	best12. ;	
         format 	  PCT022F012	best12. ;	
         format 	  PCT022F013	best12. ;	
         format 	  PCT022F014	best12. ;	
         format 	  PCT022F015	best12. ;	
         format 	  PCT022F016	best12. ;	
         format 	  PCT022F017	best12. ;	
         format 	  PCT022F018	best12. ;	
         format 	  PCT022F019	best12. ;	
         format 	  PCT022F020	best12. ;	
         format 	  PCT022F021	best12. ;	
         format 	  PCT022G001	best12. ;	
         format 	  PCT022G002	best12. ;	
         format 	  PCT022G003	best12. ;	
         format 	  PCT022G004	best12. ;	
         format 	  PCT022G005	best12. ;	
         format 	  PCT022G006	best12. ;	
         format 	  PCT022G007	best12. ;	
         format 	  PCT022G008	best12. ;	
         format 	  PCT022G009	best12. ;	
         format 	  PCT022G010	best12. ;	
         format 	  PCT022G011	best12. ;	
         format 	  PCT022G012	best12. ;	
         format 	  PCT022G013	best12. ;	
         format 	  PCT022G014	best12. ;	
         format 	  PCT022G015	best12. ;	
         format 	  PCT022G016	best12. ;	
         format 	  PCT022G017	best12. ;	
         format 	  PCT022G018	best12. ;	
         format 	  PCT022G019	best12. ;	
         format 	  PCT022G020	best12. ;	
         format 	  PCT022G021	best12. ;	
         format 	  PCT022H001	best12. ;	
         format 	  PCT022H002	best12. ;	
         format 	  PCT022H003	best12. ;	
         format 	  PCT022H004	best12. ;	
         format 	  PCT022H005	best12. ;	
         format 	  PCT022H006	best12. ;	
         format 	  PCT022H007	best12. ;	
         format 	  PCT022H008	best12. ;	
         format 	  PCT022H009	best12. ;	
         format 	  PCT022H010	best12. ;	
         format 	  PCT022H011	best12. ;	
         format 	  PCT022H012	best12. ;	
         format 	  PCT022H013	best12. ;	
         format 	  PCT022H014	best12. ;	
         format 	  PCT022H015	best12. ;	
         format 	  PCT022H016	best12. ;	
         format 	  PCT022H017	best12. ;	
         format 	  PCT022H018	best12. ;	
         format 	  PCT022H019	best12. ;	
         format 	  PCT022H020	best12. ;	
         format 	  PCT022H021	best12. ;	
         format 	  PCT022I001	best12. ;	
         format 	  PCT022I002	best12. ;	
         format 	  PCT022I003	best12. ;	
         format 	  PCT022I004	best12. ;	
         format 	  PCT022I005	best12. ;	
         format 	  PCT022I006	best12. ;	
         format 	  PCT022I007	best12. ;	
         format 	  PCT022I008	best12. ;	
         format 	  PCT022I009	best12. ;	
         format 	  PCT022I010	best12. ;	
         format 	  PCT022I011	best12. ;	
         format 	  PCT022I012	best12. ;	
         format 	  PCT022I013	best12. ;	
         format 	  PCT022I014	best12. ;	
         format 	  PCT022I015	best12. ;	
         format 	  PCT022I016	best12. ;	
         format 	  PCT022I017	best12. ;	
         format 	  PCT022I018	best12. ;	
         format 	  PCT022I019	best12. ;	
         format 	  PCT022I020	best12. ;	
         format 	  PCT022I021	best12. ;	
         format 	  PCO0010001	best12. ;	
         format 	  PCO0010002	best12. ;	
         format 	  PCO0010003	best12. ;	
         format 	  PCO0010004	best12. ;	
         format 	  PCO0010005	best12. ;	
         format 	  PCO0010006	best12. ;	
         format 	  PCO0010007	best12. ;	
         format 	  PCO0010008	best12. ;	
         format 	  PCO0010009	best12. ;	
         format 	  PCO0010010	best12. ;	
         format 	  PCO0010011	best12. ;	
         format 	  PCO0010012	best12. ;	
         format 	  PCO0010013	best12. ;	
         format 	  PCO0010014	best12. ;	
         format 	  PCO0010015	best12. ;	
         format 	  PCO0010016	best12. ;	
         format 	  PCO0010017	best12. ;	
         format 	  PCO0010018	best12. ;	
         format 	  PCO0010019	best12. ;	
         format 	  PCO0010020	best12. ;	
         format 	  PCO0010021	best12. ;	
         format 	  PCO0010022	best12. ;	
         format 	  PCO0010023	best12. ;	
         format 	  PCO0010024	best12. ;	
         format 	  PCO0010025	best12. ;	
         format 	  PCO0010026	best12. ;	
         format 	  PCO0010027	best12. ;	
         format 	  PCO0010028	best12. ;	
         format 	  PCO0010029	best12. ;	
         format 	  PCO0010030	best12. ;	
         format 	  PCO0010031	best12. ;	
         format 	  PCO0010032	best12. ;	
         format 	  PCO0010033	best12. ;	
         format 	  PCO0010034	best12. ;	
         format 	  PCO0010035	best12. ;	
         format 	  PCO0010036	best12. ;	
         format 	  PCO0010037	best12. ;	
         format 	  PCO0010038	best12. ;	
         format 	  PCO0010039	best12. ;	
         format 	  PCO0020001	best12. ;	
         format 	  PCO0020002	best12. ;	
         format 	  PCO0020003	best12. ;	
         format 	  PCO0020004	best12. ;	
         format 	  PCO0020005	best12. ;	
         format 	  PCO0020006	best12. ;	
         format 	  PCO0020007	best12. ;	
         format 	  PCO0020008	best12. ;	
         format 	  PCO0020009	best12. ;	
         format 	  PCO0020010	best12. ;	
         format 	  PCO0020011	best12. ;	
         format 	  PCO0020012	best12. ;	
         format 	  PCO0020013	best12. ;	
         format 	  PCO0020014	best12. ;	
         format 	  PCO0020015	best12. ;	
         format 	  PCO0020016	best12. ;	
         format 	  PCO0020017	best12. ;	
         format 	  PCO0020018	best12. ;	
         format 	  PCO0020019	best12. ;	
         format 	  PCO0020020	best12. ;	
         format 	  PCO0020021	best12. ;	
         format 	  PCO0020022	best12. ;	
         format 	  PCO0020023	best12. ;	
         format 	  PCO0020024	best12. ;	
         format 	  PCO0020025	best12. ;	
         format 	  PCO0020026	best12. ;	
         format 	  PCO0020027	best12. ;	
         format 	  PCO0020028	best12. ;	
         format 	  PCO0020029	best12. ;	
         format 	  PCO0020030	best12. ;	
         format 	  PCO0020031	best12. ;	
         format 	  PCO0020032	best12. ;	
         format 	  PCO0020033	best12. ;	
         format 	  PCO0020034	best12. ;	
         format 	  PCO0020035	best12. ;	
         format 	  PCO0020036	best12. ;	
         format 	  PCO0020037	best12. ;	
         format 	  PCO0020038	best12. ;	
         format 	  PCO0020039	best12. ;	
         format 	  PCO0030001	best12. ;	
         format 	  PCO0030002	best12. ;	
         format 	  PCO0030003	best12. ;	
         format 	  PCO0030004	best12. ;	
         format 	  PCO0030005	best12. ;	
         format 	  PCO0030006	best12. ;	
         format 	  PCO0030007	best12. ;	
         format 	  PCO0030008	best12. ;	
         format 	  PCO0030009	best12. ;	
         format 	  PCO0030010	best12. ;	
         format 	  PCO0030011	best12. ;	
         format 	  PCO0030012	best12. ;	
         format 	  PCO0030013	best12. ;	
         format 	  PCO0030014	best12. ;	
         format 	  PCO0030015	best12. ;	
         format 	  PCO0030016	best12. ;	
         format 	  PCO0030017	best12. ;	
         format 	  PCO0030018	best12. ;	
         format 	  PCO0030019	best12. ;	
         format 	  PCO0030020	best12. ;	
         format 	  PCO0030021	best12. ;	
         format 	  PCO0030022	best12. ;	
         format 	  PCO0030023	best12. ;	
         format 	  PCO0030024	best12. ;	
         format 	  PCO0030025	best12. ;	
         format 	  PCO0030026	best12. ;	
         format 	  PCO0030027	best12. ;	
         format 	  PCO0030028	best12. ;	
         format 	  PCO0030029	best12. ;	
         format 	  PCO0030030	best12. ;	
         format 	  PCO0030031	best12. ;	
         format 	  PCO0030032	best12. ;	
         format 	  PCO0030033	best12. ;	
         format 	  PCO0030034	best12. ;	
         format 	  PCO0030035	best12. ;	
         format 	  PCO0030036	best12. ;	
         format 	  PCO0030037	best12. ;	
         format 	  PCO0030038	best12. ;	
         format 	  PCO0030039	best12. ;	
         format 	  PCO0040001	best12. ;	
         format 	  PCO0040002	best12. ;	
         format 	  PCO0040003	best12. ;	
         format 	  PCO0040004	best12. ;	
         format 	  PCO0040005	best12. ;	
         format 	  PCO0040006	best12. ;	
         format 	  PCO0040007	best12. ;	
         format 	  PCO0040008	best12. ;	
         format 	  PCO0040009	best12. ;	
         format 	  PCO0040010	best12. ;	
         format 	  PCO0040011	best12. ;	
         format 	  PCO0040012	best12. ;	
         format 	  PCO0040013	best12. ;	
         format 	  PCO0040014	best12. ;	
         format 	  PCO0040015	best12. ;	
         format 	  PCO0040016	best12. ;	
         format 	  PCO0040017	best12. ;	
         format 	  PCO0040018	best12. ;	
         format 	  PCO0040019	best12. ;	
         format 	  PCO0040020	best12. ;	
         format 	  PCO0040021	best12. ;	
         format 	  PCO0040022	best12. ;	
         format 	  PCO0040023	best12. ;	
         format 	  PCO0040024	best12. ;	
         format 	  PCO0040025	best12. ;	
         format 	  PCO0040026	best12. ;	
         format 	  PCO0040027	best12. ;	
         format 	  PCO0040028	best12. ;	
         format 	  PCO0040029	best12. ;	
         format 	  PCO0040030	best12. ;	
         format 	  PCO0040031	best12. ;	
         format 	  PCO0040032	best12. ;	
         format 	  PCO0040033	best12. ;	
         format 	  PCO0040034	best12. ;	
         format 	  PCO0040035	best12. ;	
         format 	  PCO0040036	best12. ;	
         format 	  PCO0040037	best12. ;	
         format 	  PCO0040038	best12. ;	
         format 	  PCO0040039	best12. ;	
         format 	  PCO0050001	best12. ;	
         format 	  PCO0050002	best12. ;	
         format 	  PCO0050003	best12. ;	
         format 	  PCO0050004	best12. ;	
         format 	  PCO0050005	best12. ;	
         format 	  PCO0050006	best12. ;	
         format 	  PCO0050007	best12. ;	
         format 	  PCO0050008	best12. ;	
         format 	  PCO0050009	best12. ;	
         format 	  PCO0050010	best12. ;	
         format 	  PCO0050011	best12. ;	
         format 	  PCO0050012	best12. ;	
         format 	  PCO0050013	best12. ;	
         format 	  PCO0050014	best12. ;	
         format 	  PCO0050015	best12. ;	
         format 	  PCO0050016	best12. ;	
         format 	  PCO0050017	best12. ;	
         format 	  PCO0050018	best12. ;	
         format 	  PCO0050019	best12. ;	
         format 	  PCO0050020	best12. ;	
         format 	  PCO0050021	best12. ;	
         format 	  PCO0050022	best12. ;	
         format 	  PCO0050023	best12. ;	
         format 	  PCO0050024	best12. ;	
         format 	  PCO0050025	best12. ;	
         format 	  PCO0050026	best12. ;	
         format 	  PCO0050027	best12. ;	
         format 	  PCO0050028	best12. ;	
         format 	  PCO0050029	best12. ;	
         format 	  PCO0050030	best12. ;	
         format 	  PCO0050031	best12. ;	
         format 	  PCO0050032	best12. ;	
         format 	  PCO0050033	best12. ;	
         format 	  PCO0050034	best12. ;	
         format 	  PCO0050035	best12. ;	
         format 	  PCO0050036	best12. ;	
         format 	  PCO0050037	best12. ;	
         format 	  PCO0050038	best12. ;	
         format 	  PCO0050039	best12. ;	
         format 	  PCO0060001	best12. ;	
         format 	  PCO0060002	best12. ;	
         format 	  PCO0060003	best12. ;	
         format 	  PCO0060004	best12. ;	
         format 	  PCO0060005	best12. ;	
         format 	  PCO0060006	best12. ;	
         format 	  PCO0060007	best12. ;	
         format 	  PCO0060008	best12. ;	
         format 	  PCO0060009	best12. ;	
         format 	  PCO0060010	best12. ;	
         format 	  PCO0060011	best12. ;	
         format 	  PCO0060012	best12. ;	
         format 	  PCO0060013	best12. ;	
         format 	  PCO0060014	best12. ;	
         format 	  PCO0060015	best12. ;	
         format 	  PCO0060016	best12. ;	
         format 	  PCO0060017	best12. ;	
         format 	  PCO0060018	best12. ;	
         format 	  PCO0060019	best12. ;	
         format 	  PCO0060020	best12. ;	
         format 	  PCO0060021	best12. ;	
         format 	  PCO0060022	best12. ;	
         format 	  PCO0060023	best12. ;	
         format 	  PCO0060024	best12. ;	
         format 	  PCO0060025	best12. ;	
         format 	  PCO0060026	best12. ;	
         format 	  PCO0060027	best12. ;	
         format 	  PCO0060028	best12. ;	
         format 	  PCO0060029	best12. ;	
         format 	  PCO0060030	best12. ;	
         format 	  PCO0060031	best12. ;	
         format 	  PCO0060032	best12. ;	
         format 	  PCO0060033	best12. ;	
         format 	  PCO0060034	best12. ;	
         format 	  PCO0060035	best12. ;	
         format 	  PCO0060036	best12. ;	
         format 	  PCO0060037	best12. ;	
         format 	  PCO0060038	best12. ;	
         format 	  PCO0060039	best12. ;	
         format 	  PCO0070001	best12. ;	
         format 	  PCO0070002	best12. ;	
         format 	  PCO0070003	best12. ;	
         format 	  PCO0070004	best12. ;	
         format 	  PCO0070005	best12. ;	
         format 	  PCO0070006	best12. ;	
         format 	  PCO0070007	best12. ;	
         format 	  PCO0070008	best12. ;	
         format 	  PCO0070009	best12. ;	
         format 	  PCO0070010	best12. ;	
         format 	  PCO0070011	best12. ;	
         format 	  PCO0070012	best12. ;	
         format 	  PCO0070013	best12. ;	
         format 	  PCO0070014	best12. ;	
         format 	  PCO0070015	best12. ;	
         format 	  PCO0070016	best12. ;	
         format 	  PCO0070017	best12. ;	
         format 	  PCO0070018	best12. ;	
         format 	  PCO0070019	best12. ;	
         format 	  PCO0070020	best12. ;	
         format 	  PCO0070021	best12. ;	
         format 	  PCO0070022	best12. ;	
         format 	  PCO0070023	best12. ;	
         format 	  PCO0070024	best12. ;	
         format 	  PCO0070025	best12. ;	
         format 	  PCO0070026	best12. ;	
         format 	  PCO0070027	best12. ;	
         format 	  PCO0070028	best12. ;	
         format 	  PCO0070029	best12. ;	
         format 	  PCO0070030	best12. ;	
         format 	  PCO0070031	best12. ;	
         format 	  PCO0070032	best12. ;	
         format 	  PCO0070033	best12. ;	
         format 	  PCO0070034	best12. ;	
         format 	  PCO0070035	best12. ;	
         format 	  PCO0070036	best12. ;	
         format 	  PCO0070037	best12. ;	
         format 	  PCO0070038	best12. ;	
         format 	  PCO0070039	best12. ;	
         format 	  PCO0080001	best12. ;	
         format 	  PCO0080002	best12. ;	
         format 	  PCO0080003	best12. ;	
         format 	  PCO0080004	best12. ;	
         format 	  PCO0080005	best12. ;	
         format 	  PCO0080006	best12. ;	
         format 	  PCO0080007	best12. ;	
         format 	  PCO0080008	best12. ;	
         format 	  PCO0080009	best12. ;	
         format 	  PCO0080010	best12. ;	
         format 	  PCO0080011	best12. ;	
         format 	  PCO0080012	best12. ;	
         format 	  PCO0080013	best12. ;	
         format 	  PCO0080014	best12. ;	
         format 	  PCO0080015	best12. ;	
         format 	  PCO0080016	best12. ;	
         format 	  PCO0080017	best12. ;	
         format 	  PCO0080018	best12. ;	
         format 	  PCO0080019	best12. ;	
         format 	  PCO0080020	best12. ;	
         format 	  PCO0080021	best12. ;	
         format 	  PCO0080022	best12. ;	
         format 	  PCO0080023	best12. ;	
         format 	  PCO0080024	best12. ;	
         format 	  PCO0080025	best12. ;	
         format 	  PCO0080026	best12. ;	
         format 	  PCO0080027	best12. ;	
         format 	  PCO0080028	best12. ;	
         format 	  PCO0080029	best12. ;	
         format 	  PCO0080030	best12. ;	
         format 	  PCO0080031	best12. ;	
         format 	  PCO0080032	best12. ;	
         format 	  PCO0080033	best12. ;	
         format 	  PCO0080034	best12. ;	
         format 	  PCO0080035	best12. ;	
         format 	  PCO0080036	best12. ;	
         format 	  PCO0080037	best12. ;	
         format 	  PCO0080038	best12. ;	
         format 	  PCO0080039	best12. ;	
         format 	  PCO0090001	best12. ;	
         format 	  PCO0090002	best12. ;	
         format 	  PCO0090003	best12. ;	
         format 	  PCO0090004	best12. ;	
         format 	  PCO0090005	best12. ;	
         format 	  PCO0090006	best12. ;	
         format 	  PCO0090007	best12. ;	
         format 	  PCO0090008	best12. ;	
         format 	  PCO0090009	best12. ;	
         format 	  PCO0090010	best12. ;	
         format 	  PCO0090011	best12. ;	
         format 	  PCO0090012	best12. ;	
         format 	  PCO0090013	best12. ;	
         format 	  PCO0090014	best12. ;	
         format 	  PCO0090015	best12. ;	
         format 	  PCO0090016	best12. ;	
         format 	  PCO0090017	best12. ;	
         format 	  PCO0090018	best12. ;	
         format 	  PCO0090019	best12. ;	
         format 	  PCO0090020	best12. ;	
         format 	  PCO0090021	best12. ;	
         format 	  PCO0090022	best12. ;	
         format 	  PCO0090023	best12. ;	
         format 	  PCO0090024	best12. ;	
         format 	  PCO0090025	best12. ;	
         format 	  PCO0090026	best12. ;	
         format 	  PCO0090027	best12. ;	
         format 	  PCO0090028	best12. ;	
         format 	  PCO0090029	best12. ;	
         format 	  PCO0090030	best12. ;	
         format 	  PCO0090031	best12. ;	
         format 	  PCO0090032	best12. ;	
         format 	  PCO0090033	best12. ;	
         format 	  PCO0090034	best12. ;	
         format 	  PCO0090035	best12. ;	
         format 	  PCO0090036	best12. ;	
         format 	  PCO0090037	best12. ;	
         format 	  PCO0090038	best12. ;	
         format 	  PCO0090039	best12. ;	
         format 	  PCO0100001	best12. ;	
         format 	  PCO0100002	best12. ;	
         format 	  PCO0100003	best12. ;	
         format 	  PCO0100004	best12. ;	
         format 	  PCO0100005	best12. ;	
         format 	  PCO0100006	best12. ;	
         format 	  PCO0100007	best12. ;	
         format 	  PCO0100008	best12. ;	
         format 	  PCO0100009	best12. ;	
         format 	  PCO0100010	best12. ;	
         format 	  PCO0100011	best12. ;	
         format 	  PCO0100012	best12. ;	
         format 	  PCO0100013	best12. ;	
         format 	  PCO0100014	best12. ;	
         format 	  PCO0100015	best12. ;	
         format 	  PCO0100016	best12. ;	
         format 	  PCO0100017	best12. ;	
         format 	  PCO0100018	best12. ;	
         format 	  PCO0100019	best12. ;	
         format 	  PCO0100020	best12. ;	
         format 	  PCO0100021	best12. ;	
         format 	  PCO0100022	best12. ;	
         format 	  PCO0100023	best12. ;	
         format 	  PCO0100024	best12. ;	
         format 	  PCO0100025	best12. ;	
         format 	  PCO0100026	best12. ;	
         format 	  PCO0100027	best12. ;	
         format 	  PCO0100028	best12. ;	
         format 	  PCO0100029	best12. ;	
         format 	  PCO0100030	best12. ;	
         format 	  PCO0100031	best12. ;	
         format 	  PCO0100032	best12. ;	
         format 	  PCO0100033	best12. ;	
         format 	  PCO0100034	best12. ;	
         format 	  PCO0100035	best12. ;	
         format 	  PCO0100036	best12. ;	
         format 	  PCO0100037	best12. ;	
         format 	  PCO0100038	best12. ;	
         format 	  PCO0100039	best12. ;	
         format 	  H00010001 	best12. ;	
         format 	  H0020001 	best12. ;	
         format 	  H0020002 	best12. ;	
         format 	  H0020003 	best12. ;	
         format 	  H0020004 	best12. ;	
         format 	  H0020005 	best12. ;	
         format 	  H0020006 	best12. ;	
         format 	  H0030001 	best12. ;	
         format 	  H0030002 	best12. ;	
         format 	  H0030003 	best12. ;	
         format 	  H0040001 	best12. ;	
         format 	  H0040002 	best12. ;	
         format 	  H0040003 	best12. ;	
         format 	  H0040004 	best12. ;	
         format 	  H0050001 	best12. ;	
         format 	  H0050002 	best12. ;	
         format 	  H0050003 	best12. ;	
         format 	  H0050004 	best12. ;	
         format 	  H0050005 	best12. ;	
         format 	  H0050006 	best12. ;	
         format 	  H0050007 	best12. ;	
         format 	  H0050008 	best12. ;	
         format 	  H0060001 	best12. ;	
         format 	  H0060002 	best12. ;	
         format 	  H0060003 	best12. ;	
         format 	  H0060004 	best12. ;	
         format 	  H0060005 	best12. ;	
         format 	  H0060006 	best12. ;	
         format 	  H0060007 	best12. ;	
         format 	  H0060008 	best12. ;	
         format 	  H0070001 	best12. ;	
         format 	  H0070002 	best12. ;	
         format 	  H0070003 	best12. ;	
         format 	  H0070004 	best12. ;	
         format 	  H0070005 	best12. ;	
         format 	  H0070006 	best12. ;	
         format 	  H0070007 	best12. ;	
         format 	  H0070008 	best12. ;	
         format 	  H0070009 	best12. ;	
         format 	  H0070010 	best12. ;	
         format 	  H0070011 	best12. ;	
         format 	  H0070012 	best12. ;	
         format 	  H0070013 	best12. ;	
         format 	  H0070014 	best12. ;	
         format 	  H0070015 	best12. ;	
         format 	  H0070016 	best12. ;	
         format 	  H0070017 	best12. ;	
         format 	  H0080001 	best12. ;	
         format 	  H0080002 	best12. ;	
         format 	  H0080003 	best12. ;	
         format 	  H0080004 	best12. ;	
         format 	  H0080005 	best12. ;	
         format 	  H0080006 	best12. ;	
         format 	  H0080007 	best12. ;	
         format 	  H0090001 	best12. ;	
         format 	  H0090002 	best12. ;	
         format 	  H0090003 	best12. ;	
         format 	  H0090004 	best12. ;	
         format 	  H0090005 	best12. ;	
         format 	  H0090006 	best12. ;	
         format 	  H0090007 	best12. ;	
         format 	  H0090008 	best12. ;	
         format 	  H0090009 	best12. ;	
         format 	  H0090010 	best12. ;	
         format 	  H0090011 	best12. ;	
         format 	  H0090012 	best12. ;	
         format 	  H0090013 	best12. ;	
         format 	  H0090014 	best12. ;	
         format 	  H0090015 	best12. ;	
         format 	  H0100001 	best12. ;	
         format 	  H0110001 	best12. ;	
         format 	  H0110002 	best12. ;	
         format 	  H0110003 	best12. ;	
         format 	  H0110004 	best12. ;	
         format 	  H0120001 	best12. ;	
         format 	  H0120002 	best12. ;	
         format 	  H0120003 	best12. ;	
         format 	  H0130001 	best12. ;	
         format 	  H0130002 	best12. ;	
         format 	  H0130003 	best12. ;	
         format 	  H0130004 	best12. ;	
         format 	  H0130005 	best12. ;	
         format 	  H0130006 	best12. ;	
         format 	  H0130007 	best12. ;	
         format 	  H0130008 	best12. ;	
         format 	  H0140001 	best12. ;	
         format 	  H0140002 	best12. ;	
         format 	  H0140003 	best12. ;	
         format 	  H0140004 	best12. ;	
         format 	  H0140005 	best12. ;	
         format 	  H0140006 	best12. ;	
         format 	  H0140007 	best12. ;	
         format 	  H0140008 	best12. ;	
         format 	  H0140009 	best12. ;	
         format 	  H0140010 	best12. ;	
         format 	  H0140011 	best12. ;	
         format 	  H0140012 	best12. ;	
         format 	  H0140013 	best12. ;	
         format 	  H0140014 	best12. ;	
         format 	  H0140015 	best12. ;	
         format 	  H0140016 	best12. ;	
         format 	  H0140017 	best12. ;	
         format 	  H0150001 	best12. ;	
         format 	  H0150002 	best12. ;	
         format 	  H0150003 	best12. ;	
         format 	  H0150004 	best12. ;	
         format 	  H0150005 	best12. ;	
         format 	  H0150006 	best12. ;	
         format 	  H0150007 	best12. ;	
         format 	  H0160001 	best12. ;	
         format 	  H0160002 	best12. ;	
         format 	  H0160003 	best12. ;	
         format 	  H0160004 	best12. ;	
         format 	  H0160005 	best12. ;	
         format 	  H0160006 	best12. ;	
         format 	  H0160007 	best12. ;	
         format 	  H0160008 	best12. ;	
         format 	  H0160009 	best12. ;	
         format 	  H0160010 	best12. ;	
         format 	  H0160011 	best12. ;	
         format 	  H0160012 	best12. ;	
         format 	  H0160013 	best12. ;	
         format 	  H0160014 	best12. ;	
         format 	  H0160015 	best12. ;	
         format 	  H0160016 	best12. ;	
         format 	  H0160017 	best12. ;	
         format 	  H0170001 	best12. ;	
         format 	  H0170002 	best12. ;	
         format 	  H0170003 	best12. ;	
         format 	  H0170004 	best12. ;	
         format 	  H0170005 	best12. ;	
         format 	  H0170006 	best12. ;	
         format 	  H0170007 	best12. ;	
         format 	  H0170008 	best12. ;	
         format 	  H0170009 	best12. ;	
         format 	  H0170010 	best12. ;	
         format 	  H0170011 	best12. ;	
         format 	  H0170012 	best12. ;	
         format 	  H0170013 	best12. ;	
         format 	  H0170014 	best12. ;	
         format 	  H0170015 	best12. ;	
         format 	  H0170016 	best12. ;	
         format 	  H0170017 	best12. ;	
         format 	  H0170018 	best12. ;	
         format 	  H0170019 	best12. ;	
         format 	  H0170020 	best12. ;	
         format 	  H0170021 	best12. ;	
         format 	  H0180001 	best12. ;	
         format 	  H0180002 	best12. ;	
         format 	  H0180003 	best12. ;	
         format 	  H0180004 	best12. ;	
         format 	  H0180005 	best12. ;	
         format 	  H0180006 	best12. ;	
         format 	  H0180007 	best12. ;	
         format 	  H0180008 	best12. ;	
         format 	  H0180009 	best12. ;	
         format 	  H0180010 	best12. ;	
         format 	  H0180011 	best12. ;	
         format 	  H0180012 	best12. ;	
         format 	  H0180013 	best12. ;	
         format 	  H0180014 	best12. ;	
         format 	  H0180015 	best12. ;	
         format 	  H0180016 	best12. ;	
         format 	  H0180017 	best12. ;	
         format 	  H0180018 	best12. ;	
         format 	  H0180019 	best12. ;	
         format 	  H0180020 	best12. ;	
         format 	  H0180021 	best12. ;	
         format 	  H0180022 	best12. ;	
         format 	  H0180023 	best12. ;	
         format 	  H0180024 	best12. ;	
         format 	  H0180025 	best12. ;	
         format 	  H0180026 	best12. ;	
         format 	  H0180027 	best12. ;	
         format 	  H0180028 	best12. ;	
         format 	  H0180029 	best12. ;	
         format 	  H0180030 	best12. ;	
         format 	  H0180031 	best12. ;	
         format 	  H0180032 	best12. ;	
         format 	  H0180033 	best12. ;	
         format 	  H0180034 	best12. ;	
         format 	  H0180035 	best12. ;	
         format 	  H0180036 	best12. ;	
         format 	  H0180037 	best12. ;	
         format 	  H0180038 	best12. ;	
         format 	  H0180039 	best12. ;	
         format 	  H0180040 	best12. ;	
         format 	  H0180041 	best12. ;	
         format 	  H0180042 	best12. ;	
         format 	  H0180043 	best12. ;	
         format 	  H0180044 	best12. ;	
         format 	  H0180045 	best12. ;	
         format 	  H0180046 	best12. ;	
         format 	  H0180047 	best12. ;	
         format 	  H0180048 	best12. ;	
         format 	  H0180049 	best12. ;	
         format 	  H0180050 	best12. ;	
         format 	  H0180051 	best12. ;	
         format 	  H0180052 	best12. ;	
         format 	  H0180053 	best12. ;	
         format 	  H0180054 	best12. ;	
         format 	  H0180055 	best12. ;	
         format 	  H0180056 	best12. ;	
         format 	  H0180057 	best12. ;	
         format 	  H0180058 	best12. ;	
         format 	  H0180059 	best12. ;	
         format 	  H0180060 	best12. ;	
         format 	  H0180061 	best12. ;	
         format 	  H0180062 	best12. ;	
         format 	  H0180063 	best12. ;	
         format 	  H0180064 	best12. ;	
         format 	  H0180065 	best12. ;	
         format 	  H0180066 	best12. ;	
         format 	  H0180067 	best12. ;	
         format 	  H0180068 	best12. ;	
         format 	  H0180069 	best12. ;	
         format 	  H0190001 	best12. ;	
         format 	  H0190002 	best12. ;	
         format 	  H0190003 	best12. ;	
         format 	  H0190004 	best12. ;	
         format 	  H0190005 	best12. ;	
         format 	  H0190006 	best12. ;	
         format 	  H0190007 	best12. ;	
         format 	  H0200001 	best12. ;	
         format 	  H0200002 	best12. ;	
         format 	  H0200003 	best12. ;	
         format 	  H0210001 	best12. ;	
         format 	  H0210002 	best12. ;	
         format 	  H0210003 	best12. ;	
         format 	  H0220001 	best12. ;	
         format 	  H0220002 	best12. ;	
         format 	  H0220003 	best12. ;	
         format 	  H011A0001 	best12. ;	
         format 	  H011A0002 	best12. ;	
         format 	  H011A0003 	best12. ;	
         format 	  H011A0004 	best12. ;	
         format 	  H011B0001 	best12. ;	
         format 	  H011B0002 	best12. ;	
         format 	  H011B0003 	best12. ;	
         format 	  H011B0004 	best12. ;	
         format 	  H011C0001 	best12. ;	
         format 	  H011C0002 	best12. ;	
         format 	  H011C0003 	best12. ;	
         format 	  H011C0004 	best12. ;	
         format 	  H011D0001 	best12. ;	
         format 	  H011D0002 	best12. ;	
         format 	  H011D0003 	best12. ;	
         format 	  H011D0004 	best12. ;	
         format 	  H011E0001 	best12. ;	
         format 	  H011E0002 	best12. ;	
         format 	  H011E0003 	best12. ;	
         format 	  H011E0004 	best12. ;	
         format 	  H011F0001 	best12. ;	
         format 	  H011F0002 	best12. ;	
         format 	  H011F0003 	best12. ;	
         format 	  H011F0004 	best12. ;	
         format 	  H011G0001 	best12. ;	
         format 	  H011G0002 	best12. ;	
         format 	  H011G0003 	best12. ;	
         format 	  H011G0004 	best12. ;	
         format 	  H011H0001 	best12. ;	
         format 	  H011H0002 	best12. ;	
         format 	  H011H0003 	best12. ;	
         format 	  H011H0004 	best12. ;	
         format 	  H011I0001 	best12. ;	
         format 	  H011I0002 	best12. ;	
         format 	  H011I0003 	best12. ;	
         format 	  H011I0004 	best12. ;	
         format 	  H012A0001 	best12. ;	
         format 	  H012A0002 	best12. ;	
         format 	  H012A0003 	best12. ;	
         format 	  H012B0001 	best12. ;	
         format 	  H012B0002 	best12. ;	
         format 	  H012B0003 	best12. ;	
         format 	  H012C0001 	best12. ;	
         format 	  H012C0002 	best12. ;	
         format 	  H012C0003 	best12. ;	
         format 	  H012D0001 	best12. ;	
         format 	  H012D0002 	best12. ;	
         format 	  H012D0003 	best12. ;	
         format 	  H012E0001 	best12. ;	
         format 	  H012E0002 	best12. ;	
         format 	  H012E0003 	best12. ;	
         format 	  H012F0001 	best12. ;	
         format 	  H012F0002 	best12. ;	
         format 	  H012F0003 	best12. ;	
         format 	  H012G0001 	best12. ;	
         format 	  H012G0002 	best12. ;	
         format 	  H012G0003 	best12. ;	
         format 	  H012H0001 	best12. ;	
         format 	  H012H0002 	best12. ;	
         format 	  H012H0003 	best12. ;	
         format 	  H012I0001 	best12. ;	
         format 	  H012I0002 	best12. ;	
         format 	  H012I0003 	best12. ;	
         format 	  H016A0001 	best12. ;	
         format 	  H016A0002 	best12. ;	
         format 	  H016A0003 	best12. ;	
         format 	  H016A0004 	best12. ;	
         format 	  H016A0005 	best12. ;	
         format 	  H016A0006 	best12. ;	
         format 	  H016A0007 	best12. ;	
         format 	  H016A0008 	best12. ;	
         format 	  H016A0009 	best12. ;	
         format 	  H016A0010 	best12. ;	
         format 	  H016A0011 	best12. ;	
         format 	  H016A0012 	best12. ;	
         format 	  H016A0013 	best12. ;	
         format 	  H016A0014 	best12. ;	
         format 	  H016A0015 	best12. ;	
         format 	  H016A0016 	best12. ;	
         format 	  H016A0017 	best12. ;	
         format 	  H016B0001 	best12. ;	
         format 	  H016B0002 	best12. ;	
         format 	  H016B0003 	best12. ;	
         format 	  H016B0004 	best12. ;	
         format 	  H016B0005 	best12. ;	
         format 	  H016B0006 	best12. ;	
         format 	  H016B0007 	best12. ;	
         format 	  H016B0008 	best12. ;	
         format 	  H016B0009 	best12. ;	
         format 	  H016B0010 	best12. ;	
         format 	  H016B0011 	best12. ;	
         format 	  H016B0012 	best12. ;	
         format 	  H016B0013 	best12. ;	
         format 	  H016B0014 	best12. ;	
         format 	  H016B0015 	best12. ;	
         format 	  H016B0016 	best12. ;	
         format 	  H016B0017 	best12. ;	
         format 	  H016C0001 	best12. ;	
         format 	  H016C0002 	best12. ;	
         format 	  H016C0003 	best12. ;	
         format 	  H016C0004 	best12. ;	
         format 	  H016C0005 	best12. ;	
         format 	  H016C0006 	best12. ;	
         format 	  H016C0007 	best12. ;	
         format 	  H016C0008 	best12. ;	
         format 	  H016C0009 	best12. ;	
         format 	  H016C0010 	best12. ;	
         format 	  H016C0011 	best12. ;	
         format 	  H016C0012 	best12. ;	
         format 	  H016C0013 	best12. ;	
         format 	  H016C0014 	best12. ;	
         format 	  H016C0015 	best12. ;	
         format 	  H016C0016 	best12. ;	
         format 	  H016C0017 	best12. ;	
         format 	  H016D0001 	best12. ;	
         format 	  H016D0002 	best12. ;	
         format 	  H016D0003 	best12. ;	
         format 	  H016D0004 	best12. ;	
         format 	  H016D0005 	best12. ;	
         format 	  H016D0006 	best12. ;	
         format 	  H016D0007 	best12. ;	
         format 	  H016D0008 	best12. ;	
         format 	  H016D0009 	best12. ;	
         format 	  H016D0010 	best12. ;	
         format 	  H016D0011 	best12. ;	
         format 	  H016D0012 	best12. ;	
         format 	  H016D0013 	best12. ;	
         format 	  H016D0014 	best12. ;	
         format 	  H016D0015 	best12. ;	
         format 	  H016D0016 	best12. ;	
         format 	  H016D0017 	best12. ;	
         format 	  H016E0001 	best12. ;	
         format 	  H016E0002 	best12. ;	
         format 	  H016E0003 	best12. ;	
         format 	  H016E0004 	best12. ;	
         format 	  H016E0005 	best12. ;	
         format 	  H016E0006 	best12. ;	
         format 	  H016E0007 	best12. ;	
         format 	  H016E0008 	best12. ;	
         format 	  H016E0009 	best12. ;	
         format 	  H016E0010 	best12. ;	
         format 	  H016E0011 	best12. ;	
         format 	  H016E0012 	best12. ;	
         format 	  H016E0013 	best12. ;	
         format 	  H016E0014 	best12. ;	
         format 	  H016E0015 	best12. ;	
         format 	  H016E0016 	best12. ;	
         format 	  H016E0017 	best12. ;	
         format 	  H016F0001 	best12. ;	
         format 	  H016F0002 	best12. ;	
         format 	  H016F0003 	best12. ;	
         format 	  H016F0004 	best12. ;	
         format 	  H016F0005 	best12. ;	
         format 	  H016F0006 	best12. ;	
         format 	  H016F0007 	best12. ;	
         format 	  H016F0008 	best12. ;	
         format 	  H016F0009 	best12. ;	
         format 	  H016F0010 	best12. ;	
         format 	  H016F0011 	best12. ;	
         format 	  H016F0012 	best12. ;	
         format 	  H016F0013 	best12. ;	
         format 	  H016F0014 	best12. ;	
         format 	  H016F0015 	best12. ;	
         format 	  H016F0016 	best12. ;	
         format 	  H016F0017 	best12. ;	
         format 	  H016G0001 	best12. ;	
         format 	  H016G0002 	best12. ;	
         format 	  H016G0003 	best12. ;	
         format 	  H016G0004 	best12. ;	
         format 	  H016G0005 	best12. ;	
         format 	  H016G0006 	best12. ;	
         format 	  H016G0007 	best12. ;	
         format 	  H016G0008 	best12. ;	
         format 	  H016G0009 	best12. ;	
         format 	  H016G0010 	best12. ;	
         format 	  H016G0011 	best12. ;	
         format 	  H016G0012 	best12. ;	
         format 	  H016G0013 	best12. ;	
         format 	  H016G0014 	best12. ;	
         format 	  H016G0015 	best12. ;	
         format 	  H016G0016 	best12. ;	
         format 	  H016G0017 	best12. ;	
         format 	  H016H0001 	best12. ;	
         format 	  H016H0002 	best12. ;	
         format 	  H016H0003 	best12. ;	
         format 	  H016H0004 	best12. ;	
         format 	  H016H0005 	best12. ;	
         format 	  H016H0006 	best12. ;	
         format 	  H016H0007 	best12. ;	
         format 	  H016H0008 	best12. ;	
         format 	  H016H0009 	best12. ;	
         format 	  H016H0010 	best12. ;	
         format 	  H016H0011 	best12. ;	
         format 	  H016H0012 	best12. ;	
         format 	  H016H0013 	best12. ;	
         format 	  H016H0014 	best12. ;	
         format 	  H016H0015 	best12. ;	
         format 	  H016H0016 	best12. ;	
         format 	  H016H0017 	best12. ;	
         format 	  H016I0001 	best12. ;	
         format 	  H016I0002 	best12. ;	
         format 	  H016I0003 	best12. ;	
         format 	  H016I0004 	best12. ;	
         format 	  H016I0005 	best12. ;	
         format 	  H016I0006 	best12. ;	
         format 	  H016I0007 	best12. ;	
         format 	  H016I0008 	best12. ;	
         format 	  H016I0009 	best12. ;	
         format 	  H016I0010 	best12. ;	
         format 	  H016I0011 	best12. ;	
         format 	  H016I0012 	best12. ;	
         format 	  H016I0013 	best12. ;	
         format 	  H016I0014 	best12. ;	
         format 	  H016I0015 	best12. ;	
         format 	  H016I0016 	best12. ;	
         format 	  H016I0017 	best12. ;	
         format 	  H017A0001 	best12. ;	
         format 	  H017A0002 	best12. ;	
         format 	  H017A0003 	best12. ;	
         format 	  H017A0004 	best12. ;	
         format 	  H017A0005 	best12. ;	
         format 	  H017A0006 	best12. ;	
         format 	  H017A0007 	best12. ;	
         format 	  H017A0008 	best12. ;	
         format 	  H017A0009 	best12. ;	
         format 	  H017A0010 	best12. ;	
         format 	  H017A0011 	best12. ;	
         format 	  H017A0012 	best12. ;	
         format 	  H017A0013 	best12. ;	
         format 	  H017A0014 	best12. ;	
         format 	  H017A0015 	best12. ;	
         format 	  H017A0016 	best12. ;	
         format 	  H017A0017 	best12. ;	
         format 	  H017A0018 	best12. ;	
         format 	  H017A0019 	best12. ;	
         format 	  H017A0020 	best12. ;	
         format 	  H017A0021 	best12. ;	
         format 	  H017B0001 	best12. ;	
         format 	  H017B0002 	best12. ;	
         format 	  H017B0003 	best12. ;	
         format 	  H017B0004 	best12. ;	
         format 	  H017B0005 	best12. ;	
         format 	  H017B0006 	best12. ;	
         format 	  H017B0007 	best12. ;	
         format 	  H017B0008 	best12. ;	
         format 	  H017B0009 	best12. ;	
         format 	  H017B0010 	best12. ;	
         format 	  H017B0011 	best12. ;	
         format 	  H017B0012 	best12. ;	
         format 	  H017B0013 	best12. ;	
         format 	  H017B0014 	best12. ;	
         format 	  H017B0015 	best12. ;	
         format 	  H017B0016 	best12. ;	
         format 	  H017B0017 	best12. ;	
         format 	  H017B0018 	best12. ;	
         format 	  H017B0019 	best12. ;	
         format 	  H017B0020 	best12. ;	
         format 	  H017B0021 	best12. ;	
         format 	  H017C0001 	best12. ;	
         format 	  H017C0002 	best12. ;	
         format 	  H017C0003 	best12. ;	
         format 	  H017C0004 	best12. ;	
         format 	  H017C0005 	best12. ;	
         format 	  H017C0006 	best12. ;	
         format 	  H017C0007 	best12. ;	
         format 	  H017C0008 	best12. ;	
         format 	  H017C0009 	best12. ;	
         format 	  H017C0010 	best12. ;	
         format 	  H017C0011 	best12. ;	
         format 	  H017C0012 	best12. ;	
         format 	  H017C0013 	best12. ;	
         format 	  H017C0014 	best12. ;	
         format 	  H017C0015 	best12. ;	
         format 	  H017C0016 	best12. ;	
         format 	  H017C0017 	best12. ;	
         format 	  H017C0018 	best12. ;	
         format 	  H017C0019 	best12. ;	
         format 	  H017C0020 	best12. ;	
         format 	  H017C0021 	best12. ;	
         format 	  H017D0001 	best12. ;	
         format 	  H017D0002 	best12. ;	
         format 	  H017D0003 	best12. ;	
         format 	  H017D0004 	best12. ;	
         format 	  H017D0005 	best12. ;	
         format 	  H017D0006 	best12. ;	
         format 	  H017D0007 	best12. ;	
         format 	  H017D0008 	best12. ;	
         format 	  H017D0009 	best12. ;	
         format 	  H017D0010 	best12. ;	
         format 	  H017D0011 	best12. ;	
         format 	  H017D0012 	best12. ;	
         format 	  H017D0013 	best12. ;	
         format 	  H017D0014 	best12. ;	
         format 	  H017D0015 	best12. ;	
         format 	  H017D0016 	best12. ;	
         format 	  H017D0017 	best12. ;	
         format 	  H017D0018 	best12. ;	
         format 	  H017D0019 	best12. ;	
         format 	  H017D0020 	best12. ;	
         format 	  H017D0021 	best12. ;	
         format 	  H017E0001 	best12. ;	
         format 	  H017E0002 	best12. ;	
         format 	  H017E0003 	best12. ;	
         format 	  H017E0004 	best12. ;	
         format 	  H017E0005 	best12. ;	
         format 	  H017E0006 	best12. ;	
         format 	  H017E0007 	best12. ;	
         format 	  H017E0008 	best12. ;	
         format 	  H017E0009 	best12. ;	
         format 	  H017E0010 	best12. ;	
         format 	  H017E0011 	best12. ;	
         format 	  H017E0012 	best12. ;	
         format 	  H017E0013 	best12. ;	
         format 	  H017E0014 	best12. ;	
         format 	  H017E0015 	best12. ;	
         format 	  H017E0016 	best12. ;	
         format 	  H017E0017 	best12. ;	
         format 	  H017E0018 	best12. ;	
         format 	  H017E0019 	best12. ;	
         format 	  H017E0020 	best12. ;	
         format 	  H017E0021 	best12. ;	
         format 	  H017F0001 	best12. ;	
         format 	  H017F0002 	best12. ;	
         format 	  H017F0003 	best12. ;	
         format 	  H017F0004 	best12. ;	
         format 	  H017F0005 	best12. ;	
         format 	  H017F0006 	best12. ;	
         format 	  H017F0007 	best12. ;	
         format 	  H017F0008 	best12. ;	
         format 	  H017F0009 	best12. ;	
         format 	  H017F0010 	best12. ;	
         format 	  H017F0011 	best12. ;	
         format 	  H017F0012 	best12. ;	
         format 	  H017F0013 	best12. ;	
         format 	  H017F0014 	best12. ;	
         format 	  H017F0015 	best12. ;	
         format 	  H017F0016 	best12. ;	
         format 	  H017F0017 	best12. ;	
         format 	  H017F0018 	best12. ;	
         format 	  H017F0019 	best12. ;	
         format 	  H017F0020 	best12. ;	
         format 	  H017F0021 	best12. ;	
         format 	  H017G0001 	best12. ;	
         format 	  H017G0002 	best12. ;	
         format 	  H017G0003 	best12. ;	
         format 	  H017G0004 	best12. ;	
         format 	  H017G0005 	best12. ;	
         format 	  H017G0006 	best12. ;	
         format 	  H017G0007 	best12. ;	
         format 	  H017G0008 	best12. ;	
         format 	  H017G0009 	best12. ;	
         format 	  H017G0010 	best12. ;	
         format 	  H017G0011 	best12. ;	
         format 	  H017G0012 	best12. ;	
         format 	  H017G0013 	best12. ;	
         format 	  H017G0014 	best12. ;	
         format 	  H017G0015 	best12. ;	
         format 	  H017G0016 	best12. ;	
         format 	  H017G0017 	best12. ;	
         format 	  H017G0018 	best12. ;	
         format 	  H017G0019 	best12. ;	
         format 	  H017G0020 	best12. ;	
         format 	  H017G0021 	best12. ;	
         format 	  H017H0001 	best12. ;	
         format 	  H017H0002 	best12. ;	
         format 	  H017H0003 	best12. ;	
         format 	  H017H0004 	best12. ;	
         format 	  H017H0005 	best12. ;	
         format 	  H017H0006 	best12. ;	
         format 	  H017H0007 	best12. ;	
         format 	  H017H0008 	best12. ;	
         format 	  H017H0009 	best12. ;	
         format 	  H017H0010 	best12. ;	
         format 	  H017H0011 	best12. ;	
         format 	  H017H0012 	best12. ;	
         format 	  H017H0013 	best12. ;	
         format 	  H017H0014 	best12. ;	
         format 	  H017H0015 	best12. ;	
         format 	  H017H0016 	best12. ;	
         format 	  H017H0017 	best12. ;	
         format 	  H017H0018 	best12. ;	
         format 	  H017H0019 	best12. ;	
         format 	  H017H0020 	best12. ;	
         format 	  H017H0021 	best12. ;	
         format 	  H017I0001 	best12. ;	
         format 	  H017I0002 	best12. ;	
         format 	  H017I0003 	best12. ;	
         format 	  H017I0004 	best12. ;	
         format 	  H017I0005 	best12. ;	
         format 	  H017I0006 	best12. ;	
         format 	  H017I0007 	best12. ;	
         format 	  H017I0008 	best12. ;	
         format 	  H017I0009 	best12. ;	
         format 	  H017I0010 	best12. ;	
         format 	  H017I0011 	best12. ;	
         format 	  H017I0012 	best12. ;	
         format 	  H017I0013 	best12. ;	
         format 	  H017I0014 	best12. ;	
         format 	  H017I0015 	best12. ;	
         format 	  H017I0016 	best12. ;	
         format 	  H017I0017 	best12. ;	
         format 	  H017I0018 	best12. ;	
         format 	  H017I0019 	best12. ;	
         format 	  H017I0020 	best12. ;	
         format 	  H017I0021 	best12. ;	
         format 	  HCT0010001	best12. ;	
         format 	  HCT0010002	best12. ;	
         format 	  HCT0010003	best12. ;	
         format 	  HCT0010004	best12. ;	
         format 	  HCT0010005	best12. ;	
         format 	  HCT0010006	best12. ;	
         format 	  HCT0010007	best12. ;	
         format 	  HCT0010008	best12. ;	
         format 	  HCT0010009	best12. ;	
         format 	  HCT0010010	best12. ;	
         format 	  HCT0010011	best12. ;	
         format 	  HCT0010012	best12. ;	
         format 	  HCT0010013	best12. ;	
         format 	  HCT0010014	best12. ;	
         format 	  HCT0010015	best12. ;	
         format 	  HCT0010016	best12. ;	
         format 	  HCT0010017	best12. ;	
         format 	  HCT0010018	best12. ;	
         format 	  HCT0010019	best12. ;	
         format 	  HCT0010020	best12. ;	
         format 	  HCT0010021	best12. ;	
         format 	  HCT0010022	best12. ;	
         format 	  HCT0010023	best12. ;	
         format 	  HCT0010024	best12. ;	
         format 	  HCT0010025	best12. ;	
         format 	  HCT0010026	best12. ;	
         format 	  HCT0010027	best12. ;	
         format 	  HCT0010028	best12. ;	
         format 	  HCT0010029	best12. ;	
         format 	  HCT0010030	best12. ;	
         format 	  HCT0010031	best12. ;	
         format 	  HCT0010032	best12. ;	
         format 	  HCT0010033	best12. ;	
         format 	  HCT0010034	best12. ;	
         format 	  HCT0010035	best12. ;	
         format 	  HCT0020001	best12. ;	
         format 	  HCT0020002	best12. ;	
         format 	  HCT0020003	best12. ;	
         format 	  HCT0020004	best12. ;	
         format 	  HCT0020005	best12. ;	
         format 	  HCT0020006	best12. ;	
         format 	  HCT0020007	best12. ;	
         format 	  HCT0020008	best12. ;	
         format 	  HCT0020009	best12. ;	
         format 	  HCT0020010	best12. ;	
         format 	  HCT0020011	best12. ;	
         format 	  HCT0020012	best12. ;	
         format 	  HCT0020013	best12. ;	
         format 	  HCT0030001	best12. ;	
         format 	  HCT0030002	best12. ;	
         format 	  HCT0030003	best12. ;	
         format 	  HCT0030004	best12. ;	
         format 	  HCT0030005	best12. ;	
         format 	  HCT0030006	best12. ;	
         format 	  HCT0030007	best12. ;	
         format 	  HCT0030008	best12. ;	
         format 	  HCT0030009	best12. ;	
         format 	  HCT0030010	best12. ;	
         format 	  HCT0030011	best12. ;	
         format 	  HCT0030012	best12. ;	
         format 	  HCT0030013	best12. ;	
         format 	  HCT0040001	best12. ;	
         format 	  HCT0040002	best12. ;	
         format 	  HCT0040003	best12. ;	
         format 	  HCT0040004	best12. ;	
         format 	  HCT0040005	best12. ;	
         format 	  HCT0040006	best12. ;	
         format 	  HCT0040007	best12. ;	
         format 	  HCT0040008	best12. ;	
         format 	  HCT0040009	best12. ;	
         format 	  HCT0040010	best12. ;	
         format 	  HCT0040011	best12. ;	
         format 	  HCT0040012	best12. ;	
         format 	  HCT0040013	best12. ;	
         format 	  PCT0230001	best12. ;	
         format 	  PCT0230002	best12. ;	
         format 	  PCT0230003	best12. ;	
         format 	  PCT0230004	best12. ;	
         format 	  PCT0230005	best12. ;	
         format 	  PCT0230006	best12. ;	
         format 	  PCT0230007	best12. ;	
         format 	  PCT0230008	best12. ;	
         format 	  PCT0230009	best12. ;	
         format 	  PCT0230010	best12. ;	
         format 	  PCT0230011	best12. ;	
         format 	  PCT0230012	best12. ;	
         format 	  PCT0230013	best12. ;	
         format 	  PCT0230014	best12. ;	
         format 	  PCT0230015	best12. ;	
         format 	  PCT0230016	best12. ;	
         format 	  PCT0230017	best12. ;	
         format 	  PCT0230018	best12. ;	
         format 	  PCT0230019	best12. ;	
         format 	  PCT0230020	best12. ;	
         format 	  PCT0230021	best12. ;	
         format 	  PCT0230022	best12. ;	
         format 	  PCT0230023	best12. ;	
         format 	  PCT0230024	best12. ;	
         format 	  PCT0240001	best12. ;	
         format 	  PCT0240002	best12. ;	
         format 	  PCT0240003	best12. ;	
         format 	  PCT0240004	best12. ;	
         format 	  PCT0240005	best12. ;	
         format 	  PCT0240006	best12. ;	
         format 	  PCT0240007	best12. ;	
         format 	  PCT0240008	best12. ;	
         format 	  PCT0240009	best12. ;	
         format 	  PCT0240010	best12. ;	
         format 	  PCT0240011	best12. ;	
         format 	  PCT0240012	best12. ;	
         format 	  PCT0240013	best12. ;	
         format 	  PCT0240014	best12. ;	
         format 	  PCT0240015	best12. ;	
         format 	  PCT0240016	best12. ;	
         format 	  PCT0240017	best12. ;	
         format 	  PCT0240018	best12. ;	
         format 	  PCT0240019	best12. ;	
         format 	  PCT0240020	best12. ;	
         format 	  PCT0240021	best12. ;	
         format 	  PCT0240022	best12. ;	
         format 	  PCT0240023	best12. ;	
      input			
                  FILEID $			
                  STUSAB $			
                  SUMLEV $			
                  GEOCOMP $			
                  CHARITER $			
                  CIFSN	$		
                  LOGRECNO			
                  REGION $			
                  DIVISION $			
                  STATE $			
                  COUNTY $			
                  COUNTYCC $			
                  COUNTYSC $			
                  COUSUB $			
                  COUSUBCC $			
                  COUSUBSC $			
                  PLACE $			
                  PLACECC $			
                  PLACESC $			
                  TRACT $			
                  BLKGRP $			
                  BLOCK $			
                  IUC $			
                  CONCIT $			
                  CONCITCC $			
                  CONCITSC $			
                  AIANHH $			
                  AIANHHFP $			
                  AIANHHCC $			
                  AIHHTLI $			
                  AITSCE $			
                  AITS $			
                  AITSCC $			
                  TTRACT $			
                  TBLKGRP $			
                  ANRC $			
                  ANRCCC $			
                  CBSA $			
                  CBSASC $			
                  METDIV $			
                  CSA $			
                  NECTA $			
                  NECTASC $			
                  NECTADIV $			
                  CNECTA $			
                  CBSAPCI $			
                  NECTAPCI $			
                  UA $			
                  UASC $			
                  UATYPE $			
                  UR $			
                  CD $			
                  SLDU $			
                  SLDL $			
                  VTD $			
                  VTDI $			
                  RESERVE2 $			
                  ZCTA5 $			
                  SUBMCD $			
                  SUBMCDCC $			
                  SDELEM $			
                  SDSEC $			
                  SDUNI $			
                  AREALAND $			
                  AREAWATR $			
                  NAME $			
                  FUNCSTAT $			
                  GCUNI $			
                  POP100			
                  HU100			
                  INTPTLAT $			
                  INTPTLON $			
                  LSADC $			
                  PARTFLAG $			
                  RESERVE3 $			
                  UGA $			
                  STATENS $			
                  COUNTYNS $			
                  COUSUBNS $			
                  PLACENS $			
                  CONCITNS $			
                  AIANHHNS $			
                  AITSNS $			
                  ANRCNS $			
                  SUBMCDNS $			
                  CD113 $			
                  CD114 $			
                  CD115 $			
                  SLDU2	$		
                  SLDU3	$		
                  SLDU4	$		
                  SLDL2	$		
                  SLDL3	$		
                  SLDL4	$		
                  AIANHHSC $			
                  CSASC $			
                  CNECTASC $			
                  MEMI $			
                  NMEMI $			
                  PUMA $			
                  RESERVED	$	 	
                  P0010001			
                  P0020001			
                  P0020002			
                  P0020003			
                  P0020004			
                  P0020005			
                  P0020006			
                  P0030001			
                  P0030002			
                  P0030003			
                  P0030004			
                  P0030005			
                  P0030006			
                  P0030007			
                  P0030008			
                  P0040001			
                  P0040002			
                  P0040003			
                  P0050001			
                  P0050002			
                  P0050003			
                  P0050004			
                  P0050005			
                  P0050006			
                  P0050007			
                  P0050008			
                  P0050009			
                  P0050010			
                  P0050011			
                  P0050012			
                  P0050013			
                  P0050014			
                  P0050015			
                  P0050016			
                  P0050017			
                  P0060001			
                  P0060002			
                  P0060003			
                  P0060004			
                  P0060005			
                  P0060006			
                  P0060007			
                  P0070001			
                  P0070002			
                  P0070003			
                  P0070004			
                  P0070005			
                  P0070006			
                  P0070007			
                  P0070008			
                  P0070009			
                  P0070010			
                  P0070011			
                  P0070012			
                  P0070013			
                  P0070014			
                  P0070015			
                  P0080001			
                  P0080002			
                  P0080003			
                  P0080004			
                  P0080005			
                  P0080006			
                  P0080007			
                  P0080008			
                  P0080009			
                  P0080010			
                  P0080011			
                  P0080012			
                  P0080013			
                  P0080014			
                  P0080015			
                  P0080016			
                  P0080017			
                  P0080018			
                  P0080019			
                  P0080020			
                  P0080021			
                  P0080022			
                  P0080023			
                  P0080024			
                  P0080025			
                  P0080026			
                  P0080027			
                  P0080028			
                  P0080029			
                  P0080030			
                  P0080031			
                  P0080032			
                  P0080033			
                  P0080034			
                  P0080035			
                  P0080036			
                  P0080037			
                  P0080038			
                  P0080039			
                  P0080040			
                  P0080041			
                  P0080042			
                  P0080043			
                  P0080044			
                  P0080045			
                  P0080046			
                  P0080047			
                  P0080048			
                  P0080049			
                  P0080050			
                  P0080051			
                  P0080052			
                  P0080053			
                  P0080054			
                  P0080055			
                  P0080056			
                  P0080057			
                  P0080058			
                  P0080059			
                  P0080060			
                  P0080061			
                  P0080062			
                  P0080063			
                  P0080064			
                  P0080065			
                  P0080066			
                  P0080067			
                  P0080068			
                  P0080069			
                  P0080070			
                  P0080071			
                  P0090001			
                  P0090002			
                  P0090003			
                  P0090004			
                  P0090005			
                  P0090006			
                  P0090007			
                  P0090008			
                  P0090009			
                  P0090010			
                  P0090011			
                  P0090012			
                  P0090013			
                  P0090014			
                  P0090015			
                  P0090016			
                  P0090017			
                  P0090018			
                  P0090019			
                  P0090020			
                  P0090021			
                  P0090022			
                  P0090023			
                  P0090024			
                  P0090025			
                  P0090026			
                  P0090027			
                  P0090028			
                  P0090029			
                  P0090030			
                  P0090031			
                  P0090032			
                  P0090033			
                  P0090034			
                  P0090035			
                  P0090036			
                  P0090037			
                  P0090038			
                  P0090039			
                  P0090040			
                  P0090041			
                  P0090042			
                  P0090043			
                  P0090044			
                  P0090045			
                  P0090046			
                  P0090047			
                  P0090048			
                  P0090049			
                  P0090050			
                  P0090051			
                  P0090052			
                  P0090053			
                  P0090054			
                  P0090055			
                  P0090056			
                  P0090057			
                  P0090058			
                  P0090059			
                  P0090060			
                  P0090061			
                  P0090062			
                  P0090063			
                  P0090064			
                  P0090065			
                  P0090066			
                  P0090067			
                  P0090068			
                  P0090069			
                  P0090070			
                  P0090071			
                  P0090072			
                  P0090073			
                  P0100001			
                  P0100002			
                  P0100003			
                  P0100004			
                  P0100005			
                  P0100006			
                  P0100007			
                  P0100008			
                  P0100009			
                  P0100010			
                  P0100011			
                  P0100012			
                  P0100013			
                  P0100014			
                  P0100015			
                  P0100016			
                  P0100017			
                  P0100018			
                  P0100019			
                  P0100020			
                  P0100021			
                  P0100022			
                  P0100023			
                  P0100024			
                  P0100025			
                  P0100026			
                  P0100027			
                  P0100028			
                  P0100029			
                  P0100030			
                  P0100031			
                  P0100032			
                  P0100033			
                  P0100034			
                  P0100035			
                  P0100036			
                  P0100037			
                  P0100038			
                  P0100039			
                  P0100040			
                  P0100041			
                  P0100042			
                  P0100043			
                  P0100044			
                  P0100045			
                  P0100046			
                  P0100047			
                  P0100048			
                  P0100049			
                  P0100050			
                  P0100051			
                  P0100052			
                  P0100053			
                  P0100054			
                  P0100055			
                  P0100056			
                  P0100057			
                  P0100058			
                  P0100059			
                  P0100060			
                  P0100061			
                  P0100062			
                  P0100063			
                  P0100064			
                  P0100065			
                  P0100066			
                  P0100067			
                  P0100068			
                  P0100069			
                  P0100070			
                  P0100071			
                  P0110001			
                  P0110002			
                  P0110003			
                  P0110004			
                  P0110005			
                  P0110006			
                  P0110007			
                  P0110008			
                  P0110009			
                  P0110010			
                  P0110011			
                  P0110012			
                  P0110013			
                  P0110014			
                  P0110015			
                  P0110016			
                  P0110017			
                  P0110018			
                  P0110019			
                  P0110020			
                  P0110021			
                  P0110022			
                  P0110023			
                  P0110024			
                  P0110025			
                  P0110026			
                  P0110027			
                  P0110028			
                  P0110029			
                  P0110030			
                  P0110031			
                  P0110032			
                  P0110033			
                  P0110034			
                  P0110035			
                  P0110036			
                  P0110037			
                  P0110038			
                  P0110039			
                  P0110040			
                  P0110041			
                  P0110042			
                  P0110043			
                  P0110044			
                  P0110045			
                  P0110046			
                  P0110047			
                  P0110048			
                  P0110049			
                  P0110050			
                  P0110051			
                  P0110052			
                  P0110053			
                  P0110054			
                  P0110055			
                  P0110056			
                  P0110057			
                  P0110058			
                  P0110059			
                  P0110060			
                  P0110061			
                  P0110062			
                  P0110063			
                  P0110064			
                  P0110065			
                  P0110066			
                  P0110067			
                  P0110068			
                  P0110069			
                  P0110070			
                  P0110071			
                  P0110072			
                  P0110073			
                  P0120001			
                  P0120002			
                  P0120003			
                  P0120004			
                  P0120005			
                  P0120006			
                  P0120007			
                  P0120008			
                  P0120009			
                  P0120010			
                  P0120011			
                  P0120012			
                  P0120013			
                  P0120014			
                  P0120015			
                  P0120016			
                  P0120017			
                  P0120018			
                  P0120019			
                  P0120020			
                  P0120021			
                  P0120022			
                  P0120023			
                  P0120024			
                  P0120025			
                  P0120026			
                  P0120027			
                  P0120028			
                  P0120029			
                  P0120030			
                  P0120031			
                  P0120032			
                  P0120033			
                  P0120034			
                  P0120035			
                  P0120036			
                  P0120037			
                  P0120038			
                  P0120039			
                  P0120040			
                  P0120041			
                  P0120042			
                  P0120043			
                  P0120044			
                  P0120045			
                  P0120046			
                  P0120047			
                  P0120048			
                  P0120049			
                  P0130001			
                  P0130002			
                  P0130003			
                  P0140001			
                  P0140002			
                  P0140003			
                  P0140004			
                  P0140005			
                  P0140006			
                  P0140007			
                  P0140008			
                  P0140009			
                  P0140010			
                  P0140011			
                  P0140012			
                  P0140013			
                  P0140014			
                  P0140015			
                  P0140016			
                  P0140017			
                  P0140018			
                  P0140019			
                  P0140020			
                  P0140021			
                  P0140022			
                  P0140023			
                  P0140024			
                  P0140025			
                  P0140026			
                  P0140027			
                  P0140028			
                  P0140029			
                  P0140030			
                  P0140031			
                  P0140032			
                  P0140033			
                  P0140034			
                  P0140035			
                  P0140036			
                  P0140037			
                  P0140038			
                  P0140039			
                  P0140040			
                  P0140041			
                  P0140042			
                  P0140043			
                  P0150001			
                  P0150002			
                  P0150003			
                  P0150004			
                  P0150005			
                  P0150006			
                  P0150007			
                  P0150008			
                  P0150009			
                  P0150010			
                  P0150011			
                  P0150012			
                  P0150013			
                  P0150014			
                  P0150015			
                  P0150016			
                  P0150017			
                  P0160001			
                  P0160002			
                  P0160003			
                  P0170001			
                  P0170002			
                  P0170003			
                  P0180001			
                  P0180002			
                  P0180003			
                  P0180004			
                  P0180005			
                  P0180006			
                  P0180007			
                  P0180008			
                  P0180009			
                  P0190001			
                  P0190002			
                  P0190003			
                  P0190004			
                  P0190005			
                  P0190006			
                  P0190007			
                  P0190008			
                  P0190009			
                  P0190010			
                  P0190011			
                  P0190012			
                  P0190013			
                  P0190014			
                  P0190015			
                  P0190016			
                  P0190017			
                  P0190018			
                  P0190019			
                  P0200001			
                  P0200002			
                  P0200003			
                  P0200004			
                  P0200005			
                  P0200006			
                  P0200007			
                  P0200008			
                  P0200009			
                  P0200010			
                  P0200011			
                  P0200012			
                  P0200013			
                  P0200014			
                  P0200015			
                  P0200016			
                  P0200017			
                  P0200018			
                  P0200019			
                  P0200020			
                  P0200021			
                  P0200022			
                  P0200023			
                  P0200024			
                  P0200025			
                  P0200026			
                  P0200027			
                  P0200028			
                  P0200029			
                  P0200030			
                  P0200031			
                  P0200032			
                  P0200033			
                  P0200034			
                  P0210001			
                  P0210002			
                  P0210003			
                  P0210004			
                  P0210005			
                  P0210006			
                  P0210007			
                  P0210008			
                  P0210009			
                  P0210010			
                  P0210011			
                  P0210012			
                  P0210013			
                  P0210014			
                  P0210015			
                  P0210016			
                  P0210017			
                  P0210018			
                  P0210019			
                  P0210020			
                  P0210021			
                  P0210022			
                  P0210023			
                  P0210024			
                  P0210025			
                  P0210026			
                  P0210027			
                  P0210028			
                  P0210029			
                  P0210030			
                  P0210031			
                  P0220001			
                  P0220002			
                  P0220003			
                  P0220004			
                  P0220005			
                  P0220006			
                  P0220007			
                  P0220008			
                  P0220009			
                  P0220010			
                  P0220011			
                  P0220012			
                  P0220013			
                  P0220014			
                  P0220015			
                  P0220016			
                  P0220017			
                  P0220018			
                  P0220019			
                  P0220020			
                  P0220021			
                  P0230001			
                  P0230002			
                  P0230003			
                  P0230004			
                  P0230005			
                  P0230006			
                  P0230007			
                  P0230008			
                  P0230009			
                  P0230010			
                  P0230011			
                  P0230012			
                  P0230013			
                  P0230014			
                  P0230015			
                  P0240001			
                  P0240002			
                  P0240003			
                  P0240004			
                  P0240005			
                  P0240006			
                  P0240007			
                  P0240008			
                  P0240009			
                  P0240010			
                  P0240011			
                  P0250001			
                  P0250002			
                  P0250003			
                  P0250004			
                  P0250005			
                  P0250006			
                  P0250007			
                  P0250008			
                  P0250009			
                  P0250010			
                  P0250011			
                  P0260001			
                  P0260002			
                  P0260003			
                  P0260004			
                  P0260005			
                  P0260006			
                  P0260007			
                  P0260008			
                  P0260009			
                  P0260010			
                  P0260011			
                  P0270001			
                  P0270002			
                  P0270003			
                  P0280001			
                  P0280002			
                  P0280003			
                  P0280004			
                  P0280005			
                  P0280006			
                  P0280007			
                  P0280008			
                  P0280009			
                  P0280010			
                  P0280011			
                  P0280012			
                  P0280013			
                  P0280014			
                  P0280015			
                  P0280016			
                  P0290001			
                  P0290002			
                  P0290003			
                  P0290004			
                  P0290005			
                  P0290006			
                  P0290007			
                  P0290008			
                  P0290009			
                  P0290010			
                  P0290011			
                  P0290012			
                  P0290013			
                  P0290014			
                  P0290015			
                  P0290016			
                  P0290017			
                  P0290018			
                  P0290019			
                  P0290020			
                  P0290021			
                  P0290022			
                  P0290023			
                  P0290024			
                  P0290025			
                  P0290026			
                  P0290027			
                  P0290028			
                  P0300001			
                  P0300002			
                  P0300003			
                  P0300004			
                  P0300005			
                  P0300006			
                  P0300007			
                  P0300008			
                  P0300009			
                  P0300010			
                  P0300011			
                  P0300012			
                  P0300013			
                  P0310001			
                  P0310002			
                  P0310003			
                  P0310004			
                  P0310005			
                  P0310006			
                  P0310007			
                  P0310008			
                  P0310009			
                  P0310010			
                  P0310011			
                  P0310012			
                  P0310013			
                  P0310014			
                  P0310015			
                  P0310016			
                  P0320001			
                  P0320002			
                  P0320003			
                  P0320004			
                  P0320005			
                  P0320006			
                  P0320007			
                  P0320008			
                  P0320009			
                  P0320010			
                  P0320011			
                  P0320012			
                  P0320013			
                  P0320014			
                  P0320015			
                  P0320016			
                  P0320017			
                  P0320018			
                  P0320019			
                  P0320020			
                  P0320021			
                  P0320022			
                  P0320023			
                  P0320024			
                  P0320025			
                  P0320026			
                  P0320027			
                  P0320028			
                  P0320029			
                  P0320030			
                  P0320031			
                  P0320032			
                  P0320033			
                  P0320034			
                  P0320035			
                  P0320036			
                  P0320037			
                  P0320038			
                  P0320039			
                  P0320040			
                  P0320041			
                  P0320042			
                  P0320043			
                  P0320044			
                  P0320045			
                  P0330001			
                  P0330002			
                  P0330003			
                  P0330004			
                  P0330005			
                  P0330006			
                  P0330007			
                  P0340001			
                  P0340002			
                  P0340003			
                  P0340004			
                  P0340005			
                  P0340006			
                  P0340007			
                  P0340008			
                  P0340009			
                  P0340010			
                  P0340011			
                  P0340012			
                  P0340013			
                  P0340014			
                  P0340015			
                  P0340016			
                  P0340017			
                  P0340018			
                  P0340019			
                  P0340020			
                  P0340021			
                  P0340022			
                  P0350001			
                  P0360001			
                  P0360002			
                  P0360003			
                  P0370001			
                  P0370002			
                  P0370003			
                  P0380001			
                  P0380002			
                  P0380003			
                  P0380004			
                  P0380005			
                  P0380006			
                  P0380007			
                  P0380008			
                  P0380009			
                  P0380010			
                  P0380011			
                  P0380012			
                  P0380013			
                  P0380014			
                  P0380015			
                  P0380016			
                  P0380017			
                  P0380018			
                  P0380019			
                  P0380020			
                  P0390001			
                  P0390002			
                  P0390003			
                  P0390004			
                  P0390005			
                  P0390006			
                  P0390007			
                  P0390008			
                  P0390009			
                  P0390010			
                  P0390011			
                  P0390012			
                  P0390013			
                  P0390014			
                  P0390015			
                  P0390016			
                  P0390017			
                  P0390018			
                  P0390019			
                  P0390020			
                  P0400001			
                  P0400002			
                  P0400003			
                  P0400004			
                  P0400005			
                  P0400006			
                  P0400007			
                  P0400008			
                  P0400009			
                  P0400010			
                  P0400011			
                  P0400012			
                  P0400013			
                  P0400014			
                  P0400015			
                  P0400016			
                  P0400017			
                  P0400018			
                  P0400019			
                  P0400020			
                  P0410001			
                  P0410002			
                  P0410003			
                  P0410004			
                  P0410005			
                  P0410006			
                  P0420001			
                  P0420002			
                  P0420003			
                  P0420004			
                  P0420005			
                  P0420006			
                  P0420007			
                  P0420008			
                  P0420009			
                  P0420010			
                  P0430001			
                  P0430002			
                  P0430003			
                  P0430004			
                  P0430005			
                  P0430006			
                  P0430007			
                  P0430008			
                  P0430009			
                  P0430010			
                  P0430011			
                  P0430012			
                  P0430013			
                  P0430014			
                  P0430015			
                  P0430016			
                  P0430017			
                  P0430018			
                  P0430019			
                  P0430020			
                  P0430021			
                  P0430022			
                  P0430023			
                  P0430024			
                  P0430025			
                  P0430026			
                  P0430027			
                  P0430028			
                  P0430029			
                  P0430030			
                  P0430031			
                  P0430032			
                  P0430033			
                  P0430034			
                  P0430035			
                  P0430036			
                  P0430037			
                  P0430038			
                  P0430039			
                  P0430040			
                  P0430041			
                  P0430042			
                  P0430043			
                  P0430044			
                  P0430045			
                  P0430046			
                  P0430047			
                  P0430048			
                  P0430049			
                  P0430050			
                  P0430051			
                  P0430052			
                  P0430053			
                  P0430054			
                  P0430055			
                  P0430056			
                  P0430057			
                  P0430058			
                  P0430059			
                  P0430060			
                  P0430061			
                  P0430062			
                  P0430063			
                  P0440001			
                  P0440002			
                  P0440003			
                  P0450001			
                  P0450002			
                  P0450003			
                  P0460001			
                  P0460002			
                  P0460003			
                  P0470001			
                  P0470002			
                  P0470003			
                  P0480001			
                  P0480002			
                  P0480003			
                  P0490001			
                  P0490002			
                  P0490003			
                  P0500001			
                  P0500002			
                  P0500003			
                  P0510001			
                  P0510002			
                  P0510003			
                  P012A001			
                  P012A002			
                  P012A003			
                  P012A004			
                  P012A005			
                  P012A006			
                  P012A007			
                  P012A008			
                  P012A009			
                  P012A010			
                  P012A011			
                  P012A012			
                  P012A013			
                  P012A014			
                  P012A015			
                  P012A016			
                  P012A017			
                  P012A018			
                  P012A019			
                  P012A020			
                  P012A021			
                  P012A022			
                  P012A023			
                  P012A024			
                  P012A025			
                  P012A026			
                  P012A027			
                  P012A028			
                  P012A029			
                  P012A030			
                  P012A031			
                  P012A032			
                  P012A033			
                  P012A034			
                  P012A035			
                  P012A036			
                  P012A037			
                  P012A038			
                  P012A039			
                  P012A040			
                  P012A041			
                  P012A042			
                  P012A043			
                  P012A044			
                  P012A045			
                  P012A046			
                  P012A047			
                  P012A048			
                  P012A049			
                  P012B001			
                  P012B002			
                  P012B003			
                  P012B004			
                  P012B005			
                  P012B006			
                  P012B007			
                  P012B008			
                  P012B009			
                  P012B010			
                  P012B011			
                  P012B012			
                  P012B013			
                  P012B014			
                  P012B015			
                  P012B016			
                  P012B017			
                  P012B018			
                  P012B019			
                  P012B020			
                  P012B021			
                  P012B022			
                  P012B023			
                  P012B024			
                  P012B025			
                  P012B026			
                  P012B027			
                  P012B028			
                  P012B029			
                  P012B030			
                  P012B031			
                  P012B032			
                  P012B033			
                  P012B034			
                  P012B035			
                  P012B036			
                  P012B037			
                  P012B038			
                  P012B039			
                  P012B040			
                  P012B041			
                  P012B042			
                  P012B043			
                  P012B044			
                  P012B045			
                  P012B046			
                  P012B047			
                  P012B048			
                  P012B049			
                  P012C001			
                  P012C002			
                  P012C003			
                  P012C004			
                  P012C005			
                  P012C006			
                  P012C007			
                  P012C008			
                  P012C009			
                  P012C010			
                  P012C011			
                  P012C012			
                  P012C013			
                  P012C014			
                  P012C015			
                  P012C016			
                  P012C017			
                  P012C018			
                  P012C019			
                  P012C020			
                  P012C021			
                  P012C022			
                  P012C023			
                  P012C024			
                  P012C025			
                  P012C026			
                  P012C027			
                  P012C028			
                  P012C029			
                  P012C030			
                  P012C031			
                  P012C032			
                  P012C033			
                  P012C034			
                  P012C035			
                  P012C036			
                  P012C037			
                  P012C038			
                  P012C039			
                  P012C040			
                  P012C041			
                  P012C042			
                  P012C043			
                  P012C044			
                  P012C045			
                  P012C046			
                  P012C047			
                  P012C048			
                  P012C049			
                  P012D001			
                  P012D002			
                  P012D003			
                  P012D004			
                  P012D005			
                  P012D006			
                  P012D007			
                  P012D008			
                  P012D009			
                  P012D010			
                  P012D011			
                  P012D012			
                  P012D013			
                  P012D014			
                  P012D015			
                  P012D016			
                  P012D017			
                  P012D018			
                  P012D019			
                  P012D020			
                  P012D021			
                  P012D022			
                  P012D023			
                  P012D024			
                  P012D025			
                  P012D026			
                  P012D027			
                  P012D028			
                  P012D029			
                  P012D030			
                  P012D031			
                  P012D032			
                  P012D033			
                  P012D034			
                  P012D035			
                  P012D036			
                  P012D037			
                  P012D038			
                  P012D039			
                  P012D040			
                  P012D041			
                  P012D042			
                  P012D043			
                  P012D044			
                  P012D045			
                  P012D046			
                  P012D047			
                  P012D048			
                  P012D049			
                  P012E001			
                  P012E002			
                  P012E003			
                  P012E004			
                  P012E005			
                  P012E006			
                  P012E007			
                  P012E008			
                  P012E009			
                  P012E010			
                  P012E011			
                  P012E012			
                  P012E013			
                  P012E014			
                  P012E015			
                  P012E016			
                  P012E017			
                  P012E018			
                  P012E019			
                  P012E020			
                  P012E021			
                  P012E022			
                  P012E023			
                  P012E024			
                  P012E025			
                  P012E026			
                  P012E027			
                  P012E028			
                  P012E029			
                  P012E030			
                  P012E031			
                  P012E032			
                  P012E033			
                  P012E034			
                  P012E035			
                  P012E036			
                  P012E037			
                  P012E038			
                  P012E039			
                  P012E040			
                  P012E041			
                  P012E042			
                  P012E043			
                  P012E044			
                  P012E045			
                  P012E046			
                  P012E047			
                  P012E048			
                  P012E049			
                  P012F001			
                  P012F002			
                  P012F003			
                  P012F004			
                  P012F005			
                  P012F006			
                  P012F007			
                  P012F008			
                  P012F009			
                  P012F010			
                  P012F011			
                  P012F012			
                  P012F013			
                  P012F014			
                  P012F015			
                  P012F016			
                  P012F017			
                  P012F018			
                  P012F019			
                  P012F020			
                  P012F021			
                  P012F022			
                  P012F023			
                  P012F024			
                  P012F025			
                  P012F026			
                  P012F027			
                  P012F028			
                  P012F029			
                  P012F030			
                  P012F031			
                  P012F032			
                  P012F033			
                  P012F034			
                  P012F035			
                  P012F036			
                  P012F037			
                  P012F038			
                  P012F039			
                  P012F040			
                  P012F041			
                  P012F042			
                  P012F043			
                  P012F044			
                  P012F045			
                  P012F046			
                  P012F047			
                  P012F048			
                  P012F049			
                  P012G001			
                  P012G002			
                  P012G003			
                  P012G004			
                  P012G005			
                  P012G006			
                  P012G007			
                  P012G008			
                  P012G009			
                  P012G010			
                  P012G011			
                  P012G012			
                  P012G013			
                  P012G014			
                  P012G015			
                  P012G016			
                  P012G017			
                  P012G018			
                  P012G019			
                  P012G020			
                  P012G021			
                  P012G022			
                  P012G023			
                  P012G024			
                  P012G025			
                  P012G026			
                  P012G027			
                  P012G028			
                  P012G029			
                  P012G030			
                  P012G031			
                  P012G032			
                  P012G033			
                  P012G034			
                  P012G035			
                  P012G036			
                  P012G037			
                  P012G038			
                  P012G039			
                  P012G040			
                  P012G041			
                  P012G042			
                  P012G043			
                  P012G044			
                  P012G045			
                  P012G046			
                  P012G047			
                  P012G048			
                  P012G049			
                  P012H001			
                  P012H002			
                  P012H003			
                  P012H004			
                  P012H005			
                  P012H006			
                  P012H007			
                  P012H008			
                  P012H009			
                  P012H010			
                  P012H011			
                  P012H012			
                  P012H013			
                  P012H014			
                  P012H015			
                  P012H016			
                  P012H017			
                  P012H018			
                  P012H019			
                  P012H020			
                  P012H021			
                  P012H022			
                  P012H023			
                  P012H024			
                  P012H025			
                  P012H026			
                  P012H027			
                  P012H028			
                  P012H029			
                  P012H030			
                  P012H031			
                  P012H032			
                  P012H033			
                  P012H034			
                  P012H035			
                  P012H036			
                  P012H037			
                  P012H038			
                  P012H039			
                  P012H040			
                  P012H041			
                  P012H042			
                  P012H043			
                  P012H044			
                  P012H045			
                  P012H046			
                  P012H047			
                  P012H048			
                  P012H049			
                  P012I001			
                  P012I002			
                  P012I003			
                  P012I004			
                  P012I005			
                  P012I006			
                  P012I007			
                  P012I008			
                  P012I009			
                  P012I010			
                  P012I011			
                  P012I012			
                  P012I013			
                  P012I014			
                  P012I015			
                  P012I016			
                  P012I017			
                  P012I018			
                  P012I019			
                  P012I020			
                  P012I021			
                  P012I022			
                  P012I023			
                  P012I024			
                  P012I025			
                  P012I026			
                  P012I027			
                  P012I028			
                  P012I029			
                  P012I030			
                  P012I031			
                  P012I032			
                  P012I033			
                  P012I034			
                  P012I035			
                  P012I036			
                  P012I037			
                  P012I038			
                  P012I039			
                  P012I040			
                  P012I041			
                  P012I042			
                  P012I043			
                  P012I044			
                  P012I045			
                  P012I046			
                  P012I047			
                  P012I048			
                  P012I049			
                  P013A001			
                  P013A002			
                  P013A003			
                  P013B001			
                  P013B002			
                  P013B003			
                  P013C001			
                  P013C002			
                  P013C003			
                  P013D001			
                  P013D002			
                  P013D003			
                  P013E001			
                  P013E002			
                  P013E003			
                  P013F001			
                  P013F002			
                  P013F003			
                  P013G001			
                  P013G002			
                  P013G003			
                  P013H001			
                  P013H002			
                  P013H003			
                  P013I001			
                  P013I002			
                  P013I003			
                  P016A001			
                  P016A002			
                  P016A003			
                  P016B001			
                  P016B002			
                  P016B003			
                  P016C001			
                  P016C002			
                  P016C003			
                  P016D001			
                  P016D002			
                  P016D003			
                  P016E001			
                  P016E002			
                  P016E003			
                  P016F001			
                  P016F002			
                  P016F003			
                  P016G001			
                  P016G002			
                  P016G003			
                  P016H001			
                  P016H002			
                  P016H003			
                  P016I001			
                  P016I002			
                  P016I003			
                  P017A001			
                  P017A002			
                  P017A003			
                  P017B001			
                  P017B002			
                  P017B003			
                  P017C001			
                  P017C002			
                  P017C003			
                  P017D001			
                  P017D002			
                  P017D003			
                  P017E001			
                  P017E002			
                  P017E003			
                  P017F001			
                  P017F002			
                  P017F003			
                  P017G001			
                  P017G002			
                  P017G003			
                  P017H001			
                  P017H002			
                  P017H003			
                  P017I001			
                  P017I002			
                  P017I003			
                  P018A001			
                  P018A002			
                  P018A003			
                  P018A004			
                  P018A005			
                  P018A006			
                  P018A007			
                  P018A008			
                  P018A009			
                  P018B001			
                  P018B002			
                  P018B003			
                  P018B004			
                  P018B005			
                  P018B006			
                  P018B007			
                  P018B008			
                  P018B009			
                  P018C001			
                  P018C002			
                  P018C003			
                  P018C004			
                  P018C005			
                  P018C006			
                  P018C007			
                  P018C008			
                  P018C009			
                  P018D001			
                  P018D002			
                  P018D003			
                  P018D004			
                  P018D005			
                  P018D006			
                  P018D007			
                  P018D008			
                  P018D009			
                  P018E001			
                  P018E002			
                  P018E003			
                  P018E004			
                  P018E005			
                  P018E006			
                  P018E007			
                  P018E008			
                  P018E009			
                  P018F001			
                  P018F002			
                  P018F003			
                  P018F004			
                  P018F005			
                  P018F006			
                  P018F007			
                  P018F008			
                  P018F009			
                  P018G001			
                  P018G002			
                  P018G003			
                  P018G004			
                  P018G005			
                  P018G006			
                  P018G007			
                  P018G008			
                  P018G009			
                  P018H001			
                  P018H002			
                  P018H003			
                  P018H004			
                  P018H005			
                  P018H006			
                  P018H007			
                  P018H008			
                  P018H009			
                  P018I001			
                  P018I002			
                  P018I003			
                  P018I004			
                  P018I005			
                  P018I006			
                  P018I007			
                  P018I008			
                  P018I009			
                  P028A001			
                  P028A002			
                  P028A003			
                  P028A004			
                  P028A005			
                  P028A006			
                  P028A007			
                  P028A008			
                  P028A009			
                  P028A010			
                  P028A011			
                  P028A012			
                  P028A013			
                  P028A014			
                  P028A015			
                  P028A016			
                  P028B001			
                  P028B002			
                  P028B003			
                  P028B004			
                  P028B005			
                  P028B006			
                  P028B007			
                  P028B008			
                  P028B009			
                  P028B010			
                  P028B011			
                  P028B012			
                  P028B013			
                  P028B014			
                  P028B015			
                  P028B016			
                  P028C001			
                  P028C002			
                  P028C003			
                  P028C004			
                  P028C005			
                  P028C006			
                  P028C007			
                  P028C008			
                  P028C009			
                  P028C010			
                  P028C011			
                  P028C012			
                  P028C013			
                  P028C014			
                  P028C015			
                  P028C016			
                  P028D001			
                  P028D002			
                  P028D003			
                  P028D004			
                  P028D005			
                  P028D006			
                  P028D007			
                  P028D008			
                  P028D009			
                  P028D010			
                  P028D011			
                  P028D012			
                  P028D013			
                  P028D014			
                  P028D015			
                  P028D016			
                  P028E001			
                  P028E002			
                  P028E003			
                  P028E004			
                  P028E005			
                  P028E006			
                  P028E007			
                  P028E008			
                  P028E009			
                  P028E010			
                  P028E011			
                  P028E012			
                  P028E013			
                  P028E014			
                  P028E015			
                  P028E016			
                  P028F001			
                  P028F002			
                  P028F003			
                  P028F004			
                  P028F005			
                  P028F006			
                  P028F007			
                  P028F008			
                  P028F009			
                  P028F010			
                  P028F011			
                  P028F012			
                  P028F013			
                  P028F014			
                  P028F015			
                  P028F016			
                  P028G001			
                  P028G002			
                  P028G003			
                  P028G004			
                  P028G005			
                  P028G006			
                  P028G007			
                  P028G008			
                  P028G009			
                  P028G010			
                  P028G011			
                  P028G012			
                  P028G013			
                  P028G014			
                  P028G015			
                  P028G016			
                  P028H001			
                  P028H002			
                  P028H003			
                  P028H004			
                  P028H005			
                  P028H006			
                  P028H007			
                  P028H008			
                  P028H009			
                  P028H010			
                  P028H011			
                  P028H012			
                  P028H013			
                  P028H014			
                  P028H015			
                  P028H016			
                  P028I001			
                  P028I002			
                  P028I003			
                  P028I004			
                  P028I005			
                  P028I006			
                  P028I007			
                  P028I008			
                  P028I009			
                  P028I010			
                  P028I011			
                  P028I012			
                  P028I013			
                  P028I014			
                  P028I015			
                  P028I016			
                  P029A001			
                  P029A002			
                  P029A003			
                  P029A004			
                  P029A005			
                  P029A006			
                  P029A007			
                  P029A008			
                  P029A009			
                  P029A010			
                  P029A011			
                  P029A012			
                  P029A013			
                  P029A014			
                  P029A015			
                  P029A016			
                  P029A017			
                  P029A018			
                  P029A019			
                  P029A020			
                  P029A021			
                  P029A022			
                  P029A023			
                  P029A024			
                  P029A025			
                  P029A026			
                  P029A027			
                  P029A028			
                  P029B001			
                  P029B002			
                  P029B003			
                  P029B004			
                  P029B005			
                  P029B006			
                  P029B007			
                  P029B008			
                  P029B009			
                  P029B010			
                  P029B011			
                  P029B012			
                  P029B013			
                  P029B014			
                  P029B015			
                  P029B016			
                  P029B017			
                  P029B018			
                  P029B019			
                  P029B020			
                  P029B021			
                  P029B022			
                  P029B023			
                  P029B024			
                  P029B025			
                  P029B026			
                  P029B027			
                  P029B028			
                  P029C001			
                  P029C002			
                  P029C003			
                  P029C004			
                  P029C005			
                  P029C006			
                  P029C007			
                  P029C008			
                  P029C009			
                  P029C010			
                  P029C011			
                  P029C012			
                  P029C013			
                  P029C014			
                  P029C015			
                  P029C016			
                  P029C017			
                  P029C018			
                  P029C019			
                  P029C020			
                  P029C021			
                  P029C022			
                  P029C023			
                  P029C024			
                  P029C025			
                  P029C026			
                  P029C027			
                  P029C028			
                  P029D001			
                  P029D002			
                  P029D003			
                  P029D004			
                  P029D005			
                  P029D006			
                  P029D007			
                  P029D008			
                  P029D009			
                  P029D010			
                  P029D011			
                  P029D012			
                  P029D013			
                  P029D014			
                  P029D015			
                  P029D016			
                  P029D017			
                  P029D018			
                  P029D019			
                  P029D020			
                  P029D021			
                  P029D022			
                  P029D023			
                  P029D024			
                  P029D025			
                  P029D026			
                  P029D027			
                  P029D028			
                  P029E001			
                  P029E002			
                  P029E003			
                  P029E004			
                  P029E005			
                  P029E006			
                  P029E007			
                  P029E008			
                  P029E009			
                  P029E010			
                  P029E011			
                  P029E012			
                  P029E013			
                  P029E014			
                  P029E015			
                  P029E016			
                  P029E017			
                  P029E018			
                  P029E019			
                  P029E020			
                  P029E021			
                  P029E022			
                  P029E023			
                  P029E024			
                  P029E025			
                  P029E026			
                  P029E027			
                  P029E028			
                  P029F001			
                  P029F002			
                  P029F003			
                  P029F004			
                  P029F005			
                  P029F006			
                  P029F007			
                  P029F008			
                  P029F009			
                  P029F010			
                  P029F011			
                  P029F012			
                  P029F013			
                  P029F014			
                  P029F015			
                  P029F016			
                  P029F017			
                  P029F018			
                  P029F019			
                  P029F020			
                  P029F021			
                  P029F022			
                  P029F023			
                  P029F024			
                  P029F025			
                  P029F026			
                  P029F027			
                  P029F028			
                  P029G001			
                  P029G002			
                  P029G003			
                  P029G004			
                  P029G005			
                  P029G006			
                  P029G007			
                  P029G008			
                  P029G009			
                  P029G010			
                  P029G011			
                  P029G012			
                  P029G013			
                  P029G014			
                  P029G015			
                  P029G016			
                  P029G017			
                  P029G018			
                  P029G019			
                  P029G020			
                  P029G021			
                  P029G022			
                  P029G023			
                  P029G024			
                  P029G025			
                  P029G026			
                  P029G027			
                  P029G028			
                  P029H001			
                  P029H002			
                  P029H003			
                  P029H004			
                  P029H005			
                  P029H006			
                  P029H007			
                  P029H008			
                  P029H009			
                  P029H010			
                  P029H011			
                  P029H012			
                  P029H013			
                  P029H014			
                  P029H015			
                  P029H016			
                  P029H017			
                  P029H018			
                  P029H019			
                  P029H020			
                  P029H021			
                  P029H022			
                  P029H023			
                  P029H024			
                  P029H025			
                  P029H026			
                  P029H027			
                  P029H028			
                  P029I001			
                  P029I002			
                  P029I003			
                  P029I004			
                  P029I005			
                  P029I006			
                  P029I007			
                  P029I008			
                  P029I009			
                  P029I010			
                  P029I011			
                  P029I012			
                  P029I013			
                  P029I014			
                  P029I015			
                  P029I016			
                  P029I017			
                  P029I018			
                  P029I019			
                  P029I020			
                  P029I021			
                  P029I022			
                  P029I023			
                  P029I024			
                  P029I025			
                  P029I026			
                  P029I027			
                  P029I028			
                  P031A001			
                  P031A002			
                  P031A003			
                  P031A004			
                  P031A005			
                  P031A006			
                  P031A007			
                  P031A008			
                  P031A009			
                  P031A010			
                  P031A011			
                  P031A012			
                  P031A013			
                  P031A014			
                  P031A015			
                  P031A016			
                  P031B001			
                  P031B002			
                  P031B003			
                  P031B004			
                  P031B005			
                  P031B006			
                  P031B007			
                  P031B008			
                  P031B009			
                  P031B010			
                  P031B011			
                  P031B012			
                  P031B013			
                  P031B014			
                  P031B015			
                  P031B016			
                  P031C001			
                  P031C002			
                  P031C003			
                  P031C004			
                  P031C005			
                  P031C006			
                  P031C007			
                  P031C008			
                  P031C009			
                  P031C010			
                  P031C011			
                  P031C012			
                  P031C013			
                  P031C014			
                  P031C015			
                  P031C016			
                  P031D001			
                  P031D002			
                  P031D003			
                  P031D004			
                  P031D005			
                  P031D006			
                  P031D007			
                  P031D008			
                  P031D009			
                  P031D010			
                  P031D011			
                  P031D012			
                  P031D013			
                  P031D014			
                  P031D015			
                  P031D016			
                  P031E001			
                  P031E002			
                  P031E003			
                  P031E004			
                  P031E005			
                  P031E006			
                  P031E007			
                  P031E008			
                  P031E009			
                  P031E010			
                  P031E011			
                  P031E012			
                  P031E013			
                  P031E014			
                  P031E015			
                  P031E016			
                  P031F001			
                  P031F002			
                  P031F003			
                  P031F004			
                  P031F005			
                  P031F006			
                  P031F007			
                  P031F008			
                  P031F009			
                  P031F010			
                  P031F011			
                  P031F012			
                  P031F013			
                  P031F014			
                  P031F015			
                  P031F016			
                  P031G001			
                  P031G002			
                  P031G003			
                  P031G004			
                  P031G005			
                  P031G006			
                  P031G007			
                  P031G008			
                  P031G009			
                  P031G010			
                  P031G011			
                  P031G012			
                  P031G013			
                  P031G014			
                  P031G015			
                  P031G016			
                  P031H001			
                  P031H002			
                  P031H003			
                  P031H004			
                  P031H005			
                  P031H006			
                  P031H007			
                  P031H008			
                  P031H009			
                  P031H010			
                  P031H011			
                  P031H012			
                  P031H013			
                  P031H014			
                  P031H015			
                  P031H016			
                  P031I001			
                  P031I002			
                  P031I003			
                  P031I004			
                  P031I005			
                  P031I006			
                  P031I007			
                  P031I008			
                  P031I009			
                  P031I010			
                  P031I011			
                  P031I012			
                  P031I013			
                  P031I014			
                  P031I015			
                  P031I016			
                  P034A001			
                  P034A002			
                  P034A003			
                  P034A004			
                  P034A005			
                  P034A006			
                  P034A007			
                  P034A008			
                  P034A009			
                  P034A010			
                  P034A011			
                  P034A012			
                  P034A013			
                  P034A014			
                  P034A015			
                  P034A016			
                  P034A017			
                  P034A018			
                  P034A019			
                  P034A020			
                  P034A021			
                  P034A022			
                  P034B001			
                  P034B002			
                  P034B003			
                  P034B004			
                  P034B005			
                  P034B006			
                  P034B007			
                  P034B008			
                  P034B009			
                  P034B010			
                  P034B011			
                  P034B012			
                  P034B013			
                  P034B014			
                  P034B015			
                  P034B016			
                  P034B017			
                  P034B018			
                  P034B019			
                  P034B020			
                  P034B021			
                  P034B022			
                  P034C001			
                  P034C002			
                  P034C003			
                  P034C004			
                  P034C005			
                  P034C006			
                  P034C007			
                  P034C008			
                  P034C009			
                  P034C010			
                  P034C011			
                  P034C012			
                  P034C013			
                  P034C014			
                  P034C015			
                  P034C016			
                  P034C017			
                  P034C018			
                  P034C019			
                  P034C020			
                  P034C021			
                  P034C022			
                  P034D001			
                  P034D002			
                  P034D003			
                  P034D004			
                  P034D005			
                  P034D006			
                  P034D007			
                  P034D008			
                  P034D009			
                  P034D010			
                  P034D011			
                  P034D012			
                  P034D013			
                  P034D014			
                  P034D015			
                  P034D016			
                  P034D017			
                  P034D018			
                  P034D019			
                  P034D020			
                  P034D021			
                  P034D022			
                  P034E001			
                  P034E002			
                  P034E003			
                  P034E004			
                  P034E005			
                  P034E006			
                  P034E007			
                  P034E008			
                  P034E009			
                  P034E010			
                  P034E011			
                  P034E012			
                  P034E013			
                  P034E014			
                  P034E015			
                  P034E016			
                  P034E017			
                  P034E018			
                  P034E019			
                  P034E020			
                  P034E021			
                  P034E022			
                  P034F001			
                  P034F002			
                  P034F003			
                  P034F004			
                  P034F005			
                  P034F006			
                  P034F007			
                  P034F008			
                  P034F009			
                  P034F010			
                  P034F011			
                  P034F012			
                  P034F013			
                  P034F014			
                  P034F015			
                  P034F016			
                  P034F017			
                  P034F018			
                  P034F019			
                  P034F020			
                  P034F021			
                  P034F022			
                  P034G001			
                  P034G002			
                  P034G003			
                  P034G004			
                  P034G005			
                  P034G006			
                  P034G007			
                  P034G008			
                  P034G009			
                  P034G010			
                  P034G011			
                  P034G012			
                  P034G013			
                  P034G014			
                  P034G015			
                  P034G016			
                  P034G017			
                  P034G018			
                  P034G019			
                  P034G020			
                  P034G021			
                  P034G022			
                  P034H001			
                  P034H002			
                  P034H003			
                  P034H004			
                  P034H005			
                  P034H006			
                  P034H007			
                  P034H008			
                  P034H009			
                  P034H010			
                  P034H011			
                  P034H012			
                  P034H013			
                  P034H014			
                  P034H015			
                  P034H016			
                  P034H017			
                  P034H018			
                  P034H019			
                  P034H020			
                  P034H021			
                  P034H022			
                  P034I001			
                  P034I002			
                  P034I003			
                  P034I004			
                  P034I005			
                  P034I006			
                  P034I007			
                  P034I008			
                  P034I009			
                  P034I010			
                  P034I011			
                  P034I012			
                  P034I013			
                  P034I014			
                  P034I015			
                  P034I016			
                  P034I017			
                  P034I018			
                  P034I019			
                  P034I020			
                  P034I021			
                  P034I022			
                  P035A001			
                  P035B001			
                  P035C001			
                  P035D001			
                  P035E001			
                  P035F001			
                  P035G001			
                  P035H001			
                  P035I001			
                  P036A001			
                  P036A002			
                  P036A003			
                  P036B001			
                  P036B002			
                  P036B003			
                  P036C001			
                  P036C002			
                  P036C003			
                  P036D001			
                  P036D002			
                  P036D003			
                  P036E001			
                  P036E002			
                  P036E003			
                  P036F001			
                  P036F002			
                  P036F003			
                  P036G001			
                  P036G002			
                  P036G003			
                  P036H001			
                  P036H002			
                  P036H003			
                  P036I001			
                  P036I002			
                  P036I003			
                  P037A001			
                  P037A002			
                  P037A003			
                  P037B001			
                  P037B002			
                  P037B003			
                  P037C001			
                  P037C002			
                  P037C003			
                  P037D001			
                  P037D002			
                  P037D003			
                  P037E001			
                  P037E002			
                  P037E003			
                  P037F001			
                  P037F002			
                  P037F003			
                  P037G001			
                  P037G002			
                  P037G003			
                  P037H001			
                  P037H002			
                  P037H003			
                  P037I001			
                  P037I002			
                  P037I003			
                  P038A001			
                  P038A002			
                  P038A003			
                  P038A004			
                  P038A005			
                  P038A006			
                  P038A007			
                  P038A008			
                  P038A009			
                  P038A010			
                  P038A011			
                  P038A012			
                  P038A013			
                  P038A014			
                  P038A015			
                  P038A016			
                  P038A017			
                  P038A018			
                  P038A019			
                  P038A020			
                  P038B001			
                  P038B002			
                  P038B003			
                  P038B004			
                  P038B005			
                  P038B006			
                  P038B007			
                  P038B008			
                  P038B009			
                  P038B010			
                  P038B011			
                  P038B012			
                  P038B013			
                  P038B014			
                  P038B015			
                  P038B016			
                  P038B017			
                  P038B018			
                  P038B019			
                  P038B020			
                  P038C001			
                  P038C002			
                  P038C003			
                  P038C004			
                  P038C005			
                  P038C006			
                  P038C007			
                  P038C008			
                  P038C009			
                  P038C010			
                  P038C011			
                  P038C012			
                  P038C013			
                  P038C014			
                  P038C015			
                  P038C016			
                  P038C017			
                  P038C018			
                  P038C019			
                  P038C020			
                  P038D001			
                  P038D002			
                  P038D003			
                  P038D004			
                  P038D005			
                  P038D006			
                  P038D007			
                  P038D008			
                  P038D009			
                  P038D010			
                  P038D011			
                  P038D012			
                  P038D013			
                  P038D014			
                  P038D015			
                  P038D016			
                  P038D017			
                  P038D018			
                  P038D019			
                  P038D020			
                  P038E001			
                  P038E002			
                  P038E003			
                  P038E004			
                  P038E005			
                  P038E006			
                  P038E007			
                  P038E008			
                  P038E009			
                  P038E010			
                  P038E011			
                  P038E012			
                  P038E013			
                  P038E014			
                  P038E015			
                  P038E016			
                  P038E017			
                  P038E018			
                  P038E019			
                  P038E020			
                  P038F001			
                  P038F002			
                  P038F003			
                  P038F004			
                  P038F005			
                  P038F006			
                  P038F007			
                  P038F008			
                  P038F009			
                  P038F010			
                  P038F011			
                  P038F012			
                  P038F013			
                  P038F014			
                  P038F015			
                  P038F016			
                  P038F017			
                  P038F018			
                  P038F019			
                  P038F020			
                  P038G001			
                  P038G002			
                  P038G003			
                  P038G004			
                  P038G005			
                  P038G006			
                  P038G007			
                  P038G008			
                  P038G009			
                  P038G010			
                  P038G011			
                  P038G012			
                  P038G013			
                  P038G014			
                  P038G015			
                  P038G016			
                  P038G017			
                  P038G018			
                  P038G019			
                  P038G020			
                  P038H001			
                  P038H002			
                  P038H003			
                  P038H004			
                  P038H005			
                  P038H006			
                  P038H007			
                  P038H008			
                  P038H009			
                  P038H010			
                  P038H011			
                  P038H012			
                  P038H013			
                  P038H014			
                  P038H015			
                  P038H016			
                  P038H017			
                  P038H018			
                  P038H019			
                  P038H020			
                  P038I001			
                  P038I002			
                  P038I003			
                  P038I004			
                  P038I005			
                  P038I006			
                  P038I007			
                  P038I008			
                  P038I009			
                  P038I010			
                  P038I011			
                  P038I012			
                  P038I013			
                  P038I014			
                  P038I015			
                  P038I016			
                  P038I017			
                  P038I018			
                  P038I019			
                  P038I020			
                  P039A001			
                  P039A002			
                  P039A003			
                  P039A004			
                  P039A005			
                  P039A006			
                  P039A007			
                  P039A008			
                  P039A009			
                  P039A010			
                  P039A011			
                  P039A012			
                  P039A013			
                  P039A014			
                  P039A015			
                  P039A016			
                  P039A017			
                  P039A018			
                  P039A019			
                  P039A020			
                  P039B001			
                  P039B002			
                  P039B003			
                  P039B004			
                  P039B005			
                  P039B006			
                  P039B007			
                  P039B008			
                  P039B009			
                  P039B010			
                  P039B011			
                  P039B012			
                  P039B013			
                  P039B014			
                  P039B015			
                  P039B016			
                  P039B017			
                  P039B018			
                  P039B019			
                  P039B020			
                  P039C001			
                  P039C002			
                  P039C003			
                  P039C004			
                  P039C005			
                  P039C006			
                  P039C007			
                  P039C008			
                  P039C009			
                  P039C010			
                  P039C011			
                  P039C012			
                  P039C013			
                  P039C014			
                  P039C015			
                  P039C016			
                  P039C017			
                  P039C018			
                  P039C019			
                  P039C020			
                  P039D001			
                  P039D002			
                  P039D003			
                  P039D004			
                  P039D005			
                  P039D006			
                  P039D007			
                  P039D008			
                  P039D009			
                  P039D010			
                  P039D011			
                  P039D012			
                  P039D013			
                  P039D014			
                  P039D015			
                  P039D016			
                  P039D017			
                  P039D018			
                  P039D019			
                  P039D020			
                  P039E001			
                  P039E002			
                  P039E003			
                  P039E004			
                  P039E005			
                  P039E006			
                  P039E007			
                  P039E008			
                  P039E009			
                  P039E010			
                  P039E011			
                  P039E012			
                  P039E013			
                  P039E014			
                  P039E015			
                  P039E016			
                  P039E017			
                  P039E018			
                  P039E019			
                  P039E020			
                  P039F001			
                  P039F002			
                  P039F003			
                  P039F004			
                  P039F005			
                  P039F006			
                  P039F007			
                  P039F008			
                  P039F009			
                  P039F010			
                  P039F011			
                  P039F012			
                  P039F013			
                  P039F014			
                  P039F015			
                  P039F016			
                  P039F017			
                  P039F018			
                  P039F019			
                  P039F020			
                  P039G001			
                  P039G002			
                  P039G003			
                  P039G004			
                  P039G005			
                  P039G006			
                  P039G007			
                  P039G008			
                  P039G009			
                  P039G010			
                  P039G011			
                  P039G012			
                  P039G013			
                  P039G014			
                  P039G015			
                  P039G016			
                  P039G017			
                  P039G018			
                  P039G019			
                  P039G020			
                  P039H001			
                  P039H002			
                  P039H003			
                  P039H004			
                  P039H005			
                  P039H006			
                  P039H007			
                  P039H008			
                  P039H009			
                  P039H010			
                  P039H011			
                  P039H012			
                  P039H013			
                  P039H014			
                  P039H015			
                  P039H016			
                  P039H017			
                  P039H018			
                  P039H019			
                  P039H020			
                  P039I001			
                  P039I002			
                  P039I003			
                  P039I004			
                  P039I005			
                  P039I006			
                  P039I007			
                  P039I008			
                  P039I009			
                  P039I010			
                  P039I011			
                  P039I012			
                  P039I013			
                  P039I014			
                  P039I015			
                  P039I016			
                  P039I017			
                  P039I018			
                  P039I019			
                  P039I020			
                  PCT0010001			
                  PCT0010002			
                  PCT0010003			
                  PCT0010004			
                  PCT0010005			
                  PCT0010006			
                  PCT0010007			
                  PCT0010008			
                  PCT0010009			
                  PCT0010010			
                  PCT0010011			
                  PCT0010012			
                  PCT0010013			
                  PCT0010014			
                  PCT0010015			
                  PCT0010016			
                  PCT0010017			
                  PCT0010018			
                  PCT0010019			
                  PCT0010020			
                  PCT0010021			
                  PCT0010022			
                  PCT0010023			
                  PCT0010024			
                  PCT0010025			
                  PCT0010026			
                  PCT0010027			
                  PCT0010028			
                  PCT0010029			
                  PCT0010030			
                  PCT0010031			
                  PCT0010032			
                  PCT0010033			
                  PCT0010034			
                  PCT0010035			
                  PCT0010036			
                  PCT0010037			
                  PCT0010038			
                  PCT0010039			
                  PCT0010040			
                  PCT0010041			
                  PCT0010042			
                  PCT0010043			
                  PCT0010044			
                  PCT0010045			
                  PCT0010046			
                  PCT0010047			
                  PCT0010048			
                  PCT0010049			
                  PCT0010050			
                  PCT0010051			
                  PCT0010052			
                  PCT0010053			
                  PCT0010054			
                  PCT0020001			
                  PCT0020002			
                  PCT0020003			
                  PCT0020004			
                  PCT0020005			
                  PCT0020006			
                  PCT0020007			
                  PCT0020008			
                  PCT0020009			
                  PCT0020010			
                  PCT0020011			
                  PCT0020012			
                  PCT0020013			
                  PCT0020014			
                  PCT0020015			
                  PCT0020016			
                  PCT0020017			
                  PCT0020018			
                  PCT0020019			
                  PCT0020020			
                  PCT0020021			
                  PCT0020022			
                  PCT0020023			
                  PCT0020024			
                  PCT0020025			
                  PCT0020026			
                  PCT0020027			
                  PCT0020028			
                  PCT0020029			
                  PCT0020030			
                  PCT0020031			
                  PCT0020032			
                  PCT0020033			
                  PCT0020034			
                  PCT0020035			
                  PCT0020036			
                  PCT0020037			
                  PCT0020038			
                  PCT0020039			
                  PCT0020040			
                  PCT0020041			
                  PCT0020042			
                  PCT0020043			
                  PCT0020044			
                  PCT0020045			
                  PCT0020046			
                  PCT0020047			
                  PCT0020048			
                  PCT0020049			
                  PCT0020050			
                  PCT0020051			
                  PCT0020052			
                  PCT0020053			
                  PCT0020054			
                  PCT0030001			
                  PCT0030002			
                  PCT0030003			
                  PCT0030004			
                  PCT0030005			
                  PCT0030006			
                  PCT0030007			
                  PCT0030008			
                  PCT0030009			
                  PCT0030010			
                  PCT0030011			
                  PCT0030012			
                  PCT0030013			
                  PCT0030014			
                  PCT0030015			
                  PCT0030016			
                  PCT0030017			
                  PCT0030018			
                  PCT0030019			
                  PCT0030020			
                  PCT0030021			
                  PCT0030022			
                  PCT0030023			
                  PCT0030024			
                  PCT0030025			
                  PCT0030026			
                  PCT0030027			
                  PCT0030028			
                  PCT0030029			
                  PCT0030030			
                  PCT0030031			
                  PCT0030032			
                  PCT0030033			
                  PCT0030034			
                  PCT0030035			
                  PCT0030036			
                  PCT0030037			
                  PCT0030038			
                  PCT0030039			
                  PCT0030040			
                  PCT0030041			
                  PCT0030042			
                  PCT0030043			
                  PCT0030044			
                  PCT0030045			
                  PCT0030046			
                  PCT0030047			
                  PCT0030048			
                  PCT0030049			
                  PCT0030050			
  PCT0030051			
  PCT0030052			
  PCT0030053			
  PCT0030054			
  PCT0040001			
  PCT0040002			
  PCT0040003			
  PCT0040004			
  PCT0040005			
  PCT0040006			
  PCT0040007			
  PCT0040008			
  PCT0040009			
  PCT0050001			
  PCT0050002			
  PCT0050003			
  PCT0050004			
  PCT0050005			
  PCT0050006			
  PCT0050007			
  PCT0050008			
  PCT0050009			
  PCT0050010			
  PCT0050011			
  PCT0050012			
  PCT0050013			
  PCT0050014			
  PCT0050015			
  PCT0050016			
  PCT0050017			
  PCT0050018			
  PCT0050019			
  PCT0050020			
  PCT0050021			
  PCT0050022			
  PCT0060001			
  PCT0060002			
  PCT0060003			
  PCT0060004			
  PCT0060005			
  PCT0060006			
  PCT0060007			
  PCT0060008			
  PCT0060009			
  PCT0060010			
  PCT0060011			
  PCT0060012			
  PCT0060013			
  PCT0060014			
  PCT0060015			
  PCT0060016			
  PCT0060017			
  PCT0060018			
  PCT0060019			
  PCT0060020			
  PCT0060021			
  PCT0060022			
  PCT0070001			
  PCT0070002			
  PCT0070003			
  PCT0070004			
  PCT0070005			
  PCT0070006			
  PCT0070007			
  PCT0070008			
  PCT0070009			
  PCT0070010			
  PCT0070011			
  PCT0070012			
  PCT0070013			
  PCT0070014			
  PCT0070015			
  PCT0070016			
  PCT0070017			
  PCT0070018			
  PCT0070019			
  PCT0070020			
  PCT0070021			
  PCT0070022			
  PCT0080001			
  PCT0080002			
  PCT0080003			
  PCT0080004			
  PCT0080005			
  PCT0080006			
  PCT0080007			
  PCT0080008			
  PCT0080009			
  PCT0080010			
  PCT0080011			
  PCT0080012			
  PCT0080013			
  PCT0080014			
  PCT0090001			
  PCT0090002			
  PCT0090003			
  PCT0090004			
  PCT0090005			
  PCT0090006			
  PCT0090007			
  PCT0090008			
  PCT0090009			
  PCT0090010			
  PCT0090011			
  PCT0090012			
  PCT0090013			
  PCT0090014			
  PCT0100001			
  PCT0100002			
  PCT0100003			
  PCT0100004			
  PCT0100005			
  PCT0100006			
  PCT0100007			
  PCT0100008			
  PCT0100009			
  PCT0100010			
  PCT0100011			
  PCT0100012			
  PCT0100013			
  PCT0100014			
  PCT0110001			
  PCT0110002			
  PCT0110003			
  PCT0110004			
  PCT0110005			
  PCT0110006			
  PCT0110007			
  PCT0110008			
  PCT0110009			
  PCT0110010			
  PCT0110011			
  PCT0110012			
  PCT0110013			
  PCT0110014			
  PCT0110015			
  PCT0110016			
  PCT0110017			
  PCT0110018			
  PCT0110019			
  PCT0110020			
  PCT0110021			
  PCT0110022			
  PCT0110023			
  PCT0110024			
  PCT0110025			
  PCT0110026			
  PCT0110027			
  PCT0110028			
  PCT0110029			
  PCT0110030			
  PCT0110031			
  PCT0120001			
  PCT0120002			
  PCT0120003			
  PCT0120004			
  PCT0120005			
  PCT0120006			
  PCT0120007			
  PCT0120008			
  PCT0120009			
  PCT0120010			
  PCT0120011			
  PCT0120012			
  PCT0120013			
  PCT0120014			
  PCT0120015			
  PCT0120016			
  PCT0120017			
  PCT0120018			
  PCT0120019			
  PCT0120020			
  PCT0120021			
  PCT0120022			
  PCT0120023			
  PCT0120024			
  PCT0120025			
  PCT0120026			
  PCT0120027			
  PCT0120028			
  PCT0120029			
  PCT0120030			
  PCT0120031			
  PCT0120032			
  PCT0120033			
  PCT0120034			
  PCT0120035			
  PCT0120036			
  PCT0120037			
  PCT0120038			
  PCT0120039			
  PCT0120040			
  PCT0120041			
  PCT0120042			
  PCT0120043			
  PCT0120044			
  PCT0120045			
  PCT0120046			
  PCT0120047			
  PCT0120048			
  PCT0120049			
  PCT0120050			
  PCT0120051			
  PCT0120052			
  PCT0120053			
  PCT0120054			
  PCT0120055			
  PCT0120056			
  PCT0120057			
  PCT0120058			
  PCT0120059			
  PCT0120060			
  PCT0120061			
  PCT0120062			
  PCT0120063			
  PCT0120064			
  PCT0120065			
  PCT0120066			
  PCT0120067			
  PCT0120068			
  PCT0120069			
  PCT0120070			
  PCT0120071			
  PCT0120072			
  PCT0120073			
  PCT0120074			
  PCT0120075			
  PCT0120076			
  PCT0120077			
  PCT0120078			
  PCT0120079			
  PCT0120080			
  PCT0120081			
  PCT0120082			
  PCT0120083			
  PCT0120084			
  PCT0120085			
  PCT0120086			
  PCT0120087			
  PCT0120088			
  PCT0120089			
  PCT0120090			
  PCT0120091			
  PCT0120092			
  PCT0120093			
  PCT0120094			
  PCT0120095			
  PCT0120096			
  PCT0120097			
  PCT0120098			
  PCT0120099			
  PCT0120100			
  PCT0120101			
  PCT0120102			
  PCT0120103			
  PCT0120104			
  PCT0120105			
  PCT0120106			
  PCT0120107			
  PCT0120108			
  PCT0120109			
  PCT0120110			
  PCT0120111			
  PCT0120112			
  PCT0120113			
  PCT0120114			
  PCT0120115			
  PCT0120116			
  PCT0120117			
  PCT0120118			
  PCT0120119			
  PCT0120120			
  PCT0120121			
  PCT0120122			
  PCT0120123			
  PCT0120124			
  PCT0120125			
  PCT0120126			
  PCT0120127			
  PCT0120128			
  PCT0120129			
  PCT0120130			
  PCT0120131			
  PCT0120132			
  PCT0120133			
  PCT0120134			
  PCT0120135			
  PCT0120136			
  PCT0120137			
  PCT0120138			
  PCT0120139			
  PCT0120140			
  PCT0120141			
  PCT0120142			
  PCT0120143			
  PCT0120144			
  PCT0120145			
  PCT0120146			
  PCT0120147			
  PCT0120148			
  PCT0120149			
  PCT0120150			
  PCT0120151			
  PCT0120152			
  PCT0120153			
  PCT0120154			
  PCT0120155			
  PCT0120156			
  PCT0120157			
  PCT0120158			
  PCT0120159			
  PCT0120160			
  PCT0120161			
  PCT0120162			
  PCT0120163			
  PCT0120164			
  PCT0120165			
  PCT0120166			
  PCT0120167			
  PCT0120168			
  PCT0120169			
  PCT0120170			
  PCT0120171			
  PCT0120172			
  PCT0120173			
  PCT0120174			
  PCT0120175			
  PCT0120176			
  PCT0120177			
  PCT0120178			
  PCT0120179			
  PCT0120180			
  PCT0120181			
  PCT0120182			
  PCT0120183			
  PCT0120184			
  PCT0120185			
  PCT0120186			
  PCT0120187			
  PCT0120188			
  PCT0120189			
  PCT0120190			
  PCT0120191			
  PCT0120192			
  PCT0120193			
  PCT0120194			
  PCT0120195			
  PCT0120196			
  PCT0120197			
  PCT0120198			
  PCT0120199			
  PCT0120200			
  PCT0120201			
  PCT0120202			
  PCT0120203			
  PCT0120204			
  PCT0120205			
  PCT0120206			
  PCT0120207			
  PCT0120208			
  PCT0120209			
  PCT0130001			
  PCT0130002			
  PCT0130003			
  PCT0130004			
  PCT0130005			
  PCT0130006			
  PCT0130007			
  PCT0130008			
  PCT0130009			
  PCT0130010			
  PCT0130011			
  PCT0130012			
  PCT0130013			
  PCT0130014			
  PCT0130015			
  PCT0130016			
  PCT0130017			
  PCT0130018			
  PCT0130019			
  PCT0130020			
  PCT0130021			
  PCT0130022			
  PCT0130023			
  PCT0130024			
  PCT0130025			
  PCT0130026			
  PCT0130027			
  PCT0130028			
  PCT0130029			
  PCT0130030			
  PCT0130031			
  PCT0130032			
  PCT0130033			
  PCT0130034			
  PCT0130035			
  PCT0130036			
  PCT0130037			
  PCT0130038			
  PCT0130039			
  PCT0130040			
  PCT0130041			
  PCT0130042			
  PCT0130043			
  PCT0130044			
  PCT0130045			
  PCT0130046			
  PCT0130047			
  PCT0130048			
  PCT0130049			
  PCT0140001			
  PCT0140002			
  PCT0140003			
  PCT0150001			
  PCT0150002			
  PCT0150003			
  PCT0150004			
  PCT0150005			
  PCT0150006			
  PCT0150007			
  PCT0150008			
  PCT0150009			
  PCT0150010			
  PCT0150011			
  PCT0150012			
  PCT0150013			
  PCT0150014			
  PCT0150015			
  PCT0150016			
  PCT0150017			
  PCT0150018			
  PCT0150019			
  PCT0150020			
  PCT0150021			
  PCT0150022			
  PCT0150023			
  PCT0150024			
  PCT0150025			
  PCT0150026			
  PCT0150027			
  PCT0150028			
  PCT0150029			
  PCT0150030			
  PCT0150031			
  PCT0150032			
  PCT0150033			
  PCT0150034			
  PCT0160001			
  PCT0160002			
  PCT0160003			
  PCT0160004			
  PCT0160005			
  PCT0160006			
  PCT0160007			
  PCT0160008			
  PCT0160009			
  PCT0160010			
  PCT0160011			
  PCT0160012			
  PCT0160013			
  PCT0160014			
  PCT0160015			
  PCT0160016			
  PCT0160017			
  PCT0160018			
  PCT0160019			
  PCT0160020			
  PCT0160021			
  PCT0160022			
  PCT0160023			
  PCT0160024			
  PCT0160025			
  PCT0160026			
  PCT0170001			
  PCT0170002			
  PCT0170003			
  PCT0170004			
  PCT0170005			
  PCT0170006			
  PCT0170007			
  PCT0170008			
  PCT0170009			
  PCT0170010			
  PCT0170011			
  PCT0170012			
  PCT0170013			
  PCT0170014			
  PCT0170015			
  PCT0170016			
  PCT0170017			
  PCT0170018			
  PCT0180001			
  PCT0180002			
  PCT0180003			
  PCT0180004			
  PCT0180005			
  PCT0180006			
  PCT0180007			
  PCT0180008			
  PCT0180009			
  PCT0180010			
  PCT0180011			
  PCT0180012			
  PCT0180013			
  PCT0180014			
  PCT0180015			
  PCT0190001			
  PCT0190002			
  PCT0190003			
  PCT0190004			
  PCT0190005			
  PCT0190006			
  PCT0190007			
  PCT0190008			
  PCT0190009			
  PCT0190010			
  PCT0190011			
  PCT0200001			
  PCT0200002			
  PCT0200003			
  PCT0200004			
  PCT0200005			
  PCT0200006			
  PCT0200007			
  PCT0200008			
  PCT0200009			
  PCT0200010			
  PCT0200011			
  PCT0200012			
  PCT0200013			
  PCT0200014			
  PCT0200015			
  PCT0200016			
  PCT0200017			
  PCT0200018			
  PCT0200019			
  PCT0200020			
  PCT0200021			
  PCT0200022			
  PCT0200023			
  PCT0200024			
  PCT0200025			
  PCT0200026			
  PCT0200027			
  PCT0200028			
  PCT0200029			
  PCT0200030			
  PCT0200031			
  PCT0200032			
  PCT0210001			
  PCT0210002			
  PCT0210003			
  PCT0210004			
  PCT0210005			
  PCT0210006			
  PCT0210007			
  PCT0210008			
  PCT0210009			
  PCT0210010			
  PCT0210011			
  PCT0210012			
  PCT0210013			
  PCT0210014			
  PCT0210015			
  PCT0210016			
  PCT0210017			
  PCT0210018			
  PCT0210019			
  PCT0210020			
  PCT0210021			
  PCT0210022			
  PCT0210023			
  PCT0210024			
  PCT0210025			
  PCT0210026			
  PCT0210027			
  PCT0210028			
  PCT0210029			
  PCT0210030			
  PCT0210031			
  PCT0210032			
  PCT0210033			
  PCT0210034			
  PCT0210035			
  PCT0210036			
  PCT0210037			
  PCT0210038			
  PCT0210039			
  PCT0210040			
  PCT0210041			
  PCT0210042			
  PCT0210043			
  PCT0210044			
  PCT0210045			
  PCT0210046			
  PCT0210047			
  PCT0210048			
  PCT0210049			
  PCT0210050			
  PCT0210051			
  PCT0210052			
  PCT0210053			
  PCT0210054			
  PCT0210055			
  PCT0210056			
  PCT0210057			
  PCT0210058			
  PCT0210059			
  PCT0210060			
  PCT0210061			
  PCT0210062			
  PCT0210063			
  PCT0210064			
  PCT0210065			
  PCT0210066			
  PCT0210067			
  PCT0210068			
  PCT0210069			
  PCT0210070			
  PCT0210071			
  PCT0210072			
  PCT0210073			
  PCT0210074			
  PCT0210075			
  PCT0210076			
  PCT0210077			
  PCT0210078			
  PCT0210079			
  PCT0210080			
  PCT0210081			
  PCT0210082			
  PCT0210083			
  PCT0210084			
  PCT0210085			
  PCT0210086			
  PCT0210087			
  PCT0210088			
  PCT0210089			
  PCT0210090			
  PCT0210091			
  PCT0210092			
  PCT0210093			
  PCT0210094			
  PCT0210095			
  PCT0210096			
  PCT0210097			
  PCT0210098			
  PCT0210099			
  PCT0210100			
  PCT0210101			
  PCT0210102			
  PCT0210103			
  PCT0210104			
  PCT0210105			
  PCT0210106			
  PCT0210107			
  PCT0210108			
  PCT0210109			
  PCT0210110			
  PCT0210111			
  PCT0210112			
  PCT0210113			
  PCT0210114			
  PCT0210115			
  PCT0210116			
  PCT0210117			
  PCT0210118			
  PCT0210119			
  PCT0210120			
  PCT0210121			
  PCT0210122			
  PCT0210123			
  PCT0210124			
  PCT0210125			
  PCT0210126			
  PCT0210127			
  PCT0210128			
  PCT0210129			
  PCT0210130			
  PCT0210131			
  PCT0210132			
  PCT0210133			
  PCT0210134			
  PCT0210135			
  PCT0210136			
  PCT0210137			
  PCT0210138			
  PCT0210139			
  PCT0210140			
  PCT0210141			
  PCT0210142			
  PCT0210143			
  PCT0210144			
  PCT0210145			
  PCT0210146			
  PCT0210147			
  PCT0210148			
  PCT0210149			
  PCT0210150			
  PCT0210151			
  PCT0210152			
  PCT0210153			
  PCT0210154			
  PCT0210155			
  PCT0210156			
  PCT0210157			
  PCT0210158			
  PCT0210159			
  PCT0210160			
  PCT0210161			
  PCT0210162			
  PCT0210163			
  PCT0210164			
  PCT0210165			
  PCT0210166			
  PCT0210167			
  PCT0210168			
  PCT0210169			
  PCT0210170			
  PCT0210171			
  PCT0210172			
  PCT0210173			
  PCT0210174			
  PCT0210175			
  PCT0210176			
  PCT0210177			
  PCT0210178			
  PCT0210179			
  PCT0210180			
  PCT0210181			
  PCT0210182			
  PCT0210183			
  PCT0210184			
  PCT0210185			
  PCT0210186			
  PCT0210187			
  PCT0210188			
  PCT0210189			
  PCT0210190			
  PCT0210191			
  PCT0210192			
  PCT0210193			
  PCT0210194			
  PCT0210195			
  PCT0220001			
  PCT0220002			
  PCT0220003			
  PCT0220004			
  PCT0220005			
  PCT0220006			
  PCT0220007			
  PCT0220008			
  PCT0220009			
  PCT0220010			
  PCT0220011			
  PCT0220012			
  PCT0220013			
  PCT0220014			
  PCT0220015			
  PCT0220016			
  PCT0220017			
  PCT0220018			
  PCT0220019			
  PCT0220020			
  PCT0220021			
  PCT012A001			
  PCT012A002			
  PCT012A003			
  PCT012A004			
  PCT012A005			
  PCT012A006			
  PCT012A007			
  PCT012A008			
  PCT012A009			
  PCT012A010			
  PCT012A011			
  PCT012A012			
  PCT012A013			
  PCT012A014			
  PCT012A015			
  PCT012A016			
  PCT012A017			
  PCT012A018			
  PCT012A019			
  PCT012A020			
  PCT012A021			
  PCT012A022			
  PCT012A023			
  PCT012A024			
  PCT012A025			
  PCT012A026			
  PCT012A027			
  PCT012A028			
  PCT012A029			
  PCT012A030			
  PCT012A031			
  PCT012A032			
  PCT012A033			
  PCT012A034			
  PCT012A035			
  PCT012A036			
  PCT012A037			
  PCT012A038			
  PCT012A039			
  PCT012A040			
  PCT012A041			
  PCT012A042			
  PCT012A043			
  PCT012A044			
  PCT012A045			
  PCT012A046			
  PCT012A047			
  PCT012A048			
  PCT012A049			
  PCT012A050			
  PCT012A051			
  PCT012A052			
  PCT012A053			
  PCT012A054			
  PCT012A055			
  PCT012A056			
  PCT012A057			
  PCT012A058			
  PCT012A059			
  PCT012A060			
  PCT012A061			
  PCT012A062			
  PCT012A063			
  PCT012A064			
  PCT012A065			
  PCT012A066			
  PCT012A067			
  PCT012A068			
  PCT012A069			
  PCT012A070			
  PCT012A071			
  PCT012A072			
  PCT012A073			
  PCT012A074			
  PCT012A075			
  PCT012A076			
  PCT012A077			
  PCT012A078			
  PCT012A079			
  PCT012A080			
  PCT012A081			
  PCT012A082			
  PCT012A083			
  PCT012A084			
  PCT012A085			
  PCT012A086			
  PCT012A087			
  PCT012A088			
  PCT012A089			
  PCT012A090			
  PCT012A091			
  PCT012A092			
  PCT012A093			
  PCT012A094			
  PCT012A095			
  PCT012A096			
  PCT012A097			
  PCT012A098			
  PCT012A099			
  PCT012A100			
  PCT012A101			
  PCT012A102			
  PCT012A103			
  PCT012A104			
  PCT012A105			
  PCT012A106			
  PCT012A107			
  PCT012A108			
  PCT012A109			
  PCT012A110			
  PCT012A111			
  PCT012A112			
  PCT012A113			
  PCT012A114			
  PCT012A115			
  PCT012A116			
  PCT012A117			
  PCT012A118			
  PCT012A119			
  PCT012A120			
  PCT012A121			
  PCT012A122			
  PCT012A123			
  PCT012A124			
  PCT012A125			
  PCT012A126			
  PCT012A127			
  PCT012A128			
  PCT012A129			
  PCT012A130			
  PCT012A131			
  PCT012A132			
  PCT012A133			
  PCT012A134			
  PCT012A135			
  PCT012A136			
  PCT012A137			
  PCT012A138			
  PCT012A139			
  PCT012A140			
  PCT012A141			
  PCT012A142			
  PCT012A143			
  PCT012A144			
  PCT012A145			
  PCT012A146			
  PCT012A147			
  PCT012A148			
  PCT012A149			
  PCT012A150			
  PCT012A151			
  PCT012A152			
  PCT012A153			
  PCT012A154			
  PCT012A155			
  PCT012A156			
  PCT012A157			
  PCT012A158			
  PCT012A159			
  PCT012A160			
  PCT012A161			
  PCT012A162			
  PCT012A163			
  PCT012A164			
  PCT012A165			
  PCT012A166			
  PCT012A167			
  PCT012A168			
  PCT012A169			
  PCT012A170			
  PCT012A171			
  PCT012A172			
  PCT012A173			
  PCT012A174			
  PCT012A175			
  PCT012A176			
  PCT012A177			
  PCT012A178			
  PCT012A179			
  PCT012A180			
  PCT012A181			
  PCT012A182			
  PCT012A183			
  PCT012A184			
  PCT012A185			
  PCT012A186			
  PCT012A187			
  PCT012A188			
  PCT012A189			
  PCT012A190			
  PCT012A191			
  PCT012A192			
  PCT012A193			
  PCT012A194			
  PCT012A195			
  PCT012A196			
  PCT012A197			
  PCT012A198			
  PCT012A199			
  PCT012A200			
  PCT012A201			
  PCT012A202			
  PCT012A203			
  PCT012A204			
  PCT012A205			
  PCT012A206			
  PCT012A207			
  PCT012A208			
  PCT012A209			
  PCT012B001			
  PCT012B002			
  PCT012B003			
  PCT012B004			
  PCT012B005			
  PCT012B006			
  PCT012B007			
  PCT012B008			
  PCT012B009			
  PCT012B010			
  PCT012B011			
  PCT012B012			
  PCT012B013			
  PCT012B014			
  PCT012B015			
  PCT012B016			
  PCT012B017			
  PCT012B018			
  PCT012B019			
  PCT012B020			
  PCT012B021			
  PCT012B022			
  PCT012B023			
  PCT012B024			
  PCT012B025			
  PCT012B026			
  PCT012B027			
  PCT012B028			
  PCT012B029			
  PCT012B030			
  PCT012B031			
  PCT012B032			
  PCT012B033			
  PCT012B034			
  PCT012B035			
  PCT012B036			
  PCT012B037			
  PCT012B038			
  PCT012B039			
  PCT012B040			
  PCT012B041			
  PCT012B042			
  PCT012B043			
  PCT012B044			
  PCT012B045			
  PCT012B046			
  PCT012B047			
  PCT012B048			
  PCT012B049			
  PCT012B050			
  PCT012B051			
  PCT012B052			
  PCT012B053			
  PCT012B054			
  PCT012B055			
  PCT012B056			
  PCT012B057			
  PCT012B058			
  PCT012B059			
  PCT012B060			
  PCT012B061			
  PCT012B062			
  PCT012B063			
  PCT012B064			
  PCT012B065			
  PCT012B066			
  PCT012B067			
  PCT012B068			
  PCT012B069			
  PCT012B070			
  PCT012B071			
  PCT012B072			
  PCT012B073			
  PCT012B074			
  PCT012B075			
  PCT012B076			
  PCT012B077			
  PCT012B078			
  PCT012B079			
  PCT012B080			
  PCT012B081			
  PCT012B082			
  PCT012B083			
  PCT012B084			
  PCT012B085			
  PCT012B086			
  PCT012B087			
  PCT012B088			
  PCT012B089			
  PCT012B090			
  PCT012B091			
  PCT012B092			
  PCT012B093			
  PCT012B094			
  PCT012B095			
  PCT012B096			
  PCT012B097			
  PCT012B098			
  PCT012B099			
  PCT012B100			
  PCT012B101			
  PCT012B102			
  PCT012B103			
  PCT012B104			
  PCT012B105			
  PCT012B106			
  PCT012B107			
  PCT012B108			
  PCT012B109			
  PCT012B110			
  PCT012B111			
  PCT012B112			
  PCT012B113			
  PCT012B114			
  PCT012B115			
  PCT012B116			
  PCT012B117			
  PCT012B118			
  PCT012B119			
  PCT012B120			
  PCT012B121			
  PCT012B122			
  PCT012B123			
  PCT012B124			
  PCT012B125			
  PCT012B126			
  PCT012B127			
  PCT012B128			
  PCT012B129			
  PCT012B130			
  PCT012B131			
  PCT012B132			
  PCT012B133			
  PCT012B134			
  PCT012B135			
  PCT012B136			
  PCT012B137			
  PCT012B138			
  PCT012B139			
  PCT012B140			
  PCT012B141			
  PCT012B142			
  PCT012B143			
  PCT012B144			
  PCT012B145			
  PCT012B146			
  PCT012B147			
  PCT012B148			
  PCT012B149			
  PCT012B150			
  PCT012B151			
  PCT012B152			
  PCT012B153			
  PCT012B154			
  PCT012B155			
  PCT012B156			
  PCT012B157			
  PCT012B158			
  PCT012B159			
  PCT012B160			
  PCT012B161			
  PCT012B162			
  PCT012B163			
  PCT012B164			
  PCT012B165			
  PCT012B166			
  PCT012B167			
  PCT012B168			
  PCT012B169			
  PCT012B170			
  PCT012B171			
  PCT012B172			
  PCT012B173			
  PCT012B174			
  PCT012B175			
  PCT012B176			
  PCT012B177			
  PCT012B178			
  PCT012B179			
  PCT012B180			
  PCT012B181			
  PCT012B182			
  PCT012B183			
  PCT012B184			
  PCT012B185			
  PCT012B186			
  PCT012B187			
  PCT012B188			
  PCT012B189			
  PCT012B190			
  PCT012B191			
  PCT012B192			
  PCT012B193			
  PCT012B194			
  PCT012B195			
  PCT012B196			
  PCT012B197			
  PCT012B198			
  PCT012B199			
  PCT012B200			
  PCT012B201			
  PCT012B202			
  PCT012B203			
  PCT012B204			
  PCT012B205			
  PCT012B206			
  PCT012B207			
  PCT012B208			
  PCT012B209			
  PCT012C001			
  PCT012C002			
  PCT012C003			
  PCT012C004			
  PCT012C005			
  PCT012C006			
  PCT012C007			
  PCT012C008			
  PCT012C009			
  PCT012C010			
  PCT012C011			
  PCT012C012			
  PCT012C013			
  PCT012C014			
  PCT012C015			
  PCT012C016			
  PCT012C017			
  PCT012C018			
  PCT012C019			
  PCT012C020			
  PCT012C021			
  PCT012C022			
  PCT012C023			
  PCT012C024			
  PCT012C025			
  PCT012C026			
  PCT012C027			
  PCT012C028			
  PCT012C029			
  PCT012C030			
  PCT012C031			
  PCT012C032			
  PCT012C033			
  PCT012C034			
  PCT012C035			
  PCT012C036			
  PCT012C037			
  PCT012C038			
  PCT012C039			
  PCT012C040			
  PCT012C041			
  PCT012C042			
  PCT012C043			
  PCT012C044			
  PCT012C045			
  PCT012C046			
  PCT012C047			
  PCT012C048			
  PCT012C049			
  PCT012C050			
  PCT012C051			
  PCT012C052			
  PCT012C053			
  PCT012C054			
  PCT012C055			
  PCT012C056			
  PCT012C057			
  PCT012C058			
  PCT012C059			
  PCT012C060			
  PCT012C061			
  PCT012C062			
  PCT012C063			
  PCT012C064			
  PCT012C065			
  PCT012C066			
  PCT012C067			
  PCT012C068			
  PCT012C069			
  PCT012C070			
  PCT012C071			
  PCT012C072			
  PCT012C073			
  PCT012C074			
  PCT012C075			
  PCT012C076			
  PCT012C077			
  PCT012C078			
  PCT012C079			
  PCT012C080			
  PCT012C081			
  PCT012C082			
  PCT012C083			
  PCT012C084			
  PCT012C085			
  PCT012C086			
  PCT012C087			
  PCT012C088			
  PCT012C089			
  PCT012C090			
  PCT012C091			
  PCT012C092			
  PCT012C093			
  PCT012C094			
  PCT012C095			
  PCT012C096			
  PCT012C097			
  PCT012C098			
  PCT012C099			
  PCT012C100			
  PCT012C101			
  PCT012C102			
  PCT012C103			
  PCT012C104			
  PCT012C105			
  PCT012C106			
  PCT012C107			
  PCT012C108			
  PCT012C109			
  PCT012C110			
  PCT012C111			
  PCT012C112			
  PCT012C113			
  PCT012C114			
  PCT012C115			
  PCT012C116			
  PCT012C117			
  PCT012C118			
  PCT012C119			
  PCT012C120			
  PCT012C121			
  PCT012C122			
  PCT012C123			
  PCT012C124			
  PCT012C125			
  PCT012C126			
  PCT012C127			
  PCT012C128			
  PCT012C129			
  PCT012C130			
  PCT012C131			
  PCT012C132			
  PCT012C133			
  PCT012C134			
  PCT012C135			
  PCT012C136			
  PCT012C137			
  PCT012C138			
  PCT012C139			
  PCT012C140			
  PCT012C141			
  PCT012C142			
  PCT012C143			
  PCT012C144			
  PCT012C145			
  PCT012C146			
  PCT012C147			
  PCT012C148			
  PCT012C149			
  PCT012C150			
  PCT012C151			
  PCT012C152			
  PCT012C153			
  PCT012C154			
  PCT012C155			
  PCT012C156			
  PCT012C157			
  PCT012C158			
  PCT012C159			
  PCT012C160			
  PCT012C161			
  PCT012C162			
  PCT012C163			
  PCT012C164			
  PCT012C165			
  PCT012C166			
  PCT012C167			
  PCT012C168			
  PCT012C169			
  PCT012C170			
  PCT012C171			
  PCT012C172			
  PCT012C173			
  PCT012C174			
  PCT012C175			
  PCT012C176			
  PCT012C177			
  PCT012C178			
  PCT012C179			
  PCT012C180			
  PCT012C181			
  PCT012C182			
  PCT012C183			
  PCT012C184			
  PCT012C185			
  PCT012C186			
  PCT012C187			
  PCT012C188			
  PCT012C189			
  PCT012C190			
  PCT012C191			
  PCT012C192			
  PCT012C193			
  PCT012C194			
  PCT012C195			
  PCT012C196			
  PCT012C197			
  PCT012C198			
  PCT012C199			
  PCT012C200			
  PCT012C201			
  PCT012C202			
  PCT012C203			
  PCT012C204			
  PCT012C205			
  PCT012C206			
  PCT012C207			
  PCT012C208			
  PCT012C209			
  PCT012D001			
  PCT012D002			
  PCT012D003			
  PCT012D004			
  PCT012D005			
  PCT012D006			
  PCT012D007			
  PCT012D008			
  PCT012D009			
  PCT012D010			
  PCT012D011			
  PCT012D012			
  PCT012D013			
  PCT012D014			
  PCT012D015			
  PCT012D016			
  PCT012D017			
  PCT012D018			
  PCT012D019			
  PCT012D020			
  PCT012D021			
  PCT012D022			
  PCT012D023			
  PCT012D024			
  PCT012D025			
  PCT012D026			
  PCT012D027			
  PCT012D028			
  PCT012D029			
  PCT012D030			
  PCT012D031			
  PCT012D032			
  PCT012D033			
  PCT012D034			
  PCT012D035			
  PCT012D036			
  PCT012D037			
  PCT012D038			
  PCT012D039			
  PCT012D040			
  PCT012D041			
  PCT012D042			
  PCT012D043			
  PCT012D044			
  PCT012D045			
  PCT012D046			
  PCT012D047			
  PCT012D048			
  PCT012D049			
  PCT012D050			
  PCT012D051			
  PCT012D052			
  PCT012D053			
  PCT012D054			
  PCT012D055			
  PCT012D056			
  PCT012D057			
  PCT012D058			
  PCT012D059			
  PCT012D060			
  PCT012D061			
  PCT012D062			
  PCT012D063			
  PCT012D064			
  PCT012D065			
  PCT012D066			
  PCT012D067			
  PCT012D068			
  PCT012D069			
  PCT012D070			
  PCT012D071			
  PCT012D072			
  PCT012D073			
  PCT012D074			
  PCT012D075			
  PCT012D076			
  PCT012D077			
  PCT012D078			
  PCT012D079			
  PCT012D080			
  PCT012D081			
  PCT012D082			
  PCT012D083			
  PCT012D084			
  PCT012D085			
  PCT012D086			
  PCT012D087			
  PCT012D088			
  PCT012D089			
  PCT012D090			
  PCT012D091			
  PCT012D092			
  PCT012D093			
  PCT012D094			
  PCT012D095			
  PCT012D096			
  PCT012D097			
  PCT012D098			
  PCT012D099			
  PCT012D100			
  PCT012D101			
  PCT012D102			
  PCT012D103			
  PCT012D104			
  PCT012D105			
  PCT012D106			
  PCT012D107			
  PCT012D108			
  PCT012D109			
  PCT012D110			
  PCT012D111			
  PCT012D112			
  PCT012D113			
  PCT012D114			
  PCT012D115			
  PCT012D116			
  PCT012D117			
  PCT012D118			
  PCT012D119			
  PCT012D120			
  PCT012D121			
  PCT012D122			
  PCT012D123			
  PCT012D124			
  PCT012D125			
  PCT012D126			
  PCT012D127			
  PCT012D128			
  PCT012D129			
  PCT012D130			
  PCT012D131			
  PCT012D132			
  PCT012D133			
  PCT012D134			
  PCT012D135			
  PCT012D136			
  PCT012D137			
  PCT012D138			
  PCT012D139			
  PCT012D140			
  PCT012D141			
  PCT012D142			
  PCT012D143			
  PCT012D144			
  PCT012D145			
  PCT012D146			
  PCT012D147			
  PCT012D148			
  PCT012D149			
  PCT012D150			
  PCT012D151			
  PCT012D152			
  PCT012D153			
  PCT012D154			
  PCT012D155			
  PCT012D156			
  PCT012D157			
  PCT012D158			
  PCT012D159			
  PCT012D160			
  PCT012D161			
  PCT012D162			
  PCT012D163			
  PCT012D164			
  PCT012D165			
  PCT012D166			
  PCT012D167			
  PCT012D168			
  PCT012D169			
  PCT012D170			
  PCT012D171			
  PCT012D172			
  PCT012D173			
  PCT012D174			
  PCT012D175			
  PCT012D176			
  PCT012D177			
  PCT012D178			
  PCT012D179			
  PCT012D180			
  PCT012D181			
  PCT012D182			
  PCT012D183			
  PCT012D184			
  PCT012D185			
  PCT012D186			
  PCT012D187			
  PCT012D188			
  PCT012D189			
  PCT012D190			
  PCT012D191			
  PCT012D192			
  PCT012D193			
  PCT012D194			
  PCT012D195			
  PCT012D196			
  PCT012D197			
  PCT012D198			
  PCT012D199			
  PCT012D200			
  PCT012D201			
  PCT012D202			
  PCT012D203			
  PCT012D204			
  PCT012D205			
  PCT012D206			
  PCT012D207			
  PCT012D208			
  PCT012D209			
  PCT012E001			
  PCT012E002			
  PCT012E003			
  PCT012E004			
  PCT012E005			
  PCT012E006			
  PCT012E007			
  PCT012E008			
  PCT012E009			
  PCT012E010			
  PCT012E011			
  PCT012E012			
  PCT012E013			
  PCT012E014			
  PCT012E015			
  PCT012E016			
  PCT012E017			
  PCT012E018			
  PCT012E019			
  PCT012E020			
  PCT012E021			
  PCT012E022			
  PCT012E023			
  PCT012E024			
  PCT012E025			
  PCT012E026			
  PCT012E027			
  PCT012E028			
  PCT012E029			
  PCT012E030			
  PCT012E031			
  PCT012E032			
  PCT012E033			
  PCT012E034			
  PCT012E035			
  PCT012E036			
  PCT012E037			
  PCT012E038			
  PCT012E039			
  PCT012E040			
  PCT012E041			
  PCT012E042			
  PCT012E043			
  PCT012E044			
  PCT012E045			
  PCT012E046			
  PCT012E047			
  PCT012E048			
  PCT012E049			
  PCT012E050			
  PCT012E051			
  PCT012E052			
  PCT012E053			
  PCT012E054			
  PCT012E055			
  PCT012E056			
  PCT012E057			
  PCT012E058			
  PCT012E059			
  PCT012E060			
  PCT012E061			
  PCT012E062			
  PCT012E063			
  PCT012E064			
  PCT012E065			
  PCT012E066			
  PCT012E067			
  PCT012E068			
  PCT012E069			
  PCT012E070			
  PCT012E071			
  PCT012E072			
  PCT012E073			
  PCT012E074			
  PCT012E075			
  PCT012E076			
  PCT012E077			
  PCT012E078			
  PCT012E079			
  PCT012E080			
  PCT012E081			
  PCT012E082			
  PCT012E083			
  PCT012E084			
  PCT012E085			
  PCT012E086			
  PCT012E087			
  PCT012E088			
  PCT012E089			
  PCT012E090			
  PCT012E091			
  PCT012E092			
  PCT012E093			
  PCT012E094			
  PCT012E095			
  PCT012E096			
  PCT012E097			
  PCT012E098			
  PCT012E099			
  PCT012E100			
  PCT012E101			
  PCT012E102			
  PCT012E103			
  PCT012E104			
  PCT012E105			
  PCT012E106			
  PCT012E107			
  PCT012E108			
  PCT012E109			
  PCT012E110			
  PCT012E111			
  PCT012E112			
  PCT012E113			
  PCT012E114			
  PCT012E115			
  PCT012E116			
  PCT012E117			
  PCT012E118			
  PCT012E119			
  PCT012E120			
  PCT012E121			
  PCT012E122			
  PCT012E123			
  PCT012E124			
  PCT012E125			
  PCT012E126			
  PCT012E127			
  PCT012E128			
  PCT012E129			
  PCT012E130			
  PCT012E131			
  PCT012E132			
  PCT012E133			
  PCT012E134			
  PCT012E135			
  PCT012E136			
  PCT012E137			
  PCT012E138			
  PCT012E139			
  PCT012E140			
  PCT012E141			
  PCT012E142			
  PCT012E143			
  PCT012E144			
  PCT012E145			
  PCT012E146			
  PCT012E147			
  PCT012E148			
  PCT012E149			
  PCT012E150			
  PCT012E151			
  PCT012E152			
  PCT012E153			
  PCT012E154			
  PCT012E155			
  PCT012E156			
  PCT012E157			
  PCT012E158			
  PCT012E159			
  PCT012E160			
  PCT012E161			
  PCT012E162			
  PCT012E163			
  PCT012E164			
  PCT012E165			
  PCT012E166			
  PCT012E167			
  PCT012E168			
  PCT012E169			
  PCT012E170			
  PCT012E171			
  PCT012E172			
  PCT012E173			
  PCT012E174			
  PCT012E175			
  PCT012E176			
  PCT012E177			
  PCT012E178			
  PCT012E179			
  PCT012E180			
  PCT012E181			
  PCT012E182			
  PCT012E183			
  PCT012E184			
  PCT012E185			
  PCT012E186			
  PCT012E187			
  PCT012E188			
  PCT012E189			
  PCT012E190			
  PCT012E191			
  PCT012E192			
  PCT012E193			
  PCT012E194			
  PCT012E195			
  PCT012E196			
  PCT012E197			
  PCT012E198			
  PCT012E199			
  PCT012E200			
  PCT012E201			
  PCT012E202			
  PCT012E203			
  PCT012E204			
  PCT012E205			
  PCT012E206			
  PCT012E207			
  PCT012E208			
  PCT012E209			
  PCT012F001			
  PCT012F002			
  PCT012F003			
  PCT012F004			
  PCT012F005			
  PCT012F006			
  PCT012F007			
  PCT012F008			
  PCT012F009			
  PCT012F010			
  PCT012F011			
  PCT012F012			
  PCT012F013			
  PCT012F014			
  PCT012F015			
  PCT012F016			
  PCT012F017			
  PCT012F018			
  PCT012F019			
  PCT012F020			
  PCT012F021			
  PCT012F022			
  PCT012F023			
  PCT012F024			
  PCT012F025			
  PCT012F026			
  PCT012F027			
  PCT012F028			
  PCT012F029			
  PCT012F030			
  PCT012F031			
  PCT012F032			
  PCT012F033			
  PCT012F034			
  PCT012F035			
  PCT012F036			
  PCT012F037			
  PCT012F038			
  PCT012F039			
  PCT012F040			
  PCT012F041			
  PCT012F042			
  PCT012F043			
  PCT012F044			
  PCT012F045			
  PCT012F046			
  PCT012F047			
  PCT012F048			
  PCT012F049			
  PCT012F050			
  PCT012F051			
  PCT012F052			
  PCT012F053			
  PCT012F054			
  PCT012F055			
  PCT012F056			
  PCT012F057			
  PCT012F058			
  PCT012F059			
  PCT012F060			
  PCT012F061			
  PCT012F062			
  PCT012F063			
  PCT012F064			
  PCT012F065			
  PCT012F066			
  PCT012F067			
  PCT012F068			
  PCT012F069			
  PCT012F070			
  PCT012F071			
  PCT012F072			
  PCT012F073			
  PCT012F074			
  PCT012F075			
  PCT012F076			
  PCT012F077			
  PCT012F078			
  PCT012F079			
  PCT012F080			
  PCT012F081			
  PCT012F082			
  PCT012F083			
  PCT012F084			
  PCT012F085			
  PCT012F086			
  PCT012F087			
  PCT012F088			
  PCT012F089			
  PCT012F090			
  PCT012F091			
  PCT012F092			
  PCT012F093			
  PCT012F094			
  PCT012F095			
  PCT012F096			
  PCT012F097			
  PCT012F098			
  PCT012F099			
  PCT012F100			
  PCT012F101			
  PCT012F102			
  PCT012F103			
  PCT012F104			
  PCT012F105			
  PCT012F106			
  PCT012F107			
  PCT012F108			
  PCT012F109			
  PCT012F110			
  PCT012F111			
  PCT012F112			
  PCT012F113			
  PCT012F114			
  PCT012F115			
  PCT012F116			
  PCT012F117			
  PCT012F118			
  PCT012F119			
  PCT012F120			
  PCT012F121			
  PCT012F122			
  PCT012F123			
  PCT012F124			
  PCT012F125			
  PCT012F126			
  PCT012F127			
  PCT012F128			
  PCT012F129			
  PCT012F130			
  PCT012F131			
  PCT012F132			
  PCT012F133			
  PCT012F134			
  PCT012F135			
  PCT012F136			
  PCT012F137			
  PCT012F138			
  PCT012F139			
  PCT012F140			
  PCT012F141			
  PCT012F142			
  PCT012F143			
  PCT012F144			
  PCT012F145			
  PCT012F146			
  PCT012F147			
  PCT012F148			
  PCT012F149			
  PCT012F150			
  PCT012F151			
  PCT012F152			
  PCT012F153			
  PCT012F154			
  PCT012F155			
  PCT012F156			
  PCT012F157			
  PCT012F158			
  PCT012F159			
  PCT012F160			
  PCT012F161			
  PCT012F162			
  PCT012F163			
  PCT012F164			
  PCT012F165			
  PCT012F166			
  PCT012F167			
  PCT012F168			
  PCT012F169			
  PCT012F170			
  PCT012F171			
  PCT012F172			
  PCT012F173			
  PCT012F174			
  PCT012F175			
  PCT012F176			
  PCT012F177			
  PCT012F178			
  PCT012F179			
  PCT012F180			
  PCT012F181			
  PCT012F182			
  PCT012F183			
  PCT012F184			
  PCT012F185			
  PCT012F186			
  PCT012F187			
  PCT012F188			
  PCT012F189			
  PCT012F190			
  PCT012F191			
  PCT012F192			
  PCT012F193			
  PCT012F194			
  PCT012F195			
  PCT012F196			
  PCT012F197			
  PCT012F198			
  PCT012F199			
  PCT012F200			
  PCT012F201			
  PCT012F202			
  PCT012F203			
  PCT012F204			
  PCT012F205			
  PCT012F206			
  PCT012F207			
  PCT012F208			
  PCT012F209			
  PCT012G001			
  PCT012G002			
  PCT012G003			
  PCT012G004			
  PCT012G005			
  PCT012G006			
  PCT012G007			
  PCT012G008			
  PCT012G009			
  PCT012G010			
  PCT012G011			
  PCT012G012			
  PCT012G013			
  PCT012G014			
  PCT012G015			
  PCT012G016			
  PCT012G017			
  PCT012G018			
  PCT012G019			
  PCT012G020			
  PCT012G021			
  PCT012G022			
  PCT012G023			
  PCT012G024			
  PCT012G025			
  PCT012G026			
  PCT012G027			
  PCT012G028			
  PCT012G029			
  PCT012G030			
  PCT012G031			
  PCT012G032			
  PCT012G033			
  PCT012G034			
  PCT012G035			
  PCT012G036			
  PCT012G037			
  PCT012G038			
  PCT012G039			
  PCT012G040			
  PCT012G041			
  PCT012G042			
  PCT012G043			
  PCT012G044			
  PCT012G045			
  PCT012G046			
  PCT012G047			
  PCT012G048			
  PCT012G049			
  PCT012G050			
  PCT012G051			
  PCT012G052			
  PCT012G053			
  PCT012G054			
  PCT012G055			
  PCT012G056			
  PCT012G057			
  PCT012G058			
  PCT012G059			
  PCT012G060			
  PCT012G061			
  PCT012G062			
  PCT012G063			
  PCT012G064			
  PCT012G065			
  PCT012G066			
  PCT012G067			
  PCT012G068			
  PCT012G069			
  PCT012G070			
  PCT012G071			
  PCT012G072			
  PCT012G073			
  PCT012G074			
  PCT012G075			
  PCT012G076			
  PCT012G077			
  PCT012G078			
  PCT012G079			
  PCT012G080			
  PCT012G081			
  PCT012G082			
  PCT012G083			
  PCT012G084			
  PCT012G085			
  PCT012G086			
  PCT012G087			
  PCT012G088			
  PCT012G089			
  PCT012G090			
  PCT012G091			
  PCT012G092			
  PCT012G093			
  PCT012G094			
  PCT012G095			
  PCT012G096			
  PCT012G097			
  PCT012G098			
  PCT012G099			
  PCT012G100			
  PCT012G101			
  PCT012G102			
  PCT012G103			
  PCT012G104			
  PCT012G105			
  PCT012G106			
  PCT012G107			
  PCT012G108			
  PCT012G109			
  PCT012G110			
  PCT012G111			
  PCT012G112			
  PCT012G113			
  PCT012G114			
  PCT012G115			
  PCT012G116			
  PCT012G117			
  PCT012G118			
  PCT012G119			
  PCT012G120			
  PCT012G121			
  PCT012G122			
  PCT012G123			
  PCT012G124			
  PCT012G125			
  PCT012G126			
  PCT012G127			
  PCT012G128			
  PCT012G129			
  PCT012G130			
  PCT012G131			
  PCT012G132			
  PCT012G133			
  PCT012G134			
  PCT012G135			
  PCT012G136			
  PCT012G137			
  PCT012G138			
  PCT012G139			
  PCT012G140			
  PCT012G141			
  PCT012G142			
  PCT012G143			
  PCT012G144			
  PCT012G145			
  PCT012G146			
  PCT012G147			
  PCT012G148			
  PCT012G149			
  PCT012G150			
  PCT012G151			
  PCT012G152			
  PCT012G153			
  PCT012G154			
  PCT012G155			
  PCT012G156			
  PCT012G157			
  PCT012G158			
  PCT012G159			
  PCT012G160			
  PCT012G161			
  PCT012G162			
  PCT012G163			
  PCT012G164			
  PCT012G165			
  PCT012G166			
  PCT012G167			
  PCT012G168			
  PCT012G169			
  PCT012G170			
  PCT012G171			
  PCT012G172			
  PCT012G173			
  PCT012G174			
  PCT012G175			
  PCT012G176			
  PCT012G177			
  PCT012G178			
  PCT012G179			
  PCT012G180			
  PCT012G181			
  PCT012G182			
  PCT012G183			
  PCT012G184			
  PCT012G185			
  PCT012G186			
  PCT012G187			
  PCT012G188			
  PCT012G189			
  PCT012G190			
  PCT012G191			
  PCT012G192			
  PCT012G193			
  PCT012G194			
  PCT012G195			
  PCT012G196			
  PCT012G197			
  PCT012G198			
  PCT012G199			
  PCT012G200			
  PCT012G201			
  PCT012G202			
  PCT012G203			
  PCT012G204			
  PCT012G205			
  PCT012G206			
  PCT012G207			
  PCT012G208			
  PCT012G209			
  PCT012H001			
  PCT012H002			
  PCT012H003			
  PCT012H004			
  PCT012H005			
  PCT012H006			
  PCT012H007			
  PCT012H008			
  PCT012H009			
  PCT012H010			
  PCT012H011			
  PCT012H012			
  PCT012H013			
  PCT012H014			
  PCT012H015			
  PCT012H016			
  PCT012H017			
  PCT012H018			
  PCT012H019			
  PCT012H020			
  PCT012H021			
  PCT012H022			
  PCT012H023			
  PCT012H024			
  PCT012H025			
  PCT012H026			
  PCT012H027			
  PCT012H028			
  PCT012H029			
  PCT012H030			
  PCT012H031			
  PCT012H032			
  PCT012H033			
  PCT012H034			
  PCT012H035			
  PCT012H036			
  PCT012H037			
  PCT012H038			
  PCT012H039			
  PCT012H040			
  PCT012H041			
  PCT012H042			
  PCT012H043			
  PCT012H044			
  PCT012H045			
  PCT012H046			
  PCT012H047			
  PCT012H048			
  PCT012H049			
  PCT012H050			
  PCT012H051			
  PCT012H052			
  PCT012H053			
  PCT012H054			
  PCT012H055			
  PCT012H056			
  PCT012H057			
  PCT012H058			
  PCT012H059			
  PCT012H060			
  PCT012H061			
  PCT012H062			
  PCT012H063			
  PCT012H064			
  PCT012H065			
  PCT012H066			
  PCT012H067			
  PCT012H068			
  PCT012H069			
  PCT012H070			
  PCT012H071			
  PCT012H072			
  PCT012H073			
  PCT012H074			
  PCT012H075			
  PCT012H076			
  PCT012H077			
  PCT012H078			
  PCT012H079			
  PCT012H080			
  PCT012H081			
  PCT012H082			
  PCT012H083			
  PCT012H084			
  PCT012H085			
  PCT012H086			
  PCT012H087			
  PCT012H088			
  PCT012H089			
  PCT012H090			
  PCT012H091			
  PCT012H092			
  PCT012H093			
  PCT012H094			
  PCT012H095			
  PCT012H096			
  PCT012H097			
  PCT012H098			
  PCT012H099			
  PCT012H100			
  PCT012H101			
  PCT012H102			
  PCT012H103			
  PCT012H104			
  PCT012H105			
  PCT012H106			
  PCT012H107			
  PCT012H108			
  PCT012H109			
  PCT012H110			
  PCT012H111			
  PCT012H112			
  PCT012H113			
  PCT012H114			
  PCT012H115			
  PCT012H116			
  PCT012H117			
  PCT012H118			
  PCT012H119			
  PCT012H120			
  PCT012H121			
  PCT012H122			
  PCT012H123			
  PCT012H124			
  PCT012H125			
  PCT012H126			
  PCT012H127			
  PCT012H128			
  PCT012H129			
  PCT012H130			
  PCT012H131			
  PCT012H132			
  PCT012H133			
  PCT012H134			
  PCT012H135			
  PCT012H136			
  PCT012H137			
  PCT012H138			
  PCT012H139			
  PCT012H140			
  PCT012H141			
  PCT012H142			
  PCT012H143			
  PCT012H144			
  PCT012H145			
  PCT012H146			
  PCT012H147			
  PCT012H148			
  PCT012H149			
  PCT012H150			
  PCT012H151			
  PCT012H152			
  PCT012H153			
  PCT012H154			
  PCT012H155			
  PCT012H156			
  PCT012H157			
  PCT012H158			
  PCT012H159			
  PCT012H160			
  PCT012H161			
  PCT012H162			
  PCT012H163			
  PCT012H164			
  PCT012H165			
  PCT012H166			
  PCT012H167			
  PCT012H168			
  PCT012H169			
  PCT012H170			
  PCT012H171			
  PCT012H172			
  PCT012H173			
  PCT012H174			
  PCT012H175			
  PCT012H176			
  PCT012H177			
  PCT012H178			
  PCT012H179			
  PCT012H180			
  PCT012H181			
  PCT012H182			
  PCT012H183			
  PCT012H184			
  PCT012H185			
  PCT012H186			
  PCT012H187			
  PCT012H188			
  PCT012H189			
  PCT012H190			
  PCT012H191			
  PCT012H192			
  PCT012H193			
  PCT012H194			
  PCT012H195			
  PCT012H196			
  PCT012H197			
  PCT012H198			
  PCT012H199			
  PCT012H200			
  PCT012H201			
  PCT012H202			
  PCT012H203			
  PCT012H204			
  PCT012H205			
  PCT012H206			
  PCT012H207			
  PCT012H208			
  PCT012H209			
  PCT012I001			
  PCT012I002			
  PCT012I003			
  PCT012I004			
  PCT012I005			
  PCT012I006			
  PCT012I007			
  PCT012I008			
  PCT012I009			
  PCT012I010			
  PCT012I011			
  PCT012I012			
  PCT012I013			
  PCT012I014			
  PCT012I015			
  PCT012I016			
  PCT012I017			
  PCT012I018			
  PCT012I019			
  PCT012I020			
  PCT012I021			
  PCT012I022			
  PCT012I023			
  PCT012I024			
  PCT012I025			
  PCT012I026			
  PCT012I027			
  PCT012I028			
  PCT012I029			
  PCT012I030			
  PCT012I031			
  PCT012I032			
  PCT012I033			
  PCT012I034			
  PCT012I035			
  PCT012I036			
  PCT012I037			
  PCT012I038			
  PCT012I039			
  PCT012I040			
  PCT012I041			
  PCT012I042			
  PCT012I043			
  PCT012I044			
  PCT012I045			
  PCT012I046			
  PCT012I047			
  PCT012I048			
  PCT012I049			
  PCT012I050			
  PCT012I051			
  PCT012I052			
  PCT012I053			
  PCT012I054			
  PCT012I055			
  PCT012I056			
  PCT012I057			
  PCT012I058			
  PCT012I059			
  PCT012I060			
  PCT012I061			
  PCT012I062			
  PCT012I063			
  PCT012I064			
  PCT012I065			
  PCT012I066			
  PCT012I067			
  PCT012I068			
  PCT012I069			
  PCT012I070			
  PCT012I071			
  PCT012I072			
  PCT012I073			
  PCT012I074			
  PCT012I075			
  PCT012I076			
  PCT012I077			
  PCT012I078			
  PCT012I079			
  PCT012I080			
  PCT012I081			
  PCT012I082			
  PCT012I083			
  PCT012I084			
  PCT012I085			
  PCT012I086			
  PCT012I087			
  PCT012I088			
  PCT012I089			
  PCT012I090			
  PCT012I091			
  PCT012I092			
  PCT012I093			
  PCT012I094			
  PCT012I095			
  PCT012I096			
  PCT012I097			
  PCT012I098			
  PCT012I099			
  PCT012I100			
  PCT012I101			
  PCT012I102			
  PCT012I103			
  PCT012I104			
  PCT012I105			
  PCT012I106			
  PCT012I107			
  PCT012I108			
  PCT012I109			
  PCT012I110			
  PCT012I111			
  PCT012I112			
  PCT012I113			
  PCT012I114			
  PCT012I115			
  PCT012I116			
  PCT012I117			
  PCT012I118			
  PCT012I119			
  PCT012I120			
  PCT012I121			
  PCT012I122			
  PCT012I123			
  PCT012I124			
  PCT012I125			
  PCT012I126			
  PCT012I127			
  PCT012I128			
  PCT012I129			
  PCT012I130			
  PCT012I131			
  PCT012I132			
  PCT012I133			
  PCT012I134			
  PCT012I135			
  PCT012I136			
  PCT012I137			
  PCT012I138			
  PCT012I139			
  PCT012I140			
  PCT012I141			
  PCT012I142			
  PCT012I143			
  PCT012I144			
  PCT012I145			
  PCT012I146			
  PCT012I147			
  PCT012I148			
  PCT012I149			
  PCT012I150			
  PCT012I151			
  PCT012I152			
  PCT012I153			
  PCT012I154			
  PCT012I155			
  PCT012I156			
  PCT012I157			
  PCT012I158			
  PCT012I159			
  PCT012I160			
  PCT012I161			
  PCT012I162			
  PCT012I163			
  PCT012I164			
  PCT012I165			
  PCT012I166			
  PCT012I167			
  PCT012I168			
  PCT012I169			
  PCT012I170			
  PCT012I171			
  PCT012I172			
  PCT012I173			
  PCT012I174			
  PCT012I175			
  PCT012I176			
  PCT012I177			
  PCT012I178			
  PCT012I179			
  PCT012I180			
  PCT012I181			
  PCT012I182			
  PCT012I183			
  PCT012I184			
  PCT012I185			
  PCT012I186			
  PCT012I187			
  PCT012I188			
  PCT012I189			
  PCT012I190			
  PCT012I191			
  PCT012I192			
  PCT012I193			
  PCT012I194			
  PCT012I195			
  PCT012I196			
  PCT012I197			
  PCT012I198			
  PCT012I199			
  PCT012I200			
  PCT012I201			
  PCT012I202			
  PCT012I203			
  PCT012I204			
  PCT012I205			
  PCT012I206			
  PCT012I207			
  PCT012I208			
  PCT012I209			
  PCT012J001			
  PCT012J002			
  PCT012J003			
  PCT012J004			
  PCT012J005			
  PCT012J006			
  PCT012J007			
  PCT012J008			
  PCT012J009			
  PCT012J010			
  PCT012J011			
  PCT012J012			
  PCT012J013			
  PCT012J014			
  PCT012J015			
  PCT012J016			
  PCT012J017			
  PCT012J018			
  PCT012J019			
  PCT012J020			
  PCT012J021			
  PCT012J022			
  PCT012J023			
  PCT012J024			
  PCT012J025			
  PCT012J026			
  PCT012J027			
  PCT012J028			
  PCT012J029			
  PCT012J030			
  PCT012J031			
  PCT012J032			
  PCT012J033			
  PCT012J034			
  PCT012J035			
  PCT012J036			
  PCT012J037			
  PCT012J038			
  PCT012J039			
  PCT012J040			
  PCT012J041			
  PCT012J042			
  PCT012J043			
  PCT012J044			
  PCT012J045			
  PCT012J046			
  PCT012J047			
  PCT012J048			
  PCT012J049			
  PCT012J050			
  PCT012J051			
  PCT012J052			
  PCT012J053			
  PCT012J054			
  PCT012J055			
  PCT012J056			
  PCT012J057			
  PCT012J058			
  PCT012J059			
  PCT012J060			
  PCT012J061			
  PCT012J062			
  PCT012J063			
  PCT012J064			
  PCT012J065			
  PCT012J066			
  PCT012J067			
  PCT012J068			
  PCT012J069			
  PCT012J070			
  PCT012J071			
  PCT012J072			
  PCT012J073			
  PCT012J074			
  PCT012J075			
  PCT012J076			
  PCT012J077			
  PCT012J078			
  PCT012J079			
  PCT012J080			
  PCT012J081			
  PCT012J082			
  PCT012J083			
  PCT012J084			
  PCT012J085			
  PCT012J086			
  PCT012J087			
  PCT012J088			
  PCT012J089			
  PCT012J090			
  PCT012J091			
  PCT012J092			
  PCT012J093			
  PCT012J094			
  PCT012J095			
  PCT012J096			
  PCT012J097			
  PCT012J098			
  PCT012J099			
  PCT012J100			
  PCT012J101			
  PCT012J102			
  PCT012J103			
  PCT012J104			
  PCT012J105			
  PCT012J106			
  PCT012J107			
  PCT012J108			
  PCT012J109			
  PCT012J110			
  PCT012J111			
  PCT012J112			
  PCT012J113			
  PCT012J114			
  PCT012J115			
  PCT012J116			
  PCT012J117			
  PCT012J118			
  PCT012J119			
  PCT012J120			
  PCT012J121			
  PCT012J122			
  PCT012J123			
  PCT012J124			
  PCT012J125			
  PCT012J126			
  PCT012J127			
  PCT012J128			
  PCT012J129			
  PCT012J130			
  PCT012J131			
  PCT012J132			
  PCT012J133			
  PCT012J134			
  PCT012J135			
  PCT012J136			
  PCT012J137			
  PCT012J138			
  PCT012J139			
  PCT012J140			
  PCT012J141			
  PCT012J142			
  PCT012J143			
  PCT012J144			
  PCT012J145			
  PCT012J146			
  PCT012J147			
  PCT012J148			
  PCT012J149			
  PCT012J150			
  PCT012J151			
  PCT012J152			
  PCT012J153			
  PCT012J154			
  PCT012J155			
  PCT012J156			
  PCT012J157			
  PCT012J158			
  PCT012J159			
  PCT012J160			
  PCT012J161			
  PCT012J162			
  PCT012J163			
  PCT012J164			
  PCT012J165			
  PCT012J166			
  PCT012J167			
  PCT012J168			
  PCT012J169			
  PCT012J170			
  PCT012J171			
  PCT012J172			
  PCT012J173			
  PCT012J174			
  PCT012J175			
  PCT012J176			
  PCT012J177			
  PCT012J178			
  PCT012J179			
  PCT012J180			
  PCT012J181			
  PCT012J182			
  PCT012J183			
  PCT012J184			
  PCT012J185			
  PCT012J186			
  PCT012J187			
  PCT012J188			
  PCT012J189			
  PCT012J190			
  PCT012J191			
  PCT012J192			
  PCT012J193			
  PCT012J194			
  PCT012J195			
  PCT012J196			
  PCT012J197			
  PCT012J198			
  PCT012J199			
  PCT012J200			
  PCT012J201			
  PCT012J202			
  PCT012J203			
  PCT012J204			
  PCT012J205			
  PCT012J206			
  PCT012J207			
  PCT012J208			
  PCT012J209			
  PCT012K001			
  PCT012K002			
  PCT012K003			
  PCT012K004			
  PCT012K005			
  PCT012K006			
  PCT012K007			
  PCT012K008			
  PCT012K009			
  PCT012K010			
  PCT012K011			
  PCT012K012			
  PCT012K013			
  PCT012K014			
  PCT012K015			
  PCT012K016			
  PCT012K017			
  PCT012K018			
  PCT012K019			
  PCT012K020			
  PCT012K021			
  PCT012K022			
  PCT012K023			
  PCT012K024			
  PCT012K025			
  PCT012K026			
  PCT012K027			
  PCT012K028			
  PCT012K029			
  PCT012K030			
  PCT012K031			
  PCT012K032			
  PCT012K033			
  PCT012K034			
  PCT012K035			
  PCT012K036			
  PCT012K037			
  PCT012K038			
  PCT012K039			
  PCT012K040			
  PCT012K041			
  PCT012K042			
  PCT012K043			
  PCT012K044			
  PCT012K045			
  PCT012K046			
  PCT012K047			
  PCT012K048			
  PCT012K049			
  PCT012K050			
  PCT012K051			
  PCT012K052			
  PCT012K053			
  PCT012K054			
  PCT012K055			
  PCT012K056			
  PCT012K057			
  PCT012K058			
  PCT012K059			
  PCT012K060			
  PCT012K061			
  PCT012K062			
  PCT012K063			
  PCT012K064			
  PCT012K065			
  PCT012K066			
  PCT012K067			
  PCT012K068			
  PCT012K069			
  PCT012K070			
  PCT012K071			
  PCT012K072			
  PCT012K073			
  PCT012K074			
  PCT012K075			
  PCT012K076			
  PCT012K077			
  PCT012K078			
  PCT012K079			
  PCT012K080			
  PCT012K081			
  PCT012K082			
  PCT012K083			
  PCT012K084			
  PCT012K085			
  PCT012K086			
  PCT012K087			
  PCT012K088			
  PCT012K089			
  PCT012K090			
  PCT012K091			
  PCT012K092			
  PCT012K093			
  PCT012K094			
  PCT012K095			
  PCT012K096			
  PCT012K097			
  PCT012K098			
  PCT012K099			
  PCT012K100			
  PCT012K101			
  PCT012K102			
  PCT012K103			
  PCT012K104			
  PCT012K105			
  PCT012K106			
  PCT012K107			
  PCT012K108			
  PCT012K109			
  PCT012K110			
  PCT012K111			
  PCT012K112			
  PCT012K113			
  PCT012K114			
  PCT012K115			
  PCT012K116			
  PCT012K117			
  PCT012K118			
  PCT012K119			
  PCT012K120			
  PCT012K121			
  PCT012K122			
  PCT012K123			
  PCT012K124			
  PCT012K125			
  PCT012K126			
  PCT012K127			
  PCT012K128			
  PCT012K129			
  PCT012K130			
  PCT012K131			
  PCT012K132			
  PCT012K133			
  PCT012K134			
  PCT012K135			
  PCT012K136			
  PCT012K137			
  PCT012K138			
  PCT012K139			
  PCT012K140			
  PCT012K141			
  PCT012K142			
  PCT012K143			
  PCT012K144			
  PCT012K145			
  PCT012K146			
  PCT012K147			
  PCT012K148			
  PCT012K149			
  PCT012K150			
  PCT012K151			
  PCT012K152			
  PCT012K153			
  PCT012K154			
  PCT012K155			
  PCT012K156			
  PCT012K157			
  PCT012K158			
  PCT012K159			
  PCT012K160			
  PCT012K161			
  PCT012K162			
  PCT012K163			
  PCT012K164			
  PCT012K165			
  PCT012K166			
  PCT012K167			
  PCT012K168			
  PCT012K169			
  PCT012K170			
  PCT012K171			
  PCT012K172			
  PCT012K173			
  PCT012K174			
  PCT012K175			
  PCT012K176			
  PCT012K177			
  PCT012K178			
  PCT012K179			
  PCT012K180			
  PCT012K181			
  PCT012K182			
  PCT012K183			
  PCT012K184			
  PCT012K185			
  PCT012K186			
  PCT012K187			
  PCT012K188			
  PCT012K189			
  PCT012K190			
  PCT012K191			
  PCT012K192			
  PCT012K193			
  PCT012K194			
  PCT012K195			
  PCT012K196			
  PCT012K197			
  PCT012K198			
  PCT012K199			
  PCT012K200			
  PCT012K201			
  PCT012K202			
  PCT012K203			
  PCT012K204			
  PCT012K205			
  PCT012K206			
  PCT012K207			
  PCT012K208			
  PCT012K209			
  PCT012L001			
  PCT012L002			
  PCT012L003			
  PCT012L004			
  PCT012L005			
  PCT012L006			
  PCT012L007			
  PCT012L008			
  PCT012L009			
  PCT012L010			
  PCT012L011			
  PCT012L012			
  PCT012L013			
  PCT012L014			
  PCT012L015			
  PCT012L016			
  PCT012L017			
  PCT012L018			
  PCT012L019			
  PCT012L020			
  PCT012L021			
  PCT012L022			
  PCT012L023			
  PCT012L024			
  PCT012L025			
  PCT012L026			
  PCT012L027			
  PCT012L028			
  PCT012L029			
  PCT012L030			
  PCT012L031			
  PCT012L032			
  PCT012L033			
  PCT012L034			
  PCT012L035			
  PCT012L036			
  PCT012L037			
  PCT012L038			
  PCT012L039			
  PCT012L040			
  PCT012L041			
  PCT012L042			
  PCT012L043			
  PCT012L044			
  PCT012L045			
  PCT012L046			
  PCT012L047			
  PCT012L048			
  PCT012L049			
  PCT012L050			
  PCT012L051			
  PCT012L052			
  PCT012L053			
  PCT012L054			
  PCT012L055			
  PCT012L056			
  PCT012L057			
  PCT012L058			
  PCT012L059			
  PCT012L060			
  PCT012L061			
  PCT012L062			
  PCT012L063			
  PCT012L064			
  PCT012L065			
  PCT012L066			
  PCT012L067			
  PCT012L068			
  PCT012L069			
  PCT012L070			
  PCT012L071			
  PCT012L072			
  PCT012L073			
  PCT012L074			
  PCT012L075			
  PCT012L076			
  PCT012L077			
  PCT012L078			
  PCT012L079			
  PCT012L080			
  PCT012L081			
  PCT012L082			
  PCT012L083			
  PCT012L084			
  PCT012L085			
  PCT012L086			
  PCT012L087			
  PCT012L088			
  PCT012L089			
  PCT012L090			
  PCT012L091			
  PCT012L092			
  PCT012L093			
  PCT012L094			
  PCT012L095			
  PCT012L096			
  PCT012L097			
  PCT012L098			
  PCT012L099			
  PCT012L100			
  PCT012L101			
  PCT012L102			
  PCT012L103			
  PCT012L104			
  PCT012L105			
  PCT012L106			
  PCT012L107			
  PCT012L108			
  PCT012L109			
  PCT012L110			
  PCT012L111			
  PCT012L112			
  PCT012L113			
  PCT012L114			
  PCT012L115			
  PCT012L116			
  PCT012L117			
  PCT012L118			
  PCT012L119			
  PCT012L120			
  PCT012L121			
  PCT012L122			
  PCT012L123			
  PCT012L124			
  PCT012L125			
  PCT012L126			
  PCT012L127			
  PCT012L128			
  PCT012L129			
  PCT012L130			
  PCT012L131			
  PCT012L132			
  PCT012L133			
  PCT012L134			
  PCT012L135			
  PCT012L136			
  PCT012L137			
  PCT012L138			
  PCT012L139			
  PCT012L140			
  PCT012L141			
  PCT012L142			
  PCT012L143			
  PCT012L144			
  PCT012L145			
  PCT012L146			
  PCT012L147			
  PCT012L148			
  PCT012L149			
  PCT012L150			
  PCT012L151			
  PCT012L152			
  PCT012L153			
  PCT012L154			
  PCT012L155			
  PCT012L156			
  PCT012L157			
  PCT012L158			
  PCT012L159			
  PCT012L160			
  PCT012L161			
  PCT012L162			
  PCT012L163			
  PCT012L164			
  PCT012L165			
  PCT012L166			
  PCT012L167			
  PCT012L168			
  PCT012L169			
  PCT012L170			
  PCT012L171			
  PCT012L172			
  PCT012L173			
  PCT012L174			
  PCT012L175			
  PCT012L176			
  PCT012L177			
  PCT012L178			
  PCT012L179			
  PCT012L180			
  PCT012L181			
  PCT012L182			
  PCT012L183			
  PCT012L184			
  PCT012L185			
  PCT012L186			
  PCT012L187			
  PCT012L188			
  PCT012L189			
  PCT012L190			
  PCT012L191			
  PCT012L192			
  PCT012L193			
  PCT012L194			
  PCT012L195			
  PCT012L196			
  PCT012L197			
  PCT012L198			
  PCT012L199			
  PCT012L200			
  PCT012L201			
  PCT012L202			
  PCT012L203			
  PCT012L204			
  PCT012L205			
  PCT012L206			
  PCT012L207			
  PCT012L208			
  PCT012L209			
  PCT012M001			
  PCT012M002			
  PCT012M003			
  PCT012M004			
  PCT012M005			
  PCT012M006			
  PCT012M007			
  PCT012M008			
  PCT012M009			
  PCT012M010			
  PCT012M011			
  PCT012M012			
  PCT012M013			
  PCT012M014			
  PCT012M015			
  PCT012M016			
  PCT012M017			
  PCT012M018			
  PCT012M019			
  PCT012M020			
  PCT012M021			
  PCT012M022			
  PCT012M023			
  PCT012M024			
  PCT012M025			
  PCT012M026			
  PCT012M027			
  PCT012M028			
  PCT012M029			
  PCT012M030			
  PCT012M031			
  PCT012M032			
  PCT012M033			
  PCT012M034			
  PCT012M035			
  PCT012M036			
  PCT012M037			
  PCT012M038			
  PCT012M039			
  PCT012M040			
  PCT012M041			
  PCT012M042			
  PCT012M043			
  PCT012M044			
  PCT012M045			
  PCT012M046			
  PCT012M047			
  PCT012M048			
  PCT012M049			
  PCT012M050			
  PCT012M051			
  PCT012M052			
  PCT012M053			
  PCT012M054			
  PCT012M055			
  PCT012M056			
  PCT012M057			
  PCT012M058			
  PCT012M059			
  PCT012M060			
  PCT012M061			
  PCT012M062			
  PCT012M063			
  PCT012M064			
  PCT012M065			
  PCT012M066			
  PCT012M067			
  PCT012M068			
  PCT012M069			
  PCT012M070			
  PCT012M071			
  PCT012M072			
  PCT012M073			
  PCT012M074			
  PCT012M075			
  PCT012M076			
  PCT012M077			
  PCT012M078			
  PCT012M079			
  PCT012M080			
  PCT012M081			
  PCT012M082			
  PCT012M083			
  PCT012M084			
  PCT012M085			
  PCT012M086			
  PCT012M087			
  PCT012M088			
  PCT012M089			
  PCT012M090			
  PCT012M091			
  PCT012M092			
  PCT012M093			
  PCT012M094			
  PCT012M095			
  PCT012M096			
  PCT012M097			
  PCT012M098			
  PCT012M099			
  PCT012M100			
  PCT012M101			
  PCT012M102			
  PCT012M103			
  PCT012M104			
  PCT012M105			
  PCT012M106			
  PCT012M107			
  PCT012M108			
  PCT012M109			
  PCT012M110			
  PCT012M111			
  PCT012M112			
  PCT012M113			
  PCT012M114			
  PCT012M115			
  PCT012M116			
  PCT012M117			
  PCT012M118			
  PCT012M119			
  PCT012M120			
  PCT012M121			
  PCT012M122			
  PCT012M123			
  PCT012M124			
  PCT012M125			
  PCT012M126			
  PCT012M127			
  PCT012M128			
  PCT012M129			
  PCT012M130			
  PCT012M131			
  PCT012M132			
  PCT012M133			
  PCT012M134			
  PCT012M135			
  PCT012M136			
  PCT012M137			
  PCT012M138			
  PCT012M139			
  PCT012M140			
  PCT012M141			
  PCT012M142			
  PCT012M143			
  PCT012M144			
  PCT012M145			
  PCT012M146			
  PCT012M147			
  PCT012M148			
  PCT012M149			
  PCT012M150			
  PCT012M151			
  PCT012M152			
  PCT012M153			
  PCT012M154			
  PCT012M155			
  PCT012M156			
  PCT012M157			
  PCT012M158			
  PCT012M159			
  PCT012M160			
  PCT012M161			
  PCT012M162			
  PCT012M163			
  PCT012M164			
  PCT012M165			
  PCT012M166			
  PCT012M167			
  PCT012M168			
  PCT012M169			
  PCT012M170			
  PCT012M171			
  PCT012M172			
  PCT012M173			
  PCT012M174			
  PCT012M175			
  PCT012M176			
  PCT012M177			
  PCT012M178			
  PCT012M179			
  PCT012M180			
  PCT012M181			
  PCT012M182			
  PCT012M183			
  PCT012M184			
  PCT012M185			
  PCT012M186			
  PCT012M187			
  PCT012M188			
  PCT012M189			
  PCT012M190			
  PCT012M191			
  PCT012M192			
  PCT012M193			
  PCT012M194			
  PCT012M195			
  PCT012M196			
  PCT012M197			
  PCT012M198			
  PCT012M199			
  PCT012M200			
  PCT012M201			
  PCT012M202			
  PCT012M203			
  PCT012M204			
  PCT012M205			
  PCT012M206			
  PCT012M207			
  PCT012M208			
  PCT012M209			
  PCT012N001			
  PCT012N002			
  PCT012N003			
  PCT012N004			
  PCT012N005			
  PCT012N006			
  PCT012N007			
  PCT012N008			
  PCT012N009			
  PCT012N010			
  PCT012N011			
  PCT012N012			
  PCT012N013			
  PCT012N014			
  PCT012N015			
  PCT012N016			
  PCT012N017			
  PCT012N018			
  PCT012N019			
  PCT012N020			
  PCT012N021			
  PCT012N022			
  PCT012N023			
  PCT012N024			
  PCT012N025			
  PCT012N026			
  PCT012N027			
  PCT012N028			
  PCT012N029			
  PCT012N030			
  PCT012N031			
  PCT012N032			
  PCT012N033			
  PCT012N034			
  PCT012N035			
  PCT012N036			
  PCT012N037			
  PCT012N038			
  PCT012N039			
  PCT012N040			
  PCT012N041			
  PCT012N042			
  PCT012N043			
  PCT012N044			
  PCT012N045			
  PCT012N046			
  PCT012N047			
  PCT012N048			
  PCT012N049			
  PCT012N050			
  PCT012N051			
  PCT012N052			
  PCT012N053			
  PCT012N054			
  PCT012N055			
  PCT012N056			
  PCT012N057			
  PCT012N058			
  PCT012N059			
  PCT012N060			
  PCT012N061			
  PCT012N062			
  PCT012N063			
  PCT012N064			
  PCT012N065			
  PCT012N066			
  PCT012N067			
  PCT012N068			
  PCT012N069			
  PCT012N070			
  PCT012N071			
  PCT012N072			
  PCT012N073			
  PCT012N074			
  PCT012N075			
  PCT012N076			
  PCT012N077			
  PCT012N078			
  PCT012N079			
  PCT012N080			
  PCT012N081			
  PCT012N082			
  PCT012N083			
  PCT012N084			
  PCT012N085			
  PCT012N086			
  PCT012N087			
  PCT012N088			
  PCT012N089			
  PCT012N090			
  PCT012N091			
  PCT012N092			
  PCT012N093			
  PCT012N094			
  PCT012N095			
  PCT012N096			
  PCT012N097			
  PCT012N098			
  PCT012N099			
  PCT012N100			
  PCT012N101			
  PCT012N102			
  PCT012N103			
  PCT012N104			
  PCT012N105			
  PCT012N106			
  PCT012N107			
  PCT012N108			
  PCT012N109			
  PCT012N110			
  PCT012N111			
  PCT012N112			
  PCT012N113			
  PCT012N114			
  PCT012N115			
  PCT012N116			
  PCT012N117			
  PCT012N118			
  PCT012N119			
  PCT012N120			
  PCT012N121			
  PCT012N122			
  PCT012N123			
  PCT012N124			
  PCT012N125			
  PCT012N126			
  PCT012N127			
  PCT012N128			
  PCT012N129			
  PCT012N130			
  PCT012N131			
  PCT012N132			
  PCT012N133			
  PCT012N134			
  PCT012N135			
  PCT012N136			
  PCT012N137			
  PCT012N138			
  PCT012N139			
  PCT012N140			
  PCT012N141			
  PCT012N142			
  PCT012N143			
  PCT012N144			
  PCT012N145			
  PCT012N146			
  PCT012N147			
  PCT012N148			
  PCT012N149			
  PCT012N150			
  PCT012N151			
  PCT012N152			
  PCT012N153			
  PCT012N154			
  PCT012N155			
  PCT012N156			
  PCT012N157			
  PCT012N158			
  PCT012N159			
  PCT012N160			
  PCT012N161			
  PCT012N162			
  PCT012N163			
  PCT012N164			
  PCT012N165			
  PCT012N166			
  PCT012N167			
  PCT012N168			
  PCT012N169			
  PCT012N170			
  PCT012N171			
  PCT012N172			
  PCT012N173			
  PCT012N174			
  PCT012N175			
  PCT012N176			
  PCT012N177			
  PCT012N178			
  PCT012N179			
  PCT012N180			
  PCT012N181			
  PCT012N182			
  PCT012N183			
  PCT012N184			
  PCT012N185			
  PCT012N186			
  PCT012N187			
  PCT012N188			
  PCT012N189			
  PCT012N190			
  PCT012N191			
  PCT012N192			
  PCT012N193			
  PCT012N194			
  PCT012N195			
  PCT012N196			
  PCT012N197			
  PCT012N198			
  PCT012N199			
  PCT012N200			
  PCT012N201			
  PCT012N202			
  PCT012N203			
  PCT012N204			
  PCT012N205			
  PCT012N206			
  PCT012N207			
  PCT012N208			
  PCT012N209			
  PCT012O001			
  PCT012O002			
  PCT012O003			
  PCT012O004			
  PCT012O005			
  PCT012O006			
  PCT012O007			
  PCT012O008			
  PCT012O009			
  PCT012O010			
  PCT012O011			
  PCT012O012			
  PCT012O013			
  PCT012O014			
  PCT012O015			
  PCT012O016			
  PCT012O017			
  PCT012O018			
  PCT012O019			
  PCT012O020			
  PCT012O021			
  PCT012O022			
  PCT012O023			
  PCT012O024			
  PCT012O025			
  PCT012O026			
  PCT012O027			
  PCT012O028			
  PCT012O029			
  PCT012O030			
  PCT012O031			
  PCT012O032			
  PCT012O033			
  PCT012O034			
  PCT012O035			
  PCT012O036			
  PCT012O037			
  PCT012O038			
  PCT012O039			
  PCT012O040			
  PCT012O041			
  PCT012O042			
  PCT012O043			
  PCT012O044			
  PCT012O045			
  PCT012O046			
  PCT012O047			
  PCT012O048			
  PCT012O049			
  PCT012O050			
  PCT012O051			
  PCT012O052			
  PCT012O053			
  PCT012O054			
  PCT012O055			
  PCT012O056			
  PCT012O057			
  PCT012O058			
  PCT012O059			
  PCT012O060			
  PCT012O061			
  PCT012O062			
  PCT012O063			
  PCT012O064			
  PCT012O065			
  PCT012O066			
  PCT012O067			
  PCT012O068			
  PCT012O069			
  PCT012O070			
  PCT012O071			
  PCT012O072			
  PCT012O073			
  PCT012O074			
  PCT012O075			
  PCT012O076			
  PCT012O077			
  PCT012O078			
  PCT012O079			
  PCT012O080			
  PCT012O081			
  PCT012O082			
  PCT012O083			
  PCT012O084			
  PCT012O085			
  PCT012O086			
  PCT012O087			
  PCT012O088			
  PCT012O089			
  PCT012O090			
  PCT012O091			
  PCT012O092			
  PCT012O093			
  PCT012O094			
  PCT012O095			
  PCT012O096			
  PCT012O097			
  PCT012O098			
  PCT012O099			
  PCT012O100			
  PCT012O101			
  PCT012O102			
  PCT012O103			
  PCT012O104			
  PCT012O105			
  PCT012O106			
  PCT012O107			
  PCT012O108			
  PCT012O109			
  PCT012O110			
  PCT012O111			
  PCT012O112			
  PCT012O113			
  PCT012O114			
  PCT012O115			
  PCT012O116			
  PCT012O117			
  PCT012O118			
  PCT012O119			
  PCT012O120			
  PCT012O121			
  PCT012O122			
  PCT012O123			
  PCT012O124			
  PCT012O125			
  PCT012O126			
  PCT012O127			
  PCT012O128			
  PCT012O129			
  PCT012O130			
  PCT012O131			
  PCT012O132			
  PCT012O133			
  PCT012O134			
  PCT012O135			
  PCT012O136			
  PCT012O137			
  PCT012O138			
  PCT012O139			
  PCT012O140			
  PCT012O141			
  PCT012O142			
  PCT012O143			
  PCT012O144			
  PCT012O145			
  PCT012O146			
  PCT012O147			
  PCT012O148			
  PCT012O149			
  PCT012O150			
  PCT012O151			
  PCT012O152			
  PCT012O153			
  PCT012O154			
  PCT012O155			
  PCT012O156			
  PCT012O157			
  PCT012O158			
  PCT012O159			
  PCT012O160			
  PCT012O161			
  PCT012O162			
  PCT012O163			
  PCT012O164			
  PCT012O165			
  PCT012O166			
  PCT012O167			
  PCT012O168			
  PCT012O169			
  PCT012O170			
  PCT012O171			
  PCT012O172			
  PCT012O173			
  PCT012O174			
  PCT012O175			
  PCT012O176			
  PCT012O177			
  PCT012O178			
  PCT012O179			
  PCT012O180			
  PCT012O181			
  PCT012O182			
  PCT012O183			
  PCT012O184			
  PCT012O185			
  PCT012O186			
  PCT012O187			
  PCT012O188			
  PCT012O189			
  PCT012O190			
  PCT012O191			
  PCT012O192			
  PCT012O193			
  PCT012O194			
  PCT012O195			
  PCT012O196			
  PCT012O197			
  PCT012O198			
  PCT012O199			
  PCT012O200			
  PCT012O201			
  PCT012O202			
  PCT012O203			
  PCT012O204			
  PCT012O205			
  PCT012O206			
  PCT012O207			
  PCT012O208			
  PCT012O209			
  PCT013A001			
  PCT013A002			
  PCT013A003			
  PCT013A004			
  PCT013A005			
  PCT013A006			
  PCT013A007			
  PCT013A008			
  PCT013A009			
  PCT013A010			
  PCT013A011			
  PCT013A012			
  PCT013A013			
  PCT013A014			
  PCT013A015			
  PCT013A016			
  PCT013A017			
  PCT013A018			
  PCT013A019			
  PCT013A020			
  PCT013A021			
  PCT013A022			
  PCT013A023			
  PCT013A024			
  PCT013A025			
  PCT013A026			
  PCT013A027			
  PCT013A028			
  PCT013A029			
  PCT013A030			
  PCT013A031			
  PCT013A032			
  PCT013A033			
  PCT013A034			
  PCT013A035			
  PCT013A036			
  PCT013A037			
  PCT013A038			
  PCT013A039			
  PCT013A040			
  PCT013A041			
  PCT013A042			
  PCT013A043			
  PCT013A044			
  PCT013A045			
  PCT013A046			
  PCT013A047			
  PCT013A048			
  PCT013A049			
  PCT013B001			
  PCT013B002			
  PCT013B003			
  PCT013B004			
  PCT013B005			
  PCT013B006			
  PCT013B007			
  PCT013B008			
  PCT013B009			
  PCT013B010			
  PCT013B011			
  PCT013B012			
  PCT013B013			
  PCT013B014			
  PCT013B015			
  PCT013B016			
  PCT013B017			
  PCT013B018			
  PCT013B019			
  PCT013B020			
  PCT013B021			
  PCT013B022			
  PCT013B023			
  PCT013B024			
  PCT013B025			
  PCT013B026			
  PCT013B027			
  PCT013B028			
  PCT013B029			
  PCT013B030			
  PCT013B031			
  PCT013B032			
  PCT013B033			
  PCT013B034			
  PCT013B035			
  PCT013B036			
  PCT013B037			
  PCT013B038			
  PCT013B039			
  PCT013B040			
  PCT013B041			
  PCT013B042			
  PCT013B043			
  PCT013B044			
  PCT013B045			
  PCT013B046			
  PCT013B047			
  PCT013B048			
  PCT013B049			
  PCT013C001			
  PCT013C002			
  PCT013C003			
  PCT013C004			
  PCT013C005			
  PCT013C006			
  PCT013C007			
  PCT013C008			
  PCT013C009			
  PCT013C010			
  PCT013C011			
  PCT013C012			
  PCT013C013			
  PCT013C014			
  PCT013C015			
  PCT013C016			
  PCT013C017			
  PCT013C018			
  PCT013C019			
  PCT013C020			
  PCT013C021			
  PCT013C022			
  PCT013C023			
  PCT013C024			
  PCT013C025			
  PCT013C026			
  PCT013C027			
  PCT013C028			
  PCT013C029			
  PCT013C030			
  PCT013C031			
  PCT013C032			
  PCT013C033			
  PCT013C034			
  PCT013C035			
  PCT013C036			
  PCT013C037			
  PCT013C038			
  PCT013C039			
  PCT013C040			
  PCT013C041			
  PCT013C042			
  PCT013C043			
  PCT013C044			
  PCT013C045			
  PCT013C046			
  PCT013C047			
  PCT013C048			
  PCT013C049			
  PCT013D001			
  PCT013D002			
  PCT013D003			
  PCT013D004			
  PCT013D005			
  PCT013D006			
  PCT013D007			
  PCT013D008			
  PCT013D009			
  PCT013D010			
  PCT013D011			
  PCT013D012			
  PCT013D013			
  PCT013D014			
  PCT013D015			
  PCT013D016			
  PCT013D017			
  PCT013D018			
  PCT013D019			
  PCT013D020			
  PCT013D021			
  PCT013D022			
  PCT013D023			
  PCT013D024			
  PCT013D025			
  PCT013D026			
  PCT013D027			
  PCT013D028			
  PCT013D029			
  PCT013D030			
  PCT013D031			
  PCT013D032			
  PCT013D033			
  PCT013D034			
  PCT013D035			
  PCT013D036			
  PCT013D037			
  PCT013D038			
  PCT013D039			
  PCT013D040			
  PCT013D041			
  PCT013D042			
  PCT013D043			
  PCT013D044			
  PCT013D045			
  PCT013D046			
  PCT013D047			
  PCT013D048			
  PCT013D049			
  PCT013E001			
  PCT013E002			
  PCT013E003			
  PCT013E004			
  PCT013E005			
  PCT013E006			
  PCT013E007			
  PCT013E008			
  PCT013E009			
  PCT013E010			
  PCT013E011			
  PCT013E012			
  PCT013E013			
  PCT013E014			
  PCT013E015			
  PCT013E016			
  PCT013E017			
  PCT013E018			
  PCT013E019			
  PCT013E020			
  PCT013E021			
  PCT013E022			
  PCT013E023			
  PCT013E024			
  PCT013E025			
  PCT013E026			
  PCT013E027			
  PCT013E028			
  PCT013E029			
  PCT013E030			
  PCT013E031			
  PCT013E032			
  PCT013E033			
  PCT013E034			
  PCT013E035			
  PCT013E036			
  PCT013E037			
  PCT013E038			
  PCT013E039			
  PCT013E040			
  PCT013E041			
  PCT013E042			
  PCT013E043			
  PCT013E044			
  PCT013E045			
  PCT013E046			
  PCT013E047			
  PCT013E048			
  PCT013E049			
  PCT013F001			
  PCT013F002			
  PCT013F003			
  PCT013F004			
  PCT013F005			
  PCT013F006			
  PCT013F007			
  PCT013F008			
  PCT013F009			
  PCT013F010			
  PCT013F011			
  PCT013F012			
  PCT013F013			
  PCT013F014			
  PCT013F015			
  PCT013F016			
  PCT013F017			
  PCT013F018			
  PCT013F019			
  PCT013F020			
  PCT013F021			
  PCT013F022			
  PCT013F023			
  PCT013F024			
  PCT013F025			
  PCT013F026			
  PCT013F027			
  PCT013F028			
  PCT013F029			
  PCT013F030			
  PCT013F031			
  PCT013F032			
  PCT013F033			
  PCT013F034			
  PCT013F035			
  PCT013F036			
  PCT013F037			
  PCT013F038			
  PCT013F039			
  PCT013F040			
  PCT013F041			
  PCT013F042			
  PCT013F043			
  PCT013F044			
  PCT013F045			
  PCT013F046			
  PCT013F047			
  PCT013F048			
  PCT013F049			
  PCT013G001			
  PCT013G002			
  PCT013G003			
  PCT013G004			
  PCT013G005			
  PCT013G006			
  PCT013G007			
  PCT013G008			
  PCT013G009			
  PCT013G010			
  PCT013G011			
  PCT013G012			
  PCT013G013			
  PCT013G014			
  PCT013G015			
  PCT013G016			
  PCT013G017			
  PCT013G018			
  PCT013G019			
  PCT013G020			
  PCT013G021			
  PCT013G022			
  PCT013G023			
  PCT013G024			
  PCT013G025			
  PCT013G026			
  PCT013G027			
  PCT013G028			
  PCT013G029			
  PCT013G030			
  PCT013G031			
  PCT013G032			
  PCT013G033			
  PCT013G034			
  PCT013G035			
  PCT013G036			
  PCT013G037			
  PCT013G038			
  PCT013G039			
  PCT013G040			
  PCT013G041			
  PCT013G042			
  PCT013G043			
  PCT013G044			
  PCT013G045			
  PCT013G046			
  PCT013G047			
  PCT013G048			
  PCT013G049			
  PCT013H001			
  PCT013H002			
  PCT013H003			
  PCT013H004			
  PCT013H005			
  PCT013H006			
  PCT013H007			
  PCT013H008			
  PCT013H009			
  PCT013H010			
  PCT013H011			
  PCT013H012			
  PCT013H013			
  PCT013H014			
  PCT013H015			
  PCT013H016			
  PCT013H017			
  PCT013H018			
  PCT013H019			
  PCT013H020			
  PCT013H021			
  PCT013H022			
  PCT013H023			
  PCT013H024			
  PCT013H025			
  PCT013H026			
  PCT013H027			
  PCT013H028			
  PCT013H029			
  PCT013H030			
  PCT013H031			
  PCT013H032			
  PCT013H033			
  PCT013H034			
  PCT013H035			
  PCT013H036			
  PCT013H037			
  PCT013H038			
  PCT013H039			
  PCT013H040			
  PCT013H041			
  PCT013H042			
  PCT013H043			
  PCT013H044			
  PCT013H045			
  PCT013H046			
  PCT013H047			
  PCT013H048			
  PCT013H049			
  PCT013I001			
  PCT013I002			
  PCT013I003			
  PCT013I004			
  PCT013I005			
  PCT013I006			
  PCT013I007			
  PCT013I008			
  PCT013I009			
  PCT013I010			
  PCT013I011			
  PCT013I012			
  PCT013I013			
  PCT013I014			
  PCT013I015			
  PCT013I016			
  PCT013I017			
  PCT013I018			
  PCT013I019			
  PCT013I020			
  PCT013I021			
  PCT013I022			
  PCT013I023			
  PCT013I024			
  PCT013I025			
  PCT013I026			
  PCT013I027			
  PCT013I028			
  PCT013I029			
  PCT013I030			
  PCT013I031			
  PCT013I032			
  PCT013I033			
  PCT013I034			
  PCT013I035			
  PCT013I036			
  PCT013I037			
  PCT013I038			
  PCT013I039			
  PCT013I040			
  PCT013I041			
  PCT013I042			
  PCT013I043			
  PCT013I044			
  PCT013I045			
  PCT013I046			
  PCT013I047			
  PCT013I048			
  PCT013I049			
  PCT014A001			
  PCT014A002			
  PCT014A003			
  PCT014B001			
  PCT014B002			
  PCT014B003			
  PCT014C001			
  PCT014C002			
  PCT014C003			
  PCT014D001			
  PCT014D002			
  PCT014D003			
  PCT014E001			
  PCT014E002			
  PCT014E003			
  PCT014F001			
  PCT014F002			
  PCT014F003			
  PCT014G001			
  PCT014G002			
  PCT014G003			
  PCT014H001			
  PCT014H002			
  PCT014H003			
  PCT014I001			
  PCT014I002			
  PCT014I003			
  PCT019A001			
  PCT019A002			
  PCT019A003			
  PCT019A004			
  PCT019A005			
  PCT019A006			
  PCT019A007			
  PCT019A008			
  PCT019A009			
  PCT019A010			
  PCT019A011			
  PCT019B001			
  PCT019B002			
  PCT019B003			
  PCT019B004			
  PCT019B005			
  PCT019B006			
  PCT019B007			
  PCT019B008			
  PCT019B009			
  PCT019B010			
  PCT019B011			
  PCT019C001			
  PCT019C002			
  PCT019C003			
  PCT019C004			
  PCT019C005			
  PCT019C006			
  PCT019C007			
  PCT019C008			
  PCT019C009			
  PCT019C010			
  PCT019C011			
  PCT019D001			
  PCT019D002			
  PCT019D003			
  PCT019D004			
  PCT019D005			
  PCT019D006			
  PCT019D007			
  PCT019D008			
  PCT019D009			
  PCT019D010			
  PCT019D011			
  PCT019E001			
  PCT019E002			
  PCT019E003			
  PCT019E004			
  PCT019E005			
  PCT019E006			
  PCT019E007			
  PCT019E008			
  PCT019E009			
  PCT019E010			
  PCT019E011			
  PCT019F001			
  PCT019F002			
  PCT019F003			
  PCT019F004			
  PCT019F005			
  PCT019F006			
  PCT019F007			
  PCT019F008			
  PCT019F009			
  PCT019F010			
  PCT019F011			
  PCT019G001			
  PCT019G002			
  PCT019G003			
  PCT019G004			
  PCT019G005			
  PCT019G006			
  PCT019G007			
  PCT019G008			
  PCT019G009			
  PCT019G010			
  PCT019G011			
  PCT019H001			
  PCT019H002			
  PCT019H003			
  PCT019H004			
  PCT019H005			
  PCT019H006			
  PCT019H007			
  PCT019H008			
  PCT019H009			
  PCT019H010			
  PCT019H011			
  PCT019I001			
  PCT019I002			
  PCT019I003			
  PCT019I004			
  PCT019I005			
  PCT019I006			
  PCT019I007			
  PCT019I008			
  PCT019I009			
  PCT019I010			
  PCT019I011			
  PCT020A001			
  PCT020A002			
  PCT020A003			
  PCT020A004			
  PCT020A005			
  PCT020A006			
  PCT020A007			
  PCT020A008			
  PCT020A009			
  PCT020A010			
  PCT020A011			
  PCT020A012			
  PCT020A013			
  PCT020A014			
  PCT020A015			
  PCT020A016			
  PCT020A017			
  PCT020A018			
  PCT020A019			
  PCT020A020			
  PCT020A021			
  PCT020A022			
  PCT020A023			
  PCT020A024			
  PCT020A025			
  PCT020A026			
  PCT020A027			
  PCT020A028			
  PCT020A029			
  PCT020A030			
  PCT020A031			
  PCT020A032			
  PCT020B001			
  PCT020B002			
  PCT020B003			
  PCT020B004			
  PCT020B005			
  PCT020B006			
  PCT020B007			
  PCT020B008			
  PCT020B009			
  PCT020B010			
  PCT020B011			
  PCT020B012			
  PCT020B013			
  PCT020B014			
  PCT020B015			
  PCT020B016			
  PCT020B017			
  PCT020B018			
  PCT020B019			
  PCT020B020			
  PCT020B021			
  PCT020B022			
  PCT020B023			
  PCT020B024			
  PCT020B025			
  PCT020B026			
  PCT020B027			
  PCT020B028			
  PCT020B029			
  PCT020B030			
  PCT020B031			
  PCT020B032			
  PCT020C001			
  PCT020C002			
  PCT020C003			
  PCT020C004			
  PCT020C005			
  PCT020C006			
  PCT020C007			
  PCT020C008			
  PCT020C009			
  PCT020C010			
  PCT020C011			
  PCT020C012			
  PCT020C013			
  PCT020C014			
  PCT020C015			
  PCT020C016			
  PCT020C017			
  PCT020C018			
  PCT020C019			
  PCT020C020			
  PCT020C021			
  PCT020C022			
  PCT020C023			
  PCT020C024			
  PCT020C025			
  PCT020C026			
  PCT020C027			
  PCT020C028			
  PCT020C029			
  PCT020C030			
  PCT020C031			
  PCT020C032			
  PCT020D001			
  PCT020D002			
  PCT020D003			
  PCT020D004			
  PCT020D005			
  PCT020D006			
  PCT020D007			
  PCT020D008			
  PCT020D009			
  PCT020D010			
  PCT020D011			
  PCT020D012			
  PCT020D013			
  PCT020D014			
  PCT020D015			
  PCT020D016			
  PCT020D017			
  PCT020D018			
  PCT020D019			
  PCT020D020			
  PCT020D021			
  PCT020D022			
  PCT020D023			
  PCT020D024			
  PCT020D025			
  PCT020D026			
  PCT020D027			
  PCT020D028			
  PCT020D029			
  PCT020D030			
  PCT020D031			
  PCT020D032			
  PCT020E001			
  PCT020E002			
  PCT020E003			
  PCT020E004			
  PCT020E005			
  PCT020E006			
  PCT020E007			
  PCT020E008			
  PCT020E009			
  PCT020E010			
  PCT020E011			
  PCT020E012			
  PCT020E013			
  PCT020E014			
  PCT020E015			
  PCT020E016			
  PCT020E017			
  PCT020E018			
  PCT020E019			
  PCT020E020			
  PCT020E021			
  PCT020E022			
  PCT020E023			
  PCT020E024			
  PCT020E025			
  PCT020E026			
  PCT020E027			
  PCT020E028			
  PCT020E029			
  PCT020E030			
  PCT020E031			
  PCT020E032			
  PCT020F001			
  PCT020F002			
  PCT020F003			
  PCT020F004			
  PCT020F005			
  PCT020F006			
  PCT020F007			
  PCT020F008			
  PCT020F009			
  PCT020F010			
  PCT020F011			
  PCT020F012			
  PCT020F013			
  PCT020F014			
  PCT020F015			
  PCT020F016			
  PCT020F017			
  PCT020F018			
  PCT020F019			
  PCT020F020			
  PCT020F021			
  PCT020F022			
  PCT020F023			
  PCT020F024			
  PCT020F025			
  PCT020F026			
  PCT020F027			
  PCT020F028			
  PCT020F029			
  PCT020F030			
  PCT020F031			
  PCT020F032			
  PCT020G001			
  PCT020G002			
  PCT020G003			
  PCT020G004			
  PCT020G005			
  PCT020G006			
  PCT020G007			
  PCT020G008			
  PCT020G009			
  PCT020G010			
  PCT020G011			
  PCT020G012			
  PCT020G013			
  PCT020G014			
  PCT020G015			
  PCT020G016			
  PCT020G017			
  PCT020G018			
  PCT020G019			
  PCT020G020			
  PCT020G021			
  PCT020G022			
  PCT020G023			
  PCT020G024			
  PCT020G025			
  PCT020G026			
  PCT020G027			
  PCT020G028			
  PCT020G029			
  PCT020G030			
  PCT020G031			
  PCT020G032			
  PCT020H001			
  PCT020H002			
  PCT020H003			
  PCT020H004			
  PCT020H005			
  PCT020H006			
  PCT020H007			
  PCT020H008			
  PCT020H009			
  PCT020H010			
  PCT020H011			
  PCT020H012			
  PCT020H013			
  PCT020H014			
  PCT020H015			
  PCT020H016			
  PCT020H017			
  PCT020H018			
  PCT020H019			
  PCT020H020			
  PCT020H021			
  PCT020H022			
  PCT020H023			
  PCT020H024			
  PCT020H025			
  PCT020H026			
  PCT020H027			
  PCT020H028			
  PCT020H029			
  PCT020H030			
  PCT020H031			
  PCT020H032			
  PCT020I001			
  PCT020I002			
  PCT020I003			
  PCT020I004			
  PCT020I005			
  PCT020I006			
  PCT020I007			
  PCT020I008			
  PCT020I009			
  PCT020I010			
  PCT020I011			
  PCT020I012			
  PCT020I013			
  PCT020I014			
  PCT020I015			
  PCT020I016			
  PCT020I017			
  PCT020I018			
  PCT020I019			
  PCT020I020			
  PCT020I021			
  PCT020I022			
  PCT020I023			
  PCT020I024			
  PCT020I025			
  PCT020I026			
  PCT020I027			
  PCT020I028			
  PCT020I029			
  PCT020I030			
  PCT020I031			
  PCT020I032			
  PCT022A001			
  PCT022A002			
  PCT022A003			
  PCT022A004			
  PCT022A005			
  PCT022A006			
  PCT022A007			
  PCT022A008			
  PCT022A009			
  PCT022A010			
  PCT022A011			
  PCT022A012			
  PCT022A013			
  PCT022A014			
  PCT022A015			
  PCT022A016			
  PCT022A017			
  PCT022A018			
  PCT022A019			
  PCT022A020			
  PCT022A021			
  PCT022B001			
  PCT022B002			
  PCT022B003			
  PCT022B004			
  PCT022B005			
  PCT022B006			
  PCT022B007			
  PCT022B008			
  PCT022B009			
  PCT022B010			
  PCT022B011			
  PCT022B012			
  PCT022B013			
  PCT022B014			
  PCT022B015			
  PCT022B016			
  PCT022B017			
  PCT022B018			
  PCT022B019			
  PCT022B020			
  PCT022B021			
  PCT022C001			
  PCT022C002			
  PCT022C003			
  PCT022C004			
  PCT022C005			
  PCT022C006			
  PCT022C007			
  PCT022C008			
  PCT022C009			
  PCT022C010			
  PCT022C011			
  PCT022C012			
  PCT022C013			
  PCT022C014			
  PCT022C015			
  PCT022C016			
  PCT022C017			
  PCT022C018			
  PCT022C019			
  PCT022C020			
  PCT022C021			
  PCT022D001			
  PCT022D002			
  PCT022D003			
  PCT022D004			
  PCT022D005			
  PCT022D006			
  PCT022D007			
  PCT022D008			
  PCT022D009			
  PCT022D010			
  PCT022D011			
  PCT022D012			
  PCT022D013			
  PCT022D014			
  PCT022D015			
  PCT022D016			
  PCT022D017			
  PCT022D018			
  PCT022D019			
  PCT022D020			
  PCT022D021			
  PCT022E001			
  PCT022E002			
  PCT022E003			
  PCT022E004			
  PCT022E005			
  PCT022E006			
  PCT022E007			
  PCT022E008			
  PCT022E009			
  PCT022E010			
  PCT022E011			
  PCT022E012			
  PCT022E013			
  PCT022E014			
  PCT022E015			
  PCT022E016			
  PCT022E017			
  PCT022E018			
  PCT022E019			
  PCT022E020			
  PCT022E021			
  PCT022F001			
  PCT022F002			
  PCT022F003			
  PCT022F004			
  PCT022F005			
  PCT022F006			
  PCT022F007			
  PCT022F008			
  PCT022F009			
  PCT022F010			
  PCT022F011			
  PCT022F012			
  PCT022F013			
  PCT022F014			
  PCT022F015			
  PCT022F016			
  PCT022F017			
  PCT022F018			
  PCT022F019			
  PCT022F020			
  PCT022F021			
  PCT022G001			
  PCT022G002			
  PCT022G003			
  PCT022G004			
  PCT022G005			
  PCT022G006			
  PCT022G007			
  PCT022G008			
  PCT022G009			
  PCT022G010			
  PCT022G011			
  PCT022G012			
  PCT022G013			
  PCT022G014			
  PCT022G015			
  PCT022G016			
  PCT022G017			
  PCT022G018			
  PCT022G019			
  PCT022G020			
  PCT022G021			
  PCT022H001			
  PCT022H002			
  PCT022H003			
  PCT022H004			
  PCT022H005			
  PCT022H006			
  PCT022H007			
  PCT022H008			
  PCT022H009			
  PCT022H010			
  PCT022H011			
  PCT022H012			
  PCT022H013			
  PCT022H014			
  PCT022H015			
  PCT022H016			
  PCT022H017			
  PCT022H018			
  PCT022H019			
  PCT022H020			
  PCT022H021			
  PCT022I001			
  PCT022I002			
  PCT022I003			
  PCT022I004			
  PCT022I005			
  PCT022I006			
  PCT022I007			
  PCT022I008			
  PCT022I009			
  PCT022I010			
  PCT022I011			
  PCT022I012			
  PCT022I013			
  PCT022I014			
  PCT022I015			
  PCT022I016			
  PCT022I017			
  PCT022I018			
  PCT022I019			
  PCT022I020			
  PCT022I021			
  PCO0010001			
  PCO0010002			
  PCO0010003			
  PCO0010004			
  PCO0010005			
  PCO0010006			
  PCO0010007			
  PCO0010008			
  PCO0010009			
  PCO0010010			
  PCO0010011			
  PCO0010012			
  PCO0010013			
  PCO0010014			
  PCO0010015			
  PCO0010016			
  PCO0010017			
  PCO0010018			
  PCO0010019			
  PCO0010020			
  PCO0010021			
  PCO0010022			
  PCO0010023			
  PCO0010024			
  PCO0010025			
  PCO0010026			
  PCO0010027			
  PCO0010028			
  PCO0010029			
  PCO0010030			
  PCO0010031			
  PCO0010032			
  PCO0010033			
  PCO0010034			
  PCO0010035			
  PCO0010036			
  PCO0010037			
  PCO0010038			
  PCO0010039			
  PCO0020001			
  PCO0020002			
  PCO0020003			
  PCO0020004			
  PCO0020005			
  PCO0020006			
  PCO0020007			
  PCO0020008			
  PCO0020009			
  PCO0020010			
  PCO0020011			
  PCO0020012			
  PCO0020013			
  PCO0020014			
  PCO0020015			
  PCO0020016			
  PCO0020017			
  PCO0020018			
  PCO0020019			
  PCO0020020			
  PCO0020021			
  PCO0020022			
  PCO0020023			
  PCO0020024			
  PCO0020025			
  PCO0020026			
  PCO0020027			
  PCO0020028			
  PCO0020029			
  PCO0020030			
  PCO0020031			
  PCO0020032			
  PCO0020033			
  PCO0020034			
  PCO0020035			
  PCO0020036			
  PCO0020037			
  PCO0020038			
  PCO0020039			
  PCO0030001			
  PCO0030002			
  PCO0030003			
  PCO0030004			
  PCO0030005			
  PCO0030006			
  PCO0030007			
  PCO0030008			
  PCO0030009			
  PCO0030010			
  PCO0030011			
  PCO0030012			
  PCO0030013			
  PCO0030014			
  PCO0030015			
  PCO0030016			
  PCO0030017			
  PCO0030018			
  PCO0030019			
  PCO0030020			
  PCO0030021			
  PCO0030022			
  PCO0030023			
  PCO0030024			
  PCO0030025			
  PCO0030026			
  PCO0030027			
  PCO0030028			
  PCO0030029			
  PCO0030030			
  PCO0030031			
  PCO0030032			
  PCO0030033			
  PCO0030034			
  PCO0030035			
  PCO0030036			
  PCO0030037			
  PCO0030038			
  PCO0030039			
  PCO0040001			
  PCO0040002			
  PCO0040003			
  PCO0040004			
  PCO0040005			
  PCO0040006			
  PCO0040007			
  PCO0040008			
  PCO0040009			
  PCO0040010			
  PCO0040011			
  PCO0040012			
  PCO0040013			
  PCO0040014			
  PCO0040015			
  PCO0040016			
  PCO0040017			
  PCO0040018			
  PCO0040019			
  PCO0040020			
  PCO0040021			
  PCO0040022			
  PCO0040023			
  PCO0040024			
  PCO0040025			
  PCO0040026			
  PCO0040027			
  PCO0040028			
  PCO0040029			
  PCO0040030			
  PCO0040031			
  PCO0040032			
  PCO0040033			
  PCO0040034			
  PCO0040035			
  PCO0040036			
  PCO0040037			
  PCO0040038			
  PCO0040039			
  PCO0050001			
  PCO0050002			
  PCO0050003			
  PCO0050004			
  PCO0050005			
  PCO0050006			
  PCO0050007			
  PCO0050008			
  PCO0050009			
  PCO0050010			
  PCO0050011			
  PCO0050012			
  PCO0050013			
  PCO0050014			
  PCO0050015			
  PCO0050016			
  PCO0050017			
  PCO0050018			
  PCO0050019			
  PCO0050020			
  PCO0050021			
  PCO0050022			
  PCO0050023			
  PCO0050024			
  PCO0050025			
  PCO0050026			
  PCO0050027			
  PCO0050028			
  PCO0050029			
  PCO0050030			
  PCO0050031			
  PCO0050032			
  PCO0050033			
  PCO0050034			
  PCO0050035			
  PCO0050036			
  PCO0050037			
  PCO0050038			
  PCO0050039			
  PCO0060001			
  PCO0060002			
  PCO0060003			
  PCO0060004			
  PCO0060005			
  PCO0060006			
  PCO0060007			
  PCO0060008			
  PCO0060009			
  PCO0060010			
  PCO0060011			
  PCO0060012			
  PCO0060013			
  PCO0060014			
  PCO0060015			
  PCO0060016			
  PCO0060017			
  PCO0060018			
  PCO0060019			
  PCO0060020			
  PCO0060021			
  PCO0060022			
  PCO0060023			
  PCO0060024			
  PCO0060025			
  PCO0060026			
  PCO0060027			
  PCO0060028			
  PCO0060029			
  PCO0060030			
  PCO0060031			
  PCO0060032			
  PCO0060033			
  PCO0060034			
  PCO0060035			
  PCO0060036			
  PCO0060037			
  PCO0060038			
  PCO0060039			
  PCO0070001			
  PCO0070002			
  PCO0070003			
  PCO0070004			
  PCO0070005			
  PCO0070006			
  PCO0070007			
  PCO0070008			
  PCO0070009			
  PCO0070010			
  PCO0070011			
  PCO0070012			
  PCO0070013			
  PCO0070014			
  PCO0070015			
  PCO0070016			
  PCO0070017			
  PCO0070018			
  PCO0070019			
  PCO0070020			
  PCO0070021			
  PCO0070022			
  PCO0070023			
  PCO0070024			
  PCO0070025			
  PCO0070026			
  PCO0070027			
  PCO0070028			
  PCO0070029			
  PCO0070030			
  PCO0070031			
  PCO0070032			
  PCO0070033			
  PCO0070034			
  PCO0070035			
  PCO0070036			
  PCO0070037			
  PCO0070038			
  PCO0070039			
  PCO0080001			
  PCO0080002			
  PCO0080003			
  PCO0080004			
  PCO0080005			
  PCO0080006			
  PCO0080007			
  PCO0080008			
  PCO0080009			
  PCO0080010			
  PCO0080011			
  PCO0080012			
  PCO0080013			
  PCO0080014			
  PCO0080015			
  PCO0080016			
  PCO0080017			
  PCO0080018			
  PCO0080019			
  PCO0080020			
  PCO0080021			
  PCO0080022			
  PCO0080023			
  PCO0080024			
  PCO0080025			
  PCO0080026			
  PCO0080027			
  PCO0080028			
  PCO0080029			
  PCO0080030			
  PCO0080031			
  PCO0080032			
  PCO0080033			
  PCO0080034			
  PCO0080035			
  PCO0080036			
  PCO0080037			
  PCO0080038			
  PCO0080039			
  PCO0090001			
  PCO0090002			
  PCO0090003			
  PCO0090004			
  PCO0090005			
  PCO0090006			
  PCO0090007			
  PCO0090008			
  PCO0090009			
  PCO0090010			
  PCO0090011			
  PCO0090012			
  PCO0090013			
  PCO0090014			
  PCO0090015			
  PCO0090016			
  PCO0090017			
  PCO0090018			
  PCO0090019			
  PCO0090020			
  PCO0090021			
  PCO0090022			
  PCO0090023			
  PCO0090024			
  PCO0090025			
  PCO0090026			
  PCO0090027			
  PCO0090028			
  PCO0090029			
  PCO0090030			
  PCO0090031			
  PCO0090032			
  PCO0090033			
  PCO0090034			
  PCO0090035			
  PCO0090036			
  PCO0090037			
  PCO0090038			
  PCO0090039			
  PCO0100001			
  PCO0100002			
  PCO0100003			
  PCO0100004			
  PCO0100005			
  PCO0100006			
  PCO0100007			
  PCO0100008			
  PCO0100009			
  PCO0100010			
  PCO0100011			
  PCO0100012			
  PCO0100013			
  PCO0100014			
  PCO0100015			
  PCO0100016			
  PCO0100017			
  PCO0100018			
  PCO0100019			
  PCO0100020			
  PCO0100021			
  PCO0100022			
  PCO0100023			
  PCO0100024			
  PCO0100025			
  PCO0100026			
  PCO0100027			
  PCO0100028			
  PCO0100029			
  PCO0100030			
  PCO0100031			
  PCO0100032			
  PCO0100033			
  PCO0100034			
  PCO0100035			
  PCO0100036			
  PCO0100037			
  PCO0100038			
  PCO0100039			
  H00010001 			
  H0020001 			
  H0020002 			
  H0020003 			
  H0020004 			
  H0020005 			
  H0020006 			
  H0030001 			
  H0030002 			
  H0030003 			
  H0040001 			
  H0040002 			
  H0040003 			
  H0040004 			
  H0050001 			
  H0050002 			
  H0050003 			
  H0050004 			
  H0050005 			
  H0050006 			
  H0050007 			
  H0050008 			
  H0060001 			
  H0060002 			
  H0060003 			
  H0060004 			
  H0060005 			
  H0060006 			
  H0060007 			
  H0060008 			
  H0070001 			
  H0070002 			
  H0070003 			
  H0070004 			
  H0070005 			
  H0070006 			
  H0070007 			
  H0070008 			
  H0070009 			
  H0070010 			
  H0070011 			
  H0070012 			
  H0070013 			
  H0070014 			
  H0070015 			
  H0070016 			
  H0070017 			
  H0080001 			
  H0080002 			
  H0080003 			
  H0080004 			
  H0080005 			
  H0080006 			
  H0080007 			
  H0090001 			
  H0090002 			
  H0090003 			
  H0090004 			
  H0090005 			
  H0090006 			
  H0090007 			
  H0090008 			
  H0090009 			
  H0090010 			
  H0090011 			
  H0090012 			
  H0090013 			
  H0090014 			
  H0090015 			
  H0100001 			
  H0110001 			
  H0110002 			
  H0110003 			
  H0110004 			
  H0120001 			
  H0120002 			
  H0120003 			
  H0130001 			
  H0130002 			
  H0130003 			
  H0130004 			
  H0130005 			
  H0130006 			
  H0130007 			
  H0130008 			
  H0140001 			
  H0140002 			
  H0140003 			
  H0140004 			
  H0140005 			
  H0140006 			
  H0140007 			
  H0140008 			
  H0140009 			
  H0140010 			
  H0140011 			
  H0140012 			
  H0140013 			
  H0140014 			
  H0140015 			
  H0140016 			
  H0140017 			
  H0150001 			
  H0150002 			
  H0150003 			
  H0150004 			
  H0150005 			
  H0150006 			
  H0150007 			
  H0160001 			
  H0160002 			
  H0160003 			
  H0160004 			
  H0160005 			
  H0160006 			
  H0160007 			
  H0160008 			
  H0160009 			
  H0160010 			
  H0160011 			
  H0160012 			
  H0160013 			
  H0160014 			
  H0160015 			
  H0160016 			
  H0160017 			
  H0170001 			
  H0170002 			
  H0170003 			
  H0170004 			
  H0170005 			
  H0170006 			
  H0170007 			
  H0170008 			
  H0170009 			
  H0170010 			
  H0170011 			
  H0170012 			
  H0170013 			
  H0170014 			
  H0170015 			
  H0170016 			
  H0170017 			
  H0170018 			
  H0170019 			
  H0170020 			
  H0170021 			
  H0180001 			
  H0180002 			
  H0180003 			
  H0180004 			
  H0180005 			
  H0180006 			
  H0180007 			
  H0180008 			
  H0180009 			
  H0180010 			
  H0180011 			
  H0180012 			
  H0180013 			
  H0180014 			
  H0180015 			
  H0180016 			
  H0180017 			
  H0180018 			
  H0180019 			
  H0180020 			
  H0180021 			
  H0180022 			
  H0180023 			
  H0180024 			
  H0180025 			
  H0180026 			
  H0180027 			
  H0180028 			
  H0180029 			
  H0180030 			
  H0180031 			
  H0180032 			
  H0180033 			
  H0180034 			
  H0180035 			
  H0180036 			
  H0180037 			
  H0180038 			
  H0180039 			
  H0180040 			
  H0180041 			
  H0180042 			
  H0180043 			
  H0180044 			
  H0180045 			
  H0180046 			
  H0180047 			
  H0180048 			
  H0180049 			
  H0180050 			
  H0180051 			
  H0180052 			
  H0180053 			
  H0180054 			
  H0180055 			
  H0180056 			
  H0180057 			
  H0180058 			
  H0180059 			
  H0180060 			
  H0180061 			
  H0180062 			
  H0180063 			
  H0180064 			
  H0180065 			
  H0180066 			
  H0180067 			
  H0180068 			
  H0180069 			
  H0190001 			
  H0190002 			
  H0190003 			
  H0190004 			
  H0190005 			
  H0190006 			
  H0190007 			
  H0200001 			
  H0200002 			
  H0200003 			
  H0210001 			
  H0210002 			
  H0210003 			
  H0220001 			
  H0220002 			
  H0220003 			
  H011A0001 			
  H011A0002 			
  H011A0003 			
  H011A0004 			
  H011B0001 			
  H011B0002 			
  H011B0003 			
  H011B0004 			
  H011C0001 			
  H011C0002 			
  H011C0003 			
  H011C0004 			
  H011D0001 			
  H011D0002 			
  H011D0003 			
  H011D0004 			
  H011E0001 			
  H011E0002 			
  H011E0003 			
  H011E0004 			
  H011F0001 			
  H011F0002 			
  H011F0003 			
  H011F0004 			
  H011G0001 			
  H011G0002 			
  H011G0003 			
  H011G0004 			
  H011H0001 			
  H011H0002 			
  H011H0003 			
  H011H0004 			
  H011I0001 			
  H011I0002 			
  H011I0003 			
  H011I0004 			
  H012A0001 			
  H012A0002 			
  H012A0003 			
  H012B0001 			
  H012B0002 			
  H012B0003 			
  H012C0001 			
  H012C0002 			
  H012C0003 			
  H012D0001 			
  H012D0002 			
  H012D0003 			
  H012E0001 			
  H012E0002 			
  H012E0003 			
  H012F0001 			
  H012F0002 			
  H012F0003 			
  H012G0001 			
  H012G0002 			
  H012G0003 			
  H012H0001 			
  H012H0002 			
  H012H0003 			
  H012I0001 			
  H012I0002 			
  H012I0003 			
  H016A0001 			
  H016A0002 			
  H016A0003 			
  H016A0004 			
  H016A0005 			
  H016A0006 			
  H016A0007 			
  H016A0008 			
  H016A0009 			
  H016A0010 			
  H016A0011 			
  H016A0012 			
  H016A0013 			
  H016A0014 			
  H016A0015 			
  H016A0016 			
  H016A0017 			
  H016B0001 			
  H016B0002 			
  H016B0003 			
  H016B0004 			
  H016B0005 			
  H016B0006 			
  H016B0007 			
  H016B0008 			
  H016B0009 			
  H016B0010 			
  H016B0011 			
  H016B0012 			
  H016B0013 			
  H016B0014 			
  H016B0015 			
  H016B0016 			
  H016B0017 			
  H016C0001 			
  H016C0002 			
  H016C0003 			
  H016C0004 			
  H016C0005 			
  H016C0006 			
  H016C0007 			
  H016C0008 			
  H016C0009 			
  H016C0010 			
  H016C0011 			
  H016C0012 			
  H016C0013 			
  H016C0014 			
  H016C0015 			
  H016C0016 			
  H016C0017 			
  H016D0001 			
  H016D0002 			
  H016D0003 			
  H016D0004 			
  H016D0005 			
  H016D0006 			
  H016D0007 			
  H016D0008 			
  H016D0009 			
  H016D0010 			
  H016D0011 			
  H016D0012 			
  H016D0013 			
  H016D0014 			
  H016D0015 			
  H016D0016 			
  H016D0017 			
  H016E0001 			
  H016E0002 			
  H016E0003 			
  H016E0004 			
  H016E0005 			
  H016E0006 			
  H016E0007 			
  H016E0008 			
  H016E0009 			
  H016E0010 			
  H016E0011 			
  H016E0012 			
  H016E0013 			
  H016E0014 			
  H016E0015 			
  H016E0016 			
  H016E0017 			
  H016F0001 			
  H016F0002 			
  H016F0003 			
  H016F0004 			
  H016F0005 			
  H016F0006 			
  H016F0007 			
  H016F0008 			
  H016F0009 			
  H016F0010 			
  H016F0011 			
  H016F0012 			
  H016F0013 			
  H016F0014 			
  H016F0015 			
  H016F0016 			
  H016F0017 			
  H016G0001 			
  H016G0002 			
  H016G0003 			
  H016G0004 			
  H016G0005 			
  H016G0006 			
  H016G0007 			
  H016G0008 			
  H016G0009 			
  H016G0010 			
  H016G0011 			
  H016G0012 			
  H016G0013 			
  H016G0014 			
  H016G0015 			
  H016G0016 			
  H016G0017 			
  H016H0001 			
  H016H0002 			
  H016H0003 			
  H016H0004 			
  H016H0005 			
  H016H0006 			
  H016H0007 			
  H016H0008 			
  H016H0009 			
  H016H0010 			
  H016H0011 			
  H016H0012 			
  H016H0013 			
  H016H0014 			
  H016H0015 			
  H016H0016 			
  H016H0017 			
  H016I0001 			
  H016I0002 			
  H016I0003 			
  H016I0004 			
  H016I0005 			
  H016I0006 			
  H016I0007 			
  H016I0008 			
  H016I0009 			
  H016I0010 			
  H016I0011 			
  H016I0012 			
  H016I0013 			
  H016I0014 			
  H016I0015 			
  H016I0016 			
  H016I0017 			
  H017A0001 			
  H017A0002 			
  H017A0003 			
  H017A0004 			
  H017A0005 			
  H017A0006 			
  H017A0007 			
  H017A0008 			
  H017A0009 			
  H017A0010 			
  H017A0011 			
  H017A0012 			
  H017A0013 			
  H017A0014 			
  H017A0015 			
  H017A0016 			
  H017A0017 			
  H017A0018 			
  H017A0019 			
  H017A0020 			
  H017A0021 			
  H017B0001 			
  H017B0002 			
  H017B0003 			
  H017B0004 			
  H017B0005 			
  H017B0006 			
  H017B0007 			
  H017B0008 			
  H017B0009 			
  H017B0010 			
  H017B0011 			
  H017B0012 			
  H017B0013 			
  H017B0014 			
  H017B0015 			
  H017B0016 			
  H017B0017 			
  H017B0018 			
  H017B0019 			
  H017B0020 			
  H017B0021 			
  H017C0001 			
  H017C0002 			
  H017C0003 			
  H017C0004 			
  H017C0005 			
  H017C0006 			
  H017C0007 			
  H017C0008 			
  H017C0009 			
  H017C0010 			
  H017C0011 			
  H017C0012 			
  H017C0013 			
  H017C0014 			
  H017C0015 			
  H017C0016 			
  H017C0017 			
  H017C0018 			
  H017C0019 			
  H017C0020 			
  H017C0021 			
  H017D0001 			
  H017D0002 			
  H017D0003 			
  H017D0004 			
  H017D0005 			
  H017D0006 			
  H017D0007 			
  H017D0008 			
  H017D0009 			
  H017D0010 			
  H017D0011 			
  H017D0012 			
  H017D0013 			
  H017D0014 			
  H017D0015 			
  H017D0016 			
  H017D0017 			
  H017D0018 			
  H017D0019 			
  H017D0020 			
  H017D0021 			
  H017E0001 			
  H017E0002 			
  H017E0003 			
  H017E0004 			
  H017E0005 			
  H017E0006 			
  H017E0007 			
  H017E0008 			
  H017E0009 			
  H017E0010 			
  H017E0011 			
  H017E0012 			
  H017E0013 			
  H017E0014 			
  H017E0015 			
  H017E0016 			
  H017E0017 			
  H017E0018 			
  H017E0019 			
  H017E0020 			
  H017E0021 			
  H017F0001 			
  H017F0002 			
  H017F0003 			
  H017F0004 			
  H017F0005 			
  H017F0006 			
  H017F0007 			
  H017F0008 			
  H017F0009 			
  H017F0010 			
  H017F0011 			
  H017F0012 			
  H017F0013 			
  H017F0014 			
  H017F0015 			
  H017F0016 			
  H017F0017 			
  H017F0018 			
  H017F0019 			
  H017F0020 			
  H017F0021 			
  H017G0001 			
  H017G0002 			
  H017G0003 			
  H017G0004 			
  H017G0005 			
  H017G0006 			
  H017G0007 			
  H017G0008 			
  H017G0009 			
  H017G0010 			
  H017G0011 			
  H017G0012 			
  H017G0013 			
  H017G0014 			
  H017G0015 			
  H017G0016 			
  H017G0017 			
  H017G0018 			
  H017G0019 			
  H017G0020 			
  H017G0021 			
  H017H0001 			
  H017H0002 			
  H017H0003 			
  H017H0004 			
  H017H0005 			
  H017H0006 			
  H017H0007 			
  H017H0008 			
  H017H0009 			
  H017H0010 			
  H017H0011 			
  H017H0012 			
  H017H0013 			
  H017H0014 			
  H017H0015 			
  H017H0016 			
  H017H0017 			
  H017H0018 			
  H017H0019 			
  H017H0020 			
  H017H0021 			
  H017I0001 			
  H017I0002 			
  H017I0003 			
  H017I0004 			
  H017I0005 			
  H017I0006 			
  H017I0007 			
  H017I0008 			
  H017I0009 			
  H017I0010 			
  H017I0011 			
  H017I0012 			
  H017I0013 			
  H017I0014 			
  H017I0015 			
  H017I0016 			
  H017I0017 			
  H017I0018 			
  H017I0019 			
  H017I0020 			
  H017I0021 			
  HCT0010001			
  HCT0010002			
  HCT0010003			
  HCT0010004			
  HCT0010005			
  HCT0010006			
  HCT0010007			
  HCT0010008			
  HCT0010009			
  HCT0010010			
  HCT0010011			
  HCT0010012			
  HCT0010013			
  HCT0010014			
  HCT0010015			
  HCT0010016			
  HCT0010017			
  HCT0010018			
  HCT0010019			
  HCT0010020			
  HCT0010021			
  HCT0010022			
  HCT0010023			
  HCT0010024			
  HCT0010025			
  HCT0010026			
  HCT0010027			
  HCT0010028			
  HCT0010029			
  HCT0010030			
  HCT0010031			
  HCT0010032			
  HCT0010033			
  HCT0010034			
  HCT0010035			
  HCT0020001			
  HCT0020002			
  HCT0020003			
  HCT0020004			
  HCT0020005			
  HCT0020006			
  HCT0020007			
  HCT0020008			
  HCT0020009			
  HCT0020010			
  HCT0020011			
  HCT0020012			
  HCT0020013			
  HCT0030001			
  HCT0030002			
  HCT0030003			
  HCT0030004			
  HCT0030005			
  HCT0030006			
  HCT0030007			
  HCT0030008			
  HCT0030009			
  HCT0030010			
  HCT0030011			
  HCT0030012			
  HCT0030013			
  HCT0040001			
  HCT0040002			
  HCT0040003			
  HCT0040004			
  HCT0040005			
  HCT0040006			
  HCT0040007			
  HCT0040008			
  HCT0040009			
  HCT0040010			
  HCT0040011			
  HCT0040012			
  HCT0040013			
  PCT0230001			
  PCT0230002			
  PCT0230003			
  PCT0230004			
  PCT0230005			
  PCT0230006			
  PCT0230007			
  PCT0230008			
  PCT0230009			
  PCT0230010			
  PCT0230011			
  PCT0230012			
  PCT0230013			
  PCT0230014			
  PCT0230015			
  PCT0230016			
  PCT0230017			
  PCT0230018			
  PCT0230019			
  PCT0230020			
  PCT0230021			
  PCT0230022			
  PCT0230023			
  PCT0230024			
  PCT0240001			
  PCT0240002			
  PCT0240003			
  PCT0240004			
  PCT0240005			
  PCT0240006			
  PCT0240007			
  PCT0240008			
  PCT0240009			
  PCT0240010			
  PCT0240011			
  PCT0240012			
  PCT0240013			
  PCT0240014			
  PCT0240015			
  PCT0240016			
  PCT0240017			
  PCT0240018			
  PCT0240019			
  PCT0240020			
  PCT0240021			
  PCT0240022			
  PCT0240023			
;			
RUN;			