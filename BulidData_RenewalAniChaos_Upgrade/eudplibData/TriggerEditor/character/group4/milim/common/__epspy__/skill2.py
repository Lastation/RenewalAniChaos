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
# (Line 5) import func.sound as s;
from func import sound as s
# (Line 7) function main(playerID)
# (Line 8) {
@EUDFunc
def f_main(playerID):
    # (Line 9) if (v.P_WaitMain[playerID] == 0)
    if EUDIf()(v.P_WaitMain[playerID] == 0):
        # (Line 10) {
        # (Line 11) if (v.P_CountMain[playerID] == 0)
        if EUDIf()(v.P_CountMain[playerID] == 0):
            # (Line 12) {
            # (Line 13) if (v.P_LoopMain[playerID] == 0)
            if EUDIf()(v.P_LoopMain[playerID] == 0):
                # (Line 14) {
                # (Line 15) trg.Shape_Square(playerID, 1, "Target", 50, 0);
                trg.Shape_Square(playerID, 1, "Target", 50, 0)
                # (Line 16) trg.Shape_Square(playerID, 1, "Target", 100, 0);
                trg.Shape_Square(playerID, 1, "Target", 100, 0)
                # (Line 17) KillUnitAt(All, "Target", "Anywhere", playerID);
                # (Line 19) trg.Main_Wait(80);
                DoActions(KillUnitAt(All, "Target", "Anywhere", playerID))
                trg.Main_Wait(80)
                # (Line 20) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 21) }
                # (Line 22) else if (v.P_LoopMain[playerID] == 1)
            if EUDElseIf()(v.P_LoopMain[playerID] == 1):
                # (Line 23) {
                # (Line 24) trg.Shape_Square(playerID, 1, "Target", 50, 100);
                trg.Shape_Square(playerID, 1, "Target", 50, 100)
                # (Line 25) trg.Shape_Square(playerID, 1, "Target", 100, 50);
                trg.Shape_Square(playerID, 1, "Target", 100, 50)
                # (Line 26) KillUnitAt(All, "Target", "Anywhere", playerID);
                # (Line 28) trg.Main_Wait(80);
                DoActions(KillUnitAt(All, "Target", "Anywhere", playerID))
                trg.Main_Wait(80)
                # (Line 29) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 30) }
                # (Line 31) else if (v.P_LoopMain[playerID] == 2)
            if EUDElseIf()(v.P_LoopMain[playerID] == 2):
                # (Line 32) {
                # (Line 33) trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 50, 100);
                trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 50, 100)
                # (Line 34) trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 100, 50);
                trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 100, 50)
                # (Line 35) KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID);
                # (Line 37) trg.Shape_Square(playerID, 1, "40 + 1n Goliath", 50, 100);
                DoActions(KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID))
                trg.Shape_Square(playerID, 1, "40 + 1n Goliath", 50, 100)
                # (Line 38) trg.Shape_Square(playerID, 1, "40 + 1n Goliath", 100, 50);
                trg.Shape_Square(playerID, 1, "40 + 1n Goliath", 100, 50)
                # (Line 40) MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
                # (Line 41) MoveUnit(All, "40 + 1n Goliath", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
                DoActions(MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere"))
                # (Line 42) Order("40 + 1n Goliath", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                DoActions(MoveUnit(All, "40 + 1n Goliath", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]))
                # (Line 44) trg.Main_Wait(80);
                DoActions(Order("40 + 1n Goliath", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                trg.Main_Wait(80)
                # (Line 45) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 46) }
                # (Line 47) else if (v.P_LoopMain[playerID] == 3)
            if EUDElseIf()(v.P_LoopMain[playerID] == 3):
                # (Line 48) {
                # (Line 49) KillUnitAt(All, "40 + 1n Goliath", "Anywhere", playerID);
                # (Line 50) trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 100, 150);
                DoActions(KillUnitAt(All, "40 + 1n Goliath", "Anywhere", playerID))
                trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 100, 150)
                # (Line 51) trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 150, 100);
                trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 150, 100)
                # (Line 52) KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID);
                # (Line 54) trg.Main_Wait(80);
                DoActions(KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID))
                trg.Main_Wait(80)
                # (Line 55) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 56) }
                # (Line 57) else if (v.P_LoopMain[playerID] == 4)
            if EUDElseIf()(v.P_LoopMain[playerID] == 4):
                # (Line 58) {
                # (Line 59) trg.Shape_Square(playerID, 1, "Kakaru (Twilight)", 100, 150);
                trg.Shape_Square(playerID, 1, "Kakaru (Twilight)", 100, 150)
                # (Line 60) trg.Shape_Square(playerID, 1, "Kakaru (Twilight)", 150, 100);
                trg.Shape_Square(playerID, 1, "Kakaru (Twilight)", 150, 100)
                # (Line 61) trg.Shape_Square(playerID, 1, "Kakaru (Twilight)", 50, 100);
                trg.Shape_Square(playerID, 1, "Kakaru (Twilight)", 50, 100)
                # (Line 62) trg.Shape_Square(playerID, 1, "Kakaru (Twilight)", 100, 50);
                trg.Shape_Square(playerID, 1, "Kakaru (Twilight)", 100, 50)
                # (Line 63) KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", playerID);
                # (Line 65) trg.Main_Wait(320);
                DoActions(KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", playerID))
                trg.Main_Wait(320)
                # (Line 66) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 67) }
                # (Line 68) else if (v.P_LoopMain[playerID] == 5)
            if EUDElseIf()(v.P_LoopMain[playerID] == 5):
                # (Line 69) {
                # (Line 70) trg.Shape_Dot(playerID, 1, "40 + 1n Zealot", 50, 0);
                trg.Shape_Dot(playerID, 1, "40 + 1n Zealot", 50, 0)
                # (Line 71) trg.Shape_Dot(playerID, 1, "40 + 1n Zealot", -50, 0);
                trg.Shape_Dot(playerID, 1, "40 + 1n Zealot", -50, 0)
                # (Line 72) KillUnitAt(All, "40 + 1n Zealot", "Anywhere", playerID);
                # (Line 74) trg.Shape_Dot(playerID, 1, "40 + 1n Wraith", 50, 0);
                DoActions(KillUnitAt(All, "40 + 1n Zealot", "Anywhere", playerID))
                trg.Shape_Dot(playerID, 1, "40 + 1n Wraith", 50, 0)
                # (Line 75) trg.Shape_Dot(playerID, 1, "40 + 1n Wraith", -50, 0);
                trg.Shape_Dot(playerID, 1, "40 + 1n Wraith", -50, 0)
                # (Line 77) MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
                # (Line 78) Order("40 + 1n Wraith", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                DoActions(MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere"))
                # (Line 80) trg.Main_Wait(240);
                DoActions(Order("40 + 1n Wraith", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                trg.Main_Wait(240)
                # (Line 81) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 82) }
                # (Line 83) else if (v.P_LoopMain[playerID] == 6)
            if EUDElseIf()(v.P_LoopMain[playerID] == 6):
                # (Line 84) {
                # (Line 85) RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);
                # (Line 87) trg.Shape_Dot(playerID, 1, "40 + 1n Zealot", 0, 50);
                DoActions(RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID))
                trg.Shape_Dot(playerID, 1, "40 + 1n Zealot", 0, 50)
                # (Line 88) trg.Shape_Dot(playerID, 1, "40 + 1n Zealot", 0, -50);
                trg.Shape_Dot(playerID, 1, "40 + 1n Zealot", 0, -50)
                # (Line 89) KillUnitAt(All, "40 + 1n Zealot", "Anywhere", playerID);
                # (Line 91) trg.Shape_Dot(playerID, 1, "40 + 1n Wraith", 0, 50);
                DoActions(KillUnitAt(All, "40 + 1n Zealot", "Anywhere", playerID))
                trg.Shape_Dot(playerID, 1, "40 + 1n Wraith", 0, 50)
                # (Line 92) trg.Shape_Dot(playerID, 1, "40 + 1n Wraith", 0, -50);
                trg.Shape_Dot(playerID, 1, "40 + 1n Wraith", 0, -50)
                # (Line 94) MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
                # (Line 95) Order("40 + 1n Wraith", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                DoActions(MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere"))
                # (Line 97) trg.Main_Wait(240);
                DoActions(Order("40 + 1n Wraith", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                trg.Main_Wait(240)
                # (Line 98) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 99) }
                # (Line 100) else if (v.P_LoopMain[playerID] == 7)
            if EUDElseIf()(v.P_LoopMain[playerID] == 7):
                # (Line 101) {
                # (Line 102) RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);
                # (Line 104) trg.Shape_Dot(playerID, 1, "40 + 1n Zealot", 50, 50);
                DoActions(RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID))
                trg.Shape_Dot(playerID, 1, "40 + 1n Zealot", 50, 50)
                # (Line 105) trg.Shape_Dot(playerID, 1, "40 + 1n Zealot", -50, -50);
                trg.Shape_Dot(playerID, 1, "40 + 1n Zealot", -50, -50)
                # (Line 106) KillUnitAt(All, "40 + 1n Zealot", "Anywhere", playerID);
                # (Line 108) trg.Shape_Dot(playerID, 1, "40 + 1n Wraith", 50, 50);
                DoActions(KillUnitAt(All, "40 + 1n Zealot", "Anywhere", playerID))
                trg.Shape_Dot(playerID, 1, "40 + 1n Wraith", 50, 50)
                # (Line 109) trg.Shape_Dot(playerID, 1, "40 + 1n Wraith", -50, -50);
                trg.Shape_Dot(playerID, 1, "40 + 1n Wraith", -50, -50)
                # (Line 111) MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
                # (Line 112) Order("40 + 1n Wraith", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                DoActions(MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere"))
                # (Line 114) trg.Main_Wait(240);
                DoActions(Order("40 + 1n Wraith", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                trg.Main_Wait(240)
                # (Line 115) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 116) }
                # (Line 117) else if (v.P_LoopMain[playerID] == 8)
            if EUDElseIf()(v.P_LoopMain[playerID] == 8):
                # (Line 118) {
                # (Line 119) RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);
                # (Line 121) trg.Shape_Dot(playerID, 1, "40 + 1n Zealot", -50, 50);
                DoActions(RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID))
                trg.Shape_Dot(playerID, 1, "40 + 1n Zealot", -50, 50)
                # (Line 122) trg.Shape_Dot(playerID, 1, "40 + 1n Zealot", 50, -50);
                trg.Shape_Dot(playerID, 1, "40 + 1n Zealot", 50, -50)
                # (Line 123) KillUnitAt(All, "40 + 1n Zealot", "Anywhere", playerID);
                # (Line 125) trg.Shape_Dot(playerID, 1, "40 + 1n Wraith", -50, 50);
                DoActions(KillUnitAt(All, "40 + 1n Zealot", "Anywhere", playerID))
                trg.Shape_Dot(playerID, 1, "40 + 1n Wraith", -50, 50)
                # (Line 126) trg.Shape_Dot(playerID, 1, "40 + 1n Wraith", 50, -50);
                trg.Shape_Dot(playerID, 1, "40 + 1n Wraith", 50, -50)
                # (Line 128) MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
                # (Line 129) Order("40 + 1n Wraith", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                DoActions(MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere"))
                # (Line 131) trg.Main_Wait(240);
                DoActions(Order("40 + 1n Wraith", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                trg.Main_Wait(240)
                # (Line 132) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 133) }
                # (Line 134) else if (v.P_LoopMain[playerID] == 9)
            if EUDElseIf()(v.P_LoopMain[playerID] == 9):
                # (Line 135) {
                # (Line 136) RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);
                # (Line 137) trg.Main_Wait(80);
                DoActions(RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID))
                trg.Main_Wait(80)
                # (Line 139) v.P_CountMain[playerID] += 1;
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 140) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 141) }
                # (Line 142) }
            EUDEndIf()
            # (Line 143) else if (v.P_CountMain[playerID] == 1)
        if EUDElseIf()(v.P_CountMain[playerID] == 1):
            # (Line 144) {
            # (Line 145) trg.SkillEnd();
            trg.SkillEnd()
            # (Line 146) }
            # (Line 147) }
        EUDEndIf()
        # (Line 148) }
    EUDEndIf()