from eudplib import *


def onPluginStart():
    # 와이어 프레임
    WireOffset = f_epdread_epd(EPD(0x68C204))
    DoActions([
        SetMemoryEPD(WireOffset + 187, SetTo, 201654273),
        SetMemoryEPD(WireOffset + 188, SetTo, 3792055862),
        SetMemoryEPD(WireOffset + 189, SetTo, 16973824),
        SetMemoryEPD(WireOffset + 189, SetTo, 16973824),
        SetMemoryEPD(WireOffset + 190, SetTo, 1055014458),
        SetMemoryEPD(WireOffset + 191, SetTo, 100663297),
        SetMemoryEPD(WireOffset + 191, SetTo, 100663297),
        SetMemoryEPD(WireOffset + 192, SetTo, 328152384),
        SetMemoryEPD(WireOffset + 193, SetTo, 167903232),
        SetMemoryEPD(WireOffset + 223, SetTo, 51183618),
        SetMemoryEPD(WireOffset + 224, SetTo, 1717648419),
        SetMemoryEPD(WireOffset + 225, SetTo, 0),
        SetMemoryEPD(WireOffset + 267, SetTo, 16777218),
        SetMemoryEPD(WireOffset + 268, SetTo, 4195630656),
        SetMemoryEPD(WireOffset + 269, SetTo, 2),
        SetMemoryEPD(WireOffset + 273, SetTo, 196610),
        SetMemoryEPD(WireOffset + 274, SetTo, 2330476602),
        SetMemoryEPD(WireOffset + 275, SetTo, 196611),
        SetMemoryEPD(WireOffset + 275, SetTo, 196611),
        SetMemoryEPD(WireOffset + 276, SetTo, 2330476602),
        SetMemoryEPD(WireOffset + 277, SetTo, 196611),
        SetMemoryEPD(WireOffset + 277, SetTo, 196611),
        SetMemoryEPD(WireOffset + 278, SetTo, 2330476602),
        SetMemoryEPD(WireOffset + 279, SetTo, 196611),
        SetMemoryEPD(WireOffset + 279, SetTo, 196611),
        SetMemoryEPD(WireOffset + 280, SetTo, 2330476602),
        SetMemoryEPD(WireOffset + 281, SetTo, 196611),
        SetMemoryEPD(WireOffset + 281, SetTo, 196611),
        SetMemoryEPD(WireOffset + 282, SetTo, 2330476602),
        SetMemoryEPD(WireOffset + 283, SetTo, 458755),
        SetMemoryEPD(WireOffset + 285, SetTo, 196611),
        SetMemoryEPD(WireOffset + 286, SetTo, 2330476602),
        SetMemoryEPD(WireOffset + 287, SetTo, 134283267),
        SetMemoryEPD(WireOffset + 295, SetTo, 196611),
        SetMemoryEPD(WireOffset + 296, SetTo, 2330476602),
        SetMemoryEPD(WireOffset + 297, SetTo, 196611),
        SetMemoryEPD(WireOffset + 297, SetTo, 196611),
        SetMemoryEPD(WireOffset + 298, SetTo, 2330476602),
        SetMemoryEPD(WireOffset + 299, SetTo, 16908291),
        SetMemoryEPD(WireOffset + 303, SetTo, 196611),
        SetMemoryEPD(WireOffset + 304, SetTo, 2330476602),
        SetMemoryEPD(WireOffset + 305, SetTo, 196611),
        SetMemoryEPD(WireOffset + 305, SetTo, 196611),
        SetMemoryEPD(WireOffset + 306, SetTo, 2330476602),
        SetMemoryEPD(WireOffset + 307, SetTo, 83951619),
        SetMemoryEPD(WireOffset + 309, SetTo, 196611),
        SetMemoryEPD(WireOffset + 310, SetTo, 2330476602),
        SetMemoryEPD(WireOffset + 311, SetTo, 196611),
        SetMemoryEPD(WireOffset + 319, SetTo, 196611),
        SetMemoryEPD(WireOffset + 320, SetTo, 2330476602),
        SetMemoryEPD(WireOffset + 321, SetTo, 196611),
        SetMemoryEPD(WireOffset + 321, SetTo, 196611),
        SetMemoryEPD(WireOffset + 322, SetTo, 2330476602),
        SetMemoryEPD(WireOffset + 323, SetTo, 83951619),
        SetMemoryEPD(WireOffset + 327, SetTo, 196611),
        SetMemoryEPD(WireOffset + 328, SetTo, 2330476602),
        SetMemoryEPD(WireOffset + 329, SetTo, 196611),
        SetMemoryEPD(WireOffset + 329, SetTo, 196611),
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
        SetMemoryEPD(GrpOffset + 187, SetTo, 16777216),
        SetMemoryEPD(GrpOffset + 188, SetTo, 1271864864),
        SetMemoryEPD(GrpOffset + 189, SetTo, 65536),
        SetMemoryEPD(GrpOffset + 189, SetTo, 65536),
        SetMemoryEPD(GrpOffset + 190, SetTo, 1939218463),
        SetMemoryEPD(GrpOffset + 191, SetTo, 50331648),
        SetMemoryEPD(GrpOffset + 191, SetTo, 50331648),
        SetMemoryEPD(GrpOffset + 192, SetTo, 142482464),
        SetMemoryEPD(GrpOffset + 193, SetTo, 83951616),
        SetMemoryEPD(GrpOffset + 223, SetTo, 33947648),
        SetMemoryEPD(GrpOffset + 224, SetTo, 679157266),
        SetMemoryEPD(GrpOffset + 225, SetTo, 83951616),
    ])
    tranOffset = f_epdread_epd(EPD(0x68C1F4))
    DoActions([
        SetMemoryEPD(tranOffset + 187, SetTo, 33554432),
        SetMemoryEPD(tranOffset + 188, SetTo, 1470570016),
        SetMemoryEPD(tranOffset + 189, SetTo, 83951616),
    ])
    DoActions([ # 스테이터스인포메이션
        SetMemory(0x5196E0, SetTo, 4344192),
        SetMemory(0x5196E4, SetTo, 4353872),
        SetMemory(0x5198D8, SetTo, 4344192),
        SetMemory(0x5198DC, SetTo, 4353872),
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
    bytebuffer = bytearray([1,0,228,0,208,130,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,208,130,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,208,130,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,208,130,66,0,112,51,66,0,0,0,0,0,156,2,0,0,8,0,2,0,208,130,66,0,112,151,66,0,0,0,0,0,72,4,72,4,9,0,2,0,208,130,66,0,112,151,66,0,0,0,0,0,73,4,73,4])
    btnptr2 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,208,130,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,208,130,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,208,130,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,208,130,66,0,112,51,66,0,0,0,0,0,156,2,0,0,8,0,3,0,208,130,66,0,112,151,66,0,0,0,0,0,74,4,74,4,9,0,3,0,208,130,66,0,112,151,66,0,0,0,0,0,75,4,75,4])
    btnptr3 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,96,136,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,208,130,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,96,136,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,96,136,66,0,112,51,66,0,0,0,0,0,156,2,0,0,8,0,5,0,208,130,66,0,112,151,66,0,0,0,0,0,26,4,26,4,9,0,5,0,208,130,66,0,112,151,66,0,0,0,0,0,27,4,27,4])
    btnptr5 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,208,130,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,208,130,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,208,130,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,208,130,66,0,112,51,66,0,0,0,0,0,156,2,0,0,8,0,16,0,208,130,66,0,112,151,66,0,0,0,0,0,30,4,30,4,9,0,16,0,208,130,66,0,112,151,66,0,0,0,0,0,31,4,31,4])
    btnptr16 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,208,130,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,208,130,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,208,130,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,208,130,66,0,112,51,66,0,0,0,0,0,156,2,0,0,8,0,17,0,208,130,66,0,112,151,66,0,0,0,0,0,100,4,100,4,9,0,17,0,208,130,66,0,112,151,66,0,0,0,0,0,101,4,101,4])
    btnptr17 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,208,130,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,208,130,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,208,130,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,208,130,66,0,112,51,66,0,0,0,0,0,156,2,0,0,8,0,19,0,208,130,66,0,112,151,66,0,0,0,0,0,92,4,92,4,9,0,19,0,208,130,66,0,112,151,66,0,0,0,0,0,93,4,93,4])
    btnptr19 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,208,130,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,208,130,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,208,130,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,208,130,66,0,112,51,66,0,0,0,0,0,156,2,0,0,8,0,21,0,208,130,66,0,112,151,66,0,0,0,0,0,50,4,50,4,9,0,21,0,208,130,66,0,112,151,66,0,0,0,0,0,51,4,51,4])
    btnptr21 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,96,136,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,208,130,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,96,136,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,96,136,66,0,112,51,66,0,0,0,0,0,156,2,0,0,8,0,23,0,208,130,66,0,112,151,66,0,0,0,0,0,68,4,68,4,9,0,23,0,208,130,66,0,112,151,66,0,0,0,0,0,69,4,69,4])
    btnptr23 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,192,131,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,192,131,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,160,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,192,131,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,192,131,66,0,112,51,66,0,0,0,0,0,156,2,0,0,8,0,37,0,208,130,66,0,112,151,66,0,0,0,0,0,48,4,48,4,9,0,37,0,208,130,66,0,112,151,66,0,0,0,0,0,49,4,49,4])
    btnptr37 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,192,131,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,192,131,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,160,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,192,131,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,192,131,66,0,112,51,66,0,0,0,0,0,156,2,0,0,8,0,38,0,208,130,66,0,112,151,66,0,0,0,0,0,96,4,96,4,9,0,38,0,208,130,66,0,112,151,66,0,0,0,0,0,97,4,97,4])
    btnptr38 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,208,130,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,208,130,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,208,130,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,208,130,66,0,112,51,66,0,0,0,0,0,156,2,0,0,8,0,39,0,208,130,66,0,112,151,66,0,0,0,0,0,88,4,88,4,9,0,39,0,208,130,66,0,112,151,66,0,0,0,0,0,89,4,89,4])
    btnptr39 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,208,130,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,208,130,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,208,130,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,208,130,66,0,112,51,66,0,0,0,0,0,156,2,0,0,8,0,40,0,208,130,66,0,112,151,66,0,0,0,0,0,90,4,90,4,9,0,40,0,208,130,66,0,112,151,66,0,0,0,0,0,91,4,91,4])
    btnptr40 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,208,130,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,208,130,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,208,130,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,208,130,66,0,112,51,66,0,0,0,0,0,156,2,0,0,8,0,43,0,208,130,66,0,112,151,66,0,0,0,0,0,70,4,70,4,9,0,43,0,208,130,66,0,112,151,66,0,0,0,0,0,71,4,71,4])
    btnptr43 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,208,130,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,208,130,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,208,130,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,208,130,66,0,112,51,66,0,0,0,0,0,156,2,0,0,8,0,44,0,208,130,66,0,112,151,66,0,0,0,0,0,36,4,36,4,9,0,44,0,208,130,66,0,112,151,66,0,0,0,0,0,37,4,37,4])
    btnptr44 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,192,131,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,192,131,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,192,131,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,192,131,66,0,112,51,66,0,0,0,0,0,156,2,0,0,8,0,46,0,208,130,66,0,112,151,66,0,0,0,0,0,98,4,98,4,9,0,46,0,208,130,66,0,112,151,66,0,0,0,0,0,99,4,99,4])
    btnptr46 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,208,130,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,208,130,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,208,130,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,208,130,66,0,112,51,66,0,0,0,0,0,156,2,0,0,8,0,48,0,208,130,66,0,112,151,66,0,0,0,0,0,44,4,44,4,9,0,48,0,208,130,66,0,112,151,66,0,0,0,0,0,45,4,45,4])
    btnptr48 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,208,130,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,208,130,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,208,130,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,208,130,66,0,112,51,66,0,0,0,0,0,156,2,0,0,8,0,51,0,208,130,66,0,112,151,66,0,0,0,0,0,64,4,64,4,9,0,51,0,208,130,66,0,112,151,66,0,0,0,0,0,65,4,65,4])
    btnptr51 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,192,131,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,192,131,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,192,131,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,192,131,66,0,112,51,66,0,0,0,0,0,156,2,0,0,8,0,52,0,208,130,66,0,112,151,66,0,0,0,0,0,46,4,46,4,9,0,52,0,208,130,66,0,112,151,66,0,0,0,0,0,47,4,47,4])
    btnptr52 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,192,131,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,192,131,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,160,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,192,131,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,192,131,66,0,112,51,66,0,0,0,0,0,156,2,0,0,8,0,53,0,208,130,66,0,112,151,66,0,0,0,0,0,38,4,38,4,9,0,53,0,208,130,66,0,112,151,66,0,0,0,0,0,39,4,39,4])
    btnptr53 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,192,131,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,192,131,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,160,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,192,131,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,192,131,66,0,112,51,66,0,0,0,0,0,156,2,0,0,8,0,54,0,208,130,66,0,112,151,66,0,0,0,0,0,24,4,24,4,9,0,54,0,208,130,66,0,112,151,66,0,0,0,0,0,25,4,25,4])
    btnptr54 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,208,130,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,208,130,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,208,130,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,208,130,66,0,112,51,66,0,0,0,0,0,156,2,0,0,8,0,55,0,208,130,66,0,112,151,66,0,0,0,0,0,34,4,34,4,9,0,55,0,208,130,66,0,112,151,66,0,0,0,0,0,35,4,35,4])
    btnptr55 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,208,130,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,208,130,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,208,130,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,208,130,66,0,112,51,66,0,0,0,0,0,156,2,0,0,8,0,56,0,208,130,66,0,112,151,66,0,0,0,0,0,42,4,42,4,9,0,56,0,208,130,66,0,112,151,66,0,0,0,0,0,43,4,43,4])
    btnptr56 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,208,130,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,208,130,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,208,130,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,208,130,66,0,112,51,66,0,0,0,0,0,156,2,0,0,8,0,61,0,208,130,66,0,112,151,66,0,0,0,0,0,94,4,94,4,9,0,61,0,208,130,66,0,112,151,66,0,0,0,0,0,95,4,95,4])
    btnptr61 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,208,130,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,208,130,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,208,130,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,208,130,66,0,112,51,66,0,0,0,0,0,156,2,0,0,8,0,63,0,208,130,66,0,112,151,66,0,0,0,0,0,76,4,76,4,9,0,63,0,208,130,66,0,112,151,66,0,0,0,0,0,77,4,77,4])
    btnptr63 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,208,130,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,208,130,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,208,130,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,208,130,66,0,112,51,66,0,0,0,0,0,156,2,0,0,8,0,66,0,208,130,66,0,112,151,66,0,0,0,0,0,84,4,84,4,9,0,66,0,208,130,66,0,112,151,66,0,0,0,0,0,85,4,85,4])
    btnptr66 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,208,130,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,208,130,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,208,130,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,208,130,66,0,112,51,66,0,0,0,0,0,156,2,0,0,8,0,67,0,208,130,66,0,112,151,66,0,0,0,0,0,66,4,66,4,9,0,67,0,208,130,66,0,112,151,66,0,0,0,0,0,67,4,67,4])
    btnptr67 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,208,130,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,208,130,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,208,130,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,208,130,66,0,112,51,66,0,0,0,0,0,156,2,0,0,8,0,68,0,208,130,66,0,112,151,66,0,0,0,0,0,78,4,78,4,9,0,68,0,208,130,66,0,112,151,66,0,0,0,0,0,79,4,79,4])
    btnptr68 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,208,130,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,208,130,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,208,130,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,208,130,66,0,112,51,66,0,0,0,0,0,156,2,0,0,8,0,71,0,208,130,66,0,112,151,66,0,0,0,0,0,86,4,86,4,9,0,71,0,208,130,66,0,112,151,66,0,0,0,0,0,87,4,87,4])
    btnptr71 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,208,130,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,208,130,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,208,130,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,208,130,66,0,112,51,66,0,0,0,0,0,156,2,0,0,8,0,74,0,208,130,66,0,112,151,66,0,0,0,0,0,60,4,60,4,9,0,74,0,208,130,66,0,112,151,66,0,0,0,0,0,61,4,61,4])
    btnptr74 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,208,130,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,208,130,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,208,130,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,208,130,66,0,112,51,66,0,0,0,0,0,156,2,0,0,8,0,75,0,208,130,66,0,112,151,66,0,0,0,0,0,54,4,54,4,9,0,75,0,208,130,66,0,112,151,66,0,0,0,0,0,55,4,55,4])
    btnptr75 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,208,130,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,208,130,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,208,130,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,208,130,66,0,112,51,66,0,0,0,0,0,156,2,0,0,8,0,76,0,208,130,66,0,112,151,66,0,0,0,0,0,32,4,33,4,9,0,76,0,208,130,66,0,112,151,66,0,0,0,0,0,33,4,33,4])
    btnptr76 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,208,130,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,208,130,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,208,130,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,208,130,66,0,112,51,66,0,0,0,0,0,156,2,0,0,8,0,77,0,208,130,66,0,112,151,66,0,0,0,0,0,58,4,58,4,9,0,77,0,208,130,66,0,112,151,66,0,0,0,0,0,59,4,59,4])
    btnptr77 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,208,130,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,208,130,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,208,130,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,208,130,66,0,112,51,66,0,0,0,0,0,156,2,0,0,8,0,78,0,208,130,66,0,112,151,66,0,0,0,0,0,82,4,82,4,9,0,78,0,208,130,66,0,112,151,66,0,0,0,0,0,83,4,83,4])
    btnptr78 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,208,130,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,208,130,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,208,130,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,208,130,66,0,112,51,66,0,0,0,0,0,156,2,0,0,8,0,79,0,208,130,66,0,112,151,66,0,0,0,0,0,62,4,62,4,9,0,79,0,208,130,66,0,112,151,66,0,0,0,0,0,63,4,63,4])
    btnptr79 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,208,130,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,208,130,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,208,130,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,208,130,66,0,112,51,66,0,0,0,0,0,156,2,0,0,8,0,80,0,208,130,66,0,112,151,66,0,0,0,0,0,52,4,52,4,9,0,80,0,208,130,66,0,112,151,66,0,0,0,0,0,53,4,53,4])
    btnptr80 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,208,130,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,208,130,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,208,130,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,208,130,66,0,112,51,66,0,0,0,0,0,156,2,0,0,8,0,86,0,208,130,66,0,112,151,66,0,0,0,0,0,40,4,40,4,9,0,86,0,208,130,66,0,112,151,66,0,0,0,0,0,41,4,41,4])
    btnptr86 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,208,130,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,208,130,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,208,130,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,208,130,66,0,112,51,66,0,0,0,0,0,156,2,0,0,8,0,79,0,208,130,66,0,112,151,66,0,0,0,0,0,80,4,80,4,9,0,79,0,208,130,66,0,112,151,66,0,0,0,0,0,81,4,81,4])
    btnptr87 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,208,130,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,208,130,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,208,130,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,208,130,66,0,112,51,66,0,0,0,0,0,156,2,0,0,8,0,99,0,208,130,66,0,112,151,66,0,0,0,0,0,56,4,56,4,9,0,99,0,208,130,66,0,112,151,66,0,0,0,0,0,57,4,57,4])
    btnptr99 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,208,130,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,208,130,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,208,130,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,208,130,66,0,112,51,66,0,0,0,0,0,156,2,0,0,8,0,100,0,208,130,66,0,112,151,66,0,0,0,0,0,28,4,28,4,9,0,100,0,208,130,66,0,112,151,66,0,0,0,0,0,29,4,29,4])
    btnptr100 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,38,1,80,148,66,0,16,51,66,0,3,0,3,0,220,5,220,5,2,0,99,1,80,148,66,0,16,51,66,0,4,0,4,0,221,5,221,5,3,0,15,1,80,148,66,0,16,51,66,0,5,0,5,0,222,5,222,5])
    btnptr112 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,219,0,96,142,66,0,176,52,66,0,60,0,60,0,91,2,0,0,2,0,83,0,96,142,66,0,176,52,66,0,83,0,83,0,96,2,211,2,3,0,84,0,96,142,66,0,176,52,66,0,84,0,84,0,86,2,212,2])
    btnptr155 = Db(bytebuffer)
    DoActions([
        SetMemory(0x518804, SetTo, btnptr2),
        SetMemory(0x518800, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x518810, SetTo, btnptr3),
        SetMemory(0x51880C, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x518828, SetTo, btnptr5),
        SetMemory(0x518824, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x5188AC, SetTo, btnptr16),
        SetMemory(0x5188A8, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x5188B8, SetTo, btnptr17),
        SetMemory(0x5188B4, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x5188D0, SetTo, btnptr19),
        SetMemory(0x5188CC, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x5188E8, SetTo, btnptr21),
        SetMemory(0x5188E4, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x518900, SetTo, btnptr23),
        SetMemory(0x5188FC, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x5189A8, SetTo, btnptr37),
        SetMemory(0x5189A4, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x5189B4, SetTo, btnptr38),
        SetMemory(0x5189B0, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x5189C0, SetTo, btnptr39),
        SetMemory(0x5189BC, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x5189CC, SetTo, btnptr40),
        SetMemory(0x5189C8, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x5189F0, SetTo, btnptr43),
        SetMemory(0x5189EC, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x5189FC, SetTo, btnptr44),
        SetMemory(0x5189F8, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x518A14, SetTo, btnptr46),
        SetMemory(0x518A10, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x518A2C, SetTo, btnptr48),
        SetMemory(0x518A28, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x518A50, SetTo, btnptr51),
        SetMemory(0x518A4C, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x518A5C, SetTo, btnptr52),
        SetMemory(0x518A58, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x518A68, SetTo, btnptr53),
        SetMemory(0x518A64, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x518A74, SetTo, btnptr54),
        SetMemory(0x518A70, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x518A80, SetTo, btnptr55),
        SetMemory(0x518A7C, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x518A8C, SetTo, btnptr56),
        SetMemory(0x518A88, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x518AC8, SetTo, btnptr61),
        SetMemory(0x518AC4, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x518AE0, SetTo, btnptr63),
        SetMemory(0x518ADC, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x518B04, SetTo, btnptr66),
        SetMemory(0x518B00, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x518B10, SetTo, btnptr67),
        SetMemory(0x518B0C, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x518B1C, SetTo, btnptr68),
        SetMemory(0x518B18, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x518B40, SetTo, btnptr71),
        SetMemory(0x518B3C, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x518B64, SetTo, btnptr74),
        SetMemory(0x518B60, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x518B70, SetTo, btnptr75),
        SetMemory(0x518B6C, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x518B7C, SetTo, btnptr76),
        SetMemory(0x518B78, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x518B88, SetTo, btnptr77),
        SetMemory(0x518B84, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x518B94, SetTo, btnptr78),
        SetMemory(0x518B90, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x518BA0, SetTo, btnptr79),
        SetMemory(0x518B9C, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x518BAC, SetTo, btnptr80),
        SetMemory(0x518BA8, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x518BF4, SetTo, btnptr86),
        SetMemory(0x518BF0, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x518C00, SetTo, btnptr87),
        SetMemory(0x518BFC, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x518C90, SetTo, btnptr99),
        SetMemory(0x518C8C, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x518C9C, SetTo, btnptr100),
        SetMemory(0x518C98, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x518D2C, SetTo, btnptr112),
        SetMemory(0x518D28, SetTo, 3),
    ])
    DoActions([
        SetMemory(0x518F30, SetTo, btnptr155),
        SetMemory(0x518F2C, SetTo, 3),
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
        SetMemory(0x660A70 + 96, SetTo, 0),
        SetMemory(0x660A70 + 100, SetTo, 126),
        SetMemory(0x660A70 + 104, SetTo, 0),
        SetMemory(0x660A70 + 108, SetTo, 0),
        SetMemory(0x660A70 + 112, SetTo, 0),
        SetMemory(0x660A70 + 116, SetTo, 130),
        SetMemory(0x660A70 + 120, SetTo, 9175179),
        SetMemory(0x660A70 + 124, SetTo, 145),
        SetMemory(0x660A70 + 128, SetTo, 10092694),
        SetMemory(0x660A70 + 132, SetTo, 10551453),
        SetMemory(0x660A70 + 136, SetTo, 10813440),
        SetMemory(0x660A70 + 140, SetTo, 11206824),
        SetMemory(0x660A70 + 144, SetTo, 11731119),
        SetMemory(0x660A70 + 148, SetTo, 0),
        SetMemory(0x660A70 + 152, SetTo, 0),
        SetMemory(0x660A70 + 156, SetTo, 0),
        SetMemory(0x660A70 + 160, SetTo, 0),
        SetMemory(0x660A70 + 164, SetTo, 12189696),
        SetMemory(0x660A70 + 168, SetTo, 12320955),
        SetMemory(0x660A70 + 172, SetTo, 0),
        SetMemory(0x660A70 + 176, SetTo, 0),
        SetMemory(0x660A70 + 180, SetTo, 0),
        SetMemory(0x660A70 + 184, SetTo, 12779520),
        SetMemory(0x660A70 + 188, SetTo, 12910788),
        SetMemory(0x660A70 + 192, SetTo, 198),
        SetMemory(0x660A70 + 196, SetTo, 0),
        SetMemory(0x660A70 + 200, SetTo, 0),
        SetMemory(0x660A70 + 204, SetTo, 13041664),
        SetMemory(0x660A70 + 208, SetTo, 0),
        SetMemory(0x660A70 + 212, SetTo, 13697229),
        SetMemory(0x660A70 + 216, SetTo, 14483671),
        SetMemory(0x660A70 + 220, SetTo, 15007969),
        SetMemory(0x660A70 + 224, SetTo, 15663338),
        SetMemory(0x660A70 + 228, SetTo, 16318708),
        SetMemory(0x660A70 + 232, SetTo, 16974078),
        SetMemory(0x660A70 + 236, SetTo, 264),
        SetMemory(0x660A70 + 240, SetTo, 269),
        SetMemory(0x660A70 + 244, SetTo, 18284818),
        SetMemory(0x660A70 + 248, SetTo, 18940188),
        SetMemory(0x660A70 + 252, SetTo, 0),
        SetMemory(0x660A70 + 256, SetTo, 0),
        SetMemory(0x660A70 + 260, SetTo, 19267584),
        SetMemory(0x660A70 + 264, SetTo, 19857706),
        SetMemory(0x660A70 + 268, SetTo, 20513076),
        SetMemory(0x660A70 + 272, SetTo, 21168446),
        SetMemory(0x660A70 + 276, SetTo, 22020424),
        SetMemory(0x660A70 + 280, SetTo, 23069019),
        SetMemory(0x660A70 + 284, SetTo, 24314216),
        SetMemory(0x660A70 + 288, SetTo, 375),
        SetMemory(0x660A70 + 292, SetTo, 379),
        SetMemory(0x660A70 + 296, SetTo, 25100288),
        SetMemory(0x660A70 + 300, SetTo, 0),
        SetMemory(0x660A70 + 304, SetTo, 0),
        SetMemory(0x660A70 + 308, SetTo, 25493890),
        SetMemory(0x660A70 + 312, SetTo, 25952649),
        SetMemory(0x660A70 + 316, SetTo, 26148864),
        SetMemory(0x660A70 + 320, SetTo, 403),
        SetMemory(0x660A70 + 324, SetTo, 26935703),
        SetMemory(0x660A70 + 328, SetTo, 27459999),
        SetMemory(0x660A70 + 332, SetTo, 27984295),
        SetMemory(0x660A70 + 336, SetTo, 28246016),
        SetMemory(0x660A70 + 340, SetTo, 28836275),
        SetMemory(0x660A70 + 344, SetTo, 444),
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
    

