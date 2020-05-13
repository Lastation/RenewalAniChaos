from eudplib import *


def onPluginStart():
    DoActions([  # Basic DatFile Actions
        SetMemory(0x663158, Add, -14),# units:Elevation Level  index:8    from 18 To 4
        SetMemory(0x663178, Add, -234881024),# units:Elevation Level  index:43    from 18 To 4
        SetMemory(0x66317C, Add, -14),# units:Elevation Level  index:44    from 18 To 4
        SetMemory(0x663184, Add, -234881024),# units:Elevation Level  index:55    from 18 To 4
        SetMemory(0x663188, Add, -14),# units:Elevation Level  index:56    from 18 To 4
        SetMemory(0x663194, Add, -201326592),# units:Elevation Level  index:71    from 16 To 4
        SetMemory(0x6631A0, Add, -14),# units:Elevation Level  index:80    from 18 To 4
        SetMemory(0x6631A4, Add, -786432),# units:Elevation Level  index:86    from 16 To 4
        SetMemory(0x660FC8, Add, -8388608),# units:Unknown (old Movement)  index:2    from 193 To 65
        SetMemory(0x662EA0, Add, 105),# units:Comp AI Idle  index:0    from 2 To 107
        SetMemory(0x662EA0, Add, 26880),# units:Comp AI Idle  index:1    from 2 To 107
        SetMemory(0x662EA0, Add, 6881280),# units:Comp AI Idle  index:2    from 2 To 107
        SetMemory(0x662EA0, Add, 1761607680),# units:Comp AI Idle  index:3    from 2 To 107
        SetMemory(0x662EA4, Add, 26880),# units:Comp AI Idle  index:5    from 2 To 107
        SetMemory(0x662EA8, Add, 105),# units:Comp AI Idle  index:8    from 2 To 107
        SetMemory(0x662EA8, Add, 6881280),# units:Comp AI Idle  index:10    from 2 To 107
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
        SetMemory(0x662268, Add, 105),# units:Human AI Idle  index:0    from 2 To 107
        SetMemory(0x662268, Add, 26880),# units:Human AI Idle  index:1    from 2 To 107
        SetMemory(0x662268, Add, 6881280),# units:Human AI Idle  index:2    from 2 To 107
        SetMemory(0x662268, Add, 1761607680),# units:Human AI Idle  index:3    from 2 To 107
        SetMemory(0x66226C, Add, 26880),# units:Human AI Idle  index:5    from 2 To 107
        SetMemory(0x662270, Add, 105),# units:Human AI Idle  index:8    from 2 To 107
        SetMemory(0x662270, Add, 6881280),# units:Human AI Idle  index:10    from 2 To 107
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
        SetMemory(0x6622C8, Add, 1761607680),# units:Human AI Idle  index:99    from 2 To 107
        SetMemory(0x6622CC, Add, 105),# units:Human AI Idle  index:100    from 2 To 107
        SetMemory(0x6622CC, Add, 6881280),# units:Human AI Idle  index:102    from 2 To 107
        SetMemory(0x6622D0, Add, 105),# units:Human AI Idle  index:104    from 2 To 107
        SetMemory(0x664898, Add, 105),# units:Return to Idle  index:0    from 2 To 107
        SetMemory(0x664898, Add, 26880),# units:Return to Idle  index:1    from 2 To 107
        SetMemory(0x664898, Add, 6881280),# units:Return to Idle  index:2    from 2 To 107
        SetMemory(0x664898, Add, 1761607680),# units:Return to Idle  index:3    from 2 To 107
        SetMemory(0x66489C, Add, 26880),# units:Return to Idle  index:5    from 2 To 107
        SetMemory(0x6648A0, Add, 105),# units:Return to Idle  index:8    from 2 To 107
        SetMemory(0x6648A0, Add, 6881280),# units:Return to Idle  index:10    from 2 To 107
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
        SetMemory(0x6648F8, Add, 1761607680),# units:Return to Idle  index:99    from 2 To 107
        SetMemory(0x6648FC, Add, 105),# units:Return to Idle  index:100    from 2 To 107
        SetMemory(0x6648FC, Add, 6881280),# units:Return to Idle  index:102    from 2 To 107
        SetMemory(0x664900, Add, 105),# units:Return to Idle  index:104    from 2 To 107
        SetMemory(0x663330, Add, -2816),# units:Attack Unit  index:17    from 21 To 10
        SetMemory(0x66335C, Add, -184549376),# units:Attack Unit  index:63    from 21 To 10
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
        SetMemory(0x664080, Add, -65536),# units:Special Ability Flags  index:0    from 402718720 To 402653184
        SetMemory(0x664084, Add, -2163200),# units:Special Ability Flags  index:1    from 404816384 To 402653184
        SetMemory(0x664088, Add, -1073741824),# units:Special Ability Flags  index:2    from 1476395008 To 402653184
        SetMemory(0x66408C, Add, -1073741824),# units:Special Ability Flags  index:3    from 1476395008 To 402653184
        SetMemory(0x664094, Add, -1107296256),# units:Special Ability Flags  index:5    from 1509949440 To 402653184
        SetMemory(0x6640A0, Add, -1109393924),# units:Special Ability Flags  index:8    from 1512047108 To 402653184
        SetMemory(0x6640A8, Add, -65600),# units:Special Ability Flags  index:10    from 402718784 To 402653184
        SetMemory(0x6640B0, Add, -1142947844),# units:Special Ability Flags  index:12    from 1545601028 To 402653184
        SetMemory(0x6640C0, Add, -2163264),# units:Special Ability Flags  index:16    from 404816448 To 402653184
        SetMemory(0x6640C4, Add, -1073741888),# units:Special Ability Flags  index:17    from 1476395072 To 402653184
        SetMemory(0x6640CC, Add, -1073741888),# units:Special Ability Flags  index:19    from 1476395072 To 402653184
        SetMemory(0x6640D0, Add, -65600),# units:Special Ability Flags  index:20    from 402718784 To 402653184
        SetMemory(0x6640D4, Add, -1109393988),# units:Special Ability Flags  index:21    from 1512047172 To 402653184
        SetMemory(0x6640DC, Add, -1107296320),# units:Special Ability Flags  index:23    from 1509949504 To 402653184
        SetMemory(0x6640EC, Add, -1142947908),# units:Special Ability Flags  index:27    from 1545601092 To 402653184
        SetMemory(0x6640F0, Add, -1142947908),# units:Special Ability Flags  index:28    from 1545601092 To 402653184
        SetMemory(0x6640F4, Add, -1142947908),# units:Special Ability Flags  index:29    from 1545601092 To 402653184
        SetMemory(0x664100, Add, -65536),# units:Special Ability Flags  index:32    from 402718720 To 402653184
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
        SetMemory(0x664174, Add, -4259840),# units:Special Ability Flags  index:61    from 406913024 To 402653184
        SetMemory(0x66417C, Add, -69206272),# units:Special Ability Flags  index:63    from 471859456 To 402653184
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
        SetMemory(0x6641C0, Add, -1107296324),# units:Special Ability Flags  index:80    from 1509949508 To 402653184
        SetMemory(0x6641D8, Add, -1109393476),# units:Special Ability Flags  index:86    from 1512046660 To 402653184
        SetMemory(0x6641DC, Add, -2162752),# units:Special Ability Flags  index:87    from 404815936 To 402653184
        SetMemory(0x6641E0, Add, -1107296324),# units:Special Ability Flags  index:88    from 1509949508 To 402653184
        SetMemory(0x66420C, Add, -2163264),# units:Special Ability Flags  index:99    from 404816448 To 402653184
        SetMemory(0x664210, Add, -2163264),# units:Special Ability Flags  index:100    from 404816448 To 402653184
        SetMemory(0x664218, Add, -1142947908),# units:Special Ability Flags  index:102    from 1545601092 To 402653184
        SetMemory(0x66421C, Add, -65664),# units:Special Ability Flags  index:103    from 403767424 To 403701760
        SetMemory(0x664220, Add, -2163392),# units:Special Ability Flags  index:104    from 404816576 To 402653184
        SetMemory(0x6635D4, Add, 256),# units:Armor Upgrade  index:5    from 1 To 2
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
        SetMemory(0x663630, Add, 16777216),# units:Armor Upgrade  index:99    from 0 To 1
        SetMemory(0x663634, Add, 2),# units:Armor Upgrade  index:100    from 0 To 2
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
        SetMemory(0x6620C4, Add, -65536),# units:Right-click Action  index:46    from 2 To 1
        SetMemory(0x6620CC, Add, -1),# units:Right-click Action  index:52    from 2 To 1
        SetMemory(0x6620D4, Add, -16777216),# units:Right-click Action  index:63    from 2 To 1
        SetMemory(0x6620D8, Add, -16777216),# units:Right-click Action  index:67    from 2 To 1
        SetMemory(0x661FC0, Add, -275),# units:Ready Sound  index:0    from 275 To 0
        SetMemory(0x661FC0, Add, -14745600),# units:Ready Sound  index:1    from 225 To 0
        SetMemory(0x661FC4, Add, -352),# units:Ready Sound  index:2    from 352 To 0
        SetMemory(0x661FC4, Add, -15794176),# units:Ready Sound  index:3    from 241 To 0
        SetMemory(0x661FC8, Add, -20709376),# units:Ready Sound  index:5    from 316 To 0
        SetMemory(0x661FD0, Add, -256),# units:Ready Sound  index:8    from 256 To 0
        SetMemory(0x661FD4, Add, -295),# units:Ready Sound  index:10    from 295 To 0
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
        SetMemory(0x660074, Add, -64815104),# units:What Sound Start  index:99    from 989 To 0
        SetMemory(0x660078, Add, -230),# units:What Sound Start  index:100    from 230 To 0
        SetMemory(0x66007C, Add, -449),# units:What Sound Start  index:102    from 449 To 0
        SetMemory(0x66007C, Add, -71106560),# units:What Sound Start  index:103    from 1085 To 0
        SetMemory(0x660080, Add, -1121),# units:What Sound Start  index:104    from 1121 To 0
        SetMemory(0x662BF0, Add, -290),# units:What Sound End  index:0    from 290 To 0
        SetMemory(0x662BF0, Add, -15269888),# units:What Sound End  index:1    from 233 To 0
        SetMemory(0x662BF4, Add, -363),# units:What Sound End  index:2    from 363 To 0
        SetMemory(0x662BF4, Add, -16449536),# units:What Sound End  index:3    from 251 To 0
        SetMemory(0x662BF8, Add, -21430272),# units:What Sound End  index:5    from 327 To 0
        SetMemory(0x662C00, Add, -268),# units:What Sound End  index:8    from 268 To 0
        SetMemory(0x662C04, Add, -302),# units:What Sound End  index:10    from 302 To 0
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
        SetMemory(0x662CB4, Add, -65011712),# units:What Sound End  index:99    from 992 To 0
        SetMemory(0x662CB8, Add, -233),# units:What Sound End  index:100    from 233 To 0
        SetMemory(0x662CBC, Add, -452),# units:What Sound End  index:102    from 452 To 0
        SetMemory(0x662CBC, Add, -71303168),# units:What Sound End  index:103    from 1088 To 0
        SetMemory(0x662CC0, Add, -1124),# units:What Sound End  index:104    from 1124 To 0
        SetMemory(0x663B38, Add, -280),# units:Piss Sound Start  index:0    from 280 To 0
        SetMemory(0x663B38, Add, -14811136),# units:Piss Sound Start  index:1    from 226 To 0
        SetMemory(0x663B3C, Add, -356),# units:Piss Sound Start  index:2    from 356 To 0
        SetMemory(0x663B3C, Add, -15859712),# units:Piss Sound Start  index:3    from 242 To 0
        SetMemory(0x663B40, Add, -20971520),# units:Piss Sound Start  index:5    from 320 To 0
        SetMemory(0x663B48, Add, -258),# units:Piss Sound Start  index:8    from 258 To 0
        SetMemory(0x663B4C, Add, -303),# units:Piss Sound Start  index:10    from 303 To 0
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
        SetMemory(0x662860, Add, 0),# units:StarEdit Placement Box Width  index:0    from 17 To 17
        SetMemory(0x662868, Add, -15),# units:StarEdit Placement Box Width  index:2    from 32 To 17
        SetMemory(0x66286C, Add, -15),# units:StarEdit Placement Box Width  index:3    from 32 To 17
        SetMemory(0x662874, Add, -15),# units:StarEdit Placement Box Width  index:5    from 32 To 17
        SetMemory(0x662880, Add, -21),# units:StarEdit Placement Box Width  index:8    from 38 To 17
        SetMemory(0x6628A0, Add, 2),# units:StarEdit Placement Box Width  index:16    from 15 To 17
        SetMemory(0x6628A4, Add, -15),# units:StarEdit Placement Box Width  index:17    from 32 To 17
        SetMemory(0x6628AC, Add, -15),# units:StarEdit Placement Box Width  index:19    from 32 To 17
        SetMemory(0x6628B4, Add, -21),# units:StarEdit Placement Box Width  index:21    from 38 To 17
        SetMemory(0x6628BC, Add, -15),# units:StarEdit Placement Box Width  index:23    from 32 To 17
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
        SetMemory(0x662954, Add, -7),# units:StarEdit Placement Box Width  index:61    from 24 To 17
        SetMemory(0x66295C, Add, -15),# units:StarEdit Placement Box Width  index:63    from 32 To 17
        SetMemory(0x662964, Add, -6),# units:StarEdit Placement Box Width  index:65    from 23 To 17
        SetMemory(0x662968, Add, -15),# units:StarEdit Placement Box Width  index:66    from 32 To 17
        SetMemory(0x66296C, Add, -7),# units:StarEdit Placement Box Width  index:67    from 24 To 17
        SetMemory(0x662970, Add, -15),# units:StarEdit Placement Box Width  index:68    from 32 To 17
        SetMemory(0x66297C, Add, -27),# units:StarEdit Placement Box Width  index:71    from 44 To 17
        SetMemory(0x662988, Add, -7),# units:StarEdit Placement Box Width  index:74    from 24 To 17
        SetMemory(0x66298C, Add, -7),# units:StarEdit Placement Box Width  index:75    from 24 To 17
        SetMemory(0x662990, Add, -15),# units:StarEdit Placement Box Width  index:76    from 32 To 17
        SetMemory(0x662994, Add, -7),# units:StarEdit Placement Box Width  index:77    from 24 To 17
        SetMemory(0x662998, Add, -15),# units:StarEdit Placement Box Width  index:78    from 32 To 17
        SetMemory(0x66299C, Add, -7),# units:StarEdit Placement Box Width  index:79    from 24 To 17
        SetMemory(0x6629A0, Add, -19),# units:StarEdit Placement Box Width  index:80    from 36 To 17
        SetMemory(0x6629B8, Add, -27),# units:StarEdit Placement Box Width  index:86    from 44 To 17
        SetMemory(0x6629BC, Add, -7),# units:StarEdit Placement Box Width  index:87    from 24 To 17
        SetMemory(0x6629EC, Add, 2),# units:StarEdit Placement Box Width  index:99    from 15 To 17
        SetMemory(0x6629F0, Add, 2),# units:StarEdit Placement Box Width  index:100    from 15 To 17
        SetMemory(0x662860, Add, -196608),# units:StarEdit Placement Box Height  index:0    from 20 To 17
        SetMemory(0x662868, Add, -983040),# units:StarEdit Placement Box Height  index:2    from 32 To 17
        SetMemory(0x66286C, Add, -983040),# units:StarEdit Placement Box Height  index:3    from 32 To 17
        SetMemory(0x662874, Add, -983040),# units:StarEdit Placement Box Height  index:5    from 32 To 17
        SetMemory(0x662880, Add, -851968),# units:StarEdit Placement Box Height  index:8    from 30 To 17
        SetMemory(0x6628A0, Add, -327680),# units:StarEdit Placement Box Height  index:16    from 22 To 17
        SetMemory(0x6628A4, Add, -983040),# units:StarEdit Placement Box Height  index:17    from 32 To 17
        SetMemory(0x6628AC, Add, -983040),# units:StarEdit Placement Box Height  index:19    from 32 To 17
        SetMemory(0x6628B4, Add, -851968),# units:StarEdit Placement Box Height  index:21    from 30 To 17
        SetMemory(0x6628BC, Add, -983040),# units:StarEdit Placement Box Height  index:23    from 32 To 17
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
        SetMemory(0x662954, Add, -851968),# units:StarEdit Placement Box Height  index:61    from 30 To 17
        SetMemory(0x66295C, Add, -983040),# units:StarEdit Placement Box Height  index:63    from 32 To 17
        SetMemory(0x662964, Add, -655360),# units:StarEdit Placement Box Height  index:65    from 27 To 17
        SetMemory(0x662968, Add, -983040),# units:StarEdit Placement Box Height  index:66    from 32 To 17
        SetMemory(0x66296C, Add, -720896),# units:StarEdit Placement Box Height  index:67    from 28 To 17
        SetMemory(0x662970, Add, -983040),# units:StarEdit Placement Box Height  index:68    from 32 To 17
        SetMemory(0x66297C, Add, -1769472),# units:StarEdit Placement Box Height  index:71    from 44 To 17
        SetMemory(0x662988, Add, -851968),# units:StarEdit Placement Box Height  index:74    from 30 To 17
        SetMemory(0x66298C, Add, -851968),# units:StarEdit Placement Box Height  index:75    from 30 To 17
        SetMemory(0x662990, Add, -983040),# units:StarEdit Placement Box Height  index:76    from 32 To 17
        SetMemory(0x662994, Add, -851968),# units:StarEdit Placement Box Height  index:77    from 30 To 17
        SetMemory(0x662998, Add, -983040),# units:StarEdit Placement Box Height  index:78    from 32 To 17
        SetMemory(0x66299C, Add, -720896),# units:StarEdit Placement Box Height  index:79    from 28 To 17
        SetMemory(0x6629A0, Add, -983040),# units:StarEdit Placement Box Height  index:80    from 32 To 17
        SetMemory(0x6629B8, Add, -1769472),# units:StarEdit Placement Box Height  index:86    from 44 To 17
        SetMemory(0x6629BC, Add, -720896),# units:StarEdit Placement Box Height  index:87    from 28 To 17
        SetMemory(0x6629EC, Add, -327680),# units:StarEdit Placement Box Height  index:99    from 22 To 17
        SetMemory(0x6629F0, Add, -327680),# units:StarEdit Placement Box Height  index:100    from 22 To 17
        SetMemory(0x6617D8, Add, -8),# units:Unit Size Left  index:2    from 16 To 8
        SetMemory(0x6617E0, Add, -8),# units:Unit Size Left  index:3    from 16 To 8
        SetMemory(0x6617F0, Add, -8),# units:Unit Size Left  index:5    from 16 To 8
        SetMemory(0x661808, Add, -11),# units:Unit Size Left  index:8    from 19 To 8
        SetMemory(0x661848, Add, 1),# units:Unit Size Left  index:16    from 7 To 8
        SetMemory(0x661850, Add, -8),# units:Unit Size Left  index:17    from 16 To 8
        SetMemory(0x661860, Add, -8),# units:Unit Size Left  index:19    from 16 To 8
        SetMemory(0x661870, Add, -11),# units:Unit Size Left  index:21    from 19 To 8
        SetMemory(0x661880, Add, -8),# units:Unit Size Left  index:23    from 16 To 8
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
        SetMemory(0x6619B0, Add, -4),# units:Unit Size Left  index:61    from 12 To 8
        SetMemory(0x6619C0, Add, -8),# units:Unit Size Left  index:63    from 16 To 8
        SetMemory(0x6619D0, Add, -3),# units:Unit Size Left  index:65    from 11 To 8
        SetMemory(0x6619D8, Add, -7),# units:Unit Size Left  index:66    from 15 To 8
        SetMemory(0x6619E0, Add, -4),# units:Unit Size Left  index:67    from 12 To 8
        SetMemory(0x6619E8, Add, -8),# units:Unit Size Left  index:68    from 16 To 8
        SetMemory(0x661A00, Add, -14),# units:Unit Size Left  index:71    from 22 To 8
        SetMemory(0x661A18, Add, -4),# units:Unit Size Left  index:74    from 12 To 8
        SetMemory(0x661A20, Add, -4),# units:Unit Size Left  index:75    from 12 To 8
        SetMemory(0x661A28, Add, -8),# units:Unit Size Left  index:76    from 16 To 8
        SetMemory(0x661A30, Add, -3),# units:Unit Size Left  index:77    from 11 To 8
        SetMemory(0x661A38, Add, -7),# units:Unit Size Left  index:78    from 15 To 8
        SetMemory(0x661A40, Add, -4),# units:Unit Size Left  index:79    from 12 To 8
        SetMemory(0x661A48, Add, -10),# units:Unit Size Left  index:80    from 18 To 8
        SetMemory(0x661A78, Add, -14),# units:Unit Size Left  index:86    from 22 To 8
        SetMemory(0x661A80, Add, -4),# units:Unit Size Left  index:87    from 12 To 8
        SetMemory(0x661AE0, Add, 1),# units:Unit Size Left  index:99    from 7 To 8
        SetMemory(0x661AE8, Add, 1),# units:Unit Size Left  index:100    from 7 To 8
        SetMemory(0x6617C8, Add, -65536),# units:Unit Size Up  index:0    from 9 To 8
        SetMemory(0x6617D8, Add, -524288),# units:Unit Size Up  index:2    from 16 To 8
        SetMemory(0x6617E0, Add, -524288),# units:Unit Size Up  index:3    from 16 To 8
        SetMemory(0x6617F0, Add, -524288),# units:Unit Size Up  index:5    from 16 To 8
        SetMemory(0x661808, Add, -458752),# units:Unit Size Up  index:8    from 15 To 8
        SetMemory(0x661848, Add, -131072),# units:Unit Size Up  index:16    from 10 To 8
        SetMemory(0x661850, Add, -524288),# units:Unit Size Up  index:17    from 16 To 8
        SetMemory(0x661860, Add, -524288),# units:Unit Size Up  index:19    from 16 To 8
        SetMemory(0x661870, Add, -458752),# units:Unit Size Up  index:21    from 15 To 8
        SetMemory(0x661880, Add, -524288),# units:Unit Size Up  index:23    from 16 To 8
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
        SetMemory(0x6619B0, Add, 131072),# units:Unit Size Up  index:61    from 6 To 8
        SetMemory(0x6619C0, Add, -524288),# units:Unit Size Up  index:63    from 16 To 8
        SetMemory(0x6619D0, Add, 196608),# units:Unit Size Up  index:65    from 5 To 8
        SetMemory(0x6619D8, Add, -458752),# units:Unit Size Up  index:66    from 15 To 8
        SetMemory(0x6619E0, Add, -131072),# units:Unit Size Up  index:67    from 10 To 8
        SetMemory(0x6619E8, Add, -524288),# units:Unit Size Up  index:68    from 16 To 8
        SetMemory(0x661A00, Add, -917504),# units:Unit Size Up  index:71    from 22 To 8
        SetMemory(0x661A18, Add, 131072),# units:Unit Size Up  index:74    from 6 To 8
        SetMemory(0x661A20, Add, 131072),# units:Unit Size Up  index:75    from 6 To 8
        SetMemory(0x661A28, Add, -524288),# units:Unit Size Up  index:76    from 16 To 8
        SetMemory(0x661A30, Add, 196608),# units:Unit Size Up  index:77    from 5 To 8
        SetMemory(0x661A38, Add, -458752),# units:Unit Size Up  index:78    from 15 To 8
        SetMemory(0x661A40, Add, -131072),# units:Unit Size Up  index:79    from 10 To 8
        SetMemory(0x661A48, Add, -524288),# units:Unit Size Up  index:80    from 16 To 8
        SetMemory(0x661A78, Add, -917504),# units:Unit Size Up  index:86    from 22 To 8
        SetMemory(0x661A80, Add, -393216),# units:Unit Size Up  index:87    from 14 To 8
        SetMemory(0x661AE0, Add, -131072),# units:Unit Size Up  index:99    from 10 To 8
        SetMemory(0x661AE8, Add, -131072),# units:Unit Size Up  index:100    from 10 To 8
        SetMemory(0x6617DC, Add, -7),# units:Unit Size Right  index:2    from 15 To 8
        SetMemory(0x6617E4, Add, -7),# units:Unit Size Right  index:3    from 15 To 8
        SetMemory(0x6617F4, Add, -7),# units:Unit Size Right  index:5    from 15 To 8
        SetMemory(0x66180C, Add, -10),# units:Unit Size Right  index:8    from 18 To 8
        SetMemory(0x66184C, Add, 1),# units:Unit Size Right  index:16    from 7 To 8
        SetMemory(0x661854, Add, -7),# units:Unit Size Right  index:17    from 15 To 8
        SetMemory(0x661864, Add, -7),# units:Unit Size Right  index:19    from 15 To 8
        SetMemory(0x661874, Add, -10),# units:Unit Size Right  index:21    from 18 To 8
        SetMemory(0x661884, Add, -7),# units:Unit Size Right  index:23    from 15 To 8
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
        SetMemory(0x6619B4, Add, -3),# units:Unit Size Right  index:61    from 11 To 8
        SetMemory(0x6619C4, Add, -7),# units:Unit Size Right  index:63    from 15 To 8
        SetMemory(0x6619D4, Add, -3),# units:Unit Size Right  index:65    from 11 To 8
        SetMemory(0x6619DC, Add, -8),# units:Unit Size Right  index:66    from 16 To 8
        SetMemory(0x6619E4, Add, -3),# units:Unit Size Right  index:67    from 11 To 8
        SetMemory(0x6619EC, Add, -7),# units:Unit Size Right  index:68    from 15 To 8
        SetMemory(0x661A04, Add, -13),# units:Unit Size Right  index:71    from 21 To 8
        SetMemory(0x661A1C, Add, -3),# units:Unit Size Right  index:74    from 11 To 8
        SetMemory(0x661A24, Add, -3),# units:Unit Size Right  index:75    from 11 To 8
        SetMemory(0x661A2C, Add, -7),# units:Unit Size Right  index:76    from 15 To 8
        SetMemory(0x661A34, Add, -3),# units:Unit Size Right  index:77    from 11 To 8
        SetMemory(0x661A3C, Add, -8),# units:Unit Size Right  index:78    from 16 To 8
        SetMemory(0x661A44, Add, -3),# units:Unit Size Right  index:79    from 11 To 8
        SetMemory(0x661A4C, Add, -9),# units:Unit Size Right  index:80    from 17 To 8
        SetMemory(0x661A7C, Add, -13),# units:Unit Size Right  index:86    from 21 To 8
        SetMemory(0x661A84, Add, -3),# units:Unit Size Right  index:87    from 11 To 8
        SetMemory(0x661AE4, Add, 1),# units:Unit Size Right  index:99    from 7 To 8
        SetMemory(0x661AEC, Add, 1),# units:Unit Size Right  index:100    from 7 To 8
        SetMemory(0x6617CC, Add, -131072),# units:Unit Size Down  index:0    from 10 To 8
        SetMemory(0x6617DC, Add, -458752),# units:Unit Size Down  index:2    from 15 To 8
        SetMemory(0x6617E4, Add, -458752),# units:Unit Size Down  index:3    from 15 To 8
        SetMemory(0x6617F4, Add, -458752),# units:Unit Size Down  index:5    from 15 To 8
        SetMemory(0x66180C, Add, -393216),# units:Unit Size Down  index:8    from 14 To 8
        SetMemory(0x66184C, Add, -196608),# units:Unit Size Down  index:16    from 11 To 8
        SetMemory(0x661854, Add, -458752),# units:Unit Size Down  index:17    from 15 To 8
        SetMemory(0x661864, Add, -458752),# units:Unit Size Down  index:19    from 15 To 8
        SetMemory(0x661874, Add, -393216),# units:Unit Size Down  index:21    from 14 To 8
        SetMemory(0x661884, Add, -458752),# units:Unit Size Down  index:23    from 15 To 8
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
        SetMemory(0x6619B4, Add, -720896),# units:Unit Size Down  index:61    from 19 To 8
        SetMemory(0x6619C4, Add, -458752),# units:Unit Size Down  index:63    from 15 To 8
        SetMemory(0x6619D4, Add, -327680),# units:Unit Size Down  index:65    from 13 To 8
        SetMemory(0x6619DC, Add, -524288),# units:Unit Size Down  index:66    from 16 To 8
        SetMemory(0x6619E4, Add, -327680),# units:Unit Size Down  index:67    from 13 To 8
        SetMemory(0x6619EC, Add, -458752),# units:Unit Size Down  index:68    from 15 To 8
        SetMemory(0x661A04, Add, -851968),# units:Unit Size Down  index:71    from 21 To 8
        SetMemory(0x661A1C, Add, -720896),# units:Unit Size Down  index:74    from 19 To 8
        SetMemory(0x661A24, Add, -720896),# units:Unit Size Down  index:75    from 19 To 8
        SetMemory(0x661A2C, Add, -458752),# units:Unit Size Down  index:76    from 15 To 8
        SetMemory(0x661A34, Add, -327680),# units:Unit Size Down  index:77    from 13 To 8
        SetMemory(0x661A3C, Add, -524288),# units:Unit Size Down  index:78    from 16 To 8
        SetMemory(0x661A44, Add, -327680),# units:Unit Size Down  index:79    from 13 To 8
        SetMemory(0x661A4C, Add, -458752),# units:Unit Size Down  index:80    from 15 To 8
        SetMemory(0x661A7C, Add, -851968),# units:Unit Size Down  index:86    from 21 To 8
        SetMemory(0x661A84, Add, -327680),# units:Unit Size Down  index:87    from 13 To 8
        SetMemory(0x661AE4, Add, -196608),# units:Unit Size Down  index:99    from 11 To 8
        SetMemory(0x661AEC, Add, -196608),# units:Unit Size Down  index:100    from 11 To 8
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
    ])

