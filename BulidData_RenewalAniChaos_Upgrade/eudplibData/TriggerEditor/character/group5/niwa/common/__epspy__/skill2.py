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
                # (Line 13) trg.Shape_Square(playerID, 1, "Bengalaas (Jungle)", 50, 0);
                trg.Shape_Square(playerID, 1, "Bengalaas (Jungle)", 50, 0)
                # (Line 14) KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", playerID);
                # (Line 16) trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 50, 50);
                DoActions(KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", playerID))
                trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 50, 50)
                # (Line 17) KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID);
                # (Line 19) trg.Shape_Square(playerID, 1, "40 + 1n Mojo", 50, 0);
                DoActions(KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID))
                trg.Shape_Square(playerID, 1, "40 + 1n Mojo", 50, 0)
                # (Line 21) MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
                # (Line 22) Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                DoActions(MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere"))
                # (Line 23) }
                DoActions(Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                # (Line 24) else if (v.P_LoopMain[playerID] == 2)
            if EUDElseIf()(v.P_LoopMain[playerID] == 2):
                # (Line 25) {
                # (Line 26) KillUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID);
                # (Line 28) trg.Shape_Square(playerID, 1, "Bengalaas (Jungle)", 50, 50);
                DoActions(KillUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID))
                trg.Shape_Square(playerID, 1, "Bengalaas (Jungle)", 50, 50)
                # (Line 29) KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", playerID);
                # (Line 31) trg.Shape_Square(playerID, 1, "Kakaru (Twilight)", 100, 100);
                DoActions(KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", playerID))
                trg.Shape_Square(playerID, 1, "Kakaru (Twilight)", 100, 100)
                # (Line 32) KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", playerID);
                # (Line 34) trg.Shape_Square(playerID, 1, "40 + 1n Mojo", 50, 50);
                DoActions(KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", playerID))
                trg.Shape_Square(playerID, 1, "40 + 1n Mojo", 50, 50)
                # (Line 36) MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
                # (Line 37) Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                DoActions(MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere"))
                # (Line 38) }
                DoActions(Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                # (Line 39) else if (v.P_LoopMain[playerID] == 4)
            if EUDElseIf()(v.P_LoopMain[playerID] == 4):
                # (Line 40) {
                # (Line 41) KillUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID);
                # (Line 43) trg.Shape_Dot(playerID, 1, "Target", 0, 0);
                DoActions(KillUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID))
                trg.Shape_Dot(playerID, 1, "Target", 0, 0)
                # (Line 44) KillUnitAt(All, "Target", "Anywhere", playerID);
                # (Line 47) trg.Shape_Square(playerID, 1, "40 + 1n Mutalisk", 50, 50);
                DoActions(KillUnitAt(All, "Target", "Anywhere", playerID))
                trg.Shape_Square(playerID, 1, "40 + 1n Mutalisk", 50, 50)
                # (Line 48) KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", playerID);
                # (Line 50) trg.Shape_Square(playerID, 1, "50 + 1n Battlecruiser", 100, 100);
                DoActions(KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", playerID))
                trg.Shape_Square(playerID, 1, "50 + 1n Battlecruiser", 100, 100)
                # (Line 51) KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID);
                # (Line 53) trg.Shape_Square(playerID, 1, "40 + 1n Mojo", 100, 0);
                DoActions(KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID))
                trg.Shape_Square(playerID, 1, "40 + 1n Mojo", 100, 0)
                # (Line 55) MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
                # (Line 56) Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                DoActions(MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere"))
                # (Line 57) }
                DoActions(Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                # (Line 58) else if (v.P_LoopMain[playerID] == 6)
            if EUDElseIf()(v.P_LoopMain[playerID] == 6):
                # (Line 59) {
                # (Line 60) KillUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID);
                # (Line 62) trg.Shape_Dot(playerID, 1, "Target", 0, 0);
                DoActions(KillUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID))
                trg.Shape_Dot(playerID, 1, "Target", 0, 0)
                # (Line 63) KillUnitAt(All, "Target", "Anywhere", playerID);
                # (Line 65) trg.Shape_Square(playerID, 1, "40 + 1n Mutalisk", 50, 50);
                DoActions(KillUnitAt(All, "Target", "Anywhere", playerID))
                trg.Shape_Square(playerID, 1, "40 + 1n Mutalisk", 50, 50)
                # (Line 66) KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", playerID);
                # (Line 68) trg.Shape_Square(playerID, 1, "50 + 1n Battlecruiser", 100, 0);
                DoActions(KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", playerID))
                trg.Shape_Square(playerID, 1, "50 + 1n Battlecruiser", 100, 0)
                # (Line 69) KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID);
                # (Line 71) trg.Shape_Square(playerID, 1, "40 + 1n Mojo", 50, 0);
                DoActions(KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID))
                trg.Shape_Square(playerID, 1, "40 + 1n Mojo", 50, 0)
                # (Line 73) MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
                # (Line 74) Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                DoActions(MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere"))
                # (Line 75) }
                DoActions(Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                # (Line 77) trg.Main_Wait(80);
            EUDEndIf()
            trg.Main_Wait(80)
            # (Line 79) v.P_LoopMain[playerID] += 1;
            _ARRW(v.P_LoopMain, playerID).__iadd__(1)
            # (Line 81) if (v.P_LoopMain[playerID] == 8)
            if EUDIf()(v.P_LoopMain[playerID] == 8):
                # (Line 82) {
                # (Line 83) v.P_CountMain[playerID] += 1;
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 84) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 85) }
                # (Line 86) }
            EUDEndIf()
            # (Line 87) else if (v.P_CountMain[playerID] == 1)
        if EUDElseIf()(v.P_CountMain[playerID] == 1):
            # (Line 88) {
            # (Line 89) KillUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID);
            # (Line 91) trg.SkillEnd();
            DoActions(KillUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID))
            trg.SkillEnd()
            # (Line 92) }
            # (Line 93) }
        EUDEndIf()
        # (Line 94) }
    EUDEndIf()