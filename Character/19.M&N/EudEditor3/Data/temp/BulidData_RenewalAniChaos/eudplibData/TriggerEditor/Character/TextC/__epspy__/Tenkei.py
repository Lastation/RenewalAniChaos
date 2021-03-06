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

# (Line 1) import Variable as v;
import Variable as v
# (Line 3) const s = StringBuffer();
s = _CGFW(lambda: [StringBuffer()], 1)[0]
# (Line 5) function NormalText(cp)
# (Line 6) {
@EUDFunc
def NormalText(cp):
    # (Line 7) switch (v.Sound_Text3[cp])
    EUDSwitch(v.Sound_Text3[cp])
    # (Line 8) {
    # (Line 9) case 6000:
    _t1 = EUDSwitchCase()
    # (Line 10) s.print("\n\n\x13\x02Iwahune Tenkei\n\x13\x04하항, 풋내나는구만 정말이지\n\n");
    if _t1(6000):
        s.print("\n\n\x13\x02Iwahune Tenkei\n\x13\x04하항, 풋내나는구만 정말이지\n\n")
        # (Line 11) PlayWAV("iwa_sss.ogg");
        # (Line 12) v.Sound_Text3[cp] = 0;
        DoActions(PlayWAV("iwa_sss.ogg"))
        _ARRW(v.Sound_Text3, cp) << (0)
        # (Line 13) break;
        EUDBreak()
        # (Line 14) case 6001:
    _t2 = EUDSwitchCase()
    # (Line 15) s.print("\n\n\x13\x02Iwahune Tenkei\n\x13\x04이상의 세계라는 것을 자신의 힘으로 만들 수 있다고 믿는 건\n\n");
    if _t2(6001):
        s.print("\n\n\x13\x02Iwahune Tenkei\n\x13\x04이상의 세계라는 것을 자신의 힘으로 만들 수 있다고 믿는 건\n\n")
        # (Line 16) PlayWAV("iwa_sssccc.ogg");
        # (Line 17) v.Sound_Text3[cp] = 0;
        DoActions(PlayWAV("iwa_sssccc.ogg"))
        _ARRW(v.Sound_Text3, cp) << (0)
        # (Line 18) break;
        EUDBreak()
        # (Line 19) case 6002:
    _t3 = EUDSwitchCase()
    # (Line 20) s.print("\n\n\x13\x02Iwahune Tenkei\n\x13\x04무나카타, 네가 아직 좌절을 맛본 적 없는 풋내기라서야\n\n");
    if _t3(6002):
        s.print("\n\n\x13\x02Iwahune Tenkei\n\x13\x04무나카타, 네가 아직 좌절을 맛본 적 없는 풋내기라서야\n\n")
        # (Line 21) v.Sound_Text3[cp] = 0;
        _ARRW(v.Sound_Text3, cp) << (0)
        # (Line 22) break;
        EUDBreak()
        # (Line 23) case 6003:
    _t4 = EUDSwitchCase()
    # (Line 24) s.print("\n\n\x13\x02Iwahune Tenkei\n\x13\x04어이어이, 어딜 노리는 거냐~?\n\n");
    if _t4(6003):
        s.print("\n\n\x13\x02Iwahune Tenkei\n\x13\x04어이어이, 어딜 노리는 거냐~?\n\n")
        # (Line 25) PlayWAV("iwa_aac.ogg");
        # (Line 26) v.Sound_Text3[cp] = 0;
        DoActions(PlayWAV("iwa_aac.ogg"))
        _ARRW(v.Sound_Text3, cp) << (0)
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
    # (Line 35) case 18000:
    _t1 = EUDSwitchCase()
    # (Line 36) s.printAt(3,"\x13\x02Iwahune Tenkei\n\x13\x04약해진 상대한테 전력을 쏟는 것도 쪽팔리지만,");
    if _t1(18000):
        s.printAt(3, "\x13\x02Iwahune Tenkei\n\x13\x04약해진 상대한테 전력을 쏟는 것도 쪽팔리지만,")
        # (Line 37) PlayWAV("iwa_aaa.ogg");
        # (Line 38) v.Sound_Text_Uilti[cp] = 0;
        DoActions(PlayWAV("iwa_aaa.ogg"))
        _ARRW(v.Sound_Text_Uilti, cp) << (0)
        # (Line 39) break;
        EUDBreak()
        # (Line 40) case 18001:
    _t2 = EUDSwitchCase()
    # (Line 41) s.printAt(3,"\x13\x02Iwahune Tenkei\n\x13\x04이쪽도 슬슬 물러날 때다!");
    if _t2(18001):
        s.printAt(3, "\x13\x02Iwahune Tenkei\n\x13\x04이쪽도 슬슬 물러날 때다!")
        # (Line 42) v.Sound_Text_Uilti[cp] = 0;
        _ARRW(v.Sound_Text_Uilti, cp) << (0)
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
    # (Line 51) case 18000:
    _t1 = EUDSwitchCase()
    # (Line 52) s.print("\n\n\x13\x02Iwahune Tenkei\n\x13\x04아, 잠깐만\n\n");
    if _t1(18000):
        s.print("\n\n\x13\x02Iwahune Tenkei\n\x13\x04아, 잠깐만\n\n")
        # (Line 53) PlayWAV("iwa_o.ogg");
        # (Line 54) v.Sound_Text_Uniq[cp] = 0;
        DoActions(PlayWAV("iwa_o.ogg"))
        _ARRW(v.Sound_Text_Uniq, cp) << (0)
        # (Line 55) break;
        EUDBreak()
        # (Line 56) case 18001:
    _t2 = EUDSwitchCase()
    # (Line 57) s.print("\n\n\x13\x02Iwahune Tenkei\n\x13\x04너무 죽기 살기로 덤비지 마, 풋내기\n\n");
    if _t2(18001):
        s.print("\n\n\x13\x02Iwahune Tenkei\n\x13\x04너무 죽기 살기로 덤비지 마, 풋내기\n\n")
        # (Line 58) v.Sound_Text_Uniq[cp] = 0;
        _ARRW(v.Sound_Text_Uniq, cp) << (0)
        # (Line 59) break;
        EUDBreak()
        # (Line 60) }
    # (Line 61) }
    EUDEndSwitch()
