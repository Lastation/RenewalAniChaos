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

# (Line 1) import PluginVariables as msqcvar;
import PluginVariables as msqcvar
# (Line 2) import Variable as v;
import Variable as v
# (Line 3) import Function as f;
import Function as f
# (Line 5) function NormalText(cp)
# (Line 6) {
@EUDFunc
def NormalText(cp):
    # (Line 7) switch (v.Sound_Text1[cp])
    EUDSwitch(v.Sound_Text1[cp])
    # (Line 8) {
    # (Line 9) case 3000:
    _t1 = EUDSwitchCase()
    # (Line 10) PlayWAV("staredit\\wav\\Hime_1.ogg");
    if _t1(3000):
        # (Line 11) f.stb.print("\n\x13\x04Tenkawa \x07MaiHime\n\x13\x04있잖아, 힘에는 책임이 따르고 파워에는 책임이 따른다구?\n");
        DoActions(PlayWAV("staredit\\wav\\Hime_1.ogg"))
        f.stb.print("\n\x13\x04Tenkawa \x07MaiHime\n\x13\x04있잖아, 힘에는 책임이 따르고 파워에는 책임이 따른다구?\n")
        # (Line 12) v.Sound_Text1[cp] = 0;
        _ARRW(v.Sound_Text1, cp) << (0)
        # (Line 13) break;
        EUDBreak()
        # (Line 14) case 3001:
    _t2 = EUDSwitchCase()
    # (Line 15) PlayWAV("staredit\\wav\\Hime_2.ogg");
    if _t2(3001):
        # (Line 16) f.stb.print("\n\x13\x04Tenkawa \x07MaiHime\n\x13\x04즉 힘이야말로 책임이며 책임이야말로 파워!\n");
        DoActions(PlayWAV("staredit\\wav\\Hime_2.ogg"))
        f.stb.print("\n\x13\x04Tenkawa \x07MaiHime\n\x13\x04즉 힘이야말로 책임이며 책임이야말로 파워!\n")
        # (Line 17) v.Sound_Text1[cp] = 0;
        _ARRW(v.Sound_Text1, cp) << (0)
        # (Line 18) break;
        EUDBreak()
        # (Line 19) case 3002:
    _t3 = EUDSwitchCase()
    # (Line 20) f.stb.print("\n\x13\x04Tenkawa \x07MaiHime\n\x13\x04따라서 힘이야말로 파워!\n");
    if _t3(3002):
        f.stb.print("\n\x13\x04Tenkawa \x07MaiHime\n\x13\x04따라서 힘이야말로 파워!\n")
        # (Line 21) v.Sound_Text1[cp] = 0;
        _ARRW(v.Sound_Text1, cp) << (0)
        # (Line 22) break;
        EUDBreak()
        # (Line 23) case 3100:
    _t4 = EUDSwitchCase()
    # (Line 24) PlayWAV("staredit\\wav\\Hime_3.ogg");
    if _t4(3100):
        # (Line 25) f.stb.print("\n\x13\x04Tenkawa \x07MaiHime\n\x13\x04여기는 나의 영역이다\n");
        DoActions(PlayWAV("staredit\\wav\\Hime_3.ogg"))
        f.stb.print("\n\x13\x04Tenkawa \x07MaiHime\n\x13\x04여기는 나의 영역이다\n")
        # (Line 26) v.Sound_Text1[cp] = 0;
        _ARRW(v.Sound_Text1, cp) << (0)
        # (Line 27) break;
        EUDBreak()
        # (Line 28) case 3101:
    _t5 = EUDSwitchCase()
    # (Line 29) f.stb.print("\n\x13\x04Tenkawa \x07MaiHime\n\n\x13\x04내 \x07세계\x04에\n\x13\x04네놈들이 들어올 자리는 없어!!!\n");
    if _t5(3101):
        f.stb.print("\n\x13\x04Tenkawa \x07MaiHime\n\n\x13\x04내 \x07세계\x04에\n\x13\x04네놈들이 들어올 자리는 없어!!!\n")
        # (Line 30) v.Sound_Text1[cp] = 0;
        _ARRW(v.Sound_Text1, cp) << (0)
        # (Line 31) break;
        EUDBreak()
        # (Line 32) case 3300:
    _t6 = EUDSwitchCase()
    # (Line 33) PlayWAV("staredit\\wav\\Hime_0.ogg");
    if _t6(3300):
        # (Line 34) f.stb.print("\n\x13\x04Tenkawa \x07MaiHime\n\x13\x04강하닷―――!!\n");
        DoActions(PlayWAV("staredit\\wav\\Hime_0.ogg"))
        f.stb.print("\n\x13\x04Tenkawa \x07MaiHime\n\x13\x04강하닷―――!!\n")
        # (Line 35) v.Sound_Text1[cp] = 0;
        _ARRW(v.Sound_Text1, cp) << (0)
        # (Line 36) break;
        EUDBreak()
        # (Line 37) }
    # (Line 38) }
    EUDEndSwitch()
    # (Line 40) function UiltimateText(cp)

# (Line 41) {
@EUDFunc
def UiltimateText(cp):
    # (Line 42) switch (v.Sound_Text_Uilti[cp])
    EUDSwitch(v.Sound_Text_Uilti[cp])
    # (Line 43) {
    # (Line 44) case 3200:
    _t1 = EUDSwitchCase()
    # (Line 45) PlayWAV("staredit\\wav\\Hime_EX01.ogg");
    if _t1(3200):
        # (Line 46) f.stb.printAt(3, "\x13\x04Tenkawa \x07MaiHime\n\x13\x04이정도 힘으로 나에게 \x06싸움\x04을 걸었던거야?");
        DoActions(PlayWAV("staredit\\wav\\Hime_EX01.ogg"))
        f.stb.printAt(3, "\x13\x04Tenkawa \x07MaiHime\n\x13\x04이정도 힘으로 나에게 \x06싸움\x04을 걸었던거야?")
        # (Line 47) v.Sound_Text_Uilti[cp] = 0;
        _ARRW(v.Sound_Text_Uilti, cp) << (0)
        # (Line 48) break;
        EUDBreak()
        # (Line 49) case 3201:
    _t2 = EUDSwitchCase()
    # (Line 50) PlayWAV("staredit\\wav\\Hime_EX02.ogg");
    if _t2(3201):
        # (Line 51) f.stb.printAt(3, "\x13\x04Tenkawa \x07MaiHime\n\x13\x04이정도 힘으로 모두를 \x08죽이려고했던거야?");
        DoActions(PlayWAV("staredit\\wav\\Hime_EX02.ogg"))
        f.stb.printAt(3, "\x13\x04Tenkawa \x07MaiHime\n\x13\x04이정도 힘으로 모두를 \x08죽이려고했던거야?")
        # (Line 52) v.Sound_Text_Uilti[cp] = 0;
        _ARRW(v.Sound_Text_Uilti, cp) << (0)
        # (Line 53) break;
        EUDBreak()
        # (Line 54) }
    # (Line 55) }
    EUDEndSwitch()
    # (Line 57) function UniqueText(cp)

# (Line 58) {
@EUDFunc
def UniqueText(cp):
    # (Line 59) switch (v.Sound_Text_Uniq[cp])
    EUDSwitch(v.Sound_Text_Uniq[cp])
    # (Line 60) {
    # (Line 61) case 3000:
    _t1 = EUDSwitchCase()
    # (Line 62) PlayWAV("staredit\\wav\\Hime_Unique01.ogg");
    if _t1(3000):
        # (Line 63) f.stb.printAt(3, "\x13\x04Tenkawa \x07MaiHime\n\x13\x04제군 ! \x07광연\x04의 시간이다!");
        DoActions(PlayWAV("staredit\\wav\\Hime_Unique01.ogg"))
        f.stb.printAt(3, "\x13\x04Tenkawa \x07MaiHime\n\x13\x04제군 ! \x07광연\x04의 시간이다!")
        # (Line 64) v.Sound_Text_Uniq[cp] = 0;
        _ARRW(v.Sound_Text_Uniq, cp) << (0)
        # (Line 65) break;
        EUDBreak()
        # (Line 66) }
    # (Line 67) }
    EUDEndSwitch()