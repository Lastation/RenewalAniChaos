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
# (Line 5) function FlowerShape(playerID : TrgPlayer, count, Unit : TrgUnit, i, distance, interval);
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
            # (Line 13) if (v.P_LoopMain[playerID] < 4)
            if EUDIf()(v.P_LoopMain[playerID] >= 4, neg=True):
                # (Line 14) {
                # (Line 15) FlowerShape(playerID, 1, "40 + 1n Mojo", 0, 50, 50);
                FlowerShape(playerID, 1, "40 + 1n Mojo", 0, 50, 50)
                # (Line 16) FlowerShape(playerID, 1, "40 + 1n Mojo", 1, 50, 50);
                FlowerShape(playerID, 1, "40 + 1n Mojo", 1, 50, 50)
                # (Line 17) FlowerShape(playerID, 1, "40 + 1n Mojo", 2, 50, 50);
                FlowerShape(playerID, 1, "40 + 1n Mojo", 2, 50, 50)
                # (Line 18) FlowerShape(playerID, 1, "40 + 1n Mojo", 3, 50, 50);
                FlowerShape(playerID, 1, "40 + 1n Mojo", 3, 50, 50)
                # (Line 19) FlowerShape(playerID, 1, "40 + 1n Mojo", 4, 50, 50);
                FlowerShape(playerID, 1, "40 + 1n Mojo", 4, 50, 50)
                # (Line 20) FlowerShape(playerID, 1, "60 + 1n Archon", 0, 50, 50);
                FlowerShape(playerID, 1, "60 + 1n Archon", 0, 50, 50)
                # (Line 21) FlowerShape(playerID, 1, "60 + 1n Archon", 1, 50, 50);
                FlowerShape(playerID, 1, "60 + 1n Archon", 1, 50, 50)
                # (Line 22) FlowerShape(playerID, 1, "60 + 1n Archon", 2, 50, 50);
                FlowerShape(playerID, 1, "60 + 1n Archon", 2, 50, 50)
                # (Line 23) FlowerShape(playerID, 1, "60 + 1n Archon", 3, 50, 50);
                FlowerShape(playerID, 1, "60 + 1n Archon", 3, 50, 50)
                # (Line 24) FlowerShape(playerID, 1, "60 + 1n Archon", 4, 50, 50);
                FlowerShape(playerID, 1, "60 + 1n Archon", 4, 50, 50)
                # (Line 26) KillUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID);
                # (Line 27) KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID))
                # (Line 29) trg.Main_Wait(80);
                DoActions(KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID))
                trg.Main_Wait(80)
                # (Line 31) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 32) }
                # (Line 33) else if (v.P_LoopMain[playerID] == 4)
            if EUDElseIf()(v.P_LoopMain[playerID] == 4):
                # (Line 34) {
                # (Line 35) FlowerShape(playerID, 1, "40 + 1n Guardian", 0, 50, 50);
                FlowerShape(playerID, 1, "40 + 1n Guardian", 0, 50, 50)
                # (Line 36) FlowerShape(playerID, 1, "40 + 1n Guardian", 1, 50, 50);
                FlowerShape(playerID, 1, "40 + 1n Guardian", 1, 50, 50)
                # (Line 37) FlowerShape(playerID, 1, "40 + 1n Guardian", 2, 50, 50);
                FlowerShape(playerID, 1, "40 + 1n Guardian", 2, 50, 50)
                # (Line 38) FlowerShape(playerID, 1, "40 + 1n Guardian", 3, 50, 50);
                FlowerShape(playerID, 1, "40 + 1n Guardian", 3, 50, 50)
                # (Line 39) FlowerShape(playerID, 1, "40 + 1n Guardian", 4, 50, 50);
                FlowerShape(playerID, 1, "40 + 1n Guardian", 4, 50, 50)
                # (Line 40) FlowerShape(playerID, 1, "Protoss Dark Archon", 0, 50, 50);
                FlowerShape(playerID, 1, "Protoss Dark Archon", 0, 50, 50)
                # (Line 41) FlowerShape(playerID, 1, "Protoss Dark Archon", 1, 50, 50);
                FlowerShape(playerID, 1, "Protoss Dark Archon", 1, 50, 50)
                # (Line 42) FlowerShape(playerID, 1, "Protoss Dark Archon", 2, 50, 50);
                FlowerShape(playerID, 1, "Protoss Dark Archon", 2, 50, 50)
                # (Line 43) FlowerShape(playerID, 1, "Protoss Dark Archon", 3, 50, 50);
                FlowerShape(playerID, 1, "Protoss Dark Archon", 3, 50, 50)
                # (Line 44) FlowerShape(playerID, 1, "Protoss Dark Archon", 4, 50, 50);
                FlowerShape(playerID, 1, "Protoss Dark Archon", 4, 50, 50)
                # (Line 46) KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID);
                # (Line 47) KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID))
                # (Line 48) SetDeaths(playerID, SetTo, 720, " `UniqueCoolTime");
                DoActions(KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID))
                # (Line 49) SetDeaths(playerID, Add, 1, " `UniqueSkill");
                DoActions(SetDeaths(playerID, SetTo, 720, " `UniqueCoolTime"))
                # (Line 51) trg.Main_Wait(80);
                DoActions(SetDeaths(playerID, Add, 1, " `UniqueSkill"))
                trg.Main_Wait(80)
                # (Line 53) v.P_CountMain[playerID] += 1;
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 54) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 55) }
                # (Line 56) }
            EUDEndIf()
            # (Line 58) else if (v.P_CountMain[playerID] == 1)
        if EUDElseIf()(v.P_CountMain[playerID] == 1):
            # (Line 59) {
            # (Line 60) trg.SkillEnd();
            trg.SkillEnd()
            # (Line 61) }
            # (Line 62) }
        EUDEndIf()
        # (Line 63) }
    EUDEndIf()
    # (Line 66) function FlowerShape(playerID : TrgPlayer, count, Unit : TrgUnit, i, distance, interval)

# (Line 68) {
@EUDTypedFunc([TrgPlayer, None, TrgUnit, None, None, None])
def FlowerShape(playerID, count, Unit, i, distance, interval):
    # (Line 69) trg.Table_Sin(playerID, (72 * i + 90), distance);
    trg.Table_Sin(playerID, (72 * i + 90), distance)
    # (Line 70) trg.Table_Cos(playerID, (72 * i + 90), distance);
    trg.Table_Cos(playerID, (72 * i + 90), distance)
    # (Line 72) var x_o = v.P_AngleCos[playerID];
    x_o = EUDVariable()
    x_o << (v.P_AngleCos[playerID])
    # (Line 73) var y_o = v.P_AngleSin[playerID];
    y_o = EUDVariable()
    y_o << (v.P_AngleSin[playerID])
    # (Line 75) trg.Table_Sin(playerID, ((72 * i + 90) + 30), interval);
    trg.Table_Sin(playerID, ((72 * i + 90) + 30), interval)
    # (Line 76) trg.Table_Cos(playerID, ((72 * i + 90) + 30), interval);
    trg.Table_Cos(playerID, ((72 * i + 90) + 30), interval)
    # (Line 78) var x_i1 = v.P_AngleCos[playerID];
    x_i1 = EUDVariable()
    x_i1 << (v.P_AngleCos[playerID])
    # (Line 79) var y_i1 = v.P_AngleSin[playerID];
    y_i1 = EUDVariable()
    y_i1 << (v.P_AngleSin[playerID])
    # (Line 81) trg.Table_Sin(playerID, ((72 * i + 90) - 30), interval);
    trg.Table_Sin(playerID, ((72 * i + 90) - 30), interval)
    # (Line 82) trg.Table_Cos(playerID, ((72 * i + 90) - 30), interval);
    trg.Table_Cos(playerID, ((72 * i + 90) - 30), interval)
    # (Line 84) var x_i2 = v.P_AngleCos[playerID];
    x_i2 = EUDVariable()
    x_i2 << (v.P_AngleCos[playerID])
    # (Line 85) var y_i2 = v.P_AngleSin[playerID];
    y_i2 = EUDVariable()
    y_i2 << (v.P_AngleSin[playerID])
    # (Line 87) var x = x_o;
    x = EUDVariable()
    x << (x_o)
    # (Line 88) var y = y_o;
    y = EUDVariable()
    y << (y_o)
    # (Line 90) trg.Shape_Dot(playerID, 1, Unit, x, y);
    trg.Shape_Dot(playerID, 1, Unit, x, y)
    # (Line 92) x = x + x_i1;
    x << (x + x_i1)
    # (Line 93) y = y + y_i1;
    y << (y + y_i1)
    # (Line 95) trg.Shape_Dot(playerID, 1, Unit, x, y);
    trg.Shape_Dot(playerID, 1, Unit, x, y)
    # (Line 97) x = x + x_i1;
    x << (x + x_i1)
    # (Line 98) y = y + y_i1;
    y << (y + y_i1)
    # (Line 100) trg.Shape_Dot(playerID, 1, Unit, x, y);
    trg.Shape_Dot(playerID, 1, Unit, x, y)
    # (Line 102) x = x + x_i2;
    x << (x + x_i2)
    # (Line 103) y = y + y_i2;
    y << (y + y_i2)
    # (Line 105) trg.Shape_Dot(playerID, 1, Unit, x, y);
    trg.Shape_Dot(playerID, 1, Unit, x, y)
    # (Line 107) x = x + x_i2;
    x << (x + x_i2)
    # (Line 108) y = y + y_i2;
    y << (y + y_i2)
    # (Line 110) trg.Shape_Dot(playerID, 1, Unit, x, y);
    trg.Shape_Dot(playerID, 1, Unit, x, y)
    # (Line 112) x = x_o + x_i2;
    x << (x_o + x_i2)
    # (Line 113) y = y_o + y_i2;
    y << (y_o + y_i2)
    # (Line 115) trg.Shape_Dot(playerID, 1, Unit, x, y);
    trg.Shape_Dot(playerID, 1, Unit, x, y)
    # (Line 117) x = x + x_i2;
    x << (x + x_i2)
    # (Line 118) y = y + y_i2;
    y << (y + y_i2)
    # (Line 120) trg.Shape_Dot(playerID, 1, Unit, x, y);
    trg.Shape_Dot(playerID, 1, Unit, x, y)
    # (Line 122) x = x + x_i1;
    x << (x + x_i1)
    # (Line 123) y = y + y_i1;
    y << (y + y_i1)
    # (Line 125) trg.Shape_Dot(playerID, 1, Unit, x, y);
    trg.Shape_Dot(playerID, 1, Unit, x, y)
    # (Line 126) }