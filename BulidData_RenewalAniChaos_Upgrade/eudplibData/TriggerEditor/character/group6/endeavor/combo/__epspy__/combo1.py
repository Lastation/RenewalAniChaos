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
# (Line 5) var x = 0;
x = EUDCreateVariables(1)
_IGVA([x], lambda: [0])
# (Line 6) function main(playerID)
# (Line 7) {
@EUDFunc
def f_main(playerID):
    # (Line 8) if (v.P_WaitMain[playerID] == 0)
    if EUDIf()(v.P_WaitMain[playerID] == 0):
        # (Line 9) {
        # (Line 10) if (v.P_CountMain[playerID] == 0)
        if EUDIf()(v.P_CountMain[playerID] == 0):
            # (Line 11) {
            # (Line 12) KillUnitAt(All,"40 + 1n Wraith","Anywhere",playerID);
            # (Line 13) KillUnitAt(All,"60 + 1n Danimoth","Anywhere",playerID);
            DoActions(KillUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID))
            # (Line 14) if (v.P_LoopMain[playerID] == 0)
            DoActions(KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", playerID))
            if EUDIf()(v.P_LoopMain[playerID] == 0):
                # (Line 15) {
                # (Line 16) trg.Main_Wait(250);
                trg.Main_Wait(250)
                # (Line 17) }
                # (Line 18) else if (v.P_LoopMain[playerID] <= 3)
            if EUDElseIf()(v.P_LoopMain[playerID] <= 3):
                # (Line 19) {
                # (Line 20) trg.Shape_Square(playerID,1,"40 + 1n Wraith",32 + x *32 ,0);
                trg.Shape_Square(playerID, 1, "40 + 1n Wraith", 32 + x * 32, 0)
                # (Line 21) trg.Shape_Square(playerID,1,"Protoss Dark Templar",32 + x *32 ,0);
                trg.Shape_Square(playerID, 1, "Protoss Dark Templar", 32 + x * 32, 0)
                # (Line 22) KillUnitAt(All,"Protoss Dark Templar","Anywhere",playerID);
                # (Line 23) trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0);
                DoActions(KillUnitAt(All, "Protoss Dark Templar", "Anywhere", playerID))
                trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0)
                # (Line 24) Order("40 + 1n Wraith", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                # (Line 25) x += 1;
                DoActions(Order("40 + 1n Wraith", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                x.__iadd__(1)
                # (Line 26) trg.Main_Wait(125);
                trg.Main_Wait(125)
                # (Line 27) }
                # (Line 28) else if (v.P_LoopMain[playerID] == 4)
            if EUDElseIf()(v.P_LoopMain[playerID] == 4):
                # (Line 29) {
                # (Line 30) trg.Shape_Square(playerID,1,"50 + 1n Tank",160,0);
                trg.Shape_Square(playerID, 1, "50 + 1n Tank", 160, 0)
                # (Line 31) trg.Shape_Square(playerID,1,"Protoss Dark Archon",160,0);
                trg.Shape_Square(playerID, 1, "Protoss Dark Archon", 160, 0)
                # (Line 32) KillUnitAt(All,"Protoss Dark Archon","Anywhere",playerID);
                # (Line 33) trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0);
                DoActions(KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID))
                trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0)
                # (Line 34) Order("50 + 1n Tank", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                # (Line 35) trg.Main_Wait(80);
                DoActions(Order("50 + 1n Tank", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                trg.Main_Wait(80)
                # (Line 36) x = 0;
                x << (0)
                # (Line 37) }
                # (Line 38) else if (v.P_LoopMain[playerID] <= 7)
            if EUDElseIf()(v.P_LoopMain[playerID] <= 7):
                # (Line 39) {
                # (Line 40) trg.Shape_Square(playerID,1,"40 + 1n Wraith",32 + x *32 ,32 + x*32);
                trg.Shape_Square(playerID, 1, "40 + 1n Wraith", 32 + x * 32, 32 + x * 32)
                # (Line 41) trg.Shape_Square(playerID,1,"Protoss Dark Templar",32 + x *32 ,32 + x*32);
                trg.Shape_Square(playerID, 1, "Protoss Dark Templar", 32 + x * 32, 32 + x * 32)
                # (Line 42) KillUnitAt(All,"Protoss Dark Templar","Anywhere",playerID);
                # (Line 43) trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0);
                DoActions(KillUnitAt(All, "Protoss Dark Templar", "Anywhere", playerID))
                trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0)
                # (Line 44) Order("40 + 1n Wraith", playerID, "Anywhere", Move, v.P_LocationID[playerID]);
                # (Line 45) x += 1;
                DoActions(Order("40 + 1n Wraith", playerID, "Anywhere", Move, v.P_LocationID[playerID]))
                x.__iadd__(1)
                # (Line 46) trg.Main_Wait(125);
                trg.Main_Wait(125)
                # (Line 47) }
                # (Line 48) else if (v.P_LoopMain[playerID] == 8)
            if EUDElseIf()(v.P_LoopMain[playerID] == 8):
                # (Line 49) {
                # (Line 50) trg.Shape_Square(playerID,1,"50 + 1n Tank",160,160);
                trg.Shape_Square(playerID, 1, "50 + 1n Tank", 160, 160)
                # (Line 51) trg.Shape_Square(playerID,1,"Protoss Dark Archon",160,160);
                trg.Shape_Square(playerID, 1, "Protoss Dark Archon", 160, 160)
                # (Line 52) KillUnitAt(All,"Protoss Dark Archon","Anywhere",playerID);
                # (Line 53) trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0);
                DoActions(KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID))
                trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0)
                # (Line 54) Order("50 + 1n Tank", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                # (Line 55) trg.Main_Wait(800);
                DoActions(Order("50 + 1n Tank", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                trg.Main_Wait(800)
                # (Line 56) x = 0;
                x << (0)
                # (Line 57) }
                # (Line 58) else if (v.P_LoopMain[playerID] == 9)
            if EUDElseIf()(v.P_LoopMain[playerID] == 9):
                # (Line 59) {
                # (Line 60) trg.Shape_Edge(playerID,1,"60 + 1n Danimoth",45,3,64);
                trg.Shape_Edge(playerID, 1, "60 + 1n Danimoth", 45, 3, 64)
                # (Line 61) trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0);
                trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0)
                # (Line 62) Order("60 + 1n Danimoth", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                # (Line 63) trg.Main_Wait(160);
                DoActions(Order("60 + 1n Danimoth", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                trg.Main_Wait(160)
                # (Line 64) }
                # (Line 65) else if (v.P_LoopMain[playerID] == 10)
            if EUDElseIf()(v.P_LoopMain[playerID] == 10):
                # (Line 66) {
                # (Line 67) trg.Main_Wait(400);
                trg.Main_Wait(400)
                # (Line 68) }
                # (Line 69) else if (v.P_LoopMain[playerID] == 11)
            if EUDElseIf()(v.P_LoopMain[playerID] == 11):
                # (Line 70) {
                # (Line 71) trg.Shape_Dot(playerID,1,"60 + 1n Danimoth",0,0);
                trg.Shape_Dot(playerID, 1, "60 + 1n Danimoth", 0, 0)
                # (Line 72) Order("60 + 1n Danimoth", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                # (Line 73) trg.Main_Wait(160);
                DoActions(Order("60 + 1n Danimoth", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                trg.Main_Wait(160)
                # (Line 74) }
                # (Line 75) else if (v.P_LoopMain[playerID] == 12)
            if EUDElseIf()(v.P_LoopMain[playerID] == 12):
                # (Line 76) {
                # (Line 77) KillUnitAt(All,"50 + 1n Tank","Anywhere",playerID);
                # (Line 78) trg.SkillEnd();
                DoActions(KillUnitAt(All, "50 + 1n Tank", "Anywhere", playerID))
                trg.SkillEnd()
                # (Line 79) }
                # (Line 80) v.P_LoopMain[playerID] += 1;
            EUDEndIf()
            _ARRW(v.P_LoopMain, playerID).__iadd__(1)
            # (Line 81) }
            # (Line 82) }
        EUDEndIf()
        # (Line 83) }
    EUDEndIf()