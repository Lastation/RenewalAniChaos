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
    # (Line 10) case 3110:
    _t1 = EUDSwitchCase()
    # (Line 11) PlayWAV("HotoMoka_01.ogg");
    if _t1(3110):
        # (Line 12) v.Sound_Text2[cp] = 0;
        DoActions(PlayWAV("HotoMoka_01.ogg"))
        _ARRW(v.Sound_Text2, cp) << (0)
        # (Line 13) tct.print("\n\n\x13\x1BHoto Moka\n\x13\x04어서오세욧~\n\n");
        tct.f_print("\n\n\x13\x1BHoto Moka\n\x13\x04어서오세욧~\n\n")
        # (Line 14) break;
        EUDBreak()
        # (Line 15) case 3210:
    _t2 = EUDSwitchCase()
    # (Line 16) PlayWAV("HotoMoka_02.ogg");
    if _t2(3210):
        # (Line 17) v.Sound_Text2[cp] = 0;
        DoActions(PlayWAV("HotoMoka_02.ogg"))
        _ARRW(v.Sound_Text2, cp) << (0)
        # (Line 18) tct.print("\n\n\x13\x1BHoto Moka\n\x13\x04코코아가 젤 첨에 되고 싶었던거 기억나?\n\n");
        tct.f_print("\n\n\x13\x1BHoto Moka\n\x13\x04코코아가 젤 첨에 되고 싶었던거 기억나?\n\n")
        # (Line 19) break;
        EUDBreak()
        # (Line 20) case 3220:
    _t3 = EUDSwitchCase()
    # (Line 21) PlayWAV("HotoMoka_03.ogg");
    if _t3(3220):
        # (Line 22) v.Sound_Text2[cp] = 0;
        DoActions(PlayWAV("HotoMoka_03.ogg"))
        _ARRW(v.Sound_Text2, cp) << (0)
        # (Line 23) break;
        EUDBreak()
        # (Line 24) case 3221:
    _t4 = EUDSwitchCase()
    # (Line 25) v.Sound_Text2[cp] = 0;
    if _t4(3221):
        _ARRW(v.Sound_Text2, cp) << (0)
        # (Line 26) tct.print("\n\n\x13\x1BHoto Moka\n\x13\x04마법사!\n\n");
        tct.f_print("\n\n\x13\x1BHoto Moka\n\x13\x04마법사!\n\n")
        # (Line 27) break;
        EUDBreak()
        # (Line 28) }
    # (Line 29) }
    EUDEndSwitch()
    # (Line 31) function UiltimateText(cp)

# (Line 32) {
@EUDFunc
def UiltimateText(cp):
    # (Line 33) switch (v.Sound_Text_Uilti[cp])
    EUDSwitch(v.Sound_Text_Uilti[cp])
    # (Line 34) {
    # (Line 35) case 9000:
    _t1 = EUDSwitchCase()
    # (Line 36) PlayWAV("HotoMoka_Uiltimate.ogg");
    if _t1(9000):
        # (Line 37) v.Sound_Text_Uilti[cp] = 0;
        DoActions(PlayWAV("HotoMoka_Uiltimate.ogg"))
        _ARRW(v.Sound_Text_Uilti, cp) << (0)
        # (Line 38) tct.print("\n\n\x13\x1BHoto Moka\n\n\x13\x04나, 준비해올게\n\n");
        tct.f_print("\n\n\x13\x1BHoto Moka\n\n\x13\x04나, 준비해올게\n\n")
        # (Line 39) break;
        EUDBreak()
        # (Line 40) case 9001:
    _t2 = EUDSwitchCase()
    # (Line 41) v.Sound_Text_Uilti[cp] = 0;
    if _t2(9001):
        _ARRW(v.Sound_Text_Uilti, cp) << (0)
        # (Line 42) tct.print("\n\n\x13\x1BHoto Moka\n\n\x13\x04좋아, 준비 완료!\n\n");
        tct.f_print("\n\n\x13\x1BHoto Moka\n\n\x13\x04좋아, 준비 완료!\n\n")
        # (Line 43) break;
        EUDBreak()
        # (Line 44) }
    # (Line 45) }
    EUDEndSwitch()
    # (Line 47) function UniqueText(cp)

# (Line 48) {
@EUDFunc
def UniqueText(cp):
    # (Line 49) switch (v.Sound_Text_Uniq[cp])
    EUDSwitch(v.Sound_Text_Uniq[cp])
    # (Line 50) {
    # (Line 51) case 9000:
    _t1 = EUDSwitchCase()
    # (Line 52) PlayWAV("HotoMoka_00.ogg");
    if _t1(9000):
        # (Line 53) v.Sound_Text_Uniq[cp] = 0;
        DoActions(PlayWAV("HotoMoka_00.ogg"))
        _ARRW(v.Sound_Text_Uniq, cp) << (0)
        # (Line 54) txtPtr = dwread_epd(EPD(0x640B58));
        txtPtr << (f_dwread_epd(EPD(0x640B58)))
        # (Line 55) tct.print("\n\n\x13\x1BHoto Moka\n\n\x13\x04이 앞에는 전파가 닿지 않으니까\n\x13\x04핸드폰은 쓰지 못한단다?\n\n");
        tct.f_print("\n\n\x13\x1BHoto Moka\n\n\x13\x04이 앞에는 전파가 닿지 않으니까\n\x13\x04핸드폰은 쓰지 못한단다?\n\n")
        # (Line 56) SetMemory(0x640B58, SetTo, txtPtr);
        # (Line 57) break;
        DoActions(SetMemory(0x640B58, SetTo, txtPtr))
        EUDBreak()
        # (Line 58) }
    # (Line 59) }
    EUDEndSwitch()
