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
# (Line 2) import variable as v;
import variable as v
# (Line 3) import func.trig as trg;
from func import trig as trg
# (Line 5) function main(playerID)
# (Line 6) {
@EUDFunc
def f_main(playerID):
    # (Line 7) if (v.P_WaitMain[playerID] == 0)
    if EUDIf()(v.P_WaitMain[playerID] == 0):
        # (Line 8) {
        # (Line 9) if (v.P_CountMain[playerID] == 0)
        if EUDIf()(v.P_CountMain[playerID] == 0):
            # (Line 10) {
            # (Line 11) if (v.P_LoopMain[playerID] == 0)
            if EUDIf()(v.P_LoopMain[playerID] == 0):
                # (Line 12) {
                # (Line 13) trg.Table_Sin(playerID, 0, 75);
                trg.Table_Sin(playerID, 0, 75)
                # (Line 14) trg.Table_Cos(playerID, 0, 75);
                trg.Table_Cos(playerID, 0, 75)
                # (Line 16) var x = v.P_AngleCos[playerID];
                x = EUDVariable()
                x << (v.P_AngleCos[playerID])
                # (Line 17) var y = v.P_AngleSin[playerID];
                y = EUDVariable()
                y << (v.P_AngleSin[playerID])
                # (Line 19) trg.Shape_Square(playerID, 1, "Target", x, y);
                trg.Shape_Square(playerID, 1, "Target", x, y)
                # (Line 20) KillUnitAt(All, "Target", "Anywhere", playerID);
                # (Line 22) trg.Table_Sin(playerID, 45, 75);
                DoActions(KillUnitAt(All, "Target", "Anywhere", playerID))
                trg.Table_Sin(playerID, 45, 75)
                # (Line 23) trg.Table_Cos(playerID, 45, 75);
                trg.Table_Cos(playerID, 45, 75)
                # (Line 25) x = v.P_AngleCos[playerID];
                x << (v.P_AngleCos[playerID])
                # (Line 26) y = v.P_AngleSin[playerID];
                y << (v.P_AngleSin[playerID])
                # (Line 28) trg.Shape_Square(playerID, 1, "Target", x, y);
                trg.Shape_Square(playerID, 1, "Target", x, y)
                # (Line 29) KillUnitAt(All, "Target", "Anywhere", playerID);
                # (Line 30) }
                DoActions(KillUnitAt(All, "Target", "Anywhere", playerID))
                # (Line 31) else if (v.P_LoopMain[playerID] == 2)
            if EUDElseIf()(v.P_LoopMain[playerID] == 2):
                # (Line 32) {
                # (Line 33) trg.Table_Sin(playerID, 0, 150);
                trg.Table_Sin(playerID, 0, 150)
                # (Line 34) trg.Table_Cos(playerID, 0, 150);
                trg.Table_Cos(playerID, 0, 150)
                # (Line 36) var x = v.P_AngleCos[playerID];
                x = EUDVariable()
                x << (v.P_AngleCos[playerID])
                # (Line 37) var y = v.P_AngleSin[playerID];
                y = EUDVariable()
                y << (v.P_AngleSin[playerID])
                # (Line 39) trg.Shape_Square(playerID, 1, "40 + 1n Guardian", x, y);
                trg.Shape_Square(playerID, 1, "40 + 1n Guardian", x, y)
                # (Line 40) trg.Shape_Square(playerID, 1, "60 + 1n Archon", x, y);
                trg.Shape_Square(playerID, 1, "60 + 1n Archon", x, y)
                # (Line 41) KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID);
                # (Line 42) KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID))
                # (Line 44) trg.Table_Sin(playerID, 45, 150);
                DoActions(KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID))
                trg.Table_Sin(playerID, 45, 150)
                # (Line 45) trg.Table_Cos(playerID, 45, 150);
                trg.Table_Cos(playerID, 45, 150)
                # (Line 47) x = v.P_AngleCos[playerID];
                x << (v.P_AngleCos[playerID])
                # (Line 48) y = v.P_AngleSin[playerID];
                y << (v.P_AngleSin[playerID])
                # (Line 50) trg.Shape_Square(playerID, 1, "40 + 1n Guardian", x, y);
                trg.Shape_Square(playerID, 1, "40 + 1n Guardian", x, y)
                # (Line 51) trg.Shape_Square(playerID, 1, "60 + 1n Archon", x, y);
                trg.Shape_Square(playerID, 1, "60 + 1n Archon", x, y)
                # (Line 52) KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID);
                # (Line 53) KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID))
                # (Line 55) trg.Table_Sin(playerID, 0, 75);
                DoActions(KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID))
                trg.Table_Sin(playerID, 0, 75)
                # (Line 56) trg.Table_Cos(playerID, 0, 75);
                trg.Table_Cos(playerID, 0, 75)
                # (Line 58) x = v.P_AngleCos[playerID];
                x << (v.P_AngleCos[playerID])
                # (Line 59) y = v.P_AngleSin[playerID];
                y << (v.P_AngleSin[playerID])
                # (Line 61) trg.Shape_Square(playerID, 1, "Kakaru (Twilight)", x, y);
                trg.Shape_Square(playerID, 1, "Kakaru (Twilight)", x, y)
                # (Line 62) KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", playerID);
                # (Line 64) trg.Table_Sin(playerID, 45, 75);
                DoActions(KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", playerID))
                trg.Table_Sin(playerID, 45, 75)
                # (Line 65) trg.Table_Cos(playerID, 45, 75);
                trg.Table_Cos(playerID, 45, 75)
                # (Line 67) x = v.P_AngleCos[playerID];
                x << (v.P_AngleCos[playerID])
                # (Line 68) y = v.P_AngleSin[playerID];
                y << (v.P_AngleSin[playerID])
                # (Line 70) trg.Shape_Square(playerID, 1, "Kakaru (Twilight)", x, y);
                trg.Shape_Square(playerID, 1, "Kakaru (Twilight)", x, y)
                # (Line 71) KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", playerID);
                # (Line 72) }
                DoActions(KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", playerID))
                # (Line 73) else if (v.P_LoopMain[playerID] == 4)
            if EUDElseIf()(v.P_LoopMain[playerID] == 4):
                # (Line 74) {
                # (Line 75) trg.Table_Sin(playerID, 0, 150);
                trg.Table_Sin(playerID, 0, 150)
                # (Line 76) trg.Table_Cos(playerID, 0, 150);
                trg.Table_Cos(playerID, 0, 150)
                # (Line 78) var x = v.P_AngleCos[playerID];
                x = EUDVariable()
                x << (v.P_AngleCos[playerID])
                # (Line 79) var y = v.P_AngleSin[playerID];
                y = EUDVariable()
                y << (v.P_AngleSin[playerID])
                # (Line 81) trg.Shape_Square(playerID, 1, "40 + 1n Mutalisk", x, y);
                trg.Shape_Square(playerID, 1, "40 + 1n Mutalisk", x, y)
                # (Line 82) trg.Shape_Square(playerID, 1, " Unit. Hoffnung 25000", x, y);
                trg.Shape_Square(playerID, 1, " Unit. Hoffnung 25000", x, y)
                # (Line 83) KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", playerID);
                # (Line 85) trg.Table_Sin(playerID, 45, 150);
                DoActions(KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", playerID))
                trg.Table_Sin(playerID, 45, 150)
                # (Line 86) trg.Table_Cos(playerID, 45, 150);
                trg.Table_Cos(playerID, 45, 150)
                # (Line 88) x = v.P_AngleCos[playerID];
                x << (v.P_AngleCos[playerID])
                # (Line 89) y = v.P_AngleSin[playerID];
                y << (v.P_AngleSin[playerID])
                # (Line 91) trg.Shape_Square(playerID, 1, "40 + 1n Mutalisk", x, y);
                trg.Shape_Square(playerID, 1, "40 + 1n Mutalisk", x, y)
                # (Line 92) trg.Shape_Square(playerID, 1, " Unit. Hoffnung 25000", x, y);
                trg.Shape_Square(playerID, 1, " Unit. Hoffnung 25000", x, y)
                # (Line 93) KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", playerID);
                # (Line 95) MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
                DoActions(KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", playerID))
                # (Line 96) Order("40 + 1n Mutalisk", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                DoActions(MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere"))
                # (Line 97) }
                DoActions(Order("40 + 1n Mutalisk", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                # (Line 98) else if (v.P_LoopMain[playerID] == 6)
            if EUDElseIf()(v.P_LoopMain[playerID] == 6):
                # (Line 99) {
                # (Line 100) trg.Table_Sin(playerID, 0, 150);
                trg.Table_Sin(playerID, 0, 150)
                # (Line 101) trg.Table_Cos(playerID, 0, 150);
                trg.Table_Cos(playerID, 0, 150)
                # (Line 103) var x = v.P_AngleCos[playerID];
                x = EUDVariable()
                x << (v.P_AngleCos[playerID])
                # (Line 104) var y = v.P_AngleSin[playerID];
                y = EUDVariable()
                y << (v.P_AngleSin[playerID])
                # (Line 106) trg.Shape_Square(playerID, 1, "50 + 1n Tank", x, y);
                trg.Shape_Square(playerID, 1, "50 + 1n Tank", x, y)
                # (Line 107) KillUnitAt(All, "50 + 1n Tank", "Anywhere", playerID);
                # (Line 109) trg.Table_Sin(playerID, 45, 150);
                DoActions(KillUnitAt(All, "50 + 1n Tank", "Anywhere", playerID))
                trg.Table_Sin(playerID, 45, 150)
                # (Line 110) trg.Table_Cos(playerID, 45, 150);
                trg.Table_Cos(playerID, 45, 150)
                # (Line 112) x = v.P_AngleCos[playerID];
                x << (v.P_AngleCos[playerID])
                # (Line 113) y = v.P_AngleSin[playerID];
                y << (v.P_AngleSin[playerID])
                # (Line 115) trg.Shape_Square(playerID, 1, "50 + 1n Tank", x, y);
                trg.Shape_Square(playerID, 1, "50 + 1n Tank", x, y)
                # (Line 116) KillUnitAt(All, "50 + 1n Tank", "Anywhere", playerID);
                # (Line 117) }
                DoActions(KillUnitAt(All, "50 + 1n Tank", "Anywhere", playerID))
                # (Line 118) trg.Main_Wait(80);
            EUDEndIf()
            trg.Main_Wait(80)
            # (Line 120) v.P_LoopMain[playerID] += 1;
            _ARRW(v.P_LoopMain, playerID).__iadd__(1)
            # (Line 122) if (v.P_LoopMain[playerID] == 8)
            if EUDIf()(v.P_LoopMain[playerID] == 8):
                # (Line 123) {
                # (Line 124) v.P_CountMain[playerID] += 1;
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 125) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 126) }
                # (Line 127) }
            EUDEndIf()
            # (Line 128) else if (v.P_CountMain[playerID] == 1)
        if EUDElseIf()(v.P_CountMain[playerID] == 1):
            # (Line 129) {
            # (Line 130) if (v.P_LoopMain[playerID] < 8)
            if EUDIf()(v.P_LoopMain[playerID] >= 8, neg=True):
                # (Line 131) {
                # (Line 132) trg.Table_Sin(playerID, 450 - 45 * v.P_LoopMain[playerID], 150);
                trg.Table_Sin(playerID, 450 - 45 * v.P_LoopMain[playerID], 150)
                # (Line 133) trg.Table_Cos(playerID, 450 - 45 * v.P_LoopMain[playerID], 150);
                trg.Table_Cos(playerID, 450 - 45 * v.P_LoopMain[playerID], 150)
                # (Line 135) var x = v.P_AngleCos[playerID];
                x = EUDVariable()
                x << (v.P_AngleCos[playerID])
                # (Line 136) var y = v.P_AngleSin[playerID];
                y = EUDVariable()
                y << (v.P_AngleSin[playerID])
                # (Line 138) trg.Shape_Dot(playerID, 1, "40 + 1n Gantrithor", x, y);
                trg.Shape_Dot(playerID, 1, "40 + 1n Gantrithor", x, y)
                # (Line 139) KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", playerID);
                # (Line 140) }
                DoActions(KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", playerID))
                # (Line 142) trg.Main_Wait(80);
            EUDEndIf()
            trg.Main_Wait(80)
            # (Line 144) v.P_LoopMain[playerID] += 1;
            _ARRW(v.P_LoopMain, playerID).__iadd__(1)
            # (Line 146) if (v.P_LoopMain[playerID] == 8)
            if EUDIf()(v.P_LoopMain[playerID] == 8):
                # (Line 147) {
                # (Line 148) v.P_CountMain[playerID] += 1;
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 149) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 150) }
                # (Line 151) }
            EUDEndIf()
            # (Line 152) else if (v.P_CountMain[playerID] == 2)
        if EUDElseIf()(v.P_CountMain[playerID] == 2):
            # (Line 153) {
            # (Line 154) if (v.P_LoopMain[playerID] == 0)
            if EUDIf()(v.P_LoopMain[playerID] == 0):
                # (Line 155) {
                # (Line 156) trg.Table_Sin(playerID, 0, 75);
                trg.Table_Sin(playerID, 0, 75)
                # (Line 157) trg.Table_Cos(playerID, 0, 75);
                trg.Table_Cos(playerID, 0, 75)
                # (Line 159) var x = v.P_AngleCos[playerID];
                x = EUDVariable()
                x << (v.P_AngleCos[playerID])
                # (Line 160) var y = v.P_AngleSin[playerID];
                y = EUDVariable()
                y << (v.P_AngleSin[playerID])
                # (Line 162) trg.Shape_Square(playerID, 1, "80 + 1n Mutalisk", x, y);
                trg.Shape_Square(playerID, 1, "80 + 1n Mutalisk", x, y)
                # (Line 163) KillUnitAt(All, "80 + 1n Mutalisk", "Anywhere", playerID);
                # (Line 165) trg.Table_Sin(playerID, 45, 75);
                DoActions(KillUnitAt(All, "80 + 1n Mutalisk", "Anywhere", playerID))
                trg.Table_Sin(playerID, 45, 75)
                # (Line 166) trg.Table_Cos(playerID, 45, 75);
                trg.Table_Cos(playerID, 45, 75)
                # (Line 168) x = v.P_AngleCos[playerID];
                x << (v.P_AngleCos[playerID])
                # (Line 169) y = v.P_AngleSin[playerID];
                y << (v.P_AngleSin[playerID])
                # (Line 171) trg.Shape_Square(playerID, 1, "80 + 1n Mutalisk", x, y);
                trg.Shape_Square(playerID, 1, "80 + 1n Mutalisk", x, y)
                # (Line 172) KillUnitAt(All, "80 + 1n Mutalisk", "Anywhere", playerID);
                # (Line 173) }
                DoActions(KillUnitAt(All, "80 + 1n Mutalisk", "Anywhere", playerID))
                # (Line 174) else if (v.P_LoopMain[playerID] == 2)
            if EUDElseIf()(v.P_LoopMain[playerID] == 2):
                # (Line 175) {
                # (Line 176) trg.Table_Sin(playerID, 0, 150);
                trg.Table_Sin(playerID, 0, 150)
                # (Line 177) trg.Table_Cos(playerID, 0, 150);
                trg.Table_Cos(playerID, 0, 150)
                # (Line 179) var x = v.P_AngleCos[playerID];
                x = EUDVariable()
                x << (v.P_AngleCos[playerID])
                # (Line 180) var y = v.P_AngleSin[playerID];
                y = EUDVariable()
                y << (v.P_AngleSin[playerID])
                # (Line 182) trg.Shape_Square(playerID, 1, "50 + 1n Battlecruiser", x, y);
                trg.Shape_Square(playerID, 1, "50 + 1n Battlecruiser", x, y)
                # (Line 183) trg.Shape_Square(playerID, 1, "40 + 1n Goliath", x, y);
                trg.Shape_Square(playerID, 1, "40 + 1n Goliath", x, y)
                # (Line 184) KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID);
                # (Line 186) trg.Table_Sin(playerID, 45, 150);
                DoActions(KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID))
                trg.Table_Sin(playerID, 45, 150)
                # (Line 187) trg.Table_Cos(playerID, 45, 150);
                trg.Table_Cos(playerID, 45, 150)
                # (Line 189) x = v.P_AngleCos[playerID];
                x << (v.P_AngleCos[playerID])
                # (Line 190) y = v.P_AngleSin[playerID];
                y << (v.P_AngleSin[playerID])
                # (Line 192) trg.Shape_Square(playerID, 1, "50 + 1n Battlecruiser", x, y);
                trg.Shape_Square(playerID, 1, "50 + 1n Battlecruiser", x, y)
                # (Line 193) trg.Shape_Square(playerID, 1, "40 + 1n Goliath", x, y);
                trg.Shape_Square(playerID, 1, "40 + 1n Goliath", x, y)
                # (Line 194) KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID);
                # (Line 196) MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
                DoActions(KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID))
                # (Line 197) MoveUnit(All, "40 + 1n Goliath", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
                DoActions(MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere"))
                # (Line 198) Order("40 + 1n Goliath", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                DoActions(MoveUnit(All, "40 + 1n Goliath", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]))
                # (Line 199) }
                DoActions(Order("40 + 1n Goliath", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                # (Line 200) else if (v.P_LoopMain[playerID] == 3)
            if EUDElseIf()(v.P_LoopMain[playerID] == 3):
                # (Line 201) {
                # (Line 202) RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", playerID);
                # (Line 203) }
                DoActions(RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", playerID))
                # (Line 205) trg.Main_Wait(80);
            EUDEndIf()
            trg.Main_Wait(80)
            # (Line 207) v.P_LoopMain[playerID] += 1;
            _ARRW(v.P_LoopMain, playerID).__iadd__(1)
            # (Line 209) if (v.P_LoopMain[playerID] == 10)
            if EUDIf()(v.P_LoopMain[playerID] == 10):
                # (Line 210) {
                # (Line 211) v.P_CountMain[playerID] += 1;
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 212) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 213) }
                # (Line 214) }
            EUDEndIf()
            # (Line 215) else if (v.P_CountMain[playerID] == 3)
        if EUDElseIf()(v.P_CountMain[playerID] == 3):
            # (Line 216) {
            # (Line 217) if (v.P_LoopMain[playerID] < 8)
            if EUDIf()(v.P_LoopMain[playerID] >= 8, neg=True):
                # (Line 218) {
                # (Line 219) trg.MoveLoc("40 + 1n Mutalisk", playerID, 0, 0);
                trg.MoveLoc("40 + 1n Mutalisk", playerID, 0, 0)
                # (Line 220) RemoveUnitAt(1, "40 + 1n Mutalisk", "Anywhere", playerID);
                # (Line 221) trg.SkillUnit(playerID, 1, "40 + 1n Drone");
                DoActions(RemoveUnitAt(1, "40 + 1n Mutalisk", "Anywhere", playerID))
                trg.SkillUnit(playerID, 1, "40 + 1n Drone")
                # (Line 222) trg.SkillUnit(playerID, 1, " Unit. Hoffnung 25000");
                trg.SkillUnit(playerID, 1, " Unit. Hoffnung 25000")
                # (Line 224) if (v.P_LoopMain[playerID] % 2 == 0)
                if EUDIf()(v.P_LoopMain[playerID] % 2 == 0):
                    # (Line 225) {
                    # (Line 226) trg.SkillUnit(playerID, 1, "40 + 1n Gantrithor");
                    trg.SkillUnit(playerID, 1, "40 + 1n Gantrithor")
                    # (Line 227) }
                    # (Line 228) else if (v.P_LoopMain[playerID] % 2 == 1)
                if EUDElseIf()(v.P_LoopMain[playerID] % 2 == 1):
                    # (Line 229) {
                    # (Line 230) trg.SkillUnit(playerID, 1, "50 + 1n Battlecruiser");
                    trg.SkillUnit(playerID, 1, "50 + 1n Battlecruiser")
                    # (Line 231) }
                    # (Line 233) KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", playerID);
                EUDEndIf()
                # (Line 234) KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", playerID))
                # (Line 235) KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID))
                # (Line 237) MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
                DoActions(KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", playerID))
                # (Line 238) MoveUnit(All, "40 + 1n Drone", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
                DoActions(MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere"))
                # (Line 239) }
                DoActions(MoveUnit(All, "40 + 1n Drone", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]))
                # (Line 241) trg.Main_Wait(80);
            EUDEndIf()
            trg.Main_Wait(80)
            # (Line 243) v.P_LoopMain[playerID] += 1;
            _ARRW(v.P_LoopMain, playerID).__iadd__(1)
            # (Line 245) if (v.P_LoopMain[playerID] == 16)
            if EUDIf()(v.P_LoopMain[playerID] == 16):
                # (Line 246) {
                # (Line 247) v.P_CountMain[playerID] += 1;
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 248) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 249) }
                # (Line 250) }
            EUDEndIf()
            # (Line 251) else if (v.P_CountMain[playerID] == 4)
        if EUDElseIf()(v.P_CountMain[playerID] == 4):
            # (Line 252) {
            # (Line 253) if (v.P_LoopMain[playerID] == 0)
            if EUDIf()(v.P_LoopMain[playerID] == 0):
                # (Line 254) {
                # (Line 255) for (var i = 0; i < 8; i++)
                i = EUDVariable()
                i << (0)
                if EUDWhile()(i >= 8, neg=True):
                    def _t24():
                        i.__iadd__(1)
                    # (Line 256) {
                    # (Line 257) trg.MoveLoc("40 + 1n Drone", playerID, 0, 0);
                    trg.MoveLoc("40 + 1n Drone", playerID, 0, 0)
                    # (Line 258) RemoveUnitAt(1, "40 + 1n Drone", "Anywhere", playerID);
                    # (Line 259) trg.SkillUnit(playerID, 1, "40 + 1n Mojo");
                    DoActions(RemoveUnitAt(1, "40 + 1n Drone", "Anywhere", playerID))
                    trg.SkillUnit(playerID, 1, "40 + 1n Mojo")
                    # (Line 260) trg.SkillUnit(playerID, 1, "60 + 1n Hydralisk");
                    trg.SkillUnit(playerID, 1, "60 + 1n Hydralisk")
                    # (Line 261) }
                    # (Line 263) KillUnitAt(All, "60 + 1n Hydralisk", "Anywhere", playerID);
                    EUDSetContinuePoint()
                    _t24()
                EUDEndWhile()
                # (Line 265) MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
                DoActions(KillUnitAt(All, "60 + 1n Hydralisk", "Anywhere", playerID))
                # (Line 266) Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                DoActions(MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere"))
                # (Line 267) }
                DoActions(Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                # (Line 268) if (v.P_LoopMain[playerID] == 1)
            EUDEndIf()
            if EUDIf()(v.P_LoopMain[playerID] == 1):
                # (Line 269) {
                # (Line 270) for (var i = 0; i < 8; i++)
                i = EUDVariable()
                i << (0)
                if EUDWhile()(i >= 8, neg=True):
                    def _t27():
                        i.__iadd__(1)
                    # (Line 271) {
                    # (Line 272) trg.MoveLoc("40 + 1n Mojo", playerID, 0, 0);
                    trg.MoveLoc("40 + 1n Mojo", playerID, 0, 0)
                    # (Line 273) RemoveUnitAt(1, "40 + 1n Mojo", "Anywhere", playerID);
                    # (Line 274) trg.SkillUnit(playerID, 1, "Kakaru (Twilight)");
                    DoActions(RemoveUnitAt(1, "40 + 1n Mojo", "Anywhere", playerID))
                    trg.SkillUnit(playerID, 1, "Kakaru (Twilight)")
                    # (Line 275) }
                    # (Line 277) KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", playerID);
                    EUDSetContinuePoint()
                    _t27()
                EUDEndWhile()
                # (Line 278) }
                DoActions(KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", playerID))
                # (Line 279) trg.Main_Wait(80);
            EUDEndIf()
            trg.Main_Wait(80)
            # (Line 281) v.P_LoopMain[playerID] += 1;
            _ARRW(v.P_LoopMain, playerID).__iadd__(1)
            # (Line 283) if (v.P_LoopMain[playerID] == 2)
            if EUDIf()(v.P_LoopMain[playerID] == 2):
                # (Line 284) {
                # (Line 285) v.P_CountMain[playerID] += 1;
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 286) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 287) }
                # (Line 288) }
            EUDEndIf()
            # (Line 289) else if (v.P_CountMain[playerID] == 5)
        if EUDElseIf()(v.P_CountMain[playerID] == 5):
            # (Line 290) {
            # (Line 291) trg.SkillEnd();
            trg.SkillEnd()
            # (Line 292) }
            # (Line 293) }
        EUDEndIf()
        # (Line 294) }
    EUDEndIf()