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
    # (Line 8) switch (v.Sound_Text3[cp])
    EUDSwitch(v.Sound_Text3[cp])
    # (Line 9) {
    # (Line 10) case 6000:
    _t1 = EUDSwitchCase()
    # (Line 11) tct.print("\n\n\x13\x02Iwahune Tenkei\n\x13\x04하항, 풋내나는구만 정말이지\n\n");
    if _t1(6000):
        tct.f_print("\n\n\x13\x02Iwahune Tenkei\n\x13\x04하항, 풋내나는구만 정말이지\n\n")
        # (Line 12) PlayWAV("iwa_sss.ogg");
        # (Line 13) v.Sound_Text3[cp] = 0;
        DoActions(PlayWAV("iwa_sss.ogg"))
        _ARRW(v.Sound_Text3, cp) << (0)
        # (Line 14) break;
        EUDBreak()
        # (Line 15) case 6001:
    _t2 = EUDSwitchCase()
    # (Line 16) tct.print("\n\n\x13\x02Iwahune Tenkei\n\x13\x04이상의 세계라는 것을 자신의 힘으로 만들 수 있다고 믿는 건\n\n");
    if _t2(6001):
        tct.f_print("\n\n\x13\x02Iwahune Tenkei\n\x13\x04이상의 세계라는 것을 자신의 힘으로 만들 수 있다고 믿는 건\n\n")
        # (Line 17) PlayWAV("iwa_sssccc.ogg");
        # (Line 18) v.Sound_Text3[cp] = 0;
        DoActions(PlayWAV("iwa_sssccc.ogg"))
        _ARRW(v.Sound_Text3, cp) << (0)
        # (Line 19) break;
        EUDBreak()
        # (Line 20) case 6002:
    _t3 = EUDSwitchCase()
    # (Line 21) tct.print("\n\n\x13\x02Iwahune Tenkei\n\x13\x04무나카타, 네가 아직 좌절을 맛본 적 없는 풋내기라서야\n\n");
    if _t3(6002):
        tct.f_print("\n\n\x13\x02Iwahune Tenkei\n\x13\x04무나카타, 네가 아직 좌절을 맛본 적 없는 풋내기라서야\n\n")
        # (Line 22) v.Sound_Text3[cp] = 0;
        _ARRW(v.Sound_Text3, cp) << (0)
        # (Line 23) break;
        EUDBreak()
        # (Line 24) case 6003:
    _t4 = EUDSwitchCase()
    # (Line 25) tct.print("\n\n\x13\x02Iwahune Tenkei\n\x13\x04어이어이, 어딜 노리는 거냐~?\n\n");
    if _t4(6003):
        tct.f_print("\n\n\x13\x02Iwahune Tenkei\n\x13\x04어이어이, 어딜 노리는 거냐~?\n\n")
        # (Line 26) PlayWAV("iwa_aac.ogg");
        # (Line 27) v.Sound_Text3[cp] = 0;
        DoActions(PlayWAV("iwa_aac.ogg"))
        _ARRW(v.Sound_Text3, cp) << (0)
        # (Line 28) break;
        EUDBreak()
        # (Line 29) }
    # (Line 30) }
    EUDEndSwitch()
    # (Line 32) function UiltimateText(cp)

# (Line 33) {
@EUDFunc
def UiltimateText(cp):
    # (Line 34) switch (v.Sound_Text_Uilti[cp])
    EUDSwitch(v.Sound_Text_Uilti[cp])
    # (Line 35) {
    # (Line 36) case 18000:
    _t1 = EUDSwitchCase()
    # (Line 37) tct.print("\n\n\x13\x02Iwahune Tenkei\n\x13\x04약해진 상대한테 전력을 쏟는 것도 쪽팔리지만,\n\n");
    if _t1(18000):
        tct.f_print("\n\n\x13\x02Iwahune Tenkei\n\x13\x04약해진 상대한테 전력을 쏟는 것도 쪽팔리지만,\n\n")
        # (Line 38) PlayWAV("iwa_aaa.ogg");
        # (Line 39) v.Sound_Text_Uilti[cp] = 0;
        DoActions(PlayWAV("iwa_aaa.ogg"))
        _ARRW(v.Sound_Text_Uilti, cp) << (0)
        # (Line 40) break;
        EUDBreak()
        # (Line 41) case 18001:
    _t2 = EUDSwitchCase()
    # (Line 42) tct.print("\n\n\x13\x02Iwahune Tenkei\n\x13\x04이쪽도 슬슬 물러날 때다!\n\n");
    if _t2(18001):
        tct.f_print("\n\n\x13\x02Iwahune Tenkei\n\x13\x04이쪽도 슬슬 물러날 때다!\n\n")
        # (Line 43) v.Sound_Text_Uilti[cp] = 0;
        _ARRW(v.Sound_Text_Uilti, cp) << (0)
        # (Line 44) break;
        EUDBreak()
        # (Line 45) }
    # (Line 46) }
    EUDEndSwitch()
    # (Line 48) function UniqueText(cp)

# (Line 49) {
@EUDFunc
def UniqueText(cp):
    # (Line 50) switch (v.Sound_Text_Uniq[cp])
    EUDSwitch(v.Sound_Text_Uniq[cp])
    # (Line 51) {
    # (Line 52) case 18000:
    _t1 = EUDSwitchCase()
    # (Line 53) tct.print("\n\n\x13\x02Iwahune Tenkei\n\x13\x04아, 잠깐만\n\n");
    if _t1(18000):
        tct.f_print("\n\n\x13\x02Iwahune Tenkei\n\x13\x04아, 잠깐만\n\n")
        # (Line 54) PlayWAV("iwa_o.ogg");
        # (Line 55) v.Sound_Text_Uniq[cp] = 0;
        DoActions(PlayWAV("iwa_o.ogg"))
        _ARRW(v.Sound_Text_Uniq, cp) << (0)
        # (Line 56) break;
        EUDBreak()
        # (Line 57) case 18001:
    _t2 = EUDSwitchCase()
    # (Line 58) tct.print("\n\n\x13\x02Iwahune Tenkei\n\x13\x04너무 죽기 살기로 덤비지 마, 풋내기\n\n");
    if _t2(18001):
        tct.f_print("\n\n\x13\x02Iwahune Tenkei\n\x13\x04너무 죽기 살기로 덤비지 마, 풋내기\n\n")
        # (Line 59) v.Sound_Text_Uniq[cp] = 0;
        _ARRW(v.Sound_Text_Uniq, cp) << (0)
        # (Line 60) break;
        EUDBreak()
        # (Line 61) }
    # (Line 62) }
    EUDEndSwitch()