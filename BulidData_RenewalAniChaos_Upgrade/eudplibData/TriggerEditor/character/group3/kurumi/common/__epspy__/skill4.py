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
            # (Line 11) KillUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID);
            # (Line 12) KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", playerID);
            DoActions(KillUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID))
            # (Line 14) if(v.P_LoopMain[playerID] == 0)
            DoActions(KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", playerID))
            if EUDIf()(v.P_LoopMain[playerID] == 0):
                # (Line 15) {
                # (Line 16) trg.Shape_Line(playerID,1,"40 + 1n Mojo",60,2,96,0);
                trg.Shape_Line(playerID, 1, "40 + 1n Mojo", 60, 2, 96, 0)
                # (Line 17) trg.MoveLoc(v.P_UnitID[playerID], playerID,0,0);
                trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0)
                # (Line 18) Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                # (Line 19) trg.Main_Wait(50);
                DoActions(Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                trg.Main_Wait(50)
                # (Line 20) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 21) }
                # (Line 22) else if(v.P_LoopMain[playerID] == 1)
            if EUDElseIf()(v.P_LoopMain[playerID] == 1):
                # (Line 23) {
                # (Line 24) trg.Shape_Line(playerID,1,"40 + 1n Mojo",120,2,96,0);
                trg.Shape_Line(playerID, 1, "40 + 1n Mojo", 120, 2, 96, 0)
                # (Line 25) trg.MoveLoc(v.P_UnitID[playerID], playerID,0,0);
                trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0)
                # (Line 26) Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                # (Line 27) trg.Main_Wait(50);
                DoActions(Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                trg.Main_Wait(50)
                # (Line 28) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 29) }
                # (Line 30) else if(v.P_LoopMain[playerID] == 2)
            if EUDElseIf()(v.P_LoopMain[playerID] == 2):
                # (Line 31) {
                # (Line 32) trg.Shape_Line(playerID,1,"40 + 1n Mojo",180,2,96,0);
                trg.Shape_Line(playerID, 1, "40 + 1n Mojo", 180, 2, 96, 0)
                # (Line 33) trg.MoveLoc(v.P_UnitID[playerID], playerID,0,0);
                trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0)
                # (Line 34) Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                # (Line 35) trg.Main_Wait(50);
                DoActions(Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                trg.Main_Wait(50)
                # (Line 36) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 37) }
                # (Line 38) else if(v.P_LoopMain[playerID] == 3)
            if EUDElseIf()(v.P_LoopMain[playerID] == 3):
                # (Line 39) {
                # (Line 40) trg.Shape_Line(playerID,1,"40 + 1n Mojo",240,2,96,0);
                trg.Shape_Line(playerID, 1, "40 + 1n Mojo", 240, 2, 96, 0)
                # (Line 41) trg.MoveLoc(v.P_UnitID[playerID], playerID,0,0);
                trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0)
                # (Line 42) Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                # (Line 43) trg.Main_Wait(50);
                DoActions(Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                trg.Main_Wait(50)
                # (Line 44) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 45) }
                # (Line 46) else if(v.P_LoopMain[playerID] == 4)
            if EUDElseIf()(v.P_LoopMain[playerID] == 4):
                # (Line 47) {
                # (Line 48) trg.Shape_Line(playerID,1,"40 + 1n Mojo",300,2,96,0);
                trg.Shape_Line(playerID, 1, "40 + 1n Mojo", 300, 2, 96, 0)
                # (Line 49) trg.MoveLoc(v.P_UnitID[playerID], playerID,0,0);
                trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0)
                # (Line 50) Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                # (Line 51) trg.Main_Wait(50);
                DoActions(Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                trg.Main_Wait(50)
                # (Line 52) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 53) }
                # (Line 54) else if(v.P_LoopMain[playerID] == 5)
            if EUDElseIf()(v.P_LoopMain[playerID] == 5):
                # (Line 55) {
                # (Line 56) trg.Shape_Line(playerID,1,"40 + 1n Mojo",360,2,96,0);
                trg.Shape_Line(playerID, 1, "40 + 1n Mojo", 360, 2, 96, 0)
                # (Line 57) trg.MoveLoc(v.P_UnitID[playerID], playerID,0,0);
                trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0)
                # (Line 58) Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                # (Line 59) trg.Main_Wait(50);
                DoActions(Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                trg.Main_Wait(50)
                # (Line 60) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 61) }
                # (Line 62) else if(v.P_LoopMain[playerID] == 6)
            if EUDElseIf()(v.P_LoopMain[playerID] == 6):
                # (Line 63) {
                # (Line 64) trg.Shape_Line(playerID,1,"40 + 1n Mojo",60,2,96,0);
                trg.Shape_Line(playerID, 1, "40 + 1n Mojo", 60, 2, 96, 0)
                # (Line 65) trg.MoveLoc(v.P_UnitID[playerID], playerID,0,0);
                trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0)
                # (Line 66) Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                # (Line 67) trg.Main_Wait(50);
                DoActions(Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                trg.Main_Wait(50)
                # (Line 68) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 69) }
                # (Line 70) else if(v.P_LoopMain[playerID] == 7)
            if EUDElseIf()(v.P_LoopMain[playerID] == 7):
                # (Line 71) {
                # (Line 72) trg.Shape_Line(playerID,1,"40 + 1n Mojo",120,2,96,0);
                trg.Shape_Line(playerID, 1, "40 + 1n Mojo", 120, 2, 96, 0)
                # (Line 73) trg.MoveLoc(v.P_UnitID[playerID], playerID,0,0);
                trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0)
                # (Line 74) Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                # (Line 75) trg.Main_Wait(50);
                DoActions(Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                trg.Main_Wait(50)
                # (Line 76) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 77) }
                # (Line 78) else if(v.P_LoopMain[playerID] == 8)
            if EUDElseIf()(v.P_LoopMain[playerID] == 8):
                # (Line 79) {
                # (Line 80) trg.Shape_Line(playerID,1,"40 + 1n Mojo",180,2,96,0);
                trg.Shape_Line(playerID, 1, "40 + 1n Mojo", 180, 2, 96, 0)
                # (Line 82) trg.MoveLoc(v.P_UnitID[playerID], playerID,0,0);
                trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0)
                # (Line 83) Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                # (Line 84) trg.Main_Wait(50);
                DoActions(Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                trg.Main_Wait(50)
                # (Line 85) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 86) }
                # (Line 87) else if(v.P_LoopMain[playerID] == 9)
            if EUDElseIf()(v.P_LoopMain[playerID] == 9):
                # (Line 88) {
                # (Line 89) trg.Shape_Line(playerID,1,"40 + 1n Mojo",240,2,96,0);
                trg.Shape_Line(playerID, 1, "40 + 1n Mojo", 240, 2, 96, 0)
                # (Line 90) trg.MoveLoc(v.P_UnitID[playerID], playerID,0,0);
                trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0)
                # (Line 91) Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                # (Line 92) trg.Main_Wait(50);
                DoActions(Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                trg.Main_Wait(50)
                # (Line 93) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 94) }
                # (Line 95) else if(v.P_LoopMain[playerID] == 10)
            if EUDElseIf()(v.P_LoopMain[playerID] == 10):
                # (Line 96) {
                # (Line 97) trg.Shape_Line(playerID,1,"40 + 1n Mojo",300,2,96,0);
                trg.Shape_Line(playerID, 1, "40 + 1n Mojo", 300, 2, 96, 0)
                # (Line 98) trg.MoveLoc(v.P_UnitID[playerID], playerID,0,0);
                trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0)
                # (Line 99) Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                # (Line 100) trg.Main_Wait(50);
                DoActions(Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                trg.Main_Wait(50)
                # (Line 101) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 102) }
                # (Line 103) else if(v.P_LoopMain[playerID] == 11)
            if EUDElseIf()(v.P_LoopMain[playerID] == 11):
                # (Line 104) {
                # (Line 105) trg.Shape_Line(playerID,1,"40 + 1n Mojo",360,2,96,0);
                trg.Shape_Line(playerID, 1, "40 + 1n Mojo", 360, 2, 96, 0)
                # (Line 106) trg.MoveLoc(v.P_UnitID[playerID], playerID,0,0);
                trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0)
                # (Line 107) Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                # (Line 108) trg.Main_Wait(50);
                DoActions(Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                trg.Main_Wait(50)
                # (Line 109) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 110) }
                # (Line 111) else if(v.P_LoopMain[playerID] == 12)
            if EUDElseIf()(v.P_LoopMain[playerID] == 12):
                # (Line 112) {
                # (Line 113) trg.Shape_Cross(playerID,1,"60 + 1n Danimoth",45,3,96);
                trg.Shape_Cross(playerID, 1, "60 + 1n Danimoth", 45, 3, 96)
                # (Line 114) trg.MoveLoc(v.P_UnitID[playerID], playerID,0,0);
                trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0)
                # (Line 115) Order("60 + 1n Danimoth", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                # (Line 116) trg.Main_Wait(100);
                DoActions(Order("60 + 1n Danimoth", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                trg.Main_Wait(100)
                # (Line 117) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 118) }
                # (Line 119) else if(v.P_LoopMain[playerID] == 13)
            if EUDElseIf()(v.P_LoopMain[playerID] == 13):
                # (Line 120) {
                # (Line 121) trg.SkillEnd();
                trg.SkillEnd()
                # (Line 122) }
                # (Line 123) }
            EUDEndIf()
            # (Line 124) }
        EUDEndIf()
        # (Line 125) }
    EUDEndIf()