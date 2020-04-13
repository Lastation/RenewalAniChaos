from eudplib import *


def onPluginStart():
    DoActions([  # Basic DatFile Actions
        SetMemory(0x656FC4, Add, -352321536),# weapons:Weapon Cooldown  index:15    from 22 To 1
        SetMemory(0x6564EC, Add, 16777216),# weapons:Damage Factor  index:15    from 1 To 2
        SetMemory(0x657894, Add, 1509949440),# weapons:Launch Spin  index:15    from 0 To 90
    ])

