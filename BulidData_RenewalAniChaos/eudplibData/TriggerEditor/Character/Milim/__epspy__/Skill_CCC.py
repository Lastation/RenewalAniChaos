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
# (Line 4) const s = StringBuffer();
s = _CGFW(lambda: [StringBuffer()], 1)[0]
# (Line 6) function main(cp)
# (Line 7) {
@EUDFunc
def f_main(cp):
    # (Line 8) if (Switch("Unique - Milim", Cleared))
    if EUDIf()(Switch("Unique - Milim", Cleared)):
        # (Line 9) {
        # (Line 10) f.HoldPosition(cp);
        f.HoldPosition(cp)
        # (Line 11) }
        # (Line 12) f.BanReturn(cp);
    EUDEndIf()
    f.BanReturn(cp)
    # (Line 14) if (f.delay[cp] == 0)
    if EUDIf()(f.delay[cp] == 0):
        # (Line 15) {
        # (Line 16) if (f.count[cp] == 0)
        if EUDIf()(f.count[cp] == 0):
            # (Line 17) {
            # (Line 18) if (f.loop[cp] == 0)
            if EUDIf()(f.loop[cp] == 0):
                # (Line 19) {
                # (Line 20) var x = 75;
                x = EUDVariable()
                x << (75)
                # (Line 21) var y = 125;
                y = EUDVariable()
                y << (125)
                # (Line 23) f.SquareShape(cp, 1, "40 + 1n Mojo", x, y);
                f.SquareShape(cp, 1, "40 + 1n Mojo", x, y)
                # (Line 24) f.SquareShape(cp, 1, "40 + 1n Mojo", y, x);
                f.SquareShape(cp, 1, "40 + 1n Mojo", y, x)
                # (Line 25) f.SquareShape(cp, 1, " Unit. Hoffnung 25000", x, y);
                f.SquareShape(cp, 1, " Unit. Hoffnung 25000", x, y)
                # (Line 26) f.SquareShape(cp, 1, " Unit. Hoffnung 25000", y, x);
                f.SquareShape(cp, 1, " Unit. Hoffnung 25000", y, x)
                # (Line 27) KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
                # (Line 29) f.EdgeShape(cp, 1, "Target", 45, 5, 100);
                DoActions(KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp))
                f.EdgeShape(cp, 1, "Target", 45, 5, 100)
                # (Line 30) KillUnitAt(All, "Target", "Anywhere", cp);
                # (Line 32) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
                DoActions(KillUnitAt(All, "Target", "Anywhere", cp))
                # (Line 33) Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);
                DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
                # (Line 35) f.SkillWait(cp, 80);
                DoActions(Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]))
                f.SkillWait(cp, 80)
                # (Line 37) f.loop[cp] += 1;
                _ARRW(f.loop, cp).__iadd__(1)
                # (Line 38) }
                # (Line 39) else if (f.loop[cp] == 1)
            if EUDElseIf()(f.loop[cp] == 1):
                # (Line 40) {
                # (Line 41) KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);
                # (Line 43) var x = 125;
                DoActions(KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp))
                x = EUDVariable()
                x << (125)
                # (Line 44) var y = 175;
                y = EUDVariable()
                y << (175)
                # (Line 46) f.SquareShape(cp, 1, "40 + 1n Mojo", x, y);
                f.SquareShape(cp, 1, "40 + 1n Mojo", x, y)
                # (Line 47) f.SquareShape(cp, 1, "40 + 1n Mojo", y, x);
                f.SquareShape(cp, 1, "40 + 1n Mojo", y, x)
                # (Line 48) f.SquareShape(cp, 1, " Unit. Hoffnung 25000", x, y);
                f.SquareShape(cp, 1, " Unit. Hoffnung 25000", x, y)
                # (Line 49) f.SquareShape(cp, 1, " Unit. Hoffnung 25000", y, x);
                f.SquareShape(cp, 1, " Unit. Hoffnung 25000", y, x)
                # (Line 50) KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
                # (Line 52) f.EdgeShape(cp, 1, "Target", 0, 5, 100);
                DoActions(KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp))
                f.EdgeShape(cp, 1, "Target", 0, 5, 100)
                # (Line 53) KillUnitAt(All, "Target", "Anywhere", cp);
                # (Line 55) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
                DoActions(KillUnitAt(All, "Target", "Anywhere", cp))
                # (Line 56) Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);
                DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
                # (Line 58) f.SkillWait(cp, 80);
                DoActions(Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]))
                f.SkillWait(cp, 80)
                # (Line 60) f.loop[cp] += 1;
                _ARRW(f.loop, cp).__iadd__(1)
                # (Line 61) }
                # (Line 62) else if (f.loop[cp] == 2)
            if EUDElseIf()(f.loop[cp] == 2):
                # (Line 63) {
                # (Line 64) KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);
                # (Line 66) var x = 75;
                DoActions(KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp))
                x = EUDVariable()
                x << (75)
                # (Line 67) var y = 125;
                y = EUDVariable()
                y << (125)
                # (Line 69) f.SquareShape(cp, 1, "Kakaru (Twilight)", x, y);
                f.SquareShape(cp, 1, "Kakaru (Twilight)", x, y)
                # (Line 70) f.SquareShape(cp, 1, "Kakaru (Twilight)", y, x);
                f.SquareShape(cp, 1, "Kakaru (Twilight)", y, x)
                # (Line 72) KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
                # (Line 74) x = 125;
                DoActions(KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp))
                x << (125)
                # (Line 75) y = 175;
                y << (175)
                # (Line 77) f.SquareShape(cp, 1, "Kakaru (Twilight)", x, y);
                f.SquareShape(cp, 1, "Kakaru (Twilight)", x, y)
                # (Line 78) f.SquareShape(cp, 1, "Kakaru (Twilight)", y, x);
                f.SquareShape(cp, 1, "Kakaru (Twilight)", y, x)
                # (Line 80) f.EdgeShape(cp, 1, "40 + 1n Wraith", 0, 5, 100);
                f.EdgeShape(cp, 1, "40 + 1n Wraith", 0, 5, 100)
                # (Line 81) f.EdgeShape(cp, 1, "40 + 1n Firebat", 0, 3, 100);
                f.EdgeShape(cp, 1, "40 + 1n Firebat", 0, 3, 100)
                # (Line 83) KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
                # (Line 84) KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
                DoActions(KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp))
                # (Line 86) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
                DoActions(KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp))
                # (Line 87) MoveUnit(All, "40 + 1n Firebat", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
                DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
                # (Line 88) Order("40 + 1n Firebat", cp, "Anywhere", Attack, f.location[cp]);
                DoActions(MoveUnit(All, "40 + 1n Firebat", cp, "[Skill]Unit_Wait_ALL", f.location[cp]))
                # (Line 90) f.SkillWait(cp, 80);
                DoActions(Order("40 + 1n Firebat", cp, "Anywhere", Attack, f.location[cp]))
                f.SkillWait(cp, 80)
                # (Line 92) f.loop[cp] += 1;
                _ARRW(f.loop, cp).__iadd__(1)
                # (Line 93) }
                # (Line 94) else if (f.loop[cp] < 7)
            if EUDElseIf()(f.loop[cp] >= 7, neg=True):
                # (Line 95) {
                # (Line 96) KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);
                # (Line 98) f.LineShape(cp, 1, "40 + 1n Mojo", 45 * (f.loop[cp] % 4), 5, 64, 0);
                DoActions(KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp))
                f.LineShape(cp, 1, "40 + 1n Mojo", 45 * (f.loop[cp] % 4), 5, 64, 0)
                # (Line 99) f.LineShape(cp, 1, "Protoss Dark Archon", 45 * (f.loop[cp] % 4), 5, 64, 0);
                f.LineShape(cp, 1, "Protoss Dark Archon", 45 * (f.loop[cp] % 4), 5, 64, 0)
                # (Line 100) KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
                # (Line 102) Order("40 + 1n Mojo", cp, "Anywhere", Attack, "Anywhere");
                DoActions(KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp))
                # (Line 104) f.SkillWait(cp, 240);
                DoActions(Order("40 + 1n Mojo", cp, "Anywhere", Attack, "Anywhere"))
                f.SkillWait(cp, 240)
                # (Line 106) f.loop[cp] += 1;
                _ARRW(f.loop, cp).__iadd__(1)
                # (Line 107) }
                # (Line 108) else if (f.loop[cp] == 7)
            if EUDElseIf()(f.loop[cp] == 7):
                # (Line 109) {
                # (Line 110) KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);
                # (Line 112) f.SkillWait(cp, 320);
                DoActions(KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp))
                f.SkillWait(cp, 320)
                # (Line 114) f.count[cp] += 1;
                _ARRW(f.count, cp).__iadd__(1)
                # (Line 115) f.loop[cp] = 0;
                _ARRW(f.loop, cp) << (0)
                # (Line 116) }
                # (Line 117) }
            EUDEndIf()
            # (Line 118) else if (f.count[cp] == 1)
        if EUDElseIf()(f.count[cp] == 1):
            # (Line 119) {
            # (Line 120) if (f.loop[cp] == 0)
            if EUDIf()(f.loop[cp] == 0):
                # (Line 121) {
                # (Line 122) f.Table_Sin(cp, 22, 75);
                f.Table_Sin(cp, 22, 75)
                # (Line 123) f.Table_Cos(cp, 22, 75);
                f.Table_Cos(cp, 22, 75)
                # (Line 125) f.SquareShape(cp, 1, "50 + 1n Battlecruiser", f.CosAngle[cp], f.SinAngle[cp]);
                f.SquareShape(cp, 1, "50 + 1n Battlecruiser", f.CosAngle[cp], f.SinAngle[cp])
                # (Line 126) f.SquareShape(cp, 1, "60 + 1n Archon", f.CosAngle[cp], f.SinAngle[cp]);
                f.SquareShape(cp, 1, "60 + 1n Archon", f.CosAngle[cp], f.SinAngle[cp])
                # (Line 127) KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
                # (Line 129) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
                DoActions(KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp))
                # (Line 130) MoveUnit(All, "50 + 1n Tank", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
                DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
                # (Line 131) Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, f.location[cp]);
                DoActions(MoveUnit(All, "50 + 1n Tank", cp, "[Skill]Unit_Wait_ALL", f.location[cp]))
                # (Line 133) f.SkillWait(cp, 160);
                DoActions(Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, f.location[cp]))
                f.SkillWait(cp, 160)
                # (Line 135) f.loop[cp] += 1;
                _ARRW(f.loop, cp).__iadd__(1)
                # (Line 136) }
                # (Line 137) else if (f.loop[cp] == 1)
            if EUDElseIf()(f.loop[cp] == 1):
                # (Line 138) {
                # (Line 139) f.Table_Sin(cp, 67, 125);
                f.Table_Sin(cp, 67, 125)
                # (Line 140) f.Table_Cos(cp, 67, 125);
                f.Table_Cos(cp, 67, 125)
                # (Line 142) f.SquareShape(cp, 1, "40 + 1n Gantrithor", f.CosAngle[cp], f.SinAngle[cp]);
                f.SquareShape(cp, 1, "40 + 1n Gantrithor", f.CosAngle[cp], f.SinAngle[cp])
                # (Line 143) f.SquareShape(cp, 1, "50 + 1n Tank", f.CosAngle[cp], f.SinAngle[cp]);
                f.SquareShape(cp, 1, "50 + 1n Tank", f.CosAngle[cp], f.SinAngle[cp])
                # (Line 144) KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);
                # (Line 146) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
                DoActions(KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp))
                # (Line 147) MoveUnit(All, "50 + 1n Tank", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
                DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
                # (Line 148) Order("50 + 1n Tank", cp, "Anywhere", Attack, f.location[cp]);
                DoActions(MoveUnit(All, "50 + 1n Tank", cp, "[Skill]Unit_Wait_ALL", f.location[cp]))
                # (Line 150) f.SkillWait(cp, 160);
                DoActions(Order("50 + 1n Tank", cp, "Anywhere", Attack, f.location[cp]))
                f.SkillWait(cp, 160)
                # (Line 152) f.loop[cp] += 1;
                _ARRW(f.loop, cp).__iadd__(1)
                # (Line 153) }
                # (Line 154) else if (f.loop[cp] == 2)
            if EUDElseIf()(f.loop[cp] == 2):
                # (Line 155) {
                # (Line 156) f.Table_Sin(cp, 22, 175);
                f.Table_Sin(cp, 22, 175)
                # (Line 157) f.Table_Cos(cp, 22, 175);
                f.Table_Cos(cp, 22, 175)
                # (Line 159) f.SquareShape(cp, 1, "50 + 1n Battlecruiser", f.CosAngle[cp], f.SinAngle[cp]);
                f.SquareShape(cp, 1, "50 + 1n Battlecruiser", f.CosAngle[cp], f.SinAngle[cp])
                # (Line 160) f.SquareShape(cp, 1, "60 + 1n Archon", f.CosAngle[cp], f.SinAngle[cp]);
                f.SquareShape(cp, 1, "60 + 1n Archon", f.CosAngle[cp], f.SinAngle[cp])
                # (Line 161) KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
                # (Line 163) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
                DoActions(KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp))
                # (Line 164) MoveUnit(All, "50 + 1n Tank", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
                DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
                # (Line 165) Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, f.location[cp]);
                DoActions(MoveUnit(All, "50 + 1n Tank", cp, "[Skill]Unit_Wait_ALL", f.location[cp]))
                # (Line 167) f.SkillWait(cp, 160);
                DoActions(Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, f.location[cp]))
                f.SkillWait(cp, 160)
                # (Line 169) f.loop[cp] += 1;
                _ARRW(f.loop, cp).__iadd__(1)
                # (Line 170) }
                # (Line 171) else if (f.loop[cp] == 3)
            if EUDElseIf()(f.loop[cp] == 3):
                # (Line 172) {
                # (Line 173) f.Table_Sin(cp, 67, 225);
                f.Table_Sin(cp, 67, 225)
                # (Line 174) f.Table_Cos(cp, 67, 225);
                f.Table_Cos(cp, 67, 225)
                # (Line 176) f.SquareShape(cp, 1, "40 + 1n Gantrithor", f.CosAngle[cp], f.SinAngle[cp]);
                f.SquareShape(cp, 1, "40 + 1n Gantrithor", f.CosAngle[cp], f.SinAngle[cp])
                # (Line 177) f.SquareShape(cp, 1, "50 + 1n Tank", f.CosAngle[cp], f.SinAngle[cp]);
                f.SquareShape(cp, 1, "50 + 1n Tank", f.CosAngle[cp], f.SinAngle[cp])
                # (Line 178) KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);
                # (Line 180) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
                DoActions(KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp))
                # (Line 181) MoveUnit(All, "50 + 1n Tank", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
                DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
                # (Line 182) Order("50 + 1n Tank", cp, "Anywhere", Attack, f.location[cp]);
                DoActions(MoveUnit(All, "50 + 1n Tank", cp, "[Skill]Unit_Wait_ALL", f.location[cp]))
                # (Line 185) f.SkillWait(cp, 160);
                DoActions(Order("50 + 1n Tank", cp, "Anywhere", Attack, f.location[cp]))
                f.SkillWait(cp, 160)
                # (Line 187) f.loop[cp] += 1;
                _ARRW(f.loop, cp).__iadd__(1)
                # (Line 188) }
                # (Line 189) else if (f.loop[cp] == 4)
            if EUDElseIf()(f.loop[cp] == 4):
                # (Line 190) {
                # (Line 191) f.SkillWait(cp, 480);
                f.SkillWait(cp, 480)
                # (Line 193) f.count[cp] += 1;
                _ARRW(f.count, cp).__iadd__(1)
                # (Line 194) f.loop[cp] = 0;
                _ARRW(f.loop, cp) << (0)
                # (Line 195) }
                # (Line 196) }
            EUDEndIf()
            # (Line 197) else if (f.count[cp] == 2)
        if EUDElseIf()(f.count[cp] == 2):
            # (Line 198) {
            # (Line 199) if (f.loop[cp] < 4)
            if EUDIf()(f.loop[cp] >= 4, neg=True):
                # (Line 200) {
                # (Line 201) KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
                # (Line 203) RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
                DoActions(KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp))
                # (Line 205) f.Table_Sin(cp, 22 + 45 * (f.loop[cp] % 4), 75);
                DoActions(RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp))
                f.Table_Sin(cp, 22 + 45 * (f.loop[cp] % 4), 75)
                # (Line 206) f.Table_Cos(cp, 22 + 45 * (f.loop[cp] % 4), 75);
                f.Table_Cos(cp, 22 + 45 * (f.loop[cp] % 4), 75)
                # (Line 208) f.SquareShape(cp, 1, "40 + 1n Wraith", f.CosAngle[cp], f.SinAngle[cp]);
                f.SquareShape(cp, 1, "40 + 1n Wraith", f.CosAngle[cp], f.SinAngle[cp])
                # (Line 209) f.SquareShape(cp, 7, "40 + 1n Zealot", f.CosAngle[cp], f.SinAngle[cp]);
                f.SquareShape(cp, 7, "40 + 1n Zealot", f.CosAngle[cp], f.SinAngle[cp])
                # (Line 210) KillUnitAt(All, "40 + 1n Zealot", "Anywhere", cp);
                # (Line 212) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
                DoActions(KillUnitAt(All, "40 + 1n Zealot", "Anywhere", cp))
                # (Line 213) Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);
                DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
                # (Line 215) f.SkillWait(cp, 160);
                DoActions(Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]))
                f.SkillWait(cp, 160)
                # (Line 217) f.loop[cp] += 1;
                _ARRW(f.loop, cp).__iadd__(1)
                # (Line 218) }
                # (Line 219) else if (f.loop[cp] < 8)
            if EUDElseIf()(f.loop[cp] >= 8, neg=True):
                # (Line 220) {
                # (Line 221) RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
                # (Line 223) f.Table_Sin(cp, 22 + 22 * (f.loop[cp] % 4), 225);
                DoActions(RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp))
                f.Table_Sin(cp, 22 + 22 * (f.loop[cp] % 4), 225)
                # (Line 224) f.Table_Cos(cp, 22 + 22 * (f.loop[cp] % 4), 225);
                f.Table_Cos(cp, 22 + 22 * (f.loop[cp] % 4), 225)
                # (Line 226) f.SquareShape(cp, 1, "80 + 1n Tank", f.CosAngle[cp], f.SinAngle[cp]);
                f.SquareShape(cp, 1, "80 + 1n Tank", f.CosAngle[cp], f.SinAngle[cp])
                # (Line 227) KillUnitAt(All, "80 + 1n Tank", "Anywhere", cp);
                # (Line 229) f.SkillWait(cp, 80);
                DoActions(KillUnitAt(All, "80 + 1n Tank", "Anywhere", cp))
                f.SkillWait(cp, 80)
                # (Line 231) f.loop[cp] += 1;
                _ARRW(f.loop, cp).__iadd__(1)
                # (Line 232) }
                # (Line 233) else if (f.loop[cp] < 12)
            if EUDElseIf()(f.loop[cp] >= 12, neg=True):
                # (Line 234) {
                # (Line 235) RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
                # (Line 237) f.Table_Sin(cp, 22 + 22 * (f.loop[cp] % 4), 225);
                DoActions(RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp))
                f.Table_Sin(cp, 22 + 22 * (f.loop[cp] % 4), 225)
                # (Line 238) f.Table_Cos(cp, 22 + 22 * (f.loop[cp] % 4), 225);
                f.Table_Cos(cp, 22 + 22 * (f.loop[cp] % 4), 225)
                # (Line 240) f.SquareShape(cp, 1, "40 + 1n Wraith", f.CosAngle[cp], f.SinAngle[cp]);
                f.SquareShape(cp, 1, "40 + 1n Wraith", f.CosAngle[cp], f.SinAngle[cp])
                # (Line 241) f.SquareShape(cp, 1, " Unit. Hoffnung 25000", f.CosAngle[cp], f.SinAngle[cp]);
                f.SquareShape(cp, 1, " Unit. Hoffnung 25000", f.CosAngle[cp], f.SinAngle[cp])
                # (Line 242) KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
                # (Line 244) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
                DoActions(KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp))
                # (Line 245) Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);
                DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
                # (Line 247) f.SkillWait(cp, 80);
                DoActions(Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]))
                f.SkillWait(cp, 80)
                # (Line 249) f.loop[cp] += 1;
                _ARRW(f.loop, cp).__iadd__(1)
                # (Line 250) }
                # (Line 251) else if (f.loop[cp] == 12)
            if EUDElseIf()(f.loop[cp] == 12):
                # (Line 252) {
                # (Line 253) RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
                # (Line 255) f.SkillWait(cp, 640);
                DoActions(RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp))
                f.SkillWait(cp, 640)
                # (Line 257) f.count[cp] += 1;
                _ARRW(f.count, cp).__iadd__(1)
                # (Line 258) f.loop[cp] = 0;
                _ARRW(f.loop, cp) << (0)
                # (Line 259) }
                # (Line 260) }
            EUDEndIf()
            # (Line 261) else if (f.count[cp] == 3)
        if EUDElseIf()(f.count[cp] == 3):
            # (Line 262) {
            # (Line 263) KillUnitAt(All, "40 + 1n Firebat", "Anywhere", cp);
            # (Line 264) KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
            DoActions(KillUnitAt(All, "40 + 1n Firebat", "Anywhere", cp))
            # (Line 265) KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
            DoActions(KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp))
            # (Line 267) f.SkillEnd(cp);
            DoActions(KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp))
            f.SkillEnd(cp)
            # (Line 268) }
            # (Line 269) }
        EUDEndIf()
        # (Line 270) }
    EUDEndIf()