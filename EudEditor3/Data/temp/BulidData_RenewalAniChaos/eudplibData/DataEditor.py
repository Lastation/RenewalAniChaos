from eudplib import *


def onPluginStart():
    DoActions([  # Basic DatFile Actions
        SetMemory(0x664500, Add, -33554432),# units:Graphics  index:11    from 72 To 70
        SetMemory(0x664518, Add, -9437184),# units:Graphics  index:34    from 189 To 45
        SetMemory(0x664520, Add, 768),# units:Graphics  index:41    from 5 To 8
        SetMemory(0x664534, Add, -9437184),# units:Graphics  index:62    from 185 To 41
        SetMemory(0x66453C, Add, -1280),# units:Graphics  index:69    from 44 To 39
        SetMemory(0x664558, Add, -10092544),# units:Graphics  index:98    from 191 To 37
        SetMemory(0x664564, Add, 7936),# units:Graphics  index:109    from 95 To 126
        SetMemory(0x664568, Add, 419430400),# units:Graphics  index:115    from 96 To 121
        SetMemory(0x664578, Add, -19968),# units:Graphics  index:129    from 208 To 130
        SetMemory(0x6645A4, Add, 38400),# units:Graphics  index:173    from 58 To 208
        SetMemory(0x661264, Add, -330),# units:Construction Animation  index:109    from 330 To 0
        SetMemory(0x66127C, Add, -327),# units:Construction Animation  index:115    from 327 To 0
        SetMemory(0x660640, Add, -2097152),# units:Unit Direction  index:82    from 32 To 0
        SetMemory(0x66065C, Add, 2048),# units:Unit Direction  index:109    from 0 To 8
        SetMemory(0x6647B0, Add, 256),# units:Shield Enable  index:1    from 0 To 1
        SetMemory(0x6647B0, Add, 65536),# units:Shield Enable  index:2    from 0 To 1
        SetMemory(0x6647B8, Add, 0),# units:Shield Enable  index:10    from 0 To 0
        SetMemory(0x6647C0, Add, 1),# units:Shield Enable  index:16    from 0 To 1
        SetMemory(0x6647D0, Add, 65536),# units:Shield Enable  index:34    from 0 To 1
        SetMemory(0x6647D8, Add, 1),# units:Shield Enable  index:40    from 0 To 1
        SetMemory(0x6647E0, Add, 16777216),# units:Shield Enable  index:51    from 0 To 1
        SetMemory(0x6647E4, Add, 256),# units:Shield Enable  index:53    from 0 To 1
        SetMemory(0x6647E4, Add, 65536),# units:Shield Enable  index:54    from 0 To 1
        SetMemory(0x664810, Add, 16777216),# units:Shield Enable  index:99    from 0 To 1
        SetMemory(0x664820, Add, 16777216),# units:Shield Enable  index:115    from 0 To 1
        SetMemory(0x664830, Add, 65536),# units:Shield Enable  index:130    from 0 To 1
        SetMemory(0x664858, Add, 1),# units:Shield Enable  index:168    from 0 To 1
        SetMemory(0x66485C, Add, 16777216),# units:Shield Enable  index:175    from 0 To 1
        SetMemory(0x664878, Add, 1),# units:Shield Enable  index:200    from 0 To 1
        SetMemory(0x660E44, Add, 0),# units:Shield Amount  index:34    from 100 To 100
        SetMemory(0x660EAC, Add, 635699200),# units:Shield Amount  index:87    from 300 To 10000
        SetMemory(0x660EE4, Add, 19660800),# units:Shield Amount  index:115    from 100 To 400
        SetMemory(0x662354, Add, 615680),# units:Hit Points  index:1    from 11520 To 627200
        SetMemory(0x662358, Add, -5120),# units:Hit Points  index:2    from 71680 To 66560
        SetMemory(0x662390, Add, 151040),# units:Hit Points  index:16    from 476160 To 627200
        SetMemory(0x6623A4, Add, 499200),# units:Hit Points  index:21    from 128000 To 627200
        SetMemory(0x6623D8, Add, 611840),# units:Hit Points  index:34    from 15360 To 627200
        SetMemory(0x6623F0, Add, -5120),# units:Hit Points  index:40    from 81920 To 76800
        SetMemory(0x66241C, Add, 151040),# units:Hit Points  index:51    from 476160 To 627200
        SetMemory(0x662424, Add, 151040),# units:Hit Points  index:53    from 476160 To 627200
        SetMemory(0x662428, Add, 151040),# units:Hit Points  index:54    from 476160 To 627200
        SetMemory(0x662450, Add, 151040),# units:Hit Points  index:64    from 476160 To 627200
        SetMemory(0x662478, Add, 151040),# units:Hit Points  index:74    from 476160 To 627200
        SetMemory(0x662484, Add, 151040),# units:Hit Points  index:77    from 476160 To 627200
        SetMemory(0x6624AC, Add, 17899520),# units:Hit Points  index:87    from 20480 To 17920000
        SetMemory(0x6624DC, Add, 166400),# units:Hit Points  index:99    from 460800 To 627200
        SetMemory(0x662504, Add, 25472000),# units:Hit Points  index:109    from 51200 To 25523200
        SetMemory(0x66251C, Add, -25600),# units:Hit Points  index:115    from 128000 To 102400
        SetMemory(0x6631B0, Add, -131072),# units:Elevation Level  index:98    from 18 To 16
        SetMemory(0x6631C0, Add, 234881024),# units:Elevation Level  index:115    from 4 To 18
        SetMemory(0x6631C4, Add, 786432),# units:Elevation Level  index:118    from 4 To 16
        SetMemory(0x6631C8, Add, 15),# units:Elevation Level  index:120    from 4 To 19
        SetMemory(0x661034, Add, 50432),# units:Unknown (old Movement)  index:109    from 0 To 197
        SetMemory(0x661038, Add, 3305111552),# units:Unknown (old Movement)  index:115    from 0 To 197
        SetMemory(0x663DD0, Add, -768),# units:Rank/Sublabel  index:1    from 5 To 2
        SetMemory(0x663DD0, Add, -393216),# units:Rank/Sublabel  index:2    from 6 To 0
        SetMemory(0x663DD0, Add, -83886080),# units:Rank/Sublabel  index:3    from 7 To 2
        SetMemory(0x663DD4, Add, -1536),# units:Rank/Sublabel  index:5    from 8 To 2
        SetMemory(0x663DD8, Add, -8),# units:Rank/Sublabel  index:8    from 10 To 2
        SetMemory(0x663DD8, Add, -2304),# units:Rank/Sublabel  index:9    from 11 To 2
        SetMemory(0x663DDC, Add, -13),# units:Rank/Sublabel  index:12    from 15 To 2
        SetMemory(0x663DE0, Add, -17),# units:Rank/Sublabel  index:16    from 18 To 1
        SetMemory(0x663DE0, Add, -2816),# units:Rank/Sublabel  index:17    from 13 To 2
        SetMemory(0x663DE4, Add, -15),# units:Rank/Sublabel  index:20    from 17 To 2
        SetMemory(0x663DE4, Add, -3072),# units:Rank/Sublabel  index:21    from 14 To 2
        SetMemory(0x663DE4, Add, -851968),# units:Rank/Sublabel  index:22    from 15 To 2
        SetMemory(0x663DE4, Add, -285212672),# units:Rank/Sublabel  index:23    from 19 To 2
        SetMemory(0x663DE8, Add, -4352),# units:Rank/Sublabel  index:25    from 19 To 2
        SetMemory(0x663DE8, Add, -318767104),# units:Rank/Sublabel  index:27    from 21 To 2
        SetMemory(0x663DEC, Add, -18),# units:Rank/Sublabel  index:28    from 20 To 2
        SetMemory(0x663DEC, Add, -4864),# units:Rank/Sublabel  index:29    from 21 To 2
        SetMemory(0x663DEC, Add, -393216),# units:Rank/Sublabel  index:30    from 8 To 2
        SetMemory(0x663DF0, Add, -2),# units:Rank/Sublabel  index:32    from 4 To 2
        SetMemory(0x663DF0, Add, 851968),# units:Rank/Sublabel  index:34    from 3 To 16
        SetMemory(0x663DF4, Add, -768),# units:Rank/Sublabel  index:37    from 5 To 2
        SetMemory(0x663DF4, Add, -458752),# units:Rank/Sublabel  index:38    from 9 To 2
        SetMemory(0x663DF4, Add, -184549376),# units:Rank/Sublabel  index:39    from 14 To 3
        SetMemory(0x663DF8, Add, -3),# units:Rank/Sublabel  index:40    from 3 To 0
        SetMemory(0x663DF8, Add, -512),# units:Rank/Sublabel  index:41    from 4 To 2
        SetMemory(0x663DF8, Add, -134217728),# units:Rank/Sublabel  index:43    from 10 To 2
        SetMemory(0x663DFC, Add, -9),# units:Rank/Sublabel  index:44    from 11 To 2
        SetMemory(0x663E00, Add, -13),# units:Rank/Sublabel  index:48    from 15 To 2
        SetMemory(0x663E00, Add, -251658240),# units:Rank/Sublabel  index:51    from 16 To 1
        SetMemory(0x663E04, Add, -3584),# units:Rank/Sublabel  index:53    from 15 To 1
        SetMemory(0x663E04, Add, -917504),# units:Rank/Sublabel  index:54    from 15 To 1
        SetMemory(0x663E04, Add, -218103808),# units:Rank/Sublabel  index:55    from 15 To 2
        SetMemory(0x663E08, Add, -13),# units:Rank/Sublabel  index:56    from 15 To 2
        SetMemory(0x663E10, Add, -256),# units:Rank/Sublabel  index:65    from 3 To 2
        SetMemory(0x663E10, Add, -131072),# units:Rank/Sublabel  index:66    from 4 To 2
        SetMemory(0x663E10, Add, -67108864),# units:Rank/Sublabel  index:67    from 6 To 2
        SetMemory(0x663E14, Add, -7),# units:Rank/Sublabel  index:68    from 9 To 2
        SetMemory(0x663E18, Add, 256),# units:Rank/Sublabel  index:73    from 1 To 2
        SetMemory(0x663E18, Add, -720896),# units:Rank/Sublabel  index:74    from 12 To 1
        SetMemory(0x663E18, Add, -218103808),# units:Rank/Sublabel  index:75    from 15 To 2
        SetMemory(0x663E1C, Add, -3072),# units:Rank/Sublabel  index:77    from 13 To 1
        SetMemory(0x663E1C, Add, -218103808),# units:Rank/Sublabel  index:79    from 16 To 3
        SetMemory(0x663E20, Add, -10),# units:Rank/Sublabel  index:80    from 12 To 2
        SetMemory(0x663E20, Add, -983040),# units:Rank/Sublabel  index:82    from 17 To 2
        SetMemory(0x663E24, Add, -655360),# units:Rank/Sublabel  index:86    from 12 To 2
        SetMemory(0x663E28, Add, -10),# units:Rank/Sublabel  index:88    from 12 To 2
        SetMemory(0x663E30, Add, -393216),# units:Rank/Sublabel  index:98    from 8 To 2
        SetMemory(0x663E30, Add, -285212672),# units:Rank/Sublabel  index:99    from 18 To 1
        SetMemory(0x663E40, Add, 33554432),# units:Rank/Sublabel  index:115    from 0 To 2
        SetMemory(0x663E50, Add, 262144),# units:Rank/Sublabel  index:130    from 0 To 4
        SetMemory(0x663E60, Add, 3),# units:Rank/Sublabel  index:144    from 0 To 3
        SetMemory(0x663E70, Add, 196608),# units:Rank/Sublabel  index:162    from 0 To 3
        SetMemory(0x663E7C, Add, 512),# units:Rank/Sublabel  index:173    from 0 To 2
        SetMemory(0x662EB0, Add, 55),# units:Comp AI Idle  index:16    from 2 To 57
        SetMemory(0x662EC0, Add, -7733248),# units:Comp AI Idle  index:34    from 175 To 57
        SetMemory(0x662ECC, Add, 1761607680),# units:Comp AI Idle  index:47    from 2 To 107
        SetMemory(0x662ED0, Add, 922746880),# units:Comp AI Idle  index:51    from 2 To 57
        SetMemory(0x662ED4, Add, 14080),# units:Comp AI Idle  index:53    from 2 To 57
        SetMemory(0x662ED4, Add, 3604480),# units:Comp AI Idle  index:54    from 2 To 57
        SetMemory(0x662EE0, Add, 55),# units:Comp AI Idle  index:64    from 2 To 57
        SetMemory(0x662EE8, Add, 3604480),# units:Comp AI Idle  index:74    from 2 To 57
        SetMemory(0x662EEC, Add, 14080),# units:Comp AI Idle  index:77    from 2 To 57
        SetMemory(0x662EF4, Add, -8388608),# units:Comp AI Idle  index:86    from 130 To 2
        SetMemory(0x662EF4, Add, 922746880),# units:Comp AI Idle  index:87    from 2 To 57
        SetMemory(0x662F00, Add, 922746880),# units:Comp AI Idle  index:99    from 2 To 57
        SetMemory(0x662F0C, Add, -15104),# units:Comp AI Idle  index:109    from 156 To 97
        SetMemory(0x662F10, Add, -2583691264),# units:Comp AI Idle  index:115    from 156 To 2
        SetMemory(0x662F14, Add, -8716288),# units:Comp AI Idle  index:118    from 156 To 23
        SetMemory(0x662F18, Add, -133),# units:Comp AI Idle  index:120    from 156 To 23
        SetMemory(0x662F20, Add, -18944),# units:Comp AI Idle  index:129    from 97 To 23
        SetMemory(0x662F30, Add, -83),# units:Comp AI Idle  index:144    from 101 To 18
        SetMemory(0x662278, Add, 55),# units:Human AI Idle  index:16    from 2 To 57
        SetMemory(0x662288, Add, -7733248),# units:Human AI Idle  index:34    from 175 To 57
        SetMemory(0x662294, Add, 1761607680),# units:Human AI Idle  index:47    from 2 To 107
        SetMemory(0x662298, Add, 922746880),# units:Human AI Idle  index:51    from 2 To 57
        SetMemory(0x66229C, Add, 14080),# units:Human AI Idle  index:53    from 2 To 57
        SetMemory(0x66229C, Add, 3604480),# units:Human AI Idle  index:54    from 2 To 57
        SetMemory(0x6622A8, Add, 55),# units:Human AI Idle  index:64    from 2 To 57
        SetMemory(0x6622B0, Add, 3604480),# units:Human AI Idle  index:74    from 2 To 57
        SetMemory(0x6622B4, Add, 14080),# units:Human AI Idle  index:77    from 2 To 57
        SetMemory(0x6622BC, Add, -8388608),# units:Human AI Idle  index:86    from 130 To 2
        SetMemory(0x6622BC, Add, 922746880),# units:Human AI Idle  index:87    from 2 To 57
        SetMemory(0x6622C8, Add, 922746880),# units:Human AI Idle  index:99    from 2 To 57
        SetMemory(0x6622D4, Add, 18944),# units:Human AI Idle  index:109    from 23 To 97
        SetMemory(0x6622D8, Add, -352321536),# units:Human AI Idle  index:115    from 23 To 2
        SetMemory(0x6622E8, Add, -18944),# units:Human AI Idle  index:129    from 97 To 23
        SetMemory(0x6622F8, Add, -83),# units:Human AI Idle  index:144    from 101 To 18
        SetMemory(0x6648A8, Add, 55),# units:Return to Idle  index:16    from 2 To 57
        SetMemory(0x6648B8, Add, -7733248),# units:Return to Idle  index:34    from 175 To 57
        SetMemory(0x6648C4, Add, 1761607680),# units:Return to Idle  index:47    from 2 To 107
        SetMemory(0x6648C8, Add, 922746880),# units:Return to Idle  index:51    from 2 To 57
        SetMemory(0x6648CC, Add, 14080),# units:Return to Idle  index:53    from 2 To 57
        SetMemory(0x6648CC, Add, 3604480),# units:Return to Idle  index:54    from 2 To 57
        SetMemory(0x6648D8, Add, 55),# units:Return to Idle  index:64    from 2 To 57
        SetMemory(0x6648E0, Add, 3604480),# units:Return to Idle  index:74    from 2 To 57
        SetMemory(0x6648E4, Add, 14080),# units:Return to Idle  index:77    from 2 To 57
        SetMemory(0x6648EC, Add, 922746880),# units:Return to Idle  index:87    from 2 To 57
        SetMemory(0x6648F8, Add, 922746880),# units:Return to Idle  index:99    from 2 To 57
        SetMemory(0x664904, Add, 18944),# units:Return to Idle  index:109    from 23 To 97
        SetMemory(0x664908, Add, -352321536),# units:Return to Idle  index:115    from 23 To 2
        SetMemory(0x664918, Add, -18944),# units:Return to Idle  index:129    from 97 To 23
        SetMemory(0x663340, Add, -10813440),# units:Attack Unit  index:34    from 175 To 10
        SetMemory(0x663390, Add, -218103808),# units:Attack Unit  index:115    from 23 To 10
        SetMemory(0x663A70, Add, -11337728),# units:Attack Move  index:34    from 175 To 2
        SetMemory(0x663AC0, Add, -352321536),# units:Attack Move  index:115    from 23 To 2
        SetMemory(0x6636D0, Add, 16777216),# units:Ground Weapon  index:27    from 21 To 22
        SetMemory(0x6636D4, Add, 768),# units:Ground Weapon  index:29    from 21 To 24
        SetMemory(0x6636D8, Add, -8323072),# units:Ground Weapon  index:34    from 130 To 3
        SetMemory(0x6636E4, Add, -5177344),# units:Ground Weapon  index:46    from 130 To 51
        SetMemory(0x6636F8, Add, -1040187392),# units:Ground Weapon  index:67    from 130 To 68
        SetMemory(0x663718, Add, -3473408),# units:Ground Weapon  index:98    from 130 To 77
        SetMemory(0x663728, Add, -956301312),# units:Ground Weapon  index:115    from 130 To 73
        SetMemory(0x663748, Add, -78),# units:Ground Weapon  index:144    from 130 To 52
        SetMemory(0x664600, Add, 65536),# units:Max Ground Hits  index:34    from 0 To 1
        SetMemory(0x664640, Add, 65536),# units:Max Ground Hits  index:98    from 0 To 1
        SetMemory(0x664650, Add, 16777216),# units:Max Ground Hits  index:115    from 0 To 1
        SetMemory(0x6616E4, Add, 122),# units:Air Weapon  index:4    from 8 To 130
        SetMemory(0x6616E8, Add, 1),# units:Air Weapon  index:8    from 15 To 16
        SetMemory(0x6616EC, Add, -1),# units:Air Weapon  index:12    from 20 To 19
        SetMemory(0x6616F4, Add, 256),# units:Air Weapon  index:21    from 17 To 18
        SetMemory(0x6616F8, Add, 1811939328),# units:Air Weapon  index:27    from 22 To 130
        SetMemory(0x6616FC, Add, 106),# units:Air Weapon  index:28    from 24 To 130
        SetMemory(0x6616FC, Add, 27648),# units:Air Weapon  index:29    from 22 To 130
        SetMemory(0x661700, Add, -8323072),# units:Air Weapon  index:34    from 130 To 3
        SetMemory(0x66170C, Add, 1258291200),# units:Air Weapon  index:47    from 55 To 130
        SetMemory(0x66171C, Add, 1703936),# units:Air Weapon  index:62    from 104 To 130
        SetMemory(0x661730, Add, -1),# units:Air Weapon  index:80    from 76 To 75
        SetMemory(0x661740, Add, -1507328),# units:Air Weapon  index:98    from 100 To 77
        SetMemory(0x661750, Add, -956301312),# units:Air Weapon  index:115    from 130 To 73
        SetMemory(0x65FC1C, Add, -1),# units:Max Air Hits  index:4    from 1 To 0
        SetMemory(0x65FC30, Add, -16777216),# units:Max Air Hits  index:27    from 1 To 0
        SetMemory(0x65FC34, Add, -1),# units:Max Air Hits  index:28    from 1 To 0
        SetMemory(0x65FC34, Add, -256),# units:Max Air Hits  index:29    from 1 To 0
        SetMemory(0x65FC54, Add, -65536),# units:Max Air Hits  index:62    from 1 To 0
        SetMemory(0x65FC88, Add, 16777216),# units:Max Air Hits  index:115    from 0 To 1
        SetMemory(0x660198, Add, 196608),# units:AI Internal  index:34    from 0 To 3
        SetMemory(0x6601A0, Add, -768),# units:AI Internal  index:41    from 3 To 0
        SetMemory(0x664094, Add, 4),# units:Special Ability Flags  index:5    from 1509949440 To 1509949444
        SetMemory(0x6640C0, Add, -2163072),# units:Special Ability Flags  index:16    from 404816448 To 402653376
        SetMemory(0x6640CC, Add, 4),# units:Special Ability Flags  index:19    from 1476395072 To 1476395076
        SetMemory(0x6640E4, Add, 4),# units:Special Ability Flags  index:25    from 1107296320 To 1107296324
        SetMemory(0x6640F8, Add, 4),# units:Special Ability Flags  index:30    from 1107296256 To 1107296260
        SetMemory(0x664108, Add, 192),# units:Special Ability Flags  index:34    from 404815872 To 404816064
        SetMemory(0x664124, Add, -8),# units:Special Ability Flags  index:41    from 403767432 To 403767424
        SetMemory(0x664138, Add, 4),# units:Special Ability Flags  index:46    from 439419008 To 439419012
        SetMemory(0x66414C, Add, -2163200),# units:Special Ability Flags  index:51    from 404816576 To 402653376
        SetMemory(0x664150, Add, 4),# units:Special Ability Flags  index:52    from 439419072 To 439419076
        SetMemory(0x664154, Add, -1114112),# units:Special Ability Flags  index:53    from 403767488 To 402653376
        SetMemory(0x664158, Add, -1115136),# units:Special Ability Flags  index:54    from 403768512 To 402653376
        SetMemory(0x664174, Add, 4),# units:Special Ability Flags  index:61    from 406913024 To 406913028
        SetMemory(0x66417C, Add, 4),# units:Special Ability Flags  index:63    from 471859456 To 471859460
        SetMemory(0x664180, Add, -1073758024),# units:Special Ability Flags  index:64    from 1476411400 To 402653376
        SetMemory(0x664188, Add, 4),# units:Special Ability Flags  index:66    from 1509949440 To 1509949444
        SetMemory(0x6641A4, Add, 536870912),# units:Special Ability Flags  index:73    from 1476395012 To 2013265924
        SetMemory(0x6641A8, Add, -4259648),# units:Special Ability Flags  index:74    from 406913024 To 402653376
        SetMemory(0x6641AC, Add, 4),# units:Special Ability Flags  index:75    from 406913088 To 406913092
        SetMemory(0x6641B0, Add, 4),# units:Special Ability Flags  index:76    from 469762368 To 469762372
        SetMemory(0x6641B4, Add, -65408),# units:Special Ability Flags  index:77    from 402718784 To 402653376
        SetMemory(0x6641B8, Add, 4),# units:Special Ability Flags  index:78    from 1509949504 To 1509949508
        SetMemory(0x6641DC, Add, 128),# units:Special Ability Flags  index:87    from 404815936 To 404816064
        SetMemory(0x664208, Add, -64),# units:Special Ability Flags  index:98    from 1512046660 To 1512046596
        SetMemory(0x66420C, Add, -2163072),# units:Special Ability Flags  index:99    from 404816448 To 402653376
        SetMemory(0x664234, Add, -603977729),# units:Special Ability Flags  index:109    from 1140850689 To 536872960
        SetMemory(0x66424C, Add, 369100865),# units:Special Ability Flags  index:115    from 1140850691 To 1509951556
        SetMemory(0x664258, Add, -603977727),# units:Special Ability Flags  index:118    from 1140850691 To 536872964
        SetMemory(0x664260, Add, -603977727),# units:Special Ability Flags  index:120    from 1140850691 To 536872964
        SetMemory(0x664288, Add, -67108865),# units:Special Ability Flags  index:130    from 67174561 To 65696
        SetMemory(0x6642C0, Add, -131069),# units:Special Ability Flags  index:144    from 352551041 To 352419972
        SetMemory(0x6642EC, Add, -524288),# units:Special Ability Flags  index:155    from 3288858625 To 3288334337
        SetMemory(0x664308, Add, -524288),# units:Special Ability Flags  index:162    from 1409843201 To 1409318913
        SetMemory(0x664334, Add, -67106817),# units:Special Ability Flags  index:173    from 603979777 To 536872960
        SetMemory(0x66433C, Add, 268435456),# units:Special Ability Flags  index:175    from 67108865 To 335544321
        SetMemory(0x662DB8, Add, 256),# units:Target Acquisition Range  index:1    from 7 To 8
        SetMemory(0x662DD8, Add, -196608),# units:Target Acquisition Range  index:34    from 9 To 6
        SetMemory(0x662DDC, Add, 256),# units:Target Acquisition Range  index:37    from 3 To 4
        SetMemory(0x662DE0, Add, 768),# units:Target Acquisition Range  index:41    from 1 To 4
        SetMemory(0x662DF8, Add, 262144),# units:Target Acquisition Range  index:66    from 4 To 8
        SetMemory(0x662DF8, Add, 50331648),# units:Target Acquisition Range  index:67    from 3 To 6
        SetMemory(0x662DFC, Add, 3),# units:Target Acquisition Range  index:68    from 3 To 6
        SetMemory(0x662E00, Add, 83886080),# units:Target Acquisition Range  index:75    from 3 To 8
        SetMemory(0x662E04, Add, 50331648),# units:Target Acquisition Range  index:79    from 3 To 6
        SetMemory(0x662E18, Add, -262144),# units:Target Acquisition Range  index:98    from 9 To 5
        SetMemory(0x662E1C, Add, 2),# units:Target Acquisition Range  index:100    from 6 To 8
        SetMemory(0x662E20, Add, 2),# units:Target Acquisition Range  index:104    from 6 To 8
        SetMemory(0x662E28, Add, 100663296),# units:Target Acquisition Range  index:115    from 0 To 6
        SetMemory(0x663258, Add, 131072),# units:Sight Range  index:34    from 9 To 11
        SetMemory(0x66325C, Add, 256),# units:Sight Range  index:37    from 5 To 6
        SetMemory(0x663260, Add, -256),# units:Sight Range  index:41    from 7 To 6
        SetMemory(0x663280, Add, 50331648),# units:Sight Range  index:75    from 7 To 10
        SetMemory(0x6632A4, Add, -768),# units:Sight Range  index:109    from 8 To 5
        SetMemory(0x6632A8, Add, 33554432),# units:Sight Range  index:115    from 8 To 10
        SetMemory(0x6635E0, Add, 2),# units:Armor Upgrade  index:16    from 0 To 2
        SetMemory(0x6635F0, Add, 131072),# units:Armor Upgrade  index:34    from 0 To 2
        SetMemory(0x6635FC, Add, 939524096),# units:Armor Upgrade  index:47    from 4 To 60
        SetMemory(0x663600, Add, -16777216),# units:Armor Upgrade  index:51    from 3 To 2
        SetMemory(0x663604, Add, -256),# units:Armor Upgrade  index:53    from 3 To 2
        SetMemory(0x663604, Add, -65536),# units:Armor Upgrade  index:54    from 3 To 2
        SetMemory(0x663610, Add, -3),# units:Armor Upgrade  index:64    from 5 To 2
        SetMemory(0x663618, Add, -196608),# units:Armor Upgrade  index:74    from 5 To 2
        SetMemory(0x66361C, Add, -768),# units:Armor Upgrade  index:77    from 5 To 2
        SetMemory(0x663624, Add, -50331648),# units:Armor Upgrade  index:87    from 5 To 2
        SetMemory(0x663630, Add, 33554432),# units:Armor Upgrade  index:99    from 0 To 2
        SetMemory(0x663640, Add, -905969664),# units:Armor Upgrade  index:115    from 60 To 6
        SetMemory(0x6621B4, Add, -256),# units:Unit Size  index:53    from 2 To 1
        SetMemory(0x6621CC, Add, 16777216),# units:Unit Size  index:79    from 1 To 2
        SetMemory(0x6621E0, Add, 65536),# units:Unit Size  index:98    from 2 To 3
        SetMemory(0x6621EC, Add, -768),# units:Unit Size  index:109    from 3 To 0
        SetMemory(0x65FEDC, Add, 4096),# units:Armor  index:21    from 4 To 20
        SetMemory(0x65FEE8, Add, 1245184),# units:Armor  index:34    from 1 To 20
        SetMemory(0x65FF1C, Add, 973078528),# units:Armor  index:87    from 2 To 60
        SetMemory(0x65FF34, Add, -256),# units:Armor  index:109    from 1 To 0
        SetMemory(0x65FF38, Add, 33554432),# units:Armor  index:115    from 1 To 3
        SetMemory(0x6620B8, Add, -65536),# units:Right-click Action  index:34    from 2 To 1
        SetMemory(0x6620C0, Add, -768),# units:Right-click Action  index:41    from 4 To 1
        SetMemory(0x6620C4, Add, 83886080),# units:Right-click Action  index:47    from 1 To 6
        SetMemory(0x6620D8, Add, -3),# units:Right-click Action  index:64    from 4 To 1
        SetMemory(0x6620EC, Add, 0),# units:Right-click Action  index:87    from 1 To 1
        SetMemory(0x662108, Add, 16777216),# units:Right-click Action  index:115    from 0 To 1
        SetMemory(0x662118, Add, 262144),# units:Right-click Action  index:130    from 2 To 6
        SetMemory(0x662004, Add, -999),# units:Ready Sound  index:34    from 999 To 0
        SetMemory(0x662084, Add, -492),# units:Ready Sound  index:98    from 1041 To 549
        SetMemory(0x65FFF4, Add, -1001),# units:What Sound Start  index:34    from 1001 To 0
        SetMemory(0x660074, Add, -485),# units:What Sound Start  index:98    from 1044 To 559
        SetMemory(0x660088, Add, -25034752),# units:What Sound Start  index:109    from 397 To 15
        SetMemory(0x660094, Add, 9895936),# units:What Sound Start  index:115    from 389 To 540
        SetMemory(0x662C34, Add, -1004),# units:What Sound End  index:34    from 1004 To 0
        SetMemory(0x662CB4, Add, -485),# units:What Sound End  index:98    from 1047 To 562
        SetMemory(0x662CC8, Add, -25034752),# units:What Sound End  index:109    from 397 To 15
        SetMemory(0x662CD4, Add, 10092544),# units:What Sound End  index:115    from 389 To 543
        SetMemory(0x663B7C, Add, -1009),# units:Piss Sound Start  index:34    from 1009 To 0
        SetMemory(0x663BFC, Add, -498),# units:Piss Sound Start  index:98    from 1052 To 554
        SetMemory(0x661F2C, Add, -1015),# units:Piss Sound End  index:34    from 1015 To 0
        SetMemory(0x661FAC, Add, -500),# units:Piss Sound End  index:98    from 1058 To 558
        SetMemory(0x663C54, Add, -1005),# units:Yes Sound Start  index:34    from 1005 To 0
        SetMemory(0x663CD4, Add, -485),# units:Yes Sound Start  index:98    from 1048 To 563
        SetMemory(0x661484, Add, -1008),# units:Yes Sound End  index:34    from 1008 To 0
        SetMemory(0x661504, Add, -486),# units:Yes Sound End  index:98    from 1051 To 565
        SetMemory(0x662864, Add, 2),# units:StarEdit Placement Box Width  index:1    from 15 To 17
        SetMemory(0x662868, Add, -15),# units:StarEdit Placement Box Width  index:2    from 32 To 17
        SetMemory(0x66286C, Add, -15),# units:StarEdit Placement Box Width  index:3    from 32 To 17
        SetMemory(0x662874, Add, -15),# units:StarEdit Placement Box Width  index:5    from 32 To 17
        SetMemory(0x662880, Add, -29),# units:StarEdit Placement Box Width  index:8    from 38 To 9
        SetMemory(0x662884, Add, -56),# units:StarEdit Placement Box Width  index:9    from 65 To 9
        SetMemory(0x66288C, Add, -28),# units:StarEdit Placement Box Width  index:11    from 49 To 21
        SetMemory(0x662890, Add, -71),# units:StarEdit Placement Box Width  index:12    from 80 To 9
        SetMemory(0x6628A0, Add, 2),# units:StarEdit Placement Box Width  index:16    from 15 To 17
        SetMemory(0x6628A4, Add, -23),# units:StarEdit Placement Box Width  index:17    from 32 To 9
        SetMemory(0x6628AC, Add, -15),# units:StarEdit Placement Box Width  index:19    from 32 To 17
        SetMemory(0x6628B0, Add, -1),# units:StarEdit Placement Box Width  index:20    from 18 To 17
        SetMemory(0x6628B4, Add, -29),# units:StarEdit Placement Box Width  index:21    from 38 To 9
        SetMemory(0x6628B8, Add, -56),# units:StarEdit Placement Box Width  index:22    from 65 To 9
        SetMemory(0x6628BC, Add, -15),# units:StarEdit Placement Box Width  index:23    from 32 To 17
        SetMemory(0x6628C4, Add, -15),# units:StarEdit Placement Box Width  index:25    from 32 To 17
        SetMemory(0x6628CC, Add, -66),# units:StarEdit Placement Box Width  index:27    from 75 To 9
        SetMemory(0x6628D0, Add, -66),# units:StarEdit Placement Box Width  index:28    from 75 To 9
        SetMemory(0x6628D4, Add, -66),# units:StarEdit Placement Box Width  index:29    from 75 To 9
        SetMemory(0x6628D8, Add, -7),# units:StarEdit Placement Box Width  index:30    from 32 To 25
        SetMemory(0x6628E0, Add, -6),# units:StarEdit Placement Box Width  index:32    from 23 To 17
        SetMemory(0x6628E8, Add, 7),# units:StarEdit Placement Box Width  index:34    from 17 To 24
        SetMemory(0x66290C, Add, -35),# units:StarEdit Placement Box Width  index:43    from 44 To 9
        SetMemory(0x662910, Add, -35),# units:StarEdit Placement Box Width  index:44    from 44 To 9
        SetMemory(0x66291C, Add, -15),# units:StarEdit Placement Box Width  index:47    from 24 To 9
        SetMemory(0x66292C, Add, 2),# units:StarEdit Placement Box Width  index:51    from 15 To 17
        SetMemory(0x662930, Add, -12),# units:StarEdit Placement Box Width  index:52    from 29 To 17
        SetMemory(0x662934, Add, -4),# units:StarEdit Placement Box Width  index:53    from 21 To 17
        SetMemory(0x662938, Add, 1),# units:StarEdit Placement Box Width  index:54    from 16 To 17
        SetMemory(0x66293C, Add, -35),# units:StarEdit Placement Box Width  index:55    from 44 To 9
        SetMemory(0x662940, Add, -35),# units:StarEdit Placement Box Width  index:56    from 44 To 9
        SetMemory(0x662958, Add, -35),# units:StarEdit Placement Box Width  index:62    from 44 To 9
        SetMemory(0x66295C, Add, -15),# units:StarEdit Placement Box Width  index:63    from 32 To 17
        SetMemory(0x662968, Add, -15),# units:StarEdit Placement Box Width  index:66    from 32 To 17
        SetMemory(0x662970, Add, -15),# units:StarEdit Placement Box Width  index:68    from 32 To 17
        SetMemory(0x662974, Add, -19),# units:StarEdit Placement Box Width  index:69    from 40 To 21
        SetMemory(0x662978, Add, -19),# units:StarEdit Placement Box Width  index:70    from 36 To 17
        SetMemory(0x66297C, Add, -27),# units:StarEdit Placement Box Width  index:71    from 44 To 17
        SetMemory(0x662980, Add, -47),# units:StarEdit Placement Box Width  index:72    from 64 To 17
        SetMemory(0x662988, Add, -7),# units:StarEdit Placement Box Width  index:74    from 24 To 17
        SetMemory(0x66298C, Add, -15),# units:StarEdit Placement Box Width  index:75    from 24 To 9
        SetMemory(0x662990, Add, -15),# units:StarEdit Placement Box Width  index:76    from 32 To 17
        SetMemory(0x662994, Add, -7),# units:StarEdit Placement Box Width  index:77    from 24 To 17
        SetMemory(0x6629A0, Add, -27),# units:StarEdit Placement Box Width  index:80    from 36 To 9
        SetMemory(0x6629A8, Add, -55),# units:StarEdit Placement Box Width  index:82    from 64 To 9
        SetMemory(0x6629AC, Add, -15),# units:StarEdit Placement Box Width  index:83    from 32 To 17
        SetMemory(0x6629B8, Add, -35),# units:StarEdit Placement Box Width  index:86    from 44 To 9
        SetMemory(0x6629C0, Add, -27),# units:StarEdit Placement Box Width  index:88    from 36 To 9
        SetMemory(0x6629E8, Add, -40),# units:StarEdit Placement Box Width  index:98    from 49 To 9
        SetMemory(0x6629EC, Add, 2),# units:StarEdit Placement Box Width  index:99    from 15 To 17
        SetMemory(0x6629F8, Add, -66),# units:StarEdit Placement Box Width  index:102    from 75 To 9
        SetMemory(0x662A14, Add, -64),# units:StarEdit Placement Box Width  index:109    from 96 To 32
        SetMemory(0x662A2C, Add, -55),# units:StarEdit Placement Box Width  index:115    from 64 To 9
        SetMemory(0x662A38, Add, -55),# units:StarEdit Placement Box Width  index:118    from 64 To 9
        SetMemory(0x662A40, Add, -55),# units:StarEdit Placement Box Width  index:120    from 64 To 9
        SetMemory(0x662A60, Add, -7),# units:StarEdit Placement Box Width  index:128    from 32 To 25
        SetMemory(0x662A64, Add, -23),# units:StarEdit Placement Box Width  index:129    from 32 To 9
        SetMemory(0x662A68, Add, -103),# units:StarEdit Placement Box Width  index:130    from 128 To 25
        SetMemory(0x662AA0, Add, -47),# units:StarEdit Placement Box Width  index:144    from 64 To 17
        SetMemory(0x662B14, Add, -97),# units:StarEdit Placement Box Width  index:173    from 128 To 31
        SetMemory(0x662B1C, Add, -40),# units:StarEdit Placement Box Width  index:175    from 160 To 120
        SetMemory(0x662860, Add, -196608),# units:StarEdit Placement Box Height  index:0    from 20 To 17
        SetMemory(0x662864, Add, -327680),# units:StarEdit Placement Box Height  index:1    from 22 To 17
        SetMemory(0x662868, Add, -983040),# units:StarEdit Placement Box Height  index:2    from 32 To 17
        SetMemory(0x66286C, Add, -983040),# units:StarEdit Placement Box Height  index:3    from 32 To 17
        SetMemory(0x662874, Add, -983040),# units:StarEdit Placement Box Height  index:5    from 32 To 17
        SetMemory(0x662880, Add, -1376256),# units:StarEdit Placement Box Height  index:8    from 30 To 9
        SetMemory(0x662884, Add, -2686976),# units:StarEdit Placement Box Height  index:9    from 50 To 9
        SetMemory(0x66288C, Add, -1048576),# units:StarEdit Placement Box Height  index:11    from 37 To 21
        SetMemory(0x662890, Add, -3604480),# units:StarEdit Placement Box Height  index:12    from 64 To 9
        SetMemory(0x6628A0, Add, -327680),# units:StarEdit Placement Box Height  index:16    from 22 To 17
        SetMemory(0x6628A4, Add, -1507328),# units:StarEdit Placement Box Height  index:17    from 32 To 9
        SetMemory(0x6628AC, Add, -983040),# units:StarEdit Placement Box Height  index:19    from 32 To 17
        SetMemory(0x6628B0, Add, -327680),# units:StarEdit Placement Box Height  index:20    from 22 To 17
        SetMemory(0x6628B4, Add, -1376256),# units:StarEdit Placement Box Height  index:21    from 30 To 9
        SetMemory(0x6628B8, Add, -2686976),# units:StarEdit Placement Box Height  index:22    from 50 To 9
        SetMemory(0x6628BC, Add, -983040),# units:StarEdit Placement Box Height  index:23    from 32 To 17
        SetMemory(0x6628C4, Add, -983040),# units:StarEdit Placement Box Height  index:25    from 32 To 17
        SetMemory(0x6628CC, Add, -3276800),# units:StarEdit Placement Box Height  index:27    from 59 To 9
        SetMemory(0x6628D0, Add, -3276800),# units:StarEdit Placement Box Height  index:28    from 59 To 9
        SetMemory(0x6628D4, Add, -3276800),# units:StarEdit Placement Box Height  index:29    from 59 To 9
        SetMemory(0x6628D8, Add, -458752),# units:StarEdit Placement Box Height  index:30    from 32 To 25
        SetMemory(0x6628E0, Add, -720896),# units:StarEdit Placement Box Height  index:32    from 28 To 17
        SetMemory(0x6628E8, Add, 524288),# units:StarEdit Placement Box Height  index:34    from 20 To 28
        SetMemory(0x66290C, Add, -2293760),# units:StarEdit Placement Box Height  index:43    from 44 To 9
        SetMemory(0x662910, Add, -2293760),# units:StarEdit Placement Box Height  index:44    from 44 To 9
        SetMemory(0x66291C, Add, -983040),# units:StarEdit Placement Box Height  index:47    from 24 To 9
        SetMemory(0x66292C, Add, -327680),# units:StarEdit Placement Box Height  index:51    from 22 To 17
        SetMemory(0x662930, Add, -786432),# units:StarEdit Placement Box Height  index:52    from 29 To 17
        SetMemory(0x662934, Add, -393216),# units:StarEdit Placement Box Height  index:53    from 23 To 17
        SetMemory(0x662938, Add, 65536),# units:StarEdit Placement Box Height  index:54    from 16 To 17
        SetMemory(0x66293C, Add, -2293760),# units:StarEdit Placement Box Height  index:55    from 44 To 9
        SetMemory(0x662940, Add, -2293760),# units:StarEdit Placement Box Height  index:56    from 44 To 9
        SetMemory(0x662958, Add, -2293760),# units:StarEdit Placement Box Height  index:62    from 44 To 9
        SetMemory(0x66295C, Add, -983040),# units:StarEdit Placement Box Height  index:63    from 32 To 17
        SetMemory(0x662968, Add, -983040),# units:StarEdit Placement Box Height  index:66    from 32 To 17
        SetMemory(0x662970, Add, -983040),# units:StarEdit Placement Box Height  index:68    from 32 To 17
        SetMemory(0x662974, Add, -720896),# units:StarEdit Placement Box Height  index:69    from 32 To 21
        SetMemory(0x662978, Add, -983040),# units:StarEdit Placement Box Height  index:70    from 32 To 17
        SetMemory(0x66297C, Add, -1769472),# units:StarEdit Placement Box Height  index:71    from 44 To 17
        SetMemory(0x662980, Add, -3080192),# units:StarEdit Placement Box Height  index:72    from 64 To 17
        SetMemory(0x662988, Add, -851968),# units:StarEdit Placement Box Height  index:74    from 30 To 17
        SetMemory(0x66298C, Add, -1376256),# units:StarEdit Placement Box Height  index:75    from 30 To 9
        SetMemory(0x662990, Add, -983040),# units:StarEdit Placement Box Height  index:76    from 32 To 17
        SetMemory(0x662994, Add, -851968),# units:StarEdit Placement Box Height  index:77    from 30 To 17
        SetMemory(0x6629A0, Add, -1507328),# units:StarEdit Placement Box Height  index:80    from 32 To 9
        SetMemory(0x6629A8, Add, -3604480),# units:StarEdit Placement Box Height  index:82    from 64 To 9
        SetMemory(0x6629AC, Add, -983040),# units:StarEdit Placement Box Height  index:83    from 32 To 17
        SetMemory(0x6629B8, Add, -2293760),# units:StarEdit Placement Box Height  index:86    from 44 To 9
        SetMemory(0x6629C0, Add, -1507328),# units:StarEdit Placement Box Height  index:88    from 32 To 9
        SetMemory(0x6629E8, Add, -1835008),# units:StarEdit Placement Box Height  index:98    from 37 To 9
        SetMemory(0x6629EC, Add, -327680),# units:StarEdit Placement Box Height  index:99    from 22 To 17
        SetMemory(0x6629F8, Add, -3276800),# units:StarEdit Placement Box Height  index:102    from 59 To 9
        SetMemory(0x662A14, Add, -2097152),# units:StarEdit Placement Box Height  index:109    from 64 To 32
        SetMemory(0x662A2C, Add, -3604480),# units:StarEdit Placement Box Height  index:115    from 64 To 9
        SetMemory(0x662A38, Add, -3604480),# units:StarEdit Placement Box Height  index:118    from 64 To 9
        SetMemory(0x662A40, Add, -3604480),# units:StarEdit Placement Box Height  index:120    from 64 To 9
        SetMemory(0x662A60, Add, -458752),# units:StarEdit Placement Box Height  index:128    from 32 To 25
        SetMemory(0x662A64, Add, -1507328),# units:StarEdit Placement Box Height  index:129    from 32 To 9
        SetMemory(0x662A68, Add, -4653056),# units:StarEdit Placement Box Height  index:130    from 96 To 25
        SetMemory(0x662AA0, Add, -3080192),# units:StarEdit Placement Box Height  index:144    from 64 To 17
        SetMemory(0x662B14, Add, -4259840),# units:StarEdit Placement Box Height  index:173    from 96 To 31
        SetMemory(0x662B1C, Add, -2621440),# units:StarEdit Placement Box Height  index:175    from 128 To 88
        SetMemory(0x662704, Add, -128),# units:Addon Horizontal (X) Position  index:9    from 128 To 0
        SetMemory(0x662710, Add, -128),# units:Addon Horizontal (X) Position  index:12    from 128 To 0
        SetMemory(0x662718, Add, -128),# units:Addon Horizontal (X) Position  index:14    from 128 To 0
        SetMemory(0x662704, Add, -2097152),# units:Addon Vertical (Y) Position  index:9    from 32 To 0
        SetMemory(0x662710, Add, -2097152),# units:Addon Vertical (Y) Position  index:12    from 32 To 0
        SetMemory(0x662718, Add, -2097152),# units:Addon Vertical (Y) Position  index:14    from 32 To 0
        SetMemory(0x6617D0, Add, 1),# units:Unit Size Left  index:1    from 7 To 8
        SetMemory(0x6617D8, Add, -8),# units:Unit Size Left  index:2    from 16 To 8
        SetMemory(0x6617E0, Add, -8),# units:Unit Size Left  index:3    from 16 To 8
        SetMemory(0x6617F0, Add, -8),# units:Unit Size Left  index:5    from 16 To 8
        SetMemory(0x661808, Add, -15),# units:Unit Size Left  index:8    from 19 To 4
        SetMemory(0x661810, Add, -28),# units:Unit Size Left  index:9    from 32 To 4
        SetMemory(0x661820, Add, -14),# units:Unit Size Left  index:11    from 24 To 10
        SetMemory(0x661828, Add, -33),# units:Unit Size Left  index:12    from 37 To 4
        SetMemory(0x661848, Add, 1),# units:Unit Size Left  index:16    from 7 To 8
        SetMemory(0x661850, Add, -12),# units:Unit Size Left  index:17    from 16 To 4
        SetMemory(0x661860, Add, -8),# units:Unit Size Left  index:19    from 16 To 8
        SetMemory(0x661870, Add, -15),# units:Unit Size Left  index:21    from 19 To 4
        SetMemory(0x661878, Add, -28),# units:Unit Size Left  index:22    from 32 To 4
        SetMemory(0x661880, Add, -8),# units:Unit Size Left  index:23    from 16 To 8
        SetMemory(0x661890, Add, -8),# units:Unit Size Left  index:25    from 16 To 8
        SetMemory(0x6618A0, Add, -33),# units:Unit Size Left  index:27    from 37 To 4
        SetMemory(0x6618A8, Add, -33),# units:Unit Size Left  index:28    from 37 To 4
        SetMemory(0x6618B0, Add, -33),# units:Unit Size Left  index:29    from 37 To 4
        SetMemory(0x6618B8, Add, -4),# units:Unit Size Left  index:30    from 16 To 12
        SetMemory(0x6618C8, Add, -3),# units:Unit Size Left  index:32    from 11 To 8
        SetMemory(0x6618D8, Add, 4),# units:Unit Size Left  index:34    from 8 To 12
        SetMemory(0x661920, Add, -18),# units:Unit Size Left  index:43    from 22 To 4
        SetMemory(0x661928, Add, -18),# units:Unit Size Left  index:44    from 22 To 4
        SetMemory(0x661940, Add, -8),# units:Unit Size Left  index:47    from 12 To 4
        SetMemory(0x661960, Add, 1),# units:Unit Size Left  index:51    from 7 To 8
        SetMemory(0x661970, Add, -2),# units:Unit Size Left  index:53    from 10 To 8
        SetMemory(0x661980, Add, -18),# units:Unit Size Left  index:55    from 22 To 4
        SetMemory(0x661988, Add, -18),# units:Unit Size Left  index:56    from 22 To 4
        SetMemory(0x6619B8, Add, -18),# units:Unit Size Left  index:62    from 22 To 4
        SetMemory(0x6619C0, Add, -8),# units:Unit Size Left  index:63    from 16 To 8
        SetMemory(0x6619D8, Add, -7),# units:Unit Size Left  index:66    from 15 To 8
        SetMemory(0x6619E8, Add, -8),# units:Unit Size Left  index:68    from 16 To 8
        SetMemory(0x6619F0, Add, -10),# units:Unit Size Left  index:69    from 20 To 10
        SetMemory(0x6619F8, Add, -10),# units:Unit Size Left  index:70    from 18 To 8
        SetMemory(0x661A00, Add, -14),# units:Unit Size Left  index:71    from 22 To 8
        SetMemory(0x661A08, Add, -24),# units:Unit Size Left  index:72    from 32 To 8
        SetMemory(0x661A18, Add, -4),# units:Unit Size Left  index:74    from 12 To 8
        SetMemory(0x661A20, Add, -10),# units:Unit Size Left  index:75    from 12 To 2
        SetMemory(0x661A28, Add, -8),# units:Unit Size Left  index:76    from 16 To 8
        SetMemory(0x661A30, Add, -3),# units:Unit Size Left  index:77    from 11 To 8
        SetMemory(0x661A48, Add, -14),# units:Unit Size Left  index:80    from 18 To 4
        SetMemory(0x661A58, Add, -28),# units:Unit Size Left  index:82    from 32 To 4
        SetMemory(0x661A60, Add, -8),# units:Unit Size Left  index:83    from 16 To 8
        SetMemory(0x661A78, Add, -18),# units:Unit Size Left  index:86    from 22 To 4
        SetMemory(0x661A88, Add, -14),# units:Unit Size Left  index:88    from 18 To 4
        SetMemory(0x661AB8, Add, -12),# units:Unit Size Left  index:94    from 16 To 4
        SetMemory(0x661AD8, Add, -20),# units:Unit Size Left  index:98    from 24 To 4
        SetMemory(0x661AE0, Add, 1),# units:Unit Size Left  index:99    from 7 To 8
        SetMemory(0x661AF8, Add, -33),# units:Unit Size Left  index:102    from 37 To 4
        SetMemory(0x661B30, Add, -22),# units:Unit Size Left  index:109    from 38 To 16
        SetMemory(0x661B60, Add, -43),# units:Unit Size Left  index:115    from 47 To 4
        SetMemory(0x661B78, Add, -41),# units:Unit Size Left  index:118    from 47 To 6
        SetMemory(0x661B88, Add, -35),# units:Unit Size Left  index:120    from 39 To 4
        SetMemory(0x661BC8, Add, -4),# units:Unit Size Left  index:128    from 16 To 12
        SetMemory(0x661BD0, Add, -12),# units:Unit Size Left  index:129    from 16 To 4
        SetMemory(0x661BD8, Add, -46),# units:Unit Size Left  index:130    from 58 To 12
        SetMemory(0x661C48, Add, -16),# units:Unit Size Left  index:144    from 24 To 8
        SetMemory(0x661D30, Add, -49),# units:Unit Size Left  index:173    from 64 To 15
        SetMemory(0x661D40, Add, -20),# units:Unit Size Left  index:175    from 80 To 60
        SetMemory(0x6617C8, Add, -65536),# units:Unit Size Up  index:0    from 9 To 8
        SetMemory(0x6617D0, Add, -131072),# units:Unit Size Up  index:1    from 10 To 8
        SetMemory(0x6617D8, Add, -524288),# units:Unit Size Up  index:2    from 16 To 8
        SetMemory(0x6617E0, Add, -524288),# units:Unit Size Up  index:3    from 16 To 8
        SetMemory(0x6617F0, Add, -524288),# units:Unit Size Up  index:5    from 16 To 8
        SetMemory(0x661808, Add, -720896),# units:Unit Size Up  index:8    from 15 To 4
        SetMemory(0x661810, Add, -1900544),# units:Unit Size Up  index:9    from 33 To 4
        SetMemory(0x661820, Add, -393216),# units:Unit Size Up  index:11    from 16 To 10
        SetMemory(0x661828, Add, -1638400),# units:Unit Size Up  index:12    from 29 To 4
        SetMemory(0x661848, Add, -131072),# units:Unit Size Up  index:16    from 10 To 8
        SetMemory(0x661850, Add, -786432),# units:Unit Size Up  index:17    from 16 To 4
        SetMemory(0x661860, Add, -524288),# units:Unit Size Up  index:19    from 16 To 8
        SetMemory(0x661868, Add, -65536),# units:Unit Size Up  index:20    from 9 To 8
        SetMemory(0x661870, Add, -720896),# units:Unit Size Up  index:21    from 15 To 4
        SetMemory(0x661878, Add, -1900544),# units:Unit Size Up  index:22    from 33 To 4
        SetMemory(0x661880, Add, -524288),# units:Unit Size Up  index:23    from 16 To 8
        SetMemory(0x661890, Add, -524288),# units:Unit Size Up  index:25    from 16 To 8
        SetMemory(0x6618A0, Add, -1638400),# units:Unit Size Up  index:27    from 29 To 4
        SetMemory(0x6618A8, Add, -1638400),# units:Unit Size Up  index:28    from 29 To 4
        SetMemory(0x6618B0, Add, -1638400),# units:Unit Size Up  index:29    from 29 To 4
        SetMemory(0x6618B8, Add, -262144),# units:Unit Size Up  index:30    from 16 To 12
        SetMemory(0x6618C8, Add, 65536),# units:Unit Size Up  index:32    from 7 To 8
        SetMemory(0x6618D8, Add, 327680),# units:Unit Size Up  index:34    from 9 To 14
        SetMemory(0x661920, Add, -1179648),# units:Unit Size Up  index:43    from 22 To 4
        SetMemory(0x661928, Add, -1179648),# units:Unit Size Up  index:44    from 22 To 4
        SetMemory(0x661940, Add, -524288),# units:Unit Size Up  index:47    from 12 To 4
        SetMemory(0x661960, Add, -131072),# units:Unit Size Up  index:51    from 10 To 8
        SetMemory(0x661970, Add, -131072),# units:Unit Size Up  index:53    from 10 To 8
        SetMemory(0x661978, Add, 262144),# units:Unit Size Up  index:54    from 4 To 8
        SetMemory(0x661980, Add, -1179648),# units:Unit Size Up  index:55    from 22 To 4
        SetMemory(0x661988, Add, -1179648),# units:Unit Size Up  index:56    from 22 To 4
        SetMemory(0x6619B8, Add, -1179648),# units:Unit Size Up  index:62    from 22 To 4
        SetMemory(0x6619C0, Add, -524288),# units:Unit Size Up  index:63    from 16 To 8
        SetMemory(0x6619D8, Add, -458752),# units:Unit Size Up  index:66    from 15 To 8
        SetMemory(0x6619E8, Add, -524288),# units:Unit Size Up  index:68    from 16 To 8
        SetMemory(0x6619F0, Add, -393216),# units:Unit Size Up  index:69    from 16 To 10
        SetMemory(0x6619F8, Add, -524288),# units:Unit Size Up  index:70    from 16 To 8
        SetMemory(0x661A00, Add, -917504),# units:Unit Size Up  index:71    from 22 To 8
        SetMemory(0x661A08, Add, -1572864),# units:Unit Size Up  index:72    from 32 To 8
        SetMemory(0x661A18, Add, 131072),# units:Unit Size Up  index:74    from 6 To 8
        SetMemory(0x661A20, Add, -262144),# units:Unit Size Up  index:75    from 6 To 2
        SetMemory(0x661A28, Add, -524288),# units:Unit Size Up  index:76    from 16 To 8
        SetMemory(0x661A30, Add, 196608),# units:Unit Size Up  index:77    from 5 To 8
        SetMemory(0x661A48, Add, -786432),# units:Unit Size Up  index:80    from 16 To 4
        SetMemory(0x661A58, Add, -1835008),# units:Unit Size Up  index:82    from 32 To 4
        SetMemory(0x661A60, Add, -524288),# units:Unit Size Up  index:83    from 16 To 8
        SetMemory(0x661A78, Add, -1179648),# units:Unit Size Up  index:86    from 22 To 4
        SetMemory(0x661A88, Add, -786432),# units:Unit Size Up  index:88    from 16 To 4
        SetMemory(0x661AB8, Add, -786432),# units:Unit Size Up  index:94    from 16 To 4
        SetMemory(0x661AD8, Add, -786432),# units:Unit Size Up  index:98    from 16 To 4
        SetMemory(0x661AE0, Add, -131072),# units:Unit Size Up  index:99    from 10 To 8
        SetMemory(0x661AF8, Add, -1638400),# units:Unit Size Up  index:102    from 29 To 4
        SetMemory(0x661B30, Add, -393216),# units:Unit Size Up  index:109    from 22 To 16
        SetMemory(0x661B60, Add, -1310720),# units:Unit Size Up  index:115    from 24 To 4
        SetMemory(0x661B78, Add, -1179648),# units:Unit Size Up  index:118    from 24 To 6
        SetMemory(0x661B88, Add, -1310720),# units:Unit Size Up  index:120    from 24 To 4
        SetMemory(0x661BC8, Add, -262144),# units:Unit Size Up  index:128    from 16 To 12
        SetMemory(0x661BD0, Add, -786432),# units:Unit Size Up  index:129    from 16 To 4
        SetMemory(0x661BD8, Add, -1900544),# units:Unit Size Up  index:130    from 41 To 12
        SetMemory(0x661C48, Add, -1048576),# units:Unit Size Up  index:144    from 24 To 8
        SetMemory(0x661D30, Add, -2162688),# units:Unit Size Up  index:173    from 48 To 15
        SetMemory(0x661D40, Add, 720896),# units:Unit Size Up  index:175    from 34 To 45
        SetMemory(0x6617D4, Add, 1),# units:Unit Size Right  index:1    from 7 To 8
        SetMemory(0x6617DC, Add, -7),# units:Unit Size Right  index:2    from 15 To 8
        SetMemory(0x6617E4, Add, -7),# units:Unit Size Right  index:3    from 15 To 8
        SetMemory(0x6617F4, Add, -7),# units:Unit Size Right  index:5    from 15 To 8
        SetMemory(0x66180C, Add, -14),# units:Unit Size Right  index:8    from 18 To 4
        SetMemory(0x661814, Add, -28),# units:Unit Size Right  index:9    from 32 To 4
        SetMemory(0x661824, Add, -14),# units:Unit Size Right  index:11    from 24 To 10
        SetMemory(0x66182C, Add, -33),# units:Unit Size Right  index:12    from 37 To 4
        SetMemory(0x66184C, Add, 1),# units:Unit Size Right  index:16    from 7 To 8
        SetMemory(0x661854, Add, -11),# units:Unit Size Right  index:17    from 15 To 4
        SetMemory(0x661864, Add, -7),# units:Unit Size Right  index:19    from 15 To 8
        SetMemory(0x661874, Add, -14),# units:Unit Size Right  index:21    from 18 To 4
        SetMemory(0x66187C, Add, -28),# units:Unit Size Right  index:22    from 32 To 4
        SetMemory(0x661884, Add, -7),# units:Unit Size Right  index:23    from 15 To 8
        SetMemory(0x661894, Add, -7),# units:Unit Size Right  index:25    from 15 To 8
        SetMemory(0x6618A4, Add, -33),# units:Unit Size Right  index:27    from 37 To 4
        SetMemory(0x6618AC, Add, -33),# units:Unit Size Right  index:28    from 37 To 4
        SetMemory(0x6618B4, Add, -33),# units:Unit Size Right  index:29    from 37 To 4
        SetMemory(0x6618BC, Add, -3),# units:Unit Size Right  index:30    from 15 To 12
        SetMemory(0x6618CC, Add, -3),# units:Unit Size Right  index:32    from 11 To 8
        SetMemory(0x6618DC, Add, 3),# units:Unit Size Right  index:34    from 8 To 11
        SetMemory(0x661924, Add, -17),# units:Unit Size Right  index:43    from 21 To 4
        SetMemory(0x66192C, Add, -17),# units:Unit Size Right  index:44    from 21 To 4
        SetMemory(0x661944, Add, -7),# units:Unit Size Right  index:47    from 11 To 4
        SetMemory(0x661964, Add, 1),# units:Unit Size Right  index:51    from 7 To 8
        SetMemory(0x661974, Add, -2),# units:Unit Size Right  index:53    from 10 To 8
        SetMemory(0x66197C, Add, 1),# units:Unit Size Right  index:54    from 7 To 8
        SetMemory(0x661984, Add, -17),# units:Unit Size Right  index:55    from 21 To 4
        SetMemory(0x66198C, Add, -17),# units:Unit Size Right  index:56    from 21 To 4
        SetMemory(0x6619BC, Add, -17),# units:Unit Size Right  index:62    from 21 To 4
        SetMemory(0x6619C4, Add, -7),# units:Unit Size Right  index:63    from 15 To 8
        SetMemory(0x6619DC, Add, -8),# units:Unit Size Right  index:66    from 16 To 8
        SetMemory(0x6619EC, Add, -7),# units:Unit Size Right  index:68    from 15 To 8
        SetMemory(0x6619F4, Add, -9),# units:Unit Size Right  index:69    from 19 To 10
        SetMemory(0x6619FC, Add, -9),# units:Unit Size Right  index:70    from 17 To 8
        SetMemory(0x661A04, Add, -13),# units:Unit Size Right  index:71    from 21 To 8
        SetMemory(0x661A0C, Add, -23),# units:Unit Size Right  index:72    from 31 To 8
        SetMemory(0x661A1C, Add, -3),# units:Unit Size Right  index:74    from 11 To 8
        SetMemory(0x661A24, Add, -9),# units:Unit Size Right  index:75    from 11 To 2
        SetMemory(0x661A2C, Add, -7),# units:Unit Size Right  index:76    from 15 To 8
        SetMemory(0x661A34, Add, -3),# units:Unit Size Right  index:77    from 11 To 8
        SetMemory(0x661A4C, Add, -13),# units:Unit Size Right  index:80    from 17 To 4
        SetMemory(0x661A5C, Add, -27),# units:Unit Size Right  index:82    from 31 To 4
        SetMemory(0x661A64, Add, -7),# units:Unit Size Right  index:83    from 15 To 8
        SetMemory(0x661A7C, Add, -17),# units:Unit Size Right  index:86    from 21 To 4
        SetMemory(0x661A8C, Add, -13),# units:Unit Size Right  index:88    from 17 To 4
        SetMemory(0x661ABC, Add, -11),# units:Unit Size Right  index:94    from 15 To 4
        SetMemory(0x661ADC, Add, -20),# units:Unit Size Right  index:98    from 24 To 4
        SetMemory(0x661AE4, Add, 1),# units:Unit Size Right  index:99    from 7 To 8
        SetMemory(0x661AFC, Add, -33),# units:Unit Size Right  index:102    from 37 To 4
        SetMemory(0x661B34, Add, -23),# units:Unit Size Right  index:109    from 38 To 15
        SetMemory(0x661B64, Add, -24),# units:Unit Size Right  index:115    from 28 To 4
        SetMemory(0x661B7C, Add, -22),# units:Unit Size Right  index:118    from 28 To 6
        SetMemory(0x661B8C, Add, -27),# units:Unit Size Right  index:120    from 31 To 4
        SetMemory(0x661BCC, Add, -3),# units:Unit Size Right  index:128    from 15 To 12
        SetMemory(0x661BD4, Add, -11),# units:Unit Size Right  index:129    from 15 To 4
        SetMemory(0x661BDC, Add, -46),# units:Unit Size Right  index:130    from 58 To 12
        SetMemory(0x661C4C, Add, -15),# units:Unit Size Right  index:144    from 23 To 8
        SetMemory(0x661D34, Add, -48),# units:Unit Size Right  index:173    from 63 To 15
        SetMemory(0x661D44, Add, -19),# units:Unit Size Right  index:175    from 79 To 60
        SetMemory(0x6617CC, Add, -131072),# units:Unit Size Down  index:0    from 10 To 8
        SetMemory(0x6617D4, Add, -196608),# units:Unit Size Down  index:1    from 11 To 8
        SetMemory(0x6617DC, Add, -458752),# units:Unit Size Down  index:2    from 15 To 8
        SetMemory(0x6617E4, Add, -458752),# units:Unit Size Down  index:3    from 15 To 8
        SetMemory(0x6617F4, Add, -458752),# units:Unit Size Down  index:5    from 15 To 8
        SetMemory(0x66180C, Add, -655360),# units:Unit Size Down  index:8    from 14 To 4
        SetMemory(0x661814, Add, -786432),# units:Unit Size Down  index:9    from 16 To 4
        SetMemory(0x661824, Add, -655360),# units:Unit Size Down  index:11    from 20 To 10
        SetMemory(0x66182C, Add, -1638400),# units:Unit Size Down  index:12    from 29 To 4
        SetMemory(0x66184C, Add, -196608),# units:Unit Size Down  index:16    from 11 To 8
        SetMemory(0x661854, Add, -720896),# units:Unit Size Down  index:17    from 15 To 4
        SetMemory(0x661864, Add, -458752),# units:Unit Size Down  index:19    from 15 To 8
        SetMemory(0x66186C, Add, -131072),# units:Unit Size Down  index:20    from 10 To 8
        SetMemory(0x661874, Add, -655360),# units:Unit Size Down  index:21    from 14 To 4
        SetMemory(0x66187C, Add, -786432),# units:Unit Size Down  index:22    from 16 To 4
        SetMemory(0x661884, Add, -458752),# units:Unit Size Down  index:23    from 15 To 8
        SetMemory(0x661894, Add, -458752),# units:Unit Size Down  index:25    from 15 To 8
        SetMemory(0x6618A4, Add, -1638400),# units:Unit Size Down  index:27    from 29 To 4
        SetMemory(0x6618AC, Add, -1638400),# units:Unit Size Down  index:28    from 29 To 4
        SetMemory(0x6618B4, Add, -1638400),# units:Unit Size Down  index:29    from 29 To 4
        SetMemory(0x6618BC, Add, -196608),# units:Unit Size Down  index:30    from 15 To 12
        SetMemory(0x6618CC, Add, -393216),# units:Unit Size Down  index:32    from 14 To 8
        SetMemory(0x6618DC, Add, 196608),# units:Unit Size Down  index:34    from 10 To 13
        SetMemory(0x661924, Add, -1114112),# units:Unit Size Down  index:43    from 21 To 4
        SetMemory(0x66192C, Add, -1114112),# units:Unit Size Down  index:44    from 21 To 4
        SetMemory(0x661944, Add, -458752),# units:Unit Size Down  index:47    from 11 To 4
        SetMemory(0x661964, Add, -196608),# units:Unit Size Down  index:51    from 11 To 8
        SetMemory(0x661974, Add, -262144),# units:Unit Size Down  index:53    from 12 To 8
        SetMemory(0x66197C, Add, -196608),# units:Unit Size Down  index:54    from 11 To 8
        SetMemory(0x661984, Add, -1114112),# units:Unit Size Down  index:55    from 21 To 4
        SetMemory(0x66198C, Add, -1114112),# units:Unit Size Down  index:56    from 21 To 4
        SetMemory(0x6619BC, Add, -1114112),# units:Unit Size Down  index:62    from 21 To 4
        SetMemory(0x6619C4, Add, -458752),# units:Unit Size Down  index:63    from 15 To 8
        SetMemory(0x6619DC, Add, -524288),# units:Unit Size Down  index:66    from 16 To 8
        SetMemory(0x6619EC, Add, -458752),# units:Unit Size Down  index:68    from 15 To 8
        SetMemory(0x6619F4, Add, -327680),# units:Unit Size Down  index:69    from 15 To 10
        SetMemory(0x6619FC, Add, -458752),# units:Unit Size Down  index:70    from 15 To 8
        SetMemory(0x661A04, Add, -851968),# units:Unit Size Down  index:71    from 21 To 8
        SetMemory(0x661A0C, Add, -1507328),# units:Unit Size Down  index:72    from 31 To 8
        SetMemory(0x661A1C, Add, -720896),# units:Unit Size Down  index:74    from 19 To 8
        SetMemory(0x661A24, Add, -1114112),# units:Unit Size Down  index:75    from 19 To 2
        SetMemory(0x661A2C, Add, -458752),# units:Unit Size Down  index:76    from 15 To 8
        SetMemory(0x661A34, Add, -327680),# units:Unit Size Down  index:77    from 13 To 8
        SetMemory(0x661A4C, Add, -720896),# units:Unit Size Down  index:80    from 15 To 4
        SetMemory(0x661A5C, Add, -1769472),# units:Unit Size Down  index:82    from 31 To 4
        SetMemory(0x661A64, Add, -458752),# units:Unit Size Down  index:83    from 15 To 8
        SetMemory(0x661A7C, Add, -1114112),# units:Unit Size Down  index:86    from 21 To 4
        SetMemory(0x661A8C, Add, -720896),# units:Unit Size Down  index:88    from 15 To 4
        SetMemory(0x661ABC, Add, -720896),# units:Unit Size Down  index:94    from 15 To 4
        SetMemory(0x661ADC, Add, -1048576),# units:Unit Size Down  index:98    from 20 To 4
        SetMemory(0x661AE4, Add, -196608),# units:Unit Size Down  index:99    from 11 To 8
        SetMemory(0x661AFC, Add, -1638400),# units:Unit Size Down  index:102    from 29 To 4
        SetMemory(0x661B34, Add, -720896),# units:Unit Size Down  index:109    from 26 To 15
        SetMemory(0x661B64, Add, -1179648),# units:Unit Size Down  index:115    from 22 To 4
        SetMemory(0x661B7C, Add, -1048576),# units:Unit Size Down  index:118    from 22 To 6
        SetMemory(0x661B8C, Add, -1310720),# units:Unit Size Down  index:120    from 24 To 4
        SetMemory(0x661BCC, Add, -196608),# units:Unit Size Down  index:128    from 15 To 12
        SetMemory(0x661BD4, Add, -720896),# units:Unit Size Down  index:129    from 15 To 4
        SetMemory(0x661BDC, Add, -1900544),# units:Unit Size Down  index:130    from 41 To 12
        SetMemory(0x661C4C, Add, -983040),# units:Unit Size Down  index:144    from 23 To 8
        SetMemory(0x661D34, Add, -2097152),# units:Unit Size Down  index:173    from 47 To 15
        SetMemory(0x661D44, Add, -1179648),# units:Unit Size Down  index:175    from 63 To 45
        SetMemory(0x662FCC, Add, -48),# units:Portrait  index:34    from 90 To 42
        SetMemory(0x66304C, Add, -50),# units:Portrait  index:98    from 96 To 46
        SetMemory(0x663060, Add, 4259840),# units:Portrait  index:109    from 17 To 82
        SetMemory(0x66306C, Add, 1835008),# units:Portrait  index:115    from 17 To 45
        SetMemory(0x6638CC, Add, 50),# units:Mineral Cost  index:34    from 50 To 100
        SetMemory(0x663960, Add, -6488064),# units:Mineral Cost  index:109    from 100 To 1
        SetMemory(0x66396C, Add, 36044800),# units:Mineral Cost  index:115    from 50 To 600
        SetMemory(0x65FD44, Add, 275),# units:Vespene Cost  index:34    from 25 To 300
        SetMemory(0x65FDC4, Add, 300),# units:Vespene Cost  index:98    from 0 To 300
        SetMemory(0x65FDD8, Add, 65536),# units:Vespene Cost  index:109    from 0 To 1
        SetMemory(0x65FDE4, Add, 16384000),# units:Vespene Cost  index:115    from 50 To 300
        SetMemory(0x66046C, Add, 1050),# units:Build Time  index:34    from 450 To 1500
        SetMemory(0x6604EC, Add, 1),# units:Build Time  index:98    from 0 To 1
        SetMemory(0x660500, Add, -39256064),# units:Build Time  index:109    from 600 To 1
        SetMemory(0x66050C, Add, 117964800),# units:Build Time  index:115    from 600 To 2400
        SetMemory(0x6637C0, Add, 131072),# units:Staredit Group Flags  index:34    from 10 To 12
        SetMemory(0x6637C4, Add, 256),# units:Staredit Group Flags  index:37    from 9 To 10
        SetMemory(0x6637C4, Add, 65536),# units:Staredit Group Flags  index:38    from 9 To 10
        SetMemory(0x6637C4, Add, 16777216),# units:Staredit Group Flags  index:39    from 9 To 10
        SetMemory(0x6637C8, Add, 1),# units:Staredit Group Flags  index:40    from 9 To 10
        SetMemory(0x6637C8, Add, 256),# units:Staredit Group Flags  index:41    from 9 To 10
        SetMemory(0x6637C8, Add, 16777216),# units:Staredit Group Flags  index:43    from 9 To 10
        SetMemory(0x6637CC, Add, 1),# units:Staredit Group Flags  index:44    from 9 To 10
        SetMemory(0x6637D0, Add, 1),# units:Staredit Group Flags  index:48    from 9 To 10
        SetMemory(0x6637D0, Add, 16777216),# units:Staredit Group Flags  index:51    from 9 To 10
        SetMemory(0x6637D4, Add, 256),# units:Staredit Group Flags  index:53    from 9 To 10
        SetMemory(0x6637D4, Add, 65536),# units:Staredit Group Flags  index:54    from 9 To 10
        SetMemory(0x6637D4, Add, 16777216),# units:Staredit Group Flags  index:55    from 9 To 10
        SetMemory(0x6637D8, Add, 1),# units:Staredit Group Flags  index:56    from 9 To 10
        SetMemory(0x6637E0, Add, -512),# units:Staredit Group Flags  index:65    from 12 To 10
        SetMemory(0x6637E0, Add, -131072),# units:Staredit Group Flags  index:66    from 12 To 10
        SetMemory(0x6637E0, Add, -33554432),# units:Staredit Group Flags  index:67    from 12 To 10
        SetMemory(0x6637E4, Add, -2),# units:Staredit Group Flags  index:68    from 12 To 10
        SetMemory(0x6637E8, Add, -512),# units:Staredit Group Flags  index:73    from 12 To 10
        SetMemory(0x6637E8, Add, -131072),# units:Staredit Group Flags  index:74    from 12 To 10
        SetMemory(0x6637EC, Add, -512),# units:Staredit Group Flags  index:77    from 12 To 10
        SetMemory(0x6637EC, Add, -33554432),# units:Staredit Group Flags  index:79    from 12 To 10
        SetMemory(0x6637F0, Add, -2),# units:Staredit Group Flags  index:80    from 12 To 10
        SetMemory(0x6637F0, Add, -131072),# units:Staredit Group Flags  index:82    from 12 To 10
        SetMemory(0x6637F4, Add, -131072),# units:Staredit Group Flags  index:86    from 12 To 10
        SetMemory(0x6637F8, Add, -2),# units:Staredit Group Flags  index:88    from 12 To 10
        SetMemory(0x66380C, Add, 28160),# units:Staredit Group Flags  index:109    from 18 To 128
        SetMemory(0x663810, Add, -134217728),# units:Staredit Group Flags  index:115    from 18 To 10
        SetMemory(0x663820, Add, -2555904),# units:Staredit Group Flags  index:130    from 49 To 10
        SetMemory(0x663830, Add, -7),# units:Staredit Group Flags  index:144    from 17 To 10
        SetMemory(0x664734, Add, -4096),# units:Supply Provided  index:109    from 16 To 0
        SetMemory(0x663CE8, Add, -262144),# units:Supply Required  index:2    from 4 To 0
        SetMemory(0x663CF0, Add, -4),# units:Supply Required  index:8    from 4 To 0
        SetMemory(0x663CF4, Add, -12),# units:Supply Required  index:12    from 12 To 0
        SetMemory(0x663D08, Add, -131072),# units:Supply Required  index:34    from 2 To 0
        SetMemory(0x663D24, Add, -4),# units:Supply Required  index:60    from 4 To 0
        SetMemory(0x663D2C, Add, -1024),# units:Supply Required  index:69    from 4 To 0
        SetMemory(0x663D2C, Add, -393216),# units:Supply Required  index:70    from 6 To 0
        SetMemory(0x663D2C, Add, -134217728),# units:Supply Required  index:71    from 8 To 0
        SetMemory(0x663D30, Add, -12),# units:Supply Required  index:72    from 12 To 0
        SetMemory(0x663D38, Add, -134217728),# units:Supply Required  index:83    from 8 To 0
        SetMemory(0x663D3C, Add, -2),# units:Supply Required  index:84    from 2 To 0
        SetMemory(0x664430, Add, 65536),# units:Space Required  index:34    from 1 To 2
        SetMemory(0x66344C, Add, -125),# units:Build Score  index:34    from 125 To 0
        SetMemory(0x6634CC, Add, 1025),# units:Build Score  index:98    from 0 To 1025
        SetMemory(0x6634E0, Add, -3276800),# units:Build Score  index:109    from 50 To 0
        SetMemory(0x6634EC, Add, -6553600),# units:Build Score  index:115    from 100 To 0
        SetMemory(0x663EBC, Add, 9850),# units:Destroy Score  index:2    from 150 To 10000
        SetMemory(0x663EFC, Add, 1150),# units:Destroy Score  index:34    from 250 To 1400
        SetMemory(0x663F04, Add, 570163200),# units:Destroy Score  index:39    from 1300 To 10000
        SetMemory(0x663F08, Add, 9975),# units:Destroy Score  index:40    from 25 To 10000
        SetMemory(0x663F1C, Add, -262144000),# units:Destroy Score  index:51    from 4000 To 0
        SetMemory(0x663F7C, Add, 750),# units:Destroy Score  index:98    from 1300 To 2050
        SetMemory(0x663F90, Add, -9830400),# units:Destroy Score  index:109    from 150 To 0
        SetMemory(0x663F9C, Add, 150732800),# units:Destroy Score  index:115    from 300 To 2600
        SetMemory(0x663FDC, Add, -240),# units:Destroy Score  index:146    from 240 To 0
        SetMemory(0x663FFC, Add, -300),# units:Destroy Score  index:162    from 300 To 0
        SetMemory(0x6606F8, Add, -65536),# units:Broodwar Unit Flag  index:34    from 1 To 0
        SetMemory(0x66154C, Add, 29556736),# units:Staredit Availability Flags  index:27    from 4 To 455
        SetMemory(0x66155C, Add, -512),# units:Staredit Availability Flags  index:34    from 975 To 463
        SetMemory(0x6615C4, Add, 30081024),# units:Staredit Availability Flags  index:87    from 4 To 463
        SetMemory(0x6615DC, Add, 459),# units:Staredit Availability Flags  index:98    from 4 To 463
        SetMemory(0x6615F0, Add, -7864320),# units:Staredit Availability Flags  index:109    from 463 To 343
        SetMemory(0x6615FC, Add, -524288),# units:Staredit Availability Flags  index:115    from 463 To 455
        SetMemory(0x6572E0, Add, -65536),# weapons:Label  index:1    from 230 To 229
        SetMemory(0x6572E4, Add, -2),# weapons:Label  index:2    from 231 To 229
        SetMemory(0x6572E4, Add, -196608),# weapons:Label  index:3    from 232 To 229
        SetMemory(0x6572E8, Add, -4),# weapons:Label  index:4    from 233 To 229
        SetMemory(0x6572E8, Add, -327680),# weapons:Label  index:5    from 234 To 229
        SetMemory(0x6572EC, Add, -87),# weapons:Label  index:6    from 316 To 229
        SetMemory(0x6572EC, Add, -393216),# weapons:Label  index:7    from 235 To 229
        SetMemory(0x6572F0, Add, -7),# weapons:Label  index:8    from 236 To 229
        SetMemory(0x6572F0, Add, -524288),# weapons:Label  index:9    from 237 To 229
        SetMemory(0x6572F4, Add, -9),# weapons:Label  index:10    from 238 To 229
        SetMemory(0x6572F4, Add, -655360),# weapons:Label  index:11    from 239 To 229
        SetMemory(0x6572F8, Add, -11),# weapons:Label  index:12    from 240 To 229
        SetMemory(0x6572F8, Add, -786432),# weapons:Label  index:13    from 241 To 229
        SetMemory(0x6572FC, Add, -13),# weapons:Label  index:14    from 242 To 229
        SetMemory(0x6572FC, Add, -917504),# weapons:Label  index:15    from 243 To 229
        SetMemory(0x657300, Add, -15),# weapons:Label  index:16    from 244 To 229
        SetMemory(0x657300, Add, -1048576),# weapons:Label  index:17    from 245 To 229
        SetMemory(0x657304, Add, -17),# weapons:Label  index:18    from 246 To 229
        SetMemory(0x657304, Add, -1179648),# weapons:Label  index:19    from 247 To 229
        SetMemory(0x657308, Add, -19),# weapons:Label  index:20    from 248 To 229
        SetMemory(0x657308, Add, -1310720),# weapons:Label  index:21    from 249 To 229
        SetMemory(0x65730C, Add, -21),# weapons:Label  index:22    from 250 To 229
        SetMemory(0x65730C, Add, -1441792),# weapons:Label  index:23    from 251 To 229
        SetMemory(0x657310, Add, -23),# weapons:Label  index:24    from 252 To 229
        SetMemory(0x657310, Add, -1572864),# weapons:Label  index:25    from 253 To 229
        SetMemory(0x657314, Add, -25),# weapons:Label  index:26    from 254 To 229
        SetMemory(0x657314, Add, -1703936),# weapons:Label  index:27    from 255 To 229
        SetMemory(0x657318, Add, -27),# weapons:Label  index:28    from 256 To 229
        SetMemory(0x657318, Add, -1835008),# weapons:Label  index:29    from 257 To 229
        SetMemory(0x65731C, Add, -92),# weapons:Label  index:30    from 321 To 229
        SetMemory(0x657324, Add, -2031616),# weapons:Label  index:35    from 260 To 229
        SetMemory(0x657328, Add, -32),# weapons:Label  index:36    from 261 To 229
        SetMemory(0x657328, Add, -2162688),# weapons:Label  index:37    from 262 To 229
        SetMemory(0x65732C, Add, -34),# weapons:Label  index:38    from 263 To 229
        SetMemory(0x65732C, Add, -2293760),# weapons:Label  index:39    from 264 To 229
        SetMemory(0x657330, Add, -36),# weapons:Label  index:40    from 265 To 229
        SetMemory(0x657330, Add, -2424832),# weapons:Label  index:41    from 266 To 229
        SetMemory(0x657334, Add, -38),# weapons:Label  index:42    from 267 To 229
        SetMemory(0x657334, Add, -2555904),# weapons:Label  index:43    from 268 To 229
        SetMemory(0x657338, Add, -39),# weapons:Label  index:44    from 268 To 229
        SetMemory(0x657338, Add, -2686976),# weapons:Label  index:45    from 270 To 229
        SetMemory(0x65733C, Add, -42),# weapons:Label  index:46    from 271 To 229
        SetMemory(0x65733C, Add, -2818048),# weapons:Label  index:47    from 272 To 229
        SetMemory(0x657340, Add, -44),# weapons:Label  index:48    from 273 To 229
        SetMemory(0x657340, Add, -2949120),# weapons:Label  index:49    from 274 To 229
        SetMemory(0x657344, Add, -46),# weapons:Label  index:50    from 275 To 229
        SetMemory(0x657344, Add, -3080192),# weapons:Label  index:51    from 276 To 229
        SetMemory(0x65735C, Add, -52),# weapons:Label  index:62    from 281 To 229
        SetMemory(0x65735C, Add, -3407872),# weapons:Label  index:63    from 281 To 229
        SetMemory(0x657360, Add, -53),# weapons:Label  index:64    from 282 To 229
        SetMemory(0x657360, Add, -3538944),# weapons:Label  index:65    from 283 To 229
        SetMemory(0x657364, Add, -57),# weapons:Label  index:66    from 286 To 229
        SetMemory(0x657364, Add, -3801088),# weapons:Label  index:67    from 287 To 229
        SetMemory(0x657368, Add, -59),# weapons:Label  index:68    from 288 To 229
        SetMemory(0x657368, Add, -65536),# weapons:Label  index:69    from 289 To 288
        SetMemory(0x65736C, Add, -61),# weapons:Label  index:70    from 290 To 229
        SetMemory(0x65736C, Add, -4063232),# weapons:Label  index:71    from 291 To 229
        SetMemory(0x657370, Add, -4194304),# weapons:Label  index:73    from 293 To 229
        SetMemory(0x657374, Add, -65),# weapons:Label  index:74    from 294 To 229
        SetMemory(0x657374, Add, -4325376),# weapons:Label  index:75    from 295 To 229
        SetMemory(0x657378, Add, -67),# weapons:Label  index:76    from 296 To 229
        SetMemory(0x657378, Add, -4456448),# weapons:Label  index:77    from 297 To 229
        SetMemory(0x65737C, Add, -69),# weapons:Label  index:78    from 298 To 229
        SetMemory(0x65737C, Add, -4587520),# weapons:Label  index:79    from 299 To 229
        SetMemory(0x657388, Add, -3670016),# weapons:Label  index:85    from 285 To 229
        SetMemory(0x65738C, Add, -55),# weapons:Label  index:86    from 284 To 229
        SetMemory(0x6573A0, Add, -80),# weapons:Label  index:96    from 309 To 229
        SetMemory(0x6573A0, Add, -5308416),# weapons:Label  index:97    from 310 To 229
        SetMemory(0x6573A4, Add, -5308416),# weapons:Label  index:99    from 310 To 229
        SetMemory(0x6573B0, Add, -1009),# weapons:Label  index:104    from 1238 To 229
        SetMemory(0x6573BC, Add, -3604480),# weapons:Label  index:111    from 284 To 229
        SetMemory(0x6573C0, Add, -2),# weapons:Label  index:112    from 231 To 229
        SetMemory(0x6573C0, Add, -131072),# weapons:Label  index:113    from 231 To 229
        SetMemory(0x6573C4, Add, -64),# weapons:Label  index:114    from 293 To 229
        SetMemory(0x6573C4, Add, -4259840),# weapons:Label  index:115    from 294 To 229
        SetMemory(0x6573C8, Add, -2),# weapons:Label  index:116    from 231 To 229
        SetMemory(0x657A00, Add, 2),# weapons:Target Flags  index:52    from 1 To 3
        SetMemory(0x657A14, Add, 0),# weapons:Target Flags  index:62    from 2 To 2
        SetMemory(0x656A84, Add, -64),# weapons:Minimum Range  index:27    from 64 To 0
        SetMemory(0x656A88, Add, -64),# weapons:Minimum Range  index:28    from 64 To 0
        SetMemory(0x657470, Add, 32),# weapons:Maximum Range  index:0    from 128 To 160
        SetMemory(0x6574D4, Add, -17),# weapons:Maximum Range  index:25    from 32 To 15
        SetMemory(0x6574DC, Add, -30),# weapons:Maximum Range  index:27    from 384 To 354
        SetMemory(0x6574E0, Add, 96),# weapons:Maximum Range  index:28    from 384 To 480
        SetMemory(0x6574E4, Add, -128),# weapons:Maximum Range  index:29    from 224 To 96
        SetMemory(0x6574FC, Add, 113),# weapons:Maximum Range  index:35    from 15 To 128
        SetMemory(0x657500, Add, 17),# weapons:Maximum Range  index:36    from 15 To 32
        SetMemory(0x657510, Add, 39),# weapons:Maximum Range  index:40    from 25 To 64
        SetMemory(0x657514, Add, 39),# weapons:Maximum Range  index:41    from 25 To 64
        SetMemory(0x657518, Add, 14),# weapons:Maximum Range  index:42    from 2 To 16
        SetMemory(0x65751C, Add, 96),# weapons:Maximum Range  index:43    from 32 To 128
        SetMemory(0x657530, Add, 32),# weapons:Maximum Range  index:48    from 96 To 128
        SetMemory(0x657534, Add, 32),# weapons:Maximum Range  index:49    from 96 To 128
        SetMemory(0x657558, Add, -160),# weapons:Maximum Range  index:58    from 288 To 128
        SetMemory(0x657568, Add, 96),# weapons:Maximum Range  index:62    from 32 To 128
        SetMemory(0x657570, Add, 81),# weapons:Maximum Range  index:64    from 15 To 96
        SetMemory(0x657574, Add, 17),# weapons:Maximum Range  index:65    from 15 To 32
        SetMemory(0x657578, Add, 32),# weapons:Maximum Range  index:66    from 128 To 160
        SetMemory(0x65757C, Add, 128),# weapons:Maximum Range  index:67    from 128 To 256
        SetMemory(0x657580, Add, 64),# weapons:Maximum Range  index:68    from 96 To 160
        SetMemory(0x657584, Add, 96),# weapons:Maximum Range  index:69    from 96 To 192
        SetMemory(0x657588, Add, 290),# weapons:Maximum Range  index:70    from 64 To 354
        SetMemory(0x65758C, Add, 290),# weapons:Maximum Range  index:71    from 64 To 354
        SetMemory(0x657594, Add, 128),# weapons:Maximum Range  index:73    from 128 To 256
        SetMemory(0x6575A4, Add, 160),# weapons:Maximum Range  index:77    from 160 To 320
        SetMemory(0x6575C4, Add, 305),# weapons:Maximum Range  index:85    from 15 To 320
        SetMemory(0x6575C8, Add, 17),# weapons:Maximum Range  index:86    from 15 To 32
        SetMemory(0x65762C, Add, 49),# weapons:Maximum Range  index:111    from 15 To 64
        SetMemory(0x657634, Add, 64),# weapons:Maximum Range  index:113    from 192 To 256
        SetMemory(0x657640, Add, 64),# weapons:Maximum Range  index:116    from 192 To 256
        SetMemory(0x6571D0, Add, 2),# weapons:Damage Upgrade  index:0    from 7 To 9
        SetMemory(0x6571D0, Add, 512),# weapons:Damage Upgrade  index:1    from 7 To 9
        SetMemory(0x6571D0, Add, 131072),# weapons:Damage Upgrade  index:2    from 7 To 9
        SetMemory(0x6571D0, Add, 33554432),# weapons:Damage Upgrade  index:3    from 7 To 9
        SetMemory(0x6571D4, Add, 1),# weapons:Damage Upgrade  index:4    from 8 To 9
        SetMemory(0x6571D4, Add, 256),# weapons:Damage Upgrade  index:5    from 8 To 9
        SetMemory(0x6571D4, Add, 16777216),# weapons:Damage Upgrade  index:7    from 8 To 9
        SetMemory(0x6571D8, Add, 1),# weapons:Damage Upgrade  index:8    from 8 To 9
        SetMemory(0x6571D8, Add, 256),# weapons:Damage Upgrade  index:9    from 8 To 9
        SetMemory(0x6571D8, Add, 65536),# weapons:Damage Upgrade  index:10    from 8 To 9
        SetMemory(0x6571D8, Add, 16777216),# weapons:Damage Upgrade  index:11    from 8 To 9
        SetMemory(0x6571DC, Add, 1),# weapons:Damage Upgrade  index:12    from 8 To 9
        SetMemory(0x6571DC, Add, -13056),# weapons:Damage Upgrade  index:13    from 60 To 9
        SetMemory(0x6571DC, Add, -3342336),# weapons:Damage Upgrade  index:14    from 60 To 9
        SetMemory(0x6571E8, Add, 512),# weapons:Damage Upgrade  index:25    from 7 To 9
        SetMemory(0x6571E8, Add, 131072),# weapons:Damage Upgrade  index:26    from 7 To 9
        SetMemory(0x6571E8, Add, 16777216),# weapons:Damage Upgrade  index:27    from 8 To 9
        SetMemory(0x6571EC, Add, 1),# weapons:Damage Upgrade  index:28    from 8 To 9
        SetMemory(0x6571EC, Add, -13056),# weapons:Damage Upgrade  index:29    from 60 To 9
        SetMemory(0x6571EC, Add, -3342336),# weapons:Damage Upgrade  index:30    from 60 To 9
        SetMemory(0x6571F0, Add, -16777216),# weapons:Damage Upgrade  index:35    from 10 To 9
        SetMemory(0x6571F4, Add, -1),# weapons:Damage Upgrade  index:36    from 10 To 9
        SetMemory(0x6571F4, Add, -256),# weapons:Damage Upgrade  index:37    from 10 To 9
        SetMemory(0x6571F4, Add, -131072),# weapons:Damage Upgrade  index:38    from 11 To 9
        SetMemory(0x6571F4, Add, -33554432),# weapons:Damage Upgrade  index:39    from 11 To 9
        SetMemory(0x6571F8, Add, -1),# weapons:Damage Upgrade  index:40    from 10 To 9
        SetMemory(0x6571F8, Add, -256),# weapons:Damage Upgrade  index:41    from 10 To 9
        SetMemory(0x6571F8, Add, -65536),# weapons:Damage Upgrade  index:42    from 10 To 9
        SetMemory(0x6571F8, Add, -855638016),# weapons:Damage Upgrade  index:43    from 60 To 9
        SetMemory(0x6571FC, Add, -51),# weapons:Damage Upgrade  index:44    from 60 To 9
        SetMemory(0x6571FC, Add, -768),# weapons:Damage Upgrade  index:45    from 12 To 9
        SetMemory(0x6571FC, Add, -196608),# weapons:Damage Upgrade  index:46    from 12 To 9
        SetMemory(0x6571FC, Add, -50331648),# weapons:Damage Upgrade  index:47    from 12 To 9
        SetMemory(0x657200, Add, -3),# weapons:Damage Upgrade  index:48    from 12 To 9
        SetMemory(0x657200, Add, -768),# weapons:Damage Upgrade  index:49    from 12 To 9
        SetMemory(0x657200, Add, -131072),# weapons:Damage Upgrade  index:50    from 11 To 9
        SetMemory(0x657200, Add, -33554432),# weapons:Damage Upgrade  index:51    from 11 To 9
        SetMemory(0x657204, Add, -51),# weapons:Damage Upgrade  index:52    from 60 To 9
        SetMemory(0x657204, Add, -13056),# weapons:Damage Upgrade  index:53    from 60 To 9
        SetMemory(0x65720C, Add, -3342336),# weapons:Damage Upgrade  index:62    from 60 To 9
        SetMemory(0x65720C, Add, -855638016),# weapons:Damage Upgrade  index:63    from 60 To 9
        SetMemory(0x657210, Add, -4),# weapons:Damage Upgrade  index:64    from 13 To 9
        SetMemory(0x657210, Add, -1024),# weapons:Damage Upgrade  index:65    from 13 To 9
        SetMemory(0x657210, Add, -262144),# weapons:Damage Upgrade  index:66    from 13 To 9
        SetMemory(0x657210, Add, -67108864),# weapons:Damage Upgrade  index:67    from 13 To 9
        SetMemory(0x657214, Add, -4),# weapons:Damage Upgrade  index:68    from 13 To 9
        SetMemory(0x657214, Add, -1024),# weapons:Damage Upgrade  index:69    from 13 To 9
        SetMemory(0x657214, Add, -262144),# weapons:Damage Upgrade  index:70    from 13 To 9
        SetMemory(0x657214, Add, -67108864),# weapons:Damage Upgrade  index:71    from 13 To 9
        SetMemory(0x657218, Add, -5),# weapons:Damage Upgrade  index:72    from 14 To 9
        SetMemory(0x657218, Add, -1280),# weapons:Damage Upgrade  index:73    from 14 To 9
        SetMemory(0x657218, Add, -327680),# weapons:Damage Upgrade  index:74    from 14 To 9
        SetMemory(0x657218, Add, -83886080),# weapons:Damage Upgrade  index:75    from 14 To 9
        SetMemory(0x65721C, Add, -5),# weapons:Damage Upgrade  index:76    from 14 To 9
        SetMemory(0x65721C, Add, -1280),# weapons:Damage Upgrade  index:77    from 14 To 9
        SetMemory(0x65721C, Add, -327680),# weapons:Damage Upgrade  index:78    from 14 To 9
        SetMemory(0x65721C, Add, -83886080),# weapons:Damage Upgrade  index:79    from 14 To 9
        SetMemory(0x657224, Add, -1024),# weapons:Damage Upgrade  index:85    from 13 To 9
        SetMemory(0x657224, Add, -262144),# weapons:Damage Upgrade  index:86    from 13 To 9
        SetMemory(0x657230, Add, 1),# weapons:Damage Upgrade  index:96    from 8 To 9
        SetMemory(0x657230, Add, 256),# weapons:Damage Upgrade  index:97    from 8 To 9
        SetMemory(0x657230, Add, 16777216),# weapons:Damage Upgrade  index:99    from 8 To 9
        SetMemory(0x657234, Add, -5),# weapons:Damage Upgrade  index:100    from 14 To 9
        SetMemory(0x657238, Add, -3),# weapons:Damage Upgrade  index:104    from 12 To 9
        SetMemory(0x65723C, Add, -512),# weapons:Damage Upgrade  index:109    from 11 To 9
        SetMemory(0x65723C, Add, -67108864),# weapons:Damage Upgrade  index:111    from 13 To 9
        SetMemory(0x657240, Add, 2),# weapons:Damage Upgrade  index:112    from 7 To 9
        SetMemory(0x657240, Add, 512),# weapons:Damage Upgrade  index:113    from 7 To 9
        SetMemory(0x657240, Add, -327680),# weapons:Damage Upgrade  index:114    from 14 To 9
        SetMemory(0x657240, Add, -83886080),# weapons:Damage Upgrade  index:115    from 14 To 9
        SetMemory(0x657244, Add, 2),# weapons:Damage Upgrade  index:116    from 7 To 9
        SetMemory(0x657270, Add, -256),# weapons:Weapon Type  index:25    from 2 To 1
        SetMemory(0x657270, Add, -65536),# weapons:Weapon Type  index:26    from 2 To 1
        SetMemory(0x657288, Add, -16777216),# weapons:Weapon Type  index:51    from 2 To 1
        SetMemory(0x65728C, Add, 512),# weapons:Weapon Type  index:53    from 1 To 3
        SetMemory(0x65729C, Add, -2),# weapons:Weapon Type  index:68    from 3 To 1
        SetMemory(0x6572A0, Add, -256),# weapons:Weapon Type  index:73    from 3 To 2
        SetMemory(0x6572CC, Add, 1),# weapons:Weapon Type  index:116    from 2 To 3
        SetMemory(0x6566A0, Add, -6),# weapons:Weapon Behavior  index:48    from 7 To 1
        SetMemory(0x6566A0, Add, -1536),# weapons:Weapon Behavior  index:49    from 7 To 1
        SetMemory(0x6566A8, Add, -65536),# weapons:Weapon Behavior  index:58    from 1 To 0
        SetMemory(0x656710, Add, -512),# weapons:Explosion Type  index:25    from 3 To 1
        SetMemory(0x656710, Add, 16777216),# weapons:Explosion Type  index:27    from 2 To 3
        SetMemory(0x656714, Add, 1),# weapons:Explosion Type  index:28    from 2 To 3
        SetMemory(0x656728, Add, -33554432),# weapons:Explosion Type  index:51    from 2 To 0
        SetMemory(0x6568B8, Add, -983040),# weapons:Inner Splash Range  index:25    from 15 To 0
        SetMemory(0x6568EC, Add, -655360),# weapons:Inner Splash Range  index:51    from 10 To 0
        SetMemory(0x6570F8, Add, -1310720),# weapons:Medium Splash Range  index:25    from 20 To 0
        SetMemory(0x65712C, Add, -1310720),# weapons:Medium Splash Range  index:51    from 20 To 0
        SetMemory(0x6577B0, Add, -1638400),# weapons:Outer Splash Range  index:25    from 25 To 0
        SetMemory(0x6577E4, Add, -1966080),# weapons:Outer Splash Range  index:51    from 30 To 0
        SetMemory(0x656F14, Add, 4587520),# weapons:Damage Amount  index:51    from 10 To 80
        SetMemory(0x656F38, Add, 55),# weapons:Damage Amount  index:68    from 5 To 60
        SetMemory(0x656F38, Add, 0),# weapons:Damage Amount  index:69    from 350 To 350
        SetMemory(0x656F40, Add, 2097152),# weapons:Damage Amount  index:73    from 8 To 40
        SetMemory(0x656FD0, Add, 2048),# weapons:Weapon Cooldown  index:25    from 22 To 30
        SetMemory(0x656FD8, Add, 234881024),# weapons:Weapon Cooldown  index:35    from 8 To 22
        SetMemory(0x656FDC, Add, 14),# weapons:Weapon Cooldown  index:36    from 8 To 22
        SetMemory(0x656FEC, Add, 7),# weapons:Weapon Cooldown  index:52    from 15 To 22
        SetMemory(0x656FF0, Add, 16318464),# weapons:Weapon Cooldown  index:58    from 1 To 250
        SetMemory(0x656FF8, Add, -393216),# weapons:Weapon Cooldown  index:66    from 30 To 24
        SetMemory(0x656FFC, Add, -15),# weapons:Weapon Cooldown  index:68    from 30 To 15
        SetMemory(0x656990, Add, 112),# weapons:Attack Angle  index:0    from 16 To 128
        SetMemory(0x656990, Add, 28672),# weapons:Attack Angle  index:1    from 16 To 128
        SetMemory(0x656990, Add, 7340032),# weapons:Attack Angle  index:2    from 16 To 128
        SetMemory(0x656990, Add, 1879048192),# weapons:Attack Angle  index:3    from 16 To 128
        SetMemory(0x656994, Add, 64),# weapons:Attack Angle  index:4    from 64 To 128
        SetMemory(0x656994, Add, 16384),# weapons:Attack Angle  index:5    from 64 To 128
        SetMemory(0x656994, Add, 1879048192),# weapons:Attack Angle  index:7    from 16 To 128
        SetMemory(0x656998, Add, 28672),# weapons:Attack Angle  index:9    from 16 To 128
        SetMemory(0x6569A0, Add, 112),# weapons:Attack Angle  index:16    from 16 To 128
        SetMemory(0x6569A0, Add, 7340032),# weapons:Attack Angle  index:18    from 16 To 128
        SetMemory(0x6569A0, Add, 1879048192),# weapons:Attack Angle  index:19    from 16 To 128
        SetMemory(0x6569A4, Add, 112),# weapons:Attack Angle  index:20    from 16 To 128
        SetMemory(0x6569A4, Add, 7340032),# weapons:Attack Angle  index:22    from 16 To 128
        SetMemory(0x6569A4, Add, 1879048192),# weapons:Attack Angle  index:23    from 16 To 128
        SetMemory(0x6569A8, Add, 112),# weapons:Attack Angle  index:24    from 16 To 128
        SetMemory(0x6569B4, Add, 112),# weapons:Attack Angle  index:36    from 16 To 128
        SetMemory(0x6569B4, Add, 28672),# weapons:Attack Angle  index:37    from 16 To 128
        SetMemory(0x6569B4, Add, 1879048192),# weapons:Attack Angle  index:39    from 16 To 128
        SetMemory(0x6569B8, Add, 1879048192),# weapons:Attack Angle  index:43    from 16 To 128
        SetMemory(0x6569BC, Add, 7340032),# weapons:Attack Angle  index:46    from 16 To 128
        SetMemory(0x6569BC, Add, 1879048192),# weapons:Attack Angle  index:47    from 16 To 128
        SetMemory(0x6569C0, Add, 112),# weapons:Attack Angle  index:48    from 16 To 128
        SetMemory(0x6569C0, Add, 28672),# weapons:Attack Angle  index:49    from 16 To 128
        SetMemory(0x6569CC, Add, 7340032),# weapons:Attack Angle  index:62    from 16 To 128
        SetMemory(0x6569D0, Add, 28672),# weapons:Attack Angle  index:65    from 16 To 128
        SetMemory(0x6569D4, Add, 112),# weapons:Attack Angle  index:68    from 16 To 128
        SetMemory(0x6569D4, Add, 7340032),# weapons:Attack Angle  index:70    from 16 To 128
        SetMemory(0x6569D4, Add, 1879048192),# weapons:Attack Angle  index:71    from 16 To 128
        SetMemory(0x6569D8, Add, 28672),# weapons:Attack Angle  index:73    from 16 To 128
        SetMemory(0x6569D8, Add, 1879048192),# weapons:Attack Angle  index:75    from 16 To 128
        SetMemory(0x6569DC, Add, 28672),# weapons:Attack Angle  index:77    from 16 To 128
        SetMemory(0x6569DC, Add, 7340032),# weapons:Attack Angle  index:78    from 16 To 128
        SetMemory(0x6569E4, Add, 7340032),# weapons:Attack Angle  index:86    from 16 To 128
        SetMemory(0x6569FC, Add, 1879048192),# weapons:Attack Angle  index:111    from 16 To 128
        SetMemory(0x656A00, Add, 112),# weapons:Attack Angle  index:112    from 16 To 128
        SetMemory(0x656A00, Add, 28672),# weapons:Attack Angle  index:113    from 16 To 128
        SetMemory(0x656A00, Add, 7340032),# weapons:Attack Angle  index:114    from 16 To 128
        SetMemory(0x656A04, Add, 112),# weapons:Attack Angle  index:116    from 16 To 128
        SetMemory(0x6C9EF8, Add, 1706),# flingy:Speed  index:0    from 1707 To 3413
        SetMemory(0x6C9F18, Add, 829),# flingy:Speed  index:8    from 1 To 830
        SetMemory(0x6C9F1C, Add, 1279),# flingy:Speed  index:9    from 1 To 1280
        SetMemory(0x6C9F34, Add, 829),# flingy:Speed  index:15    from 1 To 830
        SetMemory(0x6C9F94, Add, 427),# flingy:Speed  index:39    from 853 To 1280
        SetMemory(0x6C9FA4, Add, -1024),# flingy:Speed  index:43    from 1280 To 256
        SetMemory(0x6C9FAC, Add, 427),# flingy:Speed  index:45    from 853 To 1280
        SetMemory(0x6C9FB0, Add, 427),# flingy:Speed  index:46    from 853 To 1280
        SetMemory(0x6C9FBC, Add, 829),# flingy:Speed  index:49    from 1 To 830
        SetMemory(0x6CA010, Add, 384),# flingy:Speed  index:70    from 640 To 1024
        SetMemory(0x6CA01C, Add, 1279),# flingy:Speed  index:73    from 1 To 1280
        SetMemory(0x6CA020, Add, 1279),# flingy:Speed  index:74    from 1 To 1280
        SetMemory(0x6CA02C, Add, 1279),# flingy:Speed  index:77    from 1 To 1280
        SetMemory(0x6CA058, Add, -683),# flingy:Speed  index:88    from 1707 To 1024
        SetMemory(0x6CA170, Add, -4533),# flingy:Speed  index:158    from 8533 To 4000
        SetMemory(0x6CA1EC, Add, 1279),# flingy:Speed  index:189    from 1 To 1280
        SetMemory(0x6C9C88, Add, 829),# flingy:Acceleration  index:8    from 1 To 830
        SetMemory(0x6C9C88, Add, 83820544),# flingy:Acceleration  index:9    from 1 To 1280
        SetMemory(0x6C9C94, Add, 54329344),# flingy:Acceleration  index:15    from 1 To 830
        SetMemory(0x6C9CC4, Add, 393216),# flingy:Acceleration  index:39    from 27 To 33
        SetMemory(0x6C9CCC, Add, -1048576),# flingy:Acceleration  index:43    from 48 To 32
        SetMemory(0x6C9CD0, Add, 82116608),# flingy:Acceleration  index:45    from 27 To 1280
        SetMemory(0x6C9CD4, Add, 1253),# flingy:Acceleration  index:46    from 27 To 1280
        SetMemory(0x6C9CD8, Add, 54329344),# flingy:Acceleration  index:49    from 1 To 830
        SetMemory(0x6C9D04, Add, 6),# flingy:Acceleration  index:70    from 27 To 33
        SetMemory(0x6C9D08, Add, 83820544),# flingy:Acceleration  index:73    from 1 To 1280
        SetMemory(0x6C9D0C, Add, 1279),# flingy:Acceleration  index:74    from 1 To 1280
        SetMemory(0x6C9D10, Add, 83820544),# flingy:Acceleration  index:77    from 1 To 1280
        SetMemory(0x6C9DB4, Add, -4533),# flingy:Acceleration  index:158    from 8533 To 4000
        SetMemory(0x6C9DF0, Add, 83820544),# flingy:Acceleration  index:189    from 1 To 1280
        SetMemory(0x6C9E04, Add, 3145728),# flingy:Acceleration  index:199    from 16 To 64
        SetMemory(0x6C9950, Add, -1),# flingy:Halt Distance  index:8    from 1 To 0
        SetMemory(0x6C9954, Add, -1),# flingy:Halt Distance  index:9    from 1 To 0
        SetMemory(0x6C99CC, Add, 11350),# flingy:Halt Distance  index:39    from 13474 To 24824
        SetMemory(0x6C99DC, Add, -16811),# flingy:Halt Distance  index:43    from 17067 To 256
        SetMemory(0x6C99E4, Add, -13474),# flingy:Halt Distance  index:45    from 13474 To 0
        SetMemory(0x6C99E8, Add, -13474),# flingy:Halt Distance  index:46    from 13474 To 0
        SetMemory(0x6C99F4, Add, -1),# flingy:Halt Distance  index:49    from 1 To 0
        SetMemory(0x6C9A48, Add, 17239),# flingy:Halt Distance  index:70    from 7585 To 24824
        SetMemory(0x6C9A54, Add, -1),# flingy:Halt Distance  index:73    from 1 To 0
        SetMemory(0x6C9A58, Add, -1),# flingy:Halt Distance  index:74    from 1 To 0
        SetMemory(0x6C9A64, Add, -1),# flingy:Halt Distance  index:77    from 1 To 0
        SetMemory(0x6C9A90, Add, -14569),# flingy:Halt Distance  index:88    from 14569 To 0
        SetMemory(0x6C9BA8, Add, -2267),# flingy:Halt Distance  index:158    from 4267 To 2000
        SetMemory(0x6C9C24, Add, -1),# flingy:Halt Distance  index:189    from 1 To 0
        SetMemory(0x6C9E28, Add, -3328),# flingy:Turn Radius  index:9    from 40 To 27
        SetMemory(0x6C9E44, Add, 335544320),# flingy:Turn Radius  index:39    from 20 To 40
        SetMemory(0x6C9E4C, Add, -851968),# flingy:Turn Radius  index:46    from 40 To 27
        SetMemory(0x6C9E50, Add, -1536),# flingy:Turn Radius  index:49    from 40 To 34
        SetMemory(0x6C9E64, Add, 1310720),# flingy:Turn Radius  index:70    from 20 To 40
        SetMemory(0x6C9E68, Add, -851968),# flingy:Turn Radius  index:74    from 40 To 27
        SetMemory(0x6C9EDC, Add, -3328),# flingy:Turn Radius  index:189    from 40 To 27
        SetMemory(0x6C9860, Add, -2),# flingy:Movement Control  index:8    from 2 To 0
        SetMemory(0x6C9860, Add, -512),# flingy:Movement Control  index:9    from 2 To 0
        SetMemory(0x6C9864, Add, -33554432),# flingy:Movement Control  index:15    from 2 To 0
        SetMemory(0x6C9884, Add, -256),# flingy:Movement Control  index:45    from 1 To 0
        SetMemory(0x6C9884, Add, -131072),# flingy:Movement Control  index:46    from 2 To 0
        SetMemory(0x6C9888, Add, -512),# flingy:Movement Control  index:49    from 2 To 0
        SetMemory(0x6C98A0, Add, -512),# flingy:Movement Control  index:73    from 2 To 0
        SetMemory(0x6C98A0, Add, -131072),# flingy:Movement Control  index:74    from 2 To 0
        SetMemory(0x6C98A4, Add, -512),# flingy:Movement Control  index:77    from 2 To 0
        SetMemory(0x6C9914, Add, -512),# flingy:Movement Control  index:189    from 2 To 0
        SetMemory(0x666364, Add, 184),# sprites:Image File  index:258    from 293 To 477
        SetMemory(0x666368, Add, 12582912),# sprites:Image File  index:261    from 301 To 493
        SetMemory(0x6663A4, Add, -1900544),# sprites:Image File  index:291    from 396 To 367
        SetMemory(0x669E88, Add, 33554432),# images:Draw Function  index:99    from 0 To 2
        SetMemory(0x669F88, Add, 2560),# images:Draw Function  index:353    from 0 To 10
        SetMemory(0x66A044, Add, 4096),# images:Draw Function  index:541    from 0 To 16
        SetMemory(0x66EDD4, Add, 120),# images:Iscript ID  index:99    from 59 To 179
        SetMemory(0x66F1CC, Add, -46),# images:Iscript ID  index:353    from 207 To 161
        SetMemory(0x655AC4, Add, 1),# upgrades:Icon  index:2    from 291 To 292
        SetMemory(0x655A44, Add, -2),# upgrades:Label  index:2    from 413 To 411
    ])

