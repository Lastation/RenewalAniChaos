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
            # (Line 11) KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);
            # (Line 12) KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
            DoActions(KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp))
            # (Line 14) if (f.loop[cp] < 5)
            DoActions(KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp))
            if EUDIf()(f.loop[cp] >= 5, neg=True):
                # (Line 15) {
                # (Line 16) f.DoubleShape(cp, 1, "Protoss Dark Archon", -100, 100 - 50 * f.loop[cp]);
                f.DoubleShape(cp, 1, "Protoss Dark Archon", -100, 100 - 50 * f.loop[cp])
                # (Line 17) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
                # (Line 18) f.DoubleShape(cp, 1, "40 + 1n Goliath", 100 - 50 * f.loop[cp], 100);
                DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
                f.DoubleShape(cp, 1, "40 + 1n Goliath", 100 - 50 * f.loop[cp], 100)
                # (Line 19) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
                # (Line 20) Order("40 + 1n Goliath", cp, "Anywhere", Attack, f.location[cp]);
                DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
                # (Line 21) }
                DoActions(Order("40 + 1n Goliath", cp, "Anywhere", Attack, f.location[cp]))
                # (Line 22) if (f.loop[cp] == 5)
            EUDEndIf()
            if EUDIf()(f.loop[cp] == 5):
                # (Line 23) {
                # (Line 24) f.DoubleShape(cp, 1, "Protoss Dark Archon", -50, 100);
                f.DoubleShape(cp, 1, "Protoss Dark Archon", -50, 100)
                # (Line 25) f.DoubleShape(cp, 1, "40 + 1n Goliath", -100, 50);
                f.DoubleShape(cp, 1, "40 + 1n Goliath", -100, 50)
                # (Line 26) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
                # (Line 27) Order("40 + 1n Goliath", cp, "Anywhere", Attack, f.location[cp]);
                DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
                # (Line 28) }
                DoActions(Order("40 + 1n Goliath", cp, "Anywhere", Attack, f.location[cp]))
                # (Line 29) if (f.loop[cp] == 6)
            EUDEndIf()
            if EUDIf()(f.loop[cp] == 6):
                # (Line 30) {
                # (Line 31) f.DoubleShape(cp, 1, "Protoss Dark Archon", 0, -100);
                f.DoubleShape(cp, 1, "Protoss Dark Archon", 0, -100)
                # (Line 32) f.DoubleShape(cp, 1, "40 + 1n Goliath", -100, 0);
                f.DoubleShape(cp, 1, "40 + 1n Goliath", -100, 0)
                # (Line 33) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
                # (Line 34) Order("40 + 1n Goliath", cp, "Anywhere", Attack, f.location[cp]);
                DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
                # (Line 35) }
                DoActions(Order("40 + 1n Goliath", cp, "Anywhere", Attack, f.location[cp]))
                # (Line 36) if (f.loop[cp] == 7)
            EUDEndIf()
            if EUDIf()(f.loop[cp] == 7):
                # (Line 37) {
                # (Line 38) f.EdgeShape(cp, 1, "Protoss Dark Archon", 45,3, 50);
                f.EdgeShape(cp, 1, "Protoss Dark Archon", 45, 3, 50)
                # (Line 39) f.EdgeShape(cp, 1, "40 + 1n Goliath", 45,3, 50);
                f.EdgeShape(cp, 1, "40 + 1n Goliath", 45, 3, 50)
                # (Line 40) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
                # (Line 41) Order("40 + 1n Goliath", cp, "Anywhere", Attack, f.location[cp]);
                DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
                # (Line 42) }
                DoActions(Order("40 + 1n Goliath", cp, "Anywhere", Attack, f.location[cp]))
                # (Line 43) f.SkillWait(cp, 80);
            EUDEndIf()
            f.SkillWait(cp, 80)
            # (Line 45) f.loop[cp] += 1;
            _ARRW(f.loop, cp).__iadd__(1)
            # (Line 47) if (f.loop[cp] == 8)
            if EUDIf()(f.loop[cp] == 8):
                # (Line 48) {
                # (Line 49) f.count[cp] += 1;
                _ARRW(f.count, cp).__iadd__(1)
                # (Line 50) f.loop[cp] = 0;
                _ARRW(f.loop, cp) << (0)
                # (Line 51) }
                # (Line 52) }
            EUDEndIf()
            # (Line 54) else if (f.count[cp] == 1)
        if EUDElseIf()(f.count[cp] == 1):
            # (Line 55) {
            # (Line 56) KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);
            # (Line 57) KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
            DoActions(KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp))
            # (Line 59) f.SkillEnd(cp);
            DoActions(KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp))
            f.SkillEnd(cp)
            # (Line 60) }
            # (Line 61) }
        EUDEndIf()
        # (Line 62) }
    EUDEndIf()