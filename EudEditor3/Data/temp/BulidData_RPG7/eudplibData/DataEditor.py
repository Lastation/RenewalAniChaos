from eudplib import *


def onPluginStart():
    DoActions([  # Basic DatFile Actions
        SetMemory(0x664524, Add, 26880),# units:Graphics  index:45    from 13 To 118
        SetMemory(0x6605F4, Add, -301989888),# units:Unit Direction  index:7    from 32 To 14
        SetMemory(0x663158, Add, -4096),# units:Elevation Level  index:9    from 16 To 0
        SetMemory(0x663178, Add, -786432),# units:Elevation Level  index:42    from 16 To 4
        SetMemory(0x663DD0, Add, -1),# units:Rank/Sublabel  index:0    from 2 To 1
        SetMemory(0x66409C, Add, -134217728),# units:Special Ability Flags  index:7    from 1476460552 To 1342242824
        SetMemory(0x664114, Add, -128),# units:Special Ability Flags  index:37    from 403768448 To 403768320
        SetMemory(0x664118, Add, -128),# units:Special Ability Flags  index:38    from 403767424 To 403767296
        SetMemory(0x66411C, Add, -128),# units:Special Ability Flags  index:39    from 469827712 To 469827584
        SetMemory(0x664124, Add, -128),# units:Special Ability Flags  index:41    from 403767432 To 403767304
        SetMemory(0x664128, Add, -130023428),# units:Special Ability Flags  index:42    from 436306052 To 306282624
        SetMemory(0x66438C, Add, 4194304),# units:Special Ability Flags  index:195    from 536870913 To 541065217
        SetMemory(0x662B6C, Add, -32),# units:StarEdit Placement Box Width  index:195    from 96 To 64
        SetMemory(0x662B6C, Add, 0),# units:StarEdit Placement Box Height  index:195    from 64 To 64
        SetMemory(0x661918, Add, -20),# units:Unit Size Left  index:42    from 25 To 5
        SetMemory(0x661DE0, Add, -47),# units:Unit Size Left  index:195    from 48 To 1
        SetMemory(0x661918, Add, -1310720),# units:Unit Size Up  index:42    from 25 To 5
        SetMemory(0x661DE0, Add, -2031616),# units:Unit Size Up  index:195    from 32 To 1
        SetMemory(0x66191C, Add, -19),# units:Unit Size Right  index:42    from 24 To 5
        SetMemory(0x661DE4, Add, -46),# units:Unit Size Right  index:195    from 47 To 1
        SetMemory(0x66191C, Add, -1245184),# units:Unit Size Down  index:42    from 24 To 5
        SetMemory(0x661DE4, Add, -1966080),# units:Unit Size Down  index:195    from 31 To 1
        SetMemory(0x656EB0, Add, 14),# weapons:Damage Amount  index:0    from 6 To 20
        SetMemory(0x666398, Add, 227),# sprites:Image File  index:284    from 356 To 583
        SetMemory(0x66A06C, Add, -100663296),# images:Draw Function  index:583    from 15 To 9
        SetMemory(0x66A094, Add, 9),# images:Draw Function  index:620    from 0 To 9
        SetMemory(0x66A094, Add, 589824),# images:Draw Function  index:622    from 0 To 9
        SetMemory(0x66A098, Add, 9),# images:Draw Function  index:624    from 0 To 9
        SetMemory(0x66A098, Add, 589824),# images:Draw Function  index:626    from 0 To 9
        SetMemory(0x66A09C, Add, 9),# images:Draw Function  index:628    from 0 To 9
        SetMemory(0x66A09C, Add, 589824),# images:Draw Function  index:630    from 0 To 9
        SetMemory(0x66A0A0, Add, 9),# images:Draw Function  index:632    from 0 To 9
        SetMemory(0x66A0A0, Add, 589824),# images:Draw Function  index:634    from 0 To 9
        SetMemory(0x66A0A4, Add, 9),# images:Draw Function  index:636    from 0 To 9
        SetMemory(0x66A0A4, Add, 589824),# images:Draw Function  index:638    from 0 To 9
    ])

