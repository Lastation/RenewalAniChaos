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
# (Line 4) function main(cp)
# (Line 5) {
@EUDFunc
def f_main(cp):
    # (Line 6) if (f.delay[cp] == 0)
    if EUDIf()(f.delay[cp] == 0):
        # (Line 7) {
        # (Line 8) if (f.count[cp] == 0)
        if EUDIf()(f.count[cp] == 0):
            # (Line 9) {
            # (Line 10) if (f.loop[cp] == 0)
            if EUDIf()(f.loop[cp] == 0):
                # (Line 11) {
                # (Line 12) f.NxNSquareShape(cp, 1, "40 + 1n Mojo", 3, 50);
                f.NxNSquareShape(cp, 1, "40 + 1n Mojo", 3, 50)
                # (Line 13) f.SquareShape(cp, 1, "40 + 1n Marine", 50, 50);
                f.SquareShape(cp, 1, "40 + 1n Marine", 50, 50)
                # (Line 14) f.SquareShape(cp, 1, "40 + 1n Marine", 0, 50);
                f.SquareShape(cp, 1, "40 + 1n Marine", 0, 50)
                # (Line 16) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
                # (Line 17) MoveUnit(All, "40 + 1n Marine", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
                DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
                # (Line 18) Order("40 + 1n Marine", cp, "Anywhere", Attack, f.location[cp]);
                DoActions(MoveUnit(All, "40 + 1n Marine", cp, "[Skill]Unit_Wait_ALL", f.location[cp]))
                # (Line 20) KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);
                DoActions(Order("40 + 1n Marine", cp, "Anywhere", Attack, f.location[cp]))
                # (Line 22) f.SkillWait(cp, 160);
                DoActions(KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp))
                f.SkillWait(cp, 160)
                # (Line 23) f.count[cp] += 1;
                _ARRW(f.count, cp).__iadd__(1)
                # (Line 24) f.loop[cp] = 0;
                _ARRW(f.loop, cp) << (0)
                # (Line 25) }
                # (Line 26) }
            EUDEndIf()
            # (Line 27) else if (f.count[cp] == 1)
        if EUDElseIf()(f.count[cp] == 1):
            # (Line 28) {
            # (Line 29) if (f.loop[cp] < 4)
            if EUDIf()(f.loop[cp] >= 4, neg=True):
                # (Line 30) {
                # (Line 31) f.DotShape(cp, 1, "Protoss Dark Templar", 100 - 50 * f.loop[cp], 100);
                f.DotShape(cp, 1, "Protoss Dark Templar", 100 - 50 * f.loop[cp], 100)
                # (Line 32) f.DotShape(cp, 1, "Protoss Dark Templar", -100 + 50 * f.loop[cp], -100);
                f.DotShape(cp, 1, "Protoss Dark Templar", -100 + 50 * f.loop[cp], -100)
                # (Line 33) f.DotShape(cp, 1, "40 + 1n Zealot", -100, 100 - 50 * f.loop[cp]);
                f.DotShape(cp, 1, "40 + 1n Zealot", -100, 100 - 50 * f.loop[cp])
                # (Line 34) f.DotShape(cp, 1, "40 + 1n Zealot", 100, -100 + 50 * f.loop[cp]);
                f.DotShape(cp, 1, "40 + 1n Zealot", 100, -100 + 50 * f.loop[cp])
                # (Line 35) KillUnitAt(All, "40 + 1n Zealot", "Anywhere", cp);
                # (Line 36) KillUnitAt(All, "Protoss Dark Templar", "Anywhere", cp);
                DoActions(KillUnitAt(All, "40 + 1n Zealot", "Anywhere", cp))
                # (Line 38) f.SkillWait(cp, 80);
                DoActions(KillUnitAt(All, "Protoss Dark Templar", "Anywhere", cp))
                f.SkillWait(cp, 80)
                # (Line 39) f.loop[cp] += 1;
                _ARRW(f.loop, cp).__iadd__(1)
                # (Line 40) }
                # (Line 41) else if (f.loop[cp] == 4)
            if EUDElseIf()(f.loop[cp] == 4):
                # (Line 42) {
                # (Line 43) KillUnitAt(All, "40 + 1n Marine", "Anywhere", cp);
                # (Line 44) f.NxNSquareShape(cp, 1, "Kakaru (Twilight)", 3, 50);
                DoActions(KillUnitAt(All, "40 + 1n Marine", "Anywhere", cp))
                f.NxNSquareShape(cp, 1, "Kakaru (Twilight)", 3, 50)
                # (Line 45) KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
                # (Line 46) f.EdgeShape(cp, 1, "40 + 1n Ghost", 45, 3, 75);
                DoActions(KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp))
                f.EdgeShape(cp, 1, "40 + 1n Ghost", 45, 3, 75)
                # (Line 47) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
                # (Line 48) MoveUnit(All, "40 + 1n Ghost", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
                DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
                # (Line 49) Order("40 + 1n Ghost", cp, "Anywhere", Attack, f.location[cp]);
                DoActions(MoveUnit(All, "40 + 1n Ghost", cp, "[Skill]Unit_Wait_ALL", f.location[cp]))
                # (Line 51) f.SkillWait(cp, 320);
                DoActions(Order("40 + 1n Ghost", cp, "Anywhere", Attack, f.location[cp]))
                f.SkillWait(cp, 320)
                # (Line 53) f.loop[cp] += 1;
                _ARRW(f.loop, cp).__iadd__(1)
                # (Line 54) }
                # (Line 55) else if (f.loop[cp] == 5)
            if EUDElseIf()(f.loop[cp] == 5):
                # (Line 56) {
                # (Line 57) KillUnitAt(All, "40 + 1n Ghost", "Anywhere", cp);
                # (Line 58) f.EdgeShape(cp, 1, "60 + 1n Danimoth", 45, 5, 100);
                DoActions(KillUnitAt(All, "40 + 1n Ghost", "Anywhere", cp))
                f.EdgeShape(cp, 1, "60 + 1n Danimoth", 45, 5, 100)
                # (Line 59) KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", cp);
                # (Line 60) f.EdgeShape(cp, 1, "40 + 1n Ghost", 45, 3, 100);
                DoActions(KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", cp))
                f.EdgeShape(cp, 1, "40 + 1n Ghost", 45, 3, 100)
                # (Line 61) f.EdgeShape(cp, 1, "60 + 1n Archon", 45, 4, 100);
                f.EdgeShape(cp, 1, "60 + 1n Archon", 45, 4, 100)
                # (Line 62) KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
                # (Line 64) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
                DoActions(KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp))
                # (Line 65) MoveUnit(All, "40 + 1n Ghost", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
                DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
                # (Line 66) Order("40 + 1n Ghost", cp, "Anywhere", Attack, f.location[cp]);
                DoActions(MoveUnit(All, "40 + 1n Ghost", cp, "[Skill]Unit_Wait_ALL", f.location[cp]))
                # (Line 68) f.SkillWait(cp, 320);
                DoActions(Order("40 + 1n Ghost", cp, "Anywhere", Attack, f.location[cp]))
                f.SkillWait(cp, 320)
                # (Line 70) f.count[cp] += 1;
                _ARRW(f.count, cp).__iadd__(1)
                # (Line 71) f.loop[cp] = 0;
                _ARRW(f.loop, cp) << (0)
                # (Line 72) }
                # (Line 73) }
            EUDEndIf()
            # (Line 74) else if (f.count[cp] == 2)
        if EUDElseIf()(f.count[cp] == 2):
            # (Line 75) {
            # (Line 76) KillUnitAt(All, "40 + 1n Ghost", "Anywhere", cp);
            # (Line 77) f.SkillEnd(cp);
            DoActions(KillUnitAt(All, "40 + 1n Ghost", "Anywhere", cp))
            f.SkillEnd(cp)
            # (Line 78) }
            # (Line 79) }
        EUDEndIf()
        # (Line 80) }
    EUDEndIf()