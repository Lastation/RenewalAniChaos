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
# (Line 3) function main(cp)
# (Line 4) {
@EUDFunc
def f_main(cp):
    # (Line 5) if (f.delay[cp] == 0)
    if EUDIf()(f.delay[cp] == 0):
        # (Line 6) {
        # (Line 7) if (f.count[cp] == 0)
        if EUDIf()(f.count[cp] == 0):
            # (Line 8) {
            # (Line 9) if (f.loop[cp] < 4)
            if EUDIf()(f.loop[cp] >= 4, neg=True):
                # (Line 10) {
                # (Line 11) f.LineShape(cp, 1, "Target", 90 * f.loop[cp] + 45, 5, 50, 50);
                f.LineShape(cp, 1, "Target", 90 * f.loop[cp] + 45, 5, 50, 50)
                # (Line 12) f.LineShape(cp, 1, "Protoss Dark Templar", 90 * f.loop[cp] + 45, 5, 50, 50);
                f.LineShape(cp, 1, "Protoss Dark Templar", 90 * f.loop[cp] + 45, 5, 50, 50)
                # (Line 13) KillUnitAt(All, "Target", "Anywhere", cp);
                # (Line 14) KillUnitAt(All, "Protoss Dark Templar", "Anywhere", cp);
                DoActions(KillUnitAt(All, "Target", "Anywhere", cp))
                # (Line 15) f.SkillWait(cp, 80);
                DoActions(KillUnitAt(All, "Protoss Dark Templar", "Anywhere", cp))
                f.SkillWait(cp, 80)
                # (Line 16) f.loop[cp] += 1;
                _ARRW(f.loop, cp).__iadd__(1)
                # (Line 17) }
                # (Line 18) else if (f.loop[cp] == 4)
            if EUDElseIf()(f.loop[cp] == 4):
                # (Line 19) {
                # (Line 20) f.SkillWait(cp, 80);
                f.SkillWait(cp, 80)
                # (Line 22) f.count[cp] += 1;
                _ARRW(f.count, cp).__iadd__(1)
                # (Line 23) f.loop[cp] = 0;
                _ARRW(f.loop, cp) << (0)
                # (Line 24) }
                # (Line 25) }
            EUDEndIf()
            # (Line 26) else if (f.count[cp] == 1)
        if EUDElseIf()(f.count[cp] == 1):
            # (Line 27) {
            # (Line 28) if (f.loop[cp] < 3)
            if EUDIf()(f.loop[cp] >= 3, neg=True):
                # (Line 29) {
                # (Line 30) RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
                # (Line 32) f.LineShape(cp, 1, "40 + 1n Wraith", 45 * 3 * f.loop[cp], 5, 50, 0);
                DoActions(RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp))
                f.LineShape(cp, 1, "40 + 1n Wraith", 45 * 3 * f.loop[cp], 5, 50, 0)
                # (Line 33) f.LineShape(cp, 1, "40 + 1n Zealot", 45 * 3 * f.loop[cp], 5, 50, 0);
                f.LineShape(cp, 1, "40 + 1n Zealot", 45 * 3 * f.loop[cp], 5, 50, 0)
                # (Line 34) KillUnitAt(All, "40 + 1n Zealot", "Anywhere", cp);
                # (Line 36) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
                DoActions(KillUnitAt(All, "40 + 1n Zealot", "Anywhere", cp))
                # (Line 37) Order("40 + 1n Wraith", cp, "Anywhere", Attack, "Anywhere");
                DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
                # (Line 39) f.SkillWait(cp, 80);
                DoActions(Order("40 + 1n Wraith", cp, "Anywhere", Attack, "Anywhere"))
                f.SkillWait(cp, 80)
                # (Line 40) f.loop[cp] += 1;
                _ARRW(f.loop, cp).__iadd__(1)
                # (Line 41) }
                # (Line 42) else if (f.loop[cp] == 3)
            if EUDElseIf()(f.loop[cp] == 3):
                # (Line 43) {
                # (Line 44) RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
                # (Line 46) f.SkillWait(cp, 80);
                DoActions(RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp))
                f.SkillWait(cp, 80)
                # (Line 48) f.count[cp] += 1;
                _ARRW(f.count, cp).__iadd__(1)
                # (Line 49) f.loop[cp] = 0;
                _ARRW(f.loop, cp) << (0)
                # (Line 50) }
                # (Line 51) }
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