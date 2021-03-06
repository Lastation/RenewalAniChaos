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
    # (Line 9) if (v.P_CountMain[playerID] == 1)
    if EUDIf()(v.P_CountMain[playerID] == 1):
        # (Line 10) {
        # (Line 11) MoveLocation("25.Milim_Bozo", v.P_UnitID[playerID], playerID, "Anywhere");
        # (Line 12) }
        DoActions(MoveLocation("25.Milim_Bozo", v.P_UnitID[playerID], playerID, "Anywhere"))
        # (Line 14) trg.Debuff_Stop();
    EUDEndIf()
    trg.Debuff_Stop()
    # (Line 15) trg.Debuff_BanReturn();
    trg.Debuff_BanReturn()
    # (Line 17) if (v.P_WaitMain[playerID] == 0)
    if EUDIf()(v.P_WaitMain[playerID] == 0):
        # (Line 18) {
        # (Line 19) if (v.P_CountMain[playerID] == 0)
        if EUDIf()(v.P_CountMain[playerID] == 0):
            # (Line 20) {
            # (Line 21) if (v.P_LoopMain[playerID] == 0)
            if EUDIf()(v.P_LoopMain[playerID] == 0):
                # (Line 22) {
                # (Line 23) CreateUnit(1, "Flame Blue", "[Skill]Unit_Wait_8", playerID);
                # (Line 24) SetInvincibility(Enable, "Any unit", playerID, "[Skill]Unit_Wait_ALL");
                DoActions(CreateUnit(1, "Flame Blue", "[Skill]Unit_Wait_8", playerID))
                # (Line 25) MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
                DoActions(SetInvincibility(Enable, "Any unit", playerID, "[Skill]Unit_Wait_ALL"))
                # (Line 26) MoveUnit(All, "Flame Blue", playerID, "Anywhere", v.P_LocationID[playerID]);
                DoActions(MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere"))
                # (Line 27) MoveLocation("25.Milim_Bozo", "Flame Blue", playerID, "Anywhere");
                DoActions(MoveUnit(All, "Flame Blue", playerID, "Anywhere", v.P_LocationID[playerID]))
                # (Line 29) trg.Main_Wait(80);
                DoActions(MoveLocation("25.Milim_Bozo", "Flame Blue", playerID, "Anywhere"))
                trg.Main_Wait(80)
                # (Line 31) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 32) }
                # (Line 33) else if (v.P_LoopMain[playerID] < 60)
            if EUDElseIf()(v.P_LoopMain[playerID] >= 60, neg=True):
                # (Line 34) {
                # (Line 35) var x = 50;
                x = EUDVariable()
                x << (50)
                # (Line 37) if (playerID >= 3) x = -x;
                if EUDIf()(playerID >= 3):
                    x << (-x)
                    # (Line 39) trg.Shape_Dot(playerID, 8, "40 + 1n Zealot", 0, 0);
                EUDEndIf()
                trg.Shape_Dot(playerID, 8, "40 + 1n Zealot", 0, 0)
                # (Line 40) KillUnitAt(All, "40 + 1n Zealot", "Anywhere", playerID);
                # (Line 42) addloc("25.Milim_Bozo", x * 3, 0);
                DoActions(KillUnitAt(All, "40 + 1n Zealot", "Anywhere", playerID))
                f_addloc("25.Milim_Bozo", x * 3, 0)
                # (Line 43) MoveUnit(All, "Flame Blue", playerID, "Anywhere", "25.Milim_Bozo");
                # (Line 45) CreateUnit(3, "40 + 1n Wraith", "[Skill]Unit_Wait_8", playerID);
                DoActions(MoveUnit(All, "Flame Blue", playerID, "Anywhere", "25.Milim_Bozo"))
                # (Line 46) SetInvincibility(Enable, "Any unit", playerID, "[Skill]Unit_Wait_ALL");
                DoActions(CreateUnit(3, "40 + 1n Wraith", "[Skill]Unit_Wait_8", playerID))
                # (Line 48) MoveLocation(v.P_LocationID[playerID], "Flame Blue", playerID, "Anywhere");
                DoActions(SetInvincibility(Enable, "Any unit", playerID, "[Skill]Unit_Wait_ALL"))
                # (Line 49) MoveUnit(1, "40 + 1n Wraith", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
                DoActions(MoveLocation(v.P_LocationID[playerID], "Flame Blue", playerID, "Anywhere"))
                # (Line 50) addloc(v.P_LocationID[playerID], -x, 0);
                DoActions(MoveUnit(1, "40 + 1n Wraith", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]))
                f_addloc(v.P_LocationID[playerID], -x, 0)
                # (Line 51) MoveUnit(1, "40 + 1n Wraith", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
                # (Line 52) addloc(v.P_LocationID[playerID], -x, 0);
                DoActions(MoveUnit(1, "40 + 1n Wraith", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]))
                f_addloc(v.P_LocationID[playerID], -x, 0)
                # (Line 53) MoveUnit(1, "40 + 1n Wraith", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
                # (Line 54) KillUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);
                DoActions(MoveUnit(1, "40 + 1n Wraith", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]))
                # (Line 56) if ((playerID >= 3 && (Bring(playerID, AtLeast, 1, "Flame Blue", "[Potal]Shop7") || Bring(playerID, AtLeast, 1, "Flame Blue", "[Potal]Potal7")))
                DoActions(KillUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID))
                _t7 = EUDIf()
                # (Line 57) || (playerID < 3 && (Bring(playerID, AtLeast, 1, "Flame Blue", "[Potal]Shop8") || Bring(playerID, AtLeast, 1, "Flame Blue", "[Potal]Potal8"))))
                if _t7(EUDSCOr()((EUDSCAnd()(playerID >= 3)((EUDSCOr()(Bring(playerID, AtLeast, 1, "Flame Blue", "[Potal]Shop7"))(Bring(playerID, AtLeast, 1, "Flame Blue", "[Potal]Potal7"))()))()))((EUDSCAnd()(playerID >= 3, neg=True)((EUDSCOr()(Bring(playerID, AtLeast, 1, "Flame Blue", "[Potal]Shop8"))(Bring(playerID, AtLeast, 1, "Flame Blue", "[Potal]Potal8"))()))()))()):
                    # (Line 58) {
                    # (Line 59) SetDeaths(playerID, SetTo, 120, " `UniqueCoolTime");
                    # (Line 61) trg.Main_Wait(80);
                    DoActions(SetDeaths(playerID, SetTo, 120, " `UniqueCoolTime"))
                    trg.Main_Wait(80)
                    # (Line 63) v.P_CountMain[playerID] = 2;
                    _ARRW(v.P_CountMain, playerID) << (2)
                    # (Line 64) v.P_LoopMain[playerID] = 0;
                    _ARRW(v.P_LoopMain, playerID) << (0)
                    # (Line 65) }
                    # (Line 66) else if (playerID < 3)
                if EUDElseIf()(playerID >= 3, neg=True):
                    # (Line 67) {
                    # (Line 68) if (Bring(P8, AtLeast, 1, "Buildings", "25.Milim_Bozo"))
                    if EUDIf()(Bring(P8, AtLeast, 1, "Buildings", "25.Milim_Bozo")):
                        # (Line 69) {
                        # (Line 70) SetSwitch("Unique - MilimWarning", Set);
                        # (Line 71) SetSwitch("Recall - Milim", Set);
                        DoActions(SetSwitch("Unique - MilimWarning", Set))
                        # (Line 73) s.CharacterVoice(3);
                        DoActions(SetSwitch("Recall - Milim", Set))
                        s.CharacterVoice(3)
                        # (Line 75) trg.Main_Wait(80);
                        trg.Main_Wait(80)
                        # (Line 77) v.P_CountMain[playerID] += 1;
                        _ARRW(v.P_CountMain, playerID).__iadd__(1)
                        # (Line 78) v.P_LoopMain[playerID] = 0;
                        _ARRW(v.P_LoopMain, playerID) << (0)
                        # (Line 79) }
                        # (Line 80) else
                        # (Line 81) {
                    if EUDElse()():
                        # (Line 82) trg.Main_Wait(80);
                        trg.Main_Wait(80)
                        # (Line 84) v.P_LoopMain[playerID] += 1;
                        _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                        # (Line 85) }
                        # (Line 86) }
                    EUDEndIf()
                    # (Line 87) else if (playerID >= 3)
                if EUDElseIf()(playerID >= 3):
                    # (Line 88) {
                    # (Line 89) if (Bring(P7, AtLeast, 1, "Buildings", "25.Milim_Bozo"))
                    if EUDIf()(Bring(P7, AtLeast, 1, "Buildings", "25.Milim_Bozo")):
                        # (Line 90) {
                        # (Line 91) SetSwitch("Unique - MilimWarning", Set);
                        # (Line 92) SetSwitch("Recall - Milim", Set);
                        DoActions(SetSwitch("Unique - MilimWarning", Set))
                        # (Line 94) s.CharacterVoice(3);
                        DoActions(SetSwitch("Recall - Milim", Set))
                        s.CharacterVoice(3)
                        # (Line 96) trg.Main_Wait(80);
                        trg.Main_Wait(80)
                        # (Line 98) v.P_CountMain[playerID] += 1;
                        _ARRW(v.P_CountMain, playerID).__iadd__(1)
                        # (Line 99) v.P_LoopMain[playerID] = 0;
                        _ARRW(v.P_LoopMain, playerID) << (0)
                        # (Line 100) }
                        # (Line 101) else
                        # (Line 102) {
                    if EUDElse()():
                        # (Line 103) trg.Main_Wait(80);
                        trg.Main_Wait(80)
                        # (Line 105) v.P_LoopMain[playerID] += 1;
                        _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                        # (Line 106) }
                        # (Line 107) }
                    EUDEndIf()
                    # (Line 108) }
                EUDEndIf()
                # (Line 109) else if (v.P_LoopMain[playerID] == 60)
            if EUDElseIf()(v.P_LoopMain[playerID] == 60):
                # (Line 110) {
                # (Line 111) SetDeaths(playerID, SetTo, 120, " `UniqueCoolTime");
                # (Line 113) trg.Main_Wait(80);
                DoActions(SetDeaths(playerID, SetTo, 120, " `UniqueCoolTime"))
                trg.Main_Wait(80)
                # (Line 115) v.P_CountMain[playerID] = 2;
                _ARRW(v.P_CountMain, playerID) << (2)
                # (Line 116) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 117) }
                # (Line 118) }
            EUDEndIf()
            # (Line 119) else if (v.P_CountMain[playerID] == 1)
        if EUDElseIf()(v.P_CountMain[playerID] == 1):
            # (Line 120) {
            # (Line 121) if (v.P_LoopMain[playerID] < 40)
            if EUDIf()(v.P_LoopMain[playerID] >= 40, neg=True):
                # (Line 122) {
                # (Line 123) trg.Shape_Edge(playerID, 1, "50 + 1n Tank", 0, 7, 120);
                trg.Shape_Edge(playerID, 1, "50 + 1n Tank", 0, 7, 120)
                # (Line 124) if (v.P_LoopMain[playerID] % 2 == 0)
                if EUDIf()(v.P_LoopMain[playerID] % 2 == 0):
                    # (Line 125) {
                    # (Line 126) trg.Shape_Edge(playerID, 1, "Protoss Dark Archon", 0, 3, 40);
                    trg.Shape_Edge(playerID, 1, "Protoss Dark Archon", 0, 3, 40)
                    # (Line 127) }
                    # (Line 128) else if (v.P_LoopMain[playerID] % 2 == 1)
                if EUDElseIf()(v.P_LoopMain[playerID] % 2 == 1):
                    # (Line 129) {
                    # (Line 130) trg.Shape_Edge(playerID, 1, "Protoss Dark Archon", 0, 5, 80);
                    trg.Shape_Edge(playerID, 1, "Protoss Dark Archon", 0, 5, 80)
                    # (Line 131) }
                    # (Line 132) KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID);
                EUDEndIf()
                # (Line 133) KillUnitAt(All, "50 + 1n Tank", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID))
                # (Line 134) KillUnitAt(All, "60 + 1n High Templar", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "50 + 1n Tank", "Anywhere", playerID))
                # (Line 135) KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "60 + 1n High Templar", "Anywhere", playerID))
                # (Line 137) trg.Main_Wait(80);
                DoActions(KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", playerID))
                trg.Main_Wait(80)
                # (Line 139) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 140) }
                # (Line 141) else if (v.P_LoopMain[playerID] == 40)
            if EUDElseIf()(v.P_LoopMain[playerID] == 40):
                # (Line 142) {
                # (Line 143) MoveLocation("25.Milim_Bozo", "Flame Blue", playerID, "Anywhere");
                # (Line 145) if (Deaths(CurrentPlayer, Exactly, 0, (210)))
                DoActions(MoveLocation("25.Milim_Bozo", "Flame Blue", playerID, "Anywhere"))
                if EUDIf()(Deaths(CurrentPlayer, Exactly, 0, (210))):
                    # (Line 146) {
                    # (Line 147) MoveUnit(All, v.P_UnitID[playerID], playerID, "Anywhere", "25.Milim_Bozo");
                    # (Line 148) CenterView("25.Milim_Bozo");
                    DoActions(MoveUnit(All, v.P_UnitID[playerID], playerID, "Anywhere", "25.Milim_Bozo"))
                    # (Line 149) }
                    DoActions(CenterView("25.Milim_Bozo"))
                    # (Line 151) trg.Shape_NxNSquare(playerID, 1, "130 + 1n Norad", 3, 75);
                EUDEndIf()
                trg.Shape_NxNSquare(playerID, 1, "130 + 1n Norad", 3, 75)
                # (Line 152) trg.Shape_Dot(playerID, 16, "80 + 1n Goliath", 0, 0);
                trg.Shape_Dot(playerID, 16, "80 + 1n Goliath", 0, 0)
                # (Line 153) Order("130 + 1n Norad", playerID, "Anywhere", Attack, "Anywhere");
                # (Line 154) MoveUnit(All, "80 + 1n Goliath", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
                DoActions(Order("130 + 1n Norad", playerID, "Anywhere", Attack, "Anywhere"))
                # (Line 155) Order("80 + 1n Goliath", playerID, "Anywhere", Attack, "Anywhere");
                DoActions(MoveUnit(All, "80 + 1n Goliath", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]))
                # (Line 156) SetSwitch("Recall - Milim", Clear);
                DoActions(Order("80 + 1n Goliath", playerID, "Anywhere", Attack, "Anywhere"))
                # (Line 158) trg.Main_Wait(80);
                DoActions(SetSwitch("Recall - Milim", Clear))
                trg.Main_Wait(80)
                # (Line 160) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 161) }
                # (Line 162) else if (v.P_LoopMain[playerID] < 45)
            if EUDElseIf()(v.P_LoopMain[playerID] >= 45, neg=True):
                # (Line 163) {
                # (Line 164) var i = v.P_LoopMain[playerID] - 41;
                i = EUDVariable()
                i << (v.P_LoopMain[playerID] - 41)
                # (Line 166) trg.Shape_Edge(playerID, 1, "60 + 1n Siege", 0, 5 + 2 * i, 100 + 50 * i);
                trg.Shape_Edge(playerID, 1, "60 + 1n Siege", 0, 5 + 2 * i, 100 + 50 * i)
                # (Line 167) trg.Shape_Edge(playerID, 1, "50 + 1n Battlecruiser", 0, 3 + 2 * i, 50 + 50 * i);
                trg.Shape_Edge(playerID, 1, "50 + 1n Battlecruiser", 0, 3 + 2 * i, 50 + 50 * i)
                # (Line 168) KillUnitAt(All, "60 + 1n Siege", "Anywhere", playerID);
                # (Line 169) KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "60 + 1n Siege", "Anywhere", playerID))
                # (Line 171) trg.Main_Wait(80);
                DoActions(KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID))
                trg.Main_Wait(80)
                # (Line 173) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 174) }
                # (Line 175) else if (v.P_LoopMain[playerID] == 45)
            if EUDElseIf()(v.P_LoopMain[playerID] == 45):
                # (Line 176) {
                # (Line 177) KillUnitAt(All, "130 + 1n Norad", "Anywhere", playerID);
                # (Line 178) KillUnitAt(All, "80 + 1n Goliath", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "130 + 1n Norad", "Anywhere", playerID))
                # (Line 180) trg.Shape_Edge(playerID, 1, " Unit. Hoffnung 25000", 0, 3, 50);
                DoActions(KillUnitAt(All, "80 + 1n Goliath", "Anywhere", playerID))
                trg.Shape_Edge(playerID, 1, " Unit. Hoffnung 25000", 0, 3, 50)
                # (Line 181) trg.Shape_Edge(playerID, 1, " Unit. Hoffnung 25000", 0, 5, 100);
                trg.Shape_Edge(playerID, 1, " Unit. Hoffnung 25000", 0, 5, 100)
                # (Line 182) trg.Shape_Edge(playerID, 1, " Unit. Hoffnung 25000", 0, 7, 150);
                trg.Shape_Edge(playerID, 1, " Unit. Hoffnung 25000", 0, 7, 150)
                # (Line 183) trg.Shape_Edge(playerID, 1, " Unit. Hoffnung 25000", 0, 9, 150);
                trg.Shape_Edge(playerID, 1, " Unit. Hoffnung 25000", 0, 9, 150)
                # (Line 184) KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", playerID);
                # (Line 186) trg.Main_Wait(80);
                DoActions(KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", playerID))
                trg.Main_Wait(80)
                # (Line 188) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 189) }
                # (Line 190) else if (v.P_LoopMain[playerID] == 46)
            if EUDElseIf()(v.P_LoopMain[playerID] == 46):
                # (Line 191) {
                # (Line 192) s.CharacterVoice(4);
                s.CharacterVoice(4)
                # (Line 193) SetSwitch("Unique - Milim", Set);
                # (Line 194) SetDeaths(playerID, SetTo, 1440, " `UniqueCoolTime");
                DoActions(SetSwitch("Unique - Milim", Set))
                # (Line 195) SetDeaths(playerID, SetTo, 300, " `UniqueSkill");
                DoActions(SetDeaths(playerID, SetTo, 1440, " `UniqueCoolTime"))
                # (Line 197) trg.Main_Wait(80);
                DoActions(SetDeaths(playerID, SetTo, 300, " `UniqueSkill"))
                trg.Main_Wait(80)
                # (Line 199) v.P_CountMain[playerID] += 1;
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 200) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 201) }
                # (Line 202) }
            EUDEndIf()
            # (Line 203) else if (v.P_CountMain[playerID] == 2)
        if EUDElseIf()(v.P_CountMain[playerID] == 2):
            # (Line 204) {
            # (Line 205) RemoveUnitAt(All, "Flame Blue", "Anywhere", playerID);
            # (Line 206) SetSwitch("Unique - MilimWarning", Clear);
            DoActions(RemoveUnitAt(All, "Flame Blue", "Anywhere", playerID))
            # (Line 207) trg.SkillEnd();
            DoActions(SetSwitch("Unique - MilimWarning", Clear))
            trg.SkillEnd()
            # (Line 208) }
            # (Line 210) }
        EUDEndIf()
        # (Line 211) }
    EUDEndIf()
