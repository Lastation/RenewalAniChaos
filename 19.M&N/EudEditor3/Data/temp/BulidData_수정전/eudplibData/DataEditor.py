from eudplib import *


def onPluginStart():
    DoActions([  # Basic DatFile Actions
        SetMemory(0x66438C, Add, 4259839),# units:Special Ability Flags  index:195    from 536870913 To 541130752
        SetMemory(0x662B6C, Add, -95),# units:StarEdit Placement Box Width  index:195    from 96 To 1
        SetMemory(0x662B6C, Add, -4128768),# units:StarEdit Placement Box Height  index:195    from 64 To 1
        SetMemory(0x661DE0, Add, -47),# units:Unit Size Left  index:195    from 48 To 1
        SetMemory(0x661DE0, Add, -2031616),# units:Unit Size Up  index:195    from 32 To 1
        SetMemory(0x661DE4, Add, -46),# units:Unit Size Right  index:195    from 47 To 1
        SetMemory(0x661DE4, Add, -1966080),# units:Unit Size Down  index:195    from 31 To 1
        SetMemory(0x666398, Add, 204),# sprites:Image File  index:284    from 356 To 560
        SetMemory(0x66A058, Add, -2),# images:Draw Function  index:560    from 11 To 9
        SetMemory(0x66F508, Add, -200),# images:Iscript ID  index:560    from 289 To 89
    ])

