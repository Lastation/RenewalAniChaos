from eudplib import *


def onPluginStart():
    # 와이어 프레임
    WireOffset = f_epdread_epd(EPD(0x68C204))
    DoActions([
        SetMemoryEPD(WireOffset + 1, SetTo, 117571648),
        SetMemoryEPD(WireOffset + 2, SetTo, 4001378617),
        SetMemoryEPD(WireOffset + 3, SetTo, 100663296),
        SetMemoryEPD(WireOffset + 5, SetTo, 17235968),
        SetMemoryEPD(WireOffset + 6, SetTo, 1797406510),
        SetMemoryEPD(WireOffset + 7, SetTo, 327680),
        SetMemoryEPD(WireOffset + 17, SetTo, 100663296),
        SetMemoryEPD(WireOffset + 18, SetTo, 328152384),
        SetMemoryEPD(WireOffset + 19, SetTo, 33554432),
        SetMemoryEPD(WireOffset + 19, SetTo, 33554432),
        SetMemoryEPD(WireOffset + 20, SetTo, 1916550464),
        SetMemoryEPD(WireOffset + 21, SetTo, 100663297),
        SetMemoryEPD(WireOffset + 21, SetTo, 100663297),
        SetMemoryEPD(WireOffset + 22, SetTo, 328152384),
        SetMemoryEPD(WireOffset + 23, SetTo, 167903232),
        SetMemoryEPD(WireOffset + 25, SetTo, 17235970),
        SetMemoryEPD(WireOffset + 26, SetTo, 1797406510),
        SetMemoryEPD(WireOffset + 27, SetTo, 100728832),
        SetMemoryEPD(WireOffset + 39, SetTo, 100663296),
        SetMemoryEPD(WireOffset + 40, SetTo, 328152384),
        SetMemoryEPD(WireOffset + 41, SetTo, 117571584),
        SetMemoryEPD(WireOffset + 41, SetTo, 117571584),
        SetMemoryEPD(WireOffset + 42, SetTo, 4001378617),
        SetMemoryEPD(WireOffset + 43, SetTo, 83886080),
        SetMemoryEPD(WireOffset + 55, SetTo, 16777216),
        SetMemoryEPD(WireOffset + 56, SetTo, 2625910848),
        SetMemoryEPD(WireOffset + 57, SetTo, 16777216),
        SetMemoryEPD(WireOffset + 59, SetTo, 16777216),
        SetMemoryEPD(WireOffset + 60, SetTo, 2625910848),
        SetMemoryEPD(WireOffset + 61, SetTo, 0),
        SetMemoryEPD(WireOffset + 65, SetTo, 0),
        SetMemoryEPD(WireOffset + 66, SetTo, 2037923904),
        SetMemoryEPD(WireOffset + 67, SetTo, 851969),
        SetMemoryEPD(WireOffset + 75, SetTo, 0),
        SetMemoryEPD(WireOffset + 76, SetTo, 1471365184),
        SetMemoryEPD(WireOffset + 77, SetTo, 84606977),
        SetMemoryEPD(WireOffset + 79, SetTo, 17235968),
        SetMemoryEPD(WireOffset + 80, SetTo, 1797406510),
        SetMemoryEPD(WireOffset + 81, SetTo, 84082688),
        SetMemoryEPD(WireOffset + 123, SetTo, 50331649),
        SetMemoryEPD(WireOffset + 124, SetTo, 345062208),
        SetMemoryEPD(WireOffset + 125, SetTo, 16777217),
        SetMemoryEPD(WireOffset + 127, SetTo, 117571585),
        SetMemoryEPD(WireOffset + 128, SetTo, 4001378617),
        SetMemoryEPD(WireOffset + 129, SetTo, 16973824),
        SetMemoryEPD(WireOffset + 131, SetTo, 50397185),
        SetMemoryEPD(WireOffset + 132, SetTo, 1631665468),
        SetMemoryEPD(WireOffset + 133, SetTo, 17235969),
        SetMemoryEPD(WireOffset + 135, SetTo, 1),
        SetMemoryEPD(WireOffset + 136, SetTo, 1471365184),
        SetMemoryEPD(WireOffset + 137, SetTo, 50397185),
        SetMemoryEPD(WireOffset + 153, SetTo, 100663297),
        SetMemoryEPD(WireOffset + 154, SetTo, 328152384),
        SetMemoryEPD(WireOffset + 155, SetTo, 0),
        SetMemoryEPD(WireOffset + 155, SetTo, 0),
        SetMemoryEPD(WireOffset + 156, SetTo, 657866813),
        SetMemoryEPD(WireOffset + 157, SetTo, 17235969),
        SetMemoryEPD(WireOffset + 159, SetTo, 1),
        SetMemoryEPD(WireOffset + 160, SetTo, 1471365184),
        SetMemoryEPD(WireOffset + 161, SetTo, 1),
        SetMemoryEPD(WireOffset + 161, SetTo, 1),
        SetMemoryEPD(WireOffset + 162, SetTo, 2037923904),
        SetMemoryEPD(WireOffset + 163, SetTo, 100859905),
        SetMemoryEPD(WireOffset + 175, SetTo, 33554432),
        SetMemoryEPD(WireOffset + 176, SetTo, 1916550464),
        SetMemoryEPD(WireOffset + 177, SetTo, 1),
        SetMemoryEPD(WireOffset + 177, SetTo, 1),
        SetMemoryEPD(WireOffset + 178, SetTo, 2037923904),
        SetMemoryEPD(WireOffset + 179, SetTo, 100728833),
        SetMemoryEPD(WireOffset + 181, SetTo, 67436545),
        SetMemoryEPD(WireOffset + 182, SetTo, 3150067253),
        SetMemoryEPD(WireOffset + 183, SetTo, 100663297),
        SetMemoryEPD(WireOffset + 187, SetTo, 201654273),
        SetMemoryEPD(WireOffset + 188, SetTo, 3792055862),
        SetMemoryEPD(WireOffset + 189, SetTo, 16973824),
        SetMemoryEPD(WireOffset + 189, SetTo, 16973824),
        SetMemoryEPD(WireOffset + 190, SetTo, 1055014458),
        SetMemoryEPD(WireOffset + 191, SetTo, 100663297),
        SetMemoryEPD(WireOffset + 191, SetTo, 100663297),
        SetMemoryEPD(WireOffset + 192, SetTo, 328152384),
        SetMemoryEPD(WireOffset + 193, SetTo, 167903232),
        SetMemoryEPD(WireOffset + 199, SetTo, 117571585),
        SetMemoryEPD(WireOffset + 200, SetTo, 4001378617),
        SetMemoryEPD(WireOffset + 201, SetTo, 33554432),
        SetMemoryEPD(WireOffset + 201, SetTo, 33554432),
        SetMemoryEPD(WireOffset + 202, SetTo, 1916550464),
        SetMemoryEPD(WireOffset + 203, SetTo, 83951617),
        SetMemoryEPD(WireOffset + 205, SetTo, 117571586),
        SetMemoryEPD(WireOffset + 206, SetTo, 4001378617),
        SetMemoryEPD(WireOffset + 207, SetTo, 100663296),
        SetMemoryEPD(WireOffset + 209, SetTo, 33554434),
        SetMemoryEPD(WireOffset + 210, SetTo, 1916550464),
        SetMemoryEPD(WireOffset + 211, SetTo, 83951617),
        SetMemoryEPD(WireOffset + 251, SetTo, 67436546),
        SetMemoryEPD(WireOffset + 252, SetTo, 3150067253),
        SetMemoryEPD(WireOffset + 253, SetTo, 16777217),
        SetMemoryEPD(WireOffset + 279, SetTo, 118292483),
        SetMemoryEPD(WireOffset + 280, SetTo, 3417977891),
        SetMemoryEPD(WireOffset + 281, SetTo, 118292482),
        SetMemoryEPD(WireOffset + 281, SetTo, 118292482),
        SetMemoryEPD(WireOffset + 282, SetTo, 3417977891),
        SetMemoryEPD(WireOffset + 283, SetTo, 458754),
        SetMemoryEPD(WireOffset + 285, SetTo, 118292483),
        SetMemoryEPD(WireOffset + 286, SetTo, 3417977891),
        SetMemoryEPD(WireOffset + 287, SetTo, 134283266),
        SetMemoryEPD(WireOffset + 295, SetTo, 118292483),
        SetMemoryEPD(WireOffset + 296, SetTo, 3417977891),
        SetMemoryEPD(WireOffset + 297, SetTo, 100728834),
        SetMemoryEPD(WireOffset + 297, SetTo, 100728834),
        SetMemoryEPD(WireOffset + 298, SetTo, 1599157567),
        SetMemoryEPD(WireOffset + 299, SetTo, 16908288),
        SetMemoryEPD(WireOffset + 303, SetTo, 100728835),
        SetMemoryEPD(WireOffset + 304, SetTo, 1599157567),
        SetMemoryEPD(WireOffset + 305, SetTo, 100728832),
        SetMemoryEPD(WireOffset + 305, SetTo, 100728832),
        SetMemoryEPD(WireOffset + 306, SetTo, 1599157567),
        SetMemoryEPD(WireOffset + 307, SetTo, 83951616),
        SetMemoryEPD(WireOffset + 309, SetTo, 100728835),
        SetMemoryEPD(WireOffset + 310, SetTo, 1599157567),
        SetMemoryEPD(WireOffset + 311, SetTo, 67436544),
        SetMemoryEPD(WireOffset + 311, SetTo, 67436544),
        SetMemoryEPD(WireOffset + 312, SetTo, 3150067253),
        SetMemoryEPD(WireOffset + 313, SetTo, 196609),
        SetMemoryEPD(WireOffset + 319, SetTo, 67436547),
        SetMemoryEPD(WireOffset + 320, SetTo, 3150067253),
        SetMemoryEPD(WireOffset + 321, SetTo, 67436545),
        SetMemoryEPD(WireOffset + 321, SetTo, 67436545),
        SetMemoryEPD(WireOffset + 322, SetTo, 3150067253),
        SetMemoryEPD(WireOffset + 323, SetTo, 83951617),
        SetMemoryEPD(WireOffset + 327, SetTo, 67436547),
        SetMemoryEPD(WireOffset + 328, SetTo, 3150067253),
        SetMemoryEPD(WireOffset + 329, SetTo, 196609),
        SetMemoryEPD(WireOffset + 329, SetTo, 196609),
        SetMemoryEPD(WireOffset + 330, SetTo, 2330476602),
        SetMemoryEPD(WireOffset + 331, SetTo, 196611),
        SetMemoryEPD(WireOffset + 331, SetTo, 196611),
        SetMemoryEPD(WireOffset + 332, SetTo, 2330476602),
        SetMemoryEPD(WireOffset + 333, SetTo, 196611),
        SetMemoryEPD(WireOffset + 333, SetTo, 196611),
        SetMemoryEPD(WireOffset + 334, SetTo, 2330476602),
        SetMemoryEPD(WireOffset + 335, SetTo, 196611),
        SetMemoryEPD(WireOffset + 335, SetTo, 196611),
        SetMemoryEPD(WireOffset + 336, SetTo, 2330476602),
        SetMemoryEPD(WireOffset + 337, SetTo, 196611),
        SetMemoryEPD(WireOffset + 337, SetTo, 196611),
        SetMemoryEPD(WireOffset + 338, SetTo, 2330476602),
        SetMemoryEPD(WireOffset + 339, SetTo, 196611),
        SetMemoryEPD(WireOffset + 339, SetTo, 196611),
        SetMemoryEPD(WireOffset + 340, SetTo, 2330476602),
        SetMemoryEPD(WireOffset + 341, SetTo, 196611),
        SetMemoryEPD(WireOffset + 341, SetTo, 196611),
        SetMemoryEPD(WireOffset + 342, SetTo, 2330476602),
        SetMemoryEPD(WireOffset + 343, SetTo, 196611),
        SetMemoryEPD(WireOffset + 343, SetTo, 196611),
        SetMemoryEPD(WireOffset + 344, SetTo, 2330476602),
        SetMemoryEPD(WireOffset + 345, SetTo, 196611),
        SetMemoryEPD(WireOffset + 345, SetTo, 196611),
        SetMemoryEPD(WireOffset + 346, SetTo, 2330476602),
        SetMemoryEPD(WireOffset + 347, SetTo, 196611),
        SetMemoryEPD(WireOffset + 347, SetTo, 196611),
        SetMemoryEPD(WireOffset + 348, SetTo, 2330476602),
        SetMemoryEPD(WireOffset + 349, SetTo, 196611),
        SetMemoryEPD(WireOffset + 349, SetTo, 196611),
        SetMemoryEPD(WireOffset + 350, SetTo, 2330476602),
        SetMemoryEPD(WireOffset + 351, SetTo, 196611),
        SetMemoryEPD(WireOffset + 351, SetTo, 196611),
        SetMemoryEPD(WireOffset + 352, SetTo, 2330476602),
        SetMemoryEPD(WireOffset + 353, SetTo, 117440515),
    ])
    GrpOffset = f_epdread_epd(EPD(0x68C1FC))
    DoActions([
        SetMemoryEPD(GrpOffset + 1, SetTo, 33554464),
        SetMemoryEPD(GrpOffset + 2, SetTo, 1363287072),
        SetMemoryEPD(GrpOffset + 3, SetTo, 50331648),
        SetMemoryEPD(GrpOffset + 5, SetTo, 196608),
        SetMemoryEPD(GrpOffset + 6, SetTo, 710090775),
        SetMemoryEPD(GrpOffset + 7, SetTo, 196608),
        SetMemoryEPD(GrpOffset + 17, SetTo, 50331648),
        SetMemoryEPD(GrpOffset + 18, SetTo, 142482464),
        SetMemoryEPD(GrpOffset + 19, SetTo, 0),
        SetMemoryEPD(GrpOffset + 19, SetTo, 0),
        SetMemoryEPD(GrpOffset + 20, SetTo, 2245533472),
        SetMemoryEPD(GrpOffset + 21, SetTo, 50331648),
        SetMemoryEPD(GrpOffset + 21, SetTo, 50331648),
        SetMemoryEPD(GrpOffset + 22, SetTo, 142482464),
        SetMemoryEPD(GrpOffset + 23, SetTo, 83951616),
        SetMemoryEPD(GrpOffset + 25, SetTo, 196608),
        SetMemoryEPD(GrpOffset + 26, SetTo, 710090775),
        SetMemoryEPD(GrpOffset + 27, SetTo, 131072),
        SetMemoryEPD(GrpOffset + 39, SetTo, 50331648),
        SetMemoryEPD(GrpOffset + 40, SetTo, 142482464),
        SetMemoryEPD(GrpOffset + 41, SetTo, 33554432),
        SetMemoryEPD(GrpOffset + 41, SetTo, 33554432),
        SetMemoryEPD(GrpOffset + 42, SetTo, 1363287072),
        SetMemoryEPD(GrpOffset + 43, SetTo, 67108864),
        SetMemoryEPD(GrpOffset + 55, SetTo, 16777216),
        SetMemoryEPD(GrpOffset + 56, SetTo, 552082976),
        SetMemoryEPD(GrpOffset + 57, SetTo, 16777216),
        SetMemoryEPD(GrpOffset + 59, SetTo, 16777216),
        SetMemoryEPD(GrpOffset + 60, SetTo, 552082976),
        SetMemoryEPD(GrpOffset + 61, SetTo, 65536),
        SetMemoryEPD(GrpOffset + 65, SetTo, 0),
        SetMemoryEPD(GrpOffset + 66, SetTo, 2291474463),
        SetMemoryEPD(GrpOffset + 67, SetTo, 458752),
        SetMemoryEPD(GrpOffset + 75, SetTo, 0),
        SetMemoryEPD(GrpOffset + 76, SetTo, 2089164832),
        SetMemoryEPD(GrpOffset + 77, SetTo, 196608),
        SetMemoryEPD(GrpOffset + 79, SetTo, 196608),
        SetMemoryEPD(GrpOffset + 80, SetTo, 710090775),
        SetMemoryEPD(GrpOffset + 81, SetTo, 16973824),
        SetMemoryEPD(GrpOffset + 123, SetTo, 33554432),
        SetMemoryEPD(GrpOffset + 124, SetTo, 1679760672),
        SetMemoryEPD(GrpOffset + 125, SetTo, 16777216),
        SetMemoryEPD(GrpOffset + 127, SetTo, 33554432),
        SetMemoryEPD(GrpOffset + 128, SetTo, 1363287072),
        SetMemoryEPD(GrpOffset + 129, SetTo, 65536),
        SetMemoryEPD(GrpOffset + 131, SetTo, 0),
        SetMemoryEPD(GrpOffset + 132, SetTo, 2145132576),
        SetMemoryEPD(GrpOffset + 133, SetTo, 17039360),
        SetMemoryEPD(GrpOffset + 135, SetTo, 0),
        SetMemoryEPD(GrpOffset + 136, SetTo, 2089164832),
        SetMemoryEPD(GrpOffset + 137, SetTo, 0),
        SetMemoryEPD(GrpOffset + 153, SetTo, 50331648),
        SetMemoryEPD(GrpOffset + 154, SetTo, 142482464),
        SetMemoryEPD(GrpOffset + 155, SetTo, 0),
        SetMemoryEPD(GrpOffset + 155, SetTo, 0),
        SetMemoryEPD(GrpOffset + 156, SetTo, 1805525022),
        SetMemoryEPD(GrpOffset + 157, SetTo, 17039360),
        SetMemoryEPD(GrpOffset + 159, SetTo, 0),
        SetMemoryEPD(GrpOffset + 160, SetTo, 2089164832),
        SetMemoryEPD(GrpOffset + 161, SetTo, 0),
        SetMemoryEPD(GrpOffset + 161, SetTo, 0),
        SetMemoryEPD(GrpOffset + 162, SetTo, 2291474463),
        SetMemoryEPD(GrpOffset + 163, SetTo, 33554432),
        SetMemoryEPD(GrpOffset + 175, SetTo, 0),
        SetMemoryEPD(GrpOffset + 176, SetTo, 2245533472),
        SetMemoryEPD(GrpOffset + 177, SetTo, 0),
        SetMemoryEPD(GrpOffset + 177, SetTo, 0),
        SetMemoryEPD(GrpOffset + 178, SetTo, 2291474463),
        SetMemoryEPD(GrpOffset + 179, SetTo, 50331648),
        SetMemoryEPD(GrpOffset + 181, SetTo, 16842752),
        SetMemoryEPD(GrpOffset + 182, SetTo, 2518490396),
        SetMemoryEPD(GrpOffset + 183, SetTo, 50331648),
        SetMemoryEPD(GrpOffset + 187, SetTo, 16777216),
        SetMemoryEPD(GrpOffset + 188, SetTo, 1271864864),
        SetMemoryEPD(GrpOffset + 189, SetTo, 65536),
        SetMemoryEPD(GrpOffset + 189, SetTo, 65536),
        SetMemoryEPD(GrpOffset + 190, SetTo, 1939218463),
        SetMemoryEPD(GrpOffset + 191, SetTo, 50331648),
        SetMemoryEPD(GrpOffset + 191, SetTo, 50331648),
        SetMemoryEPD(GrpOffset + 192, SetTo, 142482464),
        SetMemoryEPD(GrpOffset + 193, SetTo, 83951616),
        SetMemoryEPD(GrpOffset + 199, SetTo, 33554432),
        SetMemoryEPD(GrpOffset + 200, SetTo, 1363287072),
        SetMemoryEPD(GrpOffset + 201, SetTo, 0),
        SetMemoryEPD(GrpOffset + 201, SetTo, 0),
        SetMemoryEPD(GrpOffset + 202, SetTo, 2245533472),
        SetMemoryEPD(GrpOffset + 203, SetTo, 50331648),
        SetMemoryEPD(GrpOffset + 205, SetTo, 33554432),
        SetMemoryEPD(GrpOffset + 206, SetTo, 1363287072),
        SetMemoryEPD(GrpOffset + 207, SetTo, 50331648),
        SetMemoryEPD(GrpOffset + 209, SetTo, 0),
        SetMemoryEPD(GrpOffset + 210, SetTo, 2245533472),
        SetMemoryEPD(GrpOffset + 211, SetTo, 83951616),
        SetMemoryEPD(GrpOffset + 251, SetTo, 16842752),
        SetMemoryEPD(GrpOffset + 252, SetTo, 2518490396),
        SetMemoryEPD(GrpOffset + 253, SetTo, 33554432),
    ])
    tranOffset = f_epdread_epd(EPD(0x68C1F4))
    DoActions([
        SetMemoryEPD(tranOffset + 55, SetTo, 83951616),
        SetMemoryEPD(tranOffset + 56, SetTo, 455608605),
        SetMemoryEPD(tranOffset + 57, SetTo, 83951616),
        SetMemoryEPD(tranOffset + 59, SetTo, 83951616),
        SetMemoryEPD(tranOffset + 60, SetTo, 455608605),
        SetMemoryEPD(tranOffset + 61, SetTo, 0),
        SetMemoryEPD(tranOffset + 65, SetTo, 83951616),
        SetMemoryEPD(tranOffset + 66, SetTo, 1512245533),
        SetMemoryEPD(tranOffset + 67, SetTo, 458752),
        SetMemoryEPD(tranOffset + 127, SetTo, 83886080),
        SetMemoryEPD(tranOffset + 128, SetTo, 129381664),
        SetMemoryEPD(tranOffset + 129, SetTo, 65536),
        SetMemoryEPD(tranOffset + 153, SetTo, 83886080),
        SetMemoryEPD(tranOffset + 154, SetTo, 129381664),
        SetMemoryEPD(tranOffset + 155, SetTo, 0),
        SetMemoryEPD(tranOffset + 155, SetTo, 0),
        SetMemoryEPD(tranOffset + 156, SetTo, 1865564191),
        SetMemoryEPD(tranOffset + 157, SetTo, 17235968),
        SetMemoryEPD(tranOffset + 161, SetTo, 83951616),
        SetMemoryEPD(tranOffset + 162, SetTo, 1512245533),
        SetMemoryEPD(tranOffset + 163, SetTo, 100859904),
        SetMemoryEPD(tranOffset + 175, SetTo, 83951616),
        SetMemoryEPD(tranOffset + 176, SetTo, 1512245533),
        SetMemoryEPD(tranOffset + 177, SetTo, 83951616),
        SetMemoryEPD(tranOffset + 177, SetTo, 83951616),
        SetMemoryEPD(tranOffset + 178, SetTo, 1512245533),
        SetMemoryEPD(tranOffset + 179, SetTo, 50331648),
        SetMemoryEPD(tranOffset + 187, SetTo, 33554432),
        SetMemoryEPD(tranOffset + 188, SetTo, 1470570016),
        SetMemoryEPD(tranOffset + 189, SetTo, 83951616),
        SetMemoryEPD(tranOffset + 199, SetTo, 83886080),
        SetMemoryEPD(tranOffset + 200, SetTo, 129381664),
        SetMemoryEPD(tranOffset + 201, SetTo, 83951616),
        SetMemoryEPD(tranOffset + 201, SetTo, 83951616),
        SetMemoryEPD(tranOffset + 202, SetTo, 1512245533),
        SetMemoryEPD(tranOffset + 203, SetTo, 100663296),
        SetMemoryEPD(tranOffset + 205, SetTo, 83951616),
        SetMemoryEPD(tranOffset + 206, SetTo, 1512245533),
        SetMemoryEPD(tranOffset + 207, SetTo, 100663296),
        SetMemoryEPD(tranOffset + 209, SetTo, 83951616),
        SetMemoryEPD(tranOffset + 210, SetTo, 1512245533),
        SetMemoryEPD(tranOffset + 211, SetTo, 83951616),
    ])
    DoActions([ # 스테이터스인포메이션
        SetMemory(0x519698, SetTo, 4344192),
        SetMemory(0x51969C, SetTo, 4353872),
        SetMemory(0x5196D4, SetTo, 4344192),
        SetMemory(0x5196D8, SetTo, 4353872),
        SetMemory(0x519914, SetTo, 4344192),
        SetMemory(0x519918, SetTo, 4353872),
        SetMemory(0x51995C, SetTo, 4344192),
        SetMemory(0x519960, SetTo, 4353872),
        SetMemory(0x519968, SetTo, 4344192),
        SetMemory(0x51996C, SetTo, 4353872),
        SetMemory(0x519980, SetTo, 4344192),
        SetMemory(0x519984, SetTo, 4353872),
        SetMemory(0x51998C, SetTo, 4344192),
        SetMemory(0x519990, SetTo, 4353872),
        SetMemory(0x519998, SetTo, 4344192),
        SetMemory(0x51999C, SetTo, 4353872),
        SetMemory(0x5199F8, SetTo, 4344192),
        SetMemory(0x5199FC, SetTo, 4353872),
        SetMemory(0x519A04, SetTo, 4344192),
        SetMemory(0x519A08, SetTo, 4353872),
        SetMemory(0x519A10, SetTo, 4344192),
        SetMemory(0x519A14, SetTo, 4353872),
        SetMemory(0x519A1C, SetTo, 4344192),
        SetMemory(0x519A20, SetTo, 4353872),
        SetMemory(0x519A28, SetTo, 4344192),
        SetMemory(0x519A2C, SetTo, 4353872),
        SetMemory(0x519A34, SetTo, 4344192),
        SetMemory(0x519A38, SetTo, 4353872),
        SetMemory(0x519A4C, SetTo, 4344192),
        SetMemory(0x519A50, SetTo, 4353872),
        SetMemory(0x519A88, SetTo, 4344192),
        SetMemory(0x519A8C, SetTo, 4353872),
        SetMemory(0x519A94, SetTo, 4344192),
        SetMemory(0x519A98, SetTo, 4353872),
        SetMemory(0x519AB8, SetTo, 4344192),
        SetMemory(0x519ABC, SetTo, 4353872),
        SetMemory(0x519AC4, SetTo, 4344192),
        SetMemory(0x519AC8, SetTo, 4353872),
        SetMemory(0x519ADC, SetTo, 4344192),
        SetMemory(0x519AE0, SetTo, 4353872),
        SetMemory(0x519AE8, SetTo, 4344192),
        SetMemory(0x519AEC, SetTo, 4353872),
        SetMemory(0x519B18, SetTo, 4344192),
        SetMemory(0x519B1C, SetTo, 4353872),
        SetMemory(0x519B24, SetTo, 4344192),
        SetMemory(0x519B28, SetTo, 4353872),
        SetMemory(0x519B48, SetTo, 4344192),
        SetMemory(0x519B4C, SetTo, 4353872),
        SetMemory(0x519B54, SetTo, 4344192),
        SetMemory(0x519B58, SetTo, 4353872),
        SetMemory(0x519B60, SetTo, 4344192),
        SetMemory(0x519B64, SetTo, 4353872),
        SetMemory(0x519B6C, SetTo, 4344192),
        SetMemory(0x519B70, SetTo, 4353872),
        SetMemory(0x519B78, SetTo, 4344192),
        SetMemory(0x519B7C, SetTo, 4353872),
        SetMemory(0x519B84, SetTo, 4344192),
        SetMemory(0x519B88, SetTo, 4353872),
        SetMemory(0x519B90, SetTo, 4344192),
        SetMemory(0x519B94, SetTo, 4353872),
        SetMemory(0x519B9C, SetTo, 4344192),
        SetMemory(0x519BA0, SetTo, 4353872),
        SetMemory(0x519BA8, SetTo, 4344192),
        SetMemory(0x519BAC, SetTo, 4353872),
        SetMemory(0x519BB4, SetTo, 4344192),
        SetMemory(0x519BB8, SetTo, 4353872),
        SetMemory(0x519BC0, SetTo, 4344192),
        SetMemory(0x519BC4, SetTo, 4353872),
        SetMemory(0x519BCC, SetTo, 4344192),
        SetMemory(0x519BD0, SetTo, 4353872),
        SetMemory(0x519BD8, SetTo, 4344192),
        SetMemory(0x519BDC, SetTo, 4353872),
    ])
    # 버튼셋
    bytebuffer = bytearray([1,0,228,0,208,130,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,208,130,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,208,130,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,208,130,66,0,112,51,66,0,0,0,0,0,156,2,0,0])
    btnptr0 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,38,1,80,148,66,0,16,51,66,0,3,0,3,0,158,1,0,0,2,0,99,1,80,148,66,0,16,51,66,0,4,0,4,0,159,1,0,0,3,0,15,1,80,148,66,0,16,51,66,0,5,0,5,0,160,1,0,0])
    btnptr112 = Db(bytebuffer)
    DoActions([
        SetMemory(0x5187EC, SetTo, btnptr0),
        SetMemory(0x5187E8, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x5187F8, SetTo, btnptr0),
        SetMemory(0x5187F4, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518804, SetTo, btnptr0),
        SetMemory(0x518800, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518840, SetTo, btnptr0),
        SetMemory(0x51883C, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x51884C, SetTo, btnptr0),
        SetMemory(0x518848, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518858, SetTo, btnptr0),
        SetMemory(0x518854, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518864, SetTo, btnptr0),
        SetMemory(0x518860, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x51887C, SetTo, btnptr0),
        SetMemory(0x518878, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x5188AC, SetTo, btnptr0),
        SetMemory(0x5188A8, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x5188D0, SetTo, btnptr0),
        SetMemory(0x5188CC, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x5188DC, SetTo, btnptr0),
        SetMemory(0x5188D8, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x5188E8, SetTo, btnptr0),
        SetMemory(0x5188E4, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518930, SetTo, btnptr0),
        SetMemory(0x51892C, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x51893C, SetTo, btnptr0),
        SetMemory(0x518938, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518948, SetTo, btnptr0),
        SetMemory(0x518944, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x51896C, SetTo, btnptr0),
        SetMemory(0x518968, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x5189A8, SetTo, btnptr0),
        SetMemory(0x5189A4, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x5189B4, SetTo, btnptr0),
        SetMemory(0x5189B0, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x5189C0, SetTo, btnptr0),
        SetMemory(0x5189BC, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x5189CC, SetTo, btnptr0),
        SetMemory(0x5189C8, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x5189F0, SetTo, btnptr0),
        SetMemory(0x5189EC, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x5189FC, SetTo, btnptr0),
        SetMemory(0x5189F8, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518A14, SetTo, btnptr0),
        SetMemory(0x518A10, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518A2C, SetTo, btnptr0),
        SetMemory(0x518A28, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518A50, SetTo, btnptr0),
        SetMemory(0x518A4C, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518A5C, SetTo, btnptr0),
        SetMemory(0x518A58, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518A68, SetTo, btnptr0),
        SetMemory(0x518A64, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518A74, SetTo, btnptr0),
        SetMemory(0x518A70, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518A80, SetTo, btnptr0),
        SetMemory(0x518A7C, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518A8C, SetTo, btnptr0),
        SetMemory(0x518A88, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518ABC, SetTo, btnptr0),
        SetMemory(0x518AB8, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518AC8, SetTo, btnptr0),
        SetMemory(0x518AC4, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518AE0, SetTo, btnptr0),
        SetMemory(0x518ADC, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518AEC, SetTo, btnptr0),
        SetMemory(0x518AE8, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518AF8, SetTo, btnptr0),
        SetMemory(0x518AF4, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518B04, SetTo, btnptr0),
        SetMemory(0x518B00, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518B10, SetTo, btnptr0),
        SetMemory(0x518B0C, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518B1C, SetTo, btnptr0),
        SetMemory(0x518B18, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518B34, SetTo, btnptr0),
        SetMemory(0x518B30, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518B40, SetTo, btnptr0),
        SetMemory(0x518B3C, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518B64, SetTo, btnptr0),
        SetMemory(0x518B60, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518B70, SetTo, btnptr0),
        SetMemory(0x518B6C, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518B7C, SetTo, btnptr0),
        SetMemory(0x518B78, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518B88, SetTo, btnptr0),
        SetMemory(0x518B84, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518B94, SetTo, btnptr0),
        SetMemory(0x518B90, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518BA0, SetTo, btnptr0),
        SetMemory(0x518B9C, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518BAC, SetTo, btnptr0),
        SetMemory(0x518BA8, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518C00, SetTo, btnptr0),
        SetMemory(0x518BFC, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518C0C, SetTo, btnptr0),
        SetMemory(0x518C08, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518C90, SetTo, btnptr0),
        SetMemory(0x518C8C, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518C9C, SetTo, btnptr0),
        SetMemory(0x518C98, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518CB4, SetTo, btnptr0),
        SetMemory(0x518CB0, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518CCC, SetTo, btnptr0),
        SetMemory(0x518CC8, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518D2C, SetTo, btnptr112),
        SetMemory(0x518D28, SetTo, 3),
    ])
    DoActions([
        SetMemory(0x518D5C, SetTo, btnptr0),
        SetMemory(0x518D58, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518DA4, SetTo, btnptr0),
        SetMemory(0x518DA0, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518DB0, SetTo, btnptr0),
        SetMemory(0x518DAC, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518DC8, SetTo, btnptr0),
        SetMemory(0x518DC4, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518DD4, SetTo, btnptr0),
        SetMemory(0x518DD0, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518DE0, SetTo, btnptr0),
        SetMemory(0x518DDC, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518E40, SetTo, btnptr0),
        SetMemory(0x518E3C, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518E4C, SetTo, btnptr0),
        SetMemory(0x518E48, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518E58, SetTo, btnptr0),
        SetMemory(0x518E54, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518E64, SetTo, btnptr0),
        SetMemory(0x518E60, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518E70, SetTo, btnptr0),
        SetMemory(0x518E6C, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518E7C, SetTo, btnptr0),
        SetMemory(0x518E78, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518E94, SetTo, btnptr0),
        SetMemory(0x518E90, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518ED0, SetTo, btnptr0),
        SetMemory(0x518ECC, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518EDC, SetTo, btnptr0),
        SetMemory(0x518ED8, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518F00, SetTo, btnptr0),
        SetMemory(0x518EFC, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518F0C, SetTo, btnptr0),
        SetMemory(0x518F08, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518F24, SetTo, btnptr0),
        SetMemory(0x518F20, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518F30, SetTo, btnptr0),
        SetMemory(0x518F2C, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518F60, SetTo, btnptr0),
        SetMemory(0x518F5C, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518F6C, SetTo, btnptr0),
        SetMemory(0x518F68, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518F90, SetTo, btnptr0),
        SetMemory(0x518F8C, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518F9C, SetTo, btnptr0),
        SetMemory(0x518F98, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518FA8, SetTo, btnptr0),
        SetMemory(0x518FA4, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518FB4, SetTo, btnptr0),
        SetMemory(0x518FB0, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518FC0, SetTo, btnptr0),
        SetMemory(0x518FBC, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518FCC, SetTo, btnptr0),
        SetMemory(0x518FC8, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518FD8, SetTo, btnptr0),
        SetMemory(0x518FD4, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518FE4, SetTo, btnptr0),
        SetMemory(0x518FE0, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518FF0, SetTo, btnptr0),
        SetMemory(0x518FEC, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518FFC, SetTo, btnptr0),
        SetMemory(0x518FF8, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x519008, SetTo, btnptr0),
        SetMemory(0x519004, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x519014, SetTo, btnptr0),
        SetMemory(0x519010, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x519020, SetTo, btnptr0),
        SetMemory(0x51901C, SetTo, 5),
    ])
    inputData = open('../temp/RequireData', 'rb').read()
    inputData_db = Db(inputData)
    inputDwordN = (len(inputData) + 3) // 4

    addrEPD = EPD(0x514178)
    f_repmovsd_epd(addrEPD, EPD(inputData_db), inputDwordN)


def beforeTriggerExec():
    DoActions([
        SetMemory(0x660A70 + 0, SetTo, 393217),
        SetMemory(0x660A70 + 4, SetTo, 1179661),
        SetMemory(0x660A70 + 8, SetTo, 1572864),
        SetMemory(0x660A70 + 12, SetTo, 2031616),
        SetMemory(0x660A70 + 16, SetTo, 2687012),
        SetMemory(0x660A70 + 20, SetTo, 3211264),
        SetMemory(0x660A70 + 24, SetTo, 56),
        SetMemory(0x660A70 + 28, SetTo, 64),
        SetMemory(0x660A70 + 32, SetTo, 0),
        SetMemory(0x660A70 + 36, SetTo, 0),
        SetMemory(0x660A70 + 40, SetTo, 0),
        SetMemory(0x660A70 + 44, SetTo, 0),
        SetMemory(0x660A70 + 48, SetTo, 0),
        SetMemory(0x660A70 + 52, SetTo, 0),
        SetMemory(0x660A70 + 56, SetTo, 0),
        SetMemory(0x660A70 + 60, SetTo, 0),
        SetMemory(0x660A70 + 64, SetTo, 69),
        SetMemory(0x660A70 + 68, SetTo, 75),
        SetMemory(0x660A70 + 72, SetTo, 5373952),
        SetMemory(0x660A70 + 76, SetTo, 5898326),
        SetMemory(0x660A70 + 80, SetTo, 6160384),
        SetMemory(0x660A70 + 84, SetTo, 6553697),
        SetMemory(0x660A70 + 88, SetTo, 7274603),
        SetMemory(0x660A70 + 92, SetTo, 7798899),
        SetMemory(0x660A70 + 96, SetTo, 8257536),
        SetMemory(0x660A70 + 100, SetTo, 127),
        SetMemory(0x660A70 + 104, SetTo, 0),
        SetMemory(0x660A70 + 108, SetTo, 0),
        SetMemory(0x660A70 + 112, SetTo, 0),
        SetMemory(0x660A70 + 116, SetTo, 131),
        SetMemory(0x660A70 + 120, SetTo, 9437324),
        SetMemory(0x660A70 + 124, SetTo, 10092693),
        SetMemory(0x660A70 + 128, SetTo, 10420379),
        SetMemory(0x660A70 + 132, SetTo, 10879138),
        SetMemory(0x660A70 + 136, SetTo, 11141120),
        SetMemory(0x660A70 + 140, SetTo, 11534509),
        SetMemory(0x660A70 + 144, SetTo, 12058804),
        SetMemory(0x660A70 + 148, SetTo, 0),
        SetMemory(0x660A70 + 152, SetTo, 0),
        SetMemory(0x660A70 + 156, SetTo, 0),
        SetMemory(0x660A70 + 160, SetTo, 191),
        SetMemory(0x660A70 + 164, SetTo, 12582912),
        SetMemory(0x660A70 + 168, SetTo, 13107396),
        SetMemory(0x660A70 + 172, SetTo, 13565952),
        SetMemory(0x660A70 + 176, SetTo, 208),
        SetMemory(0x660A70 + 180, SetTo, 0),
        SetMemory(0x660A70 + 184, SetTo, 0),
        SetMemory(0x660A70 + 188, SetTo, 0),
        SetMemory(0x660A70 + 192, SetTo, 0),
        SetMemory(0x660A70 + 196, SetTo, 13697024),
        SetMemory(0x660A70 + 200, SetTo, 0),
        SetMemory(0x660A70 + 204, SetTo, 14024914),
        SetMemory(0x660A70 + 208, SetTo, 220),
        SetMemory(0x660A70 + 212, SetTo, 14745821),
        SetMemory(0x660A70 + 216, SetTo, 15532263),
        SetMemory(0x660A70 + 220, SetTo, 16056561),
        SetMemory(0x660A70 + 224, SetTo, 16711930),
        SetMemory(0x660A70 + 228, SetTo, 17367300),
        SetMemory(0x660A70 + 232, SetTo, 18022670),
        SetMemory(0x660A70 + 236, SetTo, 280),
        SetMemory(0x660A70 + 240, SetTo, 285),
        SetMemory(0x660A70 + 244, SetTo, 19333410),
        SetMemory(0x660A70 + 248, SetTo, 19988780),
        SetMemory(0x660A70 + 252, SetTo, 0),
        SetMemory(0x660A70 + 256, SetTo, 0),
        SetMemory(0x660A70 + 260, SetTo, 20316160),
        SetMemory(0x660A70 + 264, SetTo, 20906298),
        SetMemory(0x660A70 + 268, SetTo, 21561668),
        SetMemory(0x660A70 + 272, SetTo, 22217038),
        SetMemory(0x660A70 + 276, SetTo, 23069016),
        SetMemory(0x660A70 + 280, SetTo, 24117611),
        SetMemory(0x660A70 + 284, SetTo, 25362808),
        SetMemory(0x660A70 + 288, SetTo, 391),
        SetMemory(0x660A70 + 292, SetTo, 395),
        SetMemory(0x660A70 + 296, SetTo, 26148864),
        SetMemory(0x660A70 + 300, SetTo, 0),
        SetMemory(0x660A70 + 304, SetTo, 0),
        SetMemory(0x660A70 + 308, SetTo, 26542482),
        SetMemory(0x660A70 + 312, SetTo, 27001241),
        SetMemory(0x660A70 + 316, SetTo, 27197440),
        SetMemory(0x660A70 + 320, SetTo, 419),
        SetMemory(0x660A70 + 324, SetTo, 27984295),
        SetMemory(0x660A70 + 328, SetTo, 28508591),
        SetMemory(0x660A70 + 332, SetTo, 29032887),
        SetMemory(0x660A70 + 336, SetTo, 29294592),
        SetMemory(0x660A70 + 340, SetTo, 29884867),
        SetMemory(0x660A70 + 344, SetTo, 460),
        SetMemory(0x660A70 + 348, SetTo, 0),
        SetMemory(0x660A70 + 352, SetTo, 0),
        SetMemory(0x660A70 + 356, SetTo, 0),
        SetMemory(0x660A70 + 360, SetTo, 0),
        SetMemory(0x660A70 + 364, SetTo, 0),
        SetMemory(0x660A70 + 368, SetTo, 0),
        SetMemory(0x660A70 + 372, SetTo, 0),
        SetMemory(0x660A70 + 376, SetTo, 0),
        SetMemory(0x660A70 + 380, SetTo, 0),
        SetMemory(0x660A70 + 384, SetTo, 0),
        SetMemory(0x660A70 + 388, SetTo, 0),
        SetMemory(0x660A70 + 392, SetTo, 0),
        SetMemory(0x660A70 + 396, SetTo, 0),
        SetMemory(0x660A70 + 400, SetTo, 0),
        SetMemory(0x660A70 + 404, SetTo, 0),
        SetMemory(0x660A70 + 408, SetTo, 0),
        SetMemory(0x660A70 + 412, SetTo, 0),
        SetMemory(0x660A70 + 416, SetTo, 0),
        SetMemory(0x660A70 + 420, SetTo, 0),
        SetMemory(0x660A70 + 424, SetTo, 0),
        SetMemory(0x660A70 + 428, SetTo, 0),
        SetMemory(0x660A70 + 432, SetTo, 0),
        SetMemory(0x660A70 + 436, SetTo, 0),
        SetMemory(0x660A70 + 440, SetTo, 0),
        SetMemory(0x660A70 + 444, SetTo, 0),
        SetMemory(0x660A70 + 448, SetTo, 0),
        SetMemory(0x660A70 + 452, SetTo, 0),
        SetMemory(0x6558C0 + 0, SetTo, 851969),
        SetMemory(0x6558C0 + 4, SetTo, 2424857),
        SetMemory(0x6558C0 + 8, SetTo, 2687015),
        SetMemory(0x6558C0 + 12, SetTo, 3538987),
        SetMemory(0x6558C0 + 16, SetTo, 5111874),
        SetMemory(0x6558C0 + 20, SetTo, 6815834),
        SetMemory(0x6558C0 + 24, SetTo, 8847478),
        SetMemory(0x6558C0 + 28, SetTo, 10289298),
        SetMemory(0x6558C0 + 32, SetTo, 11337896),
        SetMemory(0x6558C0 + 36, SetTo, 11665408),
        SetMemory(0x6558C0 + 40, SetTo, 12320951),
        SetMemory(0x6558C0 + 44, SetTo, 12976321),
        SetMemory(0x6558C0 + 48, SetTo, 13762763),
        SetMemory(0x6558C0 + 52, SetTo, 14680281),
        SetMemory(0x6558C0 + 56, SetTo, 15270116),
        SetMemory(0x6558C0 + 60, SetTo, 15794413),
        SetMemory(0x6558C0 + 64, SetTo, 16318709),
        SetMemory(0x6558C0 + 68, SetTo, 16843005),
        SetMemory(0x6558C0 + 72, SetTo, 17367301),
        SetMemory(0x6558C0 + 76, SetTo, 17891597),
        SetMemory(0x6558C0 + 80, SetTo, 18415893),
        SetMemory(0x6558C0 + 84, SetTo, 18940189),
        SetMemory(0x6558C0 + 88, SetTo, 293),
        SetMemory(0x6558C0 + 92, SetTo, 19464192),
        SetMemory(0x6558C0 + 96, SetTo, 19791872),
        SetMemory(0x6558C0 + 100, SetTo, 20119552),
        SetMemory(0x6558C0 + 104, SetTo, 20840761),
        SetMemory(0x6558C0 + 108, SetTo, 323),
        SetMemory(0x6558C0 + 112, SetTo, 0),
        SetMemory(0x6558C0 + 116, SetTo, 0),
        SetMemory(0x656198 + 0, SetTo, 393217),
        SetMemory(0x656198 + 4, SetTo, 1048587),
        SetMemory(0x656198 + 8, SetTo, 1376256),
        SetMemory(0x656198 + 12, SetTo, 1703936),
        SetMemory(0x656198 + 16, SetTo, 2359327),
        SetMemory(0x656198 + 20, SetTo, 3014697),
        SetMemory(0x656198 + 24, SetTo, 3670016),
        SetMemory(0x656198 + 28, SetTo, 3932160),
        SetMemory(0x656198 + 32, SetTo, 4456512),
        SetMemory(0x656198 + 36, SetTo, 4980808),
        SetMemory(0x656198 + 40, SetTo, 5505104),
        SetMemory(0x656198 + 44, SetTo, 88),
        SetMemory(0x656198 + 48, SetTo, 6422620),
        SetMemory(0x656198 + 52, SetTo, 6750208),
        SetMemory(0x656198 + 56, SetTo, 7077888),
        SetMemory(0x656198 + 60, SetTo, 7798897),
        SetMemory(0x656198 + 64, SetTo, 124),
        SetMemory(0x656198 + 68, SetTo, 0),
        SetMemory(0x656198 + 72, SetTo, 0),
        SetMemory(0x656198 + 76, SetTo, 0),
        SetMemory(0x656198 + 80, SetTo, 0),
        SetMemory(0x656198 + 84, SetTo, 0),
        SetMemory(0x6562F8 + 0, SetTo, 1048577),
        SetMemory(0x6562F8 + 4, SetTo, 2818082),
        SetMemory(0x6562F8 + 8, SetTo, 3670069),
        SetMemory(0x6562F8 + 12, SetTo, 5046343),
        SetMemory(0x6562F8 + 16, SetTo, 6619222),
        SetMemory(0x6562F8 + 20, SetTo, 8585326),
        SetMemory(0x6562F8 + 24, SetTo, 10944673),
        SetMemory(0x6562F8 + 28, SetTo, 11993264),
        SetMemory(0x6562F8 + 32, SetTo, 13697217),
        SetMemory(0x6562F8 + 36, SetTo, 14942430),
        SetMemory(0x6562F8 + 40, SetTo, 16318704),
        SetMemory(0x6562F8 + 44, SetTo, 17498370),
        SetMemory(0x6562F8 + 48, SetTo, 17957134),
        SetMemory(0x6562F8 + 52, SetTo, 18546688),
        SetMemory(0x6562F8 + 56, SetTo, 19071263),
        SetMemory(0x6562F8 + 60, SetTo, 19530022),
        SetMemory(0x6562F8 + 64, SetTo, 302),
        SetMemory(0x6562F8 + 68, SetTo, 307),
        SetMemory(0x6562F8 + 72, SetTo, 0),
        SetMemory(0x6562F8 + 76, SetTo, 0),
        SetMemory(0x6562F8 + 80, SetTo, 0),
        SetMemory(0x6562F8 + 84, SetTo, 0),
        SetMemory(0x665580 + 0, SetTo, 327682),
        SetMemory(0x665580 + 4, SetTo, 786440),
        SetMemory(0x665580 + 8, SetTo, 1310736),
        SetMemory(0x665580 + 12, SetTo, 1835032),
        SetMemory(0x665580 + 16, SetTo, 2621476),
        SetMemory(0x665580 + 20, SetTo, 3145772),
        SetMemory(0x665580 + 24, SetTo, 3670068),
        SetMemory(0x665580 + 28, SetTo, 4194364),
        SetMemory(0x665580 + 32, SetTo, 0),
        SetMemory(0x665580 + 36, SetTo, 5308484),
        SetMemory(0x665580 + 40, SetTo, 7405677),
        SetMemory(0x665580 + 44, SetTo, 7929973),
        SetMemory(0x665580 + 48, SetTo, 8126464),
        SetMemory(0x665580 + 52, SetTo, 8650880),
        SetMemory(0x665580 + 56, SetTo, 9568395),
        SetMemory(0x665580 + 60, SetTo, 10289305),
        SetMemory(0x665580 + 64, SetTo, 10813601),
        SetMemory(0x665580 + 68, SetTo, 11337897),
        SetMemory(0x665580 + 72, SetTo, 177),
        SetMemory(0x665580 + 76, SetTo, 11730944),
        SetMemory(0x665580 + 80, SetTo, 12124342),
        SetMemory(0x665580 + 84, SetTo, 0),
        SetMemory(0x665580 + 88, SetTo, 0),
        SetMemory(0x665580 + 92, SetTo, 192),
        SetMemory(0x665580 + 96, SetTo, 12910592),
        SetMemory(0x665580 + 100, SetTo, 13697225),
        SetMemory(0x665580 + 104, SetTo, 15139039),
        SetMemory(0x665580 + 108, SetTo, 16187631),
        SetMemory(0x665580 + 112, SetTo, 17629445),
        SetMemory(0x665580 + 116, SetTo, 18678037),
        SetMemory(0x665580 + 120, SetTo, 19726629),
        SetMemory(0x665580 + 124, SetTo, 309),
        SetMemory(0x665580 + 128, SetTo, 21102909),
        SetMemory(0x665580 + 132, SetTo, 21364736),
        SetMemory(0x665580 + 136, SetTo, 21626880),
        SetMemory(0x665580 + 140, SetTo, 22085965),
        SetMemory(0x665580 + 144, SetTo, 341),
        SetMemory(0x665580 + 148, SetTo, 345),
        SetMemory(0x665580 + 152, SetTo, 22806528),
        SetMemory(0x665580 + 156, SetTo, 23789921),
        SetMemory(0x665580 + 160, SetTo, 24183150),
        SetMemory(0x665580 + 164, SetTo, 372),
        SetMemory(0x665580 + 168, SetTo, 24772983),
        SetMemory(0x665580 + 172, SetTo, 381),
        SetMemory(0x665580 + 176, SetTo, 0),
        SetMemory(0x665580 + 180, SetTo, 384),
        SetMemory(0x665580 + 184, SetTo, 25559427),
        SetMemory(0x665580 + 188, SetTo, 26149260),
        SetMemory(0x665580 + 192, SetTo, 26411008),
        SetMemory(0x665580 + 196, SetTo, 0),
        SetMemory(0x665580 + 200, SetTo, 26804630),
        SetMemory(0x665580 + 204, SetTo, 27787686),
        SetMemory(0x665580 + 208, SetTo, 431),
        SetMemory(0x665580 + 212, SetTo, 28508160),
        SetMemory(0x665580 + 216, SetTo, 439),
        SetMemory(0x665580 + 220, SetTo, 29229056),
        SetMemory(0x665580 + 224, SetTo, 449),
        SetMemory(0x665580 + 228, SetTo, 0),
        SetMemory(0x665580 + 232, SetTo, 0),
        SetMemory(0x665580 + 236, SetTo, 0),
        SetMemory(0x665580 + 240, SetTo, 0),
        SetMemory(0x665580 + 244, SetTo, 29622272),
        SetMemory(0x665580 + 248, SetTo, 29884416),
        SetMemory(0x665580 + 252, SetTo, 30409164),
        SetMemory(0x665580 + 256, SetTo, 30933460),
        SetMemory(0x665580 + 260, SetTo, 31719900),
        SetMemory(0x665580 + 264, SetTo, 32178176),
        SetMemory(0x665580 + 268, SetTo, 32702958),
        SetMemory(0x665580 + 272, SetTo, 504),
        SetMemory(0x665580 + 276, SetTo, 0),
        SetMemory(0x665580 + 280, SetTo, 512),
        SetMemory(0x665580 + 284, SetTo, 0),
        SetMemory(0x665580 + 288, SetTo, 0),
        SetMemory(0x665580 + 292, SetTo, 0),
        SetMemory(0x665580 + 296, SetTo, 0),
        SetMemory(0x665580 + 300, SetTo, 0),
        SetMemory(0x665580 + 304, SetTo, 516),
        SetMemory(0x665580 + 308, SetTo, 34078720),
        SetMemory(0x665580 + 312, SetTo, 34734080),
        SetMemory(0x665580 + 316, SetTo, 0),
        SetMemory(0x665580 + 320, SetTo, 0),
        SetMemory(0x665580 + 324, SetTo, 0),
        SetMemory(0x665580 + 328, SetTo, 34996224),
        SetMemory(0x665580 + 332, SetTo, 36569626),
        SetMemory(0x665580 + 336, SetTo, 38470206),
        SetMemory(0x665580 + 340, SetTo, 40567384),
        SetMemory(0x665580 + 344, SetTo, 0),
        SetMemory(0x665580 + 348, SetTo, 41811968),
        SetMemory(0x665580 + 352, SetTo, 42336898),
        SetMemory(0x665580 + 356, SetTo, 650),
        SetMemory(0x665580 + 360, SetTo, 0),
        SetMemory(0x665580 + 364, SetTo, 654),
        SetMemory(0x665580 + 368, SetTo, 0),
        SetMemory(0x665580 + 372, SetTo, 0),
    ])
    

