from eudplib import *


def onPluginStart():
    DoActions([  # Basic DatFile Actions
        SetMemory(0x6644F8, Add, -67),# units:Graphics  index:0    from 78 To 11
        SetMemory(0x6644F8, Add, -720896),# units:Graphics  index:2    from 88 To 77
        SetMemory(0x664500, Add, -11008),# units:Graphics  index:9    from 86 To 43
        SetMemory(0x664500, Add, 458752),# units:Graphics  index:10    from 73 To 80
        SetMemory(0x664504, Add, 7),# units:Graphics  index:12    from 70 To 77
        SetMemory(0x664508, Add, -234881024),# units:Graphics  index:19    from 88 To 74
        SetMemory(0x664518, Add, -36),# units:Graphics  index:32    from 73 To 37
        SetMemory(0x66451C, Add, 7680),# units:Graphics  index:37    from 15 To 45
        SetMemory(0x66451C, Add, 939524096),# units:Graphics  index:39    from 14 To 70
        SetMemory(0x664534, Add, -256),# units:Graphics  index:61    from 188 To 187
        SetMemory(0x664534, Add, -1828716544),# units:Graphics  index:63    from 187 To 78
        SetMemory(0x664538, Add, -2816),# units:Graphics  index:65    from 49 To 38
        SetMemory(0x664544, Add, 42),# units:Graphics  index:76    from 38 To 80
        SetMemory(0x664544, Add, -768),# units:Graphics  index:77    from 49 To 46
        SetMemory(0x664548, Add, -6),# units:Graphics  index:80    from 43 To 37
        SetMemory(0x66454C, Add, -33554432),# units:Graphics  index:87    from 45 To 43
        SetMemory(0x664550, Add, -6),# units:Graphics  index:88    from 43 To 37
        SetMemory(0x664550, Add, -4325376),# units:Graphics  index:90    from 116 To 50
        SetMemory(0x664554, Add, -49408),# units:Graphics  index:93    from 198 To 5
        SetMemory(0x664554, Add, -10289152),# units:Graphics  index:94    from 199 To 42
        SetMemory(0x664554, Add, -553648128),# units:Graphics  index:95    from 114 To 81
        SetMemory(0x664558, Add, 67108864),# units:Graphics  index:99    from 74 To 78
        SetMemory(0x66455C, Add, -31),# units:Graphics  index:100    from 74 To 43
        SetMemory(0x66455C, Add, 524288),# units:Graphics  index:102    from 70 To 78
        SetMemory(0x664560, Add, -31),# units:Graphics  index:104    from 74 To 43
        SetMemory(0x664564, Add, -6144),# units:Graphics  index:109    from 95 To 71
        SetMemory(0x664564, Add, -335544320),# units:Graphics  index:111    from 91 To 71
        SetMemory(0x664568, Add, -6656),# units:Graphics  index:113    from 97 To 71
        SetMemory(0x664568, Add, -6881280),# units:Graphics  index:114    from 110 To 5
        SetMemory(0x66456C, Add, -65),# units:Graphics  index:116    from 107 To 42
        SetMemory(0x664570, Add, -4521984),# units:Graphics  index:122    from 111 To 42
        SetMemory(0x664570, Add, -838860800),# units:Graphics  index:123    from 92 To 42
        SetMemory(0x664574, Add, 3072),# units:Graphics  index:125    from 104 To 116
        SetMemory(0x664574, Add, -2031616),# units:Graphics  index:126    from 102 To 71
        SetMemory(0x664574, Add, -469762048),# units:Graphics  index:127    from 99 To 71
        SetMemory(0x66457C, Add, 620756992),# units:Graphics  index:135    from 34 To 71
        SetMemory(0x664580, Add, -22),# units:Graphics  index:136    from 27 To 5
        SetMemory(0x664580, Add, -5376),# units:Graphics  index:137    from 26 To 5
        SetMemory(0x664580, Add, -1507328),# units:Graphics  index:138    from 28 To 5
        SetMemory(0x664580, Add, 855638016),# units:Graphics  index:139    from 20 To 71
        SetMemory(0x664584, Add, 39),# units:Graphics  index:140    from 32 To 71
        SetMemory(0x664584, Add, 3473408),# units:Graphics  index:142    from 18 To 71
        SetMemory(0x664588, Add, 687865856),# units:Graphics  index:147    from 30 To 71
        SetMemory(0x66458C, Add, 40),# units:Graphics  index:148    from 31 To 71
        SetMemory(0x66458C, Add, 922746880),# units:Graphics  index:151    from 16 To 71
        SetMemory(0x664590, Add, 55),# units:Graphics  index:152    from 16 To 71
        SetMemory(0x664590, Add, 786432),# units:Graphics  index:154    from 59 To 71
        SetMemory(0x664590, Add, 134217728),# units:Graphics  index:155    from 63 To 71
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
        SetMemory(0x661264, Add, -330),# units:Construction Animation  index:109    from 330 To 0
        SetMemory(0x66126C, Add, -325),# units:Construction Animation  index:111    from 325 To 0
        SetMemory(0x661274, Add, -327),# units:Construction Animation  index:113    from 327 To 0
        SetMemory(0x661278, Add, -325),# units:Construction Animation  index:114    from 325 To 0
        SetMemory(0x661280, Add, -327),# units:Construction Animation  index:116    from 327 To 0
        SetMemory(0x661298, Add, -327),# units:Construction Animation  index:122    from 327 To 0
        SetMemory(0x66129C, Add, -327),# units:Construction Animation  index:123    from 327 To 0
        SetMemory(0x6612A4, Add, -330),# units:Construction Animation  index:125    from 330 To 0
        SetMemory(0x6612A8, Add, -325),# units:Construction Animation  index:126    from 325 To 0
        SetMemory(0x6612AC, Add, -104),# units:Construction Animation  index:127    from 104 To 0
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
        SetMemory(0x660648, Add, -1048576),# units:Unit Direction  index:90    from 32 To 16
        SetMemory(0x66064C, Add, -4096),# units:Unit Direction  index:93    from 32 To 16
        SetMemory(0x66064C, Add, -1048576),# units:Unit Direction  index:94    from 32 To 16
        SetMemory(0x66064C, Add, -268435456),# units:Unit Direction  index:95    from 32 To 16
        SetMemory(0x660650, Add, -16),# units:Unit Direction  index:96    from 32 To 16
        SetMemory(0x66065C, Add, 8192),# units:Unit Direction  index:109    from 0 To 32
        SetMemory(0x66065C, Add, 536870912),# units:Unit Direction  index:111    from 0 To 32
        SetMemory(0x660660, Add, 8192),# units:Unit Direction  index:113    from 0 To 32
        SetMemory(0x660660, Add, 2097152),# units:Unit Direction  index:114    from 0 To 32
        SetMemory(0x660664, Add, 32),# units:Unit Direction  index:116    from 0 To 32
        SetMemory(0x660668, Add, 2097152),# units:Unit Direction  index:122    from 0 To 32
        SetMemory(0x660668, Add, 536870912),# units:Unit Direction  index:123    from 0 To 32
        SetMemory(0x66066C, Add, 8192),# units:Unit Direction  index:125    from 0 To 32
        SetMemory(0x66066C, Add, 2097152),# units:Unit Direction  index:126    from 0 To 32
        SetMemory(0x66066C, Add, 536870912),# units:Unit Direction  index:127    from 0 To 32
        SetMemory(0x660674, Add, 536870912),# units:Unit Direction  index:135    from 0 To 32
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
        SetMemory(0x660688, Add, 536870912),# units:Unit Direction  index:155    from 0 To 32
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
        SetMemory(0x6647B0, Add, 256),# units:Shield Enable  index:1    from 0 To 1
        SetMemory(0x6647B8, Add, 256),# units:Shield Enable  index:9    from 0 To 1
        SetMemory(0x6647B8, Add, 65536),# units:Shield Enable  index:10    from 0 To 1
        SetMemory(0x6647C0, Add, 16777216),# units:Shield Enable  index:19    from 0 To 1
        SetMemory(0x6647C8, Add, 16777216),# units:Shield Enable  index:27    from 0 To 1
        SetMemory(0x6647CC, Add, 1),# units:Shield Enable  index:28    from 0 To 1
        SetMemory(0x6647CC, Add, 256),# units:Shield Enable  index:29    from 0 To 1
        SetMemory(0x6647D0, Add, 1),# units:Shield Enable  index:32    from 0 To 1
        SetMemory(0x6647D8, Add, 1),# units:Shield Enable  index:40    from 0 To 1
        SetMemory(0x6647DC, Add, 65536),# units:Shield Enable  index:46    from 0 To 1
        SetMemory(0x6647E0, Add, 1),# units:Shield Enable  index:48    from 0 To 1
        SetMemory(0x6647E4, Add, 256),# units:Shield Enable  index:53    from 0 To 1
        SetMemory(0x6647EC, Add, -1),# units:Shield Enable  index:60    from 1 To 0
        SetMemory(0x6647EC, Add, -256),# units:Shield Enable  index:61    from 1 To 0
        SetMemory(0x6647EC, Add, 0),# units:Shield Enable  index:63    from 1 To 1
        SetMemory(0x6647F0, Add, -1),# units:Shield Enable  index:64    from 1 To 0
        SetMemory(0x6647F0, Add, 0),# units:Shield Enable  index:65    from 1 To 1
        SetMemory(0x6647F0, Add, -65536),# units:Shield Enable  index:66    from 1 To 0
        SetMemory(0x6647F0, Add, -16777216),# units:Shield Enable  index:67    from 1 To 0
        SetMemory(0x6647F4, Add, 0),# units:Shield Enable  index:68    from 1 To 1
        SetMemory(0x6647F4, Add, 0),# units:Shield Enable  index:70    from 1 To 1
        SetMemory(0x6647F4, Add, -16777216),# units:Shield Enable  index:71    from 1 To 0
        SetMemory(0x6647F8, Add, -65536),# units:Shield Enable  index:74    from 1 To 0
        SetMemory(0x6647F8, Add, 0),# units:Shield Enable  index:75    from 1 To 1
        SetMemory(0x6647FC, Add, -1),# units:Shield Enable  index:76    from 1 To 0
        SetMemory(0x6647FC, Add, -256),# units:Shield Enable  index:77    from 1 To 0
        SetMemory(0x6647FC, Add, -65536),# units:Shield Enable  index:78    from 1 To 0
        SetMemory(0x6647FC, Add, -16777216),# units:Shield Enable  index:79    from 1 To 0
        SetMemory(0x664800, Add, 0),# units:Shield Enable  index:80    from 1 To 1
        SetMemory(0x664804, Add, -16777216),# units:Shield Enable  index:87    from 1 To 0
        SetMemory(0x664808, Add, 0),# units:Shield Enable  index:88    from 1 To 1
        SetMemory(0x664810, Add, 16777216),# units:Shield Enable  index:99    from 0 To 1
        SetMemory(0x664814, Add, 65536),# units:Shield Enable  index:102    from 0 To 1
        SetMemory(0x664848, Add, -65536),# units:Shield Enable  index:154    from 1 To 0
        SetMemory(0x664848, Add, -16777216),# units:Shield Enable  index:155    from 1 To 0
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
        SetMemory(0x660E7C, Add, 19660800),# units:Shield Amount  index:63    from 200 To 500
        SetMemory(0x660EA0, Add, -300),# units:Shield Amount  index:80    from 400 To 100
        SetMemory(0x660EAC, Add, -13107200),# units:Shield Amount  index:87    from 300 To 100
        SetMemory(0x660EB0, Add, -150),# units:Shield Amount  index:88    from 250 To 100
        SetMemory(0x660F34, Add, -650),# units:Shield Amount  index:154    from 750 To 100
        SetMemory(0x660F34, Add, -26214400),# units:Shield Amount  index:155    from 500 To 100
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
        SetMemory(0x6623BC, Add, -38400),# units:Hit Points  index:27    from 256000 To 217600
        SetMemory(0x6623C4, Add, 38400),# units:Hit Points  index:29    from 179200 To 217600
        SetMemory(0x66244C, Add, 147200),# units:Hit Points  index:63    from 6400 To 153600
        SetMemory(0x6624AC, Add, 81920),# units:Hit Points  index:87    from 20480 To 102400
        SetMemory(0x6624B0, Add, 38400),# units:Hit Points  index:88    from 64000 To 102400
        SetMemory(0x6624DC, Add, 51200),# units:Hit Points  index:99    from 51200 To 102400
        SetMemory(0x6624E0, Add, 38400),# units:Hit Points  index:100    from 64000 To 102400
        SetMemory(0x6624E8, Add, -166400),# units:Hit Points  index:102    from 179200 To 12800
        SetMemory(0x6624F0, Add, -64000),# units:Hit Points  index:104    from 76800 To 12800
        SetMemory(0x662504, Add, -117760),# units:Hit Points  index:109    from 128000 To 10240
        SetMemory(0x66250C, Add, -245760),# units:Hit Points  index:111    from 256000 To 10240
        SetMemory(0x662514, Add, -309760),# units:Hit Points  index:113    from 320000 To 10240
        SetMemory(0x662518, Add, -322560),# units:Hit Points  index:114    from 332800 To 10240
        SetMemory(0x662520, Add, -207360),# units:Hit Points  index:116    from 217600 To 10240
        SetMemory(0x662538, Add, -207360),# units:Hit Points  index:122    from 217600 To 10240
        SetMemory(0x66253C, Add, -181760),# units:Hit Points  index:123    from 192000 To 10240
        SetMemory(0x662544, Add, -79360),# units:Hit Points  index:125    from 89600 To 10240
        SetMemory(0x662548, Add, -168960),# units:Hit Points  index:126    from 179200 To 10240
        SetMemory(0x66254C, Add, -501760),# units:Hit Points  index:127    from 512000 To 10240
        SetMemory(0x66256C, Add, -207360),# units:Hit Points  index:135    from 217600 To 10240
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
        SetMemory(0x6625BC, Add, -117760),# units:Hit Points  index:155    from 128000 To 10240
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
        SetMemory(0x663158, Add, -14),# units:Elevation Level  index:8    from 18 To 4
        SetMemory(0x663158, Add, -3072),# units:Elevation Level  index:9    from 16 To 4
        SetMemory(0x66315C, Add, -12),# units:Elevation Level  index:12    from 16 To 4
        SetMemory(0x663164, Add, -3584),# units:Elevation Level  index:21    from 18 To 4
        SetMemory(0x663168, Add, -201326592),# units:Elevation Level  index:27    from 16 To 4
        SetMemory(0x66316C, Add, -12),# units:Elevation Level  index:28    from 16 To 4
        SetMemory(0x66316C, Add, -3072),# units:Elevation Level  index:29    from 16 To 4
        SetMemory(0x663178, Add, -234881024),# units:Elevation Level  index:43    from 18 To 4
        SetMemory(0x66317C, Add, -14),# units:Elevation Level  index:44    from 18 To 4
        SetMemory(0x663184, Add, -234881024),# units:Elevation Level  index:55    from 18 To 4
        SetMemory(0x663188, Add, -14),# units:Elevation Level  index:56    from 18 To 4
        SetMemory(0x66318C, Add, -14),# units:Elevation Level  index:60    from 18 To 4
        SetMemory(0x663194, Add, -917504),# units:Elevation Level  index:70    from 18 To 4
        SetMemory(0x663194, Add, -201326592),# units:Elevation Level  index:71    from 16 To 4
        SetMemory(0x6631A0, Add, -14),# units:Elevation Level  index:80    from 18 To 4
        SetMemory(0x6631A8, Add, -14),# units:Elevation Level  index:88    from 18 To 4
        SetMemory(0x6631A8, Add, 917504),# units:Elevation Level  index:90    from 4 To 18
        SetMemory(0x6631AC, Add, 3584),# units:Elevation Level  index:93    from 4 To 18
        SetMemory(0x6631AC, Add, 0),# units:Elevation Level  index:94    from 18 To 18
        SetMemory(0x6631AC, Add, 234881024),# units:Elevation Level  index:95    from 4 To 18
        SetMemory(0x6631B0, Add, 14),# units:Elevation Level  index:96    from 4 To 18
        SetMemory(0x6631B4, Add, -786432),# units:Elevation Level  index:102    from 16 To 4
        SetMemory(0x6631CC, Add, 256),# units:Elevation Level  index:125    from 3 To 4
        SetMemory(0x6631DC, Add, 131072),# units:Elevation Level  index:142    from 2 To 4
        SetMemory(0x661004, Add, 67108864),# units:Unknown (old Movement)  index:63    from 193 To 197
        SetMemory(0x661018, Add, -132),# units:Unknown (old Movement)  index:80    from 197 To 65
        SetMemory(0x661020, Add, -132),# units:Unknown (old Movement)  index:88    from 197 To 65
        SetMemory(0x66102C, Add, -8650752),# units:Unknown (old Movement)  index:102    from 197 To 65
        SetMemory(0x661034, Add, 16640),# units:Unknown (old Movement)  index:109    from 0 To 65
        SetMemory(0x661034, Add, -2214592512),# units:Unknown (old Movement)  index:111    from 197 To 65
        SetMemory(0x661038, Add, -33792),# units:Unknown (old Movement)  index:113    from 197 To 65
        SetMemory(0x661038, Add, -8650752),# units:Unknown (old Movement)  index:114    from 197 To 65
        SetMemory(0x66103C, Add, -132),# units:Unknown (old Movement)  index:116    from 197 To 65
        SetMemory(0x661040, Add, -8650752),# units:Unknown (old Movement)  index:122    from 197 To 65
        SetMemory(0x661040, Add, 1090519040),# units:Unknown (old Movement)  index:123    from 0 To 65
        SetMemory(0x661044, Add, 16640),# units:Unknown (old Movement)  index:125    from 0 To 65
        SetMemory(0x661044, Add, 4259840),# units:Unknown (old Movement)  index:126    from 0 To 65
        SetMemory(0x661044, Add, 1090519040),# units:Unknown (old Movement)  index:127    from 0 To 65
        SetMemory(0x66104C, Add, 1090519040),# units:Unknown (old Movement)  index:135    from 0 To 65
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
        SetMemory(0x661060, Add, 1090519040),# units:Unknown (old Movement)  index:155    from 0 To 65
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
        SetMemory(0x663DD0, Add, -2),# units:Rank/Sublabel  index:0    from 2 To 0
        SetMemory(0x663DD0, Add, -1280),# units:Rank/Sublabel  index:1    from 5 To 0
        SetMemory(0x663DD0, Add, -393216),# units:Rank/Sublabel  index:2    from 6 To 0
        SetMemory(0x663DD8, Add, -10),# units:Rank/Sublabel  index:8    from 10 To 0
        SetMemory(0x663DD8, Add, -2816),# units:Rank/Sublabel  index:9    from 11 To 0
        SetMemory(0x663DD8, Add, -786432),# units:Rank/Sublabel  index:10    from 12 To 0
        SetMemory(0x663DDC, Add, -15),# units:Rank/Sublabel  index:12    from 15 To 0
        SetMemory(0x663DE0, Add, -18),# units:Rank/Sublabel  index:16    from 18 To 0
        SetMemory(0x663DE0, Add, -285212672),# units:Rank/Sublabel  index:19    from 17 To 0
        SetMemory(0x663DE4, Add, -17),# units:Rank/Sublabel  index:20    from 17 To 0
        SetMemory(0x663DE4, Add, -3584),# units:Rank/Sublabel  index:21    from 14 To 0
        SetMemory(0x663DE8, Add, -318767104),# units:Rank/Sublabel  index:27    from 21 To 2
        SetMemory(0x663DEC, Add, -20),# units:Rank/Sublabel  index:28    from 20 To 0
        SetMemory(0x663DEC, Add, -5120),# units:Rank/Sublabel  index:29    from 21 To 1
        SetMemory(0x663DF0, Add, -4),# units:Rank/Sublabel  index:32    from 4 To 0
        SetMemory(0x663DF4, Add, -1280),# units:Rank/Sublabel  index:37    from 5 To 0
        SetMemory(0x663DF4, Add, -589824),# units:Rank/Sublabel  index:38    from 9 To 0
        SetMemory(0x663DF4, Add, -218103808),# units:Rank/Sublabel  index:39    from 14 To 1
        SetMemory(0x663DF8, Add, -2),# units:Rank/Sublabel  index:40    from 3 To 1
        SetMemory(0x663DF8, Add, -150994944),# units:Rank/Sublabel  index:43    from 10 To 1
        SetMemory(0x663DFC, Add, -10),# units:Rank/Sublabel  index:44    from 11 To 1
        SetMemory(0x663DFC, Add, -720896),# units:Rank/Sublabel  index:46    from 12 To 1
        SetMemory(0x663E00, Add, -14),# units:Rank/Sublabel  index:48    from 15 To 1
        SetMemory(0x663E00, Add, -251658240),# units:Rank/Sublabel  index:51    from 16 To 1
        SetMemory(0x663E04, Add, -14),# units:Rank/Sublabel  index:52    from 15 To 1
        SetMemory(0x663E04, Add, -3584),# units:Rank/Sublabel  index:53    from 15 To 1
        SetMemory(0x663E04, Add, -917504),# units:Rank/Sublabel  index:54    from 15 To 1
        SetMemory(0x663E04, Add, -234881024),# units:Rank/Sublabel  index:55    from 15 To 1
        SetMemory(0x663E08, Add, -14),# units:Rank/Sublabel  index:56    from 15 To 1
        SetMemory(0x663E0C, Add, -7),# units:Rank/Sublabel  index:60    from 8 To 1
        SetMemory(0x663E0C, Add, -2560),# units:Rank/Sublabel  index:61    from 12 To 2
        SetMemory(0x663E0C, Add, -134217728),# units:Rank/Sublabel  index:63    from 9 To 1
        SetMemory(0x663E10, Add, -256),# units:Rank/Sublabel  index:65    from 3 To 2
        SetMemory(0x663E10, Add, -131072),# units:Rank/Sublabel  index:66    from 4 To 2
        SetMemory(0x663E10, Add, -67108864),# units:Rank/Sublabel  index:67    from 6 To 2
        SetMemory(0x663E14, Add, -7),# units:Rank/Sublabel  index:68    from 9 To 2
        SetMemory(0x663E14, Add, -393216),# units:Rank/Sublabel  index:70    from 8 To 2
        SetMemory(0x663E14, Add, -134217728),# units:Rank/Sublabel  index:71    from 10 To 2
        SetMemory(0x663E18, Add, -655360),# units:Rank/Sublabel  index:74    from 12 To 2
        SetMemory(0x663E18, Add, -218103808),# units:Rank/Sublabel  index:75    from 15 To 2
        SetMemory(0x663E1C, Add, -15),# units:Rank/Sublabel  index:76    from 17 To 2
        SetMemory(0x663E1C, Add, -2816),# units:Rank/Sublabel  index:77    from 13 To 2
        SetMemory(0x663E1C, Add, -786432),# units:Rank/Sublabel  index:78    from 14 To 2
        SetMemory(0x663E1C, Add, -234881024),# units:Rank/Sublabel  index:79    from 16 To 2
        SetMemory(0x663E20, Add, -11),# units:Rank/Sublabel  index:80    from 12 To 1
        SetMemory(0x663E24, Add, -251658240),# units:Rank/Sublabel  index:87    from 16 To 1
        SetMemory(0x663E28, Add, -10),# units:Rank/Sublabel  index:88    from 12 To 2
        SetMemory(0x663E30, Add, -268435456),# units:Rank/Sublabel  index:99    from 18 To 2
        SetMemory(0x663E34, Add, -20),# units:Rank/Sublabel  index:100    from 22 To 2
        SetMemory(0x663E38, Add, -15),# units:Rank/Sublabel  index:104    from 15 To 0
        SetMemory(0x663E3C, Add, 768),# units:Rank/Sublabel  index:109    from 0 To 3
        SetMemory(0x663E3C, Add, 50331648),# units:Rank/Sublabel  index:111    from 0 To 3
        SetMemory(0x663E40, Add, 768),# units:Rank/Sublabel  index:113    from 0 To 3
        SetMemory(0x663E40, Add, 4390912),# units:Rank/Sublabel  index:114    from 0 To 67
        SetMemory(0x663E44, Add, 13),# units:Rank/Sublabel  index:116    from 0 To 13
        SetMemory(0x663E48, Add, 851968),# units:Rank/Sublabel  index:122    from 0 To 13
        SetMemory(0x663E48, Add, 218103808),# units:Rank/Sublabel  index:123    from 0 To 13
        SetMemory(0x663E4C, Add, 3072),# units:Rank/Sublabel  index:125    from 0 To 12
        SetMemory(0x663E4C, Add, 983040),# units:Rank/Sublabel  index:126    from 0 To 15
        SetMemory(0x663E4C, Add, 251658240),# units:Rank/Sublabel  index:127    from 0 To 15
        SetMemory(0x663E54, Add, 251658240),# units:Rank/Sublabel  index:135    from 0 To 15
        SetMemory(0x663E58, Add, 14),# units:Rank/Sublabel  index:136    from 0 To 14
        SetMemory(0x663E58, Add, 3584),# units:Rank/Sublabel  index:137    from 0 To 14
        SetMemory(0x663E58, Add, 917504),# units:Rank/Sublabel  index:138    from 0 To 14
        SetMemory(0x663E58, Add, 83886080),# units:Rank/Sublabel  index:139    from 0 To 5
        SetMemory(0x663E5C, Add, 5),# units:Rank/Sublabel  index:140    from 0 To 5
        SetMemory(0x663E5C, Add, 327680),# units:Rank/Sublabel  index:142    from 0 To 5
        SetMemory(0x663E60, Add, 83886080),# units:Rank/Sublabel  index:147    from 0 To 5
        SetMemory(0x663E64, Add, 5),# units:Rank/Sublabel  index:148    from 0 To 5
        SetMemory(0x663E64, Add, 83886080),# units:Rank/Sublabel  index:151    from 0 To 5
        SetMemory(0x663E68, Add, 5),# units:Rank/Sublabel  index:152    from 0 To 5
        SetMemory(0x663E68, Add, 327680),# units:Rank/Sublabel  index:154    from 0 To 5
        SetMemory(0x663E68, Add, 83886080),# units:Rank/Sublabel  index:155    from 0 To 5
        SetMemory(0x663E6C, Add, 83886080),# units:Rank/Sublabel  index:159    from 0 To 5
        SetMemory(0x663E70, Add, 5),# units:Rank/Sublabel  index:160    from 0 To 5
        SetMemory(0x663E70, Add, 83886080),# units:Rank/Sublabel  index:163    from 0 To 5
        SetMemory(0x663E74, Add, 11),# units:Rank/Sublabel  index:164    from 0 To 11
        SetMemory(0x663E74, Add, 17920),# units:Rank/Sublabel  index:165    from 0 To 70
        SetMemory(0x663E74, Add, 4521984),# units:Rank/Sublabel  index:166    from 0 To 69
        SetMemory(0x663E74, Add, 1140850688),# units:Rank/Sublabel  index:167    from 0 To 68
        SetMemory(0x663E78, Add, 11),# units:Rank/Sublabel  index:168    from 0 To 11
        SetMemory(0x663E78, Add, 2560),# units:Rank/Sublabel  index:169    from 0 To 10
        SetMemory(0x663E78, Add, 524288),# units:Rank/Sublabel  index:170    from 0 To 8
        SetMemory(0x663E78, Add, 117440512),# units:Rank/Sublabel  index:171    from 0 To 7
        SetMemory(0x663E7C, Add, 9),# units:Rank/Sublabel  index:172    from 0 To 9
        SetMemory(0x663E7C, Add, 1280),# units:Rank/Sublabel  index:173    from 0 To 5
        SetMemory(0x663E7C, Add, 262144),# units:Rank/Sublabel  index:174    from 0 To 4
        SetMemory(0x663E7C, Add, 100663296),# units:Rank/Sublabel  index:175    from 0 To 6
        SetMemory(0x662EA0, Add, 105),# units:Comp AI Idle  index:0    from 2 To 107
        SetMemory(0x662EA0, Add, 26880),# units:Comp AI Idle  index:1    from 2 To 107
        SetMemory(0x662EA0, Add, 6881280),# units:Comp AI Idle  index:2    from 2 To 107
        SetMemory(0x662EA8, Add, 105),# units:Comp AI Idle  index:8    from 2 To 107
        SetMemory(0x662EA8, Add, 26880),# units:Comp AI Idle  index:9    from 2 To 107
        SetMemory(0x662EA8, Add, 6881280),# units:Comp AI Idle  index:10    from 2 To 107
        SetMemory(0x662EAC, Add, 105),# units:Comp AI Idle  index:12    from 2 To 107
        SetMemory(0x662EB0, Add, 105),# units:Comp AI Idle  index:16    from 2 To 107
        SetMemory(0x662EB0, Add, 1761607680),# units:Comp AI Idle  index:19    from 2 To 107
        SetMemory(0x662EB4, Add, 105),# units:Comp AI Idle  index:20    from 2 To 107
        SetMemory(0x662EB4, Add, 26880),# units:Comp AI Idle  index:21    from 2 To 107
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
        SetMemory(0x662EDC, Add, 105),# units:Comp AI Idle  index:60    from 2 To 107
        SetMemory(0x662EDC, Add, 26880),# units:Comp AI Idle  index:61    from 2 To 107
        SetMemory(0x662EDC, Add, 1761607680),# units:Comp AI Idle  index:63    from 2 To 107
        SetMemory(0x662EE0, Add, 26880),# units:Comp AI Idle  index:65    from 2 To 107
        SetMemory(0x662EE0, Add, 6881280),# units:Comp AI Idle  index:66    from 2 To 107
        SetMemory(0x662EE0, Add, 1761607680),# units:Comp AI Idle  index:67    from 2 To 107
        SetMemory(0x662EE4, Add, 105),# units:Comp AI Idle  index:68    from 2 To 107
        SetMemory(0x662EE4, Add, 6881280),# units:Comp AI Idle  index:70    from 2 To 107
        SetMemory(0x662EE4, Add, -385875968),# units:Comp AI Idle  index:71    from 130 To 107
        SetMemory(0x662EE8, Add, 6881280),# units:Comp AI Idle  index:74    from 2 To 107
        SetMemory(0x662EE8, Add, 1761607680),# units:Comp AI Idle  index:75    from 2 To 107
        SetMemory(0x662EEC, Add, 105),# units:Comp AI Idle  index:76    from 2 To 107
        SetMemory(0x662EEC, Add, 26880),# units:Comp AI Idle  index:77    from 2 To 107
        SetMemory(0x662EEC, Add, 6881280),# units:Comp AI Idle  index:78    from 2 To 107
        SetMemory(0x662EEC, Add, 1761607680),# units:Comp AI Idle  index:79    from 2 To 107
        SetMemory(0x662EF0, Add, 105),# units:Comp AI Idle  index:80    from 2 To 107
        SetMemory(0x662EF4, Add, 1761607680),# units:Comp AI Idle  index:87    from 2 To 107
        SetMemory(0x662EF8, Add, 105),# units:Comp AI Idle  index:88    from 2 To 107
        SetMemory(0x662F00, Add, 1761607680),# units:Comp AI Idle  index:99    from 2 To 107
        SetMemory(0x662F04, Add, 105),# units:Comp AI Idle  index:100    from 2 To 107
        SetMemory(0x662F04, Add, 6881280),# units:Comp AI Idle  index:102    from 2 To 107
        SetMemory(0x662F08, Add, 105),# units:Comp AI Idle  index:104    from 2 To 107
        SetMemory(0x662F0C, Add, -39424),# units:Comp AI Idle  index:109    from 156 To 2
        SetMemory(0x662F0C, Add, -2583691264),# units:Comp AI Idle  index:111    from 156 To 2
        SetMemory(0x662F10, Add, -39424),# units:Comp AI Idle  index:113    from 156 To 2
        SetMemory(0x662F10, Add, -10092544),# units:Comp AI Idle  index:114    from 156 To 2
        SetMemory(0x662F14, Add, -154),# units:Comp AI Idle  index:116    from 156 To 2
        SetMemory(0x662F18, Add, -10092544),# units:Comp AI Idle  index:122    from 156 To 2
        SetMemory(0x662F18, Add, -2583691264),# units:Comp AI Idle  index:123    from 156 To 2
        SetMemory(0x662F1C, Add, -39424),# units:Comp AI Idle  index:125    from 156 To 2
        SetMemory(0x662F1C, Add, -10092544),# units:Comp AI Idle  index:126    from 156 To 2
        SetMemory(0x662F1C, Add, -2583691264),# units:Comp AI Idle  index:127    from 156 To 2
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
        SetMemory(0x662F38, Add, -2583691264),# units:Comp AI Idle  index:155    from 156 To 2
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
        SetMemory(0x662270, Add, 105),# units:Human AI Idle  index:8    from 2 To 107
        SetMemory(0x662270, Add, 26880),# units:Human AI Idle  index:9    from 2 To 107
        SetMemory(0x662270, Add, 6881280),# units:Human AI Idle  index:10    from 2 To 107
        SetMemory(0x662274, Add, 105),# units:Human AI Idle  index:12    from 2 To 107
        SetMemory(0x662278, Add, 105),# units:Human AI Idle  index:16    from 2 To 107
        SetMemory(0x662278, Add, 1761607680),# units:Human AI Idle  index:19    from 2 To 107
        SetMemory(0x66227C, Add, 105),# units:Human AI Idle  index:20    from 2 To 107
        SetMemory(0x66227C, Add, 26880),# units:Human AI Idle  index:21    from 2 To 107
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
        SetMemory(0x6622A4, Add, 105),# units:Human AI Idle  index:60    from 2 To 107
        SetMemory(0x6622A4, Add, 26880),# units:Human AI Idle  index:61    from 2 To 107
        SetMemory(0x6622A4, Add, 1761607680),# units:Human AI Idle  index:63    from 2 To 107
        SetMemory(0x6622A8, Add, 26880),# units:Human AI Idle  index:65    from 2 To 107
        SetMemory(0x6622A8, Add, 6881280),# units:Human AI Idle  index:66    from 2 To 107
        SetMemory(0x6622A8, Add, 1761607680),# units:Human AI Idle  index:67    from 2 To 107
        SetMemory(0x6622AC, Add, 105),# units:Human AI Idle  index:68    from 2 To 107
        SetMemory(0x6622AC, Add, 6881280),# units:Human AI Idle  index:70    from 2 To 107
        SetMemory(0x6622AC, Add, -385875968),# units:Human AI Idle  index:71    from 130 To 107
        SetMemory(0x6622B0, Add, 6881280),# units:Human AI Idle  index:74    from 2 To 107
        SetMemory(0x6622B0, Add, 1761607680),# units:Human AI Idle  index:75    from 2 To 107
        SetMemory(0x6622B4, Add, 105),# units:Human AI Idle  index:76    from 2 To 107
        SetMemory(0x6622B4, Add, 26880),# units:Human AI Idle  index:77    from 2 To 107
        SetMemory(0x6622B4, Add, 6881280),# units:Human AI Idle  index:78    from 2 To 107
        SetMemory(0x6622B4, Add, 1761607680),# units:Human AI Idle  index:79    from 2 To 107
        SetMemory(0x6622B8, Add, 105),# units:Human AI Idle  index:80    from 2 To 107
        SetMemory(0x6622BC, Add, 1761607680),# units:Human AI Idle  index:87    from 2 To 107
        SetMemory(0x6622C0, Add, 105),# units:Human AI Idle  index:88    from 2 To 107
        SetMemory(0x6622C0, Add, -10747904),# units:Human AI Idle  index:90    from 166 To 2
        SetMemory(0x6622C4, Add, -41984),# units:Human AI Idle  index:93    from 166 To 2
        SetMemory(0x6622C4, Add, -10747904),# units:Human AI Idle  index:94    from 166 To 2
        SetMemory(0x6622C4, Add, -2751463424),# units:Human AI Idle  index:95    from 166 To 2
        SetMemory(0x6622C8, Add, -164),# units:Human AI Idle  index:96    from 166 To 2
        SetMemory(0x6622C8, Add, 1761607680),# units:Human AI Idle  index:99    from 2 To 107
        SetMemory(0x6622CC, Add, 105),# units:Human AI Idle  index:100    from 2 To 107
        SetMemory(0x6622CC, Add, 6881280),# units:Human AI Idle  index:102    from 2 To 107
        SetMemory(0x6622D0, Add, 105),# units:Human AI Idle  index:104    from 2 To 107
        SetMemory(0x6622D4, Add, -5376),# units:Human AI Idle  index:109    from 23 To 2
        SetMemory(0x6622D4, Add, -352321536),# units:Human AI Idle  index:111    from 23 To 2
        SetMemory(0x6622D8, Add, -5376),# units:Human AI Idle  index:113    from 23 To 2
        SetMemory(0x6622D8, Add, -1376256),# units:Human AI Idle  index:114    from 23 To 2
        SetMemory(0x6622DC, Add, -21),# units:Human AI Idle  index:116    from 23 To 2
        SetMemory(0x6622E0, Add, -1376256),# units:Human AI Idle  index:122    from 23 To 2
        SetMemory(0x6622E0, Add, -352321536),# units:Human AI Idle  index:123    from 23 To 2
        SetMemory(0x6622E4, Add, -5376),# units:Human AI Idle  index:125    from 23 To 2
        SetMemory(0x6622E4, Add, -1376256),# units:Human AI Idle  index:126    from 23 To 2
        SetMemory(0x6622E4, Add, -352321536),# units:Human AI Idle  index:127    from 23 To 2
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
        SetMemory(0x662300, Add, -352321536),# units:Human AI Idle  index:155    from 23 To 2
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
        SetMemory(0x6648A0, Add, 105),# units:Return to Idle  index:8    from 2 To 107
        SetMemory(0x6648A0, Add, 26880),# units:Return to Idle  index:9    from 2 To 107
        SetMemory(0x6648A0, Add, 6881280),# units:Return to Idle  index:10    from 2 To 107
        SetMemory(0x6648A4, Add, 105),# units:Return to Idle  index:12    from 2 To 107
        SetMemory(0x6648A8, Add, 105),# units:Return to Idle  index:16    from 2 To 107
        SetMemory(0x6648A8, Add, 1761607680),# units:Return to Idle  index:19    from 2 To 107
        SetMemory(0x6648AC, Add, 105),# units:Return to Idle  index:20    from 2 To 107
        SetMemory(0x6648AC, Add, 26880),# units:Return to Idle  index:21    from 2 To 107
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
        SetMemory(0x6648D4, Add, 105),# units:Return to Idle  index:60    from 2 To 107
        SetMemory(0x6648D4, Add, 26880),# units:Return to Idle  index:61    from 2 To 107
        SetMemory(0x6648D8, Add, 26880),# units:Return to Idle  index:65    from 2 To 107
        SetMemory(0x6648D8, Add, 6881280),# units:Return to Idle  index:66    from 2 To 107
        SetMemory(0x6648D8, Add, 1761607680),# units:Return to Idle  index:67    from 2 To 107
        SetMemory(0x6648DC, Add, 105),# units:Return to Idle  index:68    from 2 To 107
        SetMemory(0x6648DC, Add, 6881280),# units:Return to Idle  index:70    from 2 To 107
        SetMemory(0x6648DC, Add, 1761607680),# units:Return to Idle  index:71    from 2 To 107
        SetMemory(0x6648E0, Add, 6881280),# units:Return to Idle  index:74    from 2 To 107
        SetMemory(0x6648E0, Add, 1761607680),# units:Return to Idle  index:75    from 2 To 107
        SetMemory(0x6648E4, Add, 105),# units:Return to Idle  index:76    from 2 To 107
        SetMemory(0x6648E4, Add, 26880),# units:Return to Idle  index:77    from 2 To 107
        SetMemory(0x6648E4, Add, 6881280),# units:Return to Idle  index:78    from 2 To 107
        SetMemory(0x6648E4, Add, 1761607680),# units:Return to Idle  index:79    from 2 To 107
        SetMemory(0x6648E8, Add, 105),# units:Return to Idle  index:80    from 2 To 107
        SetMemory(0x6648EC, Add, 1761607680),# units:Return to Idle  index:87    from 2 To 107
        SetMemory(0x6648F0, Add, 105),# units:Return to Idle  index:88    from 2 To 107
        SetMemory(0x6648F0, Add, -10747904),# units:Return to Idle  index:90    from 166 To 2
        SetMemory(0x6648F4, Add, -41984),# units:Return to Idle  index:93    from 166 To 2
        SetMemory(0x6648F4, Add, -10747904),# units:Return to Idle  index:94    from 166 To 2
        SetMemory(0x6648F4, Add, -2751463424),# units:Return to Idle  index:95    from 166 To 2
        SetMemory(0x6648F8, Add, -164),# units:Return to Idle  index:96    from 166 To 2
        SetMemory(0x6648F8, Add, 1761607680),# units:Return to Idle  index:99    from 2 To 107
        SetMemory(0x6648FC, Add, 105),# units:Return to Idle  index:100    from 2 To 107
        SetMemory(0x6648FC, Add, 6881280),# units:Return to Idle  index:102    from 2 To 107
        SetMemory(0x664900, Add, 105),# units:Return to Idle  index:104    from 2 To 107
        SetMemory(0x664904, Add, -5376),# units:Return to Idle  index:109    from 23 To 2
        SetMemory(0x664904, Add, -352321536),# units:Return to Idle  index:111    from 23 To 2
        SetMemory(0x664908, Add, -5376),# units:Return to Idle  index:113    from 23 To 2
        SetMemory(0x664908, Add, -1376256),# units:Return to Idle  index:114    from 23 To 2
        SetMemory(0x66490C, Add, -21),# units:Return to Idle  index:116    from 23 To 2
        SetMemory(0x664910, Add, -1376256),# units:Return to Idle  index:122    from 23 To 2
        SetMemory(0x664910, Add, -352321536),# units:Return to Idle  index:123    from 23 To 2
        SetMemory(0x664914, Add, -5376),# units:Return to Idle  index:125    from 23 To 2
        SetMemory(0x664914, Add, -1376256),# units:Return to Idle  index:126    from 23 To 2
        SetMemory(0x664914, Add, -352321536),# units:Return to Idle  index:127    from 23 To 2
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
        SetMemory(0x664930, Add, -352321536),# units:Return to Idle  index:155    from 23 To 2
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
        SetMemory(0x66335C, Add, -184549376),# units:Attack Unit  index:63    from 21 To 10
        SetMemory(0x663378, Add, -10813440),# units:Attack Unit  index:90    from 188 To 23
        SetMemory(0x66337C, Add, -42240),# units:Attack Unit  index:93    from 188 To 23
        SetMemory(0x66337C, Add, -10813440),# units:Attack Unit  index:94    from 188 To 23
        SetMemory(0x66337C, Add, -2768240640),# units:Attack Unit  index:95    from 188 To 23
        SetMemory(0x663380, Add, -165),# units:Attack Unit  index:96    from 188 To 23
        SetMemory(0x6633A8, Add, 0),# units:Attack Unit  index:139    from 23 To 23
        SetMemory(0x6633AC, Add, 0),# units:Attack Unit  index:140    from 23 To 23
        SetMemory(0x6633AC, Add, 0),# units:Attack Unit  index:142    from 23 To 23
        SetMemory(0x6633B0, Add, 0),# units:Attack Unit  index:147    from 23 To 23
        SetMemory(0x6633B4, Add, 0),# units:Attack Unit  index:148    from 23 To 23
        SetMemory(0x6633B4, Add, 0),# units:Attack Unit  index:151    from 23 To 23
        SetMemory(0x6633B8, Add, 0),# units:Attack Unit  index:152    from 23 To 23
        SetMemory(0x6633B8, Add, 0),# units:Attack Unit  index:154    from 23 To 23
        SetMemory(0x6633B8, Add, 0),# units:Attack Unit  index:155    from 23 To 23
        SetMemory(0x6633BC, Add, 0),# units:Attack Unit  index:159    from 23 To 23
        SetMemory(0x6633C0, Add, 0),# units:Attack Unit  index:160    from 23 To 23
        SetMemory(0x6633C0, Add, 0),# units:Attack Unit  index:163    from 23 To 23
        SetMemory(0x6633C4, Add, 0),# units:Attack Unit  index:164    from 23 To 23
        SetMemory(0x6633C4, Add, 0),# units:Attack Unit  index:165    from 23 To 23
        SetMemory(0x6633C4, Add, 0),# units:Attack Unit  index:166    from 23 To 23
        SetMemory(0x6633C4, Add, 0),# units:Attack Unit  index:167    from 23 To 23
        SetMemory(0x6633C8, Add, 0),# units:Attack Unit  index:168    from 23 To 23
        SetMemory(0x6633C8, Add, 0),# units:Attack Unit  index:169    from 23 To 23
        SetMemory(0x6633C8, Add, 0),# units:Attack Unit  index:170    from 23 To 23
        SetMemory(0x6633C8, Add, 0),# units:Attack Unit  index:171    from 23 To 23
        SetMemory(0x6633CC, Add, 0),# units:Attack Unit  index:172    from 23 To 23
        SetMemory(0x6633CC, Add, 0),# units:Attack Unit  index:173    from 23 To 23
        SetMemory(0x6633CC, Add, 0),# units:Attack Unit  index:174    from 23 To 23
        SetMemory(0x6633CC, Add, 0),# units:Attack Unit  index:175    from 23 To 23
        SetMemory(0x663A58, Add, 0),# units:Attack Move  index:10    from 2 To 2
        SetMemory(0x663AA8, Add, -12189696),# units:Attack Move  index:90    from 188 To 2
        SetMemory(0x663AAC, Add, -47616),# units:Attack Move  index:93    from 188 To 2
        SetMemory(0x663AAC, Add, -12189696),# units:Attack Move  index:94    from 188 To 2
        SetMemory(0x663AAC, Add, -3120562176),# units:Attack Move  index:95    from 188 To 2
        SetMemory(0x663AB0, Add, -186),# units:Attack Move  index:96    from 188 To 2
        SetMemory(0x663ABC, Add, -5376),# units:Attack Move  index:109    from 23 To 2
        SetMemory(0x663ABC, Add, -352321536),# units:Attack Move  index:111    from 23 To 2
        SetMemory(0x663AC0, Add, -5376),# units:Attack Move  index:113    from 23 To 2
        SetMemory(0x663AC0, Add, -1376256),# units:Attack Move  index:114    from 23 To 2
        SetMemory(0x663AC4, Add, -21),# units:Attack Move  index:116    from 23 To 2
        SetMemory(0x663AC8, Add, -1376256),# units:Attack Move  index:122    from 23 To 2
        SetMemory(0x663AC8, Add, -352321536),# units:Attack Move  index:123    from 23 To 2
        SetMemory(0x663ACC, Add, -5376),# units:Attack Move  index:125    from 23 To 2
        SetMemory(0x663ACC, Add, -1376256),# units:Attack Move  index:126    from 23 To 2
        SetMemory(0x663ACC, Add, -352321536),# units:Attack Move  index:127    from 23 To 2
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
        SetMemory(0x663AE8, Add, -352321536),# units:Attack Move  index:155    from 23 To 2
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
        SetMemory(0x6636B8, Add, 0),# units:Ground Weapon  index:0    from 0 To 0
        SetMemory(0x6636B8, Add, -256),# units:Ground Weapon  index:1    from 2 To 1
        SetMemory(0x6636B8, Add, -131072),# units:Ground Weapon  index:2    from 4 To 2
        SetMemory(0x6636C0, Add, -13),# units:Ground Weapon  index:8    from 16 To 3
        SetMemory(0x6636C0, Add, -32256),# units:Ground Weapon  index:9    from 130 To 4
        SetMemory(0x6636C0, Add, -1376256),# units:Ground Weapon  index:10    from 26 To 5
        SetMemory(0x6636C4, Add, -12),# units:Ground Weapon  index:12    from 19 To 7
        SetMemory(0x6636C8, Add, 6),# units:Ground Weapon  index:16    from 3 To 9
        SetMemory(0x6636C8, Add, 100663296),# units:Ground Weapon  index:19    from 5 To 11
        SetMemory(0x6636CC, Add, 11),# units:Ground Weapon  index:20    from 1 To 12
        SetMemory(0x6636CC, Add, -512),# units:Ground Weapon  index:21    from 18 To 16
        SetMemory(0x6636D0, Add, -184549376),# units:Ground Weapon  index:27    from 21 To 10
        SetMemory(0x6636D4, Add, -15),# units:Ground Weapon  index:28    from 23 To 8
        SetMemory(0x6636D4, Add, -1024),# units:Ground Weapon  index:29    from 21 To 17
        SetMemory(0x6636D8, Add, 18),# units:Ground Weapon  index:32    from 25 To 43
        SetMemory(0x6636DC, Add, -4352),# units:Ground Weapon  index:37    from 35 To 18
        SetMemory(0x6636DC, Add, -1245184),# units:Ground Weapon  index:38    from 38 To 19
        SetMemory(0x6636DC, Add, -335544320),# units:Ground Weapon  index:39    from 40 To 20
        SetMemory(0x6636E0, Add, -21),# units:Ground Weapon  index:40    from 42 To 21
        SetMemory(0x6636E0, Add, -436207616),# units:Ground Weapon  index:43    from 48 To 22
        SetMemory(0x6636E4, Add, -23),# units:Ground Weapon  index:44    from 46 To 23
        SetMemory(0x6636E4, Add, -6946816),# units:Ground Weapon  index:46    from 130 To 24
        SetMemory(0x6636E8, Add, -16),# units:Ground Weapon  index:48    from 41 To 25
        SetMemory(0x6636E8, Add, -184549376),# units:Ground Weapon  index:51    from 37 To 26
        SetMemory(0x6636EC, Add, -103),# units:Ground Weapon  index:52    from 130 To 27
        SetMemory(0x6636EC, Add, -2816),# units:Ground Weapon  index:53    from 39 To 28
        SetMemory(0x6636EC, Add, -458752),# units:Ground Weapon  index:54    from 36 To 29
        SetMemory(0x6636EC, Add, -234881024),# units:Ground Weapon  index:55    from 49 To 35
        SetMemory(0x6636F0, Add, -11),# units:Ground Weapon  index:56    from 47 To 36
        SetMemory(0x6636F4, Add, -93),# units:Ground Weapon  index:60    from 130 To 37
        SetMemory(0x6636F4, Add, -18688),# units:Ground Weapon  index:61    from 111 To 38
        SetMemory(0x6636F4, Add, -1056964608),# units:Ground Weapon  index:63    from 130 To 67
        SetMemory(0x6636F8, Add, -6400),# units:Ground Weapon  index:65    from 64 To 39
        SetMemory(0x6636F8, Add, -1703936),# units:Ground Weapon  index:66    from 66 To 40
        SetMemory(0x6636F8, Add, -1493172224),# units:Ground Weapon  index:67    from 130 To 41
        SetMemory(0x6636FC, Add, -28),# units:Ground Weapon  index:68    from 70 To 42
        SetMemory(0x6636FC, Add, -1769472),# units:Ground Weapon  index:70    from 73 To 46
        SetMemory(0x6636FC, Add, -503316480),# units:Ground Weapon  index:71    from 77 To 47
        SetMemory(0x663700, Add, -2490368),# units:Ground Weapon  index:74    from 86 To 48
        SetMemory(0x663700, Add, -603979776),# units:Ground Weapon  index:75    from 85 To 49
        SetMemory(0x663704, Add, -21),# units:Ground Weapon  index:76    from 71 To 50
        SetMemory(0x663704, Add, -3584),# units:Ground Weapon  index:77    from 65 To 51
        SetMemory(0x663704, Add, -983040),# units:Ground Weapon  index:78    from 67 To 52
        SetMemory(0x663704, Add, -268435456),# units:Ground Weapon  index:79    from 69 To 53
        SetMemory(0x663708, Add, -9),# units:Ground Weapon  index:80    from 75 To 66
        SetMemory(0x66370C, Add, -16777216),# units:Ground Weapon  index:87    from 69 To 68
        SetMemory(0x663710, Add, -45),# units:Ground Weapon  index:88    from 114 To 69
        SetMemory(0x663718, Add, -704643072),# units:Ground Weapon  index:99    from 112 To 70
        SetMemory(0x66371C, Add, -45),# units:Ground Weapon  index:100    from 116 To 71
        SetMemory(0x66371C, Add, 1507328),# units:Ground Weapon  index:102    from 21 To 44
        SetMemory(0x663720, Add, -98),# units:Ground Weapon  index:104    from 113 To 15
        SetMemory(0x6645E0, Add, 0),# units:Max Ground Hits  index:0    from 1 To 1
        SetMemory(0x6645E0, Add, 0),# units:Max Ground Hits  index:1    from 1 To 1
        SetMemory(0x6645E0, Add, 0),# units:Max Ground Hits  index:2    from 1 To 1
        SetMemory(0x6645E8, Add, 0),# units:Max Ground Hits  index:8    from 1 To 1
        SetMemory(0x6645E8, Add, 256),# units:Max Ground Hits  index:9    from 0 To 1
        SetMemory(0x6645E8, Add, -131072),# units:Max Ground Hits  index:10    from 3 To 1
        SetMemory(0x6645EC, Add, 0),# units:Max Ground Hits  index:12    from 1 To 1
        SetMemory(0x6645F0, Add, 0),# units:Max Ground Hits  index:16    from 1 To 1
        SetMemory(0x6645F0, Add, 0),# units:Max Ground Hits  index:19    from 1 To 1
        SetMemory(0x6645F4, Add, 0),# units:Max Ground Hits  index:20    from 1 To 1
        SetMemory(0x6645F4, Add, 0),# units:Max Ground Hits  index:21    from 1 To 1
        SetMemory(0x664600, Add, -2),# units:Max Ground Hits  index:32    from 3 To 1
        SetMemory(0x664604, Add, 0),# units:Max Ground Hits  index:37    from 1 To 1
        SetMemory(0x664604, Add, 0),# units:Max Ground Hits  index:38    from 1 To 1
        SetMemory(0x664604, Add, 0),# units:Max Ground Hits  index:39    from 1 To 1
        SetMemory(0x66460C, Add, 65536),# units:Max Ground Hits  index:46    from 0 To 1
        SetMemory(0x664614, Add, 1),# units:Max Ground Hits  index:52    from 0 To 1
        SetMemory(0x66461C, Add, 1),# units:Max Ground Hits  index:60    from 0 To 1
        SetMemory(0x66461C, Add, 16777216),# units:Max Ground Hits  index:63    from 0 To 1
        SetMemory(0x664620, Add, -256),# units:Max Ground Hits  index:65    from 2 To 1
        SetMemory(0x664620, Add, 16777216),# units:Max Ground Hits  index:67    from 0 To 1
        SetMemory(0x66462C, Add, -256),# units:Max Ground Hits  index:77    from 2 To 1
        SetMemory(0x6616E0, Add, 130),# units:Air Weapon  index:0    from 0 To 130
        SetMemory(0x6616E0, Add, 32768),# units:Air Weapon  index:1    from 2 To 130
        SetMemory(0x6616E0, Add, 0),# units:Air Weapon  index:2    from 130 To 130
        SetMemory(0x6616E8, Add, 115),# units:Air Weapon  index:8    from 15 To 130
        SetMemory(0x6616E8, Add, 0),# units:Air Weapon  index:9    from 130 To 130
        SetMemory(0x6616E8, Add, 0),# units:Air Weapon  index:10    from 130 To 130
        SetMemory(0x6616EC, Add, 110),# units:Air Weapon  index:12    from 20 To 130
        SetMemory(0x6616F0, Add, 127),# units:Air Weapon  index:16    from 3 To 130
        SetMemory(0x6616F0, Add, 0),# units:Air Weapon  index:19    from 130 To 130
        SetMemory(0x6616F4, Add, 129),# units:Air Weapon  index:20    from 1 To 130
        SetMemory(0x6616F4, Add, 28928),# units:Air Weapon  index:21    from 17 To 130
        SetMemory(0x6616F8, Add, 1811939328),# units:Air Weapon  index:27    from 22 To 130
        SetMemory(0x6616FC, Add, 106),# units:Air Weapon  index:28    from 24 To 130
        SetMemory(0x6616FC, Add, 27648),# units:Air Weapon  index:29    from 22 To 130
        SetMemory(0x661704, Add, 0),# units:Air Weapon  index:37    from 130 To 130
        SetMemory(0x661704, Add, 6029312),# units:Air Weapon  index:38    from 38 To 130
        SetMemory(0x661704, Add, 0),# units:Air Weapon  index:39    from 130 To 130
        SetMemory(0x661708, Add, 0),# units:Air Weapon  index:40    from 130 To 130
        SetMemory(0x661708, Add, 1375731712),# units:Air Weapon  index:43    from 48 To 130
        SetMemory(0x66170C, Add, 0),# units:Air Weapon  index:44    from 130 To 130
        SetMemory(0x66170C, Add, 0),# units:Air Weapon  index:46    from 130 To 130
        SetMemory(0x661710, Add, 0),# units:Air Weapon  index:48    from 130 To 130
        SetMemory(0x661710, Add, 0),# units:Air Weapon  index:51    from 130 To 130
        SetMemory(0x661714, Add, 0),# units:Air Weapon  index:52    from 130 To 130
        SetMemory(0x661714, Add, 23296),# units:Air Weapon  index:53    from 39 To 130
        SetMemory(0x661714, Add, 0),# units:Air Weapon  index:54    from 130 To 130
        SetMemory(0x661714, Add, 1358954496),# units:Air Weapon  index:55    from 49 To 130
        SetMemory(0x661718, Add, 0),# units:Air Weapon  index:56    from 130 To 130
        SetMemory(0x66171C, Add, 30),# units:Air Weapon  index:60    from 100 To 130
        SetMemory(0x66171C, Add, 0),# units:Air Weapon  index:61    from 130 To 130
        SetMemory(0x661720, Add, 0),# units:Air Weapon  index:65    from 130 To 130
        SetMemory(0x661720, Add, 4194304),# units:Air Weapon  index:66    from 66 To 130
        SetMemory(0x661720, Add, 0),# units:Air Weapon  index:67    from 130 To 130
        SetMemory(0x661724, Add, 60),# units:Air Weapon  index:68    from 70 To 130
        SetMemory(0x661724, Add, 3670016),# units:Air Weapon  index:70    from 74 To 130
        SetMemory(0x661724, Add, 889192448),# units:Air Weapon  index:71    from 77 To 130
        SetMemory(0x661728, Add, 0),# units:Air Weapon  index:74    from 130 To 130
        SetMemory(0x661728, Add, 0),# units:Air Weapon  index:75    from 130 To 130
        SetMemory(0x66172C, Add, 59),# units:Air Weapon  index:76    from 71 To 130
        SetMemory(0x66172C, Add, 0),# units:Air Weapon  index:77    from 130 To 130
        SetMemory(0x66172C, Add, 4128768),# units:Air Weapon  index:78    from 67 To 130
        SetMemory(0x66172C, Add, 0),# units:Air Weapon  index:79    from 130 To 130
        SetMemory(0x661730, Add, 54),# units:Air Weapon  index:80    from 76 To 130
        SetMemory(0x661738, Add, 15),# units:Air Weapon  index:88    from 115 To 130
        SetMemory(0x661740, Add, 301989888),# units:Air Weapon  index:99    from 112 To 130
        SetMemory(0x661744, Add, 14),# units:Air Weapon  index:100    from 116 To 130
        SetMemory(0x661744, Add, 7077888),# units:Air Weapon  index:102    from 22 To 130
        SetMemory(0x661748, Add, 17),# units:Air Weapon  index:104    from 113 To 130
        SetMemory(0x65FC18, Add, -1),# units:Max Air Hits  index:0    from 1 To 0
        SetMemory(0x65FC18, Add, -256),# units:Max Air Hits  index:1    from 1 To 0
        SetMemory(0x65FC18, Add, 0),# units:Max Air Hits  index:2    from 0 To 0
        SetMemory(0x65FC20, Add, -1),# units:Max Air Hits  index:8    from 1 To 0
        SetMemory(0x65FC20, Add, 0),# units:Max Air Hits  index:9    from 0 To 0
        SetMemory(0x65FC20, Add, 0),# units:Max Air Hits  index:10    from 0 To 0
        SetMemory(0x65FC24, Add, -1),# units:Max Air Hits  index:12    from 1 To 0
        SetMemory(0x65FC28, Add, -1),# units:Max Air Hits  index:16    from 1 To 0
        SetMemory(0x65FC28, Add, 0),# units:Max Air Hits  index:19    from 0 To 0
        SetMemory(0x65FC2C, Add, -1),# units:Max Air Hits  index:20    from 1 To 0
        SetMemory(0x65FC2C, Add, -256),# units:Max Air Hits  index:21    from 1 To 0
        SetMemory(0x65FC30, Add, -16777216),# units:Max Air Hits  index:27    from 1 To 0
        SetMemory(0x65FC34, Add, -1),# units:Max Air Hits  index:28    from 1 To 0
        SetMemory(0x65FC34, Add, -256),# units:Max Air Hits  index:29    from 1 To 0
        SetMemory(0x65FC3C, Add, 0),# units:Max Air Hits  index:37    from 0 To 0
        SetMemory(0x65FC3C, Add, -65536),# units:Max Air Hits  index:38    from 1 To 0
        SetMemory(0x65FC3C, Add, 0),# units:Max Air Hits  index:39    from 0 To 0
        SetMemory(0x65FC40, Add, -16777216),# units:Max Air Hits  index:43    from 1 To 0
        SetMemory(0x65FC4C, Add, -256),# units:Max Air Hits  index:53    from 1 To 0
        SetMemory(0x65FC4C, Add, -16777216),# units:Max Air Hits  index:55    from 1 To 0
        SetMemory(0x65FC54, Add, -1),# units:Max Air Hits  index:60    from 1 To 0
        SetMemory(0x65FC58, Add, -65536),# units:Max Air Hits  index:66    from 1 To 0
        SetMemory(0x65FC5C, Add, -1),# units:Max Air Hits  index:68    from 1 To 0
        SetMemory(0x65FC5C, Add, -65536),# units:Max Air Hits  index:70    from 1 To 0
        SetMemory(0x65FC5C, Add, -16777216),# units:Max Air Hits  index:71    from 1 To 0
        SetMemory(0x65FC64, Add, -1),# units:Max Air Hits  index:76    from 1 To 0
        SetMemory(0x65FC64, Add, -65536),# units:Max Air Hits  index:78    from 1 To 0
        SetMemory(0x65FC68, Add, -1),# units:Max Air Hits  index:80    from 1 To 0
        SetMemory(0x65FC70, Add, -1),# units:Max Air Hits  index:88    from 1 To 0
        SetMemory(0x65FC78, Add, -16777216),# units:Max Air Hits  index:99    from 1 To 0
        SetMemory(0x65FC7C, Add, -1),# units:Max Air Hits  index:100    from 1 To 0
        SetMemory(0x65FC7C, Add, -65536),# units:Max Air Hits  index:102    from 1 To 0
        SetMemory(0x65FC80, Add, -1),# units:Max Air Hits  index:104    from 1 To 0
        SetMemory(0x6601B4, Add, 50331648),# units:AI Internal  index:63    from 0 To 3
        SetMemory(0x6601DC, Add, -196608),# units:AI Internal  index:102    from 3 To 0
        SetMemory(0x6601E0, Add, -3),# units:AI Internal  index:104    from 3 To 0
        SetMemory(0x6601E4, Add, -768),# units:AI Internal  index:109    from 3 To 0
        SetMemory(0x6601E4, Add, -50331648),# units:AI Internal  index:111    from 3 To 0
        SetMemory(0x6601E8, Add, -768),# units:AI Internal  index:113    from 3 To 0
        SetMemory(0x6601E8, Add, -196608),# units:AI Internal  index:114    from 3 To 0
        SetMemory(0x6601EC, Add, -3),# units:AI Internal  index:116    from 3 To 0
        SetMemory(0x6601F0, Add, -196608),# units:AI Internal  index:122    from 3 To 0
        SetMemory(0x6601F0, Add, -50331648),# units:AI Internal  index:123    from 3 To 0
        SetMemory(0x6601F4, Add, -768),# units:AI Internal  index:125    from 3 To 0
        SetMemory(0x6601F4, Add, -196608),# units:AI Internal  index:126    from 3 To 0
        SetMemory(0x6601F4, Add, -50331648),# units:AI Internal  index:127    from 3 To 0
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
        SetMemory(0x660210, Add, -50331648),# units:AI Internal  index:155    from 3 To 0
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
        SetMemory(0x6640A0, Add, -1109393924),# units:Special Ability Flags  index:8    from 1512047108 To 402653184
        SetMemory(0x6640A4, Add, -1109426372),# units:Special Ability Flags  index:9    from 1512079620 To 402653248
        SetMemory(0x6640A8, Add, -65536),# units:Special Ability Flags  index:10    from 402718784 To 402653248
        SetMemory(0x6640B0, Add, -1142947844),# units:Special Ability Flags  index:12    from 1545601028 To 402653184
        SetMemory(0x6640C0, Add, -2163200),# units:Special Ability Flags  index:16    from 404816448 To 402653248
        SetMemory(0x6640CC, Add, -1073741888),# units:Special Ability Flags  index:19    from 1476395072 To 402653184
        SetMemory(0x6640D0, Add, -65600),# units:Special Ability Flags  index:20    from 402718784 To 402653184
        SetMemory(0x6640D4, Add, -1109393988),# units:Special Ability Flags  index:21    from 1512047172 To 402653184
        SetMemory(0x6640EC, Add, -1142947844),# units:Special Ability Flags  index:27    from 1545601092 To 402653248
        SetMemory(0x6640F0, Add, -1142947844),# units:Special Ability Flags  index:28    from 1545601092 To 402653248
        SetMemory(0x6640F4, Add, -1142947844),# units:Special Ability Flags  index:29    from 1545601092 To 402653248
        SetMemory(0x664100, Add, -65472),# units:Special Ability Flags  index:32    from 402718720 To 402653248
        SetMemory(0x664114, Add, -1115264),# units:Special Ability Flags  index:37    from 403768448 To 402653184
        SetMemory(0x664118, Add, -1114240),# units:Special Ability Flags  index:38    from 403767424 To 402653184
        SetMemory(0x66411C, Add, -67174528),# units:Special Ability Flags  index:39    from 469827712 To 402653184
        SetMemory(0x664120, Add, -65664),# units:Special Ability Flags  index:40    from 402718848 To 402653184
        SetMemory(0x66412C, Add, -33620100),# units:Special Ability Flags  index:43    from 436273284 To 402653184
        SetMemory(0x664130, Add, -83951748),# units:Special Ability Flags  index:44    from 486604932 To 402653184
        SetMemory(0x664138, Add, -36765824),# units:Special Ability Flags  index:46    from 439419008 To 402653184
        SetMemory(0x664140, Add, -67174592),# units:Special Ability Flags  index:48    from 469827776 To 402653184
        SetMemory(0x66414C, Add, -2163392),# units:Special Ability Flags  index:51    from 404816576 To 402653184
        SetMemory(0x664150, Add, -36765888),# units:Special Ability Flags  index:52    from 439419072 To 402653184
        SetMemory(0x664154, Add, -1114304),# units:Special Ability Flags  index:53    from 403767488 To 402653184
        SetMemory(0x664158, Add, -1115328),# units:Special Ability Flags  index:54    from 403768512 To 402653184
        SetMemory(0x66415C, Add, -33620164),# units:Special Ability Flags  index:55    from 436273348 To 402653184
        SetMemory(0x664160, Add, -83951812),# units:Special Ability Flags  index:56    from 486604996 To 402653184
        SetMemory(0x664170, Add, -1109393412),# units:Special Ability Flags  index:60    from 1512046596 To 402653184
        SetMemory(0x664174, Add, -4259840),# units:Special Ability Flags  index:61    from 406913024 To 402653184
        SetMemory(0x66417C, Add, 1038090048),# units:Special Ability Flags  index:63    from 471859456 To 1509949504
        SetMemory(0x664184, Add, -65536),# units:Special Ability Flags  index:65    from 402718720 To 402653184
        SetMemory(0x664188, Add, -1107296256),# units:Special Ability Flags  index:66    from 1509949440 To 402653184
        SetMemory(0x66418C, Add, -2162688),# units:Special Ability Flags  index:67    from 404815872 To 402653184
        SetMemory(0x664190, Add, -67109120),# units:Special Ability Flags  index:68    from 469762304 To 402653184
        SetMemory(0x664198, Add, -1107296260),# units:Special Ability Flags  index:70    from 1509949444 To 402653184
        SetMemory(0x66419C, Add, -1109393412),# units:Special Ability Flags  index:71    from 1512046596 To 402653184
        SetMemory(0x6641A8, Add, -4259840),# units:Special Ability Flags  index:74    from 406913024 To 402653184
        SetMemory(0x6641AC, Add, -4259904),# units:Special Ability Flags  index:75    from 406913088 To 402653184
        SetMemory(0x6641B0, Add, -67109184),# units:Special Ability Flags  index:76    from 469762368 To 402653184
        SetMemory(0x6641B4, Add, -65600),# units:Special Ability Flags  index:77    from 402718784 To 402653184
        SetMemory(0x6641B8, Add, -1107296320),# units:Special Ability Flags  index:78    from 1509949504 To 402653184
        SetMemory(0x6641BC, Add, -2162752),# units:Special Ability Flags  index:79    from 404815936 To 402653184
        SetMemory(0x6641C0, Add, -1107296260),# units:Special Ability Flags  index:80    from 1509949508 To 402653248
        SetMemory(0x6641DC, Add, -2162688),# units:Special Ability Flags  index:87    from 404815936 To 402653248
        SetMemory(0x6641E0, Add, -1107296260),# units:Special Ability Flags  index:88    from 1509949508 To 402653248
        SetMemory(0x6641E8, Add, -65536),# units:Special Ability Flags  index:90    from 402718720 To 402653184
        SetMemory(0x6641F4, Add, -65536),# units:Special Ability Flags  index:93    from 402718720 To 402653184
        SetMemory(0x6641F8, Add, -65540),# units:Special Ability Flags  index:94    from 402718724 To 402653184
        SetMemory(0x6641FC, Add, -65536),# units:Special Ability Flags  index:95    from 402718720 To 402653184
        SetMemory(0x664200, Add, -65536),# units:Special Ability Flags  index:96    from 402718720 To 402653184
        SetMemory(0x66420C, Add, -2163200),# units:Special Ability Flags  index:99    from 404816448 To 402653248
        SetMemory(0x664210, Add, -2163200),# units:Special Ability Flags  index:100    from 404816448 To 402653248
        SetMemory(0x664218, Add, -1142947844),# units:Special Ability Flags  index:102    from 1545601092 To 402653248
        SetMemory(0x664220, Add, -2163328),# units:Special Ability Flags  index:104    from 404816576 To 402653248
        SetMemory(0x664234, Add, -201326593),# units:Special Ability Flags  index:109    from 1140850689 To 939524096
        SetMemory(0x66423C, Add, -2348810273),# units:Special Ability Flags  index:111    from 3288334369 To 939524096
        SetMemory(0x664244, Add, -2348810273),# units:Special Ability Flags  index:113    from 3288334369 To 939524096
        SetMemory(0x664248, Add, -738197537),# units:Special Ability Flags  index:114    from 1140850721 To 402653184
        SetMemory(0x664250, Add, -738197537),# units:Special Ability Flags  index:116    from 1140850721 To 402653184
        SetMemory(0x664268, Add, -738197537),# units:Special Ability Flags  index:122    from 1140850721 To 402653184
        SetMemory(0x66426C, Add, -738197505),# units:Special Ability Flags  index:123    from 1140850689 To 402653184
        SetMemory(0x664274, Add, -2885681153),# units:Special Ability Flags  index:125    from 3288334337 To 402653184
        SetMemory(0x664278, Add, -738197505),# units:Special Ability Flags  index:126    from 1140850689 To 402653184
        SetMemory(0x66427C, Add, -738197505),# units:Special Ability Flags  index:127    from 1140850689 To 402653184
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
        SetMemory(0x6642EC, Add, -2886205441),# units:Special Ability Flags  index:155    from 3288858625 To 402653184
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
        SetMemory(0x662DB8, Add, 0),# units:Target Acquisition Range  index:0    from 4 To 4
        SetMemory(0x662DF4, Add, -33554432),# units:Target Acquisition Range  index:63    from 7 To 5
        SetMemory(0x662E08, Add, -1),# units:Target Acquisition Range  index:80    from 4 To 3
        SetMemory(0x662E10, Add, -1),# units:Target Acquisition Range  index:88    from 4 To 3
        SetMemory(0x662E18, Add, -50331648),# units:Target Acquisition Range  index:99    from 6 To 3
        SetMemory(0x662E1C, Add, -3),# units:Target Acquisition Range  index:100    from 6 To 3
        SetMemory(0x662E1C, Add, -196608),# units:Target Acquisition Range  index:102    from 6 To 3
        SetMemory(0x662E20, Add, -3),# units:Target Acquisition Range  index:104    from 6 To 3
        SetMemory(0x663250, Add, 50331648),# units:Sight Range  index:27    from 8 To 11
        SetMemory(0x663274, Add, -16777216),# units:Sight Range  index:63    from 10 To 9
        SetMemory(0x663288, Add, -1),# units:Sight Range  index:80    from 10 To 9
        SetMemory(0x66328C, Add, 33554432),# units:Sight Range  index:87    from 7 To 9
        SetMemory(0x663290, Add, -1),# units:Sight Range  index:88    from 10 To 9
        SetMemory(0x663298, Add, -16777216),# units:Sight Range  index:99    from 10 To 9
        SetMemory(0x66329C, Add, -2),# units:Sight Range  index:100    from 11 To 9
        SetMemory(0x66329C, Add, -262144),# units:Sight Range  index:102    from 11 To 7
        SetMemory(0x6632A0, Add, -4),# units:Sight Range  index:104    from 11 To 7
        SetMemory(0x6632A4, Add, -256),# units:Sight Range  index:109    from 8 To 7
        SetMemory(0x6632A4, Add, -16777216),# units:Sight Range  index:111    from 8 To 7
        SetMemory(0x6632A8, Add, -256),# units:Sight Range  index:113    from 8 To 7
        SetMemory(0x6632A8, Add, -196608),# units:Sight Range  index:114    from 10 To 7
        SetMemory(0x6632AC, Add, -3),# units:Sight Range  index:116    from 10 To 7
        SetMemory(0x6632B0, Add, -65536),# units:Sight Range  index:122    from 8 To 7
        SetMemory(0x6632B0, Add, -16777216),# units:Sight Range  index:123    from 8 To 7
        SetMemory(0x6632B4, Add, -768),# units:Sight Range  index:125    from 10 To 7
        SetMemory(0x6632B4, Add, -196608),# units:Sight Range  index:126    from 10 To 7
        SetMemory(0x6632B4, Add, -16777216),# units:Sight Range  index:127    from 8 To 7
        SetMemory(0x6632BC, Add, -16777216),# units:Sight Range  index:135    from 8 To 7
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
        SetMemory(0x6632D0, Add, -50331648),# units:Sight Range  index:155    from 10 To 7
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
        SetMemory(0x6635D0, Add, 2),# units:Armor Upgrade  index:0    from 0 To 2
        SetMemory(0x6635D0, Add, 512),# units:Armor Upgrade  index:1    from 0 To 2
        SetMemory(0x6635D0, Add, 65536),# units:Armor Upgrade  index:2    from 1 To 2
        SetMemory(0x6635D8, Add, 131072),# units:Armor Upgrade  index:10    from 0 To 2
        SetMemory(0x6635E0, Add, 2),# units:Armor Upgrade  index:16    from 0 To 2
        SetMemory(0x6635E0, Add, 16777216),# units:Armor Upgrade  index:19    from 1 To 2
        SetMemory(0x6635E4, Add, 2),# units:Armor Upgrade  index:20    from 0 To 2
        SetMemory(0x6635E4, Add, 0),# units:Armor Upgrade  index:21    from 2 To 2
        SetMemory(0x6635F0, Add, 2),# units:Armor Upgrade  index:32    from 0 To 2
        SetMemory(0x6635F0, Add, 3932160),# units:Armor Upgrade  index:34    from 0 To 60
        SetMemory(0x6635F4, Add, -256),# units:Armor Upgrade  index:37    from 3 To 2
        SetMemory(0x6635F4, Add, -65536),# units:Armor Upgrade  index:38    from 3 To 2
        SetMemory(0x6635F4, Add, -33554432),# units:Armor Upgrade  index:39    from 3 To 1
        SetMemory(0x6635F8, Add, -2),# units:Armor Upgrade  index:40    from 3 To 1
        SetMemory(0x6635F8, Add, -50331648),# units:Armor Upgrade  index:43    from 4 To 1
        SetMemory(0x6635FC, Add, -3),# units:Armor Upgrade  index:44    from 4 To 1
        SetMemory(0x6635FC, Add, -131072),# units:Armor Upgrade  index:46    from 3 To 1
        SetMemory(0x663600, Add, -2),# units:Armor Upgrade  index:48    from 3 To 1
        SetMemory(0x663600, Add, -33554432),# units:Armor Upgrade  index:51    from 3 To 1
        SetMemory(0x663604, Add, -2),# units:Armor Upgrade  index:52    from 3 To 1
        SetMemory(0x663604, Add, -512),# units:Armor Upgrade  index:53    from 3 To 1
        SetMemory(0x663604, Add, -131072),# units:Armor Upgrade  index:54    from 3 To 1
        SetMemory(0x663604, Add, -50331648),# units:Armor Upgrade  index:55    from 4 To 1
        SetMemory(0x663608, Add, -3),# units:Armor Upgrade  index:56    from 4 To 1
        SetMemory(0x66360C, Add, -5),# units:Armor Upgrade  index:60    from 6 To 1
        SetMemory(0x66360C, Add, -1280),# units:Armor Upgrade  index:61    from 5 To 0
        SetMemory(0x66360C, Add, -67108864),# units:Armor Upgrade  index:63    from 5 To 1
        SetMemory(0x663610, Add, -1280),# units:Armor Upgrade  index:65    from 5 To 0
        SetMemory(0x663610, Add, -327680),# units:Armor Upgrade  index:66    from 5 To 0
        SetMemory(0x663610, Add, -83886080),# units:Armor Upgrade  index:67    from 5 To 0
        SetMemory(0x663614, Add, -5),# units:Armor Upgrade  index:68    from 5 To 0
        SetMemory(0x663614, Add, -393216),# units:Armor Upgrade  index:70    from 6 To 0
        SetMemory(0x663614, Add, -100663296),# units:Armor Upgrade  index:71    from 6 To 0
        SetMemory(0x663618, Add, -327680),# units:Armor Upgrade  index:74    from 5 To 0
        SetMemory(0x663618, Add, -83886080),# units:Armor Upgrade  index:75    from 5 To 0
        SetMemory(0x66361C, Add, -5),# units:Armor Upgrade  index:76    from 5 To 0
        SetMemory(0x66361C, Add, -1280),# units:Armor Upgrade  index:77    from 5 To 0
        SetMemory(0x66361C, Add, -327680),# units:Armor Upgrade  index:78    from 5 To 0
        SetMemory(0x66361C, Add, -83886080),# units:Armor Upgrade  index:79    from 5 To 0
        SetMemory(0x663620, Add, -5),# units:Armor Upgrade  index:80    from 6 To 1
        SetMemory(0x663624, Add, -67108864),# units:Armor Upgrade  index:87    from 5 To 1
        SetMemory(0x663628, Add, -6),# units:Armor Upgrade  index:88    from 6 To 0
        SetMemory(0x663628, Add, 0),# units:Armor Upgrade  index:90    from 60 To 60
        SetMemory(0x66362C, Add, -7680),# units:Armor Upgrade  index:93    from 60 To 30
        SetMemory(0x66362C, Add, -1900544),# units:Armor Upgrade  index:94    from 60 To 31
        SetMemory(0x66362C, Add, -469762048),# units:Armor Upgrade  index:95    from 60 To 32
        SetMemory(0x663630, Add, -27),# units:Armor Upgrade  index:96    from 60 To 33
        SetMemory(0x663638, Add, -1),# units:Armor Upgrade  index:104    from 3 To 2
        SetMemory(0x66363C, Add, 0),# units:Armor Upgrade  index:109    from 60 To 60
        SetMemory(0x66363C, Add, 0),# units:Armor Upgrade  index:111    from 60 To 60
        SetMemory(0x663640, Add, 0),# units:Armor Upgrade  index:113    from 60 To 60
        SetMemory(0x66364C, Add, 0),# units:Armor Upgrade  index:125    from 60 To 60
        SetMemory(0x663658, Add, 0),# units:Armor Upgrade  index:138    from 60 To 60
        SetMemory(0x663658, Add, -520093696),# units:Armor Upgrade  index:139    from 60 To 29
        SetMemory(0x66365C, Add, -32),# units:Armor Upgrade  index:140    from 60 To 28
        SetMemory(0x66365C, Add, -2162688),# units:Armor Upgrade  index:142    from 60 To 27
        SetMemory(0x663660, Add, -570425344),# units:Armor Upgrade  index:147    from 60 To 26
        SetMemory(0x663664, Add, -35),# units:Armor Upgrade  index:148    from 60 To 25
        SetMemory(0x663664, Add, -603979776),# units:Armor Upgrade  index:151    from 60 To 24
        SetMemory(0x663668, Add, -37),# units:Armor Upgrade  index:152    from 60 To 23
        SetMemory(0x663668, Add, -2490368),# units:Armor Upgrade  index:154    from 60 To 22
        SetMemory(0x663668, Add, -654311424),# units:Armor Upgrade  index:155    from 60 To 21
        SetMemory(0x66366C, Add, -671088640),# units:Armor Upgrade  index:159    from 60 To 20
        SetMemory(0x663670, Add, -41),# units:Armor Upgrade  index:160    from 60 To 19
        SetMemory(0x663670, Add, -704643072),# units:Armor Upgrade  index:163    from 60 To 18
        SetMemory(0x663674, Add, -43),# units:Armor Upgrade  index:164    from 60 To 17
        SetMemory(0x663674, Add, -11264),# units:Armor Upgrade  index:165    from 60 To 16
        SetMemory(0x663674, Add, -1703936),# units:Armor Upgrade  index:166    from 60 To 34
        SetMemory(0x663674, Add, -771751936),# units:Armor Upgrade  index:167    from 60 To 14
        SetMemory(0x663678, Add, -47),# units:Armor Upgrade  index:168    from 60 To 13
        SetMemory(0x663678, Add, -12288),# units:Armor Upgrade  index:169    from 60 To 12
        SetMemory(0x663678, Add, -3211264),# units:Armor Upgrade  index:170    from 60 To 11
        SetMemory(0x663678, Add, -838860800),# units:Armor Upgrade  index:171    from 60 To 10
        SetMemory(0x66367C, Add, -51),# units:Armor Upgrade  index:172    from 60 To 9
        SetMemory(0x66367C, Add, -13312),# units:Armor Upgrade  index:173    from 60 To 8
        SetMemory(0x66367C, Add, -3473408),# units:Armor Upgrade  index:174    from 60 To 7
        SetMemory(0x66367C, Add, -905969664),# units:Armor Upgrade  index:175    from 60 To 6
        SetMemory(0x6621D0, Add, -2),# units:Unit Size  index:80    from 3 To 1
        SetMemory(0x6621D8, Add, -2),# units:Unit Size  index:88    from 3 To 1
        SetMemory(0x6621DC, Add, 65536),# units:Unit Size  index:94    from 1 To 2
        SetMemory(0x6621DC, Add, 33554432),# units:Unit Size  index:95    from 1 To 3
        SetMemory(0x6621E0, Add, -1),# units:Unit Size  index:96    from 1 To 0
        SetMemory(0x6621E4, Add, -131072),# units:Unit Size  index:102    from 3 To 1
        SetMemory(0x6621EC, Add, -512),# units:Unit Size  index:109    from 3 To 1
        SetMemory(0x6621EC, Add, -33554432),# units:Unit Size  index:111    from 3 To 1
        SetMemory(0x6621F0, Add, -512),# units:Unit Size  index:113    from 3 To 1
        SetMemory(0x6621F0, Add, -131072),# units:Unit Size  index:114    from 3 To 1
        SetMemory(0x6621F4, Add, -2),# units:Unit Size  index:116    from 3 To 1
        SetMemory(0x6621F8, Add, -131072),# units:Unit Size  index:122    from 3 To 1
        SetMemory(0x6621F8, Add, -33554432),# units:Unit Size  index:123    from 3 To 1
        SetMemory(0x6621FC, Add, -512),# units:Unit Size  index:125    from 3 To 1
        SetMemory(0x6621FC, Add, -131072),# units:Unit Size  index:126    from 3 To 1
        SetMemory(0x6621FC, Add, -33554432),# units:Unit Size  index:127    from 3 To 1
        SetMemory(0x662204, Add, -33554432),# units:Unit Size  index:135    from 3 To 1
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
        SetMemory(0x662218, Add, -33554432),# units:Unit Size  index:155    from 3 To 1
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
        SetMemory(0x65FED0, Add, -256),# units:Armor  index:9    from 1 To 0
        SetMemory(0x65FED0, Add, -196608),# units:Armor  index:10    from 3 To 0
        SetMemory(0x65FED4, Add, -3),# units:Armor  index:12    from 3 To 0
        SetMemory(0x65FED8, Add, -3),# units:Armor  index:16    from 3 To 0
        SetMemory(0x65FED8, Add, -50331648),# units:Armor  index:19    from 3 To 0
        SetMemory(0x65FEDC, Add, -3),# units:Armor  index:20    from 3 To 0
        SetMemory(0x65FEDC, Add, -1024),# units:Armor  index:21    from 4 To 0
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
        SetMemory(0x65FF04, Add, -1),# units:Armor  index:60    from 1 To 0
        SetMemory(0x65FF04, Add, -256),# units:Armor  index:61    from 1 To 0
        SetMemory(0x65FF04, Add, 33554432),# units:Armor  index:63    from 1 To 3
        SetMemory(0x65FF08, Add, -256),# units:Armor  index:65    from 1 To 0
        SetMemory(0x65FF08, Add, -65536),# units:Armor  index:66    from 1 To 0
        SetMemory(0x65FF0C, Add, -16777216),# units:Armor  index:71    from 1 To 0
        SetMemory(0x65FF14, Add, -3),# units:Armor  index:76    from 3 To 0
        SetMemory(0x65FF14, Add, -512),# units:Armor  index:77    from 2 To 0
        SetMemory(0x65FF14, Add, -196608),# units:Armor  index:78    from 3 To 0
        SetMemory(0x65FF14, Add, -33554432),# units:Armor  index:79    from 2 To 0
        SetMemory(0x65FF18, Add, -3),# units:Armor  index:80    from 3 To 0
        SetMemory(0x65FF1C, Add, -33554432),# units:Armor  index:87    from 2 To 0
        SetMemory(0x65FF20, Add, -3),# units:Armor  index:88    from 3 To 0
        SetMemory(0x65FF28, Add, -33554432),# units:Armor  index:99    from 2 To 0
        SetMemory(0x65FF2C, Add, -3),# units:Armor  index:100    from 3 To 0
        SetMemory(0x65FF2C, Add, -196608),# units:Armor  index:102    from 4 To 1
        SetMemory(0x65FF30, Add, -2),# units:Armor  index:104    from 3 To 1
        SetMemory(0x65FF34, Add, -256),# units:Armor  index:109    from 1 To 0
        SetMemory(0x65FF34, Add, -16777216),# units:Armor  index:111    from 1 To 0
        SetMemory(0x65FF38, Add, -256),# units:Armor  index:113    from 1 To 0
        SetMemory(0x65FF38, Add, -65536),# units:Armor  index:114    from 1 To 0
        SetMemory(0x65FF3C, Add, -1),# units:Armor  index:116    from 1 To 0
        SetMemory(0x65FF40, Add, -65536),# units:Armor  index:122    from 1 To 0
        SetMemory(0x65FF40, Add, -16777216),# units:Armor  index:123    from 1 To 0
        SetMemory(0x65FF44, Add, -256),# units:Armor  index:125    from 1 To 0
        SetMemory(0x65FF44, Add, -65536),# units:Armor  index:126    from 1 To 0
        SetMemory(0x65FF44, Add, -16777216),# units:Armor  index:127    from 1 To 0
        SetMemory(0x65FF4C, Add, -16777216),# units:Armor  index:135    from 1 To 0
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
        SetMemory(0x65FF60, Add, -16777216),# units:Armor  index:155    from 1 To 0
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
        SetMemory(0x6620A0, Add, -256),# units:Right-click Action  index:9    from 2 To 1
        SetMemory(0x6620D4, Add, -16777216),# units:Right-click Action  index:63    from 2 To 1
        SetMemory(0x662104, Add, 512),# units:Right-click Action  index:109    from 0 To 2
        SetMemory(0x662110, Add, 33554432),# units:Right-click Action  index:123    from 0 To 2
        SetMemory(0x662114, Add, 512),# units:Right-click Action  index:125    from 0 To 2
        SetMemory(0x662114, Add, 131072),# units:Right-click Action  index:126    from 0 To 2
        SetMemory(0x662114, Add, 33554432),# units:Right-click Action  index:127    from 0 To 2
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
        SetMemory(0x662130, Add, 33554432),# units:Right-click Action  index:155    from 0 To 2
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
        SetMemory(0x66203C, Add, -33816576),# units:Ready Sound  index:63    from 1065 To 549
        SetMemory(0x662040, Add, -597),# units:Ready Sound  index:64    from 597 To 0
        SetMemory(0x662060, Add, -534),# units:Ready Sound  index:80    from 534 To 0
        SetMemory(0x66208C, Add, 928),# units:Ready Sound  index:102    from 0 To 928
        SetMemory(0x662090, Add, 928),# units:Ready Sound  index:104    from 0 To 928
        SetMemory(0x65FFE4, Add, -2490368),# units:What Sound Start  index:27    from 449 To 411
        SetMemory(0x65FFE8, Add, -2490368),# units:What Sound Start  index:29    from 449 To 411
        SetMemory(0x66002C, Add, -33554432),# units:What Sound Start  index:63    from 1071 To 559
        SetMemory(0x660030, Add, -606),# units:What Sound Start  index:64    from 606 To 0
        SetMemory(0x660050, Add, -540),# units:What Sound Start  index:80    from 540 To 0
        SetMemory(0x660060, Add, -1136),# units:What Sound Start  index:88    from 1136 To 0
        SetMemory(0x660064, Add, -46),# units:What Sound Start  index:90    from 46 To 0
        SetMemory(0x660068, Add, -63700992),# units:What Sound Start  index:93    from 972 To 0
        SetMemory(0x66006C, Add, -976),# units:What Sound Start  index:94    from 976 To 0
        SetMemory(0x66006C, Add, -3276800),# units:What Sound Start  index:95    from 50 To 0
        SetMemory(0x660070, Add, -968),# units:What Sound Start  index:96    from 968 To 0
        SetMemory(0x660074, Add, -64815104),# units:What Sound Start  index:99    from 989 To 0
        SetMemory(0x660078, Add, -230),# units:What Sound Start  index:100    from 230 To 0
        SetMemory(0x66007C, Add, 484),# units:What Sound Start  index:102    from 449 To 933
        SetMemory(0x660080, Add, -188),# units:What Sound Start  index:104    from 1121 To 933
        SetMemory(0x660088, Add, -26017792),# units:What Sound Start  index:109    from 397 To 0
        SetMemory(0x66008C, Add, -983040),# units:What Sound Start  index:111    from 15 To 0
        SetMemory(0x660090, Add, -983040),# units:What Sound Start  index:113    from 15 To 0
        SetMemory(0x660094, Add, -15),# units:What Sound Start  index:114    from 15 To 0
        SetMemory(0x660098, Add, -395),# units:What Sound Start  index:116    from 395 To 0
        SetMemory(0x6600A4, Add, -402),# units:What Sound Start  index:122    from 402 To 0
        SetMemory(0x6600A4, Add, -25296896),# units:What Sound Start  index:123    from 386 To 0
        SetMemory(0x6600A8, Add, -983040),# units:What Sound Start  index:125    from 15 To 0
        SetMemory(0x6600AC, Add, -394),# units:What Sound Start  index:126    from 394 To 0
        SetMemory(0x6600AC, Add, -25624576),# units:What Sound Start  index:127    from 391 To 0
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
        SetMemory(0x6600E4, Add, -31981568),# units:What Sound Start  index:155    from 488 To 0
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
        SetMemory(0x662C24, Add, -2490368),# units:What Sound End  index:27    from 452 To 414
        SetMemory(0x662C28, Add, -2490368),# units:What Sound End  index:29    from 452 To 414
        SetMemory(0x662C6C, Add, -33554432),# units:What Sound End  index:63    from 1074 To 562
        SetMemory(0x662C70, Add, -609),# units:What Sound End  index:64    from 609 To 0
        SetMemory(0x662C90, Add, -543),# units:What Sound End  index:80    from 543 To 0
        SetMemory(0x662CA0, Add, -1139),# units:What Sound End  index:88    from 1139 To 0
        SetMemory(0x662CA4, Add, -48),# units:What Sound End  index:90    from 48 To 0
        SetMemory(0x662CA8, Add, -63832064),# units:What Sound End  index:93    from 974 To 0
        SetMemory(0x662CAC, Add, -978),# units:What Sound End  index:94    from 978 To 0
        SetMemory(0x662CAC, Add, -3407872),# units:What Sound End  index:95    from 52 To 0
        SetMemory(0x662CB0, Add, -970),# units:What Sound End  index:96    from 970 To 0
        SetMemory(0x662CB4, Add, -65011712),# units:What Sound End  index:99    from 992 To 0
        SetMemory(0x662CB8, Add, -233),# units:What Sound End  index:100    from 233 To 0
        SetMemory(0x662CBC, Add, 484),# units:What Sound End  index:102    from 452 To 936
        SetMemory(0x662CC0, Add, -188),# units:What Sound End  index:104    from 1124 To 936
        SetMemory(0x662CC8, Add, -26017792),# units:What Sound End  index:109    from 397 To 0
        SetMemory(0x662CCC, Add, -983040),# units:What Sound End  index:111    from 15 To 0
        SetMemory(0x662CD0, Add, -983040),# units:What Sound End  index:113    from 15 To 0
        SetMemory(0x662CD4, Add, -15),# units:What Sound End  index:114    from 15 To 0
        SetMemory(0x662CD8, Add, -395),# units:What Sound End  index:116    from 395 To 0
        SetMemory(0x662CE4, Add, -402),# units:What Sound End  index:122    from 402 To 0
        SetMemory(0x662CE4, Add, -25296896),# units:What Sound End  index:123    from 386 To 0
        SetMemory(0x662CE8, Add, -983040),# units:What Sound End  index:125    from 15 To 0
        SetMemory(0x662CEC, Add, -394),# units:What Sound End  index:126    from 394 To 0
        SetMemory(0x662CEC, Add, -25624576),# units:What Sound End  index:127    from 391 To 0
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
        SetMemory(0x662D24, Add, -31981568),# units:What Sound End  index:155    from 488 To 0
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
        SetMemory(0x663B6C, Add, -2424832),# units:Piss Sound Start  index:27    from 444 To 407
        SetMemory(0x663B70, Add, -2424832),# units:Piss Sound Start  index:29    from 444 To 407
        SetMemory(0x663BB4, Add, -33619968),# units:Piss Sound Start  index:63    from 1067 To 554
        SetMemory(0x663BB8, Add, -602),# units:Piss Sound Start  index:64    from 602 To 0
        SetMemory(0x663BD8, Add, -535),# units:Piss Sound Start  index:80    from 535 To 0
        SetMemory(0x663BE8, Add, -1130),# units:Piss Sound Start  index:88    from 1130 To 0
        SetMemory(0x663BFC, Add, -64225280),# units:Piss Sound Start  index:99    from 980 To 0
        SetMemory(0x663C00, Add, -226),# units:Piss Sound Start  index:100    from 226 To 0
        SetMemory(0x663C04, Add, 485),# units:Piss Sound Start  index:102    from 444 To 929
        SetMemory(0x663C08, Add, -183),# units:Piss Sound Start  index:104    from 1112 To 929
        SetMemory(0x661F1C, Add, -2490368),# units:Piss Sound End  index:27    from 448 To 410
        SetMemory(0x661F20, Add, -2490368),# units:Piss Sound End  index:29    from 448 To 410
        SetMemory(0x661F64, Add, -33554432),# units:Piss Sound End  index:63    from 1070 To 558
        SetMemory(0x661F68, Add, -605),# units:Piss Sound End  index:64    from 605 To 0
        SetMemory(0x661F88, Add, -539),# units:Piss Sound End  index:80    from 539 To 0
        SetMemory(0x661F98, Add, -1135),# units:Piss Sound End  index:88    from 1135 To 0
        SetMemory(0x661FAC, Add, -64749568),# units:Piss Sound End  index:99    from 988 To 0
        SetMemory(0x661FB0, Add, -229),# units:Piss Sound End  index:100    from 229 To 0
        SetMemory(0x661FB4, Add, 484),# units:Piss Sound End  index:102    from 448 To 932
        SetMemory(0x661FB8, Add, -188),# units:Piss Sound End  index:104    from 1120 To 932
        SetMemory(0x663C44, Add, -2490368),# units:Yes Sound Start  index:27    from 453 To 415
        SetMemory(0x663C48, Add, -2490368),# units:Yes Sound Start  index:29    from 453 To 415
        SetMemory(0x663C8C, Add, -33554432),# units:Yes Sound Start  index:63    from 1075 To 563
        SetMemory(0x663C90, Add, -610),# units:Yes Sound Start  index:64    from 610 To 0
        SetMemory(0x663CB0, Add, -544),# units:Yes Sound Start  index:80    from 544 To 0
        SetMemory(0x663CC0, Add, -1140),# units:Yes Sound Start  index:88    from 1140 To 0
        SetMemory(0x663CD4, Add, -65077248),# units:Yes Sound Start  index:99    from 993 To 0
        SetMemory(0x663CD8, Add, -234),# units:Yes Sound Start  index:100    from 234 To 0
        SetMemory(0x663CDC, Add, 484),# units:Yes Sound Start  index:102    from 453 To 937
        SetMemory(0x663CE0, Add, -188),# units:Yes Sound Start  index:104    from 1125 To 937
        SetMemory(0x661474, Add, -2490368),# units:Yes Sound End  index:27    from 456 To 418
        SetMemory(0x661478, Add, -2490368),# units:Yes Sound End  index:29    from 456 To 418
        SetMemory(0x6614BC, Add, -33619968),# units:Yes Sound End  index:63    from 1078 To 565
        SetMemory(0x6614C0, Add, -613),# units:Yes Sound End  index:64    from 613 To 0
        SetMemory(0x6614E0, Add, -547),# units:Yes Sound End  index:80    from 547 To 0
        SetMemory(0x6614F0, Add, -1143),# units:Yes Sound End  index:88    from 1143 To 0
        SetMemory(0x661504, Add, -65273856),# units:Yes Sound End  index:99    from 996 To 0
        SetMemory(0x661508, Add, -237),# units:Yes Sound End  index:100    from 237 To 0
        SetMemory(0x66150C, Add, 484),# units:Yes Sound End  index:102    from 456 To 940
        SetMemory(0x661510, Add, -188),# units:Yes Sound End  index:104    from 1128 To 940
        SetMemory(0x662864, Add, 2),# units:StarEdit Placement Box Width  index:1    from 15 To 17
        SetMemory(0x662868, Add, -15),# units:StarEdit Placement Box Width  index:2    from 32 To 17
        SetMemory(0x662880, Add, -21),# units:StarEdit Placement Box Width  index:8    from 38 To 17
        SetMemory(0x662884, Add, -48),# units:StarEdit Placement Box Width  index:9    from 65 To 17
        SetMemory(0x662888, Add, -6),# units:StarEdit Placement Box Width  index:10    from 23 To 17
        SetMemory(0x662890, Add, -63),# units:StarEdit Placement Box Width  index:12    from 80 To 17
        SetMemory(0x6628A0, Add, 2),# units:StarEdit Placement Box Width  index:16    from 15 To 17
        SetMemory(0x6628AC, Add, -15),# units:StarEdit Placement Box Width  index:19    from 32 To 17
        SetMemory(0x6628B0, Add, -1),# units:StarEdit Placement Box Width  index:20    from 18 To 17
        SetMemory(0x6628B4, Add, -21),# units:StarEdit Placement Box Width  index:21    from 38 To 17
        SetMemory(0x6628CC, Add, -58),# units:StarEdit Placement Box Width  index:27    from 75 To 17
        SetMemory(0x6628D0, Add, -58),# units:StarEdit Placement Box Width  index:28    from 75 To 17
        SetMemory(0x6628D4, Add, -58),# units:StarEdit Placement Box Width  index:29    from 75 To 17
        SetMemory(0x6628E0, Add, -6),# units:StarEdit Placement Box Width  index:32    from 23 To 17
        SetMemory(0x6628F4, Add, 1),# units:StarEdit Placement Box Width  index:37    from 16 To 17
        SetMemory(0x6628F8, Add, -4),# units:StarEdit Placement Box Width  index:38    from 21 To 17
        SetMemory(0x6628FC, Add, -21),# units:StarEdit Placement Box Width  index:39    from 38 To 17
        SetMemory(0x662900, Add, -2),# units:StarEdit Placement Box Width  index:40    from 19 To 17
        SetMemory(0x66290C, Add, -27),# units:StarEdit Placement Box Width  index:43    from 44 To 17
        SetMemory(0x662910, Add, -27),# units:StarEdit Placement Box Width  index:44    from 44 To 17
        SetMemory(0x662918, Add, -10),# units:StarEdit Placement Box Width  index:46    from 27 To 17
        SetMemory(0x662920, Add, -21),# units:StarEdit Placement Box Width  index:48    from 38 To 17
        SetMemory(0x66292C, Add, 2),# units:StarEdit Placement Box Width  index:51    from 15 To 17
        SetMemory(0x662930, Add, -12),# units:StarEdit Placement Box Width  index:52    from 29 To 17
        SetMemory(0x662934, Add, -4),# units:StarEdit Placement Box Width  index:53    from 21 To 17
        SetMemory(0x662938, Add, 1),# units:StarEdit Placement Box Width  index:54    from 16 To 17
        SetMemory(0x66293C, Add, -27),# units:StarEdit Placement Box Width  index:55    from 44 To 17
        SetMemory(0x662940, Add, -27),# units:StarEdit Placement Box Width  index:56    from 44 To 17
        SetMemory(0x662950, Add, -19),# units:StarEdit Placement Box Width  index:60    from 36 To 17
        SetMemory(0x662954, Add, -7),# units:StarEdit Placement Box Width  index:61    from 24 To 17
        SetMemory(0x66295C, Add, -15),# units:StarEdit Placement Box Width  index:63    from 32 To 17
        SetMemory(0x662960, Add, -14),# units:StarEdit Placement Box Width  index:64    from 23 To 9
        SetMemory(0x662964, Add, -6),# units:StarEdit Placement Box Width  index:65    from 23 To 17
        SetMemory(0x662968, Add, -15),# units:StarEdit Placement Box Width  index:66    from 32 To 17
        SetMemory(0x66296C, Add, -7),# units:StarEdit Placement Box Width  index:67    from 24 To 17
        SetMemory(0x662970, Add, -15),# units:StarEdit Placement Box Width  index:68    from 32 To 17
        SetMemory(0x662978, Add, -19),# units:StarEdit Placement Box Width  index:70    from 36 To 17
        SetMemory(0x66297C, Add, -27),# units:StarEdit Placement Box Width  index:71    from 44 To 17
        SetMemory(0x662988, Add, -7),# units:StarEdit Placement Box Width  index:74    from 24 To 17
        SetMemory(0x66298C, Add, -7),# units:StarEdit Placement Box Width  index:75    from 24 To 17
        SetMemory(0x662990, Add, -15),# units:StarEdit Placement Box Width  index:76    from 32 To 17
        SetMemory(0x662994, Add, -7),# units:StarEdit Placement Box Width  index:77    from 24 To 17
        SetMemory(0x662998, Add, -15),# units:StarEdit Placement Box Width  index:78    from 32 To 17
        SetMemory(0x66299C, Add, -7),# units:StarEdit Placement Box Width  index:79    from 24 To 17
        SetMemory(0x6629A0, Add, -19),# units:StarEdit Placement Box Width  index:80    from 36 To 17
        SetMemory(0x6629BC, Add, -7),# units:StarEdit Placement Box Width  index:87    from 24 To 17
        SetMemory(0x6629C0, Add, -19),# units:StarEdit Placement Box Width  index:88    from 36 To 17
        SetMemory(0x6629C8, Add, -23),# units:StarEdit Placement Box Width  index:90    from 32 To 9
        SetMemory(0x6629D4, Add, -23),# units:StarEdit Placement Box Width  index:93    from 32 To 9
        SetMemory(0x6629D8, Add, -23),# units:StarEdit Placement Box Width  index:94    from 32 To 9
        SetMemory(0x6629DC, Add, -23),# units:StarEdit Placement Box Width  index:95    from 32 To 9
        SetMemory(0x6629E0, Add, -23),# units:StarEdit Placement Box Width  index:96    from 32 To 9
        SetMemory(0x6629EC, Add, 2),# units:StarEdit Placement Box Width  index:99    from 15 To 17
        SetMemory(0x6629F0, Add, 2),# units:StarEdit Placement Box Width  index:100    from 15 To 17
        SetMemory(0x6629F8, Add, -58),# units:StarEdit Placement Box Width  index:102    from 75 To 17
        SetMemory(0x662A00, Add, 2),# units:StarEdit Placement Box Width  index:104    from 15 To 17
        SetMemory(0x662A14, Add, -89),# units:StarEdit Placement Box Width  index:109    from 96 To 7
        SetMemory(0x662A1C, Add, -121),# units:StarEdit Placement Box Width  index:111    from 128 To 7
        SetMemory(0x662A24, Add, -121),# units:StarEdit Placement Box Width  index:113    from 128 To 7
        SetMemory(0x662A28, Add, -121),# units:StarEdit Placement Box Width  index:114    from 128 To 7
        SetMemory(0x662A30, Add, -121),# units:StarEdit Placement Box Width  index:116    from 128 To 7
        SetMemory(0x662A48, Add, -121),# units:StarEdit Placement Box Width  index:122    from 128 To 7
        SetMemory(0x662A4C, Add, -89),# units:StarEdit Placement Box Width  index:123    from 96 To 7
        SetMemory(0x662A54, Add, -89),# units:StarEdit Placement Box Width  index:125    from 96 To 7
        SetMemory(0x662A58, Add, -89),# units:StarEdit Placement Box Width  index:126    from 96 To 7
        SetMemory(0x662A5C, Add, -89),# units:StarEdit Placement Box Width  index:127    from 96 To 7
        SetMemory(0x662A7C, Add, -89),# units:StarEdit Placement Box Width  index:135    from 96 To 7
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
        SetMemory(0x662ACC, Add, -89),# units:StarEdit Placement Box Width  index:155    from 96 To 7
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
        SetMemory(0x662860, Add, -196608),# units:StarEdit Placement Box Height  index:0    from 20 To 17
        SetMemory(0x662864, Add, -327680),# units:StarEdit Placement Box Height  index:1    from 22 To 17
        SetMemory(0x662868, Add, -983040),# units:StarEdit Placement Box Height  index:2    from 32 To 17
        SetMemory(0x662880, Add, -851968),# units:StarEdit Placement Box Height  index:8    from 30 To 17
        SetMemory(0x662884, Add, -2162688),# units:StarEdit Placement Box Height  index:9    from 50 To 17
        SetMemory(0x662888, Add, -720896),# units:StarEdit Placement Box Height  index:10    from 28 To 17
        SetMemory(0x662890, Add, -3080192),# units:StarEdit Placement Box Height  index:12    from 64 To 17
        SetMemory(0x6628A0, Add, -327680),# units:StarEdit Placement Box Height  index:16    from 22 To 17
        SetMemory(0x6628AC, Add, -983040),# units:StarEdit Placement Box Height  index:19    from 32 To 17
        SetMemory(0x6628B0, Add, -327680),# units:StarEdit Placement Box Height  index:20    from 22 To 17
        SetMemory(0x6628B4, Add, -851968),# units:StarEdit Placement Box Height  index:21    from 30 To 17
        SetMemory(0x6628CC, Add, -2752512),# units:StarEdit Placement Box Height  index:27    from 59 To 17
        SetMemory(0x6628D0, Add, -2752512),# units:StarEdit Placement Box Height  index:28    from 59 To 17
        SetMemory(0x6628D4, Add, -2752512),# units:StarEdit Placement Box Height  index:29    from 59 To 17
        SetMemory(0x6628E0, Add, -720896),# units:StarEdit Placement Box Height  index:32    from 28 To 17
        SetMemory(0x6628F4, Add, 65536),# units:StarEdit Placement Box Height  index:37    from 16 To 17
        SetMemory(0x6628F8, Add, -393216),# units:StarEdit Placement Box Height  index:38    from 23 To 17
        SetMemory(0x6628FC, Add, -983040),# units:StarEdit Placement Box Height  index:39    from 32 To 17
        SetMemory(0x662900, Add, -131072),# units:StarEdit Placement Box Height  index:40    from 19 To 17
        SetMemory(0x66290C, Add, -1769472),# units:StarEdit Placement Box Height  index:43    from 44 To 17
        SetMemory(0x662910, Add, -1769472),# units:StarEdit Placement Box Height  index:44    from 44 To 17
        SetMemory(0x662918, Add, -524288),# units:StarEdit Placement Box Height  index:46    from 25 To 17
        SetMemory(0x662920, Add, -983040),# units:StarEdit Placement Box Height  index:48    from 32 To 17
        SetMemory(0x66292C, Add, -327680),# units:StarEdit Placement Box Height  index:51    from 22 To 17
        SetMemory(0x662930, Add, -786432),# units:StarEdit Placement Box Height  index:52    from 29 To 17
        SetMemory(0x662934, Add, -393216),# units:StarEdit Placement Box Height  index:53    from 23 To 17
        SetMemory(0x662938, Add, 65536),# units:StarEdit Placement Box Height  index:54    from 16 To 17
        SetMemory(0x66293C, Add, -1769472),# units:StarEdit Placement Box Height  index:55    from 44 To 17
        SetMemory(0x662940, Add, -1769472),# units:StarEdit Placement Box Height  index:56    from 44 To 17
        SetMemory(0x662950, Add, -983040),# units:StarEdit Placement Box Height  index:60    from 32 To 17
        SetMemory(0x662954, Add, -851968),# units:StarEdit Placement Box Height  index:61    from 30 To 17
        SetMemory(0x66295C, Add, -983040),# units:StarEdit Placement Box Height  index:63    from 32 To 17
        SetMemory(0x662960, Add, -917504),# units:StarEdit Placement Box Height  index:64    from 23 To 9
        SetMemory(0x662964, Add, -655360),# units:StarEdit Placement Box Height  index:65    from 27 To 17
        SetMemory(0x662968, Add, -983040),# units:StarEdit Placement Box Height  index:66    from 32 To 17
        SetMemory(0x66296C, Add, -720896),# units:StarEdit Placement Box Height  index:67    from 28 To 17
        SetMemory(0x662970, Add, -983040),# units:StarEdit Placement Box Height  index:68    from 32 To 17
        SetMemory(0x662978, Add, -983040),# units:StarEdit Placement Box Height  index:70    from 32 To 17
        SetMemory(0x66297C, Add, -1769472),# units:StarEdit Placement Box Height  index:71    from 44 To 17
        SetMemory(0x662988, Add, -851968),# units:StarEdit Placement Box Height  index:74    from 30 To 17
        SetMemory(0x66298C, Add, -851968),# units:StarEdit Placement Box Height  index:75    from 30 To 17
        SetMemory(0x662990, Add, -983040),# units:StarEdit Placement Box Height  index:76    from 32 To 17
        SetMemory(0x662994, Add, -851968),# units:StarEdit Placement Box Height  index:77    from 30 To 17
        SetMemory(0x662998, Add, -983040),# units:StarEdit Placement Box Height  index:78    from 32 To 17
        SetMemory(0x66299C, Add, -720896),# units:StarEdit Placement Box Height  index:79    from 28 To 17
        SetMemory(0x6629A0, Add, -983040),# units:StarEdit Placement Box Height  index:80    from 32 To 17
        SetMemory(0x6629BC, Add, -720896),# units:StarEdit Placement Box Height  index:87    from 28 To 17
        SetMemory(0x6629C0, Add, -983040),# units:StarEdit Placement Box Height  index:88    from 32 To 17
        SetMemory(0x6629C8, Add, -1507328),# units:StarEdit Placement Box Height  index:90    from 32 To 9
        SetMemory(0x6629D4, Add, -1507328),# units:StarEdit Placement Box Height  index:93    from 32 To 9
        SetMemory(0x6629D8, Add, -1507328),# units:StarEdit Placement Box Height  index:94    from 32 To 9
        SetMemory(0x6629DC, Add, -1507328),# units:StarEdit Placement Box Height  index:95    from 32 To 9
        SetMemory(0x6629E0, Add, -1507328),# units:StarEdit Placement Box Height  index:96    from 32 To 9
        SetMemory(0x6629EC, Add, -327680),# units:StarEdit Placement Box Height  index:99    from 22 To 17
        SetMemory(0x6629F0, Add, -327680),# units:StarEdit Placement Box Height  index:100    from 22 To 17
        SetMemory(0x6629F8, Add, -2752512),# units:StarEdit Placement Box Height  index:102    from 59 To 17
        SetMemory(0x662A00, Add, -327680),# units:StarEdit Placement Box Height  index:104    from 22 To 17
        SetMemory(0x662A14, Add, -3735552),# units:StarEdit Placement Box Height  index:109    from 64 To 7
        SetMemory(0x662A1C, Add, -5832704),# units:StarEdit Placement Box Height  index:111    from 96 To 7
        SetMemory(0x662A24, Add, -5832704),# units:StarEdit Placement Box Height  index:113    from 96 To 7
        SetMemory(0x662A28, Add, -5832704),# units:StarEdit Placement Box Height  index:114    from 96 To 7
        SetMemory(0x662A30, Add, -5832704),# units:StarEdit Placement Box Height  index:116    from 96 To 7
        SetMemory(0x662A48, Add, -5832704),# units:StarEdit Placement Box Height  index:122    from 96 To 7
        SetMemory(0x662A4C, Add, -3735552),# units:StarEdit Placement Box Height  index:123    from 64 To 7
        SetMemory(0x662A54, Add, -3735552),# units:StarEdit Placement Box Height  index:125    from 64 To 7
        SetMemory(0x662A58, Add, -3735552),# units:StarEdit Placement Box Height  index:126    from 64 To 7
        SetMemory(0x662A5C, Add, -3735552),# units:StarEdit Placement Box Height  index:127    from 64 To 7
        SetMemory(0x662A7C, Add, -3735552),# units:StarEdit Placement Box Height  index:135    from 64 To 7
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
        SetMemory(0x662ACC, Add, -3735552),# units:StarEdit Placement Box Height  index:155    from 64 To 7
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
        SetMemory(0x6617D0, Add, 1),# units:Unit Size Left  index:1    from 7 To 8
        SetMemory(0x6617D8, Add, -8),# units:Unit Size Left  index:2    from 16 To 8
        SetMemory(0x661808, Add, -11),# units:Unit Size Left  index:8    from 19 To 8
        SetMemory(0x661810, Add, -24),# units:Unit Size Left  index:9    from 32 To 8
        SetMemory(0x661818, Add, -3),# units:Unit Size Left  index:10    from 11 To 8
        SetMemory(0x661828, Add, -29),# units:Unit Size Left  index:12    from 37 To 8
        SetMemory(0x661848, Add, 1),# units:Unit Size Left  index:16    from 7 To 8
        SetMemory(0x661860, Add, -8),# units:Unit Size Left  index:19    from 16 To 8
        SetMemory(0x661870, Add, -11),# units:Unit Size Left  index:21    from 19 To 8
        SetMemory(0x6618A0, Add, -29),# units:Unit Size Left  index:27    from 37 To 8
        SetMemory(0x6618A8, Add, -29),# units:Unit Size Left  index:28    from 37 To 8
        SetMemory(0x6618B0, Add, -29),# units:Unit Size Left  index:29    from 37 To 8
        SetMemory(0x6618C8, Add, -3),# units:Unit Size Left  index:32    from 11 To 8
        SetMemory(0x6618F8, Add, -2),# units:Unit Size Left  index:38    from 10 To 8
        SetMemory(0x661900, Add, -11),# units:Unit Size Left  index:39    from 19 To 8
        SetMemory(0x661908, Add, -1),# units:Unit Size Left  index:40    from 9 To 8
        SetMemory(0x661920, Add, -14),# units:Unit Size Left  index:43    from 22 To 8
        SetMemory(0x661928, Add, -14),# units:Unit Size Left  index:44    from 22 To 8
        SetMemory(0x661938, Add, -5),# units:Unit Size Left  index:46    from 13 To 8
        SetMemory(0x661948, Add, -11),# units:Unit Size Left  index:48    from 19 To 8
        SetMemory(0x661960, Add, 1),# units:Unit Size Left  index:51    from 7 To 8
        SetMemory(0x661968, Add, -6),# units:Unit Size Left  index:52    from 14 To 8
        SetMemory(0x661970, Add, -2),# units:Unit Size Left  index:53    from 10 To 8
        SetMemory(0x661980, Add, -14),# units:Unit Size Left  index:55    from 22 To 8
        SetMemory(0x661988, Add, -14),# units:Unit Size Left  index:56    from 22 To 8
        SetMemory(0x6619A8, Add, -10),# units:Unit Size Left  index:60    from 18 To 8
        SetMemory(0x6619B0, Add, -4),# units:Unit Size Left  index:61    from 12 To 8
        SetMemory(0x6619C0, Add, -8),# units:Unit Size Left  index:63    from 16 To 8
        SetMemory(0x6619C8, Add, -7),# units:Unit Size Left  index:64    from 11 To 4
        SetMemory(0x6619D0, Add, -3),# units:Unit Size Left  index:65    from 11 To 8
        SetMemory(0x6619D8, Add, -7),# units:Unit Size Left  index:66    from 15 To 8
        SetMemory(0x6619E0, Add, -4),# units:Unit Size Left  index:67    from 12 To 8
        SetMemory(0x6619E8, Add, -8),# units:Unit Size Left  index:68    from 16 To 8
        SetMemory(0x6619F8, Add, -10),# units:Unit Size Left  index:70    from 18 To 8
        SetMemory(0x661A00, Add, -14),# units:Unit Size Left  index:71    from 22 To 8
        SetMemory(0x661A18, Add, -4),# units:Unit Size Left  index:74    from 12 To 8
        SetMemory(0x661A20, Add, -4),# units:Unit Size Left  index:75    from 12 To 8
        SetMemory(0x661A28, Add, -8),# units:Unit Size Left  index:76    from 16 To 8
        SetMemory(0x661A30, Add, -3),# units:Unit Size Left  index:77    from 11 To 8
        SetMemory(0x661A38, Add, -7),# units:Unit Size Left  index:78    from 15 To 8
        SetMemory(0x661A40, Add, -4),# units:Unit Size Left  index:79    from 12 To 8
        SetMemory(0x661A48, Add, -10),# units:Unit Size Left  index:80    from 18 To 8
        SetMemory(0x661A80, Add, -4),# units:Unit Size Left  index:87    from 12 To 8
        SetMemory(0x661A88, Add, -10),# units:Unit Size Left  index:88    from 18 To 8
        SetMemory(0x661A98, Add, -12),# units:Unit Size Left  index:90    from 16 To 4
        SetMemory(0x661AB0, Add, -12),# units:Unit Size Left  index:93    from 16 To 4
        SetMemory(0x661AB8, Add, -12),# units:Unit Size Left  index:94    from 16 To 4
        SetMemory(0x661AC0, Add, -12),# units:Unit Size Left  index:95    from 16 To 4
        SetMemory(0x661AC8, Add, -12),# units:Unit Size Left  index:96    from 16 To 4
        SetMemory(0x661AE0, Add, 1),# units:Unit Size Left  index:99    from 7 To 8
        SetMemory(0x661AE8, Add, 1),# units:Unit Size Left  index:100    from 7 To 8
        SetMemory(0x661AF8, Add, -29),# units:Unit Size Left  index:102    from 37 To 8
        SetMemory(0x661B08, Add, 1),# units:Unit Size Left  index:104    from 7 To 8
        SetMemory(0x661B30, Add, -35),# units:Unit Size Left  index:109    from 38 To 3
        SetMemory(0x661B40, Add, -45),# units:Unit Size Left  index:111    from 48 To 3
        SetMemory(0x661B50, Add, -53),# units:Unit Size Left  index:113    from 56 To 3
        SetMemory(0x661B58, Add, -45),# units:Unit Size Left  index:114    from 48 To 3
        SetMemory(0x661B68, Add, -45),# units:Unit Size Left  index:116    from 48 To 3
        SetMemory(0x661B98, Add, -45),# units:Unit Size Left  index:122    from 48 To 3
        SetMemory(0x661BA0, Add, -45),# units:Unit Size Left  index:123    from 48 To 3
        SetMemory(0x661BB0, Add, -29),# units:Unit Size Left  index:125    from 32 To 3
        SetMemory(0x661BB8, Add, -45),# units:Unit Size Left  index:126    from 48 To 3
        SetMemory(0x661BC0, Add, -45),# units:Unit Size Left  index:127    from 48 To 3
        SetMemory(0x661C00, Add, -37),# units:Unit Size Left  index:135    from 40 To 3
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
        SetMemory(0x661CA0, Add, -33),# units:Unit Size Left  index:155    from 36 To 3
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
        SetMemory(0x6617C8, Add, -65536),# units:Unit Size Up  index:0    from 9 To 8
        SetMemory(0x6617D0, Add, -131072),# units:Unit Size Up  index:1    from 10 To 8
        SetMemory(0x6617D8, Add, -524288),# units:Unit Size Up  index:2    from 16 To 8
        SetMemory(0x661808, Add, -458752),# units:Unit Size Up  index:8    from 15 To 8
        SetMemory(0x661810, Add, -1638400),# units:Unit Size Up  index:9    from 33 To 8
        SetMemory(0x661818, Add, -327680),# units:Unit Size Up  index:10    from 13 To 8
        SetMemory(0x661828, Add, -1376256),# units:Unit Size Up  index:12    from 29 To 8
        SetMemory(0x661848, Add, -131072),# units:Unit Size Up  index:16    from 10 To 8
        SetMemory(0x661860, Add, -524288),# units:Unit Size Up  index:19    from 16 To 8
        SetMemory(0x661868, Add, -65536),# units:Unit Size Up  index:20    from 9 To 8
        SetMemory(0x661870, Add, -458752),# units:Unit Size Up  index:21    from 15 To 8
        SetMemory(0x6618A0, Add, -1376256),# units:Unit Size Up  index:27    from 29 To 8
        SetMemory(0x6618A8, Add, -1376256),# units:Unit Size Up  index:28    from 29 To 8
        SetMemory(0x6618B0, Add, -1376256),# units:Unit Size Up  index:29    from 29 To 8
        SetMemory(0x6618C8, Add, 65536),# units:Unit Size Up  index:32    from 7 To 8
        SetMemory(0x6618F0, Add, 262144),# units:Unit Size Up  index:37    from 4 To 8
        SetMemory(0x6618F8, Add, -131072),# units:Unit Size Up  index:38    from 10 To 8
        SetMemory(0x661900, Add, -524288),# units:Unit Size Up  index:39    from 16 To 8
        SetMemory(0x661908, Add, -65536),# units:Unit Size Up  index:40    from 9 To 8
        SetMemory(0x661920, Add, -917504),# units:Unit Size Up  index:43    from 22 To 8
        SetMemory(0x661928, Add, -917504),# units:Unit Size Up  index:44    from 22 To 8
        SetMemory(0x661938, Add, -262144),# units:Unit Size Up  index:46    from 12 To 8
        SetMemory(0x661948, Add, -524288),# units:Unit Size Up  index:48    from 16 To 8
        SetMemory(0x661960, Add, -131072),# units:Unit Size Up  index:51    from 10 To 8
        SetMemory(0x661968, Add, -393216),# units:Unit Size Up  index:52    from 14 To 8
        SetMemory(0x661970, Add, -131072),# units:Unit Size Up  index:53    from 10 To 8
        SetMemory(0x661978, Add, 262144),# units:Unit Size Up  index:54    from 4 To 8
        SetMemory(0x661980, Add, -917504),# units:Unit Size Up  index:55    from 22 To 8
        SetMemory(0x661988, Add, -917504),# units:Unit Size Up  index:56    from 22 To 8
        SetMemory(0x6619A8, Add, -524288),# units:Unit Size Up  index:60    from 16 To 8
        SetMemory(0x6619B0, Add, 131072),# units:Unit Size Up  index:61    from 6 To 8
        SetMemory(0x6619C0, Add, -524288),# units:Unit Size Up  index:63    from 16 To 8
        SetMemory(0x6619C8, Add, -458752),# units:Unit Size Up  index:64    from 11 To 4
        SetMemory(0x6619D0, Add, 196608),# units:Unit Size Up  index:65    from 5 To 8
        SetMemory(0x6619D8, Add, -458752),# units:Unit Size Up  index:66    from 15 To 8
        SetMemory(0x6619E0, Add, -131072),# units:Unit Size Up  index:67    from 10 To 8
        SetMemory(0x6619E8, Add, -524288),# units:Unit Size Up  index:68    from 16 To 8
        SetMemory(0x6619F8, Add, -524288),# units:Unit Size Up  index:70    from 16 To 8
        SetMemory(0x661A00, Add, -917504),# units:Unit Size Up  index:71    from 22 To 8
        SetMemory(0x661A18, Add, 131072),# units:Unit Size Up  index:74    from 6 To 8
        SetMemory(0x661A20, Add, 131072),# units:Unit Size Up  index:75    from 6 To 8
        SetMemory(0x661A28, Add, -524288),# units:Unit Size Up  index:76    from 16 To 8
        SetMemory(0x661A30, Add, 196608),# units:Unit Size Up  index:77    from 5 To 8
        SetMemory(0x661A38, Add, -458752),# units:Unit Size Up  index:78    from 15 To 8
        SetMemory(0x661A40, Add, -131072),# units:Unit Size Up  index:79    from 10 To 8
        SetMemory(0x661A48, Add, -524288),# units:Unit Size Up  index:80    from 16 To 8
        SetMemory(0x661A80, Add, -393216),# units:Unit Size Up  index:87    from 14 To 8
        SetMemory(0x661A88, Add, -524288),# units:Unit Size Up  index:88    from 16 To 8
        SetMemory(0x661A98, Add, -786432),# units:Unit Size Up  index:90    from 16 To 4
        SetMemory(0x661AB0, Add, -786432),# units:Unit Size Up  index:93    from 16 To 4
        SetMemory(0x661AB8, Add, -786432),# units:Unit Size Up  index:94    from 16 To 4
        SetMemory(0x661AC0, Add, -786432),# units:Unit Size Up  index:95    from 16 To 4
        SetMemory(0x661AC8, Add, -786432),# units:Unit Size Up  index:96    from 16 To 4
        SetMemory(0x661AE0, Add, -131072),# units:Unit Size Up  index:99    from 10 To 8
        SetMemory(0x661AE8, Add, -131072),# units:Unit Size Up  index:100    from 10 To 8
        SetMemory(0x661AF8, Add, -1376256),# units:Unit Size Up  index:102    from 29 To 8
        SetMemory(0x661B08, Add, -131072),# units:Unit Size Up  index:104    from 10 To 8
        SetMemory(0x661B30, Add, -1245184),# units:Unit Size Up  index:109    from 22 To 3
        SetMemory(0x661B40, Add, -2424832),# units:Unit Size Up  index:111    from 40 To 3
        SetMemory(0x661B50, Add, -2424832),# units:Unit Size Up  index:113    from 40 To 3
        SetMemory(0x661B58, Add, -2424832),# units:Unit Size Up  index:114    from 40 To 3
        SetMemory(0x661B68, Add, -2293760),# units:Unit Size Up  index:116    from 38 To 3
        SetMemory(0x661B98, Add, -1900544),# units:Unit Size Up  index:122    from 32 To 3
        SetMemory(0x661BA0, Add, -1900544),# units:Unit Size Up  index:123    from 32 To 3
        SetMemory(0x661BB0, Add, -1376256),# units:Unit Size Up  index:125    from 24 To 3
        SetMemory(0x661BB8, Add, -1900544),# units:Unit Size Up  index:126    from 32 To 3
        SetMemory(0x661BC0, Add, -1900544),# units:Unit Size Up  index:127    from 32 To 3
        SetMemory(0x661C00, Add, -1900544),# units:Unit Size Up  index:135    from 32 To 3
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
        SetMemory(0x661CA0, Add, -851968),# units:Unit Size Up  index:155    from 16 To 3
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
        SetMemory(0x6617D4, Add, 1),# units:Unit Size Right  index:1    from 7 To 8
        SetMemory(0x6617DC, Add, -7),# units:Unit Size Right  index:2    from 15 To 8
        SetMemory(0x66180C, Add, -10),# units:Unit Size Right  index:8    from 18 To 8
        SetMemory(0x661814, Add, -24),# units:Unit Size Right  index:9    from 32 To 8
        SetMemory(0x66181C, Add, -3),# units:Unit Size Right  index:10    from 11 To 8
        SetMemory(0x66182C, Add, -29),# units:Unit Size Right  index:12    from 37 To 8
        SetMemory(0x66184C, Add, 1),# units:Unit Size Right  index:16    from 7 To 8
        SetMemory(0x661864, Add, -7),# units:Unit Size Right  index:19    from 15 To 8
        SetMemory(0x661874, Add, -10),# units:Unit Size Right  index:21    from 18 To 8
        SetMemory(0x6618A4, Add, -29),# units:Unit Size Right  index:27    from 37 To 8
        SetMemory(0x6618AC, Add, -29),# units:Unit Size Right  index:28    from 37 To 8
        SetMemory(0x6618B4, Add, -29),# units:Unit Size Right  index:29    from 37 To 8
        SetMemory(0x6618CC, Add, -3),# units:Unit Size Right  index:32    from 11 To 8
        SetMemory(0x6618F4, Add, 1),# units:Unit Size Right  index:37    from 7 To 8
        SetMemory(0x6618FC, Add, -2),# units:Unit Size Right  index:38    from 10 To 8
        SetMemory(0x661904, Add, -10),# units:Unit Size Right  index:39    from 18 To 8
        SetMemory(0x66190C, Add, -1),# units:Unit Size Right  index:40    from 9 To 8
        SetMemory(0x661924, Add, -13),# units:Unit Size Right  index:43    from 21 To 8
        SetMemory(0x66192C, Add, -13),# units:Unit Size Right  index:44    from 21 To 8
        SetMemory(0x66193C, Add, -5),# units:Unit Size Right  index:46    from 13 To 8
        SetMemory(0x66194C, Add, -10),# units:Unit Size Right  index:48    from 18 To 8
        SetMemory(0x661964, Add, 1),# units:Unit Size Right  index:51    from 7 To 8
        SetMemory(0x66196C, Add, -6),# units:Unit Size Right  index:52    from 14 To 8
        SetMemory(0x661974, Add, -2),# units:Unit Size Right  index:53    from 10 To 8
        SetMemory(0x66197C, Add, 1),# units:Unit Size Right  index:54    from 7 To 8
        SetMemory(0x661984, Add, -13),# units:Unit Size Right  index:55    from 21 To 8
        SetMemory(0x66198C, Add, -13),# units:Unit Size Right  index:56    from 21 To 8
        SetMemory(0x6619AC, Add, -9),# units:Unit Size Right  index:60    from 17 To 8
        SetMemory(0x6619B4, Add, -3),# units:Unit Size Right  index:61    from 11 To 8
        SetMemory(0x6619C4, Add, -7),# units:Unit Size Right  index:63    from 15 To 8
        SetMemory(0x6619CC, Add, -7),# units:Unit Size Right  index:64    from 11 To 4
        SetMemory(0x6619D4, Add, -3),# units:Unit Size Right  index:65    from 11 To 8
        SetMemory(0x6619DC, Add, -8),# units:Unit Size Right  index:66    from 16 To 8
        SetMemory(0x6619E4, Add, -3),# units:Unit Size Right  index:67    from 11 To 8
        SetMemory(0x6619EC, Add, -7),# units:Unit Size Right  index:68    from 15 To 8
        SetMemory(0x6619FC, Add, -9),# units:Unit Size Right  index:70    from 17 To 8
        SetMemory(0x661A04, Add, -13),# units:Unit Size Right  index:71    from 21 To 8
        SetMemory(0x661A1C, Add, -3),# units:Unit Size Right  index:74    from 11 To 8
        SetMemory(0x661A24, Add, -3),# units:Unit Size Right  index:75    from 11 To 8
        SetMemory(0x661A2C, Add, -7),# units:Unit Size Right  index:76    from 15 To 8
        SetMemory(0x661A34, Add, -3),# units:Unit Size Right  index:77    from 11 To 8
        SetMemory(0x661A3C, Add, -8),# units:Unit Size Right  index:78    from 16 To 8
        SetMemory(0x661A44, Add, -3),# units:Unit Size Right  index:79    from 11 To 8
        SetMemory(0x661A4C, Add, -9),# units:Unit Size Right  index:80    from 17 To 8
        SetMemory(0x661A84, Add, -3),# units:Unit Size Right  index:87    from 11 To 8
        SetMemory(0x661A8C, Add, -9),# units:Unit Size Right  index:88    from 17 To 8
        SetMemory(0x661A9C, Add, -11),# units:Unit Size Right  index:90    from 15 To 4
        SetMemory(0x661AB4, Add, -11),# units:Unit Size Right  index:93    from 15 To 4
        SetMemory(0x661ABC, Add, -11),# units:Unit Size Right  index:94    from 15 To 4
        SetMemory(0x661AC4, Add, -11),# units:Unit Size Right  index:95    from 15 To 4
        SetMemory(0x661ACC, Add, -11),# units:Unit Size Right  index:96    from 15 To 4
        SetMemory(0x661AE4, Add, 1),# units:Unit Size Right  index:99    from 7 To 8
        SetMemory(0x661AEC, Add, 1),# units:Unit Size Right  index:100    from 7 To 8
        SetMemory(0x661AFC, Add, -29),# units:Unit Size Right  index:102    from 37 To 8
        SetMemory(0x661B0C, Add, 1),# units:Unit Size Right  index:104    from 7 To 8
        SetMemory(0x661B34, Add, -35),# units:Unit Size Right  index:109    from 38 To 3
        SetMemory(0x661B44, Add, -53),# units:Unit Size Right  index:111    from 56 To 3
        SetMemory(0x661B54, Add, -53),# units:Unit Size Right  index:113    from 56 To 3
        SetMemory(0x661B5C, Add, -45),# units:Unit Size Right  index:114    from 48 To 3
        SetMemory(0x661B6C, Add, -45),# units:Unit Size Right  index:116    from 48 To 3
        SetMemory(0x661B9C, Add, -45),# units:Unit Size Right  index:122    from 48 To 3
        SetMemory(0x661BA4, Add, -44),# units:Unit Size Right  index:123    from 47 To 3
        SetMemory(0x661BB4, Add, -29),# units:Unit Size Right  index:125    from 32 To 3
        SetMemory(0x661BBC, Add, -44),# units:Unit Size Right  index:126    from 47 To 3
        SetMemory(0x661BC4, Add, -44),# units:Unit Size Right  index:127    from 47 To 3
        SetMemory(0x661C04, Add, -37),# units:Unit Size Right  index:135    from 40 To 3
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
        SetMemory(0x661CA4, Add, -37),# units:Unit Size Right  index:155    from 40 To 3
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
        SetMemory(0x6617CC, Add, -131072),# units:Unit Size Down  index:0    from 10 To 8
        SetMemory(0x6617D4, Add, -196608),# units:Unit Size Down  index:1    from 11 To 8
        SetMemory(0x6617DC, Add, -458752),# units:Unit Size Down  index:2    from 15 To 8
        SetMemory(0x66180C, Add, -393216),# units:Unit Size Down  index:8    from 14 To 8
        SetMemory(0x661814, Add, -524288),# units:Unit Size Down  index:9    from 16 To 8
        SetMemory(0x66181C, Add, -393216),# units:Unit Size Down  index:10    from 14 To 8
        SetMemory(0x66182C, Add, -1376256),# units:Unit Size Down  index:12    from 29 To 8
        SetMemory(0x66184C, Add, -196608),# units:Unit Size Down  index:16    from 11 To 8
        SetMemory(0x661864, Add, -458752),# units:Unit Size Down  index:19    from 15 To 8
        SetMemory(0x66186C, Add, -131072),# units:Unit Size Down  index:20    from 10 To 8
        SetMemory(0x661874, Add, -393216),# units:Unit Size Down  index:21    from 14 To 8
        SetMemory(0x6618A4, Add, -1376256),# units:Unit Size Down  index:27    from 29 To 8
        SetMemory(0x6618AC, Add, -1376256),# units:Unit Size Down  index:28    from 29 To 8
        SetMemory(0x6618B4, Add, -1376256),# units:Unit Size Down  index:29    from 29 To 8
        SetMemory(0x6618CC, Add, -393216),# units:Unit Size Down  index:32    from 14 To 8
        SetMemory(0x6618F4, Add, -196608),# units:Unit Size Down  index:37    from 11 To 8
        SetMemory(0x6618FC, Add, -262144),# units:Unit Size Down  index:38    from 12 To 8
        SetMemory(0x661904, Add, -458752),# units:Unit Size Down  index:39    from 15 To 8
        SetMemory(0x66190C, Add, -65536),# units:Unit Size Down  index:40    from 9 To 8
        SetMemory(0x661924, Add, -851968),# units:Unit Size Down  index:43    from 21 To 8
        SetMemory(0x66192C, Add, -851968),# units:Unit Size Down  index:44    from 21 To 8
        SetMemory(0x66193C, Add, -262144),# units:Unit Size Down  index:46    from 12 To 8
        SetMemory(0x66194C, Add, -458752),# units:Unit Size Down  index:48    from 15 To 8
        SetMemory(0x661964, Add, -196608),# units:Unit Size Down  index:51    from 11 To 8
        SetMemory(0x66196C, Add, -393216),# units:Unit Size Down  index:52    from 14 To 8
        SetMemory(0x661974, Add, -262144),# units:Unit Size Down  index:53    from 12 To 8
        SetMemory(0x66197C, Add, -196608),# units:Unit Size Down  index:54    from 11 To 8
        SetMemory(0x661984, Add, -851968),# units:Unit Size Down  index:55    from 21 To 8
        SetMemory(0x66198C, Add, -851968),# units:Unit Size Down  index:56    from 21 To 8
        SetMemory(0x6619AC, Add, -458752),# units:Unit Size Down  index:60    from 15 To 8
        SetMemory(0x6619B4, Add, -720896),# units:Unit Size Down  index:61    from 19 To 8
        SetMemory(0x6619C4, Add, -458752),# units:Unit Size Down  index:63    from 15 To 8
        SetMemory(0x6619CC, Add, -458752),# units:Unit Size Down  index:64    from 11 To 4
        SetMemory(0x6619D4, Add, -327680),# units:Unit Size Down  index:65    from 13 To 8
        SetMemory(0x6619DC, Add, -524288),# units:Unit Size Down  index:66    from 16 To 8
        SetMemory(0x6619E4, Add, -327680),# units:Unit Size Down  index:67    from 13 To 8
        SetMemory(0x6619EC, Add, -458752),# units:Unit Size Down  index:68    from 15 To 8
        SetMemory(0x6619FC, Add, -458752),# units:Unit Size Down  index:70    from 15 To 8
        SetMemory(0x661A04, Add, -851968),# units:Unit Size Down  index:71    from 21 To 8
        SetMemory(0x661A1C, Add, -720896),# units:Unit Size Down  index:74    from 19 To 8
        SetMemory(0x661A24, Add, -720896),# units:Unit Size Down  index:75    from 19 To 8
        SetMemory(0x661A2C, Add, -458752),# units:Unit Size Down  index:76    from 15 To 8
        SetMemory(0x661A34, Add, -327680),# units:Unit Size Down  index:77    from 13 To 8
        SetMemory(0x661A3C, Add, -524288),# units:Unit Size Down  index:78    from 16 To 8
        SetMemory(0x661A44, Add, -327680),# units:Unit Size Down  index:79    from 13 To 8
        SetMemory(0x661A4C, Add, -458752),# units:Unit Size Down  index:80    from 15 To 8
        SetMemory(0x661A84, Add, -327680),# units:Unit Size Down  index:87    from 13 To 8
        SetMemory(0x661A8C, Add, -458752),# units:Unit Size Down  index:88    from 15 To 8
        SetMemory(0x661A9C, Add, -720896),# units:Unit Size Down  index:90    from 15 To 4
        SetMemory(0x661AB4, Add, -720896),# units:Unit Size Down  index:93    from 15 To 4
        SetMemory(0x661ABC, Add, -720896),# units:Unit Size Down  index:94    from 15 To 4
        SetMemory(0x661AC4, Add, -720896),# units:Unit Size Down  index:95    from 15 To 4
        SetMemory(0x661ACC, Add, -720896),# units:Unit Size Down  index:96    from 15 To 4
        SetMemory(0x661AE4, Add, -196608),# units:Unit Size Down  index:99    from 11 To 8
        SetMemory(0x661AEC, Add, -196608),# units:Unit Size Down  index:100    from 11 To 8
        SetMemory(0x661AFC, Add, -1376256),# units:Unit Size Down  index:102    from 29 To 8
        SetMemory(0x661B0C, Add, -196608),# units:Unit Size Down  index:104    from 11 To 8
        SetMemory(0x661B34, Add, -1507328),# units:Unit Size Down  index:109    from 26 To 3
        SetMemory(0x661B44, Add, -1900544),# units:Unit Size Down  index:111    from 32 To 3
        SetMemory(0x661B54, Add, -2424832),# units:Unit Size Down  index:113    from 40 To 3
        SetMemory(0x661B5C, Add, -2293760),# units:Unit Size Down  index:114    from 38 To 3
        SetMemory(0x661B6C, Add, -2293760),# units:Unit Size Down  index:116    from 38 To 3
        SetMemory(0x661B9C, Add, -1638400),# units:Unit Size Down  index:122    from 28 To 3
        SetMemory(0x661BA4, Add, -1245184),# units:Unit Size Down  index:123    from 22 To 3
        SetMemory(0x661BB4, Add, -851968),# units:Unit Size Down  index:125    from 16 To 3
        SetMemory(0x661BBC, Add, -1835008),# units:Unit Size Down  index:126    from 31 To 3
        SetMemory(0x661BC4, Add, -1835008),# units:Unit Size Down  index:127    from 31 To 3
        SetMemory(0x661C04, Add, -1376256),# units:Unit Size Down  index:135    from 24 To 3
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
        SetMemory(0x661CA4, Add, -1114112),# units:Unit Size Down  index:155    from 20 To 3
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
        SetMemory(0x662FBC, Add, -196608),# units:Portrait  index:27    from 16 To 13
        SetMemory(0x662FC0, Add, -65536),# units:Portrait  index:29    from 14 To 13
        SetMemory(0x663004, Add, -3473408),# units:Portrait  index:63    from 99 To 46
        SetMemory(0x663034, Add, -917504),# units:Portrait  index:87    from 59 To 45
        SetMemory(0x663038, Add, -50),# units:Portrait  index:88    from 95 To 45
        SetMemory(0x66304C, Add, -3211264),# units:Portrait  index:99    from 94 To 45
        SetMemory(0x663050, Add, -48),# units:Portrait  index:100    from 93 To 45
        SetMemory(0x663054, Add, -64),# units:Portrait  index:102    from 92 To 28
        SetMemory(0x663058, Add, -66),# units:Portrait  index:104    from 94 To 28
        SetMemory(0x663060, Add, 4063232),# units:Portrait  index:109    from 17 To 79
        SetMemory(0x663064, Add, 4063232),# units:Portrait  index:111    from 17 To 79
        SetMemory(0x663068, Add, 4063232),# units:Portrait  index:113    from 17 To 79
        SetMemory(0x66306C, Add, 62),# units:Portrait  index:114    from 17 To 79
        SetMemory(0x663070, Add, 62),# units:Portrait  index:116    from 17 To 79
        SetMemory(0x66307C, Add, 62),# units:Portrait  index:122    from 17 To 79
        SetMemory(0x66307C, Add, 4063232),# units:Portrait  index:123    from 17 To 79
        SetMemory(0x663080, Add, 4063232),# units:Portrait  index:125    from 17 To 79
        SetMemory(0x663084, Add, 65),# units:Portrait  index:126    from 14 To 79
        SetMemory(0x663084, Add, 4063232),# units:Portrait  index:127    from 17 To 79
        SetMemory(0x663094, Add, 2686976),# units:Portrait  index:135    from 38 To 79
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
        SetMemory(0x6630BC, Add, 1245184),# units:Portrait  index:155    from 60 To 79
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
        SetMemory(0x663904, Add, 3276800),# units:Mineral Cost  index:63    from 0 To 50
        SetMemory(0x663928, Add, -400),# units:Mineral Cost  index:80    from 600 To 200
        SetMemory(0x663934, Add, 6553600),# units:Mineral Cost  index:87    from 100 To 200
        SetMemory(0x663938, Add, -400),# units:Mineral Cost  index:88    from 600 To 200
        SetMemory(0x663954, Add, -750),# units:Mineral Cost  index:102    from 800 To 50
        SetMemory(0x663958, Add, -150),# units:Mineral Cost  index:104    from 200 To 50
        SetMemory(0x663960, Add, -6553600),# units:Mineral Cost  index:109    from 100 To 0
        SetMemory(0x663964, Add, -9830400),# units:Mineral Cost  index:111    from 150 To 0
        SetMemory(0x663968, Add, -13107200),# units:Mineral Cost  index:113    from 200 To 0
        SetMemory(0x66396C, Add, -150),# units:Mineral Cost  index:114    from 150 To 0
        SetMemory(0x663970, Add, -100),# units:Mineral Cost  index:116    from 100 To 0
        SetMemory(0x66397C, Add, -125),# units:Mineral Cost  index:122    from 125 To 0
        SetMemory(0x66397C, Add, -6553600),# units:Mineral Cost  index:123    from 100 To 0
        SetMemory(0x663980, Add, -6553600),# units:Mineral Cost  index:125    from 100 To 0
        SetMemory(0x663984, Add, -800),# units:Mineral Cost  index:126    from 800 To 0
        SetMemory(0x663984, Add, -13107200),# units:Mineral Cost  index:127    from 200 To 0
        SetMemory(0x663994, Add, -6553600),# units:Mineral Cost  index:135    from 100 To 0
        SetMemory(0x663998, Add, -100),# units:Mineral Cost  index:136    from 100 To 0
        SetMemory(0x663998, Add, -6553600),# units:Mineral Cost  index:137    from 100 To 0
        SetMemory(0x66399C, Add, -150),# units:Mineral Cost  index:138    from 150 To 0
        SetMemory(0x66399C, Add, -4915200),# units:Mineral Cost  index:139    from 75 To 0
        SetMemory(0x6639A0, Add, -150),# units:Mineral Cost  index:140    from 150 To 0
        SetMemory(0x6639A4, Add, -200),# units:Mineral Cost  index:142    from 200 To 0
        SetMemory(0x6639AC, Add, -65536),# units:Mineral Cost  index:147    from 1 To 0
        SetMemory(0x6639B0, Add, -1),# units:Mineral Cost  index:148    from 1 To 0
        SetMemory(0x6639BC, Add, -400),# units:Mineral Cost  index:154    from 400 To 0
        SetMemory(0x6639BC, Add, -13107200),# units:Mineral Cost  index:155    from 200 To 0
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
        SetMemory(0x65FD7C, Add, 65536000),# units:Vespene Cost  index:63    from 0 To 1000
        SetMemory(0x65FDC4, Add, 14745600),# units:Vespene Cost  index:99    from 75 To 300
        SetMemory(0x65FDC8, Add, 225),# units:Vespene Cost  index:100    from 75 To 300
        SetMemory(0x65FDCC, Add, -575),# units:Vespene Cost  index:102    from 600 To 25
        SetMemory(0x65FDD0, Add, -50),# units:Vespene Cost  index:104    from 75 To 25
        SetMemory(0x65FDE0, Add, -6553600),# units:Vespene Cost  index:113    from 100 To 0
        SetMemory(0x65FDE4, Add, -100),# units:Vespene Cost  index:114    from 100 To 0
        SetMemory(0x65FDE8, Add, -150),# units:Vespene Cost  index:116    from 150 To 0
        SetMemory(0x65FDF4, Add, -3276800),# units:Vespene Cost  index:123    from 50 To 0
        SetMemory(0x65FDFC, Add, -600),# units:Vespene Cost  index:126    from 600 To 0
        SetMemory(0x65FE0C, Add, -3276800),# units:Vespene Cost  index:135    from 50 To 0
        SetMemory(0x65FE10, Add, -100),# units:Vespene Cost  index:136    from 100 To 0
        SetMemory(0x65FE10, Add, -9830400),# units:Vespene Cost  index:137    from 150 To 0
        SetMemory(0x65FE14, Add, -100),# units:Vespene Cost  index:138    from 100 To 0
        SetMemory(0x65FE18, Add, -200),# units:Vespene Cost  index:140    from 200 To 0
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
        SetMemory(0x66045C, Add, -157286400),# units:Build Time  index:27    from 4800 To 2400
        SetMemory(0x660460, Add, -157286400),# units:Build Time  index:29    from 4800 To 2400
        SetMemory(0x6604A4, Add, 294912000),# units:Build Time  index:63    from 300 To 4800
        SetMemory(0x6604C8, Add, -900),# units:Build Time  index:80    from 2400 To 1500
        SetMemory(0x6604D8, Add, -900),# units:Build Time  index:88    from 2400 To 1500
        SetMemory(0x6604F4, Add, -4440),# units:Build Time  index:102    from 4800 To 360
        SetMemory(0x6604F8, Add, -1140),# units:Build Time  index:104    from 1500 To 360
        SetMemory(0x660500, Add, -39256064),# units:Build Time  index:109    from 600 To 1
        SetMemory(0x660504, Add, -78577664),# units:Build Time  index:111    from 1200 To 1
        SetMemory(0x660508, Add, -78577664),# units:Build Time  index:113    from 1200 To 1
        SetMemory(0x66050C, Add, -1049),# units:Build Time  index:114    from 1050 To 1
        SetMemory(0x660510, Add, -899),# units:Build Time  index:116    from 900 To 1
        SetMemory(0x66051C, Add, -899),# units:Build Time  index:122    from 900 To 1
        SetMemory(0x66051C, Add, -78577664),# units:Build Time  index:123    from 1200 To 1
        SetMemory(0x660520, Add, -29425664),# units:Build Time  index:125    from 450 To 1
        SetMemory(0x660524, Add, -4799),# units:Build Time  index:126    from 4800 To 1
        SetMemory(0x660524, Add, -58916864),# units:Build Time  index:127    from 900 To 1
        SetMemory(0x660534, Add, -39256064),# units:Build Time  index:135    from 600 To 1
        SetMemory(0x660538, Add, -899),# units:Build Time  index:136    from 900 To 1
        SetMemory(0x660538, Add, -117899264),# units:Build Time  index:137    from 1800 To 1
        SetMemory(0x66053C, Add, -899),# units:Build Time  index:138    from 900 To 1
        SetMemory(0x66053C, Add, -39256064),# units:Build Time  index:139    from 600 To 1
        SetMemory(0x660540, Add, -1199),# units:Build Time  index:140    from 1200 To 1
        SetMemory(0x660544, Add, -1199),# units:Build Time  index:142    from 1200 To 1
        SetMemory(0x660554, Add, 65536),# units:Build Time  index:151    from 0 To 1
        SetMemory(0x660558, Add, 1),# units:Build Time  index:152    from 0 To 1
        SetMemory(0x66055C, Add, -1799),# units:Build Time  index:154    from 1800 To 1
        SetMemory(0x66055C, Add, -78577664),# units:Build Time  index:155    from 1200 To 1
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
        SetMemory(0x6637DC, Add, -2),# units:Staredit Group Flags  index:60    from 12 To 10
        SetMemory(0x6637DC, Add, -512),# units:Staredit Group Flags  index:61    from 12 To 10
        SetMemory(0x6637DC, Add, -33554432),# units:Staredit Group Flags  index:63    from 12 To 10
        SetMemory(0x6637E0, Add, -512),# units:Staredit Group Flags  index:65    from 12 To 10
        SetMemory(0x6637E0, Add, -131072),# units:Staredit Group Flags  index:66    from 12 To 10
        SetMemory(0x6637E0, Add, -33554432),# units:Staredit Group Flags  index:67    from 12 To 10
        SetMemory(0x6637E4, Add, -2),# units:Staredit Group Flags  index:68    from 12 To 10
        SetMemory(0x6637E4, Add, -131072),# units:Staredit Group Flags  index:70    from 12 To 10
        SetMemory(0x6637E4, Add, -33554432),# units:Staredit Group Flags  index:71    from 12 To 10
        SetMemory(0x6637E8, Add, -131072),# units:Staredit Group Flags  index:74    from 12 To 10
        SetMemory(0x6637E8, Add, -33554432),# units:Staredit Group Flags  index:75    from 12 To 10
        SetMemory(0x6637EC, Add, -2),# units:Staredit Group Flags  index:76    from 12 To 10
        SetMemory(0x6637EC, Add, -512),# units:Staredit Group Flags  index:77    from 12 To 10
        SetMemory(0x6637EC, Add, -131072),# units:Staredit Group Flags  index:78    from 12 To 10
        SetMemory(0x6637EC, Add, -33554432),# units:Staredit Group Flags  index:79    from 12 To 10
        SetMemory(0x6637F0, Add, -2),# units:Staredit Group Flags  index:80    from 12 To 10
        SetMemory(0x6637F4, Add, -33554432),# units:Staredit Group Flags  index:87    from 12 To 10
        SetMemory(0x6637F8, Add, -2),# units:Staredit Group Flags  index:88    from 12 To 10
        SetMemory(0x663808, Add, 1),# units:Staredit Group Flags  index:104    from 9 To 10
        SetMemory(0x66380C, Add, -2048),# units:Staredit Group Flags  index:109    from 18 To 10
        SetMemory(0x66380C, Add, -671088640),# units:Staredit Group Flags  index:111    from 50 To 10
        SetMemory(0x663810, Add, -10240),# units:Staredit Group Flags  index:113    from 50 To 10
        SetMemory(0x663810, Add, -2621440),# units:Staredit Group Flags  index:114    from 50 To 10
        SetMemory(0x663814, Add, -8),# units:Staredit Group Flags  index:116    from 18 To 10
        SetMemory(0x663818, Add, -524288),# units:Staredit Group Flags  index:122    from 18 To 10
        SetMemory(0x663818, Add, -134217728),# units:Staredit Group Flags  index:123    from 18 To 10
        SetMemory(0x66381C, Add, -2048),# units:Staredit Group Flags  index:125    from 18 To 10
        SetMemory(0x66381C, Add, -524288),# units:Staredit Group Flags  index:126    from 18 To 10
        SetMemory(0x66381C, Add, -134217728),# units:Staredit Group Flags  index:127    from 18 To 10
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
        SetMemory(0x663838, Add, -704643072),# units:Staredit Group Flags  index:155    from 52 To 10
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
        SetMemory(0x664734, Add, -4096),# units:Supply Provided  index:109    from 16 To 0
        SetMemory(0x664760, Add, -1179648),# units:Supply Provided  index:154    from 18 To 0
        SetMemory(0x663D24, Add, -134217728),# units:Supply Required  index:63    from 8 To 0
        SetMemory(0x663D4C, Add, 131072),# units:Supply Required  index:102    from 0 To 2
        SetMemory(0x663D50, Add, 2),# units:Supply Required  index:104    from 0 To 2
        SetMemory(0x66444C, Add, 4211081216),# units:Space Required  index:63    from 4 To 255
        SetMemory(0x664460, Add, -254),# units:Space Required  index:80    from 255 To 1
        SetMemory(0x664464, Add, -16777216),# units:Space Required  index:87    from 2 To 1
        SetMemory(0x664468, Add, -254),# units:Space Required  index:88    from 255 To 1
        SetMemory(0x664474, Add, -16646144),# units:Space Required  index:102    from 255 To 1
        SetMemory(0x66447C, Add, -65024),# units:Space Required  index:109    from 255 To 1
        SetMemory(0x66447C, Add, -4261412864),# units:Space Required  index:111    from 255 To 1
        SetMemory(0x664480, Add, -65024),# units:Space Required  index:113    from 255 To 1
        SetMemory(0x664480, Add, -16646144),# units:Space Required  index:114    from 255 To 1
        SetMemory(0x664484, Add, -254),# units:Space Required  index:116    from 255 To 1
        SetMemory(0x664488, Add, -16646144),# units:Space Required  index:122    from 255 To 1
        SetMemory(0x664488, Add, -4261412864),# units:Space Required  index:123    from 255 To 1
        SetMemory(0x66448C, Add, -65024),# units:Space Required  index:125    from 255 To 1
        SetMemory(0x66448C, Add, -16646144),# units:Space Required  index:126    from 255 To 1
        SetMemory(0x66448C, Add, -4261412864),# units:Space Required  index:127    from 255 To 1
        SetMemory(0x664494, Add, -4261412864),# units:Space Required  index:135    from 255 To 1
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
        SetMemory(0x6644A8, Add, -4261412864),# units:Space Required  index:155    from 255 To 1
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
        SetMemory(0x660A04, Add, -1024),# units:Space Provided  index:125    from 4 To 0
        SetMemory(0x663484, Add, -42598400),# units:Build Score  index:63    from 650 To 0
        SetMemory(0x6634D4, Add, 100),# units:Build Score  index:102    from 0 To 100
        SetMemory(0x6634D8, Add, 100),# units:Build Score  index:104    from 0 To 100
        SetMemory(0x6634E0, Add, -3276800),# units:Build Score  index:109    from 50 To 0
        SetMemory(0x6634E4, Add, -4915200),# units:Build Score  index:111    from 75 To 0
        SetMemory(0x6634E8, Add, -13107200),# units:Build Score  index:113    from 200 To 0
        SetMemory(0x6634EC, Add, -200),# units:Build Score  index:114    from 200 To 0
        SetMemory(0x6634F0, Add, -275),# units:Build Score  index:116    from 275 To 0
        SetMemory(0x6634FC, Add, -65),# units:Build Score  index:122    from 65 To 0
        SetMemory(0x6634FC, Add, -6553600),# units:Build Score  index:123    from 100 To 0
        SetMemory(0x663500, Add, -3276800),# units:Build Score  index:125    from 50 To 0
        SetMemory(0x663514, Add, -6553600),# units:Build Score  index:135    from 100 To 0
        SetMemory(0x663518, Add, -150),# units:Build Score  index:136    from 150 To 0
        SetMemory(0x663518, Add, -13107200),# units:Build Score  index:137    from 200 To 0
        SetMemory(0x66351C, Add, -175),# units:Build Score  index:138    from 175 To 0
        SetMemory(0x66351C, Add, -2621440),# units:Build Score  index:139    from 40 To 0
        SetMemory(0x663520, Add, -275),# units:Build Score  index:140    from 275 To 0
        SetMemory(0x663524, Add, -75),# units:Build Score  index:142    from 75 To 0
        SetMemory(0x66353C, Add, -400),# units:Build Score  index:154    from 400 To 0
        SetMemory(0x66353C, Add, -19660800),# units:Build Score  index:155    from 300 To 0
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
        SetMemory(0x663F34, Add, 183500800),# units:Destroy Score  index:63    from 1300 To 4100
        SetMemory(0x663F58, Add, 1400),# units:Destroy Score  index:80    from 2600 To 4000
        SetMemory(0x663F64, Add, 170393600),# units:Destroy Score  index:87    from 1400 To 4000
        SetMemory(0x663F68, Add, 1600),# units:Destroy Score  index:88    from 2400 To 4000
        SetMemory(0x663F7C, Add, 216268800),# units:Destroy Score  index:99    from 700 To 4000
        SetMemory(0x663F80, Add, 3300),# units:Destroy Score  index:100    from 700 To 4000
        SetMemory(0x663F84, Add, -4600),# units:Destroy Score  index:102    from 4800 To 200
        SetMemory(0x663F88, Add, -500),# units:Destroy Score  index:104    from 700 To 200
        SetMemory(0x663F90, Add, -9175040),# units:Destroy Score  index:109    from 150 To 10
        SetMemory(0x663F94, Add, -14090240),# units:Destroy Score  index:111    from 225 To 10
        SetMemory(0x663F98, Add, -38666240),# units:Destroy Score  index:113    from 600 To 10
        SetMemory(0x663F9C, Add, -590),# units:Destroy Score  index:114    from 600 To 10
        SetMemory(0x663FA0, Add, -815),# units:Destroy Score  index:116    from 825 To 10
        SetMemory(0x663FAC, Add, -185),# units:Destroy Score  index:122    from 195 To 10
        SetMemory(0x663FAC, Add, -19005440),# units:Destroy Score  index:123    from 300 To 10
        SetMemory(0x663FB0, Add, -9175040),# units:Destroy Score  index:125    from 150 To 10
        SetMemory(0x663FB4, Add, -4990),# units:Destroy Score  index:126    from 5000 To 10
        SetMemory(0x663FB4, Add, -327024640),# units:Destroy Score  index:127    from 5000 To 10
        SetMemory(0x663FC4, Add, -19005440),# units:Destroy Score  index:135    from 300 To 10
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
        SetMemory(0x663FEC, Add, -58327040),# units:Destroy Score  index:155    from 900 To 10
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
        SetMemory(0x660714, Add, -16777216),# units:Broodwar Unit Flag  index:63    from 1 To 0
        SetMemory(0x660730, Add, -1),# units:Broodwar Unit Flag  index:88    from 1 To 0
        SetMemory(0x660738, Add, -16777216),# units:Broodwar Unit Flag  index:99    from 1 To 0
        SetMemory(0x66073C, Add, -1),# units:Broodwar Unit Flag  index:100    from 1 To 0
        SetMemory(0x660740, Add, -1),# units:Broodwar Unit Flag  index:104    from 1 To 0
        SetMemory(0x660784, Add, -16777216),# units:Broodwar Unit Flag  index:175    from 1 To 0
        SetMemory(0x66154C, Add, 30081024),# units:Staredit Availability Flags  index:27    from 4 To 463
        SetMemory(0x661550, Add, 8),# units:Staredit Availability Flags  index:28    from 455 To 463
        SetMemory(0x661550, Add, 524288),# units:Staredit Availability Flags  index:29    from 455 To 463
        SetMemory(0x661594, Add, -33554432),# units:Staredit Availability Flags  index:63    from 967 To 455
        SetMemory(0x6615C4, Add, 29556736),# units:Staredit Availability Flags  index:87    from 4 To 455
        SetMemory(0x6615C8, Add, -512),# units:Staredit Availability Flags  index:88    from 967 To 455
        SetMemory(0x6615DC, Add, -33554432),# units:Staredit Availability Flags  index:99    from 967 To 455
        SetMemory(0x6615E0, Add, -512),# units:Staredit Availability Flags  index:100    from 967 To 455
        SetMemory(0x6615E4, Add, 459),# units:Staredit Availability Flags  index:102    from 4 To 463
        SetMemory(0x6615E8, Add, -504),# units:Staredit Availability Flags  index:104    from 967 To 463
        SetMemory(0x661614, Add, 8),# units:Staredit Availability Flags  index:126    from 455 To 463
        SetMemory(0x661614, Add, 524288),# units:Staredit Availability Flags  index:127    from 455 To 463
        SetMemory(0x66162C, Add, 0),# units:Staredit Availability Flags  index:139    from 463 To 463
        SetMemory(0x661630, Add, 0),# units:Staredit Availability Flags  index:140    from 463 To 463
        SetMemory(0x661634, Add, 0),# units:Staredit Availability Flags  index:142    from 463 To 463
        SetMemory(0x66163C, Add, 524288),# units:Staredit Availability Flags  index:147    from 455 To 463
        SetMemory(0x661640, Add, 8),# units:Staredit Availability Flags  index:148    from 455 To 463
        SetMemory(0x661644, Add, 524288),# units:Staredit Availability Flags  index:151    from 455 To 463
        SetMemory(0x661648, Add, 8),# units:Staredit Availability Flags  index:152    from 455 To 463
        SetMemory(0x66164C, Add, 0),# units:Staredit Availability Flags  index:154    from 463 To 463
        SetMemory(0x66164C, Add, 0),# units:Staredit Availability Flags  index:155    from 463 To 463
        SetMemory(0x661654, Add, 0),# units:Staredit Availability Flags  index:159    from 463 To 463
        SetMemory(0x661658, Add, 0),# units:Staredit Availability Flags  index:160    from 463 To 463
        SetMemory(0x66165C, Add, 0),# units:Staredit Availability Flags  index:163    from 463 To 463
        SetMemory(0x661660, Add, 0),# units:Staredit Availability Flags  index:164    from 463 To 463
        SetMemory(0x661660, Add, 0),# units:Staredit Availability Flags  index:165    from 463 To 463
        SetMemory(0x661664, Add, 0),# units:Staredit Availability Flags  index:166    from 463 To 463
        SetMemory(0x661664, Add, 0),# units:Staredit Availability Flags  index:167    from 463 To 463
        SetMemory(0x661668, Add, 8),# units:Staredit Availability Flags  index:168    from 455 To 463
        SetMemory(0x661668, Add, 0),# units:Staredit Availability Flags  index:169    from 463 To 463
        SetMemory(0x66166C, Add, 0),# units:Staredit Availability Flags  index:170    from 463 To 463
        SetMemory(0x66166C, Add, 0),# units:Staredit Availability Flags  index:171    from 463 To 463
        SetMemory(0x661670, Add, 0),# units:Staredit Availability Flags  index:172    from 463 To 463
        SetMemory(0x661670, Add, 524288),# units:Staredit Availability Flags  index:173    from 455 To 463
        SetMemory(0x661674, Add, 8),# units:Staredit Availability Flags  index:174    from 455 To 463
        SetMemory(0x661674, Add, -33030144),# units:Staredit Availability Flags  index:175    from 967 To 463
        SetMemory(0x6572E0, Add, 4),# weapons:Label  index:0    from 229 To 233
        SetMemory(0x6572E0, Add, 131072),# weapons:Label  index:1    from 230 To 232
        SetMemory(0x6572E4, Add, 1),# weapons:Label  index:2    from 231 To 232
        SetMemory(0x6572E4, Add, -65536),# weapons:Label  index:3    from 232 To 231
        SetMemory(0x6572E8, Add, -2),# weapons:Label  index:4    from 233 To 231
        SetMemory(0x6572E8, Add, -262144),# weapons:Label  index:5    from 234 To 230
        SetMemory(0x6572EC, Add, -327680),# weapons:Label  index:7    from 235 To 230
        SetMemory(0x6572F0, Add, -2),# weapons:Label  index:8    from 236 To 234
        SetMemory(0x6572F0, Add, -458752),# weapons:Label  index:9    from 237 To 230
        SetMemory(0x6572F4, Add, 7),# weapons:Label  index:10    from 238 To 245
        SetMemory(0x6572F4, Add, -655360),# weapons:Label  index:11    from 239 To 229
        SetMemory(0x6572F8, Add, -11),# weapons:Label  index:12    from 240 To 229
        SetMemory(0x6572FC, Add, -655360),# weapons:Label  index:15    from 243 To 233
        SetMemory(0x657300, Add, -15),# weapons:Label  index:16    from 244 To 229
        SetMemory(0x657300, Add, 65536),# weapons:Label  index:17    from 245 To 246
        SetMemory(0x657304, Add, -17),# weapons:Label  index:18    from 246 To 229
        SetMemory(0x657304, Add, -1179648),# weapons:Label  index:19    from 247 To 229
        SetMemory(0x657308, Add, -10),# weapons:Label  index:20    from 248 To 238
        SetMemory(0x657308, Add, -720896),# weapons:Label  index:21    from 249 To 238
        SetMemory(0x65730C, Add, -12),# weapons:Label  index:22    from 250 To 238
        SetMemory(0x65730C, Add, -917504),# weapons:Label  index:23    from 251 To 237
        SetMemory(0x657310, Add, -15),# weapons:Label  index:24    from 252 To 237
        SetMemory(0x657310, Add, -1114112),# weapons:Label  index:25    from 253 To 236
        SetMemory(0x657314, Add, -18),# weapons:Label  index:26    from 254 To 236
        SetMemory(0x657314, Add, -1245184),# weapons:Label  index:27    from 255 To 236
        SetMemory(0x657318, Add, -21),# weapons:Label  index:28    from 256 To 235
        SetMemory(0x657318, Add, -1441792),# weapons:Label  index:29    from 257 To 235
        SetMemory(0x657324, Add, -1638400),# weapons:Label  index:35    from 260 To 235
        SetMemory(0x657328, Add, -26),# weapons:Label  index:36    from 261 To 235
        SetMemory(0x657328, Add, -1769472),# weapons:Label  index:37    from 262 To 235
        SetMemory(0x65732C, Add, -20),# weapons:Label  index:38    from 263 To 243
        SetMemory(0x65732C, Add, -1376256),# weapons:Label  index:39    from 264 To 243
        SetMemory(0x657330, Add, -22),# weapons:Label  index:40    from 265 To 243
        SetMemory(0x657330, Add, -1572864),# weapons:Label  index:41    from 266 To 242
        SetMemory(0x657334, Add, -25),# weapons:Label  index:42    from 267 To 242
        SetMemory(0x657334, Add, -2293760),# weapons:Label  index:43    from 268 To 233
        SetMemory(0x657338, Add, -35),# weapons:Label  index:44    from 268 To 233
        SetMemory(0x65733C, Add, -30),# weapons:Label  index:46    from 271 To 241
        SetMemory(0x65733C, Add, -2031616),# weapons:Label  index:47    from 272 To 241
        SetMemory(0x657340, Add, -32),# weapons:Label  index:48    from 273 To 241
        SetMemory(0x657340, Add, -2228224),# weapons:Label  index:49    from 274 To 240
        SetMemory(0x657344, Add, -35),# weapons:Label  index:50    from 275 To 240
        SetMemory(0x657344, Add, -2359296),# weapons:Label  index:51    from 276 To 240
        SetMemory(0x657348, Add, -38),# weapons:Label  index:52    from 278 To 240
        SetMemory(0x657348, Add, -2555904),# weapons:Label  index:53    from 279 To 240
        SetMemory(0x657364, Add, -47),# weapons:Label  index:66    from 286 To 239
        SetMemory(0x657364, Add, -3145728),# weapons:Label  index:67    from 287 To 239
        SetMemory(0x657368, Add, -49),# weapons:Label  index:68    from 288 To 239
        SetMemory(0x657368, Add, -2949120),# weapons:Label  index:69    from 289 To 244
        SetMemory(0x65736C, Add, -46),# weapons:Label  index:70    from 290 To 244
        SetMemory(0x65736C, Add, -3080192),# weapons:Label  index:71    from 291 To 244
        SetMemory(0x656CA8, Add, 23),# weapons:Graphics  index:0    from 142 To 165
        SetMemory(0x656CB4, Add, 19),# weapons:Graphics  index:3    from 143 To 162
        SetMemory(0x656CB8, Add, 10),# weapons:Graphics  index:4    from 145 To 155
        SetMemory(0x656CBC, Add, 6),# weapons:Graphics  index:5    from 145 To 151
        SetMemory(0x656CC4, Add, 18),# weapons:Graphics  index:7    from 142 To 160
        SetMemory(0x656CC8, Add, 12),# weapons:Graphics  index:8    from 146 To 158
        SetMemory(0x656CCC, Add, 64),# weapons:Graphics  index:9    from 142 To 206
        SetMemory(0x656CD0, Add, 12),# weapons:Graphics  index:10    from 146 To 158
        SetMemory(0x656CD8, Add, -1),# weapons:Graphics  index:12    from 143 To 142
        SetMemory(0x656CE4, Add, 22),# weapons:Graphics  index:15    from 144 To 166
        SetMemory(0x656CE8, Add, 0),# weapons:Graphics  index:16    from 149 To 149
        SetMemory(0x656CEC, Add, 14),# weapons:Graphics  index:17    from 144 To 158
        SetMemory(0x656CF4, Add, 2),# weapons:Graphics  index:19    from 148 To 150
        SetMemory(0x656CFC, Add, -148),# weapons:Graphics  index:21    from 148 To 0
        SetMemory(0x656D00, Add, 7),# weapons:Graphics  index:22    from 148 To 155
        SetMemory(0x656D04, Add, 19),# weapons:Graphics  index:23    from 148 To 167
        SetMemory(0x656D0C, Add, -172),# weapons:Graphics  index:25    from 172 To 0
        SetMemory(0x656D10, Add, -172),# weapons:Graphics  index:26    from 172 To 0
        SetMemory(0x656D14, Add, 12),# weapons:Graphics  index:27    from 150 To 162
        SetMemory(0x656D18, Add, 54),# weapons:Graphics  index:28    from 150 To 204
        SetMemory(0x656D1C, Add, -146),# weapons:Graphics  index:29    from 146 To 0
        SetMemory(0x656D34, Add, 163),# weapons:Graphics  index:35    from 0 To 163
        SetMemory(0x656D38, Add, 204),# weapons:Graphics  index:36    from 0 To 204
        SetMemory(0x656D3C, Add, 160),# weapons:Graphics  index:37    from 0 To 160
        SetMemory(0x656D40, Add, 33),# weapons:Graphics  index:38    from 171 To 204
        SetMemory(0x656D44, Add, -6),# weapons:Graphics  index:39    from 171 To 165
        SetMemory(0x656D48, Add, 154),# weapons:Graphics  index:40    from 0 To 154
        SetMemory(0x656D4C, Add, 206),# weapons:Graphics  index:41    from 0 To 206
        SetMemory(0x656D50, Add, 155),# weapons:Graphics  index:42    from 0 To 155
        SetMemory(0x656D54, Add, -10),# weapons:Graphics  index:43    from 171 To 161
        SetMemory(0x656D58, Add, 0),# weapons:Graphics  index:44    from 171 To 171
        SetMemory(0x656D68, Add, -2),# weapons:Graphics  index:48    from 165 To 163
        SetMemory(0x656D74, Add, -11),# weapons:Graphics  index:51    from 162 To 151
        SetMemory(0x656D78, Add, -7),# weapons:Graphics  index:52    from 166 To 159
        SetMemory(0x656D7C, Add, -2),# weapons:Graphics  index:53    from 161 To 159
        SetMemory(0x656DB0, Add, 2),# weapons:Graphics  index:66    from 159 To 161
        SetMemory(0x656DB4, Add, 12),# weapons:Graphics  index:67    from 159 To 171
        SetMemory(0x656DB8, Add, 23),# weapons:Graphics  index:68    from 143 To 166
        SetMemory(0x656DBC, Add, 18),# weapons:Graphics  index:69    from 143 To 161
        SetMemory(0x656DC0, Add, 15),# weapons:Graphics  index:70    from 156 To 171
        SetMemory(0x656DC4, Add, 10),# weapons:Graphics  index:71    from 156 To 166
        SetMemory(0x657998, Add, -1),# weapons:Target Flags  index:0    from 3 To 2
        SetMemory(0x657998, Add, -65536),# weapons:Target Flags  index:1    from 3 To 2
        SetMemory(0x65799C, Add, -1),# weapons:Target Flags  index:2    from 3 To 2
        SetMemory(0x65799C, Add, -65536),# weapons:Target Flags  index:3    from 3 To 2
        SetMemory(0x6579A0, Add, 0),# weapons:Target Flags  index:4    from 2 To 2
        SetMemory(0x6579A0, Add, 0),# weapons:Target Flags  index:5    from 2 To 2
        SetMemory(0x6579A4, Add, 0),# weapons:Target Flags  index:7    from 2 To 2
        SetMemory(0x6579A8, Add, 1),# weapons:Target Flags  index:8    from 1 To 2
        SetMemory(0x6579A8, Add, 0),# weapons:Target Flags  index:9    from 2 To 2
        SetMemory(0x6579AC, Add, 1),# weapons:Target Flags  index:10    from 1 To 2
        SetMemory(0x6579AC, Add, 0),# weapons:Target Flags  index:11    from 2 To 2
        SetMemory(0x6579B0, Add, 0),# weapons:Target Flags  index:12    from 2 To 2
        SetMemory(0x6579B4, Add, 65536),# weapons:Target Flags  index:15    from 1 To 2
        SetMemory(0x6579B8, Add, 0),# weapons:Target Flags  index:16    from 2 To 2
        SetMemory(0x6579B8, Add, 65536),# weapons:Target Flags  index:17    from 1 To 2
        SetMemory(0x6579BC, Add, 0),# weapons:Target Flags  index:18    from 2 To 2
        SetMemory(0x6579BC, Add, 0),# weapons:Target Flags  index:19    from 2 To 2
        SetMemory(0x6579C0, Add, 1),# weapons:Target Flags  index:20    from 1 To 2
        SetMemory(0x6579C0, Add, 0),# weapons:Target Flags  index:21    from 2 To 2
        SetMemory(0x6579C4, Add, 1),# weapons:Target Flags  index:22    from 1 To 2
        SetMemory(0x6579C4, Add, 0),# weapons:Target Flags  index:23    from 2 To 2
        SetMemory(0x6579C8, Add, 1),# weapons:Target Flags  index:24    from 1 To 2
        SetMemory(0x6579C8, Add, 0),# weapons:Target Flags  index:25    from 2 To 2
        SetMemory(0x6579CC, Add, 0),# weapons:Target Flags  index:26    from 2 To 2
        SetMemory(0x6579CC, Add, 0),# weapons:Target Flags  index:27    from 2 To 2
        SetMemory(0x6579D0, Add, 0),# weapons:Target Flags  index:28    from 2 To 2
        SetMemory(0x6579D0, Add, 65536),# weapons:Target Flags  index:29    from 1 To 2
        SetMemory(0x6579DC, Add, 0),# weapons:Target Flags  index:35    from 2 To 2
        SetMemory(0x6579E0, Add, 0),# weapons:Target Flags  index:36    from 2 To 2
        SetMemory(0x6579E0, Add, 0),# weapons:Target Flags  index:37    from 2 To 2
        SetMemory(0x6579E4, Add, -1),# weapons:Target Flags  index:38    from 3 To 2
        SetMemory(0x6579E4, Add, -65536),# weapons:Target Flags  index:39    from 3 To 2
        SetMemory(0x6579F8, Add, -1),# weapons:Target Flags  index:48    from 3 To 2
        SetMemory(0x6579F8, Add, -65536),# weapons:Target Flags  index:49    from 3 To 2
        SetMemory(0x657A00, Add, 1),# weapons:Target Flags  index:52    from 1 To 2
        SetMemory(0x657A00, Add, 0),# weapons:Target Flags  index:53    from 2 To 2
        SetMemory(0x657A20, Add, 1),# weapons:Target Flags  index:68    from 2 To 3
        SetMemory(0x657A24, Add, -1),# weapons:Target Flags  index:70    from 3 To 2
        SetMemory(0x657A24, Add, -65536),# weapons:Target Flags  index:71    from 3 To 2
        SetMemory(0x657580, Add, 32),# weapons:Maximum Range  index:68    from 96 To 128
        SetMemory(0x657588, Add, 32),# weapons:Maximum Range  index:70    from 64 To 96
        SetMemory(0x65758C, Add, 32),# weapons:Maximum Range  index:71    from 64 To 96
        SetMemory(0x6571D0, Add, -2),# weapons:Damage Upgrade  index:0    from 7 To 5
        SetMemory(0x6571D0, Add, -512),# weapons:Damage Upgrade  index:1    from 7 To 5
        SetMemory(0x6571D0, Add, -131072),# weapons:Damage Upgrade  index:2    from 7 To 5
        SetMemory(0x6571D0, Add, -33554432),# weapons:Damage Upgrade  index:3    from 7 To 5
        SetMemory(0x6571D4, Add, -3),# weapons:Damage Upgrade  index:4    from 8 To 5
        SetMemory(0x6571D4, Add, -768),# weapons:Damage Upgrade  index:5    from 8 To 5
        SetMemory(0x6571D4, Add, -50331648),# weapons:Damage Upgrade  index:7    from 8 To 5
        SetMemory(0x6571D8, Add, -3),# weapons:Damage Upgrade  index:8    from 8 To 5
        SetMemory(0x6571D8, Add, -768),# weapons:Damage Upgrade  index:9    from 8 To 5
        SetMemory(0x6571D8, Add, -327680),# weapons:Damage Upgrade  index:10    from 8 To 3
        SetMemory(0x6571D8, Add, -50331648),# weapons:Damage Upgrade  index:11    from 8 To 5
        SetMemory(0x6571DC, Add, -3),# weapons:Damage Upgrade  index:12    from 8 To 5
        SetMemory(0x6571DC, Add, -67108864),# weapons:Damage Upgrade  index:15    from 9 To 5
        SetMemory(0x6571E0, Add, -4),# weapons:Damage Upgrade  index:16    from 9 To 5
        SetMemory(0x6571E0, Add, -1280),# weapons:Damage Upgrade  index:17    from 9 To 4
        SetMemory(0x6571E0, Add, -262144),# weapons:Damage Upgrade  index:18    from 9 To 5
        SetMemory(0x6571E0, Add, -67108864),# weapons:Damage Upgrade  index:19    from 9 To 5
        SetMemory(0x6571E4, Add, -5),# weapons:Damage Upgrade  index:20    from 9 To 4
        SetMemory(0x6571E4, Add, -1280),# weapons:Damage Upgrade  index:21    from 9 To 4
        SetMemory(0x6571E4, Add, -327680),# weapons:Damage Upgrade  index:22    from 9 To 4
        SetMemory(0x6571E4, Add, -83886080),# weapons:Damage Upgrade  index:23    from 9 To 4
        SetMemory(0x6571E8, Add, -5),# weapons:Damage Upgrade  index:24    from 9 To 4
        SetMemory(0x6571E8, Add, -768),# weapons:Damage Upgrade  index:25    from 7 To 4
        SetMemory(0x6571E8, Add, -196608),# weapons:Damage Upgrade  index:26    from 7 To 4
        SetMemory(0x6571E8, Add, -67108864),# weapons:Damage Upgrade  index:27    from 8 To 4
        SetMemory(0x6571EC, Add, -4),# weapons:Damage Upgrade  index:28    from 8 To 4
        SetMemory(0x6571EC, Add, -14336),# weapons:Damage Upgrade  index:29    from 60 To 4
        SetMemory(0x6571F0, Add, -100663296),# weapons:Damage Upgrade  index:35    from 10 To 4
        SetMemory(0x6571F4, Add, -6),# weapons:Damage Upgrade  index:36    from 10 To 4
        SetMemory(0x6571F4, Add, -1536),# weapons:Damage Upgrade  index:37    from 10 To 4
        SetMemory(0x6571F4, Add, -524288),# weapons:Damage Upgrade  index:38    from 11 To 3
        SetMemory(0x6571F4, Add, -134217728),# weapons:Damage Upgrade  index:39    from 11 To 3
        SetMemory(0x6571F8, Add, -7),# weapons:Damage Upgrade  index:40    from 10 To 3
        SetMemory(0x6571F8, Add, -1792),# weapons:Damage Upgrade  index:41    from 10 To 3
        SetMemory(0x6571F8, Add, -458752),# weapons:Damage Upgrade  index:42    from 10 To 3
        SetMemory(0x6571F8, Add, -922746880),# weapons:Damage Upgrade  index:43    from 60 To 5
        SetMemory(0x6571FC, Add, -55),# weapons:Damage Upgrade  index:44    from 60 To 5
        SetMemory(0x6571FC, Add, -589824),# weapons:Damage Upgrade  index:46    from 12 To 3
        SetMemory(0x6571FC, Add, -150994944),# weapons:Damage Upgrade  index:47    from 12 To 3
        SetMemory(0x657200, Add, -9),# weapons:Damage Upgrade  index:48    from 12 To 3
        SetMemory(0x657200, Add, -2304),# weapons:Damage Upgrade  index:49    from 12 To 3
        SetMemory(0x657200, Add, -524288),# weapons:Damage Upgrade  index:50    from 11 To 3
        SetMemory(0x657200, Add, -134217728),# weapons:Damage Upgrade  index:51    from 11 To 3
        SetMemory(0x657204, Add, -57),# weapons:Damage Upgrade  index:52    from 60 To 3
        SetMemory(0x657204, Add, -14592),# weapons:Damage Upgrade  index:53    from 60 To 3
        SetMemory(0x657210, Add, -589824),# weapons:Damage Upgrade  index:66    from 13 To 4
        SetMemory(0x657210, Add, -150994944),# weapons:Damage Upgrade  index:67    from 13 To 4
        SetMemory(0x657214, Add, -9),# weapons:Damage Upgrade  index:68    from 13 To 4
        SetMemory(0x657214, Add, -2560),# weapons:Damage Upgrade  index:69    from 13 To 3
        SetMemory(0x657214, Add, -655360),# weapons:Damage Upgrade  index:70    from 13 To 3
        SetMemory(0x657214, Add, -167772160),# weapons:Damage Upgrade  index:71    from 13 To 3
        SetMemory(0x657258, Add, -1),# weapons:Weapon Type  index:0    from 3 To 2
        SetMemory(0x657258, Add, -256),# weapons:Weapon Type  index:1    from 3 To 2
        SetMemory(0x65725C, Add, -16777216),# weapons:Weapon Type  index:7    from 3 To 2
        SetMemory(0x657260, Add, 1),# weapons:Weapon Type  index:8    from 1 To 2
        SetMemory(0x657260, Add, -256),# weapons:Weapon Type  index:9    from 3 To 2
        SetMemory(0x657260, Add, 131072),# weapons:Weapon Type  index:10    from 1 To 3
        SetMemory(0x657260, Add, 16777216),# weapons:Weapon Type  index:11    from 1 To 2
        SetMemory(0x657264, Add, 1),# weapons:Weapon Type  index:12    from 1 To 2
        SetMemory(0x657264, Add, 16777216),# weapons:Weapon Type  index:15    from 1 To 2
        SetMemory(0x657268, Add, -1),# weapons:Weapon Type  index:16    from 3 To 2
        SetMemory(0x657268, Add, -65536),# weapons:Weapon Type  index:18    from 3 To 2
        SetMemory(0x657268, Add, -16777216),# weapons:Weapon Type  index:19    from 3 To 2
        SetMemory(0x65726C, Add, -2),# weapons:Weapon Type  index:20    from 3 To 1
        SetMemory(0x65726C, Add, -512),# weapons:Weapon Type  index:21    from 3 To 1
        SetMemory(0x65726C, Add, -131072),# weapons:Weapon Type  index:22    from 3 To 1
        SetMemory(0x65726C, Add, -33554432),# weapons:Weapon Type  index:23    from 3 To 1
        SetMemory(0x657270, Add, -2),# weapons:Weapon Type  index:24    from 3 To 1
        SetMemory(0x657270, Add, -256),# weapons:Weapon Type  index:25    from 2 To 1
        SetMemory(0x657270, Add, -65536),# weapons:Weapon Type  index:26    from 2 To 1
        SetMemory(0x657278, Add, -33554432),# weapons:Weapon Type  index:35    from 3 To 1
        SetMemory(0x65727C, Add, -2),# weapons:Weapon Type  index:36    from 3 To 1
        SetMemory(0x65727C, Add, -512),# weapons:Weapon Type  index:37    from 3 To 1
        SetMemory(0x65727C, Add, 131072),# weapons:Weapon Type  index:38    from 1 To 3
        SetMemory(0x65727C, Add, 33554432),# weapons:Weapon Type  index:39    from 1 To 3
        SetMemory(0x657280, Add, -16777216),# weapons:Weapon Type  index:43    from 3 To 2
        SetMemory(0x657284, Add, -1),# weapons:Weapon Type  index:44    from 3 To 2
        SetMemory(0x657288, Add, 65536),# weapons:Weapon Type  index:50    from 2 To 3
        SetMemory(0x657288, Add, 16777216),# weapons:Weapon Type  index:51    from 2 To 3
        SetMemory(0x65728C, Add, 512),# weapons:Weapon Type  index:53    from 1 To 3
        SetMemory(0x65729C, Add, -2),# weapons:Weapon Type  index:68    from 3 To 1
        SetMemory(0x656670, Add, -1),# weapons:Weapon Behavior  index:0    from 2 To 1
        SetMemory(0x656670, Add, 0),# weapons:Weapon Behavior  index:3    from 2 To 2
        SetMemory(0x656674, Add, 2),# weapons:Weapon Behavior  index:4    from 0 To 2
        SetMemory(0x656674, Add, 512),# weapons:Weapon Behavior  index:5    from 0 To 2
        SetMemory(0x656678, Add, 0),# weapons:Weapon Behavior  index:8    from 1 To 1
        SetMemory(0x656678, Add, 0),# weapons:Weapon Behavior  index:9    from 2 To 2
        SetMemory(0x656678, Add, 0),# weapons:Weapon Behavior  index:10    from 1 To 1
        SetMemory(0x65667C, Add, 16777216),# weapons:Weapon Behavior  index:15    from 0 To 1
        SetMemory(0x656680, Add, 256),# weapons:Weapon Behavior  index:17    from 0 To 1
        SetMemory(0x656680, Add, 33554432),# weapons:Weapon Behavior  index:19    from 0 To 2
        SetMemory(0x656684, Add, 1),# weapons:Weapon Behavior  index:20    from 0 To 1
        SetMemory(0x656684, Add, 65536),# weapons:Weapon Behavior  index:22    from 0 To 1
        SetMemory(0x656684, Add, 16777216),# weapons:Weapon Behavior  index:23    from 0 To 1
        SetMemory(0x656688, Add, 1),# weapons:Weapon Behavior  index:24    from 0 To 1
        SetMemory(0x656688, Add, -1280),# weapons:Weapon Behavior  index:25    from 5 To 0
        SetMemory(0x656688, Add, -327680),# weapons:Weapon Behavior  index:26    from 5 To 0
        SetMemory(0x656688, Add, -16777216),# weapons:Weapon Behavior  index:27    from 2 To 1
        SetMemory(0x65668C, Add, -256),# weapons:Weapon Behavior  index:29    from 1 To 0
        SetMemory(0x656690, Add, -67108864),# weapons:Weapon Behavior  index:35    from 5 To 1
        SetMemory(0x656694, Add, -4),# weapons:Weapon Behavior  index:36    from 5 To 1
        SetMemory(0x656694, Add, -768),# weapons:Weapon Behavior  index:37    from 5 To 2
        SetMemory(0x656694, Add, -65536),# weapons:Weapon Behavior  index:38    from 2 To 1
        SetMemory(0x656698, Add, -4),# weapons:Weapon Behavior  index:40    from 5 To 1
        SetMemory(0x656698, Add, -768),# weapons:Weapon Behavior  index:41    from 5 To 2
        SetMemory(0x656698, Add, -262144),# weapons:Weapon Behavior  index:42    from 5 To 1
        SetMemory(0x656698, Add, -16777216),# weapons:Weapon Behavior  index:43    from 2 To 1
        SetMemory(0x65669C, Add, 65536),# weapons:Weapon Behavior  index:46    from 1 To 2
        SetMemory(0x6566A0, Add, -6),# weapons:Weapon Behavior  index:48    from 7 To 1
        SetMemory(0x6566A0, Add, -1280),# weapons:Weapon Behavior  index:49    from 7 To 2
        SetMemory(0x6566A0, Add, 65536),# weapons:Weapon Behavior  index:50    from 0 To 1
        SetMemory(0x6566A0, Add, 67108864),# weapons:Weapon Behavior  index:51    from 0 To 4
        SetMemory(0x6566B0, Add, 0),# weapons:Weapon Behavior  index:66    from 1 To 1
        SetMemory(0x6566B0, Add, 16777216),# weapons:Weapon Behavior  index:67    from 1 To 2
        SetMemory(0x6566B4, Add, -1),# weapons:Weapon Behavior  index:68    from 2 To 1
        SetMemory(0x6566B4, Add, -256),# weapons:Weapon Behavior  index:69    from 2 To 1
        SetMemory(0x6566B4, Add, 0),# weapons:Weapon Behavior  index:70    from 2 To 2
        SetMemory(0x6566B4, Add, -16777216),# weapons:Weapon Behavior  index:71    from 2 To 1
        SetMemory(0x657048, Add, 225),# weapons:Remove After  index:8    from 30 To 255
        SetMemory(0x657048, Add, 14745600),# weapons:Remove After  index:10    from 30 To 255
        SetMemory(0x65704C, Add, 0),# weapons:Remove After  index:15    from 255 To 255
        SetMemory(0x657068, Add, 0),# weapons:Remove After  index:43    from 255 To 255
        SetMemory(0x65706C, Add, 0),# weapons:Remove After  index:44    from 255 To 255
        SetMemory(0x657084, Add, 0),# weapons:Remove After  index:68    from 255 To 255
        SetMemory(0x65673C, Add, -131072),# weapons:Explosion Type  index:70    from 3 To 1
        SetMemory(0x65673C, Add, -33554432),# weapons:Explosion Type  index:71    from 3 To 1
        SetMemory(0x656914, Add, -3),# weapons:Inner Splash Range  index:70    from 3 To 0
        SetMemory(0x656914, Add, -196608),# weapons:Inner Splash Range  index:71    from 3 To 0
        SetMemory(0x657154, Add, -15),# weapons:Medium Splash Range  index:70    from 15 To 0
        SetMemory(0x657154, Add, -983040),# weapons:Medium Splash Range  index:71    from 15 To 0
        SetMemory(0x65780C, Add, -30),# weapons:Outer Splash Range  index:70    from 30 To 0
        SetMemory(0x65780C, Add, -1966080),# weapons:Outer Splash Range  index:71    from 30 To 0
        SetMemory(0x656F34, Add, -1638400),# weapons:Damage Amount  index:67    from 45 To 20
        SetMemory(0x656F38, Add, 15),# weapons:Damage Amount  index:68    from 5 To 20
        SetMemory(0x656F3C, Add, -10),# weapons:Damage Amount  index:70    from 30 To 20
        SetMemory(0x656F3C, Add, -2621440),# weapons:Damage Amount  index:71    from 60 To 20
        SetMemory(0x657700, Add, 1),# weapons:Damage Bonus  index:68    from 1 To 2
        SetMemory(0x657704, Add, -2),# weapons:Damage Bonus  index:70    from 3 To 1
        SetMemory(0x657704, Add, -131072),# weapons:Damage Bonus  index:71    from 3 To 1
        SetMemory(0x656FF8, Add, 134217728),# weapons:Weapon Cooldown  index:67    from 22 To 30
        SetMemory(0x656FFC, Add, 131072),# weapons:Weapon Cooldown  index:70    from 20 To 22
        SetMemory(0x656FFC, Add, 33554432),# weapons:Weapon Cooldown  index:71    from 20 To 22
        SetMemory(0x6564E8, Add, -1),# weapons:Damage Factor  index:8    from 2 To 1
        SetMemory(0x6564E8, Add, -65536),# weapons:Damage Factor  index:10    from 2 To 1
        SetMemory(0x656990, Add, 0),# weapons:Attack Angle  index:3    from 16 To 16
        SetMemory(0x656994, Add, -32),# weapons:Attack Angle  index:4    from 64 To 32
        SetMemory(0x656994, Add, -8192),# weapons:Attack Angle  index:5    from 64 To 32
        SetMemory(0x656994, Add, 268435456),# weapons:Attack Angle  index:7    from 16 To 32
        SetMemory(0x656998, Add, 4096),# weapons:Attack Angle  index:9    from 16 To 32
        SetMemory(0x65699C, Add, 16),# weapons:Attack Angle  index:12    from 16 To 32
        SetMemory(0x65699C, Add, 268435456),# weapons:Attack Angle  index:15    from 16 To 32
        SetMemory(0x6569AC, Add, 16),# weapons:Attack Angle  index:28    from 16 To 32
        SetMemory(0x6569B4, Add, 1048576),# weapons:Attack Angle  index:38    from 16 To 32
        SetMemory(0x6569C4, Add, -96),# weapons:Attack Angle  index:52    from 128 To 32
        SetMemory(0x6569C4, Add, -24576),# weapons:Attack Angle  index:53    from 128 To 32
        SetMemory(0x6569D0, Add, -6291456),# weapons:Attack Angle  index:66    from 128 To 32
        SetMemory(0x6569D0, Add, -1610612736),# weapons:Attack Angle  index:67    from 128 To 32
        SetMemory(0x6569D4, Add, 16),# weapons:Attack Angle  index:68    from 16 To 32
        SetMemory(0x657890, Add, -64),# weapons:Launch Spin  index:8    from 64 To 0
        SetMemory(0x657890, Add, -4194304),# weapons:Launch Spin  index:10    from 64 To 0
        SetMemory(0x657914, Add, -20),# weapons:Forward Offset  index:4    from 20 To 0
        SetMemory(0x657914, Add, -5120),# weapons:Forward Offset  index:5    from 20 To 0
        SetMemory(0x657918, Add, -5),# weapons:Forward Offset  index:8    from 5 To 0
        SetMemory(0x657918, Add, -327680),# weapons:Forward Offset  index:10    from 5 To 0
        SetMemory(0x65791C, Add, -335544320),# weapons:Forward Offset  index:15    from 20 To 0
        SetMemory(0x657920, Add, -45),# weapons:Forward Offset  index:16    from 45 To 0
        SetMemory(0x657920, Add, -5120),# weapons:Forward Offset  index:17    from 20 To 0
        SetMemory(0x657920, Add, -2949120),# weapons:Forward Offset  index:18    from 45 To 0
        SetMemory(0x657920, Add, -1258291200),# weapons:Forward Offset  index:19    from 75 To 0
        SetMemory(0x657924, Add, -75),# weapons:Forward Offset  index:20    from 75 To 0
        SetMemory(0x657924, Add, -19200),# weapons:Forward Offset  index:21    from 75 To 0
        SetMemory(0x657924, Add, -4915200),# weapons:Forward Offset  index:22    from 75 To 0
        SetMemory(0x657924, Add, -1258291200),# weapons:Forward Offset  index:23    from 75 To 0
        SetMemory(0x657928, Add, -75),# weapons:Forward Offset  index:24    from 75 To 0
        SetMemory(0x657928, Add, -5120),# weapons:Forward Offset  index:25    from 20 To 0
        SetMemory(0x657928, Add, -1310720),# weapons:Forward Offset  index:26    from 20 To 0
        SetMemory(0x65792C, Add, -2560),# weapons:Forward Offset  index:29    from 10 To 0
        SetMemory(0x657938, Add, -327680),# weapons:Forward Offset  index:42    from 5 To 0
        SetMemory(0x657940, Add, -5),# weapons:Forward Offset  index:48    from 5 To 0
        SetMemory(0x657940, Add, -1280),# weapons:Forward Offset  index:49    from 5 To 0
        SetMemory(0x657940, Add, -1638400),# weapons:Forward Offset  index:50    from 25 To 0
        SetMemory(0x657940, Add, -419430400),# weapons:Forward Offset  index:51    from 25 To 0
        SetMemory(0x657944, Add, -5),# weapons:Forward Offset  index:52    from 5 To 0
        SetMemory(0x656C3C, Add, -5120),# weapons:Upward Offset  index:29    from 20 To 0
        SetMemory(0x656780, Add, -52),# weapons:Icon  index:0    from 323 To 271
        SetMemory(0x656780, Add, -3407872),# weapons:Icon  index:1    from 323 To 271
        SetMemory(0x656784, Add, -53),# weapons:Icon  index:2    from 324 To 271
        SetMemory(0x656784, Add, -3473408),# weapons:Icon  index:3    from 324 To 271
        SetMemory(0x656788, Add, -54),# weapons:Icon  index:4    from 325 To 271
        SetMemory(0x656788, Add, -3538944),# weapons:Icon  index:5    from 325 To 271
        SetMemory(0x65678C, Add, -3604480),# weapons:Icon  index:7    from 326 To 271
        SetMemory(0x656790, Add, -56),# weapons:Icon  index:8    from 327 To 271
        SetMemory(0x656790, Add, -3604480),# weapons:Icon  index:9    from 326 To 271
        SetMemory(0x656794, Add, -33),# weapons:Icon  index:10    from 327 To 294
        SetMemory(0x656794, Add, -3735552),# weapons:Icon  index:11    from 328 To 271
        SetMemory(0x656798, Add, -57),# weapons:Icon  index:12    from 328 To 271
        SetMemory(0x65679C, Add, -3932160),# weapons:Icon  index:15    from 331 To 271
        SetMemory(0x6567A0, Add, -61),# weapons:Icon  index:16    from 332 To 271
        SetMemory(0x6567A0, Add, 1572864),# weapons:Icon  index:17    from 331 To 355
        SetMemory(0x6567A4, Add, -61),# weapons:Icon  index:18    from 332 To 271
        SetMemory(0x6567A4, Add, -4063232),# weapons:Icon  index:19    from 333 To 271
        SetMemory(0x6567A8, Add, 21),# weapons:Icon  index:20    from 334 To 355
        SetMemory(0x6567A8, Add, 1441792),# weapons:Icon  index:21    from 333 To 355
        SetMemory(0x6567AC, Add, 21),# weapons:Icon  index:22    from 334 To 355
        SetMemory(0x6567AC, Add, 1441792),# weapons:Icon  index:23    from 333 To 355
        SetMemory(0x6567B0, Add, 21),# weapons:Icon  index:24    from 334 To 355
        SetMemory(0x6567B0, Add, 1310720),# weapons:Icon  index:25    from 335 To 355
        SetMemory(0x6567B4, Add, 20),# weapons:Icon  index:26    from 335 To 355
        SetMemory(0x6567B4, Add, 1245184),# weapons:Icon  index:27    from 336 To 355
        SetMemory(0x6567B8, Add, 19),# weapons:Icon  index:28    from 336 To 355
        SetMemory(0x6567B8, Add, 1179648),# weapons:Icon  index:29    from 337 To 355
        SetMemory(0x6567C4, Add, 1114112),# weapons:Icon  index:35    from 338 To 355
        SetMemory(0x6567C8, Add, 17),# weapons:Icon  index:36    from 338 To 355
        SetMemory(0x6567C8, Add, 1114112),# weapons:Icon  index:37    from 338 To 355
        SetMemory(0x6567CC, Add, -45),# weapons:Icon  index:38    from 339 To 294
        SetMemory(0x6567CC, Add, -2949120),# weapons:Icon  index:39    from 339 To 294
        SetMemory(0x6567D0, Add, -46),# weapons:Icon  index:40    from 340 To 294
        SetMemory(0x6567D0, Add, -3014656),# weapons:Icon  index:41    from 340 To 294
        SetMemory(0x6567D4, Add, -47),# weapons:Icon  index:42    from 341 To 294
        SetMemory(0x6567D4, Add, -4653056),# weapons:Icon  index:43    from 342 To 271
        SetMemory(0x6567D8, Add, -71),# weapons:Icon  index:44    from 342 To 271
        SetMemory(0x6567DC, Add, -50),# weapons:Icon  index:46    from 344 To 294
        SetMemory(0x6567DC, Add, -3276800),# weapons:Icon  index:47    from 344 To 294
        SetMemory(0x6567E0, Add, -51),# weapons:Icon  index:48    from 345 To 294
        SetMemory(0x6567E0, Add, -3342336),# weapons:Icon  index:49    from 345 To 294
        SetMemory(0x6567E4, Add, -52),# weapons:Icon  index:50    from 346 To 294
        SetMemory(0x6567E4, Add, -3407872),# weapons:Icon  index:51    from 346 To 294
        SetMemory(0x6567E8, Add, -53),# weapons:Icon  index:52    from 347 To 294
        SetMemory(0x6567E8, Add, -3538944),# weapons:Icon  index:53    from 348 To 294
        SetMemory(0x656804, Add, 1),# weapons:Icon  index:66    from 354 To 355
        SetMemory(0x656804, Add, 65536),# weapons:Icon  index:67    from 354 To 355
        SetMemory(0x656808, Add, -3997696),# weapons:Icon  index:69    from 355 To 294
        SetMemory(0x65680C, Add, -62),# weapons:Icon  index:70    from 356 To 294
        SetMemory(0x65680C, Add, -4063232),# weapons:Icon  index:71    from 356 To 294
        SetMemory(0x6CA458, Add, -196608),# flingy:Sprite  index:161    from 355 To 352
        SetMemory(0x6C9F0C, Add, 32),# flingy:Speed  index:5    from 1280 To 1312
        SetMemory(0x6C9FA0, Add, 32),# flingy:Speed  index:42    from 1280 To 1312
        SetMemory(0x6CA03C, Add, 32),# flingy:Speed  index:81    from 1280 To 1312
        SetMemory(0x6CA17C, Add, 8533),# flingy:Speed  index:161    from 0 To 8533
        SetMemory(0x6CA218, Add, 1311),# flingy:Speed  index:200    from 1 To 1312
        SetMemory(0x6C9C80, Add, 4194304),# flingy:Acceleration  index:5    from 67 To 131
        SetMemory(0x6C9CCC, Add, 64),# flingy:Acceleration  index:42    from 67 To 131
        SetMemory(0x6C9D18, Add, 4194304),# flingy:Acceleration  index:81    from 67 To 131
        SetMemory(0x6C9DB8, Add, 43712512),# flingy:Acceleration  index:161    from 0 To 667
        SetMemory(0x6C9E08, Add, 130),# flingy:Acceleration  index:200    from 1 To 131
        SetMemory(0x6C9944, Add, -12227),# flingy:Halt Distance  index:5    from 12227 To 0
        SetMemory(0x6C99D8, Add, -12227),# flingy:Halt Distance  index:42    from 12227 To 0
        SetMemory(0x6C9A74, Add, -12227),# flingy:Halt Distance  index:81    from 12227 To 0
        SetMemory(0x6C9BB4, Add, 54582),# flingy:Halt Distance  index:161    from 0 To 54582
        SetMemory(0x6C9C50, Add, -1),# flingy:Halt Distance  index:200    from 1 To 0
        SetMemory(0x6C9EC0, Add, 32512),# flingy:Turn Radius  index:161    from 0 To 127
        SetMemory(0x6C9EE8, Add, 13),# flingy:Turn Radius  index:200    from 27 To 40
        SetMemory(0x6C98F8, Add, -512),# flingy:Movement Control  index:161    from 2 To 0
        SetMemory(0x6C9920, Add, -2),# flingy:Movement Control  index:200    from 2 To 0
        SetMemory(0x666398, Add, 65536),# sprites:Image File  index:285    from 358 To 359
        SetMemory(0x66641C, Add, -21495808),# sprites:Image File  index:351    from 542 To 214
        SetMemory(0x666440, Add, -123),# sprites:Image File  index:368    from 514 To 391
        SetMemory(0x666558, Add, -327680),# sprites:Image File  index:509    from 965 To 960
        SetMemory(0x669EFC, Add, 65536),# images:Draw Function  index:214    from 9 To 10
        SetMemory(0x669FAC, Add, 16777216),# images:Draw Function  index:391    from 9 To 10
        SetMemory(0x66A044, Add, 4096),# images:Draw Function  index:541    from 0 To 16
        SetMemory(0x66A04C, Add, 2560),# images:Draw Function  index:549    from 0 To 10
        SetMemory(0x66A1E8, Add, 1048576),# images:Draw Function  index:962    from 0 To 16
        SetMemory(0x655744, Add, -9830400),# upgrades:Mineral Cost Base  index:3    from 150 To 0
        SetMemory(0x655748, Add, -150),# upgrades:Mineral Cost Base  index:4    from 150 To 0
        SetMemory(0x655748, Add, -6553600),# upgrades:Mineral Cost Base  index:5    from 100 To 0
        SetMemory(0x6559C4, Add, -4718592),# upgrades:Mineral Cost Factor  index:3    from 75 To 3
        SetMemory(0x6559C8, Add, -72),# upgrades:Mineral Cost Factor  index:4    from 75 To 3
        SetMemory(0x6559C8, Add, -4718592),# upgrades:Mineral Cost Factor  index:5    from 75 To 3
        SetMemory(0x655844, Add, -9830400),# upgrades:Vespene Cost Base  index:3    from 150 To 0
        SetMemory(0x655848, Add, -150),# upgrades:Vespene Cost Base  index:4    from 150 To 0
        SetMemory(0x655848, Add, -6553600),# upgrades:Vespene Cost Base  index:5    from 100 To 0
        SetMemory(0x6557C4, Add, -4915200),# upgrades:Vespene Cost Factor  index:3    from 75 To 0
        SetMemory(0x6557C8, Add, -75),# upgrades:Vespene Cost Factor  index:4    from 75 To 0
        SetMemory(0x6557C8, Add, -4915200),# upgrades:Vespene Cost Factor  index:5    from 75 To 0
        SetMemory(0x655B84, Add, -262144000),# upgrades:Research Time Base  index:3    from 4000 To 0
        SetMemory(0x655B88, Add, -4000),# upgrades:Research Time Base  index:4    from 4000 To 0
        SetMemory(0x655B88, Add, -262144000),# upgrades:Research Time Base  index:5    from 4000 To 0
        SetMemory(0x655944, Add, -31457280),# upgrades:Research Time Factor  index:3    from 480 To 0
        SetMemory(0x655948, Add, -480),# upgrades:Research Time Factor  index:4    from 480 To 0
        SetMemory(0x655948, Add, -31457280),# upgrades:Research Time Factor  index:5    from 480 To 0
        SetMemory(0x655AC0, Add, -80),# upgrades:Icon  index:0    from 292 To 212
        SetMemory(0x655AC0, Add, -18284544),# upgrades:Icon  index:1    from 293 To 14
        SetMemory(0x655AC4, Add, -34),# upgrades:Icon  index:2    from 291 To 257
        SetMemory(0x655AC4, Add, -196608),# upgrades:Icon  index:3    from 297 To 294
        SetMemory(0x655AC8, Add, 57),# upgrades:Icon  index:4    from 298 To 355
        SetMemory(0x655AC8, Add, -2097152),# upgrades:Icon  index:5    from 303 To 271
        SetMemory(0x655ACC, Add, 61),# upgrades:Icon  index:6    from 304 To 365
        SetMemory(0x655ACC, Add, 5046272),# upgrades:Icon  index:7    from 288 To 365
        SetMemory(0x655AD0, Add, 76),# upgrades:Icon  index:8    from 289 To 365
        SetMemory(0x655AD0, Add, 4915200),# upgrades:Icon  index:9    from 290 To 365
        SetMemory(0x655AD4, Add, 66),# upgrades:Icon  index:10    from 299 To 365
        SetMemory(0x655AD4, Add, 4259840),# upgrades:Icon  index:11    from 300 To 365
        SetMemory(0x655AD8, Add, 64),# upgrades:Icon  index:12    from 301 To 365
        SetMemory(0x655AD8, Add, 3932160),# upgrades:Icon  index:13    from 305 To 365
        SetMemory(0x655ADC, Add, 59),# upgrades:Icon  index:14    from 306 To 365
        SetMemory(0x655ADC, Add, 3604480),# upgrades:Icon  index:15    from 310 To 365
        SetMemory(0x655AE0, Add, 127),# upgrades:Icon  index:16    from 238 To 365
        SetMemory(0x655AE0, Add, 5111808),# upgrades:Icon  index:17    from 287 To 365
        SetMemory(0x655AE4, Add, 126),# upgrades:Icon  index:18    from 239 To 365
        SetMemory(0x655AE4, Add, 7667712),# upgrades:Icon  index:19    from 248 To 365
        SetMemory(0x655AE8, Add, 116),# upgrades:Icon  index:20    from 249 To 365
        SetMemory(0x655AE8, Add, 7143424),# upgrades:Icon  index:21    from 256 To 365
        SetMemory(0x655AEC, Add, 81),# upgrades:Icon  index:22    from 284 To 365
        SetMemory(0x655AEC, Add, 5242880),# upgrades:Icon  index:23    from 285 To 365
        SetMemory(0x655AF0, Add, 104),# upgrades:Icon  index:24    from 261 To 365
        SetMemory(0x655AF0, Add, 6750208),# upgrades:Icon  index:25    from 262 To 365
        SetMemory(0x655AF4, Add, 69),# upgrades:Icon  index:26    from 296 To 365
        SetMemory(0x655AF4, Add, 6684672),# upgrades:Icon  index:27    from 263 To 365
        SetMemory(0x655AF8, Add, 101),# upgrades:Icon  index:28    from 264 To 365
        SetMemory(0x655AF8, Add, 6488064),# upgrades:Icon  index:29    from 266 To 365
        SetMemory(0x655AFC, Add, -56),# upgrades:Icon  index:30    from 268 To 212
        SetMemory(0x655AFC, Add, -18350080),# upgrades:Icon  index:31    from 294 To 14
        SetMemory(0x655B00, Add, -38),# upgrades:Icon  index:32    from 295 To 257
        SetMemory(0x655B04, Add, 58),# upgrades:Icon  index:34    from 307 To 365
        SetMemory(0x655B04, Add, -393216),# upgrades:Icon  index:35    from 314 To 308
        SetMemory(0x655A44, Add, 1769472),# upgrades:Label  index:3    from 414 To 441
        SetMemory(0x655A48, Add, 27),# upgrades:Label  index:4    from 415 To 442
        SetMemory(0x655A48, Add, 1769472),# upgrades:Label  index:5    from 416 To 443
    ])

