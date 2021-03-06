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
# (Line 4) import func.sound as s;
from func import sound as s
# (Line 6) function main(playerID)
# (Line 7) {
@EUDFunc
def f_main(playerID):
    # (Line 8) trg.Debuff_Stop();
    trg.Debuff_Stop()
    # (Line 9) MoveLocation("23.Mayuri_Bozo", v.P_UnitID[playerID], playerID, "Anywhere");
    # (Line 10) MoveUnit(All, "50 + 1n Battlecruiser", playerID, "Anywhere", "[Skill]HoldPosition");
    DoActions(MoveLocation("23.Mayuri_Bozo", v.P_UnitID[playerID], playerID, "Anywhere"))
    # (Line 11) trg.Buff_ShieldFix(1);
    DoActions(MoveUnit(All, "50 + 1n Battlecruiser", playerID, "Anywhere", "[Skill]HoldPosition"))
    trg.Buff_ShieldFix(1)
    # (Line 13) if (v.P_WaitMain[playerID] == 0)
    if EUDIf()(v.P_WaitMain[playerID] == 0):
        # (Line 14) {
        # (Line 15) if (v.P_CountMain[playerID] == 0)
        if EUDIf()(v.P_CountMain[playerID] == 0):
            # (Line 16) {
            # (Line 17) if (v.P_LoopMain[playerID] < 12)
            if EUDIf()(v.P_LoopMain[playerID] >= 12, neg=True):
                # (Line 18) {
                # (Line 19) SetDeaths(playerID, SetTo, 1, " `ShieldRecharge");
                # (Line 21) GiveUnits(All, "60 + 3n Siege", P9, "Anywhere", playerID);
                DoActions(SetDeaths(playerID, SetTo, 1, " `ShieldRecharge"))
                # (Line 22) SetSwitch("Recall - Mayuri", Set);
                DoActions(GiveUnits(All, "60 + 3n Siege", P9, "Anywhere", playerID))
                # (Line 24) KillUnitAt(10, "50 + 1n Battlecruiser", "Anywhere", playerID);
                DoActions(SetSwitch("Recall - Mayuri", Set))
                # (Line 26) trg.Main_Wait(80);
                DoActions(KillUnitAt(10, "50 + 1n Battlecruiser", "Anywhere", playerID))
                trg.Main_Wait(80)
                # (Line 28) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 29) }
                # (Line 30) else if (v.P_LoopMain[playerID] == 12)
            if EUDElseIf()(v.P_LoopMain[playerID] == 12):
                # (Line 31) {
                # (Line 32) s.CharacterVoice(14);
                s.CharacterVoice(14)
                # (Line 34) KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID);
                # (Line 36) trg.Main_Wait(80);
                DoActions(KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID))
                trg.Main_Wait(80)
                # (Line 38) v.P_CountMain[playerID] += 1;
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 39) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 40) }
                # (Line 41) }
            EUDEndIf()
            # (Line 42) else if (v.P_CountMain[playerID] == 1)
        if EUDElseIf()(v.P_CountMain[playerID] == 1):
            # (Line 43) {
            # (Line 44) if (v.P_LoopMain[playerID] < 36)
            if EUDIf()(v.P_LoopMain[playerID] >= 36, neg=True):
                # (Line 45) {
                # (Line 46) KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", playerID);
                # (Line 48) trg.Shape_NxNSquare(playerID, 1, " Creep. Dunkelheit", 7, 75);
                DoActions(KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", playerID))
                trg.Shape_NxNSquare(playerID, 1, " Creep. Dunkelheit", 7, 75)
                # (Line 50) MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
                # (Line 51) MoveUnit(All, " Creep. Dunkelheit", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
                DoActions(MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere"))
                # (Line 52) Order(" Creep. Dunkelheit", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                DoActions(MoveUnit(All, " Creep. Dunkelheit", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]))
                # (Line 54) trg.Main_Wait(80);
                DoActions(Order(" Creep. Dunkelheit", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                trg.Main_Wait(80)
                # (Line 56) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 57) }
                # (Line 58) else if (v.P_LoopMain[playerID] == 36)
            if EUDElseIf()(v.P_LoopMain[playerID] == 36):
                # (Line 59) {
                # (Line 60) KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", playerID);
                # (Line 61) KillUnitAt(All, "60 + 3n Siege", "Anywhere", playerID);
                DoActions(KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", playerID))
                # (Line 63) trg.Main_Wait(80);
                DoActions(KillUnitAt(All, "60 + 3n Siege", "Anywhere", playerID))
                trg.Main_Wait(80)
                # (Line 65) v.P_CountMain[playerID] += 1;
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 66) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 67) }
                # (Line 68) }
            EUDEndIf()
            # (Line 69) else if (v.P_CountMain[playerID] == 2)
        if EUDElseIf()(v.P_CountMain[playerID] == 2):
            # (Line 70) {
            # (Line 72) SetSwitch("Recall - Mayuri", Clear);
            # (Line 73) SetSwitch("UiltimateSwitch", Clear);
            DoActions(SetSwitch("Recall - Mayuri", Clear))
            # (Line 74) trg.SkillEnd();
            DoActions(SetSwitch("UiltimateSwitch", Clear))
            trg.SkillEnd()
            # (Line 75) }
            # (Line 76) }
        EUDEndIf()
        # (Line 77) }
    EUDEndIf()
