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
    # (Line 8) trg.Buff_ShieldFix(20);
    trg.Buff_ShieldFix(20)
    # (Line 9) if (v.P_WaitMain[playerID] == 0)
    if EUDIf()(v.P_WaitMain[playerID] == 0):
        # (Line 10) {
        # (Line 11) if (v.P_CountMain[playerID] == 0)
        if EUDIf()(v.P_CountMain[playerID] == 0):
            # (Line 12) {
            # (Line 13) KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
            # (Line 14) RemoveUnitAt(All, "80 + 1n Vulture", "Anywhere", CurrentPlayer);
            DoActions(KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer))
            # (Line 15) RemoveUnitAt(All, "60 + 3n Ghost", "Anywhere", CurrentPlayer);
            DoActions(RemoveUnitAt(All, "80 + 1n Vulture", "Anywhere", CurrentPlayer))
            # (Line 16) KillUnitAt(All, "100 + 1n Hyperion", "Anywhere", CurrentPlayer);
            DoActions(RemoveUnitAt(All, "60 + 3n Ghost", "Anywhere", CurrentPlayer))
            # (Line 18) if (v.P_LoopMain[playerID] < 17)
            DoActions(KillUnitAt(All, "100 + 1n Hyperion", "Anywhere", CurrentPlayer))
            if EUDIf()(v.P_LoopMain[playerID] >= 17, neg=True):
                # (Line 19) {
                # (Line 20) var Degree = (15 * v.P_LoopMain[playerID]) % 90;
                Degree = EUDVariable()
                Degree << ((15 * v.P_LoopMain[playerID]) % 90)
                # (Line 21) trg.Table_Cos(playerID, Degree, 224);
                trg.Table_Cos(playerID, Degree, 224)
                # (Line 22) trg.Table_Sin(playerID, Degree, 224);
                trg.Table_Sin(playerID, Degree, 224)
                # (Line 24) trg.Shape_Square(playerID, 1, "40 + 1n Ghost", v.P_AngleCos[playerID], v.P_AngleSin[playerID]);
                trg.Shape_Square(playerID, 1, "40 + 1n Ghost", v.P_AngleCos[playerID], v.P_AngleSin[playerID])
                # (Line 25) adv.Shape_SquareAt(playerID, "40 + 1n Ghost", 1, "40 + 1n Mojo", 32, 32);
                adv.Shape_SquareAt(playerID, "40 + 1n Ghost", 1, "40 + 1n Mojo", 32, 32)
                # (Line 26) adv.Shape_SquareAt(playerID, "40 + 1n Ghost", 1, "40 + 1n Mojo", 0, 32);
                adv.Shape_SquareAt(playerID, "40 + 1n Ghost", 1, "40 + 1n Mojo", 0, 32)
                # (Line 27) adv.Shape_SquareAt(playerID, "40 + 1n Ghost", 1, "80 + 1n Vulture", 32, 32);
                adv.Shape_SquareAt(playerID, "40 + 1n Ghost", 1, "80 + 1n Vulture", 32, 32)
                # (Line 28) adv.Shape_SquareAt(playerID, "40 + 1n Ghost", 1, "80 + 1n Vulture", 0, 32);
                adv.Shape_SquareAt(playerID, "40 + 1n Ghost", 1, "80 + 1n Vulture", 0, 32)
                # (Line 29) RemoveUnitAt(1, "40 + 1n Ghost", "Anywhere", playerID);
                # (Line 30) adv.Shape_SquareAt(playerID, "40 + 1n Ghost", 1, "40 + 1n Mojo", 32, 32);
                DoActions(RemoveUnitAt(1, "40 + 1n Ghost", "Anywhere", playerID))
                adv.Shape_SquareAt(playerID, "40 + 1n Ghost", 1, "40 + 1n Mojo", 32, 32)
                # (Line 31) adv.Shape_SquareAt(playerID, "40 + 1n Ghost", 1, "40 + 1n Mojo", 0, 32);
                adv.Shape_SquareAt(playerID, "40 + 1n Ghost", 1, "40 + 1n Mojo", 0, 32)
                # (Line 32) adv.Shape_SquareAt(playerID, "40 + 1n Ghost", 1, "80 + 1n Vulture", 32, 32);
                adv.Shape_SquareAt(playerID, "40 + 1n Ghost", 1, "80 + 1n Vulture", 32, 32)
                # (Line 33) adv.Shape_SquareAt(playerID, "40 + 1n Ghost", 1, "80 + 1n Vulture", 0, 32);
                adv.Shape_SquareAt(playerID, "40 + 1n Ghost", 1, "80 + 1n Vulture", 0, 32)
                # (Line 34) RemoveUnitAt(1, "40 + 1n Ghost", "Anywhere", playerID);
                # (Line 35) adv.Shape_SquareAt(playerID, "40 + 1n Ghost", 1, "40 + 1n Mojo", 32, 32);
                DoActions(RemoveUnitAt(1, "40 + 1n Ghost", "Anywhere", playerID))
                adv.Shape_SquareAt(playerID, "40 + 1n Ghost", 1, "40 + 1n Mojo", 32, 32)
                # (Line 36) adv.Shape_SquareAt(playerID, "40 + 1n Ghost", 1, "40 + 1n Mojo", 0, 32);
                adv.Shape_SquareAt(playerID, "40 + 1n Ghost", 1, "40 + 1n Mojo", 0, 32)
                # (Line 37) adv.Shape_SquareAt(playerID, "40 + 1n Ghost", 1, "80 + 1n Vulture", 32, 32);
                adv.Shape_SquareAt(playerID, "40 + 1n Ghost", 1, "80 + 1n Vulture", 32, 32)
                # (Line 38) adv.Shape_SquareAt(playerID, "40 + 1n Ghost", 1, "80 + 1n Vulture", 0, 32);
                adv.Shape_SquareAt(playerID, "40 + 1n Ghost", 1, "80 + 1n Vulture", 0, 32)
                # (Line 39) RemoveUnitAt(1, "40 + 1n Ghost", "Anywhere", playerID);
                # (Line 40) adv.Shape_SquareAt(playerID, "40 + 1n Ghost", 1, "40 + 1n Mojo", 32, 32);
                DoActions(RemoveUnitAt(1, "40 + 1n Ghost", "Anywhere", playerID))
                adv.Shape_SquareAt(playerID, "40 + 1n Ghost", 1, "40 + 1n Mojo", 32, 32)
                # (Line 41) adv.Shape_SquareAt(playerID, "40 + 1n Ghost", 1, "40 + 1n Mojo", 0, 32);
                adv.Shape_SquareAt(playerID, "40 + 1n Ghost", 1, "40 + 1n Mojo", 0, 32)
                # (Line 42) adv.Shape_SquareAt(playerID, "40 + 1n Ghost", 1, "80 + 1n Vulture", 32, 32);
                adv.Shape_SquareAt(playerID, "40 + 1n Ghost", 1, "80 + 1n Vulture", 32, 32)
                # (Line 43) adv.Shape_SquareAt(playerID, "40 + 1n Ghost", 1, "80 + 1n Vulture", 0, 32);
                adv.Shape_SquareAt(playerID, "40 + 1n Ghost", 1, "80 + 1n Vulture", 0, 32)
                # (Line 44) RemoveUnitAt(1, "40 + 1n Ghost", "Anywhere", playerID);
                # (Line 45) trg.Shape_Square(playerID, 1, "40 + 1n Gantrithor", v.P_AngleCos[playerID], v.P_AngleSin[playerID]);
                DoActions(RemoveUnitAt(1, "40 + 1n Ghost", "Anywhere", playerID))
                trg.Shape_Square(playerID, 1, "40 + 1n Gantrithor", v.P_AngleCos[playerID], v.P_AngleSin[playerID])
                # (Line 46) trg.Shape_Square(playerID, 1, "60 + 3n Ghost", v.P_AngleCos[playerID], v.P_AngleSin[playerID]);
                trg.Shape_Square(playerID, 1, "60 + 3n Ghost", v.P_AngleCos[playerID], v.P_AngleSin[playerID])
                # (Line 47) trg.Shape_Square(playerID, 1, "100 + 1n Hyperion", 32, 32);
                trg.Shape_Square(playerID, 1, "100 + 1n Hyperion", 32, 32)
                # (Line 48) trg.Shape_Square(playerID, 1, "100 + 1n Hyperion", 0, 32);
                trg.Shape_Square(playerID, 1, "100 + 1n Hyperion", 0, 32)
                # (Line 49) trg.Shape_Square(playerID, 1, "Bengalaas", 32, 32);
                trg.Shape_Square(playerID, 1, "Bengalaas", 32, 32)
                # (Line 50) trg.Shape_Square(playerID, 1, "Bengalaas", 0, 32);
                trg.Shape_Square(playerID, 1, "Bengalaas", 0, 32)
                # (Line 52) MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
                # (Line 53) Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                DoActions(MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere"))
                # (Line 54) Order("80 + 1n Vulture", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                DoActions(Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                # (Line 55) Order("60 + 3n Ghost", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                DoActions(Order("80 + 1n Vulture", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                # (Line 56) Order("100 + 1n Hyperion", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                DoActions(Order("60 + 3n Ghost", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                # (Line 57) KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", playerID);
                DoActions(Order("100 + 1n Hyperion", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                # (Line 58) KillUnitAt(All, "Bengalaas", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", playerID))
                # (Line 59) trg.Main_Wait(83);
                DoActions(KillUnitAt(All, "Bengalaas", "Anywhere", playerID))
                trg.Main_Wait(83)
                # (Line 60) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 61) }
                # (Line 62) else if (v.P_LoopMain[playerID] == 17)
            if EUDElseIf()(v.P_LoopMain[playerID] == 17):
                # (Line 63) {
                # (Line 64) trg.SkillEnd();
                trg.SkillEnd()
                # (Line 65) }
                # (Line 66) }
            EUDEndIf()
            # (Line 67) }
        EUDEndIf()
        # (Line 68) }
    EUDEndIf()