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
# (Line 4) import func.trigadv as adv;
from func import trigadv as adv
# (Line 6) function main(playerID)
# (Line 7) {
@EUDFunc
def f_main(playerID):
    # (Line 8) var x;
    x = EUDVariable()
    # (Line 9) var y;
    y = EUDVariable()
    # (Line 11) if (v.P_WaitMain[playerID] == 0)
    if EUDIf()(v.P_WaitMain[playerID] == 0):
        # (Line 12) {
        # (Line 13) if (v.P_CountMain[playerID] == 0)
        if EUDIf()(v.P_CountMain[playerID] == 0):
            # (Line 14) {
            # (Line 15) if (v.P_LoopMain[playerID] == 0)
            if EUDIf()(v.P_LoopMain[playerID] == 0):
                # (Line 16) {
                # (Line 17) adv.Shape_QuadNxNSquareAt(playerID, 1, "40 + 1n Mojo", 2, 50, 75, 75);
                adv.Shape_QuadNxNSquareAt(playerID, 1, "40 + 1n Mojo", 2, 50, 75, 75)
                # (Line 18) adv.Shape_QuadNxNSquareAt(playerID, 1, "60 + 1n Archon", 2, 50, 75, 75);
                adv.Shape_QuadNxNSquareAt(playerID, 1, "60 + 1n Archon", 2, 50, 75, 75)
                # (Line 20) MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
                # (Line 21) Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                DoActions(MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere"))
                # (Line 23) KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
                DoActions(Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                # (Line 24) }
                DoActions(KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID))
                # (Line 25) else if (v.P_LoopMain[playerID] == 5)
            if EUDElseIf()(v.P_LoopMain[playerID] == 5):
                # (Line 26) {
                # (Line 27) KillUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID);
                # (Line 28) }
                DoActions(KillUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID))
                # (Line 29) else if (v.P_LoopMain[playerID] == 6)
            if EUDElseIf()(v.P_LoopMain[playerID] == 6):
                # (Line 30) {
                # (Line 31) adv.Shape_QuadNxNSquareAt(playerID, 1, "40 + 1n Wraith", 2, 50, 75, 75);
                adv.Shape_QuadNxNSquareAt(playerID, 1, "40 + 1n Wraith", 2, 50, 75, 75)
                # (Line 32) adv.Shape_QuadNxNSquareAt(playerID, 1, "Scantid (Desert)", 2, 50, 75, 75);
                adv.Shape_QuadNxNSquareAt(playerID, 1, "Scantid (Desert)", 2, 50, 75, 75)
                # (Line 34) MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
                # (Line 35) Order("40 + 1n Wraith", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                DoActions(MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere"))
                # (Line 37) KillUnitAt(All, "Scantid (Desert)", "Anywhere", playerID);
                DoActions(Order("40 + 1n Wraith", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                # (Line 38) }
                DoActions(KillUnitAt(All, "Scantid (Desert)", "Anywhere", playerID))
                # (Line 40) trg.Main_Wait(80);
            EUDEndIf()
            trg.Main_Wait(80)
            # (Line 42) v.P_LoopMain[playerID] += 1;
            _ARRW(v.P_LoopMain, playerID).__iadd__(1)
            # (Line 44) if (v.P_LoopMain[playerID] == 9)
            if EUDIf()(v.P_LoopMain[playerID] == 9):
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
            # (Line 52) RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);
            # (Line 54) adv.Shape_QuadNxNSquareAt(playerID, 1, "Kakaru (Twilight)", 2, 50, 75, 75);
            DoActions(RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID))
            adv.Shape_QuadNxNSquareAt(playerID, 1, "Kakaru (Twilight)", 2, 50, 75, 75)
            # (Line 55) KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", playerID);
            # (Line 57) trg.SkillEnd();
            DoActions(KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", playerID))
            trg.SkillEnd()
            # (Line 58) }
            # (Line 59) }
        EUDEndIf()
        # (Line 60) }
    EUDEndIf()