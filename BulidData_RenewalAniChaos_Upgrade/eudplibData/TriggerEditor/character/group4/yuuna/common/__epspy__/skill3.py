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
            # (Line 11) if (v.P_LoopMain[playerID] < 4)
            if EUDIf()(v.P_LoopMain[playerID] >= 4, neg=True):
                # (Line 12) {
                # (Line 13) trg.Shape_Square(playerID, 1, "60 + 1n Archon", 200 - v.P_LoopMain[playerID] * 50, 0);
                trg.Shape_Square(playerID, 1, "60 + 1n Archon", 200 - v.P_LoopMain[playerID] * 50, 0)
                # (Line 14) KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
                # (Line 16) trg.Main_Wait(50);
                DoActions(KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID))
                trg.Main_Wait(50)
                # (Line 17) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 18) }
                # (Line 19) else if (v.P_LoopMain[playerID] == 4)
            if EUDElseIf()(v.P_LoopMain[playerID] == 4):
                # (Line 20) {
                # (Line 21) trg.Shape_Square(playerID, 4, "60 + 1n Archon", 50, 50);
                trg.Shape_Square(playerID, 4, "60 + 1n Archon", 50, 50)
                # (Line 22) KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
                # (Line 24) trg.Main_Wait(50);
                DoActions(KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID))
                trg.Main_Wait(50)
                # (Line 25) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 26) }
                # (Line 27) else if (v.P_LoopMain[playerID] == 5)
            if EUDElseIf()(v.P_LoopMain[playerID] == 5):
                # (Line 28) {
                # (Line 29) trg.Shape_NxNSquare(playerID, 1, "50 + 1n Battlecruiser", 3, 75);
                trg.Shape_NxNSquare(playerID, 1, "50 + 1n Battlecruiser", 3, 75)
                # (Line 30) Order("50 + 1n Battlecruiser", playerID, "Anywhere", Attack, "Anywhere");
                # (Line 32) trg.Main_Wait(0);
                DoActions(Order("50 + 1n Battlecruiser", playerID, "Anywhere", Attack, "Anywhere"))
                trg.Main_Wait(0)
                # (Line 34) v.P_CountMain[playerID] += 1;
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 35) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 36) }
                # (Line 38) }
            EUDEndIf()
            # (Line 39) else if (v.P_CountMain[playerID] == 1)
        if EUDElseIf()(v.P_CountMain[playerID] == 1):
            # (Line 40) {
            # (Line 41) if (v.P_LoopMain[playerID] < 4)
            if EUDIf()(v.P_LoopMain[playerID] >= 4, neg=True):
                # (Line 42) {
                # (Line 43) v.P_Distance[playerID] = 125;
                _ARRW(v.P_Distance, playerID) << (125)
                # (Line 45) trg.Table_Cos(playerID, 45 + 90 * v.P_LoopMain[playerID], v.P_Distance[playerID]);
                trg.Table_Cos(playerID, 45 + 90 * v.P_LoopMain[playerID], v.P_Distance[playerID])
                # (Line 46) trg.Table_Sin(playerID, 45 + 90 * v.P_LoopMain[playerID], v.P_Distance[playerID]);
                trg.Table_Sin(playerID, 45 + 90 * v.P_LoopMain[playerID], v.P_Distance[playerID])
                # (Line 48) trg.MoveLoc(v.P_UnitID[playerID], playerID, v.P_AngleCos[playerID], v.P_AngleSin[playerID]);
                trg.MoveLoc(v.P_UnitID[playerID], playerID, v.P_AngleCos[playerID], v.P_AngleSin[playerID])
                # (Line 49) trg.SkillUnit(playerID, 1, "40 + 1n Wraith");
                trg.SkillUnit(playerID, 1, "40 + 1n Wraith")
                # (Line 50) trg.SkillUnit(playerID, 1, "40 + 1n Goliath");
                trg.SkillUnit(playerID, 1, "40 + 1n Goliath")
                # (Line 52) v.P_Distance[playerID] = 175;
                _ARRW(v.P_Distance, playerID) << (175)
                # (Line 54) trg.Table_Cos(playerID, 45 + 90 * v.P_LoopMain[playerID], v.P_Distance[playerID]);
                trg.Table_Cos(playerID, 45 + 90 * v.P_LoopMain[playerID], v.P_Distance[playerID])
                # (Line 55) trg.Table_Sin(playerID, 45 + 90 * v.P_LoopMain[playerID], v.P_Distance[playerID]);
                trg.Table_Sin(playerID, 45 + 90 * v.P_LoopMain[playerID], v.P_Distance[playerID])
                # (Line 57) trg.MoveLoc(v.P_UnitID[playerID], playerID, v.P_AngleCos[playerID], v.P_AngleSin[playerID]);
                trg.MoveLoc(v.P_UnitID[playerID], playerID, v.P_AngleCos[playerID], v.P_AngleSin[playerID])
                # (Line 58) trg.SkillUnit(playerID, 1, "40 + 1n Wraith");
                trg.SkillUnit(playerID, 1, "40 + 1n Wraith")
                # (Line 59) trg.SkillUnit(playerID, 1, "40 + 1n Goliath");
                trg.SkillUnit(playerID, 1, "40 + 1n Goliath")
                # (Line 61) KillUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);
                # (Line 63) trg.Main_Wait(50);
                DoActions(KillUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID))
                trg.Main_Wait(50)
                # (Line 64) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 65) }
                # (Line 66) else if (v.P_LoopMain[playerID] == 4)
            if EUDElseIf()(v.P_LoopMain[playerID] == 4):
                # (Line 67) {
                # (Line 68) MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
                # (Line 69) KillUnitAt(All, "40 + 1n Goliath", "Anywhere", playerID);
                DoActions(MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere"))
                # (Line 71) trg.Main_Wait(0);
                DoActions(KillUnitAt(All, "40 + 1n Goliath", "Anywhere", playerID))
                trg.Main_Wait(0)
                # (Line 73) v.P_CountMain[playerID] += 1;
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 74) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 75) }
                # (Line 76) }
            EUDEndIf()
            # (Line 77) else if (v.P_CountMain[playerID] == 2)
        if EUDElseIf()(v.P_CountMain[playerID] == 2):
            # (Line 78) {
            # (Line 79) if (v.P_LoopMain[playerID] < 4)
            if EUDIf()(v.P_LoopMain[playerID] >= 4, neg=True):
                # (Line 80) {
                # (Line 81) v.P_Distance[playerID] = 100;
                _ARRW(v.P_Distance, playerID) << (100)
                # (Line 83) trg.Table_Cos(playerID, 0 + 90 * v.P_LoopMain[playerID], v.P_Distance[playerID]);
                trg.Table_Cos(playerID, 0 + 90 * v.P_LoopMain[playerID], v.P_Distance[playerID])
                # (Line 84) trg.Table_Sin(playerID, 0 + 90 * v.P_LoopMain[playerID], v.P_Distance[playerID]);
                trg.Table_Sin(playerID, 0 + 90 * v.P_LoopMain[playerID], v.P_Distance[playerID])
                # (Line 86) trg.MoveLoc(v.P_UnitID[playerID], playerID, v.P_AngleCos[playerID], v.P_AngleSin[playerID]);
                trg.MoveLoc(v.P_UnitID[playerID], playerID, v.P_AngleCos[playerID], v.P_AngleSin[playerID])
                # (Line 87) trg.SkillUnit(playerID, 1, "40 + 1n Wraith");
                trg.SkillUnit(playerID, 1, "40 + 1n Wraith")
                # (Line 88) trg.SkillUnit(playerID, 1, "40 + 1n Goliath");
                trg.SkillUnit(playerID, 1, "40 + 1n Goliath")
                # (Line 90) v.P_Distance[playerID] = 150;
                _ARRW(v.P_Distance, playerID) << (150)
                # (Line 92) trg.Table_Cos(playerID, 0 + 90 * v.P_LoopMain[playerID], v.P_Distance[playerID]);
                trg.Table_Cos(playerID, 0 + 90 * v.P_LoopMain[playerID], v.P_Distance[playerID])
                # (Line 93) trg.Table_Sin(playerID, 0 + 90 * v.P_LoopMain[playerID], v.P_Distance[playerID]);
                trg.Table_Sin(playerID, 0 + 90 * v.P_LoopMain[playerID], v.P_Distance[playerID])
                # (Line 95) trg.MoveLoc(v.P_UnitID[playerID], playerID, v.P_AngleCos[playerID], v.P_AngleSin[playerID]);
                trg.MoveLoc(v.P_UnitID[playerID], playerID, v.P_AngleCos[playerID], v.P_AngleSin[playerID])
                # (Line 96) trg.SkillUnit(playerID, 1, "40 + 1n Wraith");
                trg.SkillUnit(playerID, 1, "40 + 1n Wraith")
                # (Line 97) trg.SkillUnit(playerID, 1, "40 + 1n Goliath");
                trg.SkillUnit(playerID, 1, "40 + 1n Goliath")
                # (Line 99) KillUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);
                # (Line 101) trg.Main_Wait(50);
                DoActions(KillUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID))
                trg.Main_Wait(50)
                # (Line 102) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 103) }
                # (Line 104) else if (v.P_LoopMain[playerID] == 4)
            if EUDElseIf()(v.P_LoopMain[playerID] == 4):
                # (Line 105) {
                # (Line 106) MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
                # (Line 107) MoveUnit(All, "40 + 1n Goliath", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
                DoActions(MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere"))
                # (Line 108) Order("40 + 1n Goliath", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                DoActions(MoveUnit(All, "40 + 1n Goliath", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]))
                # (Line 110) trg.Main_Wait(50);
                DoActions(Order("40 + 1n Goliath", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                trg.Main_Wait(50)
                # (Line 112) v.P_CountMain[playerID] += 1;
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 113) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 114) }
                # (Line 115) }
            EUDEndIf()
            # (Line 116) else if (v.P_CountMain[playerID] == 3)
        if EUDElseIf()(v.P_CountMain[playerID] == 3):
            # (Line 117) {
            # (Line 118) KillUnitAt(All, "40 + 1n Goliath", "Anywhere", playerID);
            # (Line 119) KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID);
            DoActions(KillUnitAt(All, "40 + 1n Goliath", "Anywhere", playerID))
            # (Line 120) trg.SkillEnd();
            DoActions(KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID))
            trg.SkillEnd()
            # (Line 121) }
            # (Line 122) }
        EUDEndIf()
        # (Line 123) }
    EUDEndIf()
