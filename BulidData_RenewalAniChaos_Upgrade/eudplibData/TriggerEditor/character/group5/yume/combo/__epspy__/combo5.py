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
    # (Line 7) trg.Buff_ShieldFix(1);
    trg.Buff_ShieldFix(1)
    # (Line 9) if (v.P_WaitMain[playerID] == 0)
    if EUDIf()(v.P_WaitMain[playerID] == 0):
        # (Line 10) {
        # (Line 11) if (v.P_CountMain[playerID] == 0)
        if EUDIf()(v.P_CountMain[playerID] == 0):
            # (Line 12) {
            # (Line 13) if (v.P_LoopMain[playerID] < 3)
            if EUDIf()(v.P_LoopMain[playerID] >= 3, neg=True):
                # (Line 14) {
                # (Line 15) SetDeaths(playerID, SetTo, 1, " `ShieldRecharge");
                # (Line 17) trg.Shape_Line(playerID, 1, "40 + 1n Mutalisk", 45 * v.P_LoopMain[playerID], 9, 50, 0);
                DoActions(SetDeaths(playerID, SetTo, 1, " `ShieldRecharge"))
                trg.Shape_Line(playerID, 1, "40 + 1n Mutalisk", 45 * v.P_LoopMain[playerID], 9, 50, 0)
                # (Line 18) trg.Shape_Line(playerID, 1, "40 + 1n Mutalisk", 45 * v.P_LoopMain[playerID], 9, 50, 75);
                trg.Shape_Line(playerID, 1, "40 + 1n Mutalisk", 45 * v.P_LoopMain[playerID], 9, 50, 75)
                # (Line 19) trg.Shape_Line(playerID, 1, "40 + 1n Mutalisk", 45 * v.P_LoopMain[playerID] + 180, 9, 50, 75);
                trg.Shape_Line(playerID, 1, "40 + 1n Mutalisk", 45 * v.P_LoopMain[playerID] + 180, 9, 50, 75)
                # (Line 20) trg.Shape_Line(playerID, 1, "60 + 1n Archon", 45 * v.P_LoopMain[playerID], 7, 75, 0);
                trg.Shape_Line(playerID, 1, "60 + 1n Archon", 45 * v.P_LoopMain[playerID], 7, 75, 0)
                # (Line 21) trg.Shape_Line(playerID, 1, "60 + 1n Archon", 45 * v.P_LoopMain[playerID], 7, 75, 75);
                trg.Shape_Line(playerID, 1, "60 + 1n Archon", 45 * v.P_LoopMain[playerID], 7, 75, 75)
                # (Line 22) trg.Shape_Line(playerID, 1, "60 + 1n Archon", 45 * v.P_LoopMain[playerID] + 180, 7, 75, 75);
                trg.Shape_Line(playerID, 1, "60 + 1n Archon", 45 * v.P_LoopMain[playerID] + 180, 7, 75, 75)
                # (Line 24) KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", playerID);
                # (Line 25) KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", playerID))
                # (Line 27) trg.Main_Wait(80);
                DoActions(KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID))
                trg.Main_Wait(80)
                # (Line 29) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 30) }
                # (Line 31) else if (v.P_LoopMain[playerID] == 3)
            if EUDElseIf()(v.P_LoopMain[playerID] == 3):
                # (Line 32) {
                # (Line 33) trg.Shape_Line(playerID, 1, "40 + 1n Mutalisk", 45 * v.P_LoopMain[playerID], 9, 50, 0);
                trg.Shape_Line(playerID, 1, "40 + 1n Mutalisk", 45 * v.P_LoopMain[playerID], 9, 50, 0)
                # (Line 34) trg.Shape_Line(playerID, 1, "40 + 1n Mutalisk", 45 * v.P_LoopMain[playerID], 9, 50, 75);
                trg.Shape_Line(playerID, 1, "40 + 1n Mutalisk", 45 * v.P_LoopMain[playerID], 9, 50, 75)
                # (Line 35) trg.Shape_Line(playerID, 1, "40 + 1n Mutalisk", 45 * v.P_LoopMain[playerID] + 180, 9, 50, 75);
                trg.Shape_Line(playerID, 1, "40 + 1n Mutalisk", 45 * v.P_LoopMain[playerID] + 180, 9, 50, 75)
                # (Line 36) trg.Shape_Line(playerID, 1, "60 + 1n Archon", 45 * v.P_LoopMain[playerID], 7, 75, 0);
                trg.Shape_Line(playerID, 1, "60 + 1n Archon", 45 * v.P_LoopMain[playerID], 7, 75, 0)
                # (Line 37) trg.Shape_Line(playerID, 1, "60 + 1n Archon", 45 * v.P_LoopMain[playerID], 7, 75, 75);
                trg.Shape_Line(playerID, 1, "60 + 1n Archon", 45 * v.P_LoopMain[playerID], 7, 75, 75)
                # (Line 38) trg.Shape_Line(playerID, 1, "60 + 1n Archon", 45 * v.P_LoopMain[playerID] + 180, 7, 75, 75);
                trg.Shape_Line(playerID, 1, "60 + 1n Archon", 45 * v.P_LoopMain[playerID] + 180, 7, 75, 75)
                # (Line 40) KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", playerID);
                # (Line 41) KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", playerID))
                # (Line 43) trg.Main_Wait(80);
                DoActions(KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID))
                trg.Main_Wait(80)
                # (Line 45) v.P_CountMain[playerID] += 1;
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 46) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 47) }
                # (Line 48) }
            EUDEndIf()
            # (Line 49) else if (v.P_CountMain[playerID] == 1)
        if EUDElseIf()(v.P_CountMain[playerID] == 1):
            # (Line 50) {
            # (Line 51) if (v.P_LoopMain[playerID] < 8)
            if EUDIf()(v.P_LoopMain[playerID] >= 8, neg=True):
                # (Line 52) {
                # (Line 53) if (v.P_LoopMain[playerID] == 0)
                if EUDIf()(v.P_LoopMain[playerID] == 0):
                    # (Line 54) {
                    # (Line 55) trg.Shape_Line(playerID, 1, "50 + 1n Battlecruiser", 45, 7, 75, 0);
                    trg.Shape_Line(playerID, 1, "50 + 1n Battlecruiser", 45, 7, 75, 0)
                    # (Line 56) trg.Shape_Line(playerID, 1, "50 + 1n Battlecruiser", 45, 7, 75, 75);
                    trg.Shape_Line(playerID, 1, "50 + 1n Battlecruiser", 45, 7, 75, 75)
                    # (Line 57) trg.Shape_Line(playerID, 1, "50 + 1n Battlecruiser", 225, 7, 75, 75);
                    trg.Shape_Line(playerID, 1, "50 + 1n Battlecruiser", 225, 7, 75, 75)
                    # (Line 58) trg.Shape_Line(playerID, 1, " Unit. Hoffnung 25000", 45, 7, 75, 0);
                    trg.Shape_Line(playerID, 1, " Unit. Hoffnung 25000", 45, 7, 75, 0)
                    # (Line 59) trg.Shape_Line(playerID, 1, " Unit. Hoffnung 25000", 45, 7, 75, 75);
                    trg.Shape_Line(playerID, 1, " Unit. Hoffnung 25000", 45, 7, 75, 75)
                    # (Line 60) trg.Shape_Line(playerID, 1, " Unit. Hoffnung 25000", 225, 7, 75, 75);
                    trg.Shape_Line(playerID, 1, " Unit. Hoffnung 25000", 225, 7, 75, 75)
                    # (Line 62) KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", playerID);
                    # (Line 64) MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
                    DoActions(KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", playerID))
                    # (Line 65) Order("50 + 1n Battlecruiser", playerID, "Anywhere", Attack, "Anywhere");
                    DoActions(MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere"))
                    # (Line 66) }
                    DoActions(Order("50 + 1n Battlecruiser", playerID, "Anywhere", Attack, "Anywhere"))
                    # (Line 67) if (v.P_LoopMain[playerID] % 2 == 0)
                EUDEndIf()
                if EUDIf()(v.P_LoopMain[playerID] % 2 == 0):
                    # (Line 68) {
                    # (Line 69) RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);
                    # (Line 71) trg.Shape_Square(playerID, 1, "40 + 1n Wraith", 160 - 40 * v.P_LoopMain[playerID], 160);
                    DoActions(RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID))
                    trg.Shape_Square(playerID, 1, "40 + 1n Wraith", 160 - 40 * v.P_LoopMain[playerID], 160)
                    # (Line 73) MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
                    # (Line 74) Order("40 + 1n Wraith", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                    DoActions(MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere"))
                    # (Line 76) trg.Table_Sin(playerID, 22 + 45 * v.P_LoopMain[playerID], 50 + 25 * v.P_LoopMain[playerID]);
                    DoActions(Order("40 + 1n Wraith", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                    trg.Table_Sin(playerID, 22 + 45 * v.P_LoopMain[playerID], 50 + 25 * v.P_LoopMain[playerID])
                    # (Line 77) trg.Table_Cos(playerID, 22 + 45 * v.P_LoopMain[playerID], 50 + 25 * v.P_LoopMain[playerID]);
                    trg.Table_Cos(playerID, 22 + 45 * v.P_LoopMain[playerID], 50 + 25 * v.P_LoopMain[playerID])
                    # (Line 79) trg.Shape_Square(playerID, 1, "60 + 1n Archon", v.P_AngleCos[playerID], v.P_AngleSin[playerID]);
                    trg.Shape_Square(playerID, 1, "60 + 1n Archon", v.P_AngleCos[playerID], v.P_AngleSin[playerID])
                    # (Line 80) }
                    # (Line 81) else if (v.P_LoopMain[playerID] % 2 == 1)
                if EUDElseIf()(v.P_LoopMain[playerID] % 2 == 1):
                    # (Line 82) {
                    # (Line 83) trg.Shape_Square(playerID, 1, "40 + 1n Mojo", 160 - 40 * v.P_LoopMain[playerID], 160);
                    trg.Shape_Square(playerID, 1, "40 + 1n Mojo", 160 - 40 * v.P_LoopMain[playerID], 160)
                    # (Line 84) KillUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID);
                    # (Line 86) trg.Table_Sin(playerID, 45 * v.P_LoopMain[playerID], 50 + 25 * v.P_LoopMain[playerID]);
                    DoActions(KillUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID))
                    trg.Table_Sin(playerID, 45 * v.P_LoopMain[playerID], 50 + 25 * v.P_LoopMain[playerID])
                    # (Line 87) trg.Table_Cos(playerID, 45 * v.P_LoopMain[playerID], 50 + 25 * v.P_LoopMain[playerID]);
                    trg.Table_Cos(playerID, 45 * v.P_LoopMain[playerID], 50 + 25 * v.P_LoopMain[playerID])
                    # (Line 89) trg.Shape_Square(playerID, 1, "Protoss Dark Archon", v.P_AngleCos[playerID], v.P_AngleSin[playerID]);
                    trg.Shape_Square(playerID, 1, "Protoss Dark Archon", v.P_AngleCos[playerID], v.P_AngleSin[playerID])
                    # (Line 90) }
                    # (Line 92) trg.Shape_Square(playerID, 1, " Unit. Hoffnung 25000", 160 - 40 * v.P_LoopMain[playerID], 160);
                EUDEndIf()
                trg.Shape_Square(playerID, 1, " Unit. Hoffnung 25000", 160 - 40 * v.P_LoopMain[playerID], 160)
                # (Line 94) KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", playerID);
                # (Line 95) KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
                DoActions(KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", playerID))
                # (Line 96) KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID))
                # (Line 98) trg.Main_Wait(80);
                DoActions(KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID))
                trg.Main_Wait(80)
                # (Line 100) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 101) }
                # (Line 102) else if (v.P_LoopMain[playerID] == 8)
            if EUDElseIf()(v.P_LoopMain[playerID] == 8):
                # (Line 103) {
                # (Line 104) KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID);
                # (Line 106) trg.Shape_Edge(playerID, 1, "40 + 1n Mutalisk", 45, 7, 160);
                DoActions(KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID))
                trg.Shape_Edge(playerID, 1, "40 + 1n Mutalisk", 45, 7, 160)
                # (Line 107) KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", playerID);
                # (Line 109) trg.Main_Wait(80);
                DoActions(KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", playerID))
                trg.Main_Wait(80)
                # (Line 111) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 112) }
                # (Line 113) else if (v.P_LoopMain[playerID] == 9)
            if EUDElseIf()(v.P_LoopMain[playerID] == 9):
                # (Line 114) {
                # (Line 115) trg.Shape_Edge(playerID, 1, "Kakaru (Twilight)", 45, 7, 160);
                trg.Shape_Edge(playerID, 1, "Kakaru (Twilight)", 45, 7, 160)
                # (Line 116) KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", playerID);
                # (Line 118) trg.Shape_Edge(playerID, 1, "40 + 1n Ghost", 45, 5, 200);
                DoActions(KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", playerID))
                trg.Shape_Edge(playerID, 1, "40 + 1n Ghost", 45, 5, 200)
                # (Line 120) trg.Shape_Edge(playerID, 1, "40 + 1n Wraith", 45, 7, 160);
                trg.Shape_Edge(playerID, 1, "40 + 1n Wraith", 45, 7, 160)
                # (Line 121) trg.Shape_Edge(playerID, 1, "40 + 1n Drone", 45, 7, 160);
                trg.Shape_Edge(playerID, 1, "40 + 1n Drone", 45, 7, 160)
                # (Line 122) KillUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);
                # (Line 123) KillUnitAt(All, "40 + 1n Drone", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID))
                # (Line 125) MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
                DoActions(KillUnitAt(All, "40 + 1n Drone", "Anywhere", playerID))
                # (Line 126) MoveUnit(All, "40 + 1n Ghost", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
                DoActions(MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere"))
                # (Line 127) Order("40 + 1n Ghost", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                DoActions(MoveUnit(All, "40 + 1n Ghost", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]))
                # (Line 129) trg.Main_Wait(400);
                DoActions(Order("40 + 1n Ghost", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                trg.Main_Wait(400)
                # (Line 131) v.P_CountMain[playerID] += 1;
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 132) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 133) }
                # (Line 134) }
            EUDEndIf()
            # (Line 135) else if (v.P_CountMain[playerID] == 2)
        if EUDElseIf()(v.P_CountMain[playerID] == 2):
            # (Line 136) {
            # (Line 137) if (v.P_LoopMain[playerID] == 0)
            if EUDIf()(v.P_LoopMain[playerID] == 0):
                # (Line 138) {
                # (Line 139) trg.Shape_Line(playerID, 1, "40 + 1n Wraith", 45, 5, 75, 0);
                trg.Shape_Line(playerID, 1, "40 + 1n Wraith", 45, 5, 75, 0)
                # (Line 140) trg.Shape_Line(playerID, 1, "Protoss Dark Archon", 45, 7, 50, 75);
                trg.Shape_Line(playerID, 1, "Protoss Dark Archon", 45, 7, 50, 75)
                # (Line 141) trg.Shape_Line(playerID, 1, "Protoss Dark Archon", 225, 7, 50, 75);
                trg.Shape_Line(playerID, 1, "Protoss Dark Archon", 225, 7, 50, 75)
                # (Line 143) MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
                # (Line 144) Order("40 + 1n Wraith", playerID, "Anywhere", Attack, "Anywhere");
                DoActions(MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere"))
                # (Line 146) KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID);
                DoActions(Order("40 + 1n Wraith", playerID, "Anywhere", Attack, "Anywhere"))
                # (Line 148) trg.Main_Wait(160);
                DoActions(KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID))
                trg.Main_Wait(160)
                # (Line 150) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 151) }
                # (Line 152) else if (v.P_LoopMain[playerID] == 1)
            if EUDElseIf()(v.P_LoopMain[playerID] == 1):
                # (Line 153) {
                # (Line 154) RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);
                # (Line 156) trg.Shape_Line(playerID, 1, "40 + 1n Wraith", 45, 5, 75, 75);
                DoActions(RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID))
                trg.Shape_Line(playerID, 1, "40 + 1n Wraith", 45, 5, 75, 75)
                # (Line 157) trg.Shape_Line(playerID, 1, "40 + 1n Wraith", 225, 5, 75, 75);
                trg.Shape_Line(playerID, 1, "40 + 1n Wraith", 225, 5, 75, 75)
                # (Line 158) trg.Shape_Line(playerID, 1, "50 + 1n Tank", 45, 7, 50, 150);
                trg.Shape_Line(playerID, 1, "50 + 1n Tank", 45, 7, 50, 150)
                # (Line 159) trg.Shape_Line(playerID, 1, "50 + 1n Tank", 225, 7, 50, 150);
                trg.Shape_Line(playerID, 1, "50 + 1n Tank", 225, 7, 50, 150)
                # (Line 161) trg.Shape_Double(playerID, 1, "40 + 1n Mutalisk", 50, 50);
                trg.Shape_Double(playerID, 1, "40 + 1n Mutalisk", 50, 50)
                # (Line 162) trg.Shape_Double(playerID, 1, "40 + 1n Mutalisk", 125, 125);
                trg.Shape_Double(playerID, 1, "40 + 1n Mutalisk", 125, 125)
                # (Line 164) trg.Shape_Double(playerID, 1, "60 + 1n High Templar", 50, 50);
                trg.Shape_Double(playerID, 1, "60 + 1n High Templar", 50, 50)
                # (Line 165) trg.Shape_Double(playerID, 1, "60 + 1n High Templar", 125, 125);
                trg.Shape_Double(playerID, 1, "60 + 1n High Templar", 125, 125)
                # (Line 167) MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
                # (Line 168) Order("40 + 1n Wraith", playerID, "Anywhere", Attack, "Anywhere");
                DoActions(MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere"))
                # (Line 170) KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", playerID);
                DoActions(Order("40 + 1n Wraith", playerID, "Anywhere", Attack, "Anywhere"))
                # (Line 171) KillUnitAt(All, "50 + 1n Tank", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", playerID))
                # (Line 172) KillUnitAt(All, "60 + 1n High Templar", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "50 + 1n Tank", "Anywhere", playerID))
                # (Line 174) trg.Main_Wait(160);
                DoActions(KillUnitAt(All, "60 + 1n High Templar", "Anywhere", playerID))
                trg.Main_Wait(160)
                # (Line 176) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 177) }
                # (Line 178) else if (v.P_LoopMain[playerID] == 2)
            if EUDElseIf()(v.P_LoopMain[playerID] == 2):
                # (Line 179) {
                # (Line 180) RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);
                # (Line 182) trg.Shape_Line(playerID, 1, "40 + 1n Wraith", 135, 5, 75, 0);
                DoActions(RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID))
                trg.Shape_Line(playerID, 1, "40 + 1n Wraith", 135, 5, 75, 0)
                # (Line 183) trg.Shape_Line(playerID, 1, "Protoss Dark Archon", 135, 7, 50, 75);
                trg.Shape_Line(playerID, 1, "Protoss Dark Archon", 135, 7, 50, 75)
                # (Line 184) trg.Shape_Line(playerID, 1, "Protoss Dark Archon", 315, 7, 50, 75);
                trg.Shape_Line(playerID, 1, "Protoss Dark Archon", 315, 7, 50, 75)
                # (Line 186) MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
                # (Line 187) Order("40 + 1n Wraith", playerID, "Anywhere", Attack, "Anywhere");
                DoActions(MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere"))
                # (Line 189) KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID);
                DoActions(Order("40 + 1n Wraith", playerID, "Anywhere", Attack, "Anywhere"))
                # (Line 191) trg.Main_Wait(160);
                DoActions(KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID))
                trg.Main_Wait(160)
                # (Line 193) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 194) }
                # (Line 195) else if (v.P_LoopMain[playerID] == 3)
            if EUDElseIf()(v.P_LoopMain[playerID] == 3):
                # (Line 196) {
                # (Line 197) RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);
                # (Line 199) trg.Shape_Line(playerID, 1, "40 + 1n Wraith", 135, 5, 75, 75);
                DoActions(RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID))
                trg.Shape_Line(playerID, 1, "40 + 1n Wraith", 135, 5, 75, 75)
                # (Line 200) trg.Shape_Line(playerID, 1, "40 + 1n Wraith", 315, 5, 75, 75);
                trg.Shape_Line(playerID, 1, "40 + 1n Wraith", 315, 5, 75, 75)
                # (Line 201) trg.Shape_Line(playerID, 1, "50 + 1n Tank", 135, 7, 50, 150);
                trg.Shape_Line(playerID, 1, "50 + 1n Tank", 135, 7, 50, 150)
                # (Line 202) trg.Shape_Line(playerID, 1, "50 + 1n Tank", 315, 7, 50, 150);
                trg.Shape_Line(playerID, 1, "50 + 1n Tank", 315, 7, 50, 150)
                # (Line 204) trg.Shape_Double(playerID, 1, "40 + 1n Mutalisk", -50, 50);
                trg.Shape_Double(playerID, 1, "40 + 1n Mutalisk", -50, 50)
                # (Line 205) trg.Shape_Double(playerID, 1, "40 + 1n Mutalisk", -125, 125);
                trg.Shape_Double(playerID, 1, "40 + 1n Mutalisk", -125, 125)
                # (Line 207) trg.Shape_Double(playerID, 1, "60 + 1n High Templar", -50, 50);
                trg.Shape_Double(playerID, 1, "60 + 1n High Templar", -50, 50)
                # (Line 208) trg.Shape_Double(playerID, 1, "60 + 1n High Templar", -125, 125);
                trg.Shape_Double(playerID, 1, "60 + 1n High Templar", -125, 125)
                # (Line 210) MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
                # (Line 211) Order("40 + 1n Wraith", playerID, "Anywhere", Attack, "Anywhere");
                DoActions(MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere"))
                # (Line 213) KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", playerID);
                DoActions(Order("40 + 1n Wraith", playerID, "Anywhere", Attack, "Anywhere"))
                # (Line 214) KillUnitAt(All, "50 + 1n Tank", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", playerID))
                # (Line 215) KillUnitAt(All, "60 + 1n High Templar", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "50 + 1n Tank", "Anywhere", playerID))
                # (Line 217) trg.Main_Wait(160);
                DoActions(KillUnitAt(All, "60 + 1n High Templar", "Anywhere", playerID))
                trg.Main_Wait(160)
                # (Line 219) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 220) }
                # (Line 221) else if (v.P_LoopMain[playerID] == 4)
            if EUDElseIf()(v.P_LoopMain[playerID] == 4):
                # (Line 222) {
                # (Line 223) RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);
                # (Line 225) trg.Main_Wait(80);
                DoActions(RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID))
                trg.Main_Wait(80)
                # (Line 227) v.P_CountMain[playerID] += 1;
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 228) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 229) }
                # (Line 230) }
            EUDEndIf()
            # (Line 231) else if (v.P_CountMain[playerID] == 3)
        if EUDElseIf()(v.P_CountMain[playerID] == 3):
            # (Line 232) {
            # (Line 233) if (v.P_LoopMain[playerID] < 4)
            if EUDIf()(v.P_LoopMain[playerID] >= 4, neg=True):
                # (Line 234) {
                # (Line 235) trg.Shape_Line(playerID, 1, "40 + 1n Mutalisk", 180 - 45 * v.P_LoopMain[playerID], 9, 50, 0);
                trg.Shape_Line(playerID, 1, "40 + 1n Mutalisk", 180 - 45 * v.P_LoopMain[playerID], 9, 50, 0)
                # (Line 236) trg.Shape_Line(playerID, 1, "40 + 1n Mutalisk", 180 - 45 * v.P_LoopMain[playerID], 9, 50, 75);
                trg.Shape_Line(playerID, 1, "40 + 1n Mutalisk", 180 - 45 * v.P_LoopMain[playerID], 9, 50, 75)
                # (Line 237) trg.Shape_Line(playerID, 1, "40 + 1n Mutalisk", 180 - 45 * v.P_LoopMain[playerID] + 180, 9, 50, 75);
                trg.Shape_Line(playerID, 1, "40 + 1n Mutalisk", 180 - 45 * v.P_LoopMain[playerID] + 180, 9, 50, 75)
                # (Line 238) trg.Shape_Line(playerID, 1, "60 + 1n Archon", 180 - 45 * v.P_LoopMain[playerID], 7, 75, 0);
                trg.Shape_Line(playerID, 1, "60 + 1n Archon", 180 - 45 * v.P_LoopMain[playerID], 7, 75, 0)
                # (Line 239) trg.Shape_Line(playerID, 1, "60 + 1n Archon", 180 - 45 * v.P_LoopMain[playerID], 7, 75, 75);
                trg.Shape_Line(playerID, 1, "60 + 1n Archon", 180 - 45 * v.P_LoopMain[playerID], 7, 75, 75)
                # (Line 240) trg.Shape_Line(playerID, 1, "60 + 1n Archon", 180 - 45 * v.P_LoopMain[playerID] + 180, 7, 75, 75);
                trg.Shape_Line(playerID, 1, "60 + 1n Archon", 180 - 45 * v.P_LoopMain[playerID] + 180, 7, 75, 75)
                # (Line 242) KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", playerID);
                # (Line 243) KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", playerID))
                # (Line 245) trg.Main_Wait(80);
                DoActions(KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID))
                trg.Main_Wait(80)
                # (Line 247) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 248) }
                # (Line 249) else if (v.P_LoopMain[playerID] == 4)
            if EUDElseIf()(v.P_LoopMain[playerID] == 4):
                # (Line 250) {
                # (Line 251) trg.Shape_Line(playerID, 1, "50 + 1n Battlecruiser", 135, 7, 75, 0);
                trg.Shape_Line(playerID, 1, "50 + 1n Battlecruiser", 135, 7, 75, 0)
                # (Line 252) trg.Shape_Line(playerID, 1, "50 + 1n Battlecruiser", 135, 7, 75, 75);
                trg.Shape_Line(playerID, 1, "50 + 1n Battlecruiser", 135, 7, 75, 75)
                # (Line 253) trg.Shape_Line(playerID, 1, "50 + 1n Battlecruiser", 315, 7, 75, 75);
                trg.Shape_Line(playerID, 1, "50 + 1n Battlecruiser", 315, 7, 75, 75)
                # (Line 254) trg.Shape_Line(playerID, 1, " Unit. Hoffnung 25000", 135, 7, 75, 0);
                trg.Shape_Line(playerID, 1, " Unit. Hoffnung 25000", 135, 7, 75, 0)
                # (Line 255) trg.Shape_Line(playerID, 1, " Unit. Hoffnung 25000", 135, 7, 75, 75);
                trg.Shape_Line(playerID, 1, " Unit. Hoffnung 25000", 135, 7, 75, 75)
                # (Line 256) trg.Shape_Line(playerID, 1, " Unit. Hoffnung 25000", 315, 7, 75, 75);
                trg.Shape_Line(playerID, 1, " Unit. Hoffnung 25000", 315, 7, 75, 75)
                # (Line 258) KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", playerID);
                # (Line 260) MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
                DoActions(KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", playerID))
                # (Line 261) Order("50 + 1n Battlecruiser", playerID, "Anywhere", Attack, "Anywhere");
                DoActions(MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere"))
                # (Line 263) trg.Main_Wait(400);
                DoActions(Order("50 + 1n Battlecruiser", playerID, "Anywhere", Attack, "Anywhere"))
                trg.Main_Wait(400)
                # (Line 265) v.P_CountMain[playerID] += 1;
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 266) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 267) }
                # (Line 268) }
            EUDEndIf()
            # (Line 269) else if (v.P_CountMain[playerID] == 4)
        if EUDElseIf()(v.P_CountMain[playerID] == 4):
            # (Line 270) {
            # (Line 271) KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID);
            # (Line 272) KillUnitAt(All, "40 + 1n Ghost", "Anywhere", playerID);
            DoActions(KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID))
            # (Line 275) trg.SkillEnd();
            DoActions(KillUnitAt(All, "40 + 1n Ghost", "Anywhere", playerID))
            trg.SkillEnd()
            # (Line 276) }
            # (Line 277) }
        EUDEndIf()
        # (Line 278) }
    EUDEndIf()