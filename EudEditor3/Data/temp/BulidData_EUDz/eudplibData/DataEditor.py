from eudplib import *


def onPluginStart():
    DoActions([  # Basic DatFile Actions
        SetMemory(0x6644F8, Add, 8),# units:Graphics  index:0    from 78 To 86
        SetMemory(0x6644F8, Add, -131072),# units:Graphics  index:2    from 88 To 86
        SetMemory(0x6644F8, Add, 184549376),# units:Graphics  index:3    from 75 To 86
        SetMemory(0x6644FC, Add, 10),# units:Graphics  index:4    from 76 To 86
        SetMemory(0x6644FC, Add, 1024),# units:Graphics  index:5    from 82 To 86
        SetMemory(0x6644FC, Add, 196608),# units:Graphics  index:6    from 83 To 86
        SetMemory(0x664500, Add, 6),# units:Graphics  index:8    from 80 To 86
        SetMemory(0x664500, Add, 851968),# units:Graphics  index:10    from 73 To 86
        SetMemory(0x664500, Add, 234881024),# units:Graphics  index:11    from 72 To 86
        SetMemory(0x664504, Add, 16),# units:Graphics  index:12    from 70 To 86
        SetMemory(0x664508, Add, 2816),# units:Graphics  index:17    from 75 To 86
        SetMemory(0x664508, Add, 655360),# units:Graphics  index:18    from 76 To 86
        SetMemory(0x664508, Add, -671088640),# units:Graphics  index:19    from 88 To 48
        SetMemory(0x66450C, Add, 8),# units:Graphics  index:20    from 78 To 86
        SetMemory(0x66450C, Add, 1536),# units:Graphics  index:21    from 80 To 86
        SetMemory(0x66450C, Add, 67108864),# units:Graphics  index:23    from 82 To 86
        SetMemory(0x664510, Add, 3),# units:Graphics  index:24    from 83 To 86
        SetMemory(0x664510, Add, 512),# units:Graphics  index:25    from 84 To 86
        SetMemory(0x664510, Add, 65536),# units:Graphics  index:26    from 85 To 86
        SetMemory(0x664510, Add, 268435456),# units:Graphics  index:27    from 70 To 86
        SetMemory(0x664514, Add, 16),# units:Graphics  index:28    from 70 To 86
        SetMemory(0x664514, Add, 4096),# units:Graphics  index:29    from 70 To 86
        SetMemory(0x664514, Add, 131072),# units:Graphics  index:30    from 84 To 86
        SetMemory(0x664514, Add, 16777216),# units:Graphics  index:31    from 85 To 86
        SetMemory(0x664518, Add, 13),# units:Graphics  index:32    from 73 To 86
        SetMemory(0x664518, Add, -6750208),# units:Graphics  index:34    from 189 To 86
        SetMemory(0x664518, Add, 1275068416),# units:Graphics  index:35    from 10 To 86
        SetMemory(0x66451C, Add, 80),# units:Graphics  index:36    from 6 To 86
        SetMemory(0x66451C, Add, 18176),# units:Graphics  index:37    from 15 To 86
        SetMemory(0x66451C, Add, 5111808),# units:Graphics  index:38    from 8 To 86
        SetMemory(0x66451C, Add, 1207959552),# units:Graphics  index:39    from 14 To 86
        SetMemory(0x664520, Add, 85),# units:Graphics  index:40    from 1 To 86
        SetMemory(0x664520, Add, 20736),# units:Graphics  index:41    from 5 To 86
        SetMemory(0x664520, Add, 4849664),# units:Graphics  index:42    from 12 To 86
        SetMemory(0x664520, Add, 1258291200),# units:Graphics  index:43    from 11 To 86
        SetMemory(0x664524, Add, 79),# units:Graphics  index:44    from 7 To 86
        SetMemory(0x664524, Add, 18688),# units:Graphics  index:45    from 13 To 86
        SetMemory(0x664524, Add, 5373952),# units:Graphics  index:46    from 4 To 86
        SetMemory(0x664524, Add, 1442840576),# units:Graphics  index:47    from 0 To 86
        SetMemory(0x664528, Add, 72),# units:Graphics  index:48    from 14 To 86
        SetMemory(0x664528, Add, 18688),# units:Graphics  index:49    from 13 To 86
        SetMemory(0x664528, Add, 5505024),# units:Graphics  index:50    from 2 To 86
        SetMemory(0x664528, Add, 1291845632),# units:Graphics  index:51    from 9 To 86
        SetMemory(0x66452C, Add, 82),# units:Graphics  index:52    from 4 To 86
        SetMemory(0x66452C, Add, 19968),# units:Graphics  index:53    from 8 To 86
        SetMemory(0x66452C, Add, 4653056),# units:Graphics  index:54    from 15 To 86
        SetMemory(0x66452C, Add, 1258291200),# units:Graphics  index:55    from 11 To 86
        SetMemory(0x664530, Add, 79),# units:Graphics  index:56    from 7 To 86
        SetMemory(0x664530, Add, 18944),# units:Graphics  index:57    from 12 To 86
        SetMemory(0x664530, Add, 1392508928),# units:Graphics  index:59    from 3 To 86
        SetMemory(0x664534, Add, -105),# units:Graphics  index:60    from 191 To 86
        SetMemory(0x664534, Add, -26112),# units:Graphics  index:61    from 188 To 86
        SetMemory(0x664534, Add, -6488064),# units:Graphics  index:62    from 185 To 86
        SetMemory(0x664534, Add, -1694498816),# units:Graphics  index:63    from 187 To 86
        SetMemory(0x664538, Add, 44),# units:Graphics  index:64    from 42 To 86
        SetMemory(0x664538, Add, 9472),# units:Graphics  index:65    from 49 To 86
        SetMemory(0x664538, Add, 3014656),# units:Graphics  index:66    from 40 To 86
        SetMemory(0x664538, Add, 687865856),# units:Graphics  index:67    from 45 To 86
        SetMemory(0x66453C, Add, 48),# units:Graphics  index:68    from 38 To 86
        SetMemory(0x66453C, Add, 10752),# units:Graphics  index:69    from 44 To 86
        SetMemory(0x66453C, Add, 2818048),# units:Graphics  index:70    from 43 To 86
        SetMemory(0x66453C, Add, 822083584),# units:Graphics  index:71    from 37 To 86
        SetMemory(0x664540, Add, 2621440),# units:Graphics  index:74    from 46 To 86
        SetMemory(0x664540, Add, 671088640),# units:Graphics  index:75    from 46 To 86
        SetMemory(0x664544, Add, 48),# units:Graphics  index:76    from 38 To 86
        SetMemory(0x664544, Add, 9472),# units:Graphics  index:77    from 49 To 86
        SetMemory(0x664544, Add, 3014656),# units:Graphics  index:78    from 40 To 86
        SetMemory(0x664544, Add, 687865856),# units:Graphics  index:79    from 45 To 86
        SetMemory(0x664548, Add, 9984),# units:Graphics  index:81    from 47 To 86
        SetMemory(0x664548, Add, 3080192),# units:Graphics  index:82    from 39 To 86
        SetMemory(0x664548, Add, 654311424),# units:Graphics  index:83    from 47 To 86
        SetMemory(0x66454C, Add, 36),# units:Graphics  index:84    from 50 To 86
        SetMemory(0x66454C, Add, 3211264),# units:Graphics  index:86    from 37 To 86
        SetMemory(0x66454C, Add, 687865856),# units:Graphics  index:87    from 45 To 86
        SetMemory(0x664550, Add, 43),# units:Graphics  index:88    from 43 To 86
        SetMemory(0x664550, Add, -7424),# units:Graphics  index:89    from 115 To 86
        SetMemory(0x664550, Add, -1966080),# units:Graphics  index:90    from 116 To 86
        SetMemory(0x664550, Add, 721420288),# units:Graphics  index:91    from 43 To 86
        SetMemory(0x664554, Add, 43),# units:Graphics  index:92    from 43 To 86
        SetMemory(0x664554, Add, -28672),# units:Graphics  index:93    from 198 To 86
        SetMemory(0x664554, Add, -7405568),# units:Graphics  index:94    from 199 To 86
        SetMemory(0x664554, Add, -469762048),# units:Graphics  index:95    from 114 To 86
        SetMemory(0x664558, Add, -114),# units:Graphics  index:96    from 200 To 86
        SetMemory(0x664558, Add, -25088),# units:Graphics  index:97    from 184 To 86
        SetMemory(0x664558, Add, -6881280),# units:Graphics  index:98    from 191 To 86
        SetMemory(0x664558, Add, 201326592),# units:Graphics  index:99    from 74 To 86
        SetMemory(0x66455C, Add, 12),# units:Graphics  index:100    from 74 To 86
        SetMemory(0x66455C, Add, 1048576),# units:Graphics  index:102    from 70 To 86
        SetMemory(0x66455C, Add, -1677721600),# units:Graphics  index:103    from 186 To 86
        SetMemory(0x664560, Add, 12),# units:Graphics  index:104    from 74 To 86
        SetMemory(0x664560, Add, -524288),# units:Graphics  index:106    from 94 To 86
        SetMemory(0x664560, Add, -117440512),# units:Graphics  index:107    from 93 To 86
        SetMemory(0x664564, Add, -22),# units:Graphics  index:108    from 108 To 86
        SetMemory(0x664564, Add, -2304),# units:Graphics  index:109    from 95 To 86
        SetMemory(0x664564, Add, -1245184),# units:Graphics  index:110    from 105 To 86
        SetMemory(0x664564, Add, -83886080),# units:Graphics  index:111    from 91 To 86
        SetMemory(0x664568, Add, -2816),# units:Graphics  index:113    from 97 To 86
        SetMemory(0x664568, Add, -1572864),# units:Graphics  index:114    from 110 To 86
        SetMemory(0x664568, Add, -167772160),# units:Graphics  index:115    from 96 To 86
        SetMemory(0x66456C, Add, -21),# units:Graphics  index:116    from 107 To 86
        SetMemory(0x66456C, Add, -3072),# units:Graphics  index:117    from 98 To 86
        SetMemory(0x66456C, Add, -1114112),# units:Graphics  index:118    from 103 To 86
        SetMemory(0x66456C, Add, 721420288),# units:Graphics  index:119    from 43 To 86
        SetMemory(0x664570, Add, -14),# units:Graphics  index:120    from 100 To 86
        SetMemory(0x664570, Add, 11008),# units:Graphics  index:121    from 43 To 86
        SetMemory(0x664570, Add, -1638400),# units:Graphics  index:122    from 111 To 86
        SetMemory(0x664570, Add, -100663296),# units:Graphics  index:123    from 92 To 86
        SetMemory(0x664574, Add, -15),# units:Graphics  index:124    from 101 To 86
        SetMemory(0x664574, Add, -4608),# units:Graphics  index:125    from 104 To 86
        SetMemory(0x664574, Add, -1048576),# units:Graphics  index:126    from 102 To 86
        SetMemory(0x664574, Add, -218103808),# units:Graphics  index:127    from 99 To 86
        SetMemory(0x664578, Add, -121),# units:Graphics  index:128    from 207 To 86
        SetMemory(0x664578, Add, -31232),# units:Graphics  index:129    from 208 To 86
        SetMemory(0x664578, Add, 4521984),# units:Graphics  index:130    from 17 To 86
        SetMemory(0x664578, Add, 1073741824),# units:Graphics  index:131    from 22 To 86
        SetMemory(0x66457C, Add, 62),# units:Graphics  index:132    from 24 To 86
        SetMemory(0x66457C, Add, 16128),# units:Graphics  index:133    from 23 To 86
        SetMemory(0x66457C, Add, 3735552),# units:Graphics  index:134    from 29 To 86
        SetMemory(0x66457C, Add, 872415232),# units:Graphics  index:135    from 34 To 86
        SetMemory(0x664580, Add, 59),# units:Graphics  index:136    from 27 To 86
        SetMemory(0x664580, Add, 15360),# units:Graphics  index:137    from 26 To 86
        SetMemory(0x664580, Add, 3801088),# units:Graphics  index:138    from 28 To 86
        SetMemory(0x664580, Add, 1107296256),# units:Graphics  index:139    from 20 To 86
        SetMemory(0x664584, Add, 54),# units:Graphics  index:140    from 32 To 86
        SetMemory(0x664584, Add, 13056),# units:Graphics  index:141    from 35 To 86
        SetMemory(0x664584, Add, 4456448),# units:Graphics  index:142    from 18 To 86
        SetMemory(0x664584, Add, 1090519040),# units:Graphics  index:143    from 21 To 86
        SetMemory(0x664588, Add, 50),# units:Graphics  index:144    from 36 To 86
        SetMemory(0x664588, Add, 11008),# units:Graphics  index:145    from 43 To 86
        SetMemory(0x664588, Add, 3997696),# units:Graphics  index:146    from 25 To 86
        SetMemory(0x664588, Add, 939524096),# units:Graphics  index:147    from 30 To 86
        SetMemory(0x66458C, Add, 55),# units:Graphics  index:148    from 31 To 86
        SetMemory(0x66458C, Add, 13568),# units:Graphics  index:149    from 33 To 86
        SetMemory(0x66458C, Add, 4390912),# units:Graphics  index:150    from 19 To 86
        SetMemory(0x66458C, Add, 1174405120),# units:Graphics  index:151    from 16 To 86
        SetMemory(0x664590, Add, 70),# units:Graphics  index:152    from 16 To 86
        SetMemory(0x664590, Add, 11008),# units:Graphics  index:153    from 43 To 86
        SetMemory(0x664590, Add, 1769472),# units:Graphics  index:154    from 59 To 86
        SetMemory(0x664590, Add, 385875968),# units:Graphics  index:155    from 63 To 86
        SetMemory(0x664594, Add, 24),# units:Graphics  index:156    from 62 To 86
        SetMemory(0x664594, Add, 8704),# units:Graphics  index:157    from 52 To 86
        SetMemory(0x664594, Add, 2818048),# units:Graphics  index:158    from 43 To 86
        SetMemory(0x664594, Add, 553648128),# units:Graphics  index:159    from 53 To 86
        SetMemory(0x664598, Add, 30),# units:Graphics  index:160    from 56 To 86
        SetMemory(0x664598, Add, 11008),# units:Graphics  index:161    from 43 To 86
        SetMemory(0x664598, Add, 1703936),# units:Graphics  index:162    from 60 To 86
        SetMemory(0x664598, Add, 536870912),# units:Graphics  index:163    from 54 To 86
        SetMemory(0x66459C, Add, 29),# units:Graphics  index:164    from 57 To 86
        SetMemory(0x66459C, Add, 8960),# units:Graphics  index:165    from 51 To 86
        SetMemory(0x66459C, Add, 2031616),# units:Graphics  index:166    from 55 To 86
        SetMemory(0x66459C, Add, 352321536),# units:Graphics  index:167    from 65 To 86
        SetMemory(0x6645A0, Add, 20),# units:Graphics  index:168    from 66 To 86
        SetMemory(0x6645A0, Add, 4352),# units:Graphics  index:169    from 69 To 86
        SetMemory(0x6645A0, Add, 1638400),# units:Graphics  index:170    from 61 To 86
        SetMemory(0x6645A0, Add, 318767104),# units:Graphics  index:171    from 67 To 86
        SetMemory(0x6645A4, Add, 22),# units:Graphics  index:172    from 64 To 86
        SetMemory(0x6645A4, Add, 7168),# units:Graphics  index:173    from 58 To 86
        SetMemory(0x6645D0, Add, -196608),# units:Graphics  index:218    from 129 To 126
        SetMemory(0x6612EC, Add, -105),# units:Construction Animation  index:143    from 105 To 0
        SetMemory(0x6612F0, Add, -105),# units:Construction Animation  index:144    from 105 To 0
        SetMemory(0x66134C, Add, -200),# units:Construction Animation  index:167    from 200 To 0
        SetMemory(0x6647BC, Add, 16777216),# units:Shield Enable  index:15    from 0 To 1
        SetMemory(0x6647C0, Add, 1),# units:Shield Enable  index:16    from 0 To 1
        SetMemory(0x660E20, Add, 9900),# units:Shield Amount  index:16    from 100 To 10000
        SetMemory(0x662390, Add, 2496000),# units:Hit Points  index:16    from 20480000 To 22976000
        SetMemory(0x663158, Add, -16),# units:Elevation Level  index:8    from 18 To 2
        SetMemory(0x663158, Add, -3584),# units:Elevation Level  index:9    from 16 To 2
        SetMemory(0x663158, Add, -234881024),# units:Elevation Level  index:11    from 16 To 2
        SetMemory(0x66315C, Add, -14),# units:Elevation Level  index:12    from 16 To 2
        SetMemory(0x663168, Add, -234881024),# units:Elevation Level  index:27    from 16 To 2
        SetMemory(0x66316C, Add, -14),# units:Elevation Level  index:28    from 16 To 2
        SetMemory(0x66317C, Add, -268435456),# units:Elevation Level  index:47    from 18 To 2
        SetMemory(0x663198, Add, -33554432),# units:Elevation Level  index:75    from 4 To 2
        SetMemory(0x6631A4, Add, -16),# units:Elevation Level  index:84    from 18 To 2
        SetMemory(0x6631B4, Add, -33554432),# units:Elevation Level  index:103    from 4 To 2
        SetMemory(0x6631C8, Add, -2),# units:Elevation Level  index:120    from 4 To 2
        SetMemory(0x6631E0, Add, -512),# units:Elevation Level  index:145    from 4 To 2
        SetMemory(0x6631F0, Add, -512),# units:Elevation Level  index:161    from 4 To 2
        SetMemory(0x6631F0, Add, -131072),# units:Elevation Level  index:162    from 4 To 2
        SetMemory(0x6631F0, Add, -33554432),# units:Elevation Level  index:163    from 4 To 2
        SetMemory(0x6631F4, Add, -2),# units:Elevation Level  index:164    from 4 To 2
        SetMemory(0x6631F4, Add, -512),# units:Elevation Level  index:165    from 4 To 2
        SetMemory(0x6631F4, Add, -131072),# units:Elevation Level  index:166    from 4 To 2
        SetMemory(0x6631F4, Add, -33554432),# units:Elevation Level  index:167    from 4 To 2
        SetMemory(0x6631F8, Add, -2),# units:Elevation Level  index:168    from 4 To 2
        SetMemory(0x6631F8, Add, -512),# units:Elevation Level  index:169    from 4 To 2
        SetMemory(0x6631F8, Add, -131072),# units:Elevation Level  index:170    from 4 To 2
        SetMemory(0x6631F8, Add, -33554432),# units:Elevation Level  index:171    from 4 To 2
        SetMemory(0x6631FC, Add, -2),# units:Elevation Level  index:172    from 4 To 2
        SetMemory(0x660FE8, Add, 16777216),# units:Unknown (old Movement)  index:35    from 64 To 65
        SetMemory(0x663DD0, Add, -1),# units:Rank/Sublabel  index:0    from 2 To 1
        SetMemory(0x663DD0, Add, -393216),# units:Rank/Sublabel  index:2    from 6 To 0
        SetMemory(0x663DD0, Add, -117440512),# units:Rank/Sublabel  index:3    from 7 To 0
        SetMemory(0x663DD4, Add, 1),# units:Rank/Sublabel  index:4    from 0 To 1
        SetMemory(0x663DD4, Add, -1792),# units:Rank/Sublabel  index:5    from 8 To 1
        SetMemory(0x663DD4, Add, 65536),# units:Rank/Sublabel  index:6    from 0 To 1
        SetMemory(0x663DD8, Add, -9),# units:Rank/Sublabel  index:8    from 10 To 1
        SetMemory(0x663DD8, Add, -2560),# units:Rank/Sublabel  index:9    from 11 To 1
        SetMemory(0x663DD8, Add, -720896),# units:Rank/Sublabel  index:10    from 12 To 1
        SetMemory(0x663DD8, Add, -134217728),# units:Rank/Sublabel  index:11    from 9 To 1
        SetMemory(0x663DDC, Add, -14),# units:Rank/Sublabel  index:12    from 15 To 1
        SetMemory(0x663DE0, Add, -16),# units:Rank/Sublabel  index:16    from 18 To 2
        SetMemory(0x663DE0, Add, -3072),# units:Rank/Sublabel  index:17    from 13 To 1
        SetMemory(0x663DE4, Add, -17),# units:Rank/Sublabel  index:20    from 17 To 0
        SetMemory(0x663DE4, Add, -3584),# units:Rank/Sublabel  index:21    from 14 To 0
        SetMemory(0x663DE4, Add, -983040),# units:Rank/Sublabel  index:22    from 15 To 0
        SetMemory(0x663DE4, Add, -318767104),# units:Rank/Sublabel  index:23    from 19 To 0
        SetMemory(0x663DE8, Add, -4864),# units:Rank/Sublabel  index:25    from 19 To 0
        SetMemory(0x663DE8, Add, -352321536),# units:Rank/Sublabel  index:27    from 21 To 0
        SetMemory(0x663DEC, Add, -20),# units:Rank/Sublabel  index:28    from 20 To 0
        SetMemory(0x663DEC, Add, -5376),# units:Rank/Sublabel  index:29    from 21 To 0
        SetMemory(0x663DEC, Add, -524288),# units:Rank/Sublabel  index:30    from 8 To 0
        SetMemory(0x663DF0, Add, -4),# units:Rank/Sublabel  index:32    from 4 To 0
        SetMemory(0x663DF0, Add, -196608),# units:Rank/Sublabel  index:34    from 3 To 0
        SetMemory(0x663DF4, Add, -1280),# units:Rank/Sublabel  index:37    from 5 To 0
        SetMemory(0x663DF4, Add, -589824),# units:Rank/Sublabel  index:38    from 9 To 0
        SetMemory(0x663DF4, Add, -234881024),# units:Rank/Sublabel  index:39    from 14 To 0
        SetMemory(0x663DF8, Add, -3),# units:Rank/Sublabel  index:40    from 3 To 0
        SetMemory(0x663DF8, Add, -1024),# units:Rank/Sublabel  index:41    from 4 To 0
        SetMemory(0x663DF8, Add, -524288),# units:Rank/Sublabel  index:42    from 8 To 0
        SetMemory(0x663DF8, Add, -167772160),# units:Rank/Sublabel  index:43    from 10 To 0
        SetMemory(0x663DFC, Add, -11),# units:Rank/Sublabel  index:44    from 11 To 0
        SetMemory(0x663DFC, Add, -3328),# units:Rank/Sublabel  index:45    from 13 To 0
        SetMemory(0x663DFC, Add, -786432),# units:Rank/Sublabel  index:46    from 12 To 0
        SetMemory(0x663DFC, Add, -100663296),# units:Rank/Sublabel  index:47    from 6 To 0
        SetMemory(0x663E00, Add, -15),# units:Rank/Sublabel  index:48    from 15 To 0
        SetMemory(0x663E00, Add, -3840),# units:Rank/Sublabel  index:49    from 15 To 0
        SetMemory(0x663E00, Add, -458752),# units:Rank/Sublabel  index:50    from 7 To 0
        SetMemory(0x663E00, Add, -268435456),# units:Rank/Sublabel  index:51    from 16 To 0
        SetMemory(0x663E04, Add, -15),# units:Rank/Sublabel  index:52    from 15 To 0
        SetMemory(0x663E04, Add, -3840),# units:Rank/Sublabel  index:53    from 15 To 0
        SetMemory(0x663E04, Add, -983040),# units:Rank/Sublabel  index:54    from 15 To 0
        SetMemory(0x663E04, Add, -251658240),# units:Rank/Sublabel  index:55    from 15 To 0
        SetMemory(0x663E08, Add, -15),# units:Rank/Sublabel  index:56    from 15 To 0
        SetMemory(0x663E08, Add, -3840),# units:Rank/Sublabel  index:57    from 15 To 0
        SetMemory(0x663E08, Add, -16777216),# units:Rank/Sublabel  index:59    from 2 To 1
        SetMemory(0x663E0C, Add, -8),# units:Rank/Sublabel  index:60    from 8 To 0
        SetMemory(0x663E0C, Add, -3072),# units:Rank/Sublabel  index:61    from 12 To 0
        SetMemory(0x663E0C, Add, -786432),# units:Rank/Sublabel  index:62    from 12 To 0
        SetMemory(0x663E0C, Add, -150994944),# units:Rank/Sublabel  index:63    from 9 To 0
        SetMemory(0x663E10, Add, -768),# units:Rank/Sublabel  index:65    from 3 To 0
        SetMemory(0x663E10, Add, -262144),# units:Rank/Sublabel  index:66    from 4 To 0
        SetMemory(0x663E10, Add, -100663296),# units:Rank/Sublabel  index:67    from 6 To 0
        SetMemory(0x663E14, Add, -9),# units:Rank/Sublabel  index:68    from 9 To 0
        SetMemory(0x663E14, Add, -1792),# units:Rank/Sublabel  index:69    from 7 To 0
        SetMemory(0x663E14, Add, -524288),# units:Rank/Sublabel  index:70    from 8 To 0
        SetMemory(0x663E14, Add, -167772160),# units:Rank/Sublabel  index:71    from 10 To 0
        SetMemory(0x663E18, Add, -11),# units:Rank/Sublabel  index:72    from 11 To 0
        SetMemory(0x663E18, Add, -786432),# units:Rank/Sublabel  index:74    from 12 To 0
        SetMemory(0x663E18, Add, -251658240),# units:Rank/Sublabel  index:75    from 15 To 0
        SetMemory(0x663E1C, Add, -17),# units:Rank/Sublabel  index:76    from 17 To 0
        SetMemory(0x663E1C, Add, -3328),# units:Rank/Sublabel  index:77    from 13 To 0
        SetMemory(0x663E1C, Add, -917504),# units:Rank/Sublabel  index:78    from 14 To 0
        SetMemory(0x663E1C, Add, -268435456),# units:Rank/Sublabel  index:79    from 16 To 0
        SetMemory(0x663E20, Add, -3072),# units:Rank/Sublabel  index:81    from 12 To 0
        SetMemory(0x663E20, Add, -1114112),# units:Rank/Sublabel  index:82    from 17 To 0
        SetMemory(0x663E20, Add, -83886080),# units:Rank/Sublabel  index:83    from 5 To 0
        SetMemory(0x663E24, Add, -1),# units:Rank/Sublabel  index:84    from 2 To 1
        SetMemory(0x663E24, Add, -786432),# units:Rank/Sublabel  index:86    from 12 To 0
        SetMemory(0x663E24, Add, -268435456),# units:Rank/Sublabel  index:87    from 16 To 0
        SetMemory(0x663E28, Add, -12),# units:Rank/Sublabel  index:88    from 12 To 0
        SetMemory(0x662EC0, Add, -2583691264),# units:Comp AI Idle  index:35    from 156 To 2
        SetMemory(0x662EE4, Add, -2147483648),# units:Comp AI Idle  index:71    from 130 To 2
        SetMemory(0x662EE8, Add, -5376),# units:Comp AI Idle  index:73    from 23 To 2
        SetMemory(0x662EF4, Add, -157),# units:Comp AI Idle  index:84    from 159 To 2
        SetMemory(0x662EF4, Add, -5376),# units:Comp AI Idle  index:85    from 23 To 2
        SetMemory(0x662EF4, Add, -8388608),# units:Comp AI Idle  index:86    from 130 To 2
        SetMemory(0x662EF8, Add, -352321536),# units:Comp AI Idle  index:91    from 23 To 2
        SetMemory(0x662EFC, Add, -21),# units:Comp AI Idle  index:92    from 23 To 2
        SetMemory(0x662F08, Add, -10092544),# units:Comp AI Idle  index:106    from 156 To 2
        SetMemory(0x662F08, Add, -2583691264),# units:Comp AI Idle  index:107    from 156 To 2
        SetMemory(0x662F0C, Add, -154),# units:Comp AI Idle  index:108    from 156 To 2
        SetMemory(0x662F0C, Add, -39424),# units:Comp AI Idle  index:109    from 156 To 2
        SetMemory(0x662F0C, Add, -10092544),# units:Comp AI Idle  index:110    from 156 To 2
        SetMemory(0x662F0C, Add, -2583691264),# units:Comp AI Idle  index:111    from 156 To 2
        SetMemory(0x662F10, Add, -39424),# units:Comp AI Idle  index:113    from 156 To 2
        SetMemory(0x662F10, Add, -10092544),# units:Comp AI Idle  index:114    from 156 To 2
        SetMemory(0x662F10, Add, -2583691264),# units:Comp AI Idle  index:115    from 156 To 2
        SetMemory(0x662F14, Add, -154),# units:Comp AI Idle  index:116    from 156 To 2
        SetMemory(0x662F14, Add, -39424),# units:Comp AI Idle  index:117    from 156 To 2
        SetMemory(0x662F14, Add, -10092544),# units:Comp AI Idle  index:118    from 156 To 2
        SetMemory(0x662F14, Add, -2583691264),# units:Comp AI Idle  index:119    from 156 To 2
        SetMemory(0x662F18, Add, -154),# units:Comp AI Idle  index:120    from 156 To 2
        SetMemory(0x662F18, Add, -39424),# units:Comp AI Idle  index:121    from 156 To 2
        SetMemory(0x662F18, Add, -10092544),# units:Comp AI Idle  index:122    from 156 To 2
        SetMemory(0x662F18, Add, -2583691264),# units:Comp AI Idle  index:123    from 156 To 2
        SetMemory(0x662F1C, Add, -16),# units:Comp AI Idle  index:124    from 18 To 2
        SetMemory(0x662F1C, Add, -39424),# units:Comp AI Idle  index:125    from 156 To 2
        SetMemory(0x662F1C, Add, -10092544),# units:Comp AI Idle  index:126    from 156 To 2
        SetMemory(0x662F1C, Add, -2583691264),# units:Comp AI Idle  index:127    from 156 To 2
        SetMemory(0x662F20, Add, -95),# units:Comp AI Idle  index:128    from 97 To 2
        SetMemory(0x662F20, Add, -24320),# units:Comp AI Idle  index:129    from 97 To 2
        SetMemory(0x662F20, Add, -10092544),# units:Comp AI Idle  index:130    from 156 To 2
        SetMemory(0x662F20, Add, -1660944384),# units:Comp AI Idle  index:131    from 101 To 2
        SetMemory(0x662F24, Add, -99),# units:Comp AI Idle  index:132    from 101 To 2
        SetMemory(0x662F24, Add, -25344),# units:Comp AI Idle  index:133    from 101 To 2
        SetMemory(0x662F24, Add, -10092544),# units:Comp AI Idle  index:134    from 156 To 2
        SetMemory(0x662F24, Add, -2583691264),# units:Comp AI Idle  index:135    from 156 To 2
        SetMemory(0x662F28, Add, -154),# units:Comp AI Idle  index:136    from 156 To 2
        SetMemory(0x662F28, Add, -39424),# units:Comp AI Idle  index:137    from 156 To 2
        SetMemory(0x662F28, Add, -10092544),# units:Comp AI Idle  index:138    from 156 To 2
        SetMemory(0x662F28, Add, -2583691264),# units:Comp AI Idle  index:139    from 156 To 2
        SetMemory(0x662F2C, Add, -154),# units:Comp AI Idle  index:140    from 156 To 2
        SetMemory(0x662F2C, Add, -39424),# units:Comp AI Idle  index:141    from 156 To 2
        SetMemory(0x662F2C, Add, -10092544),# units:Comp AI Idle  index:142    from 156 To 2
        SetMemory(0x662F2C, Add, -1660944384),# units:Comp AI Idle  index:143    from 101 To 2
        SetMemory(0x662F30, Add, -99),# units:Comp AI Idle  index:144    from 101 To 2
        SetMemory(0x662F30, Add, -39424),# units:Comp AI Idle  index:145    from 156 To 2
        SetMemory(0x662F30, Add, -6488064),# units:Comp AI Idle  index:146    from 101 To 2
        SetMemory(0x662F30, Add, -2583691264),# units:Comp AI Idle  index:147    from 156 To 2
        SetMemory(0x662F34, Add, -154),# units:Comp AI Idle  index:148    from 156 To 2
        SetMemory(0x662F34, Add, -39424),# units:Comp AI Idle  index:149    from 156 To 2
        SetMemory(0x662F34, Add, -10092544),# units:Comp AI Idle  index:150    from 156 To 2
        SetMemory(0x662F34, Add, -2583691264),# units:Comp AI Idle  index:151    from 156 To 2
        SetMemory(0x662F38, Add, -154),# units:Comp AI Idle  index:152    from 156 To 2
        SetMemory(0x662F38, Add, -39424),# units:Comp AI Idle  index:153    from 156 To 2
        SetMemory(0x662F38, Add, -10092544),# units:Comp AI Idle  index:154    from 156 To 2
        SetMemory(0x662F38, Add, -2583691264),# units:Comp AI Idle  index:155    from 156 To 2
        SetMemory(0x662F3C, Add, -162),# units:Comp AI Idle  index:156    from 164 To 2
        SetMemory(0x662F3C, Add, -39424),# units:Comp AI Idle  index:157    from 156 To 2
        SetMemory(0x662F3C, Add, -10092544),# units:Comp AI Idle  index:158    from 156 To 2
        SetMemory(0x662F3C, Add, -2583691264),# units:Comp AI Idle  index:159    from 156 To 2
        SetMemory(0x662F40, Add, -154),# units:Comp AI Idle  index:160    from 156 To 2
        SetMemory(0x662F40, Add, -39424),# units:Comp AI Idle  index:161    from 156 To 2
        SetMemory(0x662F40, Add, -1048576),# units:Comp AI Idle  index:162    from 18 To 2
        SetMemory(0x662F40, Add, -2583691264),# units:Comp AI Idle  index:163    from 156 To 2
        SetMemory(0x662F44, Add, -154),# units:Comp AI Idle  index:164    from 156 To 2
        SetMemory(0x662F44, Add, -39424),# units:Comp AI Idle  index:165    from 156 To 2
        SetMemory(0x662F44, Add, -10092544),# units:Comp AI Idle  index:166    from 156 To 2
        SetMemory(0x662F44, Add, -2583691264),# units:Comp AI Idle  index:167    from 156 To 2
        SetMemory(0x662F48, Add, -154),# units:Comp AI Idle  index:168    from 156 To 2
        SetMemory(0x662F48, Add, -39424),# units:Comp AI Idle  index:169    from 156 To 2
        SetMemory(0x662F48, Add, -10092544),# units:Comp AI Idle  index:170    from 156 To 2
        SetMemory(0x662F48, Add, -2583691264),# units:Comp AI Idle  index:171    from 156 To 2
        SetMemory(0x662F4C, Add, -154),# units:Comp AI Idle  index:172    from 156 To 2
        SetMemory(0x662F4C, Add, -39424),# units:Comp AI Idle  index:173    from 156 To 2
        SetMemory(0x662288, Add, -1258291200),# units:Human AI Idle  index:35    from 77 To 2
        SetMemory(0x6622AC, Add, -2147483648),# units:Human AI Idle  index:71    from 130 To 2
        SetMemory(0x6622B0, Add, -5376),# units:Human AI Idle  index:73    from 23 To 2
        SetMemory(0x6622BC, Add, -5376),# units:Human AI Idle  index:85    from 23 To 2
        SetMemory(0x6622BC, Add, -8388608),# units:Human AI Idle  index:86    from 130 To 2
        SetMemory(0x6622C0, Add, -41984),# units:Human AI Idle  index:89    from 166 To 2
        SetMemory(0x6622C0, Add, -10747904),# units:Human AI Idle  index:90    from 166 To 2
        SetMemory(0x6622C0, Add, -352321536),# units:Human AI Idle  index:91    from 23 To 2
        SetMemory(0x6622C4, Add, -21),# units:Human AI Idle  index:92    from 23 To 2
        SetMemory(0x6622C4, Add, -41984),# units:Human AI Idle  index:93    from 166 To 2
        SetMemory(0x6622C4, Add, -10747904),# units:Human AI Idle  index:94    from 166 To 2
        SetMemory(0x6622C4, Add, -2751463424),# units:Human AI Idle  index:95    from 166 To 2
        SetMemory(0x6622C8, Add, -164),# units:Human AI Idle  index:96    from 166 To 2
        SetMemory(0x6622D0, Add, -1376256),# units:Human AI Idle  index:106    from 23 To 2
        SetMemory(0x6622D0, Add, -352321536),# units:Human AI Idle  index:107    from 23 To 2
        SetMemory(0x6622D4, Add, -122),# units:Human AI Idle  index:108    from 124 To 2
        SetMemory(0x6622D4, Add, -5376),# units:Human AI Idle  index:109    from 23 To 2
        SetMemory(0x6622D4, Add, -1376256),# units:Human AI Idle  index:110    from 23 To 2
        SetMemory(0x6622D4, Add, -352321536),# units:Human AI Idle  index:111    from 23 To 2
        SetMemory(0x6622D8, Add, -5376),# units:Human AI Idle  index:113    from 23 To 2
        SetMemory(0x6622D8, Add, -1376256),# units:Human AI Idle  index:114    from 23 To 2
        SetMemory(0x6622D8, Add, -352321536),# units:Human AI Idle  index:115    from 23 To 2
        SetMemory(0x6622DC, Add, -21),# units:Human AI Idle  index:116    from 23 To 2
        SetMemory(0x6622DC, Add, -5376),# units:Human AI Idle  index:117    from 23 To 2
        SetMemory(0x6622DC, Add, -1376256),# units:Human AI Idle  index:118    from 23 To 2
        SetMemory(0x6622DC, Add, -352321536),# units:Human AI Idle  index:119    from 23 To 2
        SetMemory(0x6622E0, Add, -21),# units:Human AI Idle  index:120    from 23 To 2
        SetMemory(0x6622E0, Add, -5376),# units:Human AI Idle  index:121    from 23 To 2
        SetMemory(0x6622E0, Add, -1376256),# units:Human AI Idle  index:122    from 23 To 2
        SetMemory(0x6622E0, Add, -352321536),# units:Human AI Idle  index:123    from 23 To 2
        SetMemory(0x6622E4, Add, -16),# units:Human AI Idle  index:124    from 18 To 2
        SetMemory(0x6622E4, Add, -5376),# units:Human AI Idle  index:125    from 23 To 2
        SetMemory(0x6622E4, Add, -1376256),# units:Human AI Idle  index:126    from 23 To 2
        SetMemory(0x6622E4, Add, -352321536),# units:Human AI Idle  index:127    from 23 To 2
        SetMemory(0x6622E8, Add, -95),# units:Human AI Idle  index:128    from 97 To 2
        SetMemory(0x6622E8, Add, -24320),# units:Human AI Idle  index:129    from 97 To 2
        SetMemory(0x6622E8, Add, -1376256),# units:Human AI Idle  index:130    from 23 To 2
        SetMemory(0x6622E8, Add, -1660944384),# units:Human AI Idle  index:131    from 101 To 2
        SetMemory(0x6622EC, Add, -99),# units:Human AI Idle  index:132    from 101 To 2
        SetMemory(0x6622EC, Add, -25344),# units:Human AI Idle  index:133    from 101 To 2
        SetMemory(0x6622EC, Add, -1376256),# units:Human AI Idle  index:134    from 23 To 2
        SetMemory(0x6622EC, Add, -352321536),# units:Human AI Idle  index:135    from 23 To 2
        SetMemory(0x6622F0, Add, -21),# units:Human AI Idle  index:136    from 23 To 2
        SetMemory(0x6622F0, Add, -5376),# units:Human AI Idle  index:137    from 23 To 2
        SetMemory(0x6622F0, Add, -1376256),# units:Human AI Idle  index:138    from 23 To 2
        SetMemory(0x6622F0, Add, -352321536),# units:Human AI Idle  index:139    from 23 To 2
        SetMemory(0x6622F4, Add, -21),# units:Human AI Idle  index:140    from 23 To 2
        SetMemory(0x6622F4, Add, -5376),# units:Human AI Idle  index:141    from 23 To 2
        SetMemory(0x6622F4, Add, -1376256),# units:Human AI Idle  index:142    from 23 To 2
        SetMemory(0x6622F4, Add, -1660944384),# units:Human AI Idle  index:143    from 101 To 2
        SetMemory(0x6622F8, Add, -99),# units:Human AI Idle  index:144    from 101 To 2
        SetMemory(0x6622F8, Add, -5376),# units:Human AI Idle  index:145    from 23 To 2
        SetMemory(0x6622F8, Add, -6488064),# units:Human AI Idle  index:146    from 101 To 2
        SetMemory(0x6622F8, Add, -352321536),# units:Human AI Idle  index:147    from 23 To 2
        SetMemory(0x6622FC, Add, -21),# units:Human AI Idle  index:148    from 23 To 2
        SetMemory(0x6622FC, Add, -5376),# units:Human AI Idle  index:149    from 23 To 2
        SetMemory(0x6622FC, Add, -1376256),# units:Human AI Idle  index:150    from 23 To 2
        SetMemory(0x6622FC, Add, -352321536),# units:Human AI Idle  index:151    from 23 To 2
        SetMemory(0x662300, Add, -21),# units:Human AI Idle  index:152    from 23 To 2
        SetMemory(0x662300, Add, -5376),# units:Human AI Idle  index:153    from 23 To 2
        SetMemory(0x662300, Add, -1376256),# units:Human AI Idle  index:154    from 23 To 2
        SetMemory(0x662300, Add, -352321536),# units:Human AI Idle  index:155    from 23 To 2
        SetMemory(0x662304, Add, -162),# units:Human AI Idle  index:156    from 164 To 2
        SetMemory(0x662304, Add, -5376),# units:Human AI Idle  index:157    from 23 To 2
        SetMemory(0x662304, Add, -1376256),# units:Human AI Idle  index:158    from 23 To 2
        SetMemory(0x662304, Add, -352321536),# units:Human AI Idle  index:159    from 23 To 2
        SetMemory(0x662308, Add, -21),# units:Human AI Idle  index:160    from 23 To 2
        SetMemory(0x662308, Add, -5376),# units:Human AI Idle  index:161    from 23 To 2
        SetMemory(0x662308, Add, -1048576),# units:Human AI Idle  index:162    from 18 To 2
        SetMemory(0x662308, Add, -352321536),# units:Human AI Idle  index:163    from 23 To 2
        SetMemory(0x66230C, Add, -21),# units:Human AI Idle  index:164    from 23 To 2
        SetMemory(0x66230C, Add, -5376),# units:Human AI Idle  index:165    from 23 To 2
        SetMemory(0x66230C, Add, -1376256),# units:Human AI Idle  index:166    from 23 To 2
        SetMemory(0x66230C, Add, -352321536),# units:Human AI Idle  index:167    from 23 To 2
        SetMemory(0x662310, Add, -21),# units:Human AI Idle  index:168    from 23 To 2
        SetMemory(0x662310, Add, -5376),# units:Human AI Idle  index:169    from 23 To 2
        SetMemory(0x662310, Add, -1376256),# units:Human AI Idle  index:170    from 23 To 2
        SetMemory(0x662310, Add, -352321536),# units:Human AI Idle  index:171    from 23 To 2
        SetMemory(0x662314, Add, -21),# units:Human AI Idle  index:172    from 23 To 2
        SetMemory(0x662314, Add, -5376),# units:Human AI Idle  index:173    from 23 To 2
        SetMemory(0x6648B8, Add, -1258291200),# units:Return to Idle  index:35    from 77 To 2
        SetMemory(0x6648E0, Add, -15872),# units:Return to Idle  index:73    from 64 To 2
        SetMemory(0x6648EC, Add, -16128),# units:Return to Idle  index:85    from 65 To 2
        SetMemory(0x6648F0, Add, -41984),# units:Return to Idle  index:89    from 166 To 2
        SetMemory(0x6648F0, Add, -10747904),# units:Return to Idle  index:90    from 166 To 2
        SetMemory(0x6648F0, Add, -352321536),# units:Return to Idle  index:91    from 23 To 2
        SetMemory(0x6648F4, Add, -21),# units:Return to Idle  index:92    from 23 To 2
        SetMemory(0x6648F4, Add, -41984),# units:Return to Idle  index:93    from 166 To 2
        SetMemory(0x6648F4, Add, -10747904),# units:Return to Idle  index:94    from 166 To 2
        SetMemory(0x6648F4, Add, -2751463424),# units:Return to Idle  index:95    from 166 To 2
        SetMemory(0x6648F8, Add, -164),# units:Return to Idle  index:96    from 166 To 2
        SetMemory(0x664900, Add, -1376256),# units:Return to Idle  index:106    from 23 To 2
        SetMemory(0x664900, Add, -352321536),# units:Return to Idle  index:107    from 23 To 2
        SetMemory(0x664904, Add, -122),# units:Return to Idle  index:108    from 124 To 2
        SetMemory(0x664904, Add, -5376),# units:Return to Idle  index:109    from 23 To 2
        SetMemory(0x664904, Add, -1376256),# units:Return to Idle  index:110    from 23 To 2
        SetMemory(0x664904, Add, -352321536),# units:Return to Idle  index:111    from 23 To 2
        SetMemory(0x664908, Add, -5376),# units:Return to Idle  index:113    from 23 To 2
        SetMemory(0x664908, Add, -1376256),# units:Return to Idle  index:114    from 23 To 2
        SetMemory(0x664908, Add, -352321536),# units:Return to Idle  index:115    from 23 To 2
        SetMemory(0x66490C, Add, -21),# units:Return to Idle  index:116    from 23 To 2
        SetMemory(0x66490C, Add, -5376),# units:Return to Idle  index:117    from 23 To 2
        SetMemory(0x66490C, Add, -1376256),# units:Return to Idle  index:118    from 23 To 2
        SetMemory(0x66490C, Add, -352321536),# units:Return to Idle  index:119    from 23 To 2
        SetMemory(0x664910, Add, -21),# units:Return to Idle  index:120    from 23 To 2
        SetMemory(0x664910, Add, -5376),# units:Return to Idle  index:121    from 23 To 2
        SetMemory(0x664910, Add, -1376256),# units:Return to Idle  index:122    from 23 To 2
        SetMemory(0x664910, Add, -352321536),# units:Return to Idle  index:123    from 23 To 2
        SetMemory(0x664914, Add, -16),# units:Return to Idle  index:124    from 18 To 2
        SetMemory(0x664914, Add, -5376),# units:Return to Idle  index:125    from 23 To 2
        SetMemory(0x664914, Add, -1376256),# units:Return to Idle  index:126    from 23 To 2
        SetMemory(0x664914, Add, -352321536),# units:Return to Idle  index:127    from 23 To 2
        SetMemory(0x664918, Add, -95),# units:Return to Idle  index:128    from 97 To 2
        SetMemory(0x664918, Add, -24320),# units:Return to Idle  index:129    from 97 To 2
        SetMemory(0x664918, Add, -1376256),# units:Return to Idle  index:130    from 23 To 2
        SetMemory(0x664918, Add, -352321536),# units:Return to Idle  index:131    from 23 To 2
        SetMemory(0x66491C, Add, -21),# units:Return to Idle  index:132    from 23 To 2
        SetMemory(0x66491C, Add, -5376),# units:Return to Idle  index:133    from 23 To 2
        SetMemory(0x66491C, Add, -1376256),# units:Return to Idle  index:134    from 23 To 2
        SetMemory(0x66491C, Add, -352321536),# units:Return to Idle  index:135    from 23 To 2
        SetMemory(0x664920, Add, -21),# units:Return to Idle  index:136    from 23 To 2
        SetMemory(0x664920, Add, -5376),# units:Return to Idle  index:137    from 23 To 2
        SetMemory(0x664920, Add, -1376256),# units:Return to Idle  index:138    from 23 To 2
        SetMemory(0x664920, Add, -352321536),# units:Return to Idle  index:139    from 23 To 2
        SetMemory(0x664924, Add, -21),# units:Return to Idle  index:140    from 23 To 2
        SetMemory(0x664924, Add, -5376),# units:Return to Idle  index:141    from 23 To 2
        SetMemory(0x664924, Add, -1376256),# units:Return to Idle  index:142    from 23 To 2
        SetMemory(0x664924, Add, -352321536),# units:Return to Idle  index:143    from 23 To 2
        SetMemory(0x664928, Add, -16),# units:Return to Idle  index:144    from 18 To 2
        SetMemory(0x664928, Add, -5376),# units:Return to Idle  index:145    from 23 To 2
        SetMemory(0x664928, Add, -1048576),# units:Return to Idle  index:146    from 18 To 2
        SetMemory(0x664928, Add, -352321536),# units:Return to Idle  index:147    from 23 To 2
        SetMemory(0x66492C, Add, -21),# units:Return to Idle  index:148    from 23 To 2
        SetMemory(0x66492C, Add, -5376),# units:Return to Idle  index:149    from 23 To 2
        SetMemory(0x66492C, Add, -1376256),# units:Return to Idle  index:150    from 23 To 2
        SetMemory(0x66492C, Add, -352321536),# units:Return to Idle  index:151    from 23 To 2
        SetMemory(0x664930, Add, -21),# units:Return to Idle  index:152    from 23 To 2
        SetMemory(0x664930, Add, -5376),# units:Return to Idle  index:153    from 23 To 2
        SetMemory(0x664930, Add, -1376256),# units:Return to Idle  index:154    from 23 To 2
        SetMemory(0x664930, Add, -352321536),# units:Return to Idle  index:155    from 23 To 2
        SetMemory(0x664934, Add, -21),# units:Return to Idle  index:156    from 23 To 2
        SetMemory(0x664934, Add, -5376),# units:Return to Idle  index:157    from 23 To 2
        SetMemory(0x664934, Add, -1376256),# units:Return to Idle  index:158    from 23 To 2
        SetMemory(0x664934, Add, -352321536),# units:Return to Idle  index:159    from 23 To 2
        SetMemory(0x664938, Add, -21),# units:Return to Idle  index:160    from 23 To 2
        SetMemory(0x664938, Add, -5376),# units:Return to Idle  index:161    from 23 To 2
        SetMemory(0x664938, Add, -1048576),# units:Return to Idle  index:162    from 18 To 2
        SetMemory(0x664938, Add, -352321536),# units:Return to Idle  index:163    from 23 To 2
        SetMemory(0x66493C, Add, -21),# units:Return to Idle  index:164    from 23 To 2
        SetMemory(0x66493C, Add, -5376),# units:Return to Idle  index:165    from 23 To 2
        SetMemory(0x66493C, Add, -1376256),# units:Return to Idle  index:166    from 23 To 2
        SetMemory(0x66493C, Add, -352321536),# units:Return to Idle  index:167    from 23 To 2
        SetMemory(0x664940, Add, -21),# units:Return to Idle  index:168    from 23 To 2
        SetMemory(0x664940, Add, -5376),# units:Return to Idle  index:169    from 23 To 2
        SetMemory(0x664940, Add, -1376256),# units:Return to Idle  index:170    from 23 To 2
        SetMemory(0x664940, Add, -352321536),# units:Return to Idle  index:171    from 23 To 2
        SetMemory(0x664944, Add, -21),# units:Return to Idle  index:172    from 23 To 2
        SetMemory(0x664944, Add, -5376),# units:Return to Idle  index:173    from 23 To 2
        SetMemory(0x663330, Add, -10),# units:Attack Unit  index:16    from 10 To 0
        SetMemory(0x663340, Add, -2801795072),# units:Attack Unit  index:35    from 188 To 21
        SetMemory(0x663344, Add, 19),# units:Attack Unit  index:36    from 2 To 21
        SetMemory(0x663348, Add, 11),# units:Attack Unit  index:40    from 10 To 21
        SetMemory(0x663348, Add, 2816),# units:Attack Unit  index:41    from 10 To 21
        SetMemory(0x663358, Add, 318767104),# units:Attack Unit  index:59    from 2 To 21
        SetMemory(0x663364, Add, 184549376),# units:Attack Unit  index:71    from 10 To 21
        SetMemory(0x663368, Add, -32),# units:Attack Unit  index:72    from 53 To 21
        SetMemory(0x663368, Add, -15872),# units:Attack Unit  index:73    from 64 To 2
        SetMemory(0x663368, Add, 720896),# units:Attack Unit  index:74    from 10 To 21
        SetMemory(0x663368, Add, 184549376),# units:Attack Unit  index:75    from 10 To 21
        SetMemory(0x66336C, Add, 11),# units:Attack Unit  index:76    from 10 To 21
        SetMemory(0x66336C, Add, 2816),# units:Attack Unit  index:77    from 10 To 21
        SetMemory(0x66336C, Add, 720896),# units:Attack Unit  index:78    from 10 To 21
        SetMemory(0x66336C, Add, 184549376),# units:Attack Unit  index:79    from 10 To 21
        SetMemory(0x663374, Add, 11),# units:Attack Unit  index:84    from 10 To 21
        SetMemory(0x663374, Add, -16128),# units:Attack Unit  index:85    from 65 To 2
        SetMemory(0x663374, Add, 720896),# units:Attack Unit  index:86    from 10 To 21
        SetMemory(0x663374, Add, 184549376),# units:Attack Unit  index:87    from 10 To 21
        SetMemory(0x663378, Add, 11),# units:Attack Unit  index:88    from 10 To 21
        SetMemory(0x663378, Add, -42752),# units:Attack Unit  index:89    from 188 To 21
        SetMemory(0x663378, Add, -10944512),# units:Attack Unit  index:90    from 188 To 21
        SetMemory(0x663378, Add, -33554432),# units:Attack Unit  index:91    from 23 To 21
        SetMemory(0x66337C, Add, -2),# units:Attack Unit  index:92    from 23 To 21
        SetMemory(0x66337C, Add, -42752),# units:Attack Unit  index:93    from 188 To 21
        SetMemory(0x66337C, Add, -10944512),# units:Attack Unit  index:94    from 188 To 21
        SetMemory(0x66337C, Add, -2801795072),# units:Attack Unit  index:95    from 188 To 21
        SetMemory(0x663380, Add, -167),# units:Attack Unit  index:96    from 188 To 21
        SetMemory(0x663380, Add, 4864),# units:Attack Unit  index:97    from 2 To 21
        SetMemory(0x663380, Add, 720896),# units:Attack Unit  index:98    from 10 To 21
        SetMemory(0x663380, Add, 184549376),# units:Attack Unit  index:99    from 10 To 21
        SetMemory(0x663384, Add, 11),# units:Attack Unit  index:100    from 10 To 21
        SetMemory(0x663384, Add, 720896),# units:Attack Unit  index:102    from 10 To 21
        SetMemory(0x663384, Add, 167772160),# units:Attack Unit  index:103    from 11 To 21
        SetMemory(0x663388, Add, 11),# units:Attack Unit  index:104    from 10 To 21
        SetMemory(0x663388, Add, -131072),# units:Attack Unit  index:106    from 23 To 21
        SetMemory(0x663388, Add, -33554432),# units:Attack Unit  index:107    from 23 To 21
        SetMemory(0x66338C, Add, -2),# units:Attack Unit  index:108    from 23 To 21
        SetMemory(0x66338C, Add, -512),# units:Attack Unit  index:109    from 23 To 21
        SetMemory(0x66338C, Add, -131072),# units:Attack Unit  index:110    from 23 To 21
        SetMemory(0x66338C, Add, -33554432),# units:Attack Unit  index:111    from 23 To 21
        SetMemory(0x663390, Add, -512),# units:Attack Unit  index:113    from 23 To 21
        SetMemory(0x663390, Add, -131072),# units:Attack Unit  index:114    from 23 To 21
        SetMemory(0x663390, Add, -33554432),# units:Attack Unit  index:115    from 23 To 21
        SetMemory(0x663394, Add, -2),# units:Attack Unit  index:116    from 23 To 21
        SetMemory(0x663394, Add, -512),# units:Attack Unit  index:117    from 23 To 21
        SetMemory(0x663394, Add, -131072),# units:Attack Unit  index:118    from 23 To 21
        SetMemory(0x663394, Add, -33554432),# units:Attack Unit  index:119    from 23 To 21
        SetMemory(0x663398, Add, -2),# units:Attack Unit  index:120    from 23 To 21
        SetMemory(0x663398, Add, -512),# units:Attack Unit  index:121    from 23 To 21
        SetMemory(0x663398, Add, -131072),# units:Attack Unit  index:122    from 23 To 21
        SetMemory(0x663398, Add, -33554432),# units:Attack Unit  index:123    from 23 To 21
        SetMemory(0x66339C, Add, 2),# units:Attack Unit  index:124    from 19 To 21
        SetMemory(0x66339C, Add, -512),# units:Attack Unit  index:125    from 23 To 21
        SetMemory(0x66339C, Add, -131072),# units:Attack Unit  index:126    from 23 To 21
        SetMemory(0x66339C, Add, -33554432),# units:Attack Unit  index:127    from 23 To 21
        SetMemory(0x6633A0, Add, -2),# units:Attack Unit  index:128    from 23 To 21
        SetMemory(0x6633A0, Add, -512),# units:Attack Unit  index:129    from 23 To 21
        SetMemory(0x6633A0, Add, -131072),# units:Attack Unit  index:130    from 23 To 21
        SetMemory(0x6633A0, Add, -33554432),# units:Attack Unit  index:131    from 23 To 21
        SetMemory(0x6633A4, Add, -2),# units:Attack Unit  index:132    from 23 To 21
        SetMemory(0x6633A4, Add, -512),# units:Attack Unit  index:133    from 23 To 21
        SetMemory(0x6633A4, Add, -131072),# units:Attack Unit  index:134    from 23 To 21
        SetMemory(0x6633A4, Add, -33554432),# units:Attack Unit  index:135    from 23 To 21
        SetMemory(0x6633A8, Add, -2),# units:Attack Unit  index:136    from 23 To 21
        SetMemory(0x6633A8, Add, -512),# units:Attack Unit  index:137    from 23 To 21
        SetMemory(0x6633A8, Add, -131072),# units:Attack Unit  index:138    from 23 To 21
        SetMemory(0x6633A8, Add, -33554432),# units:Attack Unit  index:139    from 23 To 21
        SetMemory(0x6633AC, Add, -2),# units:Attack Unit  index:140    from 23 To 21
        SetMemory(0x6633AC, Add, -512),# units:Attack Unit  index:141    from 23 To 21
        SetMemory(0x6633AC, Add, -131072),# units:Attack Unit  index:142    from 23 To 21
        SetMemory(0x6633AC, Add, -33554432),# units:Attack Unit  index:143    from 23 To 21
        SetMemory(0x6633B0, Add, 2),# units:Attack Unit  index:144    from 19 To 21
        SetMemory(0x6633B0, Add, -512),# units:Attack Unit  index:145    from 23 To 21
        SetMemory(0x6633B0, Add, 131072),# units:Attack Unit  index:146    from 19 To 21
        SetMemory(0x6633B0, Add, -33554432),# units:Attack Unit  index:147    from 23 To 21
        SetMemory(0x6633B4, Add, -2),# units:Attack Unit  index:148    from 23 To 21
        SetMemory(0x6633B4, Add, -512),# units:Attack Unit  index:149    from 23 To 21
        SetMemory(0x6633B4, Add, -131072),# units:Attack Unit  index:150    from 23 To 21
        SetMemory(0x6633B4, Add, -33554432),# units:Attack Unit  index:151    from 23 To 21
        SetMemory(0x6633B8, Add, -2),# units:Attack Unit  index:152    from 23 To 21
        SetMemory(0x6633B8, Add, -512),# units:Attack Unit  index:153    from 23 To 21
        SetMemory(0x6633B8, Add, -131072),# units:Attack Unit  index:154    from 23 To 21
        SetMemory(0x6633B8, Add, -33554432),# units:Attack Unit  index:155    from 23 To 21
        SetMemory(0x6633BC, Add, -2),# units:Attack Unit  index:156    from 23 To 21
        SetMemory(0x6633BC, Add, -512),# units:Attack Unit  index:157    from 23 To 21
        SetMemory(0x6633BC, Add, -131072),# units:Attack Unit  index:158    from 23 To 21
        SetMemory(0x6633BC, Add, -33554432),# units:Attack Unit  index:159    from 23 To 21
        SetMemory(0x6633C0, Add, -2),# units:Attack Unit  index:160    from 23 To 21
        SetMemory(0x6633C0, Add, -5376),# units:Attack Unit  index:161    from 23 To 2
        SetMemory(0x6633C0, Add, -1114112),# units:Attack Unit  index:162    from 19 To 2
        SetMemory(0x6633C0, Add, -33554432),# units:Attack Unit  index:163    from 23 To 21
        SetMemory(0x6633C4, Add, -2),# units:Attack Unit  index:164    from 23 To 21
        SetMemory(0x6633C4, Add, -512),# units:Attack Unit  index:165    from 23 To 21
        SetMemory(0x6633C4, Add, -131072),# units:Attack Unit  index:166    from 23 To 21
        SetMemory(0x6633C4, Add, -33554432),# units:Attack Unit  index:167    from 23 To 21
        SetMemory(0x6633C8, Add, -2),# units:Attack Unit  index:168    from 23 To 21
        SetMemory(0x6633C8, Add, -512),# units:Attack Unit  index:169    from 23 To 21
        SetMemory(0x6633C8, Add, -131072),# units:Attack Unit  index:170    from 23 To 21
        SetMemory(0x6633C8, Add, -33554432),# units:Attack Unit  index:171    from 23 To 21
        SetMemory(0x6633CC, Add, -2),# units:Attack Unit  index:172    from 23 To 21
        SetMemory(0x6633CC, Add, -512),# units:Attack Unit  index:173    from 23 To 21
        SetMemory(0x663A70, Add, -3120562176),# units:Attack Move  index:35    from 188 To 2
        SetMemory(0x663A98, Add, -47616),# units:Attack Move  index:73    from 188 To 2
        SetMemory(0x663AA4, Add, -47616),# units:Attack Move  index:85    from 188 To 2
        SetMemory(0x663AA8, Add, -47616),# units:Attack Move  index:89    from 188 To 2
        SetMemory(0x663AA8, Add, -12189696),# units:Attack Move  index:90    from 188 To 2
        SetMemory(0x663AA8, Add, -352321536),# units:Attack Move  index:91    from 23 To 2
        SetMemory(0x663AAC, Add, -21),# units:Attack Move  index:92    from 23 To 2
        SetMemory(0x663AAC, Add, -47616),# units:Attack Move  index:93    from 188 To 2
        SetMemory(0x663AAC, Add, -12189696),# units:Attack Move  index:94    from 188 To 2
        SetMemory(0x663AAC, Add, -3120562176),# units:Attack Move  index:95    from 188 To 2
        SetMemory(0x663AB0, Add, -186),# units:Attack Move  index:96    from 188 To 2
        SetMemory(0x663AB8, Add, -1376256),# units:Attack Move  index:106    from 23 To 2
        SetMemory(0x663AB8, Add, -352321536),# units:Attack Move  index:107    from 23 To 2
        SetMemory(0x663ABC, Add, -21),# units:Attack Move  index:108    from 23 To 2
        SetMemory(0x663ABC, Add, -5376),# units:Attack Move  index:109    from 23 To 2
        SetMemory(0x663ABC, Add, -1376256),# units:Attack Move  index:110    from 23 To 2
        SetMemory(0x663ABC, Add, -352321536),# units:Attack Move  index:111    from 23 To 2
        SetMemory(0x663AC0, Add, -5376),# units:Attack Move  index:113    from 23 To 2
        SetMemory(0x663AC0, Add, -1376256),# units:Attack Move  index:114    from 23 To 2
        SetMemory(0x663AC0, Add, -352321536),# units:Attack Move  index:115    from 23 To 2
        SetMemory(0x663AC4, Add, -21),# units:Attack Move  index:116    from 23 To 2
        SetMemory(0x663AC4, Add, -5376),# units:Attack Move  index:117    from 23 To 2
        SetMemory(0x663AC4, Add, -1376256),# units:Attack Move  index:118    from 23 To 2
        SetMemory(0x663AC4, Add, -352321536),# units:Attack Move  index:119    from 23 To 2
        SetMemory(0x663AC8, Add, -21),# units:Attack Move  index:120    from 23 To 2
        SetMemory(0x663AC8, Add, -5376),# units:Attack Move  index:121    from 23 To 2
        SetMemory(0x663AC8, Add, -1376256),# units:Attack Move  index:122    from 23 To 2
        SetMemory(0x663AC8, Add, -352321536),# units:Attack Move  index:123    from 23 To 2
        SetMemory(0x663ACC, Add, -21),# units:Attack Move  index:124    from 23 To 2
        SetMemory(0x663ACC, Add, -5376),# units:Attack Move  index:125    from 23 To 2
        SetMemory(0x663ACC, Add, -1376256),# units:Attack Move  index:126    from 23 To 2
        SetMemory(0x663ACC, Add, -352321536),# units:Attack Move  index:127    from 23 To 2
        SetMemory(0x663AD0, Add, -21),# units:Attack Move  index:128    from 23 To 2
        SetMemory(0x663AD0, Add, -5376),# units:Attack Move  index:129    from 23 To 2
        SetMemory(0x663AD0, Add, -1376256),# units:Attack Move  index:130    from 23 To 2
        SetMemory(0x663AD0, Add, -352321536),# units:Attack Move  index:131    from 23 To 2
        SetMemory(0x663AD4, Add, -21),# units:Attack Move  index:132    from 23 To 2
        SetMemory(0x663AD4, Add, -5376),# units:Attack Move  index:133    from 23 To 2
        SetMemory(0x663AD4, Add, -1376256),# units:Attack Move  index:134    from 23 To 2
        SetMemory(0x663AD4, Add, -352321536),# units:Attack Move  index:135    from 23 To 2
        SetMemory(0x663AD8, Add, -21),# units:Attack Move  index:136    from 23 To 2
        SetMemory(0x663AD8, Add, -5376),# units:Attack Move  index:137    from 23 To 2
        SetMemory(0x663AD8, Add, -1376256),# units:Attack Move  index:138    from 23 To 2
        SetMemory(0x663AD8, Add, -352321536),# units:Attack Move  index:139    from 23 To 2
        SetMemory(0x663ADC, Add, -21),# units:Attack Move  index:140    from 23 To 2
        SetMemory(0x663ADC, Add, -5376),# units:Attack Move  index:141    from 23 To 2
        SetMemory(0x663ADC, Add, -1376256),# units:Attack Move  index:142    from 23 To 2
        SetMemory(0x663ADC, Add, -352321536),# units:Attack Move  index:143    from 23 To 2
        SetMemory(0x663AE0, Add, -21),# units:Attack Move  index:144    from 23 To 2
        SetMemory(0x663AE0, Add, -5376),# units:Attack Move  index:145    from 23 To 2
        SetMemory(0x663AE0, Add, -1376256),# units:Attack Move  index:146    from 23 To 2
        SetMemory(0x663AE0, Add, -352321536),# units:Attack Move  index:147    from 23 To 2
        SetMemory(0x663AE4, Add, -21),# units:Attack Move  index:148    from 23 To 2
        SetMemory(0x663AE4, Add, -5376),# units:Attack Move  index:149    from 23 To 2
        SetMemory(0x663AE4, Add, -1376256),# units:Attack Move  index:150    from 23 To 2
        SetMemory(0x663AE4, Add, -352321536),# units:Attack Move  index:151    from 23 To 2
        SetMemory(0x663AE8, Add, -21),# units:Attack Move  index:152    from 23 To 2
        SetMemory(0x663AE8, Add, -5376),# units:Attack Move  index:153    from 23 To 2
        SetMemory(0x663AE8, Add, -1376256),# units:Attack Move  index:154    from 23 To 2
        SetMemory(0x663AE8, Add, -352321536),# units:Attack Move  index:155    from 23 To 2
        SetMemory(0x663AEC, Add, -21),# units:Attack Move  index:156    from 23 To 2
        SetMemory(0x663AEC, Add, -5376),# units:Attack Move  index:157    from 23 To 2
        SetMemory(0x663AEC, Add, -352321536),# units:Attack Move  index:159    from 23 To 2
        SetMemory(0x663AF0, Add, -21),# units:Attack Move  index:160    from 23 To 2
        SetMemory(0x663AF0, Add, -5376),# units:Attack Move  index:161    from 23 To 2
        SetMemory(0x663AF0, Add, -1376256),# units:Attack Move  index:162    from 23 To 2
        SetMemory(0x663AF0, Add, -352321536),# units:Attack Move  index:163    from 23 To 2
        SetMemory(0x663AF4, Add, -21),# units:Attack Move  index:164    from 23 To 2
        SetMemory(0x663AF4, Add, -5376),# units:Attack Move  index:165    from 23 To 2
        SetMemory(0x663AF4, Add, -1376256),# units:Attack Move  index:166    from 23 To 2
        SetMemory(0x663AF4, Add, -352321536),# units:Attack Move  index:167    from 23 To 2
        SetMemory(0x663AF8, Add, -21),# units:Attack Move  index:168    from 23 To 2
        SetMemory(0x663AF8, Add, -5376),# units:Attack Move  index:169    from 23 To 2
        SetMemory(0x663AF8, Add, -1376256),# units:Attack Move  index:170    from 23 To 2
        SetMemory(0x663AF8, Add, -352321536),# units:Attack Move  index:171    from 23 To 2
        SetMemory(0x663AFC, Add, -21),# units:Attack Move  index:172    from 23 To 2
        SetMemory(0x663AFC, Add, -5376),# units:Attack Move  index:173    from 23 To 2
        SetMemory(0x6636C8, Add, 127),# units:Ground Weapon  index:16    from 3 To 130
        SetMemory(0x6616F0, Add, 127),# units:Air Weapon  index:16    from 3 To 130
        SetMemory(0x6601A0, Add, 3),# units:AI Internal  index:40    from 0 To 3
        SetMemory(0x6601C0, Add, 3),# units:AI Internal  index:72    from 0 To 3
        SetMemory(0x6601DC, Add, 50331648),# units:AI Internal  index:103    from 0 To 3
        SetMemory(0x6640A0, Add, -4),# units:Special Ability Flags  index:8    from 1512047108 To 1512047104
        SetMemory(0x6640A4, Add, -4),# units:Special Ability Flags  index:9    from 1512079620 To 1512079616
        SetMemory(0x6640AC, Add, -4),# units:Special Ability Flags  index:11    from 1509949444 To 1509949440
        SetMemory(0x6640B0, Add, -4),# units:Special Ability Flags  index:12    from 1545601028 To 1545601024
        SetMemory(0x6640C0, Add, -2097664),# units:Special Ability Flags  index:16    from 404816448 To 402718784
        SetMemory(0x6640D4, Add, -4),# units:Special Ability Flags  index:21    from 1512047172 To 1512047168
        SetMemory(0x6640D8, Add, -4),# units:Special Ability Flags  index:22    from 1512079684 To 1512079680
        SetMemory(0x6640EC, Add, -4),# units:Special Ability Flags  index:27    from 1545601092 To 1545601088
        SetMemory(0x6640F0, Add, -4),# units:Special Ability Flags  index:28    from 1545601092 To 1545601088
        SetMemory(0x6640F4, Add, -4),# units:Special Ability Flags  index:29    from 1545601092 To 1545601088
        SetMemory(0x66410C, Add, 33488832),# units:Special Ability Flags  index:35    from 402718848 To 436207680
        SetMemory(0x664128, Add, -4),# units:Special Ability Flags  index:42    from 436306052 To 436306048
        SetMemory(0x66413C, Add, -4),# units:Special Ability Flags  index:47    from 402719876 To 402719872
        SetMemory(0x664174, Add, -4194304),# units:Special Ability Flags  index:61    from 406913024 To 402718720
        SetMemory(0x66417C, Add, -2097152),# units:Special Ability Flags  index:63    from 471859456 To 469762304
        SetMemory(0x66419C, Add, -2097152),# units:Special Ability Flags  index:71    from 1512046596 To 1509949444
        SetMemory(0x6641A8, Add, 700448768),# units:Special Ability Flags  index:74    from 406913024 To 1107361792
        SetMemory(0x6641AC, Add, 700383168),# units:Special Ability Flags  index:75    from 406913088 To 1107296256
        SetMemory(0x6641D0, Add, -373342212),# units:Special Ability Flags  index:84    from 1480638468 To 1107296256
        SetMemory(0x6641D8, Add, -4),# units:Special Ability Flags  index:86    from 1512046660 To 1512046656
        SetMemory(0x66421C, Add, 703528832),# units:Special Ability Flags  index:103    from 403767424 To 1107296256
        SetMemory(0x664228, Add, -2147487777),# units:Special Ability Flags  index:106    from 3288338465 To 1140850688
        SetMemory(0x66422C, Add, -2097155),# units:Special Ability Flags  index:107    from 1142947843 To 1140850688
        SetMemory(0x664230, Add, -3),# units:Special Ability Flags  index:108    from 1140850691 To 1140850688
        SetMemory(0x664234, Add, -1),# units:Special Ability Flags  index:109    from 1140850689 To 1140850688
        SetMemory(0x664238, Add, -8193),# units:Special Ability Flags  index:110    from 1140858881 To 1140850688
        SetMemory(0x66423C, Add, -2147483681),# units:Special Ability Flags  index:111    from 3288334369 To 1140850688
        SetMemory(0x664244, Add, -2147483681),# units:Special Ability Flags  index:113    from 3288334369 To 1140850688
        SetMemory(0x664248, Add, -33),# units:Special Ability Flags  index:114    from 1140850721 To 1140850688
        SetMemory(0x66424C, Add, -3),# units:Special Ability Flags  index:115    from 1140850691 To 1140850688
        SetMemory(0x664250, Add, -33),# units:Special Ability Flags  index:116    from 1140850721 To 1140850688
        SetMemory(0x664254, Add, -3),# units:Special Ability Flags  index:117    from 1140850691 To 1140850688
        SetMemory(0x664258, Add, -3),# units:Special Ability Flags  index:118    from 1140850691 To 1140850688
        SetMemory(0x66425C, Add, 1107296255),# units:Special Ability Flags  index:119    from 67108865 To 1174405120
        SetMemory(0x664260, Add, -3),# units:Special Ability Flags  index:120    from 1140850691 To 1140850688
        SetMemory(0x664264, Add, -3),# units:Special Ability Flags  index:121    from 1140850691 To 1140850688
        SetMemory(0x664268, Add, -33),# units:Special Ability Flags  index:122    from 1140850721 To 1140850688
        SetMemory(0x66426C, Add, -1),# units:Special Ability Flags  index:123    from 1140850689 To 1140850688
        SetMemory(0x664270, Add, -33025),# units:Special Ability Flags  index:124    from 1409319169 To 1409286144
        SetMemory(0x664274, Add, -2147483649),# units:Special Ability Flags  index:125    from 3288334337 To 1140850688
        SetMemory(0x664278, Add, -1),# units:Special Ability Flags  index:126    from 1140850689 To 1140850688
        SetMemory(0x66427C, Add, -1),# units:Special Ability Flags  index:127    from 1140850689 To 1140850688
        SetMemory(0x664280, Add, -2048),# units:Special Ability Flags  index:128    from 536872960 To 536870912
        SetMemory(0x664284, Add, -2048),# units:Special Ability Flags  index:129    from 536872960 To 536870912
        SetMemory(0x664288, Add, -161),# units:Special Ability Flags  index:130    from 67174561 To 67174400
        SetMemory(0x66428C, Add, -2164265089),# units:Special Ability Flags  index:131    from 2231439489 To 67174400
        SetMemory(0x664290, Add, -2164265089),# units:Special Ability Flags  index:132    from 2231439489 To 67174400
        SetMemory(0x664294, Add, -2164265089),# units:Special Ability Flags  index:133    from 2231439489 To 67174400
        SetMemory(0x664298, Add, -16908417),# units:Special Ability Flags  index:134    from 84082817 To 67174400
        SetMemory(0x66429C, Add, -16908417),# units:Special Ability Flags  index:135    from 84082817 To 67174400
        SetMemory(0x6642A0, Add, -16908417),# units:Special Ability Flags  index:136    from 84082817 To 67174400
        SetMemory(0x6642A4, Add, -16908417),# units:Special Ability Flags  index:137    from 84082817 To 67174400
        SetMemory(0x6642A8, Add, -16908417),# units:Special Ability Flags  index:138    from 84082817 To 67174400
        SetMemory(0x6642AC, Add, -16908417),# units:Special Ability Flags  index:139    from 84082817 To 67174400
        SetMemory(0x6642B0, Add, -16908417),# units:Special Ability Flags  index:140    from 84082817 To 67174400
        SetMemory(0x6642B4, Add, -16908417),# units:Special Ability Flags  index:141    from 84082817 To 67174400
        SetMemory(0x6642B8, Add, -16908417),# units:Special Ability Flags  index:142    from 84082817 To 67174400
        SetMemory(0x6642BC, Add, -16908417),# units:Special Ability Flags  index:143    from 84082817 To 67174400
        SetMemory(0x6642C0, Add, 1056735103),# units:Special Ability Flags  index:144    from 352551041 To 1409286144
        SetMemory(0x6642C4, Add, 1023401855),# units:Special Ability Flags  index:145    from 83894401 To 1107296256
        SetMemory(0x6642C8, Add, -16973953),# units:Special Ability Flags  index:146    from 352518273 To 335544320
        SetMemory(0x6642CC, Add, -16941185),# units:Special Ability Flags  index:147    from 84115585 To 67174400
        SetMemory(0x6642D0, Add, -16941185),# units:Special Ability Flags  index:148    from 84115585 To 67174400
        SetMemory(0x6642D4, Add, -16785537),# units:Special Ability Flags  index:149    from 83959937 To 67174400
        SetMemory(0x6642D8, Add, -16908417),# units:Special Ability Flags  index:150    from 84082817 To 67174400
        SetMemory(0x6642DC, Add, -16941185),# units:Special Ability Flags  index:151    from 84115585 To 67174400
        SetMemory(0x6642E0, Add, -16941185),# units:Special Ability Flags  index:152    from 84115585 To 67174400
        SetMemory(0x6642E4, Add, 1056964479),# units:Special Ability Flags  index:153    from 83886209 To 1140850688
        SetMemory(0x6642E8, Add, -2147487745),# units:Special Ability Flags  index:154    from 3288338433 To 1140850688
        SetMemory(0x6642EC, Add, -2148007937),# units:Special Ability Flags  index:155    from 3288858625 To 1140850688
        SetMemory(0x6642F0, Add, -1),# units:Special Ability Flags  index:156    from 1140850689 To 1140850688
        SetMemory(0x6642F4, Add, -8193),# units:Special Ability Flags  index:157    from 1140858881 To 1140850688
        SetMemory(0x6642F8, Add, -524289),# units:Special Ability Flags  index:158    from 1141374977 To 1140850688
        SetMemory(0x6642FC, Add, -524289),# units:Special Ability Flags  index:159    from 1141374977 To 1140850688
        SetMemory(0x664300, Add, -2148007937),# units:Special Ability Flags  index:160    from 3288858625 To 1140850688
        SetMemory(0x664304, Add, -524289),# units:Special Ability Flags  index:161    from 1141374977 To 1140850688
        SetMemory(0x664308, Add, -34111489),# units:Special Ability Flags  index:162    from 1409843201 To 1375731712
        SetMemory(0x66430C, Add, -524289),# units:Special Ability Flags  index:163    from 1141374977 To 1140850688
        SetMemory(0x664310, Add, -524289),# units:Special Ability Flags  index:164    from 1141374977 To 1140850688
        SetMemory(0x664314, Add, -524289),# units:Special Ability Flags  index:165    from 1141374977 To 1140850688
        SetMemory(0x664318, Add, -524289),# units:Special Ability Flags  index:166    from 1141374977 To 1140850688
        SetMemory(0x66431C, Add, -524289),# units:Special Ability Flags  index:167    from 1141374977 To 1140850688
        SetMemory(0x664320, Add, -1),# units:Special Ability Flags  index:168    from 1140850689 To 1140850688
        SetMemory(0x664324, Add, -524289),# units:Special Ability Flags  index:169    from 1141374977 To 1140850688
        SetMemory(0x664328, Add, -524289),# units:Special Ability Flags  index:170    from 1141374977 To 1140850688
        SetMemory(0x66432C, Add, -524289),# units:Special Ability Flags  index:171    from 1141374977 To 1140850688
        SetMemory(0x664330, Add, -524289),# units:Special Ability Flags  index:172    from 1143472129 To 1142947840
        SetMemory(0x664334, Add, -33554433),# units:Special Ability Flags  index:173    from 603979777 To 570425344
        SetMemory(0x663248, Add, -9),# units:Sight Range  index:16    from 11 To 2
        SetMemory(0x65FED8, Add, -3),# units:Armor  index:16    from 3 To 0
        SetMemory(0x6620B8, Add, 33554432),# units:Right-click Action  index:35    from 0 To 2
        SetMemory(0x6620BC, Add, 2),# units:Right-click Action  index:36    from 0 To 2
        SetMemory(0x6620DC, Add, 16777216),# units:Right-click Action  index:71    from 1 To 2
        SetMemory(0x6620E0, Add, 1),# units:Right-click Action  index:72    from 1 To 2
        SetMemory(0x6620E0, Add, 1536),# units:Right-click Action  index:73    from 0 To 6
        SetMemory(0x6620E0, Add, 65536),# units:Right-click Action  index:74    from 1 To 2
        SetMemory(0x6620E0, Add, 16777216),# units:Right-click Action  index:75    from 1 To 2
        SetMemory(0x6620EC, Add, 1536),# units:Right-click Action  index:85    from 0 To 6
        SetMemory(0x6620EC, Add, 65536),# units:Right-click Action  index:86    from 1 To 2
        SetMemory(0x6620EC, Add, 16777216),# units:Right-click Action  index:87    from 1 To 2
        SetMemory(0x6620F0, Add, 1),# units:Right-click Action  index:88    from 1 To 2
        SetMemory(0x6620F0, Add, 33554432),# units:Right-click Action  index:91    from 0 To 2
        SetMemory(0x6620F4, Add, 2),# units:Right-click Action  index:92    from 0 To 2
        SetMemory(0x6620F8, Add, 512),# units:Right-click Action  index:97    from 0 To 2
        SetMemory(0x6620F8, Add, 65536),# units:Right-click Action  index:98    from 1 To 2
        SetMemory(0x6620F8, Add, 16777216),# units:Right-click Action  index:99    from 1 To 2
        SetMemory(0x6620FC, Add, 1),# units:Right-click Action  index:100    from 1 To 2
        SetMemory(0x6620FC, Add, 65536),# units:Right-click Action  index:102    from 1 To 2
        SetMemory(0x662100, Add, 1),# units:Right-click Action  index:104    from 1 To 2
        SetMemory(0x662100, Add, -67108864),# units:Right-click Action  index:107    from 6 To 2
        SetMemory(0x662104, Add, 2),# units:Right-click Action  index:108    from 0 To 2
        SetMemory(0x662104, Add, 512),# units:Right-click Action  index:109    from 0 To 2
        SetMemory(0x662104, Add, 131072),# units:Right-click Action  index:110    from 0 To 2
        SetMemory(0x662108, Add, 33554432),# units:Right-click Action  index:115    from 0 To 2
        SetMemory(0x66210C, Add, 512),# units:Right-click Action  index:117    from 0 To 2
        SetMemory(0x66210C, Add, 131072),# units:Right-click Action  index:118    from 0 To 2
        SetMemory(0x66210C, Add, 33554432),# units:Right-click Action  index:119    from 0 To 2
        SetMemory(0x662110, Add, 2),# units:Right-click Action  index:120    from 0 To 2
        SetMemory(0x662110, Add, 512),# units:Right-click Action  index:121    from 0 To 2
        SetMemory(0x662110, Add, 33554432),# units:Right-click Action  index:123    from 0 To 2
        SetMemory(0x662114, Add, -1),# units:Right-click Action  index:124    from 3 To 2
        SetMemory(0x662114, Add, 512),# units:Right-click Action  index:125    from 0 To 2
        SetMemory(0x662114, Add, 131072),# units:Right-click Action  index:126    from 0 To 2
        SetMemory(0x662114, Add, 33554432),# units:Right-click Action  index:127    from 0 To 2
        SetMemory(0x662118, Add, 2),# units:Right-click Action  index:128    from 0 To 2
        SetMemory(0x662118, Add, 512),# units:Right-click Action  index:129    from 0 To 2
        SetMemory(0x662118, Add, 33554432),# units:Right-click Action  index:131    from 0 To 2
        SetMemory(0x66211C, Add, 2),# units:Right-click Action  index:132    from 0 To 2
        SetMemory(0x66211C, Add, 512),# units:Right-click Action  index:133    from 0 To 2
        SetMemory(0x66211C, Add, 131072),# units:Right-click Action  index:134    from 0 To 2
        SetMemory(0x66211C, Add, 33554432),# units:Right-click Action  index:135    from 0 To 2
        SetMemory(0x662120, Add, 2),# units:Right-click Action  index:136    from 0 To 2
        SetMemory(0x662120, Add, 512),# units:Right-click Action  index:137    from 0 To 2
        SetMemory(0x662120, Add, 131072),# units:Right-click Action  index:138    from 0 To 2
        SetMemory(0x662120, Add, 33554432),# units:Right-click Action  index:139    from 0 To 2
        SetMemory(0x662124, Add, 2),# units:Right-click Action  index:140    from 0 To 2
        SetMemory(0x662124, Add, 512),# units:Right-click Action  index:141    from 0 To 2
        SetMemory(0x662124, Add, 131072),# units:Right-click Action  index:142    from 0 To 2
        SetMemory(0x662124, Add, 33554432),# units:Right-click Action  index:143    from 0 To 2
        SetMemory(0x662128, Add, -1),# units:Right-click Action  index:144    from 3 To 2
        SetMemory(0x662128, Add, 512),# units:Right-click Action  index:145    from 0 To 2
        SetMemory(0x662128, Add, -65536),# units:Right-click Action  index:146    from 3 To 2
        SetMemory(0x662128, Add, 33554432),# units:Right-click Action  index:147    from 0 To 2
        SetMemory(0x66212C, Add, 2),# units:Right-click Action  index:148    from 0 To 2
        SetMemory(0x66212C, Add, 512),# units:Right-click Action  index:149    from 0 To 2
        SetMemory(0x66212C, Add, 131072),# units:Right-click Action  index:150    from 0 To 2
        SetMemory(0x66212C, Add, 33554432),# units:Right-click Action  index:151    from 0 To 2
        SetMemory(0x662130, Add, 2),# units:Right-click Action  index:152    from 0 To 2
        SetMemory(0x662130, Add, 512),# units:Right-click Action  index:153    from 0 To 2
        SetMemory(0x662130, Add, 131072),# units:Right-click Action  index:154    from 0 To 2
        SetMemory(0x662130, Add, 33554432),# units:Right-click Action  index:155    from 0 To 2
        SetMemory(0x662134, Add, 2),# units:Right-click Action  index:156    from 0 To 2
        SetMemory(0x662134, Add, 512),# units:Right-click Action  index:157    from 0 To 2
        SetMemory(0x662134, Add, 131072),# units:Right-click Action  index:158    from 0 To 2
        SetMemory(0x662134, Add, 33554432),# units:Right-click Action  index:159    from 0 To 2
        SetMemory(0x662138, Add, 2),# units:Right-click Action  index:160    from 0 To 2
        SetMemory(0x662138, Add, 512),# units:Right-click Action  index:161    from 0 To 2
        SetMemory(0x662138, Add, -65536),# units:Right-click Action  index:162    from 3 To 2
        SetMemory(0x662138, Add, 33554432),# units:Right-click Action  index:163    from 0 To 2
        SetMemory(0x66213C, Add, 2),# units:Right-click Action  index:164    from 0 To 2
        SetMemory(0x66213C, Add, 512),# units:Right-click Action  index:165    from 0 To 2
        SetMemory(0x66213C, Add, 131072),# units:Right-click Action  index:166    from 0 To 2
        SetMemory(0x66213C, Add, 33554432),# units:Right-click Action  index:167    from 0 To 2
        SetMemory(0x662140, Add, 2),# units:Right-click Action  index:168    from 0 To 2
        SetMemory(0x662140, Add, 512),# units:Right-click Action  index:169    from 0 To 2
        SetMemory(0x662140, Add, 131072),# units:Right-click Action  index:170    from 0 To 2
        SetMemory(0x662140, Add, 33554432),# units:Right-click Action  index:171    from 0 To 2
        SetMemory(0x662144, Add, 2),# units:Right-click Action  index:172    from 0 To 2
        SetMemory(0x662144, Add, 512),# units:Right-click Action  index:173    from 0 To 2
        SetMemory(0x65FFD0, Add, -462),# units:What Sound Start  index:16    from 462 To 0
        SetMemory(0x662C10, Add, -465),# units:What Sound End  index:16    from 465 To 0
        SetMemory(0x663B58, Add, -457),# units:Piss Sound Start  index:16    from 457 To 0
        SetMemory(0x661F08, Add, -461),# units:Piss Sound End  index:16    from 461 To 0
        SetMemory(0x663C30, Add, -466),# units:Yes Sound Start  index:16    from 466 To 0
        SetMemory(0x661460, Add, -469),# units:Yes Sound End  index:16    from 469 To 0
        SetMemory(0x662860, Add, 4),# units:StarEdit Placement Box Width  index:0    from 17 To 21
        SetMemory(0x662868, Add, -11),# units:StarEdit Placement Box Width  index:2    from 32 To 21
        SetMemory(0x66286C, Add, -11),# units:StarEdit Placement Box Width  index:3    from 32 To 21
        SetMemory(0x662870, Add, 29),# units:StarEdit Placement Box Width  index:4    from 3 To 32
        SetMemory(0x662878, Add, 29),# units:StarEdit Placement Box Width  index:6    from 3 To 32
        SetMemory(0x662880, Add, -6),# units:StarEdit Placement Box Width  index:8    from 38 To 32
        SetMemory(0x662884, Add, -33),# units:StarEdit Placement Box Width  index:9    from 65 To 32
        SetMemory(0x662888, Add, 9),# units:StarEdit Placement Box Width  index:10    from 23 To 32
        SetMemory(0x66288C, Add, -17),# units:StarEdit Placement Box Width  index:11    from 49 To 32
        SetMemory(0x662890, Add, -48),# units:StarEdit Placement Box Width  index:12    from 80 To 32
        SetMemory(0x6628A8, Add, 29),# units:StarEdit Placement Box Width  index:18    from 3 To 32
        SetMemory(0x6628B0, Add, 14),# units:StarEdit Placement Box Width  index:20    from 18 To 32
        SetMemory(0x6628B4, Add, -6),# units:StarEdit Placement Box Width  index:21    from 38 To 32
        SetMemory(0x6628B8, Add, -33),# units:StarEdit Placement Box Width  index:22    from 65 To 32
        SetMemory(0x6628C0, Add, 29),# units:StarEdit Placement Box Width  index:24    from 3 To 32
        SetMemory(0x6628C8, Add, 29),# units:StarEdit Placement Box Width  index:26    from 3 To 32
        SetMemory(0x6628CC, Add, -43),# units:StarEdit Placement Box Width  index:27    from 75 To 32
        SetMemory(0x6628D0, Add, -43),# units:StarEdit Placement Box Width  index:28    from 75 To 32
        SetMemory(0x6628D4, Add, -43),# units:StarEdit Placement Box Width  index:29    from 75 To 32
        SetMemory(0x6628DC, Add, 29),# units:StarEdit Placement Box Width  index:31    from 3 To 32
        SetMemory(0x6628E0, Add, 9),# units:StarEdit Placement Box Width  index:32    from 23 To 32
        SetMemory(0x6628E8, Add, 15),# units:StarEdit Placement Box Width  index:34    from 17 To 32
        SetMemory(0x6628EC, Add, 16),# units:StarEdit Placement Box Width  index:35    from 16 To 32
        SetMemory(0x6628F4, Add, 16),# units:StarEdit Placement Box Width  index:37    from 16 To 32
        SetMemory(0x6628F8, Add, 11),# units:StarEdit Placement Box Width  index:38    from 21 To 32
        SetMemory(0x6628FC, Add, -6),# units:StarEdit Placement Box Width  index:39    from 38 To 32
        SetMemory(0x662900, Add, 13),# units:StarEdit Placement Box Width  index:40    from 19 To 32
        SetMemory(0x662904, Add, 9),# units:StarEdit Placement Box Width  index:41    from 23 To 32
        SetMemory(0x662908, Add, -41),# units:StarEdit Placement Box Width  index:42    from 50 To 9
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
        SetMemory(0x662988, Add, 8),# units:StarEdit Placement Box Width  index:74    from 24 To 32
        SetMemory(0x66298C, Add, 8),# units:StarEdit Placement Box Width  index:75    from 24 To 32
        SetMemory(0x662994, Add, 8),# units:StarEdit Placement Box Width  index:77    from 24 To 32
        SetMemory(0x66299C, Add, 8),# units:StarEdit Placement Box Width  index:79    from 24 To 32
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
        SetMemory(0x662A10, Add, -32),# units:StarEdit Placement Box Width  index:108    from 64 To 32
        SetMemory(0x662A14, Add, -64),# units:StarEdit Placement Box Width  index:109    from 96 To 32
        SetMemory(0x662A18, Add, -96),# units:StarEdit Placement Box Width  index:110    from 128 To 32
        SetMemory(0x662A1C, Add, -96),# units:StarEdit Placement Box Width  index:111    from 128 To 32
        SetMemory(0x662A24, Add, -96),# units:StarEdit Placement Box Width  index:113    from 128 To 32
        SetMemory(0x662A28, Add, -96),# units:StarEdit Placement Box Width  index:114    from 128 To 32
        SetMemory(0x662A2C, Add, -32),# units:StarEdit Placement Box Width  index:115    from 64 To 32
        SetMemory(0x662A30, Add, -96),# units:StarEdit Placement Box Width  index:116    from 128 To 32
        SetMemory(0x662A34, Add, -32),# units:StarEdit Placement Box Width  index:117    from 64 To 32
        SetMemory(0x662A38, Add, -32),# units:StarEdit Placement Box Width  index:118    from 64 To 32
        SetMemory(0x662A3C, Add, -64),# units:StarEdit Placement Box Width  index:119    from 96 To 32
        SetMemory(0x662A40, Add, -32),# units:StarEdit Placement Box Width  index:120    from 64 To 32
        SetMemory(0x662A44, Add, -64),# units:StarEdit Placement Box Width  index:121    from 96 To 32
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
        SetMemory(0x662AA4, Add, -64),# units:StarEdit Placement Box Width  index:145    from 96 To 32
        SetMemory(0x662AA8, Add, -43),# units:StarEdit Placement Box Width  index:146    from 64 To 21
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
        SetMemory(0x662AD8, Add, -96),# units:StarEdit Placement Box Width  index:158    from 128 To 32
        SetMemory(0x662ADC, Add, -64),# units:StarEdit Placement Box Width  index:159    from 96 To 32
        SetMemory(0x662AE0, Add, -96),# units:StarEdit Placement Box Width  index:160    from 128 To 32
        SetMemory(0x662AE4, Add, -64),# units:StarEdit Placement Box Width  index:161    from 96 To 32
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
        SetMemory(0x662860, Add, 65536),# units:StarEdit Placement Box Height  index:0    from 20 To 21
        SetMemory(0x662868, Add, -720896),# units:StarEdit Placement Box Height  index:2    from 32 To 21
        SetMemory(0x66286C, Add, -720896),# units:StarEdit Placement Box Height  index:3    from 32 To 21
        SetMemory(0x662870, Add, 1900544),# units:StarEdit Placement Box Height  index:4    from 3 To 32
        SetMemory(0x662880, Add, 131072),# units:StarEdit Placement Box Height  index:8    from 30 To 32
        SetMemory(0x662884, Add, -1179648),# units:StarEdit Placement Box Height  index:9    from 50 To 32
        SetMemory(0x662888, Add, 262144),# units:StarEdit Placement Box Height  index:10    from 28 To 32
        SetMemory(0x66288C, Add, -327680),# units:StarEdit Placement Box Height  index:11    from 37 To 32
        SetMemory(0x662890, Add, -2097152),# units:StarEdit Placement Box Height  index:12    from 64 To 32
        SetMemory(0x6628A8, Add, 1900544),# units:StarEdit Placement Box Height  index:18    from 3 To 32
        SetMemory(0x6628B0, Add, 655360),# units:StarEdit Placement Box Height  index:20    from 22 To 32
        SetMemory(0x6628B4, Add, 131072),# units:StarEdit Placement Box Height  index:21    from 30 To 32
        SetMemory(0x6628B8, Add, -1179648),# units:StarEdit Placement Box Height  index:22    from 50 To 32
        SetMemory(0x6628C0, Add, 1900544),# units:StarEdit Placement Box Height  index:24    from 3 To 32
        SetMemory(0x6628C8, Add, 1900544),# units:StarEdit Placement Box Height  index:26    from 3 To 32
        SetMemory(0x6628CC, Add, -1769472),# units:StarEdit Placement Box Height  index:27    from 59 To 32
        SetMemory(0x6628D0, Add, -1769472),# units:StarEdit Placement Box Height  index:28    from 59 To 32
        SetMemory(0x6628D4, Add, -1769472),# units:StarEdit Placement Box Height  index:29    from 59 To 32
        SetMemory(0x6628DC, Add, 1900544),# units:StarEdit Placement Box Height  index:31    from 3 To 32
        SetMemory(0x6628E0, Add, 262144),# units:StarEdit Placement Box Height  index:32    from 28 To 32
        SetMemory(0x6628E8, Add, 786432),# units:StarEdit Placement Box Height  index:34    from 20 To 32
        SetMemory(0x6628EC, Add, 1048576),# units:StarEdit Placement Box Height  index:35    from 16 To 32
        SetMemory(0x6628F4, Add, 1048576),# units:StarEdit Placement Box Height  index:37    from 16 To 32
        SetMemory(0x6628F8, Add, 589824),# units:StarEdit Placement Box Height  index:38    from 23 To 32
        SetMemory(0x662900, Add, 851968),# units:StarEdit Placement Box Height  index:40    from 19 To 32
        SetMemory(0x662904, Add, 589824),# units:StarEdit Placement Box Height  index:41    from 23 To 32
        SetMemory(0x662908, Add, -2686976),# units:StarEdit Placement Box Height  index:42    from 50 To 9
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
        SetMemory(0x662A10, Add, -2097152),# units:StarEdit Placement Box Height  index:108    from 64 To 32
        SetMemory(0x662A14, Add, -2097152),# units:StarEdit Placement Box Height  index:109    from 64 To 32
        SetMemory(0x662A18, Add, -2097152),# units:StarEdit Placement Box Height  index:110    from 64 To 32
        SetMemory(0x662A1C, Add, -4194304),# units:StarEdit Placement Box Height  index:111    from 96 To 32
        SetMemory(0x662A24, Add, -4194304),# units:StarEdit Placement Box Height  index:113    from 96 To 32
        SetMemory(0x662A28, Add, -4194304),# units:StarEdit Placement Box Height  index:114    from 96 To 32
        SetMemory(0x662A2C, Add, -2097152),# units:StarEdit Placement Box Height  index:115    from 64 To 32
        SetMemory(0x662A30, Add, -4194304),# units:StarEdit Placement Box Height  index:116    from 96 To 32
        SetMemory(0x662A34, Add, -2097152),# units:StarEdit Placement Box Height  index:117    from 64 To 32
        SetMemory(0x662A38, Add, -2097152),# units:StarEdit Placement Box Height  index:118    from 64 To 32
        SetMemory(0x662A3C, Add, -2097152),# units:StarEdit Placement Box Height  index:119    from 64 To 32
        SetMemory(0x662A40, Add, -2097152),# units:StarEdit Placement Box Height  index:120    from 64 To 32
        SetMemory(0x662A44, Add, -4194304),# units:StarEdit Placement Box Height  index:121    from 96 To 32
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
        SetMemory(0x662AA4, Add, -4194304),# units:StarEdit Placement Box Height  index:145    from 96 To 32
        SetMemory(0x662AA8, Add, -2818048),# units:StarEdit Placement Box Height  index:146    from 64 To 21
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
        SetMemory(0x662AD8, Add, -4194304),# units:StarEdit Placement Box Height  index:158    from 96 To 32
        SetMemory(0x662ADC, Add, -2097152),# units:StarEdit Placement Box Height  index:159    from 64 To 32
        SetMemory(0x662AE0, Add, -4194304),# units:StarEdit Placement Box Height  index:160    from 96 To 32
        SetMemory(0x662AE4, Add, -4194304),# units:StarEdit Placement Box Height  index:161    from 96 To 32
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
        SetMemory(0x6617C8, Add, 2),# units:Unit Size Left  index:0    from 8 To 10
        SetMemory(0x6617D8, Add, -6),# units:Unit Size Left  index:2    from 16 To 10
        SetMemory(0x6617E0, Add, -6),# units:Unit Size Left  index:3    from 16 To 10
        SetMemory(0x6617F0, Add, -6),# units:Unit Size Left  index:5    from 16 To 10
        SetMemory(0x661808, Add, -9),# units:Unit Size Left  index:8    from 19 To 10
        SetMemory(0x661810, Add, -22),# units:Unit Size Left  index:9    from 32 To 10
        SetMemory(0x661818, Add, -1),# units:Unit Size Left  index:10    from 11 To 10
        SetMemory(0x661820, Add, -14),# units:Unit Size Left  index:11    from 24 To 10
        SetMemory(0x661828, Add, -27),# units:Unit Size Left  index:12    from 37 To 10
        SetMemory(0x661848, Add, -6),# units:Unit Size Left  index:16    from 7 To 1
        SetMemory(0x661850, Add, -6),# units:Unit Size Left  index:17    from 16 To 10
        SetMemory(0x661868, Add, 2),# units:Unit Size Left  index:20    from 8 To 10
        SetMemory(0x661870, Add, -9),# units:Unit Size Left  index:21    from 19 To 10
        SetMemory(0x661878, Add, -16),# units:Unit Size Left  index:22    from 32 To 16
        SetMemory(0x661880, Add, -6),# units:Unit Size Left  index:23    from 16 To 10
        SetMemory(0x661890, Add, -6),# units:Unit Size Left  index:25    from 16 To 10
        SetMemory(0x6618A0, Add, -27),# units:Unit Size Left  index:27    from 37 To 10
        SetMemory(0x6618A8, Add, -27),# units:Unit Size Left  index:28    from 37 To 10
        SetMemory(0x6618B0, Add, -27),# units:Unit Size Left  index:29    from 37 To 10
        SetMemory(0x6618B8, Add, -6),# units:Unit Size Left  index:30    from 16 To 10
        SetMemory(0x6618C8, Add, -1),# units:Unit Size Left  index:32    from 11 To 10
        SetMemory(0x6618D8, Add, 2),# units:Unit Size Left  index:34    from 8 To 10
        SetMemory(0x6618E0, Add, 2),# units:Unit Size Left  index:35    from 8 To 10
        SetMemory(0x6618E8, Add, -6),# units:Unit Size Left  index:36    from 16 To 10
        SetMemory(0x661910, Add, -1),# units:Unit Size Left  index:41    from 11 To 10
        SetMemory(0x661918, Add, -21),# units:Unit Size Left  index:42    from 25 To 4
        SetMemory(0x661920, Add, -12),# units:Unit Size Left  index:43    from 22 To 10
        SetMemory(0x661968, Add, -4),# units:Unit Size Left  index:52    from 14 To 10
        SetMemory(0x6619B0, Add, -2),# units:Unit Size Left  index:61    from 12 To 10
        SetMemory(0x6619C0, Add, -6),# units:Unit Size Left  index:63    from 16 To 10
        SetMemory(0x661A08, Add, -31),# units:Unit Size Left  index:72    from 32 To 1
        SetMemory(0x661A20, Add, -2),# units:Unit Size Left  index:75    from 12 To 10
        SetMemory(0x661A68, Add, -6),# units:Unit Size Left  index:84    from 16 To 10
        SetMemory(0x661A78, Add, -12),# units:Unit Size Left  index:86    from 22 To 10
        SetMemory(0x661AF8, Add, -27),# units:Unit Size Left  index:102    from 37 To 10
        SetMemory(0x661B00, Add, -5),# units:Unit Size Left  index:103    from 15 To 10
        SetMemory(0x661B18, Add, -48),# units:Unit Size Left  index:106    from 58 To 10
        SetMemory(0x661B20, Add, -27),# units:Unit Size Left  index:107    from 37 To 10
        SetMemory(0x661B28, Add, -27),# units:Unit Size Left  index:108    from 37 To 10
        SetMemory(0x661B30, Add, -28),# units:Unit Size Left  index:109    from 38 To 10
        SetMemory(0x661B38, Add, -46),# units:Unit Size Left  index:110    from 56 To 10
        SetMemory(0x661B40, Add, -38),# units:Unit Size Left  index:111    from 48 To 10
        SetMemory(0x661B50, Add, -46),# units:Unit Size Left  index:113    from 56 To 10
        SetMemory(0x661B58, Add, -38),# units:Unit Size Left  index:114    from 48 To 10
        SetMemory(0x661B60, Add, -37),# units:Unit Size Left  index:115    from 47 To 10
        SetMemory(0x661B68, Add, -38),# units:Unit Size Left  index:116    from 48 To 10
        SetMemory(0x661B70, Add, -37),# units:Unit Size Left  index:117    from 47 To 10
        SetMemory(0x661B78, Add, -37),# units:Unit Size Left  index:118    from 47 To 10
        SetMemory(0x661B80, Add, -38),# units:Unit Size Left  index:119    from 48 To 10
        SetMemory(0x661B88, Add, -29),# units:Unit Size Left  index:120    from 39 To 10
        SetMemory(0x661B90, Add, -38),# units:Unit Size Left  index:121    from 48 To 10
        SetMemory(0x661B98, Add, -38),# units:Unit Size Left  index:122    from 48 To 10
        SetMemory(0x661BA0, Add, -38),# units:Unit Size Left  index:123    from 48 To 10
        SetMemory(0x661BA8, Add, -6),# units:Unit Size Left  index:124    from 16 To 10
        SetMemory(0x661BB0, Add, -22),# units:Unit Size Left  index:125    from 32 To 10
        SetMemory(0x661BB8, Add, -38),# units:Unit Size Left  index:126    from 48 To 10
        SetMemory(0x661BC0, Add, -38),# units:Unit Size Left  index:127    from 48 To 10
        SetMemory(0x661BC8, Add, -6),# units:Unit Size Left  index:128    from 16 To 10
        SetMemory(0x661BD0, Add, -6),# units:Unit Size Left  index:129    from 16 To 10
        SetMemory(0x661BD8, Add, -48),# units:Unit Size Left  index:130    from 58 To 10
        SetMemory(0x661BE0, Add, -39),# units:Unit Size Left  index:131    from 49 To 10
        SetMemory(0x661BE8, Add, -39),# units:Unit Size Left  index:132    from 49 To 10
        SetMemory(0x661BF0, Add, -39),# units:Unit Size Left  index:133    from 49 To 10
        SetMemory(0x661BF8, Add, -22),# units:Unit Size Left  index:134    from 32 To 10
        SetMemory(0x661C00, Add, -30),# units:Unit Size Left  index:135    from 40 To 10
        SetMemory(0x661C08, Add, -38),# units:Unit Size Left  index:136    from 48 To 10
        SetMemory(0x661C10, Add, -18),# units:Unit Size Left  index:137    from 28 To 10
        SetMemory(0x661C18, Add, -28),# units:Unit Size Left  index:138    from 38 To 10
        SetMemory(0x661C20, Add, -34),# units:Unit Size Left  index:139    from 44 To 10
        SetMemory(0x661C28, Add, -30),# units:Unit Size Left  index:140    from 40 To 10
        SetMemory(0x661C30, Add, -18),# units:Unit Size Left  index:141    from 28 To 10
        SetMemory(0x661C38, Add, -26),# units:Unit Size Left  index:142    from 36 To 10
        SetMemory(0x661C40, Add, -14),# units:Unit Size Left  index:143    from 24 To 10
        SetMemory(0x661C48, Add, -14),# units:Unit Size Left  index:144    from 24 To 10
        SetMemory(0x661C50, Add, -38),# units:Unit Size Left  index:145    from 48 To 10
        SetMemory(0x661C58, Add, -14),# units:Unit Size Left  index:146    from 24 To 10
        SetMemory(0x661C60, Add, -70),# units:Unit Size Left  index:147    from 80 To 10
        SetMemory(0x661C68, Add, -70),# units:Unit Size Left  index:148    from 80 To 10
        SetMemory(0x661C70, Add, -54),# units:Unit Size Left  index:149    from 64 To 10
        SetMemory(0x661C78, Add, -22),# units:Unit Size Left  index:150    from 32 To 10
        SetMemory(0x661C80, Add, -30),# units:Unit Size Left  index:151    from 40 To 10
        SetMemory(0x661C88, Add, -30),# units:Unit Size Left  index:152    from 40 To 10
        SetMemory(0x661C90, Add, -6),# units:Unit Size Left  index:153    from 16 To 10
        SetMemory(0x661C98, Add, -46),# units:Unit Size Left  index:154    from 56 To 10
        SetMemory(0x661CA0, Add, -26),# units:Unit Size Left  index:155    from 36 To 10
        SetMemory(0x661CA8, Add, -6),# units:Unit Size Left  index:156    from 16 To 10
        SetMemory(0x661CB0, Add, -38),# units:Unit Size Left  index:157    from 48 To 10
        SetMemory(0x661CB8, Add, -54),# units:Unit Size Left  index:158    from 64 To 10
        SetMemory(0x661CC0, Add, -34),# units:Unit Size Left  index:159    from 44 To 10
        SetMemory(0x661CC8, Add, -38),# units:Unit Size Left  index:160    from 48 To 10
        SetMemory(0x661CD0, Add, -38),# units:Unit Size Left  index:161    from 48 To 10
        SetMemory(0x661CD8, Add, -10),# units:Unit Size Left  index:162    from 20 To 10
        SetMemory(0x661CE0, Add, -14),# units:Unit Size Left  index:163    from 24 To 10
        SetMemory(0x661CE8, Add, -30),# units:Unit Size Left  index:164    from 40 To 10
        SetMemory(0x661CF0, Add, -22),# units:Unit Size Left  index:165    from 32 To 10
        SetMemory(0x661CF8, Add, -26),# units:Unit Size Left  index:166    from 36 To 10
        SetMemory(0x661D00, Add, -38),# units:Unit Size Left  index:167    from 48 To 10
        SetMemory(0x661D08, Add, -54),# units:Unit Size Left  index:168    from 64 To 10
        SetMemory(0x661D10, Add, -30),# units:Unit Size Left  index:169    from 40 To 10
        SetMemory(0x661D18, Add, -34),# units:Unit Size Left  index:170    from 44 To 10
        SetMemory(0x661D20, Add, -22),# units:Unit Size Left  index:171    from 32 To 10
        SetMemory(0x661D28, Add, -22),# units:Unit Size Left  index:172    from 32 To 10
        SetMemory(0x661D30, Add, -54),# units:Unit Size Left  index:173    from 64 To 10
        SetMemory(0x661E98, Add, -15),# units:Unit Size Left  index:218    from 16 To 1
        SetMemory(0x6617C8, Add, 65536),# units:Unit Size Up  index:0    from 9 To 10
        SetMemory(0x6617D8, Add, -393216),# units:Unit Size Up  index:2    from 16 To 10
        SetMemory(0x6617E0, Add, -393216),# units:Unit Size Up  index:3    from 16 To 10
        SetMemory(0x6617F0, Add, -393216),# units:Unit Size Up  index:5    from 16 To 10
        SetMemory(0x661808, Add, -327680),# units:Unit Size Up  index:8    from 15 To 10
        SetMemory(0x661810, Add, -1507328),# units:Unit Size Up  index:9    from 33 To 10
        SetMemory(0x661818, Add, -196608),# units:Unit Size Up  index:10    from 13 To 10
        SetMemory(0x661820, Add, -393216),# units:Unit Size Up  index:11    from 16 To 10
        SetMemory(0x661828, Add, -1245184),# units:Unit Size Up  index:12    from 29 To 10
        SetMemory(0x661848, Add, -589824),# units:Unit Size Up  index:16    from 10 To 1
        SetMemory(0x661850, Add, -393216),# units:Unit Size Up  index:17    from 16 To 10
        SetMemory(0x661868, Add, 65536),# units:Unit Size Up  index:20    from 9 To 10
        SetMemory(0x661870, Add, -327680),# units:Unit Size Up  index:21    from 15 To 10
        SetMemory(0x661878, Add, -1114112),# units:Unit Size Up  index:22    from 33 To 16
        SetMemory(0x661880, Add, -393216),# units:Unit Size Up  index:23    from 16 To 10
        SetMemory(0x661890, Add, -393216),# units:Unit Size Up  index:25    from 16 To 10
        SetMemory(0x6618A0, Add, -1245184),# units:Unit Size Up  index:27    from 29 To 10
        SetMemory(0x6618A8, Add, -1245184),# units:Unit Size Up  index:28    from 29 To 10
        SetMemory(0x6618B0, Add, -1245184),# units:Unit Size Up  index:29    from 29 To 10
        SetMemory(0x6618B8, Add, -393216),# units:Unit Size Up  index:30    from 16 To 10
        SetMemory(0x6618C8, Add, 196608),# units:Unit Size Up  index:32    from 7 To 10
        SetMemory(0x6618D8, Add, 65536),# units:Unit Size Up  index:34    from 9 To 10
        SetMemory(0x6618E0, Add, 131072),# units:Unit Size Up  index:35    from 8 To 10
        SetMemory(0x6618E8, Add, -393216),# units:Unit Size Up  index:36    from 16 To 10
        SetMemory(0x661910, Add, -65536),# units:Unit Size Up  index:41    from 11 To 10
        SetMemory(0x661918, Add, -1376256),# units:Unit Size Up  index:42    from 25 To 4
        SetMemory(0x661920, Add, -786432),# units:Unit Size Up  index:43    from 22 To 10
        SetMemory(0x661968, Add, -262144),# units:Unit Size Up  index:52    from 14 To 10
        SetMemory(0x6619B0, Add, 262144),# units:Unit Size Up  index:61    from 6 To 10
        SetMemory(0x6619C0, Add, -393216),# units:Unit Size Up  index:63    from 16 To 10
        SetMemory(0x661A08, Add, -2031616),# units:Unit Size Up  index:72    from 32 To 1
        SetMemory(0x661A20, Add, 262144),# units:Unit Size Up  index:75    from 6 To 10
        SetMemory(0x661A68, Add, -393216),# units:Unit Size Up  index:84    from 16 To 10
        SetMemory(0x661A78, Add, -786432),# units:Unit Size Up  index:86    from 22 To 10
        SetMemory(0x661AF8, Add, -1245184),# units:Unit Size Up  index:102    from 29 To 10
        SetMemory(0x661B00, Add, -327680),# units:Unit Size Up  index:103    from 15 To 10
        SetMemory(0x661B18, Add, -2031616),# units:Unit Size Up  index:106    from 41 To 10
        SetMemory(0x661B20, Add, -393216),# units:Unit Size Up  index:107    from 16 To 10
        SetMemory(0x661B28, Add, -393216),# units:Unit Size Up  index:108    from 16 To 10
        SetMemory(0x661B30, Add, -786432),# units:Unit Size Up  index:109    from 22 To 10
        SetMemory(0x661B38, Add, -1441792),# units:Unit Size Up  index:110    from 32 To 10
        SetMemory(0x661B40, Add, -1966080),# units:Unit Size Up  index:111    from 40 To 10
        SetMemory(0x661B50, Add, -1966080),# units:Unit Size Up  index:113    from 40 To 10
        SetMemory(0x661B58, Add, -1966080),# units:Unit Size Up  index:114    from 40 To 10
        SetMemory(0x661B60, Add, -917504),# units:Unit Size Up  index:115    from 24 To 10
        SetMemory(0x661B68, Add, -1835008),# units:Unit Size Up  index:116    from 38 To 10
        SetMemory(0x661B70, Add, -917504),# units:Unit Size Up  index:117    from 24 To 10
        SetMemory(0x661B78, Add, -917504),# units:Unit Size Up  index:118    from 24 To 10
        SetMemory(0x661B80, Add, -1441792),# units:Unit Size Up  index:119    from 32 To 10
        SetMemory(0x661B88, Add, -917504),# units:Unit Size Up  index:120    from 24 To 10
        SetMemory(0x661B90, Add, -2490368),# units:Unit Size Up  index:121    from 48 To 10
        SetMemory(0x661B98, Add, -1441792),# units:Unit Size Up  index:122    from 32 To 10
        SetMemory(0x661BA0, Add, -1441792),# units:Unit Size Up  index:123    from 32 To 10
        SetMemory(0x661BA8, Add, -1441792),# units:Unit Size Up  index:124    from 32 To 10
        SetMemory(0x661BB0, Add, -917504),# units:Unit Size Up  index:125    from 24 To 10
        SetMemory(0x661BB8, Add, -1441792),# units:Unit Size Up  index:126    from 32 To 10
        SetMemory(0x661BC0, Add, -1441792),# units:Unit Size Up  index:127    from 32 To 10
        SetMemory(0x661BC8, Add, -393216),# units:Unit Size Up  index:128    from 16 To 10
        SetMemory(0x661BD0, Add, -393216),# units:Unit Size Up  index:129    from 16 To 10
        SetMemory(0x661BD8, Add, -2031616),# units:Unit Size Up  index:130    from 41 To 10
        SetMemory(0x661BE0, Add, -1441792),# units:Unit Size Up  index:131    from 32 To 10
        SetMemory(0x661BE8, Add, -1441792),# units:Unit Size Up  index:132    from 32 To 10
        SetMemory(0x661BF0, Add, -1441792),# units:Unit Size Up  index:133    from 32 To 10
        SetMemory(0x661BF8, Add, -1441792),# units:Unit Size Up  index:134    from 32 To 10
        SetMemory(0x661C00, Add, -1441792),# units:Unit Size Up  index:135    from 32 To 10
        SetMemory(0x661C08, Add, -1441792),# units:Unit Size Up  index:136    from 32 To 10
        SetMemory(0x661C10, Add, -1441792),# units:Unit Size Up  index:137    from 32 To 10
        SetMemory(0x661C18, Add, -1179648),# units:Unit Size Up  index:138    from 28 To 10
        SetMemory(0x661C20, Add, -1441792),# units:Unit Size Up  index:139    from 32 To 10
        SetMemory(0x661C28, Add, -1441792),# units:Unit Size Up  index:140    from 32 To 10
        SetMemory(0x661C30, Add, -1441792),# units:Unit Size Up  index:141    from 32 To 10
        SetMemory(0x661C38, Add, -1179648),# units:Unit Size Up  index:142    from 28 To 10
        SetMemory(0x661C40, Add, -917504),# units:Unit Size Up  index:143    from 24 To 10
        SetMemory(0x661C48, Add, -917504),# units:Unit Size Up  index:144    from 24 To 10
        SetMemory(0x661C50, Add, -2490368),# units:Unit Size Up  index:145    from 48 To 10
        SetMemory(0x661C58, Add, -917504),# units:Unit Size Up  index:146    from 24 To 10
        SetMemory(0x661C60, Add, -1441792),# units:Unit Size Up  index:147    from 32 To 10
        SetMemory(0x661C68, Add, -1441792),# units:Unit Size Up  index:148    from 32 To 10
        SetMemory(0x661C70, Add, -1441792),# units:Unit Size Up  index:149    from 32 To 10
        SetMemory(0x661C78, Add, -1441792),# units:Unit Size Up  index:150    from 32 To 10
        SetMemory(0x661C80, Add, -1441792),# units:Unit Size Up  index:151    from 32 To 10
        SetMemory(0x661C88, Add, -1441792),# units:Unit Size Up  index:152    from 32 To 10
        SetMemory(0x661C90, Add, -393216),# units:Unit Size Up  index:153    from 16 To 10
        SetMemory(0x661C98, Add, -1900544),# units:Unit Size Up  index:154    from 39 To 10
        SetMemory(0x661CA0, Add, -393216),# units:Unit Size Up  index:155    from 16 To 10
        SetMemory(0x661CA8, Add, -131072),# units:Unit Size Up  index:156    from 12 To 10
        SetMemory(0x661CB0, Add, -1441792),# units:Unit Size Up  index:157    from 32 To 10
        SetMemory(0x661CB8, Add, -2490368),# units:Unit Size Up  index:158    from 48 To 10
        SetMemory(0x661CC0, Add, -393216),# units:Unit Size Up  index:159    from 16 To 10
        SetMemory(0x661CC8, Add, -1441792),# units:Unit Size Up  index:160    from 32 To 10
        SetMemory(0x661CD0, Add, -2490368),# units:Unit Size Up  index:161    from 48 To 10
        SetMemory(0x661CD8, Add, -393216),# units:Unit Size Up  index:162    from 16 To 10
        SetMemory(0x661CE0, Add, -917504),# units:Unit Size Up  index:163    from 24 To 10
        SetMemory(0x661CE8, Add, -917504),# units:Unit Size Up  index:164    from 24 To 10
        SetMemory(0x661CF0, Add, -917504),# units:Unit Size Up  index:165    from 24 To 10
        SetMemory(0x661CF8, Add, -917504),# units:Unit Size Up  index:166    from 24 To 10
        SetMemory(0x661D00, Add, -1966080),# units:Unit Size Up  index:167    from 40 To 10
        SetMemory(0x661D08, Add, -2490368),# units:Unit Size Up  index:168    from 48 To 10
        SetMemory(0x661D10, Add, -1441792),# units:Unit Size Up  index:169    from 32 To 10
        SetMemory(0x661D18, Add, -1179648),# units:Unit Size Up  index:170    from 28 To 10
        SetMemory(0x661D20, Add, -1441792),# units:Unit Size Up  index:171    from 32 To 10
        SetMemory(0x661D28, Add, -393216),# units:Unit Size Up  index:172    from 16 To 10
        SetMemory(0x661D30, Add, -2490368),# units:Unit Size Up  index:173    from 48 To 10
        SetMemory(0x661E98, Add, -983040),# units:Unit Size Up  index:218    from 16 To 1
        SetMemory(0x6617CC, Add, 2),# units:Unit Size Right  index:0    from 8 To 10
        SetMemory(0x6617DC, Add, -5),# units:Unit Size Right  index:2    from 15 To 10
        SetMemory(0x6617E4, Add, -5),# units:Unit Size Right  index:3    from 15 To 10
        SetMemory(0x6617F4, Add, -5),# units:Unit Size Right  index:5    from 15 To 10
        SetMemory(0x66180C, Add, -8),# units:Unit Size Right  index:8    from 18 To 10
        SetMemory(0x661814, Add, -22),# units:Unit Size Right  index:9    from 32 To 10
        SetMemory(0x66181C, Add, -1),# units:Unit Size Right  index:10    from 11 To 10
        SetMemory(0x661824, Add, -14),# units:Unit Size Right  index:11    from 24 To 10
        SetMemory(0x66182C, Add, -27),# units:Unit Size Right  index:12    from 37 To 10
        SetMemory(0x66184C, Add, -6),# units:Unit Size Right  index:16    from 7 To 1
        SetMemory(0x661854, Add, -5),# units:Unit Size Right  index:17    from 15 To 10
        SetMemory(0x66186C, Add, 2),# units:Unit Size Right  index:20    from 8 To 10
        SetMemory(0x661874, Add, -8),# units:Unit Size Right  index:21    from 18 To 10
        SetMemory(0x66187C, Add, -16),# units:Unit Size Right  index:22    from 32 To 16
        SetMemory(0x661884, Add, -5),# units:Unit Size Right  index:23    from 15 To 10
        SetMemory(0x661894, Add, -5),# units:Unit Size Right  index:25    from 15 To 10
        SetMemory(0x6618A4, Add, -27),# units:Unit Size Right  index:27    from 37 To 10
        SetMemory(0x6618AC, Add, -27),# units:Unit Size Right  index:28    from 37 To 10
        SetMemory(0x6618B4, Add, -27),# units:Unit Size Right  index:29    from 37 To 10
        SetMemory(0x6618BC, Add, -5),# units:Unit Size Right  index:30    from 15 To 10
        SetMemory(0x6618CC, Add, -1),# units:Unit Size Right  index:32    from 11 To 10
        SetMemory(0x6618DC, Add, 2),# units:Unit Size Right  index:34    from 8 To 10
        SetMemory(0x6618E4, Add, 3),# units:Unit Size Right  index:35    from 7 To 10
        SetMemory(0x6618EC, Add, -5),# units:Unit Size Right  index:36    from 15 To 10
        SetMemory(0x661914, Add, -1),# units:Unit Size Right  index:41    from 11 To 10
        SetMemory(0x66191C, Add, -20),# units:Unit Size Right  index:42    from 24 To 4
        SetMemory(0x661924, Add, -11),# units:Unit Size Right  index:43    from 21 To 10
        SetMemory(0x66196C, Add, -4),# units:Unit Size Right  index:52    from 14 To 10
        SetMemory(0x6619B4, Add, -1),# units:Unit Size Right  index:61    from 11 To 10
        SetMemory(0x6619C4, Add, -5),# units:Unit Size Right  index:63    from 15 To 10
        SetMemory(0x661A0C, Add, -30),# units:Unit Size Right  index:72    from 31 To 1
        SetMemory(0x661A24, Add, -1),# units:Unit Size Right  index:75    from 11 To 10
        SetMemory(0x661A6C, Add, -5),# units:Unit Size Right  index:84    from 15 To 10
        SetMemory(0x661A7C, Add, -11),# units:Unit Size Right  index:86    from 21 To 10
        SetMemory(0x661AFC, Add, -27),# units:Unit Size Right  index:102    from 37 To 10
        SetMemory(0x661B04, Add, -6),# units:Unit Size Right  index:103    from 16 To 10
        SetMemory(0x661B1C, Add, -48),# units:Unit Size Right  index:106    from 58 To 10
        SetMemory(0x661B24, Add, -21),# units:Unit Size Right  index:107    from 31 To 10
        SetMemory(0x661B2C, Add, -21),# units:Unit Size Right  index:108    from 31 To 10
        SetMemory(0x661B34, Add, -28),# units:Unit Size Right  index:109    from 38 To 10
        SetMemory(0x661B3C, Add, -46),# units:Unit Size Right  index:110    from 56 To 10
        SetMemory(0x661B44, Add, -46),# units:Unit Size Right  index:111    from 56 To 10
        SetMemory(0x661B54, Add, -46),# units:Unit Size Right  index:113    from 56 To 10
        SetMemory(0x661B5C, Add, -38),# units:Unit Size Right  index:114    from 48 To 10
        SetMemory(0x661B64, Add, -18),# units:Unit Size Right  index:115    from 28 To 10
        SetMemory(0x661B6C, Add, -38),# units:Unit Size Right  index:116    from 48 To 10
        SetMemory(0x661B74, Add, -18),# units:Unit Size Right  index:117    from 28 To 10
        SetMemory(0x661B7C, Add, -18),# units:Unit Size Right  index:118    from 28 To 10
        SetMemory(0x661B84, Add, -37),# units:Unit Size Right  index:119    from 47 To 10
        SetMemory(0x661B8C, Add, -21),# units:Unit Size Right  index:120    from 31 To 10
        SetMemory(0x661B94, Add, -37),# units:Unit Size Right  index:121    from 47 To 10
        SetMemory(0x661B9C, Add, -38),# units:Unit Size Right  index:122    from 48 To 10
        SetMemory(0x661BA4, Add, -37),# units:Unit Size Right  index:123    from 47 To 10
        SetMemory(0x661BAC, Add, -6),# units:Unit Size Right  index:124    from 16 To 10
        SetMemory(0x661BB4, Add, -22),# units:Unit Size Right  index:125    from 32 To 10
        SetMemory(0x661BBC, Add, -37),# units:Unit Size Right  index:126    from 47 To 10
        SetMemory(0x661BC4, Add, -37),# units:Unit Size Right  index:127    from 47 To 10
        SetMemory(0x661BCC, Add, -5),# units:Unit Size Right  index:128    from 15 To 10
        SetMemory(0x661BD4, Add, -5),# units:Unit Size Right  index:129    from 15 To 10
        SetMemory(0x661BDC, Add, -48),# units:Unit Size Right  index:130    from 58 To 10
        SetMemory(0x661BE4, Add, -39),# units:Unit Size Right  index:131    from 49 To 10
        SetMemory(0x661BEC, Add, -39),# units:Unit Size Right  index:132    from 49 To 10
        SetMemory(0x661BF4, Add, -39),# units:Unit Size Right  index:133    from 49 To 10
        SetMemory(0x661BFC, Add, -21),# units:Unit Size Right  index:134    from 31 To 10
        SetMemory(0x661C04, Add, -30),# units:Unit Size Right  index:135    from 40 To 10
        SetMemory(0x661C0C, Add, -38),# units:Unit Size Right  index:136    from 48 To 10
        SetMemory(0x661C14, Add, -18),# units:Unit Size Right  index:137    from 28 To 10
        SetMemory(0x661C1C, Add, -22),# units:Unit Size Right  index:138    from 32 To 10
        SetMemory(0x661C24, Add, -22),# units:Unit Size Right  index:139    from 32 To 10
        SetMemory(0x661C2C, Add, -22),# units:Unit Size Right  index:140    from 32 To 10
        SetMemory(0x661C34, Add, -18),# units:Unit Size Right  index:141    from 28 To 10
        SetMemory(0x661C3C, Add, -30),# units:Unit Size Right  index:142    from 40 To 10
        SetMemory(0x661C44, Add, -13),# units:Unit Size Right  index:143    from 23 To 10
        SetMemory(0x661C4C, Add, -13),# units:Unit Size Right  index:144    from 23 To 10
        SetMemory(0x661C54, Add, -37),# units:Unit Size Right  index:145    from 47 To 10
        SetMemory(0x661C5C, Add, -13),# units:Unit Size Right  index:146    from 23 To 10
        SetMemory(0x661C64, Add, -69),# units:Unit Size Right  index:147    from 79 To 10
        SetMemory(0x661C6C, Add, -69),# units:Unit Size Right  index:148    from 79 To 10
        SetMemory(0x661C74, Add, -53),# units:Unit Size Right  index:149    from 63 To 10
        SetMemory(0x661C7C, Add, -21),# units:Unit Size Right  index:150    from 31 To 10
        SetMemory(0x661C84, Add, -22),# units:Unit Size Right  index:151    from 32 To 10
        SetMemory(0x661C8C, Add, -22),# units:Unit Size Right  index:152    from 32 To 10
        SetMemory(0x661C94, Add, -5),# units:Unit Size Right  index:153    from 15 To 10
        SetMemory(0x661C9C, Add, -46),# units:Unit Size Right  index:154    from 56 To 10
        SetMemory(0x661CA4, Add, -30),# units:Unit Size Right  index:155    from 40 To 10
        SetMemory(0x661CAC, Add, -6),# units:Unit Size Right  index:156    from 16 To 10
        SetMemory(0x661CB4, Add, -38),# units:Unit Size Right  index:157    from 48 To 10
        SetMemory(0x661CBC, Add, -53),# units:Unit Size Right  index:158    from 63 To 10
        SetMemory(0x661CC4, Add, -34),# units:Unit Size Right  index:159    from 44 To 10
        SetMemory(0x661CCC, Add, -38),# units:Unit Size Right  index:160    from 48 To 10
        SetMemory(0x661CD4, Add, -37),# units:Unit Size Right  index:161    from 47 To 10
        SetMemory(0x661CDC, Add, -10),# units:Unit Size Right  index:162    from 20 To 10
        SetMemory(0x661CE4, Add, -30),# units:Unit Size Right  index:163    from 40 To 10
        SetMemory(0x661CEC, Add, -30),# units:Unit Size Right  index:164    from 40 To 10
        SetMemory(0x661CF4, Add, -22),# units:Unit Size Right  index:165    from 32 To 10
        SetMemory(0x661CFC, Add, -26),# units:Unit Size Right  index:166    from 36 To 10
        SetMemory(0x661D04, Add, -38),# units:Unit Size Right  index:167    from 48 To 10
        SetMemory(0x661D0C, Add, -53),# units:Unit Size Right  index:168    from 63 To 10
        SetMemory(0x661D14, Add, -37),# units:Unit Size Right  index:169    from 47 To 10
        SetMemory(0x661D1C, Add, -34),# units:Unit Size Right  index:170    from 44 To 10
        SetMemory(0x661D24, Add, -22),# units:Unit Size Right  index:171    from 32 To 10
        SetMemory(0x661D2C, Add, -22),# units:Unit Size Right  index:172    from 32 To 10
        SetMemory(0x661D34, Add, -53),# units:Unit Size Right  index:173    from 63 To 10
        SetMemory(0x661E9C, Add, -14),# units:Unit Size Right  index:218    from 15 To 1
        SetMemory(0x6617DC, Add, -327680),# units:Unit Size Down  index:2    from 15 To 10
        SetMemory(0x6617E4, Add, -327680),# units:Unit Size Down  index:3    from 15 To 10
        SetMemory(0x6617F4, Add, -327680),# units:Unit Size Down  index:5    from 15 To 10
        SetMemory(0x66180C, Add, -262144),# units:Unit Size Down  index:8    from 14 To 10
        SetMemory(0x661814, Add, -393216),# units:Unit Size Down  index:9    from 16 To 10
        SetMemory(0x66181C, Add, -262144),# units:Unit Size Down  index:10    from 14 To 10
        SetMemory(0x661824, Add, -655360),# units:Unit Size Down  index:11    from 20 To 10
        SetMemory(0x66182C, Add, -1245184),# units:Unit Size Down  index:12    from 29 To 10
        SetMemory(0x66184C, Add, -655360),# units:Unit Size Down  index:16    from 11 To 1
        SetMemory(0x661854, Add, -327680),# units:Unit Size Down  index:17    from 15 To 10
        SetMemory(0x661874, Add, -262144),# units:Unit Size Down  index:21    from 14 To 10
        SetMemory(0x661884, Add, -327680),# units:Unit Size Down  index:23    from 15 To 10
        SetMemory(0x661894, Add, -327680),# units:Unit Size Down  index:25    from 15 To 10
        SetMemory(0x6618A4, Add, -1245184),# units:Unit Size Down  index:27    from 29 To 10
        SetMemory(0x6618AC, Add, -1245184),# units:Unit Size Down  index:28    from 29 To 10
        SetMemory(0x6618B4, Add, -1245184),# units:Unit Size Down  index:29    from 29 To 10
        SetMemory(0x6618BC, Add, -327680),# units:Unit Size Down  index:30    from 15 To 10
        SetMemory(0x6618CC, Add, -262144),# units:Unit Size Down  index:32    from 14 To 10
        SetMemory(0x6618E4, Add, 196608),# units:Unit Size Down  index:35    from 7 To 10
        SetMemory(0x6618EC, Add, -327680),# units:Unit Size Down  index:36    from 15 To 10
        SetMemory(0x661914, Add, -65536),# units:Unit Size Down  index:41    from 11 To 10
        SetMemory(0x66191C, Add, -1310720),# units:Unit Size Down  index:42    from 24 To 4
        SetMemory(0x661924, Add, -720896),# units:Unit Size Down  index:43    from 21 To 10
        SetMemory(0x66196C, Add, -262144),# units:Unit Size Down  index:52    from 14 To 10
        SetMemory(0x6619B4, Add, -589824),# units:Unit Size Down  index:61    from 19 To 10
        SetMemory(0x6619C4, Add, -327680),# units:Unit Size Down  index:63    from 15 To 10
        SetMemory(0x661A0C, Add, -1966080),# units:Unit Size Down  index:72    from 31 To 1
        SetMemory(0x661A24, Add, -589824),# units:Unit Size Down  index:75    from 19 To 10
        SetMemory(0x661A6C, Add, -327680),# units:Unit Size Down  index:84    from 15 To 10
        SetMemory(0x661A7C, Add, -720896),# units:Unit Size Down  index:86    from 21 To 10
        SetMemory(0x661AFC, Add, -1245184),# units:Unit Size Down  index:102    from 29 To 10
        SetMemory(0x661B04, Add, -393216),# units:Unit Size Down  index:103    from 16 To 10
        SetMemory(0x661B1C, Add, -2031616),# units:Unit Size Down  index:106    from 41 To 10
        SetMemory(0x661B24, Add, -983040),# units:Unit Size Down  index:107    from 25 To 10
        SetMemory(0x661B2C, Add, -983040),# units:Unit Size Down  index:108    from 25 To 10
        SetMemory(0x661B34, Add, -1048576),# units:Unit Size Down  index:109    from 26 To 10
        SetMemory(0x661B3C, Add, -1376256),# units:Unit Size Down  index:110    from 31 To 10
        SetMemory(0x661B44, Add, -1441792),# units:Unit Size Down  index:111    from 32 To 10
        SetMemory(0x661B54, Add, -1966080),# units:Unit Size Down  index:113    from 40 To 10
        SetMemory(0x661B5C, Add, -1835008),# units:Unit Size Down  index:114    from 38 To 10
        SetMemory(0x661B64, Add, -786432),# units:Unit Size Down  index:115    from 22 To 10
        SetMemory(0x661B6C, Add, -1835008),# units:Unit Size Down  index:116    from 38 To 10
        SetMemory(0x661B74, Add, -786432),# units:Unit Size Down  index:117    from 22 To 10
        SetMemory(0x661B7C, Add, -786432),# units:Unit Size Down  index:118    from 22 To 10
        SetMemory(0x661B84, Add, -1376256),# units:Unit Size Down  index:119    from 31 To 10
        SetMemory(0x661B8C, Add, -917504),# units:Unit Size Down  index:120    from 24 To 10
        SetMemory(0x661B94, Add, -2424832),# units:Unit Size Down  index:121    from 47 To 10
        SetMemory(0x661B9C, Add, -1179648),# units:Unit Size Down  index:122    from 28 To 10
        SetMemory(0x661BA4, Add, -786432),# units:Unit Size Down  index:123    from 22 To 10
        SetMemory(0x661BAC, Add, -393216),# units:Unit Size Down  index:124    from 16 To 10
        SetMemory(0x661BB4, Add, -393216),# units:Unit Size Down  index:125    from 16 To 10
        SetMemory(0x661BBC, Add, -1376256),# units:Unit Size Down  index:126    from 31 To 10
        SetMemory(0x661BC4, Add, -1376256),# units:Unit Size Down  index:127    from 31 To 10
        SetMemory(0x661BCC, Add, -327680),# units:Unit Size Down  index:128    from 15 To 10
        SetMemory(0x661BD4, Add, -327680),# units:Unit Size Down  index:129    from 15 To 10
        SetMemory(0x661BDC, Add, -2031616),# units:Unit Size Down  index:130    from 41 To 10
        SetMemory(0x661BE4, Add, -1441792),# units:Unit Size Down  index:131    from 32 To 10
        SetMemory(0x661BEC, Add, -1441792),# units:Unit Size Down  index:132    from 32 To 10
        SetMemory(0x661BF4, Add, -1441792),# units:Unit Size Down  index:133    from 32 To 10
        SetMemory(0x661BFC, Add, -1376256),# units:Unit Size Down  index:134    from 31 To 10
        SetMemory(0x661C04, Add, -917504),# units:Unit Size Down  index:135    from 24 To 10
        SetMemory(0x661C0C, Add, 393216),# units:Unit Size Down  index:136    from 4 To 10
        SetMemory(0x661C14, Add, -917504),# units:Unit Size Down  index:137    from 24 To 10
        SetMemory(0x661C1C, Add, -1179648),# units:Unit Size Down  index:138    from 28 To 10
        SetMemory(0x661C24, Add, -655360),# units:Unit Size Down  index:139    from 20 To 10
        SetMemory(0x661C2C, Add, -1376256),# units:Unit Size Down  index:140    from 31 To 10
        SetMemory(0x661C34, Add, -917504),# units:Unit Size Down  index:141    from 24 To 10
        SetMemory(0x661C3C, Add, -524288),# units:Unit Size Down  index:142    from 18 To 10
        SetMemory(0x661C44, Add, -851968),# units:Unit Size Down  index:143    from 23 To 10
        SetMemory(0x661C4C, Add, -851968),# units:Unit Size Down  index:144    from 23 To 10
        SetMemory(0x661C54, Add, -2424832),# units:Unit Size Down  index:145    from 47 To 10
        SetMemory(0x661C5C, Add, -851968),# units:Unit Size Down  index:146    from 23 To 10
        SetMemory(0x661C64, Add, -1966080),# units:Unit Size Down  index:147    from 40 To 10
        SetMemory(0x661C6C, Add, -1966080),# units:Unit Size Down  index:148    from 40 To 10
        SetMemory(0x661C74, Add, -1376256),# units:Unit Size Down  index:149    from 31 To 10
        SetMemory(0x661C7C, Add, -1376256),# units:Unit Size Down  index:150    from 31 To 10
        SetMemory(0x661C84, Add, -1376256),# units:Unit Size Down  index:151    from 31 To 10
        SetMemory(0x661C8C, Add, -1376256),# units:Unit Size Down  index:152    from 31 To 10
        SetMemory(0x661C94, Add, -327680),# units:Unit Size Down  index:153    from 15 To 10
        SetMemory(0x661C9C, Add, -1900544),# units:Unit Size Down  index:154    from 39 To 10
        SetMemory(0x661CA4, Add, -655360),# units:Unit Size Down  index:155    from 20 To 10
        SetMemory(0x661CAC, Add, -655360),# units:Unit Size Down  index:156    from 20 To 10
        SetMemory(0x661CB4, Add, -917504),# units:Unit Size Down  index:157    from 24 To 10
        SetMemory(0x661CBC, Add, -2424832),# units:Unit Size Down  index:158    from 47 To 10
        SetMemory(0x661CC4, Add, -1179648),# units:Unit Size Down  index:159    from 28 To 10
        SetMemory(0x661CCC, Add, -1966080),# units:Unit Size Down  index:160    from 40 To 10
        SetMemory(0x661CD4, Add, -2424832),# units:Unit Size Down  index:161    from 47 To 10
        SetMemory(0x661CDC, Add, -393216),# units:Unit Size Down  index:162    from 16 To 10
        SetMemory(0x661CE4, Add, -917504),# units:Unit Size Down  index:163    from 24 To 10
        SetMemory(0x661CEC, Add, -917504),# units:Unit Size Down  index:164    from 24 To 10
        SetMemory(0x661CF4, Add, -917504),# units:Unit Size Down  index:165    from 24 To 10
        SetMemory(0x661CFC, Add, -655360),# units:Unit Size Down  index:166    from 20 To 10
        SetMemory(0x661D04, Add, -1441792),# units:Unit Size Down  index:167    from 32 To 10
        SetMemory(0x661D0C, Add, -2424832),# units:Unit Size Down  index:168    from 47 To 10
        SetMemory(0x661D14, Add, -917504),# units:Unit Size Down  index:169    from 24 To 10
        SetMemory(0x661D1C, Add, -1179648),# units:Unit Size Down  index:170    from 28 To 10
        SetMemory(0x661D24, Add, -655360),# units:Unit Size Down  index:171    from 20 To 10
        SetMemory(0x661D2C, Add, -393216),# units:Unit Size Down  index:172    from 16 To 10
        SetMemory(0x661D34, Add, -2424832),# units:Unit Size Down  index:173    from 47 To 10
        SetMemory(0x661E9C, Add, -917504),# units:Unit Size Down  index:218    from 15 To 1
        SetMemory(0x662F88, Add, 9),# units:Portrait  index:0    from 0 To 9
        SetMemory(0x662F8C, Add, 6),# units:Portrait  index:2    from 3 To 9
        SetMemory(0x662F8C, Add, 262144),# units:Portrait  index:3    from 5 To 9
        SetMemory(0x662F90, Add, 4),# units:Portrait  index:4    from 5 To 9
        SetMemory(0x662F90, Add, 196608),# units:Portrait  index:5    from 6 To 9
        SetMemory(0x662F94, Add, 3),# units:Portrait  index:6    from 6 To 9
        SetMemory(0x662F98, Add, 1),# units:Portrait  index:8    from 8 To 9
        SetMemory(0x662F9C, Add, 7),# units:Portrait  index:10    from 2 To 9
        SetMemory(0x662F9C, Add, -65536),# units:Portrait  index:11    from 10 To 9
        SetMemory(0x662FA0, Add, -2),# units:Portrait  index:12    from 11 To 9
        SetMemory(0x662FA8, Add, 262144),# units:Portrait  index:17    from 5 To 9
        SetMemory(0x662FAC, Add, 4),# units:Portrait  index:18    from 5 To 9
        SetMemory(0x662FAC, Add, 2359296),# units:Portrait  index:19    from 13 To 49
        SetMemory(0x662FB0, Add, -4),# units:Portrait  index:20    from 13 To 9
        SetMemory(0x662FB0, Add, 65536),# units:Portrait  index:21    from 8 To 9
        SetMemory(0x662FB4, Add, -327680),# units:Portrait  index:23    from 14 To 9
        SetMemory(0x662FB8, Add, -5),# units:Portrait  index:24    from 14 To 9
        SetMemory(0x662FB8, Add, -327680),# units:Portrait  index:25    from 14 To 9
        SetMemory(0x662FBC, Add, -5),# units:Portrait  index:26    from 14 To 9
        SetMemory(0x662FBC, Add, -458752),# units:Portrait  index:27    from 16 To 9
        SetMemory(0x662FC0, Add, -4),# units:Portrait  index:28    from 13 To 9
        SetMemory(0x662FC0, Add, -327680),# units:Portrait  index:29    from 14 To 9
        SetMemory(0x662FC4, Add, 3),# units:Portrait  index:30    from 6 To 9
        SetMemory(0x662FC4, Add, 196608),# units:Portrait  index:31    from 6 To 9
        SetMemory(0x662FC8, Add, 7),# units:Portrait  index:32    from 2 To 9
        SetMemory(0x662FCC, Add, -81),# units:Portrait  index:34    from 90 To 9
        SetMemory(0x662FCC, Add, -589824),# units:Portrait  index:35    from 18 To 9
        SetMemory(0x662FD0, Add, -10),# units:Portrait  index:36    from 19 To 9
        SetMemory(0x662FD0, Add, -720896),# units:Portrait  index:37    from 20 To 9
        SetMemory(0x662FD4, Add, -12),# units:Portrait  index:38    from 21 To 9
        SetMemory(0x663000, Add, -91),# units:Portrait  index:60    from 100 To 9
        SetMemory(0x663000, Add, -2621440),# units:Portrait  index:61    from 49 To 9
        SetMemory(0x663004, Add, -88),# units:Portrait  index:62    from 97 To 9
        SetMemory(0x663014, Add, -36),# units:Portrait  index:70    from 45 To 9
        SetMemory(0x663014, Add, -2424832),# units:Portrait  index:71    from 46 To 9
        SetMemory(0x66301C, Add, -2818048),# units:Portrait  index:75    from 52 To 9
        SetMemory(0x663028, Add, -3080192),# units:Portrait  index:81    from 56 To 9
        SetMemory(0x66302C, Add, -45),# units:Portrait  index:82    from 54 To 9
        SetMemory(0x66302C, Add, -3080192),# units:Portrait  index:83    from 56 To 9
        SetMemory(0x663030, Add, -46),# units:Portrait  index:84    from 55 To 9
        SetMemory(0x663054, Add, -5832704),# units:Portrait  index:103    from 98 To 9
        SetMemory(0x663078, Add, -8),# units:Portrait  index:120    from 17 To 9
        SetMemory(0x6630A4, Add, -1900544),# units:Portrait  index:143    from 38 To 9
        SetMemory(0x6630A8, Add, -29),# units:Portrait  index:144    from 38 To 9
        SetMemory(0x6630A8, Add, -1900544),# units:Portrait  index:145    from 38 To 9
        SetMemory(0x6630C4, Add, -51),# units:Portrait  index:158    from 60 To 9
        SetMemory(0x6630C4, Add, -3342336),# units:Portrait  index:159    from 60 To 9
        SetMemory(0x6630C8, Add, -3342336),# units:Portrait  index:161    from 60 To 9
        SetMemory(0x6630CC, Add, -51),# units:Portrait  index:162    from 60 To 9
        SetMemory(0x6630CC, Add, -3342336),# units:Portrait  index:163    from 60 To 9
        SetMemory(0x6630D0, Add, -51),# units:Portrait  index:164    from 60 To 9
        SetMemory(0x6630D0, Add, -3342336),# units:Portrait  index:165    from 60 To 9
        SetMemory(0x6630D4, Add, -51),# units:Portrait  index:166    from 60 To 9
        SetMemory(0x6630D4, Add, -3342336),# units:Portrait  index:167    from 60 To 9
        SetMemory(0x6630D8, Add, -32),# units:Portrait  index:168    from 41 To 9
        SetMemory(0x6630D8, Add, -3342336),# units:Portrait  index:169    from 60 To 9
        SetMemory(0x6630DC, Add, -51),# units:Portrait  index:170    from 60 To 9
        SetMemory(0x6630DC, Add, -3342336),# units:Portrait  index:171    from 60 To 9
        SetMemory(0x6630E0, Add, -51),# units:Portrait  index:172    from 60 To 9
        SetMemory(0x6630E0, Add, -3211264),# units:Portrait  index:173    from 58 To 9
        SetMemory(0x6637C0, Add, 150994944),# units:Staredit Group Flags  index:35    from 1 To 10
        SetMemory(0x6637C4, Add, 8),# units:Staredit Group Flags  index:36    from 1 To 9
        SetMemory(0x6637D8, Add, 134217728),# units:Staredit Group Flags  index:59    from 1 To 9
        SetMemory(0x6637F4, Add, 2048),# units:Staredit Group Flags  index:85    from 4 To 12
        SetMemory(0x663800, Add, 2048),# units:Staredit Group Flags  index:97    from 1 To 9
        SetMemory(0x663808, Add, -2621440),# units:Staredit Group Flags  index:106    from 50 To 10
        SetMemory(0x663808, Add, -134217728),# units:Staredit Group Flags  index:107    from 18 To 10
        SetMemory(0x66380C, Add, -8),# units:Staredit Group Flags  index:108    from 18 To 10
        SetMemory(0x66380C, Add, -2048),# units:Staredit Group Flags  index:109    from 18 To 10
        SetMemory(0x66380C, Add, -524288),# units:Staredit Group Flags  index:110    from 18 To 10
        SetMemory(0x66380C, Add, -671088640),# units:Staredit Group Flags  index:111    from 50 To 10
        SetMemory(0x663810, Add, -10240),# units:Staredit Group Flags  index:113    from 50 To 10
        SetMemory(0x663810, Add, -2621440),# units:Staredit Group Flags  index:114    from 50 To 10
        SetMemory(0x663810, Add, -134217728),# units:Staredit Group Flags  index:115    from 18 To 10
        SetMemory(0x663814, Add, -8),# units:Staredit Group Flags  index:116    from 18 To 10
        SetMemory(0x663814, Add, -2048),# units:Staredit Group Flags  index:117    from 18 To 10
        SetMemory(0x663814, Add, -524288),# units:Staredit Group Flags  index:118    from 18 To 10
        SetMemory(0x663814, Add, -134217728),# units:Staredit Group Flags  index:119    from 18 To 10
        SetMemory(0x663818, Add, -8),# units:Staredit Group Flags  index:120    from 18 To 10
        SetMemory(0x663818, Add, -2048),# units:Staredit Group Flags  index:121    from 18 To 10
        SetMemory(0x663818, Add, -524288),# units:Staredit Group Flags  index:122    from 18 To 10
        SetMemory(0x663818, Add, -134217728),# units:Staredit Group Flags  index:123    from 18 To 10
        SetMemory(0x66381C, Add, -8),# units:Staredit Group Flags  index:124    from 18 To 10
        SetMemory(0x66381C, Add, -2048),# units:Staredit Group Flags  index:125    from 18 To 10
        SetMemory(0x66381C, Add, -524288),# units:Staredit Group Flags  index:126    from 18 To 10
        SetMemory(0x66381C, Add, -134217728),# units:Staredit Group Flags  index:127    from 18 To 10
        SetMemory(0x663820, Add, 8),# units:Staredit Group Flags  index:128    from 128 To 136
        SetMemory(0x663820, Add, 2048),# units:Staredit Group Flags  index:129    from 128 To 136
        SetMemory(0x663820, Add, -2621440),# units:Staredit Group Flags  index:130    from 49 To 9
        SetMemory(0x663820, Add, -671088640),# units:Staredit Group Flags  index:131    from 49 To 9
        SetMemory(0x663824, Add, -40),# units:Staredit Group Flags  index:132    from 49 To 9
        SetMemory(0x663824, Add, -10240),# units:Staredit Group Flags  index:133    from 49 To 9
        SetMemory(0x663824, Add, -524288),# units:Staredit Group Flags  index:134    from 17 To 9
        SetMemory(0x663824, Add, -134217728),# units:Staredit Group Flags  index:135    from 17 To 9
        SetMemory(0x663828, Add, -8),# units:Staredit Group Flags  index:136    from 17 To 9
        SetMemory(0x663828, Add, -2048),# units:Staredit Group Flags  index:137    from 17 To 9
        SetMemory(0x663828, Add, -524288),# units:Staredit Group Flags  index:138    from 17 To 9
        SetMemory(0x663828, Add, -134217728),# units:Staredit Group Flags  index:139    from 17 To 9
        SetMemory(0x66382C, Add, -8),# units:Staredit Group Flags  index:140    from 17 To 9
        SetMemory(0x66382C, Add, -2048),# units:Staredit Group Flags  index:141    from 17 To 9
        SetMemory(0x66382C, Add, -524288),# units:Staredit Group Flags  index:142    from 17 To 9
        SetMemory(0x66382C, Add, -134217728),# units:Staredit Group Flags  index:143    from 17 To 9
        SetMemory(0x663830, Add, -8),# units:Staredit Group Flags  index:144    from 17 To 9
        SetMemory(0x663830, Add, -1792),# units:Staredit Group Flags  index:145    from 17 To 10
        SetMemory(0x663830, Add, -524288),# units:Staredit Group Flags  index:146    from 17 To 9
        SetMemory(0x663830, Add, -134217728),# units:Staredit Group Flags  index:147    from 17 To 9
        SetMemory(0x663834, Add, -8),# units:Staredit Group Flags  index:148    from 17 To 9
        SetMemory(0x663834, Add, -2048),# units:Staredit Group Flags  index:149    from 17 To 9
        SetMemory(0x663834, Add, -524288),# units:Staredit Group Flags  index:150    from 17 To 9
        SetMemory(0x663834, Add, -134217728),# units:Staredit Group Flags  index:151    from 17 To 9
        SetMemory(0x663838, Add, -8),# units:Staredit Group Flags  index:152    from 17 To 9
        SetMemory(0x663838, Add, -2048),# units:Staredit Group Flags  index:153    from 17 To 9
        SetMemory(0x663838, Add, -2621440),# units:Staredit Group Flags  index:154    from 52 To 12
        SetMemory(0x663838, Add, -671088640),# units:Staredit Group Flags  index:155    from 52 To 12
        SetMemory(0x66383C, Add, -8),# units:Staredit Group Flags  index:156    from 20 To 12
        SetMemory(0x66383C, Add, -2048),# units:Staredit Group Flags  index:157    from 20 To 12
        SetMemory(0x66383C, Add, -524288),# units:Staredit Group Flags  index:158    from 20 To 12
        SetMemory(0x66383C, Add, -134217728),# units:Staredit Group Flags  index:159    from 20 To 12
        SetMemory(0x663840, Add, -40),# units:Staredit Group Flags  index:160    from 52 To 12
        SetMemory(0x663840, Add, -2048),# units:Staredit Group Flags  index:161    from 20 To 12
        SetMemory(0x663840, Add, -524288),# units:Staredit Group Flags  index:162    from 20 To 12
        SetMemory(0x663840, Add, -134217728),# units:Staredit Group Flags  index:163    from 20 To 12
        SetMemory(0x663844, Add, -8),# units:Staredit Group Flags  index:164    from 20 To 12
        SetMemory(0x663844, Add, -2048),# units:Staredit Group Flags  index:165    from 20 To 12
        SetMemory(0x663844, Add, -524288),# units:Staredit Group Flags  index:166    from 20 To 12
        SetMemory(0x663844, Add, -671088640),# units:Staredit Group Flags  index:167    from 52 To 12
        SetMemory(0x663848, Add, -8),# units:Staredit Group Flags  index:168    from 20 To 12
        SetMemory(0x663848, Add, -2048),# units:Staredit Group Flags  index:169    from 20 To 12
        SetMemory(0x663848, Add, -524288),# units:Staredit Group Flags  index:170    from 20 To 12
        SetMemory(0x663848, Add, -134217728),# units:Staredit Group Flags  index:171    from 20 To 12
        SetMemory(0x66384C, Add, -8),# units:Staredit Group Flags  index:172    from 20 To 12
        SetMemory(0x66384C, Add, -2048),# units:Staredit Group Flags  index:173    from 20 To 12
        SetMemory(0x66154C, Add, 29556736),# units:Staredit Availability Flags  index:27    from 4 To 455
        SetMemory(0x66155C, Add, 30343168),# units:Staredit Availability Flags  index:35    from 0 To 463
        SetMemory(0x661560, Add, 463),# units:Staredit Availability Flags  index:36    from 0 To 463
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
        SetMemory(0x66158C, Add, 30343168),# units:Staredit Availability Flags  index:59    from 0 To 463
        SetMemory(0x661594, Add, -33030144),# units:Staredit Availability Flags  index:63    from 967 To 463
        SetMemory(0x6615A0, Add, 8),# units:Staredit Availability Flags  index:68    from 455 To 463
        SetMemory(0x6615A8, Add, 196608),# units:Staredit Availability Flags  index:73    from 452 To 455
        SetMemory(0x6615AC, Add, 8),# units:Staredit Availability Flags  index:74    from 455 To 463
        SetMemory(0x6615AC, Add, 524288),# units:Staredit Availability Flags  index:75    from 455 To 463
        SetMemory(0x6615B0, Add, 8),# units:Staredit Availability Flags  index:76    from 455 To 463
        SetMemory(0x6615B0, Add, 524288),# units:Staredit Availability Flags  index:77    from 455 To 463
        SetMemory(0x6615B4, Add, 8),# units:Staredit Availability Flags  index:78    from 455 To 463
        SetMemory(0x6615B4, Add, 524288),# units:Staredit Availability Flags  index:79    from 455 To 463
        SetMemory(0x6615C0, Add, 196608),# units:Staredit Availability Flags  index:85    from 452 To 455
        SetMemory(0x6615C4, Add, 8),# units:Staredit Availability Flags  index:86    from 455 To 463
        SetMemory(0x6615C4, Add, 30081024),# units:Staredit Availability Flags  index:87    from 4 To 463
        SetMemory(0x6615C8, Add, -504),# units:Staredit Availability Flags  index:88    from 967 To 463
        SetMemory(0x6615C8, Add, 589824),# units:Staredit Availability Flags  index:89    from 454 To 463
        SetMemory(0x6615CC, Add, 9),# units:Staredit Availability Flags  index:90    from 454 To 463
        SetMemory(0x6615CC, Add, 30343168),# units:Staredit Availability Flags  index:91    from 0 To 463
        SetMemory(0x6615D0, Add, 463),# units:Staredit Availability Flags  index:92    from 0 To 463
        SetMemory(0x6615D0, Add, -32964608),# units:Staredit Availability Flags  index:93    from 966 To 463
        SetMemory(0x6615D4, Add, -503),# units:Staredit Availability Flags  index:94    from 966 To 463
        SetMemory(0x6615D4, Add, 589824),# units:Staredit Availability Flags  index:95    from 454 To 463
        SetMemory(0x6615D8, Add, -503),# units:Staredit Availability Flags  index:96    from 966 To 463
        SetMemory(0x6615D8, Add, 30343168),# units:Staredit Availability Flags  index:97    from 0 To 463
        SetMemory(0x6615DC, Add, 459),# units:Staredit Availability Flags  index:98    from 4 To 463
        SetMemory(0x6615DC, Add, -33030144),# units:Staredit Availability Flags  index:99    from 967 To 463
        SetMemory(0x6615E0, Add, -504),# units:Staredit Availability Flags  index:100    from 967 To 463
        SetMemory(0x6615E4, Add, 459),# units:Staredit Availability Flags  index:102    from 4 To 463
        SetMemory(0x6615E4, Add, -33030144),# units:Staredit Availability Flags  index:103    from 967 To 463
        SetMemory(0x6615E8, Add, -504),# units:Staredit Availability Flags  index:104    from 967 To 463
        SetMemory(0x661604, Add, 30343168),# units:Staredit Availability Flags  index:119    from 0 To 463
        SetMemory(0x661608, Add, 30343168),# units:Staredit Availability Flags  index:121    from 0 To 463
        SetMemory(0x661614, Add, 520),# units:Staredit Availability Flags  index:126    from 455 To 975
        SetMemory(0x661614, Add, 34078720),# units:Staredit Availability Flags  index:127    from 455 To 975
        SetMemory(0x661618, Add, -520),# units:Staredit Availability Flags  index:128    from 855 To 335
        SetMemory(0x661618, Add, -34078720),# units:Staredit Availability Flags  index:129    from 855 To 335
        SetMemory(0x66161C, Add, 8),# units:Staredit Availability Flags  index:130    from 455 To 463
        SetMemory(0x661638, Add, 30343168),# units:Staredit Availability Flags  index:145    from 0 To 463
        SetMemory(0x661644, Add, 8),# units:Staredit Availability Flags  index:150    from 455 To 463
        SetMemory(0x661644, Add, 524288),# units:Staredit Availability Flags  index:151    from 455 To 463
        SetMemory(0x661648, Add, 8),# units:Staredit Availability Flags  index:152    from 455 To 463
        SetMemory(0x661648, Add, 30343168),# units:Staredit Availability Flags  index:153    from 0 To 463
        SetMemory(0x661654, Add, 463),# units:Staredit Availability Flags  index:158    from 0 To 463
        SetMemory(0x661658, Add, 30343168),# units:Staredit Availability Flags  index:161    from 0 To 463
        SetMemory(0x661668, Add, 8),# units:Staredit Availability Flags  index:168    from 455 To 463
        SetMemory(0x661670, Add, 524288),# units:Staredit Availability Flags  index:173    from 455 To 463
        SetMemory(0x6C9F94, Add, 1647),# flingy:Speed  index:39    from 853 To 2500
        SetMemory(0x6C9FB8, Add, 1999),# flingy:Speed  index:48    from 1 To 2000
        SetMemory(0x6CA014, Add, 999),# flingy:Speed  index:71    from 1 To 1000
        SetMemory(0x6CA02C, Add, 1999),# flingy:Speed  index:77    from 1 To 2000
        SetMemory(0x6C9CD8, Add, 1999),# flingy:Acceleration  index:48    from 1 To 2000
        SetMemory(0x6C9D04, Add, 65470464),# flingy:Acceleration  index:71    from 1 To 1000
        SetMemory(0x6C9D10, Add, 65470464),# flingy:Acceleration  index:77    from 1 To 1000
        SetMemory(0x6C9E64, Add, 2684354560),# flingy:Turn Radius  index:71    from 40 To 200
        SetMemory(0x6C9E6C, Add, 53760),# flingy:Turn Radius  index:77    from 40 To 250
        SetMemory(0x6C9858, Add, 2),# flingy:Movement Control  index:0    from 0 To 2
        SetMemory(0x6C989C, Add, -33554432),# flingy:Movement Control  index:71    from 2 To 0
        SetMemory(0x6C98A4, Add, -512),# flingy:Movement Control  index:77    from 2 To 0
    ])

