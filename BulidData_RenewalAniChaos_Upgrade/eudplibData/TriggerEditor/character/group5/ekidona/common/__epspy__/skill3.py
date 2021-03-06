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
            # (Line 11) if (v.P_LoopMain[playerID] < 16)
            if EUDIf()(v.P_LoopMain[playerID] >= 16, neg=True):
                # (Line 12) {
                # (Line 13) RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID);
                # (Line 15) trg.Shape_Dot(playerID, 1, "40 + 1n Mojo", 0, 0);
                DoActions(RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID))
                trg.Shape_Dot(playerID, 1, "40 + 1n Mojo", 0, 0)
                # (Line 16) trg.Shape_Dot(playerID, 1, "60 + 1n Archon", 0, 0);
                trg.Shape_Dot(playerID, 1, "60 + 1n Archon", 0, 0)
                # (Line 17) KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
                # (Line 19) Order("40 + 1n Mojo", playerID, "Anywhere", Attack, "Anywhere");
                DoActions(KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID))
                # (Line 20) }
                DoActions(Order("40 + 1n Mojo", playerID, "Anywhere", Attack, "Anywhere"))
                # (Line 22) var x = 0;
            EUDEndIf()
            x = EUDVariable()
            x << (0)
            # (Line 23) var y = 0;
            y = EUDVariable()
            y << (0)
            # (Line 25) if (v.P_LoopMain[playerID] == 8) { x = 0; y = -50; }
            if EUDIf()(v.P_LoopMain[playerID] == 8):
                x << (0)
                y << (-50)
                # (Line 26) if (v.P_LoopMain[playerID] == 9) { x = -100; y = 100; }
            EUDEndIf()
            if EUDIf()(v.P_LoopMain[playerID] == 9):
                x << (-100)
                y << (100)
                # (Line 27) if (v.P_LoopMain[playerID] == 10) { x = 0; y = 50; }
            EUDEndIf()
            if EUDIf()(v.P_LoopMain[playerID] == 10):
                x << (0)
                y << (50)
                # (Line 28) if (v.P_LoopMain[playerID] == 11) { x = 100; y = -100; }
            EUDEndIf()
            if EUDIf()(v.P_LoopMain[playerID] == 11):
                x << (100)
                y << (-100)
                # (Line 29) if (v.P_LoopMain[playerID] == 12) { x = -50; y = 0; }
            EUDEndIf()
            if EUDIf()(v.P_LoopMain[playerID] == 12):
                x << (-50)
                y << (0)
                # (Line 30) if (v.P_LoopMain[playerID] == 13) { x = 100; y = 100; }
            EUDEndIf()
            if EUDIf()(v.P_LoopMain[playerID] == 13):
                x << (100)
                y << (100)
                # (Line 31) if (v.P_LoopMain[playerID] == 14) { x = 50; y = 0; }
            EUDEndIf()
            if EUDIf()(v.P_LoopMain[playerID] == 14):
                x << (50)
                y << (0)
                # (Line 32) if (v.P_LoopMain[playerID] == 15) { x = -100; y = -100; }
            EUDEndIf()
            if EUDIf()(v.P_LoopMain[playerID] == 15):
                x << (-100)
                y << (-100)
                # (Line 34) if (v.P_LoopMain[playerID] >= 8)
            EUDEndIf()
            if EUDIf()(v.P_LoopMain[playerID] >= 8):
                # (Line 35) {
                # (Line 36) trg.Shape_Dot(playerID, 9, "60 + 1n High Templar", x, y);
                trg.Shape_Dot(playerID, 9, "60 + 1n High Templar", x, y)
                # (Line 37) KillUnitAt(All, "60 + 1n High Templar", "Anywhere", playerID);
                # (Line 38) }
                DoActions(KillUnitAt(All, "60 + 1n High Templar", "Anywhere", playerID))
                # (Line 40) trg.Main_Wait(80);
            EUDEndIf()
            trg.Main_Wait(80)
            # (Line 42) v.P_LoopMain[playerID] += 1;
            _ARRW(v.P_LoopMain, playerID).__iadd__(1)
            # (Line 44) if (v.P_LoopMain[playerID] == 16)
            if EUDIf()(v.P_LoopMain[playerID] == 16):
                # (Line 45) {
                # (Line 46) v.P_CountMain[playerID] += 1;
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 47) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 48) }
                # (Line 49) }
            EUDEndIf()
            # (Line 50) else if (v.P_CountMain[playerID] == 1)
        if EUDElseIf()(v.P_CountMain[playerID] == 1):
            # (Line 51) {
            # (Line 52) if (v.P_LoopMain[playerID] == 0)
            if EUDIf()(v.P_LoopMain[playerID] == 0):
                # (Line 53) {
                # (Line 54) RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID);
                # (Line 55) trg.Shape_Square(playerID, 1, "60 + 1n High Templar", 50, 0);
                DoActions(RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID))
                trg.Shape_Square(playerID, 1, "60 + 1n High Templar", 50, 0)
                # (Line 56) trg.Shape_Square(playerID, 1, "60 + 1n High Templar", 100, 100);
                trg.Shape_Square(playerID, 1, "60 + 1n High Templar", 100, 100)
                # (Line 57) trg.Shape_Square(playerID, 8, " Unit. Schnee", 50, 0);
                trg.Shape_Square(playerID, 8, " Unit. Schnee", 50, 0)
                # (Line 58) trg.Shape_Square(playerID, 8, " Unit. Schnee", 100, 100);
                trg.Shape_Square(playerID, 8, " Unit. Schnee", 100, 100)
                # (Line 59) KillUnitAt(All, " Unit. Schnee", "Anywhere", playerID);
                # (Line 61) MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
                DoActions(KillUnitAt(All, " Unit. Schnee", "Anywhere", playerID))
                # (Line 62) MoveUnit(All, "60 + 1n High Templar", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
                DoActions(MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere"))
                # (Line 63) Order("60 + 1n High Templar", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                DoActions(MoveUnit(All, "60 + 1n High Templar", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]))
                # (Line 64) }
                DoActions(Order("60 + 1n High Templar", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                # (Line 66) trg.Main_Wait(80);
            EUDEndIf()
            trg.Main_Wait(80)
            # (Line 68) v.P_LoopMain[playerID] += 1;
            _ARRW(v.P_LoopMain, playerID).__iadd__(1)
            # (Line 70) if (v.P_LoopMain[playerID] == 4)
            if EUDIf()(v.P_LoopMain[playerID] == 4):
                # (Line 71) {
                # (Line 72) v.P_CountMain[playerID] += 1;
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 73) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 74) }
                # (Line 75) }
            EUDEndIf()
            # (Line 76) else if (v.P_CountMain[playerID] == 2)
        if EUDElseIf()(v.P_CountMain[playerID] == 2):
            # (Line 77) {
            # (Line 78) KillUnitAt(All, "60 + 1n High Templar", "Anywhere", playerID);
            # (Line 80) trg.SkillEnd();
            DoActions(KillUnitAt(All, "60 + 1n High Templar", "Anywhere", playerID))
            trg.SkillEnd()
            # (Line 81) }
            # (Line 82) }
        EUDEndIf()
        # (Line 83) }
    EUDEndIf()
