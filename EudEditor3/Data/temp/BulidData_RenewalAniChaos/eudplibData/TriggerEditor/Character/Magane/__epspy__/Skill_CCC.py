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
            # (Line 9) RemoveUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);
            # (Line 11) f.Table_Sin(cp, 90 - 22 * f.loop[cp], 100);
            DoActions(RemoveUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp))
            f.Table_Sin(cp, 90 - 22 * f.loop[cp], 100)
            # (Line 12) f.Table_Cos(cp, 90 - 22 * f.loop[cp], 100);
            f.Table_Cos(cp, 90 - 22 * f.loop[cp], 100)
            # (Line 14) var x = f.CosAngle[cp];
            x = EUDVariable()
            x << (f.CosAngle[cp])
            # (Line 15) var y = f.SinAngle[cp];
            y = EUDVariable()
            y << (f.SinAngle[cp])
            # (Line 17) f.SquareShape(cp, 1, "40 + 1n Mutalisk", x, y);
            f.SquareShape(cp, 1, "40 + 1n Mutalisk", x, y)
            # (Line 18) f.SquareShape(cp, 1, "Scantid (Desert)", x, y);
            f.SquareShape(cp, 1, "Scantid (Desert)", x, y)
            # (Line 19) KillUnitAt(All, "Scantid (Desert)", "Anywhere", cp);
            # (Line 21) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            DoActions(KillUnitAt(All, "Scantid (Desert)", "Anywhere", cp))
            # (Line 22) Order("40 + 1n Mutalisk", cp, "Anywhere", Attack, f.location[cp]);
            DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
            # (Line 24) f.SkillWait(cp, 80);
            DoActions(Order("40 + 1n Mutalisk", cp, "Anywhere", Attack, f.location[cp]))
            f.SkillWait(cp, 80)
            # (Line 26) f.loop[cp] += 1;
            _ARRW(f.loop, cp).__iadd__(1)
            # (Line 28) if (f.loop[cp] == 4)
            if EUDIf()(f.loop[cp] == 4):
                # (Line 29) {
                # (Line 30) f.count[cp] += 1;
                _ARRW(f.count, cp).__iadd__(1)
                # (Line 31) f.loop[cp] = 0;
                _ARRW(f.loop, cp) << (0)
                # (Line 32) }
                # (Line 33) }
            EUDEndIf()
            # (Line 34) else if (f.count[cp] == 1)
        if EUDElseIf()(f.count[cp] == 1):
            # (Line 35) {
            # (Line 36) RemoveUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);
            # (Line 38) if (f.loop[cp] < 4)
            DoActions(RemoveUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp))
            if EUDIf()(f.loop[cp] >= 4, neg=True):
                # (Line 39) {
                # (Line 40) var x = 300 - 75 * f.loop[cp];
                x = EUDVariable()
                x << (300 - 75 * f.loop[cp])
                # (Line 41) var y = 75 * f.loop[cp];
                y = EUDVariable()
                y << (75 * f.loop[cp])
                # (Line 43) f.SquareShape(cp, 1, "60 + 1n Siege", x, y);
                f.SquareShape(cp, 1, "60 + 1n Siege", x, y)
                # (Line 44) f.SquareShape(cp, 1, "50 + 1n Battlecruiser", x, y);
                f.SquareShape(cp, 1, "50 + 1n Battlecruiser", x, y)
                # (Line 45) KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
                # (Line 47) f.Table_Sin(cp, 90 - 22 * f.loop[cp], 100);
                DoActions(KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp))
                f.Table_Sin(cp, 90 - 22 * f.loop[cp], 100)
                # (Line 48) f.Table_Cos(cp, 90 - 22 * f.loop[cp], 100);
                f.Table_Cos(cp, 90 - 22 * f.loop[cp], 100)
                # (Line 50) x = f.CosAngle[cp];
                x << (f.CosAngle[cp])
                # (Line 51) y = f.SinAngle[cp];
                y << (f.SinAngle[cp])
                # (Line 53) f.SquareShape(cp, 1, "40 + 1n Mutalisk", x, y);
                f.SquareShape(cp, 1, "40 + 1n Mutalisk", x, y)
                # (Line 54) f.SquareShape(cp, 1, "Scantid (Desert)", x, y);
                f.SquareShape(cp, 1, "Scantid (Desert)", x, y)
                # (Line 55) KillUnitAt(All, "Scantid (Desert)", "Anywhere", cp);
                # (Line 57) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
                DoActions(KillUnitAt(All, "Scantid (Desert)", "Anywhere", cp))
                # (Line 58) Order("40 + 1n Mutalisk", cp, "Anywhere", Attack, f.location[cp]);
                DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
                # (Line 59) }
                DoActions(Order("40 + 1n Mutalisk", cp, "Anywhere", Attack, f.location[cp]))
                # (Line 61) f.SkillWait(cp, 80);
            EUDEndIf()
            f.SkillWait(cp, 80)
            # (Line 63) f.loop[cp] += 1;
            _ARRW(f.loop, cp).__iadd__(1)
            # (Line 65) if (f.loop[cp] == 5)
            if EUDIf()(f.loop[cp] == 5):
                # (Line 66) {
                # (Line 67) f.count[cp] += 1;
                _ARRW(f.count, cp).__iadd__(1)
                # (Line 68) f.loop[cp] = 0;
                _ARRW(f.loop, cp) << (0)
                # (Line 69) }
                # (Line 70) }
            EUDEndIf()
            # (Line 71) else if (f.count[cp] == 2)
        if EUDElseIf()(f.count[cp] == 2):
            # (Line 72) {
            # (Line 73) if (f.loop[cp] < 4)
            if EUDIf()(f.loop[cp] >= 4, neg=True):
                # (Line 74) {
                # (Line 75) f.Table_Sin(cp, 22 * f.loop[cp], 200);
                f.Table_Sin(cp, 22 * f.loop[cp], 200)
                # (Line 76) f.Table_Cos(cp, 22 * f.loop[cp], 200);
                f.Table_Cos(cp, 22 * f.loop[cp], 200)
                # (Line 78) var x = f.CosAngle[cp];
                x = EUDVariable()
                x << (f.CosAngle[cp])
                # (Line 79) var y = f.SinAngle[cp];
                y = EUDVariable()
                y << (f.SinAngle[cp])
                # (Line 81) f.SquareShape(cp, 1, "Scantid (Desert)", x, y);
                f.SquareShape(cp, 1, "Scantid (Desert)", x, y)
                # (Line 82) KillUnitAt(All, "Scantid (Desert)", "Anywhere", cp);
                # (Line 83) }
                DoActions(KillUnitAt(All, "Scantid (Desert)", "Anywhere", cp))
                # (Line 85) if (f.loop[cp] == 0)
            EUDEndIf()
            if EUDIf()(f.loop[cp] == 0):
                # (Line 86) {
                # (Line 87) f.EdgeShape(cp, 1, "Target", 0, 3, 75);
                f.EdgeShape(cp, 1, "Target", 0, 3, 75)
                # (Line 88) f.EdgeShape(cp, 1, "60 + 1n Archon", 0, 3, 75);
                f.EdgeShape(cp, 1, "60 + 1n Archon", 0, 3, 75)
                # (Line 89) f.EdgeShape(cp, 1, "40 + 1n Drone", 0, 2, 75);
                f.EdgeShape(cp, 1, "40 + 1n Drone", 0, 2, 75)
                # (Line 90) KillUnitAt(All, "Target", "Anywhere", cp);
                # (Line 91) KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
                DoActions(KillUnitAt(All, "Target", "Anywhere", cp))
                # (Line 93) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
                DoActions(KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp))
                # (Line 94) MoveUnit(All, "40 + 1n Drone", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
                DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
                # (Line 95) Order("40 + 1n Drone", cp, "Anywhere", Attack, f.location[cp]);
                DoActions(MoveUnit(All, "40 + 1n Drone", cp, "[Skill]Unit_Wait_ALL", f.location[cp]))
                # (Line 96) }
                DoActions(Order("40 + 1n Drone", cp, "Anywhere", Attack, f.location[cp]))
                # (Line 97) else if (f.loop[cp] == 2)
            if EUDElseIf()(f.loop[cp] == 2):
                # (Line 98) {
                # (Line 99) f.EdgeShape(cp, 1, "Target", 45, 3, 100);
                f.EdgeShape(cp, 1, "Target", 45, 3, 100)
                # (Line 100) f.EdgeShape(cp, 1, "60 + 1n Archon", 45, 3, 100);
                f.EdgeShape(cp, 1, "60 + 1n Archon", 45, 3, 100)
                # (Line 101) f.EdgeShape(cp, 1, "40 + 1n Drone", 45, 2, 100);
                f.EdgeShape(cp, 1, "40 + 1n Drone", 45, 2, 100)
                # (Line 102) KillUnitAt(All, "Target", "Anywhere", cp);
                # (Line 103) KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
                DoActions(KillUnitAt(All, "Target", "Anywhere", cp))
                # (Line 105) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
                DoActions(KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp))
                # (Line 106) MoveUnit(All, "40 + 1n Drone", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
                DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
                # (Line 107) Order("40 + 1n Drone", cp, "Anywhere", Attack, f.location[cp]);
                DoActions(MoveUnit(All, "40 + 1n Drone", cp, "[Skill]Unit_Wait_ALL", f.location[cp]))
                # (Line 108) }
                DoActions(Order("40 + 1n Drone", cp, "Anywhere", Attack, f.location[cp]))
                # (Line 109) else if (f.loop[cp] == 4)
            if EUDElseIf()(f.loop[cp] == 4):
                # (Line 110) {
                # (Line 111) f.EdgeShape(cp, 1, "40 + 1n Drone", 45, 2, 150);
                f.EdgeShape(cp, 1, "40 + 1n Drone", 45, 2, 150)
                # (Line 112) f.EdgeShape(cp, 1, "50 + 1n Battlecruiser", 45, 2, 150);
                f.EdgeShape(cp, 1, "50 + 1n Battlecruiser", 45, 2, 150)
                # (Line 113) KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
                # (Line 115) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
                DoActions(KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp))
                # (Line 116) MoveUnit(All, "40 + 1n Drone", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
                DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
                # (Line 117) Order("40 + 1n Drone", cp, "Anywhere", Attack, f.location[cp]);
                DoActions(MoveUnit(All, "40 + 1n Drone", cp, "[Skill]Unit_Wait_ALL", f.location[cp]))
                # (Line 118) }
                DoActions(Order("40 + 1n Drone", cp, "Anywhere", Attack, f.location[cp]))
                # (Line 120) f.SkillWait(cp, 80);
            EUDEndIf()
            f.SkillWait(cp, 80)
            # (Line 122) f.loop[cp] += 1;
            _ARRW(f.loop, cp).__iadd__(1)
            # (Line 124) if (f.loop[cp] == 5)
            if EUDIf()(f.loop[cp] == 5):
                # (Line 125) {
                # (Line 126) f.count[cp] += 1;
                _ARRW(f.count, cp).__iadd__(1)
                # (Line 127) f.loop[cp] = 0;
                _ARRW(f.loop, cp) << (0)
                # (Line 128) }
                # (Line 129) }
            EUDEndIf()
            # (Line 130) else if (f.count[cp] == 3)
        if EUDElseIf()(f.count[cp] == 3):
            # (Line 131) {
            # (Line 132) if (f.loop[cp] < 4)
            if EUDIf()(f.loop[cp] >= 4, neg=True):
                # (Line 133) {
                # (Line 134) f.SquareShape(cp, 1, "40 + 1n Gantrithor", 75 * f.loop[cp], 225 - 75 * f.loop[cp]);
                f.SquareShape(cp, 1, "40 + 1n Gantrithor", 75 * f.loop[cp], 225 - 75 * f.loop[cp])
                # (Line 135) KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);
                # (Line 137) if ((f.loop[cp] % 2) == 0)
                DoActions(KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp))
                if EUDIf()((f.loop[cp] % 2) == 0):
                    # (Line 138) {
                    # (Line 139) f.DoubleShape(cp, 1, "Protoss Dark Archon", 100 - 100 * (f.loop[cp] % 2), 100 * (f.loop[cp] % 2));
                    f.DoubleShape(cp, 1, "Protoss Dark Archon", 100 - 100 * (f.loop[cp] % 2), 100 * (f.loop[cp] % 2))
                    # (Line 140) f.DoubleShape(cp, 1, "40 + 1n Mutalisk", 100 - 100 * (f.loop[cp] % 2), 100 * (f.loop[cp] % 2));
                    f.DoubleShape(cp, 1, "40 + 1n Mutalisk", 100 - 100 * (f.loop[cp] % 2), 100 * (f.loop[cp] % 2))
                    # (Line 141) KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
                    # (Line 143) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
                    DoActions(KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp))
                    # (Line 144) Order("40 + 1n Mutalisk", cp, "Anywhere", Attack, f.location[cp]);
                    DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
                    # (Line 145) }
                    DoActions(Order("40 + 1n Mutalisk", cp, "Anywhere", Attack, f.location[cp]))
                    # (Line 146) else if ((f.loop[cp] % 2) == 1)
                if EUDElseIf()((f.loop[cp] % 2) == 1):
                    # (Line 147) {
                    # (Line 148) f.DoubleShape(cp, 1, "Protoss Dark Archon", 0 - 100 * (f.loop[cp] % 2), 100 * (f.loop[cp] % 2));
                    f.DoubleShape(cp, 1, "Protoss Dark Archon", 0 - 100 * (f.loop[cp] % 2), 100 * (f.loop[cp] % 2))
                    # (Line 149) f.DoubleShape(cp, 1, "40 + 1n Mutalisk", 0 - 100 * (f.loop[cp] % 2), 100 * (f.loop[cp] % 2));
                    f.DoubleShape(cp, 1, "40 + 1n Mutalisk", 0 - 100 * (f.loop[cp] % 2), 100 * (f.loop[cp] % 2))
                    # (Line 150) KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
                    # (Line 152) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
                    DoActions(KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp))
                    # (Line 153) Order("40 + 1n Mutalisk", cp, "Anywhere", Attack, f.location[cp]);
                    DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
                    # (Line 154) }
                    DoActions(Order("40 + 1n Mutalisk", cp, "Anywhere", Attack, f.location[cp]))
                    # (Line 155) }
                EUDEndIf()
                # (Line 157) f.SkillWait(cp, 80);
            EUDEndIf()
            f.SkillWait(cp, 80)
            # (Line 159) f.loop[cp] += 1;
            _ARRW(f.loop, cp).__iadd__(1)
            # (Line 161) if (f.loop[cp] == 5)
            if EUDIf()(f.loop[cp] == 5):
                # (Line 162) {
                # (Line 163) f.count[cp] += 1;
                _ARRW(f.count, cp).__iadd__(1)
                # (Line 164) f.loop[cp] = 0;
                _ARRW(f.loop, cp) << (0)
                # (Line 165) }
                # (Line 166) }
            EUDEndIf()
            # (Line 167) else if (f.count[cp] == 4)
        if EUDElseIf()(f.count[cp] == 4):
            # (Line 168) {
            # (Line 169) var x = 0;
            x = EUDVariable()
            x << (0)
            # (Line 170) var y = 0;
            y = EUDVariable()
            y << (0)
            # (Line 172) if (f.loop[cp] == 0)
            if EUDIf()(f.loop[cp] == 0):
                # (Line 173) {
                # (Line 174) x = 150;
                x << (150)
                # (Line 175) y = 0;
                y << (0)
                # (Line 177) f.SquareShape(cp, 1, "50 + 1n Battlecruiser", -y, x);
                f.SquareShape(cp, 1, "50 + 1n Battlecruiser", -y, x)
                # (Line 178) KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
                # (Line 180) f.SquareShape(cp, 1, "40 + 1n Guardian", x, y);
                DoActions(KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp))
                f.SquareShape(cp, 1, "40 + 1n Guardian", x, y)
                # (Line 181) f.SquareShape(cp, 1, "60 + 1n Archon", x, y);
                f.SquareShape(cp, 1, "60 + 1n Archon", x, y)
                # (Line 182) KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
                # (Line 184) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
                DoActions(KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp))
                # (Line 185) Order("40 + 1n Guardian", cp, "Anywhere", Attack, f.location[cp]);
                DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
                # (Line 186) }
                DoActions(Order("40 + 1n Guardian", cp, "Anywhere", Attack, f.location[cp]))
                # (Line 187) else if (f.loop[cp] == 2)
            if EUDElseIf()(f.loop[cp] == 2):
                # (Line 188) {
                # (Line 189) x = 150;
                x << (150)
                # (Line 190) y = 150;
                y << (150)
                # (Line 192) f.SquareShape(cp, 1, "50 + 1n Battlecruiser", -y, x);
                f.SquareShape(cp, 1, "50 + 1n Battlecruiser", -y, x)
                # (Line 193) KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
                # (Line 195) f.SquareShape(cp, 1, "40 + 1n Guardian", x, y);
                DoActions(KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp))
                f.SquareShape(cp, 1, "40 + 1n Guardian", x, y)
                # (Line 196) f.SquareShape(cp, 1, "60 + 1n Archon", x, y);
                f.SquareShape(cp, 1, "60 + 1n Archon", x, y)
                # (Line 197) KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
                # (Line 199) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
                DoActions(KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp))
                # (Line 200) Order("40 + 1n Guardian", cp, "Anywhere", Attack, f.location[cp]);
                DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
                # (Line 201) }
                DoActions(Order("40 + 1n Guardian", cp, "Anywhere", Attack, f.location[cp]))
                # (Line 203) f.SkillWait(cp, 80);
            EUDEndIf()
            f.SkillWait(cp, 80)
            # (Line 205) f.loop[cp] += 1;
            _ARRW(f.loop, cp).__iadd__(1)
            # (Line 207) if (f.loop[cp] == 24)
            if EUDIf()(f.loop[cp] == 24):
                # (Line 208) {
                # (Line 209) f.count[cp] += 1;
                _ARRW(f.count, cp).__iadd__(1)
                # (Line 210) f.loop[cp] = 0;
                _ARRW(f.loop, cp) << (0)
                # (Line 211) }
                # (Line 212) }
            EUDEndIf()
            # (Line 213) else if (f.count[cp] == 5)
        if EUDElseIf()(f.count[cp] == 5):
            # (Line 214) {
            # (Line 215) KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            # (Line 216) KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);
            DoActions(KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp))
            # (Line 217) KillUnitAt(All, "40 + 1n Drone", "Anywhere", cp);
            DoActions(KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp))
            # (Line 218) KillUnitAt(All, "60 + 1n Siege", "Anywhere", cp);
            DoActions(KillUnitAt(All, "40 + 1n Drone", "Anywhere", cp))
            # (Line 219) KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);
            DoActions(KillUnitAt(All, "60 + 1n Siege", "Anywhere", cp))
            # (Line 221) f.SkillEnd(cp);
            DoActions(KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp))
            f.SkillEnd(cp)
            # (Line 222) }
            # (Line 223) }
        EUDEndIf()
        # (Line 224) }
    EUDEndIf()