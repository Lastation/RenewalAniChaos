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
# (Line 4) function Shape(cp : TrgPlayer, x, y);
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
            # (Line 12) if (f.loop[cp] == 0) Shape(cp, 50, 50);
            if EUDIf()(f.loop[cp] == 0):
                Shape(cp, 50, 50)
                # (Line 13) else if (f.loop[cp] == 1) Shape(cp, 0, 50);
            if EUDElseIf()(f.loop[cp] == 1):
                Shape(cp, 0, 50)
                # (Line 14) else if (f.loop[cp] == 2) Shape(cp, -50, 50);
            if EUDElseIf()(f.loop[cp] == 2):
                Shape(cp, -50, 50)
                # (Line 15) else if (f.loop[cp] == 3) Shape(cp, -50, 0);
            if EUDElseIf()(f.loop[cp] == 3):
                Shape(cp, -50, 0)
                # (Line 18) f.SkillWait(cp, 160);
            EUDEndIf()
            f.SkillWait(cp, 160)
            # (Line 20) f.loop[cp] += 1;
            _ARRW(f.loop, cp).__iadd__(1)
            # (Line 22) if (f.loop[cp] == 4)
            if EUDIf()(f.loop[cp] == 4):
                # (Line 23) {
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
            # (Line 30) if (f.loop[cp] == 0)
            if EUDIf()(f.loop[cp] == 0):
                # (Line 31) {
                # (Line 32) KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", cp);
                # (Line 34) f.EdgeShape(cp, 1, "60 + 1n Archon", 0, 5, 100);
                DoActions(KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", cp))
                f.EdgeShape(cp, 1, "60 + 1n Archon", 0, 5, 100)
                # (Line 35) KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
                # (Line 37) f.SkillWait(cp, 160);
                DoActions(KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp))
                f.SkillWait(cp, 160)
                # (Line 38) f.loop[cp] += 1;
                _ARRW(f.loop, cp).__iadd__(1)
                # (Line 39) }
                # (Line 40) else if (f.loop[cp] == 1)
            if EUDElseIf()(f.loop[cp] == 1):
                # (Line 41) {
                # (Line 42) f.EdgeShape(cp, 1, "60 + 1n Danimoth", 0, 5, 100);
                f.EdgeShape(cp, 1, "60 + 1n Danimoth", 0, 5, 100)
                # (Line 43) KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", cp);
                # (Line 44) f.EdgeShape(cp, 1, "40 + 1n Goliath", 0, 3, 100);
                DoActions(KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", cp))
                f.EdgeShape(cp, 1, "40 + 1n Goliath", 0, 3, 100)
                # (Line 46) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
                # (Line 47) MoveUnit(All, "40 + 1n Goliath", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
                DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
                # (Line 48) Order("40 + 1n Goliath", cp, "Anywhere", Attack, f.location[cp]);
                DoActions(MoveUnit(All, "40 + 1n Goliath", cp, "[Skill]Unit_Wait_ALL", f.location[cp]))
                # (Line 50) f.SkillWait(cp, 160);
                DoActions(Order("40 + 1n Goliath", cp, "Anywhere", Attack, f.location[cp]))
                f.SkillWait(cp, 160)
                # (Line 51) f.loop[cp] += 1;
                _ARRW(f.loop, cp).__iadd__(1)
                # (Line 52) }
                # (Line 53) else if (f.loop[cp] == 2)
            if EUDElseIf()(f.loop[cp] == 2):
                # (Line 54) {
                # (Line 55) KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);
                # (Line 57) f.EdgeShape(cp, 1, "Kakaru (Twilight)", 0, 5, 100);
                DoActions(KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp))
                f.EdgeShape(cp, 1, "Kakaru (Twilight)", 0, 5, 100)
                # (Line 58) KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
                # (Line 60) f.SkillWait(cp, 480);
                DoActions(KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp))
                f.SkillWait(cp, 480)
                # (Line 61) f.loop[cp] += 1;
                _ARRW(f.loop, cp).__iadd__(1)
                # (Line 62) }
                # (Line 63) else if (f.loop[cp] == 3)
            if EUDElseIf()(f.loop[cp] == 3):
                # (Line 64) {
                # (Line 65) f.EdgeShape(cp, 1, "60 + 1n Danimoth", 45, 5, 100);
                f.EdgeShape(cp, 1, "60 + 1n Danimoth", 45, 5, 100)
                # (Line 66) KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", cp);
                # (Line 67) f.EdgeShape(cp, 1, "40 + 1n Goliath", 45, 5, 100);
                DoActions(KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", cp))
                f.EdgeShape(cp, 1, "40 + 1n Goliath", 45, 5, 100)
                # (Line 69) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
                # (Line 70) MoveUnit(All, "40 + 1n Goliath", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
                DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
                # (Line 71) Order("40 + 1n Goliath", cp, "Anywhere", Attack, f.location[cp]);
                DoActions(MoveUnit(All, "40 + 1n Goliath", cp, "[Skill]Unit_Wait_ALL", f.location[cp]))
                # (Line 73) f.SkillWait(cp, 160);
                DoActions(Order("40 + 1n Goliath", cp, "Anywhere", Attack, f.location[cp]))
                f.SkillWait(cp, 160)
                # (Line 74) f.loop[cp] += 1;
                _ARRW(f.loop, cp).__iadd__(1)
                # (Line 75) }
                # (Line 76) else if (f.loop[cp] == 4)
            if EUDElseIf()(f.loop[cp] == 4):
                # (Line 77) {
                # (Line 78) KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);
                # (Line 80) f.EdgeShape(cp, 1, "40 + 1n Gantrithor", 45, 7, 150);
                DoActions(KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp))
                f.EdgeShape(cp, 1, "40 + 1n Gantrithor", 45, 7, 150)
                # (Line 81) f.EdgeShape(cp, 1, "60 + 1n Archon", 45, 7, 150);
                f.EdgeShape(cp, 1, "60 + 1n Archon", 45, 7, 150)
                # (Line 82) KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);
                # (Line 83) KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
                DoActions(KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp))
                # (Line 85) f.EdgeShape(cp, 1, "Kakaru (Twilight)", 45, 5, 100);
                DoActions(KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp))
                f.EdgeShape(cp, 1, "Kakaru (Twilight)", 45, 5, 100)
                # (Line 86) KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
                # (Line 88) f.SkillWait(cp, 80);
                DoActions(KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp))
                f.SkillWait(cp, 80)
                # (Line 90) f.count[cp] += 1;
                _ARRW(f.count, cp).__iadd__(1)
                # (Line 91) f.loop[cp] = 0;
                _ARRW(f.loop, cp) << (0)
                # (Line 92) }
                # (Line 93) }
            EUDEndIf()
            # (Line 94) else if (f.count[cp] == 2)
        if EUDElseIf()(f.count[cp] == 2):
            # (Line 95) {
            # (Line 96) KillUnitAt(All, "40 + 1n Ghost", "Anywhere", cp);
            # (Line 97) f.SkillEnd(cp);
            DoActions(KillUnitAt(All, "40 + 1n Ghost", "Anywhere", cp))
            f.SkillEnd(cp)
            # (Line 98) }
            # (Line 99) }
        EUDEndIf()
        # (Line 100) }
    EUDEndIf()
    # (Line 102) function Shape(cp : TrgPlayer, x, y)

# (Line 103) {
@EUDTypedFunc([TrgPlayer, None, None])
def Shape(cp, x, y):
    # (Line 104) KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", cp);
    # (Line 105) f.DotShape(cp, 1, "Protoss Dark Templar", x, y);
    DoActions(KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", cp))
    f.DotShape(cp, 1, "Protoss Dark Templar", x, y)
    # (Line 106) f.DotShape(cp, 1, "Protoss Dark Templar", -x, -y);
    f.DotShape(cp, 1, "Protoss Dark Templar", -x, -y)
    # (Line 107) f.DotShape(cp, 1, "40 + 1n Mojo", x, y);
    f.DotShape(cp, 1, "40 + 1n Mojo", x, y)
    # (Line 108) f.DotShape(cp, 1, "40 + 1n Mojo", -x, -y);
    f.DotShape(cp, 1, "40 + 1n Mojo", -x, -y)
    # (Line 109) f.DotShape(cp, 1, "Kakaru (Twilight)", -y, x);
    f.DotShape(cp, 1, "Kakaru (Twilight)", -y, x)
    # (Line 110) f.DotShape(cp, 1, "Kakaru (Twilight)", y, -x);
    f.DotShape(cp, 1, "Kakaru (Twilight)", y, -x)
    # (Line 111) f.DotShape(cp, 1, " Creep. Dunkelheit", -y, x);
    f.DotShape(cp, 1, " Creep. Dunkelheit", -y, x)
    # (Line 112) f.DotShape(cp, 1, " Creep. Dunkelheit", y, -x);
    f.DotShape(cp, 1, " Creep. Dunkelheit", y, -x)
    # (Line 113) KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);
    # (Line 114) KillUnitAt(All, "Protoss Dark Templar", "Anywhere", cp);
    DoActions(KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp))
    # (Line 115) KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
    DoActions(KillUnitAt(All, "Protoss Dark Templar", "Anywhere", cp))
    # (Line 116) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
    DoActions(KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp))
    # (Line 117) MoveUnit(All, " Creep. Dunkelheit", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
    DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
    # (Line 118) Order(" Creep. Dunkelheit", cp, "Anywhere", Attack, f.location[cp]);
    DoActions(MoveUnit(All, " Creep. Dunkelheit", cp, "[Skill]Unit_Wait_ALL", f.location[cp]))
    # (Line 119) }
    DoActions(Order(" Creep. Dunkelheit", cp, "Anywhere", Attack, f.location[cp]))