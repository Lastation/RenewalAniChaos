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
# (Line 2) import Function as f;
import Function as f
# (Line 4) const looker = PVariable();
looker = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 6) function Text(num);
# (Line 7) function Looker()
# (Line 8) {
@EUDFunc
def Looker():
    # (Line 9) if (looker[getuserplayerid() - 128] > 0)
    if EUDIf()(looker[f_getuserplayerid() - 128] <= 0, neg=True):
        # (Line 10) {
        # (Line 11) Text(looker[getuserplayerid() - 128]);
        Text(looker[f_getuserplayerid() - 128])
        # (Line 12) looker[getuserplayerid() - 128] = 0;
        _ARRW(looker, f_getuserplayerid() - 128) << (0)
        # (Line 13) }
        # (Line 14) }
    EUDEndIf()
    # (Line 16) function main(cp)

# (Line 17) {
@EUDFunc
def f_main(cp):
    # (Line 18) if (f.Kiana_Voice[cp] > 0)
    if EUDIf()(f.Kiana_Voice[cp] <= 0, neg=True):
        # (Line 19) {
        # (Line 20) Text(f.Kiana_Voice[cp]);
        Text(f.Kiana_Voice[cp])
        # (Line 21) looker[cp] = f.Kiana_Voice[cp];
        _ARRW(looker, cp) << (f.Kiana_Voice[cp])
        # (Line 22) f.Kiana_Voice[cp] = 0;
        _ARRW(f.Kiana_Voice, cp) << (0)
        # (Line 23) }
        # (Line 24) }
    EUDEndIf()
    # (Line 26) function Text(num)

# (Line 27) {
@EUDFunc
def Text(num):
    # (Line 28) switch (num)
    EUDSwitch(num)
    # (Line 29) {
    # (Line 30) case 1:
    _t1 = EUDSwitchCase()
    # (Line 31) PlayWAV("Kiana_01.ogg");
    if _t1(1):
        # (Line 32) f.stb.print("\x13\x19Kiana Kaslana\n\n\x13\x04네코 참!");
        DoActions(PlayWAV("Kiana_01.ogg"))
        f.stb.print("\x13\x19Kiana Kaslana\n\n\x13\x04네코 참!")
        # (Line 33) break;
        EUDBreak()
        # (Line 34) }
    # (Line 35) }
    EUDEndSwitch()