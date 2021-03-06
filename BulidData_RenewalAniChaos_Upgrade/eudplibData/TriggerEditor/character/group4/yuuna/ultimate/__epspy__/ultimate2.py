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
# (Line 6) function FlowerShape(cp : TrgPlayer, count, Unit : TrgUnit, i, distance, interval);
# (Line 8) function main(playerID)
# (Line 9) {
@EUDFunc
def f_main(playerID):
    # (Line 10) MoveLocation("22.Yuuna_Bozo", v.P_UnitID[playerID], playerID, "Anywhere");
    # (Line 11) trg.Debuff_BanReturn();
    DoActions(MoveLocation("22.Yuuna_Bozo", v.P_UnitID[playerID], playerID, "Anywhere"))
    trg.Debuff_BanReturn()
    # (Line 12) trg.Debuff_Stop();
    trg.Debuff_Stop()
    # (Line 13) trg.Buff_ShieldFix(1);
    trg.Buff_ShieldFix(1)
    # (Line 15) if (v.P_WaitMain[playerID] == 0)
    if EUDIf()(v.P_WaitMain[playerID] == 0):
        # (Line 16) {
        # (Line 17) if (v.P_CountMain[playerID] == 0)
        if EUDIf()(v.P_CountMain[playerID] == 0):
            # (Line 18) {
            # (Line 19) if (v.P_LoopMain[playerID] == 0)
            if EUDIf()(v.P_LoopMain[playerID] == 0):
                # (Line 20) {
                # (Line 21) SetSwitch("Recall - Yuuna", Set);
                # (Line 24) trg.Main_Wait(2000);
                DoActions(SetSwitch("Recall - Yuuna", Set))
                trg.Main_Wait(2000)
                # (Line 26) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 27) }
                # (Line 28) else if (v.P_LoopMain[playerID] == 1)
            if EUDElseIf()(v.P_LoopMain[playerID] == 1):
                # (Line 29) {
                # (Line 30) trg.Main_Wait(80);
                trg.Main_Wait(80)
                # (Line 32) v.P_CountMain[playerID] += 1;
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 33) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 34) v.P_LoopSub1[playerID] = 0;
                _ARRW(v.P_LoopSub1, playerID) << (0)
                # (Line 35) }
                # (Line 36) }
            EUDEndIf()
            # (Line 37) else if (v.P_CountMain[playerID] == 1)
        if EUDElseIf()(v.P_CountMain[playerID] == 1):
            # (Line 38) {
            # (Line 39) if (v.P_LoopMain[playerID] == 0)
            if EUDIf()(v.P_LoopMain[playerID] == 0):
                # (Line 40) {
                # (Line 41) trg.Main_Wait(3200);
                trg.Main_Wait(3200)
                # (Line 43) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 44) }
                # (Line 45) else if (v.P_LoopMain[playerID] == 1)
            if EUDElseIf()(v.P_LoopMain[playerID] == 1):
                # (Line 46) {
                # (Line 47) s.CharacterVoice(13);
                s.CharacterVoice(13)
                # (Line 49) trg.Main_Wait(80);
                trg.Main_Wait(80)
                # (Line 51) v.P_CountMain[playerID] += 1;
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 52) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 53) v.P_LoopSub1[playerID] = 0;
                _ARRW(v.P_LoopSub1, playerID) << (0)
                # (Line 54) }
                # (Line 55) }
            EUDEndIf()
            # (Line 56) else if (v.P_CountMain[playerID] == 2)
        if EUDElseIf()(v.P_CountMain[playerID] == 2):
            # (Line 57) {
            # (Line 58) if (v.P_LoopMain[playerID] < 4)
            if EUDIf()(v.P_LoopMain[playerID] >= 4, neg=True):
                # (Line 59) {
                # (Line 60) trg.Shape_NxNSquare(playerID, 1, "40 + 1n Wraith", 2 * v.P_LoopMain[playerID] + 5, 75);
                trg.Shape_NxNSquare(playerID, 1, "40 + 1n Wraith", 2 * v.P_LoopMain[playerID] + 5, 75)
                # (Line 61) trg.Shape_NxNSquare(playerID, 1, "50 + 1n Tank", 2 * v.P_LoopMain[playerID] + 5, 75);
                trg.Shape_NxNSquare(playerID, 1, "50 + 1n Tank", 2 * v.P_LoopMain[playerID] + 5, 75)
                # (Line 62) KillUnitAt(All, "50 + 1n Tank", "Anywhere", playerID);
                # (Line 63) KillUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "50 + 1n Tank", "Anywhere", playerID))
                # (Line 65) trg.Main_Wait(80);
                DoActions(KillUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID))
                trg.Main_Wait(80)
                # (Line 67) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 68) }
                # (Line 69) else if (v.P_LoopMain[playerID] == 4)
            if EUDElseIf()(v.P_LoopMain[playerID] == 4):
                # (Line 70) {
                # (Line 71) trg.Shape_NxNSquare(playerID, 1, "130 + 1n Norad", 11, 75);
                trg.Shape_NxNSquare(playerID, 1, "130 + 1n Norad", 11, 75)
                # (Line 72) trg.Shape_NxNSquare(playerID, 1, "60 + 1n Siege", 11, 75);
                trg.Shape_NxNSquare(playerID, 1, "60 + 1n Siege", 11, 75)
                # (Line 73) KillUnitAt(All, "130 + 1n Norad", "Anywhere", playerID);
                # (Line 75) trg.Main_Wait(80);
                DoActions(KillUnitAt(All, "130 + 1n Norad", "Anywhere", playerID))
                trg.Main_Wait(80)
                # (Line 77) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 78) }
                # (Line 79) else if (v.P_LoopMain[playerID] == 5)
            if EUDElseIf()(v.P_LoopMain[playerID] == 5):
                # (Line 80) {
                # (Line 81) trg.Main_Wait(1120);
                trg.Main_Wait(1120)
                # (Line 83) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 84) }
                # (Line 85) else if (v.P_LoopMain[playerID] == 6)
            if EUDElseIf()(v.P_LoopMain[playerID] == 6):
                # (Line 86) {
                # (Line 87) trg.Main_Wait(80);
                trg.Main_Wait(80)
                # (Line 89) v.P_CountMain[playerID] += 1;
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 90) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 91) v.P_LoopSub1[playerID] = 0;
                _ARRW(v.P_LoopSub1, playerID) << (0)
                # (Line 92) }
                # (Line 93) }
            EUDEndIf()
            # (Line 94) else if (v.P_CountMain[playerID] == 3)
        if EUDElseIf()(v.P_CountMain[playerID] == 3):
            # (Line 95) {
            # (Line 96) if (v.P_LoopMain[playerID] == 0)
            if EUDIf()(v.P_LoopMain[playerID] == 0):
                # (Line 97) {
                # (Line 98) trg.Main_Wait(1280);
                trg.Main_Wait(1280)
                # (Line 100) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 101) }
                # (Line 102) else if (v.P_LoopMain[playerID] == 1)
            if EUDElseIf()(v.P_LoopMain[playerID] == 1):
                # (Line 103) {
                # (Line 104) trg.Main_Wait(80);
                trg.Main_Wait(80)
                # (Line 106) v.P_CountMain[playerID] += 1;
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 107) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 108) v.P_LoopSub1[playerID] = 0;
                _ARRW(v.P_LoopSub1, playerID) << (0)
                # (Line 109) }
                # (Line 110) }
            EUDEndIf()
            # (Line 111) else if (v.P_CountMain[playerID] == 4)
        if EUDElseIf()(v.P_CountMain[playerID] == 4):
            # (Line 112) {
            # (Line 113) if (v.P_LoopMain[playerID] < 4)
            if EUDIf()(v.P_LoopMain[playerID] >= 4, neg=True):
                # (Line 114) {
                # (Line 115) RemoveUnitAt(All, "130 + 1n Norad", "Anywhere", playerID);
                # (Line 116) trg.Shape_NxNSquare(playerID, 1, "130 + 1n Norad", 2 * v.P_LoopMain[playerID] + 5, 75);
                DoActions(RemoveUnitAt(All, "130 + 1n Norad", "Anywhere", playerID))
                trg.Shape_NxNSquare(playerID, 1, "130 + 1n Norad", 2 * v.P_LoopMain[playerID] + 5, 75)
                # (Line 117) trg.Shape_NxNSquare(playerID, 1, "50 + 1n Tank", 2 * v.P_LoopMain[playerID] + 5, 75);
                trg.Shape_NxNSquare(playerID, 1, "50 + 1n Tank", 2 * v.P_LoopMain[playerID] + 5, 75)
                # (Line 118) KillUnitAt(All, "50 + 1n Tank", "Anywhere", playerID);
                # (Line 119) MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
                DoActions(KillUnitAt(All, "50 + 1n Tank", "Anywhere", playerID))
                # (Line 120) Order("130 + 1n Norad", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                DoActions(MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere"))
                # (Line 122) trg.Main_Wait(80);
                DoActions(Order("130 + 1n Norad", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                trg.Main_Wait(80)
                # (Line 124) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 125) }
                # (Line 126) else if (v.P_LoopMain[playerID] == 4)
            if EUDElseIf()(v.P_LoopMain[playerID] == 4):
                # (Line 127) {
                # (Line 128) trg.Main_Wait(4000);
                trg.Main_Wait(4000)
                # (Line 130) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 131) }
                # (Line 132) else if (v.P_LoopMain[playerID] == 5)
            if EUDElseIf()(v.P_LoopMain[playerID] == 5):
                # (Line 133) {
                # (Line 134) KillUnitAt(All, "130 + 1n Norad", "Anywhere", playerID);
                # (Line 135) KillUnitAt(All, "60 + 1n Siege", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "130 + 1n Norad", "Anywhere", playerID))
                # (Line 136) SetDeaths(playerID, SetTo, 0, " `ShieldRecharge");
                DoActions(KillUnitAt(All, "60 + 1n Siege", "Anywhere", playerID))
                # (Line 138) trg.Main_Wait(80);
                DoActions(SetDeaths(playerID, SetTo, 0, " `ShieldRecharge"))
                trg.Main_Wait(80)
                # (Line 140) v.P_CountMain[playerID] += 1;
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 141) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 142) v.P_LoopSub1[playerID] = 0;
                _ARRW(v.P_LoopSub1, playerID) << (0)
                # (Line 143) }
                # (Line 144) }
            EUDEndIf()
            # (Line 145) else if (v.P_CountMain[playerID] == 5)
        if EUDElseIf()(v.P_CountMain[playerID] == 5):
            # (Line 146) {
            # (Line 147) SetSwitch("Recall - Yuuna", Clear);
            # (Line 148) SetSwitch("UiltimateSwitch", Clear);
            DoActions(SetSwitch("Recall - Yuuna", Clear))
            # (Line 149) trg.SkillEnd();
            DoActions(SetSwitch("UiltimateSwitch", Clear))
            trg.SkillEnd()
            # (Line 150) }
            # (Line 151) }
        EUDEndIf()
        # (Line 153) if (v.P_WaitSub1[playerID] == 0)
    EUDEndIf()
    if EUDIf()(v.P_WaitSub1[playerID] == 0):
        # (Line 154) {
        # (Line 155) if (v.P_CountMain[playerID] == 1)
        if EUDIf()(v.P_CountMain[playerID] == 1):
            # (Line 156) {
            # (Line 157) if (v.P_LoopSub1[playerID] < 32)
            if EUDIf()(v.P_LoopSub1[playerID] >= 32, neg=True):
                # (Line 158) {
                # (Line 159) trg.Table_Sin(playerID, 50 * v.P_LoopSub1[playerID], 50 + 10 * v.P_LoopSub1[playerID]);
                trg.Table_Sin(playerID, 50 * v.P_LoopSub1[playerID], 50 + 10 * v.P_LoopSub1[playerID])
                # (Line 160) trg.Table_Cos(playerID, 50 * v.P_LoopSub1[playerID], 50 + 10 * v.P_LoopSub1[playerID]);
                trg.Table_Cos(playerID, 50 * v.P_LoopSub1[playerID], 50 + 10 * v.P_LoopSub1[playerID])
                # (Line 162) trg.Shape_Square(playerID, 16, "Rhynadon (Badlands)", v.P_AngleCos[playerID], v.P_AngleSin[playerID]);
                trg.Shape_Square(playerID, 16, "Rhynadon (Badlands)", v.P_AngleCos[playerID], v.P_AngleSin[playerID])
                # (Line 163) KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", playerID);
                # (Line 165) trg.Sub1_Wait(80);
                DoActions(KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", playerID))
                trg.Sub1_Wait(80)
                # (Line 167) v.P_LoopSub1[playerID] += 1;
                _ARRW(v.P_LoopSub1, playerID).__iadd__(1)
                # (Line 168) }
                # (Line 169) }
            EUDEndIf()
            # (Line 170) if (v.P_CountMain[playerID] == 3)
        EUDEndIf()
        if EUDIf()(v.P_CountMain[playerID] == 3):
            # (Line 171) {
            # (Line 172) if (v.P_LoopSub1[playerID] == 0)
            if EUDIf()(v.P_LoopSub1[playerID] == 0):
                # (Line 173) {
                # (Line 174) RemoveUnitAt(All, "130 + 1n Norad", "Anywhere", playerID);
                # (Line 175) trg.Shape_NxNSquare(playerID, 1, "130 + 1n Norad", 3, 75);
                DoActions(RemoveUnitAt(All, "130 + 1n Norad", "Anywhere", playerID))
                trg.Shape_NxNSquare(playerID, 1, "130 + 1n Norad", 3, 75)
                # (Line 176) Order("130 + 1n Norad", playerID, "Anywhere", Attack, "Anywhere");
                # (Line 177) trg.Shape_NxNSquare(playerID, 1, "50 + 1n Tank", 3, 75);
                DoActions(Order("130 + 1n Norad", playerID, "Anywhere", Attack, "Anywhere"))
                trg.Shape_NxNSquare(playerID, 1, "50 + 1n Tank", 3, 75)
                # (Line 178) KillUnitAt(All, "50 + 1n Tank", "Anywhere", playerID);
                # (Line 180) trg.Sub1_Wait(80);
                DoActions(KillUnitAt(All, "50 + 1n Tank", "Anywhere", playerID))
                trg.Sub1_Wait(80)
                # (Line 182) v.P_LoopSub1[playerID] = 0;
                _ARRW(v.P_LoopSub1, playerID) << (0)
                # (Line 183) }
                # (Line 184) }
            EUDEndIf()
            # (Line 185) }
        EUDEndIf()
        # (Line 186) }
    EUDEndIf()
