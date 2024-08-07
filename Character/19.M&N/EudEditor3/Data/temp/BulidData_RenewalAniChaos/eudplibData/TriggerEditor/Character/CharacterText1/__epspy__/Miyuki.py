## NOTE: THIS FILE IS GENERATED BY EPSCRIPT! DO NOT MODITY
from eudplib import *

def _IGVA(vList, exprListGen):
    def _():
        exprList = exprListGen()
        SetVariables(vList, exprList)
    EUDOnStart(_)

def _CGFW(exprf, retn):
    rets = [ExprProxy(None) for _ in range(retn)]
    def _():
        vals = exprf()
        for ret, val in zip(rets, vals):
            ret._value = val
    EUDOnStart(_)
    return rets

def _ARR(items):
    k = EUDArray(len(items))
    for i, item in enumerate(items):
        k[i] = item
    return k

def _VARR(items):
    k = EUDVArray(len(items))()
    for i, item in enumerate(items):
        k[i] = item
    return k

def _SRET(v, klist):
    return List2Assignable([v[k] for k in klist])

def _SV(dL, sL):
    [d << s for d, s in zip(FlattenList(dL), FlattenList(sL))]

class _ATTW:
    def __init__(self, obj, attrName):
        self.obj = obj
        self.attrName = attrName

    def __lshift__(self, r):
        setattr(self.obj, self.attrName, r)

    def __iadd__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov + v)

    def __isub__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov - v)

    def __imul__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov * v)

    def __ifloordiv__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov // v)

    def __iand__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov & v)

    def __ior__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov | v)

    def __ixor__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov ^ v)

class _ARRW:
    def __init__(self, obj, index):
        self.obj = obj
        self.index = index

    def __lshift__(self, r):
        self.obj[self.index] = r

    def __iadd__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov + v

    def __isub__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov - v

    def __imul__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov * v

    def __ifloordiv__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov // v

    def __iand__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov & v

    def __ior__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov | v

    def __ixor__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov ^ v

def _L2V(l):
    ret = EUDVariable()
    if EUDIf()(l):
        ret << 1
    if EUDElse()():
        ret << 0
    EUDEndIf()
    return ret

def _MVAR(vs):
    return List2Assignable([
        v.makeL() if IsEUDVariable(v) else EUDVariable() << v
        for v in FlattenList(vs)])

def _LSH(l, r):
    if IsEUDVariable(l):  return f_bitlshift(l, r)
    else: return l << r

## NOTE: THIS FILE IS GENERATED BY EPSCRIPT! DO NOT MODITY

# (Line 1) import customText as tct;
import customText as tct
# (Line 2) import Variable as v;
import Variable as v
# (Line 4) var txtPtr, btnPtr, btnPos, oldCP;
txtPtr, btnPtr, btnPos, oldCP = EUDCreateVariables(4)
# (Line 6) function NormalText(cp)
# (Line 7) {
@EUDFunc
def NormalText(cp):
    # (Line 8) switch (v.Sound_Text1[cp])
    EUDSwitch(v.Sound_Text1[cp])
    # (Line 9) {
    # (Line 10) case 5000:
    _t1 = EUDSwitchCase()
    # (Line 11) PlayWAV("staredit\\wav\\Miyuki_01.ogg");
    if _t1(5000):
        # (Line 12) v.Sound_Text1[cp] = 0;
        DoActions(PlayWAV("staredit\\wav\\Miyuki_01.ogg"))
        _ARRW(v.Sound_Text1, cp) << (0)
        # (Line 13) tct.print("\n\x13\x1CSone \x04Miyoki\n\x13\x04어디로 도망치는 거야?\n");
        tct.f_print("\n\x13\x1CSone \x04Miyoki\n\x13\x04어디로 도망치는 거야?\n")
        # (Line 14) break;
        EUDBreak()
        # (Line 15) case 5001:
    _t2 = EUDSwitchCase()
    # (Line 16) v.Sound_Text1[cp] = 0;
    if _t2(5001):
        _ARRW(v.Sound_Text1, cp) << (0)
        # (Line 17) tct.print("\n\x13\x1CSone \x04Miyoki\n\x13\x04도망갈 장소라니, 어디에도 없는데\n");
        tct.f_print("\n\x13\x1CSone \x04Miyoki\n\x13\x04도망갈 장소라니, 어디에도 없는데\n")
        # (Line 18) break;
        EUDBreak()
        # (Line 19) case 5300:
    _t3 = EUDSwitchCase()
    # (Line 20) PlayWAV("staredit\\wav\\Miyuki_02.ogg");
    if _t3(5300):
        # (Line 21) v.Sound_Text1[cp] = 0;
        DoActions(PlayWAV("staredit\\wav\\Miyuki_02.ogg"))
        _ARRW(v.Sound_Text1, cp) << (0)
        # (Line 22) tct.print("\n\x13\x1CSone \x04Miyoki\n\x13\x19영원한 사랑\x04을 맹세한 상대에게 배신당하는 \x06고통-\n");
        tct.f_print("\n\x13\x1CSone \x04Miyoki\n\x13\x19영원한 사랑\x04을 맹세한 상대에게 배신당하는 \x06고통-\n")
        # (Line 23) break;
        EUDBreak()
        # (Line 24) case 5301:
    _t4 = EUDSwitchCase()
    # (Line 25) v.Sound_Text1[cp] = 0;
    if _t4(5301):
        _ARRW(v.Sound_Text1, cp) << (0)
        # (Line 26) tct.print("\n\x13\x1CSone \x04Miyoki\n\x13\x04당신도 알게 되었을까?\n");
        tct.f_print("\n\x13\x1CSone \x04Miyoki\n\x13\x04당신도 알게 되었을까?\n")
        # (Line 27) break;
        EUDBreak()
        # (Line 28) case 5400:
    _t5 = EUDSwitchCase()
    # (Line 29) PlayWAV("staredit\\wav\\Miyuki_00.ogg");
    if _t5(5400):
        # (Line 30) v.Sound_Text1[cp] = 0;
        DoActions(PlayWAV("staredit\\wav\\Miyuki_00.ogg"))
        _ARRW(v.Sound_Text1, cp) << (0)
        # (Line 31) tct.print("\n\x13\x1CSone \x04Miyoki\n\x13\x04지금부터, 듬뿍, \x06복수\x04해 주겠어\n");
        tct.f_print("\n\x13\x1CSone \x04Miyoki\n\x13\x04지금부터, 듬뿍, \x06복수\x04해 주겠어\n")
        # (Line 32) break;
        EUDBreak()
        # (Line 33) }
    # (Line 34) }
    EUDEndSwitch()
    # (Line 36) function UiltimateText(cp)

# (Line 37) {
@EUDFunc
def UiltimateText(cp):
    # (Line 38) switch (v.Sound_Text_Uilti[cp])
    EUDSwitch(v.Sound_Text_Uilti[cp])
    # (Line 39) {
    # (Line 40) case 5100:
    _t1 = EUDSwitchCase()
    # (Line 41) PlayWAV("staredit\\wav\\Miyuki_Ultimate.ogg");
    if _t1(5100):
        # (Line 42) v.Sound_Text_Uilti[cp] = 0;
        DoActions(PlayWAV("staredit\\wav\\Miyuki_Ultimate.ogg"))
        _ARRW(v.Sound_Text_Uilti, cp) << (0)
        # (Line 43) txtPtr = dwread_epd(EPD(0x640B58));
        txtPtr << (f_dwread_epd(EPD(0x640B58)))
        # (Line 44) tct.print("\n\n\n\n\x13\x1CSone \x04Miyoki\n\n\x13\x04이것으로, 세계는 업데이트 된다\n\n\n\n");
        tct.f_print("\n\n\n\n\x13\x1CSone \x04Miyoki\n\n\x13\x04이것으로, 세계는 업데이트 된다\n\n\n\n")
        # (Line 45) SetMemory(0x640B58, SetTo, txtPtr);
        # (Line 46) break;
        DoActions(SetMemory(0x640B58, SetTo, txtPtr))
        EUDBreak()
        # (Line 47) case 5101:
    _t2 = EUDSwitchCase()
    # (Line 48) v.Sound_Text_Uilti[cp] = 0;
    if _t2(5101):
        _ARRW(v.Sound_Text_Uilti, cp) << (0)
        # (Line 49) txtPtr = dwread_epd(EPD(0x640B58));
        txtPtr << (f_dwread_epd(EPD(0x640B58)))
        # (Line 50) tct.print("\n\n\n\n\x13\x1CSone \x04Miyoki\n\n\x13\x04당신은 허구의 존재가 되는거야\n\n\n\n");
        tct.f_print("\n\n\n\n\x13\x1CSone \x04Miyoki\n\n\x13\x04당신은 허구의 존재가 되는거야\n\n\n\n")
        # (Line 51) SetMemory(0x640B58, SetTo, txtPtr);
        # (Line 52) break;
        DoActions(SetMemory(0x640B58, SetTo, txtPtr))
        EUDBreak()
        # (Line 53) case 5200:
    _t3 = EUDSwitchCase()
    # (Line 54) PlayWAV("staredit\\wav\\Miyuki_Ultimate2.ogg");
    if _t3(5200):
        # (Line 55) v.Sound_Text_Uilti[cp] = 0;
        DoActions(PlayWAV("staredit\\wav\\Miyuki_Ultimate2.ogg"))
        _ARRW(v.Sound_Text_Uilti, cp) << (0)
        # (Line 56) txtPtr = dwread_epd(EPD(0x640B58));
        txtPtr << (f_dwread_epd(EPD(0x640B58)))
        # (Line 57) tct.print("\n\n\n\n\x13\x1CSone \x04Miyoki\n\n\x13\x06미안해, \x04그렇지만 ――\n\n\n\n");
        tct.f_print("\n\n\n\n\x13\x1CSone \x04Miyoki\n\n\x13\x06미안해, \x04그렇지만 ――\n\n\n\n")
        # (Line 58) SetMemory(0x640B58, SetTo, txtPtr);
        # (Line 59) break;
        DoActions(SetMemory(0x640B58, SetTo, txtPtr))
        EUDBreak()
        # (Line 60) case 5201:
    _t4 = EUDSwitchCase()
    # (Line 61) v.Sound_Text_Uilti[cp] = 0;
    if _t4(5201):
        _ARRW(v.Sound_Text_Uilti, cp) << (0)
        # (Line 62) txtPtr = dwread_epd(EPD(0x640B58));
        txtPtr << (f_dwread_epd(EPD(0x640B58)))
        # (Line 63) tct.print("\n\n\n\n\x13\x1CSone \x04Miyoki\n\n\x13\x06이제, 이것 밖에, 방법이 없는거야...\n\n\n\n");
        tct.f_print("\n\n\n\n\x13\x1CSone \x04Miyoki\n\n\x13\x06이제, 이것 밖에, 방법이 없는거야...\n\n\n\n")
        # (Line 64) SetMemory(0x640B58, SetTo, txtPtr);
        # (Line 65) break;
        DoActions(SetMemory(0x640B58, SetTo, txtPtr))
        EUDBreak()
        # (Line 66) }
    # (Line 67) }
    EUDEndSwitch()
    # (Line 69) function UniqueText(cp)

# (Line 70) {
@EUDFunc
def UniqueText(cp):
    # (Line 71) switch (v.Sound_Text_Uniq[cp])
    EUDSwitch(v.Sound_Text_Uniq[cp])
    # (Line 72) {
    # (Line 73) case 5000:
    _t1 = EUDSwitchCase()
    # (Line 74) PlayWAV("Miyuki_Unique01.ogg");
    if _t1(5000):
        # (Line 75) v.Sound_Text_Uniq[cp] = 0;
        DoActions(PlayWAV("Miyuki_Unique01.ogg"))
        _ARRW(v.Sound_Text_Uniq, cp) << (0)
        # (Line 76) tct.print("\n\n\x13\x1CSone \x04Miyoki\n\x13\x04나를... \x06속였었네,\n\n");
        tct.f_print("\n\n\x13\x1CSone \x04Miyoki\n\x13\x04나를... \x06속였었네,\n\n")
        # (Line 77) break;
        EUDBreak()
        # (Line 78) case 5001:
    _t2 = EUDSwitchCase()
    # (Line 79) PlayWAV("Miyuki_Unique02.ogg");
    if _t2(5001):
        # (Line 80) v.Sound_Text_Uniq[cp] = 0;
        DoActions(PlayWAV("Miyuki_Unique02.ogg"))
        _ARRW(v.Sound_Text_Uniq, cp) << (0)
        # (Line 81) tct.print("\n\n\x13\x1CSone \x04Miyoki\n\x13\x04속였으니 \x06벌\x04을 주지 않으면 안되겠네.\n\n");
        tct.f_print("\n\n\x13\x1CSone \x04Miyoki\n\x13\x04속였으니 \x06벌\x04을 주지 않으면 안되겠네.\n\n")
        # (Line 82) break;
        EUDBreak()
        # (Line 83) }
    # (Line 84) }
    EUDEndSwitch()
