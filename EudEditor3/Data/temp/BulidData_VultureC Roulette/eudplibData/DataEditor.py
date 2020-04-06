from eudplib import *


def onPluginStart():
    DoActions([  # Basic DatFile Actions
        SetMemory(0x6644F8, Add, 10),# units:Graphics  index:0    from 78 To 88
        SetMemory(0x6644F8, Add, 3584),# units:Graphics  index:1    from 74 To 88
        SetMemory(0x6644FC, Add, 117440512),# units:Graphics  index:7    from 81 To 88
        SetMemory(0x664500, Add, 8),# units:Graphics  index:8    from 80 To 88
        SetMemory(0x664500, Add, 2147483648),# units:Graphics  index:11    from 72 To 200
        SetMemory(0x66450C, Add, -7168),# units:Graphics  index:21    from 80 To 52
        SetMemory(0x664518, Add, -7077888),# units:Graphics  index:34    from 189 To 81
        SetMemory(0x664550, Add, 1),# units:Graphics  index:88    from 43 To 44
        SetMemory(0x66455C, Add, -1507328),# units:Graphics  index:102    from 70 To 47
        SetMemory(0x664568, Add, -512),# units:Graphics  index:113    from 97 To 95
        SetMemory(0x664568, Add, 1157627904),# units:Graphics  index:115    from 96 To 165
        SetMemory(0x66456C, Add, 48),# units:Graphics  index:116    from 107 To 155
        SetMemory(0x66456C, Add, 13056),# units:Graphics  index:117    from 98 To 149
        SetMemory(0x66459C, Add, 7424),# units:Graphics  index:165    from 51 To 80
        SetMemory(0x66459C, Add, -2883584),# units:Graphics  index:166    from 55 To 11
        SetMemory(0x66459C, Add, 385875968),# units:Graphics  index:167    from 65 To 88
        SetMemory(0x6645AC, Add, 36864),# units:Graphics  index:181    from 43 To 187
        SetMemory(0x6645B8, Add, -7798784),# units:Graphics  index:194    from 122 To 3
        SetMemory(0x6645B8, Add, -2013265920),# units:Graphics  index:195    from 123 To 3
        SetMemory(0x6645BC, Add, -121),# units:Graphics  index:196    from 124 To 3
        SetMemory(0x6645BC, Add, -30464),# units:Graphics  index:197    from 122 To 3
        SetMemory(0x6645BC, Add, -7864320),# units:Graphics  index:198    from 123 To 3
        SetMemory(0x6645BC, Add, -2030043136),# units:Graphics  index:199    from 124 To 3
        SetMemory(0x6607EC, Add, -393216),# units:Subunit 1  index:23    from 24 To 18
        SetMemory(0x6607F8, Add, -204),# units:Subunit 1  index:28    from 228 To 24
        SetMemory(0x66134C, Add, -200),# units:Construction Animation  index:167    from 200 To 0
        SetMemory(0x661384, Add, -325),# units:Construction Animation  index:181    from 325 To 0
        SetMemory(0x660640, Add, -20),# units:Unit Direction  index:80    from 32 To 12
        SetMemory(0x660694, Add, 3072),# units:Unit Direction  index:165    from 0 To 12
        SetMemory(0x660694, Add, 786432),# units:Unit Direction  index:166    from 0 To 12
        SetMemory(0x660694, Add, 201326592),# units:Unit Direction  index:167    from 0 To 12
        SetMemory(0x6606A4, Add, 8192),# units:Unit Direction  index:181    from 0 To 32
        SetMemory(0x6606B0, Add, 2097152),# units:Unit Direction  index:194    from 0 To 32
        SetMemory(0x6606B0, Add, 536870912),# units:Unit Direction  index:195    from 0 To 32
        SetMemory(0x6606B4, Add, 32),# units:Unit Direction  index:196    from 0 To 32
        SetMemory(0x6606B4, Add, 8192),# units:Unit Direction  index:197    from 0 To 32
        SetMemory(0x6606B4, Add, 2097152),# units:Unit Direction  index:198    from 0 To 32
        SetMemory(0x6606B4, Add, 536870912),# units:Unit Direction  index:199    from 0 To 32
        SetMemory(0x6647B0, Add, 1),# units:Shield Enable  index:0    from 0 To 1
        SetMemory(0x6647B0, Add, 256),# units:Shield Enable  index:1    from 0 To 1
        SetMemory(0x6647B0, Add, 65536),# units:Shield Enable  index:2    from 0 To 1
        SetMemory(0x6647B0, Add, 16777216),# units:Shield Enable  index:3    from 0 To 1
        SetMemory(0x6647B4, Add, 256),# units:Shield Enable  index:5    from 0 To 1
        SetMemory(0x6647B4, Add, 16777216),# units:Shield Enable  index:7    from 0 To 1
        SetMemory(0x6647B8, Add, 1),# units:Shield Enable  index:8    from 0 To 1
        SetMemory(0x6647C0, Add, 1),# units:Shield Enable  index:16    from 0 To 1
        SetMemory(0x6647C0, Add, 16777216),# units:Shield Enable  index:19    from 0 To 1
        SetMemory(0x6647C4, Add, 256),# units:Shield Enable  index:21    from 0 To 1
        SetMemory(0x6647C4, Add, 16777216),# units:Shield Enable  index:23    from 0 To 1
        SetMemory(0x6647DC, Add, 1),# units:Shield Enable  index:44    from 0 To 1
        SetMemory(0x6647F0, Add, -256),# units:Shield Enable  index:65    from 1 To 0
        SetMemory(0x664864, Add, 256),# units:Shield Enable  index:181    from 0 To 1
        SetMemory(0x664870, Add, 65536),# units:Shield Enable  index:194    from 0 To 1
        SetMemory(0x664870, Add, 16777216),# units:Shield Enable  index:195    from 0 To 1
        SetMemory(0x664874, Add, 1),# units:Shield Enable  index:196    from 0 To 1
        SetMemory(0x664874, Add, 256),# units:Shield Enable  index:197    from 0 To 1
        SetMemory(0x664874, Add, 65536),# units:Shield Enable  index:198    from 0 To 1
        SetMemory(0x664874, Add, 16777216),# units:Shield Enable  index:199    from 0 To 1
        SetMemory(0x660E00, Add, -347),# units:Shield Amount  index:0    from 350 To 3
        SetMemory(0x660E00, Add, -6356992),# units:Shield Amount  index:1    from 100 To 3
        SetMemory(0x660E04, Add, -97),# units:Shield Amount  index:2    from 100 To 3
        SetMemory(0x660E04, Add, 6553600),# units:Shield Amount  index:3    from 100 To 200
        SetMemory(0x660E0C, Add, -6356992),# units:Shield Amount  index:7    from 100 To 3
        SetMemory(0x660E10, Add, -97),# units:Shield Amount  index:8    from 100 To 3
        SetMemory(0x660E24, Add, -6356992),# units:Shield Amount  index:19    from 100 To 3
        SetMemory(0x660E2C, Add, 255590400),# units:Shield Amount  index:23    from 100 To 4000
        SetMemory(0x660E58, Add, 200),# units:Shield Amount  index:44    from 100 To 300
        SetMemory(0x660E84, Add, 2000),# units:Shield Amount  index:66    from 0 To 2000
        SetMemory(0x660E8C, Add, 50),# units:Shield Amount  index:70    from 150 To 200
        SetMemory(0x660E9C, Add, 98238464),# units:Shield Amount  index:79    from 1 To 1500
        SetMemory(0x660F4C, Add, -3276800),# units:Shield Amount  index:167    from 600 To 550
        SetMemory(0x660F68, Add, -6488064),# units:Shield Amount  index:181    from 100 To 1
        SetMemory(0x660F84, Add, -97),# units:Shield Amount  index:194    from 100 To 3
        SetMemory(0x660F84, Add, -6356992),# units:Shield Amount  index:195    from 100 To 3
        SetMemory(0x660F88, Add, -97),# units:Shield Amount  index:196    from 100 To 3
        SetMemory(0x660F88, Add, -6356992),# units:Shield Amount  index:197    from 100 To 3
        SetMemory(0x660F8C, Add, -97),# units:Shield Amount  index:198    from 100 To 3
        SetMemory(0x660F8C, Add, -6356992),# units:Shield Amount  index:199    from 100 To 3
        SetMemory(0x662350, Add, 24576),# units:Hit Points  index:0    from 1024 To 25600
        SetMemory(0x662354, Add, 14080),# units:Hit Points  index:1    from 11520 To 25600
        SetMemory(0x662358, Add, 20480),# units:Hit Points  index:2    from 5120 To 25600
        SetMemory(0x66235C, Add, 15360),# units:Hit Points  index:3    from 5120 To 20480
        SetMemory(0x66236C, Add, 10240),# units:Hit Points  index:7    from 15360 To 25600
        SetMemory(0x662370, Add, 25344),# units:Hit Points  index:8    from 256 To 25600
        SetMemory(0x662380, Add, 148480),# units:Hit Points  index:12    from 5120 To 153600
        SetMemory(0x6623AC, Add, -15104),# units:Hit Points  index:23    from 15360 To 256
        SetMemory(0x6623EC, Add, -46080),# units:Hit Points  index:39    from 51200 To 5120
        SetMemory(0x662400, Add, 13312),# units:Hit Points  index:44    from 2048 To 15360
        SetMemory(0x662408, Add, 256),# units:Hit Points  index:46    from 1280 To 1536
        SetMemory(0x662440, Add, 16640),# units:Hit Points  index:60    from 3840 To 20480
        SetMemory(0x662458, Add, 7680),# units:Hit Points  index:66    from 5120 To 12800
        SetMemory(0x662468, Add, 16640),# units:Hit Points  index:70    from 3840 To 20480
        SetMemory(0x66247C, Add, 35840),# units:Hit Points  index:75    from 15360 To 51200
        SetMemory(0x66248C, Add, 2304),# units:Hit Points  index:79    from 256 To 2560
        SetMemory(0x6624A8, Add, 5120),# units:Hit Points  index:86    from 15360 To 20480
        SetMemory(0x6625EC, Add, -12800),# units:Hit Points  index:167    from 153600 To 140800
        SetMemory(0x662624, Add, -76800),# units:Hit Points  index:181    from 204800 To 128000
        SetMemory(0x662658, Add, -25574400),# units:Hit Points  index:194    from 25600000 To 25600
        SetMemory(0x66265C, Add, -25574400),# units:Hit Points  index:195    from 25600000 To 25600
        SetMemory(0x662660, Add, -25574400),# units:Hit Points  index:196    from 25600000 To 25600
        SetMemory(0x662664, Add, -25574400),# units:Hit Points  index:197    from 25600000 To 25600
        SetMemory(0x662668, Add, -25574400),# units:Hit Points  index:198    from 25600000 To 25600
        SetMemory(0x66266C, Add, -25574400),# units:Hit Points  index:199    from 25600000 To 25600
        SetMemory(0x663150, Add, 8),# units:Elevation Level  index:0    from 4 To 12
        SetMemory(0x663150, Add, 2048),# units:Elevation Level  index:1    from 4 To 12
        SetMemory(0x663150, Add, 524288),# units:Elevation Level  index:2    from 4 To 12
        SetMemory(0x663150, Add, 134217728),# units:Elevation Level  index:3    from 4 To 12
        SetMemory(0x663154, Add, 8),# units:Elevation Level  index:4    from 4 To 12
        SetMemory(0x663154, Add, 2048),# units:Elevation Level  index:5    from 4 To 12
        SetMemory(0x663154, Add, 524288),# units:Elevation Level  index:6    from 4 To 12
        SetMemory(0x663154, Add, 134217728),# units:Elevation Level  index:7    from 4 To 12
        SetMemory(0x663158, Add, -6),# units:Elevation Level  index:8    from 18 To 12
        SetMemory(0x663160, Add, 8),# units:Elevation Level  index:16    from 4 To 12
        SetMemory(0x663160, Add, 589824),# units:Elevation Level  index:18    from 4 To 13
        SetMemory(0x663160, Add, 134217728),# units:Elevation Level  index:19    from 4 To 12
        SetMemory(0x663164, Add, 8),# units:Elevation Level  index:20    from 4 To 12
        SetMemory(0x663164, Add, 134217728),# units:Elevation Level  index:23    from 4 To 12
        SetMemory(0x663170, Add, 524288),# units:Elevation Level  index:34    from 4 To 12
        SetMemory(0x663174, Add, 8),# units:Elevation Level  index:36    from 4 To 12
        SetMemory(0x663174, Add, -1024),# units:Elevation Level  index:37    from 4 To 0
        SetMemory(0x663174, Add, 524288),# units:Elevation Level  index:38    from 4 To 12
        SetMemory(0x66318C, Add, 2048),# units:Elevation Level  index:61    from 4 To 12
        SetMemory(0x663190, Add, 524288),# units:Elevation Level  index:66    from 4 To 12
        SetMemory(0x663198, Add, 134217728),# units:Elevation Level  index:75    from 4 To 12
        SetMemory(0x66319C, Add, 134217728),# units:Elevation Level  index:79    from 4 To 12
        SetMemory(0x6631A8, Add, 983040),# units:Elevation Level  index:90    from 4 To 19
        SetMemory(0x6631B0, Add, 2048),# units:Elevation Level  index:97    from 4 To 12
        SetMemory(0x6631BC, Add, -1024),# units:Elevation Level  index:109    from 4 To 0
        SetMemory(0x6631BC, Add, 150994944),# units:Elevation Level  index:111    from 4 To 13
        SetMemory(0x6631C0, Add, -1024),# units:Elevation Level  index:113    from 4 To 0
        SetMemory(0x6631C0, Add, 589824),# units:Elevation Level  index:114    from 4 To 13
        SetMemory(0x6631C0, Add, 150994944),# units:Elevation Level  index:115    from 4 To 13
        SetMemory(0x6631C4, Add, 9),# units:Elevation Level  index:116    from 4 To 13
        SetMemory(0x6631C4, Add, 2304),# units:Elevation Level  index:117    from 4 To 13
        SetMemory(0x6631C8, Add, 15),# units:Elevation Level  index:120    from 4 To 19
        SetMemory(0x6631C8, Add, 150994944),# units:Elevation Level  index:123    from 4 To 13
        SetMemory(0x6631F4, Add, 3584),# units:Elevation Level  index:165    from 4 To 18
        SetMemory(0x6631F4, Add, 917504),# units:Elevation Level  index:166    from 4 To 18
        SetMemory(0x6631F4, Add, 234881024),# units:Elevation Level  index:167    from 4 To 18
        SetMemory(0x660FC8, Add, 128),# units:Unknown (old Movement)  index:0    from 65 To 193
        SetMemory(0x660FC8, Add, 32768),# units:Unknown (old Movement)  index:1    from 65 To 193
        SetMemory(0x660FD0, Add, -4),# units:Unknown (old Movement)  index:8    from 197 To 193
        SetMemory(0x660FE8, Add, 8388608),# units:Unknown (old Movement)  index:34    from 65 To 193
        SetMemory(0x66107C, Add, 49408),# units:Unknown (old Movement)  index:181    from 0 To 193
        SetMemory(0x661088, Add, 12648448),# units:Unknown (old Movement)  index:194    from 0 To 193
        SetMemory(0x661088, Add, 3238002688),# units:Unknown (old Movement)  index:195    from 0 To 193
        SetMemory(0x66108C, Add, 193),# units:Unknown (old Movement)  index:196    from 0 To 193
        SetMemory(0x66108C, Add, 49408),# units:Unknown (old Movement)  index:197    from 0 To 193
        SetMemory(0x66108C, Add, 12648448),# units:Unknown (old Movement)  index:198    from 0 To 193
        SetMemory(0x66108C, Add, 3238002688),# units:Unknown (old Movement)  index:199    from 0 To 193
        SetMemory(0x663DD0, Add, 15),# units:Rank/Sublabel  index:0    from 2 To 17
        SetMemory(0x663DD0, Add, 3072),# units:Rank/Sublabel  index:1    from 5 To 17
        SetMemory(0x663DD0, Add, 720896),# units:Rank/Sublabel  index:2    from 6 To 17
        SetMemory(0x663DD0, Add, 637534208),# units:Rank/Sublabel  index:3    from 7 To 45
        SetMemory(0x663DD4, Add, 13568),# units:Rank/Sublabel  index:5    from 8 To 61
        SetMemory(0x663DD4, Add, 268435456),# units:Rank/Sublabel  index:7    from 1 To 17
        SetMemory(0x663DD8, Add, 7),# units:Rank/Sublabel  index:8    from 10 To 17
        SetMemory(0x663DDC, Add, 29),# units:Rank/Sublabel  index:12    from 15 To 44
        SetMemory(0x663DE0, Add, 53),# units:Rank/Sublabel  index:16    from 18 To 71
        SetMemory(0x663DE4, Add, 31),# units:Rank/Sublabel  index:20    from 17 To 48
        SetMemory(0x663DE4, Add, 7936),# units:Rank/Sublabel  index:21    from 14 To 45
        SetMemory(0x663DE4, Add, -983040),# units:Rank/Sublabel  index:22    from 15 To 0
        SetMemory(0x663DE4, Add, 486539264),# units:Rank/Sublabel  index:23    from 19 To 48
        SetMemory(0x663DE8, Add, 67),# units:Rank/Sublabel  index:24    from 0 To 67
        SetMemory(0x663DEC, Add, 47),# units:Rank/Sublabel  index:28    from 20 To 67
        SetMemory(0x663DF0, Add, 40),# units:Rank/Sublabel  index:32    from 4 To 44
        SetMemory(0x663DF0, Add, -131072),# units:Rank/Sublabel  index:34    from 3 To 1
        SetMemory(0x663DF4, Add, 9984),# units:Rank/Sublabel  index:37    from 5 To 44
        SetMemory(0x663DF4, Add, 2490368),# units:Rank/Sublabel  index:38    from 9 To 47
        SetMemory(0x663DF4, Add, 503316480),# units:Rank/Sublabel  index:39    from 14 To 44
        SetMemory(0x663DF8, Add, 61),# units:Rank/Sublabel  index:40    from 3 To 64
        SetMemory(0x663DF8, Add, 10240),# units:Rank/Sublabel  index:41    from 4 To 44
        SetMemory(0x663DF8, Add, 2490368),# units:Rank/Sublabel  index:42    from 8 To 46
        SetMemory(0x663DFC, Add, 36),# units:Rank/Sublabel  index:44    from 11 To 47
        SetMemory(0x663DFC, Add, 2097152),# units:Rank/Sublabel  index:46    from 12 To 44
        SetMemory(0x663E00, Add, 704643072),# units:Rank/Sublabel  index:51    from 16 To 58
        SetMemory(0x663E0C, Add, 40),# units:Rank/Sublabel  index:60    from 8 To 48
        SetMemory(0x663E0C, Add, 12288),# units:Rank/Sublabel  index:61    from 12 To 60
        SetMemory(0x663E10, Add, 16128),# units:Rank/Sublabel  index:65    from 3 To 66
        SetMemory(0x663E10, Add, 2752512),# units:Rank/Sublabel  index:66    from 4 To 46
        SetMemory(0x663E14, Add, 43),# units:Rank/Sublabel  index:68    from 9 To 52
        SetMemory(0x663E14, Add, 2555904),# units:Rank/Sublabel  index:70    from 8 To 47
        SetMemory(0x663E18, Add, 939524096),# units:Rank/Sublabel  index:75    from 15 To 71
        SetMemory(0x663E1C, Add, 553648128),# units:Rank/Sublabel  index:79    from 16 To 49
        SetMemory(0x663E24, Add, 2424832),# units:Rank/Sublabel  index:86    from 12 To 49
        SetMemory(0x663E28, Add, 56),# units:Rank/Sublabel  index:88    from 12 To 68
        SetMemory(0x663E34, Add, 4521984),# units:Rank/Sublabel  index:102    from 0 To 69
        SetMemory(0x663E90, Add, 983040),# units:Rank/Sublabel  index:194    from 0 To 15
        SetMemory(0x663E90, Add, 251658240),# units:Rank/Sublabel  index:195    from 0 To 15
        SetMemory(0x663E94, Add, 15),# units:Rank/Sublabel  index:196    from 0 To 15
        SetMemory(0x663E94, Add, 3840),# units:Rank/Sublabel  index:197    from 0 To 15
        SetMemory(0x663E94, Add, 983040),# units:Rank/Sublabel  index:198    from 0 To 15
        SetMemory(0x663E94, Add, 251658240),# units:Rank/Sublabel  index:199    from 0 To 15
        SetMemory(0x662EAC, Add, 8),# units:Comp AI Idle  index:12    from 2 To 10
        SetMemory(0x662EC0, Add, -11337728),# units:Comp AI Idle  index:34    from 175 To 2
        SetMemory(0x662EC8, Add, -10289152),# units:Comp AI Idle  index:42    from 159 To 2
        SetMemory(0x662F0C, Add, -39424),# units:Comp AI Idle  index:109    from 156 To 2
        SetMemory(0x662F0C, Add, -2583691264),# units:Comp AI Idle  index:111    from 156 To 2
        SetMemory(0x662F10, Add, -39424),# units:Comp AI Idle  index:113    from 156 To 2
        SetMemory(0x662F10, Add, -10092544),# units:Comp AI Idle  index:114    from 156 To 2
        SetMemory(0x662F18, Add, -2583691264),# units:Comp AI Idle  index:123    from 156 To 2
        SetMemory(0x662F54, Add, -5376),# units:Comp AI Idle  index:181    from 23 To 2
        SetMemory(0x662F60, Add, -1376256),# units:Comp AI Idle  index:194    from 23 To 2
        SetMemory(0x662F60, Add, -352321536),# units:Comp AI Idle  index:195    from 23 To 2
        SetMemory(0x662F64, Add, -21),# units:Comp AI Idle  index:196    from 23 To 2
        SetMemory(0x662F64, Add, -38656),# units:Comp AI Idle  index:197    from 153 To 2
        SetMemory(0x662F64, Add, -9895936),# units:Comp AI Idle  index:198    from 153 To 2
        SetMemory(0x662F64, Add, -2533359616),# units:Comp AI Idle  index:199    from 153 To 2
        SetMemory(0x662274, Add, 8),# units:Human AI Idle  index:12    from 2 To 10
        SetMemory(0x662288, Add, -11337728),# units:Human AI Idle  index:34    from 175 To 2
        SetMemory(0x662290, Add, -5963776),# units:Human AI Idle  index:42    from 93 To 2
        SetMemory(0x6622D4, Add, -5376),# units:Human AI Idle  index:109    from 23 To 2
        SetMemory(0x6622D4, Add, -352321536),# units:Human AI Idle  index:111    from 23 To 2
        SetMemory(0x6622D8, Add, -5376),# units:Human AI Idle  index:113    from 23 To 2
        SetMemory(0x6622D8, Add, -1376256),# units:Human AI Idle  index:114    from 23 To 2
        SetMemory(0x6622E0, Add, -352321536),# units:Human AI Idle  index:123    from 23 To 2
        SetMemory(0x66231C, Add, -5376),# units:Human AI Idle  index:181    from 23 To 2
        SetMemory(0x662328, Add, -1376256),# units:Human AI Idle  index:194    from 23 To 2
        SetMemory(0x662328, Add, -352321536),# units:Human AI Idle  index:195    from 23 To 2
        SetMemory(0x66232C, Add, -21),# units:Human AI Idle  index:196    from 23 To 2
        SetMemory(0x66232C, Add, -38656),# units:Human AI Idle  index:197    from 153 To 2
        SetMemory(0x66232C, Add, -9895936),# units:Human AI Idle  index:198    from 153 To 2
        SetMemory(0x66232C, Add, -2533359616),# units:Human AI Idle  index:199    from 153 To 2
        SetMemory(0x6648A4, Add, 8),# units:Return to Idle  index:12    from 2 To 10
        SetMemory(0x6648B8, Add, -11337728),# units:Return to Idle  index:34    from 175 To 2
        SetMemory(0x6648C0, Add, -5963776),# units:Return to Idle  index:42    from 93 To 2
        SetMemory(0x664904, Add, -5376),# units:Return to Idle  index:109    from 23 To 2
        SetMemory(0x664904, Add, -352321536),# units:Return to Idle  index:111    from 23 To 2
        SetMemory(0x664908, Add, -5376),# units:Return to Idle  index:113    from 23 To 2
        SetMemory(0x664908, Add, -1376256),# units:Return to Idle  index:114    from 23 To 2
        SetMemory(0x664910, Add, -352321536),# units:Return to Idle  index:123    from 23 To 2
        SetMemory(0x66494C, Add, -5376),# units:Return to Idle  index:181    from 23 To 2
        SetMemory(0x664958, Add, -1376256),# units:Return to Idle  index:194    from 23 To 2
        SetMemory(0x664958, Add, -352321536),# units:Return to Idle  index:195    from 23 To 2
        SetMemory(0x66495C, Add, -21),# units:Return to Idle  index:196    from 23 To 2
        SetMemory(0x66495C, Add, -5376),# units:Return to Idle  index:197    from 23 To 2
        SetMemory(0x66495C, Add, -1376256),# units:Return to Idle  index:198    from 23 To 2
        SetMemory(0x66495C, Add, -352321536),# units:Return to Idle  index:199    from 23 To 2
        SetMemory(0x663320, Add, -184549376),# units:Attack Unit  index:3    from 21 To 10
        SetMemory(0x663334, Add, -184549376),# units:Attack Unit  index:23    from 21 To 10
        SetMemory(0x663338, Add, -11),# units:Attack Unit  index:24    from 22 To 11
        SetMemory(0x663340, Add, -10813440),# units:Attack Unit  index:34    from 175 To 10
        SetMemory(0x663348, Add, -720896),# units:Attack Unit  index:42    from 21 To 10
        SetMemory(0x66338C, Add, -512),# units:Attack Unit  index:109    from 23 To 21
        SetMemory(0x66338C, Add, -33554432),# units:Attack Unit  index:111    from 23 To 21
        SetMemory(0x663390, Add, -512),# units:Attack Unit  index:113    from 23 To 21
        SetMemory(0x663390, Add, -131072),# units:Attack Unit  index:114    from 23 To 21
        SetMemory(0x663398, Add, -33554432),# units:Attack Unit  index:123    from 23 To 21
        SetMemory(0x6633D4, Add, -512),# units:Attack Unit  index:181    from 23 To 21
        SetMemory(0x6633E0, Add, -851968),# units:Attack Unit  index:194    from 23 To 10
        SetMemory(0x6633E0, Add, -218103808),# units:Attack Unit  index:195    from 23 To 10
        SetMemory(0x6633E4, Add, -13),# units:Attack Unit  index:196    from 23 To 10
        SetMemory(0x6633E4, Add, -3328),# units:Attack Unit  index:197    from 23 To 10
        SetMemory(0x6633E4, Add, -851968),# units:Attack Unit  index:198    from 23 To 10
        SetMemory(0x6633E4, Add, -218103808),# units:Attack Unit  index:199    from 23 To 10
        SetMemory(0x663A5C, Add, 8),# units:Attack Move  index:12    from 2 To 10
        SetMemory(0x663A70, Add, -11337728),# units:Attack Move  index:34    from 175 To 2
        SetMemory(0x663ABC, Add, -5376),# units:Attack Move  index:109    from 23 To 2
        SetMemory(0x663ABC, Add, -352321536),# units:Attack Move  index:111    from 23 To 2
        SetMemory(0x663AC0, Add, -5376),# units:Attack Move  index:113    from 23 To 2
        SetMemory(0x663AC0, Add, -1376256),# units:Attack Move  index:114    from 23 To 2
        SetMemory(0x663AC8, Add, -352321536),# units:Attack Move  index:123    from 23 To 2
        SetMemory(0x663B04, Add, -5376),# units:Attack Move  index:181    from 23 To 2
        SetMemory(0x663B10, Add, -1376256),# units:Attack Move  index:194    from 23 To 2
        SetMemory(0x663B10, Add, -352321536),# units:Attack Move  index:195    from 23 To 2
        SetMemory(0x663B14, Add, -21),# units:Attack Move  index:196    from 23 To 2
        SetMemory(0x663B14, Add, -5376),# units:Attack Move  index:197    from 23 To 2
        SetMemory(0x663B14, Add, -1376256),# units:Attack Move  index:198    from 23 To 2
        SetMemory(0x663B14, Add, -352321536),# units:Attack Move  index:199    from 23 To 2
        SetMemory(0x6636B8, Add, 5),# units:Ground Weapon  index:0    from 0 To 5
        SetMemory(0x6636B8, Add, 768),# units:Ground Weapon  index:1    from 2 To 5
        SetMemory(0x6636B8, Add, 65536),# units:Ground Weapon  index:2    from 4 To 5
        SetMemory(0x6636BC, Add, 1),# units:Ground Weapon  index:4    from 7 To 8
        SetMemory(0x6636BC, Add, -134217728),# units:Ground Weapon  index:7    from 13 To 5
        SetMemory(0x6636C0, Add, -11),# units:Ground Weapon  index:8    from 16 To 5
        SetMemory(0x6636C8, Add, 1245184),# units:Ground Weapon  index:18    from 9 To 28
        SetMemory(0x6636CC, Add, 15616),# units:Ground Weapon  index:21    from 18 To 79
        SetMemory(0x6636D8, Add, -7667712),# units:Ground Weapon  index:34    from 130 To 13
        SetMemory(0x6636E0, Add, -5111808),# units:Ground Weapon  index:42    from 130 To 52
        SetMemory(0x6636E0, Add, 1375731712),# units:Ground Weapon  index:43    from 48 To 130
        SetMemory(0x6636E4, Add, -5242880),# units:Ground Weapon  index:46    from 130 To 50
        SetMemory(0x6636E8, Add, 89),# units:Ground Weapon  index:48    from 41 To 130
        SetMemory(0x6636EC, Add, 6160384),# units:Ground Weapon  index:54    from 36 To 130
        SetMemory(0x6636F0, Add, 62),# units:Ground Weapon  index:56    from 47 To 109
        SetMemory(0x6636F4, Add, -30),# units:Ground Weapon  index:60    from 130 To 100
        SetMemory(0x6636F4, Add, -1703936),# units:Ground Weapon  index:62    from 130 To 104
        SetMemory(0x6636FC, Add, -1310720),# units:Ground Weapon  index:70    from 73 To 53
        SetMemory(0x6636FC, Add, 889192448),# units:Ground Weapon  index:71    from 77 To 130
        SetMemory(0x663708, Add, 55),# units:Ground Weapon  index:80    from 75 To 130
        SetMemory(0x66371C, Add, 14),# units:Ground Weapon  index:100    from 116 To 130
        SetMemory(0x66371C, Add, 6291456),# units:Ground Weapon  index:102    from 21 To 117
        SetMemory(0x663778, Add, -8192000),# units:Ground Weapon  index:194    from 130 To 5
        SetMemory(0x663778, Add, -2097152000),# units:Ground Weapon  index:195    from 130 To 5
        SetMemory(0x66377C, Add, -125),# units:Ground Weapon  index:196    from 130 To 5
        SetMemory(0x66377C, Add, -32000),# units:Ground Weapon  index:197    from 130 To 5
        SetMemory(0x66377C, Add, -8192000),# units:Ground Weapon  index:198    from 130 To 5
        SetMemory(0x66377C, Add, -2097152000),# units:Ground Weapon  index:199    from 130 To 5
        SetMemory(0x664600, Add, 65536),# units:Max Ground Hits  index:34    from 0 To 1
        SetMemory(0x6646A0, Add, 65536),# units:Max Ground Hits  index:194    from 0 To 1
        SetMemory(0x6646A0, Add, 16777216),# units:Max Ground Hits  index:195    from 0 To 1
        SetMemory(0x6646A4, Add, 1),# units:Max Ground Hits  index:196    from 0 To 1
        SetMemory(0x6646A4, Add, 256),# units:Max Ground Hits  index:197    from 0 To 1
        SetMemory(0x6646A4, Add, 65536),# units:Max Ground Hits  index:198    from 0 To 1
        SetMemory(0x6646A4, Add, 16777216),# units:Max Ground Hits  index:199    from 0 To 1
        SetMemory(0x6616E0, Add, 130),# units:Air Weapon  index:0    from 0 To 130
        SetMemory(0x6616E0, Add, 32768),# units:Air Weapon  index:1    from 2 To 130
        SetMemory(0x6616E4, Add, 122),# units:Air Weapon  index:4    from 8 To 130
        SetMemory(0x6616E8, Add, 115),# units:Air Weapon  index:8    from 15 To 130
        SetMemory(0x6616EC, Add, 110),# units:Air Weapon  index:12    from 20 To 130
        SetMemory(0x6616F0, Add, 7864320),# units:Air Weapon  index:18    from 10 To 130
        SetMemory(0x6616F4, Add, 15872),# units:Air Weapon  index:21    from 17 To 79
        SetMemory(0x6616F8, Add, -118),# units:Air Weapon  index:24    from 130 To 12
        SetMemory(0x6616FC, Add, 106),# units:Air Weapon  index:28    from 24 To 130
        SetMemory(0x661708, Add, 1375731712),# units:Air Weapon  index:43    from 48 To 130
        SetMemory(0x661724, Add, 3670016),# units:Air Weapon  index:70    from 74 To 130
        SetMemory(0x661724, Add, 889192448),# units:Air Weapon  index:71    from 77 To 130
        SetMemory(0x661730, Add, 54),# units:Air Weapon  index:80    from 76 To 130
        SetMemory(0x661738, Add, 15),# units:Air Weapon  index:88    from 115 To 130
        SetMemory(0x661744, Add, 14),# units:Air Weapon  index:100    from 116 To 130
        SetMemory(0x661744, Add, 7077888),# units:Air Weapon  index:102    from 22 To 130
        SetMemory(0x65FC18, Add, -1),# units:Max Air Hits  index:0    from 1 To 0
        SetMemory(0x65FC18, Add, -256),# units:Max Air Hits  index:1    from 1 To 0
        SetMemory(0x65FC20, Add, -1),# units:Max Air Hits  index:8    from 1 To 0
        SetMemory(0x65FC30, Add, 1),# units:Max Air Hits  index:24    from 0 To 1
        SetMemory(0x65FC7C, Add, -65536),# units:Max Air Hits  index:102    from 1 To 0
        SetMemory(0x660178, Add, 3),# units:AI Internal  index:0    from 0 To 3
        SetMemory(0x660178, Add, 768),# units:AI Internal  index:1    from 0 To 3
        SetMemory(0x660178, Add, 196608),# units:AI Internal  index:2    from 0 To 3
        SetMemory(0x660180, Add, 3),# units:AI Internal  index:8    from 0 To 3
        SetMemory(0x660198, Add, 3),# units:AI Internal  index:32    from 0 To 3
        SetMemory(0x660198, Add, 196608),# units:AI Internal  index:34    from 0 To 3
        SetMemory(0x66019C, Add, 512),# units:AI Internal  index:37    from 0 To 2
        SetMemory(0x66019C, Add, 196608),# units:AI Internal  index:38    from 0 To 3
        SetMemory(0x6601A0, Add, 2),# units:AI Internal  index:40    from 0 To 2
        SetMemory(0x6601A4, Add, 3),# units:AI Internal  index:44    from 0 To 3
        SetMemory(0x6601A4, Add, 196608),# units:AI Internal  index:46    from 0 To 3
        SetMemory(0x6601B8, Add, 196608),# units:AI Internal  index:66    from 0 To 3
        SetMemory(0x66022C, Add, -768),# units:AI Internal  index:181    from 3 To 0
        SetMemory(0x664080, Add, 1073676352),# units:Special Ability Flags  index:0    from 402718720 To 1476395072
        SetMemory(0x664084, Add, 1071578688),# units:Special Ability Flags  index:1    from 404816384 To 1476395072
        SetMemory(0x664088, Add, 64),# units:Special Ability Flags  index:2    from 1476395008 To 1476395072
        SetMemory(0x66408C, Add, 64),# units:Special Ability Flags  index:3    from 1476395008 To 1476395072
        SetMemory(0x66409C, Add, -65480),# units:Special Ability Flags  index:7    from 1476460552 To 1476395072
        SetMemory(0x6640A0, Add, -35652036),# units:Special Ability Flags  index:8    from 1512047108 To 1476395072
        SetMemory(0x6640B0, Add, -4),# units:Special Ability Flags  index:12    from 1545601028 To 1545601024
        SetMemory(0x6640D4, Add, -2097732),# units:Special Ability Flags  index:21    from 1512047172 To 1509949440
        SetMemory(0x6640D8, Add, 536838144),# units:Special Ability Flags  index:22    from 1512079684 To 2048917828
        SetMemory(0x6640E4, Add, 4),# units:Special Ability Flags  index:25    from 1107296320 To 1107296324
        SetMemory(0x6640E8, Add, 4),# units:Special Ability Flags  index:26    from 805306384 To 805306388
        SetMemory(0x6640F0, Add, -4),# units:Special Ability Flags  index:28    from 1545601092 To 1545601088
        SetMemory(0x664100, Add, 64),# units:Special Ability Flags  index:32    from 402718720 To 402718784
        SetMemory(0x664108, Add, 1071644672),# units:Special Ability Flags  index:34    from 404815872 To 1476460544
        SetMemory(0x664110, Add, 536870912),# units:Special Ability Flags  index:36    from 65536 To 536936448
        SetMemory(0x664114, Add, -128),# units:Special Ability Flags  index:37    from 403768448 To 403768320
        SetMemory(0x664118, Add, -64),# units:Special Ability Flags  index:38    from 403767424 To 403767360
        SetMemory(0x66411C, Add, -128),# units:Special Ability Flags  index:39    from 469827712 To 469827584
        SetMemory(0x664128, Add, -32772),# units:Special Ability Flags  index:42    from 436306052 To 436273280
        SetMemory(0x664130, Add, -68),# units:Special Ability Flags  index:44    from 486604932 To 486604864
        SetMemory(0x664138, Add, -2097280),# units:Special Ability Flags  index:46    from 439419008 To 437321728
        SetMemory(0x66414C, Add, -128),# units:Special Ability Flags  index:51    from 404816576 To 404816448
        SetMemory(0x664160, Add, -134217728),# units:Special Ability Flags  index:56    from 486604996 To 352387268
        SetMemory(0x664170, Add, -4),# units:Special Ability Flags  index:60    from 1512046596 To 1512046592
        SetMemory(0x664174, Add, -4194304),# units:Special Ability Flags  index:61    from 406913024 To 402718720
        SetMemory(0x664178, Add, -4),# units:Special Ability Flags  index:62    from 486604932 To 486604928
        SetMemory(0x664198, Add, -4),# units:Special Ability Flags  index:70    from 1509949444 To 1509949440
        SetMemory(0x6641C0, Add, 536870912),# units:Special Ability Flags  index:80    from 1509949508 To 2046820420
        SetMemory(0x6641D8, Add, -4),# units:Special Ability Flags  index:86    from 1512046660 To 1512046656
        SetMemory(0x6641E0, Add, 4194300),# units:Special Ability Flags  index:88    from 1509949508 To 1514143808
        SetMemory(0x6641E8, Add, 4),# units:Special Ability Flags  index:90    from 402718720 To 402718724
        SetMemory(0x664204, Add, 536870916),# units:Special Ability Flags  index:97    from 65536 To 536936452
        SetMemory(0x664218, Add, -4),# units:Special Ability Flags  index:102    from 1545601092 To 1545601088
        SetMemory(0x664234, Add, 872417283),# units:Special Ability Flags  index:109    from 1140850689 To 2013267972
        SetMemory(0x66423C, Add, -1275066397),# units:Special Ability Flags  index:111    from 3288334369 To 2013267972
        SetMemory(0x664244, Add, -1275066397),# units:Special Ability Flags  index:113    from 3288334369 To 2013267972
        SetMemory(0x664248, Add, 872417251),# units:Special Ability Flags  index:114    from 1140850721 To 2013267972
        SetMemory(0x66424C, Add, 469764097),# units:Special Ability Flags  index:115    from 1140850691 To 1610614788
        SetMemory(0x664250, Add, 469764067),# units:Special Ability Flags  index:116    from 1140850721 To 1610614788
        SetMemory(0x664254, Add, 469764097),# units:Special Ability Flags  index:117    from 1140850691 To 1610614788
        SetMemory(0x664260, Add, 2),# units:Special Ability Flags  index:120    from 1140850691 To 1140850693
        SetMemory(0x66426C, Add, 872417283),# units:Special Ability Flags  index:123    from 1140850689 To 2013267972
        SetMemory(0x664300, Add, -2148007933),# units:Special Ability Flags  index:160    from 3288858625 To 1140850692
        SetMemory(0x664314, Add, 905445379),# units:Special Ability Flags  index:165    from 1141374977 To 2046820356
        SetMemory(0x664318, Add, 905445379),# units:Special Ability Flags  index:166    from 1141374977 To 2046820356
        SetMemory(0x66431C, Add, 905445379),# units:Special Ability Flags  index:167    from 1141374977 To 2046820356
        SetMemory(0x664354, Add, -132120321),# units:Special Ability Flags  index:181    from 1140850689 To 1008730368
        SetMemory(0x664388, Add, 1476395011),# units:Special Ability Flags  index:194    from 536870913 To 2013265924
        SetMemory(0x66438C, Add, 1476395011),# units:Special Ability Flags  index:195    from 536870913 To 2013265924
        SetMemory(0x664390, Add, 1476395011),# units:Special Ability Flags  index:196    from 536870913 To 2013265924
        SetMemory(0x664394, Add, 1476395011),# units:Special Ability Flags  index:197    from 536870913 To 2013265924
        SetMemory(0x664398, Add, 1476395011),# units:Special Ability Flags  index:198    from 536870913 To 2013265924
        SetMemory(0x66439C, Add, 1476395011),# units:Special Ability Flags  index:199    from 536870913 To 2013265924
        SetMemory(0x662DB8, Add, 1),# units:Target Acquisition Range  index:0    from 4 To 5
        SetMemory(0x662DB8, Add, -512),# units:Target Acquisition Range  index:1    from 7 To 5
        SetMemory(0x662DB8, Add, 50331648),# units:Target Acquisition Range  index:3    from 6 To 9
        SetMemory(0x662DBC, Add, 1),# units:Target Acquisition Range  index:4    from 6 To 7
        SetMemory(0x662DBC, Add, -512),# units:Target Acquisition Range  index:5    from 8 To 6
        SetMemory(0x662DBC, Add, -131072),# units:Target Acquisition Range  index:6    from 8 To 6
        SetMemory(0x662DBC, Add, 67108864),# units:Target Acquisition Range  index:7    from 1 To 5
        SetMemory(0x662DC4, Add, 1),# units:Target Acquisition Range  index:12    from 6 To 7
        SetMemory(0x662DC8, Add, 4),# units:Target Acquisition Range  index:16    from 6 To 10
        SetMemory(0x662DC8, Add, 131072),# units:Target Acquisition Range  index:18    from 5 To 7
        SetMemory(0x662DCC, Add, 2),# units:Target Acquisition Range  index:20    from 5 To 7
        SetMemory(0x662DCC, Add, 512),# units:Target Acquisition Range  index:21    from 5 To 7
        SetMemory(0x662DCC, Add, 33554432),# units:Target Acquisition Range  index:23    from 7 To 9
        SetMemory(0x662DD8, Add, 2),# units:Target Acquisition Range  index:32    from 3 To 5
        SetMemory(0x662DDC, Add, 1792),# units:Target Acquisition Range  index:37    from 3 To 10
        SetMemory(0x662DDC, Add, 196608),# units:Target Acquisition Range  index:38    from 4 To 7
        SetMemory(0x662DDC, Add, 50331648),# units:Target Acquisition Range  index:39    from 3 To 6
        SetMemory(0x662DE0, Add, 3),# units:Target Acquisition Range  index:40    from 3 To 6
        SetMemory(0x662DE0, Add, 1536),# units:Target Acquisition Range  index:41    from 1 To 7
        SetMemory(0x662DE0, Add, 589824),# units:Target Acquisition Range  index:42    from 0 To 9
        SetMemory(0x662DE4, Add, -1),# units:Target Acquisition Range  index:44    from 8 To 7
        SetMemory(0x662DE4, Add, 655360),# units:Target Acquisition Range  index:46    from 0 To 10
        SetMemory(0x662DE8, Add, 262144),# units:Target Acquisition Range  index:50    from 3 To 7
        SetMemory(0x662DE8, Add, 67108864),# units:Target Acquisition Range  index:51    from 3 To 7
        SetMemory(0x662DF0, Add, -1),# units:Target Acquisition Range  index:56    from 8 To 7
        SetMemory(0x662DF4, Add, -2),# units:Target Acquisition Range  index:60    from 9 To 7
        SetMemory(0x662DF4, Add, 768),# units:Target Acquisition Range  index:61    from 3 To 6
        SetMemory(0x662DF8, Add, 1280),# units:Target Acquisition Range  index:65    from 3 To 8
        SetMemory(0x662DF8, Add, 327680),# units:Target Acquisition Range  index:66    from 4 To 9
        SetMemory(0x662DFC, Add, 4),# units:Target Acquisition Range  index:68    from 3 To 7
        SetMemory(0x662DFC, Add, 327680),# units:Target Acquisition Range  index:70    from 4 To 9
        SetMemory(0x662E00, Add, 100663296),# units:Target Acquisition Range  index:75    from 3 To 9
        SetMemory(0x662E04, Add, 100663296),# units:Target Acquisition Range  index:79    from 3 To 9
        SetMemory(0x662E0C, Add, 131072),# units:Target Acquisition Range  index:86    from 5 To 7
        SetMemory(0x662E10, Add, 3),# units:Target Acquisition Range  index:88    from 4 To 7
        SetMemory(0x662E1C, Add, 65536),# units:Target Acquisition Range  index:102    from 6 To 7
        SetMemory(0x662E6C, Add, 1792),# units:Target Acquisition Range  index:181    from 0 To 7
        SetMemory(0x662E78, Add, 327680),# units:Target Acquisition Range  index:194    from 0 To 5
        SetMemory(0x662E78, Add, 83886080),# units:Target Acquisition Range  index:195    from 0 To 5
        SetMemory(0x662E7C, Add, 5),# units:Target Acquisition Range  index:196    from 0 To 5
        SetMemory(0x662E7C, Add, 1280),# units:Target Acquisition Range  index:197    from 0 To 5
        SetMemory(0x662E7C, Add, 327680),# units:Target Acquisition Range  index:198    from 0 To 5
        SetMemory(0x662E7C, Add, 83886080),# units:Target Acquisition Range  index:199    from 0 To 5
        SetMemory(0x663238, Add, 1),# units:Sight Range  index:0    from 7 To 8
        SetMemory(0x663238, Add, -256),# units:Sight Range  index:1    from 9 To 8
        SetMemory(0x66323C, Add, 16777216),# units:Sight Range  index:7    from 7 To 8
        SetMemory(0x663240, Add, 1),# units:Sight Range  index:8    from 7 To 8
        SetMemory(0x663258, Add, -131072),# units:Sight Range  index:34    from 9 To 7
        SetMemory(0x6632A8, Add, 512),# units:Sight Range  index:113    from 8 To 10
        SetMemory(0x6632EC, Add, 256),# units:Sight Range  index:181    from 9 To 10
        SetMemory(0x6635D0, Add, 1),# units:Armor Upgrade  index:0    from 0 To 1
        SetMemory(0x6635D0, Add, 256),# units:Armor Upgrade  index:1    from 0 To 1
        SetMemory(0x6635D4, Add, 16777216),# units:Armor Upgrade  index:7    from 0 To 1
        SetMemory(0x6635D8, Add, -1),# units:Armor Upgrade  index:8    from 2 To 1
        SetMemory(0x6635D8, Add, 973078528),# units:Armor Upgrade  index:11    from 2 To 60
        SetMemory(0x6635E4, Add, 1024),# units:Armor Upgrade  index:21    from 2 To 6
        SetMemory(0x6635E4, Add, 3801088),# units:Armor Upgrade  index:22    from 2 To 60
        SetMemory(0x663634, Add, 196608),# units:Armor Upgrade  index:102    from 2 To 5
        SetMemory(0x663674, Add, -14848),# units:Armor Upgrade  index:165    from 60 To 2
        SetMemory(0x663674, Add, -3670016),# units:Armor Upgrade  index:166    from 60 To 4
        SetMemory(0x663674, Add, -989855744),# units:Armor Upgrade  index:167    from 60 To 1
        SetMemory(0x663684, Add, -14080),# units:Armor Upgrade  index:181    from 60 To 5
        SetMemory(0x663690, Add, -3866624),# units:Armor Upgrade  index:194    from 60 To 1
        SetMemory(0x663690, Add, -989855744),# units:Armor Upgrade  index:195    from 60 To 1
        SetMemory(0x663694, Add, -59),# units:Armor Upgrade  index:196    from 60 To 1
        SetMemory(0x663694, Add, -15104),# units:Armor Upgrade  index:197    from 60 To 1
        SetMemory(0x663694, Add, -3866624),# units:Armor Upgrade  index:198    from 60 To 1
        SetMemory(0x663694, Add, -989855744),# units:Armor Upgrade  index:199    from 60 To 1
        SetMemory(0x662180, Add, 1),# units:Unit Size  index:0    from 1 To 2
        SetMemory(0x662180, Add, 256),# units:Unit Size  index:1    from 1 To 2
        SetMemory(0x662184, Add, 16777216),# units:Unit Size  index:7    from 1 To 2
        SetMemory(0x662188, Add, -1),# units:Unit Size  index:8    from 3 To 2
        SetMemory(0x6621EC, Add, -512),# units:Unit Size  index:109    from 3 To 1
        SetMemory(0x6621F0, Add, -512),# units:Unit Size  index:113    from 3 To 1
        SetMemory(0x6621F0, Add, -131072),# units:Unit Size  index:114    from 3 To 1
        SetMemory(0x662234, Add, 768),# units:Unit Size  index:181    from 0 To 3
        SetMemory(0x662240, Add, 131072),# units:Unit Size  index:194    from 0 To 2
        SetMemory(0x662240, Add, 33554432),# units:Unit Size  index:195    from 0 To 2
        SetMemory(0x662244, Add, 2),# units:Unit Size  index:196    from 0 To 2
        SetMemory(0x662244, Add, 512),# units:Unit Size  index:197    from 0 To 2
        SetMemory(0x662244, Add, 131072),# units:Unit Size  index:198    from 0 To 2
        SetMemory(0x662244, Add, 33554432),# units:Unit Size  index:199    from 0 To 2
        SetMemory(0x65FEC8, Add, 1),# units:Armor  index:0    from 99 To 100
        SetMemory(0x65FEC8, Add, 25600),# units:Armor  index:1    from 0 To 100
        SetMemory(0x65FEC8, Add, 65536),# units:Armor  index:2    from 99 To 100
        SetMemory(0x65FECC, Add, 1677721600),# units:Armor  index:7    from 0 To 100
        SetMemory(0x65FED0, Add, 1),# units:Armor  index:8    from 99 To 100
        SetMemory(0x65FED4, Add, -99),# units:Armor  index:12    from 99 To 0
        SetMemory(0x65FEE8, Add, -65536),# units:Armor  index:34    from 99 To 98
        SetMemory(0x65FEEC, Add, 150994944),# units:Armor  index:39    from 90 To 99
        SetMemory(0x65FEF4, Add, 5),# units:Armor  index:44    from 94 To 99
        SetMemory(0x65FF10, Add, 1660944384),# units:Armor  index:75    from 0 To 99
        SetMemory(0x65FF14, Add, 16777216),# units:Armor  index:79    from 98 To 99
        SetMemory(0x65FF7C, Add, 65280),# units:Armor  index:181    from 0 To 255
        SetMemory(0x65FF88, Add, 6553600),# units:Armor  index:194    from 0 To 100
        SetMemory(0x65FF88, Add, 1677721600),# units:Armor  index:195    from 0 To 100
        SetMemory(0x65FF8C, Add, 100),# units:Armor  index:196    from 0 To 100
        SetMemory(0x65FF8C, Add, 25600),# units:Armor  index:197    from 0 To 100
        SetMemory(0x65FF8C, Add, 6553600),# units:Armor  index:198    from 0 To 100
        SetMemory(0x65FF8C, Add, 1677721600),# units:Armor  index:199    from 0 To 100
        SetMemory(0x66209C, Add, -67108864),# units:Right-click Action  index:7    from 5 To 1
        SetMemory(0x6620B8, Add, 196608),# units:Right-click Action  index:34    from 2 To 5
        SetMemory(0x6620C0, Add, -65536),# units:Right-click Action  index:42    from 2 To 1
        SetMemory(0x662104, Add, 512),# units:Right-click Action  index:109    from 0 To 2
        SetMemory(0x662104, Add, -33554432),# units:Right-click Action  index:111    from 2 To 0
        SetMemory(0x66214C, Add, 512),# units:Right-click Action  index:181    from 0 To 2
        SetMemory(0x662158, Add, 65536),# units:Right-click Action  index:194    from 0 To 1
        SetMemory(0x662158, Add, 16777216),# units:Right-click Action  index:195    from 0 To 1
        SetMemory(0x66215C, Add, 1),# units:Right-click Action  index:196    from 0 To 1
        SetMemory(0x66215C, Add, 256),# units:Right-click Action  index:197    from 0 To 1
        SetMemory(0x66215C, Add, 65536),# units:Right-click Action  index:198    from 0 To 1
        SetMemory(0x66215C, Add, 16777216),# units:Right-click Action  index:199    from 0 To 1
        SetMemory(0x661FC0, Add, -275),# units:Ready Sound  index:0    from 275 To 0
        SetMemory(0x661FC0, Add, -14745600),# units:Ready Sound  index:1    from 225 To 0
        SetMemory(0x661FC4, Add, -352),# units:Ready Sound  index:2    from 352 To 0
        SetMemory(0x661FCC, Add, -24117248),# units:Ready Sound  index:7    from 368 To 0
        SetMemory(0x661FD0, Add, -256),# units:Ready Sound  index:8    from 256 To 0
        SetMemory(0x662004, Add, -631),# units:Ready Sound  index:34    from 999 To 368
        SetMemory(0x65FFB0, Add, 136),# units:What Sound Start  index:0    from 287 To 423
        SetMemory(0x65FFB0, Add, 12648448),# units:What Sound Start  index:1    from 230 To 423
        SetMemory(0x65FFB4, Add, 63),# units:What Sound Start  index:2    from 360 To 423
        SetMemory(0x65FFBC, Add, 3014656),# units:What Sound Start  index:7    from 377 To 423
        SetMemory(0x65FFC0, Add, 158),# units:What Sound Start  index:8    from 265 To 423
        SetMemory(0x65FFF4, Add, -624),# units:What Sound Start  index:34    from 1001 To 377
        SetMemory(0x6600A0, Add, -1),# units:What Sound Start  index:120    from 392 To 391
        SetMemory(0x6600FC, Add, 30343168),# units:What Sound Start  index:167    from 15 To 478
        SetMemory(0x660118, Add, 69206016),# units:What Sound Start  index:181    from 15 To 1071
        SetMemory(0x660134, Add, 408),# units:What Sound Start  index:194    from 15 To 423
        SetMemory(0x660134, Add, 26738688),# units:What Sound Start  index:195    from 15 To 423
        SetMemory(0x660138, Add, 408),# units:What Sound Start  index:196    from 15 To 423
        SetMemory(0x660138, Add, 26738688),# units:What Sound Start  index:197    from 15 To 423
        SetMemory(0x66013C, Add, 408),# units:What Sound Start  index:198    from 15 To 423
        SetMemory(0x66013C, Add, 26738688),# units:What Sound Start  index:199    from 15 To 423
        SetMemory(0x662BF0, Add, 136),# units:What Sound End  index:0    from 290 To 426
        SetMemory(0x662BF0, Add, 12648448),# units:What Sound End  index:1    from 233 To 426
        SetMemory(0x662BF4, Add, 63),# units:What Sound End  index:2    from 363 To 426
        SetMemory(0x662BFC, Add, 3014656),# units:What Sound End  index:7    from 380 To 426
        SetMemory(0x662C00, Add, 158),# units:What Sound End  index:8    from 268 To 426
        SetMemory(0x662C34, Add, -624),# units:What Sound End  index:34    from 1004 To 380
        SetMemory(0x662CE0, Add, -1),# units:What Sound End  index:120    from 392 To 391
        SetMemory(0x662D3C, Add, 30343168),# units:What Sound End  index:167    from 15 To 478
        SetMemory(0x662D58, Add, 69402624),# units:What Sound End  index:181    from 15 To 1074
        SetMemory(0x662D74, Add, 411),# units:What Sound End  index:194    from 15 To 426
        SetMemory(0x662D74, Add, 26935296),# units:What Sound End  index:195    from 15 To 426
        SetMemory(0x662D78, Add, 411),# units:What Sound End  index:196    from 15 To 426
        SetMemory(0x662D78, Add, 26935296),# units:What Sound End  index:197    from 15 To 426
        SetMemory(0x662D7C, Add, 411),# units:What Sound End  index:198    from 15 To 426
        SetMemory(0x662D7C, Add, 26935296),# units:What Sound End  index:199    from 15 To 426
        SetMemory(0x663B38, Add, 139),# units:Piss Sound Start  index:0    from 280 To 419
        SetMemory(0x663B38, Add, 12648448),# units:Piss Sound Start  index:1    from 226 To 419
        SetMemory(0x663B3C, Add, 63),# units:Piss Sound Start  index:2    from 356 To 419
        SetMemory(0x663B44, Add, 3211264),# units:Piss Sound Start  index:7    from 370 To 419
        SetMemory(0x663B48, Add, 161),# units:Piss Sound Start  index:8    from 258 To 419
        SetMemory(0x663B7C, Add, -639),# units:Piss Sound Start  index:34    from 1009 To 370
        SetMemory(0x661EE8, Add, 136),# units:Piss Sound End  index:0    from 286 To 422
        SetMemory(0x661EE8, Add, 12648448),# units:Piss Sound End  index:1    from 229 To 422
        SetMemory(0x661EEC, Add, 63),# units:Piss Sound End  index:2    from 359 To 422
        SetMemory(0x661EF4, Add, 3014656),# units:Piss Sound End  index:7    from 376 To 422
        SetMemory(0x661EF8, Add, 158),# units:Piss Sound End  index:8    from 264 To 422
        SetMemory(0x661F2C, Add, -639),# units:Piss Sound End  index:34    from 1015 To 376
        SetMemory(0x663C10, Add, 136),# units:Yes Sound Start  index:0    from 291 To 427
        SetMemory(0x663C10, Add, 12648448),# units:Yes Sound Start  index:1    from 234 To 427
        SetMemory(0x663C14, Add, 63),# units:Yes Sound Start  index:2    from 364 To 427
        SetMemory(0x663C1C, Add, 3014656),# units:Yes Sound Start  index:7    from 381 To 427
        SetMemory(0x663C20, Add, 158),# units:Yes Sound Start  index:8    from 269 To 427
        SetMemory(0x663C54, Add, -624),# units:Yes Sound Start  index:34    from 1005 To 381
        SetMemory(0x661440, Add, 136),# units:Yes Sound End  index:0    from 294 To 430
        SetMemory(0x661440, Add, 12648448),# units:Yes Sound End  index:1    from 237 To 430
        SetMemory(0x661444, Add, 63),# units:Yes Sound End  index:2    from 367 To 430
        SetMemory(0x66144C, Add, 3014656),# units:Yes Sound End  index:7    from 384 To 430
        SetMemory(0x661450, Add, 158),# units:Yes Sound End  index:8    from 272 To 430
        SetMemory(0x661484, Add, -624),# units:Yes Sound End  index:34    from 1008 To 384
        SetMemory(0x662860, Add, 15),# units:StarEdit Placement Box Width  index:0    from 17 To 32
        SetMemory(0x662864, Add, 17),# units:StarEdit Placement Box Width  index:1    from 15 To 32
        SetMemory(0x66287C, Add, 9),# units:StarEdit Placement Box Width  index:7    from 23 To 32
        SetMemory(0x662880, Add, -6),# units:StarEdit Placement Box Width  index:8    from 38 To 32
        SetMemory(0x6628B4, Add, -22),# units:StarEdit Placement Box Width  index:21    from 38 To 16
        SetMemory(0x6628B8, Add, -64),# units:StarEdit Placement Box Width  index:22    from 65 To 1
        SetMemory(0x6628E8, Add, 6),# units:StarEdit Placement Box Width  index:34    from 17 To 23
        SetMemory(0x6628F0, Add, -32),# units:StarEdit Placement Box Width  index:36    from 32 To 0
        SetMemory(0x6628F4, Add, -9),# units:StarEdit Placement Box Width  index:37    from 16 To 7
        SetMemory(0x662900, Add, -11),# units:StarEdit Placement Box Width  index:40    from 19 To 8
        SetMemory(0x662904, Add, -9),# units:StarEdit Placement Box Width  index:41    from 23 To 14
        SetMemory(0x662908, Add, -10),# units:StarEdit Placement Box Width  index:42    from 50 To 40
        SetMemory(0x662918, Add, -15),# units:StarEdit Placement Box Width  index:46    from 27 To 12
        SetMemory(0x662948, Add, -49),# units:StarEdit Placement Box Width  index:58    from 50 To 1
        SetMemory(0x6629A0, Add, 28),# units:StarEdit Placement Box Width  index:80    from 36 To 64
        SetMemory(0x6629C8, Add, -31),# units:StarEdit Placement Box Width  index:90    from 32 To 1
        SetMemory(0x6629D8, Add, -31),# units:StarEdit Placement Box Width  index:94    from 32 To 1
        SetMemory(0x6629F8, Add, -43),# units:StarEdit Placement Box Width  index:102    from 75 To 32
        SetMemory(0x662A14, Add, -95),# units:StarEdit Placement Box Width  index:109    from 96 To 1
        SetMemory(0x662A1C, Add, -127),# units:StarEdit Placement Box Width  index:111    from 128 To 1
        SetMemory(0x662A24, Add, -127),# units:StarEdit Placement Box Width  index:113    from 128 To 1
        SetMemory(0x662A28, Add, -127),# units:StarEdit Placement Box Width  index:114    from 128 To 1
        SetMemory(0x662A2C, Add, -63),# units:StarEdit Placement Box Width  index:115    from 64 To 1
        SetMemory(0x662A30, Add, -127),# units:StarEdit Placement Box Width  index:116    from 128 To 1
        SetMemory(0x662A34, Add, -63),# units:StarEdit Placement Box Width  index:117    from 64 To 1
        SetMemory(0x662A40, Add, -63),# units:StarEdit Placement Box Width  index:120    from 64 To 1
        SetMemory(0x662A4C, Add, -95),# units:StarEdit Placement Box Width  index:123    from 96 To 1
        SetMemory(0x662AE0, Add, -127),# units:StarEdit Placement Box Width  index:160    from 128 To 1
        SetMemory(0x662AF4, Add, -32),# units:StarEdit Placement Box Width  index:165    from 96 To 64
        SetMemory(0x662AF8, Add, -32),# units:StarEdit Placement Box Width  index:166    from 96 To 64
        SetMemory(0x662AFC, Add, -64),# units:StarEdit Placement Box Width  index:167    from 128 To 64
        SetMemory(0x662B34, Add, -64),# units:StarEdit Placement Box Width  index:181    from 64 To 0
        SetMemory(0x662B68, Add, -96),# units:StarEdit Placement Box Width  index:194    from 96 To 0
        SetMemory(0x662B6C, Add, -96),# units:StarEdit Placement Box Width  index:195    from 96 To 0
        SetMemory(0x662B70, Add, -96),# units:StarEdit Placement Box Width  index:196    from 96 To 0
        SetMemory(0x662B74, Add, -96),# units:StarEdit Placement Box Width  index:197    from 96 To 0
        SetMemory(0x662B78, Add, -96),# units:StarEdit Placement Box Width  index:198    from 96 To 0
        SetMemory(0x662B7C, Add, -96),# units:StarEdit Placement Box Width  index:199    from 96 To 0
        SetMemory(0x662860, Add, 786432),# units:StarEdit Placement Box Height  index:0    from 20 To 32
        SetMemory(0x662864, Add, 655360),# units:StarEdit Placement Box Height  index:1    from 22 To 32
        SetMemory(0x66287C, Add, 589824),# units:StarEdit Placement Box Height  index:7    from 23 To 32
        SetMemory(0x662880, Add, 131072),# units:StarEdit Placement Box Height  index:8    from 30 To 32
        SetMemory(0x6628B4, Add, -917504),# units:StarEdit Placement Box Height  index:21    from 30 To 16
        SetMemory(0x6628B8, Add, -3211264),# units:StarEdit Placement Box Height  index:22    from 50 To 1
        SetMemory(0x6628E8, Add, 196608),# units:StarEdit Placement Box Height  index:34    from 20 To 23
        SetMemory(0x6628F0, Add, -2097152),# units:StarEdit Placement Box Height  index:36    from 32 To 0
        SetMemory(0x6628F4, Add, -524288),# units:StarEdit Placement Box Height  index:37    from 16 To 8
        SetMemory(0x662900, Add, -720896),# units:StarEdit Placement Box Height  index:40    from 19 To 8
        SetMemory(0x662904, Add, -589824),# units:StarEdit Placement Box Height  index:41    from 23 To 14
        SetMemory(0x662908, Add, -655360),# units:StarEdit Placement Box Height  index:42    from 50 To 40
        SetMemory(0x662918, Add, -851968),# units:StarEdit Placement Box Height  index:46    from 25 To 12
        SetMemory(0x662948, Add, -3211264),# units:StarEdit Placement Box Height  index:58    from 50 To 1
        SetMemory(0x6629A0, Add, 2097152),# units:StarEdit Placement Box Height  index:80    from 32 To 64
        SetMemory(0x6629C8, Add, -2031616),# units:StarEdit Placement Box Height  index:90    from 32 To 1
        SetMemory(0x6629D8, Add, -2031616),# units:StarEdit Placement Box Height  index:94    from 32 To 1
        SetMemory(0x6629F8, Add, -1769472),# units:StarEdit Placement Box Height  index:102    from 59 To 32
        SetMemory(0x662A14, Add, -4128768),# units:StarEdit Placement Box Height  index:109    from 64 To 1
        SetMemory(0x662A1C, Add, -6225920),# units:StarEdit Placement Box Height  index:111    from 96 To 1
        SetMemory(0x662A24, Add, -6225920),# units:StarEdit Placement Box Height  index:113    from 96 To 1
        SetMemory(0x662A28, Add, -6225920),# units:StarEdit Placement Box Height  index:114    from 96 To 1
        SetMemory(0x662A2C, Add, -4128768),# units:StarEdit Placement Box Height  index:115    from 64 To 1
        SetMemory(0x662A30, Add, -6225920),# units:StarEdit Placement Box Height  index:116    from 96 To 1
        SetMemory(0x662A34, Add, -4128768),# units:StarEdit Placement Box Height  index:117    from 64 To 1
        SetMemory(0x662A40, Add, -4128768),# units:StarEdit Placement Box Height  index:120    from 64 To 1
        SetMemory(0x662A4C, Add, -4128768),# units:StarEdit Placement Box Height  index:123    from 64 To 1
        SetMemory(0x662AE0, Add, -6225920),# units:StarEdit Placement Box Height  index:160    from 96 To 1
        SetMemory(0x662AFC, Add, -2097152),# units:StarEdit Placement Box Height  index:167    from 96 To 64
        SetMemory(0x662B34, Add, -4128768),# units:StarEdit Placement Box Height  index:181    from 64 To 1
        SetMemory(0x662B68, Add, -4194304),# units:StarEdit Placement Box Height  index:194    from 64 To 0
        SetMemory(0x662B6C, Add, -4194304),# units:StarEdit Placement Box Height  index:195    from 64 To 0
        SetMemory(0x662B70, Add, -4194304),# units:StarEdit Placement Box Height  index:196    from 64 To 0
        SetMemory(0x662B74, Add, -4194304),# units:StarEdit Placement Box Height  index:197    from 64 To 0
        SetMemory(0x662B78, Add, -4194304),# units:StarEdit Placement Box Height  index:198    from 64 To 0
        SetMemory(0x662B7C, Add, -4194304),# units:StarEdit Placement Box Height  index:199    from 64 To 0
        SetMemory(0x662704, Add, -128),# units:Addon Horizontal (X) Position  index:9    from 128 To 0
        SetMemory(0x66270C, Add, -128),# units:Addon Horizontal (X) Position  index:11    from 128 To 0
        SetMemory(0x662704, Add, -2097152),# units:Addon Vertical (Y) Position  index:9    from 32 To 0
        SetMemory(0x66270C, Add, -2097152),# units:Addon Vertical (Y) Position  index:11    from 32 To 0
        SetMemory(0x6617C8, Add, 8),# units:Unit Size Left  index:0    from 8 To 16
        SetMemory(0x6617D0, Add, 9),# units:Unit Size Left  index:1    from 7 To 16
        SetMemory(0x661800, Add, 5),# units:Unit Size Left  index:7    from 11 To 16
        SetMemory(0x661808, Add, -3),# units:Unit Size Left  index:8    from 19 To 16
        SetMemory(0x661870, Add, -11),# units:Unit Size Left  index:21    from 19 To 8
        SetMemory(0x661878, Add, -31),# units:Unit Size Left  index:22    from 32 To 1
        SetMemory(0x6618D8, Add, 3),# units:Unit Size Left  index:34    from 8 To 11
        SetMemory(0x6618E8, Add, -15),# units:Unit Size Left  index:36    from 16 To 1
        SetMemory(0x6618F0, Add, -4),# units:Unit Size Left  index:37    from 8 To 4
        SetMemory(0x661908, Add, -5),# units:Unit Size Left  index:40    from 9 To 4
        SetMemory(0x661910, Add, -4),# units:Unit Size Left  index:41    from 11 To 7
        SetMemory(0x661918, Add, -5),# units:Unit Size Left  index:42    from 25 To 20
        SetMemory(0x661938, Add, -7),# units:Unit Size Left  index:46    from 13 To 6
        SetMemory(0x661998, Add, -23),# units:Unit Size Left  index:58    from 24 To 1
        SetMemory(0x661A48, Add, 14),# units:Unit Size Left  index:80    from 18 To 32
        SetMemory(0x661A98, Add, -15),# units:Unit Size Left  index:90    from 16 To 1
        SetMemory(0x661AB8, Add, -15),# units:Unit Size Left  index:94    from 16 To 1
        SetMemory(0x661AF8, Add, -21),# units:Unit Size Left  index:102    from 37 To 16
        SetMemory(0x661B30, Add, -37),# units:Unit Size Left  index:109    from 38 To 1
        SetMemory(0x661B40, Add, -47),# units:Unit Size Left  index:111    from 48 To 1
        SetMemory(0x661B50, Add, -55),# units:Unit Size Left  index:113    from 56 To 1
        SetMemory(0x661B58, Add, -47),# units:Unit Size Left  index:114    from 48 To 1
        SetMemory(0x661B60, Add, -46),# units:Unit Size Left  index:115    from 47 To 1
        SetMemory(0x661B68, Add, -47),# units:Unit Size Left  index:116    from 48 To 1
        SetMemory(0x661B70, Add, -46),# units:Unit Size Left  index:117    from 47 To 1
        SetMemory(0x661B88, Add, -38),# units:Unit Size Left  index:120    from 39 To 1
        SetMemory(0x661BA0, Add, -47),# units:Unit Size Left  index:123    from 48 To 1
        SetMemory(0x661CC8, Add, -47),# units:Unit Size Left  index:160    from 48 To 1
        SetMemory(0x661CF8, Add, -4),# units:Unit Size Left  index:166    from 36 To 32
        SetMemory(0x661D00, Add, -16),# units:Unit Size Left  index:167    from 48 To 32
        SetMemory(0x661D70, Add, -32),# units:Unit Size Left  index:181    from 32 To 0
        SetMemory(0x661DD8, Add, -36),# units:Unit Size Left  index:194    from 48 To 12
        SetMemory(0x661DE0, Add, -36),# units:Unit Size Left  index:195    from 48 To 12
        SetMemory(0x661DE8, Add, -36),# units:Unit Size Left  index:196    from 48 To 12
        SetMemory(0x661DF0, Add, -36),# units:Unit Size Left  index:197    from 48 To 12
        SetMemory(0x661DF8, Add, -36),# units:Unit Size Left  index:198    from 48 To 12
        SetMemory(0x661E00, Add, -36),# units:Unit Size Left  index:199    from 48 To 12
        SetMemory(0x6617C8, Add, 458752),# units:Unit Size Up  index:0    from 9 To 16
        SetMemory(0x6617D0, Add, 393216),# units:Unit Size Up  index:1    from 10 To 16
        SetMemory(0x661800, Add, 327680),# units:Unit Size Up  index:7    from 11 To 16
        SetMemory(0x661808, Add, 65536),# units:Unit Size Up  index:8    from 15 To 16
        SetMemory(0x661870, Add, -458752),# units:Unit Size Up  index:21    from 15 To 8
        SetMemory(0x661878, Add, -2097152),# units:Unit Size Up  index:22    from 33 To 1
        SetMemory(0x6618D8, Add, 131072),# units:Unit Size Up  index:34    from 9 To 11
        SetMemory(0x6618E8, Add, -983040),# units:Unit Size Up  index:36    from 16 To 1
        SetMemory(0x6618F0, Add, -196608),# units:Unit Size Up  index:37    from 4 To 1
        SetMemory(0x661908, Add, -327680),# units:Unit Size Up  index:40    from 9 To 4
        SetMemory(0x661910, Add, -262144),# units:Unit Size Up  index:41    from 11 To 7
        SetMemory(0x661918, Add, -327680),# units:Unit Size Up  index:42    from 25 To 20
        SetMemory(0x661938, Add, -393216),# units:Unit Size Up  index:46    from 12 To 6
        SetMemory(0x661998, Add, -983040),# units:Unit Size Up  index:58    from 16 To 1
        SetMemory(0x661A48, Add, 1048576),# units:Unit Size Up  index:80    from 16 To 32
        SetMemory(0x661A98, Add, -983040),# units:Unit Size Up  index:90    from 16 To 1
        SetMemory(0x661AB8, Add, -983040),# units:Unit Size Up  index:94    from 16 To 1
        SetMemory(0x661AF8, Add, -851968),# units:Unit Size Up  index:102    from 29 To 16
        SetMemory(0x661B30, Add, -1376256),# units:Unit Size Up  index:109    from 22 To 1
        SetMemory(0x661B40, Add, -2555904),# units:Unit Size Up  index:111    from 40 To 1
        SetMemory(0x661B50, Add, -2555904),# units:Unit Size Up  index:113    from 40 To 1
        SetMemory(0x661B58, Add, -2555904),# units:Unit Size Up  index:114    from 40 To 1
        SetMemory(0x661B60, Add, -1507328),# units:Unit Size Up  index:115    from 24 To 1
        SetMemory(0x661B68, Add, -2424832),# units:Unit Size Up  index:116    from 38 To 1
        SetMemory(0x661B70, Add, -1507328),# units:Unit Size Up  index:117    from 24 To 1
        SetMemory(0x661B88, Add, -1507328),# units:Unit Size Up  index:120    from 24 To 1
        SetMemory(0x661BA0, Add, -2031616),# units:Unit Size Up  index:123    from 32 To 1
        SetMemory(0x661CC8, Add, -2031616),# units:Unit Size Up  index:160    from 32 To 1
        SetMemory(0x661CF0, Add, 524288),# units:Unit Size Up  index:165    from 24 To 32
        SetMemory(0x661CF8, Add, 524288),# units:Unit Size Up  index:166    from 24 To 32
        SetMemory(0x661D00, Add, -524288),# units:Unit Size Up  index:167    from 40 To 32
        SetMemory(0x661D70, Add, -2097152),# units:Unit Size Up  index:181    from 32 To 0
        SetMemory(0x661DD8, Add, -1310720),# units:Unit Size Up  index:194    from 32 To 12
        SetMemory(0x661DE0, Add, -1310720),# units:Unit Size Up  index:195    from 32 To 12
        SetMemory(0x661DE8, Add, -1310720),# units:Unit Size Up  index:196    from 32 To 12
        SetMemory(0x661DF0, Add, -1310720),# units:Unit Size Up  index:197    from 32 To 12
        SetMemory(0x661DF8, Add, -1310720),# units:Unit Size Up  index:198    from 32 To 12
        SetMemory(0x661E00, Add, -1310720),# units:Unit Size Up  index:199    from 32 To 12
        SetMemory(0x6617CC, Add, 7),# units:Unit Size Right  index:0    from 8 To 15
        SetMemory(0x6617D4, Add, 8),# units:Unit Size Right  index:1    from 7 To 15
        SetMemory(0x661804, Add, 4),# units:Unit Size Right  index:7    from 11 To 15
        SetMemory(0x66180C, Add, -3),# units:Unit Size Right  index:8    from 18 To 15
        SetMemory(0x661874, Add, -11),# units:Unit Size Right  index:21    from 18 To 7
        SetMemory(0x66187C, Add, -31),# units:Unit Size Right  index:22    from 32 To 1
        SetMemory(0x6618DC, Add, 3),# units:Unit Size Right  index:34    from 8 To 11
        SetMemory(0x6618EC, Add, -14),# units:Unit Size Right  index:36    from 15 To 1
        SetMemory(0x6618F4, Add, -4),# units:Unit Size Right  index:37    from 7 To 3
        SetMemory(0x66190C, Add, -5),# units:Unit Size Right  index:40    from 9 To 4
        SetMemory(0x661914, Add, -4),# units:Unit Size Right  index:41    from 11 To 7
        SetMemory(0x66191C, Add, -4),# units:Unit Size Right  index:42    from 24 To 20
        SetMemory(0x66193C, Add, -7),# units:Unit Size Right  index:46    from 13 To 6
        SetMemory(0x66199C, Add, -23),# units:Unit Size Right  index:58    from 24 To 1
        SetMemory(0x661A4C, Add, 15),# units:Unit Size Right  index:80    from 17 To 32
        SetMemory(0x661A9C, Add, -14),# units:Unit Size Right  index:90    from 15 To 1
        SetMemory(0x661ABC, Add, -14),# units:Unit Size Right  index:94    from 15 To 1
        SetMemory(0x661AFC, Add, -22),# units:Unit Size Right  index:102    from 37 To 15
        SetMemory(0x661B34, Add, -37),# units:Unit Size Right  index:109    from 38 To 1
        SetMemory(0x661B44, Add, -55),# units:Unit Size Right  index:111    from 56 To 1
        SetMemory(0x661B54, Add, -55),# units:Unit Size Right  index:113    from 56 To 1
        SetMemory(0x661B5C, Add, -47),# units:Unit Size Right  index:114    from 48 To 1
        SetMemory(0x661B64, Add, -27),# units:Unit Size Right  index:115    from 28 To 1
        SetMemory(0x661B6C, Add, -47),# units:Unit Size Right  index:116    from 48 To 1
        SetMemory(0x661B74, Add, -27),# units:Unit Size Right  index:117    from 28 To 1
        SetMemory(0x661B8C, Add, -30),# units:Unit Size Right  index:120    from 31 To 1
        SetMemory(0x661BA4, Add, -46),# units:Unit Size Right  index:123    from 47 To 1
        SetMemory(0x661CCC, Add, -47),# units:Unit Size Right  index:160    from 48 To 1
        SetMemory(0x661CFC, Add, -4),# units:Unit Size Right  index:166    from 36 To 32
        SetMemory(0x661D04, Add, -16),# units:Unit Size Right  index:167    from 48 To 32
        SetMemory(0x661D74, Add, -31),# units:Unit Size Right  index:181    from 31 To 0
        SetMemory(0x661DDC, Add, -35),# units:Unit Size Right  index:194    from 47 To 12
        SetMemory(0x661DE4, Add, -35),# units:Unit Size Right  index:195    from 47 To 12
        SetMemory(0x661DEC, Add, -35),# units:Unit Size Right  index:196    from 47 To 12
        SetMemory(0x661DF4, Add, -35),# units:Unit Size Right  index:197    from 47 To 12
        SetMemory(0x661DFC, Add, -35),# units:Unit Size Right  index:198    from 47 To 12
        SetMemory(0x661E04, Add, -35),# units:Unit Size Right  index:199    from 47 To 12
        SetMemory(0x6617CC, Add, 327680),# units:Unit Size Down  index:0    from 10 To 15
        SetMemory(0x6617D4, Add, 262144),# units:Unit Size Down  index:1    from 11 To 15
        SetMemory(0x661804, Add, 262144),# units:Unit Size Down  index:7    from 11 To 15
        SetMemory(0x66180C, Add, 65536),# units:Unit Size Down  index:8    from 14 To 15
        SetMemory(0x661874, Add, -458752),# units:Unit Size Down  index:21    from 14 To 7
        SetMemory(0x66187C, Add, -983040),# units:Unit Size Down  index:22    from 16 To 1
        SetMemory(0x6618DC, Add, 65536),# units:Unit Size Down  index:34    from 10 To 11
        SetMemory(0x6618EC, Add, -917504),# units:Unit Size Down  index:36    from 15 To 1
        SetMemory(0x6618F4, Add, -262144),# units:Unit Size Down  index:37    from 11 To 7
        SetMemory(0x66190C, Add, -327680),# units:Unit Size Down  index:40    from 9 To 4
        SetMemory(0x661914, Add, -262144),# units:Unit Size Down  index:41    from 11 To 7
        SetMemory(0x66191C, Add, -262144),# units:Unit Size Down  index:42    from 24 To 20
        SetMemory(0x66193C, Add, -393216),# units:Unit Size Down  index:46    from 12 To 6
        SetMemory(0x66199C, Add, -1245184),# units:Unit Size Down  index:58    from 20 To 1
        SetMemory(0x661A4C, Add, 1114112),# units:Unit Size Down  index:80    from 15 To 32
        SetMemory(0x661A9C, Add, -917504),# units:Unit Size Down  index:90    from 15 To 1
        SetMemory(0x661ABC, Add, -917504),# units:Unit Size Down  index:94    from 15 To 1
        SetMemory(0x661AFC, Add, -917504),# units:Unit Size Down  index:102    from 29 To 15
        SetMemory(0x661B34, Add, -1638400),# units:Unit Size Down  index:109    from 26 To 1
        SetMemory(0x661B44, Add, -2031616),# units:Unit Size Down  index:111    from 32 To 1
        SetMemory(0x661B54, Add, -2555904),# units:Unit Size Down  index:113    from 40 To 1
        SetMemory(0x661B5C, Add, -2424832),# units:Unit Size Down  index:114    from 38 To 1
        SetMemory(0x661B64, Add, -1376256),# units:Unit Size Down  index:115    from 22 To 1
        SetMemory(0x661B6C, Add, -2424832),# units:Unit Size Down  index:116    from 38 To 1
        SetMemory(0x661B74, Add, -1376256),# units:Unit Size Down  index:117    from 22 To 1
        SetMemory(0x661B8C, Add, -1507328),# units:Unit Size Down  index:120    from 24 To 1
        SetMemory(0x661BA4, Add, -1376256),# units:Unit Size Down  index:123    from 22 To 1
        SetMemory(0x661CCC, Add, -2555904),# units:Unit Size Down  index:160    from 40 To 1
        SetMemory(0x661CF4, Add, 524288),# units:Unit Size Down  index:165    from 24 To 32
        SetMemory(0x661CFC, Add, 786432),# units:Unit Size Down  index:166    from 20 To 32
        SetMemory(0x661D74, Add, -2031616),# units:Unit Size Down  index:181    from 31 To 0
        SetMemory(0x661DDC, Add, -1245184),# units:Unit Size Down  index:194    from 31 To 12
        SetMemory(0x661DE4, Add, -1245184),# units:Unit Size Down  index:195    from 31 To 12
        SetMemory(0x661DEC, Add, -1245184),# units:Unit Size Down  index:196    from 31 To 12
        SetMemory(0x661DF4, Add, -1245184),# units:Unit Size Down  index:197    from 31 To 12
        SetMemory(0x661DFC, Add, -1245184),# units:Unit Size Down  index:198    from 31 To 12
        SetMemory(0x661E04, Add, -1245184),# units:Unit Size Down  index:199    from 31 To 12
        SetMemory(0x662F88, Add, 13),# units:Portrait  index:0    from 0 To 13
        SetMemory(0x662F88, Add, 786432),# units:Portrait  index:1    from 1 To 13
        SetMemory(0x662F8C, Add, 10),# units:Portrait  index:2    from 3 To 13
        SetMemory(0x662F94, Add, 393216),# units:Portrait  index:7    from 7 To 13
        SetMemory(0x662F98, Add, 5),# units:Portrait  index:8    from 8 To 13
        SetMemory(0x662F9C, Add, 6094848),# units:Portrait  index:11    from 10 To 103
        SetMemory(0x662FB0, Add, 2621440),# units:Portrait  index:21    from 8 To 48
        SetMemory(0x662FCC, Add, -83),# units:Portrait  index:34    from 90 To 7
        SetMemory(0x663038, Add, -51),# units:Portrait  index:88    from 95 To 44
        SetMemory(0x663054, Add, -36),# units:Portrait  index:102    from 92 To 56
        SetMemory(0x6630D0, Add, -3407872),# units:Portrait  index:165    from 60 To 8
        SetMemory(0x6630D4, Add, -34),# units:Portrait  index:166    from 60 To 26
        SetMemory(0x6630D4, Add, -3735552),# units:Portrait  index:167    from 60 To 3
        SetMemory(0x6630F0, Add, 1638400),# units:Portrait  index:181    from 74 To 99
        SetMemory(0x66310C, Add, -25),# units:Portrait  index:194    from 38 To 13
        SetMemory(0x66310C, Add, -262144),# units:Portrait  index:195    from 17 To 13
        SetMemory(0x663110, Add, -47),# units:Portrait  index:196    from 60 To 13
        SetMemory(0x663110, Add, -1638400),# units:Portrait  index:197    from 38 To 13
        SetMemory(0x663114, Add, -4),# units:Portrait  index:198    from 17 To 13
        SetMemory(0x663114, Add, -3080192),# units:Portrait  index:199    from 60 To 13
        SetMemory(0x663888, Add, -50),# units:Mineral Cost  index:0    from 50 To 0
        SetMemory(0x663888, Add, -1638400),# units:Mineral Cost  index:1    from 25 To 0
        SetMemory(0x66388C, Add, -75),# units:Mineral Cost  index:2    from 75 To 0
        SetMemory(0x66388C, Add, -6553600),# units:Mineral Cost  index:3    from 100 To 0
        SetMemory(0x663890, Add, -9830400),# units:Mineral Cost  index:5    from 150 To 0
        SetMemory(0x663894, Add, -3276800),# units:Mineral Cost  index:7    from 50 To 0
        SetMemory(0x663968, Add, -3276800),# units:Mineral Cost  index:113    from 200 To 150
        SetMemory(0x6639F0, Add, -65536),# units:Mineral Cost  index:181    from 1 To 0
        SetMemory(0x663A0C, Add, -100),# units:Mineral Cost  index:194    from 250 To 150
        SetMemory(0x663A0C, Add, 6553600),# units:Mineral Cost  index:195    from 50 To 150
        SetMemory(0x663A10, Add, 50),# units:Mineral Cost  index:196    from 100 To 150
        SetMemory(0x663A10, Add, -6553600),# units:Mineral Cost  index:197    from 250 To 150
        SetMemory(0x663A14, Add, 100),# units:Mineral Cost  index:198    from 50 To 150
        SetMemory(0x663A14, Add, 3276800),# units:Mineral Cost  index:199    from 100 To 150
        SetMemory(0x65FD00, Add, -4915200),# units:Vespene Cost  index:1    from 75 To 0
        SetMemory(0x65FD04, Add, -3276800),# units:Vespene Cost  index:3    from 50 To 0
        SetMemory(0x65FD08, Add, 0),# units:Vespene Cost  index:4    from 0 To 0
        SetMemory(0x65FD08, Add, -6553600),# units:Vespene Cost  index:5    from 100 To 0
        SetMemory(0x65FD10, Add, -100),# units:Vespene Cost  index:8    from 100 To 0
        SetMemory(0x65FD44, Add, -25),# units:Vespene Cost  index:34    from 25 To 0
        SetMemory(0x65FE4C, Add, -9830400),# units:Vespene Cost  index:167    from 150 To 0
        SetMemory(0x65FE68, Add, -65536),# units:Vespene Cost  index:181    from 1 To 0
        SetMemory(0x65FE84, Add, -3276800),# units:Vespene Cost  index:195    from 50 To 0
        SetMemory(0x65FE88, Add, -100),# units:Vespene Cost  index:196    from 100 To 0
        SetMemory(0x65FE8C, Add, -50),# units:Vespene Cost  index:198    from 50 To 0
        SetMemory(0x65FE8C, Add, -6553600),# units:Vespene Cost  index:199    from 100 To 0
        SetMemory(0x660428, Add, 540),# units:Build Time  index:0    from 360 To 900
        SetMemory(0x660428, Add, 9830400),# units:Build Time  index:1    from 750 To 900
        SetMemory(0x66042C, Add, -449),# units:Build Time  index:2    from 450 To 1
        SetMemory(0x660434, Add, 39321600),# units:Build Time  index:7    from 300 To 900
        SetMemory(0x66046C, Add, -150),# units:Build Time  index:34    from 450 To 300
        SetMemory(0x660508, Add, -9830400),# units:Build Time  index:113    from 1200 To 1050
        SetMemory(0x660574, Add, 9830400),# units:Build Time  index:167    from 1050 To 1200
        SetMemory(0x660590, Add, 19595264),# units:Build Time  index:181    from 1 To 300
        SetMemory(0x6605AC, Add, 899),# units:Build Time  index:194    from 1 To 900
        SetMemory(0x6605AC, Add, 58916864),# units:Build Time  index:195    from 1 To 900
        SetMemory(0x6605B0, Add, 899),# units:Build Time  index:196    from 1 To 900
        SetMemory(0x6605B0, Add, 58916864),# units:Build Time  index:197    from 1 To 900
        SetMemory(0x6605B4, Add, 899),# units:Build Time  index:198    from 1 To 900
        SetMemory(0x6605B4, Add, 58916864),# units:Build Time  index:199    from 1 To 900
        SetMemory(0x6637C4, Add, 8),# units:Staredit Group Flags  index:36    from 1 To 9
        SetMemory(0x6637C4, Add, 65536),# units:Staredit Group Flags  index:38    from 9 To 10
        SetMemory(0x6637C4, Add, 16777216),# units:Staredit Group Flags  index:39    from 9 To 10
        SetMemory(0x6637C8, Add, 1),# units:Staredit Group Flags  index:40    from 9 To 10
        SetMemory(0x6637C8, Add, 256),# units:Staredit Group Flags  index:41    from 9 To 10
        SetMemory(0x6637C8, Add, 65536),# units:Staredit Group Flags  index:42    from 9 To 10
        SetMemory(0x6637CC, Add, 1),# units:Staredit Group Flags  index:44    from 9 To 10
        SetMemory(0x6637CC, Add, 65536),# units:Staredit Group Flags  index:46    from 9 To 10
        SetMemory(0x6637D0, Add, 16777216),# units:Staredit Group Flags  index:51    from 9 To 10
        SetMemory(0x6637DC, Add, -2),# units:Staredit Group Flags  index:60    from 12 To 10
        SetMemory(0x6637DC, Add, -512),# units:Staredit Group Flags  index:61    from 12 To 10
        SetMemory(0x6637E0, Add, -512),# units:Staredit Group Flags  index:65    from 12 To 10
        SetMemory(0x6637E0, Add, -131072),# units:Staredit Group Flags  index:66    from 12 To 10
        SetMemory(0x6637E4, Add, -2),# units:Staredit Group Flags  index:68    from 12 To 10
        SetMemory(0x6637E4, Add, -131072),# units:Staredit Group Flags  index:70    from 12 To 10
        SetMemory(0x6637E8, Add, -33554432),# units:Staredit Group Flags  index:75    from 12 To 10
        SetMemory(0x6637EC, Add, -33554432),# units:Staredit Group Flags  index:79    from 12 To 10
        SetMemory(0x6637F4, Add, -131072),# units:Staredit Group Flags  index:86    from 12 To 10
        SetMemory(0x6637F8, Add, -2),# units:Staredit Group Flags  index:88    from 12 To 10
        SetMemory(0x663800, Add, 2048),# units:Staredit Group Flags  index:97    from 1 To 9
        SetMemory(0x663804, Add, -1),# units:Staredit Group Flags  index:100    from 10 To 9
        SetMemory(0x66380C, Add, -2048),# units:Staredit Group Flags  index:109    from 18 To 10
        SetMemory(0x66380C, Add, -671088640),# units:Staredit Group Flags  index:111    from 50 To 10
        SetMemory(0x663810, Add, -10240),# units:Staredit Group Flags  index:113    from 50 To 10
        SetMemory(0x663810, Add, -2621440),# units:Staredit Group Flags  index:114    from 50 To 10
        SetMemory(0x663810, Add, -134217728),# units:Staredit Group Flags  index:115    from 18 To 10
        SetMemory(0x663814, Add, -8),# units:Staredit Group Flags  index:116    from 18 To 10
        SetMemory(0x663814, Add, -2048),# units:Staredit Group Flags  index:117    from 18 To 10
        SetMemory(0x663818, Add, -134217728),# units:Staredit Group Flags  index:123    from 18 To 10
        SetMemory(0x663840, Add, -48),# units:Staredit Group Flags  index:160    from 52 To 4
        SetMemory(0x663844, Add, -2048),# units:Staredit Group Flags  index:165    from 20 To 12
        SetMemory(0x663844, Add, -524288),# units:Staredit Group Flags  index:166    from 20 To 12
        SetMemory(0x663844, Add, -704643072),# units:Staredit Group Flags  index:167    from 52 To 10
        SetMemory(0x663854, Add, -33792),# units:Staredit Group Flags  index:181    from 144 To 12
        SetMemory(0x663860, Add, 589824),# units:Staredit Group Flags  index:194    from 1 To 10
        SetMemory(0x663860, Add, 134217728),# units:Staredit Group Flags  index:195    from 2 To 10
        SetMemory(0x663864, Add, 6),# units:Staredit Group Flags  index:196    from 4 To 10
        SetMemory(0x663864, Add, 2304),# units:Staredit Group Flags  index:197    from 1 To 10
        SetMemory(0x663864, Add, 524288),# units:Staredit Group Flags  index:198    from 2 To 10
        SetMemory(0x663864, Add, 100663296),# units:Staredit Group Flags  index:199    from 4 To 10
        SetMemory(0x663CE8, Add, -2),# units:Supply Required  index:0    from 2 To 0
        SetMemory(0x663CE8, Add, -512),# units:Supply Required  index:1    from 2 To 0
        SetMemory(0x663CE8, Add, -262144),# units:Supply Required  index:2    from 4 To 0
        SetMemory(0x663CE8, Add, -67108864),# units:Supply Required  index:3    from 4 To 0
        SetMemory(0x663CEC, Add, -1024),# units:Supply Required  index:5    from 4 To 0
        SetMemory(0x663CEC, Add, -33554432),# units:Supply Required  index:7    from 2 To 0
        SetMemory(0x663CF0, Add, -4),# units:Supply Required  index:8    from 4 To 0
        SetMemory(0x663D9C, Add, 2048),# units:Supply Required  index:181    from 0 To 8
        SetMemory(0x664410, Add, 1),# units:Space Required  index:0    from 1 To 2
        SetMemory(0x664410, Add, 256),# units:Space Required  index:1    from 1 To 2
        SetMemory(0x664414, Add, 16777216),# units:Space Required  index:7    from 1 To 2
        SetMemory(0x664418, Add, -253),# units:Space Required  index:8    from 255 To 2
        SetMemory(0x6644C4, Add, -64256),# units:Space Required  index:181    from 255 To 4
        SetMemory(0x6644D0, Add, -16580608),# units:Space Required  index:194    from 255 To 2
        SetMemory(0x6644D0, Add, -4244635648),# units:Space Required  index:195    from 255 To 2
        SetMemory(0x6644D4, Add, -253),# units:Space Required  index:196    from 255 To 2
        SetMemory(0x6644D4, Add, -64768),# units:Space Required  index:197    from 255 To 2
        SetMemory(0x6644D4, Add, -16580608),# units:Space Required  index:198    from 255 To 2
        SetMemory(0x6644D4, Add, -4244635648),# units:Space Required  index:199    from 255 To 2
        SetMemory(0x663408, Add, -50),# units:Build Score  index:0    from 50 To 0
        SetMemory(0x663408, Add, -11468800),# units:Build Score  index:1    from 175 To 0
        SetMemory(0x66340C, Add, -75),# units:Build Score  index:2    from 75 To 0
        SetMemory(0x663414, Add, -3276800),# units:Build Score  index:7    from 50 To 0
        SetMemory(0x663418, Add, -400),# units:Build Score  index:8    from 400 To 0
        SetMemory(0x66344C, Add, -75),# units:Build Score  index:34    from 125 To 50
        SetMemory(0x663554, Add, -13107200),# units:Build Score  index:167    from 300 To 100
        SetMemory(0x663570, Add, 41943040),# units:Build Score  index:181    from 10 To 650
        SetMemory(0x663EB8, Add, 200),# units:Destroy Score  index:0    from 100 To 300
        SetMemory(0x663EB8, Add, -3276800),# units:Destroy Score  index:1    from 350 To 300
        SetMemory(0x663EBC, Add, 150),# units:Destroy Score  index:2    from 150 To 300
        SetMemory(0x663EC4, Add, 13107200),# units:Destroy Score  index:7    from 100 To 300
        SetMemory(0x663EC8, Add, -500),# units:Destroy Score  index:8    from 800 To 300
        SetMemory(0x663EFC, Add, -150),# units:Destroy Score  index:34    from 250 To 100
        SetMemory(0x664004, Add, -39321600),# units:Destroy Score  index:167    from 900 To 300
        SetMemory(0x664020, Add, 84541440),# units:Destroy Score  index:181    from 10 To 1300
        SetMemory(0x66403C, Add, 300),# units:Destroy Score  index:194    from 0 To 300
        SetMemory(0x66403C, Add, 19660800),# units:Destroy Score  index:195    from 0 To 300
        SetMemory(0x664040, Add, 300),# units:Destroy Score  index:196    from 0 To 300
        SetMemory(0x664040, Add, 19660800),# units:Destroy Score  index:197    from 0 To 300
        SetMemory(0x664044, Add, 300),# units:Destroy Score  index:198    from 0 To 300
        SetMemory(0x664044, Add, 19660800),# units:Destroy Score  index:199    from 0 To 300
        SetMemory(0x6606F8, Add, -65536),# units:Broodwar Unit Flag  index:34    from 1 To 0
        SetMemory(0x66078C, Add, 256),# units:Broodwar Unit Flag  index:181    from 0 To 1
        SetMemory(0x661518, Add, -8),# units:Staredit Availability Flags  index:0    from 463 To 455
        SetMemory(0x661518, Add, -524288),# units:Staredit Availability Flags  index:1    from 463 To 455
        SetMemory(0x66151C, Add, -8),# units:Staredit Availability Flags  index:2    from 463 To 455
        SetMemory(0x661524, Add, -524288),# units:Staredit Availability Flags  index:7    from 463 To 455
        SetMemory(0x661528, Add, -8),# units:Staredit Availability Flags  index:8    from 463 To 455
        SetMemory(0x661558, Add, 131072),# units:Staredit Availability Flags  index:33    from 0 To 2
        SetMemory(0x66155C, Add, -512),# units:Staredit Availability Flags  index:34    from 975 To 463
        SetMemory(0x661560, Add, 322),# units:Staredit Availability Flags  index:36    from 0 To 322
        SetMemory(0x6615D8, Add, 21102592),# units:Staredit Availability Flags  index:97    from 0 To 322
        SetMemory(0x6615E4, Add, 451),# units:Staredit Availability Flags  index:102    from 4 To 455
        SetMemory(0x661660, Add, -524288),# units:Staredit Availability Flags  index:165    from 463 To 455
        SetMemory(0x661664, Add, -8),# units:Staredit Availability Flags  index:166    from 463 To 455
        SetMemory(0x661664, Add, -524288),# units:Staredit Availability Flags  index:167    from 463 To 455
        SetMemory(0x661680, Add, 63373312),# units:Staredit Availability Flags  index:181    from 0 To 967
        SetMemory(0x6573C4, Add, 2),# weapons:Label  index:114    from 293 To 295
        SetMemory(0x6573C8, Add, 76349440),# weapons:Label  index:117    from 229 To 1394
        SetMemory(0x656CA8, Add, 17),# weapons:Graphics  index:0    from 142 To 159
        SetMemory(0x656CAC, Add, 13),# weapons:Graphics  index:1    from 142 To 155
        SetMemory(0x656CB0, Add, 3),# weapons:Graphics  index:2    from 143 To 146
        SetMemory(0x656CB4, Add, 21),# weapons:Graphics  index:3    from 143 To 164
        SetMemory(0x656CD4, Add, 7),# weapons:Graphics  index:11    from 143 To 150
        SetMemory(0x656CD8, Add, 59),# weapons:Graphics  index:12    from 143 To 202
        SetMemory(0x656DBC, Add, -143),# weapons:Graphics  index:69    from 143 To 0
        SetMemory(0x656E38, Add, -57),# weapons:Graphics  index:100    from 206 To 149
        SetMemory(0x656E48, Add, -38),# weapons:Graphics  index:104    from 204 To 166
        SetMemory(0x656E7C, Add, 30),# weapons:Graphics  index:117    from 142 To 172
        SetMemory(0x6579B4, Add, 65536),# weapons:Target Flags  index:15    from 1 To 2
        SetMemory(0x6579F8, Add, -1),# weapons:Target Flags  index:48    from 3 To 2
        SetMemory(0x657A2C, Add, 2),# weapons:Target Flags  index:74    from 1 To 3
        SetMemory(0x657A34, Add, -65536),# weapons:Target Flags  index:79    from 3 To 2
        SetMemory(0x657A60, Add, 2),# weapons:Target Flags  index:100    from 1 To 3
        SetMemory(0x656A88, Add, -64),# weapons:Minimum Range  index:28    from 64 To 0
        SetMemory(0x657470, Add, 8),# weapons:Maximum Range  index:0    from 128 To 136
        SetMemory(0x657474, Add, -64),# weapons:Maximum Range  index:1    from 160 To 96
        SetMemory(0x657478, Add, -84),# weapons:Maximum Range  index:2    from 224 To 140
        SetMemory(0x65747C, Add, -64),# weapons:Maximum Range  index:3    from 192 To 128
        SetMemory(0x657490, Add, -32),# weapons:Maximum Range  index:8    from 160 To 128
        SetMemory(0x65749C, Add, -72),# weapons:Maximum Range  index:11    from 224 To 152
        SetMemory(0x6574A0, Add, -32),# weapons:Maximum Range  index:12    from 224 To 192
        SetMemory(0x6574A4, Add, 6),# weapons:Maximum Range  index:13    from 10 To 16
        SetMemory(0x6574BC, Add, -64),# weapons:Maximum Range  index:19    from 192 To 128
        SetMemory(0x6574E0, Add, -224),# weapons:Maximum Range  index:28    from 384 To 160
        SetMemory(0x6574FC, Add, 17),# weapons:Maximum Range  index:35    from 15 To 32
        SetMemory(0x657504, Add, 125),# weapons:Maximum Range  index:37    from 15 To 140
        SetMemory(0x657508, Add, -40),# weapons:Maximum Range  index:38    from 128 To 88
        SetMemory(0x65750C, Add, -40),# weapons:Maximum Range  index:39    from 160 To 120
        SetMemory(0x657510, Add, 103),# weapons:Maximum Range  index:40    from 25 To 128
        SetMemory(0x657518, Add, 94),# weapons:Maximum Range  index:42    from 2 To 96
        SetMemory(0x65751C, Add, 32),# weapons:Maximum Range  index:43    from 32 To 64
        SetMemory(0x657528, Add, -120),# weapons:Maximum Range  index:46    from 256 To 136
        SetMemory(0x657530, Add, 64),# weapons:Maximum Range  index:48    from 96 To 160
        SetMemory(0x657538, Add, -16),# weapons:Maximum Range  index:50    from 128 To 112
        SetMemory(0x657540, Add, -112),# weapons:Maximum Range  index:52    from 224 To 112
        SetMemory(0x657544, Add, -64),# weapons:Maximum Range  index:53    from 224 To 160
        SetMemory(0x657568, Add, -31),# weapons:Maximum Range  index:62    from 32 To 1
        SetMemory(0x657570, Add, 17),# weapons:Maximum Range  index:64    from 15 To 32
        SetMemory(0x657584, Add, 36),# weapons:Maximum Range  index:69    from 96 To 132
        SetMemory(0x657588, Add, 68),# weapons:Maximum Range  index:70    from 64 To 132
        SetMemory(0x657598, Add, 12),# weapons:Maximum Range  index:74    from 128 To 140
        SetMemory(0x6575A8, Add, -20),# weapons:Maximum Range  index:78    from 160 To 140
        SetMemory(0x6575AC, Add, 32),# weapons:Maximum Range  index:79    from 128 To 160
        SetMemory(0x6575C4, Add, 113),# weapons:Maximum Range  index:85    from 15 To 128
        SetMemory(0x657600, Add, -16),# weapons:Maximum Range  index:100    from 160 To 144
        SetMemory(0x657610, Add, -60),# weapons:Maximum Range  index:104    from 192 To 132
        SetMemory(0x657624, Add, 96),# weapons:Maximum Range  index:109    from 192 To 288
        SetMemory(0x65762C, Add, 125),# weapons:Maximum Range  index:111    from 15 To 140
        SetMemory(0x657638, Add, 32),# weapons:Maximum Range  index:114    from 128 To 160
        SetMemory(0x657644, Add, 27),# weapons:Maximum Range  index:117    from 128 To 155
        SetMemory(0x657258, Add, 1),# weapons:Weapon Type  index:0    from 3 To 4
        SetMemory(0x657258, Add, 256),# weapons:Weapon Type  index:1    from 3 To 4
        SetMemory(0x657258, Add, 131072),# weapons:Weapon Type  index:2    from 2 To 4
        SetMemory(0x657258, Add, 33554432),# weapons:Weapon Type  index:3    from 2 To 4
        SetMemory(0x65725C, Add, 256),# weapons:Weapon Type  index:5    from 2 To 3
        SetMemory(0x657260, Add, 3),# weapons:Weapon Type  index:8    from 1 To 4
        SetMemory(0x657260, Add, 50331648),# weapons:Weapon Type  index:11    from 1 To 4
        SetMemory(0x657264, Add, 3),# weapons:Weapon Type  index:12    from 1 To 4
        SetMemory(0x657264, Add, 256),# weapons:Weapon Type  index:13    from 3 To 4
        SetMemory(0x657264, Add, 33554432),# weapons:Weapon Type  index:15    from 1 To 3
        SetMemory(0x657268, Add, 16777216),# weapons:Weapon Type  index:19    from 3 To 4
        SetMemory(0x657270, Add, 512),# weapons:Weapon Type  index:25    from 2 To 4
        SetMemory(0x657274, Add, 2),# weapons:Weapon Type  index:28    from 1 To 3
        SetMemory(0x657278, Add, 16777216),# weapons:Weapon Type  index:35    from 3 To 4
        SetMemory(0x65727C, Add, 256),# weapons:Weapon Type  index:37    from 3 To 4
        SetMemory(0x65727C, Add, 196608),# weapons:Weapon Type  index:38    from 1 To 4
        SetMemory(0x65727C, Add, 50331648),# weapons:Weapon Type  index:39    from 1 To 4
        SetMemory(0x657280, Add, 1),# weapons:Weapon Type  index:40    from 3 To 4
        SetMemory(0x657280, Add, 65536),# weapons:Weapon Type  index:42    from 3 To 4
        SetMemory(0x657280, Add, 16777216),# weapons:Weapon Type  index:43    from 3 To 4
        SetMemory(0x657288, Add, 131072),# weapons:Weapon Type  index:50    from 2 To 4
        SetMemory(0x65728C, Add, 1),# weapons:Weapon Type  index:52    from 3 To 4
        SetMemory(0x65728C, Add, 512),# weapons:Weapon Type  index:53    from 1 To 3
        SetMemory(0x65728C, Add, 196608),# weapons:Weapon Type  index:54    from 1 To 4
        SetMemory(0x657298, Add, 1),# weapons:Weapon Type  index:64    from 3 To 4
        SetMemory(0x657298, Add, 196608),# weapons:Weapon Type  index:66    from 1 To 4
        SetMemory(0x65729C, Add, 65536),# weapons:Weapon Type  index:70    from 3 To 4
        SetMemory(0x6572A0, Add, 256),# weapons:Weapon Type  index:73    from 3 To 4
        SetMemory(0x6572A0, Add, 196608),# weapons:Weapon Type  index:74    from 1 To 4
        SetMemory(0x6572A4, Add, 196608),# weapons:Weapon Type  index:78    from 1 To 4
        SetMemory(0x6572BC, Add, 3),# weapons:Weapon Type  index:100    from 1 To 4
        SetMemory(0x6572C0, Add, 3),# weapons:Weapon Type  index:104    from 1 To 4
        SetMemory(0x6572C4, Add, 256),# weapons:Weapon Type  index:109    from 3 To 4
        SetMemory(0x6572C4, Add, 16777216),# weapons:Weapon Type  index:111    from 3 To 4
        SetMemory(0x6572C8, Add, 65536),# weapons:Weapon Type  index:114    from 3 To 4
        SetMemory(0x6572CC, Add, 256),# weapons:Weapon Type  index:117    from 3 To 4
        SetMemory(0x656670, Add, -2),# weapons:Weapon Behavior  index:0    from 2 To 0
        SetMemory(0x656670, Add, -512),# weapons:Weapon Behavior  index:1    from 2 To 0
        SetMemory(0x656670, Add, -131072),# weapons:Weapon Behavior  index:2    from 2 To 0
        SetMemory(0x65667C, Add, -1),# weapons:Weapon Behavior  index:12    from 2 To 1
        SetMemory(0x65667C, Add, 134217728),# weapons:Weapon Behavior  index:15    from 0 To 8
        SetMemory(0x6566A0, Add, -7),# weapons:Weapon Behavior  index:48    from 7 To 0
        SetMemory(0x6566D4, Add, -1),# weapons:Weapon Behavior  index:100    from 2 To 1
        SetMemory(0x6566E4, Add, 768),# weapons:Weapon Behavior  index:117    from 2 To 5
        SetMemory(0x656710, Add, -512),# weapons:Explosion Type  index:25    from 3 To 1
        SetMemory(0x656714, Add, -1),# weapons:Explosion Type  index:28    from 2 To 1
        SetMemory(0x656728, Add, -65536),# weapons:Explosion Type  index:50    from 2 To 1
        SetMemory(0x65672C, Add, 65536),# weapons:Explosion Type  index:54    from 2 To 3
        SetMemory(0x65673C, Add, -131072),# weapons:Explosion Type  index:70    from 3 To 1
        SetMemory(0x6568C0, Add, -10),# weapons:Inner Splash Range  index:28    from 10 To 0
        SetMemory(0x6568F4, Add, 20),# weapons:Inner Splash Range  index:54    from 20 To 40
        SetMemory(0x657100, Add, -25),# weapons:Medium Splash Range  index:28    from 25 To 0
        SetMemory(0x657134, Add, 10),# weapons:Medium Splash Range  index:54    from 40 To 50
        SetMemory(0x6577B8, Add, -40),# weapons:Outer Splash Range  index:28    from 40 To 0
        SetMemory(0x656EB0, Add, 34),# weapons:Damage Amount  index:0    from 6 To 40
        SetMemory(0x656EB0, Add, 1441792),# weapons:Damage Amount  index:1    from 18 To 40
        SetMemory(0x656EB4, Add, 30),# weapons:Damage Amount  index:2    from 10 To 40
        SetMemory(0x656EB8, Add, -5898240),# weapons:Damage Amount  index:5    from 100 To 10
        SetMemory(0x656EC0, Add, 10),# weapons:Damage Amount  index:8    from 10 To 20
        SetMemory(0x656EC4, Add, 3276800),# weapons:Damage Amount  index:11    from 30 To 80
        SetMemory(0x656EC8, Add, -66),# weapons:Damage Amount  index:12    from 70 To 4
        SetMemory(0x656EC8, Add, 2293760),# weapons:Damage Amount  index:13    from 5 To 40
        SetMemory(0x656ECC, Add, -655360),# weapons:Damage Amount  index:15    from 20 To 10
        SetMemory(0x656ED0, Add, 2),# weapons:Damage Amount  index:16    from 8 To 10
        SetMemory(0x656ED4, Add, -327680),# weapons:Damage Amount  index:19    from 25 To 20
        SetMemory(0x656EE0, Add, 786432),# weapons:Damage Amount  index:25    from 8 To 20
        SetMemory(0x656EE8, Add, -140),# weapons:Damage Amount  index:28    from 150 To 10
        SetMemory(0x656EF4, Add, 1179648),# weapons:Damage Amount  index:35    from 5 To 23
        SetMemory(0x656EF8, Add, -655360),# weapons:Damage Amount  index:37    from 50 To 40
        SetMemory(0x656EFC, Add, 30),# weapons:Damage Amount  index:38    from 10 To 40
        SetMemory(0x656EFC, Add, 1310720),# weapons:Damage Amount  index:39    from 20 To 40
        SetMemory(0x656F00, Add, 10),# weapons:Damage Amount  index:40    from 20 To 30
        SetMemory(0x656F04, Add, 16),# weapons:Damage Amount  index:42    from 4 To 20
        SetMemory(0x656F04, Add, -169279488),# weapons:Damage Amount  index:43    from 2613 To 30
        SetMemory(0x656F0C, Add, 20),# weapons:Damage Amount  index:46    from 20 To 40
        SetMemory(0x656F10, Add, 1),# weapons:Damage Amount  index:48    from 9 To 10
        SetMemory(0x656F14, Add, 25),# weapons:Damage Amount  index:50    from 5 To 30
        SetMemory(0x656F18, Add, 12),# weapons:Damage Amount  index:52    from 15 To 27
        SetMemory(0x656F18, Add, -1966080),# weapons:Damage Amount  index:53    from 40 To 10
        SetMemory(0x656F1C, Add, -430),# weapons:Damage Amount  index:54    from 500 To 70
        SetMemory(0x656F30, Add, 84),# weapons:Damage Amount  index:64    from 16 To 100
        SetMemory(0x656F34, Add, 20),# weapons:Damage Amount  index:66    from 20 To 40
        SetMemory(0x656F38, Add, 327680),# weapons:Damage Amount  index:69    from 20 To 25
        SetMemory(0x656F3C, Add, 10),# weapons:Damage Amount  index:70    from 30 To 40
        SetMemory(0x656F40, Add, 2621440),# weapons:Damage Amount  index:73    from 0 To 40
        SetMemory(0x656F44, Add, 14),# weapons:Damage Amount  index:74    from 0 To 14
        SetMemory(0x656F4C, Add, 23),# weapons:Damage Amount  index:78    from 0 To 23
        SetMemory(0x656F4C, Add, 262144),# weapons:Damage Amount  index:79    from 6 To 10
        SetMemory(0x656F58, Add, -5242880),# weapons:Damage Amount  index:85    from 100 To 20
        SetMemory(0x656F78, Add, 25),# weapons:Damage Amount  index:100    from 5 To 30
        SetMemory(0x656F80, Add, -5),# weapons:Damage Amount  index:104    from 25 To 20
        SetMemory(0x656F88, Add, -131072),# weapons:Damage Amount  index:109    from 20 To 18
        SetMemory(0x656F94, Add, 10),# weapons:Damage Amount  index:114    from 20 To 30
        SetMemory(0x656F98, Add, 65142784),# weapons:Damage Amount  index:117    from 6 To 1000
        SetMemory(0x656FB8, Add, -150994944),# weapons:Weapon Cooldown  index:3    from 22 To 13
        SetMemory(0x656FC0, Add, -12),# weapons:Weapon Cooldown  index:8    from 22 To 10
        SetMemory(0x656FC0, Add, -117440512),# weapons:Weapon Cooldown  index:11    from 37 To 30
        SetMemory(0x656FC4, Add, -11),# weapons:Weapon Cooldown  index:12    from 37 To 26
        SetMemory(0x656FC8, Add, -8),# weapons:Weapon Cooldown  index:16    from 30 To 22
        SetMemory(0x656FC8, Add, -251658240),# weapons:Weapon Cooldown  index:19    from 30 To 15
        SetMemory(0x656FCC, Add, -2048),# weapons:Weapon Cooldown  index:21    from 30 To 22
        SetMemory(0x656FD4, Add, -53),# weapons:Weapon Cooldown  index:28    from 75 To 22
        SetMemory(0x656FE4, Add, -655360),# weapons:Weapon Cooldown  index:46    from 30 To 20
        SetMemory(0x656FE8, Add, -8),# weapons:Weapon Cooldown  index:48    from 30 To 22
        SetMemory(0x656FE8, Add, -720896),# weapons:Weapon Cooldown  index:50    from 22 To 11
        SetMemory(0x656FEC, Add, -2560),# weapons:Weapon Cooldown  index:53    from 32 To 22
        SetMemory(0x656FF8, Add, -983040),# weapons:Weapon Cooldown  index:66    from 30 To 15
        SetMemory(0x657000, Add, -3840),# weapons:Weapon Cooldown  index:73    from 30 To 15
        SetMemory(0x657004, Add, -2490368),# weapons:Weapon Cooldown  index:78    from 45 To 7
        SetMemory(0x657004, Add, 352321536),# weapons:Weapon Cooldown  index:79    from 1 To 22
        SetMemory(0x65700C, Add, -2816),# weapons:Weapon Cooldown  index:85    from 22 To 11
        SetMemory(0x65701C, Add, 7),# weapons:Weapon Cooldown  index:100    from 8 To 15
        SetMemory(0x657024, Add, 16128),# weapons:Weapon Cooldown  index:109    from 37 To 100
        SetMemory(0x657028, Add, -655360),# weapons:Weapon Cooldown  index:114    from 30 To 20
        SetMemory(0x65702C, Add, 8960),# weapons:Weapon Cooldown  index:117    from 15 To 50
        SetMemory(0x656548, Add, 1),# weapons:Damage Factor  index:104    from 1 To 2
        SetMemory(0x65699C, Add, 805306368),# weapons:Attack Angle  index:15    from 16 To 64
        SetMemory(0x6569A0, Add, 48),# weapons:Attack Angle  index:16    from 16 To 64
        SetMemory(0x6569A0, Add, 67108864),# weapons:Attack Angle  index:19    from 16 To 20
        SetMemory(0x6569A4, Add, 12288),# weapons:Attack Angle  index:21    from 16 To 64
        SetMemory(0x6569AC, Add, 48),# weapons:Attack Angle  index:28    from 16 To 64
        SetMemory(0x6569C0, Add, 48),# weapons:Attack Angle  index:48    from 16 To 64
        SetMemory(0x6569C0, Add, 262144),# weapons:Attack Angle  index:50    from 16 To 20
        SetMemory(0x6569C4, Add, -96),# weapons:Attack Angle  index:52    from 128 To 32
        SetMemory(0x6569C4, Add, -16384),# weapons:Attack Angle  index:53    from 128 To 64
        SetMemory(0x6569DC, Add, 805306368),# weapons:Attack Angle  index:79    from 16 To 64
        SetMemory(0x6569FC, Add, 2048),# weapons:Attack Angle  index:109    from 0 To 8
        SetMemory(0x656A00, Add, -262144),# weapons:Attack Angle  index:114    from 16 To 12
        SetMemory(0x657888, Add, 335544320),# weapons:Launch Spin  index:3    from 0 To 20
        SetMemory(0x657894, Add, 1073741824),# weapons:Launch Spin  index:15    from 0 To 64
        SetMemory(0x6578F0, Add, 30),# weapons:Launch Spin  index:104    from 0 To 30
        SetMemory(0x65791C, Add, 50),# weapons:Forward Offset  index:12    from 0 To 50
        SetMemory(0x657920, Add, -25),# weapons:Forward Offset  index:16    from 45 To 20
        SetMemory(0x657924, Add, -14080),# weapons:Forward Offset  index:21    from 75 To 20
        SetMemory(0x657940, Add, 10),# weapons:Forward Offset  index:48    from 5 To 15
        SetMemory(0x657978, Add, -45),# weapons:Forward Offset  index:104    from 45 To 0
        SetMemory(0x6567B8, Add, -28),# weapons:Icon  index:28    from 336 To 308
        SetMemory(0x656808, Add, -2686976),# weapons:Icon  index:69    from 355 To 314
        SetMemory(0x656828, Add, -5177344),# weapons:Icon  index:85    from 353 To 274
        SetMemory(0x656868, Add, -15597568),# weapons:Icon  index:117    from 323 To 85
        SetMemory(0x6CA31C, Add, 7012352),# flingy:Sprite  index:3    from 137 To 244
        SetMemory(0x6CA380, Add, -184),# flingy:Sprite  index:52    from 204 To 20
        SetMemory(0x6CA384, Add, -3670016),# flingy:Sprite  index:55    from 207 To 151
        SetMemory(0x6CA434, Add, 10485760),# flingy:Sprite  index:143    from 346 To 506
        SetMemory(0x6C9F08, Add, 549),# flingy:Speed  index:4    from 1 To 550
        SetMemory(0x6C9F0C, Add, -630),# flingy:Speed  index:5    from 1280 To 650
        SetMemory(0x6C9F14, Add, -360),# flingy:Speed  index:7    from 640 To 280
        SetMemory(0x6C9F18, Add, 424),# flingy:Speed  index:8    from 1 To 425
        SetMemory(0x6C9F1C, Add, 499),# flingy:Speed  index:9    from 1 To 500
        SetMemory(0x6C9F28, Add, 300),# flingy:Speed  index:12    from 213 To 513
        SetMemory(0x6C9F30, Add, 349),# flingy:Speed  index:14    from 1 To 350
        SetMemory(0x6C9F34, Add, 1129),# flingy:Speed  index:15    from 1 To 1130
        SetMemory(0x6C9F8C, Add, -800),# flingy:Speed  index:37    from 1280 To 480
        SetMemory(0x6C9F90, Add, -680),# flingy:Speed  index:38    from 1280 To 600
        SetMemory(0x6C9F98, Add, 424),# flingy:Speed  index:40    from 1 To 425
        SetMemory(0x6C9FA4, Add, -480),# flingy:Speed  index:43    from 1280 To 800
        SetMemory(0x6C9FAC, Add, -503),# flingy:Speed  index:45    from 853 To 350
        SetMemory(0x6C9FB0, Add, -303),# flingy:Speed  index:46    from 853 To 550
        SetMemory(0x6C9FB4, Add, 274),# flingy:Speed  index:47    from 1 To 275
        SetMemory(0x6C9FBC, Add, 639),# flingy:Speed  index:49    from 1 To 640
        SetMemory(0x6C9FC8, Add, 1050),# flingy:Speed  index:52    from 0 To 1050
        SetMemory(0x6CA010, Add, -315),# flingy:Speed  index:70    from 640 To 325
        SetMemory(0x6CA01C, Add, 524),# flingy:Speed  index:73    from 1 To 525
        SetMemory(0x6CA020, Add, 399),# flingy:Speed  index:74    from 1 To 400
        SetMemory(0x6CA024, Add, 579),# flingy:Speed  index:75    from 1 To 580
        SetMemory(0x6CA02C, Add, 549),# flingy:Speed  index:77    from 1 To 550
        SetMemory(0x6CA030, Add, 524),# flingy:Speed  index:78    from 1 To 525
        SetMemory(0x6CA038, Add, -927),# flingy:Speed  index:80    from 1707 To 780
        SetMemory(0x6CA03C, Add, -610),# flingy:Speed  index:81    from 1280 To 670
        SetMemory(0x6CA040, Add, 284),# flingy:Speed  index:82    from 1 To 285
        SetMemory(0x6CA058, Add, -657),# flingy:Speed  index:88    from 1707 To 1050
        SetMemory(0x6CA064, Add, -427),# flingy:Speed  index:91    from 427 To 0
        SetMemory(0x6CA0E0, Add, 1500),# flingy:Speed  index:122    from 0 To 1500
        SetMemory(0x6CA0E4, Add, 3000),# flingy:Speed  index:123    from 0 To 3000
        SetMemory(0x6CA13C, Add, -4267),# flingy:Speed  index:145    from 8533 To 4266
        SetMemory(0x6CA148, Add, -13000),# flingy:Speed  index:148    from 25600 To 12600
        SetMemory(0x6CA14C, Add, -8000),# flingy:Speed  index:149    from 17067 To 9067
        SetMemory(0x6CA174, Add, -9000),# flingy:Speed  index:159    from 17067 To 8067
        SetMemory(0x6CA184, Add, 4000),# flingy:Speed  index:163    from 8533 To 12533
        SetMemory(0x6CA190, Add, -4000),# flingy:Speed  index:166    from 8533 To 4533
        SetMemory(0x6CA1DC, Add, -610),# flingy:Speed  index:185    from 1280 To 670
        SetMemory(0x6CA1F4, Add, -627),# flingy:Speed  index:191    from 1707 To 1080
        SetMemory(0x6CA224, Add, -2600),# flingy:Speed  index:203    from 4800 To 2200
        SetMemory(0x6C9C80, Add, 149),# flingy:Acceleration  index:4    from 1 To 150
        SetMemory(0x6C9C80, Add, -2162688),# flingy:Acceleration  index:5    from 67 To 34
        SetMemory(0x6C9C84, Add, -917504),# flingy:Acceleration  index:7    from 27 To 13
        SetMemory(0x6C9C88, Add, 299),# flingy:Acceleration  index:8    from 1 To 300
        SetMemory(0x6C9C88, Add, 13041664),# flingy:Acceleration  index:9    from 1 To 200
        SetMemory(0x6C9C90, Add, 10),# flingy:Acceleration  index:12    from 27 To 37
        SetMemory(0x6C9C94, Add, 299),# flingy:Acceleration  index:14    from 1 To 300
        SetMemory(0x6C9C94, Add, 9764864),# flingy:Acceleration  index:15    from 1 To 150
        SetMemory(0x6C9CC0, Add, -589824),# flingy:Acceleration  index:37    from 33 To 24
        SetMemory(0x6C9CC4, Add, -93),# flingy:Acceleration  index:38    from 160 To 67
        SetMemory(0x6C9CC8, Add, 299),# flingy:Acceleration  index:40    from 1 To 300
        SetMemory(0x6C9CCC, Add, -1179648),# flingy:Acceleration  index:43    from 48 To 30
        SetMemory(0x6C9CD0, Add, -196608),# flingy:Acceleration  index:45    from 27 To 24
        SetMemory(0x6C9CD4, Add, 523),# flingy:Acceleration  index:46    from 27 To 550
        SetMemory(0x6C9CD4, Add, 13041664),# flingy:Acceleration  index:47    from 1 To 200
        SetMemory(0x6C9CD8, Add, 3211264),# flingy:Acceleration  index:49    from 1 To 50
        SetMemory(0x6C9CE0, Add, 160),# flingy:Acceleration  index:52    from 0 To 160
        SetMemory(0x6C9D04, Add, -19),# flingy:Acceleration  index:70    from 27 To 8
        SetMemory(0x6C9D08, Add, 2162688),# flingy:Acceleration  index:73    from 1 To 34
        SetMemory(0x6C9D0C, Add, 29),# flingy:Acceleration  index:74    from 1 To 30
        SetMemory(0x6C9D0C, Add, 13041664),# flingy:Acceleration  index:75    from 1 To 200
        SetMemory(0x6C9D10, Add, 13041664),# flingy:Acceleration  index:77    from 1 To 200
        SetMemory(0x6C9D14, Add, 199),# flingy:Acceleration  index:78    from 1 To 200
        SetMemory(0x6C9D18, Add, -33),# flingy:Acceleration  index:80    from 67 To 34
        SetMemory(0x6C9D18, Add, -2621440),# flingy:Acceleration  index:81    from 67 To 27
        SetMemory(0x6C9D1C, Add, 199),# flingy:Acceleration  index:82    from 1 To 200
        SetMemory(0x6C9D28, Add, -77),# flingy:Acceleration  index:88    from 100 To 23
        SetMemory(0x6C9D2C, Add, -2162688),# flingy:Acceleration  index:91    from 33 To 0
        SetMemory(0x6C9D6C, Add, 1500),# flingy:Acceleration  index:122    from 0 To 1500
        SetMemory(0x6C9D6C, Add, 4587520),# flingy:Acceleration  index:123    from 0 To 70
        SetMemory(0x6C9D98, Add, -21823488),# flingy:Acceleration  index:145    from 667 To 334
        SetMemory(0x6C9D9C, Add, 400),# flingy:Acceleration  index:146    from 267 To 667
        SetMemory(0x6C9DA0, Add, -5000),# flingy:Acceleration  index:148    from 8533 To 3533
        SetMemory(0x6C9DAC, Add, -130),# flingy:Acceleration  index:154    from 267 To 137
        SetMemory(0x6C9DB4, Add, -29491200),# flingy:Acceleration  index:159    from 850 To 400
        SetMemory(0x6C9DBC, Add, -300),# flingy:Acceleration  index:162    from 667 To 367
        SetMemory(0x6C9DBC, Add, 45875200),# flingy:Acceleration  index:163    from 667 To 1367
        SetMemory(0x6C9DC0, Add, -19660800),# flingy:Acceleration  index:165    from 667 To 367
        SetMemory(0x6C9DC4, Add, -400),# flingy:Acceleration  index:166    from 667 To 267
        SetMemory(0x6C9DE8, Add, -1966080),# flingy:Acceleration  index:185    from 48 To 18
        SetMemory(0x6C9DF4, Add, -2293760),# flingy:Acceleration  index:191    from 67 To 32
        SetMemory(0x6C9E0C, Add, -100),# flingy:Acceleration  index:202    from 267 To 167
        SetMemory(0x6C9E0C, Add, -170393600),# flingy:Acceleration  index:203    from 4800 To 2200
        SetMemory(0x6C994C, Add, -7435),# flingy:Halt Distance  index:7    from 7585 To 150
        SetMemory(0x6C9960, Add, 1000),# flingy:Halt Distance  index:12    from 840 To 1840
        SetMemory(0x6C99C4, Add, -20800),# flingy:Halt Distance  index:37    from 24824 To 4024
        SetMemory(0x6C99C8, Add, -4020),# flingy:Halt Distance  index:38    from 5120 To 1100
        SetMemory(0x6C99DC, Add, -7500),# flingy:Halt Distance  index:43    from 17067 To 9567
        SetMemory(0x6C99E0, Add, -8856),# flingy:Halt Distance  index:44    from 37756 To 28900
        SetMemory(0x6C99E4, Add, 10000),# flingy:Halt Distance  index:45    from 13474 To 23474
        SetMemory(0x6C99E8, Add, -13473),# flingy:Halt Distance  index:46    from 13474 To 1
        SetMemory(0x6C9A00, Add, 21500),# flingy:Halt Distance  index:52    from 0 To 21500
        SetMemory(0x6C9A48, Add, -6235),# flingy:Halt Distance  index:70    from 7585 To 1350
        SetMemory(0x6C9A70, Add, 10000),# flingy:Halt Distance  index:80    from 21745 To 31745
        SetMemory(0x6C9A90, Add, -7000),# flingy:Halt Distance  index:88    from 14569 To 7569
        SetMemory(0x6C9A9C, Add, -2763),# flingy:Halt Distance  index:91    from 2763 To 0
        SetMemory(0x6C9B74, Add, -27291),# flingy:Halt Distance  index:145    from 54582 To 27291
        SetMemory(0x6C9C14, Add, 9000),# flingy:Halt Distance  index:185    from 17067 To 26067
        SetMemory(0x6C9C2C, Add, 10000),# flingy:Halt Distance  index:191    from 17067 To 27067
        SetMemory(0x6C9E24, Add, 335544320),# flingy:Turn Radius  index:7    from 20 To 40
        SetMemory(0x6C9E28, Add, -13),# flingy:Turn Radius  index:8    from 27 To 14
        SetMemory(0x6C9E2C, Add, -218103808),# flingy:Turn Radius  index:15    from 27 To 14
        SetMemory(0x6C9E44, Add, -983040),# flingy:Turn Radius  index:38    from 40 To 25
        SetMemory(0x6C9E48, Add, -15),# flingy:Turn Radius  index:40    from 40 To 25
        SetMemory(0x6C9E48, Add, 167772160),# flingy:Turn Radius  index:43    from 30 To 40
        SetMemory(0x6C9E54, Add, 40),# flingy:Turn Radius  index:52    from 0 To 40
        SetMemory(0x6C9E64, Add, 983040),# flingy:Turn Radius  index:70    from 20 To 35
        SetMemory(0x6C9E70, Add, -5120),# flingy:Turn Radius  index:81    from 40 To 20
        SetMemory(0x6C9E70, Add, 262144),# flingy:Turn Radius  index:82    from 13 To 17
        SetMemory(0x6C9E74, Add, 29184),# flingy:Turn Radius  index:85    from 13 To 127
        SetMemory(0x6C9E78, Add, -452984832),# flingy:Turn Radius  index:91    from 27 To 0
        SetMemory(0x6C9EB8, Add, -851968),# flingy:Turn Radius  index:154    from 13 To 0
        SetMemory(0x6C9ED8, Add, -3840),# flingy:Turn Radius  index:185    from 30 To 15
        SetMemory(0x6C9858, Add, -33554432),# flingy:Movement Control  index:3    from 2 To 0
        SetMemory(0x6C985C, Add, -2),# flingy:Movement Control  index:4    from 2 To 0
        SetMemory(0x6C9860, Add, -2),# flingy:Movement Control  index:8    from 2 To 0
        SetMemory(0x6C9860, Add, -512),# flingy:Movement Control  index:9    from 2 To 0
        SetMemory(0x6C9864, Add, -131072),# flingy:Movement Control  index:14    from 2 To 0
        SetMemory(0x6C9864, Add, -33554432),# flingy:Movement Control  index:15    from 2 To 0
        SetMemory(0x6C9880, Add, -2),# flingy:Movement Control  index:40    from 2 To 0
        SetMemory(0x6C9884, Add, -131072),# flingy:Movement Control  index:46    from 2 To 0
        SetMemory(0x6C9884, Add, -33554432),# flingy:Movement Control  index:47    from 2 To 0
        SetMemory(0x6C9888, Add, -512),# flingy:Movement Control  index:49    from 2 To 0
        SetMemory(0x6C988C, Add, -2),# flingy:Movement Control  index:52    from 2 To 0
        SetMemory(0x6C98A0, Add, -512),# flingy:Movement Control  index:73    from 2 To 0
        SetMemory(0x6C98A0, Add, -131072),# flingy:Movement Control  index:74    from 2 To 0
        SetMemory(0x6C98A0, Add, -33554432),# flingy:Movement Control  index:75    from 2 To 0
        SetMemory(0x6C98A4, Add, -512),# flingy:Movement Control  index:77    from 2 To 0
        SetMemory(0x6C98A4, Add, -131072),# flingy:Movement Control  index:78    from 2 To 0
        SetMemory(0x6C98A8, Add, -131072),# flingy:Movement Control  index:82    from 2 To 0
        SetMemory(0x6C98B0, Add, 16777216),# flingy:Movement Control  index:91    from 1 To 2
        SetMemory(0x6C98D0, Add, -131072),# flingy:Movement Control  index:122    from 2 To 0
        SetMemory(0x6C98D0, Add, -33554432),# flingy:Movement Control  index:123    from 2 To 0
        SetMemory(0x666188, Add, -502),# sprites:Image File  index:20    from 618 To 116
        SetMemory(0x666300, Add, 184),# sprites:Image File  index:208    from 171 To 355
        SetMemory(0x66634C, Add, -27),# sprites:Image File  index:246    from 260 To 233
        SetMemory(0x666350, Add, 8060928),# sprites:Image File  index:249    from 266 To 389
        SetMemory(0x666354, Add, 117),# sprites:Image File  index:250    from 268 To 385
        SetMemory(0x666358, Add, 46202880),# sprites:Image File  index:253    from 278 To 983
        SetMemory(0x66635C, Add, 16711680),# sprites:Image File  index:255    from 285 To 540
        SetMemory(0x666378, Add, -183),# sprites:Image File  index:268    from 319 To 136
        SetMemory(0x6663C8, Add, 8978432),# sprites:Image File  index:309    from 422 To 559
        SetMemory(0x666414, Add, -213),# sprites:Image File  index:346    from 531 To 318
        SetMemory(0x666458, Add, -102),# sprites:Image File  index:380    from 546 To 444
        SetMemory(0x66655C, Add, -33357824),# sprites:Image File  index:511    from 961 To 452
        SetMemory(0x666560, Add, -433),# sprites:Image File  index:512    from 962 To 529
        SetMemory(0x666560, Add, -42270720),# sprites:Image File  index:513    from 963 To 318
        SetMemory(0x665D9C, Add, -65536),# sprites:Is Visible  index:342    from 1 To 0
        SetMemory(0x66C2B0, Add, -16777216),# images:Clickable  index:355    from 1 To 0
        SetMemory(0x669E2C, Add, 16),# images:Draw Function  index:4    from 0 To 16
        SetMemory(0x669E48, Add, 268435456),# images:Draw Function  index:35    from 0 To 16
        SetMemory(0x669EC0, Add, 2560),# images:Draw Function  index:153    from 0 To 10
        SetMemory(0x669ED4, Add, -2048),# images:Draw Function  index:173    from 10 To 2
        SetMemory(0x669F04, Add, 8),# images:Draw Function  index:220    from 9 To 17
        SetMemory(0x669FAC, Add, 117440512),# images:Draw Function  index:391    from 9 To 16
        SetMemory(0x669FD4, Add, 1792),# images:Draw Function  index:429    from 9 To 16
        SetMemory(0x669FE4, Add, 524288),# images:Draw Function  index:446    from 9 To 17
        SetMemory(0x669FE4, Add, 134217728),# images:Draw Function  index:447    from 9 To 17
        SetMemory(0x669FE8, Add, 1),# images:Draw Function  index:448    from 9 To 10
        SetMemory(0x66A018, Add, 167772160),# images:Draw Function  index:499    from 0 To 10
        SetMemory(0x66A020, Add, 16),# images:Draw Function  index:504    from 0 To 16
        SetMemory(0x66A020, Add, 1114112),# images:Draw Function  index:506    from 0 To 17
        SetMemory(0x66A020, Add, 268435456),# images:Draw Function  index:507    from 0 To 16
        SetMemory(0x66A024, Add, 7),# images:Draw Function  index:508    from 9 To 16
        SetMemory(0x66A028, Add, 4),# images:Draw Function  index:512    from 9 To 13
        SetMemory(0x66A028, Add, 1024),# images:Draw Function  index:513    from 9 To 13
        SetMemory(0x66A028, Add, 458752),# images:Draw Function  index:514    from 9 To 16
        SetMemory(0x66A028, Add, 268435456),# images:Draw Function  index:515    from 0 To 16
        SetMemory(0x66A02C, Add, 285212672),# images:Draw Function  index:519    from 0 To 17
        SetMemory(0x66A038, Add, 134217728),# images:Draw Function  index:531    from 9 To 17
        SetMemory(0x66A03C, Add, 1792),# images:Draw Function  index:533    from 9 To 16
        SetMemory(0x66A03C, Add, 524288),# images:Draw Function  index:534    from 9 To 17
        SetMemory(0x66A054, Add, 16777216),# images:Draw Function  index:559    from 9 To 10
        SetMemory(0x66ECDC, Add, 120),# images:Iscript ID  index:37    from 22 To 142
        SetMemory(0x66EE20, Add, -1),# images:Iscript ID  index:118    from 157 To 156
        SetMemory(0x66EEA4, Add, -132),# images:Iscript ID  index:151    from 163 To 31
        SetMemory(0x66F0DC, Add, 56),# images:Iscript ID  index:293    from 117 To 173
        SetMemory(0x66F138, Add, 109),# images:Iscript ID  index:316    from 131 To 240
        SetMemory(0x66F208, Add, -40),# images:Iscript ID  index:368    from 309 To 269
        SetMemory(0x66F2E0, Add, 57),# images:Iscript ID  index:422    from 273 To 330
        SetMemory(0x66F358, Add, -9),# images:Iscript ID  index:452    from 322 To 313
        SetMemory(0x66F414, Add, -249),# images:Iscript ID  index:499    from 331 To 82
        SetMemory(0x66F438, Add, 62),# images:Iscript ID  index:508    from 259 To 321
        SetMemory(0x66F444, Add, -175),# images:Iscript ID  index:511    from 264 To 89
        SetMemory(0x66F470, Add, -144),# images:Iscript ID  index:522    from 233 To 89
        SetMemory(0x66F4A4, Add, -154),# images:Iscript ID  index:535    from 243 To 89
        SetMemory(0x66F4B8, Add, -178),# images:Iscript ID  index:540    from 252 To 74
        SetMemory(0x66F4FC, Add, -60),# images:Iscript ID  index:557    from 321 To 261
        SetMemory(0x66F504, Add, -60),# images:Iscript ID  index:559    from 321 To 261
        SetMemory(0x66FAC8, Add, -279),# images:Iscript ID  index:928    from 368 To 89
        SetMemory(0x66FACC, Add, -208),# images:Iscript ID  index:929    from 369 To 161
        SetMemory(0x66FAF8, Add, -6),# images:Iscript ID  index:940    from 275 To 269
        SetMemory(0x66FB68, Add, -240),# images:Iscript ID  index:968    from 389 To 149
        SetMemory(0x66FB78, Add, -63),# images:Iscript ID  index:972    from 394 To 331
        SetMemory(0x66FB7C, Add, -69),# images:Iscript ID  index:973    from 390 To 321
        SetMemory(0x66FB84, Add, -301),# images:Iscript ID  index:975    from 390 To 89
        SetMemory(0x656394, Add, 225),# techdata:Energy Required  index:10    from 25 To 250
    ])

