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

# (Line 1) import Function as f;
import Function as f
# (Line 3) const s = StringBuffer();
s = _CGFW(lambda: [StringBuffer()], 1)[0]
# (Line 5) function main(cp)
# (Line 6) {
@EUDFunc
def f_main(cp):
    # (Line 7) if (f.delay[cp] == 0)
    if EUDIf()(f.delay[cp] == 0):
        # (Line 8) {
        # (Line 9) if (f.count[cp] == 0)
        if EUDIf()(f.count[cp] == 0):
            # (Line 10) {
            # (Line 11) if (f.loop[cp] == 0)
            if EUDIf()(f.loop[cp] == 0):
                # (Line 12) {
                # (Line 13) if (cp < 3) SetSwitch("Unique - Nanami1", Set);
                if EUDIf()(cp >= 3, neg=True):
                    # (Line 14) else SetSwitch("Unique - Nanami2", Set);
                    DoActions(SetSwitch("Unique - Nanami1", Set))
                if EUDElse()():
                    # (Line 16) f.DotShape(cp, 1, "50 + 1n Battlecruiser", 0, 0);
                    DoActions(SetSwitch("Unique - Nanami2", Set))
                EUDEndIf()
                f.DotShape(cp, 1, "50 + 1n Battlecruiser", 0, 0)
                # (Line 17) KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
                # (Line 19) SetDeaths(cp, SetTo, 2160, " `UniqueCoolTime");
                DoActions(KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp))
                # (Line 20) SetDeaths(cp, SetTo, 720, " `UniqueSkill");
                DoActions(SetDeaths(cp, SetTo, 2160, " `UniqueCoolTime"))
                # (Line 22) f.SkillWait(cp, 80);
                DoActions(SetDeaths(cp, SetTo, 720, " `UniqueSkill"))
                f.SkillWait(cp, 80)
                # (Line 24) f.count[cp] += 1;
                _ARRW(f.count, cp).__iadd__(1)
                # (Line 25) f.loop[cp] = 0;
                _ARRW(f.loop, cp) << (0)
                # (Line 26) }
                # (Line 27) }
            EUDEndIf()
            # (Line 28) else if (f.count[cp] == 1)
        if EUDElseIf()(f.count[cp] == 1):
            # (Line 29) {
            # (Line 30) f.SkillEnd(cp);
            f.SkillEnd(cp)
            # (Line 31) }
            # (Line 32) }
        EUDEndIf()
        # (Line 33) }
    EUDEndIf()