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
    # (Line 7) f.HoldPosition(cp);
    f.HoldPosition(cp)
    # (Line 8) ModifyUnitShields(All, f.heroID[cp], cp, "Anywhere", 1);
    # (Line 10) if (f.delay[cp] == 0)
    DoActions(ModifyUnitShields(All, f.heroID[cp], cp, "Anywhere", 1))
    if EUDIf()(f.delay[cp] == 0):
        # (Line 11) {
        # (Line 12) if (f.count[cp] == 0)
        if EUDIf()(f.count[cp] == 0):
            # (Line 13) {
            # (Line 14) if (f.loop[cp] < 8)
            if EUDIf()(f.loop[cp] >= 8, neg=True):
                # (Line 15) {
                # (Line 16) SetDeaths(cp, SetTo, 1, " `ShieldRecharge");
                # (Line 18) if (f.loop[cp] % 2 == 0)
                DoActions(SetDeaths(cp, SetTo, 1, " `ShieldRecharge"))
                if EUDIf()(f.loop[cp] % 2 == 0):
                    # (Line 19) {
                    # (Line 20) KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", cp);
                    # (Line 21) KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);
                    DoActions(KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", cp))
                    # (Line 23) f.Table_Sin(cp, (45 * f.loop[cp] + 22), 100);
                    DoActions(KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp))
                    f.Table_Sin(cp, (45 * f.loop[cp] + 22), 100)
                    # (Line 24) f.Table_Cos(cp, (45 * f.loop[cp] + 22), 100);
                    f.Table_Cos(cp, (45 * f.loop[cp] + 22), 100)
                    # (Line 26) f.DotShape(cp, 1, "40 + 1n Wraith", f.CosAngle[cp], f.SinAngle[cp]);
                    f.DotShape(cp, 1, "40 + 1n Wraith", f.CosAngle[cp], f.SinAngle[cp])
                    # (Line 27) f.DotShape(cp, 1, "40 + 1n Wraith", -f.CosAngle[cp], -f.SinAngle[cp]);
                    f.DotShape(cp, 1, "40 + 1n Wraith", -f.CosAngle[cp], -f.SinAngle[cp])
                    # (Line 28) f.DotShape(cp, 1, "40 + 1n Zealot", f.CosAngle[cp], f.SinAngle[cp]);
                    f.DotShape(cp, 1, "40 + 1n Zealot", f.CosAngle[cp], f.SinAngle[cp])
                    # (Line 29) f.DotShape(cp, 1, "40 + 1n Zealot", -f.CosAngle[cp], -f.SinAngle[cp]);
                    f.DotShape(cp, 1, "40 + 1n Zealot", -f.CosAngle[cp], -f.SinAngle[cp])
                    # (Line 30) f.DotShape(cp, 1, "Target", -f.SinAngle[cp], f.CosAngle[cp]);
                    f.DotShape(cp, 1, "Target", -f.SinAngle[cp], f.CosAngle[cp])
                    # (Line 31) f.DotShape(cp, 1, "Target", f.SinAngle[cp], -f.CosAngle[cp]);
                    f.DotShape(cp, 1, "Target", f.SinAngle[cp], -f.CosAngle[cp])
                    # (Line 32) f.DotShape(cp, 1, " Creep. Dunkelheit", -f.SinAngle[cp], f.CosAngle[cp]);
                    f.DotShape(cp, 1, " Creep. Dunkelheit", -f.SinAngle[cp], f.CosAngle[cp])
                    # (Line 33) f.DotShape(cp, 1, " Creep. Dunkelheit", f.SinAngle[cp], -f.CosAngle[cp]);
                    f.DotShape(cp, 1, " Creep. Dunkelheit", f.SinAngle[cp], -f.CosAngle[cp])
                    # (Line 35) f.EdgeShape(cp, 1, "60 + 1n High Templar", 0, 7, 150);
                    f.EdgeShape(cp, 1, "60 + 1n High Templar", 0, 7, 150)
                    # (Line 36) KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);
                    # (Line 38) f.Table_Sin(cp, (22 * f.loop[cp] + 22), 50 * (f.loop[cp] / 2) + 50);
                    DoActions(KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp))
                    f.Table_Sin(cp, (22 * f.loop[cp] + 22), 50 * (f.loop[cp] // 2) + 50)
                    # (Line 39) f.Table_Cos(cp, (22 * f.loop[cp] + 22), 50 * (f.loop[cp] / 2) + 50);
                    f.Table_Cos(cp, (22 * f.loop[cp] + 22), 50 * (f.loop[cp] // 2) + 50)
                    # (Line 41) f.SquareShape(cp, 1, "60 + 1n Siege", f.CosAngle[cp], f.SinAngle[cp]);
                    f.SquareShape(cp, 1, "60 + 1n Siege", f.CosAngle[cp], f.SinAngle[cp])
                    # (Line 42) f.SquareShape(cp, 1, "40 + 1n Gantrithor", f.CosAngle[cp], f.SinAngle[cp]);
                    f.SquareShape(cp, 1, "40 + 1n Gantrithor", f.CosAngle[cp], f.SinAngle[cp])
                    # (Line 44) KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);
                    # (Line 45) KillUnitAt(All, "40 + 1n Zealot", "Anywhere", cp);
                    DoActions(KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp))
                    # (Line 46) KillUnitAt(All, "Target", "Anywhere", cp);
                    DoActions(KillUnitAt(All, "40 + 1n Zealot", "Anywhere", cp))
                    # (Line 48) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
                    DoActions(KillUnitAt(All, "Target", "Anywhere", cp))
                    # (Line 49) MoveUnit(All, " Creep. Dunkelheit", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
                    DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
                    # (Line 50) Order(" Creep. Dunkelheit", cp, "Anywhere", Attack, f.location[cp]);
                    DoActions(MoveUnit(All, " Creep. Dunkelheit", cp, "[Skill]Unit_Wait_ALL", f.location[cp]))
                    # (Line 51) Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);
                    DoActions(Order(" Creep. Dunkelheit", cp, "Anywhere", Attack, f.location[cp]))
                    # (Line 53) }
                    DoActions(Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]))
                    # (Line 54) else
                    # (Line 55) {
                if EUDElse()():
                    # (Line 56) KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", cp);
                    # (Line 57) KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
                    DoActions(KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", cp))
                    # (Line 59) f.Table_Sin(cp, (45 * f.loop[cp] + 112), 100);
                    DoActions(KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp))
                    f.Table_Sin(cp, (45 * f.loop[cp] + 112), 100)
                    # (Line 60) f.Table_Cos(cp, (45 * f.loop[cp] + 112), 100);
                    f.Table_Cos(cp, (45 * f.loop[cp] + 112), 100)
                    # (Line 62) f.DotShape(cp, 1, "40 + 1n Mojo", f.CosAngle[cp], f.SinAngle[cp]);
                    f.DotShape(cp, 1, "40 + 1n Mojo", f.CosAngle[cp], f.SinAngle[cp])
                    # (Line 63) f.DotShape(cp, 1, "40 + 1n Mojo", -f.CosAngle[cp], -f.SinAngle[cp]);
                    f.DotShape(cp, 1, "40 + 1n Mojo", -f.CosAngle[cp], -f.SinAngle[cp])
                    # (Line 64) f.DotShape(cp, 1, "Protoss Dark Archon", f.CosAngle[cp], f.SinAngle[cp]);
                    f.DotShape(cp, 1, "Protoss Dark Archon", f.CosAngle[cp], f.SinAngle[cp])
                    # (Line 65) f.DotShape(cp, 1, "Protoss Dark Archon", -f.CosAngle[cp], -f.SinAngle[cp]);
                    f.DotShape(cp, 1, "Protoss Dark Archon", -f.CosAngle[cp], -f.SinAngle[cp])
                    # (Line 66) f.DotShape(cp, 1, "Target", -f.SinAngle[cp], f.CosAngle[cp]);
                    f.DotShape(cp, 1, "Target", -f.SinAngle[cp], f.CosAngle[cp])
                    # (Line 67) f.DotShape(cp, 1, "Target", f.SinAngle[cp], -f.CosAngle[cp]);
                    f.DotShape(cp, 1, "Target", f.SinAngle[cp], -f.CosAngle[cp])
                    # (Line 68) f.DotShape(cp, 1, " Creep. Dunkelheit", -f.SinAngle[cp], f.CosAngle[cp]);
                    f.DotShape(cp, 1, " Creep. Dunkelheit", -f.SinAngle[cp], f.CosAngle[cp])
                    # (Line 69) f.DotShape(cp, 1, " Creep. Dunkelheit", f.SinAngle[cp], -f.CosAngle[cp]);
                    f.DotShape(cp, 1, " Creep. Dunkelheit", f.SinAngle[cp], -f.CosAngle[cp])
                    # (Line 71) f.EdgeShape(cp, 1, "60 + 1n High Templar", 45, 7, 150);
                    f.EdgeShape(cp, 1, "60 + 1n High Templar", 45, 7, 150)
                    # (Line 72) KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);
                    # (Line 74) KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
                    DoActions(KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp))
                    # (Line 75) KillUnitAt(All, "Target", "Anywhere", cp);
                    DoActions(KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp))
                    # (Line 77) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
                    DoActions(KillUnitAt(All, "Target", "Anywhere", cp))
                    # (Line 78) MoveUnit(All, " Creep. Dunkelheit", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
                    DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
                    # (Line 79) Order(" Creep. Dunkelheit", cp, "Anywhere", Attack, f.location[cp]);
                    DoActions(MoveUnit(All, " Creep. Dunkelheit", cp, "[Skill]Unit_Wait_ALL", f.location[cp]))
                    # (Line 80) Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);
                    DoActions(Order(" Creep. Dunkelheit", cp, "Anywhere", Attack, f.location[cp]))
                    # (Line 81) }
                    DoActions(Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]))
                    # (Line 83) f.SkillWait(cp, 240);
                EUDEndIf()
                f.SkillWait(cp, 240)
                # (Line 85) f.loop[cp] += 1;
                _ARRW(f.loop, cp).__iadd__(1)
                # (Line 86) }
                # (Line 87) else if (f.loop[cp] < 16)
            if EUDElseIf()(f.loop[cp] >= 16, neg=True):
                # (Line 88) {
                # (Line 89) if (f.loop[cp] % 2 == 0)
                if EUDIf()(f.loop[cp] % 2 == 0):
                    # (Line 90) {
                    # (Line 91) KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", cp);
                    # (Line 92) KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);
                    DoActions(KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", cp))
                    # (Line 94) f.Table_Sin(cp, (45 * f.loop[cp] + 22), 100);
                    DoActions(KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp))
                    f.Table_Sin(cp, (45 * f.loop[cp] + 22), 100)
                    # (Line 95) f.Table_Cos(cp, (45 * f.loop[cp] + 22), 100);
                    f.Table_Cos(cp, (45 * f.loop[cp] + 22), 100)
                    # (Line 97) f.DotShape(cp, 1, "40 + 1n Wraith", f.CosAngle[cp], f.SinAngle[cp]);
                    f.DotShape(cp, 1, "40 + 1n Wraith", f.CosAngle[cp], f.SinAngle[cp])
                    # (Line 98) f.DotShape(cp, 1, "40 + 1n Wraith", -f.CosAngle[cp], -f.SinAngle[cp]);
                    f.DotShape(cp, 1, "40 + 1n Wraith", -f.CosAngle[cp], -f.SinAngle[cp])
                    # (Line 99) f.DotShape(cp, 1, "40 + 1n Zealot", f.CosAngle[cp], f.SinAngle[cp]);
                    f.DotShape(cp, 1, "40 + 1n Zealot", f.CosAngle[cp], f.SinAngle[cp])
                    # (Line 100) f.DotShape(cp, 1, "40 + 1n Zealot", -f.CosAngle[cp], -f.SinAngle[cp]);
                    f.DotShape(cp, 1, "40 + 1n Zealot", -f.CosAngle[cp], -f.SinAngle[cp])
                    # (Line 101) f.DotShape(cp, 1, "Target", -f.SinAngle[cp], f.CosAngle[cp]);
                    f.DotShape(cp, 1, "Target", -f.SinAngle[cp], f.CosAngle[cp])
                    # (Line 102) f.DotShape(cp, 1, "Target", f.SinAngle[cp], -f.CosAngle[cp]);
                    f.DotShape(cp, 1, "Target", f.SinAngle[cp], -f.CosAngle[cp])
                    # (Line 103) f.DotShape(cp, 1, " Creep. Dunkelheit", -f.SinAngle[cp], f.CosAngle[cp]);
                    f.DotShape(cp, 1, " Creep. Dunkelheit", -f.SinAngle[cp], f.CosAngle[cp])
                    # (Line 104) f.DotShape(cp, 1, " Creep. Dunkelheit", f.SinAngle[cp], -f.CosAngle[cp]);
                    f.DotShape(cp, 1, " Creep. Dunkelheit", f.SinAngle[cp], -f.CosAngle[cp])
                    # (Line 106) f.EdgeShape(cp, 1, "60 + 1n High Templar", 0, 7, 150);
                    f.EdgeShape(cp, 1, "60 + 1n High Templar", 0, 7, 150)
                    # (Line 107) KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);
                    # (Line 109) f.Table_Sin(cp, (22 * f.loop[cp] + 112), 50 * (f.loop[cp] / 2 - 4) + 50);
                    DoActions(KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp))
                    f.Table_Sin(cp, (22 * f.loop[cp] + 112), 50 * (f.loop[cp] // 2 - 4) + 50)
                    # (Line 110) f.Table_Cos(cp, (22 * f.loop[cp] + 112), 50 * (f.loop[cp] / 2 - 4) + 50);
                    f.Table_Cos(cp, (22 * f.loop[cp] + 112), 50 * (f.loop[cp] // 2 - 4) + 50)
                    # (Line 112) f.SquareShape(cp, 1, "60 + 1n Siege", f.CosAngle[cp], f.SinAngle[cp]);
                    f.SquareShape(cp, 1, "60 + 1n Siege", f.CosAngle[cp], f.SinAngle[cp])
                    # (Line 113) f.SquareShape(cp, 1, "40 + 1n Gantrithor", f.CosAngle[cp], f.SinAngle[cp]);
                    f.SquareShape(cp, 1, "40 + 1n Gantrithor", f.CosAngle[cp], f.SinAngle[cp])
                    # (Line 115) KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);
                    # (Line 116) KillUnitAt(All, "40 + 1n Zealot", "Anywhere", cp);
                    DoActions(KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp))
                    # (Line 117) KillUnitAt(All, "Target", "Anywhere", cp);
                    DoActions(KillUnitAt(All, "40 + 1n Zealot", "Anywhere", cp))
                    # (Line 119) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
                    DoActions(KillUnitAt(All, "Target", "Anywhere", cp))
                    # (Line 120) MoveUnit(All, " Creep. Dunkelheit", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
                    DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
                    # (Line 121) Order(" Creep. Dunkelheit", cp, "Anywhere", Attack, f.location[cp]);
                    DoActions(MoveUnit(All, " Creep. Dunkelheit", cp, "[Skill]Unit_Wait_ALL", f.location[cp]))
                    # (Line 122) Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);
                    DoActions(Order(" Creep. Dunkelheit", cp, "Anywhere", Attack, f.location[cp]))
                    # (Line 123) }
                    DoActions(Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]))
                    # (Line 124) else
                    # (Line 125) {
                if EUDElse()():
                    # (Line 126) KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", cp);
                    # (Line 127) KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
                    DoActions(KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", cp))
                    # (Line 129) f.Table_Sin(cp, (45 * f.loop[cp] + 112), 100);
                    DoActions(KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp))
                    f.Table_Sin(cp, (45 * f.loop[cp] + 112), 100)
                    # (Line 130) f.Table_Cos(cp, (45 * f.loop[cp] + 112), 100);
                    f.Table_Cos(cp, (45 * f.loop[cp] + 112), 100)
                    # (Line 132) f.DotShape(cp, 1, "40 + 1n Mojo", f.CosAngle[cp], f.SinAngle[cp]);
                    f.DotShape(cp, 1, "40 + 1n Mojo", f.CosAngle[cp], f.SinAngle[cp])
                    # (Line 133) f.DotShape(cp, 1, "40 + 1n Mojo", -f.CosAngle[cp], -f.SinAngle[cp]);
                    f.DotShape(cp, 1, "40 + 1n Mojo", -f.CosAngle[cp], -f.SinAngle[cp])
                    # (Line 134) f.DotShape(cp, 1, "Protoss Dark Archon", f.CosAngle[cp], f.SinAngle[cp]);
                    f.DotShape(cp, 1, "Protoss Dark Archon", f.CosAngle[cp], f.SinAngle[cp])
                    # (Line 135) f.DotShape(cp, 1, "Protoss Dark Archon", -f.CosAngle[cp], -f.SinAngle[cp]);
                    f.DotShape(cp, 1, "Protoss Dark Archon", -f.CosAngle[cp], -f.SinAngle[cp])
                    # (Line 136) f.DotShape(cp, 1, "Target", -f.SinAngle[cp], f.CosAngle[cp]);
                    f.DotShape(cp, 1, "Target", -f.SinAngle[cp], f.CosAngle[cp])
                    # (Line 137) f.DotShape(cp, 1, "Target", f.SinAngle[cp], -f.CosAngle[cp]);
                    f.DotShape(cp, 1, "Target", f.SinAngle[cp], -f.CosAngle[cp])
                    # (Line 138) f.DotShape(cp, 1, " Creep. Dunkelheit", -f.SinAngle[cp], f.CosAngle[cp]);
                    f.DotShape(cp, 1, " Creep. Dunkelheit", -f.SinAngle[cp], f.CosAngle[cp])
                    # (Line 139) f.DotShape(cp, 1, " Creep. Dunkelheit", f.SinAngle[cp], -f.CosAngle[cp]);
                    f.DotShape(cp, 1, " Creep. Dunkelheit", f.SinAngle[cp], -f.CosAngle[cp])
                    # (Line 141) f.EdgeShape(cp, 1, "60 + 1n High Templar", 45, 7, 150);
                    f.EdgeShape(cp, 1, "60 + 1n High Templar", 45, 7, 150)
                    # (Line 142) KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);
                    # (Line 144) KillUnitAt(All, "Target", "Anywhere", cp);
                    DoActions(KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp))
                    # (Line 145) KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
                    DoActions(KillUnitAt(All, "Target", "Anywhere", cp))
                    # (Line 147) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
                    DoActions(KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp))
                    # (Line 148) MoveUnit(All, " Creep. Dunkelheit", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
                    DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
                    # (Line 149) Order(" Creep. Dunkelheit", cp, "Anywhere", Attack, f.location[cp]);
                    DoActions(MoveUnit(All, " Creep. Dunkelheit", cp, "[Skill]Unit_Wait_ALL", f.location[cp]))
                    # (Line 150) Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);
                    DoActions(Order(" Creep. Dunkelheit", cp, "Anywhere", Attack, f.location[cp]))
                    # (Line 151) }
                    DoActions(Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]))
                    # (Line 153) f.SkillWait(cp, 240);
                EUDEndIf()
                f.SkillWait(cp, 240)
                # (Line 155) f.loop[cp] += 1;
                _ARRW(f.loop, cp).__iadd__(1)
                # (Line 156) }
                # (Line 157) else if (f.loop[cp] == 16)
            if EUDElseIf()(f.loop[cp] == 16):
                # (Line 158) {
                # (Line 159) KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);
                # (Line 160) KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", cp);
                DoActions(KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp))
                # (Line 162) f.Voice_Routine(cp, 9);
                DoActions(KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", cp))
                f.Voice_Routine(cp, 9)
                # (Line 164) f.SkillWait(cp, 80);
                f.SkillWait(cp, 80)
                # (Line 166) f.count[cp] += 1;
                _ARRW(f.count, cp).__iadd__(1)
                # (Line 167) f.loop[cp] = 0;
                _ARRW(f.loop, cp) << (0)
                # (Line 168) }
                # (Line 169) }
            EUDEndIf()
            # (Line 170) else if (f.count[cp] == 1)
        if EUDElseIf()(f.count[cp] == 1):
            # (Line 171) {
            # (Line 172) if (f.loop[cp] == 0)
            if EUDIf()(f.loop[cp] == 0):
                # (Line 173) {
                # (Line 174) f.EdgeShape(cp, 1, " Unit. Hoffnung 25000", 0, 5, 150);
                f.EdgeShape(cp, 1, " Unit. Hoffnung 25000", 0, 5, 150)
                # (Line 175) f.EdgeShape(cp, 1, " Unit. Hoffnung 25000", 45, 5, 150);
                f.EdgeShape(cp, 1, " Unit. Hoffnung 25000", 45, 5, 150)
                # (Line 176) KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
                # (Line 178) f.SkillWait(cp, 960);
                DoActions(KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp))
                f.SkillWait(cp, 960)
                # (Line 179) f.loop[cp] += 1;
                _ARRW(f.loop, cp).__iadd__(1)
                # (Line 180) }
                # (Line 181) else if (f.loop[cp] < 5)
            if EUDElseIf()(f.loop[cp] >= 5, neg=True):
                # (Line 182) {
                # (Line 183) if (f.loop[cp] % 2 == 1)
                if EUDIf()(f.loop[cp] % 2 == 1):
                    # (Line 184) {
                    # (Line 185) f.EdgeShape(cp, 1, " Creep. Dunkelheit", 0, 4, 100);
                    f.EdgeShape(cp, 1, " Creep. Dunkelheit", 0, 4, 100)
                    # (Line 186) f.EdgeShape(cp, 1, " Creep. Dunkelheit", 0, 2, 50);
                    f.EdgeShape(cp, 1, " Creep. Dunkelheit", 0, 2, 50)
                    # (Line 188) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
                    # (Line 189) Order(" Creep. Dunkelheit", cp, "Anywhere", Attack, f.location[cp]);
                    DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
                    # (Line 190) }
                    DoActions(Order(" Creep. Dunkelheit", cp, "Anywhere", Attack, f.location[cp]))
                    # (Line 191) else
                    # (Line 192) {
                if EUDElse()():
                    # (Line 193) KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", cp);
                    # (Line 194) }
                    DoActions(KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", cp))
                    # (Line 196) f.SkillWait(cp, 160);
                EUDEndIf()
                f.SkillWait(cp, 160)
                # (Line 198) f.loop[cp] += 1;
                _ARRW(f.loop, cp).__iadd__(1)
                # (Line 199) }
                # (Line 200) else if (f.loop[cp] == 5)
            if EUDElseIf()(f.loop[cp] == 5):
                # (Line 201) {
                # (Line 202) f.EdgeShape(cp, 1, " Unit. Hoffnung 25000", 0, 5, 150);
                f.EdgeShape(cp, 1, " Unit. Hoffnung 25000", 0, 5, 150)
                # (Line 203) f.EdgeShape(cp, 1, " Unit. Hoffnung 25000", 45, 5, 150);
                f.EdgeShape(cp, 1, " Unit. Hoffnung 25000", 45, 5, 150)
                # (Line 204) KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
                # (Line 206) f.SkillWait(cp, 480);
                DoActions(KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp))
                f.SkillWait(cp, 480)
                # (Line 208) f.count[cp] += 1;
                _ARRW(f.count, cp).__iadd__(1)
                # (Line 209) f.loop[cp] = 0;
                _ARRW(f.loop, cp) << (0)
                # (Line 210) }
                # (Line 211) }
            EUDEndIf()
            # (Line 212) else if (f.count[cp] == 2)
        if EUDElseIf()(f.count[cp] == 2):
            # (Line 213) {
            # (Line 214) SetDeaths(cp, SetTo, 0, " `ShieldRecharge");
            # (Line 215) KillUnitAt(All, "60 + 1n Siege", "Anywhere", cp);
            DoActions(SetDeaths(cp, SetTo, 0, " `ShieldRecharge"))
            # (Line 216) f.SkillEnd(cp);
            DoActions(KillUnitAt(All, "60 + 1n Siege", "Anywhere", cp))
            f.SkillEnd(cp)
            # (Line 217) }
            # (Line 218) }
        EUDEndIf()
        # (Line 219) }
    EUDEndIf()