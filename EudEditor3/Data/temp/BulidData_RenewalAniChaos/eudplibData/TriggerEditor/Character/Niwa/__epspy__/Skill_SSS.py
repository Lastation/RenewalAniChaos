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
            # (Line 9) if (f.loop[cp] == 0)
            if EUDIf()(f.loop[cp] == 0):
                # (Line 10) {
                # (Line 11) f.Table_Sin(cp, 0, 75);
                f.Table_Sin(cp, 0, 75)
                # (Line 12) f.Table_Cos(cp, 0, 75);
                f.Table_Cos(cp, 0, 75)
                # (Line 14) var x = f.CosAngle[cp];
                x = EUDVariable()
                x << (f.CosAngle[cp])
                # (Line 15) var y = f.SinAngle[cp];
                y = EUDVariable()
                y << (f.SinAngle[cp])
                # (Line 17) f.SquareShape(cp, 1, "Target", x, y);
                f.SquareShape(cp, 1, "Target", x, y)
                # (Line 18) KillUnitAt(All, "Target", "Anywhere", cp);
                # (Line 20) f.Table_Sin(cp, 45, 75);
                DoActions(KillUnitAt(All, "Target", "Anywhere", cp))
                f.Table_Sin(cp, 45, 75)
                # (Line 21) f.Table_Cos(cp, 45, 75);
                f.Table_Cos(cp, 45, 75)
                # (Line 23) x = f.CosAngle[cp];
                x << (f.CosAngle[cp])
                # (Line 24) y = f.SinAngle[cp];
                y << (f.SinAngle[cp])
                # (Line 26) f.SquareShape(cp, 1, "Target", x, y);
                f.SquareShape(cp, 1, "Target", x, y)
                # (Line 27) KillUnitAt(All, "Target", "Anywhere", cp);
                # (Line 28) }
                DoActions(KillUnitAt(All, "Target", "Anywhere", cp))
                # (Line 29) else if (f.loop[cp] == 2)
            if EUDElseIf()(f.loop[cp] == 2):
                # (Line 30) {
                # (Line 31) f.Table_Sin(cp, 0, 150);
                f.Table_Sin(cp, 0, 150)
                # (Line 32) f.Table_Cos(cp, 0, 150);
                f.Table_Cos(cp, 0, 150)
                # (Line 34) var x = f.CosAngle[cp];
                x = EUDVariable()
                x << (f.CosAngle[cp])
                # (Line 35) var y = f.SinAngle[cp];
                y = EUDVariable()
                y << (f.SinAngle[cp])
                # (Line 37) f.SquareShape(cp, 1, "40 + 1n Guardian", x, y);
                f.SquareShape(cp, 1, "40 + 1n Guardian", x, y)
                # (Line 38) f.SquareShape(cp, 1, "60 + 1n Archon", x, y);
                f.SquareShape(cp, 1, "60 + 1n Archon", x, y)
                # (Line 39) KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
                # (Line 40) KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
                DoActions(KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp))
                # (Line 42) f.Table_Sin(cp, 45, 150);
                DoActions(KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp))
                f.Table_Sin(cp, 45, 150)
                # (Line 43) f.Table_Cos(cp, 45, 150);
                f.Table_Cos(cp, 45, 150)
                # (Line 45) x = f.CosAngle[cp];
                x << (f.CosAngle[cp])
                # (Line 46) y = f.SinAngle[cp];
                y << (f.SinAngle[cp])
                # (Line 48) f.SquareShape(cp, 1, "40 + 1n Guardian", x, y);
                f.SquareShape(cp, 1, "40 + 1n Guardian", x, y)
                # (Line 49) f.SquareShape(cp, 1, "60 + 1n Archon", x, y);
                f.SquareShape(cp, 1, "60 + 1n Archon", x, y)
                # (Line 50) KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
                # (Line 51) KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
                DoActions(KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp))
                # (Line 53) f.Table_Sin(cp, 0, 75);
                DoActions(KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp))
                f.Table_Sin(cp, 0, 75)
                # (Line 54) f.Table_Cos(cp, 0, 75);
                f.Table_Cos(cp, 0, 75)
                # (Line 56) x = f.CosAngle[cp];
                x << (f.CosAngle[cp])
                # (Line 57) y = f.SinAngle[cp];
                y << (f.SinAngle[cp])
                # (Line 59) f.SquareShape(cp, 1, "Kakaru (Twilight)", x, y);
                f.SquareShape(cp, 1, "Kakaru (Twilight)", x, y)
                # (Line 60) KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
                # (Line 62) f.Table_Sin(cp, 45, 75);
                DoActions(KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp))
                f.Table_Sin(cp, 45, 75)
                # (Line 63) f.Table_Cos(cp, 45, 75);
                f.Table_Cos(cp, 45, 75)
                # (Line 65) x = f.CosAngle[cp];
                x << (f.CosAngle[cp])
                # (Line 66) y = f.SinAngle[cp];
                y << (f.SinAngle[cp])
                # (Line 68) f.SquareShape(cp, 1, "Kakaru (Twilight)", x, y);
                f.SquareShape(cp, 1, "Kakaru (Twilight)", x, y)
                # (Line 69) KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
                # (Line 70) }
                DoActions(KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp))
                # (Line 71) else if (f.loop[cp] == 4)
            if EUDElseIf()(f.loop[cp] == 4):
                # (Line 72) {
                # (Line 73) f.Table_Sin(cp, 0, 150);
                f.Table_Sin(cp, 0, 150)
                # (Line 74) f.Table_Cos(cp, 0, 150);
                f.Table_Cos(cp, 0, 150)
                # (Line 76) var x = f.CosAngle[cp];
                x = EUDVariable()
                x << (f.CosAngle[cp])
                # (Line 77) var y = f.SinAngle[cp];
                y = EUDVariable()
                y << (f.SinAngle[cp])
                # (Line 79) f.SquareShape(cp, 1, "40 + 1n Mutalisk", x, y);
                f.SquareShape(cp, 1, "40 + 1n Mutalisk", x, y)
                # (Line 80) f.SquareShape(cp, 1, " Unit. Hoffnung 25000", x, y);
                f.SquareShape(cp, 1, " Unit. Hoffnung 25000", x, y)
                # (Line 81) KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
                # (Line 83) f.Table_Sin(cp, 45, 150);
                DoActions(KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp))
                f.Table_Sin(cp, 45, 150)
                # (Line 84) f.Table_Cos(cp, 45, 150);
                f.Table_Cos(cp, 45, 150)
                # (Line 86) x = f.CosAngle[cp];
                x << (f.CosAngle[cp])
                # (Line 87) y = f.SinAngle[cp];
                y << (f.SinAngle[cp])
                # (Line 89) f.SquareShape(cp, 1, "40 + 1n Mutalisk", x, y);
                f.SquareShape(cp, 1, "40 + 1n Mutalisk", x, y)
                # (Line 90) f.SquareShape(cp, 1, " Unit. Hoffnung 25000", x, y);
                f.SquareShape(cp, 1, " Unit. Hoffnung 25000", x, y)
                # (Line 91) KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
                # (Line 93) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
                DoActions(KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp))
                # (Line 94) Order("40 + 1n Mutalisk", cp, "Anywhere", Attack, f.location[cp]);
                DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
                # (Line 95) }
                DoActions(Order("40 + 1n Mutalisk", cp, "Anywhere", Attack, f.location[cp]))
                # (Line 96) else if (f.loop[cp] == 6)
            if EUDElseIf()(f.loop[cp] == 6):
                # (Line 97) {
                # (Line 98) f.Table_Sin(cp, 0, 150);
                f.Table_Sin(cp, 0, 150)
                # (Line 99) f.Table_Cos(cp, 0, 150);
                f.Table_Cos(cp, 0, 150)
                # (Line 101) var x = f.CosAngle[cp];
                x = EUDVariable()
                x << (f.CosAngle[cp])
                # (Line 102) var y = f.SinAngle[cp];
                y = EUDVariable()
                y << (f.SinAngle[cp])
                # (Line 104) f.SquareShape(cp, 1, "50 + 1n Tank", x, y);
                f.SquareShape(cp, 1, "50 + 1n Tank", x, y)
                # (Line 105) KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
                # (Line 107) f.Table_Sin(cp, 45, 150);
                DoActions(KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp))
                f.Table_Sin(cp, 45, 150)
                # (Line 108) f.Table_Cos(cp, 45, 150);
                f.Table_Cos(cp, 45, 150)
                # (Line 110) x = f.CosAngle[cp];
                x << (f.CosAngle[cp])
                # (Line 111) y = f.SinAngle[cp];
                y << (f.SinAngle[cp])
                # (Line 113) f.SquareShape(cp, 1, "50 + 1n Tank", x, y);
                f.SquareShape(cp, 1, "50 + 1n Tank", x, y)
                # (Line 114) KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
                # (Line 115) }
                DoActions(KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp))
                # (Line 116) f.SkillWait(cp, 80);
            EUDEndIf()
            f.SkillWait(cp, 80)
            # (Line 118) f.loop[cp] += 1;
            _ARRW(f.loop, cp).__iadd__(1)
            # (Line 120) if (f.loop[cp] == 8)
            if EUDIf()(f.loop[cp] == 8):
                # (Line 121) {
                # (Line 122) f.count[cp] += 1;
                _ARRW(f.count, cp).__iadd__(1)
                # (Line 123) f.loop[cp] = 0;
                _ARRW(f.loop, cp) << (0)
                # (Line 124) }
                # (Line 125) }
            EUDEndIf()
            # (Line 126) else if (f.count[cp] == 1)
        if EUDElseIf()(f.count[cp] == 1):
            # (Line 127) {
            # (Line 128) if (f.loop[cp] < 8)
            if EUDIf()(f.loop[cp] >= 8, neg=True):
                # (Line 129) {
                # (Line 130) f.Table_Sin(cp, 450 - 45 * f.loop[cp], 150);
                f.Table_Sin(cp, 450 - 45 * f.loop[cp], 150)
                # (Line 131) f.Table_Cos(cp, 450 - 45 * f.loop[cp], 150);
                f.Table_Cos(cp, 450 - 45 * f.loop[cp], 150)
                # (Line 133) var x = f.CosAngle[cp];
                x = EUDVariable()
                x << (f.CosAngle[cp])
                # (Line 134) var y = f.SinAngle[cp];
                y = EUDVariable()
                y << (f.SinAngle[cp])
                # (Line 136) f.DotShape(cp, 1, "40 + 1n Gantrithor", x, y);
                f.DotShape(cp, 1, "40 + 1n Gantrithor", x, y)
                # (Line 137) KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);
                # (Line 138) }
                DoActions(KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp))
                # (Line 140) f.SkillWait(cp, 80);
            EUDEndIf()
            f.SkillWait(cp, 80)
            # (Line 142) f.loop[cp] += 1;
            _ARRW(f.loop, cp).__iadd__(1)
            # (Line 144) if (f.loop[cp] == 8)
            if EUDIf()(f.loop[cp] == 8):
                # (Line 145) {
                # (Line 146) f.count[cp] += 1;
                _ARRW(f.count, cp).__iadd__(1)
                # (Line 147) f.loop[cp] = 0;
                _ARRW(f.loop, cp) << (0)
                # (Line 148) }
                # (Line 149) }
            EUDEndIf()
            # (Line 150) else if (f.count[cp] == 2)
        if EUDElseIf()(f.count[cp] == 2):
            # (Line 151) {
            # (Line 152) if (f.loop[cp] == 0)
            if EUDIf()(f.loop[cp] == 0):
                # (Line 153) {
                # (Line 154) f.Table_Sin(cp, 0, 75);
                f.Table_Sin(cp, 0, 75)
                # (Line 155) f.Table_Cos(cp, 0, 75);
                f.Table_Cos(cp, 0, 75)
                # (Line 157) var x = f.CosAngle[cp];
                x = EUDVariable()
                x << (f.CosAngle[cp])
                # (Line 158) var y = f.SinAngle[cp];
                y = EUDVariable()
                y << (f.SinAngle[cp])
                # (Line 160) f.SquareShape(cp, 1, "80 + 1n Mutalisk", x, y);
                f.SquareShape(cp, 1, "80 + 1n Mutalisk", x, y)
                # (Line 161) KillUnitAt(All, "80 + 1n Mutalisk", "Anywhere", cp);
                # (Line 163) f.Table_Sin(cp, 45, 75);
                DoActions(KillUnitAt(All, "80 + 1n Mutalisk", "Anywhere", cp))
                f.Table_Sin(cp, 45, 75)
                # (Line 164) f.Table_Cos(cp, 45, 75);
                f.Table_Cos(cp, 45, 75)
                # (Line 166) x = f.CosAngle[cp];
                x << (f.CosAngle[cp])
                # (Line 167) y = f.SinAngle[cp];
                y << (f.SinAngle[cp])
                # (Line 169) f.SquareShape(cp, 1, "80 + 1n Mutalisk", x, y);
                f.SquareShape(cp, 1, "80 + 1n Mutalisk", x, y)
                # (Line 170) KillUnitAt(All, "80 + 1n Mutalisk", "Anywhere", cp);
                # (Line 171) }
                DoActions(KillUnitAt(All, "80 + 1n Mutalisk", "Anywhere", cp))
                # (Line 172) else if (f.loop[cp] == 2)
            if EUDElseIf()(f.loop[cp] == 2):
                # (Line 173) {
                # (Line 174) f.Table_Sin(cp, 0, 150);
                f.Table_Sin(cp, 0, 150)
                # (Line 175) f.Table_Cos(cp, 0, 150);
                f.Table_Cos(cp, 0, 150)
                # (Line 177) var x = f.CosAngle[cp];
                x = EUDVariable()
                x << (f.CosAngle[cp])
                # (Line 178) var y = f.SinAngle[cp];
                y = EUDVariable()
                y << (f.SinAngle[cp])
                # (Line 180) f.SquareShape(cp, 1, "50 + 1n Battlecruiser", x, y);
                f.SquareShape(cp, 1, "50 + 1n Battlecruiser", x, y)
                # (Line 181) f.SquareShape(cp, 1, "40 + 1n Goliath", x, y);
                f.SquareShape(cp, 1, "40 + 1n Goliath", x, y)
                # (Line 182) KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
                # (Line 184) f.Table_Sin(cp, 45, 150);
                DoActions(KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp))
                f.Table_Sin(cp, 45, 150)
                # (Line 185) f.Table_Cos(cp, 45, 150);
                f.Table_Cos(cp, 45, 150)
                # (Line 187) x = f.CosAngle[cp];
                x << (f.CosAngle[cp])
                # (Line 188) y = f.SinAngle[cp];
                y << (f.SinAngle[cp])
                # (Line 190) f.SquareShape(cp, 1, "50 + 1n Battlecruiser", x, y);
                f.SquareShape(cp, 1, "50 + 1n Battlecruiser", x, y)
                # (Line 191) f.SquareShape(cp, 1, "40 + 1n Goliath", x, y);
                f.SquareShape(cp, 1, "40 + 1n Goliath", x, y)
                # (Line 192) KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
                # (Line 194) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
                DoActions(KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp))
                # (Line 195) MoveUnit(All, "40 + 1n Goliath", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
                DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
                # (Line 196) Order("40 + 1n Goliath", cp, "Anywhere", Attack, f.location[cp]);
                DoActions(MoveUnit(All, "40 + 1n Goliath", cp, "[Skill]Unit_Wait_ALL", f.location[cp]))
                # (Line 197) }
                DoActions(Order("40 + 1n Goliath", cp, "Anywhere", Attack, f.location[cp]))
                # (Line 198) else if (f.loop[cp] == 3)
            if EUDElseIf()(f.loop[cp] == 3):
                # (Line 199) {
                # (Line 200) RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);
                # (Line 201) }
                DoActions(RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", cp))
                # (Line 203) f.SkillWait(cp, 80);
            EUDEndIf()
            f.SkillWait(cp, 80)
            # (Line 205) f.loop[cp] += 1;
            _ARRW(f.loop, cp).__iadd__(1)
            # (Line 207) if (f.loop[cp] == 10)
            if EUDIf()(f.loop[cp] == 10):
                # (Line 208) {
                # (Line 209) f.count[cp] += 1;
                _ARRW(f.count, cp).__iadd__(1)
                # (Line 210) f.loop[cp] = 0;
                _ARRW(f.loop, cp) << (0)
                # (Line 211) }
                # (Line 212) }
            EUDEndIf()
            # (Line 213) else if (f.count[cp] == 3)
        if EUDElseIf()(f.count[cp] == 3):
            # (Line 214) {
            # (Line 215) if (f.loop[cp] < 8)
            if EUDIf()(f.loop[cp] >= 8, neg=True):
                # (Line 216) {
                # (Line 217) f.MoveLoc("40 + 1n Mutalisk", cp, 0, 0);
                f.MoveLoc("40 + 1n Mutalisk", cp, 0, 0)
                # (Line 218) RemoveUnitAt(1, "40 + 1n Mutalisk", "Anywhere", cp);
                # (Line 219) f.SkillUnit(cp, 1, "40 + 1n Drone");
                DoActions(RemoveUnitAt(1, "40 + 1n Mutalisk", "Anywhere", cp))
                f.SkillUnit(cp, 1, "40 + 1n Drone")
                # (Line 220) f.SkillUnit(cp, 1, " Unit. Hoffnung 25000");
                f.SkillUnit(cp, 1, " Unit. Hoffnung 25000")
                # (Line 222) if (f.loop[cp] % 2 == 0)
                if EUDIf()(f.loop[cp] % 2 == 0):
                    # (Line 223) {
                    # (Line 224) f.SkillUnit(cp, 1, "40 + 1n Gantrithor");
                    f.SkillUnit(cp, 1, "40 + 1n Gantrithor")
                    # (Line 225) }
                    # (Line 226) else if (f.loop[cp] % 2 == 1)
                if EUDElseIf()(f.loop[cp] % 2 == 1):
                    # (Line 227) {
                    # (Line 228) f.SkillUnit(cp, 1, "50 + 1n Battlecruiser");
                    f.SkillUnit(cp, 1, "50 + 1n Battlecruiser")
                    # (Line 229) }
                    # (Line 231) KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);
                EUDEndIf()
                # (Line 232) KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
                DoActions(KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp))
                # (Line 233) KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
                DoActions(KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp))
                # (Line 235) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
                DoActions(KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp))
                # (Line 236) MoveUnit(All, "40 + 1n Drone", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
                DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
                # (Line 237) }
                DoActions(MoveUnit(All, "40 + 1n Drone", cp, "[Skill]Unit_Wait_ALL", f.location[cp]))
                # (Line 239) f.SkillWait(cp, 80);
            EUDEndIf()
            f.SkillWait(cp, 80)
            # (Line 241) f.loop[cp] += 1;
            _ARRW(f.loop, cp).__iadd__(1)
            # (Line 243) if (f.loop[cp] == 16)
            if EUDIf()(f.loop[cp] == 16):
                # (Line 244) {
                # (Line 245) f.count[cp] += 1;
                _ARRW(f.count, cp).__iadd__(1)
                # (Line 246) f.loop[cp] = 0;
                _ARRW(f.loop, cp) << (0)
                # (Line 247) }
                # (Line 248) }
            EUDEndIf()
            # (Line 249) else if (f.count[cp] == 4)
        if EUDElseIf()(f.count[cp] == 4):
            # (Line 250) {
            # (Line 251) if (f.loop[cp] == 0)
            if EUDIf()(f.loop[cp] == 0):
                # (Line 252) {
                # (Line 253) for (var i = 0; i < 8; i++)
                i = EUDVariable()
                i << (0)
                if EUDWhile()(i >= 8, neg=True):
                    def _t24():
                        i.__iadd__(1)
                    # (Line 254) {
                    # (Line 255) f.MoveLoc("40 + 1n Drone", cp, 0, 0);
                    f.MoveLoc("40 + 1n Drone", cp, 0, 0)
                    # (Line 256) RemoveUnitAt(1, "40 + 1n Drone", "Anywhere", cp);
                    # (Line 257) f.SkillUnit(cp, 1, "40 + 1n Mojo");
                    DoActions(RemoveUnitAt(1, "40 + 1n Drone", "Anywhere", cp))
                    f.SkillUnit(cp, 1, "40 + 1n Mojo")
                    # (Line 258) f.SkillUnit(cp, 1, "60 + 1n Hydralisk");
                    f.SkillUnit(cp, 1, "60 + 1n Hydralisk")
                    # (Line 259) }
                    # (Line 261) KillUnitAt(All, "60 + 1n Hydralisk", "Anywhere", cp);
                    EUDSetContinuePoint()
                    _t24()
                EUDEndWhile()
                # (Line 263) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
                DoActions(KillUnitAt(All, "60 + 1n Hydralisk", "Anywhere", cp))
                # (Line 264) Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);
                DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
                # (Line 265) }
                DoActions(Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]))
                # (Line 266) if (f.loop[cp] == 1)
            EUDEndIf()
            if EUDIf()(f.loop[cp] == 1):
                # (Line 267) {
                # (Line 268) for (var i = 0; i < 8; i++)
                i = EUDVariable()
                i << (0)
                if EUDWhile()(i >= 8, neg=True):
                    def _t27():
                        i.__iadd__(1)
                    # (Line 269) {
                    # (Line 270) f.MoveLoc("40 + 1n Mojo", cp, 0, 0);
                    f.MoveLoc("40 + 1n Mojo", cp, 0, 0)
                    # (Line 271) RemoveUnitAt(1, "40 + 1n Mojo", "Anywhere", cp);
                    # (Line 272) f.SkillUnit(cp, 1, "Kakaru (Twilight)");
                    DoActions(RemoveUnitAt(1, "40 + 1n Mojo", "Anywhere", cp))
                    f.SkillUnit(cp, 1, "Kakaru (Twilight)")
                    # (Line 273) }
                    # (Line 275) KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
                    EUDSetContinuePoint()
                    _t27()
                EUDEndWhile()
                # (Line 276) }
                DoActions(KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp))
                # (Line 277) f.SkillWait(cp, 80);
            EUDEndIf()
            f.SkillWait(cp, 80)
            # (Line 279) f.loop[cp] += 1;
            _ARRW(f.loop, cp).__iadd__(1)
            # (Line 281) if (f.loop[cp] == 2)
            if EUDIf()(f.loop[cp] == 2):
                # (Line 282) {
                # (Line 283) f.count[cp] += 1;
                _ARRW(f.count, cp).__iadd__(1)
                # (Line 284) f.loop[cp] = 0;
                _ARRW(f.loop, cp) << (0)
                # (Line 285) }
                # (Line 286) }
            EUDEndIf()
            # (Line 287) else if (f.count[cp] == 5)
        if EUDElseIf()(f.count[cp] == 5):
            # (Line 288) {
            # (Line 289) f.SkillEnd(cp);
            f.SkillEnd(cp)
            # (Line 290) }
            # (Line 291) }
        EUDEndIf()
        # (Line 292) }
    EUDEndIf()