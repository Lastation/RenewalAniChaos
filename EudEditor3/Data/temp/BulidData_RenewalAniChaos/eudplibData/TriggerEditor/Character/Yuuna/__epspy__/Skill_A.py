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
            # (Line 11) if (f.loop[cp] < 8)
            if EUDIf()(f.loop[cp] >= 8, neg=True):
                # (Line 12) {
                # (Line 13) f.LineShape(cp, 1, "Kakaru (Twilight)", 45 * 3 * f.loop[cp], 7, 50, 50);
                f.LineShape(cp, 1, "Kakaru (Twilight)", 45 * 3 * f.loop[cp], 7, 50, 50)
                # (Line 14) f.LineShape(cp, 1, "Protoss Dark Templar", 45 * 3 * f.loop[cp], 7, 50, 50);
                f.LineShape(cp, 1, "Protoss Dark Templar", 45 * 3 * f.loop[cp], 7, 50, 50)
                # (Line 15) KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
                # (Line 16) KillUnitAt(All, "Protoss Dark Templar", "Anywhere", cp);
                DoActions(KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp))
                # (Line 17) f.SkillWait(cp, 50);
                DoActions(KillUnitAt(All, "Protoss Dark Templar", "Anywhere", cp))
                f.SkillWait(cp, 50)
                # (Line 18) f.loop[cp] += 1;
                _ARRW(f.loop, cp).__iadd__(1)
                # (Line 19) }
                # (Line 20) else if (f.loop[cp] == 8)
            if EUDElseIf()(f.loop[cp] == 8):
                # (Line 21) {
                # (Line 22) f.SkillWait(cp, 0);
                f.SkillWait(cp, 0)
                # (Line 24) f.count[cp] += 1;
                _ARRW(f.count, cp).__iadd__(1)
                # (Line 25) f.loop[cp] = 0;
                _ARRW(f.loop, cp) << (0)
                # (Line 26) }
                # (Line 27) }
            EUDEndIf()
            # (Line 28) if (f.count[cp] == 1)
        EUDEndIf()
        if EUDIf()(f.count[cp] == 1):
            # (Line 29) {
            # (Line 30) if (f.loop[cp] < 2)
            if EUDIf()(f.loop[cp] >= 2, neg=True):
                # (Line 31) {
                # (Line 32) RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
                # (Line 33) f.NxNSquareShape(cp, 1, "50 + 1n Battlecruiser", 3, 75);
                DoActions(RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp))
                f.NxNSquareShape(cp, 1, "50 + 1n Battlecruiser", 3, 75)
                # (Line 34) Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, "Anywhere");
                # (Line 36) f.SkillWait(cp, 50);
                DoActions(Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, "Anywhere"))
                f.SkillWait(cp, 50)
                # (Line 37) f.loop[cp] += 1;
                _ARRW(f.loop, cp).__iadd__(1)
                # (Line 38) }
                # (Line 39) else if (f.loop[cp] == 2)
            if EUDElseIf()(f.loop[cp] == 2):
                # (Line 40) {
                # (Line 41) RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
                # (Line 42) f.NxNSquareShape(cp, 1, " Unit. Hoffnung 25000", 3, 75);
                DoActions(RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp))
                f.NxNSquareShape(cp, 1, " Unit. Hoffnung 25000", 3, 75)
                # (Line 43) KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
                # (Line 45) f.SkillWait(cp, 0);
                DoActions(KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp))
                f.SkillWait(cp, 0)
                # (Line 47) f.count[cp] += 1;
                _ARRW(f.count, cp).__iadd__(1)
                # (Line 48) f.loop[cp] = 0;
                _ARRW(f.loop, cp) << (0)
                # (Line 49) }
                # (Line 50) }
            EUDEndIf()
            # (Line 52) else if (f.count[cp] == 2)
        if EUDElseIf()(f.count[cp] == 2):
            # (Line 53) {
            # (Line 54) f.SkillEnd(cp);
            f.SkillEnd(cp)
            # (Line 55) }
            # (Line 56) }
        EUDEndIf()
        # (Line 57) }
    EUDEndIf()