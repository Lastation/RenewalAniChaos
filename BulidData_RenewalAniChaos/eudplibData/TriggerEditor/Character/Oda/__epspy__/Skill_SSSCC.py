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
    # (Line 6) MoveUnit(All, "40 + 1n Goliath", cp, "Anywhere", "[Skill]HoldPosition");
    # (Line 7) MoveUnit(All, "50 + 1n Tank", cp, "Anywhere", "[Skill]HoldPosition");
    DoActions(MoveUnit(All, "40 + 1n Goliath", cp, "Anywhere", "[Skill]HoldPosition"))
    # (Line 8) MoveUnit(All, "40 + 1n Marine", cp, "Anywhere", "[Skill]HoldPosition");
    DoActions(MoveUnit(All, "50 + 1n Tank", cp, "Anywhere", "[Skill]HoldPosition"))
    # (Line 10) f.BanReturn(cp);
    DoActions(MoveUnit(All, "40 + 1n Marine", cp, "Anywhere", "[Skill]HoldPosition"))
    f.BanReturn(cp)
    # (Line 11) f.HoldPosition(cp);
    f.HoldPosition(cp)
    # (Line 13) if (f.delay[cp] == 0)
    if EUDIf()(f.delay[cp] == 0):
        # (Line 14) {
        # (Line 15) if (f.count[cp] == 0)
        if EUDIf()(f.count[cp] == 0):
            # (Line 16) {
            # (Line 17) var i = f.loop[cp] / 2;
            i = EUDVariable()
            i << (f.loop[cp] // 2)
            # (Line 19) if (f.loop[cp] % 2 == 0)
            if EUDIf()(f.loop[cp] % 2 == 0):
                # (Line 20) {
                # (Line 21) RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
                # (Line 23) f.SquareShape(cp, 1, "50 + 1n Battlecruiser", -100 + 50 * i, 100);
                DoActions(RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp))
                f.SquareShape(cp, 1, "50 + 1n Battlecruiser", -100 + 50 * i, 100)
                # (Line 24) f.SquareShape(cp, 1, "50 + 1n Tank", -100 + 50 * i, 100);
                f.SquareShape(cp, 1, "50 + 1n Tank", -100 + 50 * i, 100)
                # (Line 25) f.SquareShape(cp, 1, "60 + 1n Siege", -100 + 50 * i, 100);
                f.SquareShape(cp, 1, "60 + 1n Siege", -100 + 50 * i, 100)
                # (Line 27) KillUnitAt(All, "60 + 1n Siege", "Anywhere", cp);
                # (Line 29) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
                DoActions(KillUnitAt(All, "60 + 1n Siege", "Anywhere", cp))
                # (Line 30) MoveUnit(All, "50 + 1n Tank", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
                DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
                # (Line 31) Order("50 + 1n Tank", cp, "Anywhere", Attack, f.location[cp]);
                DoActions(MoveUnit(All, "50 + 1n Tank", cp, "[Skill]Unit_Wait_ALL", f.location[cp]))
                # (Line 32) Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, f.location[cp]);
                DoActions(Order("50 + 1n Tank", cp, "Anywhere", Attack, f.location[cp]))
                # (Line 33) }
                DoActions(Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, f.location[cp]))
                # (Line 35) i = f.loop[cp];
            EUDEndIf()
            i << (f.loop[cp])
            # (Line 37) if (f.loop[cp] < 6)
            if EUDIf()(f.loop[cp] >= 6, neg=True):
                # (Line 38) {
                # (Line 39) f.SquareShape(cp, 1, "Protoss Dark Archon", -150 + 50 * i, 150);
                f.SquareShape(cp, 1, "Protoss Dark Archon", -150 + 50 * i, 150)
                # (Line 40) f.SquareShape(cp, 1, "40 + 1n Guardian", -150 + 50 * i, 150);
                f.SquareShape(cp, 1, "40 + 1n Guardian", -150 + 50 * i, 150)
                # (Line 41) KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
                # (Line 42) KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
                DoActions(KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp))
                # (Line 43) }
                DoActions(KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp))
                # (Line 44) else if (f.loop[cp] < 8)
            if EUDElseIf()(f.loop[cp] >= 8, neg=True):
                # (Line 45) {
                # (Line 46) f.EdgeShape(cp, 1, "Protoss Dark Archon", 45, 7, 150);
                f.EdgeShape(cp, 1, "Protoss Dark Archon", 45, 7, 150)
                # (Line 47) f.EdgeShape(cp, 1, "40 + 1n Guardian", 45, 7, 150);
                f.EdgeShape(cp, 1, "40 + 1n Guardian", 45, 7, 150)
                # (Line 48) KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
                # (Line 49) KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
                DoActions(KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp))
                # (Line 50) }
                DoActions(KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp))
                # (Line 52) f.SkillWait(cp, 160);
            EUDEndIf()
            f.SkillWait(cp, 160)
            # (Line 54) f.loop[cp] += 1;
            _ARRW(f.loop, cp).__iadd__(1)
            # (Line 56) if (f.loop[cp] == 8)
            if EUDIf()(f.loop[cp] == 8):
                # (Line 57) {
                # (Line 58) f.count[cp] += 1;
                _ARRW(f.count, cp).__iadd__(1)
                # (Line 59) f.loop[cp] = 0;
                _ARRW(f.loop, cp) << (0)
                # (Line 60) }
                # (Line 61) }
            EUDEndIf()
            # (Line 62) else if (f.count[cp] == 1)
        if EUDElseIf()(f.count[cp] == 1):
            # (Line 63) {
            # (Line 64) var i = f.loop[cp];
            i = EUDVariable()
            i << (f.loop[cp])
            # (Line 66) if (f.loop[cp] == 0)
            if EUDIf()(f.loop[cp] == 0):
                # (Line 67) {
                # (Line 68) RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
                # (Line 69) }
                DoActions(RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp))
                # (Line 71) if (f.loop[cp] < 3)
            EUDEndIf()
            if EUDIf()(f.loop[cp] >= 3, neg=True):
                # (Line 72) {
                # (Line 73) f.EdgeShape(cp, 1, "50 + 1n Tank", 45, 3 + 2 * i, 50 + 50 * i);
                f.EdgeShape(cp, 1, "50 + 1n Tank", 45, 3 + 2 * i, 50 + 50 * i)
                # (Line 74) KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
                # (Line 75) }
                DoActions(KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp))
                # (Line 76) else if (f.loop[cp] < 7)
            if EUDElseIf()(f.loop[cp] >= 7, neg=True):
                # (Line 77) {
                # (Line 78) f.EdgeShape(cp, 1, "40 + 1n Wraith", 45, 7 - 2 * (i - 3), 150 - 50 * (i - 3));
                f.EdgeShape(cp, 1, "40 + 1n Wraith", 45, 7 - 2 * (i - 3), 150 - 50 * (i - 3))
                # (Line 79) KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
                # (Line 80) }
                DoActions(KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp))
                # (Line 82) if (f.loop[cp] == 2)
            EUDEndIf()
            if EUDIf()(f.loop[cp] == 2):
                # (Line 83) {
                # (Line 84) f.SquareShape(cp, 1, "60 + 1n Siege", 150, 150);
                f.SquareShape(cp, 1, "60 + 1n Siege", 150, 150)
                # (Line 85) f.SquareShape(cp, 1, "60 + 1n Siege", 75, 150);
                f.SquareShape(cp, 1, "60 + 1n Siege", 75, 150)
                # (Line 86) f.SquareShape(cp, 1, "60 + 1n Siege", 150, 75);
                f.SquareShape(cp, 1, "60 + 1n Siege", 150, 75)
                # (Line 87) }
                # (Line 88) else if (f.loop[cp] == 4)
            if EUDElseIf()(f.loop[cp] == 4):
                # (Line 89) {
                # (Line 90) RemoveUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
                # (Line 91) }
                DoActions(RemoveUnitAt(All, "50 + 1n Tank", "Anywhere", cp))
                # (Line 93) f.SkillWait(cp, 80);
            EUDEndIf()
            f.SkillWait(cp, 80)
            # (Line 95) f.loop[cp] += 1;
            _ARRW(f.loop, cp).__iadd__(1)
            # (Line 97) if (f.loop[cp] == 19)
            if EUDIf()(f.loop[cp] == 19):
                # (Line 98) {
                # (Line 99) KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);
                # (Line 101) f.count[cp] += 1;
                DoActions(KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp))
                _ARRW(f.count, cp).__iadd__(1)
                # (Line 102) f.loop[cp] = 0;
                _ARRW(f.loop, cp) << (0)
                # (Line 103) }
                # (Line 104) }
            EUDEndIf()
            # (Line 105) else if (f.count[cp] == 2)
        if EUDElseIf()(f.count[cp] == 2):
            # (Line 106) {
            # (Line 107) var i = f.loop[cp];
            i = EUDVariable()
            i << (f.loop[cp])
            # (Line 109) if (f.loop[cp] == 0)
            if EUDIf()(f.loop[cp] == 0):
                # (Line 110) {
                # (Line 111) RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
                # (Line 112) }
                DoActions(RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp))
                # (Line 114) if (f.loop[cp] < 3)
            EUDEndIf()
            if EUDIf()(f.loop[cp] >= 3, neg=True):
                # (Line 115) {
                # (Line 116) f.EdgeShape(cp, 1, "Protoss Dark Archon", 0, 3 + 2 * i, 50 + 50 * i);
                f.EdgeShape(cp, 1, "Protoss Dark Archon", 0, 3 + 2 * i, 50 + 50 * i)
                # (Line 117) KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
                # (Line 118) }
                DoActions(KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp))
                # (Line 119) else if (f.loop[cp] < 11)
            if EUDElseIf()(f.loop[cp] >= 11, neg=True):
                # (Line 120) {
                # (Line 121) f.EdgeShape(cp, 1, "40 + 1n Guardian", 0, 5, 100);
                f.EdgeShape(cp, 1, "40 + 1n Guardian", 0, 5, 100)
                # (Line 122) KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
                # (Line 124) f.SquareShape(cp, 1, "60 + 1n High Templar", 120 - 15 * (i - 3), 15 * (i - 3));
                DoActions(KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp))
                f.SquareShape(cp, 1, "60 + 1n High Templar", 120 - 15 * (i - 3), 15 * (i - 3))
                # (Line 125) f.SquareShape(cp, 1, "60 + 1n High Templar", 10 * (i - 3), 80 - 10 * (i - 3));
                f.SquareShape(cp, 1, "60 + 1n High Templar", 10 * (i - 3), 80 - 10 * (i - 3))
                # (Line 126) KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);
                # (Line 127) }
                DoActions(KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp))
                # (Line 129) if (f.loop[cp] == 3)
            EUDEndIf()
            if EUDIf()(f.loop[cp] == 3):
                # (Line 130) {
                # (Line 131) f.EdgeShape(cp, 1, "40 + 1n Marine", 0, 5, 100);
                f.EdgeShape(cp, 1, "40 + 1n Marine", 0, 5, 100)
                # (Line 133) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
                # (Line 134) MoveUnit(All, "40 + 1n Marine", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
                DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
                # (Line 135) Order("40 + 1n Marine", cp, "Anywhere", Attack, f.location[cp]);
                DoActions(MoveUnit(All, "40 + 1n Marine", cp, "[Skill]Unit_Wait_ALL", f.location[cp]))
                # (Line 136) }
                DoActions(Order("40 + 1n Marine", cp, "Anywhere", Attack, f.location[cp]))
                # (Line 137) else if (f.loop[cp] == 11)
            if EUDElseIf()(f.loop[cp] == 11):
                # (Line 138) {
                # (Line 139) KillUnitAt(All, "40 + 1n Marine", "Anywhere", cp);
                # (Line 141) f.EdgeShape(cp, 1, "40 + 1n Wraith", 0, 5, 100);
                DoActions(KillUnitAt(All, "40 + 1n Marine", "Anywhere", cp))
                f.EdgeShape(cp, 1, "40 + 1n Wraith", 0, 5, 100)
                # (Line 142) KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
                # (Line 144) }
                DoActions(KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp))
                # (Line 146) f.SkillWait(cp, 80);
            EUDEndIf()
            f.SkillWait(cp, 80)
            # (Line 148) f.loop[cp] += 1;
            _ARRW(f.loop, cp).__iadd__(1)
            # (Line 150) if (f.loop[cp] == 17)
            if EUDIf()(f.loop[cp] == 17):
                # (Line 151) {
                # (Line 152) KillUnitAt(All, "60 + 1n Siege", "Anywhere", cp);
                # (Line 154) f.count[cp] += 1;
                DoActions(KillUnitAt(All, "60 + 1n Siege", "Anywhere", cp))
                _ARRW(f.count, cp).__iadd__(1)
                # (Line 155) f.loop[cp] = 0;
                _ARRW(f.loop, cp) << (0)
                # (Line 156) }
                # (Line 157) }
            EUDEndIf()
            # (Line 158) else if (f.count[cp] == 3)
        if EUDElseIf()(f.count[cp] == 3):
            # (Line 159) {
            # (Line 160) f.SkillEnd(cp);
            f.SkillEnd(cp)
            # (Line 161) }
            # (Line 162) }
        EUDEndIf()
        # (Line 163) }
    EUDEndIf()