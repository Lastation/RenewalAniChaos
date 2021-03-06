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
    # (Line 8) switch (v.Sound_Text2[cp])
    EUDSwitch(v.Sound_Text2[cp])
    # (Line 9) {
    # (Line 10) case 2000:
    _t1 = EUDSwitchCase()
    # (Line 11) PlayWAV("Anzu_01.ogg");
    if _t1(2000):
        # (Line 12) v.Sound_Text2[cp] = 0;
        DoActions(PlayWAV("Anzu_01.ogg"))
        _ARRW(v.Sound_Text2, cp) << (0)
        # (Line 13) tct.print("\n\x13\x1BFutaba Anzu\n\x13\x04엣헴!\x04\n");
        tct.f_print("\n\x13\x1BFutaba Anzu\n\x13\x04엣헴!\x04\n")
        # (Line 14) break;
        EUDBreak()
        # (Line 15) case 2010:
    _t2 = EUDSwitchCase()
    # (Line 16) PlayWAV("Anzu_02.ogg");
    if _t2(2010):
        # (Line 17) v.Sound_Text2[cp] = 0;
        DoActions(PlayWAV("Anzu_02.ogg"))
        _ARRW(v.Sound_Text2, cp) << (0)
        # (Line 18) tct.print("\n\x13\x1BFutaba Anzu\n\x13\x04지지 않으려면 ··· \x17이것 \x04밖에 없어!\n");
        tct.f_print("\n\x13\x1BFutaba Anzu\n\x13\x04지지 않으려면 ··· \x17이것 \x04밖에 없어!\n")
        # (Line 19) break;
        EUDBreak()
        # (Line 20) case 2011:
    _t3 = EUDSwitchCase()
    # (Line 21) PlayWAV("Anzu_03.ogg");
    if _t3(2011):
        # (Line 22) v.Sound_Text2[cp] = 0;
        DoActions(PlayWAV("Anzu_03.ogg"))
        _ARRW(v.Sound_Text2, cp) << (0)
        # (Line 23) tct.print("\n\x13\x1BFutaba Anzu\n\x13\x04우리의 \x17정의\x04를 위해 ―――――――!!\n");
        tct.f_print("\n\x13\x1BFutaba Anzu\n\x13\x04우리의 \x17정의\x04를 위해 ―――――――!!\n")
        # (Line 24) break;
        EUDBreak()
        # (Line 25) }
    # (Line 26) }
    EUDEndSwitch()
    # (Line 28) function UiltimateText(cp)

# (Line 29) {
@EUDFunc
def UiltimateText(cp):
    # (Line 30) switch (v.Sound_Text_Uilti[cp])
    EUDSwitch(v.Sound_Text_Uilti[cp])
    # (Line 31) {
    # (Line 32) case 8000:
    _t1 = EUDSwitchCase()
    # (Line 33) PlayWAV("Anzu_Uiltimate.ogg");
    if _t1(8000):
        # (Line 34) v.Sound_Text_Uilti[cp] = 0;
        DoActions(PlayWAV("Anzu_Uiltimate.ogg"))
        _ARRW(v.Sound_Text_Uilti, cp) << (0)
        # (Line 35) txtPtr = dwread_epd(EPD(0x640B58));
        txtPtr << (f_dwread_epd(EPD(0x640B58)))
        # (Line 36) tct.print("\n\n\n\x13\x1BFutaba Anzu\n\x13\x17「 \x04일하지 않는 \x17모든 자\x04들에게 전한다 \x17」\n\n\n");
        tct.f_print("\n\n\n\x13\x1BFutaba Anzu\n\x13\x17「 \x04일하지 않는 \x17모든 자\x04들에게 전한다 \x17」\n\n\n")
        # (Line 37) SetMemory(0x640B58, SetTo, txtPtr);
        # (Line 38) break;
        DoActions(SetMemory(0x640B58, SetTo, txtPtr))
        EUDBreak()
        # (Line 39) case 8001:
    _t2 = EUDSwitchCase()
    # (Line 40) v.Sound_Text_Uilti[cp] = 0;
    if _t2(8001):
        _ARRW(v.Sound_Text_Uilti, cp) << (0)
        # (Line 41) txtPtr = dwread_epd(EPD(0x640B58));
        txtPtr << (f_dwread_epd(EPD(0x640B58)))
        # (Line 42) tct.print("\n\n\n\x13\x1BFutaba Anzu\n\x13\x17「 \x04이것은 \x17놀이\x04도 \x17라이브\x04도 아니야! \x17」\n\n\n");
        tct.f_print("\n\n\n\x13\x1BFutaba Anzu\n\x13\x17「 \x04이것은 \x17놀이\x04도 \x17라이브\x04도 아니야! \x17」\n\n\n")
        # (Line 43) SetMemory(0x640B58, SetTo, txtPtr);
        # (Line 44) break;
        DoActions(SetMemory(0x640B58, SetTo, txtPtr))
        EUDBreak()
        # (Line 45) case 8002:
    _t3 = EUDSwitchCase()
    # (Line 46) v.Sound_Text_Uilti[cp] = 0;
    if _t3(8002):
        _ARRW(v.Sound_Text_Uilti, cp) << (0)
        # (Line 47) txtPtr = dwread_epd(EPD(0x640B58));
        txtPtr << (f_dwread_epd(EPD(0x640B58)))
        # (Line 48) tct.print("\n\n\n\x13\x1BFutaba Anzu\n\x13\x17「 \x04우리의 \x17정의\x04를 위하여―――――――――!! \x17」\n\n\n");
        tct.f_print("\n\n\n\x13\x1BFutaba Anzu\n\x13\x17「 \x04우리의 \x17정의\x04를 위하여―――――――――!! \x17」\n\n\n")
        # (Line 49) SetMemory(0x640B58, SetTo, txtPtr);
        # (Line 50) break;
        DoActions(SetMemory(0x640B58, SetTo, txtPtr))
        EUDBreak()
        # (Line 51) case 8100:
    _t4 = EUDSwitchCase()
    # (Line 52) PlayWAV("Anzu_01.ogg");
    if _t4(8100):
        # (Line 53) v.Sound_Text_Uilti[cp] = 0;
        DoActions(PlayWAV("Anzu_01.ogg"))
        _ARRW(v.Sound_Text_Uilti, cp) << (0)
        # (Line 54) txtPtr = dwread_epd(EPD(0x640B58));
        txtPtr << (f_dwread_epd(EPD(0x640B58)))
        # (Line 55) tct.print("\n\n\n\x13\x1BFutaba Anzu\n\x13\x17「 \x04엣헴! \x17」\n\n\n");
        tct.f_print("\n\n\n\x13\x1BFutaba Anzu\n\x13\x17「 \x04엣헴! \x17」\n\n\n")
        # (Line 56) SetMemory(0x640B58, SetTo, txtPtr);
        # (Line 57) break;
        DoActions(SetMemory(0x640B58, SetTo, txtPtr))
        EUDBreak()
        # (Line 58) case 8101:
    _t5 = EUDSwitchCase()
    # (Line 59) PlayWAV("Anzu_Uiltimate2.ogg");
    if _t5(8101):
        # (Line 60) v.Sound_Text_Uilti[cp] = 0;
        DoActions(PlayWAV("Anzu_Uiltimate2.ogg"))
        _ARRW(v.Sound_Text_Uilti, cp) << (0)
        # (Line 61) break;
        EUDBreak()
        # (Line 62) case 8102:
    _t6 = EUDSwitchCase()
    # (Line 63) v.Sound_Text_Uilti[cp] = 0;
    if _t6(8102):
        _ARRW(v.Sound_Text_Uilti, cp) << (0)
        # (Line 64) txtPtr = dwread_epd(EPD(0x640B58));
        txtPtr << (f_dwread_epd(EPD(0x640B58)))
        # (Line 65) tct.print("\n\n\n\x13\x1BFutaba Anzu\n\x13\x17「 \x04˙˙˙ 라는 \x17꿈\x04을 꿨어 \x17」\n\n\n");
        tct.f_print("\n\n\n\x13\x1BFutaba Anzu\n\x13\x17「 \x04˙˙˙ 라는 \x17꿈\x04을 꿨어 \x17」\n\n\n")
        # (Line 66) SetMemory(0x640B58, SetTo, txtPtr);
        # (Line 67) break;
        DoActions(SetMemory(0x640B58, SetTo, txtPtr))
        EUDBreak()
        # (Line 68) }
    # (Line 69) }
    EUDEndSwitch()
    # (Line 71) function UniqueText(cp)

# (Line 72) {
@EUDFunc
def UniqueText(cp):
    # (Line 73) switch (v.Sound_Text_Uniq[cp])
    EUDSwitch(v.Sound_Text_Uniq[cp])
    # (Line 74) {
    # (Line 75) case 8000:
    _t1 = EUDSwitchCase()
    # (Line 76) PlayWAV("Anzu_Unique.ogg");
    if _t1(8000):
        # (Line 77) v.Sound_Text_Uniq[cp] = 0;
        DoActions(PlayWAV("Anzu_Unique.ogg"))
        _ARRW(v.Sound_Text_Uniq, cp) << (0)
        # (Line 78) txtPtr = dwread_epd(EPD(0x640B58));
        txtPtr << (f_dwread_epd(EPD(0x640B58)))
        # (Line 79) tct.print("\n\n\n\x13\x1BFutaba Anzu\n\x13\x04「　시..싫어, 나는 \x17일\x04하지 않을꺼얏 !!　\x04」\n\n\n");
        tct.f_print("\n\n\n\x13\x1BFutaba Anzu\n\x13\x04「　시..싫어, 나는 \x17일\x04하지 않을꺼얏 !!　\x04」\n\n\n")
        # (Line 80) SetMemory(0x640B58, SetTo, txtPtr);
        # (Line 81) break;
        DoActions(SetMemory(0x640B58, SetTo, txtPtr))
        EUDBreak()
        # (Line 82) }
    # (Line 83) }
    EUDEndSwitch()
