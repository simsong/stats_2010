https://www2.census.gov/geo/docs/reference/grfc/

```
sqlite> select p1,p2,gpop,ghouses,bcount,name from (select b.p1,b.p2,sum(a.pop) as gpop,sum(a.houses) as ghouses,count(*) as bcount from blocks a left join table4 b on a.state=b.state and a.logrecno=b.logrecno where
 (a.pop+a.houses)>0 group by p1,p2 having gpop<1000 order by gpop) as t1 left join geo geo on substr(t1.p1,2,2)=state and t1.p2=aianhh and geo.sumlev=550 limit 30;
p1          p2          gpop        ghouses     bcount      NAME
----------  ----------  ----------  ----------  ----------  ------------------------------------------------------------------------------------------
A02         6195        0           1           1           Belkofski ANVSA
A02         6225        0           2           2           Bill Moore's ANVSA
A02         6257        0           3           1           Canyon Village ANVSA
A02         6340        0           10          5           Chulloonawick ANVSA
A02         6380        0           37          8           Council ANVSA
A02         6570        0           1           1           Hamilton ANVSA
A02         6795        0           2           1           Kodiak ANVSA
A02         6860        0           5           1           Lesnoi ANVSA
A02         6915        0           5           3           Mary's Igloo ANVSA
A02         7145        0           4           1           Ohogamiut ANVSA
A02         7185        0           1           1           Paimiut ANVSA
A02         7500        0           15          3           Solomon ANVSA
A04         4785        0           3           1           Zuni Reservation and Off-Reservation Trust Land (part)
A06         0095        0           1           1           Alturas Indian Rancheria
A15         5026        0           1           1           Honokaia Hawaiian Home Land
A15         5181        0           1           1           Pauahi Hawaiian Home Land
A15         5213        0           2           1           South Maui Hawaiian Home Land
A15         5222        0           2           1           Upolu Hawaiian Home Land
A15         5236        0           1           1           Waiakea Hawaiian Home Land
A23         2695        0           168         30          Passamaquoddy Trust Land
A26         2580        0           12          1           Ontonagon Reservation
A44         2415        0           3           3           Narragansett Reservation
P02         282         0           67          13
Q15         005_90990   0           2           1
A06         1055        1           3           1           Enterprise Rancheria
A32         4045        1           8           8           Summit Lake Reservation and Off-Reservation Trust Land
A36         2535        1           11          2           Oil Springs Reservation
P02         230         1           1           1
A02         6455        2           53          2           Ekuk ANVSA
A02         6535        2           5           2           Georgetown ANVSA
Run Time: real 8.260 user 7.745307 sys 0.501438
sqlite>
sqlite> select b.p1,b.p2,b.p3,b.p4,sum(a.pop) as gpop,count(*) as bcount from blocks a left join table4 b on a.state=b.state and a.logrecno=b.logrecno group by p1,p2,p3,p4 having gpop<1000 order by a.state,a.county
limit 10;
p1          p2          p3          p4          gpop        bcount
----------  ----------  ----------  ----------  ----------  ----------
P01         001         03220       021100      870         68
P01         001         06460       021000      144         28
P01         001         48712       020802      144         5
P01         001         99999       020100      39          12
P01         001         99999       020300      2           1
P01         001         99999       020400      0           1
P01         001         99999       020500      123         3
P01         001         99999       020600      745         17
P01         001         99999       020700      238         35
P01         003         04660       010200      155         11
Run Time: real 18.285 user 17.110696 sys 1.158552
sqlite> select b.p1,b.p2,b.p3,sum(a.pop) as gpop,count(*) as bcount from blocks a left join table4 b on a.state=b.state and a.logrecno=b.logrecno group by p1,p2,p3 having gpop<1000 order by a.state,a.county limit 10;
p1          p2          p3          gpop        bcount
----------  ----------  ----------  ----------  ----------
P01         001         03220       870         68
P01         001         06460       144         28
P01         001         48712       144         5
P01         003         46072       723         37
P01         003         59088       581         25
P01         003         70536       706         46
P01         003         73872       862         109
P01         005         03724       279         29
P01         005         07672       96          17
P01         005         44344       519         30
Run Time: real 14.965 user 14.093582 sys 0.858531
sqlite> select b.p1,b.p2,b.p3,sum(a.pop) as gpop,count(*) as bcount from blocks a left join table4 b on a.state=b.state and a.logrecno=b.logrecno group by p1,p2,p3 having gpop<1000 order by a.state,a.county limit 30;

p1          p2          p3          gpop        bcount
----------  ----------  ----------  ----------  ----------
P01         001         03220       870         68
P01         001         06460       144         28
P01         001         48712       144         5
P01         003         46072       723         37
P01         003         59088       581         25
P01         003         70536       706         46
P01         003         73872       862         109
P01         005         03724       279         29
P01         005         07672       96          17
P01         005         44344       519         30
P01         007         78264       49          18
P01         009         01396       622         38
P01         009         01660       30          8
P01         009         17968       197         19
P01         009         29032       0           6
P01         009         33640       444         44
P01         009         34480       412         35
P01         009         53448       345         41
P01         009         66408       316         33
P01         009         71280       835         51
P01         009         74160       763         59
P01         009         76680       0           2
P01         011         26152       83          8
P01         011         48424       499         35
P01         013         45496       522         64
P01         015         29992       38          8
P01         015         35152       771         42
P01         015         53232       407         24
P01         015         71832       155         11
P01         015         82104       811         38
Run Time: real 14.865 user 13.930519 sys 0.859192
sqlite> select b.p1,b.p2,b.p3,sum(a.pop) as gpop,count(*) as bcount from blocks a left join table4 b on a.state=b.state and a.logrecno=b.logrecno group by p1,p2,p3 having gpop<1000 and substr(p1,1,1)='A' order by a.
state,a.county limit 30;
p1          p2          p3          gpop        bcount
----------  ----------  ----------  ----------  ----------
A01         2865        051_03      1           1
A01         2865        053_97      282         30
A01         2865        099_07      0           1
A01         2865        101_00      0           1
A02         6195        013_00      0           6
A02         6500        013_00      35          19
A02         6735        013_00      938         16
A02         7025        013_00      52          17
A02         7410        013_00      976         15
A02         6150        016_00      61          14
A02         7075        016_00      18          10
A02         7340        016_00      102         30
A02         7390        016_00      479         51
A02         6450        020_00      54          35
A02         6020        050_00      627         18
A02         6025        050_00      346         15
A02         6105        050_00      501         38
A02         6160        050_00      277         12
A02         6275        050_00      418         12
A02         6335        050_00      118         21
A02         6390        050_00      105         16
A02         6440        050_00      296         6
A02         6535        050_00      2           3
A02         6545        050_00      243         20
A02         6685        050_00      210         20
A02         6710        050_00      569         22
A02         6750        050_00      639         32
A02         6810        050_00      439         14
A02         6835        050_00      721         55
A02         6840        050_00      321         7
Run Time: real 6.921 user 6.569775 sys 0.347348
sqlite> select b.p1,b.p2,b.p3,b.p4,sum(a.pop) as gpop,count(*) as bcount from blocks a left join table4 b on a.state=b.state and a.logrecno=b.logrecno group by p1,p2,p3,p4 having gpop<1000 order by a.state,a.county
limit 30;
p1          p2          p3          p4          gpop        bcount
----------  ----------  ----------  ----------  ----------  ----------
P01         001         03220       021100      870         68
P01         001         06460       021000      144         28
P01         001         48712       020802      144         5
P01         001         99999       020100      39          12
P01         001         99999       020300      2           1
P01         001         99999       020400      0           1
P01         001         99999       020500      123         3
P01         001         99999       020600      745         17
P01         001         99999       020700      238         35
P01         003         04660       010200      155         11
P01         003         04660       010300      915         34
P01         003         04660       010400      220         9
P01         003         25240       010800      622         63
P01         003         25240       011102      446         41
P01         003         25240       011300      2           9
P01         003         26992       011401      881         20
P01         003         26992       011403      991         63
P01         003         26992       011601      151         14
P01         003         32272       011408      6           14
P01         003         44608       010400      208         101
P01         003         44608       010703      30          8
P01         003         44608       010904      292         27
P01         003         46072       011401      723         37
P01         003         57144       011403      357         15
P01         003         57144       011601      88          24
P01         003         59088       011601      33          4
P01         003         59088       011602      548         21
P01         003         61488       011300      891         58
P01         003         70536       010905      706         46
P01         003         71976       010300      38          35
Run Time: real 18.047 user 16.903168 sys 1.127128
sqlite> select b.p1,b.p2,b.p3,b.p4,sum(a.pop) as gpop,count(*) as bcount from blocks a left join table4 b on a.state=b.state and a.logrecno=b.logrecno group by p1,p2,p3,p4 having gpop<1000 order by gpop limit 30;
p1          p2          p3          p4          gpop        bcount
----------  ----------  ----------  ----------  ----------  ----------
A01         2865        053_97      970500      0           6
A01         2865        099_07      076100      0           1
A01         2865        101_00      005408      0           1
A02         6195        013_00      000100      0           6
A02         6225        270_00      000100      0           5
A02         6257        290_00      000100      0           7
A02         6290        170_00      000101      0           50
A02         6290        170_00      000102      0           84
A02         6340        270_00      000100      0           20
A02         6380        180_00      000100      0           19
A02         6570        270_00      000100      0           7
A02         6795        150_00      000100      0           18
A02         6860        150_00      000100      0           7
A02         6915        180_00      000100      0           6
A02         7080        122_00      001200      0           2
A02         7145        270_00      000100      0           1
A02         7185        270_00      000100      0           1
A02         7500        180_00      000100      0           9
A04         1235        015_95      952002      0           1
A04         1235        015_95      952004      0           3
A04         1310        013_81      816000      0           1
A04         1505        017_96      960500      0           3
A04         1545        025_00      002100      0           8
A04         1720        005_00      002000      0           11
A04         2130        021_00      001704      0           5
A04         2430        001_97      970200      0           6
A04         2430        005_00      002100      0           10
A04         2430        005_00      002200      0           14
A04         2430        017_96      960500      0           18
A04         3340        013_21      216809      0           7
Run Time: real 16.919 user 16.013789 sys 0.891491
sqlite> select b.p1,b.p2,sum(a.pop) as gpop,count(*) as bcount from blocks a left join table4 b on a.state=b.state and a.logrecno=b.logrecno group by p1,p2 having gpop<1000 order by gpop limit 30;
p1          p2          gpop        bcount
----------  ----------  ----------  ----------
A02         6195        0           6
A02         6225        0           5
A02         6257        0           7
A02         6340        0           20
A02         6380        0           19
A02         6570        0           7
A02         6795        0           18
A02         6860        0           7
A02         6915        0           6
A02         7145        0           1
A02         7185        0           1
A02         7500        0           9
A04         4785        0           14
A06         0095        0           1
A06         0120        0           5
A06         0125        0           1
A06         0495        0           39
A06         0955        0           1
A06         1065        0           24
A06         1560        0           6
A06         1640        0           6
A06         1670        0           1
A06         1955        0           1
A06         2075        0           1
A06         2685        0           6
A06         4560        0           5
A12         0690        0           1
A12         3665        0           1
A12         4130        0           8
A15         5008        0           7
Run Time: real 12.067 user 11.448261 sys 0.612198
sqlite> select sumlev,name from geo where state='02' and aianhh='6195' limit 10;

```
