from eudplib import *


def onPluginStart():
    DoActions([  # Basic DatFile Actions
        SetMemory(0x660FC8, Add, -8388608),# units:Unknown (old Movement)  index:2    from 193 To 65
        SetMemory(0x662EA0, Add, 105),# units:Comp AI Idle  index:0    from 2 To 107
        SetMemory(0x662EA4, Add, 26880),# units:Comp AI Idle  index:5    from 2 To 107
        SetMemory(0x662F04, Add, 105),# units:Comp AI Idle  index:100    from 2 To 107
        SetMemory(0x662268, Add, 105),# units:Human AI Idle  index:0    from 2 To 107
        SetMemory(0x66226C, Add, 26880),# units:Human AI Idle  index:5    from 2 To 107
        SetMemory(0x6622CC, Add, 105),# units:Human AI Idle  index:100    from 2 To 107
        SetMemory(0x664898, Add, 105),# units:Return to Idle  index:0    from 2 To 107
        SetMemory(0x66489C, Add, 26880),# units:Return to Idle  index:5    from 2 To 107
        SetMemory(0x6648FC, Add, 105),# units:Return to Idle  index:100    from 2 To 107
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
        SetMemory(0x661FC0, Add, -275),# units:Ready Sound  index:0    from 275 To 0
        SetMemory(0x661FC8, Add, -20709376),# units:Ready Sound  index:5    from 316 To 0
        SetMemory(0x65FFB0, Add, -287),# units:What Sound Start  index:0    from 287 To 0
        SetMemory(0x65FFB8, Add, -21233664),# units:What Sound Start  index:5    from 324 To 0
        SetMemory(0x660078, Add, -230),# units:What Sound Start  index:100    from 230 To 0
        SetMemory(0x662BF0, Add, -290),# units:What Sound End  index:0    from 290 To 0
        SetMemory(0x662BF8, Add, -21430272),# units:What Sound End  index:5    from 327 To 0
        SetMemory(0x662CB8, Add, -233),# units:What Sound End  index:100    from 233 To 0
        SetMemory(0x663B38, Add, -280),# units:Piss Sound Start  index:0    from 280 To 0
        SetMemory(0x663B40, Add, -20971520),# units:Piss Sound Start  index:5    from 320 To 0
        SetMemory(0x663C00, Add, -226),# units:Piss Sound Start  index:100    from 226 To 0
        SetMemory(0x661EE8, Add, -286),# units:Piss Sound End  index:0    from 286 To 0
        SetMemory(0x661EF0, Add, -21168128),# units:Piss Sound End  index:5    from 323 To 0
        SetMemory(0x661FB0, Add, -229),# units:Piss Sound End  index:100    from 229 To 0
        SetMemory(0x663C10, Add, -291),# units:Yes Sound Start  index:0    from 291 To 0
        SetMemory(0x663C18, Add, -21495808),# units:Yes Sound Start  index:5    from 328 To 0
        SetMemory(0x663CD8, Add, -234),# units:Yes Sound Start  index:100    from 234 To 0
        SetMemory(0x661440, Add, -294),# units:Yes Sound End  index:0    from 294 To 0
        SetMemory(0x661448, Add, -21692416),# units:Yes Sound End  index:5    from 331 To 0
        SetMemory(0x661508, Add, -237),# units:Yes Sound End  index:100    from 237 To 0
        SetMemory(0x662860, Add, 0),# units:StarEdit Placement Box Width  index:0    from 17 To 17
        SetMemory(0x662874, Add, -23),# units:StarEdit Placement Box Width  index:5    from 32 To 9
        SetMemory(0x6629F0, Add, 2),# units:StarEdit Placement Box Width  index:100    from 15 To 17
        SetMemory(0x662860, Add, -196608),# units:StarEdit Placement Box Height  index:0    from 20 To 17
        SetMemory(0x662874, Add, -1507328),# units:StarEdit Placement Box Height  index:5    from 32 To 9
        SetMemory(0x6629F0, Add, -327680),# units:StarEdit Placement Box Height  index:100    from 22 To 17
        SetMemory(0x6617F0, Add, -8),# units:Unit Size Left  index:5    from 16 To 8
        SetMemory(0x661AE8, Add, 1),# units:Unit Size Left  index:100    from 7 To 8
        SetMemory(0x6617C8, Add, -65536),# units:Unit Size Up  index:0    from 9 To 8
        SetMemory(0x6617F0, Add, -524288),# units:Unit Size Up  index:5    from 16 To 8
        SetMemory(0x661AE8, Add, -131072),# units:Unit Size Up  index:100    from 10 To 8
        SetMemory(0x6617F4, Add, -7),# units:Unit Size Right  index:5    from 15 To 8
        SetMemory(0x661AEC, Add, 1),# units:Unit Size Right  index:100    from 7 To 8
        SetMemory(0x6617CC, Add, -131072),# units:Unit Size Down  index:0    from 10 To 8
        SetMemory(0x6617F4, Add, -458752),# units:Unit Size Down  index:5    from 15 To 8
        SetMemory(0x661AEC, Add, -196608),# units:Unit Size Down  index:100    from 11 To 8
        SetMemory(0x6637A0, Add, 0),# units:Staredit Group Flags  index:0    from 10 To 10
        SetMemory(0x6637A4, Add, 0),# units:Staredit Group Flags  index:5    from 10 To 10
        SetMemory(0x6637E0, Add, -512),# units:Staredit Group Flags  index:65    from 12 To 10
        SetMemory(0x663804, Add, 0),# units:Staredit Group Flags  index:100    from 10 To 10
    ])

