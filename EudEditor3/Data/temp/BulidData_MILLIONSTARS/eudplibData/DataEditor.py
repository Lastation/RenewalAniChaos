from eudplib import *


def onPluginStart():
    DoActions([  # Basic DatFile Actions
        SetMemory(0x664534, Add, -191),# units:Graphics  index:60    from 191 To 0
        SetMemory(0x664548, Add, -788529152),# units:Graphics  index:83    from 47 To 0
        SetMemory(0x66454C, Add, -50),# units:Graphics  index:84    from 50 To 0
        SetMemory(0x664554, Add, -49408),# units:Graphics  index:93    from 198 To 5
        SetMemory(0x664554, Add, -10289152),# units:Graphics  index:94    from 199 To 42
        SetMemory(0x664554, Add, -553648128),# units:Graphics  index:95    from 114 To 81
        SetMemory(0x664564, Add, -335544320),# units:Graphics  index:111    from 91 To 71
        SetMemory(0x66457C, Add, -2560),# units:Graphics  index:133    from 23 To 13
        SetMemory(0x66457C, Add, -402653184),# units:Graphics  index:135    from 34 To 10
        SetMemory(0x664580, Add, 44),# units:Graphics  index:136    from 27 To 71
        SetMemory(0x664580, Add, 11520),# units:Graphics  index:137    from 26 To 71
        SetMemory(0x664580, Add, 2818048),# units:Graphics  index:138    from 28 To 71
        SetMemory(0x664580, Add, 855638016),# units:Graphics  index:139    from 20 To 71
        SetMemory(0x664584, Add, 39),# units:Graphics  index:140    from 32 To 71
        SetMemory(0x664584, Add, 3473408),# units:Graphics  index:142    from 18 To 71
        SetMemory(0x664588, Add, 687865856),# units:Graphics  index:147    from 30 To 71
        SetMemory(0x66458C, Add, 40),# units:Graphics  index:148    from 31 To 71
        SetMemory(0x66458C, Add, 922746880),# units:Graphics  index:151    from 16 To 71
        SetMemory(0x664590, Add, 55),# units:Graphics  index:152    from 16 To 71
        SetMemory(0x664590, Add, 786432),# units:Graphics  index:154    from 59 To 71
        SetMemory(0x664594, Add, 301989888),# units:Graphics  index:159    from 53 To 71
        SetMemory(0x664598, Add, 15),# units:Graphics  index:160    from 56 To 71
        SetMemory(0x664598, Add, 285212672),# units:Graphics  index:163    from 54 To 71
        SetMemory(0x66459C, Add, 14),# units:Graphics  index:164    from 57 To 71
        SetMemory(0x66459C, Add, 5120),# units:Graphics  index:165    from 51 To 71
        SetMemory(0x66459C, Add, 1048576),# units:Graphics  index:166    from 55 To 71
        SetMemory(0x66459C, Add, 100663296),# units:Graphics  index:167    from 65 To 71
        SetMemory(0x6645A0, Add, 5),# units:Graphics  index:168    from 66 To 71
        SetMemory(0x6645A0, Add, 512),# units:Graphics  index:169    from 69 To 71
        SetMemory(0x6645A0, Add, 655360),# units:Graphics  index:170    from 61 To 71
        SetMemory(0x6645A0, Add, 67108864),# units:Graphics  index:171    from 67 To 71
        SetMemory(0x6645A4, Add, 7),# units:Graphics  index:172    from 64 To 71
        SetMemory(0x6645A4, Add, 3328),# units:Graphics  index:173    from 58 To 71
        SetMemory(0x6645A4, Add, 196608),# units:Graphics  index:174    from 68 To 71
        SetMemory(0x6645A4, Add, -2113929216),# units:Graphics  index:175    from 197 To 71
        SetMemory(0x66126C, Add, -325),# units:Construction Animation  index:111    from 325 To 0
        SetMemory(0x6612C4, Add, -103),# units:Construction Animation  index:133    from 103 To 0
        SetMemory(0x6612CC, Add, -104),# units:Construction Animation  index:135    from 104 To 0
        SetMemory(0x6612D0, Add, -104),# units:Construction Animation  index:136    from 104 To 0
        SetMemory(0x6612D4, Add, -104),# units:Construction Animation  index:137    from 104 To 0
        SetMemory(0x6612D8, Add, -104),# units:Construction Animation  index:138    from 104 To 0
        SetMemory(0x6612DC, Add, -104),# units:Construction Animation  index:139    from 104 To 0
        SetMemory(0x6612E0, Add, -104),# units:Construction Animation  index:140    from 104 To 0
        SetMemory(0x6612E8, Add, -104),# units:Construction Animation  index:142    from 104 To 0
        SetMemory(0x6612FC, Add, -103),# units:Construction Animation  index:147    from 103 To 0
        SetMemory(0x661300, Add, -103),# units:Construction Animation  index:148    from 103 To 0
        SetMemory(0x66130C, Add, -104),# units:Construction Animation  index:151    from 104 To 0
        SetMemory(0x661310, Add, -104),# units:Construction Animation  index:152    from 104 To 0
        SetMemory(0x66134C, Add, -200),# units:Construction Animation  index:167    from 200 To 0
        SetMemory(0x66062C, Add, -32),# units:Unit Direction  index:60    from 32 To 0
        SetMemory(0x660640, Add, -536870912),# units:Unit Direction  index:83    from 32 To 0
        SetMemory(0x660644, Add, -32),# units:Unit Direction  index:84    from 32 To 0
        SetMemory(0x66064C, Add, -4096),# units:Unit Direction  index:93    from 32 To 16
        SetMemory(0x66064C, Add, -1048576),# units:Unit Direction  index:94    from 32 To 16
        SetMemory(0x66064C, Add, -268435456),# units:Unit Direction  index:95    from 32 To 16
        SetMemory(0x660650, Add, -16),# units:Unit Direction  index:96    from 32 To 16
        SetMemory(0x66065C, Add, 536870912),# units:Unit Direction  index:111    from 0 To 32
        SetMemory(0x660678, Add, 32),# units:Unit Direction  index:136    from 0 To 32
        SetMemory(0x660678, Add, 8192),# units:Unit Direction  index:137    from 0 To 32
        SetMemory(0x660678, Add, 2097152),# units:Unit Direction  index:138    from 0 To 32
        SetMemory(0x660678, Add, 536870912),# units:Unit Direction  index:139    from 0 To 32
        SetMemory(0x66067C, Add, 32),# units:Unit Direction  index:140    from 0 To 32
        SetMemory(0x66067C, Add, 2097152),# units:Unit Direction  index:142    from 0 To 32
        SetMemory(0x660680, Add, 536870912),# units:Unit Direction  index:147    from 0 To 32
        SetMemory(0x660684, Add, 32),# units:Unit Direction  index:148    from 0 To 32
        SetMemory(0x660684, Add, 536870912),# units:Unit Direction  index:151    from 0 To 32
        SetMemory(0x660688, Add, 32),# units:Unit Direction  index:152    from 0 To 32
        SetMemory(0x660688, Add, 2097152),# units:Unit Direction  index:154    from 0 To 32
        SetMemory(0x66068C, Add, 536870912),# units:Unit Direction  index:159    from 0 To 32
        SetMemory(0x660690, Add, 32),# units:Unit Direction  index:160    from 0 To 32
        SetMemory(0x660690, Add, 536870912),# units:Unit Direction  index:163    from 0 To 32
        SetMemory(0x660694, Add, 32),# units:Unit Direction  index:164    from 0 To 32
        SetMemory(0x660694, Add, 8192),# units:Unit Direction  index:165    from 0 To 32
        SetMemory(0x660694, Add, 2097152),# units:Unit Direction  index:166    from 0 To 32
        SetMemory(0x660694, Add, 536870912),# units:Unit Direction  index:167    from 0 To 32
        SetMemory(0x660698, Add, 32),# units:Unit Direction  index:168    from 0 To 32
        SetMemory(0x660698, Add, 8192),# units:Unit Direction  index:169    from 0 To 32
        SetMemory(0x660698, Add, 2097152),# units:Unit Direction  index:170    from 0 To 32
        SetMemory(0x660698, Add, 536870912),# units:Unit Direction  index:171    from 0 To 32
        SetMemory(0x66069C, Add, 32),# units:Unit Direction  index:172    from 0 To 32
        SetMemory(0x66069C, Add, 8192),# units:Unit Direction  index:173    from 0 To 32
        SetMemory(0x66069C, Add, 2097152),# units:Unit Direction  index:174    from 0 To 32
        SetMemory(0x66069C, Add, 536870912),# units:Unit Direction  index:175    from 0 To 32
        SetMemory(0x664848, Add, -65536),# units:Shield Enable  index:154    from 1 To 0
        SetMemory(0x66484C, Add, -16777216),# units:Shield Enable  index:159    from 1 To 0
        SetMemory(0x664850, Add, -1),# units:Shield Enable  index:160    from 1 To 0
        SetMemory(0x664850, Add, -16777216),# units:Shield Enable  index:163    from 1 To 0
        SetMemory(0x664854, Add, -1),# units:Shield Enable  index:164    from 1 To 0
        SetMemory(0x664854, Add, -256),# units:Shield Enable  index:165    from 1 To 0
        SetMemory(0x664854, Add, -65536),# units:Shield Enable  index:166    from 1 To 0
        SetMemory(0x664854, Add, -16777216),# units:Shield Enable  index:167    from 1 To 0
        SetMemory(0x664858, Add, -256),# units:Shield Enable  index:169    from 1 To 0
        SetMemory(0x664858, Add, -65536),# units:Shield Enable  index:170    from 1 To 0
        SetMemory(0x664858, Add, -16777216),# units:Shield Enable  index:171    from 1 To 0
        SetMemory(0x66485C, Add, -1),# units:Shield Enable  index:172    from 1 To 0
        SetMemory(0x660F34, Add, -650),# units:Shield Amount  index:154    from 750 To 100
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
        SetMemory(0x662564, Add, -422400),# units:Hit Points  index:133    from 640000 To 217600
        SetMemory(0x662570, Add, -207360),# units:Hit Points  index:136    from 217600 To 10240
        SetMemory(0x662574, Add, -245760),# units:Hit Points  index:137    from 256000 To 10240
        SetMemory(0x662578, Add, -207360),# units:Hit Points  index:138    from 217600 To 10240
        SetMemory(0x66257C, Add, -181760),# units:Hit Points  index:139    from 192000 To 10240
        SetMemory(0x662580, Add, -143360),# units:Hit Points  index:140    from 153600 To 10240
        SetMemory(0x662588, Add, -181760),# units:Hit Points  index:142    from 192000 To 10240
        SetMemory(0x66259C, Add, -1269760),# units:Hit Points  index:147    from 1280000 To 10240
        SetMemory(0x6625A0, Add, -629760),# units:Hit Points  index:148    from 640000 To 10240
        SetMemory(0x6625AC, Add, -373760),# units:Hit Points  index:151    from 384000 To 10240
        SetMemory(0x6625B0, Add, -373760),# units:Hit Points  index:152    from 384000 To 10240
        SetMemory(0x6625B8, Add, -181760),# units:Hit Points  index:154    from 192000 To 10240
        SetMemory(0x6625CC, Add, -53760),# units:Hit Points  index:159    from 64000 To 10240
        SetMemory(0x6625D0, Add, -117760),# units:Hit Points  index:160    from 128000 To 10240
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
        SetMemory(0x663194, Add, -3584),# units:Elevation Level  index:69    from 18 To 4
        SetMemory(0x6631A0, Add, 201326592),# units:Elevation Level  index:83    from 4 To 16
        SetMemory(0x6631AC, Add, 3584),# units:Elevation Level  index:93    from 4 To 18
        SetMemory(0x6631AC, Add, 234881024),# units:Elevation Level  index:95    from 4 To 18
        SetMemory(0x6631B0, Add, 14),# units:Elevation Level  index:96    from 4 To 18
        SetMemory(0x6631DC, Add, 131072),# units:Elevation Level  index:142    from 2 To 4
        SetMemory(0x663214, Add, 0),# units:Elevation Level  index:196    from 0 To 0
        SetMemory(0x660FC8, Add, -8388608),# units:Unknown (old Movement)  index:2    from 193 To 65
        SetMemory(0x661034, Add, -2214592512),# units:Unknown (old Movement)  index:111    from 197 To 65
        SetMemory(0x661050, Add, 65),# units:Unknown (old Movement)  index:136    from 0 To 65
        SetMemory(0x661050, Add, 16640),# units:Unknown (old Movement)  index:137    from 0 To 65
        SetMemory(0x661050, Add, 4259840),# units:Unknown (old Movement)  index:138    from 0 To 65
        SetMemory(0x661050, Add, 1090519040),# units:Unknown (old Movement)  index:139    from 0 To 65
        SetMemory(0x661054, Add, 65),# units:Unknown (old Movement)  index:140    from 0 To 65
        SetMemory(0x661054, Add, 4259840),# units:Unknown (old Movement)  index:142    from 0 To 65
        SetMemory(0x661058, Add, 1090519040),# units:Unknown (old Movement)  index:147    from 0 To 65
        SetMemory(0x66105C, Add, 65),# units:Unknown (old Movement)  index:148    from 0 To 65
        SetMemory(0x66105C, Add, 1090519040),# units:Unknown (old Movement)  index:151    from 0 To 65
        SetMemory(0x661060, Add, 65),# units:Unknown (old Movement)  index:152    from 0 To 65
        SetMemory(0x661060, Add, 4259840),# units:Unknown (old Movement)  index:154    from 0 To 65
        SetMemory(0x661064, Add, 1090519040),# units:Unknown (old Movement)  index:159    from 0 To 65
        SetMemory(0x661068, Add, 65),# units:Unknown (old Movement)  index:160    from 0 To 65
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
        SetMemory(0x663DD0, Add, 5),# units:Rank/Sublabel  index:0    from 2 To 7
        SetMemory(0x663DD0, Add, 512),# units:Rank/Sublabel  index:1    from 5 To 7
        SetMemory(0x663DD8, Add, -393216),# units:Rank/Sublabel  index:10    from 12 To 6
        SetMemory(0x663DD8, Add, -16777216),# units:Rank/Sublabel  index:11    from 9 To 8
        SetMemory(0x663DE4, Add, -9),# units:Rank/Sublabel  index:20    from 17 To 8
        SetMemory(0x663DE8, Add, -251658240),# units:Rank/Sublabel  index:27    from 21 To 6
        SetMemory(0x663DEC, Add, -13),# units:Rank/Sublabel  index:28    from 20 To 7
        SetMemory(0x663DEC, Add, -3584),# units:Rank/Sublabel  index:29    from 21 To 7
        SetMemory(0x663DF0, Add, 4),# units:Rank/Sublabel  index:32    from 4 To 8
        SetMemory(0x663DF0, Add, 327680),# units:Rank/Sublabel  index:34    from 3 To 8
        SetMemory(0x663E14, Add, 256),# units:Rank/Sublabel  index:69    from 7 To 8
        SetMemory(0x663E14, Add, -131072),# units:Rank/Sublabel  index:70    from 8 To 6
        SetMemory(0x663E28, Add, -6),# units:Rank/Sublabel  index:88    from 12 To 6
        SetMemory(0x663E34, Add, 458752),# units:Rank/Sublabel  index:102    from 0 To 7
        SetMemory(0x663E3C, Add, 134217728),# units:Rank/Sublabel  index:111    from 0 To 8
        SetMemory(0x663E54, Add, 9216),# units:Rank/Sublabel  index:133    from 0 To 36
        SetMemory(0x663E54, Add, 587202560),# units:Rank/Sublabel  index:135    from 0 To 35
        SetMemory(0x663E58, Add, 24),# units:Rank/Sublabel  index:136    from 0 To 24
        SetMemory(0x663E58, Add, 8704),# units:Rank/Sublabel  index:137    from 0 To 34
        SetMemory(0x663E58, Add, 2162688),# units:Rank/Sublabel  index:138    from 0 To 33
        SetMemory(0x663E58, Add, 536870912),# units:Rank/Sublabel  index:139    from 0 To 32
        SetMemory(0x663E5C, Add, 31),# units:Rank/Sublabel  index:140    from 0 To 31
        SetMemory(0x663E5C, Add, 1966080),# units:Rank/Sublabel  index:142    from 0 To 30
        SetMemory(0x663E60, Add, 486539264),# units:Rank/Sublabel  index:147    from 0 To 29
        SetMemory(0x663E64, Add, 28),# units:Rank/Sublabel  index:148    from 0 To 28
        SetMemory(0x663E64, Add, 452984832),# units:Rank/Sublabel  index:151    from 0 To 27
        SetMemory(0x663E68, Add, 26),# units:Rank/Sublabel  index:152    from 0 To 26
        SetMemory(0x663E68, Add, 1638400),# units:Rank/Sublabel  index:154    from 0 To 25
        SetMemory(0x663E6C, Add, 385875968),# units:Rank/Sublabel  index:159    from 0 To 23
        SetMemory(0x663E70, Add, 22),# units:Rank/Sublabel  index:160    from 0 To 22
        SetMemory(0x663E70, Add, 352321536),# units:Rank/Sublabel  index:163    from 0 To 21
        SetMemory(0x663E74, Add, 20),# units:Rank/Sublabel  index:164    from 0 To 20
        SetMemory(0x663E74, Add, 4864),# units:Rank/Sublabel  index:165    from 0 To 19
        SetMemory(0x663E74, Add, 1179648),# units:Rank/Sublabel  index:166    from 0 To 18
        SetMemory(0x663E74, Add, 285212672),# units:Rank/Sublabel  index:167    from 0 To 17
        SetMemory(0x663E78, Add, 16),# units:Rank/Sublabel  index:168    from 0 To 16
        SetMemory(0x663E78, Add, 3840),# units:Rank/Sublabel  index:169    from 0 To 15
        SetMemory(0x663E78, Add, 917504),# units:Rank/Sublabel  index:170    from 0 To 14
        SetMemory(0x663E78, Add, 218103808),# units:Rank/Sublabel  index:171    from 0 To 13
        SetMemory(0x663E7C, Add, 12),# units:Rank/Sublabel  index:172    from 0 To 12
        SetMemory(0x663E7C, Add, 2816),# units:Rank/Sublabel  index:173    from 0 To 11
        SetMemory(0x663E7C, Add, 655360),# units:Rank/Sublabel  index:174    from 0 To 10
        SetMemory(0x663E7C, Add, 150994944),# units:Rank/Sublabel  index:175    from 0 To 9
        SetMemory(0x662EA0, Add, 105),# units:Comp AI Idle  index:0    from 2 To 107
        SetMemory(0x662EA0, Add, 26880),# units:Comp AI Idle  index:1    from 2 To 107
        SetMemory(0x662EA0, Add, 6881280),# units:Comp AI Idle  index:2    from 2 To 107
        SetMemory(0x662EA0, Add, 1761607680),# units:Comp AI Idle  index:3    from 2 To 107
        SetMemory(0x662EA4, Add, 26880),# units:Comp AI Idle  index:5    from 2 To 107
        SetMemory(0x662EA8, Add, 105),# units:Comp AI Idle  index:8    from 2 To 107
        SetMemory(0x662EA8, Add, 6881280),# units:Comp AI Idle  index:10    from 2 To 107
        SetMemory(0x662EA8, Add, 234881024),# units:Comp AI Idle  index:11    from 93 To 107
        SetMemory(0x662EAC, Add, 105),# units:Comp AI Idle  index:12    from 2 To 107
        SetMemory(0x662EB0, Add, 105),# units:Comp AI Idle  index:16    from 2 To 107
        SetMemory(0x662EB0, Add, 26880),# units:Comp AI Idle  index:17    from 2 To 107
        SetMemory(0x662EB0, Add, 1761607680),# units:Comp AI Idle  index:19    from 2 To 107
        SetMemory(0x662EB4, Add, 105),# units:Comp AI Idle  index:20    from 2 To 107
        SetMemory(0x662EB4, Add, 26880),# units:Comp AI Idle  index:21    from 2 To 107
        SetMemory(0x662EB4, Add, 1761607680),# units:Comp AI Idle  index:23    from 2 To 107
        SetMemory(0x662EB8, Add, 1761607680),# units:Comp AI Idle  index:27    from 2 To 107
        SetMemory(0x662EBC, Add, 105),# units:Comp AI Idle  index:28    from 2 To 107
        SetMemory(0x662EBC, Add, 26880),# units:Comp AI Idle  index:29    from 2 To 107
        SetMemory(0x662EC0, Add, 105),# units:Comp AI Idle  index:32    from 2 To 107
        SetMemory(0x662EC4, Add, 26880),# units:Comp AI Idle  index:37    from 2 To 107
        SetMemory(0x662EC4, Add, 6881280),# units:Comp AI Idle  index:38    from 2 To 107
        SetMemory(0x662EC4, Add, 1761607680),# units:Comp AI Idle  index:39    from 2 To 107
        SetMemory(0x662EC8, Add, 105),# units:Comp AI Idle  index:40    from 2 To 107
        SetMemory(0x662EC8, Add, 1761607680),# units:Comp AI Idle  index:43    from 2 To 107
        SetMemory(0x662ECC, Add, 105),# units:Comp AI Idle  index:44    from 2 To 107
        SetMemory(0x662ECC, Add, 6881280),# units:Comp AI Idle  index:46    from 2 To 107
        SetMemory(0x662ED0, Add, 105),# units:Comp AI Idle  index:48    from 2 To 107
        SetMemory(0x662ED0, Add, 1761607680),# units:Comp AI Idle  index:51    from 2 To 107
        SetMemory(0x662ED4, Add, 105),# units:Comp AI Idle  index:52    from 2 To 107
        SetMemory(0x662ED4, Add, 26880),# units:Comp AI Idle  index:53    from 2 To 107
        SetMemory(0x662ED4, Add, 6881280),# units:Comp AI Idle  index:54    from 2 To 107
        SetMemory(0x662ED4, Add, 1761607680),# units:Comp AI Idle  index:55    from 2 To 107
        SetMemory(0x662ED8, Add, 105),# units:Comp AI Idle  index:56    from 2 To 107
        SetMemory(0x662EDC, Add, 26880),# units:Comp AI Idle  index:61    from 2 To 107
        SetMemory(0x662EDC, Add, 1761607680),# units:Comp AI Idle  index:63    from 2 To 107
        SetMemory(0x662EE0, Add, 26880),# units:Comp AI Idle  index:65    from 2 To 107
        SetMemory(0x662EE0, Add, 6881280),# units:Comp AI Idle  index:66    from 2 To 107
        SetMemory(0x662EE0, Add, 1761607680),# units:Comp AI Idle  index:67    from 2 To 107
        SetMemory(0x662EE4, Add, 105),# units:Comp AI Idle  index:68    from 2 To 107
        SetMemory(0x662EE4, Add, 3584),# units:Comp AI Idle  index:69    from 93 To 107
        SetMemory(0x662EE4, Add, 6881280),# units:Comp AI Idle  index:70    from 2 To 107
        SetMemory(0x662EE4, Add, -385875968),# units:Comp AI Idle  index:71    from 130 To 107
        SetMemory(0x662EE8, Add, 6881280),# units:Comp AI Idle  index:74    from 2 To 107
        SetMemory(0x662EE8, Add, 1761607680),# units:Comp AI Idle  index:75    from 2 To 107
        SetMemory(0x662EEC, Add, 105),# units:Comp AI Idle  index:76    from 2 To 107
        SetMemory(0x662EEC, Add, 26880),# units:Comp AI Idle  index:77    from 2 To 107
        SetMemory(0x662EEC, Add, 6881280),# units:Comp AI Idle  index:78    from 2 To 107
        SetMemory(0x662EEC, Add, 1761607680),# units:Comp AI Idle  index:79    from 2 To 107
        SetMemory(0x662EF0, Add, 105),# units:Comp AI Idle  index:80    from 2 To 107
        SetMemory(0x662EF4, Add, -1507328),# units:Comp AI Idle  index:86    from 130 To 107
        SetMemory(0x662EF4, Add, 1761607680),# units:Comp AI Idle  index:87    from 2 To 107
        SetMemory(0x662EF8, Add, 105),# units:Comp AI Idle  index:88    from 2 To 107
        SetMemory(0x662F00, Add, 1761607680),# units:Comp AI Idle  index:99    from 2 To 107
        SetMemory(0x662F04, Add, 105),# units:Comp AI Idle  index:100    from 2 To 107
        SetMemory(0x662F04, Add, 6881280),# units:Comp AI Idle  index:102    from 2 To 107
        SetMemory(0x662F08, Add, 105),# units:Comp AI Idle  index:104    from 2 To 107
        SetMemory(0x662F0C, Add, -822083584),# units:Comp AI Idle  index:111    from 156 To 107
        SetMemory(0x662F24, Add, -25344),# units:Comp AI Idle  index:133    from 101 To 2
        SetMemory(0x662F24, Add, -2583691264),# units:Comp AI Idle  index:135    from 156 To 2
        SetMemory(0x662F28, Add, -154),# units:Comp AI Idle  index:136    from 156 To 2
        SetMemory(0x662F28, Add, -39424),# units:Comp AI Idle  index:137    from 156 To 2
        SetMemory(0x662F28, Add, -10092544),# units:Comp AI Idle  index:138    from 156 To 2
        SetMemory(0x662F28, Add, -2583691264),# units:Comp AI Idle  index:139    from 156 To 2
        SetMemory(0x662F2C, Add, -154),# units:Comp AI Idle  index:140    from 156 To 2
        SetMemory(0x662F2C, Add, -10092544),# units:Comp AI Idle  index:142    from 156 To 2
        SetMemory(0x662F30, Add, -2583691264),# units:Comp AI Idle  index:147    from 156 To 2
        SetMemory(0x662F34, Add, -154),# units:Comp AI Idle  index:148    from 156 To 2
        SetMemory(0x662F34, Add, -2583691264),# units:Comp AI Idle  index:151    from 156 To 2
        SetMemory(0x662F38, Add, -154),# units:Comp AI Idle  index:152    from 156 To 2
        SetMemory(0x662F38, Add, -10092544),# units:Comp AI Idle  index:154    from 156 To 2
        SetMemory(0x662F3C, Add, -2583691264),# units:Comp AI Idle  index:159    from 156 To 2
        SetMemory(0x662F40, Add, -154),# units:Comp AI Idle  index:160    from 156 To 2
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
        SetMemory(0x662F4C, Add, -10092544),# units:Comp AI Idle  index:174    from 156 To 2
        SetMemory(0x662F4C, Add, -2583691264),# units:Comp AI Idle  index:175    from 156 To 2
        SetMemory(0x662268, Add, 105),# units:Human AI Idle  index:0    from 2 To 107
        SetMemory(0x662268, Add, 26880),# units:Human AI Idle  index:1    from 2 To 107
        SetMemory(0x662268, Add, 6881280),# units:Human AI Idle  index:2    from 2 To 107
        SetMemory(0x662268, Add, 1761607680),# units:Human AI Idle  index:3    from 2 To 107
        SetMemory(0x66226C, Add, 26880),# units:Human AI Idle  index:5    from 2 To 107
        SetMemory(0x662270, Add, 105),# units:Human AI Idle  index:8    from 2 To 107
        SetMemory(0x662270, Add, 6881280),# units:Human AI Idle  index:10    from 2 To 107
        SetMemory(0x662270, Add, 234881024),# units:Human AI Idle  index:11    from 93 To 107
        SetMemory(0x662274, Add, 105),# units:Human AI Idle  index:12    from 2 To 107
        SetMemory(0x662278, Add, 105),# units:Human AI Idle  index:16    from 2 To 107
        SetMemory(0x662278, Add, 26880),# units:Human AI Idle  index:17    from 2 To 107
        SetMemory(0x662278, Add, 1761607680),# units:Human AI Idle  index:19    from 2 To 107
        SetMemory(0x66227C, Add, 105),# units:Human AI Idle  index:20    from 2 To 107
        SetMemory(0x66227C, Add, 26880),# units:Human AI Idle  index:21    from 2 To 107
        SetMemory(0x66227C, Add, 1761607680),# units:Human AI Idle  index:23    from 2 To 107
        SetMemory(0x662280, Add, 1761607680),# units:Human AI Idle  index:27    from 2 To 107
        SetMemory(0x662284, Add, 105),# units:Human AI Idle  index:28    from 2 To 107
        SetMemory(0x662284, Add, 26880),# units:Human AI Idle  index:29    from 2 To 107
        SetMemory(0x662288, Add, 105),# units:Human AI Idle  index:32    from 2 To 107
        SetMemory(0x66228C, Add, 26880),# units:Human AI Idle  index:37    from 2 To 107
        SetMemory(0x66228C, Add, 6881280),# units:Human AI Idle  index:38    from 2 To 107
        SetMemory(0x66228C, Add, 1761607680),# units:Human AI Idle  index:39    from 2 To 107
        SetMemory(0x662290, Add, 105),# units:Human AI Idle  index:40    from 2 To 107
        SetMemory(0x662290, Add, 1761607680),# units:Human AI Idle  index:43    from 2 To 107
        SetMemory(0x662294, Add, 105),# units:Human AI Idle  index:44    from 2 To 107
        SetMemory(0x662294, Add, 6881280),# units:Human AI Idle  index:46    from 2 To 107
        SetMemory(0x662298, Add, 105),# units:Human AI Idle  index:48    from 2 To 107
        SetMemory(0x662298, Add, 1761607680),# units:Human AI Idle  index:51    from 2 To 107
        SetMemory(0x66229C, Add, 105),# units:Human AI Idle  index:52    from 2 To 107
        SetMemory(0x66229C, Add, 26880),# units:Human AI Idle  index:53    from 2 To 107
        SetMemory(0x66229C, Add, 6881280),# units:Human AI Idle  index:54    from 2 To 107
        SetMemory(0x66229C, Add, 1761607680),# units:Human AI Idle  index:55    from 2 To 107
        SetMemory(0x6622A0, Add, 105),# units:Human AI Idle  index:56    from 2 To 107
        SetMemory(0x6622A4, Add, 26880),# units:Human AI Idle  index:61    from 2 To 107
        SetMemory(0x6622A4, Add, 1761607680),# units:Human AI Idle  index:63    from 2 To 107
        SetMemory(0x6622A8, Add, 26880),# units:Human AI Idle  index:65    from 2 To 107
        SetMemory(0x6622A8, Add, 6881280),# units:Human AI Idle  index:66    from 2 To 107
        SetMemory(0x6622A8, Add, 1761607680),# units:Human AI Idle  index:67    from 2 To 107
        SetMemory(0x6622AC, Add, 105),# units:Human AI Idle  index:68    from 2 To 107
        SetMemory(0x6622AC, Add, 3584),# units:Human AI Idle  index:69    from 93 To 107
        SetMemory(0x6622AC, Add, 6881280),# units:Human AI Idle  index:70    from 2 To 107
        SetMemory(0x6622AC, Add, -385875968),# units:Human AI Idle  index:71    from 130 To 107
        SetMemory(0x6622B0, Add, 6881280),# units:Human AI Idle  index:74    from 2 To 107
        SetMemory(0x6622B0, Add, 1761607680),# units:Human AI Idle  index:75    from 2 To 107
        SetMemory(0x6622B4, Add, 105),# units:Human AI Idle  index:76    from 2 To 107
        SetMemory(0x6622B4, Add, 26880),# units:Human AI Idle  index:77    from 2 To 107
        SetMemory(0x6622B4, Add, 6881280),# units:Human AI Idle  index:78    from 2 To 107
        SetMemory(0x6622B4, Add, 1761607680),# units:Human AI Idle  index:79    from 2 To 107
        SetMemory(0x6622B8, Add, 105),# units:Human AI Idle  index:80    from 2 To 107
        SetMemory(0x6622BC, Add, -1507328),# units:Human AI Idle  index:86    from 130 To 107
        SetMemory(0x6622BC, Add, 1761607680),# units:Human AI Idle  index:87    from 2 To 107
        SetMemory(0x6622C0, Add, 105),# units:Human AI Idle  index:88    from 2 To 107
        SetMemory(0x6622C4, Add, -41984),# units:Human AI Idle  index:93    from 166 To 2
        SetMemory(0x6622C4, Add, -10747904),# units:Human AI Idle  index:94    from 166 To 2
        SetMemory(0x6622C4, Add, -2751463424),# units:Human AI Idle  index:95    from 166 To 2
        SetMemory(0x6622C8, Add, -164),# units:Human AI Idle  index:96    from 166 To 2
        SetMemory(0x6622C8, Add, 1761607680),# units:Human AI Idle  index:99    from 2 To 107
        SetMemory(0x6622CC, Add, 105),# units:Human AI Idle  index:100    from 2 To 107
        SetMemory(0x6622CC, Add, 6881280),# units:Human AI Idle  index:102    from 2 To 107
        SetMemory(0x6622D0, Add, 105),# units:Human AI Idle  index:104    from 2 To 107
        SetMemory(0x6622D4, Add, 1409286144),# units:Human AI Idle  index:111    from 23 To 107
        SetMemory(0x6622EC, Add, -25344),# units:Human AI Idle  index:133    from 101 To 2
        SetMemory(0x6622EC, Add, -352321536),# units:Human AI Idle  index:135    from 23 To 2
        SetMemory(0x6622F0, Add, -21),# units:Human AI Idle  index:136    from 23 To 2
        SetMemory(0x6622F0, Add, -5376),# units:Human AI Idle  index:137    from 23 To 2
        SetMemory(0x6622F0, Add, -1376256),# units:Human AI Idle  index:138    from 23 To 2
        SetMemory(0x6622F0, Add, -352321536),# units:Human AI Idle  index:139    from 23 To 2
        SetMemory(0x6622F4, Add, -21),# units:Human AI Idle  index:140    from 23 To 2
        SetMemory(0x6622F4, Add, -1376256),# units:Human AI Idle  index:142    from 23 To 2
        SetMemory(0x6622F8, Add, -352321536),# units:Human AI Idle  index:147    from 23 To 2
        SetMemory(0x6622FC, Add, -21),# units:Human AI Idle  index:148    from 23 To 2
        SetMemory(0x6622FC, Add, -352321536),# units:Human AI Idle  index:151    from 23 To 2
        SetMemory(0x662300, Add, -21),# units:Human AI Idle  index:152    from 23 To 2
        SetMemory(0x662300, Add, -1376256),# units:Human AI Idle  index:154    from 23 To 2
        SetMemory(0x662304, Add, -352321536),# units:Human AI Idle  index:159    from 23 To 2
        SetMemory(0x662308, Add, -21),# units:Human AI Idle  index:160    from 23 To 2
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
        SetMemory(0x662314, Add, -1376256),# units:Human AI Idle  index:174    from 23 To 2
        SetMemory(0x662314, Add, -352321536),# units:Human AI Idle  index:175    from 23 To 2
        SetMemory(0x664898, Add, 105),# units:Return to Idle  index:0    from 2 To 107
        SetMemory(0x664898, Add, 26880),# units:Return to Idle  index:1    from 2 To 107
        SetMemory(0x664898, Add, 6881280),# units:Return to Idle  index:2    from 2 To 107
        SetMemory(0x664898, Add, 1761607680),# units:Return to Idle  index:3    from 2 To 107
        SetMemory(0x66489C, Add, 26880),# units:Return to Idle  index:5    from 2 To 107
        SetMemory(0x6648A0, Add, 105),# units:Return to Idle  index:8    from 2 To 107
        SetMemory(0x6648A0, Add, 6881280),# units:Return to Idle  index:10    from 2 To 107
        SetMemory(0x6648A0, Add, 234881024),# units:Return to Idle  index:11    from 93 To 107
        SetMemory(0x6648A4, Add, 105),# units:Return to Idle  index:12    from 2 To 107
        SetMemory(0x6648A8, Add, 105),# units:Return to Idle  index:16    from 2 To 107
        SetMemory(0x6648A8, Add, 26880),# units:Return to Idle  index:17    from 2 To 107
        SetMemory(0x6648A8, Add, 1761607680),# units:Return to Idle  index:19    from 2 To 107
        SetMemory(0x6648AC, Add, 105),# units:Return to Idle  index:20    from 2 To 107
        SetMemory(0x6648AC, Add, 26880),# units:Return to Idle  index:21    from 2 To 107
        SetMemory(0x6648AC, Add, 1761607680),# units:Return to Idle  index:23    from 2 To 107
        SetMemory(0x6648B0, Add, 1761607680),# units:Return to Idle  index:27    from 2 To 107
        SetMemory(0x6648B4, Add, 105),# units:Return to Idle  index:28    from 2 To 107
        SetMemory(0x6648B4, Add, 26880),# units:Return to Idle  index:29    from 2 To 107
        SetMemory(0x6648B8, Add, 105),# units:Return to Idle  index:32    from 2 To 107
        SetMemory(0x6648BC, Add, 26880),# units:Return to Idle  index:37    from 2 To 107
        SetMemory(0x6648BC, Add, 6881280),# units:Return to Idle  index:38    from 2 To 107
        SetMemory(0x6648BC, Add, 1761607680),# units:Return to Idle  index:39    from 2 To 107
        SetMemory(0x6648C0, Add, 105),# units:Return to Idle  index:40    from 2 To 107
        SetMemory(0x6648C0, Add, 1761607680),# units:Return to Idle  index:43    from 2 To 107
        SetMemory(0x6648C4, Add, 105),# units:Return to Idle  index:44    from 2 To 107
        SetMemory(0x6648C4, Add, 6881280),# units:Return to Idle  index:46    from 2 To 107
        SetMemory(0x6648C8, Add, 105),# units:Return to Idle  index:48    from 2 To 107
        SetMemory(0x6648C8, Add, 1761607680),# units:Return to Idle  index:51    from 2 To 107
        SetMemory(0x6648CC, Add, 105),# units:Return to Idle  index:52    from 2 To 107
        SetMemory(0x6648CC, Add, 26880),# units:Return to Idle  index:53    from 2 To 107
        SetMemory(0x6648CC, Add, 6881280),# units:Return to Idle  index:54    from 2 To 107
        SetMemory(0x6648CC, Add, 1761607680),# units:Return to Idle  index:55    from 2 To 107
        SetMemory(0x6648D0, Add, 105),# units:Return to Idle  index:56    from 2 To 107
        SetMemory(0x6648D4, Add, 26880),# units:Return to Idle  index:61    from 2 To 107
        SetMemory(0x6648D4, Add, 1761607680),# units:Return to Idle  index:63    from 2 To 107
        SetMemory(0x6648D8, Add, 26880),# units:Return to Idle  index:65    from 2 To 107
        SetMemory(0x6648D8, Add, 6881280),# units:Return to Idle  index:66    from 2 To 107
        SetMemory(0x6648D8, Add, 1761607680),# units:Return to Idle  index:67    from 2 To 107
        SetMemory(0x6648DC, Add, 105),# units:Return to Idle  index:68    from 2 To 107
        SetMemory(0x6648DC, Add, 3584),# units:Return to Idle  index:69    from 93 To 107
        SetMemory(0x6648DC, Add, 6881280),# units:Return to Idle  index:70    from 2 To 107
        SetMemory(0x6648DC, Add, 1761607680),# units:Return to Idle  index:71    from 2 To 107
        SetMemory(0x6648E0, Add, 6881280),# units:Return to Idle  index:74    from 2 To 107
        SetMemory(0x6648E0, Add, 1761607680),# units:Return to Idle  index:75    from 2 To 107
        SetMemory(0x6648E4, Add, 105),# units:Return to Idle  index:76    from 2 To 107
        SetMemory(0x6648E4, Add, 26880),# units:Return to Idle  index:77    from 2 To 107
        SetMemory(0x6648E4, Add, 6881280),# units:Return to Idle  index:78    from 2 To 107
        SetMemory(0x6648E4, Add, 1761607680),# units:Return to Idle  index:79    from 2 To 107
        SetMemory(0x6648E8, Add, 105),# units:Return to Idle  index:80    from 2 To 107
        SetMemory(0x6648EC, Add, 6881280),# units:Return to Idle  index:86    from 2 To 107
        SetMemory(0x6648EC, Add, 1761607680),# units:Return to Idle  index:87    from 2 To 107
        SetMemory(0x6648F0, Add, 105),# units:Return to Idle  index:88    from 2 To 107
        SetMemory(0x6648F4, Add, -41984),# units:Return to Idle  index:93    from 166 To 2
        SetMemory(0x6648F4, Add, -10747904),# units:Return to Idle  index:94    from 166 To 2
        SetMemory(0x6648F4, Add, -2751463424),# units:Return to Idle  index:95    from 166 To 2
        SetMemory(0x6648F8, Add, -164),# units:Return to Idle  index:96    from 166 To 2
        SetMemory(0x6648F8, Add, 1761607680),# units:Return to Idle  index:99    from 2 To 107
        SetMemory(0x6648FC, Add, 105),# units:Return to Idle  index:100    from 2 To 107
        SetMemory(0x6648FC, Add, 6881280),# units:Return to Idle  index:102    from 2 To 107
        SetMemory(0x664900, Add, 105),# units:Return to Idle  index:104    from 2 To 107
        SetMemory(0x664904, Add, 1409286144),# units:Return to Idle  index:111    from 23 To 107
        SetMemory(0x66491C, Add, -5376),# units:Return to Idle  index:133    from 23 To 2
        SetMemory(0x66491C, Add, -352321536),# units:Return to Idle  index:135    from 23 To 2
        SetMemory(0x664920, Add, -21),# units:Return to Idle  index:136    from 23 To 2
        SetMemory(0x664920, Add, -5376),# units:Return to Idle  index:137    from 23 To 2
        SetMemory(0x664920, Add, -1376256),# units:Return to Idle  index:138    from 23 To 2
        SetMemory(0x664920, Add, -352321536),# units:Return to Idle  index:139    from 23 To 2
        SetMemory(0x664924, Add, -21),# units:Return to Idle  index:140    from 23 To 2
        SetMemory(0x664924, Add, -1376256),# units:Return to Idle  index:142    from 23 To 2
        SetMemory(0x664928, Add, -352321536),# units:Return to Idle  index:147    from 23 To 2
        SetMemory(0x66492C, Add, -21),# units:Return to Idle  index:148    from 23 To 2
        SetMemory(0x66492C, Add, -352321536),# units:Return to Idle  index:151    from 23 To 2
        SetMemory(0x664930, Add, -21),# units:Return to Idle  index:152    from 23 To 2
        SetMemory(0x664930, Add, -1376256),# units:Return to Idle  index:154    from 23 To 2
        SetMemory(0x664934, Add, -352321536),# units:Return to Idle  index:159    from 23 To 2
        SetMemory(0x664938, Add, -21),# units:Return to Idle  index:160    from 23 To 2
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
        SetMemory(0x664944, Add, -1376256),# units:Return to Idle  index:174    from 23 To 2
        SetMemory(0x664944, Add, -352321536),# units:Return to Idle  index:175    from 23 To 2
        SetMemory(0x663328, Add, -184549376),# units:Attack Unit  index:11    from 21 To 10
        SetMemory(0x663330, Add, -2816),# units:Attack Unit  index:17    from 21 To 10
        SetMemory(0x66335C, Add, -184549376),# units:Attack Unit  index:63    from 21 To 10
        SetMemory(0x663364, Add, -2816),# units:Attack Unit  index:69    from 21 To 10
        SetMemory(0x66337C, Add, -42240),# units:Attack Unit  index:93    from 188 To 23
        SetMemory(0x66337C, Add, -10813440),# units:Attack Unit  index:94    from 188 To 23
        SetMemory(0x66337C, Add, -2768240640),# units:Attack Unit  index:95    from 188 To 23
        SetMemory(0x663380, Add, -165),# units:Attack Unit  index:96    from 188 To 23
        SetMemory(0x66338C, Add, 0),# units:Attack Unit  index:111    from 23 To 23
        SetMemory(0x663AAC, Add, -47616),# units:Attack Move  index:93    from 188 To 2
        SetMemory(0x663AAC, Add, -12189696),# units:Attack Move  index:94    from 188 To 2
        SetMemory(0x663AAC, Add, -3120562176),# units:Attack Move  index:95    from 188 To 2
        SetMemory(0x663AB0, Add, -186),# units:Attack Move  index:96    from 188 To 2
        SetMemory(0x663ABC, Add, -352321536),# units:Attack Move  index:111    from 23 To 2
        SetMemory(0x663AD4, Add, -5376),# units:Attack Move  index:133    from 23 To 2
        SetMemory(0x663AD4, Add, -352321536),# units:Attack Move  index:135    from 23 To 2
        SetMemory(0x663AD8, Add, -21),# units:Attack Move  index:136    from 23 To 2
        SetMemory(0x663AD8, Add, -5376),# units:Attack Move  index:137    from 23 To 2
        SetMemory(0x663AD8, Add, -1376256),# units:Attack Move  index:138    from 23 To 2
        SetMemory(0x663AD8, Add, -352321536),# units:Attack Move  index:139    from 23 To 2
        SetMemory(0x663ADC, Add, -21),# units:Attack Move  index:140    from 23 To 2
        SetMemory(0x663ADC, Add, -1376256),# units:Attack Move  index:142    from 23 To 2
        SetMemory(0x663AE0, Add, -352321536),# units:Attack Move  index:147    from 23 To 2
        SetMemory(0x663AE4, Add, -21),# units:Attack Move  index:148    from 23 To 2
        SetMemory(0x663AE4, Add, -352321536),# units:Attack Move  index:151    from 23 To 2
        SetMemory(0x663AE8, Add, -21),# units:Attack Move  index:152    from 23 To 2
        SetMemory(0x663AE8, Add, -1376256),# units:Attack Move  index:154    from 23 To 2
        SetMemory(0x663AEC, Add, -352321536),# units:Attack Move  index:159    from 23 To 2
        SetMemory(0x663AF0, Add, -21),# units:Attack Move  index:160    from 23 To 2
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
        SetMemory(0x663AFC, Add, -1376256),# units:Attack Move  index:174    from 23 To 2
        SetMemory(0x663AFC, Add, -352321536),# units:Attack Move  index:175    from 23 To 2
        SetMemory(0x6636BC, Add, 1),# units:Ground Weapon  index:4    from 7 To 8
        SetMemory(0x6636C8, Add, 65536),# units:Ground Weapon  index:18    from 9 To 10
        SetMemory(0x6636E4, Add, -5177344),# units:Ground Weapon  index:46    from 130 To 51
        SetMemory(0x6636EC, Add, -80),# units:Ground Weapon  index:52    from 130 To 50
        SetMemory(0x6636F4, Add, -838860800),# units:Ground Weapon  index:63    from 130 To 80
        SetMemory(0x6636F8, Add, -1040187392),# units:Ground Weapon  index:67    from 130 To 68
        SetMemory(0x663708, Add, 1),# units:Ground Weapon  index:80    from 75 To 76
        SetMemory(0x66370C, Add, -268435456),# units:Ground Weapon  index:87    from 69 To 53
        SetMemory(0x6616E4, Add, 122),# units:Air Weapon  index:4    from 8 To 130
        SetMemory(0x6616F0, Add, 127),# units:Air Weapon  index:16    from 3 To 130
        SetMemory(0x6616F0, Add, 7864320),# units:Air Weapon  index:18    from 10 To 130
        SetMemory(0x6616F4, Add, 28928),# units:Air Weapon  index:21    from 17 To 130
        SetMemory(0x661704, Add, 6029312),# units:Air Weapon  index:38    from 38 To 130
        SetMemory(0x661708, Add, 1375731712),# units:Air Weapon  index:43    from 48 To 130
        SetMemory(0x661714, Add, 23296),# units:Air Weapon  index:53    from 39 To 130
        SetMemory(0x661714, Add, 1358954496),# units:Air Weapon  index:55    from 49 To 130
        SetMemory(0x661720, Add, 4194304),# units:Air Weapon  index:66    from 66 To 130
        SetMemory(0x661724, Add, 889192448),# units:Air Weapon  index:71    from 77 To 130
        SetMemory(0x66172C, Add, 59),# units:Air Weapon  index:76    from 71 To 130
        SetMemory(0x66172C, Add, 4128768),# units:Air Weapon  index:78    from 67 To 130
        SetMemory(0x661730, Add, 54),# units:Air Weapon  index:80    from 76 To 130
        SetMemory(0x661734, Add, 3407872),# units:Air Weapon  index:86    from 78 To 130
        SetMemory(0x661740, Add, 301989888),# units:Air Weapon  index:99    from 112 To 130
        SetMemory(0x661744, Add, 14),# units:Air Weapon  index:100    from 116 To 130
        SetMemory(0x66175C, Add, 101),# units:Air Weapon  index:124    from 29 To 130
        SetMemory(0x65FC94, Add, -1),# units:Max Air Hits  index:124    from 1 To 0
        SetMemory(0x660180, Add, -196608),# units:AI Internal  index:10    from 3 To 0
        SetMemory(0x660188, Add, -3),# units:AI Internal  index:16    from 3 To 0
        SetMemory(0x660188, Add, -768),# units:AI Internal  index:17    from 3 To 0
        SetMemory(0x660188, Add, -50331648),# units:AI Internal  index:19    from 3 To 0
        SetMemory(0x66018C, Add, -3),# units:AI Internal  index:20    from 3 To 0
        SetMemory(0x66018C, Add, -768),# units:AI Internal  index:21    from 3 To 0
        SetMemory(0x66018C, Add, -50331648),# units:AI Internal  index:23    from 3 To 0
        SetMemory(0x660190, Add, -50331648),# units:AI Internal  index:27    from 3 To 0
        SetMemory(0x660194, Add, -3),# units:AI Internal  index:28    from 3 To 0
        SetMemory(0x660194, Add, -768),# units:AI Internal  index:29    from 3 To 0
        SetMemory(0x6601A8, Add, -3),# units:AI Internal  index:48    from 3 To 0
        SetMemory(0x6601A8, Add, -50331648),# units:AI Internal  index:51    from 3 To 0
        SetMemory(0x6601AC, Add, -3),# units:AI Internal  index:52    from 3 To 0
        SetMemory(0x6601AC, Add, -768),# units:AI Internal  index:53    from 3 To 0
        SetMemory(0x6601AC, Add, -196608),# units:AI Internal  index:54    from 3 To 0
        SetMemory(0x6601AC, Add, -50331648),# units:AI Internal  index:55    from 3 To 0
        SetMemory(0x6601B0, Add, -3),# units:AI Internal  index:56    from 3 To 0
        SetMemory(0x6601C0, Add, -196608),# units:AI Internal  index:74    from 3 To 0
        SetMemory(0x6601C0, Add, -50331648),# units:AI Internal  index:75    from 3 To 0
        SetMemory(0x6601C4, Add, -3),# units:AI Internal  index:76    from 3 To 0
        SetMemory(0x6601C4, Add, -768),# units:AI Internal  index:77    from 3 To 0
        SetMemory(0x6601C4, Add, -196608),# units:AI Internal  index:78    from 3 To 0
        SetMemory(0x6601C4, Add, -50331648),# units:AI Internal  index:79    from 3 To 0
        SetMemory(0x6601C8, Add, -3),# units:AI Internal  index:80    from 3 To 0
        SetMemory(0x6601CC, Add, -196608),# units:AI Internal  index:86    from 3 To 0
        SetMemory(0x6601CC, Add, -50331648),# units:AI Internal  index:87    from 3 To 0
        SetMemory(0x6601D0, Add, -3),# units:AI Internal  index:88    from 3 To 0
        SetMemory(0x6601D8, Add, -50331648),# units:AI Internal  index:99    from 3 To 0
        SetMemory(0x6601DC, Add, -3),# units:AI Internal  index:100    from 3 To 0
        SetMemory(0x6601DC, Add, -196608),# units:AI Internal  index:102    from 3 To 0
        SetMemory(0x6601E0, Add, -3),# units:AI Internal  index:104    from 3 To 0
        SetMemory(0x6601E4, Add, -50331648),# units:AI Internal  index:111    from 3 To 0
        SetMemory(0x6601FC, Add, -768),# units:AI Internal  index:133    from 3 To 0
        SetMemory(0x6601FC, Add, -50331648),# units:AI Internal  index:135    from 3 To 0
        SetMemory(0x660200, Add, -3),# units:AI Internal  index:136    from 3 To 0
        SetMemory(0x660200, Add, -768),# units:AI Internal  index:137    from 3 To 0
        SetMemory(0x660200, Add, -196608),# units:AI Internal  index:138    from 3 To 0
        SetMemory(0x660200, Add, -50331648),# units:AI Internal  index:139    from 3 To 0
        SetMemory(0x660204, Add, -3),# units:AI Internal  index:140    from 3 To 0
        SetMemory(0x660204, Add, -196608),# units:AI Internal  index:142    from 3 To 0
        SetMemory(0x660208, Add, -50331648),# units:AI Internal  index:147    from 3 To 0
        SetMemory(0x66020C, Add, -3),# units:AI Internal  index:148    from 3 To 0
        SetMemory(0x66020C, Add, -50331648),# units:AI Internal  index:151    from 3 To 0
        SetMemory(0x660210, Add, -3),# units:AI Internal  index:152    from 3 To 0
        SetMemory(0x660210, Add, -196608),# units:AI Internal  index:154    from 3 To 0
        SetMemory(0x660214, Add, -50331648),# units:AI Internal  index:159    from 3 To 0
        SetMemory(0x660218, Add, -3),# units:AI Internal  index:160    from 3 To 0
        SetMemory(0x660218, Add, -50331648),# units:AI Internal  index:163    from 3 To 0
        SetMemory(0x66021C, Add, -3),# units:AI Internal  index:164    from 3 To 0
        SetMemory(0x66021C, Add, -768),# units:AI Internal  index:165    from 3 To 0
        SetMemory(0x66021C, Add, -196608),# units:AI Internal  index:166    from 3 To 0
        SetMemory(0x66021C, Add, -50331648),# units:AI Internal  index:167    from 3 To 0
        SetMemory(0x660220, Add, -3),# units:AI Internal  index:168    from 3 To 0
        SetMemory(0x660220, Add, -768),# units:AI Internal  index:169    from 3 To 0
        SetMemory(0x660220, Add, -196608),# units:AI Internal  index:170    from 3 To 0
        SetMemory(0x660220, Add, -50331648),# units:AI Internal  index:171    from 3 To 0
        SetMemory(0x660224, Add, -3),# units:AI Internal  index:172    from 3 To 0
        SetMemory(0x660224, Add, -768),# units:AI Internal  index:173    from 3 To 0
        SetMemory(0x660224, Add, -196608),# units:AI Internal  index:174    from 3 To 0
        SetMemory(0x660224, Add, -50331648),# units:AI Internal  index:175    from 3 To 0
        SetMemory(0x664080, Add, -65536),# units:Special Ability Flags  index:0    from 402718720 To 402653184
        SetMemory(0x664084, Add, -2163200),# units:Special Ability Flags  index:1    from 404816384 To 402653184
        SetMemory(0x664088, Add, -1073741824),# units:Special Ability Flags  index:2    from 1476395008 To 402653184
        SetMemory(0x66408C, Add, -1073741824),# units:Special Ability Flags  index:3    from 1476395008 To 402653184
        SetMemory(0x664094, Add, -1107296256),# units:Special Ability Flags  index:5    from 1509949440 To 402653184
        SetMemory(0x6640A0, Add, -1109393920),# units:Special Ability Flags  index:8    from 1512047108 To 402653188
        SetMemory(0x6640A8, Add, -65600),# units:Special Ability Flags  index:10    from 402718784 To 402653184
        SetMemory(0x6640AC, Add, -1107296256),# units:Special Ability Flags  index:11    from 1509949444 To 402653188
        SetMemory(0x6640B0, Add, -1142947840),# units:Special Ability Flags  index:12    from 1545601028 To 402653188
        SetMemory(0x6640C0, Add, -2163264),# units:Special Ability Flags  index:16    from 404816448 To 402653184
        SetMemory(0x6640C4, Add, -1073741888),# units:Special Ability Flags  index:17    from 1476395072 To 402653184
        SetMemory(0x6640CC, Add, -1073741888),# units:Special Ability Flags  index:19    from 1476395072 To 402653184
        SetMemory(0x6640D0, Add, -65600),# units:Special Ability Flags  index:20    from 402718784 To 402653184
        SetMemory(0x6640D4, Add, -1109393984),# units:Special Ability Flags  index:21    from 1512047172 To 402653188
        SetMemory(0x6640DC, Add, -1107296320),# units:Special Ability Flags  index:23    from 1509949504 To 402653184
        SetMemory(0x6640EC, Add, -1142947904),# units:Special Ability Flags  index:27    from 1545601092 To 402653188
        SetMemory(0x6640F0, Add, -1142947904),# units:Special Ability Flags  index:28    from 1545601092 To 402653188
        SetMemory(0x6640F4, Add, -1142947904),# units:Special Ability Flags  index:29    from 1545601092 To 402653188
        SetMemory(0x664100, Add, -65536),# units:Special Ability Flags  index:32    from 402718720 To 402653184
        SetMemory(0x664114, Add, -1115264),# units:Special Ability Flags  index:37    from 403768448 To 402653184
        SetMemory(0x664118, Add, -1114240),# units:Special Ability Flags  index:38    from 403767424 To 402653184
        SetMemory(0x66411C, Add, -67174528),# units:Special Ability Flags  index:39    from 469827712 To 402653184
        SetMemory(0x664120, Add, -65664),# units:Special Ability Flags  index:40    from 402718848 To 402653184
        SetMemory(0x66412C, Add, -33620096),# units:Special Ability Flags  index:43    from 436273284 To 402653188
        SetMemory(0x664130, Add, -83951744),# units:Special Ability Flags  index:44    from 486604932 To 402653188
        SetMemory(0x664138, Add, -36765824),# units:Special Ability Flags  index:46    from 439419008 To 402653184
        SetMemory(0x664140, Add, -67174592),# units:Special Ability Flags  index:48    from 469827776 To 402653184
        SetMemory(0x66414C, Add, -2163392),# units:Special Ability Flags  index:51    from 404816576 To 402653184
        SetMemory(0x664150, Add, -36765888),# units:Special Ability Flags  index:52    from 439419072 To 402653184
        SetMemory(0x664154, Add, -1114304),# units:Special Ability Flags  index:53    from 403767488 To 402653184
        SetMemory(0x664158, Add, -1115328),# units:Special Ability Flags  index:54    from 403768512 To 402653184
        SetMemory(0x66415C, Add, -33620160),# units:Special Ability Flags  index:55    from 436273348 To 402653188
        SetMemory(0x664160, Add, -83951808),# units:Special Ability Flags  index:56    from 486604996 To 402653188
        SetMemory(0x664174, Add, -4259840),# units:Special Ability Flags  index:61    from 406913024 To 402653184
        SetMemory(0x66417C, Add, -69206272),# units:Special Ability Flags  index:63    from 471859456 To 402653184
        SetMemory(0x664184, Add, -65536),# units:Special Ability Flags  index:65    from 402718720 To 402653184
        SetMemory(0x664188, Add, -1107296256),# units:Special Ability Flags  index:66    from 1509949440 To 402653184
        SetMemory(0x66418C, Add, -2162688),# units:Special Ability Flags  index:67    from 404815872 To 402653184
        SetMemory(0x664190, Add, -67109120),# units:Special Ability Flags  index:68    from 469762304 To 402653184
        SetMemory(0x664194, Add, -1107312644),# units:Special Ability Flags  index:69    from 1509965828 To 402653184
        SetMemory(0x664198, Add, -1107296256),# units:Special Ability Flags  index:70    from 1509949444 To 402653188
        SetMemory(0x66419C, Add, -1109393408),# units:Special Ability Flags  index:71    from 1512046596 To 402653188
        SetMemory(0x6641A8, Add, -4259840),# units:Special Ability Flags  index:74    from 406913024 To 402653184
        SetMemory(0x6641AC, Add, -4259904),# units:Special Ability Flags  index:75    from 406913088 To 402653184
        SetMemory(0x6641B0, Add, -67109184),# units:Special Ability Flags  index:76    from 469762368 To 402653184
        SetMemory(0x6641B4, Add, -65600),# units:Special Ability Flags  index:77    from 402718784 To 402653184
        SetMemory(0x6641B8, Add, -1107296320),# units:Special Ability Flags  index:78    from 1509949504 To 402653184
        SetMemory(0x6641BC, Add, -2162752),# units:Special Ability Flags  index:79    from 404815936 To 402653184
        SetMemory(0x6641C0, Add, -1107296320),# units:Special Ability Flags  index:80    from 1509949508 To 402653188
        SetMemory(0x6641CC, Add, 4),# units:Special Ability Flags  index:83    from 1543520256 To 1543520260
        SetMemory(0x6641D8, Add, -1109393472),# units:Special Ability Flags  index:86    from 1512046660 To 402653188
        SetMemory(0x6641DC, Add, -2162752),# units:Special Ability Flags  index:87    from 404815936 To 402653184
        SetMemory(0x6641E0, Add, -1107296320),# units:Special Ability Flags  index:88    from 1509949508 To 402653188
        SetMemory(0x6641F4, Add, -65536),# units:Special Ability Flags  index:93    from 402718720 To 402653184
        SetMemory(0x6641F8, Add, -65540),# units:Special Ability Flags  index:94    from 402718724 To 402653184
        SetMemory(0x6641FC, Add, -65536),# units:Special Ability Flags  index:95    from 402718720 To 402653184
        SetMemory(0x664200, Add, -65536),# units:Special Ability Flags  index:96    from 402718720 To 402653184
        SetMemory(0x66420C, Add, -2163264),# units:Special Ability Flags  index:99    from 404816448 To 402653184
        SetMemory(0x664210, Add, -2163264),# units:Special Ability Flags  index:100    from 404816448 To 402653184
        SetMemory(0x664218, Add, -1142947904),# units:Special Ability Flags  index:102    from 1545601092 To 402653188
        SetMemory(0x66421C, Add, -65664),# units:Special Ability Flags  index:103    from 403767424 To 403701760
        SetMemory(0x664220, Add, -2163392),# units:Special Ability Flags  index:104    from 404816576 To 402653184
        SetMemory(0x66423C, Add, -2885681185),# units:Special Ability Flags  index:111    from 3288334369 To 402653184
        SetMemory(0x664270, Add, -32768),# units:Special Ability Flags  index:124    from 1409319169 To 1409286401
        SetMemory(0x664294, Add, -1828786305),# units:Special Ability Flags  index:133    from 2231439489 To 402653184
        SetMemory(0x66429C, Add, 318570367),# units:Special Ability Flags  index:135    from 84082817 To 402653184
        SetMemory(0x6642A0, Add, 318570367),# units:Special Ability Flags  index:136    from 84082817 To 402653184
        SetMemory(0x6642A4, Add, 318570367),# units:Special Ability Flags  index:137    from 84082817 To 402653184
        SetMemory(0x6642A8, Add, 318570367),# units:Special Ability Flags  index:138    from 84082817 To 402653184
        SetMemory(0x6642AC, Add, 318570367),# units:Special Ability Flags  index:139    from 84082817 To 402653184
        SetMemory(0x6642B0, Add, 318570367),# units:Special Ability Flags  index:140    from 84082817 To 402653184
        SetMemory(0x6642B8, Add, 318570367),# units:Special Ability Flags  index:142    from 84082817 To 402653184
        SetMemory(0x6642CC, Add, 318537599),# units:Special Ability Flags  index:147    from 84115585 To 402653184
        SetMemory(0x6642D0, Add, 318537599),# units:Special Ability Flags  index:148    from 84115585 To 402653184
        SetMemory(0x6642DC, Add, 318537599),# units:Special Ability Flags  index:151    from 84115585 To 402653184
        SetMemory(0x6642E0, Add, 318537599),# units:Special Ability Flags  index:152    from 84115585 To 402653184
        SetMemory(0x6642E8, Add, -2885685249),# units:Special Ability Flags  index:154    from 3288338433 To 402653184
        SetMemory(0x6642FC, Add, -738721793),# units:Special Ability Flags  index:159    from 1141374977 To 402653184
        SetMemory(0x664300, Add, -2886205441),# units:Special Ability Flags  index:160    from 3288858625 To 402653184
        SetMemory(0x66430C, Add, -738721793),# units:Special Ability Flags  index:163    from 1141374977 To 402653184
        SetMemory(0x664310, Add, -738721793),# units:Special Ability Flags  index:164    from 1141374977 To 402653184
        SetMemory(0x664314, Add, -738721793),# units:Special Ability Flags  index:165    from 1141374977 To 402653184
        SetMemory(0x664318, Add, -738721793),# units:Special Ability Flags  index:166    from 1141374977 To 402653184
        SetMemory(0x66431C, Add, -738721793),# units:Special Ability Flags  index:167    from 1141374977 To 402653184
        SetMemory(0x664320, Add, -738197505),# units:Special Ability Flags  index:168    from 1140850689 To 402653184
        SetMemory(0x664324, Add, -738721793),# units:Special Ability Flags  index:169    from 1141374977 To 402653184
        SetMemory(0x664328, Add, -738721793),# units:Special Ability Flags  index:170    from 1141374977 To 402653184
        SetMemory(0x66432C, Add, -738721793),# units:Special Ability Flags  index:171    from 1141374977 To 402653184
        SetMemory(0x664330, Add, -740818945),# units:Special Ability Flags  index:172    from 1143472129 To 402653184
        SetMemory(0x664334, Add, -201326593),# units:Special Ability Flags  index:173    from 603979777 To 402653184
        SetMemory(0x664338, Add, 335544319),# units:Special Ability Flags  index:174    from 67108865 To 402653184
        SetMemory(0x66433C, Add, 335544319),# units:Special Ability Flags  index:175    from 67108865 To 402653184
        SetMemory(0x664390, Add, 515),# units:Special Ability Flags  index:196    from 536870913 To 536871428
        SetMemory(0x6632BC, Add, -768),# units:Sight Range  index:133    from 11 To 8
        SetMemory(0x6632C0, Add, -1),# units:Sight Range  index:136    from 8 To 7
        SetMemory(0x6632C0, Add, -256),# units:Sight Range  index:137    from 8 To 7
        SetMemory(0x6632C0, Add, -65536),# units:Sight Range  index:138    from 8 To 7
        SetMemory(0x6632C0, Add, -16777216),# units:Sight Range  index:139    from 8 To 7
        SetMemory(0x6632C4, Add, -1),# units:Sight Range  index:140    from 8 To 7
        SetMemory(0x6632C4, Add, -65536),# units:Sight Range  index:142    from 8 To 7
        SetMemory(0x6632C8, Add, -16777216),# units:Sight Range  index:147    from 8 To 7
        SetMemory(0x6632CC, Add, -1),# units:Sight Range  index:148    from 8 To 7
        SetMemory(0x6632CC, Add, -16777216),# units:Sight Range  index:151    from 8 To 7
        SetMemory(0x6632D0, Add, -1),# units:Sight Range  index:152    from 8 To 7
        SetMemory(0x6632D0, Add, -262144),# units:Sight Range  index:154    from 11 To 7
        SetMemory(0x6632D4, Add, -50331648),# units:Sight Range  index:159    from 10 To 7
        SetMemory(0x6632D8, Add, -3),# units:Sight Range  index:160    from 10 To 7
        SetMemory(0x6632D8, Add, -50331648),# units:Sight Range  index:163    from 10 To 7
        SetMemory(0x6632DC, Add, -3),# units:Sight Range  index:164    from 10 To 7
        SetMemory(0x6632DC, Add, -768),# units:Sight Range  index:165    from 10 To 7
        SetMemory(0x6632DC, Add, -196608),# units:Sight Range  index:166    from 10 To 7
        SetMemory(0x6632DC, Add, -50331648),# units:Sight Range  index:167    from 10 To 7
        SetMemory(0x6632E0, Add, -1),# units:Sight Range  index:168    from 8 To 7
        SetMemory(0x6632E0, Add, -768),# units:Sight Range  index:169    from 10 To 7
        SetMemory(0x6632E0, Add, -196608),# units:Sight Range  index:170    from 10 To 7
        SetMemory(0x6632E0, Add, -50331648),# units:Sight Range  index:171    from 10 To 7
        SetMemory(0x6632E4, Add, -3),# units:Sight Range  index:172    from 10 To 7
        SetMemory(0x6632E4, Add, -768),# units:Sight Range  index:173    from 10 To 7
        SetMemory(0x6632E4, Add, -196608),# units:Sight Range  index:174    from 10 To 7
        SetMemory(0x6632E4, Add, -50331648),# units:Sight Range  index:175    from 10 To 7
        SetMemory(0x6635D4, Add, 256),# units:Armor Upgrade  index:5    from 1 To 2
        SetMemory(0x6635D8, Add, 973078528),# units:Armor Upgrade  index:11    from 2 To 60
        SetMemory(0x6635E0, Add, 2),# units:Armor Upgrade  index:16    from 0 To 2
        SetMemory(0x6635E0, Add, -256),# units:Armor Upgrade  index:17    from 1 To 0
        SetMemory(0x6635E0, Add, -16777216),# units:Armor Upgrade  index:19    from 1 To 0
        SetMemory(0x6635E4, Add, -256),# units:Armor Upgrade  index:21    from 2 To 1
        SetMemory(0x6635F4, Add, -256),# units:Armor Upgrade  index:37    from 3 To 2
        SetMemory(0x6635F4, Add, -196608),# units:Armor Upgrade  index:38    from 3 To 0
        SetMemory(0x6635F4, Add, -50331648),# units:Armor Upgrade  index:39    from 3 To 0
        SetMemory(0x6635F8, Add, -3),# units:Armor Upgrade  index:40    from 3 To 0
        SetMemory(0x6635F8, Add, -50331648),# units:Armor Upgrade  index:43    from 4 To 1
        SetMemory(0x6635FC, Add, -2),# units:Armor Upgrade  index:44    from 4 To 2
        SetMemory(0x6635FC, Add, -196608),# units:Armor Upgrade  index:46    from 3 To 0
        SetMemory(0x663600, Add, -1),# units:Armor Upgrade  index:48    from 3 To 2
        SetMemory(0x663600, Add, -33554432),# units:Armor Upgrade  index:51    from 3 To 1
        SetMemory(0x663604, Add, -1),# units:Armor Upgrade  index:52    from 3 To 2
        SetMemory(0x663604, Add, -256),# units:Armor Upgrade  index:53    from 3 To 2
        SetMemory(0x663604, Add, -65536),# units:Armor Upgrade  index:54    from 3 To 2
        SetMemory(0x663604, Add, -33554432),# units:Armor Upgrade  index:55    from 4 To 2
        SetMemory(0x663608, Add, -2),# units:Armor Upgrade  index:56    from 4 To 2
        SetMemory(0x66360C, Add, -1280),# units:Armor Upgrade  index:61    from 5 To 0
        SetMemory(0x66360C, Add, -83886080),# units:Armor Upgrade  index:63    from 5 To 0
        SetMemory(0x663610, Add, -327680),# units:Armor Upgrade  index:66    from 5 To 0
        SetMemory(0x663610, Add, -67108864),# units:Armor Upgrade  index:67    from 5 To 1
        SetMemory(0x663614, Add, -5),# units:Armor Upgrade  index:68    from 5 To 0
        SetMemory(0x663614, Add, 13824),# units:Armor Upgrade  index:69    from 6 To 60
        SetMemory(0x663614, Add, -262144),# units:Armor Upgrade  index:70    from 6 To 2
        SetMemory(0x663614, Add, -100663296),# units:Armor Upgrade  index:71    from 6 To 0
        SetMemory(0x663618, Add, -262144),# units:Armor Upgrade  index:74    from 5 To 1
        SetMemory(0x663618, Add, -67108864),# units:Armor Upgrade  index:75    from 5 To 1
        SetMemory(0x66361C, Add, -3),# units:Armor Upgrade  index:76    from 5 To 2
        SetMemory(0x66361C, Add, -1024),# units:Armor Upgrade  index:77    from 5 To 1
        SetMemory(0x66361C, Add, -327680),# units:Armor Upgrade  index:78    from 5 To 0
        SetMemory(0x66361C, Add, -67108864),# units:Armor Upgrade  index:79    from 5 To 1
        SetMemory(0x663620, Add, -5),# units:Armor Upgrade  index:80    from 6 To 1
        SetMemory(0x663624, Add, -262144),# units:Armor Upgrade  index:86    from 6 To 2
        SetMemory(0x663624, Add, -83886080),# units:Armor Upgrade  index:87    from 5 To 0
        SetMemory(0x66362C, Add, -7680),# units:Armor Upgrade  index:93    from 60 To 30
        SetMemory(0x66362C, Add, -1900544),# units:Armor Upgrade  index:94    from 60 To 31
        SetMemory(0x66362C, Add, -469762048),# units:Armor Upgrade  index:95    from 60 To 32
        SetMemory(0x663630, Add, -27),# units:Armor Upgrade  index:96    from 60 To 33
        SetMemory(0x663630, Add, 16777216),# units:Armor Upgrade  index:99    from 0 To 1
        SetMemory(0x663634, Add, 2),# units:Armor Upgrade  index:100    from 0 To 2
        SetMemory(0x66367C, Add, 0),# units:Armor Upgrade  index:175    from 60 To 60
        SetMemory(0x6621DC, Add, 512),# units:Unit Size  index:93    from 1 To 3
        SetMemory(0x6621DC, Add, 65536),# units:Unit Size  index:94    from 1 To 2
        SetMemory(0x6621DC, Add, 0),# units:Unit Size  index:95    from 1 To 1
        SetMemory(0x6621E0, Add, -1),# units:Unit Size  index:96    from 1 To 0
        SetMemory(0x662208, Add, -2),# units:Unit Size  index:136    from 3 To 1
        SetMemory(0x662208, Add, -512),# units:Unit Size  index:137    from 3 To 1
        SetMemory(0x662208, Add, -131072),# units:Unit Size  index:138    from 3 To 1
        SetMemory(0x662208, Add, -33554432),# units:Unit Size  index:139    from 3 To 1
        SetMemory(0x66220C, Add, -2),# units:Unit Size  index:140    from 3 To 1
        SetMemory(0x66220C, Add, -131072),# units:Unit Size  index:142    from 3 To 1
        SetMemory(0x662210, Add, -33554432),# units:Unit Size  index:147    from 3 To 1
        SetMemory(0x662214, Add, -2),# units:Unit Size  index:148    from 3 To 1
        SetMemory(0x662214, Add, -33554432),# units:Unit Size  index:151    from 3 To 1
        SetMemory(0x662218, Add, -2),# units:Unit Size  index:152    from 3 To 1
        SetMemory(0x662218, Add, -131072),# units:Unit Size  index:154    from 3 To 1
        SetMemory(0x66221C, Add, -33554432),# units:Unit Size  index:159    from 3 To 1
        SetMemory(0x662220, Add, -2),# units:Unit Size  index:160    from 3 To 1
        SetMemory(0x662220, Add, -33554432),# units:Unit Size  index:163    from 3 To 1
        SetMemory(0x662224, Add, -2),# units:Unit Size  index:164    from 3 To 1
        SetMemory(0x662224, Add, -512),# units:Unit Size  index:165    from 3 To 1
        SetMemory(0x662224, Add, -131072),# units:Unit Size  index:166    from 3 To 1
        SetMemory(0x662224, Add, -33554432),# units:Unit Size  index:167    from 3 To 1
        SetMemory(0x662228, Add, -2),# units:Unit Size  index:168    from 3 To 1
        SetMemory(0x662228, Add, -512),# units:Unit Size  index:169    from 3 To 1
        SetMemory(0x662228, Add, -131072),# units:Unit Size  index:170    from 3 To 1
        SetMemory(0x662228, Add, -33554432),# units:Unit Size  index:171    from 3 To 1
        SetMemory(0x66222C, Add, -2),# units:Unit Size  index:172    from 3 To 1
        SetMemory(0x66222C, Add, -512),# units:Unit Size  index:173    from 3 To 1
        SetMemory(0x66222C, Add, -131072),# units:Unit Size  index:174    from 3 To 1
        SetMemory(0x66222C, Add, -33554432),# units:Unit Size  index:175    from 3 To 1
        SetMemory(0x65FEC8, Add, -16777216),# units:Armor  index:3    from 1 To 0
        SetMemory(0x65FECC, Add, -256),# units:Armor  index:5    from 1 To 0
        SetMemory(0x65FED8, Add, -3),# units:Armor  index:16    from 3 To 0
        SetMemory(0x65FED8, Add, -768),# units:Armor  index:17    from 3 To 0
        SetMemory(0x65FED8, Add, -50331648),# units:Armor  index:19    from 3 To 0
        SetMemory(0x65FEDC, Add, -1024),# units:Armor  index:21    from 4 To 0
        SetMemory(0x65FEDC, Add, -50331648),# units:Armor  index:23    from 3 To 0
        SetMemory(0x65FEEC, Add, -16777216),# units:Armor  index:39    from 1 To 0
        SetMemory(0x65FEF4, Add, -2),# units:Armor  index:44    from 2 To 0
        SetMemory(0x65FEF4, Add, -65536),# units:Armor  index:46    from 1 To 0
        SetMemory(0x65FEF8, Add, -4),# units:Armor  index:48    from 4 To 0
        SetMemory(0x65FEF8, Add, -33554432),# units:Armor  index:51    from 2 To 0
        SetMemory(0x65FEFC, Add, -3),# units:Armor  index:52    from 3 To 0
        SetMemory(0x65FEFC, Add, -512),# units:Armor  index:53    from 2 To 0
        SetMemory(0x65FEFC, Add, -196608),# units:Armor  index:54    from 3 To 0
        SetMemory(0x65FEFC, Add, -50331648),# units:Armor  index:55    from 3 To 0
        SetMemory(0x65FF00, Add, -4),# units:Armor  index:56    from 4 To 0
        SetMemory(0x65FF04, Add, -256),# units:Armor  index:61    from 1 To 0
        SetMemory(0x65FF04, Add, -16777216),# units:Armor  index:63    from 1 To 0
        SetMemory(0x65FF08, Add, -65536),# units:Armor  index:66    from 1 To 0
        SetMemory(0x65FF0C, Add, -16777216),# units:Armor  index:71    from 1 To 0
        SetMemory(0x65FF14, Add, -3),# units:Armor  index:76    from 3 To 0
        SetMemory(0x65FF14, Add, -512),# units:Armor  index:77    from 2 To 0
        SetMemory(0x65FF14, Add, -196608),# units:Armor  index:78    from 3 To 0
        SetMemory(0x65FF14, Add, -33554432),# units:Armor  index:79    from 2 To 0
        SetMemory(0x65FF18, Add, -3),# units:Armor  index:80    from 3 To 0
        SetMemory(0x65FF1C, Add, -196608),# units:Armor  index:86    from 3 To 0
        SetMemory(0x65FF1C, Add, -33554432),# units:Armor  index:87    from 2 To 0
        SetMemory(0x65FF28, Add, -33554432),# units:Armor  index:99    from 2 To 0
        SetMemory(0x65FF2C, Add, -3),# units:Armor  index:100    from 3 To 0
        SetMemory(0x65FF50, Add, -1),# units:Armor  index:136    from 1 To 0
        SetMemory(0x65FF50, Add, -256),# units:Armor  index:137    from 1 To 0
        SetMemory(0x65FF50, Add, -65536),# units:Armor  index:138    from 1 To 0
        SetMemory(0x65FF50, Add, -16777216),# units:Armor  index:139    from 1 To 0
        SetMemory(0x65FF54, Add, -1),# units:Armor  index:140    from 1 To 0
        SetMemory(0x65FF54, Add, -65536),# units:Armor  index:142    from 1 To 0
        SetMemory(0x65FF58, Add, -16777216),# units:Armor  index:147    from 1 To 0
        SetMemory(0x65FF5C, Add, -1),# units:Armor  index:148    from 1 To 0
        SetMemory(0x65FF5C, Add, -16777216),# units:Armor  index:151    from 1 To 0
        SetMemory(0x65FF60, Add, -1),# units:Armor  index:152    from 1 To 0
        SetMemory(0x65FF60, Add, -65536),# units:Armor  index:154    from 1 To 0
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
        SetMemory(0x6620C4, Add, -65536),# units:Right-click Action  index:46    from 2 To 1
        SetMemory(0x6620CC, Add, -1),# units:Right-click Action  index:52    from 2 To 1
        SetMemory(0x6620D4, Add, -16777216),# units:Right-click Action  index:63    from 2 To 1
        SetMemory(0x6620D8, Add, -16777216),# units:Right-click Action  index:67    from 2 To 1
        SetMemory(0x6620DC, Add, -256),# units:Right-click Action  index:69    from 2 To 1
        SetMemory(0x662104, Add, 0),# units:Right-click Action  index:111    from 2 To 2
        SetMemory(0x66211C, Add, 512),# units:Right-click Action  index:133    from 0 To 2
        SetMemory(0x66211C, Add, 33554432),# units:Right-click Action  index:135    from 0 To 2
        SetMemory(0x662120, Add, 2),# units:Right-click Action  index:136    from 0 To 2
        SetMemory(0x662120, Add, 512),# units:Right-click Action  index:137    from 0 To 2
        SetMemory(0x662120, Add, 131072),# units:Right-click Action  index:138    from 0 To 2
        SetMemory(0x662120, Add, 33554432),# units:Right-click Action  index:139    from 0 To 2
        SetMemory(0x662124, Add, 2),# units:Right-click Action  index:140    from 0 To 2
        SetMemory(0x662124, Add, 131072),# units:Right-click Action  index:142    from 0 To 2
        SetMemory(0x662128, Add, 33554432),# units:Right-click Action  index:147    from 0 To 2
        SetMemory(0x66212C, Add, 2),# units:Right-click Action  index:148    from 0 To 2
        SetMemory(0x66212C, Add, 33554432),# units:Right-click Action  index:151    from 0 To 2
        SetMemory(0x662130, Add, 2),# units:Right-click Action  index:152    from 0 To 2
        SetMemory(0x662130, Add, 131072),# units:Right-click Action  index:154    from 0 To 2
        SetMemory(0x662134, Add, 33554432),# units:Right-click Action  index:159    from 0 To 2
        SetMemory(0x662138, Add, 2),# units:Right-click Action  index:160    from 0 To 2
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
        SetMemory(0x662144, Add, 131072),# units:Right-click Action  index:174    from 0 To 2
        SetMemory(0x662144, Add, 33554432),# units:Right-click Action  index:175    from 0 To 2
        SetMemory(0x661FC0, Add, -275),# units:Ready Sound  index:0    from 275 To 0
        SetMemory(0x661FC0, Add, -14745600),# units:Ready Sound  index:1    from 225 To 0
        SetMemory(0x661FC4, Add, -352),# units:Ready Sound  index:2    from 352 To 0
        SetMemory(0x661FC4, Add, -15794176),# units:Ready Sound  index:3    from 241 To 0
        SetMemory(0x661FC8, Add, -20709376),# units:Ready Sound  index:5    from 316 To 0
        SetMemory(0x661FD0, Add, -256),# units:Ready Sound  index:8    from 256 To 0
        SetMemory(0x661FD4, Add, -295),# units:Ready Sound  index:10    from 295 To 0
        SetMemory(0x661FD4, Add, -13697024),# units:Ready Sound  index:11    from 209 To 0
        SetMemory(0x661FD8, Add, -176),# units:Ready Sound  index:12    from 176 To 0
        SetMemory(0x661FE0, Add, -15794176),# units:Ready Sound  index:17    from 241 To 0
        SetMemory(0x661FE8, Add, -16777216),# units:Ready Sound  index:21    from 256 To 0
        SetMemory(0x662000, Add, -295),# units:Ready Sound  index:32    from 295 To 0
        SetMemory(0x662008, Add, -58982400),# units:Ready Sound  index:37    from 900 To 0
        SetMemory(0x66200C, Add, -866),# units:Ready Sound  index:38    from 866 To 0
        SetMemory(0x66200C, Add, -57802752),# units:Ready Sound  index:39    from 882 To 0
        SetMemory(0x662010, Add, -787),# units:Ready Sound  index:40    from 787 To 0
        SetMemory(0x662014, Add, -61669376),# units:Ready Sound  index:43    from 941 To 0
        SetMemory(0x662018, Add, -857),# units:Ready Sound  index:44    from 857 To 0
        SetMemory(0x66201C, Add, -814),# units:Ready Sound  index:46    from 814 To 0
        SetMemory(0x662020, Add, -882),# units:Ready Sound  index:48    from 882 To 0
        SetMemory(0x662028, Add, -814),# units:Ready Sound  index:52    from 814 To 0
        SetMemory(0x662028, Add, -56754176),# units:Ready Sound  index:53    from 866 To 0
        SetMemory(0x66202C, Add, -900),# units:Ready Sound  index:54    from 900 To 0
        SetMemory(0x66202C, Add, -61669376),# units:Ready Sound  index:55    from 941 To 0
        SetMemory(0x662030, Add, -857),# units:Ready Sound  index:56    from 857 To 0
        SetMemory(0x662038, Add, -47710208),# units:Ready Sound  index:61    from 728 To 0
        SetMemory(0x66203C, Add, -69795840),# units:Ready Sound  index:63    from 1065 To 0
        SetMemory(0x662040, Add, -43646976),# units:Ready Sound  index:65    from 666 To 0
        SetMemory(0x662044, Add, -492),# units:Ready Sound  index:66    from 492 To 0
        SetMemory(0x662044, Add, -40763392),# units:Ready Sound  index:67    from 622 To 0
        SetMemory(0x662048, Add, -567),# units:Ready Sound  index:68    from 567 To 0
        SetMemory(0x662048, Add, -33619968),# units:Ready Sound  index:69    from 513 To 0
        SetMemory(0x66204C, Add, -534),# units:Ready Sound  index:70    from 534 To 0
        SetMemory(0x66204C, Add, -35979264),# units:Ready Sound  index:71    from 549 To 0
        SetMemory(0x662054, Add, -728),# units:Ready Sound  index:74    from 728 To 0
        SetMemory(0x662058, Add, -567),# units:Ready Sound  index:76    from 567 To 0
        SetMemory(0x662060, Add, -534),# units:Ready Sound  index:80    from 534 To 0
        SetMemory(0x66206C, Add, -549),# units:Ready Sound  index:86    from 549 To 0
        SetMemory(0x66208C, Add, -70713344),# units:Ready Sound  index:103    from 1079 To 0
        SetMemory(0x65FFB0, Add, -287),# units:What Sound Start  index:0    from 287 To 0
        SetMemory(0x65FFB0, Add, -15073280),# units:What Sound Start  index:1    from 230 To 0
        SetMemory(0x65FFB4, Add, -360),# units:What Sound Start  index:2    from 360 To 0
        SetMemory(0x65FFB4, Add, -16252928),# units:What Sound Start  index:3    from 248 To 0
        SetMemory(0x65FFB8, Add, -21233664),# units:What Sound Start  index:5    from 324 To 0
        SetMemory(0x65FFC0, Add, -265),# units:What Sound Start  index:8    from 265 To 0
        SetMemory(0x65FFC4, Add, -299),# units:What Sound Start  index:10    from 299 To 0
        SetMemory(0x65FFC4, Add, -14090240),# units:What Sound Start  index:11    from 215 To 0
        SetMemory(0x65FFC8, Add, -185),# units:What Sound Start  index:12    from 185 To 0
        SetMemory(0x65FFD0, Add, -462),# units:What Sound Start  index:16    from 462 To 0
        SetMemory(0x65FFD0, Add, -16252928),# units:What Sound Start  index:17    from 248 To 0
        SetMemory(0x65FFD4, Add, -27721728),# units:What Sound Start  index:19    from 423 To 0
        SetMemory(0x65FFD8, Add, -411),# units:What Sound Start  index:20    from 411 To 0
        SetMemory(0x65FFD8, Add, -17367040),# units:What Sound Start  index:21    from 265 To 0
        SetMemory(0x65FFDC, Add, -28573696),# units:What Sound Start  index:23    from 436 To 0
        SetMemory(0x65FFE4, Add, -29425664),# units:What Sound Start  index:27    from 449 To 0
        SetMemory(0x65FFE8, Add, -411),# units:What Sound Start  index:28    from 411 To 0
        SetMemory(0x65FFE8, Add, -29425664),# units:What Sound Start  index:29    from 449 To 0
        SetMemory(0x65FFF0, Add, -299),# units:What Sound Start  index:32    from 299 To 0
        SetMemory(0x65FFF8, Add, -59047936),# units:What Sound Start  index:37    from 901 To 0
        SetMemory(0x65FFFC, Add, -870),# units:What Sound Start  index:38    from 870 To 0
        SetMemory(0x65FFFC, Add, -58064896),# units:What Sound Start  index:39    from 886 To 0
        SetMemory(0x660000, Add, -792),# units:What Sound Start  index:40    from 792 To 0
        SetMemory(0x660004, Add, -62062592),# units:What Sound Start  index:43    from 947 To 0
        SetMemory(0x660008, Add, -858),# units:What Sound Start  index:44    from 858 To 0
        SetMemory(0x66000C, Add, -821),# units:What Sound Start  index:46    from 821 To 0
        SetMemory(0x660010, Add, -886),# units:What Sound Start  index:48    from 886 To 0
        SetMemory(0x660014, Add, -62849024),# units:What Sound Start  index:51    from 959 To 0
        SetMemory(0x660018, Add, -821),# units:What Sound Start  index:52    from 821 To 0
        SetMemory(0x660018, Add, -57016320),# units:What Sound Start  index:53    from 870 To 0
        SetMemory(0x66001C, Add, -901),# units:What Sound Start  index:54    from 901 To 0
        SetMemory(0x66001C, Add, -62062592),# units:What Sound Start  index:55    from 947 To 0
        SetMemory(0x660020, Add, -858),# units:What Sound Start  index:56    from 858 To 0
        SetMemory(0x660028, Add, -48037888),# units:What Sound Start  index:61    from 733 To 0
        SetMemory(0x66002C, Add, -70189056),# units:What Sound Start  index:63    from 1071 To 0
        SetMemory(0x660030, Add, -43909120),# units:What Sound Start  index:65    from 670 To 0
        SetMemory(0x660034, Add, -498),# units:What Sound Start  index:66    from 498 To 0
        SetMemory(0x660034, Add, -41091072),# units:What Sound Start  index:67    from 627 To 0
        SetMemory(0x660038, Add, -573),# units:What Sound Start  index:68    from 573 To 0
        SetMemory(0x660038, Add, -34078720),# units:What Sound Start  index:69    from 520 To 0
        SetMemory(0x66003C, Add, -540),# units:What Sound Start  index:70    from 540 To 0
        SetMemory(0x66003C, Add, -36634624),# units:What Sound Start  index:71    from 559 To 0
        SetMemory(0x660044, Add, -733),# units:What Sound Start  index:74    from 733 To 0
        SetMemory(0x660044, Add, -48889856),# units:What Sound Start  index:75    from 746 To 0
        SetMemory(0x660048, Add, -573),# units:What Sound Start  index:76    from 573 To 0
        SetMemory(0x660048, Add, -45547520),# units:What Sound Start  index:77    from 695 To 0
        SetMemory(0x66004C, Add, -683),# units:What Sound Start  index:78    from 683 To 0
        SetMemory(0x66004C, Add, -47120384),# units:What Sound Start  index:79    from 719 To 0
        SetMemory(0x660050, Add, -540),# units:What Sound Start  index:80    from 540 To 0
        SetMemory(0x66005C, Add, -559),# units:What Sound Start  index:86    from 559 To 0
        SetMemory(0x660060, Add, -1136),# units:What Sound Start  index:88    from 1136 To 0
        SetMemory(0x660068, Add, -63700992),# units:What Sound Start  index:93    from 972 To 0
        SetMemory(0x66006C, Add, -976),# units:What Sound Start  index:94    from 976 To 0
        SetMemory(0x66006C, Add, -3276800),# units:What Sound Start  index:95    from 50 To 0
        SetMemory(0x660070, Add, -968),# units:What Sound Start  index:96    from 968 To 0
        SetMemory(0x660074, Add, -64815104),# units:What Sound Start  index:99    from 989 To 0
        SetMemory(0x660078, Add, -230),# units:What Sound Start  index:100    from 230 To 0
        SetMemory(0x66007C, Add, -449),# units:What Sound Start  index:102    from 449 To 0
        SetMemory(0x66007C, Add, -71106560),# units:What Sound Start  index:103    from 1085 To 0
        SetMemory(0x660080, Add, -1121),# units:What Sound Start  index:104    from 1121 To 0
        SetMemory(0x66008C, Add, -983040),# units:What Sound Start  index:111    from 15 To 0
        SetMemory(0x6600B8, Add, -49807360),# units:What Sound Start  index:133    from 760 To 0
        SetMemory(0x6600BC, Add, -50528256),# units:What Sound Start  index:135    from 771 To 0
        SetMemory(0x6600C0, Add, -766),# units:What Sound Start  index:136    from 766 To 0
        SetMemory(0x6600C0, Add, -50135040),# units:What Sound Start  index:137    from 765 To 0
        SetMemory(0x6600C4, Add, -767),# units:What Sound Start  index:138    from 767 To 0
        SetMemory(0x6600C4, Add, -49610752),# units:What Sound Start  index:139    from 757 To 0
        SetMemory(0x6600C8, Add, -770),# units:What Sound Start  index:140    from 770 To 0
        SetMemory(0x6600CC, Add, -755),# units:What Sound Start  index:142    from 755 To 0
        SetMemory(0x6600D4, Add, -50397184),# units:What Sound Start  index:147    from 769 To 0
        SetMemory(0x6600D8, Add, -769),# units:What Sound Start  index:148    from 769 To 0
        SetMemory(0x6600DC, Add, -49545216),# units:What Sound Start  index:151    from 756 To 0
        SetMemory(0x6600E0, Add, -756),# units:What Sound Start  index:152    from 756 To 0
        SetMemory(0x6600E4, Add, -484),# units:What Sound Start  index:154    from 484 To 0
        SetMemory(0x6600EC, Add, -31195136),# units:What Sound Start  index:159    from 476 To 0
        SetMemory(0x6600F0, Add, -479),# units:What Sound Start  index:160    from 479 To 0
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
        SetMemory(0x662BF0, Add, -290),# units:What Sound End  index:0    from 290 To 0
        SetMemory(0x662BF0, Add, -15269888),# units:What Sound End  index:1    from 233 To 0
        SetMemory(0x662BF4, Add, -363),# units:What Sound End  index:2    from 363 To 0
        SetMemory(0x662BF4, Add, -16449536),# units:What Sound End  index:3    from 251 To 0
        SetMemory(0x662BF8, Add, -21430272),# units:What Sound End  index:5    from 327 To 0
        SetMemory(0x662C00, Add, -268),# units:What Sound End  index:8    from 268 To 0
        SetMemory(0x662C04, Add, -302),# units:What Sound End  index:10    from 302 To 0
        SetMemory(0x662C04, Add, -14286848),# units:What Sound End  index:11    from 218 To 0
        SetMemory(0x662C08, Add, -188),# units:What Sound End  index:12    from 188 To 0
        SetMemory(0x662C10, Add, -465),# units:What Sound End  index:16    from 465 To 0
        SetMemory(0x662C10, Add, -16449536),# units:What Sound End  index:17    from 251 To 0
        SetMemory(0x662C14, Add, -27918336),# units:What Sound End  index:19    from 426 To 0
        SetMemory(0x662C18, Add, -414),# units:What Sound End  index:20    from 414 To 0
        SetMemory(0x662C18, Add, -17563648),# units:What Sound End  index:21    from 268 To 0
        SetMemory(0x662C1C, Add, -28770304),# units:What Sound End  index:23    from 439 To 0
        SetMemory(0x662C24, Add, -29622272),# units:What Sound End  index:27    from 452 To 0
        SetMemory(0x662C28, Add, -414),# units:What Sound End  index:28    from 414 To 0
        SetMemory(0x662C28, Add, -29622272),# units:What Sound End  index:29    from 452 To 0
        SetMemory(0x662C30, Add, -302),# units:What Sound End  index:32    from 302 To 0
        SetMemory(0x662C38, Add, -59244544),# units:What Sound End  index:37    from 904 To 0
        SetMemory(0x662C3C, Add, -872),# units:What Sound End  index:38    from 872 To 0
        SetMemory(0x662C3C, Add, -57868288),# units:What Sound End  index:39    from 883 To 0
        SetMemory(0x662C40, Add, -795),# units:What Sound End  index:40    from 795 To 0
        SetMemory(0x662C44, Add, -62259200),# units:What Sound End  index:43    from 950 To 0
        SetMemory(0x662C48, Add, -861),# units:What Sound End  index:44    from 861 To 0
        SetMemory(0x662C4C, Add, -823),# units:What Sound End  index:46    from 823 To 0
        SetMemory(0x662C50, Add, -883),# units:What Sound End  index:48    from 883 To 0
        SetMemory(0x662C54, Add, -63045632),# units:What Sound End  index:51    from 962 To 0
        SetMemory(0x662C58, Add, -823),# units:What Sound End  index:52    from 823 To 0
        SetMemory(0x662C58, Add, -57147392),# units:What Sound End  index:53    from 872 To 0
        SetMemory(0x662C5C, Add, -904),# units:What Sound End  index:54    from 904 To 0
        SetMemory(0x662C5C, Add, -62259200),# units:What Sound End  index:55    from 950 To 0
        SetMemory(0x662C60, Add, -861),# units:What Sound End  index:56    from 861 To 0
        SetMemory(0x662C68, Add, -48234496),# units:What Sound End  index:61    from 736 To 0
        SetMemory(0x662C6C, Add, -70385664),# units:What Sound End  index:63    from 1074 To 0
        SetMemory(0x662C70, Add, -44105728),# units:What Sound End  index:65    from 673 To 0
        SetMemory(0x662C74, Add, -505),# units:What Sound End  index:66    from 505 To 0
        SetMemory(0x662C74, Add, -41287680),# units:What Sound End  index:67    from 630 To 0
        SetMemory(0x662C78, Add, -576),# units:What Sound End  index:68    from 576 To 0
        SetMemory(0x662C78, Add, -34275328),# units:What Sound End  index:69    from 523 To 0
        SetMemory(0x662C7C, Add, -543),# units:What Sound End  index:70    from 543 To 0
        SetMemory(0x662C7C, Add, -36831232),# units:What Sound End  index:71    from 562 To 0
        SetMemory(0x662C84, Add, -736),# units:What Sound End  index:74    from 736 To 0
        SetMemory(0x662C84, Add, -49086464),# units:What Sound End  index:75    from 749 To 0
        SetMemory(0x662C88, Add, -576),# units:What Sound End  index:76    from 576 To 0
        SetMemory(0x662C88, Add, -45744128),# units:What Sound End  index:77    from 698 To 0
        SetMemory(0x662C8C, Add, -686),# units:What Sound End  index:78    from 686 To 0
        SetMemory(0x662C8C, Add, -47316992),# units:What Sound End  index:79    from 722 To 0
        SetMemory(0x662C90, Add, -543),# units:What Sound End  index:80    from 543 To 0
        SetMemory(0x662C9C, Add, -562),# units:What Sound End  index:86    from 562 To 0
        SetMemory(0x662CA0, Add, -1139),# units:What Sound End  index:88    from 1139 To 0
        SetMemory(0x662CA8, Add, -63832064),# units:What Sound End  index:93    from 974 To 0
        SetMemory(0x662CAC, Add, -978),# units:What Sound End  index:94    from 978 To 0
        SetMemory(0x662CAC, Add, -3407872),# units:What Sound End  index:95    from 52 To 0
        SetMemory(0x662CB0, Add, -970),# units:What Sound End  index:96    from 970 To 0
        SetMemory(0x662CB4, Add, -65011712),# units:What Sound End  index:99    from 992 To 0
        SetMemory(0x662CB8, Add, -233),# units:What Sound End  index:100    from 233 To 0
        SetMemory(0x662CBC, Add, -452),# units:What Sound End  index:102    from 452 To 0
        SetMemory(0x662CBC, Add, -71303168),# units:What Sound End  index:103    from 1088 To 0
        SetMemory(0x662CC0, Add, -1124),# units:What Sound End  index:104    from 1124 To 0
        SetMemory(0x662CCC, Add, -983040),# units:What Sound End  index:111    from 15 To 0
        SetMemory(0x662CF8, Add, -49807360),# units:What Sound End  index:133    from 760 To 0
        SetMemory(0x662CFC, Add, -50528256),# units:What Sound End  index:135    from 771 To 0
        SetMemory(0x662D00, Add, -766),# units:What Sound End  index:136    from 766 To 0
        SetMemory(0x662D00, Add, -50135040),# units:What Sound End  index:137    from 765 To 0
        SetMemory(0x662D04, Add, -767),# units:What Sound End  index:138    from 767 To 0
        SetMemory(0x662D04, Add, -49610752),# units:What Sound End  index:139    from 757 To 0
        SetMemory(0x662D08, Add, -770),# units:What Sound End  index:140    from 770 To 0
        SetMemory(0x662D0C, Add, -755),# units:What Sound End  index:142    from 755 To 0
        SetMemory(0x662D14, Add, -50397184),# units:What Sound End  index:147    from 769 To 0
        SetMemory(0x662D18, Add, -769),# units:What Sound End  index:148    from 769 To 0
        SetMemory(0x662D1C, Add, -49545216),# units:What Sound End  index:151    from 756 To 0
        SetMemory(0x662D20, Add, -756),# units:What Sound End  index:152    from 756 To 0
        SetMemory(0x662D24, Add, -484),# units:What Sound End  index:154    from 484 To 0
        SetMemory(0x662D2C, Add, -31195136),# units:What Sound End  index:159    from 476 To 0
        SetMemory(0x662D30, Add, -479),# units:What Sound End  index:160    from 479 To 0
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
        SetMemory(0x663B38, Add, -280),# units:Piss Sound Start  index:0    from 280 To 0
        SetMemory(0x663B38, Add, -14811136),# units:Piss Sound Start  index:1    from 226 To 0
        SetMemory(0x663B3C, Add, -356),# units:Piss Sound Start  index:2    from 356 To 0
        SetMemory(0x663B3C, Add, -15859712),# units:Piss Sound Start  index:3    from 242 To 0
        SetMemory(0x663B40, Add, -20971520),# units:Piss Sound Start  index:5    from 320 To 0
        SetMemory(0x663B48, Add, -258),# units:Piss Sound Start  index:8    from 258 To 0
        SetMemory(0x663B4C, Add, -303),# units:Piss Sound Start  index:10    from 303 To 0
        SetMemory(0x663B4C, Add, -13828096),# units:Piss Sound Start  index:11    from 211 To 0
        SetMemory(0x663B50, Add, -180),# units:Piss Sound Start  index:12    from 180 To 0
        SetMemory(0x663B58, Add, -457),# units:Piss Sound Start  index:16    from 457 To 0
        SetMemory(0x663B58, Add, -15859712),# units:Piss Sound Start  index:17    from 242 To 0
        SetMemory(0x663B5C, Add, -27459584),# units:Piss Sound Start  index:19    from 419 To 0
        SetMemory(0x663B60, Add, -407),# units:Piss Sound Start  index:20    from 407 To 0
        SetMemory(0x663B60, Add, -16908288),# units:Piss Sound Start  index:21    from 258 To 0
        SetMemory(0x663B64, Add, -28246016),# units:Piss Sound Start  index:23    from 431 To 0
        SetMemory(0x663B6C, Add, -29097984),# units:Piss Sound Start  index:27    from 444 To 0
        SetMemory(0x663B70, Add, -407),# units:Piss Sound Start  index:28    from 407 To 0
        SetMemory(0x663B70, Add, -29097984),# units:Piss Sound Start  index:29    from 444 To 0
        SetMemory(0x663B78, Add, -303),# units:Piss Sound Start  index:32    from 303 To 0
        SetMemory(0x663B80, Add, -58785792),# units:Piss Sound Start  index:37    from 897 To 0
        SetMemory(0x663B84, Add, -868),# units:Piss Sound Start  index:38    from 868 To 0
        SetMemory(0x663B84, Add, -57606144),# units:Piss Sound Start  index:39    from 879 To 0
        SetMemory(0x663B88, Add, -788),# units:Piss Sound Start  index:40    from 788 To 0
        SetMemory(0x663B8C, Add, -61800448),# units:Piss Sound Start  index:43    from 943 To 0
        SetMemory(0x663B90, Add, -853),# units:Piss Sound Start  index:44    from 853 To 0
        SetMemory(0x663B94, Add, -818),# units:Piss Sound Start  index:46    from 818 To 0
        SetMemory(0x663B98, Add, -879),# units:Piss Sound Start  index:48    from 879 To 0
        SetMemory(0x663B9C, Add, -62586880),# units:Piss Sound Start  index:51    from 955 To 0
        SetMemory(0x663BA0, Add, -818),# units:Piss Sound Start  index:52    from 818 To 0
        SetMemory(0x663BA0, Add, -56885248),# units:Piss Sound Start  index:53    from 868 To 0
        SetMemory(0x663BA4, Add, -897),# units:Piss Sound Start  index:54    from 897 To 0
        SetMemory(0x663BA4, Add, -61800448),# units:Piss Sound Start  index:55    from 943 To 0
        SetMemory(0x663BA8, Add, -853),# units:Piss Sound Start  index:56    from 853 To 0
        SetMemory(0x663BB0, Add, -47775744),# units:Piss Sound Start  index:61    from 729 To 0
        SetMemory(0x663BB4, Add, -69926912),# units:Piss Sound Start  index:63    from 1067 To 0
        SetMemory(0x663BB8, Add, -43712512),# units:Piss Sound Start  index:65    from 667 To 0
        SetMemory(0x663BBC, Add, -494),# units:Piss Sound Start  index:66    from 494 To 0
        SetMemory(0x663BBC, Add, -40828928),# units:Piss Sound Start  index:67    from 623 To 0
        SetMemory(0x663BC0, Add, -569),# units:Piss Sound Start  index:68    from 569 To 0
        SetMemory(0x663BC0, Add, -33751040),# units:Piss Sound Start  index:69    from 515 To 0
        SetMemory(0x663BC4, Add, -535),# units:Piss Sound Start  index:70    from 535 To 0
        SetMemory(0x663BC4, Add, -36306944),# units:Piss Sound Start  index:71    from 554 To 0
        SetMemory(0x663BCC, Add, -729),# units:Piss Sound Start  index:74    from 729 To 0
        SetMemory(0x663BCC, Add, -48627712),# units:Piss Sound Start  index:75    from 742 To 0
        SetMemory(0x663BD0, Add, -569),# units:Piss Sound Start  index:76    from 569 To 0
        SetMemory(0x663BD0, Add, -45285376),# units:Piss Sound Start  index:77    from 691 To 0
        SetMemory(0x663BD4, Add, -679),# units:Piss Sound Start  index:78    from 679 To 0
        SetMemory(0x663BD4, Add, -46858240),# units:Piss Sound Start  index:79    from 715 To 0
        SetMemory(0x663BD8, Add, -535),# units:Piss Sound Start  index:80    from 535 To 0
        SetMemory(0x663BE4, Add, -554),# units:Piss Sound Start  index:86    from 554 To 0
        SetMemory(0x663BE8, Add, -1130),# units:Piss Sound Start  index:88    from 1130 To 0
        SetMemory(0x663BFC, Add, -64225280),# units:Piss Sound Start  index:99    from 980 To 0
        SetMemory(0x663C00, Add, -226),# units:Piss Sound Start  index:100    from 226 To 0
        SetMemory(0x663C04, Add, -444),# units:Piss Sound Start  index:102    from 444 To 0
        SetMemory(0x663C04, Add, -70844416),# units:Piss Sound Start  index:103    from 1081 To 0
        SetMemory(0x663C08, Add, -1112),# units:Piss Sound Start  index:104    from 1112 To 0
        SetMemory(0x661EE8, Add, -286),# units:Piss Sound End  index:0    from 286 To 0
        SetMemory(0x661EE8, Add, -15007744),# units:Piss Sound End  index:1    from 229 To 0
        SetMemory(0x661EEC, Add, -359),# units:Piss Sound End  index:2    from 359 To 0
        SetMemory(0x661EEC, Add, -16187392),# units:Piss Sound End  index:3    from 247 To 0
        SetMemory(0x661EF0, Add, -21168128),# units:Piss Sound End  index:5    from 323 To 0
        SetMemory(0x661EF8, Add, -264),# units:Piss Sound End  index:8    from 264 To 0
        SetMemory(0x661EFC, Add, -309),# units:Piss Sound End  index:10    from 309 To 0
        SetMemory(0x661EFC, Add, -14024704),# units:Piss Sound End  index:11    from 214 To 0
        SetMemory(0x661F00, Add, -184),# units:Piss Sound End  index:12    from 184 To 0
        SetMemory(0x661F08, Add, -461),# units:Piss Sound End  index:16    from 461 To 0
        SetMemory(0x661F08, Add, -16187392),# units:Piss Sound End  index:17    from 247 To 0
        SetMemory(0x661F0C, Add, -27656192),# units:Piss Sound End  index:19    from 422 To 0
        SetMemory(0x661F10, Add, -410),# units:Piss Sound End  index:20    from 410 To 0
        SetMemory(0x661F10, Add, -17301504),# units:Piss Sound End  index:21    from 264 To 0
        SetMemory(0x661F14, Add, -28508160),# units:Piss Sound End  index:23    from 435 To 0
        SetMemory(0x661F1C, Add, -29360128),# units:Piss Sound End  index:27    from 448 To 0
        SetMemory(0x661F20, Add, -410),# units:Piss Sound End  index:28    from 410 To 0
        SetMemory(0x661F20, Add, -29360128),# units:Piss Sound End  index:29    from 448 To 0
        SetMemory(0x661F28, Add, -309),# units:Piss Sound End  index:32    from 309 To 0
        SetMemory(0x661F30, Add, -58916864),# units:Piss Sound End  index:37    from 899 To 0
        SetMemory(0x661F34, Add, -869),# units:Piss Sound End  index:38    from 869 To 0
        SetMemory(0x661F34, Add, -57737216),# units:Piss Sound End  index:39    from 881 To 0
        SetMemory(0x661F38, Add, -791),# units:Piss Sound End  index:40    from 791 To 0
        SetMemory(0x661F3C, Add, -61997056),# units:Piss Sound End  index:43    from 946 To 0
        SetMemory(0x661F40, Add, -856),# units:Piss Sound End  index:44    from 856 To 0
        SetMemory(0x661F44, Add, -820),# units:Piss Sound End  index:46    from 820 To 0
        SetMemory(0x661F48, Add, -881),# units:Piss Sound End  index:48    from 881 To 0
        SetMemory(0x661F4C, Add, -62783488),# units:Piss Sound End  index:51    from 958 To 0
        SetMemory(0x661F50, Add, -820),# units:Piss Sound End  index:52    from 820 To 0
        SetMemory(0x661F50, Add, -56950784),# units:Piss Sound End  index:53    from 869 To 0
        SetMemory(0x661F54, Add, -899),# units:Piss Sound End  index:54    from 899 To 0
        SetMemory(0x661F54, Add, -61997056),# units:Piss Sound End  index:55    from 946 To 0
        SetMemory(0x661F58, Add, -856),# units:Piss Sound End  index:56    from 856 To 0
        SetMemory(0x661F60, Add, -47972352),# units:Piss Sound End  index:61    from 732 To 0
        SetMemory(0x661F64, Add, -70123520),# units:Piss Sound End  index:63    from 1070 To 0
        SetMemory(0x661F68, Add, -43843584),# units:Piss Sound End  index:65    from 669 To 0
        SetMemory(0x661F6C, Add, -497),# units:Piss Sound End  index:66    from 497 To 0
        SetMemory(0x661F6C, Add, -41025536),# units:Piss Sound End  index:67    from 626 To 0
        SetMemory(0x661F70, Add, -572),# units:Piss Sound End  index:68    from 572 To 0
        SetMemory(0x661F70, Add, -34013184),# units:Piss Sound End  index:69    from 519 To 0
        SetMemory(0x661F74, Add, -539),# units:Piss Sound End  index:70    from 539 To 0
        SetMemory(0x661F74, Add, -36569088),# units:Piss Sound End  index:71    from 558 To 0
        SetMemory(0x661F7C, Add, -732),# units:Piss Sound End  index:74    from 732 To 0
        SetMemory(0x661F7C, Add, -48824320),# units:Piss Sound End  index:75    from 745 To 0
        SetMemory(0x661F80, Add, -572),# units:Piss Sound End  index:76    from 572 To 0
        SetMemory(0x661F80, Add, -45481984),# units:Piss Sound End  index:77    from 694 To 0
        SetMemory(0x661F84, Add, -682),# units:Piss Sound End  index:78    from 682 To 0
        SetMemory(0x661F84, Add, -47054848),# units:Piss Sound End  index:79    from 718 To 0
        SetMemory(0x661F88, Add, -539),# units:Piss Sound End  index:80    from 539 To 0
        SetMemory(0x661F94, Add, -558),# units:Piss Sound End  index:86    from 558 To 0
        SetMemory(0x661F98, Add, -1135),# units:Piss Sound End  index:88    from 1135 To 0
        SetMemory(0x661FAC, Add, -64749568),# units:Piss Sound End  index:99    from 988 To 0
        SetMemory(0x661FB0, Add, -229),# units:Piss Sound End  index:100    from 229 To 0
        SetMemory(0x661FB4, Add, -448),# units:Piss Sound End  index:102    from 448 To 0
        SetMemory(0x661FB4, Add, -71041024),# units:Piss Sound End  index:103    from 1084 To 0
        SetMemory(0x661FB8, Add, -1120),# units:Piss Sound End  index:104    from 1120 To 0
        SetMemory(0x663C10, Add, -291),# units:Yes Sound Start  index:0    from 291 To 0
        SetMemory(0x663C10, Add, -15335424),# units:Yes Sound Start  index:1    from 234 To 0
        SetMemory(0x663C14, Add, -364),# units:Yes Sound Start  index:2    from 364 To 0
        SetMemory(0x663C14, Add, -16515072),# units:Yes Sound Start  index:3    from 252 To 0
        SetMemory(0x663C18, Add, -21495808),# units:Yes Sound Start  index:5    from 328 To 0
        SetMemory(0x663C20, Add, -269),# units:Yes Sound Start  index:8    from 269 To 0
        SetMemory(0x663C24, Add, -310),# units:Yes Sound Start  index:10    from 310 To 0
        SetMemory(0x663C24, Add, -14352384),# units:Yes Sound Start  index:11    from 219 To 0
        SetMemory(0x663C28, Add, -189),# units:Yes Sound Start  index:12    from 189 To 0
        SetMemory(0x663C30, Add, -466),# units:Yes Sound Start  index:16    from 466 To 0
        SetMemory(0x663C30, Add, -16515072),# units:Yes Sound Start  index:17    from 252 To 0
        SetMemory(0x663C34, Add, -27983872),# units:Yes Sound Start  index:19    from 427 To 0
        SetMemory(0x663C38, Add, -415),# units:Yes Sound Start  index:20    from 415 To 0
        SetMemory(0x663C38, Add, -17629184),# units:Yes Sound Start  index:21    from 269 To 0
        SetMemory(0x663C3C, Add, -28835840),# units:Yes Sound Start  index:23    from 440 To 0
        SetMemory(0x663C44, Add, -29687808),# units:Yes Sound Start  index:27    from 453 To 0
        SetMemory(0x663C48, Add, -415),# units:Yes Sound Start  index:28    from 415 To 0
        SetMemory(0x663C48, Add, -29687808),# units:Yes Sound Start  index:29    from 453 To 0
        SetMemory(0x663C50, Add, -310),# units:Yes Sound Start  index:32    from 310 To 0
        SetMemory(0x663C58, Add, -59310080),# units:Yes Sound Start  index:37    from 905 To 0
        SetMemory(0x663C5C, Add, -873),# units:Yes Sound Start  index:38    from 873 To 0
        SetMemory(0x663C5C, Add, -58130432),# units:Yes Sound Start  index:39    from 887 To 0
        SetMemory(0x663C60, Add, -796),# units:Yes Sound Start  index:40    from 796 To 0
        SetMemory(0x663C64, Add, -62324736),# units:Yes Sound Start  index:43    from 951 To 0
        SetMemory(0x663C68, Add, -862),# units:Yes Sound Start  index:44    from 862 To 0
        SetMemory(0x663C6C, Add, -824),# units:Yes Sound Start  index:46    from 824 To 0
        SetMemory(0x663C70, Add, -887),# units:Yes Sound Start  index:48    from 887 To 0
        SetMemory(0x663C74, Add, -63111168),# units:Yes Sound Start  index:51    from 963 To 0
        SetMemory(0x663C78, Add, -824),# units:Yes Sound Start  index:52    from 824 To 0
        SetMemory(0x663C78, Add, -57212928),# units:Yes Sound Start  index:53    from 873 To 0
        SetMemory(0x663C7C, Add, -905),# units:Yes Sound Start  index:54    from 905 To 0
        SetMemory(0x663C7C, Add, -62324736),# units:Yes Sound Start  index:55    from 951 To 0
        SetMemory(0x663C80, Add, -862),# units:Yes Sound Start  index:56    from 862 To 0
        SetMemory(0x663C88, Add, -48300032),# units:Yes Sound Start  index:61    from 737 To 0
        SetMemory(0x663C8C, Add, -70451200),# units:Yes Sound Start  index:63    from 1075 To 0
        SetMemory(0x663C90, Add, -44171264),# units:Yes Sound Start  index:65    from 674 To 0
        SetMemory(0x663C94, Add, -506),# units:Yes Sound Start  index:66    from 506 To 0
        SetMemory(0x663C94, Add, -41353216),# units:Yes Sound Start  index:67    from 631 To 0
        SetMemory(0x663C98, Add, -577),# units:Yes Sound Start  index:68    from 577 To 0
        SetMemory(0x663C98, Add, -34340864),# units:Yes Sound Start  index:69    from 524 To 0
        SetMemory(0x663C9C, Add, -544),# units:Yes Sound Start  index:70    from 544 To 0
        SetMemory(0x663C9C, Add, -36896768),# units:Yes Sound Start  index:71    from 563 To 0
        SetMemory(0x663CA4, Add, -737),# units:Yes Sound Start  index:74    from 737 To 0
        SetMemory(0x663CA4, Add, -49152000),# units:Yes Sound Start  index:75    from 750 To 0
        SetMemory(0x663CA8, Add, -577),# units:Yes Sound Start  index:76    from 577 To 0
        SetMemory(0x663CA8, Add, -45809664),# units:Yes Sound Start  index:77    from 699 To 0
        SetMemory(0x663CAC, Add, -687),# units:Yes Sound Start  index:78    from 687 To 0
        SetMemory(0x663CAC, Add, -47382528),# units:Yes Sound Start  index:79    from 723 To 0
        SetMemory(0x663CB0, Add, -544),# units:Yes Sound Start  index:80    from 544 To 0
        SetMemory(0x663CBC, Add, -563),# units:Yes Sound Start  index:86    from 563 To 0
        SetMemory(0x663CC0, Add, -1140),# units:Yes Sound Start  index:88    from 1140 To 0
        SetMemory(0x663CD4, Add, -65077248),# units:Yes Sound Start  index:99    from 993 To 0
        SetMemory(0x663CD8, Add, -234),# units:Yes Sound Start  index:100    from 234 To 0
        SetMemory(0x663CDC, Add, -453),# units:Yes Sound Start  index:102    from 453 To 0
        SetMemory(0x663CDC, Add, -71368704),# units:Yes Sound Start  index:103    from 1089 To 0
        SetMemory(0x663CE0, Add, -1125),# units:Yes Sound Start  index:104    from 1125 To 0
        SetMemory(0x661440, Add, -294),# units:Yes Sound End  index:0    from 294 To 0
        SetMemory(0x661440, Add, -15532032),# units:Yes Sound End  index:1    from 237 To 0
        SetMemory(0x661444, Add, -367),# units:Yes Sound End  index:2    from 367 To 0
        SetMemory(0x661444, Add, -16711680),# units:Yes Sound End  index:3    from 255 To 0
        SetMemory(0x661448, Add, -21692416),# units:Yes Sound End  index:5    from 331 To 0
        SetMemory(0x661450, Add, -272),# units:Yes Sound End  index:8    from 272 To 0
        SetMemory(0x661454, Add, -313),# units:Yes Sound End  index:10    from 313 To 0
        SetMemory(0x661454, Add, -14680064),# units:Yes Sound End  index:11    from 224 To 0
        SetMemory(0x661458, Add, -192),# units:Yes Sound End  index:12    from 192 To 0
        SetMemory(0x661460, Add, -469),# units:Yes Sound End  index:16    from 469 To 0
        SetMemory(0x661460, Add, -16711680),# units:Yes Sound End  index:17    from 255 To 0
        SetMemory(0x661464, Add, -28180480),# units:Yes Sound End  index:19    from 430 To 0
        SetMemory(0x661468, Add, -418),# units:Yes Sound End  index:20    from 418 To 0
        SetMemory(0x661468, Add, -17825792),# units:Yes Sound End  index:21    from 272 To 0
        SetMemory(0x66146C, Add, -29032448),# units:Yes Sound End  index:23    from 443 To 0
        SetMemory(0x661474, Add, -29884416),# units:Yes Sound End  index:27    from 456 To 0
        SetMemory(0x661478, Add, -418),# units:Yes Sound End  index:28    from 418 To 0
        SetMemory(0x661478, Add, -29884416),# units:Yes Sound End  index:29    from 456 To 0
        SetMemory(0x661480, Add, -313),# units:Yes Sound End  index:32    from 313 To 0
        SetMemory(0x661488, Add, -59506688),# units:Yes Sound End  index:37    from 908 To 0
        SetMemory(0x66148C, Add, -876),# units:Yes Sound End  index:38    from 876 To 0
        SetMemory(0x66148C, Add, -58327040),# units:Yes Sound End  index:39    from 890 To 0
        SetMemory(0x661490, Add, -799),# units:Yes Sound End  index:40    from 799 To 0
        SetMemory(0x661494, Add, -62521344),# units:Yes Sound End  index:43    from 954 To 0
        SetMemory(0x661498, Add, -865),# units:Yes Sound End  index:44    from 865 To 0
        SetMemory(0x66149C, Add, -826),# units:Yes Sound End  index:46    from 826 To 0
        SetMemory(0x6614A0, Add, -890),# units:Yes Sound End  index:48    from 890 To 0
        SetMemory(0x6614A4, Add, -63307776),# units:Yes Sound End  index:51    from 966 To 0
        SetMemory(0x6614A8, Add, -826),# units:Yes Sound End  index:52    from 826 To 0
        SetMemory(0x6614A8, Add, -57409536),# units:Yes Sound End  index:53    from 876 To 0
        SetMemory(0x6614AC, Add, -908),# units:Yes Sound End  index:54    from 908 To 0
        SetMemory(0x6614AC, Add, -62521344),# units:Yes Sound End  index:55    from 954 To 0
        SetMemory(0x6614B0, Add, -865),# units:Yes Sound End  index:56    from 865 To 0
        SetMemory(0x6614B8, Add, -48496640),# units:Yes Sound End  index:61    from 740 To 0
        SetMemory(0x6614BC, Add, -70647808),# units:Yes Sound End  index:63    from 1078 To 0
        SetMemory(0x6614C0, Add, -44367872),# units:Yes Sound End  index:65    from 677 To 0
        SetMemory(0x6614C4, Add, -512),# units:Yes Sound End  index:66    from 512 To 0
        SetMemory(0x6614C4, Add, -41549824),# units:Yes Sound End  index:67    from 634 To 0
        SetMemory(0x6614C8, Add, -580),# units:Yes Sound End  index:68    from 580 To 0
        SetMemory(0x6614C8, Add, -34537472),# units:Yes Sound End  index:69    from 527 To 0
        SetMemory(0x6614CC, Add, -547),# units:Yes Sound End  index:70    from 547 To 0
        SetMemory(0x6614CC, Add, -37027840),# units:Yes Sound End  index:71    from 565 To 0
        SetMemory(0x6614D4, Add, -740),# units:Yes Sound End  index:74    from 740 To 0
        SetMemory(0x6614D4, Add, -49348608),# units:Yes Sound End  index:75    from 753 To 0
        SetMemory(0x6614D8, Add, -580),# units:Yes Sound End  index:76    from 580 To 0
        SetMemory(0x6614D8, Add, -46006272),# units:Yes Sound End  index:77    from 702 To 0
        SetMemory(0x6614DC, Add, -690),# units:Yes Sound End  index:78    from 690 To 0
        SetMemory(0x6614DC, Add, -47579136),# units:Yes Sound End  index:79    from 726 To 0
        SetMemory(0x6614E0, Add, -547),# units:Yes Sound End  index:80    from 547 To 0
        SetMemory(0x6614EC, Add, -565),# units:Yes Sound End  index:86    from 565 To 0
        SetMemory(0x6614F0, Add, -1143),# units:Yes Sound End  index:88    from 1143 To 0
        SetMemory(0x661504, Add, -65273856),# units:Yes Sound End  index:99    from 996 To 0
        SetMemory(0x661508, Add, -237),# units:Yes Sound End  index:100    from 237 To 0
        SetMemory(0x66150C, Add, -456),# units:Yes Sound End  index:102    from 456 To 0
        SetMemory(0x66150C, Add, -71565312),# units:Yes Sound End  index:103    from 1092 To 0
        SetMemory(0x661510, Add, -1128),# units:Yes Sound End  index:104    from 1128 To 0
        SetMemory(0x662860, Add, -8),# units:StarEdit Placement Box Width  index:0    from 17 To 9
        SetMemory(0x662864, Add, -6),# units:StarEdit Placement Box Width  index:1    from 15 To 9
        SetMemory(0x662868, Add, -23),# units:StarEdit Placement Box Width  index:2    from 32 To 9
        SetMemory(0x66286C, Add, -23),# units:StarEdit Placement Box Width  index:3    from 32 To 9
        SetMemory(0x662874, Add, -23),# units:StarEdit Placement Box Width  index:5    from 32 To 9
        SetMemory(0x662880, Add, -29),# units:StarEdit Placement Box Width  index:8    from 38 To 9
        SetMemory(0x662888, Add, -14),# units:StarEdit Placement Box Width  index:10    from 23 To 9
        SetMemory(0x66288C, Add, -40),# units:StarEdit Placement Box Width  index:11    from 49 To 9
        SetMemory(0x662890, Add, -71),# units:StarEdit Placement Box Width  index:12    from 80 To 9
        SetMemory(0x6628A0, Add, -6),# units:StarEdit Placement Box Width  index:16    from 15 To 9
        SetMemory(0x6628A4, Add, -23),# units:StarEdit Placement Box Width  index:17    from 32 To 9
        SetMemory(0x6628AC, Add, -23),# units:StarEdit Placement Box Width  index:19    from 32 To 9
        SetMemory(0x6628B0, Add, -9),# units:StarEdit Placement Box Width  index:20    from 18 To 9
        SetMemory(0x6628B4, Add, -29),# units:StarEdit Placement Box Width  index:21    from 38 To 9
        SetMemory(0x6628BC, Add, -23),# units:StarEdit Placement Box Width  index:23    from 32 To 9
        SetMemory(0x6628CC, Add, -66),# units:StarEdit Placement Box Width  index:27    from 75 To 9
        SetMemory(0x6628D0, Add, -66),# units:StarEdit Placement Box Width  index:28    from 75 To 9
        SetMemory(0x6628D4, Add, -66),# units:StarEdit Placement Box Width  index:29    from 75 To 9
        SetMemory(0x6628E0, Add, -14),# units:StarEdit Placement Box Width  index:32    from 23 To 9
        SetMemory(0x6628F4, Add, -7),# units:StarEdit Placement Box Width  index:37    from 16 To 9
        SetMemory(0x6628F8, Add, -12),# units:StarEdit Placement Box Width  index:38    from 21 To 9
        SetMemory(0x6628FC, Add, -29),# units:StarEdit Placement Box Width  index:39    from 38 To 9
        SetMemory(0x662900, Add, -10),# units:StarEdit Placement Box Width  index:40    from 19 To 9
        SetMemory(0x66290C, Add, -35),# units:StarEdit Placement Box Width  index:43    from 44 To 9
        SetMemory(0x662910, Add, -35),# units:StarEdit Placement Box Width  index:44    from 44 To 9
        SetMemory(0x662918, Add, -18),# units:StarEdit Placement Box Width  index:46    from 27 To 9
        SetMemory(0x662920, Add, -29),# units:StarEdit Placement Box Width  index:48    from 38 To 9
        SetMemory(0x66292C, Add, -6),# units:StarEdit Placement Box Width  index:51    from 15 To 9
        SetMemory(0x662930, Add, -20),# units:StarEdit Placement Box Width  index:52    from 29 To 9
        SetMemory(0x662934, Add, -12),# units:StarEdit Placement Box Width  index:53    from 21 To 9
        SetMemory(0x662938, Add, -7),# units:StarEdit Placement Box Width  index:54    from 16 To 9
        SetMemory(0x66293C, Add, -35),# units:StarEdit Placement Box Width  index:55    from 44 To 9
        SetMemory(0x662940, Add, -35),# units:StarEdit Placement Box Width  index:56    from 44 To 9
        SetMemory(0x662954, Add, -15),# units:StarEdit Placement Box Width  index:61    from 24 To 9
        SetMemory(0x66295C, Add, -23),# units:StarEdit Placement Box Width  index:63    from 32 To 9
        SetMemory(0x662964, Add, -14),# units:StarEdit Placement Box Width  index:65    from 23 To 9
        SetMemory(0x662968, Add, -15),# units:StarEdit Placement Box Width  index:66    from 32 To 17
        SetMemory(0x66296C, Add, -15),# units:StarEdit Placement Box Width  index:67    from 24 To 9
        SetMemory(0x662970, Add, -23),# units:StarEdit Placement Box Width  index:68    from 32 To 9
        SetMemory(0x662974, Add, -31),# units:StarEdit Placement Box Width  index:69    from 40 To 9
        SetMemory(0x662978, Add, -27),# units:StarEdit Placement Box Width  index:70    from 36 To 9
        SetMemory(0x66297C, Add, -35),# units:StarEdit Placement Box Width  index:71    from 44 To 9
        SetMemory(0x662988, Add, -15),# units:StarEdit Placement Box Width  index:74    from 24 To 9
        SetMemory(0x66298C, Add, -15),# units:StarEdit Placement Box Width  index:75    from 24 To 9
        SetMemory(0x662990, Add, -23),# units:StarEdit Placement Box Width  index:76    from 32 To 9
        SetMemory(0x662994, Add, -15),# units:StarEdit Placement Box Width  index:77    from 24 To 9
        SetMemory(0x662998, Add, -23),# units:StarEdit Placement Box Width  index:78    from 32 To 9
        SetMemory(0x66299C, Add, -15),# units:StarEdit Placement Box Width  index:79    from 24 To 9
        SetMemory(0x6629A0, Add, -27),# units:StarEdit Placement Box Width  index:80    from 36 To 9
        SetMemory(0x6629B8, Add, -35),# units:StarEdit Placement Box Width  index:86    from 44 To 9
        SetMemory(0x6629BC, Add, -15),# units:StarEdit Placement Box Width  index:87    from 24 To 9
        SetMemory(0x6629C0, Add, -27),# units:StarEdit Placement Box Width  index:88    from 36 To 9
        SetMemory(0x6629D4, Add, -23),# units:StarEdit Placement Box Width  index:93    from 32 To 9
        SetMemory(0x6629D8, Add, -23),# units:StarEdit Placement Box Width  index:94    from 32 To 9
        SetMemory(0x6629DC, Add, -23),# units:StarEdit Placement Box Width  index:95    from 32 To 9
        SetMemory(0x6629E0, Add, -23),# units:StarEdit Placement Box Width  index:96    from 32 To 9
        SetMemory(0x6629EC, Add, -6),# units:StarEdit Placement Box Width  index:99    from 15 To 9
        SetMemory(0x6629F0, Add, -6),# units:StarEdit Placement Box Width  index:100    from 15 To 9
        SetMemory(0x6629F8, Add, -66),# units:StarEdit Placement Box Width  index:102    from 75 To 9
        SetMemory(0x6629FC, Add, -23),# units:StarEdit Placement Box Width  index:103    from 32 To 9
        SetMemory(0x662A00, Add, -6),# units:StarEdit Placement Box Width  index:104    from 15 To 9
        SetMemory(0x662A1C, Add, -119),# units:StarEdit Placement Box Width  index:111    from 128 To 9
        SetMemory(0x662A74, Add, -119),# units:StarEdit Placement Box Width  index:133    from 128 To 9
        SetMemory(0x662A7C, Add, -87),# units:StarEdit Placement Box Width  index:135    from 96 To 9
        SetMemory(0x662A80, Add, -121),# units:StarEdit Placement Box Width  index:136    from 128 To 7
        SetMemory(0x662A84, Add, -57),# units:StarEdit Placement Box Width  index:137    from 64 To 7
        SetMemory(0x662A88, Add, -89),# units:StarEdit Placement Box Width  index:138    from 96 To 7
        SetMemory(0x662A8C, Add, -89),# units:StarEdit Placement Box Width  index:139    from 96 To 7
        SetMemory(0x662A90, Add, -89),# units:StarEdit Placement Box Width  index:140    from 96 To 7
        SetMemory(0x662A98, Add, -89),# units:StarEdit Placement Box Width  index:142    from 96 To 7
        SetMemory(0x662AAC, Add, -153),# units:StarEdit Placement Box Width  index:147    from 160 To 7
        SetMemory(0x662AB0, Add, -153),# units:StarEdit Placement Box Width  index:148    from 160 To 7
        SetMemory(0x662ABC, Add, -89),# units:StarEdit Placement Box Width  index:151    from 96 To 7
        SetMemory(0x662AC0, Add, -89),# units:StarEdit Placement Box Width  index:152    from 96 To 7
        SetMemory(0x662AC8, Add, -121),# units:StarEdit Placement Box Width  index:154    from 128 To 7
        SetMemory(0x662ADC, Add, -89),# units:StarEdit Placement Box Width  index:159    from 96 To 7
        SetMemory(0x662AE0, Add, -121),# units:StarEdit Placement Box Width  index:160    from 128 To 7
        SetMemory(0x662AEC, Add, -89),# units:StarEdit Placement Box Width  index:163    from 96 To 7
        SetMemory(0x662AF0, Add, -89),# units:StarEdit Placement Box Width  index:164    from 96 To 7
        SetMemory(0x662AF4, Add, -89),# units:StarEdit Placement Box Width  index:165    from 96 To 7
        SetMemory(0x662AF8, Add, -89),# units:StarEdit Placement Box Width  index:166    from 96 To 7
        SetMemory(0x662AFC, Add, -121),# units:StarEdit Placement Box Width  index:167    from 128 To 7
        SetMemory(0x662B00, Add, -121),# units:StarEdit Placement Box Width  index:168    from 128 To 7
        SetMemory(0x662B04, Add, -89),# units:StarEdit Placement Box Width  index:169    from 96 To 7
        SetMemory(0x662B08, Add, -89),# units:StarEdit Placement Box Width  index:170    from 96 To 7
        SetMemory(0x662B0C, Add, -89),# units:StarEdit Placement Box Width  index:171    from 96 To 7
        SetMemory(0x662B10, Add, -89),# units:StarEdit Placement Box Width  index:172    from 96 To 7
        SetMemory(0x662B14, Add, -121),# units:StarEdit Placement Box Width  index:173    from 128 To 7
        SetMemory(0x662B18, Add, -217),# units:StarEdit Placement Box Width  index:174    from 224 To 7
        SetMemory(0x662B1C, Add, -153),# units:StarEdit Placement Box Width  index:175    from 160 To 7
        SetMemory(0x662B70, Add, -63),# units:StarEdit Placement Box Width  index:196    from 96 To 33
        SetMemory(0x662860, Add, -720896),# units:StarEdit Placement Box Height  index:0    from 20 To 9
        SetMemory(0x662864, Add, -851968),# units:StarEdit Placement Box Height  index:1    from 22 To 9
        SetMemory(0x662868, Add, -1507328),# units:StarEdit Placement Box Height  index:2    from 32 To 9
        SetMemory(0x66286C, Add, -1507328),# units:StarEdit Placement Box Height  index:3    from 32 To 9
        SetMemory(0x662874, Add, -1507328),# units:StarEdit Placement Box Height  index:5    from 32 To 9
        SetMemory(0x662880, Add, -1376256),# units:StarEdit Placement Box Height  index:8    from 30 To 9
        SetMemory(0x662888, Add, -1245184),# units:StarEdit Placement Box Height  index:10    from 28 To 9
        SetMemory(0x66288C, Add, -1835008),# units:StarEdit Placement Box Height  index:11    from 37 To 9
        SetMemory(0x662890, Add, -3604480),# units:StarEdit Placement Box Height  index:12    from 64 To 9
        SetMemory(0x6628A0, Add, -851968),# units:StarEdit Placement Box Height  index:16    from 22 To 9
        SetMemory(0x6628A4, Add, -1507328),# units:StarEdit Placement Box Height  index:17    from 32 To 9
        SetMemory(0x6628AC, Add, -1507328),# units:StarEdit Placement Box Height  index:19    from 32 To 9
        SetMemory(0x6628B0, Add, -851968),# units:StarEdit Placement Box Height  index:20    from 22 To 9
        SetMemory(0x6628B4, Add, -1376256),# units:StarEdit Placement Box Height  index:21    from 30 To 9
        SetMemory(0x6628BC, Add, -1507328),# units:StarEdit Placement Box Height  index:23    from 32 To 9
        SetMemory(0x6628CC, Add, -3276800),# units:StarEdit Placement Box Height  index:27    from 59 To 9
        SetMemory(0x6628D0, Add, -3276800),# units:StarEdit Placement Box Height  index:28    from 59 To 9
        SetMemory(0x6628D4, Add, -3276800),# units:StarEdit Placement Box Height  index:29    from 59 To 9
        SetMemory(0x6628E0, Add, -1245184),# units:StarEdit Placement Box Height  index:32    from 28 To 9
        SetMemory(0x6628F4, Add, -458752),# units:StarEdit Placement Box Height  index:37    from 16 To 9
        SetMemory(0x6628F8, Add, -917504),# units:StarEdit Placement Box Height  index:38    from 23 To 9
        SetMemory(0x6628FC, Add, -1507328),# units:StarEdit Placement Box Height  index:39    from 32 To 9
        SetMemory(0x662900, Add, -655360),# units:StarEdit Placement Box Height  index:40    from 19 To 9
        SetMemory(0x66290C, Add, -2293760),# units:StarEdit Placement Box Height  index:43    from 44 To 9
        SetMemory(0x662910, Add, -2293760),# units:StarEdit Placement Box Height  index:44    from 44 To 9
        SetMemory(0x662918, Add, -1048576),# units:StarEdit Placement Box Height  index:46    from 25 To 9
        SetMemory(0x662920, Add, -1507328),# units:StarEdit Placement Box Height  index:48    from 32 To 9
        SetMemory(0x66292C, Add, -851968),# units:StarEdit Placement Box Height  index:51    from 22 To 9
        SetMemory(0x662930, Add, -1310720),# units:StarEdit Placement Box Height  index:52    from 29 To 9
        SetMemory(0x662934, Add, -917504),# units:StarEdit Placement Box Height  index:53    from 23 To 9
        SetMemory(0x662938, Add, -458752),# units:StarEdit Placement Box Height  index:54    from 16 To 9
        SetMemory(0x66293C, Add, -2293760),# units:StarEdit Placement Box Height  index:55    from 44 To 9
        SetMemory(0x662940, Add, -2293760),# units:StarEdit Placement Box Height  index:56    from 44 To 9
        SetMemory(0x662954, Add, -1376256),# units:StarEdit Placement Box Height  index:61    from 30 To 9
        SetMemory(0x66295C, Add, -1507328),# units:StarEdit Placement Box Height  index:63    from 32 To 9
        SetMemory(0x662964, Add, -1179648),# units:StarEdit Placement Box Height  index:65    from 27 To 9
        SetMemory(0x662968, Add, -983040),# units:StarEdit Placement Box Height  index:66    from 32 To 17
        SetMemory(0x66296C, Add, -1245184),# units:StarEdit Placement Box Height  index:67    from 28 To 9
        SetMemory(0x662970, Add, -1507328),# units:StarEdit Placement Box Height  index:68    from 32 To 9
        SetMemory(0x662974, Add, -1507328),# units:StarEdit Placement Box Height  index:69    from 32 To 9
        SetMemory(0x662978, Add, -1507328),# units:StarEdit Placement Box Height  index:70    from 32 To 9
        SetMemory(0x66297C, Add, -2293760),# units:StarEdit Placement Box Height  index:71    from 44 To 9
        SetMemory(0x662988, Add, -1376256),# units:StarEdit Placement Box Height  index:74    from 30 To 9
        SetMemory(0x66298C, Add, -1376256),# units:StarEdit Placement Box Height  index:75    from 30 To 9
        SetMemory(0x662990, Add, -1507328),# units:StarEdit Placement Box Height  index:76    from 32 To 9
        SetMemory(0x662994, Add, -1376256),# units:StarEdit Placement Box Height  index:77    from 30 To 9
        SetMemory(0x662998, Add, -1507328),# units:StarEdit Placement Box Height  index:78    from 32 To 9
        SetMemory(0x66299C, Add, -1245184),# units:StarEdit Placement Box Height  index:79    from 28 To 9
        SetMemory(0x6629A0, Add, -1507328),# units:StarEdit Placement Box Height  index:80    from 32 To 9
        SetMemory(0x6629B8, Add, -2293760),# units:StarEdit Placement Box Height  index:86    from 44 To 9
        SetMemory(0x6629BC, Add, -1245184),# units:StarEdit Placement Box Height  index:87    from 28 To 9
        SetMemory(0x6629C0, Add, -1507328),# units:StarEdit Placement Box Height  index:88    from 32 To 9
        SetMemory(0x6629D4, Add, -1507328),# units:StarEdit Placement Box Height  index:93    from 32 To 9
        SetMemory(0x6629D8, Add, -1507328),# units:StarEdit Placement Box Height  index:94    from 32 To 9
        SetMemory(0x6629DC, Add, -1507328),# units:StarEdit Placement Box Height  index:95    from 32 To 9
        SetMemory(0x6629E0, Add, -1507328),# units:StarEdit Placement Box Height  index:96    from 32 To 9
        SetMemory(0x6629EC, Add, -851968),# units:StarEdit Placement Box Height  index:99    from 22 To 9
        SetMemory(0x6629F0, Add, -851968),# units:StarEdit Placement Box Height  index:100    from 22 To 9
        SetMemory(0x6629F8, Add, -3276800),# units:StarEdit Placement Box Height  index:102    from 59 To 9
        SetMemory(0x6629FC, Add, -1507328),# units:StarEdit Placement Box Height  index:103    from 32 To 9
        SetMemory(0x662A00, Add, -851968),# units:StarEdit Placement Box Height  index:104    from 22 To 9
        SetMemory(0x662A1C, Add, -5701632),# units:StarEdit Placement Box Height  index:111    from 96 To 9
        SetMemory(0x662A74, Add, -5701632),# units:StarEdit Placement Box Height  index:133    from 96 To 9
        SetMemory(0x662A7C, Add, -3604480),# units:StarEdit Placement Box Height  index:135    from 64 To 9
        SetMemory(0x662A80, Add, -3735552),# units:StarEdit Placement Box Height  index:136    from 64 To 7
        SetMemory(0x662A84, Add, -3735552),# units:StarEdit Placement Box Height  index:137    from 64 To 7
        SetMemory(0x662A88, Add, -3735552),# units:StarEdit Placement Box Height  index:138    from 64 To 7
        SetMemory(0x662A8C, Add, -3735552),# units:StarEdit Placement Box Height  index:139    from 64 To 7
        SetMemory(0x662A90, Add, -3735552),# units:StarEdit Placement Box Height  index:140    from 64 To 7
        SetMemory(0x662A98, Add, -3735552),# units:StarEdit Placement Box Height  index:142    from 64 To 7
        SetMemory(0x662AAC, Add, -5832704),# units:StarEdit Placement Box Height  index:147    from 96 To 7
        SetMemory(0x662AB0, Add, -5832704),# units:StarEdit Placement Box Height  index:148    from 96 To 7
        SetMemory(0x662ABC, Add, -3735552),# units:StarEdit Placement Box Height  index:151    from 64 To 7
        SetMemory(0x662AC0, Add, -3735552),# units:StarEdit Placement Box Height  index:152    from 64 To 7
        SetMemory(0x662AC8, Add, -5832704),# units:StarEdit Placement Box Height  index:154    from 96 To 7
        SetMemory(0x662ADC, Add, -3735552),# units:StarEdit Placement Box Height  index:159    from 64 To 7
        SetMemory(0x662AE0, Add, -5832704),# units:StarEdit Placement Box Height  index:160    from 96 To 7
        SetMemory(0x662AEC, Add, -3735552),# units:StarEdit Placement Box Height  index:163    from 64 To 7
        SetMemory(0x662AF0, Add, -3735552),# units:StarEdit Placement Box Height  index:164    from 64 To 7
        SetMemory(0x662AF4, Add, -3735552),# units:StarEdit Placement Box Height  index:165    from 64 To 7
        SetMemory(0x662AF8, Add, -3735552),# units:StarEdit Placement Box Height  index:166    from 64 To 7
        SetMemory(0x662AFC, Add, -5832704),# units:StarEdit Placement Box Height  index:167    from 96 To 7
        SetMemory(0x662B00, Add, -5832704),# units:StarEdit Placement Box Height  index:168    from 96 To 7
        SetMemory(0x662B04, Add, -3735552),# units:StarEdit Placement Box Height  index:169    from 64 To 7
        SetMemory(0x662B08, Add, -3735552),# units:StarEdit Placement Box Height  index:170    from 64 To 7
        SetMemory(0x662B0C, Add, -3735552),# units:StarEdit Placement Box Height  index:171    from 64 To 7
        SetMemory(0x662B10, Add, -3735552),# units:StarEdit Placement Box Height  index:172    from 64 To 7
        SetMemory(0x662B14, Add, -5832704),# units:StarEdit Placement Box Height  index:173    from 96 To 7
        SetMemory(0x662B18, Add, -5832704),# units:StarEdit Placement Box Height  index:174    from 96 To 7
        SetMemory(0x662B1C, Add, -7929856),# units:StarEdit Placement Box Height  index:175    from 128 To 7
        SetMemory(0x662B70, Add, -2031616),# units:StarEdit Placement Box Height  index:196    from 64 To 33
        SetMemory(0x6617C8, Add, -4),# units:Unit Size Left  index:0    from 8 To 4
        SetMemory(0x6617D0, Add, -3),# units:Unit Size Left  index:1    from 7 To 4
        SetMemory(0x6617D8, Add, -12),# units:Unit Size Left  index:2    from 16 To 4
        SetMemory(0x6617E0, Add, -12),# units:Unit Size Left  index:3    from 16 To 4
        SetMemory(0x6617F0, Add, -12),# units:Unit Size Left  index:5    from 16 To 4
        SetMemory(0x661808, Add, -15),# units:Unit Size Left  index:8    from 19 To 4
        SetMemory(0x661818, Add, -7),# units:Unit Size Left  index:10    from 11 To 4
        SetMemory(0x661820, Add, -20),# units:Unit Size Left  index:11    from 24 To 4
        SetMemory(0x661828, Add, -33),# units:Unit Size Left  index:12    from 37 To 4
        SetMemory(0x661848, Add, -3),# units:Unit Size Left  index:16    from 7 To 4
        SetMemory(0x661850, Add, -12),# units:Unit Size Left  index:17    from 16 To 4
        SetMemory(0x661860, Add, -12),# units:Unit Size Left  index:19    from 16 To 4
        SetMemory(0x661868, Add, -4),# units:Unit Size Left  index:20    from 8 To 4
        SetMemory(0x661870, Add, -15),# units:Unit Size Left  index:21    from 19 To 4
        SetMemory(0x661880, Add, -12),# units:Unit Size Left  index:23    from 16 To 4
        SetMemory(0x6618A0, Add, -33),# units:Unit Size Left  index:27    from 37 To 4
        SetMemory(0x6618A8, Add, -33),# units:Unit Size Left  index:28    from 37 To 4
        SetMemory(0x6618B0, Add, -33),# units:Unit Size Left  index:29    from 37 To 4
        SetMemory(0x6618C8, Add, -7),# units:Unit Size Left  index:32    from 11 To 4
        SetMemory(0x6618F0, Add, -4),# units:Unit Size Left  index:37    from 8 To 4
        SetMemory(0x6618F8, Add, -6),# units:Unit Size Left  index:38    from 10 To 4
        SetMemory(0x661900, Add, -15),# units:Unit Size Left  index:39    from 19 To 4
        SetMemory(0x661908, Add, -5),# units:Unit Size Left  index:40    from 9 To 4
        SetMemory(0x661920, Add, -18),# units:Unit Size Left  index:43    from 22 To 4
        SetMemory(0x661928, Add, -18),# units:Unit Size Left  index:44    from 22 To 4
        SetMemory(0x661938, Add, -9),# units:Unit Size Left  index:46    from 13 To 4
        SetMemory(0x661948, Add, -15),# units:Unit Size Left  index:48    from 19 To 4
        SetMemory(0x661960, Add, -3),# units:Unit Size Left  index:51    from 7 To 4
        SetMemory(0x661968, Add, -10),# units:Unit Size Left  index:52    from 14 To 4
        SetMemory(0x661970, Add, -6),# units:Unit Size Left  index:53    from 10 To 4
        SetMemory(0x661978, Add, -4),# units:Unit Size Left  index:54    from 8 To 4
        SetMemory(0x661980, Add, -18),# units:Unit Size Left  index:55    from 22 To 4
        SetMemory(0x661988, Add, -18),# units:Unit Size Left  index:56    from 22 To 4
        SetMemory(0x6619B0, Add, -8),# units:Unit Size Left  index:61    from 12 To 4
        SetMemory(0x6619C0, Add, -12),# units:Unit Size Left  index:63    from 16 To 4
        SetMemory(0x6619D0, Add, -7),# units:Unit Size Left  index:65    from 11 To 4
        SetMemory(0x6619D8, Add, -7),# units:Unit Size Left  index:66    from 15 To 8
        SetMemory(0x6619E0, Add, -8),# units:Unit Size Left  index:67    from 12 To 4
        SetMemory(0x6619E8, Add, -12),# units:Unit Size Left  index:68    from 16 To 4
        SetMemory(0x6619F0, Add, -16),# units:Unit Size Left  index:69    from 20 To 4
        SetMemory(0x6619F8, Add, -14),# units:Unit Size Left  index:70    from 18 To 4
        SetMemory(0x661A00, Add, -18),# units:Unit Size Left  index:71    from 22 To 4
        SetMemory(0x661A18, Add, -8),# units:Unit Size Left  index:74    from 12 To 4
        SetMemory(0x661A20, Add, -8),# units:Unit Size Left  index:75    from 12 To 4
        SetMemory(0x661A28, Add, -12),# units:Unit Size Left  index:76    from 16 To 4
        SetMemory(0x661A30, Add, -7),# units:Unit Size Left  index:77    from 11 To 4
        SetMemory(0x661A38, Add, -11),# units:Unit Size Left  index:78    from 15 To 4
        SetMemory(0x661A40, Add, -8),# units:Unit Size Left  index:79    from 12 To 4
        SetMemory(0x661A48, Add, -14),# units:Unit Size Left  index:80    from 18 To 4
        SetMemory(0x661A78, Add, -18),# units:Unit Size Left  index:86    from 22 To 4
        SetMemory(0x661A80, Add, -8),# units:Unit Size Left  index:87    from 12 To 4
        SetMemory(0x661A88, Add, -14),# units:Unit Size Left  index:88    from 18 To 4
        SetMemory(0x661AB0, Add, -12),# units:Unit Size Left  index:93    from 16 To 4
        SetMemory(0x661AB8, Add, -12),# units:Unit Size Left  index:94    from 16 To 4
        SetMemory(0x661AC0, Add, -12),# units:Unit Size Left  index:95    from 16 To 4
        SetMemory(0x661AC8, Add, -12),# units:Unit Size Left  index:96    from 16 To 4
        SetMemory(0x661AE0, Add, -3),# units:Unit Size Left  index:99    from 7 To 4
        SetMemory(0x661AE8, Add, -3),# units:Unit Size Left  index:100    from 7 To 4
        SetMemory(0x661AF8, Add, -33),# units:Unit Size Left  index:102    from 37 To 4
        SetMemory(0x661B00, Add, -11),# units:Unit Size Left  index:103    from 15 To 4
        SetMemory(0x661B08, Add, -3),# units:Unit Size Left  index:104    from 7 To 4
        SetMemory(0x661B40, Add, -44),# units:Unit Size Left  index:111    from 48 To 4
        SetMemory(0x661BF0, Add, -45),# units:Unit Size Left  index:133    from 49 To 4
        SetMemory(0x661C00, Add, -36),# units:Unit Size Left  index:135    from 40 To 4
        SetMemory(0x661C08, Add, -45),# units:Unit Size Left  index:136    from 48 To 3
        SetMemory(0x661C10, Add, -25),# units:Unit Size Left  index:137    from 28 To 3
        SetMemory(0x661C18, Add, -35),# units:Unit Size Left  index:138    from 38 To 3
        SetMemory(0x661C20, Add, -41),# units:Unit Size Left  index:139    from 44 To 3
        SetMemory(0x661C28, Add, -37),# units:Unit Size Left  index:140    from 40 To 3
        SetMemory(0x661C38, Add, -33),# units:Unit Size Left  index:142    from 36 To 3
        SetMemory(0x661C60, Add, -77),# units:Unit Size Left  index:147    from 80 To 3
        SetMemory(0x661C68, Add, -77),# units:Unit Size Left  index:148    from 80 To 3
        SetMemory(0x661C80, Add, -37),# units:Unit Size Left  index:151    from 40 To 3
        SetMemory(0x661C88, Add, -37),# units:Unit Size Left  index:152    from 40 To 3
        SetMemory(0x661C98, Add, -53),# units:Unit Size Left  index:154    from 56 To 3
        SetMemory(0x661CC0, Add, -41),# units:Unit Size Left  index:159    from 44 To 3
        SetMemory(0x661CC8, Add, -45),# units:Unit Size Left  index:160    from 48 To 3
        SetMemory(0x661CE0, Add, -21),# units:Unit Size Left  index:163    from 24 To 3
        SetMemory(0x661CE8, Add, -37),# units:Unit Size Left  index:164    from 40 To 3
        SetMemory(0x661CF0, Add, -29),# units:Unit Size Left  index:165    from 32 To 3
        SetMemory(0x661CF8, Add, -33),# units:Unit Size Left  index:166    from 36 To 3
        SetMemory(0x661D00, Add, -45),# units:Unit Size Left  index:167    from 48 To 3
        SetMemory(0x661D08, Add, -61),# units:Unit Size Left  index:168    from 64 To 3
        SetMemory(0x661D10, Add, -37),# units:Unit Size Left  index:169    from 40 To 3
        SetMemory(0x661D18, Add, -41),# units:Unit Size Left  index:170    from 44 To 3
        SetMemory(0x661D20, Add, -29),# units:Unit Size Left  index:171    from 32 To 3
        SetMemory(0x661D28, Add, -29),# units:Unit Size Left  index:172    from 32 To 3
        SetMemory(0x661D30, Add, -61),# units:Unit Size Left  index:173    from 64 To 3
        SetMemory(0x661D38, Add, -109),# units:Unit Size Left  index:174    from 112 To 3
        SetMemory(0x661D40, Add, -77),# units:Unit Size Left  index:175    from 80 To 3
        SetMemory(0x661DE8, Add, -32),# units:Unit Size Left  index:196    from 48 To 16
        SetMemory(0x6617C8, Add, -327680),# units:Unit Size Up  index:0    from 9 To 4
        SetMemory(0x6617D0, Add, -393216),# units:Unit Size Up  index:1    from 10 To 4
        SetMemory(0x6617D8, Add, -786432),# units:Unit Size Up  index:2    from 16 To 4
        SetMemory(0x6617E0, Add, -786432),# units:Unit Size Up  index:3    from 16 To 4
        SetMemory(0x6617F0, Add, -786432),# units:Unit Size Up  index:5    from 16 To 4
        SetMemory(0x661808, Add, -720896),# units:Unit Size Up  index:8    from 15 To 4
        SetMemory(0x661818, Add, -589824),# units:Unit Size Up  index:10    from 13 To 4
        SetMemory(0x661820, Add, -786432),# units:Unit Size Up  index:11    from 16 To 4
        SetMemory(0x661828, Add, -1638400),# units:Unit Size Up  index:12    from 29 To 4
        SetMemory(0x661848, Add, -393216),# units:Unit Size Up  index:16    from 10 To 4
        SetMemory(0x661850, Add, -786432),# units:Unit Size Up  index:17    from 16 To 4
        SetMemory(0x661860, Add, -786432),# units:Unit Size Up  index:19    from 16 To 4
        SetMemory(0x661868, Add, -327680),# units:Unit Size Up  index:20    from 9 To 4
        SetMemory(0x661870, Add, -720896),# units:Unit Size Up  index:21    from 15 To 4
        SetMemory(0x661880, Add, -786432),# units:Unit Size Up  index:23    from 16 To 4
        SetMemory(0x6618A0, Add, -1638400),# units:Unit Size Up  index:27    from 29 To 4
        SetMemory(0x6618A8, Add, -1638400),# units:Unit Size Up  index:28    from 29 To 4
        SetMemory(0x6618B0, Add, -1638400),# units:Unit Size Up  index:29    from 29 To 4
        SetMemory(0x6618C8, Add, -196608),# units:Unit Size Up  index:32    from 7 To 4
        SetMemory(0x6618F0, Add, 0),# units:Unit Size Up  index:37    from 4 To 4
        SetMemory(0x6618F8, Add, -393216),# units:Unit Size Up  index:38    from 10 To 4
        SetMemory(0x661900, Add, -786432),# units:Unit Size Up  index:39    from 16 To 4
        SetMemory(0x661908, Add, -327680),# units:Unit Size Up  index:40    from 9 To 4
        SetMemory(0x661920, Add, -1179648),# units:Unit Size Up  index:43    from 22 To 4
        SetMemory(0x661928, Add, -1179648),# units:Unit Size Up  index:44    from 22 To 4
        SetMemory(0x661938, Add, -524288),# units:Unit Size Up  index:46    from 12 To 4
        SetMemory(0x661948, Add, -786432),# units:Unit Size Up  index:48    from 16 To 4
        SetMemory(0x661960, Add, -393216),# units:Unit Size Up  index:51    from 10 To 4
        SetMemory(0x661968, Add, -655360),# units:Unit Size Up  index:52    from 14 To 4
        SetMemory(0x661970, Add, -393216),# units:Unit Size Up  index:53    from 10 To 4
        SetMemory(0x661978, Add, 0),# units:Unit Size Up  index:54    from 4 To 4
        SetMemory(0x661980, Add, -1179648),# units:Unit Size Up  index:55    from 22 To 4
        SetMemory(0x661988, Add, -1179648),# units:Unit Size Up  index:56    from 22 To 4
        SetMemory(0x6619B0, Add, -131072),# units:Unit Size Up  index:61    from 6 To 4
        SetMemory(0x6619C0, Add, -786432),# units:Unit Size Up  index:63    from 16 To 4
        SetMemory(0x6619D0, Add, -65536),# units:Unit Size Up  index:65    from 5 To 4
        SetMemory(0x6619D8, Add, -458752),# units:Unit Size Up  index:66    from 15 To 8
        SetMemory(0x6619E0, Add, -393216),# units:Unit Size Up  index:67    from 10 To 4
        SetMemory(0x6619E8, Add, -786432),# units:Unit Size Up  index:68    from 16 To 4
        SetMemory(0x6619F0, Add, -786432),# units:Unit Size Up  index:69    from 16 To 4
        SetMemory(0x6619F8, Add, -786432),# units:Unit Size Up  index:70    from 16 To 4
        SetMemory(0x661A00, Add, -1179648),# units:Unit Size Up  index:71    from 22 To 4
        SetMemory(0x661A18, Add, -131072),# units:Unit Size Up  index:74    from 6 To 4
        SetMemory(0x661A20, Add, -131072),# units:Unit Size Up  index:75    from 6 To 4
        SetMemory(0x661A28, Add, -786432),# units:Unit Size Up  index:76    from 16 To 4
        SetMemory(0x661A30, Add, -65536),# units:Unit Size Up  index:77    from 5 To 4
        SetMemory(0x661A38, Add, -720896),# units:Unit Size Up  index:78    from 15 To 4
        SetMemory(0x661A40, Add, -393216),# units:Unit Size Up  index:79    from 10 To 4
        SetMemory(0x661A48, Add, -786432),# units:Unit Size Up  index:80    from 16 To 4
        SetMemory(0x661A78, Add, -1179648),# units:Unit Size Up  index:86    from 22 To 4
        SetMemory(0x661A80, Add, -655360),# units:Unit Size Up  index:87    from 14 To 4
        SetMemory(0x661A88, Add, -786432),# units:Unit Size Up  index:88    from 16 To 4
        SetMemory(0x661AB0, Add, -786432),# units:Unit Size Up  index:93    from 16 To 4
        SetMemory(0x661AB8, Add, -786432),# units:Unit Size Up  index:94    from 16 To 4
        SetMemory(0x661AC0, Add, -786432),# units:Unit Size Up  index:95    from 16 To 4
        SetMemory(0x661AC8, Add, -786432),# units:Unit Size Up  index:96    from 16 To 4
        SetMemory(0x661AE0, Add, -393216),# units:Unit Size Up  index:99    from 10 To 4
        SetMemory(0x661AE8, Add, -393216),# units:Unit Size Up  index:100    from 10 To 4
        SetMemory(0x661AF8, Add, -1638400),# units:Unit Size Up  index:102    from 29 To 4
        SetMemory(0x661B00, Add, -720896),# units:Unit Size Up  index:103    from 15 To 4
        SetMemory(0x661B08, Add, -393216),# units:Unit Size Up  index:104    from 10 To 4
        SetMemory(0x661B40, Add, -2359296),# units:Unit Size Up  index:111    from 40 To 4
        SetMemory(0x661BF0, Add, -1835008),# units:Unit Size Up  index:133    from 32 To 4
        SetMemory(0x661C00, Add, -1835008),# units:Unit Size Up  index:135    from 32 To 4
        SetMemory(0x661C08, Add, -1900544),# units:Unit Size Up  index:136    from 32 To 3
        SetMemory(0x661C10, Add, -1900544),# units:Unit Size Up  index:137    from 32 To 3
        SetMemory(0x661C18, Add, -1638400),# units:Unit Size Up  index:138    from 28 To 3
        SetMemory(0x661C20, Add, -1900544),# units:Unit Size Up  index:139    from 32 To 3
        SetMemory(0x661C28, Add, -1900544),# units:Unit Size Up  index:140    from 32 To 3
        SetMemory(0x661C38, Add, -1638400),# units:Unit Size Up  index:142    from 28 To 3
        SetMemory(0x661C60, Add, -1900544),# units:Unit Size Up  index:147    from 32 To 3
        SetMemory(0x661C68, Add, -1900544),# units:Unit Size Up  index:148    from 32 To 3
        SetMemory(0x661C80, Add, -1900544),# units:Unit Size Up  index:151    from 32 To 3
        SetMemory(0x661C88, Add, -1900544),# units:Unit Size Up  index:152    from 32 To 3
        SetMemory(0x661C98, Add, -2359296),# units:Unit Size Up  index:154    from 39 To 3
        SetMemory(0x661CC0, Add, -851968),# units:Unit Size Up  index:159    from 16 To 3
        SetMemory(0x661CC8, Add, -1900544),# units:Unit Size Up  index:160    from 32 To 3
        SetMemory(0x661CE0, Add, -1376256),# units:Unit Size Up  index:163    from 24 To 3
        SetMemory(0x661CE8, Add, -1376256),# units:Unit Size Up  index:164    from 24 To 3
        SetMemory(0x661CF0, Add, -1376256),# units:Unit Size Up  index:165    from 24 To 3
        SetMemory(0x661CF8, Add, -1376256),# units:Unit Size Up  index:166    from 24 To 3
        SetMemory(0x661D00, Add, -2424832),# units:Unit Size Up  index:167    from 40 To 3
        SetMemory(0x661D08, Add, -2949120),# units:Unit Size Up  index:168    from 48 To 3
        SetMemory(0x661D10, Add, -1900544),# units:Unit Size Up  index:169    from 32 To 3
        SetMemory(0x661D18, Add, -1638400),# units:Unit Size Up  index:170    from 28 To 3
        SetMemory(0x661D20, Add, -1900544),# units:Unit Size Up  index:171    from 32 To 3
        SetMemory(0x661D28, Add, -851968),# units:Unit Size Up  index:172    from 16 To 3
        SetMemory(0x661D30, Add, -2949120),# units:Unit Size Up  index:173    from 48 To 3
        SetMemory(0x661D38, Add, -2949120),# units:Unit Size Up  index:174    from 48 To 3
        SetMemory(0x661D40, Add, -2031616),# units:Unit Size Up  index:175    from 34 To 3
        SetMemory(0x661DE8, Add, -1048576),# units:Unit Size Up  index:196    from 32 To 16
        SetMemory(0x6617CC, Add, -4),# units:Unit Size Right  index:0    from 8 To 4
        SetMemory(0x6617D4, Add, -3),# units:Unit Size Right  index:1    from 7 To 4
        SetMemory(0x6617DC, Add, -11),# units:Unit Size Right  index:2    from 15 To 4
        SetMemory(0x6617E4, Add, -11),# units:Unit Size Right  index:3    from 15 To 4
        SetMemory(0x6617F4, Add, -11),# units:Unit Size Right  index:5    from 15 To 4
        SetMemory(0x66180C, Add, -14),# units:Unit Size Right  index:8    from 18 To 4
        SetMemory(0x66181C, Add, -7),# units:Unit Size Right  index:10    from 11 To 4
        SetMemory(0x661824, Add, -20),# units:Unit Size Right  index:11    from 24 To 4
        SetMemory(0x66182C, Add, -33),# units:Unit Size Right  index:12    from 37 To 4
        SetMemory(0x66184C, Add, -3),# units:Unit Size Right  index:16    from 7 To 4
        SetMemory(0x661854, Add, -11),# units:Unit Size Right  index:17    from 15 To 4
        SetMemory(0x661864, Add, -11),# units:Unit Size Right  index:19    from 15 To 4
        SetMemory(0x66186C, Add, -4),# units:Unit Size Right  index:20    from 8 To 4
        SetMemory(0x661874, Add, -14),# units:Unit Size Right  index:21    from 18 To 4
        SetMemory(0x661884, Add, -11),# units:Unit Size Right  index:23    from 15 To 4
        SetMemory(0x6618A4, Add, -33),# units:Unit Size Right  index:27    from 37 To 4
        SetMemory(0x6618AC, Add, -33),# units:Unit Size Right  index:28    from 37 To 4
        SetMemory(0x6618B4, Add, -33),# units:Unit Size Right  index:29    from 37 To 4
        SetMemory(0x6618CC, Add, -7),# units:Unit Size Right  index:32    from 11 To 4
        SetMemory(0x6618F4, Add, -3),# units:Unit Size Right  index:37    from 7 To 4
        SetMemory(0x6618FC, Add, -6),# units:Unit Size Right  index:38    from 10 To 4
        SetMemory(0x661904, Add, -14),# units:Unit Size Right  index:39    from 18 To 4
        SetMemory(0x66190C, Add, -5),# units:Unit Size Right  index:40    from 9 To 4
        SetMemory(0x661924, Add, -17),# units:Unit Size Right  index:43    from 21 To 4
        SetMemory(0x66192C, Add, -17),# units:Unit Size Right  index:44    from 21 To 4
        SetMemory(0x66193C, Add, -9),# units:Unit Size Right  index:46    from 13 To 4
        SetMemory(0x66194C, Add, -14),# units:Unit Size Right  index:48    from 18 To 4
        SetMemory(0x661964, Add, -3),# units:Unit Size Right  index:51    from 7 To 4
        SetMemory(0x66196C, Add, -10),# units:Unit Size Right  index:52    from 14 To 4
        SetMemory(0x661974, Add, -6),# units:Unit Size Right  index:53    from 10 To 4
        SetMemory(0x66197C, Add, -3),# units:Unit Size Right  index:54    from 7 To 4
        SetMemory(0x661984, Add, -17),# units:Unit Size Right  index:55    from 21 To 4
        SetMemory(0x66198C, Add, -17),# units:Unit Size Right  index:56    from 21 To 4
        SetMemory(0x6619B4, Add, -7),# units:Unit Size Right  index:61    from 11 To 4
        SetMemory(0x6619C4, Add, -11),# units:Unit Size Right  index:63    from 15 To 4
        SetMemory(0x6619D4, Add, -7),# units:Unit Size Right  index:65    from 11 To 4
        SetMemory(0x6619DC, Add, -8),# units:Unit Size Right  index:66    from 16 To 8
        SetMemory(0x6619E4, Add, -7),# units:Unit Size Right  index:67    from 11 To 4
        SetMemory(0x6619EC, Add, -11),# units:Unit Size Right  index:68    from 15 To 4
        SetMemory(0x6619F4, Add, -15),# units:Unit Size Right  index:69    from 19 To 4
        SetMemory(0x6619FC, Add, -13),# units:Unit Size Right  index:70    from 17 To 4
        SetMemory(0x661A04, Add, -17),# units:Unit Size Right  index:71    from 21 To 4
        SetMemory(0x661A1C, Add, -7),# units:Unit Size Right  index:74    from 11 To 4
        SetMemory(0x661A24, Add, -7),# units:Unit Size Right  index:75    from 11 To 4
        SetMemory(0x661A2C, Add, -11),# units:Unit Size Right  index:76    from 15 To 4
        SetMemory(0x661A34, Add, -7),# units:Unit Size Right  index:77    from 11 To 4
        SetMemory(0x661A3C, Add, -12),# units:Unit Size Right  index:78    from 16 To 4
        SetMemory(0x661A44, Add, -7),# units:Unit Size Right  index:79    from 11 To 4
        SetMemory(0x661A4C, Add, -13),# units:Unit Size Right  index:80    from 17 To 4
        SetMemory(0x661A7C, Add, -17),# units:Unit Size Right  index:86    from 21 To 4
        SetMemory(0x661A84, Add, -7),# units:Unit Size Right  index:87    from 11 To 4
        SetMemory(0x661A8C, Add, -13),# units:Unit Size Right  index:88    from 17 To 4
        SetMemory(0x661AB4, Add, -11),# units:Unit Size Right  index:93    from 15 To 4
        SetMemory(0x661ABC, Add, -11),# units:Unit Size Right  index:94    from 15 To 4
        SetMemory(0x661AC4, Add, -11),# units:Unit Size Right  index:95    from 15 To 4
        SetMemory(0x661ACC, Add, -11),# units:Unit Size Right  index:96    from 15 To 4
        SetMemory(0x661AE4, Add, -3),# units:Unit Size Right  index:99    from 7 To 4
        SetMemory(0x661AEC, Add, -3),# units:Unit Size Right  index:100    from 7 To 4
        SetMemory(0x661AFC, Add, -33),# units:Unit Size Right  index:102    from 37 To 4
        SetMemory(0x661B04, Add, -12),# units:Unit Size Right  index:103    from 16 To 4
        SetMemory(0x661B0C, Add, -3),# units:Unit Size Right  index:104    from 7 To 4
        SetMemory(0x661B44, Add, -52),# units:Unit Size Right  index:111    from 56 To 4
        SetMemory(0x661BF4, Add, -45),# units:Unit Size Right  index:133    from 49 To 4
        SetMemory(0x661C04, Add, -36),# units:Unit Size Right  index:135    from 40 To 4
        SetMemory(0x661C0C, Add, -45),# units:Unit Size Right  index:136    from 48 To 3
        SetMemory(0x661C14, Add, -25),# units:Unit Size Right  index:137    from 28 To 3
        SetMemory(0x661C1C, Add, -29),# units:Unit Size Right  index:138    from 32 To 3
        SetMemory(0x661C24, Add, -29),# units:Unit Size Right  index:139    from 32 To 3
        SetMemory(0x661C2C, Add, -29),# units:Unit Size Right  index:140    from 32 To 3
        SetMemory(0x661C3C, Add, -37),# units:Unit Size Right  index:142    from 40 To 3
        SetMemory(0x661C64, Add, -76),# units:Unit Size Right  index:147    from 79 To 3
        SetMemory(0x661C6C, Add, -76),# units:Unit Size Right  index:148    from 79 To 3
        SetMemory(0x661C84, Add, -29),# units:Unit Size Right  index:151    from 32 To 3
        SetMemory(0x661C8C, Add, -29),# units:Unit Size Right  index:152    from 32 To 3
        SetMemory(0x661C9C, Add, -53),# units:Unit Size Right  index:154    from 56 To 3
        SetMemory(0x661CC4, Add, -41),# units:Unit Size Right  index:159    from 44 To 3
        SetMemory(0x661CCC, Add, -45),# units:Unit Size Right  index:160    from 48 To 3
        SetMemory(0x661CE4, Add, -37),# units:Unit Size Right  index:163    from 40 To 3
        SetMemory(0x661CEC, Add, -37),# units:Unit Size Right  index:164    from 40 To 3
        SetMemory(0x661CF4, Add, -29),# units:Unit Size Right  index:165    from 32 To 3
        SetMemory(0x661CFC, Add, -33),# units:Unit Size Right  index:166    from 36 To 3
        SetMemory(0x661D04, Add, -45),# units:Unit Size Right  index:167    from 48 To 3
        SetMemory(0x661D0C, Add, -60),# units:Unit Size Right  index:168    from 63 To 3
        SetMemory(0x661D14, Add, -44),# units:Unit Size Right  index:169    from 47 To 3
        SetMemory(0x661D1C, Add, -41),# units:Unit Size Right  index:170    from 44 To 3
        SetMemory(0x661D24, Add, -29),# units:Unit Size Right  index:171    from 32 To 3
        SetMemory(0x661D2C, Add, -29),# units:Unit Size Right  index:172    from 32 To 3
        SetMemory(0x661D34, Add, -60),# units:Unit Size Right  index:173    from 63 To 3
        SetMemory(0x661D3C, Add, -108),# units:Unit Size Right  index:174    from 111 To 3
        SetMemory(0x661D44, Add, -76),# units:Unit Size Right  index:175    from 79 To 3
        SetMemory(0x661DEC, Add, -31),# units:Unit Size Right  index:196    from 47 To 16
        SetMemory(0x6617CC, Add, -393216),# units:Unit Size Down  index:0    from 10 To 4
        SetMemory(0x6617D4, Add, -458752),# units:Unit Size Down  index:1    from 11 To 4
        SetMemory(0x6617DC, Add, -720896),# units:Unit Size Down  index:2    from 15 To 4
        SetMemory(0x6617E4, Add, -720896),# units:Unit Size Down  index:3    from 15 To 4
        SetMemory(0x6617F4, Add, -720896),# units:Unit Size Down  index:5    from 15 To 4
        SetMemory(0x66180C, Add, -655360),# units:Unit Size Down  index:8    from 14 To 4
        SetMemory(0x66181C, Add, -655360),# units:Unit Size Down  index:10    from 14 To 4
        SetMemory(0x661824, Add, -1048576),# units:Unit Size Down  index:11    from 20 To 4
        SetMemory(0x66182C, Add, -1638400),# units:Unit Size Down  index:12    from 29 To 4
        SetMemory(0x66184C, Add, -458752),# units:Unit Size Down  index:16    from 11 To 4
        SetMemory(0x661854, Add, -720896),# units:Unit Size Down  index:17    from 15 To 4
        SetMemory(0x661864, Add, -720896),# units:Unit Size Down  index:19    from 15 To 4
        SetMemory(0x66186C, Add, -393216),# units:Unit Size Down  index:20    from 10 To 4
        SetMemory(0x661874, Add, -655360),# units:Unit Size Down  index:21    from 14 To 4
        SetMemory(0x661884, Add, -720896),# units:Unit Size Down  index:23    from 15 To 4
        SetMemory(0x6618A4, Add, -1638400),# units:Unit Size Down  index:27    from 29 To 4
        SetMemory(0x6618AC, Add, -1638400),# units:Unit Size Down  index:28    from 29 To 4
        SetMemory(0x6618B4, Add, -1638400),# units:Unit Size Down  index:29    from 29 To 4
        SetMemory(0x6618CC, Add, -655360),# units:Unit Size Down  index:32    from 14 To 4
        SetMemory(0x6618F4, Add, -458752),# units:Unit Size Down  index:37    from 11 To 4
        SetMemory(0x6618FC, Add, -524288),# units:Unit Size Down  index:38    from 12 To 4
        SetMemory(0x661904, Add, -720896),# units:Unit Size Down  index:39    from 15 To 4
        SetMemory(0x66190C, Add, -327680),# units:Unit Size Down  index:40    from 9 To 4
        SetMemory(0x661924, Add, -1114112),# units:Unit Size Down  index:43    from 21 To 4
        SetMemory(0x66192C, Add, -1114112),# units:Unit Size Down  index:44    from 21 To 4
        SetMemory(0x66193C, Add, -524288),# units:Unit Size Down  index:46    from 12 To 4
        SetMemory(0x66194C, Add, -720896),# units:Unit Size Down  index:48    from 15 To 4
        SetMemory(0x661964, Add, -458752),# units:Unit Size Down  index:51    from 11 To 4
        SetMemory(0x66196C, Add, -655360),# units:Unit Size Down  index:52    from 14 To 4
        SetMemory(0x661974, Add, -524288),# units:Unit Size Down  index:53    from 12 To 4
        SetMemory(0x66197C, Add, -458752),# units:Unit Size Down  index:54    from 11 To 4
        SetMemory(0x661984, Add, -1114112),# units:Unit Size Down  index:55    from 21 To 4
        SetMemory(0x66198C, Add, -1114112),# units:Unit Size Down  index:56    from 21 To 4
        SetMemory(0x6619B4, Add, -983040),# units:Unit Size Down  index:61    from 19 To 4
        SetMemory(0x6619C4, Add, -720896),# units:Unit Size Down  index:63    from 15 To 4
        SetMemory(0x6619D4, Add, -589824),# units:Unit Size Down  index:65    from 13 To 4
        SetMemory(0x6619DC, Add, -524288),# units:Unit Size Down  index:66    from 16 To 8
        SetMemory(0x6619E4, Add, -589824),# units:Unit Size Down  index:67    from 13 To 4
        SetMemory(0x6619EC, Add, -720896),# units:Unit Size Down  index:68    from 15 To 4
        SetMemory(0x6619F4, Add, -720896),# units:Unit Size Down  index:69    from 15 To 4
        SetMemory(0x6619FC, Add, -720896),# units:Unit Size Down  index:70    from 15 To 4
        SetMemory(0x661A04, Add, -1114112),# units:Unit Size Down  index:71    from 21 To 4
        SetMemory(0x661A1C, Add, -983040),# units:Unit Size Down  index:74    from 19 To 4
        SetMemory(0x661A24, Add, -983040),# units:Unit Size Down  index:75    from 19 To 4
        SetMemory(0x661A2C, Add, -720896),# units:Unit Size Down  index:76    from 15 To 4
        SetMemory(0x661A34, Add, -589824),# units:Unit Size Down  index:77    from 13 To 4
        SetMemory(0x661A3C, Add, -786432),# units:Unit Size Down  index:78    from 16 To 4
        SetMemory(0x661A44, Add, -589824),# units:Unit Size Down  index:79    from 13 To 4
        SetMemory(0x661A4C, Add, -720896),# units:Unit Size Down  index:80    from 15 To 4
        SetMemory(0x661A7C, Add, -1114112),# units:Unit Size Down  index:86    from 21 To 4
        SetMemory(0x661A84, Add, -589824),# units:Unit Size Down  index:87    from 13 To 4
        SetMemory(0x661A8C, Add, -720896),# units:Unit Size Down  index:88    from 15 To 4
        SetMemory(0x661AB4, Add, -720896),# units:Unit Size Down  index:93    from 15 To 4
        SetMemory(0x661ABC, Add, -720896),# units:Unit Size Down  index:94    from 15 To 4
        SetMemory(0x661AC4, Add, -720896),# units:Unit Size Down  index:95    from 15 To 4
        SetMemory(0x661ACC, Add, -720896),# units:Unit Size Down  index:96    from 15 To 4
        SetMemory(0x661AE4, Add, -458752),# units:Unit Size Down  index:99    from 11 To 4
        SetMemory(0x661AEC, Add, -458752),# units:Unit Size Down  index:100    from 11 To 4
        SetMemory(0x661AFC, Add, -1638400),# units:Unit Size Down  index:102    from 29 To 4
        SetMemory(0x661B04, Add, -786432),# units:Unit Size Down  index:103    from 16 To 4
        SetMemory(0x661B0C, Add, -458752),# units:Unit Size Down  index:104    from 11 To 4
        SetMemory(0x661B44, Add, -1835008),# units:Unit Size Down  index:111    from 32 To 4
        SetMemory(0x661BF4, Add, -1835008),# units:Unit Size Down  index:133    from 32 To 4
        SetMemory(0x661C04, Add, -1310720),# units:Unit Size Down  index:135    from 24 To 4
        SetMemory(0x661C0C, Add, -65536),# units:Unit Size Down  index:136    from 4 To 3
        SetMemory(0x661C14, Add, -1376256),# units:Unit Size Down  index:137    from 24 To 3
        SetMemory(0x661C1C, Add, -1638400),# units:Unit Size Down  index:138    from 28 To 3
        SetMemory(0x661C24, Add, -1114112),# units:Unit Size Down  index:139    from 20 To 3
        SetMemory(0x661C2C, Add, -1835008),# units:Unit Size Down  index:140    from 31 To 3
        SetMemory(0x661C3C, Add, -983040),# units:Unit Size Down  index:142    from 18 To 3
        SetMemory(0x661C64, Add, -2424832),# units:Unit Size Down  index:147    from 40 To 3
        SetMemory(0x661C6C, Add, -2424832),# units:Unit Size Down  index:148    from 40 To 3
        SetMemory(0x661C84, Add, -1835008),# units:Unit Size Down  index:151    from 31 To 3
        SetMemory(0x661C8C, Add, -1835008),# units:Unit Size Down  index:152    from 31 To 3
        SetMemory(0x661C9C, Add, -2359296),# units:Unit Size Down  index:154    from 39 To 3
        SetMemory(0x661CC4, Add, -1638400),# units:Unit Size Down  index:159    from 28 To 3
        SetMemory(0x661CCC, Add, -2424832),# units:Unit Size Down  index:160    from 40 To 3
        SetMemory(0x661CE4, Add, -1376256),# units:Unit Size Down  index:163    from 24 To 3
        SetMemory(0x661CEC, Add, -1376256),# units:Unit Size Down  index:164    from 24 To 3
        SetMemory(0x661CF4, Add, -1376256),# units:Unit Size Down  index:165    from 24 To 3
        SetMemory(0x661CFC, Add, -1114112),# units:Unit Size Down  index:166    from 20 To 3
        SetMemory(0x661D04, Add, -1900544),# units:Unit Size Down  index:167    from 32 To 3
        SetMemory(0x661D0C, Add, -2883584),# units:Unit Size Down  index:168    from 47 To 3
        SetMemory(0x661D14, Add, -1376256),# units:Unit Size Down  index:169    from 24 To 3
        SetMemory(0x661D1C, Add, -1638400),# units:Unit Size Down  index:170    from 28 To 3
        SetMemory(0x661D24, Add, -1114112),# units:Unit Size Down  index:171    from 20 To 3
        SetMemory(0x661D2C, Add, -851968),# units:Unit Size Down  index:172    from 16 To 3
        SetMemory(0x661D34, Add, -2883584),# units:Unit Size Down  index:173    from 47 To 3
        SetMemory(0x661D3C, Add, -2883584),# units:Unit Size Down  index:174    from 47 To 3
        SetMemory(0x661D44, Add, -3932160),# units:Unit Size Down  index:175    from 63 To 3
        SetMemory(0x661DEC, Add, -983040),# units:Unit Size Down  index:196    from 31 To 16
        SetMemory(0x663064, Add, 4063232),# units:Portrait  index:111    from 17 To 79
        SetMemory(0x663098, Add, 41),# units:Portrait  index:136    from 38 To 79
        SetMemory(0x663098, Add, 2686976),# units:Portrait  index:137    from 38 To 79
        SetMemory(0x66309C, Add, 41),# units:Portrait  index:138    from 38 To 79
        SetMemory(0x66309C, Add, 2686976),# units:Portrait  index:139    from 38 To 79
        SetMemory(0x6630A0, Add, 41),# units:Portrait  index:140    from 38 To 79
        SetMemory(0x6630A4, Add, 41),# units:Portrait  index:142    from 38 To 79
        SetMemory(0x6630AC, Add, 2686976),# units:Portrait  index:147    from 38 To 79
        SetMemory(0x6630B0, Add, 41),# units:Portrait  index:148    from 38 To 79
        SetMemory(0x6630B4, Add, 2949120),# units:Portrait  index:151    from 34 To 79
        SetMemory(0x6630B8, Add, 44),# units:Portrait  index:152    from 35 To 79
        SetMemory(0x6630BC, Add, 19),# units:Portrait  index:154    from 60 To 79
        SetMemory(0x6630C4, Add, 1245184),# units:Portrait  index:159    from 60 To 79
        SetMemory(0x6630C8, Add, 19),# units:Portrait  index:160    from 60 To 79
        SetMemory(0x6630CC, Add, 1245184),# units:Portrait  index:163    from 60 To 79
        SetMemory(0x6630D0, Add, 19),# units:Portrait  index:164    from 60 To 79
        SetMemory(0x6630D0, Add, 1245184),# units:Portrait  index:165    from 60 To 79
        SetMemory(0x6630D4, Add, 19),# units:Portrait  index:166    from 60 To 79
        SetMemory(0x6630D4, Add, 1245184),# units:Portrait  index:167    from 60 To 79
        SetMemory(0x6630D8, Add, 38),# units:Portrait  index:168    from 41 To 79
        SetMemory(0x6630D8, Add, 1245184),# units:Portrait  index:169    from 60 To 79
        SetMemory(0x6630DC, Add, 19),# units:Portrait  index:170    from 60 To 79
        SetMemory(0x6630DC, Add, 1245184),# units:Portrait  index:171    from 60 To 79
        SetMemory(0x6630E0, Add, 19),# units:Portrait  index:172    from 60 To 79
        SetMemory(0x6630E0, Add, 1376256),# units:Portrait  index:173    from 58 To 79
        SetMemory(0x6630E4, Add, 19),# units:Portrait  index:174    from 60 To 79
        SetMemory(0x6630E4, Add, 1245184),# units:Portrait  index:175    from 60 To 79
        SetMemory(0x663964, Add, 3276800),# units:Mineral Cost  index:111    from 150 To 200
        SetMemory(0x663990, Add, -6553600),# units:Mineral Cost  index:133    from 200 To 100
        SetMemory(0x663998, Add, -100),# units:Mineral Cost  index:136    from 100 To 0
        SetMemory(0x663998, Add, -6553600),# units:Mineral Cost  index:137    from 100 To 0
        SetMemory(0x66399C, Add, -150),# units:Mineral Cost  index:138    from 150 To 0
        SetMemory(0x66399C, Add, -4915200),# units:Mineral Cost  index:139    from 75 To 0
        SetMemory(0x6639A0, Add, -150),# units:Mineral Cost  index:140    from 150 To 0
        SetMemory(0x6639A4, Add, -200),# units:Mineral Cost  index:142    from 200 To 0
        SetMemory(0x6639AC, Add, -65536),# units:Mineral Cost  index:147    from 1 To 0
        SetMemory(0x6639B0, Add, -1),# units:Mineral Cost  index:148    from 1 To 0
        SetMemory(0x6639BC, Add, -400),# units:Mineral Cost  index:154    from 400 To 0
        SetMemory(0x6639C4, Add, -3276800),# units:Mineral Cost  index:159    from 50 To 0
        SetMemory(0x6639C8, Add, -150),# units:Mineral Cost  index:160    from 150 To 0
        SetMemory(0x6639CC, Add, -9830400),# units:Mineral Cost  index:163    from 150 To 0
        SetMemory(0x6639D0, Add, -200),# units:Mineral Cost  index:164    from 200 To 0
        SetMemory(0x6639D0, Add, -9830400),# units:Mineral Cost  index:165    from 150 To 0
        SetMemory(0x6639D4, Add, -150),# units:Mineral Cost  index:166    from 150 To 0
        SetMemory(0x6639D4, Add, -9830400),# units:Mineral Cost  index:167    from 150 To 0
        SetMemory(0x6639D8, Add, -150),# units:Mineral Cost  index:168    from 150 To 0
        SetMemory(0x6639D8, Add, -19660800),# units:Mineral Cost  index:169    from 300 To 0
        SetMemory(0x6639DC, Add, -200),# units:Mineral Cost  index:170    from 200 To 0
        SetMemory(0x6639DC, Add, -9830400),# units:Mineral Cost  index:171    from 150 To 0
        SetMemory(0x6639E0, Add, -100),# units:Mineral Cost  index:172    from 100 To 0
        SetMemory(0x6639E0, Add, -16384000),# units:Mineral Cost  index:173    from 250 To 0
        SetMemory(0x6639E4, Add, -250),# units:Mineral Cost  index:174    from 250 To 0
        SetMemory(0x6639E4, Add, -98304000),# units:Mineral Cost  index:175    from 1500 To 0
        SetMemory(0x65FDDC, Add, 4915200),# units:Vespene Cost  index:111    from 0 To 75
        SetMemory(0x65FE08, Add, -6553600),# units:Vespene Cost  index:133    from 150 To 50
        SetMemory(0x65FE10, Add, -100),# units:Vespene Cost  index:136    from 100 To 0
        SetMemory(0x65FE10, Add, -9830400),# units:Vespene Cost  index:137    from 150 To 0
        SetMemory(0x65FE14, Add, -100),# units:Vespene Cost  index:138    from 100 To 0
        SetMemory(0x65FE18, Add, -200),# units:Vespene Cost  index:140    from 200 To 0
        SetMemory(0x65FE24, Add, -65536),# units:Vespene Cost  index:147    from 1 To 0
        SetMemory(0x65FE28, Add, -1),# units:Vespene Cost  index:148    from 1 To 0
        SetMemory(0x65FE3C, Add, -6553600),# units:Vespene Cost  index:159    from 100 To 0
        SetMemory(0x65FE44, Add, -6553600),# units:Vespene Cost  index:163    from 100 To 0
        SetMemory(0x65FE48, Add, -13107200),# units:Vespene Cost  index:165    from 200 To 0
        SetMemory(0x65FE4C, Add, -9830400),# units:Vespene Cost  index:167    from 150 To 0
        SetMemory(0x65FE50, Add, -13107200),# units:Vespene Cost  index:169    from 200 To 0
        SetMemory(0x65FE54, Add, -150),# units:Vespene Cost  index:170    from 150 To 0
        SetMemory(0x65FE54, Add, -6553600),# units:Vespene Cost  index:171    from 100 To 0
        SetMemory(0x65FE5C, Add, -32768000),# units:Vespene Cost  index:175    from 500 To 0
        SetMemory(0x660504, Add, 19660800),# units:Build Time  index:111    from 1200 To 1500
        SetMemory(0x660530, Add, -78643200),# units:Build Time  index:133    from 1800 To 600
        SetMemory(0x660538, Add, -899),# units:Build Time  index:136    from 900 To 1
        SetMemory(0x660538, Add, -117899264),# units:Build Time  index:137    from 1800 To 1
        SetMemory(0x66053C, Add, -899),# units:Build Time  index:138    from 900 To 1
        SetMemory(0x66053C, Add, -39256064),# units:Build Time  index:139    from 600 To 1
        SetMemory(0x660540, Add, -1199),# units:Build Time  index:140    from 1200 To 1
        SetMemory(0x660544, Add, -1199),# units:Build Time  index:142    from 1200 To 1
        SetMemory(0x660554, Add, 65536),# units:Build Time  index:151    from 0 To 1
        SetMemory(0x660558, Add, 1),# units:Build Time  index:152    from 0 To 1
        SetMemory(0x66055C, Add, -1799),# units:Build Time  index:154    from 1800 To 1
        SetMemory(0x660564, Add, -29425664),# units:Build Time  index:159    from 450 To 1
        SetMemory(0x660568, Add, -899),# units:Build Time  index:160    from 900 To 1
        SetMemory(0x66056C, Add, -58916864),# units:Build Time  index:163    from 900 To 1
        SetMemory(0x660570, Add, -899),# units:Build Time  index:164    from 900 To 1
        SetMemory(0x660570, Add, -58916864),# units:Build Time  index:165    from 900 To 1
        SetMemory(0x660574, Add, -599),# units:Build Time  index:166    from 600 To 1
        SetMemory(0x660574, Add, -68747264),# units:Build Time  index:167    from 1050 To 1
        SetMemory(0x660578, Add, -58916864),# units:Build Time  index:169    from 900 To 1
        SetMemory(0x66057C, Add, -899),# units:Build Time  index:170    from 900 To 1
        SetMemory(0x66057C, Add, -29425664),# units:Build Time  index:171    from 450 To 1
        SetMemory(0x660580, Add, -449),# units:Build Time  index:172    from 450 To 1
        SetMemory(0x660584, Add, -314507264),# units:Build Time  index:175    from 4800 To 1
        SetMemory(0x6637A0, Add, 0),# units:Staredit Group Flags  index:0    from 10 To 10
        SetMemory(0x6637A4, Add, 0),# units:Staredit Group Flags  index:5    from 10 To 10
        SetMemory(0x6637B0, Add, 0),# units:Staredit Group Flags  index:16    from 10 To 10
        SetMemory(0x6637C4, Add, 256),# units:Staredit Group Flags  index:37    from 9 To 10
        SetMemory(0x6637C4, Add, 65536),# units:Staredit Group Flags  index:38    from 9 To 10
        SetMemory(0x6637C4, Add, 16777216),# units:Staredit Group Flags  index:39    from 9 To 10
        SetMemory(0x6637C8, Add, 1),# units:Staredit Group Flags  index:40    from 9 To 10
        SetMemory(0x6637C8, Add, 16777216),# units:Staredit Group Flags  index:43    from 9 To 10
        SetMemory(0x6637CC, Add, 1),# units:Staredit Group Flags  index:44    from 9 To 10
        SetMemory(0x6637CC, Add, 65536),# units:Staredit Group Flags  index:46    from 9 To 10
        SetMemory(0x6637D0, Add, 1),# units:Staredit Group Flags  index:48    from 9 To 10
        SetMemory(0x6637D0, Add, 16777216),# units:Staredit Group Flags  index:51    from 9 To 10
        SetMemory(0x6637D4, Add, 1),# units:Staredit Group Flags  index:52    from 9 To 10
        SetMemory(0x6637D4, Add, 256),# units:Staredit Group Flags  index:53    from 9 To 10
        SetMemory(0x6637D4, Add, 65536),# units:Staredit Group Flags  index:54    from 9 To 10
        SetMemory(0x6637D4, Add, 16777216),# units:Staredit Group Flags  index:55    from 9 To 10
        SetMemory(0x6637D8, Add, 1),# units:Staredit Group Flags  index:56    from 9 To 10
        SetMemory(0x6637DC, Add, -512),# units:Staredit Group Flags  index:61    from 12 To 10
        SetMemory(0x6637DC, Add, -33554432),# units:Staredit Group Flags  index:63    from 12 To 10
        SetMemory(0x6637E0, Add, -512),# units:Staredit Group Flags  index:65    from 12 To 10
        SetMemory(0x6637E0, Add, -131072),# units:Staredit Group Flags  index:66    from 12 To 10
        SetMemory(0x6637E0, Add, -33554432),# units:Staredit Group Flags  index:67    from 12 To 10
        SetMemory(0x6637E4, Add, -2),# units:Staredit Group Flags  index:68    from 12 To 10
        SetMemory(0x6637E4, Add, -512),# units:Staredit Group Flags  index:69    from 12 To 10
        SetMemory(0x6637E4, Add, -131072),# units:Staredit Group Flags  index:70    from 12 To 10
        SetMemory(0x6637E4, Add, -33554432),# units:Staredit Group Flags  index:71    from 12 To 10
        SetMemory(0x6637E8, Add, -131072),# units:Staredit Group Flags  index:74    from 12 To 10
        SetMemory(0x6637E8, Add, -33554432),# units:Staredit Group Flags  index:75    from 12 To 10
        SetMemory(0x6637EC, Add, -2),# units:Staredit Group Flags  index:76    from 12 To 10
        SetMemory(0x6637EC, Add, -512),# units:Staredit Group Flags  index:77    from 12 To 10
        SetMemory(0x6637EC, Add, -131072),# units:Staredit Group Flags  index:78    from 12 To 10
        SetMemory(0x6637EC, Add, -33554432),# units:Staredit Group Flags  index:79    from 12 To 10
        SetMemory(0x6637F0, Add, -2),# units:Staredit Group Flags  index:80    from 12 To 10
        SetMemory(0x6637F4, Add, -131072),# units:Staredit Group Flags  index:86    from 12 To 10
        SetMemory(0x6637F4, Add, -33554432),# units:Staredit Group Flags  index:87    from 12 To 10
        SetMemory(0x6637F8, Add, -2),# units:Staredit Group Flags  index:88    from 12 To 10
        SetMemory(0x663804, Add, 0),# units:Staredit Group Flags  index:100    from 10 To 10
        SetMemory(0x663804, Add, 16777216),# units:Staredit Group Flags  index:103    from 9 To 10
        SetMemory(0x663808, Add, 1),# units:Staredit Group Flags  index:104    from 9 To 10
        SetMemory(0x66380C, Add, -671088640),# units:Staredit Group Flags  index:111    from 50 To 10
        SetMemory(0x663824, Add, -9984),# units:Staredit Group Flags  index:133    from 49 To 10
        SetMemory(0x663824, Add, -117440512),# units:Staredit Group Flags  index:135    from 17 To 10
        SetMemory(0x663828, Add, -7),# units:Staredit Group Flags  index:136    from 17 To 10
        SetMemory(0x663828, Add, -1792),# units:Staredit Group Flags  index:137    from 17 To 10
        SetMemory(0x663828, Add, -458752),# units:Staredit Group Flags  index:138    from 17 To 10
        SetMemory(0x663828, Add, -117440512),# units:Staredit Group Flags  index:139    from 17 To 10
        SetMemory(0x66382C, Add, -7),# units:Staredit Group Flags  index:140    from 17 To 10
        SetMemory(0x66382C, Add, -458752),# units:Staredit Group Flags  index:142    from 17 To 10
        SetMemory(0x663830, Add, -117440512),# units:Staredit Group Flags  index:147    from 17 To 10
        SetMemory(0x663834, Add, -7),# units:Staredit Group Flags  index:148    from 17 To 10
        SetMemory(0x663834, Add, -117440512),# units:Staredit Group Flags  index:151    from 17 To 10
        SetMemory(0x663838, Add, -7),# units:Staredit Group Flags  index:152    from 17 To 10
        SetMemory(0x663838, Add, -2752512),# units:Staredit Group Flags  index:154    from 52 To 10
        SetMemory(0x66383C, Add, -167772160),# units:Staredit Group Flags  index:159    from 20 To 10
        SetMemory(0x663840, Add, -42),# units:Staredit Group Flags  index:160    from 52 To 10
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
        SetMemory(0x66474C, Add, -512),# units:Supply Provided  index:133    from 2 To 0
        SetMemory(0x664760, Add, -1179648),# units:Supply Provided  index:154    from 18 To 0
        SetMemory(0x663D24, Add, -4),# units:Supply Required  index:60    from 4 To 0
        SetMemory(0x664498, Add, -254),# units:Space Required  index:136    from 255 To 1
        SetMemory(0x664498, Add, -65024),# units:Space Required  index:137    from 255 To 1
        SetMemory(0x664498, Add, -16646144),# units:Space Required  index:138    from 255 To 1
        SetMemory(0x664498, Add, -4261412864),# units:Space Required  index:139    from 255 To 1
        SetMemory(0x66449C, Add, -254),# units:Space Required  index:140    from 255 To 1
        SetMemory(0x66449C, Add, -16646144),# units:Space Required  index:142    from 255 To 1
        SetMemory(0x6644A0, Add, -4261412864),# units:Space Required  index:147    from 255 To 1
        SetMemory(0x6644A4, Add, -254),# units:Space Required  index:148    from 255 To 1
        SetMemory(0x6644A4, Add, -4261412864),# units:Space Required  index:151    from 255 To 1
        SetMemory(0x6644A8, Add, -254),# units:Space Required  index:152    from 255 To 1
        SetMemory(0x6644A8, Add, -16646144),# units:Space Required  index:154    from 255 To 1
        SetMemory(0x6644AC, Add, -4261412864),# units:Space Required  index:159    from 255 To 1
        SetMemory(0x6644B0, Add, -254),# units:Space Required  index:160    from 255 To 1
        SetMemory(0x6644B0, Add, -4261412864),# units:Space Required  index:163    from 255 To 1
        SetMemory(0x6644B4, Add, -254),# units:Space Required  index:164    from 255 To 1
        SetMemory(0x6644B4, Add, -65024),# units:Space Required  index:165    from 255 To 1
        SetMemory(0x6644B4, Add, -16646144),# units:Space Required  index:166    from 255 To 1
        SetMemory(0x6644B4, Add, -4261412864),# units:Space Required  index:167    from 255 To 1
        SetMemory(0x6644B8, Add, -254),# units:Space Required  index:168    from 255 To 1
        SetMemory(0x6644B8, Add, -65024),# units:Space Required  index:169    from 255 To 1
        SetMemory(0x6644B8, Add, -16646144),# units:Space Required  index:170    from 255 To 1
        SetMemory(0x6644B8, Add, -4261412864),# units:Space Required  index:171    from 255 To 1
        SetMemory(0x6644BC, Add, -254),# units:Space Required  index:172    from 255 To 1
        SetMemory(0x6644BC, Add, -65024),# units:Space Required  index:173    from 255 To 1
        SetMemory(0x6644BC, Add, -16646144),# units:Space Required  index:174    from 255 To 1
        SetMemory(0x6644BC, Add, -4261412864),# units:Space Required  index:175    from 255 To 1
        SetMemory(0x6634E4, Add, -4915200),# units:Build Score  index:111    from 75 To 0
        SetMemory(0x663518, Add, -150),# units:Build Score  index:136    from 150 To 0
        SetMemory(0x663518, Add, -13107200),# units:Build Score  index:137    from 200 To 0
        SetMemory(0x66351C, Add, -175),# units:Build Score  index:138    from 175 To 0
        SetMemory(0x66351C, Add, -2621440),# units:Build Score  index:139    from 40 To 0
        SetMemory(0x663520, Add, -275),# units:Build Score  index:140    from 275 To 0
        SetMemory(0x663524, Add, -75),# units:Build Score  index:142    from 75 To 0
        SetMemory(0x66353C, Add, -400),# units:Build Score  index:154    from 400 To 0
        SetMemory(0x663544, Add, -11468800),# units:Build Score  index:159    from 175 To 0
        SetMemory(0x663548, Add, -75),# units:Build Score  index:160    from 75 To 0
        SetMemory(0x66354C, Add, -13107200),# units:Build Score  index:163    from 200 To 0
        SetMemory(0x663550, Add, -100),# units:Build Score  index:164    from 100 To 0
        SetMemory(0x663550, Add, -16384000),# units:Build Score  index:165    from 250 To 0
        SetMemory(0x663554, Add, -100),# units:Build Score  index:166    from 100 To 0
        SetMemory(0x663554, Add, -19660800),# units:Build Score  index:167    from 300 To 0
        SetMemory(0x663558, Add, -22937600),# units:Build Score  index:169    from 350 To 0
        SetMemory(0x66355C, Add, -450),# units:Build Score  index:170    from 450 To 0
        SetMemory(0x66355C, Add, -8192000),# units:Build Score  index:171    from 125 To 0
        SetMemory(0x663560, Add, -50),# units:Build Score  index:172    from 50 To 0
        SetMemory(0x663F94, Add, 31129600),# units:Destroy Score  index:111    from 225 To 700
        SetMemory(0x663FC0, Add, -78643200),# units:Destroy Score  index:133    from 1500 To 300
        SetMemory(0x663FC8, Add, -440),# units:Destroy Score  index:136    from 450 To 10
        SetMemory(0x663FC8, Add, -87818240),# units:Destroy Score  index:137    from 1350 To 10
        SetMemory(0x663FCC, Add, -515),# units:Destroy Score  index:138    from 525 To 10
        SetMemory(0x663FCC, Add, -7208960),# units:Destroy Score  index:139    from 120 To 10
        SetMemory(0x663FD0, Add, -815),# units:Destroy Score  index:140    from 825 To 10
        SetMemory(0x663FD4, Add, -215),# units:Destroy Score  index:142    from 225 To 10
        SetMemory(0x663FDC, Add, -654704640),# units:Destroy Score  index:147    from 10000 To 10
        SetMemory(0x663FE0, Add, -9990),# units:Destroy Score  index:148    from 10000 To 10
        SetMemory(0x663FE4, Add, -163184640),# units:Destroy Score  index:151    from 2500 To 10
        SetMemory(0x663FE8, Add, -2490),# units:Destroy Score  index:152    from 2500 To 10
        SetMemory(0x663FEC, Add, -1190),# units:Destroy Score  index:154    from 1200 To 10
        SetMemory(0x663FF4, Add, -33751040),# units:Destroy Score  index:159    from 525 To 10
        SetMemory(0x663FF8, Add, -215),# units:Destroy Score  index:160    from 225 To 10
        SetMemory(0x663FFC, Add, -38666240),# units:Destroy Score  index:163    from 600 To 10
        SetMemory(0x664000, Add, -290),# units:Destroy Score  index:164    from 300 To 10
        SetMemory(0x664000, Add, -48496640),# units:Destroy Score  index:165    from 750 To 10
        SetMemory(0x664004, Add, -290),# units:Destroy Score  index:166    from 300 To 10
        SetMemory(0x664004, Add, -58327040),# units:Destroy Score  index:167    from 900 To 10
        SetMemory(0x664008, Add, -4990),# units:Destroy Score  index:168    from 5000 To 10
        SetMemory(0x664008, Add, -68157440),# units:Destroy Score  index:169    from 1050 To 10
        SetMemory(0x66400C, Add, -1340),# units:Destroy Score  index:170    from 1350 To 10
        SetMemory(0x66400C, Add, -23920640),# units:Destroy Score  index:171    from 375 To 10
        SetMemory(0x664010, Add, -140),# units:Destroy Score  index:172    from 150 To 10
        SetMemory(0x664010, Add, -163184640),# units:Destroy Score  index:173    from 2500 To 10
        SetMemory(0x664014, Add, -4990),# units:Destroy Score  index:174    from 5000 To 10
        SetMemory(0x664014, Add, -327024640),# units:Destroy Score  index:175    from 5000 To 10
        SetMemory(0x660744, Add, 16777216),# units:Broodwar Unit Flag  index:111    from 0 To 1
        SetMemory(0x660784, Add, -16777216),# units:Broodwar Unit Flag  index:175    from 1 To 0
        SetMemory(0x6615C4, Add, 512),# units:Staredit Availability Flags  index:86    from 455 To 967
        SetMemory(0x6615C4, Add, 63111168),# units:Staredit Availability Flags  index:87    from 4 To 967
        SetMemory(0x6615E4, Add, 963),# units:Staredit Availability Flags  index:102    from 4 To 967
        SetMemory(0x6615F4, Add, 33030144),# units:Staredit Availability Flags  index:111    from 463 To 967
        SetMemory(0x66163C, Add, 524288),# units:Staredit Availability Flags  index:147    from 455 To 463
        SetMemory(0x661640, Add, 8),# units:Staredit Availability Flags  index:148    from 455 To 463
        SetMemory(0x661644, Add, 524288),# units:Staredit Availability Flags  index:151    from 455 To 463
        SetMemory(0x661648, Add, 8),# units:Staredit Availability Flags  index:152    from 455 To 463
        SetMemory(0x661668, Add, 8),# units:Staredit Availability Flags  index:168    from 455 To 463
        SetMemory(0x661670, Add, 524288),# units:Staredit Availability Flags  index:173    from 455 To 463
        SetMemory(0x661674, Add, 8),# units:Staredit Availability Flags  index:174    from 455 To 463
        SetMemory(0x661674, Add, -33030144),# units:Staredit Availability Flags  index:175    from 967 To 463
        SetMemory(0x656CB4, Add, 19),# weapons:Graphics  index:3    from 143 To 162
        SetMemory(0x656CC8, Add, 9),# weapons:Graphics  index:8    from 146 To 155
        SetMemory(0x656CD0, Add, 13),# weapons:Graphics  index:10    from 146 To 159
        SetMemory(0x656CD4, Add, 8),# weapons:Graphics  index:11    from 143 To 151
        SetMemory(0x656D60, Add, 4),# weapons:Graphics  index:46    from 163 To 167
        SetMemory(0x656D64, Add, 3),# weapons:Graphics  index:47    from 163 To 166
        SetMemory(0x656DE0, Add, -9),# weapons:Graphics  index:78    from 159 To 150
        SetMemory(0x656E78, Add, 22),# weapons:Graphics  index:116    from 143 To 165
        SetMemory(0x657998, Add, -1),# weapons:Target Flags  index:0    from 3 To 2
        SetMemory(0x657998, Add, -65536),# weapons:Target Flags  index:1    from 3 To 2
        SetMemory(0x65799C, Add, -1),# weapons:Target Flags  index:2    from 3 To 2
        SetMemory(0x65799C, Add, -65536),# weapons:Target Flags  index:3    from 3 To 2
        SetMemory(0x6579A8, Add, 1),# weapons:Target Flags  index:8    from 1 To 2
        SetMemory(0x6579AC, Add, 1),# weapons:Target Flags  index:10    from 1 To 2
        SetMemory(0x6579B4, Add, 65536),# weapons:Target Flags  index:15    from 1 To 2
        SetMemory(0x6579B8, Add, 65536),# weapons:Target Flags  index:17    from 1 To 2
        SetMemory(0x6579C0, Add, 1),# weapons:Target Flags  index:20    from 1 To 2
        SetMemory(0x6579C4, Add, 1),# weapons:Target Flags  index:22    from 1 To 2
        SetMemory(0x6579C8, Add, 1),# weapons:Target Flags  index:24    from 1 To 2
        SetMemory(0x6579D0, Add, 65536),# weapons:Target Flags  index:29    from 1 To 2
        SetMemory(0x6579D4, Add, -1),# weapons:Target Flags  index:30    from 3 To 2
        SetMemory(0x6579E4, Add, -1),# weapons:Target Flags  index:38    from 3 To 2
        SetMemory(0x6579E4, Add, -65536),# weapons:Target Flags  index:39    from 3 To 2
        SetMemory(0x6579F0, Add, -65536),# weapons:Target Flags  index:45    from 3 To 2
        SetMemory(0x6579F8, Add, -1),# weapons:Target Flags  index:48    from 3 To 2
        SetMemory(0x6579F8, Add, -65536),# weapons:Target Flags  index:49    from 3 To 2
        SetMemory(0x657A1C, Add, -1),# weapons:Target Flags  index:66    from 3 To 2
        SetMemory(0x657A1C, Add, -65536),# weapons:Target Flags  index:67    from 3 To 2
        SetMemory(0x657A24, Add, -1),# weapons:Target Flags  index:70    from 3 To 2
        SetMemory(0x657A24, Add, -65536),# weapons:Target Flags  index:71    from 3 To 2
        SetMemory(0x657A2C, Add, 1),# weapons:Target Flags  index:74    from 1 To 2
        SetMemory(0x657A30, Add, 1),# weapons:Target Flags  index:76    from 1 To 2
        SetMemory(0x657A30, Add, -65536),# weapons:Target Flags  index:77    from 3 To 2
        SetMemory(0x657A34, Add, -1),# weapons:Target Flags  index:78    from 3 To 2
        SetMemory(0x657A34, Add, -65536),# weapons:Target Flags  index:79    from 3 To 2
        SetMemory(0x657A38, Add, 65536),# weapons:Target Flags  index:81    from 1 To 2
        SetMemory(0x657A60, Add, 1),# weapons:Target Flags  index:100    from 1 To 2
        SetMemory(0x657A68, Add, 1),# weapons:Target Flags  index:104    from 1 To 2
        SetMemory(0x657A74, Add, -1),# weapons:Target Flags  index:110    from 3 To 2
        SetMemory(0x657A78, Add, -1),# weapons:Target Flags  index:112    from 3 To 2
        SetMemory(0x657A78, Add, -65536),# weapons:Target Flags  index:113    from 3 To 2
        SetMemory(0x657A7C, Add, 65536),# weapons:Target Flags  index:115    from 1 To 2
        SetMemory(0x657A80, Add, -1),# weapons:Target Flags  index:116    from 3 To 2
        SetMemory(0x656670, Add, -16777216),# weapons:Weapon Behavior  index:3    from 2 To 1
        SetMemory(0x656678, Add, -16777216),# weapons:Weapon Behavior  index:11    from 2 To 1
        SetMemory(0x6566BC, Add, 65536),# weapons:Weapon Behavior  index:78    from 1 To 2
        SetMemory(0x6566E4, Add, -1),# weapons:Weapon Behavior  index:116    from 2 To 1
        SetMemory(0x6568EC, Add, -10),# weapons:Inner Splash Range  index:50    from 10 To 0
        SetMemory(0x6568EC, Add, -655360),# weapons:Inner Splash Range  index:51    from 10 To 0
        SetMemory(0x65712C, Add, -20),# weapons:Medium Splash Range  index:50    from 20 To 0
        SetMemory(0x65712C, Add, -1310720),# weapons:Medium Splash Range  index:51    from 20 To 0
        SetMemory(0x6577E4, Add, -30),# weapons:Outer Splash Range  index:50    from 30 To 0
        SetMemory(0x6577E4, Add, -1966080),# weapons:Outer Splash Range  index:51    from 30 To 0
        SetMemory(0x6564E8, Add, -1),# weapons:Damage Factor  index:8    from 2 To 1
        SetMemory(0x6564E8, Add, -65536),# weapons:Damage Factor  index:10    from 2 To 1
        SetMemory(0x6C9F0C, Add, 32),# flingy:Speed  index:5    from 1280 To 1312
        SetMemory(0x6C9FA0, Add, 32),# flingy:Speed  index:42    from 1280 To 1312
        SetMemory(0x6CA03C, Add, 32),# flingy:Speed  index:81    from 1280 To 1312
        SetMemory(0x6C9C80, Add, 4194304),# flingy:Acceleration  index:5    from 67 To 131
        SetMemory(0x6C9CCC, Add, 64),# flingy:Acceleration  index:42    from 67 To 131
        SetMemory(0x6C9D18, Add, 4194304),# flingy:Acceleration  index:81    from 67 To 131
        SetMemory(0x6C9944, Add, -12227),# flingy:Halt Distance  index:5    from 12227 To 0
        SetMemory(0x6C99D8, Add, -12227),# flingy:Halt Distance  index:42    from 12227 To 0
        SetMemory(0x6C9A74, Add, -12227),# flingy:Halt Distance  index:81    from 12227 To 0
        SetMemory(0x666398, Add, 65536),# sprites:Image File  index:285    from 358 To 359
        SetMemory(0x665CC8, Add, 0),# sprites:Is Visible  index:130    from 1 To 1
        SetMemory(0x669E28, Add, 15),# images:Draw Function  index:0    from 0 To 15
        SetMemory(0x66A04C, Add, 10),# images:Draw Function  index:548    from 0 To 10
        SetMemory(0x66A04C, Add, 2560),# images:Draw Function  index:549    from 0 To 10
        SetMemory(0x66A054, Add, 1),# images:Draw Function  index:556    from 9 To 10
        SetMemory(0x66A1E8, Add, 655360),# images:Draw Function  index:962    from 0 To 10
        SetMemory(0x655AFC, Add, 26),# upgrades:Icon  index:30    from 268 To 294
        SetMemory(0x655AFC, Add, 3997696),# upgrades:Icon  index:31    from 294 To 355
        SetMemory(0x655B00, Add, -24),# upgrades:Icon  index:32    from 295 To 271
        SetMemory(0x655B00, Add, -196608),# upgrades:Icon  index:33    from 281 To 278
    ])

