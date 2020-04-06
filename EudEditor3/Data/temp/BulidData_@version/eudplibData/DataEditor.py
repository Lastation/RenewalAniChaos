from eudplib import *


def onPluginStart():
    DoActions([  # Basic DatFile Actions
        SetMemory(0x6644F8, Add, 34048),# units:Graphics  index:1    from 74 To 207
        SetMemory(0x6644F8, Add, 7798784),# units:Graphics  index:2    from 88 To 207
        SetMemory(0x6644FC, Add, 2130706432),# units:Graphics  index:7    from 81 To 208
        SetMemory(0x664500, Add, 127),# units:Graphics  index:8    from 80 To 207
        SetMemory(0x664500, Add, 30976),# units:Graphics  index:9    from 86 To 207
        SetMemory(0x664500, Add, 8781824),# units:Graphics  index:10    from 73 To 207
        SetMemory(0x664500, Add, 2264924160),# units:Graphics  index:11    from 72 To 207
        SetMemory(0x664504, Add, 137),# units:Graphics  index:12    from 70 To 207
        SetMemory(0x664508, Add, 130),# units:Graphics  index:16    from 77 To 207
        SetMemory(0x664508, Add, 1996488704),# units:Graphics  index:19    from 88 To 207
        SetMemory(0x66450C, Add, 129),# units:Graphics  index:20    from 78 To 207
        SetMemory(0x66450C, Add, 32512),# units:Graphics  index:21    from 80 To 207
        SetMemory(0x66450C, Add, 7929856),# units:Graphics  index:22    from 86 To 207
        SetMemory(0x664510, Add, 2298478592),# units:Graphics  index:27    from 70 To 207
        SetMemory(0x664514, Add, 137),# units:Graphics  index:28    from 70 To 207
        SetMemory(0x664514, Add, 35072),# units:Graphics  index:29    from 70 To 207
        SetMemory(0x664518, Add, 134),# units:Graphics  index:32    from 73 To 207
        SetMemory(0x664518, Add, 1179648),# units:Graphics  index:34    from 189 To 207
        SetMemory(0x66451C, Add, 49152),# units:Graphics  index:37    from 15 To 207
        SetMemory(0x66451C, Add, 13041664),# units:Graphics  index:38    from 8 To 207
        SetMemory(0x66451C, Add, 3238002688),# units:Graphics  index:39    from 14 To 207
        SetMemory(0x664520, Add, 206),# units:Graphics  index:40    from 1 To 207
        SetMemory(0x664520, Add, 31488),# units:Graphics  index:41    from 5 To 128
        SetMemory(0x664520, Add, 7602176),# units:Graphics  index:42    from 12 To 128
        SetMemory(0x664520, Add, 1962934272),# units:Graphics  index:43    from 11 To 128
        SetMemory(0x664524, Add, 121),# units:Graphics  index:44    from 7 To 128
        SetMemory(0x664524, Add, 12544),# units:Graphics  index:45    from 13 To 62
        SetMemory(0x664524, Add, 8126464),# units:Graphics  index:46    from 4 To 128
        SetMemory(0x664524, Add, 2147483648),# units:Graphics  index:47    from 0 To 128
        SetMemory(0x664528, Add, 117),# units:Graphics  index:48    from 14 To 131
        SetMemory(0x664528, Add, 30720),# units:Graphics  index:49    from 13 To 133
        SetMemory(0x664528, Add, 8585216),# units:Graphics  index:50    from 2 To 133
        SetMemory(0x664528, Add, 1996488704),# units:Graphics  index:51    from 9 To 128
        SetMemory(0x66452C, Add, 133),# units:Graphics  index:52    from 4 To 137
        SetMemory(0x66452C, Add, 30720),# units:Graphics  index:53    from 8 To 128
        SetMemory(0x66452C, Add, 12648448),# units:Graphics  index:54    from 15 To 208
        SetMemory(0x66452C, Add, 3305111552),# units:Graphics  index:55    from 11 To 208
        SetMemory(0x664530, Add, 201),# units:Graphics  index:56    from 7 To 208
        SetMemory(0x664530, Add, 50176),# units:Graphics  index:57    from 12 To 208
        SetMemory(0x664534, Add, 17),# units:Graphics  index:60    from 191 To 208
        SetMemory(0x664534, Add, 5120),# units:Graphics  index:61    from 188 To 208
        SetMemory(0x664534, Add, 1507328),# units:Graphics  index:62    from 185 To 208
        SetMemory(0x664534, Add, 352321536),# units:Graphics  index:63    from 187 To 208
        SetMemory(0x664538, Add, 166),# units:Graphics  index:64    from 42 To 208
        SetMemory(0x664538, Add, 40704),# units:Graphics  index:65    from 49 To 208
        SetMemory(0x664538, Add, 11010048),# units:Graphics  index:66    from 40 To 208
        SetMemory(0x664538, Add, 2734686208),# units:Graphics  index:67    from 45 To 208
        SetMemory(0x66453C, Add, 170),# units:Graphics  index:68    from 38 To 208
        SetMemory(0x66453C, Add, 41984),# units:Graphics  index:69    from 44 To 208
        SetMemory(0x66453C, Add, 10813440),# units:Graphics  index:70    from 43 To 208
        SetMemory(0x66453C, Add, 2868903936),# units:Graphics  index:71    from 37 To 208
        SetMemory(0x664540, Add, 169),# units:Graphics  index:72    from 39 To 208
        SetMemory(0x664540, Add, 10616832),# units:Graphics  index:74    from 46 To 208
        SetMemory(0x664540, Add, 2717908992),# units:Graphics  index:75    from 46 To 208
        SetMemory(0x664544, Add, 170),# units:Graphics  index:76    from 38 To 208
        SetMemory(0x664544, Add, 40704),# units:Graphics  index:77    from 49 To 208
        SetMemory(0x664544, Add, 6356992),# units:Graphics  index:78    from 40 To 137
        SetMemory(0x664544, Add, 1543503872),# units:Graphics  index:79    from 45 To 137
        SetMemory(0x664548, Add, 94),# units:Graphics  index:80    from 43 To 137
        SetMemory(0x664548, Add, 20736),# units:Graphics  index:81    from 47 To 128
        SetMemory(0x664548, Add, 5832704),# units:Graphics  index:82    from 39 To 128
        SetMemory(0x664548, Add, 1442840576),# units:Graphics  index:83    from 47 To 133
        SetMemory(0x66454C, Add, 83),# units:Graphics  index:84    from 50 To 133
        SetMemory(0x66454C, Add, 1638400),# units:Graphics  index:86    from 37 To 62
        SetMemory(0x66454C, Add, 1392508928),# units:Graphics  index:87    from 45 To 128
        SetMemory(0x664550, Add, 90),# units:Graphics  index:88    from 43 To 133
        SetMemory(0x664550, Add, 4608),# units:Graphics  index:89    from 115 To 133
        SetMemory(0x664550, Add, 983040),# units:Graphics  index:90    from 116 To 131
        SetMemory(0x664554, Add, -17152),# units:Graphics  index:93    from 198 To 131
        SetMemory(0x664554, Add, -4063232),# units:Graphics  index:94    from 199 To 137
        SetMemory(0x664554, Add, 385875968),# units:Graphics  index:95    from 114 To 137
        SetMemory(0x664558, Add, -67),# units:Graphics  index:96    from 200 To 133
        SetMemory(0x664558, Add, -4128768),# units:Graphics  index:98    from 191 To 128
        SetMemory(0x664558, Add, 939524096),# units:Graphics  index:99    from 74 To 130
        SetMemory(0x66455C, Add, 56),# units:Graphics  index:100    from 74 To 130
        SetMemory(0x66455C, Add, 3932160),# units:Graphics  index:102    from 70 To 130
        SetMemory(0x66455C, Add, -939524096),# units:Graphics  index:103    from 186 To 130
        SetMemory(0x664560, Add, 56),# units:Graphics  index:104    from 74 To 130
        SetMemory(0x664560, Add, 2359296),# units:Graphics  index:106    from 94 To 130
        SetMemory(0x664560, Add, 1929379840),# units:Graphics  index:107    from 93 To 208
        SetMemory(0x664564, Add, 8960),# units:Graphics  index:109    from 95 To 130
        SetMemory(0x664564, Add, 2097152),# units:Graphics  index:110    from 105 To 137
        SetMemory(0x664564, Add, 654311424),# units:Graphics  index:111    from 91 To 130
        SetMemory(0x664568, Add, 40),# units:Graphics  index:112    from 90 To 130
        SetMemory(0x664568, Add, 8448),# units:Graphics  index:113    from 97 To 130
        SetMemory(0x664568, Add, 1310720),# units:Graphics  index:114    from 110 To 130
        SetMemory(0x664568, Add, 570425344),# units:Graphics  index:115    from 96 To 130
        SetMemory(0x66456C, Add, 23),# units:Graphics  index:116    from 107 To 130
        SetMemory(0x66456C, Add, 8192),# units:Graphics  index:117    from 98 To 130
        SetMemory(0x66456C, Add, 1769472),# units:Graphics  index:118    from 103 To 130
        SetMemory(0x664570, Add, 30),# units:Graphics  index:120    from 100 To 130
        SetMemory(0x664570, Add, 1245184),# units:Graphics  index:122    from 111 To 130
        SetMemory(0x664570, Add, 637534208),# units:Graphics  index:123    from 92 To 130
        SetMemory(0x664574, Add, 29),# units:Graphics  index:124    from 101 To 130
        SetMemory(0x664574, Add, 6656),# units:Graphics  index:125    from 104 To 130
        SetMemory(0x664574, Add, 1835008),# units:Graphics  index:126    from 102 To 130
        SetMemory(0x664574, Add, 520093696),# units:Graphics  index:127    from 99 To 130
        SetMemory(0x664578, Add, -79),# units:Graphics  index:128    from 207 To 128
        SetMemory(0x664578, Add, -20224),# units:Graphics  index:129    from 208 To 129
        SetMemory(0x664578, Add, 7405568),# units:Graphics  index:130    from 17 To 130
        SetMemory(0x664578, Add, 1811939328),# units:Graphics  index:131    from 22 To 130
        SetMemory(0x66457C, Add, 106),# units:Graphics  index:132    from 24 To 130
        SetMemory(0x66457C, Add, 27392),# units:Graphics  index:133    from 23 To 130
        SetMemory(0x66457C, Add, 6619136),# units:Graphics  index:134    from 29 To 130
        SetMemory(0x66457C, Add, 1610612736),# units:Graphics  index:135    from 34 To 130
        SetMemory(0x664580, Add, 103),# units:Graphics  index:136    from 27 To 130
        SetMemory(0x664580, Add, 28416),# units:Graphics  index:137    from 26 To 137
        SetMemory(0x664580, Add, 7143424),# units:Graphics  index:138    from 28 To 137
        SetMemory(0x664580, Add, 1862270976),# units:Graphics  index:139    from 20 To 131
        SetMemory(0x664584, Add, 99),# units:Graphics  index:140    from 32 To 131
        SetMemory(0x664584, Add, 24576),# units:Graphics  index:141    from 35 To 131
        SetMemory(0x664584, Add, 2883584),# units:Graphics  index:142    from 18 To 62
        SetMemory(0x664584, Add, 1795162112),# units:Graphics  index:143    from 21 To 128
        SetMemory(0x664588, Add, 95),# units:Graphics  index:144    from 36 To 131
        SetMemory(0x664588, Add, 6946816),# units:Graphics  index:146    from 25 To 131
        SetMemory(0x664588, Add, 1795162112),# units:Graphics  index:147    from 30 To 137
        SetMemory(0x66458C, Add, 102),# units:Graphics  index:148    from 31 To 133
        SetMemory(0x66458C, Add, 25088),# units:Graphics  index:149    from 33 To 131
        SetMemory(0x66458C, Add, 7471104),# units:Graphics  index:150    from 19 To 133
        SetMemory(0x66458C, Add, 2030043136),# units:Graphics  index:151    from 16 To 137
        SetMemory(0x664590, Add, 121),# units:Graphics  index:152    from 16 To 137
        SetMemory(0x664590, Add, 4521984),# units:Graphics  index:154    from 59 To 128
        SetMemory(0x664590, Add, 1090519040),# units:Graphics  index:155    from 63 To 128
        SetMemory(0x664594, Add, 68),# units:Graphics  index:156    from 62 To 130
        SetMemory(0x664594, Add, 20736),# units:Graphics  index:157    from 52 To 133
        SetMemory(0x664594, Add, 1409286144),# units:Graphics  index:159    from 53 To 137
        SetMemory(0x664598, Add, 81),# units:Graphics  index:160    from 56 To 137
        SetMemory(0x664598, Add, 5046272),# units:Graphics  index:162    from 60 To 137
        SetMemory(0x664598, Add, 1241513984),# units:Graphics  index:163    from 54 To 128
        SetMemory(0x66459C, Add, 74),# units:Graphics  index:164    from 57 To 131
        SetMemory(0x66459C, Add, 20480),# units:Graphics  index:165    from 51 To 131
        SetMemory(0x66459C, Add, 4980736),# units:Graphics  index:166    from 55 To 131
        SetMemory(0x66459C, Add, 1107296256),# units:Graphics  index:167    from 65 To 131
        SetMemory(0x6645A0, Add, 65),# units:Graphics  index:168    from 66 To 131
        SetMemory(0x6645A0, Add, 15872),# units:Graphics  index:169    from 69 To 131
        SetMemory(0x6645A0, Add, 4587520),# units:Graphics  index:170    from 61 To 131
        SetMemory(0x6645A0, Add, 1073741824),# units:Graphics  index:171    from 67 To 131
        SetMemory(0x6645A4, Add, 67),# units:Graphics  index:172    from 64 To 131
        SetMemory(0x6645A4, Add, 17920),# units:Graphics  index:173    from 58 To 128
        SetMemory(0x6645A4, Add, 4259840),# units:Graphics  index:174    from 68 To 133
        SetMemory(0x6645A4, Add, -1073741824),# units:Graphics  index:175    from 197 To 133
        SetMemory(0x6645B4, Add, -15872),# units:Graphics  index:189    from 195 To 133
        SetMemory(0x6645B4, Add, -3997696),# units:Graphics  index:190    from 194 To 133
        SetMemory(0x6645B8, Add, 393216),# units:Graphics  index:194    from 122 To 128
        SetMemory(0x6645B8, Add, 100663296),# units:Graphics  index:195    from 123 To 129
        SetMemory(0x6645BC, Add, 83),# units:Graphics  index:196    from 124 To 207
        SetMemory(0x6645C0, Add, -68),# units:Graphics  index:200    from 196 To 128
        SetMemory(0x6645C0, Add, -16640),# units:Graphics  index:201    from 193 To 128
        SetMemory(0x6645CC, Add, 50331648),# units:Graphics  index:215    from 126 To 129
        SetMemory(0x6645D0, Add, 3),# units:Graphics  index:216    from 127 To 130
        SetMemory(0x6645D0, Add, 1280),# units:Graphics  index:217    from 128 To 133
        SetMemory(0x6645D0, Add, 16777216),# units:Graphics  index:219    from 130 To 131
        SetMemory(0x6645D4, Add, -41),# units:Graphics  index:220    from 131 To 90
        SetMemory(0x6645D4, Add, 256),# units:Graphics  index:221    from 132 To 133
        SetMemory(0x6645D4, Add, 1224736768),# units:Graphics  index:223    from 134 To 207
        SetMemory(0x6649AC, Add, 228),# units:Infestation  index:22    from 0 To 228
        SetMemory(0x6649AC, Add, 14942208),# units:Infestation  index:23    from 0 To 228
        SetMemory(0x661144, Add, -56),# units:Construction Animation  index:37    from 56 To 0
        SetMemory(0x661148, Add, -31),# units:Construction Animation  index:38    from 31 To 0
        SetMemory(0x66114C, Add, -52),# units:Construction Animation  index:39    from 52 To 0
        SetMemory(0x661154, Add, -19),# units:Construction Animation  index:41    from 19 To 0
        SetMemory(0x661158, Add, -44),# units:Construction Animation  index:42    from 44 To 0
        SetMemory(0x66115C, Add, -40),# units:Construction Animation  index:43    from 40 To 0
        SetMemory(0x661160, Add, -27),# units:Construction Animation  index:44    from 27 To 0
        SetMemory(0x661164, Add, -49),# units:Construction Animation  index:45    from 49 To 0
        SetMemory(0x661168, Add, -15),# units:Construction Animation  index:46    from 15 To 0
        SetMemory(0x66116C, Add, -2),# units:Construction Animation  index:47    from 2 To 0
        SetMemory(0x661170, Add, -52),# units:Construction Animation  index:48    from 52 To 0
        SetMemory(0x661174, Add, -49),# units:Construction Animation  index:49    from 49 To 0
        SetMemory(0x661180, Add, -15),# units:Construction Animation  index:52    from 15 To 0
        SetMemory(0x661184, Add, -31),# units:Construction Animation  index:53    from 31 To 0
        SetMemory(0x661188, Add, -56),# units:Construction Animation  index:54    from 56 To 0
        SetMemory(0x66118C, Add, -40),# units:Construction Animation  index:55    from 40 To 0
        SetMemory(0x661190, Add, -27),# units:Construction Animation  index:56    from 27 To 0
        SetMemory(0x661194, Add, -44),# units:Construction Animation  index:57    from 44 To 0
        SetMemory(0x6611A8, Add, -917),# units:Construction Animation  index:62    from 917 To 0
        SetMemory(0x66124C, Add, -919),# units:Construction Animation  index:103    from 919 To 0
        SetMemory(0x661258, Add, -325),# units:Construction Animation  index:106    from 325 To 0
        SetMemory(0x66125C, Add, -330),# units:Construction Animation  index:107    from 330 To 0
        SetMemory(0x661264, Add, -330),# units:Construction Animation  index:109    from 330 To 0
        SetMemory(0x66126C, Add, -325),# units:Construction Animation  index:111    from 325 To 0
        SetMemory(0x661270, Add, -327),# units:Construction Animation  index:112    from 327 To 0
        SetMemory(0x661274, Add, -327),# units:Construction Animation  index:113    from 327 To 0
        SetMemory(0x661278, Add, -325),# units:Construction Animation  index:114    from 325 To 0
        SetMemory(0x66127C, Add, -327),# units:Construction Animation  index:115    from 327 To 0
        SetMemory(0x661280, Add, -327),# units:Construction Animation  index:116    from 327 To 0
        SetMemory(0x661284, Add, -330),# units:Construction Animation  index:117    from 330 To 0
        SetMemory(0x661288, Add, -330),# units:Construction Animation  index:118    from 330 To 0
        SetMemory(0x661290, Add, -327),# units:Construction Animation  index:120    from 327 To 0
        SetMemory(0x661298, Add, -327),# units:Construction Animation  index:122    from 327 To 0
        SetMemory(0x66129C, Add, -327),# units:Construction Animation  index:123    from 327 To 0
        SetMemory(0x6612A0, Add, -329),# units:Construction Animation  index:124    from 329 To 0
        SetMemory(0x6612A4, Add, -330),# units:Construction Animation  index:125    from 330 To 0
        SetMemory(0x6612A8, Add, -325),# units:Construction Animation  index:126    from 325 To 0
        SetMemory(0x6612AC, Add, -104),# units:Construction Animation  index:127    from 104 To 0
        SetMemory(0x6612B8, Add, -101),# units:Construction Animation  index:130    from 101 To 0
        SetMemory(0x6612BC, Add, -104),# units:Construction Animation  index:131    from 104 To 0
        SetMemory(0x6612C0, Add, -103),# units:Construction Animation  index:132    from 103 To 0
        SetMemory(0x6612C4, Add, -103),# units:Construction Animation  index:133    from 103 To 0
        SetMemory(0x6612C8, Add, -104),# units:Construction Animation  index:134    from 104 To 0
        SetMemory(0x6612CC, Add, -104),# units:Construction Animation  index:135    from 104 To 0
        SetMemory(0x6612D0, Add, -104),# units:Construction Animation  index:136    from 104 To 0
        SetMemory(0x6612D4, Add, -104),# units:Construction Animation  index:137    from 104 To 0
        SetMemory(0x6612D8, Add, -104),# units:Construction Animation  index:138    from 104 To 0
        SetMemory(0x6612DC, Add, -104),# units:Construction Animation  index:139    from 104 To 0
        SetMemory(0x6612E0, Add, -104),# units:Construction Animation  index:140    from 104 To 0
        SetMemory(0x6612E4, Add, -104),# units:Construction Animation  index:141    from 104 To 0
        SetMemory(0x6612E8, Add, -104),# units:Construction Animation  index:142    from 104 To 0
        SetMemory(0x6612EC, Add, -105),# units:Construction Animation  index:143    from 105 To 0
        SetMemory(0x6612F0, Add, -105),# units:Construction Animation  index:144    from 105 To 0
        SetMemory(0x6612F8, Add, -105),# units:Construction Animation  index:146    from 105 To 0
        SetMemory(0x6612FC, Add, -103),# units:Construction Animation  index:147    from 103 To 0
        SetMemory(0x661300, Add, -103),# units:Construction Animation  index:148    from 103 To 0
        SetMemory(0x661304, Add, -102),# units:Construction Animation  index:149    from 102 To 0
        SetMemory(0x66130C, Add, -104),# units:Construction Animation  index:151    from 104 To 0
        SetMemory(0x661310, Add, -104),# units:Construction Animation  index:152    from 104 To 0
        SetMemory(0x66134C, Add, -200),# units:Construction Animation  index:167    from 200 To 0
        SetMemory(0x6605F0, Add, -8192),# units:Unit Direction  index:1    from 32 To 0
        SetMemory(0x6605F0, Add, -2097152),# units:Unit Direction  index:2    from 32 To 0
        SetMemory(0x6605F4, Add, -536870912),# units:Unit Direction  index:7    from 32 To 0
        SetMemory(0x6605F8, Add, -32),# units:Unit Direction  index:8    from 32 To 0
        SetMemory(0x6605F8, Add, -8192),# units:Unit Direction  index:9    from 32 To 0
        SetMemory(0x6605F8, Add, -2097152),# units:Unit Direction  index:10    from 32 To 0
        SetMemory(0x6605F8, Add, -536870912),# units:Unit Direction  index:11    from 32 To 0
        SetMemory(0x6605FC, Add, -32),# units:Unit Direction  index:12    from 32 To 0
        SetMemory(0x660600, Add, -32),# units:Unit Direction  index:16    from 32 To 0
        SetMemory(0x660600, Add, -536870912),# units:Unit Direction  index:19    from 32 To 0
        SetMemory(0x660604, Add, -32),# units:Unit Direction  index:20    from 32 To 0
        SetMemory(0x660604, Add, -8192),# units:Unit Direction  index:21    from 32 To 0
        SetMemory(0x660604, Add, -2097152),# units:Unit Direction  index:22    from 32 To 0
        SetMemory(0x660608, Add, -536870912),# units:Unit Direction  index:27    from 32 To 0
        SetMemory(0x66060C, Add, -32),# units:Unit Direction  index:28    from 32 To 0
        SetMemory(0x66060C, Add, -8192),# units:Unit Direction  index:29    from 32 To 0
        SetMemory(0x660610, Add, -32),# units:Unit Direction  index:32    from 32 To 0
        SetMemory(0x660610, Add, -2097152),# units:Unit Direction  index:34    from 32 To 0
        SetMemory(0x660614, Add, -2560),# units:Unit Direction  index:37    from 10 To 0
        SetMemory(0x660614, Add, -786432),# units:Unit Direction  index:38    from 12 To 0
        SetMemory(0x660614, Add, -234881024),# units:Unit Direction  index:39    from 14 To 0
        SetMemory(0x660618, Add, -32),# units:Unit Direction  index:40    from 32 To 0
        SetMemory(0x660618, Add, -3328),# units:Unit Direction  index:41    from 13 To 0
        SetMemory(0x660618, Add, -851968),# units:Unit Direction  index:42    from 13 To 0
        SetMemory(0x660618, Add, -251658240),# units:Unit Direction  index:43    from 15 To 0
        SetMemory(0x66061C, Add, -14),# units:Unit Direction  index:44    from 14 To 0
        SetMemory(0x66061C, Add, -3840),# units:Unit Direction  index:45    from 15 To 0
        SetMemory(0x66061C, Add, -851968),# units:Unit Direction  index:46    from 13 To 0
        SetMemory(0x660620, Add, -14),# units:Unit Direction  index:48    from 14 To 0
        SetMemory(0x660620, Add, -3840),# units:Unit Direction  index:49    from 15 To 0
        SetMemory(0x660620, Add, -2097152),# units:Unit Direction  index:50    from 32 To 0
        SetMemory(0x660620, Add, -536870912),# units:Unit Direction  index:51    from 32 To 0
        SetMemory(0x660624, Add, -13),# units:Unit Direction  index:52    from 13 To 0
        SetMemory(0x660624, Add, -3072),# units:Unit Direction  index:53    from 12 To 0
        SetMemory(0x660624, Add, -655360),# units:Unit Direction  index:54    from 10 To 0
        SetMemory(0x660624, Add, -251658240),# units:Unit Direction  index:55    from 15 To 0
        SetMemory(0x660628, Add, -14),# units:Unit Direction  index:56    from 14 To 0
        SetMemory(0x660628, Add, -3328),# units:Unit Direction  index:57    from 13 To 0
        SetMemory(0x66062C, Add, -32),# units:Unit Direction  index:60    from 32 To 0
        SetMemory(0x66062C, Add, -8192),# units:Unit Direction  index:61    from 32 To 0
        SetMemory(0x66062C, Add, -786432),# units:Unit Direction  index:62    from 12 To 0
        SetMemory(0x66062C, Add, -536870912),# units:Unit Direction  index:63    from 32 To 0
        SetMemory(0x660630, Add, -32),# units:Unit Direction  index:64    from 32 To 0
        SetMemory(0x660630, Add, -8192),# units:Unit Direction  index:65    from 32 To 0
        SetMemory(0x660630, Add, -2097152),# units:Unit Direction  index:66    from 32 To 0
        SetMemory(0x660630, Add, -536870912),# units:Unit Direction  index:67    from 32 To 0
        SetMemory(0x660634, Add, -32),# units:Unit Direction  index:68    from 32 To 0
        SetMemory(0x660634, Add, -8192),# units:Unit Direction  index:69    from 32 To 0
        SetMemory(0x660634, Add, -2097152),# units:Unit Direction  index:70    from 32 To 0
        SetMemory(0x660634, Add, -536870912),# units:Unit Direction  index:71    from 32 To 0
        SetMemory(0x660638, Add, -32),# units:Unit Direction  index:72    from 32 To 0
        SetMemory(0x660638, Add, -2097152),# units:Unit Direction  index:74    from 32 To 0
        SetMemory(0x660638, Add, -536870912),# units:Unit Direction  index:75    from 32 To 0
        SetMemory(0x66063C, Add, -32),# units:Unit Direction  index:76    from 32 To 0
        SetMemory(0x66063C, Add, -8192),# units:Unit Direction  index:77    from 32 To 0
        SetMemory(0x66063C, Add, -2097152),# units:Unit Direction  index:78    from 32 To 0
        SetMemory(0x66063C, Add, -536870912),# units:Unit Direction  index:79    from 32 To 0
        SetMemory(0x660640, Add, -32),# units:Unit Direction  index:80    from 32 To 0
        SetMemory(0x660640, Add, -8192),# units:Unit Direction  index:81    from 32 To 0
        SetMemory(0x660640, Add, -2097152),# units:Unit Direction  index:82    from 32 To 0
        SetMemory(0x660640, Add, -536870912),# units:Unit Direction  index:83    from 32 To 0
        SetMemory(0x660644, Add, -32),# units:Unit Direction  index:84    from 32 To 0
        SetMemory(0x660644, Add, -2097152),# units:Unit Direction  index:86    from 32 To 0
        SetMemory(0x660644, Add, -536870912),# units:Unit Direction  index:87    from 32 To 0
        SetMemory(0x660648, Add, -32),# units:Unit Direction  index:88    from 32 To 0
        SetMemory(0x660648, Add, -8192),# units:Unit Direction  index:89    from 32 To 0
        SetMemory(0x660648, Add, -2097152),# units:Unit Direction  index:90    from 32 To 0
        SetMemory(0x66064C, Add, -8192),# units:Unit Direction  index:93    from 32 To 0
        SetMemory(0x66064C, Add, -2097152),# units:Unit Direction  index:94    from 32 To 0
        SetMemory(0x66064C, Add, -536870912),# units:Unit Direction  index:95    from 32 To 0
        SetMemory(0x660650, Add, -32),# units:Unit Direction  index:96    from 32 To 0
        SetMemory(0x660650, Add, -2097152),# units:Unit Direction  index:98    from 32 To 0
        SetMemory(0x660650, Add, -536870912),# units:Unit Direction  index:99    from 32 To 0
        SetMemory(0x660654, Add, -32),# units:Unit Direction  index:100    from 32 To 0
        SetMemory(0x660654, Add, -2097152),# units:Unit Direction  index:102    from 32 To 0
        SetMemory(0x660654, Add, -201326592),# units:Unit Direction  index:103    from 12 To 0
        SetMemory(0x660658, Add, -32),# units:Unit Direction  index:104    from 32 To 0
        SetMemory(0x6606C4, Add, -134217728),# units:Unit Direction  index:215    from 8 To 0
        SetMemory(0x6647EC, Add, -1),# units:Shield Enable  index:60    from 1 To 0
        SetMemory(0x6647EC, Add, -256),# units:Shield Enable  index:61    from 1 To 0
        SetMemory(0x6647EC, Add, -16777216),# units:Shield Enable  index:63    from 1 To 0
        SetMemory(0x6647F0, Add, -1),# units:Shield Enable  index:64    from 1 To 0
        SetMemory(0x6647F0, Add, -256),# units:Shield Enable  index:65    from 1 To 0
        SetMemory(0x6647F0, Add, -65536),# units:Shield Enable  index:66    from 1 To 0
        SetMemory(0x6647F0, Add, -16777216),# units:Shield Enable  index:67    from 1 To 0
        SetMemory(0x6647F4, Add, -1),# units:Shield Enable  index:68    from 1 To 0
        SetMemory(0x6647F4, Add, -256),# units:Shield Enable  index:69    from 1 To 0
        SetMemory(0x6647F4, Add, -65536),# units:Shield Enable  index:70    from 1 To 0
        SetMemory(0x6647F4, Add, -16777216),# units:Shield Enable  index:71    from 1 To 0
        SetMemory(0x6647F8, Add, -1),# units:Shield Enable  index:72    from 1 To 0
        SetMemory(0x6647F8, Add, -65536),# units:Shield Enable  index:74    from 1 To 0
        SetMemory(0x6647F8, Add, -16777216),# units:Shield Enable  index:75    from 1 To 0
        SetMemory(0x6647FC, Add, -1),# units:Shield Enable  index:76    from 1 To 0
        SetMemory(0x6647FC, Add, -256),# units:Shield Enable  index:77    from 1 To 0
        SetMemory(0x6647FC, Add, -65536),# units:Shield Enable  index:78    from 1 To 0
        SetMemory(0x6647FC, Add, -16777216),# units:Shield Enable  index:79    from 1 To 0
        SetMemory(0x664800, Add, -1),# units:Shield Enable  index:80    from 1 To 0
        SetMemory(0x664800, Add, -256),# units:Shield Enable  index:81    from 1 To 0
        SetMemory(0x664800, Add, -65536),# units:Shield Enable  index:82    from 1 To 0
        SetMemory(0x664800, Add, -16777216),# units:Shield Enable  index:83    from 1 To 0
        SetMemory(0x664804, Add, -1),# units:Shield Enable  index:84    from 1 To 0
        SetMemory(0x664804, Add, -65536),# units:Shield Enable  index:86    from 1 To 0
        SetMemory(0x664804, Add, -16777216),# units:Shield Enable  index:87    from 1 To 0
        SetMemory(0x664808, Add, -1),# units:Shield Enable  index:88    from 1 To 0
        SetMemory(0x664810, Add, -65536),# units:Shield Enable  index:98    from 1 To 0
        SetMemory(0x664848, Add, -65536),# units:Shield Enable  index:154    from 1 To 0
        SetMemory(0x664848, Add, -16777216),# units:Shield Enable  index:155    from 1 To 0
        SetMemory(0x66484C, Add, -1),# units:Shield Enable  index:156    from 1 To 0
        SetMemory(0x66484C, Add, -256),# units:Shield Enable  index:157    from 1 To 0
        SetMemory(0x66484C, Add, -16777216),# units:Shield Enable  index:159    from 1 To 0
        SetMemory(0x664850, Add, -1),# units:Shield Enable  index:160    from 1 To 0
        SetMemory(0x664850, Add, -65536),# units:Shield Enable  index:162    from 1 To 0
        SetMemory(0x664850, Add, -16777216),# units:Shield Enable  index:163    from 1 To 0
        SetMemory(0x664854, Add, -1),# units:Shield Enable  index:164    from 1 To 0
        SetMemory(0x664854, Add, -256),# units:Shield Enable  index:165    from 1 To 0
        SetMemory(0x664854, Add, -65536),# units:Shield Enable  index:166    from 1 To 0
        SetMemory(0x664854, Add, -16777216),# units:Shield Enable  index:167    from 1 To 0
        SetMemory(0x664858, Add, -256),# units:Shield Enable  index:169    from 1 To 0
        SetMemory(0x664858, Add, -65536),# units:Shield Enable  index:170    from 1 To 0
        SetMemory(0x664858, Add, -16777216),# units:Shield Enable  index:171    from 1 To 0
        SetMemory(0x66485C, Add, -1),# units:Shield Enable  index:172    from 1 To 0
        SetMemory(0x660E78, Add, 20),# units:Shield Amount  index:60    from 80 To 100
        SetMemory(0x660E78, Add, 3932160),# units:Shield Amount  index:61    from 40 To 100
        SetMemory(0x660E7C, Add, -6553600),# units:Shield Amount  index:63    from 200 To 100
        SetMemory(0x660E80, Add, 80),# units:Shield Amount  index:64    from 20 To 100
        SetMemory(0x660E80, Add, 2621440),# units:Shield Amount  index:65    from 60 To 100
        SetMemory(0x660E84, Add, 20),# units:Shield Amount  index:66    from 80 To 100
        SetMemory(0x660E84, Add, 3932160),# units:Shield Amount  index:67    from 40 To 100
        SetMemory(0x660E88, Add, -250),# units:Shield Amount  index:68    from 350 To 100
        SetMemory(0x660E88, Add, 2621440),# units:Shield Amount  index:69    from 60 To 100
        SetMemory(0x660E8C, Add, -3276800),# units:Shield Amount  index:71    from 150 To 100
        SetMemory(0x660E90, Add, -50),# units:Shield Amount  index:72    from 150 To 100
        SetMemory(0x660E94, Add, 20),# units:Shield Amount  index:74    from 80 To 100
        SetMemory(0x660E94, Add, -19660800),# units:Shield Amount  index:75    from 400 To 100
        SetMemory(0x660E98, Add, -700),# units:Shield Amount  index:76    from 800 To 100
        SetMemory(0x660E98, Add, -9175040),# units:Shield Amount  index:77    from 240 To 100
        SetMemory(0x660E9C, Add, -140),# units:Shield Amount  index:78    from 240 To 100
        SetMemory(0x660E9C, Add, -13107200),# units:Shield Amount  index:79    from 300 To 100
        SetMemory(0x660EA0, Add, -300),# units:Shield Amount  index:80    from 400 To 100
        SetMemory(0x660EA0, Add, -19660800),# units:Shield Amount  index:81    from 400 To 100
        SetMemory(0x660EA4, Add, -400),# units:Shield Amount  index:82    from 500 To 100
        SetMemory(0x660EA4, Add, 1310720),# units:Shield Amount  index:83    from 80 To 100
        SetMemory(0x660EA8, Add, 80),# units:Shield Amount  index:84    from 20 To 100
        SetMemory(0x660EAC, Add, -400),# units:Shield Amount  index:86    from 500 To 100
        SetMemory(0x660EAC, Add, -13107200),# units:Shield Amount  index:87    from 300 To 100
        SetMemory(0x660EB0, Add, -150),# units:Shield Amount  index:88    from 250 To 100
        SetMemory(0x660EC4, Add, 40),# units:Shield Amount  index:98    from 60 To 100
        SetMemory(0x660F34, Add, -650),# units:Shield Amount  index:154    from 750 To 100
        SetMemory(0x660F34, Add, -26214400),# units:Shield Amount  index:155    from 500 To 100
        SetMemory(0x660F38, Add, -200),# units:Shield Amount  index:156    from 300 To 100
        SetMemory(0x660F38, Add, -22937600),# units:Shield Amount  index:157    from 450 To 100
        SetMemory(0x660F3C, Add, -9830400),# units:Shield Amount  index:159    from 250 To 100
        SetMemory(0x660F40, Add, -400),# units:Shield Amount  index:160    from 500 To 100
        SetMemory(0x660F44, Add, -22937600),# units:Shield Amount  index:163    from 450 To 100
        SetMemory(0x660F48, Add, -400),# units:Shield Amount  index:164    from 500 To 100
        SetMemory(0x660F48, Add, -26214400),# units:Shield Amount  index:165    from 500 To 100
        SetMemory(0x660F4C, Add, -450),# units:Shield Amount  index:166    from 550 To 100
        SetMemory(0x660F4C, Add, -32768000),# units:Shield Amount  index:167    from 600 To 100
        SetMemory(0x660F50, Add, -26214400),# units:Shield Amount  index:169    from 500 To 100
        SetMemory(0x660F54, Add, -400),# units:Shield Amount  index:170    from 500 To 100
        SetMemory(0x660F54, Add, -22937600),# units:Shield Amount  index:171    from 450 To 100
        SetMemory(0x660F58, Add, -100),# units:Shield Amount  index:172    from 200 To 100
        SetMemory(0x662354, Add, -1280),# units:Hit Points  index:1    from 11520 To 10240
        SetMemory(0x662358, Add, -10240),# units:Hit Points  index:2    from 20480 To 10240
        SetMemory(0x66236C, Add, -5120),# units:Hit Points  index:7    from 15360 To 10240
        SetMemory(0x662370, Add, -20480),# units:Hit Points  index:8    from 30720 To 10240
        SetMemory(0x662374, Add, -40960),# units:Hit Points  index:9    from 51200 To 10240
        SetMemory(0x662378, Add, -30720),# units:Hit Points  index:10    from 40960 To 10240
        SetMemory(0x66237C, Add, -28160),# units:Hit Points  index:11    from 38400 To 10240
        SetMemory(0x662380, Add, -117760),# units:Hit Points  index:12    from 128000 To 10240
        SetMemory(0x662390, Add, -53760),# units:Hit Points  index:16    from 64000 To 10240
        SetMemory(0x66239C, Add, -66560),# units:Hit Points  index:19    from 76800 To 10240
        SetMemory(0x6623A0, Add, -40960),# units:Hit Points  index:20    from 51200 To 10240
        SetMemory(0x6623A4, Add, -117760),# units:Hit Points  index:21    from 128000 To 10240
        SetMemory(0x6623A8, Add, -194560),# units:Hit Points  index:22    from 204800 To 10240
        SetMemory(0x6623BC, Add, -245760),# units:Hit Points  index:27    from 256000 To 10240
        SetMemory(0x6623C0, Add, -207360),# units:Hit Points  index:28    from 217600 To 10240
        SetMemory(0x6623C4, Add, -168960),# units:Hit Points  index:29    from 179200 To 10240
        SetMemory(0x6623D0, Add, -2560),# units:Hit Points  index:32    from 12800 To 10240
        SetMemory(0x6623D8, Add, -5120),# units:Hit Points  index:34    from 15360 To 10240
        SetMemory(0x6623E4, Add, 1280),# units:Hit Points  index:37    from 8960 To 10240
        SetMemory(0x6623E8, Add, -10240),# units:Hit Points  index:38    from 20480 To 10240
        SetMemory(0x6623EC, Add, -92160),# units:Hit Points  index:39    from 102400 To 10240
        SetMemory(0x6623F0, Add, 2560),# units:Hit Points  index:40    from 7680 To 10240
        SetMemory(0x6623F8, Add, -40960),# units:Hit Points  index:42    from 51200 To 10240
        SetMemory(0x6623FC, Add, -20480),# units:Hit Points  index:43    from 30720 To 10240
        SetMemory(0x662400, Add, -28160),# units:Hit Points  index:44    from 38400 To 10240
        SetMemory(0x662404, Add, -20480),# units:Hit Points  index:45    from 30720 To 10240
        SetMemory(0x662408, Add, -10240),# units:Hit Points  index:46    from 20480 To 10240
        SetMemory(0x66240C, Add, 3840),# units:Hit Points  index:47    from 6400 To 10240
        SetMemory(0x662410, Add, -194560),# units:Hit Points  index:48    from 204800 To 10240
        SetMemory(0x662414, Add, -66560),# units:Hit Points  index:49    from 76800 To 10240
        SetMemory(0x662418, Add, -5120),# units:Hit Points  index:50    from 15360 To 10240
        SetMemory(0x66241C, Add, -92160),# units:Hit Points  index:51    from 102400 To 10240
        SetMemory(0x662420, Add, -53760),# units:Hit Points  index:52    from 64000 To 10240
        SetMemory(0x662424, Add, -30720),# units:Hit Points  index:53    from 40960 To 10240
        SetMemory(0x662428, Add, -20480),# units:Hit Points  index:54    from 30720 To 10240
        SetMemory(0x66242C, Add, -66560),# units:Hit Points  index:55    from 76800 To 10240
        SetMemory(0x662430, Add, -92160),# units:Hit Points  index:56    from 102400 To 10240
        SetMemory(0x662434, Add, -245760),# units:Hit Points  index:57    from 256000 To 10240
        SetMemory(0x662440, Add, -15360),# units:Hit Points  index:60    from 25600 To 10240
        SetMemory(0x662444, Add, -10240),# units:Hit Points  index:61    from 20480 To 10240
        SetMemory(0x662448, Add, -53760),# units:Hit Points  index:62    from 64000 To 10240
        SetMemory(0x66244C, Add, 3840),# units:Hit Points  index:63    from 6400 To 10240
        SetMemory(0x662450, Add, 5120),# units:Hit Points  index:64    from 5120 To 10240
        SetMemory(0x662454, Add, -15360),# units:Hit Points  index:65    from 25600 To 10240
        SetMemory(0x662458, Add, -15360),# units:Hit Points  index:66    from 25600 To 10240
        SetMemory(0x662460, Add, 7680),# units:Hit Points  index:68    from 2560 To 10240
        SetMemory(0x662464, Add, -10240),# units:Hit Points  index:69    from 20480 To 10240
        SetMemory(0x662468, Add, -28160),# units:Hit Points  index:70    from 38400 To 10240
        SetMemory(0x66246C, Add, -40960),# units:Hit Points  index:71    from 51200 To 10240
        SetMemory(0x662470, Add, -66560),# units:Hit Points  index:72    from 76800 To 10240
        SetMemory(0x66247C, Add, -5120),# units:Hit Points  index:75    from 15360 To 10240
        SetMemory(0x662480, Add, -15360),# units:Hit Points  index:76    from 25600 To 10240
        SetMemory(0x662484, Add, -51200),# units:Hit Points  index:77    from 61440 To 10240
        SetMemory(0x662488, Add, -51200),# units:Hit Points  index:78    from 61440 To 10240
        SetMemory(0x66248C, Add, -10240),# units:Hit Points  index:79    from 20480 To 10240
        SetMemory(0x662490, Add, -92160),# units:Hit Points  index:80    from 102400 To 10240
        SetMemory(0x662494, Add, -40960),# units:Hit Points  index:81    from 51200 To 10240
        SetMemory(0x662498, Add, -194560),# units:Hit Points  index:82    from 204800 To 10240
        SetMemory(0x66249C, Add, -15360),# units:Hit Points  index:83    from 25600 To 10240
        SetMemory(0x6624A8, Add, -143360),# units:Hit Points  index:86    from 153600 To 10240
        SetMemory(0x6624AC, Add, -10240),# units:Hit Points  index:87    from 20480 To 10240
        SetMemory(0x6624B0, Add, -53760),# units:Hit Points  index:88    from 64000 To 10240
        SetMemory(0x6624B4, Add, -5120),# units:Hit Points  index:89    from 15360 To 10240
        SetMemory(0x6624B8, Add, -5120),# units:Hit Points  index:90    from 15360 To 10240
        SetMemory(0x6624C4, Add, -5120),# units:Hit Points  index:93    from 15360 To 10240
        SetMemory(0x6624C8, Add, -5120),# units:Hit Points  index:94    from 15360 To 10240
        SetMemory(0x6624CC, Add, -5120),# units:Hit Points  index:95    from 15360 To 10240
        SetMemory(0x6624D0, Add, -5120),# units:Hit Points  index:96    from 15360 To 10240
        SetMemory(0x6624D8, Add, -15360),# units:Hit Points  index:98    from 25600 To 10240
        SetMemory(0x6624DC, Add, -40960),# units:Hit Points  index:99    from 51200 To 10240
        SetMemory(0x6624E0, Add, -53760),# units:Hit Points  index:100    from 64000 To 10240
        SetMemory(0x6624E8, Add, -168960),# units:Hit Points  index:102    from 179200 To 10240
        SetMemory(0x6624EC, Add, -21760),# units:Hit Points  index:103    from 32000 To 10240
        SetMemory(0x6624F0, Add, -66560),# units:Hit Points  index:104    from 76800 To 10240
        SetMemory(0x6624F8, Add, -373760),# units:Hit Points  index:106    from 384000 To 10240
        SetMemory(0x6624FC, Add, -117760),# units:Hit Points  index:107    from 128000 To 10240
        SetMemory(0x662504, Add, -117760),# units:Hit Points  index:109    from 128000 To 10240
        SetMemory(0x662508, Add, -181760),# units:Hit Points  index:110    from 192000 To 10240
        SetMemory(0x66250C, Add, -245760),# units:Hit Points  index:111    from 256000 To 10240
        SetMemory(0x662510, Add, -143360),# units:Hit Points  index:112    from 153600 To 10240
        SetMemory(0x662514, Add, -309760),# units:Hit Points  index:113    from 320000 To 10240
        SetMemory(0x662518, Add, -322560),# units:Hit Points  index:114    from 332800 To 10240
        SetMemory(0x66251C, Add, -117760),# units:Hit Points  index:115    from 128000 To 10240
        SetMemory(0x662520, Add, -207360),# units:Hit Points  index:116    from 217600 To 10240
        SetMemory(0x662524, Add, -181760),# units:Hit Points  index:117    from 192000 To 10240
        SetMemory(0x662528, Add, -143360),# units:Hit Points  index:118    from 153600 To 10240
        SetMemory(0x662530, Add, -181760),# units:Hit Points  index:120    from 192000 To 10240
        SetMemory(0x662538, Add, -207360),# units:Hit Points  index:122    from 217600 To 10240
        SetMemory(0x66253C, Add, -181760),# units:Hit Points  index:123    from 192000 To 10240
        SetMemory(0x662540, Add, -40960),# units:Hit Points  index:124    from 51200 To 10240
        SetMemory(0x662544, Add, -79360),# units:Hit Points  index:125    from 89600 To 10240
        SetMemory(0x662548, Add, -168960),# units:Hit Points  index:126    from 179200 To 10240
        SetMemory(0x66254C, Add, -501760),# units:Hit Points  index:127    from 512000 To 10240
        SetMemory(0x662550, Add, -2549760),# units:Hit Points  index:128    from 2560000 To 10240
        SetMemory(0x662554, Add, -2549760),# units:Hit Points  index:129    from 2560000 To 10240
        SetMemory(0x662558, Add, -373760),# units:Hit Points  index:130    from 384000 To 10240
        SetMemory(0x66255C, Add, -309760),# units:Hit Points  index:131    from 320000 To 10240
        SetMemory(0x662560, Add, -450560),# units:Hit Points  index:132    from 460800 To 10240
        SetMemory(0x662564, Add, -629760),# units:Hit Points  index:133    from 640000 To 10240
        SetMemory(0x662568, Add, -53760),# units:Hit Points  index:134    from 64000 To 10240
        SetMemory(0x66256C, Add, -207360),# units:Hit Points  index:135    from 217600 To 10240
        SetMemory(0x662570, Add, -207360),# units:Hit Points  index:136    from 217600 To 10240
        SetMemory(0x662574, Add, -245760),# units:Hit Points  index:137    from 256000 To 10240
        SetMemory(0x662578, Add, -207360),# units:Hit Points  index:138    from 217600 To 10240
        SetMemory(0x66257C, Add, -181760),# units:Hit Points  index:139    from 192000 To 10240
        SetMemory(0x662580, Add, -143360),# units:Hit Points  index:140    from 153600 To 10240
        SetMemory(0x662584, Add, -143360),# units:Hit Points  index:141    from 153600 To 10240
        SetMemory(0x662588, Add, -181760),# units:Hit Points  index:142    from 192000 To 10240
        SetMemory(0x66258C, Add, -92160),# units:Hit Points  index:143    from 102400 To 10240
        SetMemory(0x662590, Add, -92160),# units:Hit Points  index:144    from 102400 To 10240
        SetMemory(0x662598, Add, -66560),# units:Hit Points  index:146    from 76800 To 10240
        SetMemory(0x66259C, Add, -1269760),# units:Hit Points  index:147    from 1280000 To 10240
        SetMemory(0x6625A0, Add, -629760),# units:Hit Points  index:148    from 640000 To 10240
        SetMemory(0x6625A4, Add, -181760),# units:Hit Points  index:149    from 192000 To 10240
        SetMemory(0x6625A8, Add, -53760),# units:Hit Points  index:150    from 64000 To 10240
        SetMemory(0x6625AC, Add, -373760),# units:Hit Points  index:151    from 384000 To 10240
        SetMemory(0x6625B0, Add, -373760),# units:Hit Points  index:152    from 384000 To 10240
        SetMemory(0x6625B8, Add, -181760),# units:Hit Points  index:154    from 192000 To 10240
        SetMemory(0x6625BC, Add, -117760),# units:Hit Points  index:155    from 128000 To 10240
        SetMemory(0x6625C0, Add, -66560),# units:Hit Points  index:156    from 76800 To 10240
        SetMemory(0x6625C4, Add, -104960),# units:Hit Points  index:157    from 115200 To 10240
        SetMemory(0x6625CC, Add, -53760),# units:Hit Points  index:159    from 64000 To 10240
        SetMemory(0x6625D0, Add, -117760),# units:Hit Points  index:160    from 128000 To 10240
        SetMemory(0x6625D8, Add, -15360),# units:Hit Points  index:162    from 25600 To 10240
        SetMemory(0x6625DC, Add, -104960),# units:Hit Points  index:163    from 115200 To 10240
        SetMemory(0x6625E0, Add, -117760),# units:Hit Points  index:164    from 128000 To 10240
        SetMemory(0x6625E4, Add, -117760),# units:Hit Points  index:165    from 128000 To 10240
        SetMemory(0x6625E8, Add, -130560),# units:Hit Points  index:166    from 140800 To 10240
        SetMemory(0x6625EC, Add, -143360),# units:Hit Points  index:167    from 153600 To 10240
        SetMemory(0x6625F0, Add, -501760),# units:Hit Points  index:168    from 512000 To 10240
        SetMemory(0x6625F4, Add, -117760),# units:Hit Points  index:169    from 128000 To 10240
        SetMemory(0x6625F8, Add, -117760),# units:Hit Points  index:170    from 128000 To 10240
        SetMemory(0x6625FC, Add, -104960),# units:Hit Points  index:171    from 115200 To 10240
        SetMemory(0x662600, Add, -40960),# units:Hit Points  index:172    from 51200 To 10240
        SetMemory(0x662604, Add, -25589760),# units:Hit Points  index:173    from 25600000 To 10240
        SetMemory(0x662608, Add, -373760),# units:Hit Points  index:174    from 384000 To 10240
        SetMemory(0x66260C, Add, -1269760),# units:Hit Points  index:175    from 1280000 To 10240
        SetMemory(0x662644, Add, -168960),# units:Hit Points  index:189    from 179200 To 10240
        SetMemory(0x662648, Add, -501760),# units:Hit Points  index:190    from 512000 To 10240
        SetMemory(0x662658, Add, -25589760),# units:Hit Points  index:194    from 25600000 To 10240
        SetMemory(0x66265C, Add, -25589760),# units:Hit Points  index:195    from 25600000 To 10240
        SetMemory(0x662660, Add, -25589760),# units:Hit Points  index:196    from 25600000 To 10240
        SetMemory(0x662670, Add, -194560),# units:Hit Points  index:200    from 204800 To 10240
        SetMemory(0x662674, Add, -629760),# units:Hit Points  index:201    from 640000 To 10240
        SetMemory(0x6626AC, Add, -25589760),# units:Hit Points  index:215    from 25600000 To 10240
        SetMemory(0x6626B0, Add, -194560),# units:Hit Points  index:216    from 204800 To 10240
        SetMemory(0x6626B4, Add, -194560),# units:Hit Points  index:217    from 204800 To 10240
        SetMemory(0x6626B8, Add, -194560),# units:Hit Points  index:218    from 204800 To 10240
        SetMemory(0x6626BC, Add, -194560),# units:Hit Points  index:219    from 204800 To 10240
        SetMemory(0x6626C0, Add, -194560),# units:Hit Points  index:220    from 204800 To 10240
        SetMemory(0x6626C4, Add, -194560),# units:Hit Points  index:221    from 204800 To 10240
        SetMemory(0x6626C8, Add, -194560),# units:Hit Points  index:222    from 204800 To 10240
        SetMemory(0x6626CC, Add, -194560),# units:Hit Points  index:223    from 204800 To 10240
        SetMemory(0x663158, Add, -14),# units:Elevation Level  index:8    from 18 To 4
        SetMemory(0x663158, Add, -3072),# units:Elevation Level  index:9    from 16 To 4
        SetMemory(0x663158, Add, -201326592),# units:Elevation Level  index:11    from 16 To 4
        SetMemory(0x66315C, Add, -12),# units:Elevation Level  index:12    from 16 To 4
        SetMemory(0x663164, Add, -3584),# units:Elevation Level  index:21    from 18 To 4
        SetMemory(0x663164, Add, -786432),# units:Elevation Level  index:22    from 16 To 4
        SetMemory(0x663168, Add, -201326592),# units:Elevation Level  index:27    from 16 To 4
        SetMemory(0x66316C, Add, -12),# units:Elevation Level  index:28    from 16 To 4
        SetMemory(0x66316C, Add, -3072),# units:Elevation Level  index:29    from 16 To 4
        SetMemory(0x663178, Add, -786432),# units:Elevation Level  index:42    from 16 To 4
        SetMemory(0x663178, Add, -234881024),# units:Elevation Level  index:43    from 18 To 4
        SetMemory(0x66317C, Add, -14),# units:Elevation Level  index:44    from 18 To 4
        SetMemory(0x66317C, Add, -3584),# units:Elevation Level  index:45    from 18 To 4
        SetMemory(0x66317C, Add, -234881024),# units:Elevation Level  index:47    from 18 To 4
        SetMemory(0x663180, Add, -3584),# units:Elevation Level  index:49    from 18 To 4
        SetMemory(0x663184, Add, -234881024),# units:Elevation Level  index:55    from 18 To 4
        SetMemory(0x663188, Add, -14),# units:Elevation Level  index:56    from 18 To 4
        SetMemory(0x663188, Add, -3072),# units:Elevation Level  index:57    from 16 To 4
        SetMemory(0x66318C, Add, -14),# units:Elevation Level  index:60    from 18 To 4
        SetMemory(0x66318C, Add, -917504),# units:Elevation Level  index:62    from 18 To 4
        SetMemory(0x663194, Add, -3584),# units:Elevation Level  index:69    from 18 To 4
        SetMemory(0x663194, Add, -917504),# units:Elevation Level  index:70    from 18 To 4
        SetMemory(0x663194, Add, -201326592),# units:Elevation Level  index:71    from 16 To 4
        SetMemory(0x663198, Add, -12),# units:Elevation Level  index:72    from 16 To 4
        SetMemory(0x6631A0, Add, -14),# units:Elevation Level  index:80    from 18 To 4
        SetMemory(0x6631A0, Add, -786432),# units:Elevation Level  index:82    from 16 To 4
        SetMemory(0x6631A4, Add, -14),# units:Elevation Level  index:84    from 18 To 4
        SetMemory(0x6631A4, Add, -786432),# units:Elevation Level  index:86    from 16 To 4
        SetMemory(0x6631A8, Add, -14),# units:Elevation Level  index:88    from 18 To 4
        SetMemory(0x6631AC, Add, -917504),# units:Elevation Level  index:94    from 18 To 4
        SetMemory(0x6631B0, Add, -917504),# units:Elevation Level  index:98    from 18 To 4
        SetMemory(0x6631B4, Add, -786432),# units:Elevation Level  index:102    from 16 To 4
        SetMemory(0x6631CC, Add, 256),# units:Elevation Level  index:125    from 3 To 4
        SetMemory(0x6631DC, Add, 131072),# units:Elevation Level  index:142    from 2 To 4
        SetMemory(0x663210, Add, 262144),# units:Elevation Level  index:194    from 0 To 4
        SetMemory(0x663210, Add, 67108864),# units:Elevation Level  index:195    from 0 To 4
        SetMemory(0x663214, Add, 4),# units:Elevation Level  index:196    from 0 To 4
        SetMemory(0x660FC8, Add, -8388608),# units:Unknown (old Movement)  index:2    from 193 To 65
        SetMemory(0x660FCC, Add, -2147483648),# units:Unknown (old Movement)  index:7    from 193 To 65
        SetMemory(0x660FD0, Add, -132),# units:Unknown (old Movement)  index:8    from 197 To 65
        SetMemory(0x660FD0, Add, -33792),# units:Unknown (old Movement)  index:9    from 197 To 65
        SetMemory(0x660FD0, Add, -2214592512),# units:Unknown (old Movement)  index:11    from 197 To 65
        SetMemory(0x660FD4, Add, -132),# units:Unknown (old Movement)  index:12    from 197 To 65
        SetMemory(0x660FD8, Add, -2147483648),# units:Unknown (old Movement)  index:19    from 193 To 65
        SetMemory(0x660FDC, Add, -33792),# units:Unknown (old Movement)  index:21    from 197 To 65
        SetMemory(0x660FDC, Add, -8650752),# units:Unknown (old Movement)  index:22    from 197 To 65
        SetMemory(0x660FE0, Add, -2214592512),# units:Unknown (old Movement)  index:27    from 197 To 65
        SetMemory(0x660FE4, Add, -132),# units:Unknown (old Movement)  index:28    from 197 To 65
        SetMemory(0x660FE4, Add, -33792),# units:Unknown (old Movement)  index:29    from 197 To 65
        SetMemory(0x660FF0, Add, -32768),# units:Unknown (old Movement)  index:41    from 193 To 65
        SetMemory(0x660FF0, Add, -8650752),# units:Unknown (old Movement)  index:42    from 197 To 65
        SetMemory(0x660FF0, Add, -2214592512),# units:Unknown (old Movement)  index:43    from 197 To 65
        SetMemory(0x660FF4, Add, -132),# units:Unknown (old Movement)  index:44    from 197 To 65
        SetMemory(0x660FF4, Add, -33792),# units:Unknown (old Movement)  index:45    from 197 To 65
        SetMemory(0x660FF4, Add, -2214592512),# units:Unknown (old Movement)  index:47    from 197 To 65
        SetMemory(0x660FF8, Add, -33792),# units:Unknown (old Movement)  index:49    from 197 To 65
        SetMemory(0x660FFC, Add, -2214592512),# units:Unknown (old Movement)  index:55    from 197 To 65
        SetMemory(0x661000, Add, -132),# units:Unknown (old Movement)  index:56    from 197 To 65
        SetMemory(0x661000, Add, -33792),# units:Unknown (old Movement)  index:57    from 197 To 65
        SetMemory(0x661004, Add, -132),# units:Unknown (old Movement)  index:60    from 197 To 65
        SetMemory(0x661004, Add, -8650752),# units:Unknown (old Movement)  index:62    from 197 To 65
        SetMemory(0x661004, Add, -2147483648),# units:Unknown (old Movement)  index:63    from 193 To 65
        SetMemory(0x661008, Add, -128),# units:Unknown (old Movement)  index:64    from 193 To 65
        SetMemory(0x66100C, Add, -128),# units:Unknown (old Movement)  index:68    from 193 To 65
        SetMemory(0x66100C, Add, -33792),# units:Unknown (old Movement)  index:69    from 197 To 65
        SetMemory(0x66100C, Add, -8650752),# units:Unknown (old Movement)  index:70    from 197 To 65
        SetMemory(0x66100C, Add, -2214592512),# units:Unknown (old Movement)  index:71    from 197 To 65
        SetMemory(0x661010, Add, -132),# units:Unknown (old Movement)  index:72    from 197 To 65
        SetMemory(0x661014, Add, -128),# units:Unknown (old Movement)  index:76    from 193 To 65
        SetMemory(0x661018, Add, -132),# units:Unknown (old Movement)  index:80    from 197 To 65
        SetMemory(0x661018, Add, -8650752),# units:Unknown (old Movement)  index:82    from 197 To 65
        SetMemory(0x66101C, Add, -132),# units:Unknown (old Movement)  index:84    from 197 To 65
        SetMemory(0x66101C, Add, -8650752),# units:Unknown (old Movement)  index:86    from 197 To 65
        SetMemory(0x661020, Add, -132),# units:Unknown (old Movement)  index:88    from 197 To 65
        SetMemory(0x661024, Add, -8650752),# units:Unknown (old Movement)  index:94    from 197 To 65
        SetMemory(0x661028, Add, -8650752),# units:Unknown (old Movement)  index:98    from 197 To 65
        SetMemory(0x66102C, Add, -8650752),# units:Unknown (old Movement)  index:102    from 197 To 65
        SetMemory(0x661030, Add, -8650752),# units:Unknown (old Movement)  index:106    from 197 To 65
        SetMemory(0x661030, Add, 1090519040),# units:Unknown (old Movement)  index:107    from 0 To 65
        SetMemory(0x661034, Add, 16640),# units:Unknown (old Movement)  index:109    from 0 To 65
        SetMemory(0x661034, Add, 4259840),# units:Unknown (old Movement)  index:110    from 0 To 65
        SetMemory(0x661034, Add, -2214592512),# units:Unknown (old Movement)  index:111    from 197 To 65
        SetMemory(0x661038, Add, 65),# units:Unknown (old Movement)  index:112    from 0 To 65
        SetMemory(0x661038, Add, -33792),# units:Unknown (old Movement)  index:113    from 197 To 65
        SetMemory(0x661038, Add, -8650752),# units:Unknown (old Movement)  index:114    from 197 To 65
        SetMemory(0x661038, Add, 1090519040),# units:Unknown (old Movement)  index:115    from 0 To 65
        SetMemory(0x66103C, Add, -132),# units:Unknown (old Movement)  index:116    from 197 To 65
        SetMemory(0x66103C, Add, 16640),# units:Unknown (old Movement)  index:117    from 0 To 65
        SetMemory(0x66103C, Add, 4259840),# units:Unknown (old Movement)  index:118    from 0 To 65
        SetMemory(0x661040, Add, 65),# units:Unknown (old Movement)  index:120    from 0 To 65
        SetMemory(0x661040, Add, -8650752),# units:Unknown (old Movement)  index:122    from 197 To 65
        SetMemory(0x661040, Add, 1090519040),# units:Unknown (old Movement)  index:123    from 0 To 65
        SetMemory(0x661044, Add, 65),# units:Unknown (old Movement)  index:124    from 0 To 65
        SetMemory(0x661044, Add, 16640),# units:Unknown (old Movement)  index:125    from 0 To 65
        SetMemory(0x661044, Add, 4259840),# units:Unknown (old Movement)  index:126    from 0 To 65
        SetMemory(0x661044, Add, 1090519040),# units:Unknown (old Movement)  index:127    from 0 To 65
        SetMemory(0x661048, Add, -132),# units:Unknown (old Movement)  index:128    from 197 To 65
        SetMemory(0x661048, Add, -33792),# units:Unknown (old Movement)  index:129    from 197 To 65
        SetMemory(0x661048, Add, -8650752),# units:Unknown (old Movement)  index:130    from 197 To 65
        SetMemory(0x661048, Add, 1090519040),# units:Unknown (old Movement)  index:131    from 0 To 65
        SetMemory(0x66104C, Add, 65),# units:Unknown (old Movement)  index:132    from 0 To 65
        SetMemory(0x66104C, Add, 16640),# units:Unknown (old Movement)  index:133    from 0 To 65
        SetMemory(0x66104C, Add, 4259840),# units:Unknown (old Movement)  index:134    from 0 To 65
        SetMemory(0x66104C, Add, 1090519040),# units:Unknown (old Movement)  index:135    from 0 To 65
        SetMemory(0x661050, Add, 65),# units:Unknown (old Movement)  index:136    from 0 To 65
        SetMemory(0x661050, Add, 16640),# units:Unknown (old Movement)  index:137    from 0 To 65
        SetMemory(0x661050, Add, 4259840),# units:Unknown (old Movement)  index:138    from 0 To 65
        SetMemory(0x661050, Add, 1090519040),# units:Unknown (old Movement)  index:139    from 0 To 65
        SetMemory(0x661054, Add, 65),# units:Unknown (old Movement)  index:140    from 0 To 65
        SetMemory(0x661054, Add, 16640),# units:Unknown (old Movement)  index:141    from 0 To 65
        SetMemory(0x661054, Add, 4259840),# units:Unknown (old Movement)  index:142    from 0 To 65
        SetMemory(0x661054, Add, 1090519040),# units:Unknown (old Movement)  index:143    from 0 To 65
        SetMemory(0x661058, Add, 65),# units:Unknown (old Movement)  index:144    from 0 To 65
        SetMemory(0x661058, Add, 65536),# units:Unknown (old Movement)  index:146    from 64 To 65
        SetMemory(0x661058, Add, 1090519040),# units:Unknown (old Movement)  index:147    from 0 To 65
        SetMemory(0x66105C, Add, 65),# units:Unknown (old Movement)  index:148    from 0 To 65
        SetMemory(0x66105C, Add, 16640),# units:Unknown (old Movement)  index:149    from 0 To 65
        SetMemory(0x66105C, Add, 4259840),# units:Unknown (old Movement)  index:150    from 0 To 65
        SetMemory(0x66105C, Add, 1090519040),# units:Unknown (old Movement)  index:151    from 0 To 65
        SetMemory(0x661060, Add, 65),# units:Unknown (old Movement)  index:152    from 0 To 65
        SetMemory(0x661060, Add, 4259840),# units:Unknown (old Movement)  index:154    from 0 To 65
        SetMemory(0x661060, Add, 1090519040),# units:Unknown (old Movement)  index:155    from 0 To 65
        SetMemory(0x661064, Add, 65),# units:Unknown (old Movement)  index:156    from 0 To 65
        SetMemory(0x661064, Add, 16640),# units:Unknown (old Movement)  index:157    from 0 To 65
        SetMemory(0x661064, Add, 1090519040),# units:Unknown (old Movement)  index:159    from 0 To 65
        SetMemory(0x661068, Add, 65),# units:Unknown (old Movement)  index:160    from 0 To 65
        SetMemory(0x661068, Add, 4259840),# units:Unknown (old Movement)  index:162    from 0 To 65
        SetMemory(0x661068, Add, 1090519040),# units:Unknown (old Movement)  index:163    from 0 To 65
        SetMemory(0x66106C, Add, 65),# units:Unknown (old Movement)  index:164    from 0 To 65
        SetMemory(0x66106C, Add, 16640),# units:Unknown (old Movement)  index:165    from 0 To 65
        SetMemory(0x66106C, Add, 4259840),# units:Unknown (old Movement)  index:166    from 0 To 65
        SetMemory(0x66106C, Add, 1090519040),# units:Unknown (old Movement)  index:167    from 0 To 65
        SetMemory(0x661070, Add, 65),# units:Unknown (old Movement)  index:168    from 0 To 65
        SetMemory(0x661070, Add, 16640),# units:Unknown (old Movement)  index:169    from 0 To 65
        SetMemory(0x661070, Add, 4259840),# units:Unknown (old Movement)  index:170    from 0 To 65
        SetMemory(0x661070, Add, 1090519040),# units:Unknown (old Movement)  index:171    from 0 To 65
        SetMemory(0x661074, Add, 65),# units:Unknown (old Movement)  index:172    from 0 To 65
        SetMemory(0x661074, Add, 16640),# units:Unknown (old Movement)  index:173    from 0 To 65
        SetMemory(0x661074, Add, 4259840),# units:Unknown (old Movement)  index:174    from 0 To 65
        SetMemory(0x661074, Add, 1090519040),# units:Unknown (old Movement)  index:175    from 0 To 65
        SetMemory(0x661084, Add, 16640),# units:Unknown (old Movement)  index:189    from 0 To 65
        SetMemory(0x661084, Add, 4259840),# units:Unknown (old Movement)  index:190    from 0 To 65
        SetMemory(0x661088, Add, 4259840),# units:Unknown (old Movement)  index:194    from 0 To 65
        SetMemory(0x661088, Add, 1090519040),# units:Unknown (old Movement)  index:195    from 0 To 65
        SetMemory(0x66108C, Add, 65),# units:Unknown (old Movement)  index:196    from 0 To 65
        SetMemory(0x661090, Add, 65),# units:Unknown (old Movement)  index:200    from 0 To 65
        SetMemory(0x661090, Add, 16640),# units:Unknown (old Movement)  index:201    from 0 To 65
        SetMemory(0x66109C, Add, -2214592512),# units:Unknown (old Movement)  index:215    from 197 To 65
        SetMemory(0x6610A0, Add, -132),# units:Unknown (old Movement)  index:216    from 197 To 65
        SetMemory(0x6610A0, Add, -33792),# units:Unknown (old Movement)  index:217    from 197 To 65
        SetMemory(0x6610A0, Add, -8650752),# units:Unknown (old Movement)  index:218    from 197 To 65
        SetMemory(0x6610A0, Add, -2214592512),# units:Unknown (old Movement)  index:219    from 197 To 65
        SetMemory(0x6610A4, Add, -132),# units:Unknown (old Movement)  index:220    from 197 To 65
        SetMemory(0x6610A4, Add, -33792),# units:Unknown (old Movement)  index:221    from 197 To 65
        SetMemory(0x6610A4, Add, -8650752),# units:Unknown (old Movement)  index:222    from 197 To 65
        SetMemory(0x6610A4, Add, -2214592512),# units:Unknown (old Movement)  index:223    from 197 To 65
        SetMemory(0x663DD0, Add, -1024),# units:Rank/Sublabel  index:1    from 5 To 1
        SetMemory(0x663DD0, Add, -327680),# units:Rank/Sublabel  index:2    from 6 To 1
        SetMemory(0x663DD4, Add, 16777216),# units:Rank/Sublabel  index:7    from 1 To 2
        SetMemory(0x663DD8, Add, -9),# units:Rank/Sublabel  index:8    from 10 To 1
        SetMemory(0x663DD8, Add, -2560),# units:Rank/Sublabel  index:9    from 11 To 1
        SetMemory(0x663DD8, Add, -720896),# units:Rank/Sublabel  index:10    from 12 To 1
        SetMemory(0x663DD8, Add, -134217728),# units:Rank/Sublabel  index:11    from 9 To 1
        SetMemory(0x663DDC, Add, -14),# units:Rank/Sublabel  index:12    from 15 To 1
        SetMemory(0x663DE0, Add, -17),# units:Rank/Sublabel  index:16    from 18 To 1
        SetMemory(0x663DE0, Add, -268435456),# units:Rank/Sublabel  index:19    from 17 To 1
        SetMemory(0x663DE4, Add, -16),# units:Rank/Sublabel  index:20    from 17 To 1
        SetMemory(0x663DE4, Add, -3328),# units:Rank/Sublabel  index:21    from 14 To 1
        SetMemory(0x663DE4, Add, -917504),# units:Rank/Sublabel  index:22    from 15 To 1
        SetMemory(0x663DE8, Add, -335544320),# units:Rank/Sublabel  index:27    from 21 To 1
        SetMemory(0x663DEC, Add, -19),# units:Rank/Sublabel  index:28    from 20 To 1
        SetMemory(0x663DEC, Add, -5120),# units:Rank/Sublabel  index:29    from 21 To 1
        SetMemory(0x663DF0, Add, -3),# units:Rank/Sublabel  index:32    from 4 To 1
        SetMemory(0x663DF0, Add, -131072),# units:Rank/Sublabel  index:34    from 3 To 1
        SetMemory(0x663DF4, Add, -1024),# units:Rank/Sublabel  index:37    from 5 To 1
        SetMemory(0x663DF4, Add, -524288),# units:Rank/Sublabel  index:38    from 9 To 1
        SetMemory(0x663DF4, Add, -218103808),# units:Rank/Sublabel  index:39    from 14 To 1
        SetMemory(0x663DF8, Add, -2),# units:Rank/Sublabel  index:40    from 3 To 1
        SetMemory(0x663DF8, Add, 768),# units:Rank/Sublabel  index:41    from 4 To 7
        SetMemory(0x663DF8, Add, -65536),# units:Rank/Sublabel  index:42    from 8 To 7
        SetMemory(0x663DF8, Add, -50331648),# units:Rank/Sublabel  index:43    from 10 To 7
        SetMemory(0x663DFC, Add, -4),# units:Rank/Sublabel  index:44    from 11 To 7
        SetMemory(0x663DFC, Add, -3072),# units:Rank/Sublabel  index:45    from 13 To 1
        SetMemory(0x663DFC, Add, -327680),# units:Rank/Sublabel  index:46    from 12 To 7
        SetMemory(0x663DFC, Add, 16777216),# units:Rank/Sublabel  index:47    from 6 To 7
        SetMemory(0x663E00, Add, -11),# units:Rank/Sublabel  index:48    from 15 To 4
        SetMemory(0x663E00, Add, -2560),# units:Rank/Sublabel  index:49    from 15 To 5
        SetMemory(0x663E00, Add, -131072),# units:Rank/Sublabel  index:50    from 7 To 5
        SetMemory(0x663E00, Add, -150994944),# units:Rank/Sublabel  index:51    from 16 To 7
        SetMemory(0x663E04, Add, -9),# units:Rank/Sublabel  index:52    from 15 To 6
        SetMemory(0x663E04, Add, -2048),# units:Rank/Sublabel  index:53    from 15 To 7
        SetMemory(0x663E04, Add, -851968),# units:Rank/Sublabel  index:54    from 15 To 2
        SetMemory(0x663E04, Add, -218103808),# units:Rank/Sublabel  index:55    from 15 To 2
        SetMemory(0x663E08, Add, -13),# units:Rank/Sublabel  index:56    from 15 To 2
        SetMemory(0x663E08, Add, -3328),# units:Rank/Sublabel  index:57    from 15 To 2
        SetMemory(0x663E0C, Add, -6),# units:Rank/Sublabel  index:60    from 8 To 2
        SetMemory(0x663E0C, Add, -2560),# units:Rank/Sublabel  index:61    from 12 To 2
        SetMemory(0x663E0C, Add, -655360),# units:Rank/Sublabel  index:62    from 12 To 2
        SetMemory(0x663E0C, Add, -117440512),# units:Rank/Sublabel  index:63    from 9 To 2
        SetMemory(0x663E10, Add, 2),# units:Rank/Sublabel  index:64    from 0 To 2
        SetMemory(0x663E10, Add, -256),# units:Rank/Sublabel  index:65    from 3 To 2
        SetMemory(0x663E10, Add, -131072),# units:Rank/Sublabel  index:66    from 4 To 2
        SetMemory(0x663E10, Add, -67108864),# units:Rank/Sublabel  index:67    from 6 To 2
        SetMemory(0x663E14, Add, -7),# units:Rank/Sublabel  index:68    from 9 To 2
        SetMemory(0x663E14, Add, -1280),# units:Rank/Sublabel  index:69    from 7 To 2
        SetMemory(0x663E14, Add, -393216),# units:Rank/Sublabel  index:70    from 8 To 2
        SetMemory(0x663E14, Add, -134217728),# units:Rank/Sublabel  index:71    from 10 To 2
        SetMemory(0x663E18, Add, -9),# units:Rank/Sublabel  index:72    from 11 To 2
        SetMemory(0x663E18, Add, -655360),# units:Rank/Sublabel  index:74    from 12 To 2
        SetMemory(0x663E18, Add, -218103808),# units:Rank/Sublabel  index:75    from 15 To 2
        SetMemory(0x663E1C, Add, -15),# units:Rank/Sublabel  index:76    from 17 To 2
        SetMemory(0x663E1C, Add, -2816),# units:Rank/Sublabel  index:77    from 13 To 2
        SetMemory(0x663E1C, Add, -524288),# units:Rank/Sublabel  index:78    from 14 To 6
        SetMemory(0x663E1C, Add, -167772160),# units:Rank/Sublabel  index:79    from 16 To 6
        SetMemory(0x663E20, Add, -6),# units:Rank/Sublabel  index:80    from 12 To 6
        SetMemory(0x663E20, Add, -1280),# units:Rank/Sublabel  index:81    from 12 To 7
        SetMemory(0x663E20, Add, -655360),# units:Rank/Sublabel  index:82    from 17 To 7
        SetMemory(0x663E24, Add, 3),# units:Rank/Sublabel  index:84    from 2 To 5
        SetMemory(0x663E24, Add, -655360),# units:Rank/Sublabel  index:86    from 12 To 2
        SetMemory(0x663E24, Add, -150994944),# units:Rank/Sublabel  index:87    from 16 To 7
        SetMemory(0x663E28, Add, -7),# units:Rank/Sublabel  index:88    from 12 To 5
        SetMemory(0x663E28, Add, 1280),# units:Rank/Sublabel  index:89    from 0 To 5
        SetMemory(0x663E28, Add, 262144),# units:Rank/Sublabel  index:90    from 0 To 4
        SetMemory(0x663E2C, Add, 1024),# units:Rank/Sublabel  index:93    from 0 To 4
        SetMemory(0x663E2C, Add, 393216),# units:Rank/Sublabel  index:94    from 0 To 6
        SetMemory(0x663E2C, Add, 100663296),# units:Rank/Sublabel  index:95    from 0 To 6
        SetMemory(0x663E30, Add, 5),# units:Rank/Sublabel  index:96    from 0 To 5
        SetMemory(0x663E30, Add, -393216),# units:Rank/Sublabel  index:98    from 8 To 2
        SetMemory(0x663E30, Add, -251658240),# units:Rank/Sublabel  index:99    from 18 To 3
        SetMemory(0x663E34, Add, -19),# units:Rank/Sublabel  index:100    from 22 To 3
        SetMemory(0x663E34, Add, 196608),# units:Rank/Sublabel  index:102    from 0 To 3
        SetMemory(0x663E34, Add, -117440512),# units:Rank/Sublabel  index:103    from 10 To 3
        SetMemory(0x663E38, Add, -12),# units:Rank/Sublabel  index:104    from 15 To 3
        SetMemory(0x663E38, Add, 196608),# units:Rank/Sublabel  index:106    from 0 To 3
        SetMemory(0x663E38, Add, 33554432),# units:Rank/Sublabel  index:107    from 0 To 2
        SetMemory(0x663E3C, Add, 768),# units:Rank/Sublabel  index:109    from 0 To 3
        SetMemory(0x663E3C, Add, 393216),# units:Rank/Sublabel  index:110    from 0 To 6
        SetMemory(0x663E3C, Add, 50331648),# units:Rank/Sublabel  index:111    from 0 To 3
        SetMemory(0x663E40, Add, 3),# units:Rank/Sublabel  index:112    from 0 To 3
        SetMemory(0x663E40, Add, 768),# units:Rank/Sublabel  index:113    from 0 To 3
        SetMemory(0x663E40, Add, 196608),# units:Rank/Sublabel  index:114    from 0 To 3
        SetMemory(0x663E40, Add, 50331648),# units:Rank/Sublabel  index:115    from 0 To 3
        SetMemory(0x663E44, Add, 3),# units:Rank/Sublabel  index:116    from 0 To 3
        SetMemory(0x663E44, Add, 768),# units:Rank/Sublabel  index:117    from 0 To 3
        SetMemory(0x663E44, Add, 196608),# units:Rank/Sublabel  index:118    from 0 To 3
        SetMemory(0x663E48, Add, 3),# units:Rank/Sublabel  index:120    from 0 To 3
        SetMemory(0x663E48, Add, 196608),# units:Rank/Sublabel  index:122    from 0 To 3
        SetMemory(0x663E48, Add, 50331648),# units:Rank/Sublabel  index:123    from 0 To 3
        SetMemory(0x663E4C, Add, 3),# units:Rank/Sublabel  index:124    from 0 To 3
        SetMemory(0x663E4C, Add, 768),# units:Rank/Sublabel  index:125    from 0 To 3
        SetMemory(0x663E4C, Add, 196608),# units:Rank/Sublabel  index:126    from 0 To 3
        SetMemory(0x663E4C, Add, 50331648),# units:Rank/Sublabel  index:127    from 0 To 3
        SetMemory(0x663E50, Add, 2),# units:Rank/Sublabel  index:128    from 0 To 2
        SetMemory(0x663E50, Add, 2048),# units:Rank/Sublabel  index:129    from 0 To 8
        SetMemory(0x663E50, Add, 196608),# units:Rank/Sublabel  index:130    from 0 To 3
        SetMemory(0x663E50, Add, 50331648),# units:Rank/Sublabel  index:131    from 0 To 3
        SetMemory(0x663E54, Add, 3),# units:Rank/Sublabel  index:132    from 0 To 3
        SetMemory(0x663E54, Add, 768),# units:Rank/Sublabel  index:133    from 0 To 3
        SetMemory(0x663E54, Add, 196608),# units:Rank/Sublabel  index:134    from 0 To 3
        SetMemory(0x663E54, Add, 50331648),# units:Rank/Sublabel  index:135    from 0 To 3
        SetMemory(0x663E58, Add, 3),# units:Rank/Sublabel  index:136    from 0 To 3
        SetMemory(0x663E58, Add, 1536),# units:Rank/Sublabel  index:137    from 0 To 6
        SetMemory(0x663E58, Add, 393216),# units:Rank/Sublabel  index:138    from 0 To 6
        SetMemory(0x663E58, Add, 67108864),# units:Rank/Sublabel  index:139    from 0 To 4
        SetMemory(0x663E5C, Add, 4),# units:Rank/Sublabel  index:140    from 0 To 4
        SetMemory(0x663E5C, Add, 1024),# units:Rank/Sublabel  index:141    from 0 To 4
        SetMemory(0x663E5C, Add, 196608),# units:Rank/Sublabel  index:142    from 0 To 3
        SetMemory(0x663E5C, Add, 117440512),# units:Rank/Sublabel  index:143    from 0 To 7
        SetMemory(0x663E60, Add, 4),# units:Rank/Sublabel  index:144    from 0 To 4
        SetMemory(0x663E60, Add, 262144),# units:Rank/Sublabel  index:146    from 0 To 4
        SetMemory(0x663E60, Add, 100663296),# units:Rank/Sublabel  index:147    from 0 To 6
        SetMemory(0x663E64, Add, 5),# units:Rank/Sublabel  index:148    from 0 To 5
        SetMemory(0x663E64, Add, 1024),# units:Rank/Sublabel  index:149    from 0 To 4
        SetMemory(0x663E64, Add, 327680),# units:Rank/Sublabel  index:150    from 0 To 5
        SetMemory(0x663E64, Add, 100663296),# units:Rank/Sublabel  index:151    from 0 To 6
        SetMemory(0x663E68, Add, 6),# units:Rank/Sublabel  index:152    from 0 To 6
        SetMemory(0x663E68, Add, 458752),# units:Rank/Sublabel  index:154    from 0 To 7
        SetMemory(0x663E68, Add, 117440512),# units:Rank/Sublabel  index:155    from 0 To 7
        SetMemory(0x663E6C, Add, 3),# units:Rank/Sublabel  index:156    from 0 To 3
        SetMemory(0x663E6C, Add, 1280),# units:Rank/Sublabel  index:157    from 0 To 5
        SetMemory(0x663E6C, Add, 100663296),# units:Rank/Sublabel  index:159    from 0 To 6
        SetMemory(0x663E70, Add, 6),# units:Rank/Sublabel  index:160    from 0 To 6
        SetMemory(0x663E70, Add, 393216),# units:Rank/Sublabel  index:162    from 0 To 6
        SetMemory(0x663E70, Add, 117440512),# units:Rank/Sublabel  index:163    from 0 To 7
        SetMemory(0x663E74, Add, 4),# units:Rank/Sublabel  index:164    from 0 To 4
        SetMemory(0x663E74, Add, 1024),# units:Rank/Sublabel  index:165    from 0 To 4
        SetMemory(0x663E74, Add, 262144),# units:Rank/Sublabel  index:166    from 0 To 4
        SetMemory(0x663E74, Add, 67108864),# units:Rank/Sublabel  index:167    from 0 To 4
        SetMemory(0x663E78, Add, 4),# units:Rank/Sublabel  index:168    from 0 To 4
        SetMemory(0x663E78, Add, 1024),# units:Rank/Sublabel  index:169    from 0 To 4
        SetMemory(0x663E78, Add, 262144),# units:Rank/Sublabel  index:170    from 0 To 4
        SetMemory(0x663E78, Add, 67108864),# units:Rank/Sublabel  index:171    from 0 To 4
        SetMemory(0x663E7C, Add, 4),# units:Rank/Sublabel  index:172    from 0 To 4
        SetMemory(0x663E7C, Add, 1792),# units:Rank/Sublabel  index:173    from 0 To 7
        SetMemory(0x663E7C, Add, 327680),# units:Rank/Sublabel  index:174    from 0 To 5
        SetMemory(0x663E7C, Add, 83886080),# units:Rank/Sublabel  index:175    from 0 To 5
        SetMemory(0x663E8C, Add, 1280),# units:Rank/Sublabel  index:189    from 0 To 5
        SetMemory(0x663E8C, Add, 327680),# units:Rank/Sublabel  index:190    from 0 To 5
        SetMemory(0x663E90, Add, 458752),# units:Rank/Sublabel  index:194    from 0 To 7
        SetMemory(0x663E90, Add, 134217728),# units:Rank/Sublabel  index:195    from 0 To 8
        SetMemory(0x663E94, Add, 1),# units:Rank/Sublabel  index:196    from 0 To 1
        SetMemory(0x663E98, Add, 7),# units:Rank/Sublabel  index:200    from 0 To 7
        SetMemory(0x663E98, Add, 1792),# units:Rank/Sublabel  index:201    from 0 To 7
        SetMemory(0x663EA4, Add, 134217728),# units:Rank/Sublabel  index:215    from 0 To 8
        SetMemory(0x663EA8, Add, 3),# units:Rank/Sublabel  index:216    from 0 To 3
        SetMemory(0x663EA8, Add, 1280),# units:Rank/Sublabel  index:217    from 0 To 5
        SetMemory(0x663EA8, Add, 524288),# units:Rank/Sublabel  index:218    from 0 To 8
        SetMemory(0x663EA8, Add, 67108864),# units:Rank/Sublabel  index:219    from 0 To 4
        SetMemory(0x663EAC, Add, 9),# units:Rank/Sublabel  index:220    from 0 To 9
        SetMemory(0x663EAC, Add, 1280),# units:Rank/Sublabel  index:221    from 0 To 5
        SetMemory(0x663EAC, Add, 327680),# units:Rank/Sublabel  index:222    from 0 To 5
        SetMemory(0x663EAC, Add, 16777216),# units:Rank/Sublabel  index:223    from 0 To 1
        SetMemory(0x662EA0, Add, 5376),# units:Comp AI Idle  index:1    from 2 To 23
        SetMemory(0x662EA0, Add, 1376256),# units:Comp AI Idle  index:2    from 2 To 23
        SetMemory(0x662EA4, Add, 352321536),# units:Comp AI Idle  index:7    from 2 To 23
        SetMemory(0x662EA8, Add, 21),# units:Comp AI Idle  index:8    from 2 To 23
        SetMemory(0x662EA8, Add, 5376),# units:Comp AI Idle  index:9    from 2 To 23
        SetMemory(0x662EA8, Add, 1376256),# units:Comp AI Idle  index:10    from 2 To 23
        SetMemory(0x662EA8, Add, -1174405120),# units:Comp AI Idle  index:11    from 93 To 23
        SetMemory(0x662EAC, Add, 21),# units:Comp AI Idle  index:12    from 2 To 23
        SetMemory(0x662EB0, Add, 21),# units:Comp AI Idle  index:16    from 2 To 23
        SetMemory(0x662EB0, Add, 352321536),# units:Comp AI Idle  index:19    from 2 To 23
        SetMemory(0x662EB4, Add, 21),# units:Comp AI Idle  index:20    from 2 To 23
        SetMemory(0x662EB4, Add, 5376),# units:Comp AI Idle  index:21    from 2 To 23
        SetMemory(0x662EB4, Add, 1376256),# units:Comp AI Idle  index:22    from 2 To 23
        SetMemory(0x662EB8, Add, 352321536),# units:Comp AI Idle  index:27    from 2 To 23
        SetMemory(0x662EBC, Add, 21),# units:Comp AI Idle  index:28    from 2 To 23
        SetMemory(0x662EBC, Add, 5376),# units:Comp AI Idle  index:29    from 2 To 23
        SetMemory(0x662EC0, Add, 21),# units:Comp AI Idle  index:32    from 2 To 23
        SetMemory(0x662EC0, Add, -9961472),# units:Comp AI Idle  index:34    from 175 To 23
        SetMemory(0x662EC4, Add, 5376),# units:Comp AI Idle  index:37    from 2 To 23
        SetMemory(0x662EC4, Add, 1376256),# units:Comp AI Idle  index:38    from 2 To 23
        SetMemory(0x662EC4, Add, 352321536),# units:Comp AI Idle  index:39    from 2 To 23
        SetMemory(0x662EC8, Add, 21),# units:Comp AI Idle  index:40    from 2 To 23
        SetMemory(0x662EC8, Add, 5376),# units:Comp AI Idle  index:41    from 2 To 23
        SetMemory(0x662EC8, Add, -8912896),# units:Comp AI Idle  index:42    from 159 To 23
        SetMemory(0x662EC8, Add, 352321536),# units:Comp AI Idle  index:43    from 2 To 23
        SetMemory(0x662ECC, Add, 21),# units:Comp AI Idle  index:44    from 2 To 23
        SetMemory(0x662ECC, Add, 5376),# units:Comp AI Idle  index:45    from 2 To 23
        SetMemory(0x662ECC, Add, 1376256),# units:Comp AI Idle  index:46    from 2 To 23
        SetMemory(0x662ECC, Add, 352321536),# units:Comp AI Idle  index:47    from 2 To 23
        SetMemory(0x662ED0, Add, 21),# units:Comp AI Idle  index:48    from 2 To 23
        SetMemory(0x662ED0, Add, 5376),# units:Comp AI Idle  index:49    from 2 To 23
        SetMemory(0x662ED0, Add, 1376256),# units:Comp AI Idle  index:50    from 2 To 23
        SetMemory(0x662ED0, Add, 352321536),# units:Comp AI Idle  index:51    from 2 To 23
        SetMemory(0x662ED4, Add, 21),# units:Comp AI Idle  index:52    from 2 To 23
        SetMemory(0x662ED4, Add, 5376),# units:Comp AI Idle  index:53    from 2 To 23
        SetMemory(0x662ED4, Add, 1376256),# units:Comp AI Idle  index:54    from 2 To 23
        SetMemory(0x662ED4, Add, 352321536),# units:Comp AI Idle  index:55    from 2 To 23
        SetMemory(0x662ED8, Add, 21),# units:Comp AI Idle  index:56    from 2 To 23
        SetMemory(0x662ED8, Add, -34048),# units:Comp AI Idle  index:57    from 156 To 23
        SetMemory(0x662EDC, Add, 21),# units:Comp AI Idle  index:60    from 2 To 23
        SetMemory(0x662EDC, Add, 5376),# units:Comp AI Idle  index:61    from 2 To 23
        SetMemory(0x662EDC, Add, 1376256),# units:Comp AI Idle  index:62    from 2 To 23
        SetMemory(0x662EDC, Add, 352321536),# units:Comp AI Idle  index:63    from 2 To 23
        SetMemory(0x662EE0, Add, 21),# units:Comp AI Idle  index:64    from 2 To 23
        SetMemory(0x662EE0, Add, 5376),# units:Comp AI Idle  index:65    from 2 To 23
        SetMemory(0x662EE0, Add, 1376256),# units:Comp AI Idle  index:66    from 2 To 23
        SetMemory(0x662EE0, Add, 352321536),# units:Comp AI Idle  index:67    from 2 To 23
        SetMemory(0x662EE4, Add, 21),# units:Comp AI Idle  index:68    from 2 To 23
        SetMemory(0x662EE4, Add, -17920),# units:Comp AI Idle  index:69    from 93 To 23
        SetMemory(0x662EE4, Add, 1376256),# units:Comp AI Idle  index:70    from 2 To 23
        SetMemory(0x662EE4, Add, -1795162112),# units:Comp AI Idle  index:71    from 130 To 23
        SetMemory(0x662EE8, Add, -27),# units:Comp AI Idle  index:72    from 50 To 23
        SetMemory(0x662EE8, Add, 1376256),# units:Comp AI Idle  index:74    from 2 To 23
        SetMemory(0x662EE8, Add, 352321536),# units:Comp AI Idle  index:75    from 2 To 23
        SetMemory(0x662EEC, Add, 21),# units:Comp AI Idle  index:76    from 2 To 23
        SetMemory(0x662EEC, Add, 5376),# units:Comp AI Idle  index:77    from 2 To 23
        SetMemory(0x662EEC, Add, 1376256),# units:Comp AI Idle  index:78    from 2 To 23
        SetMemory(0x662EEC, Add, 352321536),# units:Comp AI Idle  index:79    from 2 To 23
        SetMemory(0x662EF0, Add, 21),# units:Comp AI Idle  index:80    from 2 To 23
        SetMemory(0x662EF0, Add, -8960),# units:Comp AI Idle  index:81    from 58 To 23
        SetMemory(0x662EF0, Add, -1769472),# units:Comp AI Idle  index:82    from 50 To 23
        SetMemory(0x662EF0, Add, -587202560),# units:Comp AI Idle  index:83    from 58 To 23
        SetMemory(0x662EF4, Add, -136),# units:Comp AI Idle  index:84    from 159 To 23
        SetMemory(0x662EF4, Add, -7012352),# units:Comp AI Idle  index:86    from 130 To 23
        SetMemory(0x662EF4, Add, 352321536),# units:Comp AI Idle  index:87    from 2 To 23
        SetMemory(0x662EF8, Add, 21),# units:Comp AI Idle  index:88    from 2 To 23
        SetMemory(0x662EF8, Add, 5376),# units:Comp AI Idle  index:89    from 2 To 23
        SetMemory(0x662EF8, Add, 1376256),# units:Comp AI Idle  index:90    from 2 To 23
        SetMemory(0x662EFC, Add, 5376),# units:Comp AI Idle  index:93    from 2 To 23
        SetMemory(0x662EFC, Add, 1376256),# units:Comp AI Idle  index:94    from 2 To 23
        SetMemory(0x662EFC, Add, 352321536),# units:Comp AI Idle  index:95    from 2 To 23
        SetMemory(0x662F00, Add, 21),# units:Comp AI Idle  index:96    from 2 To 23
        SetMemory(0x662F00, Add, 1376256),# units:Comp AI Idle  index:98    from 2 To 23
        SetMemory(0x662F00, Add, 352321536),# units:Comp AI Idle  index:99    from 2 To 23
        SetMemory(0x662F04, Add, 21),# units:Comp AI Idle  index:100    from 2 To 23
        SetMemory(0x662F04, Add, 1376256),# units:Comp AI Idle  index:102    from 2 To 23
        SetMemory(0x662F04, Add, 352321536),# units:Comp AI Idle  index:103    from 2 To 23
        SetMemory(0x662F08, Add, 21),# units:Comp AI Idle  index:104    from 2 To 23
        SetMemory(0x662F08, Add, -8716288),# units:Comp AI Idle  index:106    from 156 To 23
        SetMemory(0x662F08, Add, -2231369728),# units:Comp AI Idle  index:107    from 156 To 23
        SetMemory(0x662F0C, Add, -34048),# units:Comp AI Idle  index:109    from 156 To 23
        SetMemory(0x662F0C, Add, -8716288),# units:Comp AI Idle  index:110    from 156 To 23
        SetMemory(0x662F0C, Add, -2231369728),# units:Comp AI Idle  index:111    from 156 To 23
        SetMemory(0x662F10, Add, -133),# units:Comp AI Idle  index:112    from 156 To 23
        SetMemory(0x662F10, Add, -34048),# units:Comp AI Idle  index:113    from 156 To 23
        SetMemory(0x662F10, Add, -8716288),# units:Comp AI Idle  index:114    from 156 To 23
        SetMemory(0x662F10, Add, -2231369728),# units:Comp AI Idle  index:115    from 156 To 23
        SetMemory(0x662F14, Add, -133),# units:Comp AI Idle  index:116    from 156 To 23
        SetMemory(0x662F14, Add, -34048),# units:Comp AI Idle  index:117    from 156 To 23
        SetMemory(0x662F14, Add, -8716288),# units:Comp AI Idle  index:118    from 156 To 23
        SetMemory(0x662F18, Add, -133),# units:Comp AI Idle  index:120    from 156 To 23
        SetMemory(0x662F18, Add, -8716288),# units:Comp AI Idle  index:122    from 156 To 23
        SetMemory(0x662F18, Add, -2231369728),# units:Comp AI Idle  index:123    from 156 To 23
        SetMemory(0x662F1C, Add, 5),# units:Comp AI Idle  index:124    from 18 To 23
        SetMemory(0x662F1C, Add, -34048),# units:Comp AI Idle  index:125    from 156 To 23
        SetMemory(0x662F1C, Add, -8716288),# units:Comp AI Idle  index:126    from 156 To 23
        SetMemory(0x662F1C, Add, -2231369728),# units:Comp AI Idle  index:127    from 156 To 23
        SetMemory(0x662F20, Add, -74),# units:Comp AI Idle  index:128    from 97 To 23
        SetMemory(0x662F20, Add, -18944),# units:Comp AI Idle  index:129    from 97 To 23
        SetMemory(0x662F20, Add, -8716288),# units:Comp AI Idle  index:130    from 156 To 23
        SetMemory(0x662F20, Add, -1308622848),# units:Comp AI Idle  index:131    from 101 To 23
        SetMemory(0x662F24, Add, -78),# units:Comp AI Idle  index:132    from 101 To 23
        SetMemory(0x662F24, Add, -19968),# units:Comp AI Idle  index:133    from 101 To 23
        SetMemory(0x662F24, Add, -8716288),# units:Comp AI Idle  index:134    from 156 To 23
        SetMemory(0x662F24, Add, -2231369728),# units:Comp AI Idle  index:135    from 156 To 23
        SetMemory(0x662F28, Add, -133),# units:Comp AI Idle  index:136    from 156 To 23
        SetMemory(0x662F28, Add, -34048),# units:Comp AI Idle  index:137    from 156 To 23
        SetMemory(0x662F28, Add, -8716288),# units:Comp AI Idle  index:138    from 156 To 23
        SetMemory(0x662F28, Add, -2231369728),# units:Comp AI Idle  index:139    from 156 To 23
        SetMemory(0x662F2C, Add, -133),# units:Comp AI Idle  index:140    from 156 To 23
        SetMemory(0x662F2C, Add, -34048),# units:Comp AI Idle  index:141    from 156 To 23
        SetMemory(0x662F2C, Add, -8716288),# units:Comp AI Idle  index:142    from 156 To 23
        SetMemory(0x662F2C, Add, -1308622848),# units:Comp AI Idle  index:143    from 101 To 23
        SetMemory(0x662F30, Add, -78),# units:Comp AI Idle  index:144    from 101 To 23
        SetMemory(0x662F30, Add, -5111808),# units:Comp AI Idle  index:146    from 101 To 23
        SetMemory(0x662F30, Add, -2231369728),# units:Comp AI Idle  index:147    from 156 To 23
        SetMemory(0x662F34, Add, -133),# units:Comp AI Idle  index:148    from 156 To 23
        SetMemory(0x662F34, Add, -34048),# units:Comp AI Idle  index:149    from 156 To 23
        SetMemory(0x662F34, Add, -8716288),# units:Comp AI Idle  index:150    from 156 To 23
        SetMemory(0x662F34, Add, -2231369728),# units:Comp AI Idle  index:151    from 156 To 23
        SetMemory(0x662F38, Add, -133),# units:Comp AI Idle  index:152    from 156 To 23
        SetMemory(0x662F38, Add, -8716288),# units:Comp AI Idle  index:154    from 156 To 23
        SetMemory(0x662F38, Add, -2231369728),# units:Comp AI Idle  index:155    from 156 To 23
        SetMemory(0x662F3C, Add, -141),# units:Comp AI Idle  index:156    from 164 To 23
        SetMemory(0x662F3C, Add, -34048),# units:Comp AI Idle  index:157    from 156 To 23
        SetMemory(0x662F3C, Add, -2231369728),# units:Comp AI Idle  index:159    from 156 To 23
        SetMemory(0x662F40, Add, -133),# units:Comp AI Idle  index:160    from 156 To 23
        SetMemory(0x662F40, Add, 327680),# units:Comp AI Idle  index:162    from 18 To 23
        SetMemory(0x662F40, Add, -2231369728),# units:Comp AI Idle  index:163    from 156 To 23
        SetMemory(0x662F44, Add, -133),# units:Comp AI Idle  index:164    from 156 To 23
        SetMemory(0x662F44, Add, -34048),# units:Comp AI Idle  index:165    from 156 To 23
        SetMemory(0x662F44, Add, -8716288),# units:Comp AI Idle  index:166    from 156 To 23
        SetMemory(0x662F44, Add, -2231369728),# units:Comp AI Idle  index:167    from 156 To 23
        SetMemory(0x662F48, Add, -133),# units:Comp AI Idle  index:168    from 156 To 23
        SetMemory(0x662F48, Add, -34048),# units:Comp AI Idle  index:169    from 156 To 23
        SetMemory(0x662F48, Add, -8716288),# units:Comp AI Idle  index:170    from 156 To 23
        SetMemory(0x662F48, Add, -2231369728),# units:Comp AI Idle  index:171    from 156 To 23
        SetMemory(0x662F4C, Add, -133),# units:Comp AI Idle  index:172    from 156 To 23
        SetMemory(0x662F4C, Add, -34048),# units:Comp AI Idle  index:173    from 156 To 23
        SetMemory(0x662F4C, Add, -8716288),# units:Comp AI Idle  index:174    from 156 To 23
        SetMemory(0x662F4C, Add, -2231369728),# units:Comp AI Idle  index:175    from 156 To 23
        SetMemory(0x662F5C, Add, -34048),# units:Comp AI Idle  index:189    from 156 To 23
        SetMemory(0x662F5C, Add, -8716288),# units:Comp AI Idle  index:190    from 156 To 23
        SetMemory(0x662F68, Add, -133),# units:Comp AI Idle  index:200    from 156 To 23
        SetMemory(0x662F68, Add, -34048),# units:Comp AI Idle  index:201    from 156 To 23
        SetMemory(0x662F74, Add, -1241513984),# units:Comp AI Idle  index:215    from 97 To 23
        SetMemory(0x662F78, Add, -74),# units:Comp AI Idle  index:216    from 97 To 23
        SetMemory(0x662F78, Add, -18944),# units:Comp AI Idle  index:217    from 97 To 23
        SetMemory(0x662F78, Add, -4849664),# units:Comp AI Idle  index:218    from 97 To 23
        SetMemory(0x662F78, Add, -1241513984),# units:Comp AI Idle  index:219    from 97 To 23
        SetMemory(0x662F7C, Add, -74),# units:Comp AI Idle  index:220    from 97 To 23
        SetMemory(0x662F7C, Add, -18944),# units:Comp AI Idle  index:221    from 97 To 23
        SetMemory(0x662F7C, Add, -4849664),# units:Comp AI Idle  index:222    from 97 To 23
        SetMemory(0x662F7C, Add, -1241513984),# units:Comp AI Idle  index:223    from 97 To 23
        SetMemory(0x662268, Add, 5376),# units:Human AI Idle  index:1    from 2 To 23
        SetMemory(0x662268, Add, 1376256),# units:Human AI Idle  index:2    from 2 To 23
        SetMemory(0x66226C, Add, 352321536),# units:Human AI Idle  index:7    from 2 To 23
        SetMemory(0x662270, Add, 21),# units:Human AI Idle  index:8    from 2 To 23
        SetMemory(0x662270, Add, 5376),# units:Human AI Idle  index:9    from 2 To 23
        SetMemory(0x662270, Add, 1376256),# units:Human AI Idle  index:10    from 2 To 23
        SetMemory(0x662270, Add, -1174405120),# units:Human AI Idle  index:11    from 93 To 23
        SetMemory(0x662274, Add, 21),# units:Human AI Idle  index:12    from 2 To 23
        SetMemory(0x662278, Add, 21),# units:Human AI Idle  index:16    from 2 To 23
        SetMemory(0x662278, Add, 352321536),# units:Human AI Idle  index:19    from 2 To 23
        SetMemory(0x66227C, Add, 21),# units:Human AI Idle  index:20    from 2 To 23
        SetMemory(0x66227C, Add, 5376),# units:Human AI Idle  index:21    from 2 To 23
        SetMemory(0x66227C, Add, 1376256),# units:Human AI Idle  index:22    from 2 To 23
        SetMemory(0x662280, Add, 352321536),# units:Human AI Idle  index:27    from 2 To 23
        SetMemory(0x662284, Add, 21),# units:Human AI Idle  index:28    from 2 To 23
        SetMemory(0x662284, Add, 5376),# units:Human AI Idle  index:29    from 2 To 23
        SetMemory(0x662288, Add, 21),# units:Human AI Idle  index:32    from 2 To 23
        SetMemory(0x662288, Add, -9961472),# units:Human AI Idle  index:34    from 175 To 23
        SetMemory(0x66228C, Add, 5376),# units:Human AI Idle  index:37    from 2 To 23
        SetMemory(0x66228C, Add, 1376256),# units:Human AI Idle  index:38    from 2 To 23
        SetMemory(0x66228C, Add, 352321536),# units:Human AI Idle  index:39    from 2 To 23
        SetMemory(0x662290, Add, 21),# units:Human AI Idle  index:40    from 2 To 23
        SetMemory(0x662290, Add, 5376),# units:Human AI Idle  index:41    from 2 To 23
        SetMemory(0x662290, Add, -4587520),# units:Human AI Idle  index:42    from 93 To 23
        SetMemory(0x662290, Add, 352321536),# units:Human AI Idle  index:43    from 2 To 23
        SetMemory(0x662294, Add, 21),# units:Human AI Idle  index:44    from 2 To 23
        SetMemory(0x662294, Add, 5376),# units:Human AI Idle  index:45    from 2 To 23
        SetMemory(0x662294, Add, 1376256),# units:Human AI Idle  index:46    from 2 To 23
        SetMemory(0x662294, Add, 352321536),# units:Human AI Idle  index:47    from 2 To 23
        SetMemory(0x662298, Add, 21),# units:Human AI Idle  index:48    from 2 To 23
        SetMemory(0x662298, Add, 5376),# units:Human AI Idle  index:49    from 2 To 23
        SetMemory(0x662298, Add, 1376256),# units:Human AI Idle  index:50    from 2 To 23
        SetMemory(0x662298, Add, 352321536),# units:Human AI Idle  index:51    from 2 To 23
        SetMemory(0x66229C, Add, 21),# units:Human AI Idle  index:52    from 2 To 23
        SetMemory(0x66229C, Add, 5376),# units:Human AI Idle  index:53    from 2 To 23
        SetMemory(0x66229C, Add, 1376256),# units:Human AI Idle  index:54    from 2 To 23
        SetMemory(0x66229C, Add, 352321536),# units:Human AI Idle  index:55    from 2 To 23
        SetMemory(0x6622A0, Add, 21),# units:Human AI Idle  index:56    from 2 To 23
        SetMemory(0x6622A0, Add, -17920),# units:Human AI Idle  index:57    from 93 To 23
        SetMemory(0x6622A4, Add, 21),# units:Human AI Idle  index:60    from 2 To 23
        SetMemory(0x6622A4, Add, 5376),# units:Human AI Idle  index:61    from 2 To 23
        SetMemory(0x6622A4, Add, 1376256),# units:Human AI Idle  index:62    from 2 To 23
        SetMemory(0x6622A4, Add, 352321536),# units:Human AI Idle  index:63    from 2 To 23
        SetMemory(0x6622A8, Add, 21),# units:Human AI Idle  index:64    from 2 To 23
        SetMemory(0x6622A8, Add, 5376),# units:Human AI Idle  index:65    from 2 To 23
        SetMemory(0x6622A8, Add, 1376256),# units:Human AI Idle  index:66    from 2 To 23
        SetMemory(0x6622A8, Add, 352321536),# units:Human AI Idle  index:67    from 2 To 23
        SetMemory(0x6622AC, Add, 21),# units:Human AI Idle  index:68    from 2 To 23
        SetMemory(0x6622AC, Add, -17920),# units:Human AI Idle  index:69    from 93 To 23
        SetMemory(0x6622AC, Add, 1376256),# units:Human AI Idle  index:70    from 2 To 23
        SetMemory(0x6622AC, Add, -1795162112),# units:Human AI Idle  index:71    from 130 To 23
        SetMemory(0x6622B0, Add, -27),# units:Human AI Idle  index:72    from 50 To 23
        SetMemory(0x6622B0, Add, 1376256),# units:Human AI Idle  index:74    from 2 To 23
        SetMemory(0x6622B0, Add, 352321536),# units:Human AI Idle  index:75    from 2 To 23
        SetMemory(0x6622B4, Add, 21),# units:Human AI Idle  index:76    from 2 To 23
        SetMemory(0x6622B4, Add, 5376),# units:Human AI Idle  index:77    from 2 To 23
        SetMemory(0x6622B4, Add, 1376256),# units:Human AI Idle  index:78    from 2 To 23
        SetMemory(0x6622B4, Add, 352321536),# units:Human AI Idle  index:79    from 2 To 23
        SetMemory(0x6622B8, Add, 21),# units:Human AI Idle  index:80    from 2 To 23
        SetMemory(0x6622B8, Add, -8960),# units:Human AI Idle  index:81    from 58 To 23
        SetMemory(0x6622B8, Add, -1769472),# units:Human AI Idle  index:82    from 50 To 23
        SetMemory(0x6622B8, Add, -587202560),# units:Human AI Idle  index:83    from 58 To 23
        SetMemory(0x6622BC, Add, 21),# units:Human AI Idle  index:84    from 2 To 23
        SetMemory(0x6622BC, Add, -7012352),# units:Human AI Idle  index:86    from 130 To 23
        SetMemory(0x6622BC, Add, 352321536),# units:Human AI Idle  index:87    from 2 To 23
        SetMemory(0x6622C0, Add, 21),# units:Human AI Idle  index:88    from 2 To 23
        SetMemory(0x6622C0, Add, -36608),# units:Human AI Idle  index:89    from 166 To 23
        SetMemory(0x6622C0, Add, -9371648),# units:Human AI Idle  index:90    from 166 To 23
        SetMemory(0x6622C4, Add, -36608),# units:Human AI Idle  index:93    from 166 To 23
        SetMemory(0x6622C4, Add, -9371648),# units:Human AI Idle  index:94    from 166 To 23
        SetMemory(0x6622C4, Add, -2399141888),# units:Human AI Idle  index:95    from 166 To 23
        SetMemory(0x6622C8, Add, -143),# units:Human AI Idle  index:96    from 166 To 23
        SetMemory(0x6622C8, Add, 1376256),# units:Human AI Idle  index:98    from 2 To 23
        SetMemory(0x6622C8, Add, 352321536),# units:Human AI Idle  index:99    from 2 To 23
        SetMemory(0x6622CC, Add, 21),# units:Human AI Idle  index:100    from 2 To 23
        SetMemory(0x6622CC, Add, 1376256),# units:Human AI Idle  index:102    from 2 To 23
        SetMemory(0x6622CC, Add, 352321536),# units:Human AI Idle  index:103    from 2 To 23
        SetMemory(0x6622D0, Add, 21),# units:Human AI Idle  index:104    from 2 To 23
        SetMemory(0x6622E4, Add, 5),# units:Human AI Idle  index:124    from 18 To 23
        SetMemory(0x6622E8, Add, -74),# units:Human AI Idle  index:128    from 97 To 23
        SetMemory(0x6622E8, Add, -18944),# units:Human AI Idle  index:129    from 97 To 23
        SetMemory(0x6622E8, Add, -1308622848),# units:Human AI Idle  index:131    from 101 To 23
        SetMemory(0x6622EC, Add, -78),# units:Human AI Idle  index:132    from 101 To 23
        SetMemory(0x6622EC, Add, -19968),# units:Human AI Idle  index:133    from 101 To 23
        SetMemory(0x6622F4, Add, -1308622848),# units:Human AI Idle  index:143    from 101 To 23
        SetMemory(0x6622F8, Add, -78),# units:Human AI Idle  index:144    from 101 To 23
        SetMemory(0x6622F8, Add, -5111808),# units:Human AI Idle  index:146    from 101 To 23
        SetMemory(0x662304, Add, -141),# units:Human AI Idle  index:156    from 164 To 23
        SetMemory(0x662308, Add, 327680),# units:Human AI Idle  index:162    from 18 To 23
        SetMemory(0x66233C, Add, -1241513984),# units:Human AI Idle  index:215    from 97 To 23
        SetMemory(0x662340, Add, -74),# units:Human AI Idle  index:216    from 97 To 23
        SetMemory(0x662340, Add, -18944),# units:Human AI Idle  index:217    from 97 To 23
        SetMemory(0x662340, Add, -4849664),# units:Human AI Idle  index:218    from 97 To 23
        SetMemory(0x662340, Add, -1241513984),# units:Human AI Idle  index:219    from 97 To 23
        SetMemory(0x662344, Add, -74),# units:Human AI Idle  index:220    from 97 To 23
        SetMemory(0x662344, Add, -18944),# units:Human AI Idle  index:221    from 97 To 23
        SetMemory(0x662344, Add, -4849664),# units:Human AI Idle  index:222    from 97 To 23
        SetMemory(0x662344, Add, -1241513984),# units:Human AI Idle  index:223    from 97 To 23
        SetMemory(0x664898, Add, 5376),# units:Return to Idle  index:1    from 2 To 23
        SetMemory(0x664898, Add, 1376256),# units:Return to Idle  index:2    from 2 To 23
        SetMemory(0x66489C, Add, 352321536),# units:Return to Idle  index:7    from 2 To 23
        SetMemory(0x6648A0, Add, 21),# units:Return to Idle  index:8    from 2 To 23
        SetMemory(0x6648A0, Add, 5376),# units:Return to Idle  index:9    from 2 To 23
        SetMemory(0x6648A0, Add, 1376256),# units:Return to Idle  index:10    from 2 To 23
        SetMemory(0x6648A0, Add, -1174405120),# units:Return to Idle  index:11    from 93 To 23
        SetMemory(0x6648A4, Add, 21),# units:Return to Idle  index:12    from 2 To 23
        SetMemory(0x6648A8, Add, 21),# units:Return to Idle  index:16    from 2 To 23
        SetMemory(0x6648A8, Add, 352321536),# units:Return to Idle  index:19    from 2 To 23
        SetMemory(0x6648AC, Add, 21),# units:Return to Idle  index:20    from 2 To 23
        SetMemory(0x6648AC, Add, 5376),# units:Return to Idle  index:21    from 2 To 23
        SetMemory(0x6648AC, Add, 1376256),# units:Return to Idle  index:22    from 2 To 23
        SetMemory(0x6648B0, Add, 352321536),# units:Return to Idle  index:27    from 2 To 23
        SetMemory(0x6648B4, Add, 21),# units:Return to Idle  index:28    from 2 To 23
        SetMemory(0x6648B4, Add, 5376),# units:Return to Idle  index:29    from 2 To 23
        SetMemory(0x6648B8, Add, 21),# units:Return to Idle  index:32    from 2 To 23
        SetMemory(0x6648B8, Add, -9961472),# units:Return to Idle  index:34    from 175 To 23
        SetMemory(0x6648BC, Add, 5376),# units:Return to Idle  index:37    from 2 To 23
        SetMemory(0x6648BC, Add, 1376256),# units:Return to Idle  index:38    from 2 To 23
        SetMemory(0x6648BC, Add, 352321536),# units:Return to Idle  index:39    from 2 To 23
        SetMemory(0x6648C0, Add, 21),# units:Return to Idle  index:40    from 2 To 23
        SetMemory(0x6648C0, Add, 5376),# units:Return to Idle  index:41    from 2 To 23
        SetMemory(0x6648C0, Add, -4587520),# units:Return to Idle  index:42    from 93 To 23
        SetMemory(0x6648C0, Add, 352321536),# units:Return to Idle  index:43    from 2 To 23
        SetMemory(0x6648C4, Add, 21),# units:Return to Idle  index:44    from 2 To 23
        SetMemory(0x6648C4, Add, 5376),# units:Return to Idle  index:45    from 2 To 23
        SetMemory(0x6648C4, Add, 1376256),# units:Return to Idle  index:46    from 2 To 23
        SetMemory(0x6648C4, Add, 352321536),# units:Return to Idle  index:47    from 2 To 23
        SetMemory(0x6648C8, Add, 21),# units:Return to Idle  index:48    from 2 To 23
        SetMemory(0x6648C8, Add, 5376),# units:Return to Idle  index:49    from 2 To 23
        SetMemory(0x6648C8, Add, 1376256),# units:Return to Idle  index:50    from 2 To 23
        SetMemory(0x6648C8, Add, 352321536),# units:Return to Idle  index:51    from 2 To 23
        SetMemory(0x6648CC, Add, 21),# units:Return to Idle  index:52    from 2 To 23
        SetMemory(0x6648CC, Add, 5376),# units:Return to Idle  index:53    from 2 To 23
        SetMemory(0x6648CC, Add, 1376256),# units:Return to Idle  index:54    from 2 To 23
        SetMemory(0x6648CC, Add, 352321536),# units:Return to Idle  index:55    from 2 To 23
        SetMemory(0x6648D0, Add, 21),# units:Return to Idle  index:56    from 2 To 23
        SetMemory(0x6648D0, Add, -17920),# units:Return to Idle  index:57    from 93 To 23
        SetMemory(0x6648D4, Add, 21),# units:Return to Idle  index:60    from 2 To 23
        SetMemory(0x6648D4, Add, 5376),# units:Return to Idle  index:61    from 2 To 23
        SetMemory(0x6648D4, Add, 1376256),# units:Return to Idle  index:62    from 2 To 23
        SetMemory(0x6648D4, Add, 352321536),# units:Return to Idle  index:63    from 2 To 23
        SetMemory(0x6648D8, Add, 21),# units:Return to Idle  index:64    from 2 To 23
        SetMemory(0x6648D8, Add, 5376),# units:Return to Idle  index:65    from 2 To 23
        SetMemory(0x6648D8, Add, 1376256),# units:Return to Idle  index:66    from 2 To 23
        SetMemory(0x6648D8, Add, 352321536),# units:Return to Idle  index:67    from 2 To 23
        SetMemory(0x6648DC, Add, 21),# units:Return to Idle  index:68    from 2 To 23
        SetMemory(0x6648DC, Add, -17920),# units:Return to Idle  index:69    from 93 To 23
        SetMemory(0x6648DC, Add, 1376256),# units:Return to Idle  index:70    from 2 To 23
        SetMemory(0x6648DC, Add, 352321536),# units:Return to Idle  index:71    from 2 To 23
        SetMemory(0x6648E0, Add, -27),# units:Return to Idle  index:72    from 50 To 23
        SetMemory(0x6648E0, Add, 1376256),# units:Return to Idle  index:74    from 2 To 23
        SetMemory(0x6648E0, Add, 352321536),# units:Return to Idle  index:75    from 2 To 23
        SetMemory(0x6648E4, Add, 21),# units:Return to Idle  index:76    from 2 To 23
        SetMemory(0x6648E4, Add, 5376),# units:Return to Idle  index:77    from 2 To 23
        SetMemory(0x6648E4, Add, 1376256),# units:Return to Idle  index:78    from 2 To 23
        SetMemory(0x6648E4, Add, 352321536),# units:Return to Idle  index:79    from 2 To 23
        SetMemory(0x6648E8, Add, 21),# units:Return to Idle  index:80    from 2 To 23
        SetMemory(0x6648E8, Add, -8960),# units:Return to Idle  index:81    from 58 To 23
        SetMemory(0x6648E8, Add, -1769472),# units:Return to Idle  index:82    from 50 To 23
        SetMemory(0x6648E8, Add, -587202560),# units:Return to Idle  index:83    from 58 To 23
        SetMemory(0x6648EC, Add, 21),# units:Return to Idle  index:84    from 2 To 23
        SetMemory(0x6648EC, Add, 1376256),# units:Return to Idle  index:86    from 2 To 23
        SetMemory(0x6648EC, Add, 352321536),# units:Return to Idle  index:87    from 2 To 23
        SetMemory(0x6648F0, Add, 21),# units:Return to Idle  index:88    from 2 To 23
        SetMemory(0x6648F0, Add, -36608),# units:Return to Idle  index:89    from 166 To 23
        SetMemory(0x6648F0, Add, -9371648),# units:Return to Idle  index:90    from 166 To 23
        SetMemory(0x6648F4, Add, -36608),# units:Return to Idle  index:93    from 166 To 23
        SetMemory(0x6648F4, Add, -9371648),# units:Return to Idle  index:94    from 166 To 23
        SetMemory(0x6648F4, Add, -2399141888),# units:Return to Idle  index:95    from 166 To 23
        SetMemory(0x6648F8, Add, -143),# units:Return to Idle  index:96    from 166 To 23
        SetMemory(0x6648F8, Add, 1376256),# units:Return to Idle  index:98    from 2 To 23
        SetMemory(0x6648F8, Add, 352321536),# units:Return to Idle  index:99    from 2 To 23
        SetMemory(0x6648FC, Add, 21),# units:Return to Idle  index:100    from 2 To 23
        SetMemory(0x6648FC, Add, 1376256),# units:Return to Idle  index:102    from 2 To 23
        SetMemory(0x6648FC, Add, 352321536),# units:Return to Idle  index:103    from 2 To 23
        SetMemory(0x664900, Add, 21),# units:Return to Idle  index:104    from 2 To 23
        SetMemory(0x664914, Add, 5),# units:Return to Idle  index:124    from 18 To 23
        SetMemory(0x664918, Add, -74),# units:Return to Idle  index:128    from 97 To 23
        SetMemory(0x664918, Add, -18944),# units:Return to Idle  index:129    from 97 To 23
        SetMemory(0x664928, Add, 5),# units:Return to Idle  index:144    from 18 To 23
        SetMemory(0x664928, Add, 327680),# units:Return to Idle  index:146    from 18 To 23
        SetMemory(0x664938, Add, 327680),# units:Return to Idle  index:162    from 18 To 23
        SetMemory(0x66496C, Add, -1241513984),# units:Return to Idle  index:215    from 97 To 23
        SetMemory(0x664970, Add, -74),# units:Return to Idle  index:216    from 97 To 23
        SetMemory(0x664970, Add, -18944),# units:Return to Idle  index:217    from 97 To 23
        SetMemory(0x664970, Add, -4849664),# units:Return to Idle  index:218    from 97 To 23
        SetMemory(0x664970, Add, -1241513984),# units:Return to Idle  index:219    from 97 To 23
        SetMemory(0x664974, Add, -74),# units:Return to Idle  index:220    from 97 To 23
        SetMemory(0x664974, Add, -18944),# units:Return to Idle  index:221    from 97 To 23
        SetMemory(0x664974, Add, -4849664),# units:Return to Idle  index:222    from 97 To 23
        SetMemory(0x664974, Add, -1241513984),# units:Return to Idle  index:223    from 97 To 23
        SetMemory(0x663320, Add, 3328),# units:Attack Unit  index:1    from 10 To 23
        SetMemory(0x663320, Add, 851968),# units:Attack Unit  index:2    from 10 To 23
        SetMemory(0x663324, Add, 218103808),# units:Attack Unit  index:7    from 10 To 23
        SetMemory(0x663328, Add, 13),# units:Attack Unit  index:8    from 10 To 23
        SetMemory(0x663328, Add, 3328),# units:Attack Unit  index:9    from 10 To 23
        SetMemory(0x663328, Add, 851968),# units:Attack Unit  index:10    from 10 To 23
        SetMemory(0x663328, Add, 33554432),# units:Attack Unit  index:11    from 21 To 23
        SetMemory(0x66332C, Add, 13),# units:Attack Unit  index:12    from 10 To 23
        SetMemory(0x663330, Add, 13),# units:Attack Unit  index:16    from 10 To 23
        SetMemory(0x663330, Add, 218103808),# units:Attack Unit  index:19    from 10 To 23
        SetMemory(0x663334, Add, 13),# units:Attack Unit  index:20    from 10 To 23
        SetMemory(0x663334, Add, 3328),# units:Attack Unit  index:21    from 10 To 23
        SetMemory(0x663334, Add, 851968),# units:Attack Unit  index:22    from 10 To 23
        SetMemory(0x663338, Add, 218103808),# units:Attack Unit  index:27    from 10 To 23
        SetMemory(0x66333C, Add, 13),# units:Attack Unit  index:28    from 10 To 23
        SetMemory(0x66333C, Add, 3328),# units:Attack Unit  index:29    from 10 To 23
        SetMemory(0x663340, Add, 13),# units:Attack Unit  index:32    from 10 To 23
        SetMemory(0x663340, Add, -9961472),# units:Attack Unit  index:34    from 175 To 23
        SetMemory(0x663344, Add, 3328),# units:Attack Unit  index:37    from 10 To 23
        SetMemory(0x663344, Add, 851968),# units:Attack Unit  index:38    from 10 To 23
        SetMemory(0x663344, Add, 218103808),# units:Attack Unit  index:39    from 10 To 23
        SetMemory(0x663348, Add, 13),# units:Attack Unit  index:40    from 10 To 23
        SetMemory(0x663348, Add, 3328),# units:Attack Unit  index:41    from 10 To 23
        SetMemory(0x663348, Add, 131072),# units:Attack Unit  index:42    from 21 To 23
        SetMemory(0x663348, Add, 218103808),# units:Attack Unit  index:43    from 10 To 23
        SetMemory(0x66334C, Add, 13),# units:Attack Unit  index:44    from 10 To 23
        SetMemory(0x66334C, Add, -1024),# units:Attack Unit  index:45    from 27 To 23
        SetMemory(0x66334C, Add, 851968),# units:Attack Unit  index:46    from 10 To 23
        SetMemory(0x66334C, Add, 218103808),# units:Attack Unit  index:47    from 10 To 23
        SetMemory(0x663350, Add, 13),# units:Attack Unit  index:48    from 10 To 23
        SetMemory(0x663350, Add, -1024),# units:Attack Unit  index:49    from 27 To 23
        SetMemory(0x663350, Add, -7274496),# units:Attack Unit  index:50    from 134 To 23
        SetMemory(0x663350, Add, 218103808),# units:Attack Unit  index:51    from 10 To 23
        SetMemory(0x663354, Add, 13),# units:Attack Unit  index:52    from 10 To 23
        SetMemory(0x663354, Add, 3328),# units:Attack Unit  index:53    from 10 To 23
        SetMemory(0x663354, Add, 851968),# units:Attack Unit  index:54    from 10 To 23
        SetMemory(0x663354, Add, 218103808),# units:Attack Unit  index:55    from 10 To 23
        SetMemory(0x663358, Add, 13),# units:Attack Unit  index:56    from 10 To 23
        SetMemory(0x663358, Add, 512),# units:Attack Unit  index:57    from 21 To 23
        SetMemory(0x66335C, Add, 13),# units:Attack Unit  index:60    from 10 To 23
        SetMemory(0x66335C, Add, 3328),# units:Attack Unit  index:61    from 10 To 23
        SetMemory(0x66335C, Add, 851968),# units:Attack Unit  index:62    from 10 To 23
        SetMemory(0x66335C, Add, 33554432),# units:Attack Unit  index:63    from 21 To 23
        SetMemory(0x663360, Add, 13),# units:Attack Unit  index:64    from 10 To 23
        SetMemory(0x663360, Add, 3328),# units:Attack Unit  index:65    from 10 To 23
        SetMemory(0x663360, Add, 851968),# units:Attack Unit  index:66    from 10 To 23
        SetMemory(0x663360, Add, 218103808),# units:Attack Unit  index:67    from 10 To 23
        SetMemory(0x663364, Add, 13),# units:Attack Unit  index:68    from 10 To 23
        SetMemory(0x663364, Add, 512),# units:Attack Unit  index:69    from 21 To 23
        SetMemory(0x663364, Add, 851968),# units:Attack Unit  index:70    from 10 To 23
        SetMemory(0x663364, Add, 218103808),# units:Attack Unit  index:71    from 10 To 23
        SetMemory(0x663368, Add, -30),# units:Attack Unit  index:72    from 53 To 23
        SetMemory(0x663368, Add, 851968),# units:Attack Unit  index:74    from 10 To 23
        SetMemory(0x663368, Add, 218103808),# units:Attack Unit  index:75    from 10 To 23
        SetMemory(0x66336C, Add, 13),# units:Attack Unit  index:76    from 10 To 23
        SetMemory(0x66336C, Add, 3328),# units:Attack Unit  index:77    from 10 To 23
        SetMemory(0x66336C, Add, 851968),# units:Attack Unit  index:78    from 10 To 23
        SetMemory(0x66336C, Add, 218103808),# units:Attack Unit  index:79    from 10 To 23
        SetMemory(0x663370, Add, 13),# units:Attack Unit  index:80    from 10 To 23
        SetMemory(0x663370, Add, -9216),# units:Attack Unit  index:81    from 59 To 23
        SetMemory(0x663370, Add, -1966080),# units:Attack Unit  index:82    from 53 To 23
        SetMemory(0x663370, Add, -603979776),# units:Attack Unit  index:83    from 59 To 23
        SetMemory(0x663374, Add, 13),# units:Attack Unit  index:84    from 10 To 23
        SetMemory(0x663374, Add, 851968),# units:Attack Unit  index:86    from 10 To 23
        SetMemory(0x663374, Add, 218103808),# units:Attack Unit  index:87    from 10 To 23
        SetMemory(0x663378, Add, 13),# units:Attack Unit  index:88    from 10 To 23
        SetMemory(0x663378, Add, -42240),# units:Attack Unit  index:89    from 188 To 23
        SetMemory(0x663378, Add, -10813440),# units:Attack Unit  index:90    from 188 To 23
        SetMemory(0x66337C, Add, -42240),# units:Attack Unit  index:93    from 188 To 23
        SetMemory(0x66337C, Add, -10813440),# units:Attack Unit  index:94    from 188 To 23
        SetMemory(0x66337C, Add, -2768240640),# units:Attack Unit  index:95    from 188 To 23
        SetMemory(0x663380, Add, -165),# units:Attack Unit  index:96    from 188 To 23
        SetMemory(0x663380, Add, 851968),# units:Attack Unit  index:98    from 10 To 23
        SetMemory(0x663380, Add, 218103808),# units:Attack Unit  index:99    from 10 To 23
        SetMemory(0x663384, Add, 13),# units:Attack Unit  index:100    from 10 To 23
        SetMemory(0x663384, Add, 851968),# units:Attack Unit  index:102    from 10 To 23
        SetMemory(0x663384, Add, 201326592),# units:Attack Unit  index:103    from 11 To 23
        SetMemory(0x663388, Add, 13),# units:Attack Unit  index:104    from 10 To 23
        SetMemory(0x66339C, Add, 4),# units:Attack Unit  index:124    from 19 To 23
        SetMemory(0x6633B0, Add, 4),# units:Attack Unit  index:144    from 19 To 23
        SetMemory(0x6633B0, Add, 262144),# units:Attack Unit  index:146    from 19 To 23
        SetMemory(0x6633C0, Add, 262144),# units:Attack Unit  index:162    from 19 To 23
        SetMemory(0x663A50, Add, 5376),# units:Attack Move  index:1    from 2 To 23
        SetMemory(0x663A50, Add, 1376256),# units:Attack Move  index:2    from 2 To 23
        SetMemory(0x663A54, Add, 352321536),# units:Attack Move  index:7    from 2 To 23
        SetMemory(0x663A58, Add, 21),# units:Attack Move  index:8    from 2 To 23
        SetMemory(0x663A58, Add, 5376),# units:Attack Move  index:9    from 2 To 23
        SetMemory(0x663A58, Add, 1376256),# units:Attack Move  index:10    from 2 To 23
        SetMemory(0x663A58, Add, 352321536),# units:Attack Move  index:11    from 2 To 23
        SetMemory(0x663A5C, Add, 21),# units:Attack Move  index:12    from 2 To 23
        SetMemory(0x663A60, Add, 21),# units:Attack Move  index:16    from 2 To 23
        SetMemory(0x663A60, Add, 352321536),# units:Attack Move  index:19    from 2 To 23
        SetMemory(0x663A64, Add, 21),# units:Attack Move  index:20    from 2 To 23
        SetMemory(0x663A64, Add, 5376),# units:Attack Move  index:21    from 2 To 23
        SetMemory(0x663A64, Add, 1376256),# units:Attack Move  index:22    from 2 To 23
        SetMemory(0x663A68, Add, 352321536),# units:Attack Move  index:27    from 2 To 23
        SetMemory(0x663A6C, Add, 21),# units:Attack Move  index:28    from 2 To 23
        SetMemory(0x663A6C, Add, 5376),# units:Attack Move  index:29    from 2 To 23
        SetMemory(0x663A70, Add, 21),# units:Attack Move  index:32    from 2 To 23
        SetMemory(0x663A70, Add, -9961472),# units:Attack Move  index:34    from 175 To 23
        SetMemory(0x663A74, Add, 5376),# units:Attack Move  index:37    from 2 To 23
        SetMemory(0x663A74, Add, 1376256),# units:Attack Move  index:38    from 2 To 23
        SetMemory(0x663A74, Add, 352321536),# units:Attack Move  index:39    from 2 To 23
        SetMemory(0x663A78, Add, 21),# units:Attack Move  index:40    from 2 To 23
        SetMemory(0x663A78, Add, 5376),# units:Attack Move  index:41    from 2 To 23
        SetMemory(0x663A78, Add, 1376256),# units:Attack Move  index:42    from 2 To 23
        SetMemory(0x663A78, Add, 352321536),# units:Attack Move  index:43    from 2 To 23
        SetMemory(0x663A7C, Add, 21),# units:Attack Move  index:44    from 2 To 23
        SetMemory(0x663A7C, Add, 5376),# units:Attack Move  index:45    from 2 To 23
        SetMemory(0x663A7C, Add, 1376256),# units:Attack Move  index:46    from 2 To 23
        SetMemory(0x663A7C, Add, 352321536),# units:Attack Move  index:47    from 2 To 23
        SetMemory(0x663A80, Add, 21),# units:Attack Move  index:48    from 2 To 23
        SetMemory(0x663A80, Add, 5376),# units:Attack Move  index:49    from 2 To 23
        SetMemory(0x663A80, Add, -7340032),# units:Attack Move  index:50    from 135 To 23
        SetMemory(0x663A80, Add, 352321536),# units:Attack Move  index:51    from 2 To 23
        SetMemory(0x663A84, Add, 21),# units:Attack Move  index:52    from 2 To 23
        SetMemory(0x663A84, Add, 5376),# units:Attack Move  index:53    from 2 To 23
        SetMemory(0x663A84, Add, 1376256),# units:Attack Move  index:54    from 2 To 23
        SetMemory(0x663A84, Add, 352321536),# units:Attack Move  index:55    from 2 To 23
        SetMemory(0x663A88, Add, 21),# units:Attack Move  index:56    from 2 To 23
        SetMemory(0x663A88, Add, 5376),# units:Attack Move  index:57    from 2 To 23
        SetMemory(0x663A8C, Add, 21),# units:Attack Move  index:60    from 2 To 23
        SetMemory(0x663A8C, Add, 5376),# units:Attack Move  index:61    from 2 To 23
        SetMemory(0x663A8C, Add, 1376256),# units:Attack Move  index:62    from 2 To 23
        SetMemory(0x663A8C, Add, 352321536),# units:Attack Move  index:63    from 2 To 23
        SetMemory(0x663A90, Add, 21),# units:Attack Move  index:64    from 2 To 23
        SetMemory(0x663A90, Add, 5376),# units:Attack Move  index:65    from 2 To 23
        SetMemory(0x663A90, Add, 1376256),# units:Attack Move  index:66    from 2 To 23
        SetMemory(0x663A90, Add, 352321536),# units:Attack Move  index:67    from 2 To 23
        SetMemory(0x663A94, Add, 21),# units:Attack Move  index:68    from 2 To 23
        SetMemory(0x663A94, Add, 5376),# units:Attack Move  index:69    from 2 To 23
        SetMemory(0x663A94, Add, 1376256),# units:Attack Move  index:70    from 2 To 23
        SetMemory(0x663A94, Add, 352321536),# units:Attack Move  index:71    from 2 To 23
        SetMemory(0x663A98, Add, -27),# units:Attack Move  index:72    from 50 To 23
        SetMemory(0x663A98, Add, 1376256),# units:Attack Move  index:74    from 2 To 23
        SetMemory(0x663A98, Add, 352321536),# units:Attack Move  index:75    from 2 To 23
        SetMemory(0x663A9C, Add, 21),# units:Attack Move  index:76    from 2 To 23
        SetMemory(0x663A9C, Add, 5376),# units:Attack Move  index:77    from 2 To 23
        SetMemory(0x663A9C, Add, 1376256),# units:Attack Move  index:78    from 2 To 23
        SetMemory(0x663A9C, Add, 352321536),# units:Attack Move  index:79    from 2 To 23
        SetMemory(0x663AA0, Add, 21),# units:Attack Move  index:80    from 2 To 23
        SetMemory(0x663AA0, Add, -8960),# units:Attack Move  index:81    from 58 To 23
        SetMemory(0x663AA0, Add, -1769472),# units:Attack Move  index:82    from 50 To 23
        SetMemory(0x663AA0, Add, -587202560),# units:Attack Move  index:83    from 58 To 23
        SetMemory(0x663AA4, Add, 21),# units:Attack Move  index:84    from 2 To 23
        SetMemory(0x663AA4, Add, 1376256),# units:Attack Move  index:86    from 2 To 23
        SetMemory(0x663AA4, Add, 352321536),# units:Attack Move  index:87    from 2 To 23
        SetMemory(0x663AA8, Add, 21),# units:Attack Move  index:88    from 2 To 23
        SetMemory(0x663AA8, Add, -42240),# units:Attack Move  index:89    from 188 To 23
        SetMemory(0x663AA8, Add, -10813440),# units:Attack Move  index:90    from 188 To 23
        SetMemory(0x663AAC, Add, -42240),# units:Attack Move  index:93    from 188 To 23
        SetMemory(0x663AAC, Add, -10813440),# units:Attack Move  index:94    from 188 To 23
        SetMemory(0x663AAC, Add, -2768240640),# units:Attack Move  index:95    from 188 To 23
        SetMemory(0x663AB0, Add, -165),# units:Attack Move  index:96    from 188 To 23
        SetMemory(0x663AB0, Add, 1376256),# units:Attack Move  index:98    from 2 To 23
        SetMemory(0x663AB0, Add, 352321536),# units:Attack Move  index:99    from 2 To 23
        SetMemory(0x663AB4, Add, 21),# units:Attack Move  index:100    from 2 To 23
        SetMemory(0x663AB4, Add, 1376256),# units:Attack Move  index:102    from 2 To 23
        SetMemory(0x663AB4, Add, 352321536),# units:Attack Move  index:103    from 2 To 23
        SetMemory(0x663AB8, Add, 21),# units:Attack Move  index:104    from 2 To 23
        SetMemory(0x6636B8, Add, 32768),# units:Ground Weapon  index:1    from 2 To 130
        SetMemory(0x6636B8, Add, 8257536),# units:Ground Weapon  index:2    from 4 To 130
        SetMemory(0x6636BC, Add, 1962934272),# units:Ground Weapon  index:7    from 13 To 130
        SetMemory(0x6636C0, Add, 114),# units:Ground Weapon  index:8    from 16 To 130
        SetMemory(0x6636C0, Add, 6815744),# units:Ground Weapon  index:10    from 26 To 130
        SetMemory(0x6636C4, Add, 111),# units:Ground Weapon  index:12    from 19 To 130
        SetMemory(0x6636C8, Add, 127),# units:Ground Weapon  index:16    from 3 To 130
        SetMemory(0x6636C8, Add, 2097152000),# units:Ground Weapon  index:19    from 5 To 130
        SetMemory(0x6636CC, Add, 129),# units:Ground Weapon  index:20    from 1 To 130
        SetMemory(0x6636CC, Add, 28672),# units:Ground Weapon  index:21    from 18 To 130
        SetMemory(0x6636D0, Add, 1828716544),# units:Ground Weapon  index:27    from 21 To 130
        SetMemory(0x6636D4, Add, 107),# units:Ground Weapon  index:28    from 23 To 130
        SetMemory(0x6636D4, Add, 27904),# units:Ground Weapon  index:29    from 21 To 130
        SetMemory(0x6636D8, Add, 105),# units:Ground Weapon  index:32    from 25 To 130
        SetMemory(0x6636DC, Add, 24320),# units:Ground Weapon  index:37    from 35 To 130
        SetMemory(0x6636DC, Add, 6029312),# units:Ground Weapon  index:38    from 38 To 130
        SetMemory(0x6636DC, Add, 1509949440),# units:Ground Weapon  index:39    from 40 To 130
        SetMemory(0x6636E0, Add, 88),# units:Ground Weapon  index:40    from 42 To 130
        SetMemory(0x6636E0, Add, 22272),# units:Ground Weapon  index:41    from 43 To 130
        SetMemory(0x6636E0, Add, 1375731712),# units:Ground Weapon  index:43    from 48 To 130
        SetMemory(0x6636E4, Add, 84),# units:Ground Weapon  index:44    from 46 To 130
        SetMemory(0x6636E8, Add, 89),# units:Ground Weapon  index:48    from 41 To 130
        SetMemory(0x6636E8, Add, 4980736),# units:Ground Weapon  index:50    from 54 To 130
        SetMemory(0x6636E8, Add, 1560281088),# units:Ground Weapon  index:51    from 37 To 130
        SetMemory(0x6636EC, Add, 23296),# units:Ground Weapon  index:53    from 39 To 130
        SetMemory(0x6636EC, Add, 6160384),# units:Ground Weapon  index:54    from 36 To 130
        SetMemory(0x6636EC, Add, 1358954496),# units:Ground Weapon  index:55    from 49 To 130
        SetMemory(0x6636F0, Add, 83),# units:Ground Weapon  index:56    from 47 To 130
        SetMemory(0x6636F4, Add, 4864),# units:Ground Weapon  index:61    from 111 To 130
        SetMemory(0x6636F8, Add, 68),# units:Ground Weapon  index:64    from 62 To 130
        SetMemory(0x6636F8, Add, 16896),# units:Ground Weapon  index:65    from 64 To 130
        SetMemory(0x6636F8, Add, 4194304),# units:Ground Weapon  index:66    from 66 To 130
        SetMemory(0x6636FC, Add, 60),# units:Ground Weapon  index:68    from 70 To 130
        SetMemory(0x6636FC, Add, 3735552),# units:Ground Weapon  index:70    from 73 To 130
        SetMemory(0x6636FC, Add, 889192448),# units:Ground Weapon  index:71    from 77 To 130
        SetMemory(0x663700, Add, 2883584),# units:Ground Weapon  index:74    from 86 To 130
        SetMemory(0x663700, Add, 754974720),# units:Ground Weapon  index:75    from 85 To 130
        SetMemory(0x663704, Add, 59),# units:Ground Weapon  index:76    from 71 To 130
        SetMemory(0x663704, Add, 16640),# units:Ground Weapon  index:77    from 65 To 130
        SetMemory(0x663704, Add, 4128768),# units:Ground Weapon  index:78    from 67 To 130
        SetMemory(0x663704, Add, 1023410176),# units:Ground Weapon  index:79    from 69 To 130
        SetMemory(0x663708, Add, 55),# units:Ground Weapon  index:80    from 75 To 130
        SetMemory(0x66370C, Add, 3407872),# units:Ground Weapon  index:86    from 78 To 130
        SetMemory(0x66370C, Add, 1023410176),# units:Ground Weapon  index:87    from 69 To 130
        SetMemory(0x663710, Add, 16),# units:Ground Weapon  index:88    from 114 To 130
        SetMemory(0x663718, Add, 301989888),# units:Ground Weapon  index:99    from 112 To 130
        SetMemory(0x66371C, Add, 14),# units:Ground Weapon  index:100    from 116 To 130
        SetMemory(0x66371C, Add, 7143424),# units:Ground Weapon  index:102    from 21 To 130
        SetMemory(0x66371C, Add, 352321536),# units:Ground Weapon  index:103    from 109 To 130
        SetMemory(0x663720, Add, 17),# units:Ground Weapon  index:104    from 113 To 130
        SetMemory(0x663748, Add, 5046272),# units:Ground Weapon  index:146    from 53 To 130
        SetMemory(0x663758, Add, 3276800),# units:Ground Weapon  index:162    from 80 To 130
        SetMemory(0x6645E0, Add, -256),# units:Max Ground Hits  index:1    from 1 To 0
        SetMemory(0x6645E0, Add, -65536),# units:Max Ground Hits  index:2    from 1 To 0
        SetMemory(0x6645E4, Add, -16777216),# units:Max Ground Hits  index:7    from 1 To 0
        SetMemory(0x6645E8, Add, -1),# units:Max Ground Hits  index:8    from 1 To 0
        SetMemory(0x6645E8, Add, -196608),# units:Max Ground Hits  index:10    from 3 To 0
        SetMemory(0x6645EC, Add, -1),# units:Max Ground Hits  index:12    from 1 To 0
        SetMemory(0x6645F0, Add, -1),# units:Max Ground Hits  index:16    from 1 To 0
        SetMemory(0x6645F0, Add, -16777216),# units:Max Ground Hits  index:19    from 1 To 0
        SetMemory(0x6645F4, Add, -1),# units:Max Ground Hits  index:20    from 1 To 0
        SetMemory(0x6645F4, Add, -256),# units:Max Ground Hits  index:21    from 1 To 0
        SetMemory(0x6645F8, Add, -16777216),# units:Max Ground Hits  index:27    from 1 To 0
        SetMemory(0x6645FC, Add, -1),# units:Max Ground Hits  index:28    from 1 To 0
        SetMemory(0x6645FC, Add, -256),# units:Max Ground Hits  index:29    from 1 To 0
        SetMemory(0x664600, Add, -3),# units:Max Ground Hits  index:32    from 3 To 0
        SetMemory(0x664604, Add, -256),# units:Max Ground Hits  index:37    from 1 To 0
        SetMemory(0x664604, Add, -65536),# units:Max Ground Hits  index:38    from 1 To 0
        SetMemory(0x664604, Add, -16777216),# units:Max Ground Hits  index:39    from 1 To 0
        SetMemory(0x664608, Add, -1),# units:Max Ground Hits  index:40    from 1 To 0
        SetMemory(0x664608, Add, -256),# units:Max Ground Hits  index:41    from 1 To 0
        SetMemory(0x664608, Add, -16777216),# units:Max Ground Hits  index:43    from 1 To 0
        SetMemory(0x66460C, Add, -1),# units:Max Ground Hits  index:44    from 1 To 0
        SetMemory(0x664610, Add, -1),# units:Max Ground Hits  index:48    from 1 To 0
        SetMemory(0x664610, Add, -65536),# units:Max Ground Hits  index:50    from 1 To 0
        SetMemory(0x664610, Add, -16777216),# units:Max Ground Hits  index:51    from 1 To 0
        SetMemory(0x664614, Add, -256),# units:Max Ground Hits  index:53    from 1 To 0
        SetMemory(0x664614, Add, -65536),# units:Max Ground Hits  index:54    from 1 To 0
        SetMemory(0x664614, Add, -16777216),# units:Max Ground Hits  index:55    from 1 To 0
        SetMemory(0x664618, Add, -1),# units:Max Ground Hits  index:56    from 1 To 0
        SetMemory(0x66461C, Add, -256),# units:Max Ground Hits  index:61    from 1 To 0
        SetMemory(0x664620, Add, -1),# units:Max Ground Hits  index:64    from 1 To 0
        SetMemory(0x664620, Add, -512),# units:Max Ground Hits  index:65    from 2 To 0
        SetMemory(0x664620, Add, -65536),# units:Max Ground Hits  index:66    from 1 To 0
        SetMemory(0x664624, Add, -1),# units:Max Ground Hits  index:68    from 1 To 0
        SetMemory(0x664624, Add, -65536),# units:Max Ground Hits  index:70    from 1 To 0
        SetMemory(0x664624, Add, -16777216),# units:Max Ground Hits  index:71    from 1 To 0
        SetMemory(0x664628, Add, -65536),# units:Max Ground Hits  index:74    from 1 To 0
        SetMemory(0x664628, Add, -16777216),# units:Max Ground Hits  index:75    from 1 To 0
        SetMemory(0x66462C, Add, -1),# units:Max Ground Hits  index:76    from 1 To 0
        SetMemory(0x66462C, Add, -512),# units:Max Ground Hits  index:77    from 2 To 0
        SetMemory(0x66462C, Add, -65536),# units:Max Ground Hits  index:78    from 1 To 0
        SetMemory(0x66462C, Add, -16777216),# units:Max Ground Hits  index:79    from 1 To 0
        SetMemory(0x664630, Add, -1),# units:Max Ground Hits  index:80    from 1 To 0
        SetMemory(0x664634, Add, -65536),# units:Max Ground Hits  index:86    from 1 To 0
        SetMemory(0x664634, Add, -16777216),# units:Max Ground Hits  index:87    from 1 To 0
        SetMemory(0x664638, Add, -1),# units:Max Ground Hits  index:88    from 1 To 0
        SetMemory(0x664640, Add, -16777216),# units:Max Ground Hits  index:99    from 1 To 0
        SetMemory(0x664644, Add, -1),# units:Max Ground Hits  index:100    from 1 To 0
        SetMemory(0x664644, Add, -65536),# units:Max Ground Hits  index:102    from 1 To 0
        SetMemory(0x664644, Add, -16777216),# units:Max Ground Hits  index:103    from 1 To 0
        SetMemory(0x664648, Add, -1),# units:Max Ground Hits  index:104    from 1 To 0
        SetMemory(0x664670, Add, -65536),# units:Max Ground Hits  index:146    from 1 To 0
        SetMemory(0x664680, Add, -65536),# units:Max Ground Hits  index:162    from 1 To 0
        SetMemory(0x6616E0, Add, 32768),# units:Air Weapon  index:1    from 2 To 130
        SetMemory(0x6616E8, Add, 115),# units:Air Weapon  index:8    from 15 To 130
        SetMemory(0x6616EC, Add, 110),# units:Air Weapon  index:12    from 20 To 130
        SetMemory(0x6616F0, Add, 127),# units:Air Weapon  index:16    from 3 To 130
        SetMemory(0x6616F4, Add, 129),# units:Air Weapon  index:20    from 1 To 130
        SetMemory(0x6616F4, Add, 28928),# units:Air Weapon  index:21    from 17 To 130
        SetMemory(0x6616F8, Add, 1811939328),# units:Air Weapon  index:27    from 22 To 130
        SetMemory(0x6616FC, Add, 106),# units:Air Weapon  index:28    from 24 To 130
        SetMemory(0x6616FC, Add, 27648),# units:Air Weapon  index:29    from 22 To 130
        SetMemory(0x661704, Add, 6029312),# units:Air Weapon  index:38    from 38 To 130
        SetMemory(0x661708, Add, 1375731712),# units:Air Weapon  index:43    from 48 To 130
        SetMemory(0x66170C, Add, 1258291200),# units:Air Weapon  index:47    from 55 To 130
        SetMemory(0x661714, Add, 23296),# units:Air Weapon  index:53    from 39 To 130
        SetMemory(0x661714, Add, 1358954496),# units:Air Weapon  index:55    from 49 To 130
        SetMemory(0x66171C, Add, 30),# units:Air Weapon  index:60    from 100 To 130
        SetMemory(0x66171C, Add, 1703936),# units:Air Weapon  index:62    from 104 To 130
        SetMemory(0x661720, Add, 4194304),# units:Air Weapon  index:66    from 66 To 130
        SetMemory(0x661724, Add, 60),# units:Air Weapon  index:68    from 70 To 130
        SetMemory(0x661724, Add, 3670016),# units:Air Weapon  index:70    from 74 To 130
        SetMemory(0x661724, Add, 889192448),# units:Air Weapon  index:71    from 77 To 130
        SetMemory(0x66172C, Add, 59),# units:Air Weapon  index:76    from 71 To 130
        SetMemory(0x66172C, Add, 4128768),# units:Air Weapon  index:78    from 67 To 130
        SetMemory(0x661730, Add, 54),# units:Air Weapon  index:80    from 76 To 130
        SetMemory(0x661734, Add, 3407872),# units:Air Weapon  index:86    from 78 To 130
        SetMemory(0x661738, Add, 15),# units:Air Weapon  index:88    from 115 To 130
        SetMemory(0x661740, Add, 1966080),# units:Air Weapon  index:98    from 100 To 130
        SetMemory(0x661740, Add, 301989888),# units:Air Weapon  index:99    from 112 To 130
        SetMemory(0x661744, Add, 14),# units:Air Weapon  index:100    from 116 To 130
        SetMemory(0x661744, Add, 7077888),# units:Air Weapon  index:102    from 22 To 130
        SetMemory(0x661748, Add, 17),# units:Air Weapon  index:104    from 113 To 130
        SetMemory(0x66175C, Add, 101),# units:Air Weapon  index:124    from 29 To 130
        SetMemory(0x661770, Add, 78),# units:Air Weapon  index:144    from 52 To 130
        SetMemory(0x661780, Add, 3211264),# units:Air Weapon  index:162    from 81 To 130
        SetMemory(0x65FC18, Add, -256),# units:Max Air Hits  index:1    from 1 To 0
        SetMemory(0x65FC20, Add, -1),# units:Max Air Hits  index:8    from 1 To 0
        SetMemory(0x65FC24, Add, -1),# units:Max Air Hits  index:12    from 1 To 0
        SetMemory(0x65FC28, Add, -1),# units:Max Air Hits  index:16    from 1 To 0
        SetMemory(0x65FC2C, Add, -1),# units:Max Air Hits  index:20    from 1 To 0
        SetMemory(0x65FC2C, Add, -256),# units:Max Air Hits  index:21    from 1 To 0
        SetMemory(0x65FC30, Add, -16777216),# units:Max Air Hits  index:27    from 1 To 0
        SetMemory(0x65FC34, Add, -1),# units:Max Air Hits  index:28    from 1 To 0
        SetMemory(0x65FC34, Add, -256),# units:Max Air Hits  index:29    from 1 To 0
        SetMemory(0x65FC3C, Add, -65536),# units:Max Air Hits  index:38    from 1 To 0
        SetMemory(0x65FC40, Add, -16777216),# units:Max Air Hits  index:43    from 1 To 0
        SetMemory(0x65FC44, Add, -16777216),# units:Max Air Hits  index:47    from 1 To 0
        SetMemory(0x65FC4C, Add, -256),# units:Max Air Hits  index:53    from 1 To 0
        SetMemory(0x65FC4C, Add, -16777216),# units:Max Air Hits  index:55    from 1 To 0
        SetMemory(0x65FC54, Add, -1),# units:Max Air Hits  index:60    from 1 To 0
        SetMemory(0x65FC54, Add, -65536),# units:Max Air Hits  index:62    from 1 To 0
        SetMemory(0x65FC58, Add, -65536),# units:Max Air Hits  index:66    from 1 To 0
        SetMemory(0x65FC5C, Add, -1),# units:Max Air Hits  index:68    from 1 To 0
        SetMemory(0x65FC5C, Add, -65536),# units:Max Air Hits  index:70    from 1 To 0
        SetMemory(0x65FC5C, Add, -16777216),# units:Max Air Hits  index:71    from 1 To 0
        SetMemory(0x65FC64, Add, -1),# units:Max Air Hits  index:76    from 1 To 0
        SetMemory(0x65FC64, Add, -65536),# units:Max Air Hits  index:78    from 1 To 0
        SetMemory(0x65FC68, Add, -1),# units:Max Air Hits  index:80    from 1 To 0
        SetMemory(0x65FC6C, Add, -65536),# units:Max Air Hits  index:86    from 1 To 0
        SetMemory(0x65FC70, Add, -1),# units:Max Air Hits  index:88    from 1 To 0
        SetMemory(0x65FC78, Add, -65536),# units:Max Air Hits  index:98    from 1 To 0
        SetMemory(0x65FC78, Add, -16777216),# units:Max Air Hits  index:99    from 1 To 0
        SetMemory(0x65FC7C, Add, -1),# units:Max Air Hits  index:100    from 1 To 0
        SetMemory(0x65FC7C, Add, -65536),# units:Max Air Hits  index:102    from 1 To 0
        SetMemory(0x65FC80, Add, -1),# units:Max Air Hits  index:104    from 1 To 0
        SetMemory(0x65FC94, Add, -1),# units:Max Air Hits  index:124    from 1 To 0
        SetMemory(0x65FCA8, Add, -1),# units:Max Air Hits  index:144    from 1 To 0
        SetMemory(0x65FCB8, Add, -65536),# units:Max Air Hits  index:162    from 1 To 0
        SetMemory(0x660178, Add, 768),# units:AI Internal  index:1    from 0 To 3
        SetMemory(0x660178, Add, 196608),# units:AI Internal  index:2    from 0 To 3
        SetMemory(0x660180, Add, 3),# units:AI Internal  index:8    from 0 To 3
        SetMemory(0x660180, Add, 768),# units:AI Internal  index:9    from 0 To 3
        SetMemory(0x660180, Add, 50331648),# units:AI Internal  index:11    from 0 To 3
        SetMemory(0x660184, Add, 3),# units:AI Internal  index:12    from 0 To 3
        SetMemory(0x660198, Add, 3),# units:AI Internal  index:32    from 0 To 3
        SetMemory(0x660198, Add, 196608),# units:AI Internal  index:34    from 0 To 3
        SetMemory(0x66019C, Add, 768),# units:AI Internal  index:37    from 0 To 3
        SetMemory(0x66019C, Add, 196608),# units:AI Internal  index:38    from 0 To 3
        SetMemory(0x66019C, Add, 50331648),# units:AI Internal  index:39    from 0 To 3
        SetMemory(0x6601A0, Add, 3),# units:AI Internal  index:40    from 0 To 3
        SetMemory(0x6601A0, Add, 50331648),# units:AI Internal  index:43    from 0 To 3
        SetMemory(0x6601A4, Add, 3),# units:AI Internal  index:44    from 0 To 3
        SetMemory(0x6601A4, Add, 768),# units:AI Internal  index:45    from 0 To 3
        SetMemory(0x6601A4, Add, 196608),# units:AI Internal  index:46    from 0 To 3
        SetMemory(0x6601A4, Add, 50331648),# units:AI Internal  index:47    from 0 To 3
        SetMemory(0x6601A8, Add, 196608),# units:AI Internal  index:50    from 0 To 3
        SetMemory(0x6601B4, Add, 3),# units:AI Internal  index:60    from 0 To 3
        SetMemory(0x6601B4, Add, 768),# units:AI Internal  index:61    from 0 To 3
        SetMemory(0x6601B4, Add, 196608),# units:AI Internal  index:62    from 0 To 3
        SetMemory(0x6601B4, Add, 50331648),# units:AI Internal  index:63    from 0 To 3
        SetMemory(0x6601B8, Add, 768),# units:AI Internal  index:65    from 0 To 3
        SetMemory(0x6601B8, Add, 196608),# units:AI Internal  index:66    from 0 To 3
        SetMemory(0x6601B8, Add, 50331648),# units:AI Internal  index:67    from 0 To 3
        SetMemory(0x6601BC, Add, 3),# units:AI Internal  index:68    from 0 To 3
        SetMemory(0x6601BC, Add, 768),# units:AI Internal  index:69    from 0 To 3
        SetMemory(0x6601BC, Add, 196608),# units:AI Internal  index:70    from 0 To 3
        SetMemory(0x6601BC, Add, 50331648),# units:AI Internal  index:71    from 0 To 3
        SetMemory(0x6601C0, Add, 3),# units:AI Internal  index:72    from 0 To 3
        SetMemory(0x6601C8, Add, 50331648),# units:AI Internal  index:83    from 0 To 3
        SetMemory(0x6601D8, Add, 196608),# units:AI Internal  index:98    from 0 To 3
        SetMemory(0x6601DC, Add, 50331648),# units:AI Internal  index:103    from 0 To 3
        SetMemory(0x664084, Add, 132054528),# units:Special Ability Flags  index:1    from 404816384 To 536870912
        SetMemory(0x664088, Add, -939524096),# units:Special Ability Flags  index:2    from 1476395008 To 536870912
        SetMemory(0x66409C, Add, -939589640),# units:Special Ability Flags  index:7    from 1476460552 To 536870912
        SetMemory(0x6640A0, Add, -975176196),# units:Special Ability Flags  index:8    from 1512047108 To 536870912
        SetMemory(0x6640A4, Add, -975208708),# units:Special Ability Flags  index:9    from 1512079620 To 536870912
        SetMemory(0x6640A8, Add, 134152128),# units:Special Ability Flags  index:10    from 402718784 To 536870912
        SetMemory(0x6640AC, Add, -973078532),# units:Special Ability Flags  index:11    from 1509949444 To 536870912
        SetMemory(0x6640B0, Add, -1008730116),# units:Special Ability Flags  index:12    from 1545601028 To 536870912
        SetMemory(0x6640C0, Add, 132054464),# units:Special Ability Flags  index:16    from 404816448 To 536870912
        SetMemory(0x6640CC, Add, -939524160),# units:Special Ability Flags  index:19    from 1476395072 To 536870912
        SetMemory(0x6640D0, Add, 134152128),# units:Special Ability Flags  index:20    from 402718784 To 536870912
        SetMemory(0x6640D4, Add, -975176260),# units:Special Ability Flags  index:21    from 1512047172 To 536870912
        SetMemory(0x6640D8, Add, -975208772),# units:Special Ability Flags  index:22    from 1512079684 To 536870912
        SetMemory(0x6640EC, Add, -1008730180),# units:Special Ability Flags  index:27    from 1545601092 To 536870912
        SetMemory(0x6640F0, Add, -1008730180),# units:Special Ability Flags  index:28    from 1545601092 To 536870912
        SetMemory(0x6640F4, Add, -1008730180),# units:Special Ability Flags  index:29    from 1545601092 To 536870912
        SetMemory(0x664100, Add, 134152192),# units:Special Ability Flags  index:32    from 402718720 To 536870912
        SetMemory(0x664108, Add, 132055040),# units:Special Ability Flags  index:34    from 404815872 To 536870912
        SetMemory(0x664114, Add, 133102464),# units:Special Ability Flags  index:37    from 403768448 To 536870912
        SetMemory(0x664118, Add, 133103488),# units:Special Ability Flags  index:38    from 403767424 To 536870912
        SetMemory(0x66411C, Add, 67043200),# units:Special Ability Flags  index:39    from 469827712 To 536870912
        SetMemory(0x664120, Add, 134152064),# units:Special Ability Flags  index:40    from 402718848 To 536870912
        SetMemory(0x664124, Add, 133103480),# units:Special Ability Flags  index:41    from 403767432 To 536870912
        SetMemory(0x664128, Add, 100564860),# units:Special Ability Flags  index:42    from 436306052 To 536870912
        SetMemory(0x66412C, Add, 100597628),# units:Special Ability Flags  index:43    from 436273284 To 536870912
        SetMemory(0x664130, Add, 50265980),# units:Special Ability Flags  index:44    from 486604932 To 536870912
        SetMemory(0x664134, Add, 98500476),# units:Special Ability Flags  index:45    from 438370436 To 536870912
        SetMemory(0x664138, Add, 97451904),# units:Special Ability Flags  index:46    from 439419008 To 536870912
        SetMemory(0x66413C, Add, 134151036),# units:Special Ability Flags  index:47    from 402719876 To 536870912
        SetMemory(0x664140, Add, 67043136),# units:Special Ability Flags  index:48    from 469827776 To 536870912
        SetMemory(0x664144, Add, 98500412),# units:Special Ability Flags  index:49    from 438370500 To 536870912
        SetMemory(0x664148, Add, 133103488),# units:Special Ability Flags  index:50    from 403767424 To 536870912
        SetMemory(0x66414C, Add, 132054336),# units:Special Ability Flags  index:51    from 404816576 To 536870912
        SetMemory(0x664150, Add, 97451840),# units:Special Ability Flags  index:52    from 439419072 To 536870912
        SetMemory(0x664154, Add, 133103424),# units:Special Ability Flags  index:53    from 403767488 To 536870912
        SetMemory(0x664158, Add, 133102400),# units:Special Ability Flags  index:54    from 403768512 To 536870912
        SetMemory(0x66415C, Add, 100597564),# units:Special Ability Flags  index:55    from 436273348 To 536870912
        SetMemory(0x664160, Add, 50265916),# units:Special Ability Flags  index:56    from 486604996 To 536870912
        SetMemory(0x664164, Add, 100564796),# units:Special Ability Flags  index:57    from 436306116 To 536870912
        SetMemory(0x664170, Add, -975175684),# units:Special Ability Flags  index:60    from 1512046596 To 536870912
        SetMemory(0x664174, Add, 129957888),# units:Special Ability Flags  index:61    from 406913024 To 536870912
        SetMemory(0x664178, Add, 50265980),# units:Special Ability Flags  index:62    from 486604932 To 536870912
        SetMemory(0x66417C, Add, 65011456),# units:Special Ability Flags  index:63    from 471859456 To 536870912
        SetMemory(0x664180, Add, -939540488),# units:Special Ability Flags  index:64    from 1476411400 To 536870912
        SetMemory(0x664184, Add, 134152192),# units:Special Ability Flags  index:65    from 402718720 To 536870912
        SetMemory(0x664188, Add, -973078528),# units:Special Ability Flags  index:66    from 1509949440 To 536870912
        SetMemory(0x66418C, Add, 132055040),# units:Special Ability Flags  index:67    from 404815872 To 536870912
        SetMemory(0x664190, Add, 67108608),# units:Special Ability Flags  index:68    from 469762304 To 536870912
        SetMemory(0x664194, Add, -973094916),# units:Special Ability Flags  index:69    from 1509965828 To 536870912
        SetMemory(0x664198, Add, -973078532),# units:Special Ability Flags  index:70    from 1509949444 To 536870912
        SetMemory(0x66419C, Add, -975175684),# units:Special Ability Flags  index:71    from 1512046596 To 536870912
        SetMemory(0x6641A0, Add, -1006632964),# units:Special Ability Flags  index:72    from 1543503876 To 536870912
        SetMemory(0x6641A8, Add, 129957888),# units:Special Ability Flags  index:74    from 406913024 To 536870912
        SetMemory(0x6641AC, Add, 129957824),# units:Special Ability Flags  index:75    from 406913088 To 536870912
        SetMemory(0x6641B0, Add, 67108544),# units:Special Ability Flags  index:76    from 469762368 To 536870912
        SetMemory(0x6641B4, Add, 134152128),# units:Special Ability Flags  index:77    from 402718784 To 536870912
        SetMemory(0x6641B8, Add, -973078592),# units:Special Ability Flags  index:78    from 1509949504 To 536870912
        SetMemory(0x6641BC, Add, 132054976),# units:Special Ability Flags  index:79    from 404815936 To 536870912
        SetMemory(0x6641C0, Add, -973078596),# units:Special Ability Flags  index:80    from 1509949508 To 536870912
        SetMemory(0x6641C4, Add, -1006649408),# units:Special Ability Flags  index:81    from 1543520320 To 536870912
        SetMemory(0x6641C8, Add, -1006633028),# units:Special Ability Flags  index:82    from 1543503940 To 536870912
        SetMemory(0x6641CC, Add, -1006649344),# units:Special Ability Flags  index:83    from 1543520256 To 536870912
        SetMemory(0x6641D0, Add, -943767556),# units:Special Ability Flags  index:84    from 1480638468 To 536870912
        SetMemory(0x6641D8, Add, -975175748),# units:Special Ability Flags  index:86    from 1512046660 To 536870912
        SetMemory(0x6641DC, Add, 132054976),# units:Special Ability Flags  index:87    from 404815936 To 536870912
        SetMemory(0x6641E0, Add, -973078596),# units:Special Ability Flags  index:88    from 1509949508 To 536870912
        SetMemory(0x6641E4, Add, 134152192),# units:Special Ability Flags  index:89    from 402718720 To 536870912
        SetMemory(0x6641E8, Add, 134152192),# units:Special Ability Flags  index:90    from 402718720 To 536870912
        SetMemory(0x6641F4, Add, 134152192),# units:Special Ability Flags  index:93    from 402718720 To 536870912
        SetMemory(0x6641F8, Add, 134152188),# units:Special Ability Flags  index:94    from 402718724 To 536870912
        SetMemory(0x6641FC, Add, 134152192),# units:Special Ability Flags  index:95    from 402718720 To 536870912
        SetMemory(0x664200, Add, 134152192),# units:Special Ability Flags  index:96    from 402718720 To 536870912
        SetMemory(0x664208, Add, -975175748),# units:Special Ability Flags  index:98    from 1512046660 To 536870912
        SetMemory(0x66420C, Add, 132054464),# units:Special Ability Flags  index:99    from 404816448 To 536870912
        SetMemory(0x664210, Add, 132054464),# units:Special Ability Flags  index:100    from 404816448 To 536870912
        SetMemory(0x664218, Add, -1008730180),# units:Special Ability Flags  index:102    from 1545601092 To 536870912
        SetMemory(0x66421C, Add, 133103488),# units:Special Ability Flags  index:103    from 403767424 To 536870912
        SetMemory(0x664220, Add, 132054336),# units:Special Ability Flags  index:104    from 404816576 To 536870912
        SetMemory(0x664228, Add, -2751467553),# units:Special Ability Flags  index:106    from 3288338465 To 536870912
        SetMemory(0x66422C, Add, -606076931),# units:Special Ability Flags  index:107    from 1142947843 To 536870912
        SetMemory(0x664234, Add, -603979777),# units:Special Ability Flags  index:109    from 1140850689 To 536870912
        SetMemory(0x664238, Add, -603987969),# units:Special Ability Flags  index:110    from 1140858881 To 536870912
        SetMemory(0x66423C, Add, -2751463457),# units:Special Ability Flags  index:111    from 3288334369 To 536870912
        SetMemory(0x664240, Add, -603979777),# units:Special Ability Flags  index:112    from 1140850689 To 536870912
        SetMemory(0x664244, Add, -2751463457),# units:Special Ability Flags  index:113    from 3288334369 To 536870912
        SetMemory(0x664248, Add, -603979809),# units:Special Ability Flags  index:114    from 1140850721 To 536870912
        SetMemory(0x66424C, Add, -603979779),# units:Special Ability Flags  index:115    from 1140850691 To 536870912
        SetMemory(0x664250, Add, -603979809),# units:Special Ability Flags  index:116    from 1140850721 To 536870912
        SetMemory(0x664254, Add, -603979779),# units:Special Ability Flags  index:117    from 1140850691 To 536870912
        SetMemory(0x664258, Add, -603979779),# units:Special Ability Flags  index:118    from 1140850691 To 536870912
        SetMemory(0x664260, Add, -603979779),# units:Special Ability Flags  index:120    from 1140850691 To 536870912
        SetMemory(0x664268, Add, -603979809),# units:Special Ability Flags  index:122    from 1140850721 To 536870912
        SetMemory(0x66426C, Add, -603979777),# units:Special Ability Flags  index:123    from 1140850689 To 536870912
        SetMemory(0x664270, Add, -872448257),# units:Special Ability Flags  index:124    from 1409319169 To 536870912
        SetMemory(0x664274, Add, -2751463425),# units:Special Ability Flags  index:125    from 3288334337 To 536870912
        SetMemory(0x664278, Add, -603979777),# units:Special Ability Flags  index:126    from 1140850689 To 536870912
        SetMemory(0x66427C, Add, -603979777),# units:Special Ability Flags  index:127    from 1140850689 To 536870912
        SetMemory(0x664280, Add, -2048),# units:Special Ability Flags  index:128    from 536872960 To 536870912
        SetMemory(0x664284, Add, -2048),# units:Special Ability Flags  index:129    from 536872960 To 536870912
        SetMemory(0x664288, Add, 469696351),# units:Special Ability Flags  index:130    from 67174561 To 536870912
        SetMemory(0x66428C, Add, -1694568577),# units:Special Ability Flags  index:131    from 2231439489 To 536870912
        SetMemory(0x664290, Add, -1694568577),# units:Special Ability Flags  index:132    from 2231439489 To 536870912
        SetMemory(0x664294, Add, -1694568577),# units:Special Ability Flags  index:133    from 2231439489 To 536870912
        SetMemory(0x664298, Add, 452788095),# units:Special Ability Flags  index:134    from 84082817 To 536870912
        SetMemory(0x66429C, Add, 452788095),# units:Special Ability Flags  index:135    from 84082817 To 536870912
        SetMemory(0x6642A0, Add, 452788095),# units:Special Ability Flags  index:136    from 84082817 To 536870912
        SetMemory(0x6642A4, Add, 452788095),# units:Special Ability Flags  index:137    from 84082817 To 536870912
        SetMemory(0x6642A8, Add, 452788095),# units:Special Ability Flags  index:138    from 84082817 To 536870912
        SetMemory(0x6642AC, Add, 452788095),# units:Special Ability Flags  index:139    from 84082817 To 536870912
        SetMemory(0x6642B0, Add, 452788095),# units:Special Ability Flags  index:140    from 84082817 To 536870912
        SetMemory(0x6642B4, Add, 452788095),# units:Special Ability Flags  index:141    from 84082817 To 536870912
        SetMemory(0x6642B8, Add, 452788095),# units:Special Ability Flags  index:142    from 84082817 To 536870912
        SetMemory(0x6642BC, Add, 452788095),# units:Special Ability Flags  index:143    from 84082817 To 536870912
        SetMemory(0x6642C0, Add, 184319871),# units:Special Ability Flags  index:144    from 352551041 To 536870912
        SetMemory(0x6642C8, Add, 184352639),# units:Special Ability Flags  index:146    from 352518273 To 536870912
        SetMemory(0x6642CC, Add, 452755327),# units:Special Ability Flags  index:147    from 84115585 To 536870912
        SetMemory(0x6642D0, Add, 452755327),# units:Special Ability Flags  index:148    from 84115585 To 536870912
        SetMemory(0x6642D4, Add, 452910975),# units:Special Ability Flags  index:149    from 83959937 To 536870912
        SetMemory(0x6642D8, Add, 452788095),# units:Special Ability Flags  index:150    from 84082817 To 536870912
        SetMemory(0x6642DC, Add, 452755327),# units:Special Ability Flags  index:151    from 84115585 To 536870912
        SetMemory(0x6642E0, Add, 452755327),# units:Special Ability Flags  index:152    from 84115585 To 536870912
        SetMemory(0x6642E8, Add, -2751467521),# units:Special Ability Flags  index:154    from 3288338433 To 536870912
        SetMemory(0x6642EC, Add, -2751987713),# units:Special Ability Flags  index:155    from 3288858625 To 536870912
        SetMemory(0x6642F0, Add, -603979777),# units:Special Ability Flags  index:156    from 1140850689 To 536870912
        SetMemory(0x6642F4, Add, -603987969),# units:Special Ability Flags  index:157    from 1140858881 To 536870912
        SetMemory(0x6642FC, Add, -604504065),# units:Special Ability Flags  index:159    from 1141374977 To 536870912
        SetMemory(0x664300, Add, -2751987713),# units:Special Ability Flags  index:160    from 3288858625 To 536870912
        SetMemory(0x664308, Add, -872972289),# units:Special Ability Flags  index:162    from 1409843201 To 536870912
        SetMemory(0x66430C, Add, -604504065),# units:Special Ability Flags  index:163    from 1141374977 To 536870912
        SetMemory(0x664310, Add, -604504065),# units:Special Ability Flags  index:164    from 1141374977 To 536870912
        SetMemory(0x664314, Add, -604504065),# units:Special Ability Flags  index:165    from 1141374977 To 536870912
        SetMemory(0x664318, Add, -604504065),# units:Special Ability Flags  index:166    from 1141374977 To 536870912
        SetMemory(0x66431C, Add, -604504065),# units:Special Ability Flags  index:167    from 1141374977 To 536870912
        SetMemory(0x664320, Add, -603979777),# units:Special Ability Flags  index:168    from 1140850689 To 536870912
        SetMemory(0x664324, Add, -604504065),# units:Special Ability Flags  index:169    from 1141374977 To 536870912
        SetMemory(0x664328, Add, -604504065),# units:Special Ability Flags  index:170    from 1141374977 To 536870912
        SetMemory(0x66432C, Add, -604504065),# units:Special Ability Flags  index:171    from 1141374977 To 536870912
        SetMemory(0x664330, Add, -606601217),# units:Special Ability Flags  index:172    from 1143472129 To 536870912
        SetMemory(0x664334, Add, -67108865),# units:Special Ability Flags  index:173    from 603979777 To 536870912
        SetMemory(0x664338, Add, 469762047),# units:Special Ability Flags  index:174    from 67108865 To 536870912
        SetMemory(0x66433C, Add, 469762047),# units:Special Ability Flags  index:175    from 67108865 To 536870912
        SetMemory(0x664374, Add, -603979777),# units:Special Ability Flags  index:189    from 1140850689 To 536870912
        SetMemory(0x664378, Add, -603979777),# units:Special Ability Flags  index:190    from 1140850689 To 536870912
        SetMemory(0x664388, Add, -1),# units:Special Ability Flags  index:194    from 536870913 To 536870912
        SetMemory(0x66438C, Add, -1),# units:Special Ability Flags  index:195    from 536870913 To 536870912
        SetMemory(0x664390, Add, -1),# units:Special Ability Flags  index:196    from 536870913 To 536870912
        SetMemory(0x6643A0, Add, -603979777),# units:Special Ability Flags  index:200    from 1140850689 To 536870912
        SetMemory(0x6643A4, Add, 452755327),# units:Special Ability Flags  index:201    from 84115585 To 536870912
        SetMemory(0x6643DC, Add, -2048),# units:Special Ability Flags  index:215    from 536872960 To 536870912
        SetMemory(0x6643E0, Add, -8390656),# units:Special Ability Flags  index:216    from 545261568 To 536870912
        SetMemory(0x6643E4, Add, -8390656),# units:Special Ability Flags  index:217    from 545261568 To 536870912
        SetMemory(0x6643E8, Add, -8390656),# units:Special Ability Flags  index:218    from 545261568 To 536870912
        SetMemory(0x6643EC, Add, -8390656),# units:Special Ability Flags  index:219    from 545261568 To 536870912
        SetMemory(0x6643F0, Add, 528480256),# units:Special Ability Flags  index:220    from 8390656 To 536870912
        SetMemory(0x6643F4, Add, 528480256),# units:Special Ability Flags  index:221    from 8390656 To 536870912
        SetMemory(0x6643F8, Add, 528480256),# units:Special Ability Flags  index:222    from 8390656 To 536870912
        SetMemory(0x6643FC, Add, 528480256),# units:Special Ability Flags  index:223    from 8390656 To 536870912
        SetMemory(0x662DB8, Add, -1792),# units:Target Acquisition Range  index:1    from 7 To 0
        SetMemory(0x662DB8, Add, -327680),# units:Target Acquisition Range  index:2    from 5 To 0
        SetMemory(0x662DBC, Add, -16777216),# units:Target Acquisition Range  index:7    from 1 To 0
        SetMemory(0x662DC0, Add, -5),# units:Target Acquisition Range  index:8    from 5 To 0
        SetMemory(0x662DC0, Add, -196608),# units:Target Acquisition Range  index:10    from 3 To 0
        SetMemory(0x662DC4, Add, -6),# units:Target Acquisition Range  index:12    from 6 To 0
        SetMemory(0x662DC8, Add, -6),# units:Target Acquisition Range  index:16    from 6 To 0
        SetMemory(0x662DC8, Add, -83886080),# units:Target Acquisition Range  index:19    from 5 To 0
        SetMemory(0x662DCC, Add, -5),# units:Target Acquisition Range  index:20    from 5 To 0
        SetMemory(0x662DCC, Add, -1280),# units:Target Acquisition Range  index:21    from 5 To 0
        SetMemory(0x662DD0, Add, -100663296),# units:Target Acquisition Range  index:27    from 6 To 0
        SetMemory(0x662DD4, Add, -6),# units:Target Acquisition Range  index:28    from 6 To 0
        SetMemory(0x662DD4, Add, -1536),# units:Target Acquisition Range  index:29    from 6 To 0
        SetMemory(0x662DD8, Add, -3),# units:Target Acquisition Range  index:32    from 3 To 0
        SetMemory(0x662DD8, Add, -589824),# units:Target Acquisition Range  index:34    from 9 To 0
        SetMemory(0x662DDC, Add, -768),# units:Target Acquisition Range  index:37    from 3 To 0
        SetMemory(0x662DDC, Add, -262144),# units:Target Acquisition Range  index:38    from 4 To 0
        SetMemory(0x662DDC, Add, -50331648),# units:Target Acquisition Range  index:39    from 3 To 0
        SetMemory(0x662DE0, Add, -3),# units:Target Acquisition Range  index:40    from 3 To 0
        SetMemory(0x662DE0, Add, -256),# units:Target Acquisition Range  index:41    from 1 To 0
        SetMemory(0x662DE0, Add, -50331648),# units:Target Acquisition Range  index:43    from 3 To 0
        SetMemory(0x662DE4, Add, -8),# units:Target Acquisition Range  index:44    from 8 To 0
        SetMemory(0x662DE4, Add, -2048),# units:Target Acquisition Range  index:45    from 8 To 0
        SetMemory(0x662DE4, Add, -50331648),# units:Target Acquisition Range  index:47    from 3 To 0
        SetMemory(0x662DE8, Add, -3),# units:Target Acquisition Range  index:48    from 3 To 0
        SetMemory(0x662DE8, Add, -2048),# units:Target Acquisition Range  index:49    from 8 To 0
        SetMemory(0x662DE8, Add, -196608),# units:Target Acquisition Range  index:50    from 3 To 0
        SetMemory(0x662DE8, Add, -50331648),# units:Target Acquisition Range  index:51    from 3 To 0
        SetMemory(0x662DEC, Add, -1280),# units:Target Acquisition Range  index:53    from 5 To 0
        SetMemory(0x662DEC, Add, -196608),# units:Target Acquisition Range  index:54    from 3 To 0
        SetMemory(0x662DEC, Add, -50331648),# units:Target Acquisition Range  index:55    from 3 To 0
        SetMemory(0x662DF0, Add, -8),# units:Target Acquisition Range  index:56    from 8 To 0
        SetMemory(0x662DF4, Add, -9),# units:Target Acquisition Range  index:60    from 9 To 0
        SetMemory(0x662DF4, Add, -768),# units:Target Acquisition Range  index:61    from 3 To 0
        SetMemory(0x662DF4, Add, -458752),# units:Target Acquisition Range  index:62    from 7 To 0
        SetMemory(0x662DF4, Add, -117440512),# units:Target Acquisition Range  index:63    from 7 To 0
        SetMemory(0x662DF8, Add, -1),# units:Target Acquisition Range  index:64    from 1 To 0
        SetMemory(0x662DF8, Add, -768),# units:Target Acquisition Range  index:65    from 3 To 0
        SetMemory(0x662DF8, Add, -262144),# units:Target Acquisition Range  index:66    from 4 To 0
        SetMemory(0x662DF8, Add, -50331648),# units:Target Acquisition Range  index:67    from 3 To 0
        SetMemory(0x662DFC, Add, -3),# units:Target Acquisition Range  index:68    from 3 To 0
        SetMemory(0x662DFC, Add, -262144),# units:Target Acquisition Range  index:70    from 4 To 0
        SetMemory(0x662DFC, Add, -83886080),# units:Target Acquisition Range  index:71    from 5 To 0
        SetMemory(0x662E00, Add, -8),# units:Target Acquisition Range  index:72    from 8 To 0
        SetMemory(0x662E00, Add, -196608),# units:Target Acquisition Range  index:74    from 3 To 0
        SetMemory(0x662E00, Add, -50331648),# units:Target Acquisition Range  index:75    from 3 To 0
        SetMemory(0x662E04, Add, -3),# units:Target Acquisition Range  index:76    from 3 To 0
        SetMemory(0x662E04, Add, -768),# units:Target Acquisition Range  index:77    from 3 To 0
        SetMemory(0x662E04, Add, -262144),# units:Target Acquisition Range  index:78    from 4 To 0
        SetMemory(0x662E04, Add, -50331648),# units:Target Acquisition Range  index:79    from 3 To 0
        SetMemory(0x662E08, Add, -4),# units:Target Acquisition Range  index:80    from 4 To 0
        SetMemory(0x662E08, Add, -2048),# units:Target Acquisition Range  index:81    from 8 To 0
        SetMemory(0x662E08, Add, -524288),# units:Target Acquisition Range  index:82    from 8 To 0
        SetMemory(0x662E08, Add, -134217728),# units:Target Acquisition Range  index:83    from 8 To 0
        SetMemory(0x662E0C, Add, -327680),# units:Target Acquisition Range  index:86    from 5 To 0
        SetMemory(0x662E0C, Add, -50331648),# units:Target Acquisition Range  index:87    from 3 To 0
        SetMemory(0x662E10, Add, -4),# units:Target Acquisition Range  index:88    from 4 To 0
        SetMemory(0x662E18, Add, -589824),# units:Target Acquisition Range  index:98    from 9 To 0
        SetMemory(0x662E18, Add, -100663296),# units:Target Acquisition Range  index:99    from 6 To 0
        SetMemory(0x662E1C, Add, -6),# units:Target Acquisition Range  index:100    from 6 To 0
        SetMemory(0x662E1C, Add, -393216),# units:Target Acquisition Range  index:102    from 6 To 0
        SetMemory(0x662E1C, Add, -100663296),# units:Target Acquisition Range  index:103    from 6 To 0
        SetMemory(0x662E20, Add, -6),# units:Target Acquisition Range  index:104    from 6 To 0
        SetMemory(0x662E34, Add, -7),# units:Target Acquisition Range  index:124    from 7 To 0
        SetMemory(0x662E48, Add, -7),# units:Target Acquisition Range  index:144    from 7 To 0
        SetMemory(0x662E48, Add, -458752),# units:Target Acquisition Range  index:146    from 7 To 0
        SetMemory(0x662E58, Add, -458752),# units:Target Acquisition Range  index:162    from 7 To 0
        SetMemory(0x663238, Add, -1024),# units:Sight Range  index:1    from 9 To 5
        SetMemory(0x663238, Add, -196608),# units:Sight Range  index:2    from 8 To 5
        SetMemory(0x66323C, Add, -33554432),# units:Sight Range  index:7    from 7 To 5
        SetMemory(0x663240, Add, -2),# units:Sight Range  index:8    from 7 To 5
        SetMemory(0x663240, Add, -1280),# units:Sight Range  index:9    from 10 To 5
        SetMemory(0x663240, Add, -131072),# units:Sight Range  index:10    from 7 To 5
        SetMemory(0x663240, Add, -50331648),# units:Sight Range  index:11    from 8 To 5
        SetMemory(0x663244, Add, -6),# units:Sight Range  index:12    from 11 To 5
        SetMemory(0x663248, Add, -6),# units:Sight Range  index:16    from 11 To 5
        SetMemory(0x663248, Add, -50331648),# units:Sight Range  index:19    from 8 To 5
        SetMemory(0x66324C, Add, -2),# units:Sight Range  index:20    from 7 To 5
        SetMemory(0x66324C, Add, -512),# units:Sight Range  index:21    from 7 To 5
        SetMemory(0x66324C, Add, -327680),# units:Sight Range  index:22    from 10 To 5
        SetMemory(0x663250, Add, -50331648),# units:Sight Range  index:27    from 8 To 5
        SetMemory(0x663254, Add, -6),# units:Sight Range  index:28    from 11 To 5
        SetMemory(0x663254, Add, -1536),# units:Sight Range  index:29    from 11 To 5
        SetMemory(0x663258, Add, -2),# units:Sight Range  index:32    from 7 To 5
        SetMemory(0x663258, Add, -262144),# units:Sight Range  index:34    from 9 To 5
        SetMemory(0x66325C, Add, -65536),# units:Sight Range  index:38    from 6 To 5
        SetMemory(0x66325C, Add, -33554432),# units:Sight Range  index:39    from 7 To 5
        SetMemory(0x663260, Add, -512),# units:Sight Range  index:41    from 7 To 5
        SetMemory(0x663260, Add, -262144),# units:Sight Range  index:42    from 9 To 5
        SetMemory(0x663260, Add, -33554432),# units:Sight Range  index:43    from 7 To 5
        SetMemory(0x663264, Add, -6),# units:Sight Range  index:44    from 11 To 5
        SetMemory(0x663264, Add, -1280),# units:Sight Range  index:45    from 10 To 5
        SetMemory(0x663264, Add, -327680),# units:Sight Range  index:46    from 10 To 5
        SetMemory(0x663268, Add, -2),# units:Sight Range  index:48    from 7 To 5
        SetMemory(0x663268, Add, -1280),# units:Sight Range  index:49    from 10 To 5
        SetMemory(0x663268, Add, -67108864),# units:Sight Range  index:51    from 9 To 5
        SetMemory(0x66326C, Add, -5),# units:Sight Range  index:52    from 10 To 5
        SetMemory(0x66326C, Add, -768),# units:Sight Range  index:53    from 8 To 5
        SetMemory(0x66326C, Add, -33554432),# units:Sight Range  index:55    from 7 To 5
        SetMemory(0x663270, Add, -6),# units:Sight Range  index:56    from 11 To 5
        SetMemory(0x663270, Add, -1536),# units:Sight Range  index:57    from 11 To 5
        SetMemory(0x663274, Add, -4),# units:Sight Range  index:60    from 9 To 5
        SetMemory(0x663274, Add, -512),# units:Sight Range  index:61    from 7 To 5
        SetMemory(0x663274, Add, -327680),# units:Sight Range  index:62    from 10 To 5
        SetMemory(0x663274, Add, -83886080),# units:Sight Range  index:63    from 10 To 5
        SetMemory(0x663278, Add, -3),# units:Sight Range  index:64    from 8 To 5
        SetMemory(0x663278, Add, -512),# units:Sight Range  index:65    from 7 To 5
        SetMemory(0x663278, Add, -196608),# units:Sight Range  index:66    from 8 To 5
        SetMemory(0x663278, Add, -33554432),# units:Sight Range  index:67    from 7 To 5
        SetMemory(0x66327C, Add, -3),# units:Sight Range  index:68    from 8 To 5
        SetMemory(0x66327C, Add, -768),# units:Sight Range  index:69    from 8 To 5
        SetMemory(0x66327C, Add, -196608),# units:Sight Range  index:70    from 8 To 5
        SetMemory(0x66327C, Add, -67108864),# units:Sight Range  index:71    from 9 To 5
        SetMemory(0x663280, Add, -6),# units:Sight Range  index:72    from 11 To 5
        SetMemory(0x663280, Add, -131072),# units:Sight Range  index:74    from 7 To 5
        SetMemory(0x663280, Add, -33554432),# units:Sight Range  index:75    from 7 To 5
        SetMemory(0x663284, Add, -3),# units:Sight Range  index:76    from 8 To 5
        SetMemory(0x663284, Add, -512),# units:Sight Range  index:77    from 7 To 5
        SetMemory(0x663284, Add, -196608),# units:Sight Range  index:78    from 8 To 5
        SetMemory(0x663284, Add, -33554432),# units:Sight Range  index:79    from 7 To 5
        SetMemory(0x663288, Add, -5),# units:Sight Range  index:80    from 10 To 5
        SetMemory(0x663288, Add, -1280),# units:Sight Range  index:81    from 10 To 5
        SetMemory(0x663288, Add, -262144),# units:Sight Range  index:82    from 9 To 5
        SetMemory(0x663288, Add, -83886080),# units:Sight Range  index:83    from 10 To 5
        SetMemory(0x66328C, Add, -4),# units:Sight Range  index:84    from 9 To 5
        SetMemory(0x66328C, Add, -262144),# units:Sight Range  index:86    from 9 To 5
        SetMemory(0x66328C, Add, -33554432),# units:Sight Range  index:87    from 7 To 5
        SetMemory(0x663290, Add, -5),# units:Sight Range  index:88    from 10 To 5
        SetMemory(0x663290, Add, -512),# units:Sight Range  index:89    from 7 To 5
        SetMemory(0x663290, Add, -131072),# units:Sight Range  index:90    from 7 To 5
        SetMemory(0x663294, Add, -512),# units:Sight Range  index:93    from 7 To 5
        SetMemory(0x663294, Add, -131072),# units:Sight Range  index:94    from 7 To 5
        SetMemory(0x663294, Add, -33554432),# units:Sight Range  index:95    from 7 To 5
        SetMemory(0x663298, Add, -2),# units:Sight Range  index:96    from 7 To 5
        SetMemory(0x663298, Add, -262144),# units:Sight Range  index:98    from 9 To 5
        SetMemory(0x663298, Add, -83886080),# units:Sight Range  index:99    from 10 To 5
        SetMemory(0x66329C, Add, -6),# units:Sight Range  index:100    from 11 To 5
        SetMemory(0x66329C, Add, -393216),# units:Sight Range  index:102    from 11 To 5
        SetMemory(0x66329C, Add, -50331648),# units:Sight Range  index:103    from 8 To 5
        SetMemory(0x6632A0, Add, -6),# units:Sight Range  index:104    from 11 To 5
        SetMemory(0x6632A0, Add, -327680),# units:Sight Range  index:106    from 10 To 5
        SetMemory(0x6632A0, Add, -83886080),# units:Sight Range  index:107    from 10 To 5
        SetMemory(0x6632A4, Add, -768),# units:Sight Range  index:109    from 8 To 5
        SetMemory(0x6632A4, Add, -196608),# units:Sight Range  index:110    from 8 To 5
        SetMemory(0x6632A4, Add, -50331648),# units:Sight Range  index:111    from 8 To 5
        SetMemory(0x6632A8, Add, -3),# units:Sight Range  index:112    from 8 To 5
        SetMemory(0x6632A8, Add, -768),# units:Sight Range  index:113    from 8 To 5
        SetMemory(0x6632A8, Add, -327680),# units:Sight Range  index:114    from 10 To 5
        SetMemory(0x6632A8, Add, -50331648),# units:Sight Range  index:115    from 8 To 5
        SetMemory(0x6632AC, Add, -5),# units:Sight Range  index:116    from 10 To 5
        SetMemory(0x6632AC, Add, -768),# units:Sight Range  index:117    from 8 To 5
        SetMemory(0x6632AC, Add, -196608),# units:Sight Range  index:118    from 8 To 5
        SetMemory(0x6632B0, Add, -3),# units:Sight Range  index:120    from 8 To 5
        SetMemory(0x6632B0, Add, -196608),# units:Sight Range  index:122    from 8 To 5
        SetMemory(0x6632B0, Add, -50331648),# units:Sight Range  index:123    from 8 To 5
        SetMemory(0x6632B4, Add, -6),# units:Sight Range  index:124    from 11 To 5
        SetMemory(0x6632B4, Add, -1280),# units:Sight Range  index:125    from 10 To 5
        SetMemory(0x6632B4, Add, -327680),# units:Sight Range  index:126    from 10 To 5
        SetMemory(0x6632B4, Add, -50331648),# units:Sight Range  index:127    from 8 To 5
        SetMemory(0x6632B8, Add, -327680),# units:Sight Range  index:130    from 10 To 5
        SetMemory(0x6632B8, Add, -67108864),# units:Sight Range  index:131    from 9 To 5
        SetMemory(0x6632BC, Add, -5),# units:Sight Range  index:132    from 10 To 5
        SetMemory(0x6632BC, Add, -1536),# units:Sight Range  index:133    from 11 To 5
        SetMemory(0x6632BC, Add, -196608),# units:Sight Range  index:134    from 8 To 5
        SetMemory(0x6632BC, Add, -50331648),# units:Sight Range  index:135    from 8 To 5
        SetMemory(0x6632C0, Add, -3),# units:Sight Range  index:136    from 8 To 5
        SetMemory(0x6632C0, Add, -768),# units:Sight Range  index:137    from 8 To 5
        SetMemory(0x6632C0, Add, -196608),# units:Sight Range  index:138    from 8 To 5
        SetMemory(0x6632C0, Add, -50331648),# units:Sight Range  index:139    from 8 To 5
        SetMemory(0x6632C4, Add, -3),# units:Sight Range  index:140    from 8 To 5
        SetMemory(0x6632C4, Add, -768),# units:Sight Range  index:141    from 8 To 5
        SetMemory(0x6632C4, Add, -196608),# units:Sight Range  index:142    from 8 To 5
        SetMemory(0x6632C4, Add, -83886080),# units:Sight Range  index:143    from 10 To 5
        SetMemory(0x6632C8, Add, -5),# units:Sight Range  index:144    from 10 To 5
        SetMemory(0x6632C8, Add, -327680),# units:Sight Range  index:146    from 10 To 5
        SetMemory(0x6632C8, Add, -50331648),# units:Sight Range  index:147    from 8 To 5
        SetMemory(0x6632CC, Add, -3),# units:Sight Range  index:148    from 8 To 5
        SetMemory(0x6632CC, Add, -512),# units:Sight Range  index:149    from 7 To 5
        SetMemory(0x6632CC, Add, -196608),# units:Sight Range  index:150    from 8 To 5
        SetMemory(0x6632CC, Add, -50331648),# units:Sight Range  index:151    from 8 To 5
        SetMemory(0x6632D0, Add, -3),# units:Sight Range  index:152    from 8 To 5
        SetMemory(0x6632D0, Add, -393216),# units:Sight Range  index:154    from 11 To 5
        SetMemory(0x6632D0, Add, -83886080),# units:Sight Range  index:155    from 10 To 5
        SetMemory(0x6632D4, Add, -3),# units:Sight Range  index:156    from 8 To 5
        SetMemory(0x6632D4, Add, -1280),# units:Sight Range  index:157    from 10 To 5
        SetMemory(0x6632D4, Add, -83886080),# units:Sight Range  index:159    from 10 To 5
        SetMemory(0x6632D8, Add, -5),# units:Sight Range  index:160    from 10 To 5
        SetMemory(0x6632D8, Add, -393216),# units:Sight Range  index:162    from 11 To 5
        SetMemory(0x6632D8, Add, -83886080),# units:Sight Range  index:163    from 10 To 5
        SetMemory(0x6632DC, Add, -5),# units:Sight Range  index:164    from 10 To 5
        SetMemory(0x6632DC, Add, -1280),# units:Sight Range  index:165    from 10 To 5
        SetMemory(0x6632DC, Add, -327680),# units:Sight Range  index:166    from 10 To 5
        SetMemory(0x6632DC, Add, -83886080),# units:Sight Range  index:167    from 10 To 5
        SetMemory(0x6632E0, Add, -3),# units:Sight Range  index:168    from 8 To 5
        SetMemory(0x6632E0, Add, -1280),# units:Sight Range  index:169    from 10 To 5
        SetMemory(0x6632E0, Add, -327680),# units:Sight Range  index:170    from 10 To 5
        SetMemory(0x6632E0, Add, -83886080),# units:Sight Range  index:171    from 10 To 5
        SetMemory(0x6632E4, Add, -5),# units:Sight Range  index:172    from 10 To 5
        SetMemory(0x6632E4, Add, -1280),# units:Sight Range  index:173    from 10 To 5
        SetMemory(0x6632E4, Add, -327680),# units:Sight Range  index:174    from 10 To 5
        SetMemory(0x6632E4, Add, -83886080),# units:Sight Range  index:175    from 10 To 5
        SetMemory(0x6632F4, Add, -768),# units:Sight Range  index:189    from 8 To 5
        SetMemory(0x6632F4, Add, -327680),# units:Sight Range  index:190    from 10 To 5
        SetMemory(0x6632F8, Add, -196608),# units:Sight Range  index:194    from 8 To 5
        SetMemory(0x6632F8, Add, -50331648),# units:Sight Range  index:195    from 8 To 5
        SetMemory(0x6632FC, Add, -3),# units:Sight Range  index:196    from 8 To 5
        SetMemory(0x663300, Add, -3),# units:Sight Range  index:200    from 8 To 5
        SetMemory(0x663300, Add, -1280),# units:Sight Range  index:201    from 10 To 5
        SetMemory(0x6635D0, Add, -65536),# units:Armor Upgrade  index:2    from 1 To 0
        SetMemory(0x6635D8, Add, -2),# units:Armor Upgrade  index:8    from 2 To 0
        SetMemory(0x6635D8, Add, -512),# units:Armor Upgrade  index:9    from 2 To 0
        SetMemory(0x6635D8, Add, -33554432),# units:Armor Upgrade  index:11    from 2 To 0
        SetMemory(0x6635DC, Add, -2),# units:Armor Upgrade  index:12    from 2 To 0
        SetMemory(0x6635E0, Add, -16777216),# units:Armor Upgrade  index:19    from 1 To 0
        SetMemory(0x6635E4, Add, 1),# units:Armor Upgrade  index:20    from 0 To 1
        SetMemory(0x6635E4, Add, -256),# units:Armor Upgrade  index:21    from 2 To 1
        SetMemory(0x6635E4, Add, -65536),# units:Armor Upgrade  index:22    from 2 To 1
        SetMemory(0x6635E8, Add, -16777216),# units:Armor Upgrade  index:27    from 2 To 1
        SetMemory(0x6635EC, Add, -1),# units:Armor Upgrade  index:28    from 2 To 1
        SetMemory(0x6635EC, Add, -256),# units:Armor Upgrade  index:29    from 2 To 1
        SetMemory(0x6635F0, Add, 2),# units:Armor Upgrade  index:32    from 0 To 2
        SetMemory(0x6635F0, Add, 131072),# units:Armor Upgrade  index:34    from 0 To 2
        SetMemory(0x6635F4, Add, -256),# units:Armor Upgrade  index:37    from 3 To 2
        SetMemory(0x6635F4, Add, -65536),# units:Armor Upgrade  index:38    from 3 To 2
        SetMemory(0x6635F4, Add, -16777216),# units:Armor Upgrade  index:39    from 3 To 2
        SetMemory(0x6635F8, Add, -1),# units:Armor Upgrade  index:40    from 3 To 2
        SetMemory(0x6635F8, Add, -768),# units:Armor Upgrade  index:41    from 3 To 0
        SetMemory(0x6635F8, Add, -196608),# units:Armor Upgrade  index:42    from 4 To 1
        SetMemory(0x6635F8, Add, -50331648),# units:Armor Upgrade  index:43    from 4 To 1
        SetMemory(0x6635FC, Add, -3),# units:Armor Upgrade  index:44    from 4 To 1
        SetMemory(0x6635FC, Add, 512),# units:Armor Upgrade  index:45    from 4 To 6
        SetMemory(0x6635FC, Add, 262144),# units:Armor Upgrade  index:46    from 3 To 7
        SetMemory(0x6635FC, Add, 50331648),# units:Armor Upgrade  index:47    from 4 To 7
        SetMemory(0x663600, Add, 4),# units:Armor Upgrade  index:48    from 3 To 7
        SetMemory(0x663600, Add, 768),# units:Armor Upgrade  index:49    from 4 To 7
        SetMemory(0x663600, Add, 262144),# units:Armor Upgrade  index:50    from 3 To 7
        SetMemory(0x663600, Add, 83886080),# units:Armor Upgrade  index:51    from 3 To 8
        SetMemory(0x663604, Add, 6),# units:Armor Upgrade  index:52    from 3 To 9
        SetMemory(0x663604, Add, 1792),# units:Armor Upgrade  index:53    from 3 To 10
        SetMemory(0x663604, Add, -196608),# units:Armor Upgrade  index:54    from 3 To 0
        SetMemory(0x663604, Add, -67108864),# units:Armor Upgrade  index:55    from 4 To 0
        SetMemory(0x663608, Add, -4),# units:Armor Upgrade  index:56    from 4 To 0
        SetMemory(0x663608, Add, -1024),# units:Armor Upgrade  index:57    from 4 To 0
        SetMemory(0x66360C, Add, -6),# units:Armor Upgrade  index:60    from 6 To 0
        SetMemory(0x66360C, Add, -1280),# units:Armor Upgrade  index:61    from 5 To 0
        SetMemory(0x66360C, Add, -196608),# units:Armor Upgrade  index:62    from 4 To 1
        SetMemory(0x66360C, Add, -67108864),# units:Armor Upgrade  index:63    from 5 To 1
        SetMemory(0x663610, Add, -4),# units:Armor Upgrade  index:64    from 5 To 1
        SetMemory(0x663610, Add, -1024),# units:Armor Upgrade  index:65    from 5 To 1
        SetMemory(0x663610, Add, -262144),# units:Armor Upgrade  index:66    from 5 To 1
        SetMemory(0x663610, Add, -67108864),# units:Armor Upgrade  index:67    from 5 To 1
        SetMemory(0x663614, Add, -4),# units:Armor Upgrade  index:68    from 5 To 1
        SetMemory(0x663614, Add, -1280),# units:Armor Upgrade  index:69    from 6 To 1
        SetMemory(0x663614, Add, -327680),# units:Armor Upgrade  index:70    from 6 To 1
        SetMemory(0x663614, Add, -83886080),# units:Armor Upgrade  index:71    from 6 To 1
        SetMemory(0x663618, Add, -4),# units:Armor Upgrade  index:72    from 6 To 2
        SetMemory(0x663618, Add, -196608),# units:Armor Upgrade  index:74    from 5 To 2
        SetMemory(0x663618, Add, -50331648),# units:Armor Upgrade  index:75    from 5 To 2
        SetMemory(0x66361C, Add, -3),# units:Armor Upgrade  index:76    from 5 To 2
        SetMemory(0x66361C, Add, -768),# units:Armor Upgrade  index:77    from 5 To 2
        SetMemory(0x66361C, Add, -327680),# units:Armor Upgrade  index:78    from 5 To 0
        SetMemory(0x66361C, Add, -83886080),# units:Armor Upgrade  index:79    from 5 To 0
        SetMemory(0x663620, Add, -6),# units:Armor Upgrade  index:80    from 6 To 0
        SetMemory(0x663620, Add, -1024),# units:Armor Upgrade  index:81    from 5 To 1
        SetMemory(0x663620, Add, -327680),# units:Armor Upgrade  index:82    from 6 To 1
        SetMemory(0x663620, Add, 16777216),# units:Armor Upgrade  index:83    from 5 To 6
        SetMemory(0x663624, Add, 33554432),# units:Armor Upgrade  index:87    from 5 To 7
        SetMemory(0x663628, Add, 1),# units:Armor Upgrade  index:88    from 6 To 7
        SetMemory(0x663628, Add, -13568),# units:Armor Upgrade  index:89    from 60 To 7
        SetMemory(0x663628, Add, -3473408),# units:Armor Upgrade  index:90    from 60 To 7
        SetMemory(0x66362C, Add, -13568),# units:Armor Upgrade  index:93    from 60 To 7
        SetMemory(0x66362C, Add, -3473408),# units:Armor Upgrade  index:94    from 60 To 7
        SetMemory(0x66362C, Add, -889192448),# units:Armor Upgrade  index:95    from 60 To 7
        SetMemory(0x663630, Add, -51),# units:Armor Upgrade  index:96    from 60 To 9
        SetMemory(0x663630, Add, -393216),# units:Armor Upgrade  index:98    from 6 To 0
        SetMemory(0x663634, Add, -131072),# units:Armor Upgrade  index:102    from 2 To 0
        SetMemory(0x663634, Add, -50331648),# units:Armor Upgrade  index:103    from 3 To 0
        SetMemory(0x663638, Add, -3),# units:Armor Upgrade  index:104    from 3 To 0
        SetMemory(0x663638, Add, -3932160),# units:Armor Upgrade  index:106    from 60 To 0
        SetMemory(0x663638, Add, -1006632960),# units:Armor Upgrade  index:107    from 60 To 0
        SetMemory(0x66363C, Add, -15360),# units:Armor Upgrade  index:109    from 60 To 0
        SetMemory(0x66363C, Add, -3342336),# units:Armor Upgrade  index:110    from 60 To 9
        SetMemory(0x66363C, Add, -1006632960),# units:Armor Upgrade  index:111    from 60 To 0
        SetMemory(0x663640, Add, -60),# units:Armor Upgrade  index:112    from 60 To 0
        SetMemory(0x663640, Add, -15104),# units:Armor Upgrade  index:113    from 60 To 1
        SetMemory(0x663640, Add, -3866624),# units:Armor Upgrade  index:114    from 60 To 1
        SetMemory(0x663640, Add, -989855744),# units:Armor Upgrade  index:115    from 60 To 1
        SetMemory(0x663644, Add, -59),# units:Armor Upgrade  index:116    from 60 To 1
        SetMemory(0x663644, Add, -15104),# units:Armor Upgrade  index:117    from 60 To 1
        SetMemory(0x663644, Add, -3866624),# units:Armor Upgrade  index:118    from 60 To 1
        SetMemory(0x663648, Add, -59),# units:Armor Upgrade  index:120    from 60 To 1
        SetMemory(0x663648, Add, -3866624),# units:Armor Upgrade  index:122    from 60 To 1
        SetMemory(0x663648, Add, -989855744),# units:Armor Upgrade  index:123    from 60 To 1
        SetMemory(0x66364C, Add, -59),# units:Armor Upgrade  index:124    from 60 To 1
        SetMemory(0x66364C, Add, -14848),# units:Armor Upgrade  index:125    from 60 To 2
        SetMemory(0x66364C, Add, -3801088),# units:Armor Upgrade  index:126    from 60 To 2
        SetMemory(0x66364C, Add, -973078528),# units:Armor Upgrade  index:127    from 60 To 2
        SetMemory(0x663650, Add, -60),# units:Armor Upgrade  index:128    from 60 To 0
        SetMemory(0x663650, Add, -15360),# units:Armor Upgrade  index:129    from 60 To 0
        SetMemory(0x663650, Add, -3801088),# units:Armor Upgrade  index:130    from 60 To 2
        SetMemory(0x663650, Add, -973078528),# units:Armor Upgrade  index:131    from 60 To 2
        SetMemory(0x663654, Add, -58),# units:Armor Upgrade  index:132    from 60 To 2
        SetMemory(0x663654, Add, -14848),# units:Armor Upgrade  index:133    from 60 To 2
        SetMemory(0x663654, Add, -3801088),# units:Armor Upgrade  index:134    from 60 To 2
        SetMemory(0x663654, Add, -973078528),# units:Armor Upgrade  index:135    from 60 To 2
        SetMemory(0x663658, Add, -57),# units:Armor Upgrade  index:136    from 60 To 3
        SetMemory(0x663658, Add, -15360),# units:Armor Upgrade  index:137    from 60 To 0
        SetMemory(0x663658, Add, -3932160),# units:Armor Upgrade  index:138    from 60 To 0
        SetMemory(0x663658, Add, -939524096),# units:Armor Upgrade  index:139    from 60 To 4
        SetMemory(0x66365C, Add, -56),# units:Armor Upgrade  index:140    from 60 To 4
        SetMemory(0x66365C, Add, -14336),# units:Armor Upgrade  index:141    from 60 To 4
        SetMemory(0x66365C, Add, -3538944),# units:Armor Upgrade  index:142    from 60 To 6
        SetMemory(0x66365C, Add, -889192448),# units:Armor Upgrade  index:143    from 60 To 7
        SetMemory(0x663660, Add, -53),# units:Armor Upgrade  index:144    from 60 To 7
        SetMemory(0x663660, Add, -3473408),# units:Armor Upgrade  index:146    from 60 To 7
        SetMemory(0x663660, Add, -889192448),# units:Armor Upgrade  index:147    from 60 To 7
        SetMemory(0x663664, Add, -53),# units:Armor Upgrade  index:148    from 60 To 7
        SetMemory(0x663664, Add, -13056),# units:Armor Upgrade  index:149    from 60 To 9
        SetMemory(0x663664, Add, -3473408),# units:Armor Upgrade  index:150    from 60 To 7
        SetMemory(0x663664, Add, -889192448),# units:Armor Upgrade  index:151    from 60 To 7
        SetMemory(0x663668, Add, -53),# units:Armor Upgrade  index:152    from 60 To 7
        SetMemory(0x663668, Add, -3735552),# units:Armor Upgrade  index:154    from 60 To 3
        SetMemory(0x663668, Add, -838860800),# units:Armor Upgrade  index:155    from 60 To 10
        SetMemory(0x66366C, Add, -57),# units:Armor Upgrade  index:156    from 60 To 3
        SetMemory(0x66366C, Add, -14592),# units:Armor Upgrade  index:157    from 60 To 3
        SetMemory(0x66366C, Add, -1006632960),# units:Armor Upgrade  index:159    from 60 To 0
        SetMemory(0x663670, Add, -60),# units:Armor Upgrade  index:160    from 60 To 0
        SetMemory(0x663670, Add, -3932160),# units:Armor Upgrade  index:162    from 60 To 0
        SetMemory(0x663670, Add, -989855744),# units:Armor Upgrade  index:163    from 60 To 1
        SetMemory(0x663674, Add, -56),# units:Armor Upgrade  index:164    from 60 To 4
        SetMemory(0x663674, Add, -14336),# units:Armor Upgrade  index:165    from 60 To 4
        SetMemory(0x663674, Add, -3670016),# units:Armor Upgrade  index:166    from 60 To 4
        SetMemory(0x663674, Add, -939524096),# units:Armor Upgrade  index:167    from 60 To 4
        SetMemory(0x663678, Add, -56),# units:Armor Upgrade  index:168    from 60 To 4
        SetMemory(0x663678, Add, -14336),# units:Armor Upgrade  index:169    from 60 To 4
        SetMemory(0x663678, Add, -3670016),# units:Armor Upgrade  index:170    from 60 To 4
        SetMemory(0x663678, Add, -939524096),# units:Armor Upgrade  index:171    from 60 To 4
        SetMemory(0x66367C, Add, -56),# units:Armor Upgrade  index:172    from 60 To 4
        SetMemory(0x66367C, Add, -14080),# units:Armor Upgrade  index:173    from 60 To 5
        SetMemory(0x66367C, Add, -3538944),# units:Armor Upgrade  index:174    from 60 To 6
        SetMemory(0x66367C, Add, -905969664),# units:Armor Upgrade  index:175    from 60 To 6
        SetMemory(0x66368C, Add, -13824),# units:Armor Upgrade  index:189    from 60 To 6
        SetMemory(0x66368C, Add, -3538944),# units:Armor Upgrade  index:190    from 60 To 6
        SetMemory(0x663690, Add, -3735552),# units:Armor Upgrade  index:194    from 60 To 3
        SetMemory(0x663690, Add, -889192448),# units:Armor Upgrade  index:195    from 60 To 7
        SetMemory(0x663694, Add, -58),# units:Armor Upgrade  index:196    from 60 To 2
        SetMemory(0x663698, Add, -52),# units:Armor Upgrade  index:200    from 60 To 8
        SetMemory(0x663698, Add, -13056),# units:Armor Upgrade  index:201    from 60 To 9
        SetMemory(0x6636A4, Add, -989855744),# units:Armor Upgrade  index:215    from 60 To 1
        SetMemory(0x6636A8, Add, -60),# units:Armor Upgrade  index:216    from 60 To 0
        SetMemory(0x6636A8, Add, -14336),# units:Armor Upgrade  index:217    from 60 To 4
        SetMemory(0x6636A8, Add, -3473408),# units:Armor Upgrade  index:218    from 60 To 7
        SetMemory(0x6636A8, Add, -889192448),# units:Armor Upgrade  index:219    from 60 To 7
        SetMemory(0x6636AC, Add, -53),# units:Armor Upgrade  index:220    from 60 To 7
        SetMemory(0x6636AC, Add, -12544),# units:Armor Upgrade  index:221    from 60 To 11
        SetMemory(0x6636AC, Add, -3211264),# units:Armor Upgrade  index:222    from 60 To 11
        SetMemory(0x6636AC, Add, -1006632960),# units:Armor Upgrade  index:223    from 60 To 0
        SetMemory(0x662180, Add, -256),# units:Unit Size  index:1    from 1 To 0
        SetMemory(0x662180, Add, -131072),# units:Unit Size  index:2    from 2 To 0
        SetMemory(0x662184, Add, -16777216),# units:Unit Size  index:7    from 1 To 0
        SetMemory(0x662188, Add, -3),# units:Unit Size  index:8    from 3 To 0
        SetMemory(0x662188, Add, -768),# units:Unit Size  index:9    from 3 To 0
        SetMemory(0x662188, Add, -65536),# units:Unit Size  index:10    from 1 To 0
        SetMemory(0x662188, Add, -50331648),# units:Unit Size  index:11    from 3 To 0
        SetMemory(0x66218C, Add, -3),# units:Unit Size  index:12    from 3 To 0
        SetMemory(0x662190, Add, -1),# units:Unit Size  index:16    from 1 To 0
        SetMemory(0x662190, Add, -33554432),# units:Unit Size  index:19    from 2 To 0
        SetMemory(0x662194, Add, -1),# units:Unit Size  index:20    from 1 To 0
        SetMemory(0x662194, Add, -768),# units:Unit Size  index:21    from 3 To 0
        SetMemory(0x662194, Add, -196608),# units:Unit Size  index:22    from 3 To 0
        SetMemory(0x662198, Add, -50331648),# units:Unit Size  index:27    from 3 To 0
        SetMemory(0x66219C, Add, -3),# units:Unit Size  index:28    from 3 To 0
        SetMemory(0x66219C, Add, -768),# units:Unit Size  index:29    from 3 To 0
        SetMemory(0x6621A0, Add, -1),# units:Unit Size  index:32    from 1 To 0
        SetMemory(0x6621A0, Add, -65536),# units:Unit Size  index:34    from 1 To 0
        SetMemory(0x6621A4, Add, -256),# units:Unit Size  index:37    from 1 To 0
        SetMemory(0x6621A4, Add, -131072),# units:Unit Size  index:38    from 2 To 0
        SetMemory(0x6621A4, Add, -50331648),# units:Unit Size  index:39    from 3 To 0
        SetMemory(0x6621A8, Add, -1),# units:Unit Size  index:40    from 1 To 0
        SetMemory(0x6621A8, Add, -256),# units:Unit Size  index:41    from 1 To 0
        SetMemory(0x6621A8, Add, -196608),# units:Unit Size  index:42    from 3 To 0
        SetMemory(0x6621A8, Add, -16777216),# units:Unit Size  index:43    from 1 To 0
        SetMemory(0x6621AC, Add, -3),# units:Unit Size  index:44    from 3 To 0
        SetMemory(0x6621AC, Add, -512),# units:Unit Size  index:45    from 2 To 0
        SetMemory(0x6621AC, Add, -131072),# units:Unit Size  index:46    from 2 To 0
        SetMemory(0x6621AC, Add, -16777216),# units:Unit Size  index:47    from 1 To 0
        SetMemory(0x6621B0, Add, -3),# units:Unit Size  index:48    from 3 To 0
        SetMemory(0x6621B0, Add, -512),# units:Unit Size  index:49    from 2 To 0
        SetMemory(0x6621B0, Add, -65536),# units:Unit Size  index:50    from 1 To 0
        SetMemory(0x6621B0, Add, -16777216),# units:Unit Size  index:51    from 1 To 0
        SetMemory(0x6621B4, Add, -2),# units:Unit Size  index:52    from 2 To 0
        SetMemory(0x6621B4, Add, -512),# units:Unit Size  index:53    from 2 To 0
        SetMemory(0x6621B4, Add, -65536),# units:Unit Size  index:54    from 1 To 0
        SetMemory(0x6621B4, Add, -16777216),# units:Unit Size  index:55    from 1 To 0
        SetMemory(0x6621B8, Add, -3),# units:Unit Size  index:56    from 3 To 0
        SetMemory(0x6621B8, Add, -768),# units:Unit Size  index:57    from 3 To 0
        SetMemory(0x6621BC, Add, -2),# units:Unit Size  index:60    from 2 To 0
        SetMemory(0x6621BC, Add, -256),# units:Unit Size  index:61    from 1 To 0
        SetMemory(0x6621BC, Add, -196608),# units:Unit Size  index:62    from 3 To 0
        SetMemory(0x6621BC, Add, -50331648),# units:Unit Size  index:63    from 3 To 0
        SetMemory(0x6621C0, Add, -1),# units:Unit Size  index:64    from 1 To 0
        SetMemory(0x6621C0, Add, -256),# units:Unit Size  index:65    from 1 To 0
        SetMemory(0x6621C0, Add, -196608),# units:Unit Size  index:66    from 3 To 0
        SetMemory(0x6621C0, Add, -16777216),# units:Unit Size  index:67    from 1 To 0
        SetMemory(0x6621C4, Add, -3),# units:Unit Size  index:68    from 3 To 0
        SetMemory(0x6621C4, Add, -768),# units:Unit Size  index:69    from 3 To 0
        SetMemory(0x6621C4, Add, -196608),# units:Unit Size  index:70    from 3 To 0
        SetMemory(0x6621C4, Add, -50331648),# units:Unit Size  index:71    from 3 To 0
        SetMemory(0x6621C8, Add, -3),# units:Unit Size  index:72    from 3 To 0
        SetMemory(0x6621C8, Add, -65536),# units:Unit Size  index:74    from 1 To 0
        SetMemory(0x6621C8, Add, -16777216),# units:Unit Size  index:75    from 1 To 0
        SetMemory(0x6621CC, Add, -3),# units:Unit Size  index:76    from 3 To 0
        SetMemory(0x6621CC, Add, -256),# units:Unit Size  index:77    from 1 To 0
        SetMemory(0x6621CC, Add, -196608),# units:Unit Size  index:78    from 3 To 0
        SetMemory(0x6621CC, Add, -16777216),# units:Unit Size  index:79    from 1 To 0
        SetMemory(0x6621D0, Add, -3),# units:Unit Size  index:80    from 3 To 0
        SetMemory(0x6621D0, Add, -768),# units:Unit Size  index:81    from 3 To 0
        SetMemory(0x6621D0, Add, -196608),# units:Unit Size  index:82    from 3 To 0
        SetMemory(0x6621D0, Add, -50331648),# units:Unit Size  index:83    from 3 To 0
        SetMemory(0x6621D4, Add, -1),# units:Unit Size  index:84    from 1 To 0
        SetMemory(0x6621D4, Add, -196608),# units:Unit Size  index:86    from 3 To 0
        SetMemory(0x6621D4, Add, -16777216),# units:Unit Size  index:87    from 1 To 0
        SetMemory(0x6621D8, Add, -3),# units:Unit Size  index:88    from 3 To 0
        SetMemory(0x6621D8, Add, -256),# units:Unit Size  index:89    from 1 To 0
        SetMemory(0x6621D8, Add, -65536),# units:Unit Size  index:90    from 1 To 0
        SetMemory(0x6621DC, Add, -256),# units:Unit Size  index:93    from 1 To 0
        SetMemory(0x6621DC, Add, -65536),# units:Unit Size  index:94    from 1 To 0
        SetMemory(0x6621DC, Add, -16777216),# units:Unit Size  index:95    from 1 To 0
        SetMemory(0x6621E0, Add, -1),# units:Unit Size  index:96    from 1 To 0
        SetMemory(0x6621E0, Add, -131072),# units:Unit Size  index:98    from 2 To 0
        SetMemory(0x6621E0, Add, -16777216),# units:Unit Size  index:99    from 1 To 0
        SetMemory(0x6621E4, Add, -1),# units:Unit Size  index:100    from 1 To 0
        SetMemory(0x6621E4, Add, -196608),# units:Unit Size  index:102    from 3 To 0
        SetMemory(0x6621E4, Add, -33554432),# units:Unit Size  index:103    from 2 To 0
        SetMemory(0x6621E8, Add, -1),# units:Unit Size  index:104    from 1 To 0
        SetMemory(0x6621E8, Add, -196608),# units:Unit Size  index:106    from 3 To 0
        SetMemory(0x6621E8, Add, -50331648),# units:Unit Size  index:107    from 3 To 0
        SetMemory(0x6621EC, Add, -768),# units:Unit Size  index:109    from 3 To 0
        SetMemory(0x6621EC, Add, -196608),# units:Unit Size  index:110    from 3 To 0
        SetMemory(0x6621EC, Add, -50331648),# units:Unit Size  index:111    from 3 To 0
        SetMemory(0x6621F0, Add, -3),# units:Unit Size  index:112    from 3 To 0
        SetMemory(0x6621F0, Add, -768),# units:Unit Size  index:113    from 3 To 0
        SetMemory(0x6621F0, Add, -196608),# units:Unit Size  index:114    from 3 To 0
        SetMemory(0x6621F0, Add, -50331648),# units:Unit Size  index:115    from 3 To 0
        SetMemory(0x6621F4, Add, -3),# units:Unit Size  index:116    from 3 To 0
        SetMemory(0x6621F4, Add, -768),# units:Unit Size  index:117    from 3 To 0
        SetMemory(0x6621F4, Add, -196608),# units:Unit Size  index:118    from 3 To 0
        SetMemory(0x6621F8, Add, -3),# units:Unit Size  index:120    from 3 To 0
        SetMemory(0x6621F8, Add, -196608),# units:Unit Size  index:122    from 3 To 0
        SetMemory(0x6621F8, Add, -50331648),# units:Unit Size  index:123    from 3 To 0
        SetMemory(0x6621FC, Add, -3),# units:Unit Size  index:124    from 3 To 0
        SetMemory(0x6621FC, Add, -768),# units:Unit Size  index:125    from 3 To 0
        SetMemory(0x6621FC, Add, -196608),# units:Unit Size  index:126    from 3 To 0
        SetMemory(0x6621FC, Add, -50331648),# units:Unit Size  index:127    from 3 To 0
        SetMemory(0x662200, Add, -196608),# units:Unit Size  index:130    from 3 To 0
        SetMemory(0x662200, Add, -50331648),# units:Unit Size  index:131    from 3 To 0
        SetMemory(0x662204, Add, -3),# units:Unit Size  index:132    from 3 To 0
        SetMemory(0x662204, Add, -768),# units:Unit Size  index:133    from 3 To 0
        SetMemory(0x662204, Add, -196608),# units:Unit Size  index:134    from 3 To 0
        SetMemory(0x662204, Add, -50331648),# units:Unit Size  index:135    from 3 To 0
        SetMemory(0x662208, Add, -3),# units:Unit Size  index:136    from 3 To 0
        SetMemory(0x662208, Add, -768),# units:Unit Size  index:137    from 3 To 0
        SetMemory(0x662208, Add, -196608),# units:Unit Size  index:138    from 3 To 0
        SetMemory(0x662208, Add, -50331648),# units:Unit Size  index:139    from 3 To 0
        SetMemory(0x66220C, Add, -3),# units:Unit Size  index:140    from 3 To 0
        SetMemory(0x66220C, Add, -768),# units:Unit Size  index:141    from 3 To 0
        SetMemory(0x66220C, Add, -196608),# units:Unit Size  index:142    from 3 To 0
        SetMemory(0x66220C, Add, -50331648),# units:Unit Size  index:143    from 3 To 0
        SetMemory(0x662210, Add, -3),# units:Unit Size  index:144    from 3 To 0
        SetMemory(0x662210, Add, -196608),# units:Unit Size  index:146    from 3 To 0
        SetMemory(0x662210, Add, -50331648),# units:Unit Size  index:147    from 3 To 0
        SetMemory(0x662214, Add, -3),# units:Unit Size  index:148    from 3 To 0
        SetMemory(0x662214, Add, -768),# units:Unit Size  index:149    from 3 To 0
        SetMemory(0x662214, Add, -196608),# units:Unit Size  index:150    from 3 To 0
        SetMemory(0x662214, Add, -50331648),# units:Unit Size  index:151    from 3 To 0
        SetMemory(0x662218, Add, -3),# units:Unit Size  index:152    from 3 To 0
        SetMemory(0x662218, Add, -196608),# units:Unit Size  index:154    from 3 To 0
        SetMemory(0x662218, Add, -50331648),# units:Unit Size  index:155    from 3 To 0
        SetMemory(0x66221C, Add, -3),# units:Unit Size  index:156    from 3 To 0
        SetMemory(0x66221C, Add, -768),# units:Unit Size  index:157    from 3 To 0
        SetMemory(0x66221C, Add, -50331648),# units:Unit Size  index:159    from 3 To 0
        SetMemory(0x662220, Add, -3),# units:Unit Size  index:160    from 3 To 0
        SetMemory(0x662220, Add, -196608),# units:Unit Size  index:162    from 3 To 0
        SetMemory(0x662220, Add, -50331648),# units:Unit Size  index:163    from 3 To 0
        SetMemory(0x662224, Add, -3),# units:Unit Size  index:164    from 3 To 0
        SetMemory(0x662224, Add, -768),# units:Unit Size  index:165    from 3 To 0
        SetMemory(0x662224, Add, -196608),# units:Unit Size  index:166    from 3 To 0
        SetMemory(0x662224, Add, -50331648),# units:Unit Size  index:167    from 3 To 0
        SetMemory(0x662228, Add, -3),# units:Unit Size  index:168    from 3 To 0
        SetMemory(0x662228, Add, -768),# units:Unit Size  index:169    from 3 To 0
        SetMemory(0x662228, Add, -196608),# units:Unit Size  index:170    from 3 To 0
        SetMemory(0x662228, Add, -50331648),# units:Unit Size  index:171    from 3 To 0
        SetMemory(0x66222C, Add, -3),# units:Unit Size  index:172    from 3 To 0
        SetMemory(0x66222C, Add, -768),# units:Unit Size  index:173    from 3 To 0
        SetMemory(0x66222C, Add, -196608),# units:Unit Size  index:174    from 3 To 0
        SetMemory(0x66222C, Add, -50331648),# units:Unit Size  index:175    from 3 To 0
        SetMemory(0x66223C, Add, -768),# units:Unit Size  index:189    from 3 To 0
        SetMemory(0x66223C, Add, -196608),# units:Unit Size  index:190    from 3 To 0
        SetMemory(0x662248, Add, -3),# units:Unit Size  index:200    from 3 To 0
        SetMemory(0x662248, Add, -768),# units:Unit Size  index:201    from 3 To 0
        SetMemory(0x65FED0, Add, -256),# units:Armor  index:9    from 1 To 0
        SetMemory(0x65FED0, Add, -196608),# units:Armor  index:10    from 3 To 0
        SetMemory(0x65FED0, Add, -16777216),# units:Armor  index:11    from 1 To 0
        SetMemory(0x65FED4, Add, -3),# units:Armor  index:12    from 3 To 0
        SetMemory(0x65FED8, Add, -3),# units:Armor  index:16    from 3 To 0
        SetMemory(0x65FED8, Add, -50331648),# units:Armor  index:19    from 3 To 0
        SetMemory(0x65FEDC, Add, -3),# units:Armor  index:20    from 3 To 0
        SetMemory(0x65FEDC, Add, -1024),# units:Armor  index:21    from 4 To 0
        SetMemory(0x65FEDC, Add, -262144),# units:Armor  index:22    from 4 To 0
        SetMemory(0x65FEE0, Add, -67108864),# units:Armor  index:27    from 4 To 0
        SetMemory(0x65FEE4, Add, -4),# units:Armor  index:28    from 4 To 0
        SetMemory(0x65FEE4, Add, -1024),# units:Armor  index:29    from 4 To 0
        SetMemory(0x65FEE8, Add, -1),# units:Armor  index:32    from 1 To 0
        SetMemory(0x65FEE8, Add, -65536),# units:Armor  index:34    from 1 To 0
        SetMemory(0x65FEEC, Add, -16777216),# units:Armor  index:39    from 1 To 0
        SetMemory(0x65FEF4, Add, -2),# units:Armor  index:44    from 2 To 0
        SetMemory(0x65FEF4, Add, -65536),# units:Armor  index:46    from 1 To 0
        SetMemory(0x65FEF8, Add, -4),# units:Armor  index:48    from 4 To 0
        SetMemory(0x65FEF8, Add, -768),# units:Armor  index:49    from 3 To 0
        SetMemory(0x65FEF8, Add, -33554432),# units:Armor  index:51    from 2 To 0
        SetMemory(0x65FEFC, Add, -3),# units:Armor  index:52    from 3 To 0
        SetMemory(0x65FEFC, Add, -512),# units:Armor  index:53    from 2 To 0
        SetMemory(0x65FEFC, Add, -196608),# units:Armor  index:54    from 3 To 0
        SetMemory(0x65FEFC, Add, -50331648),# units:Armor  index:55    from 3 To 0
        SetMemory(0x65FF00, Add, -4),# units:Armor  index:56    from 4 To 0
        SetMemory(0x65FF00, Add, -1024),# units:Armor  index:57    from 4 To 0
        SetMemory(0x65FF04, Add, -1),# units:Armor  index:60    from 1 To 0
        SetMemory(0x65FF04, Add, -256),# units:Armor  index:61    from 1 To 0
        SetMemory(0x65FF04, Add, -131072),# units:Armor  index:62    from 2 To 0
        SetMemory(0x65FF04, Add, -16777216),# units:Armor  index:63    from 1 To 0
        SetMemory(0x65FF08, Add, -256),# units:Armor  index:65    from 1 To 0
        SetMemory(0x65FF08, Add, -65536),# units:Armor  index:66    from 1 To 0
        SetMemory(0x65FF0C, Add, -256),# units:Armor  index:69    from 1 To 0
        SetMemory(0x65FF0C, Add, -16777216),# units:Armor  index:71    from 1 To 0
        SetMemory(0x65FF10, Add, -4),# units:Armor  index:72    from 4 To 0
        SetMemory(0x65FF14, Add, -3),# units:Armor  index:76    from 3 To 0
        SetMemory(0x65FF14, Add, -512),# units:Armor  index:77    from 2 To 0
        SetMemory(0x65FF14, Add, -196608),# units:Armor  index:78    from 3 To 0
        SetMemory(0x65FF14, Add, -33554432),# units:Armor  index:79    from 2 To 0
        SetMemory(0x65FF18, Add, -3),# units:Armor  index:80    from 3 To 0
        SetMemory(0x65FF18, Add, -768),# units:Armor  index:81    from 3 To 0
        SetMemory(0x65FF18, Add, -262144),# units:Armor  index:82    from 4 To 0
        SetMemory(0x65FF1C, Add, -196608),# units:Armor  index:86    from 3 To 0
        SetMemory(0x65FF1C, Add, -33554432),# units:Armor  index:87    from 2 To 0
        SetMemory(0x65FF20, Add, -3),# units:Armor  index:88    from 3 To 0
        SetMemory(0x65FF28, Add, -33554432),# units:Armor  index:99    from 2 To 0
        SetMemory(0x65FF2C, Add, -3),# units:Armor  index:100    from 3 To 0
        SetMemory(0x65FF2C, Add, -262144),# units:Armor  index:102    from 4 To 0
        SetMemory(0x65FF2C, Add, -16777216),# units:Armor  index:103    from 1 To 0
        SetMemory(0x65FF30, Add, -3),# units:Armor  index:104    from 3 To 0
        SetMemory(0x65FF30, Add, -65536),# units:Armor  index:106    from 1 To 0
        SetMemory(0x65FF30, Add, -16777216),# units:Armor  index:107    from 1 To 0
        SetMemory(0x65FF34, Add, -256),# units:Armor  index:109    from 1 To 0
        SetMemory(0x65FF34, Add, -65536),# units:Armor  index:110    from 1 To 0
        SetMemory(0x65FF34, Add, -16777216),# units:Armor  index:111    from 1 To 0
        SetMemory(0x65FF38, Add, -1),# units:Armor  index:112    from 1 To 0
        SetMemory(0x65FF38, Add, -256),# units:Armor  index:113    from 1 To 0
        SetMemory(0x65FF38, Add, -65536),# units:Armor  index:114    from 1 To 0
        SetMemory(0x65FF38, Add, -16777216),# units:Armor  index:115    from 1 To 0
        SetMemory(0x65FF3C, Add, -1),# units:Armor  index:116    from 1 To 0
        SetMemory(0x65FF3C, Add, -256),# units:Armor  index:117    from 1 To 0
        SetMemory(0x65FF3C, Add, -65536),# units:Armor  index:118    from 1 To 0
        SetMemory(0x65FF40, Add, -1),# units:Armor  index:120    from 1 To 0
        SetMemory(0x65FF40, Add, -65536),# units:Armor  index:122    from 1 To 0
        SetMemory(0x65FF40, Add, -16777216),# units:Armor  index:123    from 1 To 0
        SetMemory(0x65FF44, Add, -256),# units:Armor  index:125    from 1 To 0
        SetMemory(0x65FF44, Add, -65536),# units:Armor  index:126    from 1 To 0
        SetMemory(0x65FF44, Add, -16777216),# units:Armor  index:127    from 1 To 0
        SetMemory(0x65FF48, Add, -65536),# units:Armor  index:130    from 1 To 0
        SetMemory(0x65FF48, Add, -16777216),# units:Armor  index:131    from 1 To 0
        SetMemory(0x65FF4C, Add, -1),# units:Armor  index:132    from 1 To 0
        SetMemory(0x65FF4C, Add, -256),# units:Armor  index:133    from 1 To 0
        SetMemory(0x65FF4C, Add, -65536),# units:Armor  index:134    from 1 To 0
        SetMemory(0x65FF4C, Add, -16777216),# units:Armor  index:135    from 1 To 0
        SetMemory(0x65FF50, Add, -1),# units:Armor  index:136    from 1 To 0
        SetMemory(0x65FF50, Add, -256),# units:Armor  index:137    from 1 To 0
        SetMemory(0x65FF50, Add, -65536),# units:Armor  index:138    from 1 To 0
        SetMemory(0x65FF50, Add, -16777216),# units:Armor  index:139    from 1 To 0
        SetMemory(0x65FF54, Add, -1),# units:Armor  index:140    from 1 To 0
        SetMemory(0x65FF54, Add, -256),# units:Armor  index:141    from 1 To 0
        SetMemory(0x65FF54, Add, -65536),# units:Armor  index:142    from 1 To 0
        SetMemory(0x65FF58, Add, -131072),# units:Armor  index:146    from 2 To 0
        SetMemory(0x65FF58, Add, -16777216),# units:Armor  index:147    from 1 To 0
        SetMemory(0x65FF5C, Add, -1),# units:Armor  index:148    from 1 To 0
        SetMemory(0x65FF5C, Add, -256),# units:Armor  index:149    from 1 To 0
        SetMemory(0x65FF5C, Add, -65536),# units:Armor  index:150    from 1 To 0
        SetMemory(0x65FF5C, Add, -16777216),# units:Armor  index:151    from 1 To 0
        SetMemory(0x65FF60, Add, -1),# units:Armor  index:152    from 1 To 0
        SetMemory(0x65FF60, Add, -65536),# units:Armor  index:154    from 1 To 0
        SetMemory(0x65FF60, Add, -16777216),# units:Armor  index:155    from 1 To 0
        SetMemory(0x65FF64, Add, -256),# units:Armor  index:157    from 1 To 0
        SetMemory(0x65FF64, Add, -16777216),# units:Armor  index:159    from 1 To 0
        SetMemory(0x65FF68, Add, -1),# units:Armor  index:160    from 1 To 0
        SetMemory(0x65FF68, Add, -16777216),# units:Armor  index:163    from 1 To 0
        SetMemory(0x65FF6C, Add, -1),# units:Armor  index:164    from 1 To 0
        SetMemory(0x65FF6C, Add, -256),# units:Armor  index:165    from 1 To 0
        SetMemory(0x65FF6C, Add, -65536),# units:Armor  index:166    from 1 To 0
        SetMemory(0x65FF6C, Add, -16777216),# units:Armor  index:167    from 1 To 0
        SetMemory(0x65FF70, Add, -1),# units:Armor  index:168    from 1 To 0
        SetMemory(0x65FF70, Add, -256),# units:Armor  index:169    from 1 To 0
        SetMemory(0x65FF70, Add, -65536),# units:Armor  index:170    from 1 To 0
        SetMemory(0x65FF70, Add, -16777216),# units:Armor  index:171    from 1 To 0
        SetMemory(0x65FF74, Add, -1),# units:Armor  index:172    from 1 To 0
        SetMemory(0x65FF74, Add, -256),# units:Armor  index:173    from 1 To 0
        SetMemory(0x65FF74, Add, -65536),# units:Armor  index:174    from 1 To 0
        SetMemory(0x65FF74, Add, -16777216),# units:Armor  index:175    from 1 To 0
        SetMemory(0x65FF84, Add, -256),# units:Armor  index:189    from 1 To 0
        SetMemory(0x65FF84, Add, -65536),# units:Armor  index:190    from 1 To 0
        SetMemory(0x65FF90, Add, -1),# units:Armor  index:200    from 1 To 0
        SetMemory(0x65FF90, Add, -256),# units:Armor  index:201    from 1 To 0
        SetMemory(0x662098, Add, -256),# units:Right-click Action  index:1    from 1 To 0
        SetMemory(0x662098, Add, -65536),# units:Right-click Action  index:2    from 1 To 0
        SetMemory(0x66209C, Add, -83886080),# units:Right-click Action  index:7    from 5 To 0
        SetMemory(0x6620A0, Add, -1),# units:Right-click Action  index:8    from 1 To 0
        SetMemory(0x6620A0, Add, -512),# units:Right-click Action  index:9    from 2 To 0
        SetMemory(0x6620A0, Add, -65536),# units:Right-click Action  index:10    from 1 To 0
        SetMemory(0x6620A0, Add, -33554432),# units:Right-click Action  index:11    from 2 To 0
        SetMemory(0x6620A4, Add, -1),# units:Right-click Action  index:12    from 1 To 0
        SetMemory(0x6620A8, Add, -1),# units:Right-click Action  index:16    from 1 To 0
        SetMemory(0x6620A8, Add, -16777216),# units:Right-click Action  index:19    from 1 To 0
        SetMemory(0x6620AC, Add, -1),# units:Right-click Action  index:20    from 1 To 0
        SetMemory(0x6620AC, Add, -256),# units:Right-click Action  index:21    from 1 To 0
        SetMemory(0x6620AC, Add, -131072),# units:Right-click Action  index:22    from 2 To 0
        SetMemory(0x6620B0, Add, -16777216),# units:Right-click Action  index:27    from 1 To 0
        SetMemory(0x6620B4, Add, -1),# units:Right-click Action  index:28    from 1 To 0
        SetMemory(0x6620B4, Add, -256),# units:Right-click Action  index:29    from 1 To 0
        SetMemory(0x6620B8, Add, -1),# units:Right-click Action  index:32    from 1 To 0
        SetMemory(0x6620B8, Add, -131072),# units:Right-click Action  index:34    from 2 To 0
        SetMemory(0x6620BC, Add, -256),# units:Right-click Action  index:37    from 1 To 0
        SetMemory(0x6620BC, Add, -65536),# units:Right-click Action  index:38    from 1 To 0
        SetMemory(0x6620BC, Add, -16777216),# units:Right-click Action  index:39    from 1 To 0
        SetMemory(0x6620C0, Add, -1),# units:Right-click Action  index:40    from 1 To 0
        SetMemory(0x6620C0, Add, -1024),# units:Right-click Action  index:41    from 4 To 0
        SetMemory(0x6620C0, Add, -131072),# units:Right-click Action  index:42    from 2 To 0
        SetMemory(0x6620C0, Add, -16777216),# units:Right-click Action  index:43    from 1 To 0
        SetMemory(0x6620C4, Add, -1),# units:Right-click Action  index:44    from 1 To 0
        SetMemory(0x6620C4, Add, -512),# units:Right-click Action  index:45    from 2 To 0
        SetMemory(0x6620C4, Add, -131072),# units:Right-click Action  index:46    from 2 To 0
        SetMemory(0x6620C4, Add, -16777216),# units:Right-click Action  index:47    from 1 To 0
        SetMemory(0x6620C8, Add, -1),# units:Right-click Action  index:48    from 1 To 0
        SetMemory(0x6620C8, Add, -512),# units:Right-click Action  index:49    from 2 To 0
        SetMemory(0x6620C8, Add, -65536),# units:Right-click Action  index:50    from 1 To 0
        SetMemory(0x6620C8, Add, -16777216),# units:Right-click Action  index:51    from 1 To 0
        SetMemory(0x6620CC, Add, -2),# units:Right-click Action  index:52    from 2 To 0
        SetMemory(0x6620CC, Add, -256),# units:Right-click Action  index:53    from 1 To 0
        SetMemory(0x6620CC, Add, -65536),# units:Right-click Action  index:54    from 1 To 0
        SetMemory(0x6620CC, Add, -16777216),# units:Right-click Action  index:55    from 1 To 0
        SetMemory(0x6620D0, Add, -1),# units:Right-click Action  index:56    from 1 To 0
        SetMemory(0x6620D0, Add, -512),# units:Right-click Action  index:57    from 2 To 0
        SetMemory(0x6620D4, Add, -1),# units:Right-click Action  index:60    from 1 To 0
        SetMemory(0x6620D4, Add, -256),# units:Right-click Action  index:61    from 1 To 0
        SetMemory(0x6620D4, Add, -65536),# units:Right-click Action  index:62    from 1 To 0
        SetMemory(0x6620D4, Add, -33554432),# units:Right-click Action  index:63    from 2 To 0
        SetMemory(0x6620D8, Add, -4),# units:Right-click Action  index:64    from 4 To 0
        SetMemory(0x6620D8, Add, -256),# units:Right-click Action  index:65    from 1 To 0
        SetMemory(0x6620D8, Add, -65536),# units:Right-click Action  index:66    from 1 To 0
        SetMemory(0x6620D8, Add, -33554432),# units:Right-click Action  index:67    from 2 To 0
        SetMemory(0x6620DC, Add, -1),# units:Right-click Action  index:68    from 1 To 0
        SetMemory(0x6620DC, Add, -512),# units:Right-click Action  index:69    from 2 To 0
        SetMemory(0x6620DC, Add, -65536),# units:Right-click Action  index:70    from 1 To 0
        SetMemory(0x6620DC, Add, -16777216),# units:Right-click Action  index:71    from 1 To 0
        SetMemory(0x6620E0, Add, -1),# units:Right-click Action  index:72    from 1 To 0
        SetMemory(0x6620E0, Add, -65536),# units:Right-click Action  index:74    from 1 To 0
        SetMemory(0x6620E0, Add, -16777216),# units:Right-click Action  index:75    from 1 To 0
        SetMemory(0x6620E4, Add, -1),# units:Right-click Action  index:76    from 1 To 0
        SetMemory(0x6620E4, Add, -256),# units:Right-click Action  index:77    from 1 To 0
        SetMemory(0x6620E4, Add, -65536),# units:Right-click Action  index:78    from 1 To 0
        SetMemory(0x6620E4, Add, -16777216),# units:Right-click Action  index:79    from 1 To 0
        SetMemory(0x6620E8, Add, -1),# units:Right-click Action  index:80    from 1 To 0
        SetMemory(0x6620E8, Add, -256),# units:Right-click Action  index:81    from 1 To 0
        SetMemory(0x6620E8, Add, -65536),# units:Right-click Action  index:82    from 1 To 0
        SetMemory(0x6620E8, Add, -16777216),# units:Right-click Action  index:83    from 1 To 0
        SetMemory(0x6620EC, Add, -2),# units:Right-click Action  index:84    from 2 To 0
        SetMemory(0x6620EC, Add, -65536),# units:Right-click Action  index:86    from 1 To 0
        SetMemory(0x6620EC, Add, -16777216),# units:Right-click Action  index:87    from 1 To 0
        SetMemory(0x6620F0, Add, -1),# units:Right-click Action  index:88    from 1 To 0
        SetMemory(0x6620F0, Add, -512),# units:Right-click Action  index:89    from 2 To 0
        SetMemory(0x6620F0, Add, -131072),# units:Right-click Action  index:90    from 2 To 0
        SetMemory(0x6620F4, Add, -512),# units:Right-click Action  index:93    from 2 To 0
        SetMemory(0x6620F4, Add, -131072),# units:Right-click Action  index:94    from 2 To 0
        SetMemory(0x6620F4, Add, -33554432),# units:Right-click Action  index:95    from 2 To 0
        SetMemory(0x6620F8, Add, -2),# units:Right-click Action  index:96    from 2 To 0
        SetMemory(0x6620F8, Add, -65536),# units:Right-click Action  index:98    from 1 To 0
        SetMemory(0x6620F8, Add, -16777216),# units:Right-click Action  index:99    from 1 To 0
        SetMemory(0x6620FC, Add, -1),# units:Right-click Action  index:100    from 1 To 0
        SetMemory(0x6620FC, Add, -65536),# units:Right-click Action  index:102    from 1 To 0
        SetMemory(0x6620FC, Add, -33554432),# units:Right-click Action  index:103    from 2 To 0
        SetMemory(0x662100, Add, -1),# units:Right-click Action  index:104    from 1 To 0
        SetMemory(0x662100, Add, -131072),# units:Right-click Action  index:106    from 2 To 0
        SetMemory(0x662100, Add, -100663296),# units:Right-click Action  index:107    from 6 To 0
        SetMemory(0x662104, Add, -33554432),# units:Right-click Action  index:111    from 2 To 0
        SetMemory(0x662108, Add, -512),# units:Right-click Action  index:113    from 2 To 0
        SetMemory(0x662108, Add, -131072),# units:Right-click Action  index:114    from 2 To 0
        SetMemory(0x66210C, Add, -2),# units:Right-click Action  index:116    from 2 To 0
        SetMemory(0x662110, Add, -131072),# units:Right-click Action  index:122    from 2 To 0
        SetMemory(0x662114, Add, -3),# units:Right-click Action  index:124    from 3 To 0
        SetMemory(0x662118, Add, -131072),# units:Right-click Action  index:130    from 2 To 0
        SetMemory(0x662128, Add, -3),# units:Right-click Action  index:144    from 3 To 0
        SetMemory(0x662128, Add, -196608),# units:Right-click Action  index:146    from 3 To 0
        SetMemory(0x662138, Add, -196608),# units:Right-click Action  index:162    from 3 To 0
        SetMemory(0x661FC0, Add, -14745600),# units:Ready Sound  index:1    from 225 To 0
        SetMemory(0x661FC4, Add, -352),# units:Ready Sound  index:2    from 352 To 0
        SetMemory(0x661FCC, Add, -24117248),# units:Ready Sound  index:7    from 368 To 0
        SetMemory(0x661FD0, Add, -256),# units:Ready Sound  index:8    from 256 To 0
        SetMemory(0x661FD0, Add, -21757952),# units:Ready Sound  index:9    from 332 To 0
        SetMemory(0x661FD4, Add, -295),# units:Ready Sound  index:10    from 295 To 0
        SetMemory(0x661FD4, Add, -13697024),# units:Ready Sound  index:11    from 209 To 0
        SetMemory(0x661FD8, Add, -176),# units:Ready Sound  index:12    from 176 To 0
        SetMemory(0x661FE8, Add, -16777216),# units:Ready Sound  index:21    from 256 To 0
        SetMemory(0x661FEC, Add, -332),# units:Ready Sound  index:22    from 332 To 0
        SetMemory(0x662000, Add, -295),# units:Ready Sound  index:32    from 295 To 0
        SetMemory(0x662004, Add, -999),# units:Ready Sound  index:34    from 999 To 0
        SetMemory(0x662008, Add, -58982400),# units:Ready Sound  index:37    from 900 To 0
        SetMemory(0x66200C, Add, -866),# units:Ready Sound  index:38    from 866 To 0
        SetMemory(0x66200C, Add, -57802752),# units:Ready Sound  index:39    from 882 To 0
        SetMemory(0x662010, Add, -787),# units:Ready Sound  index:40    from 787 To 0
        SetMemory(0x662010, Add, -54525952),# units:Ready Sound  index:41    from 832 To 0
        SetMemory(0x662014, Add, -909),# units:Ready Sound  index:42    from 909 To 0
        SetMemory(0x662014, Add, -61669376),# units:Ready Sound  index:43    from 941 To 0
        SetMemory(0x662018, Add, -857),# units:Ready Sound  index:44    from 857 To 0
        SetMemory(0x662018, Add, -60817408),# units:Ready Sound  index:45    from 928 To 0
        SetMemory(0x66201C, Add, -814),# units:Ready Sound  index:46    from 814 To 0
        SetMemory(0x66201C, Add, -50790400),# units:Ready Sound  index:47    from 775 To 0
        SetMemory(0x662020, Add, -882),# units:Ready Sound  index:48    from 882 To 0
        SetMemory(0x662020, Add, -60817408),# units:Ready Sound  index:49    from 928 To 0
        SetMemory(0x662024, Add, -800),# units:Ready Sound  index:50    from 800 To 0
        SetMemory(0x662028, Add, -814),# units:Ready Sound  index:52    from 814 To 0
        SetMemory(0x662028, Add, -56754176),# units:Ready Sound  index:53    from 866 To 0
        SetMemory(0x66202C, Add, -900),# units:Ready Sound  index:54    from 900 To 0
        SetMemory(0x66202C, Add, -61669376),# units:Ready Sound  index:55    from 941 To 0
        SetMemory(0x662030, Add, -857),# units:Ready Sound  index:56    from 857 To 0
        SetMemory(0x662030, Add, -59572224),# units:Ready Sound  index:57    from 909 To 0
        SetMemory(0x662038, Add, -1041),# units:Ready Sound  index:60    from 1041 To 0
        SetMemory(0x662038, Add, -47710208),# units:Ready Sound  index:61    from 728 To 0
        SetMemory(0x66203C, Add, -1096),# units:Ready Sound  index:62    from 1096 To 0
        SetMemory(0x66203C, Add, -69795840),# units:Ready Sound  index:63    from 1065 To 0
        SetMemory(0x662040, Add, -597),# units:Ready Sound  index:64    from 597 To 0
        SetMemory(0x662040, Add, -43646976),# units:Ready Sound  index:65    from 666 To 0
        SetMemory(0x662044, Add, -492),# units:Ready Sound  index:66    from 492 To 0
        SetMemory(0x662044, Add, -40763392),# units:Ready Sound  index:67    from 622 To 0
        SetMemory(0x662048, Add, -567),# units:Ready Sound  index:68    from 567 To 0
        SetMemory(0x662048, Add, -33619968),# units:Ready Sound  index:69    from 513 To 0
        SetMemory(0x66204C, Add, -534),# units:Ready Sound  index:70    from 534 To 0
        SetMemory(0x66204C, Add, -35979264),# units:Ready Sound  index:71    from 549 To 0
        SetMemory(0x662050, Add, -582),# units:Ready Sound  index:72    from 582 To 0
        SetMemory(0x662054, Add, -728),# units:Ready Sound  index:74    from 728 To 0
        SetMemory(0x662058, Add, -567),# units:Ready Sound  index:76    from 567 To 0
        SetMemory(0x662060, Add, -534),# units:Ready Sound  index:80    from 534 To 0
        SetMemory(0x662060, Add, -41746432),# units:Ready Sound  index:81    from 637 To 0
        SetMemory(0x662064, Add, -41746432),# units:Ready Sound  index:83    from 637 To 0
        SetMemory(0x662068, Add, -650),# units:Ready Sound  index:84    from 650 To 0
        SetMemory(0x66206C, Add, -549),# units:Ready Sound  index:86    from 549 To 0
        SetMemory(0x66208C, Add, -70713344),# units:Ready Sound  index:103    from 1079 To 0
        SetMemory(0x65FFB0, Add, -15073280),# units:What Sound Start  index:1    from 230 To 0
        SetMemory(0x65FFB4, Add, -360),# units:What Sound Start  index:2    from 360 To 0
        SetMemory(0x65FFBC, Add, -24707072),# units:What Sound Start  index:7    from 377 To 0
        SetMemory(0x65FFC0, Add, -265),# units:What Sound Start  index:8    from 265 To 0
        SetMemory(0x65FFC0, Add, -22282240),# units:What Sound Start  index:9    from 340 To 0
        SetMemory(0x65FFC4, Add, -299),# units:What Sound Start  index:10    from 299 To 0
        SetMemory(0x65FFC4, Add, -14090240),# units:What Sound Start  index:11    from 215 To 0
        SetMemory(0x65FFC8, Add, -185),# units:What Sound Start  index:12    from 185 To 0
        SetMemory(0x65FFD0, Add, -462),# units:What Sound Start  index:16    from 462 To 0
        SetMemory(0x65FFD4, Add, -27721728),# units:What Sound Start  index:19    from 423 To 0
        SetMemory(0x65FFD8, Add, -411),# units:What Sound Start  index:20    from 411 To 0
        SetMemory(0x65FFD8, Add, -17367040),# units:What Sound Start  index:21    from 265 To 0
        SetMemory(0x65FFDC, Add, -340),# units:What Sound Start  index:22    from 340 To 0
        SetMemory(0x65FFE4, Add, -29425664),# units:What Sound Start  index:27    from 449 To 0
        SetMemory(0x65FFE8, Add, -411),# units:What Sound Start  index:28    from 411 To 0
        SetMemory(0x65FFE8, Add, -29425664),# units:What Sound Start  index:29    from 449 To 0
        SetMemory(0x65FFF0, Add, -299),# units:What Sound Start  index:32    from 299 To 0
        SetMemory(0x65FFF4, Add, -1001),# units:What Sound Start  index:34    from 1001 To 0
        SetMemory(0x65FFF8, Add, -59047936),# units:What Sound Start  index:37    from 901 To 0
        SetMemory(0x65FFFC, Add, -870),# units:What Sound Start  index:38    from 870 To 0
        SetMemory(0x65FFFC, Add, -58064896),# units:What Sound Start  index:39    from 886 To 0
        SetMemory(0x660000, Add, -792),# units:What Sound Start  index:40    from 792 To 0
        SetMemory(0x660000, Add, -54853632),# units:What Sound Start  index:41    from 837 To 0
        SetMemory(0x660004, Add, -912),# units:What Sound Start  index:42    from 912 To 0
        SetMemory(0x660004, Add, -62062592),# units:What Sound Start  index:43    from 947 To 0
        SetMemory(0x660008, Add, -858),# units:What Sound Start  index:44    from 858 To 0
        SetMemory(0x660008, Add, -61145088),# units:What Sound Start  index:45    from 933 To 0
        SetMemory(0x66000C, Add, -821),# units:What Sound Start  index:46    from 821 To 0
        SetMemory(0x66000C, Add, -51183616),# units:What Sound Start  index:47    from 781 To 0
        SetMemory(0x660010, Add, -886),# units:What Sound Start  index:48    from 886 To 0
        SetMemory(0x660010, Add, -61145088),# units:What Sound Start  index:49    from 933 To 0
        SetMemory(0x660014, Add, -805),# units:What Sound Start  index:50    from 805 To 0
        SetMemory(0x660014, Add, -62849024),# units:What Sound Start  index:51    from 959 To 0
        SetMemory(0x660018, Add, -821),# units:What Sound Start  index:52    from 821 To 0
        SetMemory(0x660018, Add, -57016320),# units:What Sound Start  index:53    from 870 To 0
        SetMemory(0x66001C, Add, -901),# units:What Sound Start  index:54    from 901 To 0
        SetMemory(0x66001C, Add, -62062592),# units:What Sound Start  index:55    from 947 To 0
        SetMemory(0x660020, Add, -858),# units:What Sound Start  index:56    from 858 To 0
        SetMemory(0x660020, Add, -59768832),# units:What Sound Start  index:57    from 912 To 0
        SetMemory(0x660028, Add, -1044),# units:What Sound Start  index:60    from 1044 To 0
        SetMemory(0x660028, Add, -48037888),# units:What Sound Start  index:61    from 733 To 0
        SetMemory(0x66002C, Add, -1101),# units:What Sound Start  index:62    from 1101 To 0
        SetMemory(0x66002C, Add, -70189056),# units:What Sound Start  index:63    from 1071 To 0
        SetMemory(0x660030, Add, -606),# units:What Sound Start  index:64    from 606 To 0
        SetMemory(0x660030, Add, -43909120),# units:What Sound Start  index:65    from 670 To 0
        SetMemory(0x660034, Add, -498),# units:What Sound Start  index:66    from 498 To 0
        SetMemory(0x660034, Add, -41091072),# units:What Sound Start  index:67    from 627 To 0
        SetMemory(0x660038, Add, -573),# units:What Sound Start  index:68    from 573 To 0
        SetMemory(0x660038, Add, -34078720),# units:What Sound Start  index:69    from 520 To 0
        SetMemory(0x66003C, Add, -540),# units:What Sound Start  index:70    from 540 To 0
        SetMemory(0x66003C, Add, -36634624),# units:What Sound Start  index:71    from 559 To 0
        SetMemory(0x660040, Add, -587),# units:What Sound Start  index:72    from 587 To 0
        SetMemory(0x660044, Add, -733),# units:What Sound Start  index:74    from 733 To 0
        SetMemory(0x660044, Add, -48889856),# units:What Sound Start  index:75    from 746 To 0
        SetMemory(0x660048, Add, -573),# units:What Sound Start  index:76    from 573 To 0
        SetMemory(0x660048, Add, -45547520),# units:What Sound Start  index:77    from 695 To 0
        SetMemory(0x66004C, Add, -683),# units:What Sound Start  index:78    from 683 To 0
        SetMemory(0x66004C, Add, -47120384),# units:What Sound Start  index:79    from 719 To 0
        SetMemory(0x660050, Add, -540),# units:What Sound Start  index:80    from 540 To 0
        SetMemory(0x660050, Add, -42074112),# units:What Sound Start  index:81    from 642 To 0
        SetMemory(0x660054, Add, -707),# units:What Sound Start  index:82    from 707 To 0
        SetMemory(0x660054, Add, -42074112),# units:What Sound Start  index:83    from 642 To 0
        SetMemory(0x660058, Add, -658),# units:What Sound Start  index:84    from 658 To 0
        SetMemory(0x66005C, Add, -559),# units:What Sound Start  index:86    from 559 To 0
        SetMemory(0x660060, Add, -1136),# units:What Sound Start  index:88    from 1136 To 0
        SetMemory(0x660060, Add, -3538944),# units:What Sound Start  index:89    from 54 To 0
        SetMemory(0x660064, Add, -46),# units:What Sound Start  index:90    from 46 To 0
        SetMemory(0x660068, Add, -63700992),# units:What Sound Start  index:93    from 972 To 0
        SetMemory(0x66006C, Add, -976),# units:What Sound Start  index:94    from 976 To 0
        SetMemory(0x66006C, Add, -3276800),# units:What Sound Start  index:95    from 50 To 0
        SetMemory(0x660070, Add, -968),# units:What Sound Start  index:96    from 968 To 0
        SetMemory(0x660074, Add, -1044),# units:What Sound Start  index:98    from 1044 To 0
        SetMemory(0x660074, Add, -64815104),# units:What Sound Start  index:99    from 989 To 0
        SetMemory(0x660078, Add, -230),# units:What Sound Start  index:100    from 230 To 0
        SetMemory(0x66007C, Add, -449),# units:What Sound Start  index:102    from 449 To 0
        SetMemory(0x66007C, Add, -71106560),# units:What Sound Start  index:103    from 1085 To 0
        SetMemory(0x660080, Add, -1121),# units:What Sound Start  index:104    from 1121 To 0
        SetMemory(0x660084, Add, -15),# units:What Sound Start  index:106    from 15 To 0
        SetMemory(0x660084, Add, -25362432),# units:What Sound Start  index:107    from 387 To 0
        SetMemory(0x660088, Add, -26017792),# units:What Sound Start  index:109    from 397 To 0
        SetMemory(0x66008C, Add, -400),# units:What Sound Start  index:110    from 400 To 0
        SetMemory(0x66008C, Add, -983040),# units:What Sound Start  index:111    from 15 To 0
        SetMemory(0x660090, Add, -385),# units:What Sound Start  index:112    from 385 To 0
        SetMemory(0x660090, Add, -983040),# units:What Sound Start  index:113    from 15 To 0
        SetMemory(0x660094, Add, -15),# units:What Sound Start  index:114    from 15 To 0
        SetMemory(0x660094, Add, -25493504),# units:What Sound Start  index:115    from 389 To 0
        SetMemory(0x660098, Add, -395),# units:What Sound Start  index:116    from 395 To 0
        SetMemory(0x660098, Add, -25559040),# units:What Sound Start  index:117    from 390 To 0
        SetMemory(0x66009C, Add, -398),# units:What Sound Start  index:118    from 398 To 0
        SetMemory(0x6600A0, Add, -392),# units:What Sound Start  index:120    from 392 To 0
        SetMemory(0x6600A4, Add, -402),# units:What Sound Start  index:122    from 402 To 0
        SetMemory(0x6600A4, Add, -25296896),# units:What Sound Start  index:123    from 386 To 0
        SetMemory(0x6600A8, Add, -393),# units:What Sound Start  index:124    from 393 To 0
        SetMemory(0x6600A8, Add, -983040),# units:What Sound Start  index:125    from 15 To 0
        SetMemory(0x6600AC, Add, -394),# units:What Sound Start  index:126    from 394 To 0
        SetMemory(0x6600AC, Add, -25624576),# units:What Sound Start  index:127    from 391 To 0
        SetMemory(0x6600B0, Add, -15),# units:What Sound Start  index:128    from 15 To 0
        SetMemory(0x6600B0, Add, -983040),# units:What Sound Start  index:129    from 15 To 0
        SetMemory(0x6600B4, Add, -15),# units:What Sound Start  index:130    from 15 To 0
        SetMemory(0x6600B4, Add, -49741824),# units:What Sound Start  index:131    from 759 To 0
        SetMemory(0x6600B8, Add, -762),# units:What Sound Start  index:132    from 762 To 0
        SetMemory(0x6600B8, Add, -49807360),# units:What Sound Start  index:133    from 760 To 0
        SetMemory(0x6600BC, Add, -768),# units:What Sound Start  index:134    from 768 To 0
        SetMemory(0x6600BC, Add, -50528256),# units:What Sound Start  index:135    from 771 To 0
        SetMemory(0x6600C0, Add, -766),# units:What Sound Start  index:136    from 766 To 0
        SetMemory(0x6600C0, Add, -50135040),# units:What Sound Start  index:137    from 765 To 0
        SetMemory(0x6600C4, Add, -767),# units:What Sound Start  index:138    from 767 To 0
        SetMemory(0x6600C4, Add, -49610752),# units:What Sound Start  index:139    from 757 To 0
        SetMemory(0x6600C8, Add, -770),# units:What Sound Start  index:140    from 770 To 0
        SetMemory(0x6600C8, Add, -50659328),# units:What Sound Start  index:141    from 773 To 0
        SetMemory(0x6600CC, Add, -755),# units:What Sound Start  index:142    from 755 To 0
        SetMemory(0x6600CC, Add, -49676288),# units:What Sound Start  index:143    from 758 To 0
        SetMemory(0x6600D0, Add, -772),# units:What Sound Start  index:144    from 772 To 0
        SetMemory(0x6600D4, Add, -763),# units:What Sound Start  index:146    from 763 To 0
        SetMemory(0x6600D4, Add, -50397184),# units:What Sound Start  index:147    from 769 To 0
        SetMemory(0x6600D8, Add, -769),# units:What Sound Start  index:148    from 769 To 0
        SetMemory(0x6600D8, Add, -49872896),# units:What Sound Start  index:149    from 761 To 0
        SetMemory(0x6600DC, Add, -764),# units:What Sound Start  index:150    from 764 To 0
        SetMemory(0x6600DC, Add, -49545216),# units:What Sound Start  index:151    from 756 To 0
        SetMemory(0x6600E0, Add, -756),# units:What Sound Start  index:152    from 756 To 0
        SetMemory(0x6600E4, Add, -484),# units:What Sound Start  index:154    from 484 To 0
        SetMemory(0x6600E4, Add, -31981568),# units:What Sound Start  index:155    from 488 To 0
        SetMemory(0x6600E8, Add, -487),# units:What Sound Start  index:156    from 487 To 0
        SetMemory(0x6600E8, Add, -31064064),# units:What Sound Start  index:157    from 474 To 0
        SetMemory(0x6600EC, Add, -31195136),# units:What Sound Start  index:159    from 476 To 0
        SetMemory(0x6600F0, Add, -479),# units:What Sound Start  index:160    from 479 To 0
        SetMemory(0x6600F4, Add, -485),# units:What Sound Start  index:162    from 485 To 0
        SetMemory(0x6600F4, Add, -31260672),# units:What Sound Start  index:163    from 477 To 0
        SetMemory(0x6600F8, Add, -480),# units:What Sound Start  index:164    from 480 To 0
        SetMemory(0x6600F8, Add, -30998528),# units:What Sound Start  index:165    from 473 To 0
        SetMemory(0x6600FC, Add, -478),# units:What Sound Start  index:166    from 478 To 0
        SetMemory(0x6600FC, Add, -983040),# units:What Sound Start  index:167    from 15 To 0
        SetMemory(0x660100, Add, -399),# units:What Sound Start  index:168    from 399 To 0
        SetMemory(0x660100, Add, -32178176),# units:What Sound Start  index:169    from 491 To 0
        SetMemory(0x660104, Add, -490),# units:What Sound Start  index:170    from 490 To 0
        SetMemory(0x660104, Add, -32047104),# units:What Sound Start  index:171    from 489 To 0
        SetMemory(0x660108, Add, -475),# units:What Sound Start  index:172    from 475 To 0
        SetMemory(0x660108, Add, -31588352),# units:What Sound Start  index:173    from 482 To 0
        SetMemory(0x66010C, Add, -486),# units:What Sound Start  index:174    from 486 To 0
        SetMemory(0x66010C, Add, -31850496),# units:What Sound Start  index:175    from 486 To 0
        SetMemory(0x660128, Add, -32178176),# units:What Sound Start  index:189    from 491 To 0
        SetMemory(0x66012C, Add, -391),# units:What Sound Start  index:190    from 391 To 0
        SetMemory(0x660134, Add, -15),# units:What Sound Start  index:194    from 15 To 0
        SetMemory(0x660134, Add, -983040),# units:What Sound Start  index:195    from 15 To 0
        SetMemory(0x660138, Add, -15),# units:What Sound Start  index:196    from 15 To 0
        SetMemory(0x660140, Add, -396),# units:What Sound Start  index:200    from 396 To 0
        SetMemory(0x660140, Add, -50397184),# units:What Sound Start  index:201    from 769 To 0
        SetMemory(0x66015C, Add, -983040),# units:What Sound Start  index:215    from 15 To 0
        SetMemory(0x660160, Add, -15),# units:What Sound Start  index:216    from 15 To 0
        SetMemory(0x660160, Add, -983040),# units:What Sound Start  index:217    from 15 To 0
        SetMemory(0x660164, Add, -15),# units:What Sound Start  index:218    from 15 To 0
        SetMemory(0x660164, Add, -983040),# units:What Sound Start  index:219    from 15 To 0
        SetMemory(0x660168, Add, -15),# units:What Sound Start  index:220    from 15 To 0
        SetMemory(0x660168, Add, -983040),# units:What Sound Start  index:221    from 15 To 0
        SetMemory(0x66016C, Add, -15),# units:What Sound Start  index:222    from 15 To 0
        SetMemory(0x66016C, Add, -983040),# units:What Sound Start  index:223    from 15 To 0
        SetMemory(0x662BF0, Add, -15269888),# units:What Sound End  index:1    from 233 To 0
        SetMemory(0x662BF4, Add, -363),# units:What Sound End  index:2    from 363 To 0
        SetMemory(0x662BFC, Add, -24903680),# units:What Sound End  index:7    from 380 To 0
        SetMemory(0x662C00, Add, -268),# units:What Sound End  index:8    from 268 To 0
        SetMemory(0x662C00, Add, -22478848),# units:What Sound End  index:9    from 343 To 0
        SetMemory(0x662C04, Add, -302),# units:What Sound End  index:10    from 302 To 0
        SetMemory(0x662C04, Add, -14286848),# units:What Sound End  index:11    from 218 To 0
        SetMemory(0x662C08, Add, -188),# units:What Sound End  index:12    from 188 To 0
        SetMemory(0x662C10, Add, -465),# units:What Sound End  index:16    from 465 To 0
        SetMemory(0x662C14, Add, -27918336),# units:What Sound End  index:19    from 426 To 0
        SetMemory(0x662C18, Add, -414),# units:What Sound End  index:20    from 414 To 0
        SetMemory(0x662C18, Add, -17563648),# units:What Sound End  index:21    from 268 To 0
        SetMemory(0x662C1C, Add, -343),# units:What Sound End  index:22    from 343 To 0
        SetMemory(0x662C24, Add, -29622272),# units:What Sound End  index:27    from 452 To 0
        SetMemory(0x662C28, Add, -414),# units:What Sound End  index:28    from 414 To 0
        SetMemory(0x662C28, Add, -29622272),# units:What Sound End  index:29    from 452 To 0
        SetMemory(0x662C30, Add, -302),# units:What Sound End  index:32    from 302 To 0
        SetMemory(0x662C34, Add, -1004),# units:What Sound End  index:34    from 1004 To 0
        SetMemory(0x662C38, Add, -59244544),# units:What Sound End  index:37    from 904 To 0
        SetMemory(0x662C3C, Add, -872),# units:What Sound End  index:38    from 872 To 0
        SetMemory(0x662C3C, Add, -57868288),# units:What Sound End  index:39    from 883 To 0
        SetMemory(0x662C40, Add, -795),# units:What Sound End  index:40    from 795 To 0
        SetMemory(0x662C40, Add, -55115776),# units:What Sound End  index:41    from 841 To 0
        SetMemory(0x662C44, Add, -915),# units:What Sound End  index:42    from 915 To 0
        SetMemory(0x662C44, Add, -62259200),# units:What Sound End  index:43    from 950 To 0
        SetMemory(0x662C48, Add, -861),# units:What Sound End  index:44    from 861 To 0
        SetMemory(0x662C48, Add, -61341696),# units:What Sound End  index:45    from 936 To 0
        SetMemory(0x662C4C, Add, -823),# units:What Sound End  index:46    from 823 To 0
        SetMemory(0x662C4C, Add, -51249152),# units:What Sound End  index:47    from 782 To 0
        SetMemory(0x662C50, Add, -883),# units:What Sound End  index:48    from 883 To 0
        SetMemory(0x662C50, Add, -61341696),# units:What Sound End  index:49    from 936 To 0
        SetMemory(0x662C54, Add, -808),# units:What Sound End  index:50    from 808 To 0
        SetMemory(0x662C54, Add, -63045632),# units:What Sound End  index:51    from 962 To 0
        SetMemory(0x662C58, Add, -823),# units:What Sound End  index:52    from 823 To 0
        SetMemory(0x662C58, Add, -57147392),# units:What Sound End  index:53    from 872 To 0
        SetMemory(0x662C5C, Add, -904),# units:What Sound End  index:54    from 904 To 0
        SetMemory(0x662C5C, Add, -62259200),# units:What Sound End  index:55    from 950 To 0
        SetMemory(0x662C60, Add, -861),# units:What Sound End  index:56    from 861 To 0
        SetMemory(0x662C60, Add, -59965440),# units:What Sound End  index:57    from 915 To 0
        SetMemory(0x662C68, Add, -1047),# units:What Sound End  index:60    from 1047 To 0
        SetMemory(0x662C68, Add, -48234496),# units:What Sound End  index:61    from 736 To 0
        SetMemory(0x662C6C, Add, -1103),# units:What Sound End  index:62    from 1103 To 0
        SetMemory(0x662C6C, Add, -70385664),# units:What Sound End  index:63    from 1074 To 0
        SetMemory(0x662C70, Add, -609),# units:What Sound End  index:64    from 609 To 0
        SetMemory(0x662C70, Add, -44105728),# units:What Sound End  index:65    from 673 To 0
        SetMemory(0x662C74, Add, -505),# units:What Sound End  index:66    from 505 To 0
        SetMemory(0x662C74, Add, -41287680),# units:What Sound End  index:67    from 630 To 0
        SetMemory(0x662C78, Add, -576),# units:What Sound End  index:68    from 576 To 0
        SetMemory(0x662C78, Add, -34275328),# units:What Sound End  index:69    from 523 To 0
        SetMemory(0x662C7C, Add, -543),# units:What Sound End  index:70    from 543 To 0
        SetMemory(0x662C7C, Add, -36831232),# units:What Sound End  index:71    from 562 To 0
        SetMemory(0x662C80, Add, -590),# units:What Sound End  index:72    from 590 To 0
        SetMemory(0x662C84, Add, -736),# units:What Sound End  index:74    from 736 To 0
        SetMemory(0x662C84, Add, -49086464),# units:What Sound End  index:75    from 749 To 0
        SetMemory(0x662C88, Add, -576),# units:What Sound End  index:76    from 576 To 0
        SetMemory(0x662C88, Add, -45744128),# units:What Sound End  index:77    from 698 To 0
        SetMemory(0x662C8C, Add, -686),# units:What Sound End  index:78    from 686 To 0
        SetMemory(0x662C8C, Add, -47316992),# units:What Sound End  index:79    from 722 To 0
        SetMemory(0x662C90, Add, -543),# units:What Sound End  index:80    from 543 To 0
        SetMemory(0x662C90, Add, -42270720),# units:What Sound End  index:81    from 645 To 0
        SetMemory(0x662C94, Add, -710),# units:What Sound End  index:82    from 710 To 0
        SetMemory(0x662C94, Add, -42270720),# units:What Sound End  index:83    from 645 To 0
        SetMemory(0x662C98, Add, -659),# units:What Sound End  index:84    from 659 To 0
        SetMemory(0x662C9C, Add, -562),# units:What Sound End  index:86    from 562 To 0
        SetMemory(0x662CA0, Add, -1139),# units:What Sound End  index:88    from 1139 To 0
        SetMemory(0x662CA0, Add, -3670016),# units:What Sound End  index:89    from 56 To 0
        SetMemory(0x662CA4, Add, -48),# units:What Sound End  index:90    from 48 To 0
        SetMemory(0x662CA8, Add, -63832064),# units:What Sound End  index:93    from 974 To 0
        SetMemory(0x662CAC, Add, -978),# units:What Sound End  index:94    from 978 To 0
        SetMemory(0x662CAC, Add, -3407872),# units:What Sound End  index:95    from 52 To 0
        SetMemory(0x662CB0, Add, -970),# units:What Sound End  index:96    from 970 To 0
        SetMemory(0x662CB4, Add, -1047),# units:What Sound End  index:98    from 1047 To 0
        SetMemory(0x662CB4, Add, -65011712),# units:What Sound End  index:99    from 992 To 0
        SetMemory(0x662CB8, Add, -233),# units:What Sound End  index:100    from 233 To 0
        SetMemory(0x662CBC, Add, -452),# units:What Sound End  index:102    from 452 To 0
        SetMemory(0x662CBC, Add, -71303168),# units:What Sound End  index:103    from 1088 To 0
        SetMemory(0x662CC0, Add, -1124),# units:What Sound End  index:104    from 1124 To 0
        SetMemory(0x662CC4, Add, -15),# units:What Sound End  index:106    from 15 To 0
        SetMemory(0x662CC4, Add, -25362432),# units:What Sound End  index:107    from 387 To 0
        SetMemory(0x662CC8, Add, -26017792),# units:What Sound End  index:109    from 397 To 0
        SetMemory(0x662CCC, Add, -400),# units:What Sound End  index:110    from 400 To 0
        SetMemory(0x662CCC, Add, -983040),# units:What Sound End  index:111    from 15 To 0
        SetMemory(0x662CD0, Add, -385),# units:What Sound End  index:112    from 385 To 0
        SetMemory(0x662CD0, Add, -983040),# units:What Sound End  index:113    from 15 To 0
        SetMemory(0x662CD4, Add, -15),# units:What Sound End  index:114    from 15 To 0
        SetMemory(0x662CD4, Add, -25493504),# units:What Sound End  index:115    from 389 To 0
        SetMemory(0x662CD8, Add, -395),# units:What Sound End  index:116    from 395 To 0
        SetMemory(0x662CD8, Add, -25559040),# units:What Sound End  index:117    from 390 To 0
        SetMemory(0x662CDC, Add, -398),# units:What Sound End  index:118    from 398 To 0
        SetMemory(0x662CE0, Add, -392),# units:What Sound End  index:120    from 392 To 0
        SetMemory(0x662CE4, Add, -402),# units:What Sound End  index:122    from 402 To 0
        SetMemory(0x662CE4, Add, -25296896),# units:What Sound End  index:123    from 386 To 0
        SetMemory(0x662CE8, Add, -393),# units:What Sound End  index:124    from 393 To 0
        SetMemory(0x662CE8, Add, -983040),# units:What Sound End  index:125    from 15 To 0
        SetMemory(0x662CEC, Add, -394),# units:What Sound End  index:126    from 394 To 0
        SetMemory(0x662CEC, Add, -25624576),# units:What Sound End  index:127    from 391 To 0
        SetMemory(0x662CF0, Add, -15),# units:What Sound End  index:128    from 15 To 0
        SetMemory(0x662CF0, Add, -983040),# units:What Sound End  index:129    from 15 To 0
        SetMemory(0x662CF4, Add, -15),# units:What Sound End  index:130    from 15 To 0
        SetMemory(0x662CF4, Add, -49741824),# units:What Sound End  index:131    from 759 To 0
        SetMemory(0x662CF8, Add, -762),# units:What Sound End  index:132    from 762 To 0
        SetMemory(0x662CF8, Add, -49807360),# units:What Sound End  index:133    from 760 To 0
        SetMemory(0x662CFC, Add, -768),# units:What Sound End  index:134    from 768 To 0
        SetMemory(0x662CFC, Add, -50528256),# units:What Sound End  index:135    from 771 To 0
        SetMemory(0x662D00, Add, -766),# units:What Sound End  index:136    from 766 To 0
        SetMemory(0x662D00, Add, -50135040),# units:What Sound End  index:137    from 765 To 0
        SetMemory(0x662D04, Add, -767),# units:What Sound End  index:138    from 767 To 0
        SetMemory(0x662D04, Add, -49610752),# units:What Sound End  index:139    from 757 To 0
        SetMemory(0x662D08, Add, -770),# units:What Sound End  index:140    from 770 To 0
        SetMemory(0x662D08, Add, -50659328),# units:What Sound End  index:141    from 773 To 0
        SetMemory(0x662D0C, Add, -755),# units:What Sound End  index:142    from 755 To 0
        SetMemory(0x662D0C, Add, -49676288),# units:What Sound End  index:143    from 758 To 0
        SetMemory(0x662D10, Add, -772),# units:What Sound End  index:144    from 772 To 0
        SetMemory(0x662D14, Add, -763),# units:What Sound End  index:146    from 763 To 0
        SetMemory(0x662D14, Add, -50397184),# units:What Sound End  index:147    from 769 To 0
        SetMemory(0x662D18, Add, -769),# units:What Sound End  index:148    from 769 To 0
        SetMemory(0x662D18, Add, -49872896),# units:What Sound End  index:149    from 761 To 0
        SetMemory(0x662D1C, Add, -764),# units:What Sound End  index:150    from 764 To 0
        SetMemory(0x662D1C, Add, -49545216),# units:What Sound End  index:151    from 756 To 0
        SetMemory(0x662D20, Add, -756),# units:What Sound End  index:152    from 756 To 0
        SetMemory(0x662D24, Add, -484),# units:What Sound End  index:154    from 484 To 0
        SetMemory(0x662D24, Add, -31981568),# units:What Sound End  index:155    from 488 To 0
        SetMemory(0x662D28, Add, -487),# units:What Sound End  index:156    from 487 To 0
        SetMemory(0x662D28, Add, -31064064),# units:What Sound End  index:157    from 474 To 0
        SetMemory(0x662D2C, Add, -31195136),# units:What Sound End  index:159    from 476 To 0
        SetMemory(0x662D30, Add, -479),# units:What Sound End  index:160    from 479 To 0
        SetMemory(0x662D34, Add, -485),# units:What Sound End  index:162    from 485 To 0
        SetMemory(0x662D34, Add, -31260672),# units:What Sound End  index:163    from 477 To 0
        SetMemory(0x662D38, Add, -480),# units:What Sound End  index:164    from 480 To 0
        SetMemory(0x662D38, Add, -30998528),# units:What Sound End  index:165    from 473 To 0
        SetMemory(0x662D3C, Add, -478),# units:What Sound End  index:166    from 478 To 0
        SetMemory(0x662D3C, Add, -983040),# units:What Sound End  index:167    from 15 To 0
        SetMemory(0x662D40, Add, -399),# units:What Sound End  index:168    from 399 To 0
        SetMemory(0x662D40, Add, -32178176),# units:What Sound End  index:169    from 491 To 0
        SetMemory(0x662D44, Add, -490),# units:What Sound End  index:170    from 490 To 0
        SetMemory(0x662D44, Add, -32047104),# units:What Sound End  index:171    from 489 To 0
        SetMemory(0x662D48, Add, -475),# units:What Sound End  index:172    from 475 To 0
        SetMemory(0x662D48, Add, -31588352),# units:What Sound End  index:173    from 482 To 0
        SetMemory(0x662D4C, Add, -486),# units:What Sound End  index:174    from 486 To 0
        SetMemory(0x662D4C, Add, -31850496),# units:What Sound End  index:175    from 486 To 0
        SetMemory(0x662D68, Add, -32178176),# units:What Sound End  index:189    from 491 To 0
        SetMemory(0x662D6C, Add, -391),# units:What Sound End  index:190    from 391 To 0
        SetMemory(0x662D74, Add, -15),# units:What Sound End  index:194    from 15 To 0
        SetMemory(0x662D74, Add, -983040),# units:What Sound End  index:195    from 15 To 0
        SetMemory(0x662D78, Add, -15),# units:What Sound End  index:196    from 15 To 0
        SetMemory(0x662D80, Add, -396),# units:What Sound End  index:200    from 396 To 0
        SetMemory(0x662D80, Add, -50397184),# units:What Sound End  index:201    from 769 To 0
        SetMemory(0x662D9C, Add, -983040),# units:What Sound End  index:215    from 15 To 0
        SetMemory(0x662DA0, Add, -15),# units:What Sound End  index:216    from 15 To 0
        SetMemory(0x662DA0, Add, -983040),# units:What Sound End  index:217    from 15 To 0
        SetMemory(0x662DA4, Add, -15),# units:What Sound End  index:218    from 15 To 0
        SetMemory(0x662DA4, Add, -983040),# units:What Sound End  index:219    from 15 To 0
        SetMemory(0x662DA8, Add, -15),# units:What Sound End  index:220    from 15 To 0
        SetMemory(0x662DA8, Add, -983040),# units:What Sound End  index:221    from 15 To 0
        SetMemory(0x662DAC, Add, -15),# units:What Sound End  index:222    from 15 To 0
        SetMemory(0x662DAC, Add, -983040),# units:What Sound End  index:223    from 15 To 0
        SetMemory(0x663B38, Add, -14811136),# units:Piss Sound Start  index:1    from 226 To 0
        SetMemory(0x663B3C, Add, -356),# units:Piss Sound Start  index:2    from 356 To 0
        SetMemory(0x663B44, Add, -24248320),# units:Piss Sound Start  index:7    from 370 To 0
        SetMemory(0x663B48, Add, -258),# units:Piss Sound Start  index:8    from 258 To 0
        SetMemory(0x663B48, Add, -21823488),# units:Piss Sound Start  index:9    from 333 To 0
        SetMemory(0x663B4C, Add, -303),# units:Piss Sound Start  index:10    from 303 To 0
        SetMemory(0x663B4C, Add, -13828096),# units:Piss Sound Start  index:11    from 211 To 0
        SetMemory(0x663B50, Add, -180),# units:Piss Sound Start  index:12    from 180 To 0
        SetMemory(0x663B58, Add, -457),# units:Piss Sound Start  index:16    from 457 To 0
        SetMemory(0x663B5C, Add, -27459584),# units:Piss Sound Start  index:19    from 419 To 0
        SetMemory(0x663B60, Add, -407),# units:Piss Sound Start  index:20    from 407 To 0
        SetMemory(0x663B60, Add, -16908288),# units:Piss Sound Start  index:21    from 258 To 0
        SetMemory(0x663B64, Add, -333),# units:Piss Sound Start  index:22    from 333 To 0
        SetMemory(0x663B6C, Add, -29097984),# units:Piss Sound Start  index:27    from 444 To 0
        SetMemory(0x663B70, Add, -407),# units:Piss Sound Start  index:28    from 407 To 0
        SetMemory(0x663B70, Add, -29097984),# units:Piss Sound Start  index:29    from 444 To 0
        SetMemory(0x663B78, Add, -303),# units:Piss Sound Start  index:32    from 303 To 0
        SetMemory(0x663B7C, Add, -1009),# units:Piss Sound Start  index:34    from 1009 To 0
        SetMemory(0x663B80, Add, -58785792),# units:Piss Sound Start  index:37    from 897 To 0
        SetMemory(0x663B84, Add, -868),# units:Piss Sound Start  index:38    from 868 To 0
        SetMemory(0x663B84, Add, -57606144),# units:Piss Sound Start  index:39    from 879 To 0
        SetMemory(0x663B88, Add, -788),# units:Piss Sound Start  index:40    from 788 To 0
        SetMemory(0x663B88, Add, -54657024),# units:Piss Sound Start  index:41    from 834 To 0
        SetMemory(0x663B8C, Add, -911),# units:Piss Sound Start  index:42    from 911 To 0
        SetMemory(0x663B8C, Add, -61800448),# units:Piss Sound Start  index:43    from 943 To 0
        SetMemory(0x663B90, Add, -853),# units:Piss Sound Start  index:44    from 853 To 0
        SetMemory(0x663B90, Add, -60882944),# units:Piss Sound Start  index:45    from 929 To 0
        SetMemory(0x663B94, Add, -818),# units:Piss Sound Start  index:46    from 818 To 0
        SetMemory(0x663B94, Add, -51052544),# units:Piss Sound Start  index:47    from 779 To 0
        SetMemory(0x663B98, Add, -879),# units:Piss Sound Start  index:48    from 879 To 0
        SetMemory(0x663B98, Add, -60882944),# units:Piss Sound Start  index:49    from 929 To 0
        SetMemory(0x663B9C, Add, -801),# units:Piss Sound Start  index:50    from 801 To 0
        SetMemory(0x663B9C, Add, -62586880),# units:Piss Sound Start  index:51    from 955 To 0
        SetMemory(0x663BA0, Add, -818),# units:Piss Sound Start  index:52    from 818 To 0
        SetMemory(0x663BA0, Add, -56885248),# units:Piss Sound Start  index:53    from 868 To 0
        SetMemory(0x663BA4, Add, -897),# units:Piss Sound Start  index:54    from 897 To 0
        SetMemory(0x663BA4, Add, -61800448),# units:Piss Sound Start  index:55    from 943 To 0
        SetMemory(0x663BA8, Add, -853),# units:Piss Sound Start  index:56    from 853 To 0
        SetMemory(0x663BA8, Add, -59703296),# units:Piss Sound Start  index:57    from 911 To 0
        SetMemory(0x663BB0, Add, -1052),# units:Piss Sound Start  index:60    from 1052 To 0
        SetMemory(0x663BB0, Add, -47775744),# units:Piss Sound Start  index:61    from 729 To 0
        SetMemory(0x663BB4, Add, -1098),# units:Piss Sound Start  index:62    from 1098 To 0
        SetMemory(0x663BB4, Add, -69926912),# units:Piss Sound Start  index:63    from 1067 To 0
        SetMemory(0x663BB8, Add, -602),# units:Piss Sound Start  index:64    from 602 To 0
        SetMemory(0x663BB8, Add, -43712512),# units:Piss Sound Start  index:65    from 667 To 0
        SetMemory(0x663BBC, Add, -494),# units:Piss Sound Start  index:66    from 494 To 0
        SetMemory(0x663BBC, Add, -40828928),# units:Piss Sound Start  index:67    from 623 To 0
        SetMemory(0x663BC0, Add, -569),# units:Piss Sound Start  index:68    from 569 To 0
        SetMemory(0x663BC0, Add, -33751040),# units:Piss Sound Start  index:69    from 515 To 0
        SetMemory(0x663BC4, Add, -535),# units:Piss Sound Start  index:70    from 535 To 0
        SetMemory(0x663BC4, Add, -36306944),# units:Piss Sound Start  index:71    from 554 To 0
        SetMemory(0x663BC8, Add, -583),# units:Piss Sound Start  index:72    from 583 To 0
        SetMemory(0x663BCC, Add, -729),# units:Piss Sound Start  index:74    from 729 To 0
        SetMemory(0x663BCC, Add, -48627712),# units:Piss Sound Start  index:75    from 742 To 0
        SetMemory(0x663BD0, Add, -569),# units:Piss Sound Start  index:76    from 569 To 0
        SetMemory(0x663BD0, Add, -45285376),# units:Piss Sound Start  index:77    from 691 To 0
        SetMemory(0x663BD4, Add, -679),# units:Piss Sound Start  index:78    from 679 To 0
        SetMemory(0x663BD4, Add, -46858240),# units:Piss Sound Start  index:79    from 715 To 0
        SetMemory(0x663BD8, Add, -535),# units:Piss Sound Start  index:80    from 535 To 0
        SetMemory(0x663BD8, Add, -41877504),# units:Piss Sound Start  index:81    from 639 To 0
        SetMemory(0x663BDC, Add, -703),# units:Piss Sound Start  index:82    from 703 To 0
        SetMemory(0x663BDC, Add, -41877504),# units:Piss Sound Start  index:83    from 639 To 0
        SetMemory(0x663BE0, Add, -653),# units:Piss Sound Start  index:84    from 653 To 0
        SetMemory(0x663BE4, Add, -554),# units:Piss Sound Start  index:86    from 554 To 0
        SetMemory(0x663BE8, Add, -1130),# units:Piss Sound Start  index:88    from 1130 To 0
        SetMemory(0x663BFC, Add, -64225280),# units:Piss Sound Start  index:99    from 980 To 0
        SetMemory(0x663C00, Add, -226),# units:Piss Sound Start  index:100    from 226 To 0
        SetMemory(0x663C04, Add, -444),# units:Piss Sound Start  index:102    from 444 To 0
        SetMemory(0x663C04, Add, -70844416),# units:Piss Sound Start  index:103    from 1081 To 0
        SetMemory(0x663C08, Add, -1112),# units:Piss Sound Start  index:104    from 1112 To 0
        SetMemory(0x661EE8, Add, -15007744),# units:Piss Sound End  index:1    from 229 To 0
        SetMemory(0x661EEC, Add, -359),# units:Piss Sound End  index:2    from 359 To 0
        SetMemory(0x661EF4, Add, -24641536),# units:Piss Sound End  index:7    from 376 To 0
        SetMemory(0x661EF8, Add, -264),# units:Piss Sound End  index:8    from 264 To 0
        SetMemory(0x661EF8, Add, -22216704),# units:Piss Sound End  index:9    from 339 To 0
        SetMemory(0x661EFC, Add, -309),# units:Piss Sound End  index:10    from 309 To 0
        SetMemory(0x661EFC, Add, -14024704),# units:Piss Sound End  index:11    from 214 To 0
        SetMemory(0x661F00, Add, -184),# units:Piss Sound End  index:12    from 184 To 0
        SetMemory(0x661F08, Add, -461),# units:Piss Sound End  index:16    from 461 To 0
        SetMemory(0x661F0C, Add, -27656192),# units:Piss Sound End  index:19    from 422 To 0
        SetMemory(0x661F10, Add, -410),# units:Piss Sound End  index:20    from 410 To 0
        SetMemory(0x661F10, Add, -17301504),# units:Piss Sound End  index:21    from 264 To 0
        SetMemory(0x661F14, Add, -339),# units:Piss Sound End  index:22    from 339 To 0
        SetMemory(0x661F1C, Add, -29360128),# units:Piss Sound End  index:27    from 448 To 0
        SetMemory(0x661F20, Add, -410),# units:Piss Sound End  index:28    from 410 To 0
        SetMemory(0x661F20, Add, -29360128),# units:Piss Sound End  index:29    from 448 To 0
        SetMemory(0x661F28, Add, -309),# units:Piss Sound End  index:32    from 309 To 0
        SetMemory(0x661F2C, Add, -1015),# units:Piss Sound End  index:34    from 1015 To 0
        SetMemory(0x661F30, Add, -58916864),# units:Piss Sound End  index:37    from 899 To 0
        SetMemory(0x661F34, Add, -869),# units:Piss Sound End  index:38    from 869 To 0
        SetMemory(0x661F34, Add, -57737216),# units:Piss Sound End  index:39    from 881 To 0
        SetMemory(0x661F38, Add, -791),# units:Piss Sound End  index:40    from 791 To 0
        SetMemory(0x661F38, Add, -54788096),# units:Piss Sound End  index:41    from 836 To 0
        SetMemory(0x661F3C, Add, -911),# units:Piss Sound End  index:42    from 911 To 0
        SetMemory(0x661F3C, Add, -61997056),# units:Piss Sound End  index:43    from 946 To 0
        SetMemory(0x661F40, Add, -856),# units:Piss Sound End  index:44    from 856 To 0
        SetMemory(0x661F40, Add, -61079552),# units:Piss Sound End  index:45    from 932 To 0
        SetMemory(0x661F44, Add, -820),# units:Piss Sound End  index:46    from 820 To 0
        SetMemory(0x661F44, Add, -51118080),# units:Piss Sound End  index:47    from 780 To 0
        SetMemory(0x661F48, Add, -881),# units:Piss Sound End  index:48    from 881 To 0
        SetMemory(0x661F48, Add, -61079552),# units:Piss Sound End  index:49    from 932 To 0
        SetMemory(0x661F4C, Add, -804),# units:Piss Sound End  index:50    from 804 To 0
        SetMemory(0x661F4C, Add, -62783488),# units:Piss Sound End  index:51    from 958 To 0
        SetMemory(0x661F50, Add, -820),# units:Piss Sound End  index:52    from 820 To 0
        SetMemory(0x661F50, Add, -56950784),# units:Piss Sound End  index:53    from 869 To 0
        SetMemory(0x661F54, Add, -899),# units:Piss Sound End  index:54    from 899 To 0
        SetMemory(0x661F54, Add, -61997056),# units:Piss Sound End  index:55    from 946 To 0
        SetMemory(0x661F58, Add, -856),# units:Piss Sound End  index:56    from 856 To 0
        SetMemory(0x661F58, Add, -59703296),# units:Piss Sound End  index:57    from 911 To 0
        SetMemory(0x661F60, Add, -1058),# units:Piss Sound End  index:60    from 1058 To 0
        SetMemory(0x661F60, Add, -47972352),# units:Piss Sound End  index:61    from 732 To 0
        SetMemory(0x661F64, Add, -1100),# units:Piss Sound End  index:62    from 1100 To 0
        SetMemory(0x661F64, Add, -70123520),# units:Piss Sound End  index:63    from 1070 To 0
        SetMemory(0x661F68, Add, -605),# units:Piss Sound End  index:64    from 605 To 0
        SetMemory(0x661F68, Add, -43843584),# units:Piss Sound End  index:65    from 669 To 0
        SetMemory(0x661F6C, Add, -497),# units:Piss Sound End  index:66    from 497 To 0
        SetMemory(0x661F6C, Add, -41025536),# units:Piss Sound End  index:67    from 626 To 0
        SetMemory(0x661F70, Add, -572),# units:Piss Sound End  index:68    from 572 To 0
        SetMemory(0x661F70, Add, -34013184),# units:Piss Sound End  index:69    from 519 To 0
        SetMemory(0x661F74, Add, -539),# units:Piss Sound End  index:70    from 539 To 0
        SetMemory(0x661F74, Add, -36569088),# units:Piss Sound End  index:71    from 558 To 0
        SetMemory(0x661F78, Add, -586),# units:Piss Sound End  index:72    from 586 To 0
        SetMemory(0x661F7C, Add, -732),# units:Piss Sound End  index:74    from 732 To 0
        SetMemory(0x661F7C, Add, -48824320),# units:Piss Sound End  index:75    from 745 To 0
        SetMemory(0x661F80, Add, -572),# units:Piss Sound End  index:76    from 572 To 0
        SetMemory(0x661F80, Add, -45481984),# units:Piss Sound End  index:77    from 694 To 0
        SetMemory(0x661F84, Add, -682),# units:Piss Sound End  index:78    from 682 To 0
        SetMemory(0x661F84, Add, -47054848),# units:Piss Sound End  index:79    from 718 To 0
        SetMemory(0x661F88, Add, -539),# units:Piss Sound End  index:80    from 539 To 0
        SetMemory(0x661F88, Add, -42008576),# units:Piss Sound End  index:81    from 641 To 0
        SetMemory(0x661F8C, Add, -706),# units:Piss Sound End  index:82    from 706 To 0
        SetMemory(0x661F8C, Add, -42008576),# units:Piss Sound End  index:83    from 641 To 0
        SetMemory(0x661F90, Add, -657),# units:Piss Sound End  index:84    from 657 To 0
        SetMemory(0x661F94, Add, -558),# units:Piss Sound End  index:86    from 558 To 0
        SetMemory(0x661F98, Add, -1135),# units:Piss Sound End  index:88    from 1135 To 0
        SetMemory(0x661FAC, Add, -64749568),# units:Piss Sound End  index:99    from 988 To 0
        SetMemory(0x661FB0, Add, -229),# units:Piss Sound End  index:100    from 229 To 0
        SetMemory(0x661FB4, Add, -448),# units:Piss Sound End  index:102    from 448 To 0
        SetMemory(0x661FB4, Add, -71041024),# units:Piss Sound End  index:103    from 1084 To 0
        SetMemory(0x661FB8, Add, -1120),# units:Piss Sound End  index:104    from 1120 To 0
        SetMemory(0x663C10, Add, -15335424),# units:Yes Sound Start  index:1    from 234 To 0
        SetMemory(0x663C14, Add, -364),# units:Yes Sound Start  index:2    from 364 To 0
        SetMemory(0x663C1C, Add, -24969216),# units:Yes Sound Start  index:7    from 381 To 0
        SetMemory(0x663C20, Add, -269),# units:Yes Sound Start  index:8    from 269 To 0
        SetMemory(0x663C20, Add, -22544384),# units:Yes Sound Start  index:9    from 344 To 0
        SetMemory(0x663C24, Add, -310),# units:Yes Sound Start  index:10    from 310 To 0
        SetMemory(0x663C24, Add, -14352384),# units:Yes Sound Start  index:11    from 219 To 0
        SetMemory(0x663C28, Add, -189),# units:Yes Sound Start  index:12    from 189 To 0
        SetMemory(0x663C30, Add, -466),# units:Yes Sound Start  index:16    from 466 To 0
        SetMemory(0x663C34, Add, -27983872),# units:Yes Sound Start  index:19    from 427 To 0
        SetMemory(0x663C38, Add, -415),# units:Yes Sound Start  index:20    from 415 To 0
        SetMemory(0x663C38, Add, -17629184),# units:Yes Sound Start  index:21    from 269 To 0
        SetMemory(0x663C3C, Add, -344),# units:Yes Sound Start  index:22    from 344 To 0
        SetMemory(0x663C44, Add, -29687808),# units:Yes Sound Start  index:27    from 453 To 0
        SetMemory(0x663C48, Add, -415),# units:Yes Sound Start  index:28    from 415 To 0
        SetMemory(0x663C48, Add, -29687808),# units:Yes Sound Start  index:29    from 453 To 0
        SetMemory(0x663C50, Add, -310),# units:Yes Sound Start  index:32    from 310 To 0
        SetMemory(0x663C54, Add, -1005),# units:Yes Sound Start  index:34    from 1005 To 0
        SetMemory(0x663C58, Add, -59310080),# units:Yes Sound Start  index:37    from 905 To 0
        SetMemory(0x663C5C, Add, -873),# units:Yes Sound Start  index:38    from 873 To 0
        SetMemory(0x663C5C, Add, -58130432),# units:Yes Sound Start  index:39    from 887 To 0
        SetMemory(0x663C60, Add, -796),# units:Yes Sound Start  index:40    from 796 To 0
        SetMemory(0x663C60, Add, -55181312),# units:Yes Sound Start  index:41    from 842 To 0
        SetMemory(0x663C64, Add, -916),# units:Yes Sound Start  index:42    from 916 To 0
        SetMemory(0x663C64, Add, -62324736),# units:Yes Sound Start  index:43    from 951 To 0
        SetMemory(0x663C68, Add, -862),# units:Yes Sound Start  index:44    from 862 To 0
        SetMemory(0x663C68, Add, -61407232),# units:Yes Sound Start  index:45    from 937 To 0
        SetMemory(0x663C6C, Add, -824),# units:Yes Sound Start  index:46    from 824 To 0
        SetMemory(0x663C6C, Add, -51314688),# units:Yes Sound Start  index:47    from 783 To 0
        SetMemory(0x663C70, Add, -887),# units:Yes Sound Start  index:48    from 887 To 0
        SetMemory(0x663C70, Add, -61407232),# units:Yes Sound Start  index:49    from 937 To 0
        SetMemory(0x663C74, Add, -809),# units:Yes Sound Start  index:50    from 809 To 0
        SetMemory(0x663C74, Add, -63111168),# units:Yes Sound Start  index:51    from 963 To 0
        SetMemory(0x663C78, Add, -824),# units:Yes Sound Start  index:52    from 824 To 0
        SetMemory(0x663C78, Add, -57212928),# units:Yes Sound Start  index:53    from 873 To 0
        SetMemory(0x663C7C, Add, -905),# units:Yes Sound Start  index:54    from 905 To 0
        SetMemory(0x663C7C, Add, -62324736),# units:Yes Sound Start  index:55    from 951 To 0
        SetMemory(0x663C80, Add, -862),# units:Yes Sound Start  index:56    from 862 To 0
        SetMemory(0x663C80, Add, -60030976),# units:Yes Sound Start  index:57    from 916 To 0
        SetMemory(0x663C88, Add, -1048),# units:Yes Sound Start  index:60    from 1048 To 0
        SetMemory(0x663C88, Add, -48300032),# units:Yes Sound Start  index:61    from 737 To 0
        SetMemory(0x663C8C, Add, -1104),# units:Yes Sound Start  index:62    from 1104 To 0
        SetMemory(0x663C8C, Add, -70451200),# units:Yes Sound Start  index:63    from 1075 To 0
        SetMemory(0x663C90, Add, -610),# units:Yes Sound Start  index:64    from 610 To 0
        SetMemory(0x663C90, Add, -44171264),# units:Yes Sound Start  index:65    from 674 To 0
        SetMemory(0x663C94, Add, -506),# units:Yes Sound Start  index:66    from 506 To 0
        SetMemory(0x663C94, Add, -41353216),# units:Yes Sound Start  index:67    from 631 To 0
        SetMemory(0x663C98, Add, -577),# units:Yes Sound Start  index:68    from 577 To 0
        SetMemory(0x663C98, Add, -34340864),# units:Yes Sound Start  index:69    from 524 To 0
        SetMemory(0x663C9C, Add, -544),# units:Yes Sound Start  index:70    from 544 To 0
        SetMemory(0x663C9C, Add, -36896768),# units:Yes Sound Start  index:71    from 563 To 0
        SetMemory(0x663CA0, Add, -591),# units:Yes Sound Start  index:72    from 591 To 0
        SetMemory(0x663CA4, Add, -737),# units:Yes Sound Start  index:74    from 737 To 0
        SetMemory(0x663CA4, Add, -49152000),# units:Yes Sound Start  index:75    from 750 To 0
        SetMemory(0x663CA8, Add, -577),# units:Yes Sound Start  index:76    from 577 To 0
        SetMemory(0x663CA8, Add, -45809664),# units:Yes Sound Start  index:77    from 699 To 0
        SetMemory(0x663CAC, Add, -687),# units:Yes Sound Start  index:78    from 687 To 0
        SetMemory(0x663CAC, Add, -47382528),# units:Yes Sound Start  index:79    from 723 To 0
        SetMemory(0x663CB0, Add, -544),# units:Yes Sound Start  index:80    from 544 To 0
        SetMemory(0x663CB0, Add, -42336256),# units:Yes Sound Start  index:81    from 646 To 0
        SetMemory(0x663CB4, Add, -711),# units:Yes Sound Start  index:82    from 711 To 0
        SetMemory(0x663CB4, Add, -42336256),# units:Yes Sound Start  index:83    from 646 To 0
        SetMemory(0x663CB8, Add, -660),# units:Yes Sound Start  index:84    from 660 To 0
        SetMemory(0x663CBC, Add, -563),# units:Yes Sound Start  index:86    from 563 To 0
        SetMemory(0x663CC0, Add, -1140),# units:Yes Sound Start  index:88    from 1140 To 0
        SetMemory(0x663CD4, Add, -65077248),# units:Yes Sound Start  index:99    from 993 To 0
        SetMemory(0x663CD8, Add, -234),# units:Yes Sound Start  index:100    from 234 To 0
        SetMemory(0x663CDC, Add, -453),# units:Yes Sound Start  index:102    from 453 To 0
        SetMemory(0x663CDC, Add, -71368704),# units:Yes Sound Start  index:103    from 1089 To 0
        SetMemory(0x663CE0, Add, -1125),# units:Yes Sound Start  index:104    from 1125 To 0
        SetMemory(0x661440, Add, -15532032),# units:Yes Sound End  index:1    from 237 To 0
        SetMemory(0x661444, Add, -367),# units:Yes Sound End  index:2    from 367 To 0
        SetMemory(0x66144C, Add, -25165824),# units:Yes Sound End  index:7    from 384 To 0
        SetMemory(0x661450, Add, -272),# units:Yes Sound End  index:8    from 272 To 0
        SetMemory(0x661450, Add, -22740992),# units:Yes Sound End  index:9    from 347 To 0
        SetMemory(0x661454, Add, -313),# units:Yes Sound End  index:10    from 313 To 0
        SetMemory(0x661454, Add, -14680064),# units:Yes Sound End  index:11    from 224 To 0
        SetMemory(0x661458, Add, -192),# units:Yes Sound End  index:12    from 192 To 0
        SetMemory(0x661460, Add, -469),# units:Yes Sound End  index:16    from 469 To 0
        SetMemory(0x661464, Add, -28180480),# units:Yes Sound End  index:19    from 430 To 0
        SetMemory(0x661468, Add, -418),# units:Yes Sound End  index:20    from 418 To 0
        SetMemory(0x661468, Add, -17825792),# units:Yes Sound End  index:21    from 272 To 0
        SetMemory(0x66146C, Add, -347),# units:Yes Sound End  index:22    from 347 To 0
        SetMemory(0x661474, Add, -29884416),# units:Yes Sound End  index:27    from 456 To 0
        SetMemory(0x661478, Add, -418),# units:Yes Sound End  index:28    from 418 To 0
        SetMemory(0x661478, Add, -29884416),# units:Yes Sound End  index:29    from 456 To 0
        SetMemory(0x661480, Add, -313),# units:Yes Sound End  index:32    from 313 To 0
        SetMemory(0x661484, Add, -1008),# units:Yes Sound End  index:34    from 1008 To 0
        SetMemory(0x661488, Add, -59506688),# units:Yes Sound End  index:37    from 908 To 0
        SetMemory(0x66148C, Add, -876),# units:Yes Sound End  index:38    from 876 To 0
        SetMemory(0x66148C, Add, -58327040),# units:Yes Sound End  index:39    from 890 To 0
        SetMemory(0x661490, Add, -799),# units:Yes Sound End  index:40    from 799 To 0
        SetMemory(0x661490, Add, -55443456),# units:Yes Sound End  index:41    from 846 To 0
        SetMemory(0x661494, Add, -919),# units:Yes Sound End  index:42    from 919 To 0
        SetMemory(0x661494, Add, -62521344),# units:Yes Sound End  index:43    from 954 To 0
        SetMemory(0x661498, Add, -865),# units:Yes Sound End  index:44    from 865 To 0
        SetMemory(0x661498, Add, -61603840),# units:Yes Sound End  index:45    from 940 To 0
        SetMemory(0x66149C, Add, -826),# units:Yes Sound End  index:46    from 826 To 0
        SetMemory(0x66149C, Add, -51380224),# units:Yes Sound End  index:47    from 784 To 0
        SetMemory(0x6614A0, Add, -890),# units:Yes Sound End  index:48    from 890 To 0
        SetMemory(0x6614A0, Add, -61603840),# units:Yes Sound End  index:49    from 940 To 0
        SetMemory(0x6614A4, Add, -812),# units:Yes Sound End  index:50    from 812 To 0
        SetMemory(0x6614A4, Add, -63307776),# units:Yes Sound End  index:51    from 966 To 0
        SetMemory(0x6614A8, Add, -826),# units:Yes Sound End  index:52    from 826 To 0
        SetMemory(0x6614A8, Add, -57409536),# units:Yes Sound End  index:53    from 876 To 0
        SetMemory(0x6614AC, Add, -908),# units:Yes Sound End  index:54    from 908 To 0
        SetMemory(0x6614AC, Add, -62521344),# units:Yes Sound End  index:55    from 954 To 0
        SetMemory(0x6614B0, Add, -865),# units:Yes Sound End  index:56    from 865 To 0
        SetMemory(0x6614B0, Add, -60227584),# units:Yes Sound End  index:57    from 919 To 0
        SetMemory(0x6614B8, Add, -1051),# units:Yes Sound End  index:60    from 1051 To 0
        SetMemory(0x6614B8, Add, -48496640),# units:Yes Sound End  index:61    from 740 To 0
        SetMemory(0x6614BC, Add, -1107),# units:Yes Sound End  index:62    from 1107 To 0
        SetMemory(0x6614BC, Add, -70647808),# units:Yes Sound End  index:63    from 1078 To 0
        SetMemory(0x6614C0, Add, -613),# units:Yes Sound End  index:64    from 613 To 0
        SetMemory(0x6614C0, Add, -44367872),# units:Yes Sound End  index:65    from 677 To 0
        SetMemory(0x6614C4, Add, -512),# units:Yes Sound End  index:66    from 512 To 0
        SetMemory(0x6614C4, Add, -41549824),# units:Yes Sound End  index:67    from 634 To 0
        SetMemory(0x6614C8, Add, -580),# units:Yes Sound End  index:68    from 580 To 0
        SetMemory(0x6614C8, Add, -34537472),# units:Yes Sound End  index:69    from 527 To 0
        SetMemory(0x6614CC, Add, -547),# units:Yes Sound End  index:70    from 547 To 0
        SetMemory(0x6614CC, Add, -37027840),# units:Yes Sound End  index:71    from 565 To 0
        SetMemory(0x6614D0, Add, -594),# units:Yes Sound End  index:72    from 594 To 0
        SetMemory(0x6614D4, Add, -740),# units:Yes Sound End  index:74    from 740 To 0
        SetMemory(0x6614D4, Add, -49348608),# units:Yes Sound End  index:75    from 753 To 0
        SetMemory(0x6614D8, Add, -580),# units:Yes Sound End  index:76    from 580 To 0
        SetMemory(0x6614D8, Add, -46006272),# units:Yes Sound End  index:77    from 702 To 0
        SetMemory(0x6614DC, Add, -690),# units:Yes Sound End  index:78    from 690 To 0
        SetMemory(0x6614DC, Add, -47579136),# units:Yes Sound End  index:79    from 726 To 0
        SetMemory(0x6614E0, Add, -547),# units:Yes Sound End  index:80    from 547 To 0
        SetMemory(0x6614E0, Add, -42532864),# units:Yes Sound End  index:81    from 649 To 0
        SetMemory(0x6614E4, Add, -714),# units:Yes Sound End  index:82    from 714 To 0
        SetMemory(0x6614E4, Add, -42532864),# units:Yes Sound End  index:83    from 649 To 0
        SetMemory(0x6614E8, Add, -661),# units:Yes Sound End  index:84    from 661 To 0
        SetMemory(0x6614EC, Add, -565),# units:Yes Sound End  index:86    from 565 To 0
        SetMemory(0x6614F0, Add, -1143),# units:Yes Sound End  index:88    from 1143 To 0
        SetMemory(0x661504, Add, -65273856),# units:Yes Sound End  index:99    from 996 To 0
        SetMemory(0x661508, Add, -237),# units:Yes Sound End  index:100    from 237 To 0
        SetMemory(0x66150C, Add, -456),# units:Yes Sound End  index:102    from 456 To 0
        SetMemory(0x66150C, Add, -71565312),# units:Yes Sound End  index:103    from 1092 To 0
        SetMemory(0x661510, Add, -1128),# units:Yes Sound End  index:104    from 1128 To 0
        SetMemory(0x662864, Add, 17),# units:StarEdit Placement Box Width  index:1    from 15 To 32
        SetMemory(0x66287C, Add, 9),# units:StarEdit Placement Box Width  index:7    from 23 To 32
        SetMemory(0x662880, Add, -6),# units:StarEdit Placement Box Width  index:8    from 38 To 32
        SetMemory(0x662884, Add, -33),# units:StarEdit Placement Box Width  index:9    from 65 To 32
        SetMemory(0x662888, Add, 9),# units:StarEdit Placement Box Width  index:10    from 23 To 32
        SetMemory(0x66288C, Add, -17),# units:StarEdit Placement Box Width  index:11    from 49 To 32
        SetMemory(0x662890, Add, -48),# units:StarEdit Placement Box Width  index:12    from 80 To 32
        SetMemory(0x6628A0, Add, 17),# units:StarEdit Placement Box Width  index:16    from 15 To 32
        SetMemory(0x6628B0, Add, 14),# units:StarEdit Placement Box Width  index:20    from 18 To 32
        SetMemory(0x6628B4, Add, -6),# units:StarEdit Placement Box Width  index:21    from 38 To 32
        SetMemory(0x6628B8, Add, -33),# units:StarEdit Placement Box Width  index:22    from 65 To 32
        SetMemory(0x6628CC, Add, -43),# units:StarEdit Placement Box Width  index:27    from 75 To 32
        SetMemory(0x6628D0, Add, -43),# units:StarEdit Placement Box Width  index:28    from 75 To 32
        SetMemory(0x6628D4, Add, -43),# units:StarEdit Placement Box Width  index:29    from 75 To 32
        SetMemory(0x6628E0, Add, 9),# units:StarEdit Placement Box Width  index:32    from 23 To 32
        SetMemory(0x6628E8, Add, 15),# units:StarEdit Placement Box Width  index:34    from 17 To 32
        SetMemory(0x6628F4, Add, 16),# units:StarEdit Placement Box Width  index:37    from 16 To 32
        SetMemory(0x6628F8, Add, 11),# units:StarEdit Placement Box Width  index:38    from 21 To 32
        SetMemory(0x6628FC, Add, -6),# units:StarEdit Placement Box Width  index:39    from 38 To 32
        SetMemory(0x662900, Add, 13),# units:StarEdit Placement Box Width  index:40    from 19 To 32
        SetMemory(0x662904, Add, 9),# units:StarEdit Placement Box Width  index:41    from 23 To 32
        SetMemory(0x662908, Add, -18),# units:StarEdit Placement Box Width  index:42    from 50 To 32
        SetMemory(0x66290C, Add, -12),# units:StarEdit Placement Box Width  index:43    from 44 To 32
        SetMemory(0x662910, Add, -12),# units:StarEdit Placement Box Width  index:44    from 44 To 32
        SetMemory(0x662914, Add, -16),# units:StarEdit Placement Box Width  index:45    from 48 To 32
        SetMemory(0x662918, Add, 5),# units:StarEdit Placement Box Width  index:46    from 27 To 32
        SetMemory(0x66291C, Add, 8),# units:StarEdit Placement Box Width  index:47    from 24 To 32
        SetMemory(0x662920, Add, -6),# units:StarEdit Placement Box Width  index:48    from 38 To 32
        SetMemory(0x662924, Add, -16),# units:StarEdit Placement Box Width  index:49    from 48 To 32
        SetMemory(0x662928, Add, 15),# units:StarEdit Placement Box Width  index:50    from 17 To 32
        SetMemory(0x66292C, Add, 17),# units:StarEdit Placement Box Width  index:51    from 15 To 32
        SetMemory(0x662930, Add, 3),# units:StarEdit Placement Box Width  index:52    from 29 To 32
        SetMemory(0x662934, Add, 11),# units:StarEdit Placement Box Width  index:53    from 21 To 32
        SetMemory(0x662938, Add, 16),# units:StarEdit Placement Box Width  index:54    from 16 To 32
        SetMemory(0x66293C, Add, -12),# units:StarEdit Placement Box Width  index:55    from 44 To 32
        SetMemory(0x662940, Add, -12),# units:StarEdit Placement Box Width  index:56    from 44 To 32
        SetMemory(0x662944, Add, -18),# units:StarEdit Placement Box Width  index:57    from 50 To 32
        SetMemory(0x662950, Add, -4),# units:StarEdit Placement Box Width  index:60    from 36 To 32
        SetMemory(0x662954, Add, 8),# units:StarEdit Placement Box Width  index:61    from 24 To 32
        SetMemory(0x662958, Add, -12),# units:StarEdit Placement Box Width  index:62    from 44 To 32
        SetMemory(0x662960, Add, 9),# units:StarEdit Placement Box Width  index:64    from 23 To 32
        SetMemory(0x662964, Add, 9),# units:StarEdit Placement Box Width  index:65    from 23 To 32
        SetMemory(0x66296C, Add, 8),# units:StarEdit Placement Box Width  index:67    from 24 To 32
        SetMemory(0x662974, Add, -8),# units:StarEdit Placement Box Width  index:69    from 40 To 32
        SetMemory(0x662978, Add, -4),# units:StarEdit Placement Box Width  index:70    from 36 To 32
        SetMemory(0x66297C, Add, -12),# units:StarEdit Placement Box Width  index:71    from 44 To 32
        SetMemory(0x662980, Add, -32),# units:StarEdit Placement Box Width  index:72    from 64 To 32
        SetMemory(0x662988, Add, 8),# units:StarEdit Placement Box Width  index:74    from 24 To 32
        SetMemory(0x66298C, Add, 8),# units:StarEdit Placement Box Width  index:75    from 24 To 32
        SetMemory(0x662994, Add, 8),# units:StarEdit Placement Box Width  index:77    from 24 To 32
        SetMemory(0x66299C, Add, 8),# units:StarEdit Placement Box Width  index:79    from 24 To 32
        SetMemory(0x6629A0, Add, -4),# units:StarEdit Placement Box Width  index:80    from 36 To 32
        SetMemory(0x6629A8, Add, -32),# units:StarEdit Placement Box Width  index:82    from 64 To 32
        SetMemory(0x6629B8, Add, -12),# units:StarEdit Placement Box Width  index:86    from 44 To 32
        SetMemory(0x6629BC, Add, 8),# units:StarEdit Placement Box Width  index:87    from 24 To 32
        SetMemory(0x6629C0, Add, -4),# units:StarEdit Placement Box Width  index:88    from 36 To 32
        SetMemory(0x6629E8, Add, -17),# units:StarEdit Placement Box Width  index:98    from 49 To 32
        SetMemory(0x6629EC, Add, 17),# units:StarEdit Placement Box Width  index:99    from 15 To 32
        SetMemory(0x6629F0, Add, 17),# units:StarEdit Placement Box Width  index:100    from 15 To 32
        SetMemory(0x6629F8, Add, -43),# units:StarEdit Placement Box Width  index:102    from 75 To 32
        SetMemory(0x662A00, Add, 17),# units:StarEdit Placement Box Width  index:104    from 15 To 32
        SetMemory(0x662A08, Add, -96),# units:StarEdit Placement Box Width  index:106    from 128 To 32
        SetMemory(0x662A0C, Add, -32),# units:StarEdit Placement Box Width  index:107    from 64 To 32
        SetMemory(0x662A14, Add, -64),# units:StarEdit Placement Box Width  index:109    from 96 To 32
        SetMemory(0x662A18, Add, -96),# units:StarEdit Placement Box Width  index:110    from 128 To 32
        SetMemory(0x662A1C, Add, -96),# units:StarEdit Placement Box Width  index:111    from 128 To 32
        SetMemory(0x662A20, Add, -64),# units:StarEdit Placement Box Width  index:112    from 96 To 32
        SetMemory(0x662A24, Add, -96),# units:StarEdit Placement Box Width  index:113    from 128 To 32
        SetMemory(0x662A28, Add, -96),# units:StarEdit Placement Box Width  index:114    from 128 To 32
        SetMemory(0x662A2C, Add, -32),# units:StarEdit Placement Box Width  index:115    from 64 To 32
        SetMemory(0x662A30, Add, -96),# units:StarEdit Placement Box Width  index:116    from 128 To 32
        SetMemory(0x662A34, Add, -32),# units:StarEdit Placement Box Width  index:117    from 64 To 32
        SetMemory(0x662A38, Add, -32),# units:StarEdit Placement Box Width  index:118    from 64 To 32
        SetMemory(0x662A40, Add, -32),# units:StarEdit Placement Box Width  index:120    from 64 To 32
        SetMemory(0x662A48, Add, -96),# units:StarEdit Placement Box Width  index:122    from 128 To 32
        SetMemory(0x662A4C, Add, -64),# units:StarEdit Placement Box Width  index:123    from 96 To 32
        SetMemory(0x662A50, Add, -32),# units:StarEdit Placement Box Width  index:124    from 64 To 32
        SetMemory(0x662A54, Add, -64),# units:StarEdit Placement Box Width  index:125    from 96 To 32
        SetMemory(0x662A58, Add, -64),# units:StarEdit Placement Box Width  index:126    from 96 To 32
        SetMemory(0x662A5C, Add, -64),# units:StarEdit Placement Box Width  index:127    from 96 To 32
        SetMemory(0x662A68, Add, -96),# units:StarEdit Placement Box Width  index:130    from 128 To 32
        SetMemory(0x662A6C, Add, -96),# units:StarEdit Placement Box Width  index:131    from 128 To 32
        SetMemory(0x662A70, Add, -96),# units:StarEdit Placement Box Width  index:132    from 128 To 32
        SetMemory(0x662A74, Add, -96),# units:StarEdit Placement Box Width  index:133    from 128 To 32
        SetMemory(0x662A78, Add, -32),# units:StarEdit Placement Box Width  index:134    from 64 To 32
        SetMemory(0x662A7C, Add, -64),# units:StarEdit Placement Box Width  index:135    from 96 To 32
        SetMemory(0x662A80, Add, -96),# units:StarEdit Placement Box Width  index:136    from 128 To 32
        SetMemory(0x662A84, Add, -32),# units:StarEdit Placement Box Width  index:137    from 64 To 32
        SetMemory(0x662A88, Add, -64),# units:StarEdit Placement Box Width  index:138    from 96 To 32
        SetMemory(0x662A8C, Add, -64),# units:StarEdit Placement Box Width  index:139    from 96 To 32
        SetMemory(0x662A90, Add, -64),# units:StarEdit Placement Box Width  index:140    from 96 To 32
        SetMemory(0x662A94, Add, -32),# units:StarEdit Placement Box Width  index:141    from 64 To 32
        SetMemory(0x662A98, Add, -64),# units:StarEdit Placement Box Width  index:142    from 96 To 32
        SetMemory(0x662A9C, Add, -32),# units:StarEdit Placement Box Width  index:143    from 64 To 32
        SetMemory(0x662AA0, Add, -32),# units:StarEdit Placement Box Width  index:144    from 64 To 32
        SetMemory(0x662AA8, Add, -32),# units:StarEdit Placement Box Width  index:146    from 64 To 32
        SetMemory(0x662AAC, Add, -128),# units:StarEdit Placement Box Width  index:147    from 160 To 32
        SetMemory(0x662AB0, Add, -128),# units:StarEdit Placement Box Width  index:148    from 160 To 32
        SetMemory(0x662AB4, Add, -96),# units:StarEdit Placement Box Width  index:149    from 128 To 32
        SetMemory(0x662AB8, Add, -32),# units:StarEdit Placement Box Width  index:150    from 64 To 32
        SetMemory(0x662ABC, Add, -64),# units:StarEdit Placement Box Width  index:151    from 96 To 32
        SetMemory(0x662AC0, Add, -64),# units:StarEdit Placement Box Width  index:152    from 96 To 32
        SetMemory(0x662AC8, Add, -96),# units:StarEdit Placement Box Width  index:154    from 128 To 32
        SetMemory(0x662ACC, Add, -64),# units:StarEdit Placement Box Width  index:155    from 96 To 32
        SetMemory(0x662AD0, Add, -32),# units:StarEdit Placement Box Width  index:156    from 64 To 32
        SetMemory(0x662AD4, Add, -96),# units:StarEdit Placement Box Width  index:157    from 128 To 32
        SetMemory(0x662ADC, Add, -64),# units:StarEdit Placement Box Width  index:159    from 96 To 32
        SetMemory(0x662AE0, Add, -96),# units:StarEdit Placement Box Width  index:160    from 128 To 32
        SetMemory(0x662AE8, Add, -32),# units:StarEdit Placement Box Width  index:162    from 64 To 32
        SetMemory(0x662AEC, Add, -64),# units:StarEdit Placement Box Width  index:163    from 96 To 32
        SetMemory(0x662AF0, Add, -64),# units:StarEdit Placement Box Width  index:164    from 96 To 32
        SetMemory(0x662AF4, Add, -64),# units:StarEdit Placement Box Width  index:165    from 96 To 32
        SetMemory(0x662AF8, Add, -64),# units:StarEdit Placement Box Width  index:166    from 96 To 32
        SetMemory(0x662AFC, Add, -96),# units:StarEdit Placement Box Width  index:167    from 128 To 32
        SetMemory(0x662B00, Add, -96),# units:StarEdit Placement Box Width  index:168    from 128 To 32
        SetMemory(0x662B04, Add, -64),# units:StarEdit Placement Box Width  index:169    from 96 To 32
        SetMemory(0x662B08, Add, -64),# units:StarEdit Placement Box Width  index:170    from 96 To 32
        SetMemory(0x662B0C, Add, -64),# units:StarEdit Placement Box Width  index:171    from 96 To 32
        SetMemory(0x662B10, Add, -64),# units:StarEdit Placement Box Width  index:172    from 96 To 32
        SetMemory(0x662B14, Add, -96),# units:StarEdit Placement Box Width  index:173    from 128 To 32
        SetMemory(0x662B18, Add, -192),# units:StarEdit Placement Box Width  index:174    from 224 To 32
        SetMemory(0x662B1C, Add, -128),# units:StarEdit Placement Box Width  index:175    from 160 To 32
        SetMemory(0x662B54, Add, -64),# units:StarEdit Placement Box Width  index:189    from 96 To 32
        SetMemory(0x662B58, Add, -128),# units:StarEdit Placement Box Width  index:190    from 160 To 32
        SetMemory(0x662B68, Add, -64),# units:StarEdit Placement Box Width  index:194    from 96 To 32
        SetMemory(0x662B6C, Add, -64),# units:StarEdit Placement Box Width  index:195    from 96 To 32
        SetMemory(0x662B70, Add, -64),# units:StarEdit Placement Box Width  index:196    from 96 To 32
        SetMemory(0x662B80, Add, -96),# units:StarEdit Placement Box Width  index:200    from 128 To 32
        SetMemory(0x662B84, Add, -64),# units:StarEdit Placement Box Width  index:201    from 96 To 32
        SetMemory(0x662864, Add, 655360),# units:StarEdit Placement Box Height  index:1    from 22 To 32
        SetMemory(0x66287C, Add, 589824),# units:StarEdit Placement Box Height  index:7    from 23 To 32
        SetMemory(0x662880, Add, 131072),# units:StarEdit Placement Box Height  index:8    from 30 To 32
        SetMemory(0x662884, Add, -1179648),# units:StarEdit Placement Box Height  index:9    from 50 To 32
        SetMemory(0x662888, Add, 262144),# units:StarEdit Placement Box Height  index:10    from 28 To 32
        SetMemory(0x66288C, Add, -327680),# units:StarEdit Placement Box Height  index:11    from 37 To 32
        SetMemory(0x662890, Add, -2097152),# units:StarEdit Placement Box Height  index:12    from 64 To 32
        SetMemory(0x6628A0, Add, 655360),# units:StarEdit Placement Box Height  index:16    from 22 To 32
        SetMemory(0x6628B0, Add, 655360),# units:StarEdit Placement Box Height  index:20    from 22 To 32
        SetMemory(0x6628B4, Add, 131072),# units:StarEdit Placement Box Height  index:21    from 30 To 32
        SetMemory(0x6628B8, Add, -1179648),# units:StarEdit Placement Box Height  index:22    from 50 To 32
        SetMemory(0x6628CC, Add, -1769472),# units:StarEdit Placement Box Height  index:27    from 59 To 32
        SetMemory(0x6628D0, Add, -1769472),# units:StarEdit Placement Box Height  index:28    from 59 To 32
        SetMemory(0x6628D4, Add, -1769472),# units:StarEdit Placement Box Height  index:29    from 59 To 32
        SetMemory(0x6628E0, Add, 262144),# units:StarEdit Placement Box Height  index:32    from 28 To 32
        SetMemory(0x6628E8, Add, 786432),# units:StarEdit Placement Box Height  index:34    from 20 To 32
        SetMemory(0x6628F4, Add, 1048576),# units:StarEdit Placement Box Height  index:37    from 16 To 32
        SetMemory(0x6628F8, Add, 589824),# units:StarEdit Placement Box Height  index:38    from 23 To 32
        SetMemory(0x662900, Add, 851968),# units:StarEdit Placement Box Height  index:40    from 19 To 32
        SetMemory(0x662904, Add, 589824),# units:StarEdit Placement Box Height  index:41    from 23 To 32
        SetMemory(0x662908, Add, -1179648),# units:StarEdit Placement Box Height  index:42    from 50 To 32
        SetMemory(0x66290C, Add, -786432),# units:StarEdit Placement Box Height  index:43    from 44 To 32
        SetMemory(0x662910, Add, -786432),# units:StarEdit Placement Box Height  index:44    from 44 To 32
        SetMemory(0x662914, Add, -1048576),# units:StarEdit Placement Box Height  index:45    from 48 To 32
        SetMemory(0x662918, Add, 458752),# units:StarEdit Placement Box Height  index:46    from 25 To 32
        SetMemory(0x66291C, Add, 524288),# units:StarEdit Placement Box Height  index:47    from 24 To 32
        SetMemory(0x662924, Add, -1048576),# units:StarEdit Placement Box Height  index:49    from 48 To 32
        SetMemory(0x662928, Add, 786432),# units:StarEdit Placement Box Height  index:50    from 20 To 32
        SetMemory(0x66292C, Add, 655360),# units:StarEdit Placement Box Height  index:51    from 22 To 32
        SetMemory(0x662930, Add, 196608),# units:StarEdit Placement Box Height  index:52    from 29 To 32
        SetMemory(0x662934, Add, 589824),# units:StarEdit Placement Box Height  index:53    from 23 To 32
        SetMemory(0x662938, Add, 1048576),# units:StarEdit Placement Box Height  index:54    from 16 To 32
        SetMemory(0x66293C, Add, -786432),# units:StarEdit Placement Box Height  index:55    from 44 To 32
        SetMemory(0x662940, Add, -786432),# units:StarEdit Placement Box Height  index:56    from 44 To 32
        SetMemory(0x662944, Add, -1179648),# units:StarEdit Placement Box Height  index:57    from 50 To 32
        SetMemory(0x662954, Add, 131072),# units:StarEdit Placement Box Height  index:61    from 30 To 32
        SetMemory(0x662958, Add, -786432),# units:StarEdit Placement Box Height  index:62    from 44 To 32
        SetMemory(0x662960, Add, 589824),# units:StarEdit Placement Box Height  index:64    from 23 To 32
        SetMemory(0x662964, Add, 327680),# units:StarEdit Placement Box Height  index:65    from 27 To 32
        SetMemory(0x66296C, Add, 262144),# units:StarEdit Placement Box Height  index:67    from 28 To 32
        SetMemory(0x66297C, Add, -786432),# units:StarEdit Placement Box Height  index:71    from 44 To 32
        SetMemory(0x662980, Add, -2097152),# units:StarEdit Placement Box Height  index:72    from 64 To 32
        SetMemory(0x662988, Add, 131072),# units:StarEdit Placement Box Height  index:74    from 30 To 32
        SetMemory(0x66298C, Add, 131072),# units:StarEdit Placement Box Height  index:75    from 30 To 32
        SetMemory(0x662994, Add, 131072),# units:StarEdit Placement Box Height  index:77    from 30 To 32
        SetMemory(0x66299C, Add, 262144),# units:StarEdit Placement Box Height  index:79    from 28 To 32
        SetMemory(0x6629A8, Add, -2097152),# units:StarEdit Placement Box Height  index:82    from 64 To 32
        SetMemory(0x6629B8, Add, -786432),# units:StarEdit Placement Box Height  index:86    from 44 To 32
        SetMemory(0x6629BC, Add, 262144),# units:StarEdit Placement Box Height  index:87    from 28 To 32
        SetMemory(0x6629E8, Add, -327680),# units:StarEdit Placement Box Height  index:98    from 37 To 32
        SetMemory(0x6629EC, Add, 655360),# units:StarEdit Placement Box Height  index:99    from 22 To 32
        SetMemory(0x6629F0, Add, 655360),# units:StarEdit Placement Box Height  index:100    from 22 To 32
        SetMemory(0x6629F8, Add, -1769472),# units:StarEdit Placement Box Height  index:102    from 59 To 32
        SetMemory(0x662A00, Add, 655360),# units:StarEdit Placement Box Height  index:104    from 22 To 32
        SetMemory(0x662A08, Add, -4194304),# units:StarEdit Placement Box Height  index:106    from 96 To 32
        SetMemory(0x662A0C, Add, -2097152),# units:StarEdit Placement Box Height  index:107    from 64 To 32
        SetMemory(0x662A14, Add, -2097152),# units:StarEdit Placement Box Height  index:109    from 64 To 32
        SetMemory(0x662A18, Add, -2097152),# units:StarEdit Placement Box Height  index:110    from 64 To 32
        SetMemory(0x662A1C, Add, -4194304),# units:StarEdit Placement Box Height  index:111    from 96 To 32
        SetMemory(0x662A20, Add, -2097152),# units:StarEdit Placement Box Height  index:112    from 64 To 32
        SetMemory(0x662A24, Add, -4194304),# units:StarEdit Placement Box Height  index:113    from 96 To 32
        SetMemory(0x662A28, Add, -4194304),# units:StarEdit Placement Box Height  index:114    from 96 To 32
        SetMemory(0x662A2C, Add, -2097152),# units:StarEdit Placement Box Height  index:115    from 64 To 32
        SetMemory(0x662A30, Add, -4194304),# units:StarEdit Placement Box Height  index:116    from 96 To 32
        SetMemory(0x662A34, Add, -2097152),# units:StarEdit Placement Box Height  index:117    from 64 To 32
        SetMemory(0x662A38, Add, -2097152),# units:StarEdit Placement Box Height  index:118    from 64 To 32
        SetMemory(0x662A40, Add, -2097152),# units:StarEdit Placement Box Height  index:120    from 64 To 32
        SetMemory(0x662A48, Add, -4194304),# units:StarEdit Placement Box Height  index:122    from 96 To 32
        SetMemory(0x662A4C, Add, -2097152),# units:StarEdit Placement Box Height  index:123    from 64 To 32
        SetMemory(0x662A50, Add, -2097152),# units:StarEdit Placement Box Height  index:124    from 64 To 32
        SetMemory(0x662A54, Add, -2097152),# units:StarEdit Placement Box Height  index:125    from 64 To 32
        SetMemory(0x662A58, Add, -2097152),# units:StarEdit Placement Box Height  index:126    from 64 To 32
        SetMemory(0x662A5C, Add, -2097152),# units:StarEdit Placement Box Height  index:127    from 64 To 32
        SetMemory(0x662A68, Add, -4194304),# units:StarEdit Placement Box Height  index:130    from 96 To 32
        SetMemory(0x662A6C, Add, -4194304),# units:StarEdit Placement Box Height  index:131    from 96 To 32
        SetMemory(0x662A70, Add, -4194304),# units:StarEdit Placement Box Height  index:132    from 96 To 32
        SetMemory(0x662A74, Add, -4194304),# units:StarEdit Placement Box Height  index:133    from 96 To 32
        SetMemory(0x662A78, Add, -2097152),# units:StarEdit Placement Box Height  index:134    from 64 To 32
        SetMemory(0x662A7C, Add, -2097152),# units:StarEdit Placement Box Height  index:135    from 64 To 32
        SetMemory(0x662A80, Add, -2097152),# units:StarEdit Placement Box Height  index:136    from 64 To 32
        SetMemory(0x662A84, Add, -2097152),# units:StarEdit Placement Box Height  index:137    from 64 To 32
        SetMemory(0x662A88, Add, -2097152),# units:StarEdit Placement Box Height  index:138    from 64 To 32
        SetMemory(0x662A8C, Add, -2097152),# units:StarEdit Placement Box Height  index:139    from 64 To 32
        SetMemory(0x662A90, Add, -2097152),# units:StarEdit Placement Box Height  index:140    from 64 To 32
        SetMemory(0x662A94, Add, -2097152),# units:StarEdit Placement Box Height  index:141    from 64 To 32
        SetMemory(0x662A98, Add, -2097152),# units:StarEdit Placement Box Height  index:142    from 64 To 32
        SetMemory(0x662A9C, Add, -2097152),# units:StarEdit Placement Box Height  index:143    from 64 To 32
        SetMemory(0x662AA0, Add, -2097152),# units:StarEdit Placement Box Height  index:144    from 64 To 32
        SetMemory(0x662AA8, Add, -2097152),# units:StarEdit Placement Box Height  index:146    from 64 To 32
        SetMemory(0x662AAC, Add, -4194304),# units:StarEdit Placement Box Height  index:147    from 96 To 32
        SetMemory(0x662AB0, Add, -4194304),# units:StarEdit Placement Box Height  index:148    from 96 To 32
        SetMemory(0x662AB4, Add, -2097152),# units:StarEdit Placement Box Height  index:149    from 64 To 32
        SetMemory(0x662AB8, Add, -2097152),# units:StarEdit Placement Box Height  index:150    from 64 To 32
        SetMemory(0x662ABC, Add, -2097152),# units:StarEdit Placement Box Height  index:151    from 64 To 32
        SetMemory(0x662AC0, Add, -2097152),# units:StarEdit Placement Box Height  index:152    from 64 To 32
        SetMemory(0x662AC8, Add, -4194304),# units:StarEdit Placement Box Height  index:154    from 96 To 32
        SetMemory(0x662ACC, Add, -2097152),# units:StarEdit Placement Box Height  index:155    from 64 To 32
        SetMemory(0x662AD0, Add, -2097152),# units:StarEdit Placement Box Height  index:156    from 64 To 32
        SetMemory(0x662AD4, Add, -2097152),# units:StarEdit Placement Box Height  index:157    from 64 To 32
        SetMemory(0x662ADC, Add, -2097152),# units:StarEdit Placement Box Height  index:159    from 64 To 32
        SetMemory(0x662AE0, Add, -4194304),# units:StarEdit Placement Box Height  index:160    from 96 To 32
        SetMemory(0x662AE8, Add, -2097152),# units:StarEdit Placement Box Height  index:162    from 64 To 32
        SetMemory(0x662AEC, Add, -2097152),# units:StarEdit Placement Box Height  index:163    from 64 To 32
        SetMemory(0x662AF0, Add, -2097152),# units:StarEdit Placement Box Height  index:164    from 64 To 32
        SetMemory(0x662AF4, Add, -2097152),# units:StarEdit Placement Box Height  index:165    from 64 To 32
        SetMemory(0x662AF8, Add, -2097152),# units:StarEdit Placement Box Height  index:166    from 64 To 32
        SetMemory(0x662AFC, Add, -4194304),# units:StarEdit Placement Box Height  index:167    from 96 To 32
        SetMemory(0x662B00, Add, -4194304),# units:StarEdit Placement Box Height  index:168    from 96 To 32
        SetMemory(0x662B04, Add, -2097152),# units:StarEdit Placement Box Height  index:169    from 64 To 32
        SetMemory(0x662B08, Add, -2097152),# units:StarEdit Placement Box Height  index:170    from 64 To 32
        SetMemory(0x662B0C, Add, -2097152),# units:StarEdit Placement Box Height  index:171    from 64 To 32
        SetMemory(0x662B10, Add, -2097152),# units:StarEdit Placement Box Height  index:172    from 64 To 32
        SetMemory(0x662B14, Add, -4194304),# units:StarEdit Placement Box Height  index:173    from 96 To 32
        SetMemory(0x662B18, Add, -4194304),# units:StarEdit Placement Box Height  index:174    from 96 To 32
        SetMemory(0x662B1C, Add, -6291456),# units:StarEdit Placement Box Height  index:175    from 128 To 32
        SetMemory(0x662B54, Add, -2097152),# units:StarEdit Placement Box Height  index:189    from 64 To 32
        SetMemory(0x662B58, Add, -4194304),# units:StarEdit Placement Box Height  index:190    from 96 To 32
        SetMemory(0x662B68, Add, -2097152),# units:StarEdit Placement Box Height  index:194    from 64 To 32
        SetMemory(0x662B6C, Add, -2097152),# units:StarEdit Placement Box Height  index:195    from 64 To 32
        SetMemory(0x662B70, Add, -2097152),# units:StarEdit Placement Box Height  index:196    from 64 To 32
        SetMemory(0x662B80, Add, -4194304),# units:StarEdit Placement Box Height  index:200    from 96 To 32
        SetMemory(0x662B84, Add, -2097152),# units:StarEdit Placement Box Height  index:201    from 64 To 32
        SetMemory(0x6626E4, Add, -128),# units:Addon Horizontal (X) Position  index:1    from 128 To 0
        SetMemory(0x662704, Add, -128),# units:Addon Horizontal (X) Position  index:9    from 128 To 0
        SetMemory(0x66270C, Add, -128),# units:Addon Horizontal (X) Position  index:11    from 128 To 0
        SetMemory(0x662710, Add, -128),# units:Addon Horizontal (X) Position  index:12    from 128 To 0
        SetMemory(0x662718, Add, -128),# units:Addon Horizontal (X) Position  index:14    from 128 To 0
        SetMemory(0x6626E4, Add, -2097152),# units:Addon Vertical (Y) Position  index:1    from 32 To 0
        SetMemory(0x662704, Add, -2097152),# units:Addon Vertical (Y) Position  index:9    from 32 To 0
        SetMemory(0x66270C, Add, -2097152),# units:Addon Vertical (Y) Position  index:11    from 32 To 0
        SetMemory(0x662710, Add, -2097152),# units:Addon Vertical (Y) Position  index:12    from 32 To 0
        SetMemory(0x662718, Add, -2097152),# units:Addon Vertical (Y) Position  index:14    from 32 To 0
        SetMemory(0x6617D0, Add, 9),# units:Unit Size Left  index:1    from 7 To 16
        SetMemory(0x661800, Add, 5),# units:Unit Size Left  index:7    from 11 To 16
        SetMemory(0x661808, Add, -3),# units:Unit Size Left  index:8    from 19 To 16
        SetMemory(0x661810, Add, -16),# units:Unit Size Left  index:9    from 32 To 16
        SetMemory(0x661818, Add, 5),# units:Unit Size Left  index:10    from 11 To 16
        SetMemory(0x661820, Add, -8),# units:Unit Size Left  index:11    from 24 To 16
        SetMemory(0x661828, Add, -21),# units:Unit Size Left  index:12    from 37 To 16
        SetMemory(0x661848, Add, 9),# units:Unit Size Left  index:16    from 7 To 16
        SetMemory(0x661868, Add, 8),# units:Unit Size Left  index:20    from 8 To 16
        SetMemory(0x661870, Add, -3),# units:Unit Size Left  index:21    from 19 To 16
        SetMemory(0x661878, Add, -16),# units:Unit Size Left  index:22    from 32 To 16
        SetMemory(0x6618A0, Add, -21),# units:Unit Size Left  index:27    from 37 To 16
        SetMemory(0x6618A8, Add, -21),# units:Unit Size Left  index:28    from 37 To 16
        SetMemory(0x6618B0, Add, -21),# units:Unit Size Left  index:29    from 37 To 16
        SetMemory(0x6618C8, Add, 5),# units:Unit Size Left  index:32    from 11 To 16
        SetMemory(0x6618D8, Add, 8),# units:Unit Size Left  index:34    from 8 To 16
        SetMemory(0x6618F0, Add, 8),# units:Unit Size Left  index:37    from 8 To 16
        SetMemory(0x6618F8, Add, 6),# units:Unit Size Left  index:38    from 10 To 16
        SetMemory(0x661900, Add, -3),# units:Unit Size Left  index:39    from 19 To 16
        SetMemory(0x661908, Add, 7),# units:Unit Size Left  index:40    from 9 To 16
        SetMemory(0x661910, Add, 5),# units:Unit Size Left  index:41    from 11 To 16
        SetMemory(0x661918, Add, -9),# units:Unit Size Left  index:42    from 25 To 16
        SetMemory(0x661920, Add, -6),# units:Unit Size Left  index:43    from 22 To 16
        SetMemory(0x661928, Add, -6),# units:Unit Size Left  index:44    from 22 To 16
        SetMemory(0x661930, Add, -8),# units:Unit Size Left  index:45    from 24 To 16
        SetMemory(0x661938, Add, 3),# units:Unit Size Left  index:46    from 13 To 16
        SetMemory(0x661940, Add, 4),# units:Unit Size Left  index:47    from 12 To 16
        SetMemory(0x661948, Add, -3),# units:Unit Size Left  index:48    from 19 To 16
        SetMemory(0x661950, Add, -8),# units:Unit Size Left  index:49    from 24 To 16
        SetMemory(0x661958, Add, 8),# units:Unit Size Left  index:50    from 8 To 16
        SetMemory(0x661960, Add, 9),# units:Unit Size Left  index:51    from 7 To 16
        SetMemory(0x661968, Add, 2),# units:Unit Size Left  index:52    from 14 To 16
        SetMemory(0x661970, Add, 6),# units:Unit Size Left  index:53    from 10 To 16
        SetMemory(0x661978, Add, 8),# units:Unit Size Left  index:54    from 8 To 16
        SetMemory(0x661980, Add, -6),# units:Unit Size Left  index:55    from 22 To 16
        SetMemory(0x661988, Add, -6),# units:Unit Size Left  index:56    from 22 To 16
        SetMemory(0x661990, Add, -9),# units:Unit Size Left  index:57    from 25 To 16
        SetMemory(0x6619A8, Add, -2),# units:Unit Size Left  index:60    from 18 To 16
        SetMemory(0x6619B0, Add, 4),# units:Unit Size Left  index:61    from 12 To 16
        SetMemory(0x6619B8, Add, -6),# units:Unit Size Left  index:62    from 22 To 16
        SetMemory(0x6619C8, Add, 5),# units:Unit Size Left  index:64    from 11 To 16
        SetMemory(0x6619D0, Add, 5),# units:Unit Size Left  index:65    from 11 To 16
        SetMemory(0x6619D8, Add, 1),# units:Unit Size Left  index:66    from 15 To 16
        SetMemory(0x6619E0, Add, 4),# units:Unit Size Left  index:67    from 12 To 16
        SetMemory(0x6619F0, Add, -4),# units:Unit Size Left  index:69    from 20 To 16
        SetMemory(0x6619F8, Add, -2),# units:Unit Size Left  index:70    from 18 To 16
        SetMemory(0x661A00, Add, -6),# units:Unit Size Left  index:71    from 22 To 16
        SetMemory(0x661A08, Add, -16),# units:Unit Size Left  index:72    from 32 To 16
        SetMemory(0x661A18, Add, 4),# units:Unit Size Left  index:74    from 12 To 16
        SetMemory(0x661A20, Add, 4),# units:Unit Size Left  index:75    from 12 To 16
        SetMemory(0x661A30, Add, 5),# units:Unit Size Left  index:77    from 11 To 16
        SetMemory(0x661A38, Add, 1),# units:Unit Size Left  index:78    from 15 To 16
        SetMemory(0x661A40, Add, 4),# units:Unit Size Left  index:79    from 12 To 16
        SetMemory(0x661A48, Add, -2),# units:Unit Size Left  index:80    from 18 To 16
        SetMemory(0x661A58, Add, -16),# units:Unit Size Left  index:82    from 32 To 16
        SetMemory(0x661A78, Add, -6),# units:Unit Size Left  index:86    from 22 To 16
        SetMemory(0x661A80, Add, 4),# units:Unit Size Left  index:87    from 12 To 16
        SetMemory(0x661A88, Add, -2),# units:Unit Size Left  index:88    from 18 To 16
        SetMemory(0x661AD8, Add, -8),# units:Unit Size Left  index:98    from 24 To 16
        SetMemory(0x661AE0, Add, 9),# units:Unit Size Left  index:99    from 7 To 16
        SetMemory(0x661AE8, Add, 9),# units:Unit Size Left  index:100    from 7 To 16
        SetMemory(0x661AF8, Add, -21),# units:Unit Size Left  index:102    from 37 To 16
        SetMemory(0x661B00, Add, 1),# units:Unit Size Left  index:103    from 15 To 16
        SetMemory(0x661B08, Add, 9),# units:Unit Size Left  index:104    from 7 To 16
        SetMemory(0x661B18, Add, -42),# units:Unit Size Left  index:106    from 58 To 16
        SetMemory(0x661B20, Add, -21),# units:Unit Size Left  index:107    from 37 To 16
        SetMemory(0x661B30, Add, -22),# units:Unit Size Left  index:109    from 38 To 16
        SetMemory(0x661B38, Add, -40),# units:Unit Size Left  index:110    from 56 To 16
        SetMemory(0x661B40, Add, -32),# units:Unit Size Left  index:111    from 48 To 16
        SetMemory(0x661B48, Add, -24),# units:Unit Size Left  index:112    from 40 To 16
        SetMemory(0x661B50, Add, -40),# units:Unit Size Left  index:113    from 56 To 16
        SetMemory(0x661B58, Add, -32),# units:Unit Size Left  index:114    from 48 To 16
        SetMemory(0x661B60, Add, -31),# units:Unit Size Left  index:115    from 47 To 16
        SetMemory(0x661B68, Add, -32),# units:Unit Size Left  index:116    from 48 To 16
        SetMemory(0x661B70, Add, -31),# units:Unit Size Left  index:117    from 47 To 16
        SetMemory(0x661B78, Add, -31),# units:Unit Size Left  index:118    from 47 To 16
        SetMemory(0x661B88, Add, -23),# units:Unit Size Left  index:120    from 39 To 16
        SetMemory(0x661B98, Add, -32),# units:Unit Size Left  index:122    from 48 To 16
        SetMemory(0x661BA0, Add, -32),# units:Unit Size Left  index:123    from 48 To 16
        SetMemory(0x661BB0, Add, -16),# units:Unit Size Left  index:125    from 32 To 16
        SetMemory(0x661BB8, Add, -32),# units:Unit Size Left  index:126    from 48 To 16
        SetMemory(0x661BC0, Add, -32),# units:Unit Size Left  index:127    from 48 To 16
        SetMemory(0x661BD8, Add, -42),# units:Unit Size Left  index:130    from 58 To 16
        SetMemory(0x661BE0, Add, -33),# units:Unit Size Left  index:131    from 49 To 16
        SetMemory(0x661BE8, Add, -33),# units:Unit Size Left  index:132    from 49 To 16
        SetMemory(0x661BF0, Add, -33),# units:Unit Size Left  index:133    from 49 To 16
        SetMemory(0x661BF8, Add, -16),# units:Unit Size Left  index:134    from 32 To 16
        SetMemory(0x661C00, Add, -24),# units:Unit Size Left  index:135    from 40 To 16
        SetMemory(0x661C08, Add, -32),# units:Unit Size Left  index:136    from 48 To 16
        SetMemory(0x661C10, Add, -12),# units:Unit Size Left  index:137    from 28 To 16
        SetMemory(0x661C18, Add, -22),# units:Unit Size Left  index:138    from 38 To 16
        SetMemory(0x661C20, Add, -28),# units:Unit Size Left  index:139    from 44 To 16
        SetMemory(0x661C28, Add, -24),# units:Unit Size Left  index:140    from 40 To 16
        SetMemory(0x661C30, Add, -12),# units:Unit Size Left  index:141    from 28 To 16
        SetMemory(0x661C38, Add, -20),# units:Unit Size Left  index:142    from 36 To 16
        SetMemory(0x661C40, Add, -8),# units:Unit Size Left  index:143    from 24 To 16
        SetMemory(0x661C48, Add, -8),# units:Unit Size Left  index:144    from 24 To 16
        SetMemory(0x661C58, Add, -8),# units:Unit Size Left  index:146    from 24 To 16
        SetMemory(0x661C60, Add, -64),# units:Unit Size Left  index:147    from 80 To 16
        SetMemory(0x661C68, Add, -64),# units:Unit Size Left  index:148    from 80 To 16
        SetMemory(0x661C70, Add, -48),# units:Unit Size Left  index:149    from 64 To 16
        SetMemory(0x661C78, Add, -16),# units:Unit Size Left  index:150    from 32 To 16
        SetMemory(0x661C80, Add, -24),# units:Unit Size Left  index:151    from 40 To 16
        SetMemory(0x661C88, Add, -24),# units:Unit Size Left  index:152    from 40 To 16
        SetMemory(0x661C98, Add, -40),# units:Unit Size Left  index:154    from 56 To 16
        SetMemory(0x661CA0, Add, -20),# units:Unit Size Left  index:155    from 36 To 16
        SetMemory(0x661CB0, Add, -32),# units:Unit Size Left  index:157    from 48 To 16
        SetMemory(0x661CC0, Add, -28),# units:Unit Size Left  index:159    from 44 To 16
        SetMemory(0x661CC8, Add, -32),# units:Unit Size Left  index:160    from 48 To 16
        SetMemory(0x661CD8, Add, -4),# units:Unit Size Left  index:162    from 20 To 16
        SetMemory(0x661CE0, Add, -8),# units:Unit Size Left  index:163    from 24 To 16
        SetMemory(0x661CE8, Add, -24),# units:Unit Size Left  index:164    from 40 To 16
        SetMemory(0x661CF0, Add, -16),# units:Unit Size Left  index:165    from 32 To 16
        SetMemory(0x661CF8, Add, -20),# units:Unit Size Left  index:166    from 36 To 16
        SetMemory(0x661D00, Add, -32),# units:Unit Size Left  index:167    from 48 To 16
        SetMemory(0x661D08, Add, -48),# units:Unit Size Left  index:168    from 64 To 16
        SetMemory(0x661D10, Add, -24),# units:Unit Size Left  index:169    from 40 To 16
        SetMemory(0x661D18, Add, -28),# units:Unit Size Left  index:170    from 44 To 16
        SetMemory(0x661D20, Add, -16),# units:Unit Size Left  index:171    from 32 To 16
        SetMemory(0x661D28, Add, -16),# units:Unit Size Left  index:172    from 32 To 16
        SetMemory(0x661D30, Add, -48),# units:Unit Size Left  index:173    from 64 To 16
        SetMemory(0x661D38, Add, -96),# units:Unit Size Left  index:174    from 112 To 16
        SetMemory(0x661D40, Add, -64),# units:Unit Size Left  index:175    from 80 To 16
        SetMemory(0x661DB0, Add, -32),# units:Unit Size Left  index:189    from 48 To 16
        SetMemory(0x661DB8, Add, -64),# units:Unit Size Left  index:190    from 80 To 16
        SetMemory(0x661DD8, Add, -32),# units:Unit Size Left  index:194    from 48 To 16
        SetMemory(0x661DE0, Add, -32),# units:Unit Size Left  index:195    from 48 To 16
        SetMemory(0x661DE8, Add, -32),# units:Unit Size Left  index:196    from 48 To 16
        SetMemory(0x661E08, Add, -40),# units:Unit Size Left  index:200    from 56 To 16
        SetMemory(0x661E10, Add, -32),# units:Unit Size Left  index:201    from 48 To 16
        SetMemory(0x6617D0, Add, 393216),# units:Unit Size Up  index:1    from 10 To 16
        SetMemory(0x661800, Add, 327680),# units:Unit Size Up  index:7    from 11 To 16
        SetMemory(0x661808, Add, 65536),# units:Unit Size Up  index:8    from 15 To 16
        SetMemory(0x661810, Add, -1114112),# units:Unit Size Up  index:9    from 33 To 16
        SetMemory(0x661818, Add, 196608),# units:Unit Size Up  index:10    from 13 To 16
        SetMemory(0x661828, Add, -851968),# units:Unit Size Up  index:12    from 29 To 16
        SetMemory(0x661848, Add, 393216),# units:Unit Size Up  index:16    from 10 To 16
        SetMemory(0x661868, Add, 458752),# units:Unit Size Up  index:20    from 9 To 16
        SetMemory(0x661870, Add, 65536),# units:Unit Size Up  index:21    from 15 To 16
        SetMemory(0x661878, Add, -1114112),# units:Unit Size Up  index:22    from 33 To 16
        SetMemory(0x6618A0, Add, -851968),# units:Unit Size Up  index:27    from 29 To 16
        SetMemory(0x6618A8, Add, -851968),# units:Unit Size Up  index:28    from 29 To 16
        SetMemory(0x6618B0, Add, -851968),# units:Unit Size Up  index:29    from 29 To 16
        SetMemory(0x6618C8, Add, 589824),# units:Unit Size Up  index:32    from 7 To 16
        SetMemory(0x6618D8, Add, 458752),# units:Unit Size Up  index:34    from 9 To 16
        SetMemory(0x6618F0, Add, 786432),# units:Unit Size Up  index:37    from 4 To 16
        SetMemory(0x6618F8, Add, 393216),# units:Unit Size Up  index:38    from 10 To 16
        SetMemory(0x661908, Add, 458752),# units:Unit Size Up  index:40    from 9 To 16
        SetMemory(0x661910, Add, 327680),# units:Unit Size Up  index:41    from 11 To 16
        SetMemory(0x661918, Add, -589824),# units:Unit Size Up  index:42    from 25 To 16
        SetMemory(0x661920, Add, -393216),# units:Unit Size Up  index:43    from 22 To 16
        SetMemory(0x661928, Add, -393216),# units:Unit Size Up  index:44    from 22 To 16
        SetMemory(0x661930, Add, -524288),# units:Unit Size Up  index:45    from 24 To 16
        SetMemory(0x661938, Add, 262144),# units:Unit Size Up  index:46    from 12 To 16
        SetMemory(0x661940, Add, 262144),# units:Unit Size Up  index:47    from 12 To 16
        SetMemory(0x661950, Add, -524288),# units:Unit Size Up  index:49    from 24 To 16
        SetMemory(0x661958, Add, 458752),# units:Unit Size Up  index:50    from 9 To 16
        SetMemory(0x661960, Add, 393216),# units:Unit Size Up  index:51    from 10 To 16
        SetMemory(0x661968, Add, 131072),# units:Unit Size Up  index:52    from 14 To 16
        SetMemory(0x661970, Add, 393216),# units:Unit Size Up  index:53    from 10 To 16
        SetMemory(0x661978, Add, 786432),# units:Unit Size Up  index:54    from 4 To 16
        SetMemory(0x661980, Add, -393216),# units:Unit Size Up  index:55    from 22 To 16
        SetMemory(0x661988, Add, -393216),# units:Unit Size Up  index:56    from 22 To 16
        SetMemory(0x661990, Add, -589824),# units:Unit Size Up  index:57    from 25 To 16
        SetMemory(0x6619B0, Add, 655360),# units:Unit Size Up  index:61    from 6 To 16
        SetMemory(0x6619B8, Add, -393216),# units:Unit Size Up  index:62    from 22 To 16
        SetMemory(0x6619C8, Add, 327680),# units:Unit Size Up  index:64    from 11 To 16
        SetMemory(0x6619D0, Add, 720896),# units:Unit Size Up  index:65    from 5 To 16
        SetMemory(0x6619D8, Add, 65536),# units:Unit Size Up  index:66    from 15 To 16
        SetMemory(0x6619E0, Add, 393216),# units:Unit Size Up  index:67    from 10 To 16
        SetMemory(0x661A00, Add, -393216),# units:Unit Size Up  index:71    from 22 To 16
        SetMemory(0x661A08, Add, -1048576),# units:Unit Size Up  index:72    from 32 To 16
        SetMemory(0x661A18, Add, 655360),# units:Unit Size Up  index:74    from 6 To 16
        SetMemory(0x661A20, Add, 655360),# units:Unit Size Up  index:75    from 6 To 16
        SetMemory(0x661A30, Add, 720896),# units:Unit Size Up  index:77    from 5 To 16
        SetMemory(0x661A38, Add, 65536),# units:Unit Size Up  index:78    from 15 To 16
        SetMemory(0x661A40, Add, 393216),# units:Unit Size Up  index:79    from 10 To 16
        SetMemory(0x661A58, Add, -1048576),# units:Unit Size Up  index:82    from 32 To 16
        SetMemory(0x661A78, Add, -393216),# units:Unit Size Up  index:86    from 22 To 16
        SetMemory(0x661A80, Add, 131072),# units:Unit Size Up  index:87    from 14 To 16
        SetMemory(0x661AE0, Add, 393216),# units:Unit Size Up  index:99    from 10 To 16
        SetMemory(0x661AE8, Add, 393216),# units:Unit Size Up  index:100    from 10 To 16
        SetMemory(0x661AF8, Add, -851968),# units:Unit Size Up  index:102    from 29 To 16
        SetMemory(0x661B00, Add, 65536),# units:Unit Size Up  index:103    from 15 To 16
        SetMemory(0x661B08, Add, 393216),# units:Unit Size Up  index:104    from 10 To 16
        SetMemory(0x661B18, Add, -1638400),# units:Unit Size Up  index:106    from 41 To 16
        SetMemory(0x661B30, Add, -393216),# units:Unit Size Up  index:109    from 22 To 16
        SetMemory(0x661B38, Add, -1048576),# units:Unit Size Up  index:110    from 32 To 16
        SetMemory(0x661B40, Add, -1572864),# units:Unit Size Up  index:111    from 40 To 16
        SetMemory(0x661B48, Add, -1048576),# units:Unit Size Up  index:112    from 32 To 16
        SetMemory(0x661B50, Add, -1572864),# units:Unit Size Up  index:113    from 40 To 16
        SetMemory(0x661B58, Add, -1572864),# units:Unit Size Up  index:114    from 40 To 16
        SetMemory(0x661B60, Add, -524288),# units:Unit Size Up  index:115    from 24 To 16
        SetMemory(0x661B68, Add, -1441792),# units:Unit Size Up  index:116    from 38 To 16
        SetMemory(0x661B70, Add, -524288),# units:Unit Size Up  index:117    from 24 To 16
        SetMemory(0x661B78, Add, -524288),# units:Unit Size Up  index:118    from 24 To 16
        SetMemory(0x661B88, Add, -524288),# units:Unit Size Up  index:120    from 24 To 16
        SetMemory(0x661B98, Add, -1048576),# units:Unit Size Up  index:122    from 32 To 16
        SetMemory(0x661BA0, Add, -1048576),# units:Unit Size Up  index:123    from 32 To 16
        SetMemory(0x661BA8, Add, -1048576),# units:Unit Size Up  index:124    from 32 To 16
        SetMemory(0x661BB0, Add, -524288),# units:Unit Size Up  index:125    from 24 To 16
        SetMemory(0x661BB8, Add, -1048576),# units:Unit Size Up  index:126    from 32 To 16
        SetMemory(0x661BC0, Add, -1048576),# units:Unit Size Up  index:127    from 32 To 16
        SetMemory(0x661BD8, Add, -1638400),# units:Unit Size Up  index:130    from 41 To 16
        SetMemory(0x661BE0, Add, -1048576),# units:Unit Size Up  index:131    from 32 To 16
        SetMemory(0x661BE8, Add, -1048576),# units:Unit Size Up  index:132    from 32 To 16
        SetMemory(0x661BF0, Add, -1048576),# units:Unit Size Up  index:133    from 32 To 16
        SetMemory(0x661BF8, Add, -1048576),# units:Unit Size Up  index:134    from 32 To 16
        SetMemory(0x661C00, Add, -1048576),# units:Unit Size Up  index:135    from 32 To 16
        SetMemory(0x661C08, Add, -1048576),# units:Unit Size Up  index:136    from 32 To 16
        SetMemory(0x661C10, Add, -1048576),# units:Unit Size Up  index:137    from 32 To 16
        SetMemory(0x661C18, Add, -786432),# units:Unit Size Up  index:138    from 28 To 16
        SetMemory(0x661C20, Add, -1048576),# units:Unit Size Up  index:139    from 32 To 16
        SetMemory(0x661C28, Add, -1048576),# units:Unit Size Up  index:140    from 32 To 16
        SetMemory(0x661C30, Add, -1048576),# units:Unit Size Up  index:141    from 32 To 16
        SetMemory(0x661C38, Add, -786432),# units:Unit Size Up  index:142    from 28 To 16
        SetMemory(0x661C40, Add, -524288),# units:Unit Size Up  index:143    from 24 To 16
        SetMemory(0x661C48, Add, -524288),# units:Unit Size Up  index:144    from 24 To 16
        SetMemory(0x661C58, Add, -524288),# units:Unit Size Up  index:146    from 24 To 16
        SetMemory(0x661C60, Add, -1048576),# units:Unit Size Up  index:147    from 32 To 16
        SetMemory(0x661C68, Add, -1048576),# units:Unit Size Up  index:148    from 32 To 16
        SetMemory(0x661C70, Add, -1048576),# units:Unit Size Up  index:149    from 32 To 16
        SetMemory(0x661C78, Add, -1048576),# units:Unit Size Up  index:150    from 32 To 16
        SetMemory(0x661C80, Add, -1048576),# units:Unit Size Up  index:151    from 32 To 16
        SetMemory(0x661C88, Add, -1048576),# units:Unit Size Up  index:152    from 32 To 16
        SetMemory(0x661C98, Add, -1507328),# units:Unit Size Up  index:154    from 39 To 16
        SetMemory(0x661CA8, Add, 262144),# units:Unit Size Up  index:156    from 12 To 16
        SetMemory(0x661CB0, Add, -1048576),# units:Unit Size Up  index:157    from 32 To 16
        SetMemory(0x661CC8, Add, -1048576),# units:Unit Size Up  index:160    from 32 To 16
        SetMemory(0x661CE0, Add, -524288),# units:Unit Size Up  index:163    from 24 To 16
        SetMemory(0x661CE8, Add, -524288),# units:Unit Size Up  index:164    from 24 To 16
        SetMemory(0x661CF0, Add, -524288),# units:Unit Size Up  index:165    from 24 To 16
        SetMemory(0x661CF8, Add, -524288),# units:Unit Size Up  index:166    from 24 To 16
        SetMemory(0x661D00, Add, -1572864),# units:Unit Size Up  index:167    from 40 To 16
        SetMemory(0x661D08, Add, -2097152),# units:Unit Size Up  index:168    from 48 To 16
        SetMemory(0x661D10, Add, -1048576),# units:Unit Size Up  index:169    from 32 To 16
        SetMemory(0x661D18, Add, -786432),# units:Unit Size Up  index:170    from 28 To 16
        SetMemory(0x661D20, Add, -1048576),# units:Unit Size Up  index:171    from 32 To 16
        SetMemory(0x661D30, Add, -2097152),# units:Unit Size Up  index:173    from 48 To 16
        SetMemory(0x661D38, Add, -2097152),# units:Unit Size Up  index:174    from 48 To 16
        SetMemory(0x661D40, Add, -1179648),# units:Unit Size Up  index:175    from 34 To 16
        SetMemory(0x661DB0, Add, -1048576),# units:Unit Size Up  index:189    from 32 To 16
        SetMemory(0x661DB8, Add, -1441792),# units:Unit Size Up  index:190    from 38 To 16
        SetMemory(0x661DD8, Add, -1048576),# units:Unit Size Up  index:194    from 32 To 16
        SetMemory(0x661DE0, Add, -1048576),# units:Unit Size Up  index:195    from 32 To 16
        SetMemory(0x661DE8, Add, -1048576),# units:Unit Size Up  index:196    from 32 To 16
        SetMemory(0x661E08, Add, -786432),# units:Unit Size Up  index:200    from 28 To 16
        SetMemory(0x661E10, Add, -1048576),# units:Unit Size Up  index:201    from 32 To 16
        SetMemory(0x6617D4, Add, 8),# units:Unit Size Right  index:1    from 7 To 15
        SetMemory(0x661804, Add, 4),# units:Unit Size Right  index:7    from 11 To 15
        SetMemory(0x66180C, Add, -3),# units:Unit Size Right  index:8    from 18 To 15
        SetMemory(0x661814, Add, -17),# units:Unit Size Right  index:9    from 32 To 15
        SetMemory(0x66181C, Add, 4),# units:Unit Size Right  index:10    from 11 To 15
        SetMemory(0x661824, Add, -9),# units:Unit Size Right  index:11    from 24 To 15
        SetMemory(0x66182C, Add, -22),# units:Unit Size Right  index:12    from 37 To 15
        SetMemory(0x66184C, Add, 8),# units:Unit Size Right  index:16    from 7 To 15
        SetMemory(0x66186C, Add, 7),# units:Unit Size Right  index:20    from 8 To 15
        SetMemory(0x661874, Add, -3),# units:Unit Size Right  index:21    from 18 To 15
        SetMemory(0x66187C, Add, -17),# units:Unit Size Right  index:22    from 32 To 15
        SetMemory(0x6618A4, Add, -22),# units:Unit Size Right  index:27    from 37 To 15
        SetMemory(0x6618AC, Add, -22),# units:Unit Size Right  index:28    from 37 To 15
        SetMemory(0x6618B4, Add, -22),# units:Unit Size Right  index:29    from 37 To 15
        SetMemory(0x6618CC, Add, 4),# units:Unit Size Right  index:32    from 11 To 15
        SetMemory(0x6618DC, Add, 7),# units:Unit Size Right  index:34    from 8 To 15
        SetMemory(0x6618F4, Add, 8),# units:Unit Size Right  index:37    from 7 To 15
        SetMemory(0x6618FC, Add, 5),# units:Unit Size Right  index:38    from 10 To 15
        SetMemory(0x661904, Add, -3),# units:Unit Size Right  index:39    from 18 To 15
        SetMemory(0x66190C, Add, 6),# units:Unit Size Right  index:40    from 9 To 15
        SetMemory(0x661914, Add, 4),# units:Unit Size Right  index:41    from 11 To 15
        SetMemory(0x66191C, Add, -9),# units:Unit Size Right  index:42    from 24 To 15
        SetMemory(0x661924, Add, -6),# units:Unit Size Right  index:43    from 21 To 15
        SetMemory(0x66192C, Add, -6),# units:Unit Size Right  index:44    from 21 To 15
        SetMemory(0x661934, Add, -8),# units:Unit Size Right  index:45    from 23 To 15
        SetMemory(0x66193C, Add, 2),# units:Unit Size Right  index:46    from 13 To 15
        SetMemory(0x661944, Add, 4),# units:Unit Size Right  index:47    from 11 To 15
        SetMemory(0x66194C, Add, -3),# units:Unit Size Right  index:48    from 18 To 15
        SetMemory(0x661954, Add, -8),# units:Unit Size Right  index:49    from 23 To 15
        SetMemory(0x66195C, Add, 7),# units:Unit Size Right  index:50    from 8 To 15
        SetMemory(0x661964, Add, 8),# units:Unit Size Right  index:51    from 7 To 15
        SetMemory(0x66196C, Add, 1),# units:Unit Size Right  index:52    from 14 To 15
        SetMemory(0x661974, Add, 5),# units:Unit Size Right  index:53    from 10 To 15
        SetMemory(0x66197C, Add, 8),# units:Unit Size Right  index:54    from 7 To 15
        SetMemory(0x661984, Add, -6),# units:Unit Size Right  index:55    from 21 To 15
        SetMemory(0x66198C, Add, -6),# units:Unit Size Right  index:56    from 21 To 15
        SetMemory(0x661994, Add, -9),# units:Unit Size Right  index:57    from 24 To 15
        SetMemory(0x6619AC, Add, -2),# units:Unit Size Right  index:60    from 17 To 15
        SetMemory(0x6619B4, Add, 4),# units:Unit Size Right  index:61    from 11 To 15
        SetMemory(0x6619BC, Add, -6),# units:Unit Size Right  index:62    from 21 To 15
        SetMemory(0x6619CC, Add, 4),# units:Unit Size Right  index:64    from 11 To 15
        SetMemory(0x6619D4, Add, 4),# units:Unit Size Right  index:65    from 11 To 15
        SetMemory(0x6619DC, Add, -1),# units:Unit Size Right  index:66    from 16 To 15
        SetMemory(0x6619E4, Add, 4),# units:Unit Size Right  index:67    from 11 To 15
        SetMemory(0x6619F4, Add, -4),# units:Unit Size Right  index:69    from 19 To 15
        SetMemory(0x6619FC, Add, -2),# units:Unit Size Right  index:70    from 17 To 15
        SetMemory(0x661A04, Add, -6),# units:Unit Size Right  index:71    from 21 To 15
        SetMemory(0x661A0C, Add, -16),# units:Unit Size Right  index:72    from 31 To 15
        SetMemory(0x661A1C, Add, 4),# units:Unit Size Right  index:74    from 11 To 15
        SetMemory(0x661A24, Add, 4),# units:Unit Size Right  index:75    from 11 To 15
        SetMemory(0x661A34, Add, 4),# units:Unit Size Right  index:77    from 11 To 15
        SetMemory(0x661A3C, Add, -1),# units:Unit Size Right  index:78    from 16 To 15
        SetMemory(0x661A44, Add, 4),# units:Unit Size Right  index:79    from 11 To 15
        SetMemory(0x661A4C, Add, -2),# units:Unit Size Right  index:80    from 17 To 15
        SetMemory(0x661A5C, Add, -16),# units:Unit Size Right  index:82    from 31 To 15
        SetMemory(0x661A7C, Add, -6),# units:Unit Size Right  index:86    from 21 To 15
        SetMemory(0x661A84, Add, 4),# units:Unit Size Right  index:87    from 11 To 15
        SetMemory(0x661A8C, Add, -2),# units:Unit Size Right  index:88    from 17 To 15
        SetMemory(0x661ADC, Add, -9),# units:Unit Size Right  index:98    from 24 To 15
        SetMemory(0x661AE4, Add, 8),# units:Unit Size Right  index:99    from 7 To 15
        SetMemory(0x661AEC, Add, 8),# units:Unit Size Right  index:100    from 7 To 15
        SetMemory(0x661AFC, Add, -22),# units:Unit Size Right  index:102    from 37 To 15
        SetMemory(0x661B04, Add, -1),# units:Unit Size Right  index:103    from 16 To 15
        SetMemory(0x661B0C, Add, 8),# units:Unit Size Right  index:104    from 7 To 15
        SetMemory(0x661B1C, Add, -43),# units:Unit Size Right  index:106    from 58 To 15
        SetMemory(0x661B24, Add, -16),# units:Unit Size Right  index:107    from 31 To 15
        SetMemory(0x661B34, Add, -23),# units:Unit Size Right  index:109    from 38 To 15
        SetMemory(0x661B3C, Add, -41),# units:Unit Size Right  index:110    from 56 To 15
        SetMemory(0x661B44, Add, -41),# units:Unit Size Right  index:111    from 56 To 15
        SetMemory(0x661B4C, Add, -29),# units:Unit Size Right  index:112    from 44 To 15
        SetMemory(0x661B54, Add, -41),# units:Unit Size Right  index:113    from 56 To 15
        SetMemory(0x661B5C, Add, -33),# units:Unit Size Right  index:114    from 48 To 15
        SetMemory(0x661B64, Add, -13),# units:Unit Size Right  index:115    from 28 To 15
        SetMemory(0x661B6C, Add, -33),# units:Unit Size Right  index:116    from 48 To 15
        SetMemory(0x661B74, Add, -13),# units:Unit Size Right  index:117    from 28 To 15
        SetMemory(0x661B7C, Add, -13),# units:Unit Size Right  index:118    from 28 To 15
        SetMemory(0x661B8C, Add, -16),# units:Unit Size Right  index:120    from 31 To 15
        SetMemory(0x661B9C, Add, -33),# units:Unit Size Right  index:122    from 48 To 15
        SetMemory(0x661BA4, Add, -32),# units:Unit Size Right  index:123    from 47 To 15
        SetMemory(0x661BAC, Add, -1),# units:Unit Size Right  index:124    from 16 To 15
        SetMemory(0x661BB4, Add, -17),# units:Unit Size Right  index:125    from 32 To 15
        SetMemory(0x661BBC, Add, -32),# units:Unit Size Right  index:126    from 47 To 15
        SetMemory(0x661BC4, Add, -32),# units:Unit Size Right  index:127    from 47 To 15
        SetMemory(0x661BDC, Add, -43),# units:Unit Size Right  index:130    from 58 To 15
        SetMemory(0x661BE4, Add, -34),# units:Unit Size Right  index:131    from 49 To 15
        SetMemory(0x661BEC, Add, -34),# units:Unit Size Right  index:132    from 49 To 15
        SetMemory(0x661BF4, Add, -34),# units:Unit Size Right  index:133    from 49 To 15
        SetMemory(0x661BFC, Add, -16),# units:Unit Size Right  index:134    from 31 To 15
        SetMemory(0x661C04, Add, -25),# units:Unit Size Right  index:135    from 40 To 15
        SetMemory(0x661C0C, Add, -33),# units:Unit Size Right  index:136    from 48 To 15
        SetMemory(0x661C14, Add, -13),# units:Unit Size Right  index:137    from 28 To 15
        SetMemory(0x661C1C, Add, -17),# units:Unit Size Right  index:138    from 32 To 15
        SetMemory(0x661C24, Add, -17),# units:Unit Size Right  index:139    from 32 To 15
        SetMemory(0x661C2C, Add, -17),# units:Unit Size Right  index:140    from 32 To 15
        SetMemory(0x661C34, Add, -13),# units:Unit Size Right  index:141    from 28 To 15
        SetMemory(0x661C3C, Add, -25),# units:Unit Size Right  index:142    from 40 To 15
        SetMemory(0x661C44, Add, -8),# units:Unit Size Right  index:143    from 23 To 15
        SetMemory(0x661C4C, Add, -8),# units:Unit Size Right  index:144    from 23 To 15
        SetMemory(0x661C5C, Add, -8),# units:Unit Size Right  index:146    from 23 To 15
        SetMemory(0x661C64, Add, -64),# units:Unit Size Right  index:147    from 79 To 15
        SetMemory(0x661C6C, Add, -64),# units:Unit Size Right  index:148    from 79 To 15
        SetMemory(0x661C74, Add, -48),# units:Unit Size Right  index:149    from 63 To 15
        SetMemory(0x661C7C, Add, -16),# units:Unit Size Right  index:150    from 31 To 15
        SetMemory(0x661C84, Add, -17),# units:Unit Size Right  index:151    from 32 To 15
        SetMemory(0x661C8C, Add, -17),# units:Unit Size Right  index:152    from 32 To 15
        SetMemory(0x661C9C, Add, -41),# units:Unit Size Right  index:154    from 56 To 15
        SetMemory(0x661CA4, Add, -25),# units:Unit Size Right  index:155    from 40 To 15
        SetMemory(0x661CAC, Add, -1),# units:Unit Size Right  index:156    from 16 To 15
        SetMemory(0x661CB4, Add, -33),# units:Unit Size Right  index:157    from 48 To 15
        SetMemory(0x661CC4, Add, -29),# units:Unit Size Right  index:159    from 44 To 15
        SetMemory(0x661CCC, Add, -33),# units:Unit Size Right  index:160    from 48 To 15
        SetMemory(0x661CDC, Add, -5),# units:Unit Size Right  index:162    from 20 To 15
        SetMemory(0x661CE4, Add, -25),# units:Unit Size Right  index:163    from 40 To 15
        SetMemory(0x661CEC, Add, -25),# units:Unit Size Right  index:164    from 40 To 15
        SetMemory(0x661CF4, Add, -17),# units:Unit Size Right  index:165    from 32 To 15
        SetMemory(0x661CFC, Add, -21),# units:Unit Size Right  index:166    from 36 To 15
        SetMemory(0x661D04, Add, -33),# units:Unit Size Right  index:167    from 48 To 15
        SetMemory(0x661D0C, Add, -48),# units:Unit Size Right  index:168    from 63 To 15
        SetMemory(0x661D14, Add, -32),# units:Unit Size Right  index:169    from 47 To 15
        SetMemory(0x661D1C, Add, -29),# units:Unit Size Right  index:170    from 44 To 15
        SetMemory(0x661D24, Add, -17),# units:Unit Size Right  index:171    from 32 To 15
        SetMemory(0x661D2C, Add, -17),# units:Unit Size Right  index:172    from 32 To 15
        SetMemory(0x661D34, Add, -48),# units:Unit Size Right  index:173    from 63 To 15
        SetMemory(0x661D3C, Add, -96),# units:Unit Size Right  index:174    from 111 To 15
        SetMemory(0x661D44, Add, -64),# units:Unit Size Right  index:175    from 79 To 15
        SetMemory(0x661DB4, Add, -32),# units:Unit Size Right  index:189    from 47 To 15
        SetMemory(0x661DBC, Add, -54),# units:Unit Size Right  index:190    from 69 To 15
        SetMemory(0x661DDC, Add, -32),# units:Unit Size Right  index:194    from 47 To 15
        SetMemory(0x661DE4, Add, -32),# units:Unit Size Right  index:195    from 47 To 15
        SetMemory(0x661DEC, Add, -32),# units:Unit Size Right  index:196    from 47 To 15
        SetMemory(0x661E0C, Add, -48),# units:Unit Size Right  index:200    from 63 To 15
        SetMemory(0x661E14, Add, -32),# units:Unit Size Right  index:201    from 47 To 15
        SetMemory(0x6617D4, Add, 262144),# units:Unit Size Down  index:1    from 11 To 15
        SetMemory(0x661804, Add, 262144),# units:Unit Size Down  index:7    from 11 To 15
        SetMemory(0x66180C, Add, 65536),# units:Unit Size Down  index:8    from 14 To 15
        SetMemory(0x661814, Add, -65536),# units:Unit Size Down  index:9    from 16 To 15
        SetMemory(0x66181C, Add, 65536),# units:Unit Size Down  index:10    from 14 To 15
        SetMemory(0x661824, Add, -327680),# units:Unit Size Down  index:11    from 20 To 15
        SetMemory(0x66182C, Add, -917504),# units:Unit Size Down  index:12    from 29 To 15
        SetMemory(0x66184C, Add, 262144),# units:Unit Size Down  index:16    from 11 To 15
        SetMemory(0x66186C, Add, 327680),# units:Unit Size Down  index:20    from 10 To 15
        SetMemory(0x661874, Add, 65536),# units:Unit Size Down  index:21    from 14 To 15
        SetMemory(0x66187C, Add, -65536),# units:Unit Size Down  index:22    from 16 To 15
        SetMemory(0x6618A4, Add, -917504),# units:Unit Size Down  index:27    from 29 To 15
        SetMemory(0x6618AC, Add, -917504),# units:Unit Size Down  index:28    from 29 To 15
        SetMemory(0x6618B4, Add, -917504),# units:Unit Size Down  index:29    from 29 To 15
        SetMemory(0x6618CC, Add, 65536),# units:Unit Size Down  index:32    from 14 To 15
        SetMemory(0x6618DC, Add, 327680),# units:Unit Size Down  index:34    from 10 To 15
        SetMemory(0x6618F4, Add, 262144),# units:Unit Size Down  index:37    from 11 To 15
        SetMemory(0x6618FC, Add, 196608),# units:Unit Size Down  index:38    from 12 To 15
        SetMemory(0x66190C, Add, 393216),# units:Unit Size Down  index:40    from 9 To 15
        SetMemory(0x661914, Add, 262144),# units:Unit Size Down  index:41    from 11 To 15
        SetMemory(0x66191C, Add, -589824),# units:Unit Size Down  index:42    from 24 To 15
        SetMemory(0x661924, Add, -393216),# units:Unit Size Down  index:43    from 21 To 15
        SetMemory(0x66192C, Add, -393216),# units:Unit Size Down  index:44    from 21 To 15
        SetMemory(0x661934, Add, -524288),# units:Unit Size Down  index:45    from 23 To 15
        SetMemory(0x66193C, Add, 196608),# units:Unit Size Down  index:46    from 12 To 15
        SetMemory(0x661944, Add, 262144),# units:Unit Size Down  index:47    from 11 To 15
        SetMemory(0x661954, Add, -524288),# units:Unit Size Down  index:49    from 23 To 15
        SetMemory(0x66195C, Add, 327680),# units:Unit Size Down  index:50    from 10 To 15
        SetMemory(0x661964, Add, 262144),# units:Unit Size Down  index:51    from 11 To 15
        SetMemory(0x66196C, Add, 65536),# units:Unit Size Down  index:52    from 14 To 15
        SetMemory(0x661974, Add, 196608),# units:Unit Size Down  index:53    from 12 To 15
        SetMemory(0x66197C, Add, 262144),# units:Unit Size Down  index:54    from 11 To 15
        SetMemory(0x661984, Add, -393216),# units:Unit Size Down  index:55    from 21 To 15
        SetMemory(0x66198C, Add, -393216),# units:Unit Size Down  index:56    from 21 To 15
        SetMemory(0x661994, Add, -589824),# units:Unit Size Down  index:57    from 24 To 15
        SetMemory(0x6619B4, Add, -262144),# units:Unit Size Down  index:61    from 19 To 15
        SetMemory(0x6619BC, Add, -393216),# units:Unit Size Down  index:62    from 21 To 15
        SetMemory(0x6619CC, Add, 262144),# units:Unit Size Down  index:64    from 11 To 15
        SetMemory(0x6619D4, Add, 131072),# units:Unit Size Down  index:65    from 13 To 15
        SetMemory(0x6619DC, Add, -65536),# units:Unit Size Down  index:66    from 16 To 15
        SetMemory(0x6619E4, Add, 131072),# units:Unit Size Down  index:67    from 13 To 15
        SetMemory(0x661A04, Add, -393216),# units:Unit Size Down  index:71    from 21 To 15
        SetMemory(0x661A0C, Add, -1048576),# units:Unit Size Down  index:72    from 31 To 15
        SetMemory(0x661A1C, Add, -262144),# units:Unit Size Down  index:74    from 19 To 15
        SetMemory(0x661A24, Add, -262144),# units:Unit Size Down  index:75    from 19 To 15
        SetMemory(0x661A34, Add, 131072),# units:Unit Size Down  index:77    from 13 To 15
        SetMemory(0x661A3C, Add, -65536),# units:Unit Size Down  index:78    from 16 To 15
        SetMemory(0x661A44, Add, 131072),# units:Unit Size Down  index:79    from 13 To 15
        SetMemory(0x661A5C, Add, -1048576),# units:Unit Size Down  index:82    from 31 To 15
        SetMemory(0x661A7C, Add, -393216),# units:Unit Size Down  index:86    from 21 To 15
        SetMemory(0x661A84, Add, 131072),# units:Unit Size Down  index:87    from 13 To 15
        SetMemory(0x661ADC, Add, -327680),# units:Unit Size Down  index:98    from 20 To 15
        SetMemory(0x661AE4, Add, 262144),# units:Unit Size Down  index:99    from 11 To 15
        SetMemory(0x661AEC, Add, 262144),# units:Unit Size Down  index:100    from 11 To 15
        SetMemory(0x661AFC, Add, -917504),# units:Unit Size Down  index:102    from 29 To 15
        SetMemory(0x661B04, Add, -65536),# units:Unit Size Down  index:103    from 16 To 15
        SetMemory(0x661B0C, Add, 262144),# units:Unit Size Down  index:104    from 11 To 15
        SetMemory(0x661B1C, Add, -1703936),# units:Unit Size Down  index:106    from 41 To 15
        SetMemory(0x661B24, Add, -655360),# units:Unit Size Down  index:107    from 25 To 15
        SetMemory(0x661B34, Add, -720896),# units:Unit Size Down  index:109    from 26 To 15
        SetMemory(0x661B3C, Add, -1048576),# units:Unit Size Down  index:110    from 31 To 15
        SetMemory(0x661B44, Add, -1114112),# units:Unit Size Down  index:111    from 32 To 15
        SetMemory(0x661B4C, Add, -589824),# units:Unit Size Down  index:112    from 24 To 15
        SetMemory(0x661B54, Add, -1638400),# units:Unit Size Down  index:113    from 40 To 15
        SetMemory(0x661B5C, Add, -1507328),# units:Unit Size Down  index:114    from 38 To 15
        SetMemory(0x661B64, Add, -458752),# units:Unit Size Down  index:115    from 22 To 15
        SetMemory(0x661B6C, Add, -1507328),# units:Unit Size Down  index:116    from 38 To 15
        SetMemory(0x661B74, Add, -458752),# units:Unit Size Down  index:117    from 22 To 15
        SetMemory(0x661B7C, Add, -458752),# units:Unit Size Down  index:118    from 22 To 15
        SetMemory(0x661B8C, Add, -589824),# units:Unit Size Down  index:120    from 24 To 15
        SetMemory(0x661B9C, Add, -851968),# units:Unit Size Down  index:122    from 28 To 15
        SetMemory(0x661BA4, Add, -458752),# units:Unit Size Down  index:123    from 22 To 15
        SetMemory(0x661BAC, Add, -65536),# units:Unit Size Down  index:124    from 16 To 15
        SetMemory(0x661BB4, Add, -65536),# units:Unit Size Down  index:125    from 16 To 15
        SetMemory(0x661BBC, Add, -1048576),# units:Unit Size Down  index:126    from 31 To 15
        SetMemory(0x661BC4, Add, -1048576),# units:Unit Size Down  index:127    from 31 To 15
        SetMemory(0x661BDC, Add, -1703936),# units:Unit Size Down  index:130    from 41 To 15
        SetMemory(0x661BE4, Add, -1114112),# units:Unit Size Down  index:131    from 32 To 15
        SetMemory(0x661BEC, Add, -1114112),# units:Unit Size Down  index:132    from 32 To 15
        SetMemory(0x661BF4, Add, -1114112),# units:Unit Size Down  index:133    from 32 To 15
        SetMemory(0x661BFC, Add, -1048576),# units:Unit Size Down  index:134    from 31 To 15
        SetMemory(0x661C04, Add, -589824),# units:Unit Size Down  index:135    from 24 To 15
        SetMemory(0x661C0C, Add, 720896),# units:Unit Size Down  index:136    from 4 To 15
        SetMemory(0x661C14, Add, -589824),# units:Unit Size Down  index:137    from 24 To 15
        SetMemory(0x661C1C, Add, -851968),# units:Unit Size Down  index:138    from 28 To 15
        SetMemory(0x661C24, Add, -327680),# units:Unit Size Down  index:139    from 20 To 15
        SetMemory(0x661C2C, Add, -1048576),# units:Unit Size Down  index:140    from 31 To 15
        SetMemory(0x661C34, Add, -589824),# units:Unit Size Down  index:141    from 24 To 15
        SetMemory(0x661C3C, Add, -196608),# units:Unit Size Down  index:142    from 18 To 15
        SetMemory(0x661C44, Add, -524288),# units:Unit Size Down  index:143    from 23 To 15
        SetMemory(0x661C4C, Add, -524288),# units:Unit Size Down  index:144    from 23 To 15
        SetMemory(0x661C5C, Add, -524288),# units:Unit Size Down  index:146    from 23 To 15
        SetMemory(0x661C64, Add, -1638400),# units:Unit Size Down  index:147    from 40 To 15
        SetMemory(0x661C6C, Add, -1638400),# units:Unit Size Down  index:148    from 40 To 15
        SetMemory(0x661C74, Add, -1048576),# units:Unit Size Down  index:149    from 31 To 15
        SetMemory(0x661C7C, Add, -1048576),# units:Unit Size Down  index:150    from 31 To 15
        SetMemory(0x661C84, Add, -1048576),# units:Unit Size Down  index:151    from 31 To 15
        SetMemory(0x661C8C, Add, -1048576),# units:Unit Size Down  index:152    from 31 To 15
        SetMemory(0x661C9C, Add, -1572864),# units:Unit Size Down  index:154    from 39 To 15
        SetMemory(0x661CA4, Add, -327680),# units:Unit Size Down  index:155    from 20 To 15
        SetMemory(0x661CAC, Add, -327680),# units:Unit Size Down  index:156    from 20 To 15
        SetMemory(0x661CB4, Add, -589824),# units:Unit Size Down  index:157    from 24 To 15
        SetMemory(0x661CC4, Add, -851968),# units:Unit Size Down  index:159    from 28 To 15
        SetMemory(0x661CCC, Add, -1638400),# units:Unit Size Down  index:160    from 40 To 15
        SetMemory(0x661CDC, Add, -65536),# units:Unit Size Down  index:162    from 16 To 15
        SetMemory(0x661CE4, Add, -589824),# units:Unit Size Down  index:163    from 24 To 15
        SetMemory(0x661CEC, Add, -589824),# units:Unit Size Down  index:164    from 24 To 15
        SetMemory(0x661CF4, Add, -589824),# units:Unit Size Down  index:165    from 24 To 15
        SetMemory(0x661CFC, Add, -327680),# units:Unit Size Down  index:166    from 20 To 15
        SetMemory(0x661D04, Add, -1114112),# units:Unit Size Down  index:167    from 32 To 15
        SetMemory(0x661D0C, Add, -2097152),# units:Unit Size Down  index:168    from 47 To 15
        SetMemory(0x661D14, Add, -589824),# units:Unit Size Down  index:169    from 24 To 15
        SetMemory(0x661D1C, Add, -851968),# units:Unit Size Down  index:170    from 28 To 15
        SetMemory(0x661D24, Add, -327680),# units:Unit Size Down  index:171    from 20 To 15
        SetMemory(0x661D2C, Add, -65536),# units:Unit Size Down  index:172    from 16 To 15
        SetMemory(0x661D34, Add, -2097152),# units:Unit Size Down  index:173    from 47 To 15
        SetMemory(0x661D3C, Add, -2097152),# units:Unit Size Down  index:174    from 47 To 15
        SetMemory(0x661D44, Add, -3145728),# units:Unit Size Down  index:175    from 63 To 15
        SetMemory(0x661DB4, Add, -1048576),# units:Unit Size Down  index:189    from 31 To 15
        SetMemory(0x661DBC, Add, -2097152),# units:Unit Size Down  index:190    from 47 To 15
        SetMemory(0x661DDC, Add, -1048576),# units:Unit Size Down  index:194    from 31 To 15
        SetMemory(0x661DE4, Add, -1048576),# units:Unit Size Down  index:195    from 31 To 15
        SetMemory(0x661DEC, Add, -1048576),# units:Unit Size Down  index:196    from 31 To 15
        SetMemory(0x661E0C, Add, -1835008),# units:Unit Size Down  index:200    from 43 To 15
        SetMemory(0x661E14, Add, -1048576),# units:Unit Size Down  index:201    from 31 To 15
        SetMemory(0x662F88, Add, 6750208),# units:Portrait  index:1    from 1 To 104
        SetMemory(0x662F8C, Add, 101),# units:Portrait  index:2    from 3 To 104
        SetMemory(0x662F94, Add, 6422528),# units:Portrait  index:7    from 7 To 105
        SetMemory(0x662F98, Add, 96),# units:Portrait  index:8    from 8 To 104
        SetMemory(0x662F98, Add, 6225920),# units:Portrait  index:9    from 9 To 104
        SetMemory(0x662F9C, Add, 102),# units:Portrait  index:10    from 2 To 104
        SetMemory(0x662F9C, Add, 6160384),# units:Portrait  index:11    from 10 To 104
        SetMemory(0x662FA0, Add, 93),# units:Portrait  index:12    from 11 To 104
        SetMemory(0x662FA8, Add, 92),# units:Portrait  index:16    from 12 To 104
        SetMemory(0x662FAC, Add, 5963776),# units:Portrait  index:19    from 13 To 104
        SetMemory(0x662FB0, Add, 91),# units:Portrait  index:20    from 13 To 104
        SetMemory(0x662FB0, Add, 6291456),# units:Portrait  index:21    from 8 To 104
        SetMemory(0x662FB4, Add, 95),# units:Portrait  index:22    from 9 To 104
        SetMemory(0x662FBC, Add, 5767168),# units:Portrait  index:27    from 16 To 104
        SetMemory(0x662FC0, Add, 91),# units:Portrait  index:28    from 13 To 104
        SetMemory(0x662FC0, Add, 5898240),# units:Portrait  index:29    from 14 To 104
        SetMemory(0x662FC8, Add, 102),# units:Portrait  index:32    from 2 To 104
        SetMemory(0x662FCC, Add, 14),# units:Portrait  index:34    from 90 To 104
        SetMemory(0x662FD0, Add, 5505024),# units:Portrait  index:37    from 20 To 104
        SetMemory(0x662FD4, Add, 83),# units:Portrait  index:38    from 21 To 104
        SetMemory(0x662FD4, Add, 5373952),# units:Portrait  index:39    from 22 To 104
        SetMemory(0x662FD8, Add, 81),# units:Portrait  index:40    from 23 To 104
        SetMemory(0x662FD8, Add, 3670016),# units:Portrait  index:41    from 24 To 80
        SetMemory(0x662FDC, Add, 55),# units:Portrait  index:42    from 25 To 80
        SetMemory(0x662FDC, Add, 3538944),# units:Portrait  index:43    from 26 To 80
        SetMemory(0x662FE0, Add, 53),# units:Portrait  index:44    from 27 To 80
        SetMemory(0x662FE0, Add, 3342336),# units:Portrait  index:45    from 28 To 79
        SetMemory(0x662FE4, Add, 51),# units:Portrait  index:46    from 29 To 80
        SetMemory(0x662FE4, Add, 3276800),# units:Portrait  index:47    from 30 To 80
        SetMemory(0x662FE8, Add, 56),# units:Portrait  index:48    from 22 To 78
        SetMemory(0x662FE8, Add, 3145728),# units:Portrait  index:49    from 28 To 76
        SetMemory(0x662FEC, Add, 43),# units:Portrait  index:50    from 33 To 76
        SetMemory(0x662FEC, Add, 2883584),# units:Portrait  index:51    from 36 To 80
        SetMemory(0x662FF0, Add, 46),# units:Portrait  index:52    from 29 To 75
        SetMemory(0x662FF0, Add, 2818048),# units:Portrait  index:53    from 37 To 80
        SetMemory(0x662FF4, Add, 85),# units:Portrait  index:54    from 20 To 105
        SetMemory(0x662FF4, Add, 5177344),# units:Portrait  index:55    from 26 To 105
        SetMemory(0x662FF8, Add, 78),# units:Portrait  index:56    from 27 To 105
        SetMemory(0x662FF8, Add, 5242880),# units:Portrait  index:57    from 25 To 105
        SetMemory(0x663000, Add, 5),# units:Portrait  index:60    from 100 To 105
        SetMemory(0x663000, Add, 3670016),# units:Portrait  index:61    from 49 To 105
        SetMemory(0x663004, Add, 8),# units:Portrait  index:62    from 97 To 105
        SetMemory(0x663004, Add, 393216),# units:Portrait  index:63    from 99 To 105
        SetMemory(0x663008, Add, 66),# units:Portrait  index:64    from 39 To 105
        SetMemory(0x663008, Add, 4259840),# units:Portrait  index:65    from 40 To 105
        SetMemory(0x66300C, Add, 64),# units:Portrait  index:66    from 41 To 105
        SetMemory(0x66300C, Add, 4128768),# units:Portrait  index:67    from 42 To 105
        SetMemory(0x663010, Add, 62),# units:Portrait  index:68    from 43 To 105
        SetMemory(0x663010, Add, 3997696),# units:Portrait  index:69    from 44 To 105
        SetMemory(0x663014, Add, 60),# units:Portrait  index:70    from 45 To 105
        SetMemory(0x663014, Add, 3866624),# units:Portrait  index:71    from 46 To 105
        SetMemory(0x663018, Add, 58),# units:Portrait  index:72    from 47 To 105
        SetMemory(0x66301C, Add, 56),# units:Portrait  index:74    from 49 To 105
        SetMemory(0x66301C, Add, 3473408),# units:Portrait  index:75    from 52 To 105
        SetMemory(0x663020, Add, 62),# units:Portrait  index:76    from 43 To 105
        SetMemory(0x663020, Add, 3604480),# units:Portrait  index:77    from 50 To 105
        SetMemory(0x663024, Add, 24),# units:Portrait  index:78    from 51 To 75
        SetMemory(0x663024, Add, 1441792),# units:Portrait  index:79    from 53 To 75
        SetMemory(0x663028, Add, 30),# units:Portrait  index:80    from 45 To 75
        SetMemory(0x663028, Add, 1572864),# units:Portrait  index:81    from 56 To 80
        SetMemory(0x66302C, Add, 26),# units:Portrait  index:82    from 54 To 80
        SetMemory(0x66302C, Add, 1310720),# units:Portrait  index:83    from 56 To 76
        SetMemory(0x663030, Add, 21),# units:Portrait  index:84    from 55 To 76
        SetMemory(0x663034, Add, 33),# units:Portrait  index:86    from 46 To 79
        SetMemory(0x663034, Add, 1376256),# units:Portrait  index:87    from 59 To 80
        SetMemory(0x663038, Add, -19),# units:Portrait  index:88    from 95 To 76
        SetMemory(0x663038, Add, 917504),# units:Portrait  index:89    from 62 To 76
        SetMemory(0x66303C, Add, 15),# units:Portrait  index:90    from 63 To 78
        SetMemory(0x663040, Add, -1507328),# units:Portrait  index:93    from 101 To 78
        SetMemory(0x663044, Add, -27),# units:Portrait  index:94    from 102 To 75
        SetMemory(0x663044, Add, 720896),# units:Portrait  index:95    from 64 To 75
        SetMemory(0x663048, Add, -27),# units:Portrait  index:96    from 103 To 76
        SetMemory(0x66304C, Add, -16),# units:Portrait  index:98    from 96 To 80
        SetMemory(0x66304C, Add, -851968),# units:Portrait  index:99    from 94 To 81
        SetMemory(0x663050, Add, -12),# units:Portrait  index:100    from 93 To 81
        SetMemory(0x663054, Add, -11),# units:Portrait  index:102    from 92 To 81
        SetMemory(0x663054, Add, -1114112),# units:Portrait  index:103    from 98 To 81
        SetMemory(0x663058, Add, -13),# units:Portrait  index:104    from 94 To 81
        SetMemory(0x66305C, Add, 64),# units:Portrait  index:106    from 17 To 81
        SetMemory(0x66305C, Add, 5767168),# units:Portrait  index:107    from 17 To 105
        SetMemory(0x663060, Add, 4194304),# units:Portrait  index:109    from 17 To 81
        SetMemory(0x663064, Add, 58),# units:Portrait  index:110    from 17 To 75
        SetMemory(0x663064, Add, 4194304),# units:Portrait  index:111    from 17 To 81
        SetMemory(0x663068, Add, 64),# units:Portrait  index:112    from 17 To 81
        SetMemory(0x663068, Add, 4194304),# units:Portrait  index:113    from 17 To 81
        SetMemory(0x66306C, Add, 64),# units:Portrait  index:114    from 17 To 81
        SetMemory(0x66306C, Add, 4194304),# units:Portrait  index:115    from 17 To 81
        SetMemory(0x663070, Add, 64),# units:Portrait  index:116    from 17 To 81
        SetMemory(0x663070, Add, 4194304),# units:Portrait  index:117    from 17 To 81
        SetMemory(0x663074, Add, 64),# units:Portrait  index:118    from 17 To 81
        SetMemory(0x663078, Add, 64),# units:Portrait  index:120    from 17 To 81
        SetMemory(0x66307C, Add, 64),# units:Portrait  index:122    from 17 To 81
        SetMemory(0x66307C, Add, 4194304),# units:Portrait  index:123    from 17 To 81
        SetMemory(0x663080, Add, 64),# units:Portrait  index:124    from 17 To 81
        SetMemory(0x663080, Add, 4194304),# units:Portrait  index:125    from 17 To 81
        SetMemory(0x663084, Add, 67),# units:Portrait  index:126    from 14 To 81
        SetMemory(0x663084, Add, 4194304),# units:Portrait  index:127    from 17 To 81
        SetMemory(0x663088, Add, -24),# units:Portrait  index:128    from 104 To 80
        SetMemory(0x663088, Add, -1703936),# units:Portrait  index:129    from 105 To 79
        SetMemory(0x66308C, Add, 48),# units:Portrait  index:130    from 33 To 81
        SetMemory(0x66308C, Add, 2818048),# units:Portrait  index:131    from 38 To 81
        SetMemory(0x663090, Add, 43),# units:Portrait  index:132    from 38 To 81
        SetMemory(0x663090, Add, 2818048),# units:Portrait  index:133    from 38 To 81
        SetMemory(0x663094, Add, 43),# units:Portrait  index:134    from 38 To 81
        SetMemory(0x663094, Add, 2818048),# units:Portrait  index:135    from 38 To 81
        SetMemory(0x663098, Add, 43),# units:Portrait  index:136    from 38 To 81
        SetMemory(0x663098, Add, 2424832),# units:Portrait  index:137    from 38 To 75
        SetMemory(0x66309C, Add, 37),# units:Portrait  index:138    from 38 To 75
        SetMemory(0x66309C, Add, 2621440),# units:Portrait  index:139    from 38 To 78
        SetMemory(0x6630A0, Add, 40),# units:Portrait  index:140    from 38 To 78
        SetMemory(0x6630A0, Add, 2621440),# units:Portrait  index:141    from 38 To 78
        SetMemory(0x6630A4, Add, 41),# units:Portrait  index:142    from 38 To 79
        SetMemory(0x6630A4, Add, 2752512),# units:Portrait  index:143    from 38 To 80
        SetMemory(0x6630A8, Add, 40),# units:Portrait  index:144    from 38 To 78
        SetMemory(0x6630AC, Add, 40),# units:Portrait  index:146    from 38 To 78
        SetMemory(0x6630AC, Add, 2424832),# units:Portrait  index:147    from 38 To 75
        SetMemory(0x6630B0, Add, 38),# units:Portrait  index:148    from 38 To 76
        SetMemory(0x6630B0, Add, 2621440),# units:Portrait  index:149    from 38 To 78
        SetMemory(0x6630B4, Add, 44),# units:Portrait  index:150    from 32 To 76
        SetMemory(0x6630B4, Add, 2686976),# units:Portrait  index:151    from 34 To 75
        SetMemory(0x6630B8, Add, 40),# units:Portrait  index:152    from 35 To 75
        SetMemory(0x6630BC, Add, 20),# units:Portrait  index:154    from 60 To 80
        SetMemory(0x6630BC, Add, 1310720),# units:Portrait  index:155    from 60 To 80
        SetMemory(0x6630C0, Add, 21),# units:Portrait  index:156    from 60 To 81
        SetMemory(0x6630C0, Add, 1048576),# units:Portrait  index:157    from 60 To 76
        SetMemory(0x6630C4, Add, 983040),# units:Portrait  index:159    from 60 To 75
        SetMemory(0x6630C8, Add, 15),# units:Portrait  index:160    from 60 To 75
        SetMemory(0x6630CC, Add, 15),# units:Portrait  index:162    from 60 To 75
        SetMemory(0x6630CC, Add, 1310720),# units:Portrait  index:163    from 60 To 80
        SetMemory(0x6630D0, Add, 18),# units:Portrait  index:164    from 60 To 78
        SetMemory(0x6630D0, Add, 1179648),# units:Portrait  index:165    from 60 To 78
        SetMemory(0x6630D4, Add, 18),# units:Portrait  index:166    from 60 To 78
        SetMemory(0x6630D4, Add, 1179648),# units:Portrait  index:167    from 60 To 78
        SetMemory(0x6630D8, Add, 37),# units:Portrait  index:168    from 41 To 78
        SetMemory(0x6630D8, Add, 1179648),# units:Portrait  index:169    from 60 To 78
        SetMemory(0x6630DC, Add, 18),# units:Portrait  index:170    from 60 To 78
        SetMemory(0x6630DC, Add, 1179648),# units:Portrait  index:171    from 60 To 78
        SetMemory(0x6630E0, Add, 18),# units:Portrait  index:172    from 60 To 78
        SetMemory(0x6630E0, Add, 1441792),# units:Portrait  index:173    from 58 To 80
        SetMemory(0x6630E4, Add, 16),# units:Portrait  index:174    from 60 To 76
        SetMemory(0x6630E4, Add, 1048576),# units:Portrait  index:175    from 60 To 76
        SetMemory(0x663100, Add, 1048576),# units:Portrait  index:189    from 60 To 76
        SetMemory(0x663104, Add, 59),# units:Portrait  index:190    from 17 To 76
        SetMemory(0x66310C, Add, 42),# units:Portrait  index:194    from 38 To 80
        SetMemory(0x66310C, Add, 4063232),# units:Portrait  index:195    from 17 To 79
        SetMemory(0x663110, Add, 44),# units:Portrait  index:196    from 60 To 104
        SetMemory(0x663118, Add, 63),# units:Portrait  index:200    from 17 To 80
        SetMemory(0x663118, Add, 2752512),# units:Portrait  index:201    from 38 To 80
        SetMemory(0x663134, Add, -196608),# units:Portrait  index:215    from 82 To 79
        SetMemory(0x663138, Add, 49),# units:Portrait  index:216    from 32 To 81
        SetMemory(0x663138, Add, -262144),# units:Portrait  index:217    from 80 To 76
        SetMemory(0x66313C, Add, -196608),# units:Portrait  index:219    from 81 To 78
        SetMemory(0x663140, Add, 1),# units:Portrait  index:220    from 78 To 79
        SetMemory(0x663140, Add, -131072),# units:Portrait  index:221    from 78 To 76
        SetMemory(0x663144, Add, 1835008),# units:Portrait  index:223    from 76 To 104
        SetMemory(0x663888, Add, 1638400),# units:Mineral Cost  index:1    from 25 To 50
        SetMemory(0x66388C, Add, -25),# units:Mineral Cost  index:2    from 75 To 50
        SetMemory(0x663898, Add, -100),# units:Mineral Cost  index:8    from 150 To 50
        SetMemory(0x663898, Add, -3276800),# units:Mineral Cost  index:9    from 100 To 50
        SetMemory(0x66389C, Add, -50),# units:Mineral Cost  index:10    from 100 To 50
        SetMemory(0x66389C, Add, -3276800),# units:Mineral Cost  index:11    from 100 To 50
        SetMemory(0x6638A0, Add, -350),# units:Mineral Cost  index:12    from 400 To 50
        SetMemory(0x6638AC, Add, -6553600),# units:Mineral Cost  index:19    from 150 To 50
        SetMemory(0x6638B0, Add, -22937600),# units:Mineral Cost  index:21    from 400 To 50
        SetMemory(0x6638BC, Add, -49152000),# units:Mineral Cost  index:27    from 800 To 50
        SetMemory(0x6638C0, Add, -750),# units:Mineral Cost  index:28    from 800 To 50
        SetMemory(0x6638C0, Add, -49152000),# units:Mineral Cost  index:29    from 800 To 50
        SetMemory(0x6638D4, Add, -25),# units:Mineral Cost  index:38    from 75 To 50
        SetMemory(0x6638D4, Add, -9830400),# units:Mineral Cost  index:39    from 200 To 50
        SetMemory(0x6638D8, Add, 49),# units:Mineral Cost  index:40    from 1 To 50
        SetMemory(0x6638DC, Add, -50),# units:Mineral Cost  index:42    from 100 To 50
        SetMemory(0x6638DC, Add, -3276800),# units:Mineral Cost  index:43    from 100 To 50
        SetMemory(0x6638E0, Add, -3276800),# units:Mineral Cost  index:45    from 100 To 50
        SetMemory(0x6638E4, Add, 1638400),# units:Mineral Cost  index:47    from 25 To 50
        SetMemory(0x6638E8, Add, -350),# units:Mineral Cost  index:48    from 400 To 50
        SetMemory(0x6638E8, Add, -9830400),# units:Mineral Cost  index:49    from 200 To 50
        SetMemory(0x6638EC, Add, -50),# units:Mineral Cost  index:50    from 100 To 50
        SetMemory(0x6638EC, Add, -9830400),# units:Mineral Cost  index:51    from 200 To 50
        SetMemory(0x6638F0, Add, -6553600),# units:Mineral Cost  index:53    from 150 To 50
        SetMemory(0x6638F4, Add, -50),# units:Mineral Cost  index:54    from 100 To 50
        SetMemory(0x6638F4, Add, -9830400),# units:Mineral Cost  index:55    from 200 To 50
        SetMemory(0x6638F8, Add, -50),# units:Mineral Cost  index:56    from 100 To 50
        SetMemory(0x6638F8, Add, -9830400),# units:Mineral Cost  index:57    from 200 To 50
        SetMemory(0x663900, Add, -100),# units:Mineral Cost  index:60    from 150 To 50
        SetMemory(0x663900, Add, -4915200),# units:Mineral Cost  index:61    from 125 To 50
        SetMemory(0x663904, Add, -100),# units:Mineral Cost  index:62    from 150 To 50
        SetMemory(0x663904, Add, 3276800),# units:Mineral Cost  index:63    from 0 To 50
        SetMemory(0x663908, Add, -3276800),# units:Mineral Cost  index:65    from 100 To 50
        SetMemory(0x66390C, Add, -75),# units:Mineral Cost  index:66    from 125 To 50
        SetMemory(0x663910, Add, 50),# units:Mineral Cost  index:68    from 0 To 50
        SetMemory(0x663910, Add, -9830400),# units:Mineral Cost  index:69    from 200 To 50
        SetMemory(0x663914, Add, -225),# units:Mineral Cost  index:70    from 275 To 50
        SetMemory(0x663914, Add, -3276800),# units:Mineral Cost  index:71    from 100 To 50
        SetMemory(0x663918, Add, -300),# units:Mineral Cost  index:72    from 350 To 50
        SetMemory(0x66391C, Add, -100),# units:Mineral Cost  index:74    from 150 To 50
        SetMemory(0x66391C, Add, -3276800),# units:Mineral Cost  index:75    from 100 To 50
        SetMemory(0x663920, Add, 50),# units:Mineral Cost  index:76    from 0 To 50
        SetMemory(0x663920, Add, -9830400),# units:Mineral Cost  index:77    from 200 To 50
        SetMemory(0x663924, Add, -250),# units:Mineral Cost  index:78    from 300 To 50
        SetMemory(0x663924, Add, -3276800),# units:Mineral Cost  index:79    from 100 To 50
        SetMemory(0x663928, Add, -550),# units:Mineral Cost  index:80    from 600 To 50
        SetMemory(0x663928, Add, -22937600),# units:Mineral Cost  index:81    from 400 To 50
        SetMemory(0x66392C, Add, -650),# units:Mineral Cost  index:82    from 700 To 50
        SetMemory(0x66392C, Add, -9830400),# units:Mineral Cost  index:83    from 200 To 50
        SetMemory(0x663930, Add, 25),# units:Mineral Cost  index:84    from 25 To 50
        SetMemory(0x663934, Add, -3276800),# units:Mineral Cost  index:87    from 100 To 50
        SetMemory(0x663938, Add, -550),# units:Mineral Cost  index:88    from 600 To 50
        SetMemory(0x663938, Add, 3211264),# units:Mineral Cost  index:89    from 1 To 50
        SetMemory(0x66393C, Add, 49),# units:Mineral Cost  index:90    from 1 To 50
        SetMemory(0x663940, Add, 3211264),# units:Mineral Cost  index:93    from 1 To 50
        SetMemory(0x663944, Add, 49),# units:Mineral Cost  index:94    from 1 To 50
        SetMemory(0x663944, Add, 3211264),# units:Mineral Cost  index:95    from 1 To 50
        SetMemory(0x663948, Add, 49),# units:Mineral Cost  index:96    from 1 To 50
        SetMemory(0x66394C, Add, -100),# units:Mineral Cost  index:98    from 150 To 50
        SetMemory(0x66394C, Add, -9830400),# units:Mineral Cost  index:99    from 200 To 50
        SetMemory(0x663950, Add, -150),# units:Mineral Cost  index:100    from 200 To 50
        SetMemory(0x663954, Add, -750),# units:Mineral Cost  index:102    from 800 To 50
        SetMemory(0x663958, Add, -150),# units:Mineral Cost  index:104    from 200 To 50
        SetMemory(0x66395C, Add, -350),# units:Mineral Cost  index:106    from 400 To 50
        SetMemory(0x663960, Add, -3276800),# units:Mineral Cost  index:109    from 100 To 50
        SetMemory(0x663964, Add, -50),# units:Mineral Cost  index:110    from 100 To 50
        SetMemory(0x663964, Add, -6553600),# units:Mineral Cost  index:111    from 150 To 50
        SetMemory(0x663968, Add, -100),# units:Mineral Cost  index:112    from 150 To 50
        SetMemory(0x663968, Add, -9830400),# units:Mineral Cost  index:113    from 200 To 50
        SetMemory(0x66396C, Add, -100),# units:Mineral Cost  index:114    from 150 To 50
        SetMemory(0x663970, Add, -50),# units:Mineral Cost  index:116    from 100 To 50
        SetMemory(0x66397C, Add, -75),# units:Mineral Cost  index:122    from 125 To 50
        SetMemory(0x66397C, Add, -3276800),# units:Mineral Cost  index:123    from 100 To 50
        SetMemory(0x663980, Add, -25),# units:Mineral Cost  index:124    from 75 To 50
        SetMemory(0x663980, Add, -3276800),# units:Mineral Cost  index:125    from 100 To 50
        SetMemory(0x663984, Add, -750),# units:Mineral Cost  index:126    from 800 To 50
        SetMemory(0x663984, Add, -9830400),# units:Mineral Cost  index:127    from 200 To 50
        SetMemory(0x663988, Add, 49),# units:Mineral Cost  index:128    from 1 To 50
        SetMemory(0x663988, Add, 3211264),# units:Mineral Cost  index:129    from 1 To 50
        SetMemory(0x66398C, Add, 49),# units:Mineral Cost  index:130    from 1 To 50
        SetMemory(0x66398C, Add, -16384000),# units:Mineral Cost  index:131    from 300 To 50
        SetMemory(0x663990, Add, -100),# units:Mineral Cost  index:132    from 150 To 50
        SetMemory(0x663990, Add, -9830400),# units:Mineral Cost  index:133    from 200 To 50
        SetMemory(0x663994, Add, -100),# units:Mineral Cost  index:134    from 150 To 50
        SetMemory(0x663994, Add, -3276800),# units:Mineral Cost  index:135    from 100 To 50
        SetMemory(0x663998, Add, -50),# units:Mineral Cost  index:136    from 100 To 50
        SetMemory(0x663998, Add, -3276800),# units:Mineral Cost  index:137    from 100 To 50
        SetMemory(0x66399C, Add, -100),# units:Mineral Cost  index:138    from 150 To 50
        SetMemory(0x66399C, Add, -1638400),# units:Mineral Cost  index:139    from 75 To 50
        SetMemory(0x6639A0, Add, -100),# units:Mineral Cost  index:140    from 150 To 50
        SetMemory(0x6639A0, Add, -9830400),# units:Mineral Cost  index:141    from 200 To 50
        SetMemory(0x6639A4, Add, -150),# units:Mineral Cost  index:142    from 200 To 50
        SetMemory(0x6639A4, Add, -1638400),# units:Mineral Cost  index:143    from 75 To 50
        SetMemory(0x6639AC, Add, 3211264),# units:Mineral Cost  index:147    from 1 To 50
        SetMemory(0x6639B0, Add, 49),# units:Mineral Cost  index:148    from 1 To 50
        SetMemory(0x6639B4, Add, 50),# units:Mineral Cost  index:150    from 0 To 50
        SetMemory(0x6639B4, Add, 3276800),# units:Mineral Cost  index:151    from 0 To 50
        SetMemory(0x6639B8, Add, 50),# units:Mineral Cost  index:152    from 0 To 50
        SetMemory(0x6639BC, Add, -350),# units:Mineral Cost  index:154    from 400 To 50
        SetMemory(0x6639BC, Add, -9830400),# units:Mineral Cost  index:155    from 200 To 50
        SetMemory(0x6639C0, Add, -50),# units:Mineral Cost  index:156    from 100 To 50
        SetMemory(0x6639C0, Add, -3276800),# units:Mineral Cost  index:157    from 100 To 50
        SetMemory(0x6639C8, Add, -100),# units:Mineral Cost  index:160    from 150 To 50
        SetMemory(0x6639CC, Add, -100),# units:Mineral Cost  index:162    from 150 To 50
        SetMemory(0x6639CC, Add, -6553600),# units:Mineral Cost  index:163    from 150 To 50
        SetMemory(0x6639D0, Add, -150),# units:Mineral Cost  index:164    from 200 To 50
        SetMemory(0x6639D0, Add, -6553600),# units:Mineral Cost  index:165    from 150 To 50
        SetMemory(0x6639D4, Add, -100),# units:Mineral Cost  index:166    from 150 To 50
        SetMemory(0x6639D4, Add, -6553600),# units:Mineral Cost  index:167    from 150 To 50
        SetMemory(0x6639D8, Add, -100),# units:Mineral Cost  index:168    from 150 To 50
        SetMemory(0x6639D8, Add, -16384000),# units:Mineral Cost  index:169    from 300 To 50
        SetMemory(0x6639DC, Add, -150),# units:Mineral Cost  index:170    from 200 To 50
        SetMemory(0x6639DC, Add, -6553600),# units:Mineral Cost  index:171    from 150 To 50
        SetMemory(0x6639E0, Add, -50),# units:Mineral Cost  index:172    from 100 To 50
        SetMemory(0x6639E0, Add, -13107200),# units:Mineral Cost  index:173    from 250 To 50
        SetMemory(0x6639E4, Add, -200),# units:Mineral Cost  index:174    from 250 To 50
        SetMemory(0x6639E4, Add, -95027200),# units:Mineral Cost  index:175    from 1500 To 50
        SetMemory(0x663A00, Add, -36044800),# units:Mineral Cost  index:189    from 600 To 50
        SetMemory(0x663A04, Add, -950),# units:Mineral Cost  index:190    from 1000 To 50
        SetMemory(0x663A0C, Add, -200),# units:Mineral Cost  index:194    from 250 To 50
        SetMemory(0x663A10, Add, -50),# units:Mineral Cost  index:196    from 100 To 50
        SetMemory(0x663A18, Add, -150),# units:Mineral Cost  index:200    from 200 To 50
        SetMemory(0x663A18, Add, -62259200),# units:Mineral Cost  index:201    from 1000 To 50
        SetMemory(0x663A34, Add, 3211264),# units:Mineral Cost  index:215    from 1 To 50
        SetMemory(0x663A38, Add, 49),# units:Mineral Cost  index:216    from 1 To 50
        SetMemory(0x663A38, Add, 3211264),# units:Mineral Cost  index:217    from 1 To 50
        SetMemory(0x663A3C, Add, 49),# units:Mineral Cost  index:218    from 1 To 50
        SetMemory(0x663A3C, Add, 3211264),# units:Mineral Cost  index:219    from 1 To 50
        SetMemory(0x663A40, Add, 49),# units:Mineral Cost  index:220    from 1 To 50
        SetMemory(0x663A40, Add, 3211264),# units:Mineral Cost  index:221    from 1 To 50
        SetMemory(0x663A44, Add, 49),# units:Mineral Cost  index:222    from 1 To 50
        SetMemory(0x663A44, Add, 3211264),# units:Mineral Cost  index:223    from 1 To 50
        SetMemory(0x65FD00, Add, -4915200),# units:Vespene Cost  index:1    from 75 To 0
        SetMemory(0x65FD10, Add, -100),# units:Vespene Cost  index:8    from 100 To 0
        SetMemory(0x65FD10, Add, -14745600),# units:Vespene Cost  index:9    from 225 To 0
        SetMemory(0x65FD14, Add, -50),# units:Vespene Cost  index:10    from 50 To 0
        SetMemory(0x65FD14, Add, -6553600),# units:Vespene Cost  index:11    from 100 To 0
        SetMemory(0x65FD18, Add, -300),# units:Vespene Cost  index:12    from 300 To 0
        SetMemory(0x65FD20, Add, -150),# units:Vespene Cost  index:16    from 150 To 0
        SetMemory(0x65FD28, Add, -13107200),# units:Vespene Cost  index:21    from 200 To 0
        SetMemory(0x65FD2C, Add, -600),# units:Vespene Cost  index:22    from 600 To 0
        SetMemory(0x65FD34, Add, -39321600),# units:Vespene Cost  index:27    from 600 To 0
        SetMemory(0x65FD38, Add, -600),# units:Vespene Cost  index:28    from 600 To 0
        SetMemory(0x65FD38, Add, -39321600),# units:Vespene Cost  index:29    from 600 To 0
        SetMemory(0x65FD40, Add, -25),# units:Vespene Cost  index:32    from 25 To 0
        SetMemory(0x65FD44, Add, -25),# units:Vespene Cost  index:34    from 25 To 0
        SetMemory(0x65FD4C, Add, -25),# units:Vespene Cost  index:38    from 25 To 0
        SetMemory(0x65FD4C, Add, -13107200),# units:Vespene Cost  index:39    from 200 To 0
        SetMemory(0x65FD50, Add, -1),# units:Vespene Cost  index:40    from 1 To 0
        SetMemory(0x65FD54, Add, -6553600),# units:Vespene Cost  index:43    from 100 To 0
        SetMemory(0x65FD58, Add, -100),# units:Vespene Cost  index:44    from 100 To 0
        SetMemory(0x65FD58, Add, -6553600),# units:Vespene Cost  index:45    from 100 To 0
        SetMemory(0x65FD5C, Add, -150),# units:Vespene Cost  index:46    from 150 To 0
        SetMemory(0x65FD5C, Add, -4915200),# units:Vespene Cost  index:47    from 75 To 0
        SetMemory(0x65FD60, Add, -400),# units:Vespene Cost  index:48    from 400 To 0
        SetMemory(0x65FD60, Add, -19660800),# units:Vespene Cost  index:49    from 300 To 0
        SetMemory(0x65FD64, Add, -50),# units:Vespene Cost  index:50    from 50 To 0
        SetMemory(0x65FD64, Add, -19660800),# units:Vespene Cost  index:51    from 300 To 0
        SetMemory(0x65FD68, Add, -200),# units:Vespene Cost  index:52    from 200 To 0
        SetMemory(0x65FD68, Add, -3276800),# units:Vespene Cost  index:53    from 50 To 0
        SetMemory(0x65FD6C, Add, -13107200),# units:Vespene Cost  index:55    from 200 To 0
        SetMemory(0x65FD70, Add, -200),# units:Vespene Cost  index:56    from 200 To 0
        SetMemory(0x65FD78, Add, -100),# units:Vespene Cost  index:60    from 100 To 0
        SetMemory(0x65FD78, Add, -6553600),# units:Vespene Cost  index:61    from 100 To 0
        SetMemory(0x65FD7C, Add, -50),# units:Vespene Cost  index:62    from 50 To 0
        SetMemory(0x65FD84, Add, -50),# units:Vespene Cost  index:66    from 50 To 0
        SetMemory(0x65FD84, Add, -9830400),# units:Vespene Cost  index:67    from 150 To 0
        SetMemory(0x65FD8C, Add, -125),# units:Vespene Cost  index:70    from 125 To 0
        SetMemory(0x65FD8C, Add, -22937600),# units:Vespene Cost  index:71    from 350 To 0
        SetMemory(0x65FD90, Add, -250),# units:Vespene Cost  index:72    from 250 To 0
        SetMemory(0x65FD94, Add, -150),# units:Vespene Cost  index:74    from 150 To 0
        SetMemory(0x65FD94, Add, -19660800),# units:Vespene Cost  index:75    from 300 To 0
        SetMemory(0x65FD9C, Add, -100),# units:Vespene Cost  index:78    from 100 To 0
        SetMemory(0x65FD9C, Add, -19660800),# units:Vespene Cost  index:79    from 300 To 0
        SetMemory(0x65FDA0, Add, -300),# units:Vespene Cost  index:80    from 300 To 0
        SetMemory(0x65FDA0, Add, -13107200),# units:Vespene Cost  index:81    from 200 To 0
        SetMemory(0x65FDA4, Add, -600),# units:Vespene Cost  index:82    from 600 To 0
        SetMemory(0x65FDA4, Add, -6553600),# units:Vespene Cost  index:83    from 100 To 0
        SetMemory(0x65FDA8, Add, -75),# units:Vespene Cost  index:84    from 75 To 0
        SetMemory(0x65FDAC, Add, -1000),# units:Vespene Cost  index:86    from 1000 To 0
        SetMemory(0x65FDAC, Add, -19660800),# units:Vespene Cost  index:87    from 300 To 0
        SetMemory(0x65FDB0, Add, -300),# units:Vespene Cost  index:88    from 300 To 0
        SetMemory(0x65FDB0, Add, -65536),# units:Vespene Cost  index:89    from 1 To 0
        SetMemory(0x65FDB4, Add, -1),# units:Vespene Cost  index:90    from 1 To 0
        SetMemory(0x65FDB8, Add, -65536),# units:Vespene Cost  index:93    from 1 To 0
        SetMemory(0x65FDBC, Add, -1),# units:Vespene Cost  index:94    from 1 To 0
        SetMemory(0x65FDBC, Add, -65536),# units:Vespene Cost  index:95    from 1 To 0
        SetMemory(0x65FDC0, Add, -1),# units:Vespene Cost  index:96    from 1 To 0
        SetMemory(0x65FDC4, Add, -100),# units:Vespene Cost  index:98    from 100 To 0
        SetMemory(0x65FDC4, Add, -4915200),# units:Vespene Cost  index:99    from 75 To 0
        SetMemory(0x65FDC8, Add, -75),# units:Vespene Cost  index:100    from 75 To 0
        SetMemory(0x65FDCC, Add, -600),# units:Vespene Cost  index:102    from 600 To 0
        SetMemory(0x65FDCC, Add, -6553600),# units:Vespene Cost  index:103    from 100 To 0
        SetMemory(0x65FDD0, Add, -75),# units:Vespene Cost  index:104    from 75 To 0
        SetMemory(0x65FDD4, Add, -3276800),# units:Vespene Cost  index:107    from 50 To 0
        SetMemory(0x65FDE0, Add, -6553600),# units:Vespene Cost  index:113    from 100 To 0
        SetMemory(0x65FDE4, Add, -100),# units:Vespene Cost  index:114    from 100 To 0
        SetMemory(0x65FDE4, Add, -3276800),# units:Vespene Cost  index:115    from 50 To 0
        SetMemory(0x65FDE8, Add, -150),# units:Vespene Cost  index:116    from 150 To 0
        SetMemory(0x65FDE8, Add, -3276800),# units:Vespene Cost  index:117    from 50 To 0
        SetMemory(0x65FDEC, Add, -50),# units:Vespene Cost  index:118    from 50 To 0
        SetMemory(0x65FDF0, Add, -50),# units:Vespene Cost  index:120    from 50 To 0
        SetMemory(0x65FDF4, Add, -3276800),# units:Vespene Cost  index:123    from 50 To 0
        SetMemory(0x65FDFC, Add, -600),# units:Vespene Cost  index:126    from 600 To 0
        SetMemory(0x65FE00, Add, -1),# units:Vespene Cost  index:128    from 1 To 0
        SetMemory(0x65FE00, Add, -65536),# units:Vespene Cost  index:129    from 1 To 0
        SetMemory(0x65FE04, Add, -1),# units:Vespene Cost  index:130    from 1 To 0
        SetMemory(0x65FE08, Add, -100),# units:Vespene Cost  index:132    from 100 To 0
        SetMemory(0x65FE08, Add, -9830400),# units:Vespene Cost  index:133    from 150 To 0
        SetMemory(0x65FE0C, Add, -3276800),# units:Vespene Cost  index:135    from 50 To 0
        SetMemory(0x65FE10, Add, -100),# units:Vespene Cost  index:136    from 100 To 0
        SetMemory(0x65FE10, Add, -9830400),# units:Vespene Cost  index:137    from 150 To 0
        SetMemory(0x65FE14, Add, -100),# units:Vespene Cost  index:138    from 100 To 0
        SetMemory(0x65FE18, Add, -200),# units:Vespene Cost  index:140    from 200 To 0
        SetMemory(0x65FE18, Add, -9830400),# units:Vespene Cost  index:141    from 150 To 0
        SetMemory(0x65FE24, Add, -65536),# units:Vespene Cost  index:147    from 1 To 0
        SetMemory(0x65FE28, Add, -1),# units:Vespene Cost  index:148    from 1 To 0
        SetMemory(0x65FE34, Add, -13107200),# units:Vespene Cost  index:155    from 200 To 0
        SetMemory(0x65FE3C, Add, -6553600),# units:Vespene Cost  index:159    from 100 To 0
        SetMemory(0x65FE44, Add, -6553600),# units:Vespene Cost  index:163    from 100 To 0
        SetMemory(0x65FE48, Add, -13107200),# units:Vespene Cost  index:165    from 200 To 0
        SetMemory(0x65FE4C, Add, -9830400),# units:Vespene Cost  index:167    from 150 To 0
        SetMemory(0x65FE50, Add, -13107200),# units:Vespene Cost  index:169    from 200 To 0
        SetMemory(0x65FE54, Add, -150),# units:Vespene Cost  index:170    from 150 To 0
        SetMemory(0x65FE54, Add, -6553600),# units:Vespene Cost  index:171    from 100 To 0
        SetMemory(0x65FE5C, Add, -32768000),# units:Vespene Cost  index:175    from 500 To 0
        SetMemory(0x65FE78, Add, -13107200),# units:Vespene Cost  index:189    from 200 To 0
        SetMemory(0x65FE7C, Add, -400),# units:Vespene Cost  index:190    from 400 To 0
        SetMemory(0x65FE84, Add, -3276800),# units:Vespene Cost  index:195    from 50 To 0
        SetMemory(0x65FE88, Add, -100),# units:Vespene Cost  index:196    from 100 To 0
        SetMemory(0x65FE90, Add, -50),# units:Vespene Cost  index:200    from 50 To 0
        SetMemory(0x65FE90, Add, -32768000),# units:Vespene Cost  index:201    from 500 To 0
        SetMemory(0x65FEAC, Add, -65536),# units:Vespene Cost  index:215    from 1 To 0
        SetMemory(0x65FEB0, Add, -1),# units:Vespene Cost  index:216    from 1 To 0
        SetMemory(0x65FEB0, Add, -65536),# units:Vespene Cost  index:217    from 1 To 0
        SetMemory(0x65FEB4, Add, -1),# units:Vespene Cost  index:218    from 1 To 0
        SetMemory(0x65FEB4, Add, -65536),# units:Vespene Cost  index:219    from 1 To 0
        SetMemory(0x65FEB8, Add, -1),# units:Vespene Cost  index:220    from 1 To 0
        SetMemory(0x65FEB8, Add, -65536),# units:Vespene Cost  index:221    from 1 To 0
        SetMemory(0x65FEBC, Add, -1),# units:Vespene Cost  index:222    from 1 To 0
        SetMemory(0x65FEBC, Add, -65536),# units:Vespene Cost  index:223    from 1 To 0
        SetMemory(0x660428, Add, -25559040),# units:Build Time  index:1    from 750 To 360
        SetMemory(0x66042C, Add, -90),# units:Build Time  index:2    from 450 To 360
        SetMemory(0x660434, Add, 3932160),# units:Build Time  index:7    from 300 To 360
        SetMemory(0x660438, Add, -540),# units:Build Time  index:8    from 900 To 360
        SetMemory(0x660438, Add, -55050240),# units:Build Time  index:9    from 1200 To 360
        SetMemory(0x66043C, Add, -360),# units:Build Time  index:10    from 720 To 360
        SetMemory(0x66043C, Add, -25559040),# units:Build Time  index:11    from 750 To 360
        SetMemory(0x660440, Add, -1640),# units:Build Time  index:12    from 2000 To 360
        SetMemory(0x660448, Add, -1140),# units:Build Time  index:16    from 1500 To 360
        SetMemory(0x66044C, Add, -35389440),# units:Build Time  index:19    from 900 To 360
        SetMemory(0x660450, Add, 359),# units:Build Time  index:20    from 1 To 360
        SetMemory(0x660450, Add, -94371840),# units:Build Time  index:21    from 1800 To 360
        SetMemory(0x660454, Add, -2040),# units:Build Time  index:22    from 2400 To 360
        SetMemory(0x66045C, Add, -290979840),# units:Build Time  index:27    from 4800 To 360
        SetMemory(0x660460, Add, -2040),# units:Build Time  index:28    from 2400 To 360
        SetMemory(0x660460, Add, -290979840),# units:Build Time  index:29    from 4800 To 360
        SetMemory(0x66046C, Add, -90),# units:Build Time  index:34    from 450 To 360
        SetMemory(0x660470, Add, -3932160),# units:Build Time  index:37    from 420 To 360
        SetMemory(0x660474, Add, -60),# units:Build Time  index:38    from 420 To 360
        SetMemory(0x660474, Add, -35389440),# units:Build Time  index:39    from 900 To 360
        SetMemory(0x660478, Add, 359),# units:Build Time  index:40    from 1 To 360
        SetMemory(0x660478, Add, 3932160),# units:Build Time  index:41    from 300 To 360
        SetMemory(0x66047C, Add, -240),# units:Build Time  index:42    from 600 To 360
        SetMemory(0x66047C, Add, -15728640),# units:Build Time  index:43    from 600 To 360
        SetMemory(0x660480, Add, -240),# units:Build Time  index:44    from 600 To 360
        SetMemory(0x660480, Add, -25559040),# units:Build Time  index:45    from 750 To 360
        SetMemory(0x660484, Add, -390),# units:Build Time  index:46    from 750 To 360
        SetMemory(0x660484, Add, -5898240),# units:Build Time  index:47    from 450 To 360
        SetMemory(0x660488, Add, -1440),# units:Build Time  index:48    from 1800 To 360
        SetMemory(0x660488, Add, -74711040),# units:Build Time  index:49    from 1500 To 360
        SetMemory(0x66048C, Add, -240),# units:Build Time  index:50    from 600 To 360
        SetMemory(0x66048C, Add, -74711040),# units:Build Time  index:51    from 1500 To 360
        SetMemory(0x660490, Add, -1140),# units:Build Time  index:52    from 1500 To 360
        SetMemory(0x660490, Add, -27525120),# units:Build Time  index:53    from 780 To 360
        SetMemory(0x660494, Add, -480),# units:Build Time  index:54    from 840 To 360
        SetMemory(0x660494, Add, -55050240),# units:Build Time  index:55    from 1200 To 360
        SetMemory(0x660498, Add, -840),# units:Build Time  index:56    from 1200 To 360
        SetMemory(0x660498, Add, -55050240),# units:Build Time  index:57    from 1200 To 360
        SetMemory(0x6604A0, Add, -240),# units:Build Time  index:60    from 600 To 360
        SetMemory(0x6604A0, Add, -25559040),# units:Build Time  index:61    from 750 To 360
        SetMemory(0x6604A4, Add, -240),# units:Build Time  index:62    from 600 To 360
        SetMemory(0x6604A4, Add, 3932160),# units:Build Time  index:63    from 300 To 360
        SetMemory(0x6604A8, Add, 60),# units:Build Time  index:64    from 300 To 360
        SetMemory(0x6604A8, Add, -15728640),# units:Build Time  index:65    from 600 To 360
        SetMemory(0x6604AC, Add, -390),# units:Build Time  index:66    from 750 To 360
        SetMemory(0x6604AC, Add, -25559040),# units:Build Time  index:67    from 750 To 360
        SetMemory(0x6604B0, Add, 60),# units:Build Time  index:68    from 300 To 360
        SetMemory(0x6604B0, Add, -35389440),# units:Build Time  index:69    from 900 To 360
        SetMemory(0x6604B4, Add, -840),# units:Build Time  index:70    from 1200 To 360
        SetMemory(0x6604B4, Add, -133693440),# units:Build Time  index:71    from 2400 To 360
        SetMemory(0x6604B8, Add, -1740),# units:Build Time  index:72    from 2100 To 360
        SetMemory(0x6604BC, Add, -390),# units:Build Time  index:74    from 750 To 360
        SetMemory(0x6604BC, Add, -74711040),# units:Build Time  index:75    from 1500 To 360
        SetMemory(0x6604C0, Add, -240),# units:Build Time  index:76    from 600 To 360
        SetMemory(0x6604C0, Add, -55050240),# units:Build Time  index:77    from 1200 To 360
        SetMemory(0x6604C4, Add, -1140),# units:Build Time  index:78    from 1500 To 360
        SetMemory(0x6604C4, Add, -74711040),# units:Build Time  index:79    from 1500 To 360
        SetMemory(0x6604C8, Add, -2040),# units:Build Time  index:80    from 2400 To 360
        SetMemory(0x6604C8, Add, -94371840),# units:Build Time  index:81    from 1800 To 360
        SetMemory(0x6604CC, Add, -3840),# units:Build Time  index:82    from 4200 To 360
        SetMemory(0x6604CC, Add, -45219840),# units:Build Time  index:83    from 1050 To 360
        SetMemory(0x6604D0, Add, -240),# units:Build Time  index:84    from 600 To 360
        SetMemory(0x6604D4, Add, -4440),# units:Build Time  index:86    from 4800 To 360
        SetMemory(0x6604D4, Add, -74711040),# units:Build Time  index:87    from 1500 To 360
        SetMemory(0x6604D8, Add, -2040),# units:Build Time  index:88    from 2400 To 360
        SetMemory(0x6604D8, Add, 23527424),# units:Build Time  index:89    from 1 To 360
        SetMemory(0x6604DC, Add, 359),# units:Build Time  index:90    from 1 To 360
        SetMemory(0x6604E0, Add, 23527424),# units:Build Time  index:93    from 1 To 360
        SetMemory(0x6604E4, Add, 359),# units:Build Time  index:94    from 1 To 360
        SetMemory(0x6604E4, Add, 23527424),# units:Build Time  index:95    from 1 To 360
        SetMemory(0x6604E8, Add, 359),# units:Build Time  index:96    from 1 To 360
        SetMemory(0x6604EC, Add, -390),# units:Build Time  index:98    from 750 To 360
        SetMemory(0x6604EC, Add, -74711040),# units:Build Time  index:99    from 1500 To 360
        SetMemory(0x6604F0, Add, -1140),# units:Build Time  index:100    from 1500 To 360
        SetMemory(0x6604F4, Add, -4440),# units:Build Time  index:102    from 4800 To 360
        SetMemory(0x6604F4, Add, -15728640),# units:Build Time  index:103    from 600 To 360
        SetMemory(0x6604F8, Add, -1140),# units:Build Time  index:104    from 1500 To 360
        SetMemory(0x6604FC, Add, -1440),# units:Build Time  index:106    from 1800 To 360
        SetMemory(0x6604FC, Add, -15728640),# units:Build Time  index:107    from 600 To 360
        SetMemory(0x660500, Add, -15728640),# units:Build Time  index:109    from 600 To 360
        SetMemory(0x660504, Add, -240),# units:Build Time  index:110    from 600 To 360
        SetMemory(0x660504, Add, -55050240),# units:Build Time  index:111    from 1200 To 360
        SetMemory(0x660508, Add, -840),# units:Build Time  index:112    from 1200 To 360
        SetMemory(0x660508, Add, -55050240),# units:Build Time  index:113    from 1200 To 360
        SetMemory(0x66050C, Add, -690),# units:Build Time  index:114    from 1050 To 360
        SetMemory(0x66050C, Add, -15728640),# units:Build Time  index:115    from 600 To 360
        SetMemory(0x660510, Add, -540),# units:Build Time  index:116    from 900 To 360
        SetMemory(0x660510, Add, -15728640),# units:Build Time  index:117    from 600 To 360
        SetMemory(0x660514, Add, -240),# units:Build Time  index:118    from 600 To 360
        SetMemory(0x660518, Add, -240),# units:Build Time  index:120    from 600 To 360
        SetMemory(0x66051C, Add, -540),# units:Build Time  index:122    from 900 To 360
        SetMemory(0x66051C, Add, -55050240),# units:Build Time  index:123    from 1200 To 360
        SetMemory(0x660520, Add, -90),# units:Build Time  index:124    from 450 To 360
        SetMemory(0x660520, Add, -5898240),# units:Build Time  index:125    from 450 To 360
        SetMemory(0x660524, Add, -4440),# units:Build Time  index:126    from 4800 To 360
        SetMemory(0x660524, Add, -35389440),# units:Build Time  index:127    from 900 To 360
        SetMemory(0x660528, Add, 359),# units:Build Time  index:128    from 1 To 360
        SetMemory(0x660528, Add, 23527424),# units:Build Time  index:129    from 1 To 360
        SetMemory(0x66052C, Add, -1440),# units:Build Time  index:130    from 1800 To 360
        SetMemory(0x66052C, Add, -94371840),# units:Build Time  index:131    from 1800 To 360
        SetMemory(0x660530, Add, -1140),# units:Build Time  index:132    from 1500 To 360
        SetMemory(0x660530, Add, -94371840),# units:Build Time  index:133    from 1800 To 360
        SetMemory(0x660534, Add, -240),# units:Build Time  index:134    from 600 To 360
        SetMemory(0x660534, Add, -15728640),# units:Build Time  index:135    from 600 To 360
        SetMemory(0x660538, Add, -540),# units:Build Time  index:136    from 900 To 360
        SetMemory(0x660538, Add, -94371840),# units:Build Time  index:137    from 1800 To 360
        SetMemory(0x66053C, Add, -540),# units:Build Time  index:138    from 900 To 360
        SetMemory(0x66053C, Add, -15728640),# units:Build Time  index:139    from 600 To 360
        SetMemory(0x660540, Add, -840),# units:Build Time  index:140    from 1200 To 360
        SetMemory(0x660540, Add, -94371840),# units:Build Time  index:141    from 1800 To 360
        SetMemory(0x660544, Add, -840),# units:Build Time  index:142    from 1200 To 360
        SetMemory(0x660544, Add, 3932160),# units:Build Time  index:143    from 300 To 360
        SetMemory(0x660548, Add, 60),# units:Build Time  index:144    from 300 To 360
        SetMemory(0x66054C, Add, 60),# units:Build Time  index:146    from 300 To 360
        SetMemory(0x66054C, Add, 23527424),# units:Build Time  index:147    from 1 To 360
        SetMemory(0x660550, Add, 359),# units:Build Time  index:148    from 1 To 360
        SetMemory(0x660550, Add, -15728640),# units:Build Time  index:149    from 600 To 360
        SetMemory(0x660554, Add, 360),# units:Build Time  index:150    from 0 To 360
        SetMemory(0x660554, Add, 23592960),# units:Build Time  index:151    from 0 To 360
        SetMemory(0x660558, Add, 360),# units:Build Time  index:152    from 0 To 360
        SetMemory(0x66055C, Add, -1440),# units:Build Time  index:154    from 1800 To 360
        SetMemory(0x66055C, Add, -55050240),# units:Build Time  index:155    from 1200 To 360
        SetMemory(0x660560, Add, -90),# units:Build Time  index:156    from 450 To 360
        SetMemory(0x660560, Add, -15728640),# units:Build Time  index:157    from 600 To 360
        SetMemory(0x660564, Add, -5898240),# units:Build Time  index:159    from 450 To 360
        SetMemory(0x660568, Add, -540),# units:Build Time  index:160    from 900 To 360
        SetMemory(0x66056C, Add, -390),# units:Build Time  index:162    from 750 To 360
        SetMemory(0x66056C, Add, -35389440),# units:Build Time  index:163    from 900 To 360
        SetMemory(0x660570, Add, -540),# units:Build Time  index:164    from 900 To 360
        SetMemory(0x660570, Add, -35389440),# units:Build Time  index:165    from 900 To 360
        SetMemory(0x660574, Add, -240),# units:Build Time  index:166    from 600 To 360
        SetMemory(0x660574, Add, -45219840),# units:Build Time  index:167    from 1050 To 360
        SetMemory(0x660578, Add, 359),# units:Build Time  index:168    from 1 To 360
        SetMemory(0x660578, Add, -35389440),# units:Build Time  index:169    from 900 To 360
        SetMemory(0x66057C, Add, -540),# units:Build Time  index:170    from 900 To 360
        SetMemory(0x66057C, Add, -5898240),# units:Build Time  index:171    from 450 To 360
        SetMemory(0x660580, Add, -90),# units:Build Time  index:172    from 450 To 360
        SetMemory(0x660580, Add, 23527424),# units:Build Time  index:173    from 1 To 360
        SetMemory(0x660584, Add, 359),# units:Build Time  index:174    from 1 To 360
        SetMemory(0x660584, Add, -290979840),# units:Build Time  index:175    from 4800 To 360
        SetMemory(0x6605A0, Add, -133693440),# units:Build Time  index:189    from 2400 To 360
        SetMemory(0x6605A4, Add, -4440),# units:Build Time  index:190    from 4800 To 360
        SetMemory(0x6605AC, Add, 359),# units:Build Time  index:194    from 1 To 360
        SetMemory(0x6605AC, Add, 23527424),# units:Build Time  index:195    from 1 To 360
        SetMemory(0x6605B0, Add, 359),# units:Build Time  index:196    from 1 To 360
        SetMemory(0x6605B8, Add, -2040),# units:Build Time  index:200    from 2400 To 360
        SetMemory(0x6605B8, Add, -133693440),# units:Build Time  index:201    from 2400 To 360
        SetMemory(0x6605D4, Add, 23527424),# units:Build Time  index:215    from 1 To 360
        SetMemory(0x6605D8, Add, 359),# units:Build Time  index:216    from 1 To 360
        SetMemory(0x6605D8, Add, 23527424),# units:Build Time  index:217    from 1 To 360
        SetMemory(0x6605DC, Add, 359),# units:Build Time  index:218    from 1 To 360
        SetMemory(0x6605DC, Add, 23527424),# units:Build Time  index:219    from 1 To 360
        SetMemory(0x6605E0, Add, 359),# units:Build Time  index:220    from 1 To 360
        SetMemory(0x6605E0, Add, 23527424),# units:Build Time  index:221    from 1 To 360
        SetMemory(0x6605E4, Add, 359),# units:Build Time  index:222    from 1 To 360
        SetMemory(0x6605E4, Add, 23527424),# units:Build Time  index:223    from 1 To 360
        SetMemory(0x6637C4, Add, 256),# units:Staredit Group Flags  index:37    from 9 To 10
        SetMemory(0x6637C4, Add, 65536),# units:Staredit Group Flags  index:38    from 9 To 10
        SetMemory(0x6637C4, Add, 16777216),# units:Staredit Group Flags  index:39    from 9 To 10
        SetMemory(0x6637C8, Add, 1),# units:Staredit Group Flags  index:40    from 9 To 10
        SetMemory(0x6637C8, Add, 256),# units:Staredit Group Flags  index:41    from 9 To 10
        SetMemory(0x6637C8, Add, 65536),# units:Staredit Group Flags  index:42    from 9 To 10
        SetMemory(0x6637C8, Add, 16777216),# units:Staredit Group Flags  index:43    from 9 To 10
        SetMemory(0x6637CC, Add, 1),# units:Staredit Group Flags  index:44    from 9 To 10
        SetMemory(0x6637CC, Add, 256),# units:Staredit Group Flags  index:45    from 9 To 10
        SetMemory(0x6637CC, Add, 65536),# units:Staredit Group Flags  index:46    from 9 To 10
        SetMemory(0x6637CC, Add, 16777216),# units:Staredit Group Flags  index:47    from 9 To 10
        SetMemory(0x6637D0, Add, 1),# units:Staredit Group Flags  index:48    from 9 To 10
        SetMemory(0x6637D0, Add, 256),# units:Staredit Group Flags  index:49    from 9 To 10
        SetMemory(0x6637D0, Add, 65536),# units:Staredit Group Flags  index:50    from 9 To 10
        SetMemory(0x6637D0, Add, 16777216),# units:Staredit Group Flags  index:51    from 9 To 10
        SetMemory(0x6637D4, Add, 1),# units:Staredit Group Flags  index:52    from 9 To 10
        SetMemory(0x6637D4, Add, 256),# units:Staredit Group Flags  index:53    from 9 To 10
        SetMemory(0x6637D4, Add, 65536),# units:Staredit Group Flags  index:54    from 9 To 10
        SetMemory(0x6637D4, Add, 16777216),# units:Staredit Group Flags  index:55    from 9 To 10
        SetMemory(0x6637D8, Add, 1),# units:Staredit Group Flags  index:56    from 9 To 10
        SetMemory(0x6637D8, Add, 256),# units:Staredit Group Flags  index:57    from 9 To 10
        SetMemory(0x6637DC, Add, -2),# units:Staredit Group Flags  index:60    from 12 To 10
        SetMemory(0x6637DC, Add, -512),# units:Staredit Group Flags  index:61    from 12 To 10
        SetMemory(0x6637DC, Add, 65536),# units:Staredit Group Flags  index:62    from 9 To 10
        SetMemory(0x6637DC, Add, -33554432),# units:Staredit Group Flags  index:63    from 12 To 10
        SetMemory(0x6637E0, Add, -2),# units:Staredit Group Flags  index:64    from 12 To 10
        SetMemory(0x6637E0, Add, -512),# units:Staredit Group Flags  index:65    from 12 To 10
        SetMemory(0x6637E0, Add, -131072),# units:Staredit Group Flags  index:66    from 12 To 10
        SetMemory(0x6637E0, Add, -33554432),# units:Staredit Group Flags  index:67    from 12 To 10
        SetMemory(0x6637E4, Add, -2),# units:Staredit Group Flags  index:68    from 12 To 10
        SetMemory(0x6637E4, Add, -512),# units:Staredit Group Flags  index:69    from 12 To 10
        SetMemory(0x6637E4, Add, -131072),# units:Staredit Group Flags  index:70    from 12 To 10
        SetMemory(0x6637E4, Add, -33554432),# units:Staredit Group Flags  index:71    from 12 To 10
        SetMemory(0x6637E8, Add, -2),# units:Staredit Group Flags  index:72    from 12 To 10
        SetMemory(0x6637E8, Add, -131072),# units:Staredit Group Flags  index:74    from 12 To 10
        SetMemory(0x6637E8, Add, -33554432),# units:Staredit Group Flags  index:75    from 12 To 10
        SetMemory(0x6637EC, Add, -2),# units:Staredit Group Flags  index:76    from 12 To 10
        SetMemory(0x6637EC, Add, -512),# units:Staredit Group Flags  index:77    from 12 To 10
        SetMemory(0x6637EC, Add, -131072),# units:Staredit Group Flags  index:78    from 12 To 10
        SetMemory(0x6637EC, Add, -33554432),# units:Staredit Group Flags  index:79    from 12 To 10
        SetMemory(0x6637F0, Add, -2),# units:Staredit Group Flags  index:80    from 12 To 10
        SetMemory(0x6637F0, Add, -512),# units:Staredit Group Flags  index:81    from 12 To 10
        SetMemory(0x6637F0, Add, -131072),# units:Staredit Group Flags  index:82    from 12 To 10
        SetMemory(0x6637F0, Add, -33554432),# units:Staredit Group Flags  index:83    from 12 To 10
        SetMemory(0x6637F4, Add, -2),# units:Staredit Group Flags  index:84    from 12 To 10
        SetMemory(0x6637F4, Add, -131072),# units:Staredit Group Flags  index:86    from 12 To 10
        SetMemory(0x6637F4, Add, -33554432),# units:Staredit Group Flags  index:87    from 12 To 10
        SetMemory(0x6637F8, Add, -2),# units:Staredit Group Flags  index:88    from 12 To 10
        SetMemory(0x6637F8, Add, -32256),# units:Staredit Group Flags  index:89    from 136 To 10
        SetMemory(0x6637F8, Add, -8257536),# units:Staredit Group Flags  index:90    from 136 To 10
        SetMemory(0x6637FC, Add, -32256),# units:Staredit Group Flags  index:93    from 136 To 10
        SetMemory(0x6637FC, Add, -8257536),# units:Staredit Group Flags  index:94    from 136 To 10
        SetMemory(0x6637FC, Add, -2113929216),# units:Staredit Group Flags  index:95    from 136 To 10
        SetMemory(0x663800, Add, -126),# units:Staredit Group Flags  index:96    from 136 To 10
        SetMemory(0x663800, Add, -131072),# units:Staredit Group Flags  index:98    from 12 To 10
        SetMemory(0x663804, Add, 16777216),# units:Staredit Group Flags  index:103    from 9 To 10
        SetMemory(0x663808, Add, 1),# units:Staredit Group Flags  index:104    from 9 To 10
        SetMemory(0x663808, Add, -2621440),# units:Staredit Group Flags  index:106    from 50 To 10
        SetMemory(0x663808, Add, -134217728),# units:Staredit Group Flags  index:107    from 18 To 10
        SetMemory(0x66380C, Add, -2048),# units:Staredit Group Flags  index:109    from 18 To 10
        SetMemory(0x66380C, Add, -524288),# units:Staredit Group Flags  index:110    from 18 To 10
        SetMemory(0x66380C, Add, -671088640),# units:Staredit Group Flags  index:111    from 50 To 10
        SetMemory(0x663810, Add, -8),# units:Staredit Group Flags  index:112    from 18 To 10
        SetMemory(0x663810, Add, -10240),# units:Staredit Group Flags  index:113    from 50 To 10
        SetMemory(0x663810, Add, -2621440),# units:Staredit Group Flags  index:114    from 50 To 10
        SetMemory(0x663810, Add, -134217728),# units:Staredit Group Flags  index:115    from 18 To 10
        SetMemory(0x663814, Add, -8),# units:Staredit Group Flags  index:116    from 18 To 10
        SetMemory(0x663814, Add, -2048),# units:Staredit Group Flags  index:117    from 18 To 10
        SetMemory(0x663814, Add, -524288),# units:Staredit Group Flags  index:118    from 18 To 10
        SetMemory(0x663818, Add, -8),# units:Staredit Group Flags  index:120    from 18 To 10
        SetMemory(0x663818, Add, -524288),# units:Staredit Group Flags  index:122    from 18 To 10
        SetMemory(0x663818, Add, -134217728),# units:Staredit Group Flags  index:123    from 18 To 10
        SetMemory(0x66381C, Add, -8),# units:Staredit Group Flags  index:124    from 18 To 10
        SetMemory(0x66381C, Add, -2048),# units:Staredit Group Flags  index:125    from 18 To 10
        SetMemory(0x66381C, Add, -524288),# units:Staredit Group Flags  index:126    from 18 To 10
        SetMemory(0x66381C, Add, -134217728),# units:Staredit Group Flags  index:127    from 18 To 10
        SetMemory(0x663820, Add, -118),# units:Staredit Group Flags  index:128    from 128 To 10
        SetMemory(0x663820, Add, -30208),# units:Staredit Group Flags  index:129    from 128 To 10
        SetMemory(0x663820, Add, -2555904),# units:Staredit Group Flags  index:130    from 49 To 10
        SetMemory(0x663820, Add, -654311424),# units:Staredit Group Flags  index:131    from 49 To 10
        SetMemory(0x663824, Add, -39),# units:Staredit Group Flags  index:132    from 49 To 10
        SetMemory(0x663824, Add, -9984),# units:Staredit Group Flags  index:133    from 49 To 10
        SetMemory(0x663824, Add, -458752),# units:Staredit Group Flags  index:134    from 17 To 10
        SetMemory(0x663824, Add, -117440512),# units:Staredit Group Flags  index:135    from 17 To 10
        SetMemory(0x663828, Add, -7),# units:Staredit Group Flags  index:136    from 17 To 10
        SetMemory(0x663828, Add, -1792),# units:Staredit Group Flags  index:137    from 17 To 10
        SetMemory(0x663828, Add, -458752),# units:Staredit Group Flags  index:138    from 17 To 10
        SetMemory(0x663828, Add, -117440512),# units:Staredit Group Flags  index:139    from 17 To 10
        SetMemory(0x66382C, Add, -7),# units:Staredit Group Flags  index:140    from 17 To 10
        SetMemory(0x66382C, Add, -1792),# units:Staredit Group Flags  index:141    from 17 To 10
        SetMemory(0x66382C, Add, -458752),# units:Staredit Group Flags  index:142    from 17 To 10
        SetMemory(0x66382C, Add, -117440512),# units:Staredit Group Flags  index:143    from 17 To 10
        SetMemory(0x663830, Add, -7),# units:Staredit Group Flags  index:144    from 17 To 10
        SetMemory(0x663830, Add, -458752),# units:Staredit Group Flags  index:146    from 17 To 10
        SetMemory(0x663830, Add, -117440512),# units:Staredit Group Flags  index:147    from 17 To 10
        SetMemory(0x663834, Add, -7),# units:Staredit Group Flags  index:148    from 17 To 10
        SetMemory(0x663834, Add, -1792),# units:Staredit Group Flags  index:149    from 17 To 10
        SetMemory(0x663834, Add, -458752),# units:Staredit Group Flags  index:150    from 17 To 10
        SetMemory(0x663834, Add, -117440512),# units:Staredit Group Flags  index:151    from 17 To 10
        SetMemory(0x663838, Add, -7),# units:Staredit Group Flags  index:152    from 17 To 10
        SetMemory(0x663838, Add, -2752512),# units:Staredit Group Flags  index:154    from 52 To 10
        SetMemory(0x663838, Add, -704643072),# units:Staredit Group Flags  index:155    from 52 To 10
        SetMemory(0x66383C, Add, -10),# units:Staredit Group Flags  index:156    from 20 To 10
        SetMemory(0x66383C, Add, -2560),# units:Staredit Group Flags  index:157    from 20 To 10
        SetMemory(0x66383C, Add, -167772160),# units:Staredit Group Flags  index:159    from 20 To 10
        SetMemory(0x663840, Add, -42),# units:Staredit Group Flags  index:160    from 52 To 10
        SetMemory(0x663840, Add, -655360),# units:Staredit Group Flags  index:162    from 20 To 10
        SetMemory(0x663840, Add, -167772160),# units:Staredit Group Flags  index:163    from 20 To 10
        SetMemory(0x663844, Add, -10),# units:Staredit Group Flags  index:164    from 20 To 10
        SetMemory(0x663844, Add, -2560),# units:Staredit Group Flags  index:165    from 20 To 10
        SetMemory(0x663844, Add, -655360),# units:Staredit Group Flags  index:166    from 20 To 10
        SetMemory(0x663844, Add, -704643072),# units:Staredit Group Flags  index:167    from 52 To 10
        SetMemory(0x663848, Add, -10),# units:Staredit Group Flags  index:168    from 20 To 10
        SetMemory(0x663848, Add, -2560),# units:Staredit Group Flags  index:169    from 20 To 10
        SetMemory(0x663848, Add, -655360),# units:Staredit Group Flags  index:170    from 20 To 10
        SetMemory(0x663848, Add, -167772160),# units:Staredit Group Flags  index:171    from 20 To 10
        SetMemory(0x66384C, Add, -10),# units:Staredit Group Flags  index:172    from 20 To 10
        SetMemory(0x66384C, Add, -2560),# units:Staredit Group Flags  index:173    from 20 To 10
        SetMemory(0x66384C, Add, -655360),# units:Staredit Group Flags  index:174    from 20 To 10
        SetMemory(0x66384C, Add, -167772160),# units:Staredit Group Flags  index:175    from 20 To 10
        SetMemory(0x66385C, Add, -2560),# units:Staredit Group Flags  index:189    from 20 To 10
        SetMemory(0x66385C, Add, -524288),# units:Staredit Group Flags  index:190    from 18 To 10
        SetMemory(0x663860, Add, 589824),# units:Staredit Group Flags  index:194    from 1 To 10
        SetMemory(0x663860, Add, 134217728),# units:Staredit Group Flags  index:195    from 2 To 10
        SetMemory(0x663864, Add, 6),# units:Staredit Group Flags  index:196    from 4 To 10
        SetMemory(0x663868, Add, -8),# units:Staredit Group Flags  index:200    from 18 To 10
        SetMemory(0x663868, Add, -1792),# units:Staredit Group Flags  index:201    from 17 To 10
        SetMemory(0x663874, Add, -1979711488),# units:Staredit Group Flags  index:215    from 128 To 10
        SetMemory(0x663878, Add, -118),# units:Staredit Group Flags  index:216    from 128 To 10
        SetMemory(0x663878, Add, -30208),# units:Staredit Group Flags  index:217    from 128 To 10
        SetMemory(0x663878, Add, -7733248),# units:Staredit Group Flags  index:218    from 128 To 10
        SetMemory(0x663878, Add, -1979711488),# units:Staredit Group Flags  index:219    from 128 To 10
        SetMemory(0x66387C, Add, -118),# units:Staredit Group Flags  index:220    from 128 To 10
        SetMemory(0x66387C, Add, -30208),# units:Staredit Group Flags  index:221    from 128 To 10
        SetMemory(0x66387C, Add, -7733248),# units:Staredit Group Flags  index:222    from 128 To 10
        SetMemory(0x66387C, Add, -1979711488),# units:Staredit Group Flags  index:223    from 128 To 10
        SetMemory(0x6646F0, Add, -1048576),# units:Supply Provided  index:42    from 16 To 0
        SetMemory(0x664700, Add, -15360),# units:Supply Provided  index:57    from 60 To 0
        SetMemory(0x664730, Add, -1310720),# units:Supply Provided  index:106    from 20 To 0
        SetMemory(0x664734, Add, -4096),# units:Supply Provided  index:109    from 16 To 0
        SetMemory(0x664748, Add, -33554432),# units:Supply Provided  index:131    from 2 To 0
        SetMemory(0x66474C, Add, -2),# units:Supply Provided  index:132    from 2 To 0
        SetMemory(0x66474C, Add, -512),# units:Supply Provided  index:133    from 2 To 0
        SetMemory(0x664760, Add, -1179648),# units:Supply Provided  index:154    from 18 To 0
        SetMemory(0x664764, Add, -16),# units:Supply Provided  index:156    from 16 To 0
        SetMemory(0x663CE8, Add, -512),# units:Supply Required  index:1    from 2 To 0
        SetMemory(0x663CE8, Add, -262144),# units:Supply Required  index:2    from 4 To 0
        SetMemory(0x663CEC, Add, -33554432),# units:Supply Required  index:7    from 2 To 0
        SetMemory(0x663CF0, Add, -4),# units:Supply Required  index:8    from 4 To 0
        SetMemory(0x663CF0, Add, -1024),# units:Supply Required  index:9    from 4 To 0
        SetMemory(0x663CF0, Add, -67108864),# units:Supply Required  index:11    from 4 To 0
        SetMemory(0x663CF4, Add, -12),# units:Supply Required  index:12    from 12 To 0
        SetMemory(0x663D08, Add, -2),# units:Supply Required  index:32    from 2 To 0
        SetMemory(0x663D08, Add, -131072),# units:Supply Required  index:34    from 2 To 0
        SetMemory(0x663D0C, Add, -256),# units:Supply Required  index:37    from 1 To 0
        SetMemory(0x663D0C, Add, -131072),# units:Supply Required  index:38    from 2 To 0
        SetMemory(0x663D0C, Add, -134217728),# units:Supply Required  index:39    from 8 To 0
        SetMemory(0x663D10, Add, -512),# units:Supply Required  index:41    from 2 To 0
        SetMemory(0x663D10, Add, -67108864),# units:Supply Required  index:43    from 4 To 0
        SetMemory(0x663D14, Add, -4),# units:Supply Required  index:44    from 4 To 0
        SetMemory(0x663D14, Add, -1024),# units:Supply Required  index:45    from 4 To 0
        SetMemory(0x663D14, Add, -262144),# units:Supply Required  index:46    from 4 To 0
        SetMemory(0x663D14, Add, -16777216),# units:Supply Required  index:47    from 1 To 0
        SetMemory(0x663D18, Add, -131072),# units:Supply Required  index:50    from 2 To 0
        SetMemory(0x663D24, Add, -4),# units:Supply Required  index:60    from 4 To 0
        SetMemory(0x663D24, Add, -1024),# units:Supply Required  index:61    from 4 To 0
        SetMemory(0x663D24, Add, -262144),# units:Supply Required  index:62    from 4 To 0
        SetMemory(0x663D24, Add, -134217728),# units:Supply Required  index:63    from 8 To 0
        SetMemory(0x663D28, Add, -2),# units:Supply Required  index:64    from 2 To 0
        SetMemory(0x663D28, Add, -1024),# units:Supply Required  index:65    from 4 To 0
        SetMemory(0x663D28, Add, -262144),# units:Supply Required  index:66    from 4 To 0
        SetMemory(0x663D28, Add, -67108864),# units:Supply Required  index:67    from 4 To 0
        SetMemory(0x663D2C, Add, -8),# units:Supply Required  index:68    from 8 To 0
        SetMemory(0x663D2C, Add, -1024),# units:Supply Required  index:69    from 4 To 0
        SetMemory(0x663D2C, Add, -393216),# units:Supply Required  index:70    from 6 To 0
        SetMemory(0x663D2C, Add, -134217728),# units:Supply Required  index:71    from 8 To 0
        SetMemory(0x663D30, Add, -12),# units:Supply Required  index:72    from 12 To 0
        SetMemory(0x663D30, Add, -131072),# units:Supply Required  index:74    from 2 To 0
        SetMemory(0x663D38, Add, -134217728),# units:Supply Required  index:83    from 8 To 0
        SetMemory(0x663D3C, Add, -2),# units:Supply Required  index:84    from 2 To 0
        SetMemory(0x663D4C, Add, -67108864),# units:Supply Required  index:103    from 4 To 0
        SetMemory(0x664410, Add, 65024),# units:Space Required  index:1    from 1 To 255
        SetMemory(0x664410, Add, 16580608),# units:Space Required  index:2    from 2 To 255
        SetMemory(0x664414, Add, 4261412864),# units:Space Required  index:7    from 1 To 255
        SetMemory(0x664418, Add, 16646144),# units:Space Required  index:10    from 1 To 255
        SetMemory(0x664420, Add, 254),# units:Space Required  index:16    from 1 To 255
        SetMemory(0x664420, Add, 4244635648),# units:Space Required  index:19    from 2 To 255
        SetMemory(0x664424, Add, 254),# units:Space Required  index:20    from 1 To 255
        SetMemory(0x664430, Add, 254),# units:Space Required  index:32    from 1 To 255
        SetMemory(0x664430, Add, 16646144),# units:Space Required  index:34    from 1 To 255
        SetMemory(0x664434, Add, 65024),# units:Space Required  index:37    from 1 To 255
        SetMemory(0x664434, Add, 16580608),# units:Space Required  index:38    from 2 To 255
        SetMemory(0x664434, Add, 4211081216),# units:Space Required  index:39    from 4 To 255
        SetMemory(0x664438, Add, 254),# units:Space Required  index:40    from 1 To 255
        SetMemory(0x664438, Add, 65024),# units:Space Required  index:41    from 1 To 255
        SetMemory(0x66443C, Add, 16580608),# units:Space Required  index:46    from 2 To 255
        SetMemory(0x664440, Add, 251),# units:Space Required  index:48    from 4 To 255
        SetMemory(0x664440, Add, 16646144),# units:Space Required  index:50    from 1 To 255
        SetMemory(0x664440, Add, 4261412864),# units:Space Required  index:51    from 1 To 255
        SetMemory(0x664444, Add, 253),# units:Space Required  index:52    from 2 To 255
        SetMemory(0x664444, Add, 64768),# units:Space Required  index:53    from 2 To 255
        SetMemory(0x664444, Add, 16646144),# units:Space Required  index:54    from 1 To 255
        SetMemory(0x66444C, Add, 64768),# units:Space Required  index:61    from 2 To 255
        SetMemory(0x66444C, Add, 4211081216),# units:Space Required  index:63    from 4 To 255
        SetMemory(0x664450, Add, 254),# units:Space Required  index:64    from 1 To 255
        SetMemory(0x664450, Add, 64768),# units:Space Required  index:65    from 2 To 255
        SetMemory(0x664450, Add, 16449536),# units:Space Required  index:66    from 4 To 255
        SetMemory(0x664450, Add, 4244635648),# units:Space Required  index:67    from 2 To 255
        SetMemory(0x664454, Add, 251),# units:Space Required  index:68    from 4 To 255
        SetMemory(0x664458, Add, 16580608),# units:Space Required  index:74    from 2 To 255
        SetMemory(0x664458, Add, 4244635648),# units:Space Required  index:75    from 2 To 255
        SetMemory(0x66445C, Add, 251),# units:Space Required  index:76    from 4 To 255
        SetMemory(0x66445C, Add, 64768),# units:Space Required  index:77    from 2 To 255
        SetMemory(0x66445C, Add, 16449536),# units:Space Required  index:78    from 4 To 255
        SetMemory(0x66445C, Add, 4244635648),# units:Space Required  index:79    from 2 To 255
        SetMemory(0x664460, Add, 64256),# units:Space Required  index:81    from 4 To 255
        SetMemory(0x664460, Add, 4211081216),# units:Space Required  index:83    from 4 To 255
        SetMemory(0x664464, Add, 4244635648),# units:Space Required  index:87    from 2 To 255
        SetMemory(0x664470, Add, 4261412864),# units:Space Required  index:99    from 1 To 255
        SetMemory(0x664474, Add, 254),# units:Space Required  index:100    from 1 To 255
        SetMemory(0x664474, Add, 4211081216),# units:Space Required  index:103    from 4 To 255
        SetMemory(0x664478, Add, 254),# units:Space Required  index:104    from 1 To 255
        SetMemory(0x660990, Add, -134217728),# units:Space Provided  index:11    from 8 To 0
        SetMemory(0x6609B0, Add, -524288),# units:Space Provided  index:42    from 8 To 0
        SetMemory(0x6609C0, Add, -2048),# units:Space Provided  index:57    from 8 To 0
        SetMemory(0x6609CC, Add, -2048),# units:Space Provided  index:69    from 8 To 0
        SetMemory(0x660A04, Add, -1024),# units:Space Provided  index:125    from 4 To 0
        SetMemory(0x663408, Add, -11468800),# units:Build Score  index:1    from 175 To 0
        SetMemory(0x66340C, Add, -75),# units:Build Score  index:2    from 75 To 0
        SetMemory(0x663414, Add, -3276800),# units:Build Score  index:7    from 50 To 0
        SetMemory(0x663418, Add, -400),# units:Build Score  index:8    from 400 To 0
        SetMemory(0x663418, Add, -40960000),# units:Build Score  index:9    from 625 To 0
        SetMemory(0x66341C, Add, -19660800),# units:Build Score  index:11    from 300 To 0
        SetMemory(0x663420, Add, -1200),# units:Build Score  index:12    from 1200 To 0
        SetMemory(0x663448, Add, -100),# units:Build Score  index:32    from 100 To 0
        SetMemory(0x66344C, Add, -125),# units:Build Score  index:34    from 125 To 0
        SetMemory(0x663450, Add, -1638400),# units:Build Score  index:37    from 25 To 0
        SetMemory(0x663454, Add, -125),# units:Build Score  index:38    from 125 To 0
        SetMemory(0x663454, Add, -42598400),# units:Build Score  index:39    from 650 To 0
        SetMemory(0x663458, Add, -3276800),# units:Build Score  index:41    from 50 To 0
        SetMemory(0x66345C, Add, -100),# units:Build Score  index:42    from 100 To 0
        SetMemory(0x66345C, Add, -19660800),# units:Build Score  index:43    from 300 To 0
        SetMemory(0x663460, Add, -550),# units:Build Score  index:44    from 550 To 0
        SetMemory(0x663460, Add, -26214400),# units:Build Score  index:45    from 400 To 0
        SetMemory(0x663464, Add, -225),# units:Build Score  index:46    from 225 To 0
        SetMemory(0x663464, Add, -6553600),# units:Build Score  index:47    from 100 To 0
        SetMemory(0x66346C, Add, -200),# units:Build Score  index:50    from 200 To 0
        SetMemory(0x663480, Add, -350),# units:Build Score  index:60    from 350 To 0
        SetMemory(0x663480, Add, -21299200),# units:Build Score  index:61    from 325 To 0
        SetMemory(0x663484, Add, -550),# units:Build Score  index:62    from 550 To 0
        SetMemory(0x663484, Add, -42598400),# units:Build Score  index:63    from 650 To 0
        SetMemory(0x663488, Add, -50),# units:Build Score  index:64    from 50 To 0
        SetMemory(0x663488, Add, -6553600),# units:Build Score  index:65    from 100 To 0
        SetMemory(0x66348C, Add, -250),# units:Build Score  index:66    from 250 To 0
        SetMemory(0x66348C, Add, -22937600),# units:Build Score  index:67    from 350 To 0
        SetMemory(0x663490, Add, -700),# units:Build Score  index:68    from 700 To 0
        SetMemory(0x663490, Add, -13107200),# units:Build Score  index:69    from 200 To 0
        SetMemory(0x663494, Add, -650),# units:Build Score  index:70    from 650 To 0
        SetMemory(0x663494, Add, -67174400),# units:Build Score  index:71    from 1025 To 0
        SetMemory(0x663498, Add, -950),# units:Build Score  index:72    from 950 To 0
        SetMemory(0x6634AC, Add, -26214400),# units:Build Score  index:83    from 400 To 0
        SetMemory(0x6634B0, Add, -225),# units:Build Score  index:84    from 225 To 0
        SetMemory(0x6634D4, Add, -16384000),# units:Build Score  index:103    from 250 To 0
        SetMemory(0x6634DC, Add, -400),# units:Build Score  index:106    from 400 To 0
        SetMemory(0x6634DC, Add, -4915200),# units:Build Score  index:107    from 75 To 0
        SetMemory(0x6634E0, Add, -3276800),# units:Build Score  index:109    from 50 To 0
        SetMemory(0x6634E4, Add, -50),# units:Build Score  index:110    from 50 To 0
        SetMemory(0x6634E4, Add, -4915200),# units:Build Score  index:111    from 75 To 0
        SetMemory(0x6634E8, Add, -100),# units:Build Score  index:112    from 100 To 0
        SetMemory(0x6634E8, Add, -13107200),# units:Build Score  index:113    from 200 To 0
        SetMemory(0x6634EC, Add, -200),# units:Build Score  index:114    from 200 To 0
        SetMemory(0x6634EC, Add, -6553600),# units:Build Score  index:115    from 100 To 0
        SetMemory(0x6634F0, Add, -275),# units:Build Score  index:116    from 275 To 0
        SetMemory(0x6634F0, Add, -4915200),# units:Build Score  index:117    from 75 To 0
        SetMemory(0x6634F4, Add, -75),# units:Build Score  index:118    from 75 To 0
        SetMemory(0x6634F8, Add, -75),# units:Build Score  index:120    from 75 To 0
        SetMemory(0x6634FC, Add, -65),# units:Build Score  index:122    from 65 To 0
        SetMemory(0x6634FC, Add, -6553600),# units:Build Score  index:123    from 100 To 0
        SetMemory(0x663500, Add, -50),# units:Build Score  index:124    from 50 To 0
        SetMemory(0x663500, Add, -3276800),# units:Build Score  index:125    from 50 To 0
        SetMemory(0x66350C, Add, -300),# units:Build Score  index:130    from 300 To 0
        SetMemory(0x66350C, Add, -19660800),# units:Build Score  index:131    from 300 To 0
        SetMemory(0x663510, Add, -100),# units:Build Score  index:132    from 100 To 0
        SetMemory(0x663510, Add, -6553600),# units:Build Score  index:133    from 100 To 0
        SetMemory(0x663514, Add, -75),# units:Build Score  index:134    from 75 To 0
        SetMemory(0x663514, Add, -6553600),# units:Build Score  index:135    from 100 To 0
        SetMemory(0x663518, Add, -150),# units:Build Score  index:136    from 150 To 0
        SetMemory(0x663518, Add, -13107200),# units:Build Score  index:137    from 200 To 0
        SetMemory(0x66351C, Add, -175),# units:Build Score  index:138    from 175 To 0
        SetMemory(0x66351C, Add, -2621440),# units:Build Score  index:139    from 40 To 0
        SetMemory(0x663520, Add, -275),# units:Build Score  index:140    from 275 To 0
        SetMemory(0x663520, Add, -16384000),# units:Build Score  index:141    from 250 To 0
        SetMemory(0x663524, Add, -75),# units:Build Score  index:142    from 75 To 0
        SetMemory(0x663524, Add, -2621440),# units:Build Score  index:143    from 40 To 0
        SetMemory(0x663528, Add, -25),# units:Build Score  index:144    from 25 To 0
        SetMemory(0x66352C, Add, -40),# units:Build Score  index:146    from 40 To 0
        SetMemory(0x663530, Add, -1638400),# units:Build Score  index:149    from 25 To 0
        SetMemory(0x66353C, Add, -400),# units:Build Score  index:154    from 400 To 0
        SetMemory(0x66353C, Add, -19660800),# units:Build Score  index:155    from 300 To 0
        SetMemory(0x663540, Add, -50),# units:Build Score  index:156    from 50 To 0
        SetMemory(0x663540, Add, -3276800),# units:Build Score  index:157    from 50 To 0
        SetMemory(0x663544, Add, -11468800),# units:Build Score  index:159    from 175 To 0
        SetMemory(0x663548, Add, -75),# units:Build Score  index:160    from 75 To 0
        SetMemory(0x66354C, Add, -100),# units:Build Score  index:162    from 100 To 0
        SetMemory(0x66354C, Add, -13107200),# units:Build Score  index:163    from 200 To 0
        SetMemory(0x663550, Add, -100),# units:Build Score  index:164    from 100 To 0
        SetMemory(0x663550, Add, -16384000),# units:Build Score  index:165    from 250 To 0
        SetMemory(0x663554, Add, -100),# units:Build Score  index:166    from 100 To 0
        SetMemory(0x663554, Add, -19660800),# units:Build Score  index:167    from 300 To 0
        SetMemory(0x663558, Add, -22937600),# units:Build Score  index:169    from 350 To 0
        SetMemory(0x66355C, Add, -450),# units:Build Score  index:170    from 450 To 0
        SetMemory(0x66355C, Add, -8192000),# units:Build Score  index:171    from 125 To 0
        SetMemory(0x663560, Add, -50),# units:Build Score  index:172    from 50 To 0
        SetMemory(0x663EB8, Add, -22937600),# units:Destroy Score  index:1    from 350 To 0
        SetMemory(0x663EBC, Add, -150),# units:Destroy Score  index:2    from 150 To 0
        SetMemory(0x663EC4, Add, -6553600),# units:Destroy Score  index:7    from 100 To 0
        SetMemory(0x663EC8, Add, -800),# units:Destroy Score  index:8    from 800 To 0
        SetMemory(0x663EC8, Add, -81920000),# units:Destroy Score  index:9    from 1250 To 0
        SetMemory(0x663ECC, Add, -400),# units:Destroy Score  index:10    from 400 To 0
        SetMemory(0x663ECC, Add, -39321600),# units:Destroy Score  index:11    from 600 To 0
        SetMemory(0x663ED0, Add, -2400),# units:Destroy Score  index:12    from 2400 To 0
        SetMemory(0x663ED8, Add, -700),# units:Destroy Score  index:16    from 700 To 0
        SetMemory(0x663EDC, Add, -19660800),# units:Destroy Score  index:19    from 300 To 0
        SetMemory(0x663EE0, Add, -200),# units:Destroy Score  index:20    from 200 To 0
        SetMemory(0x663EE0, Add, -104857600),# units:Destroy Score  index:21    from 1600 To 0
        SetMemory(0x663EE4, Add, -2500),# units:Destroy Score  index:22    from 2500 To 0
        SetMemory(0x663EEC, Add, -314572800),# units:Destroy Score  index:27    from 4800 To 0
        SetMemory(0x663EF0, Add, -4800),# units:Destroy Score  index:28    from 4800 To 0
        SetMemory(0x663EF0, Add, -314572800),# units:Destroy Score  index:29    from 4800 To 0
        SetMemory(0x663EF8, Add, -200),# units:Destroy Score  index:32    from 200 To 0
        SetMemory(0x663EFC, Add, -250),# units:Destroy Score  index:34    from 250 To 0
        SetMemory(0x663F00, Add, -3276800),# units:Destroy Score  index:37    from 50 To 0
        SetMemory(0x663F04, Add, -350),# units:Destroy Score  index:38    from 350 To 0
        SetMemory(0x663F04, Add, -85196800),# units:Destroy Score  index:39    from 1300 To 0
        SetMemory(0x663F08, Add, -25),# units:Destroy Score  index:40    from 25 To 0
        SetMemory(0x663F08, Add, -6553600),# units:Destroy Score  index:41    from 100 To 0
        SetMemory(0x663F0C, Add, -200),# units:Destroy Score  index:42    from 200 To 0
        SetMemory(0x663F0C, Add, -39321600),# units:Destroy Score  index:43    from 600 To 0
        SetMemory(0x663F10, Add, -1100),# units:Destroy Score  index:44    from 1100 To 0
        SetMemory(0x663F10, Add, -52428800),# units:Destroy Score  index:45    from 800 To 0
        SetMemory(0x663F14, Add, -450),# units:Destroy Score  index:46    from 450 To 0
        SetMemory(0x663F14, Add, -13107200),# units:Destroy Score  index:47    from 200 To 0
        SetMemory(0x663F18, Add, -2600),# units:Destroy Score  index:48    from 2600 To 0
        SetMemory(0x663F18, Add, -104857600),# units:Destroy Score  index:49    from 1600 To 0
        SetMemory(0x663F1C, Add, -400),# units:Destroy Score  index:50    from 400 To 0
        SetMemory(0x663F1C, Add, -262144000),# units:Destroy Score  index:51    from 4000 To 0
        SetMemory(0x663F20, Add, -900),# units:Destroy Score  index:52    from 900 To 0
        SetMemory(0x663F20, Add, -32768000),# units:Destroy Score  index:53    from 500 To 0
        SetMemory(0x663F24, Add, -100),# units:Destroy Score  index:54    from 100 To 0
        SetMemory(0x663F24, Add, -78643200),# units:Destroy Score  index:55    from 1200 To 0
        SetMemory(0x663F28, Add, -2200),# units:Destroy Score  index:56    from 2200 To 0
        SetMemory(0x663F28, Add, -26214400),# units:Destroy Score  index:57    from 400 To 0
        SetMemory(0x663F30, Add, -700),# units:Destroy Score  index:60    from 700 To 0
        SetMemory(0x663F30, Add, -42598400),# units:Destroy Score  index:61    from 650 To 0
        SetMemory(0x663F34, Add, -1100),# units:Destroy Score  index:62    from 1100 To 0
        SetMemory(0x663F34, Add, -85196800),# units:Destroy Score  index:63    from 1300 To 0
        SetMemory(0x663F38, Add, -100),# units:Destroy Score  index:64    from 100 To 0
        SetMemory(0x663F38, Add, -13107200),# units:Destroy Score  index:65    from 200 To 0
        SetMemory(0x663F3C, Add, -500),# units:Destroy Score  index:66    from 500 To 0
        SetMemory(0x663F3C, Add, -45875200),# units:Destroy Score  index:67    from 700 To 0
        SetMemory(0x663F40, Add, -1400),# units:Destroy Score  index:68    from 1400 To 0
        SetMemory(0x663F40, Add, -26214400),# units:Destroy Score  index:69    from 400 To 0
        SetMemory(0x663F44, Add, -1300),# units:Destroy Score  index:70    from 1300 To 0
        SetMemory(0x663F44, Add, -134348800),# units:Destroy Score  index:71    from 2050 To 0
        SetMemory(0x663F48, Add, -1900),# units:Destroy Score  index:72    from 1900 To 0
        SetMemory(0x663F4C, Add, -400),# units:Destroy Score  index:74    from 400 To 0
        SetMemory(0x663F4C, Add, -52428800),# units:Destroy Score  index:75    from 800 To 0
        SetMemory(0x663F50, Add, -2800),# units:Destroy Score  index:76    from 2800 To 0
        SetMemory(0x663F50, Add, -26214400),# units:Destroy Score  index:77    from 400 To 0
        SetMemory(0x663F54, Add, -1000),# units:Destroy Score  index:78    from 1000 To 0
        SetMemory(0x663F54, Add, -91750400),# units:Destroy Score  index:79    from 1400 To 0
        SetMemory(0x663F58, Add, -2600),# units:Destroy Score  index:80    from 2600 To 0
        SetMemory(0x663F58, Add, -104857600),# units:Destroy Score  index:81    from 1600 To 0
        SetMemory(0x663F5C, Add, -3800),# units:Destroy Score  index:82    from 3800 To 0
        SetMemory(0x663F5C, Add, -52428800),# units:Destroy Score  index:83    from 800 To 0
        SetMemory(0x663F60, Add, -450),# units:Destroy Score  index:84    from 450 To 0
        SetMemory(0x663F64, Add, -4100),# units:Destroy Score  index:86    from 4100 To 0
        SetMemory(0x663F64, Add, -91750400),# units:Destroy Score  index:87    from 1400 To 0
        SetMemory(0x663F68, Add, -2400),# units:Destroy Score  index:88    from 2400 To 0
        SetMemory(0x663F68, Add, -655360),# units:Destroy Score  index:89    from 10 To 0
        SetMemory(0x663F6C, Add, -10),# units:Destroy Score  index:90    from 10 To 0
        SetMemory(0x663F70, Add, -655360),# units:Destroy Score  index:93    from 10 To 0
        SetMemory(0x663F74, Add, -10),# units:Destroy Score  index:94    from 10 To 0
        SetMemory(0x663F74, Add, -655360),# units:Destroy Score  index:95    from 10 To 0
        SetMemory(0x663F78, Add, -10),# units:Destroy Score  index:96    from 10 To 0
        SetMemory(0x663F7C, Add, -1300),# units:Destroy Score  index:98    from 1300 To 0
        SetMemory(0x663F7C, Add, -45875200),# units:Destroy Score  index:99    from 700 To 0
        SetMemory(0x663F80, Add, -700),# units:Destroy Score  index:100    from 700 To 0
        SetMemory(0x663F84, Add, -4800),# units:Destroy Score  index:102    from 4800 To 0
        SetMemory(0x663F84, Add, -32768000),# units:Destroy Score  index:103    from 500 To 0
        SetMemory(0x663F88, Add, -700),# units:Destroy Score  index:104    from 700 To 0
        SetMemory(0x663F8C, Add, -1200),# units:Destroy Score  index:106    from 1200 To 0
        SetMemory(0x663F8C, Add, -14745600),# units:Destroy Score  index:107    from 225 To 0
        SetMemory(0x663F90, Add, -9830400),# units:Destroy Score  index:109    from 150 To 0
        SetMemory(0x663F94, Add, -150),# units:Destroy Score  index:110    from 150 To 0
        SetMemory(0x663F94, Add, -14745600),# units:Destroy Score  index:111    from 225 To 0
        SetMemory(0x663F98, Add, -300),# units:Destroy Score  index:112    from 300 To 0
        SetMemory(0x663F98, Add, -39321600),# units:Destroy Score  index:113    from 600 To 0
        SetMemory(0x663F9C, Add, -600),# units:Destroy Score  index:114    from 600 To 0
        SetMemory(0x663F9C, Add, -19660800),# units:Destroy Score  index:115    from 300 To 0
        SetMemory(0x663FA0, Add, -825),# units:Destroy Score  index:116    from 825 To 0
        SetMemory(0x663FA0, Add, -14745600),# units:Destroy Score  index:117    from 225 To 0
        SetMemory(0x663FA4, Add, -225),# units:Destroy Score  index:118    from 225 To 0
        SetMemory(0x663FA8, Add, -225),# units:Destroy Score  index:120    from 225 To 0
        SetMemory(0x663FAC, Add, -195),# units:Destroy Score  index:122    from 195 To 0
        SetMemory(0x663FAC, Add, -19660800),# units:Destroy Score  index:123    from 300 To 0
        SetMemory(0x663FB0, Add, -150),# units:Destroy Score  index:124    from 150 To 0
        SetMemory(0x663FB0, Add, -9830400),# units:Destroy Score  index:125    from 150 To 0
        SetMemory(0x663FB4, Add, -5000),# units:Destroy Score  index:126    from 5000 To 0
        SetMemory(0x663FB4, Add, -327680000),# units:Destroy Score  index:127    from 5000 To 0
        SetMemory(0x663FBC, Add, -900),# units:Destroy Score  index:130    from 900 To 0
        SetMemory(0x663FBC, Add, -58982400),# units:Destroy Score  index:131    from 900 To 0
        SetMemory(0x663FC0, Add, -1200),# units:Destroy Score  index:132    from 1200 To 0
        SetMemory(0x663FC0, Add, -98304000),# units:Destroy Score  index:133    from 1500 To 0
        SetMemory(0x663FC4, Add, -225),# units:Destroy Score  index:134    from 225 To 0
        SetMemory(0x663FC4, Add, -19660800),# units:Destroy Score  index:135    from 300 To 0
        SetMemory(0x663FC8, Add, -450),# units:Destroy Score  index:136    from 450 To 0
        SetMemory(0x663FC8, Add, -88473600),# units:Destroy Score  index:137    from 1350 To 0
        SetMemory(0x663FCC, Add, -525),# units:Destroy Score  index:138    from 525 To 0
        SetMemory(0x663FCC, Add, -7864320),# units:Destroy Score  index:139    from 120 To 0
        SetMemory(0x663FD0, Add, -825),# units:Destroy Score  index:140    from 825 To 0
        SetMemory(0x663FD0, Add, -49152000),# units:Destroy Score  index:141    from 750 To 0
        SetMemory(0x663FD4, Add, -225),# units:Destroy Score  index:142    from 225 To 0
        SetMemory(0x663FD4, Add, -7864320),# units:Destroy Score  index:143    from 120 To 0
        SetMemory(0x663FD8, Add, -195),# units:Destroy Score  index:144    from 195 To 0
        SetMemory(0x663FDC, Add, -240),# units:Destroy Score  index:146    from 240 To 0
        SetMemory(0x663FDC, Add, -655360000),# units:Destroy Score  index:147    from 10000 To 0
        SetMemory(0x663FE0, Add, -10000),# units:Destroy Score  index:148    from 10000 To 0
        SetMemory(0x663FE0, Add, -4915200),# units:Destroy Score  index:149    from 75 To 0
        SetMemory(0x663FE4, Add, -5000),# units:Destroy Score  index:150    from 5000 To 0
        SetMemory(0x663FE4, Add, -163840000),# units:Destroy Score  index:151    from 2500 To 0
        SetMemory(0x663FE8, Add, -2500),# units:Destroy Score  index:152    from 2500 To 0
        SetMemory(0x663FEC, Add, -1200),# units:Destroy Score  index:154    from 1200 To 0
        SetMemory(0x663FEC, Add, -58982400),# units:Destroy Score  index:155    from 900 To 0
        SetMemory(0x663FF0, Add, -150),# units:Destroy Score  index:156    from 150 To 0
        SetMemory(0x663FF0, Add, -9830400),# units:Destroy Score  index:157    from 150 To 0
        SetMemory(0x663FF4, Add, -34406400),# units:Destroy Score  index:159    from 525 To 0
        SetMemory(0x663FF8, Add, -225),# units:Destroy Score  index:160    from 225 To 0
        SetMemory(0x663FFC, Add, -300),# units:Destroy Score  index:162    from 300 To 0
        SetMemory(0x663FFC, Add, -39321600),# units:Destroy Score  index:163    from 600 To 0
        SetMemory(0x664000, Add, -300),# units:Destroy Score  index:164    from 300 To 0
        SetMemory(0x664000, Add, -49152000),# units:Destroy Score  index:165    from 750 To 0
        SetMemory(0x664004, Add, -300),# units:Destroy Score  index:166    from 300 To 0
        SetMemory(0x664004, Add, -58982400),# units:Destroy Score  index:167    from 900 To 0
        SetMemory(0x664008, Add, -5000),# units:Destroy Score  index:168    from 5000 To 0
        SetMemory(0x664008, Add, -68812800),# units:Destroy Score  index:169    from 1050 To 0
        SetMemory(0x66400C, Add, -1350),# units:Destroy Score  index:170    from 1350 To 0
        SetMemory(0x66400C, Add, -24576000),# units:Destroy Score  index:171    from 375 To 0
        SetMemory(0x664010, Add, -150),# units:Destroy Score  index:172    from 150 To 0
        SetMemory(0x664010, Add, -163840000),# units:Destroy Score  index:173    from 2500 To 0
        SetMemory(0x664014, Add, -5000),# units:Destroy Score  index:174    from 5000 To 0
        SetMemory(0x664014, Add, -327680000),# units:Destroy Score  index:175    from 5000 To 0
        SetMemory(0x664030, Add, -131072000),# units:Destroy Score  index:189    from 2000 To 0
        SetMemory(0x664034, Add, -3600),# units:Destroy Score  index:190    from 3600 To 0
        SetMemory(0x664048, Add, -600),# units:Destroy Score  index:200    from 600 To 0
        SetMemory(0x664048, Add, -262144000),# units:Destroy Score  index:201    from 4000 To 0
        SetMemory(0x6606F8, Add, -65536),# units:Broodwar Unit Flag  index:34    from 1 To 0
        SetMemory(0x660714, Add, -1),# units:Broodwar Unit Flag  index:60    from 1 To 0
        SetMemory(0x660714, Add, -256),# units:Broodwar Unit Flag  index:61    from 1 To 0
        SetMemory(0x660714, Add, -65536),# units:Broodwar Unit Flag  index:62    from 1 To 0
        SetMemory(0x660714, Add, -16777216),# units:Broodwar Unit Flag  index:63    from 1 To 0
        SetMemory(0x660730, Add, -1),# units:Broodwar Unit Flag  index:88    from 1 To 0
        SetMemory(0x660734, Add, -256),# units:Broodwar Unit Flag  index:93    from 1 To 0
        SetMemory(0x660734, Add, -65536),# units:Broodwar Unit Flag  index:94    from 1 To 0
        SetMemory(0x660738, Add, -1),# units:Broodwar Unit Flag  index:96    from 1 To 0
        SetMemory(0x660738, Add, -16777216),# units:Broodwar Unit Flag  index:99    from 1 To 0
        SetMemory(0x66073C, Add, -1),# units:Broodwar Unit Flag  index:100    from 1 To 0
        SetMemory(0x66073C, Add, -16777216),# units:Broodwar Unit Flag  index:103    from 1 To 0
        SetMemory(0x660740, Add, -1),# units:Broodwar Unit Flag  index:104    from 1 To 0
        SetMemory(0x660758, Add, -1),# units:Broodwar Unit Flag  index:128    from 1 To 0
        SetMemory(0x660758, Add, -256),# units:Broodwar Unit Flag  index:129    from 1 To 0
        SetMemory(0x660784, Add, -16777216),# units:Broodwar Unit Flag  index:175    from 1 To 0
        SetMemory(0x660794, Add, -256),# units:Broodwar Unit Flag  index:189    from 1 To 0
        SetMemory(0x660794, Add, -65536),# units:Broodwar Unit Flag  index:190    from 1 To 0
        SetMemory(0x6607A0, Add, -1),# units:Broodwar Unit Flag  index:200    from 1 To 0
        SetMemory(0x6607A0, Add, -256),# units:Broodwar Unit Flag  index:201    from 1 To 0
        SetMemory(0x661524, Add, 33554432),# units:Staredit Availability Flags  index:7    from 463 To 975
        SetMemory(0x66152C, Add, 8),# units:Staredit Availability Flags  index:10    from 455 To 463
        SetMemory(0x661538, Add, 8),# units:Staredit Availability Flags  index:16    from 455 To 463
        SetMemory(0x66153C, Add, 524288),# units:Staredit Availability Flags  index:19    from 455 To 463
        SetMemory(0x661540, Add, 8),# units:Staredit Availability Flags  index:20    from 455 To 463
        SetMemory(0x661540, Add, 524288),# units:Staredit Availability Flags  index:21    from 455 To 463
        SetMemory(0x661544, Add, 8),# units:Staredit Availability Flags  index:22    from 455 To 463
        SetMemory(0x66154C, Add, 30081024),# units:Staredit Availability Flags  index:27    from 4 To 463
        SetMemory(0x661550, Add, 8),# units:Staredit Availability Flags  index:28    from 455 To 463
        SetMemory(0x661550, Add, 524288),# units:Staredit Availability Flags  index:29    from 455 To 463
        SetMemory(0x66155C, Add, -512),# units:Staredit Availability Flags  index:34    from 975 To 463
        SetMemory(0x661568, Add, 8),# units:Staredit Availability Flags  index:40    from 455 To 463
        SetMemory(0x661578, Add, 8),# units:Staredit Availability Flags  index:48    from 455 To 463
        SetMemory(0x661578, Add, 524288),# units:Staredit Availability Flags  index:49    from 455 To 463
        SetMemory(0x66157C, Add, 524288),# units:Staredit Availability Flags  index:51    from 455 To 463
        SetMemory(0x661580, Add, 8),# units:Staredit Availability Flags  index:52    from 455 To 463
        SetMemory(0x661580, Add, 524288),# units:Staredit Availability Flags  index:53    from 455 To 463
        SetMemory(0x661584, Add, 8),# units:Staredit Availability Flags  index:54    from 455 To 463
        SetMemory(0x661584, Add, 524288),# units:Staredit Availability Flags  index:55    from 455 To 463
        SetMemory(0x661588, Add, 8),# units:Staredit Availability Flags  index:56    from 455 To 463
        SetMemory(0x661588, Add, 524288),# units:Staredit Availability Flags  index:57    from 455 To 463
        SetMemory(0x661590, Add, -512),# units:Staredit Availability Flags  index:60    from 975 To 463
        SetMemory(0x661590, Add, -33554432),# units:Staredit Availability Flags  index:61    from 975 To 463
        SetMemory(0x661594, Add, -512),# units:Staredit Availability Flags  index:62    from 975 To 463
        SetMemory(0x661594, Add, -33030144),# units:Staredit Availability Flags  index:63    from 967 To 463
        SetMemory(0x6615A0, Add, 8),# units:Staredit Availability Flags  index:68    from 455 To 463
        SetMemory(0x6615AC, Add, 8),# units:Staredit Availability Flags  index:74    from 455 To 463
        SetMemory(0x6615AC, Add, 524288),# units:Staredit Availability Flags  index:75    from 455 To 463
        SetMemory(0x6615B0, Add, 8),# units:Staredit Availability Flags  index:76    from 455 To 463
        SetMemory(0x6615B0, Add, 524288),# units:Staredit Availability Flags  index:77    from 455 To 463
        SetMemory(0x6615B4, Add, 8),# units:Staredit Availability Flags  index:78    from 455 To 463
        SetMemory(0x6615B4, Add, 524288),# units:Staredit Availability Flags  index:79    from 455 To 463
        SetMemory(0x6615B8, Add, 8),# units:Staredit Availability Flags  index:80    from 455 To 463
        SetMemory(0x6615B8, Add, 524288),# units:Staredit Availability Flags  index:81    from 455 To 463
        SetMemory(0x6615BC, Add, 8),# units:Staredit Availability Flags  index:82    from 455 To 463
        SetMemory(0x6615C4, Add, 8),# units:Staredit Availability Flags  index:86    from 455 To 463
        SetMemory(0x6615C4, Add, 30081024),# units:Staredit Availability Flags  index:87    from 4 To 463
        SetMemory(0x6615C8, Add, -504),# units:Staredit Availability Flags  index:88    from 967 To 463
        SetMemory(0x6615C8, Add, 589824),# units:Staredit Availability Flags  index:89    from 454 To 463
        SetMemory(0x6615CC, Add, 9),# units:Staredit Availability Flags  index:90    from 454 To 463
        SetMemory(0x6615D0, Add, -32964608),# units:Staredit Availability Flags  index:93    from 966 To 463
        SetMemory(0x6615D4, Add, -503),# units:Staredit Availability Flags  index:94    from 966 To 463
        SetMemory(0x6615D4, Add, 589824),# units:Staredit Availability Flags  index:95    from 454 To 463
        SetMemory(0x6615D8, Add, -503),# units:Staredit Availability Flags  index:96    from 966 To 463
        SetMemory(0x6615DC, Add, 459),# units:Staredit Availability Flags  index:98    from 4 To 463
        SetMemory(0x6615DC, Add, -33030144),# units:Staredit Availability Flags  index:99    from 967 To 463
        SetMemory(0x6615E0, Add, -504),# units:Staredit Availability Flags  index:100    from 967 To 463
        SetMemory(0x6615E4, Add, 459),# units:Staredit Availability Flags  index:102    from 4 To 463
        SetMemory(0x6615E4, Add, -33030144),# units:Staredit Availability Flags  index:103    from 967 To 463
        SetMemory(0x6615E8, Add, -504),# units:Staredit Availability Flags  index:104    from 967 To 463
        SetMemory(0x661614, Add, 8),# units:Staredit Availability Flags  index:126    from 455 To 463
        SetMemory(0x661614, Add, 524288),# units:Staredit Availability Flags  index:127    from 455 To 463
        SetMemory(0x661618, Add, -392),# units:Staredit Availability Flags  index:128    from 855 To 463
        SetMemory(0x661618, Add, -25690112),# units:Staredit Availability Flags  index:129    from 855 To 463
        SetMemory(0x66161C, Add, 8),# units:Staredit Availability Flags  index:130    from 455 To 463
        SetMemory(0x66163C, Add, 524288),# units:Staredit Availability Flags  index:147    from 455 To 463
        SetMemory(0x661640, Add, 8),# units:Staredit Availability Flags  index:148    from 455 To 463
        SetMemory(0x661644, Add, 8),# units:Staredit Availability Flags  index:150    from 455 To 463
        SetMemory(0x661644, Add, 524288),# units:Staredit Availability Flags  index:151    from 455 To 463
        SetMemory(0x661648, Add, 8),# units:Staredit Availability Flags  index:152    from 455 To 463
        SetMemory(0x661668, Add, 8),# units:Staredit Availability Flags  index:168    from 455 To 463
        SetMemory(0x661670, Add, 524288),# units:Staredit Availability Flags  index:173    from 455 To 463
        SetMemory(0x661674, Add, 8),# units:Staredit Availability Flags  index:174    from 455 To 463
        SetMemory(0x661674, Add, -33030144),# units:Staredit Availability Flags  index:175    from 967 To 463
        SetMemory(0x661690, Add, -33030144),# units:Staredit Availability Flags  index:189    from 967 To 463
        SetMemory(0x661694, Add, -504),# units:Staredit Availability Flags  index:190    from 967 To 463
        SetMemory(0x66169C, Add, 8),# units:Staredit Availability Flags  index:194    from 455 To 463
        SetMemory(0x66169C, Add, 524288),# units:Staredit Availability Flags  index:195    from 455 To 463
        SetMemory(0x6616A0, Add, 8),# units:Staredit Availability Flags  index:196    from 455 To 463
        SetMemory(0x6616A8, Add, -504),# units:Staredit Availability Flags  index:200    from 967 To 463
        SetMemory(0x6616A8, Add, -33030144),# units:Staredit Availability Flags  index:201    from 967 To 463
        SetMemory(0x6616C4, Add, 7864320),# units:Staredit Availability Flags  index:215    from 343 To 463
        SetMemory(0x6616C8, Add, 120),# units:Staredit Availability Flags  index:216    from 343 To 463
        SetMemory(0x6616C8, Add, 7864320),# units:Staredit Availability Flags  index:217    from 343 To 463
        SetMemory(0x6616CC, Add, 120),# units:Staredit Availability Flags  index:218    from 343 To 463
        SetMemory(0x6616CC, Add, 7864320),# units:Staredit Availability Flags  index:219    from 343 To 463
        SetMemory(0x6616D0, Add, 463),# units:Staredit Availability Flags  index:220    from 0 To 463
        SetMemory(0x6616D0, Add, 30343168),# units:Staredit Availability Flags  index:221    from 0 To 463
        SetMemory(0x6616D4, Add, 463),# units:Staredit Availability Flags  index:222    from 0 To 463
        SetMemory(0x6616D4, Add, 30343168),# units:Staredit Availability Flags  index:223    from 0 To 463
        SetMemory(0x655AC0, Add, -163),# upgrades:Icon  index:0    from 292 To 129
        SetMemory(0x655AC0, Add, -4915200),# upgrades:Icon  index:1    from 293 To 218
        SetMemory(0x655AC4, Add, -74),# upgrades:Icon  index:2    from 291 To 217
        SetMemory(0x655AC4, Add, -5373952),# upgrades:Icon  index:3    from 297 To 215
        SetMemory(0x655AC8, Add, -285),# upgrades:Icon  index:4    from 298 To 13
        SetMemory(0x655AC8, Add, -3014656),# upgrades:Icon  index:5    from 303 To 257
        SetMemory(0x655ACC, Add, 66),# upgrades:Icon  index:6    from 304 To 370
        SetMemory(0x655ACC, Add, 6094848),# upgrades:Icon  index:7    from 288 To 381
        SetMemory(0x655AD0, Add, -23),# upgrades:Icon  index:8    from 289 To 266
        SetMemory(0x655AD0, Add, 4980736),# upgrades:Icon  index:9    from 290 To 366
        SetMemory(0x655AD4, Add, 63),# upgrades:Icon  index:10    from 299 To 362
        SetMemory(0x655AD4, Add, 5636096),# upgrades:Icon  index:11    from 300 To 386
    ])

