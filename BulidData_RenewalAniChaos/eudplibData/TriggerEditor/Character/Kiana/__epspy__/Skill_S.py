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
# (Line 4) function Shape(cp, UnitA : TrgUnit, UnitB : TrgUnit, x, y);
# (Line 6) function main(cp)
# (Line 7) {
@EUDFunc
def f_main(cp):
    # (Line 8) if (f.delay[cp] == 0)
    if EUDIf()(f.delay[cp] == 0):
        # (Line 9) {
        # (Line 10) if (f.count[cp] == 0)
        if EUDIf()(f.count[cp] == 0):
            # (Line 11) {
            # (Line 12) KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
            # (Line 14) Shape(cp, "40 + 1n Wraith", "60 + 1n Archon", 96, 32);
            DoActions(KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp))
            Shape(cp, "40 + 1n Wraith", "60 + 1n Archon", 96, 32)
            # (Line 15) f.SkillWait(cp, 130);
            f.SkillWait(cp, 130)
            # (Line 16) f.count[cp] += 1;
            _ARRW(f.count, cp).__iadd__(1)
            # (Line 17) }
            # (Line 18) else if (f.count[cp] == 1)
        if EUDElseIf()(f.count[cp] == 1):
            # (Line 19) {
            # (Line 20) KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
            # (Line 22) Shape(cp, "40 + 1n Wraith", "60 + 1n Archon", 32, 32);
            DoActions(KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp))
            Shape(cp, "40 + 1n Wraith", "60 + 1n Archon", 32, 32)
            # (Line 23) f.SkillWait(cp, 130);
            f.SkillWait(cp, 130)
            # (Line 24) f.count[cp] += 1;
            _ARRW(f.count, cp).__iadd__(1)
            # (Line 25) }
            # (Line 26) else if (f.count[cp] == 2)
        if EUDElseIf()(f.count[cp] == 2):
            # (Line 27) {
            # (Line 28) KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
            # (Line 30) Shape(cp, "40 + 1n Wraith", "60 + 1n Archon", -32, 32);
            DoActions(KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp))
            Shape(cp, "40 + 1n Wraith", "60 + 1n Archon", -32, 32)
            # (Line 31) f.SkillWait(cp, 130);
            f.SkillWait(cp, 130)
            # (Line 32) f.count[cp] += 1;
            _ARRW(f.count, cp).__iadd__(1)
            # (Line 33) }
            # (Line 34) else if (f.count[cp] == 3)
        if EUDElseIf()(f.count[cp] == 3):
            # (Line 35) {
            # (Line 36) KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
            # (Line 38) Shape(cp, "40 + 1n Wraith", "60 + 1n Archon", -96, 32);
            DoActions(KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp))
            Shape(cp, "40 + 1n Wraith", "60 + 1n Archon", -96, 32)
            # (Line 39) f.SkillWait(cp, 130);
            f.SkillWait(cp, 130)
            # (Line 40) f.count[cp] += 1;
            _ARRW(f.count, cp).__iadd__(1)
            # (Line 41) }
            # (Line 42) else if (f.count[cp] == 4)
        if EUDElseIf()(f.count[cp] == 4):
            # (Line 43) {
            # (Line 44) KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
            # (Line 46) Shape(cp, "40 + 1n Mojo", "Protoss Dark Archon", 96, 32);
            DoActions(KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp))
            Shape(cp, "40 + 1n Mojo", "Protoss Dark Archon", 96, 32)
            # (Line 47) Shape(cp, "40 + 1n Mojo", "Protoss Dark Archon", 32, 32);
            Shape(cp, "40 + 1n Mojo", "Protoss Dark Archon", 32, 32)
            # (Line 48) Shape(cp, "40 + 1n Mojo", "Protoss Dark Archon", -32, 32);
            Shape(cp, "40 + 1n Mojo", "Protoss Dark Archon", -32, 32)
            # (Line 49) Shape(cp, "40 + 1n Mojo", "Protoss Dark Archon", -96, 32);
            Shape(cp, "40 + 1n Mojo", "Protoss Dark Archon", -96, 32)
            # (Line 50) f.SkillWait(cp, 130);
            f.SkillWait(cp, 130)
            # (Line 51) f.count[cp] += 1;
            _ARRW(f.count, cp).__iadd__(1)
            # (Line 52) }
            # (Line 53) else if (f.count[cp] == 5)
        if EUDElseIf()(f.count[cp] == 5):
            # (Line 54) {
            # (Line 55) KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);
            # (Line 57) f.SkillEnd(cp);
            DoActions(KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp))
            f.SkillEnd(cp)
            # (Line 58) }
            # (Line 59) }
        EUDEndIf()
        # (Line 60) }
    EUDEndIf()
    # (Line 62) function Shape(cp, UnitA : TrgUnit, UnitB : TrgUnit, x, y)

# (Line 63) {
@EUDTypedFunc([None, TrgUnit, TrgUnit, None, None])
def Shape(cp, UnitA, UnitB, x, y):
    # (Line 64) f.MoveLoc(f.heroID[cp], cp, x, y);
    f.MoveLoc(f.heroID[cp], cp, x, y)
    # (Line 65) f.SkillUnit(cp, 1, UnitA);
    f.SkillUnit(cp, 1, UnitA)
    # (Line 66) f.SkillUnit(cp, 1, UnitB);
    f.SkillUnit(cp, 1, UnitB)
    # (Line 67) f.MoveLoc(f.heroID[cp], cp, -x, -y);
    f.MoveLoc(f.heroID[cp], cp, -x, -y)
    # (Line 68) f.SkillUnit(cp, 1, UnitA);
    f.SkillUnit(cp, 1, UnitA)
    # (Line 69) f.SkillUnit(cp, 1, UnitB);
    f.SkillUnit(cp, 1, UnitB)
    # (Line 70) KillUnitAt(All, UnitB, "Anywhere", cp);
    # (Line 71) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
    DoActions(KillUnitAt(All, UnitB, "Anywhere", cp))
    # (Line 72) Order(UnitA, cp, "Anywhere", Attack, f.location[cp]);
    DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
    # (Line 73) }
    DoActions(Order(UnitA, cp, "Anywhere", Attack, f.location[cp]))