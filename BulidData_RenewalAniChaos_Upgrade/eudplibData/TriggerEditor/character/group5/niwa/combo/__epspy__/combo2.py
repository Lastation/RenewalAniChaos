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
# (Line 4) import func.trigepic as epic;
from func import trigepic as epic
# (Line 5) import func.sound as s;
from func import sound as s
# (Line 7) var x = 0;
x = EUDCreateVariables(1)
_IGVA([x], lambda: [0])
# (Line 8) var y = 0;
y = EUDCreateVariables(1)
_IGVA([y], lambda: [0])
# (Line 10) function main(playerID)
# (Line 11) {
@EUDFunc
def f_main(playerID):
    # (Line 12) MoveUnit(All, "40 + 3n Zeratul", playerID, "Anywhere", "[Skill]HoldPosition");
    # (Line 14) trg.Debuff_BanReturn();
    DoActions(MoveUnit(All, "40 + 3n Zeratul", playerID, "Anywhere", "[Skill]HoldPosition"))
    trg.Debuff_BanReturn()
    # (Line 15) trg.Debuff_Stop();
    trg.Debuff_Stop()
    # (Line 17) if (v.P_WaitMain[playerID] == 0)
    if EUDIf()(v.P_WaitMain[playerID] == 0):
        # (Line 18) {
        # (Line 19) if (v.P_CountMain[playerID] == 0)
        if EUDIf()(v.P_CountMain[playerID] == 0):
            # (Line 20) {
            # (Line 21) if (v.P_LoopMain[playerID] == 0)
            if EUDIf()(v.P_LoopMain[playerID] == 0):
                # (Line 22) {
                # (Line 23) trg.Shape_Edge(playerID, 1, "Unclean One (Defiler)", 45, 3, 32);
                trg.Shape_Edge(playerID, 1, "Unclean One (Defiler)", 45, 3, 32)
                # (Line 25) trg.Shape_NxNSquare(playerID, 1, "40 + 1n Guardian", 3, 50);
                trg.Shape_NxNSquare(playerID, 1, "40 + 1n Guardian", 3, 50)
                # (Line 26) trg.Shape_NxNSquare(playerID, 1, "Protoss Dark Archon", 3, 50);
                trg.Shape_NxNSquare(playerID, 1, "Protoss Dark Archon", 3, 50)
                # (Line 28) KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID);
                # (Line 29) KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID))
                # (Line 30) }
                DoActions(KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID))
                # (Line 31) if (v.P_LoopMain[playerID] == 1)
            EUDEndIf()
            if EUDIf()(v.P_LoopMain[playerID] == 1):
                # (Line 32) {
                # (Line 33) trg.Shape_NxNSquare(playerID, 1, "Kakaru (Twilight)", 3, 50);
                trg.Shape_NxNSquare(playerID, 1, "Kakaru (Twilight)", 3, 50)
                # (Line 34) KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", playerID);
                # (Line 35) }
                DoActions(KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", playerID))
                # (Line 51) trg.Main_Wait(80);
            EUDEndIf()
            trg.Main_Wait(80)
            # (Line 53) v.P_LoopMain[playerID] += 1;
            _ARRW(v.P_LoopMain, playerID).__iadd__(1)
            # (Line 55) if (v.P_LoopMain[playerID] == 8)
            if EUDIf()(v.P_LoopMain[playerID] == 8):
                # (Line 56) {
                # (Line 57) v.P_CountMain[playerID] += 1;
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 58) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 59) }
                # (Line 60) }
            EUDEndIf()
            # (Line 61) else if (v.P_CountMain[playerID] == 1)
        if EUDElseIf()(v.P_CountMain[playerID] == 1):
            # (Line 62) {
            # (Line 63) if (v.P_LoopMain[playerID] == 0)
            if EUDIf()(v.P_LoopMain[playerID] == 0):
                # (Line 64) {
                # (Line 65) trg.Shape_Square(playerID, 1, "60 + 1n Hydralisk", 100, 100);
                trg.Shape_Square(playerID, 1, "60 + 1n Hydralisk", 100, 100)
                # (Line 67) trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 100, 100);
                trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 100, 100)
                # (Line 68) epic.Shape_Square(playerID, 1, "60 + 1n Archon", 100, 100, 1);
                epic.Shape_Square(playerID, 1, "60 + 1n Archon", 100, 100, 1)
                # (Line 70) trg.Shape_Square(playerID, 1, "50 + 1n Battlecruiser", 100, 0);
                trg.Shape_Square(playerID, 1, "50 + 1n Battlecruiser", 100, 0)
                # (Line 72) KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID);
                # (Line 73) KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID))
                # (Line 74) KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID))
                # (Line 76) MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
                DoActions(KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID))
                # (Line 77) MoveUnit(All, "60 + 1n Hydralisk", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
                DoActions(MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere"))
                # (Line 78) Order("60 + 1n Hydralisk", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                DoActions(MoveUnit(All, "60 + 1n Hydralisk", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]))
                # (Line 79) }
                DoActions(Order("60 + 1n Hydralisk", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                # (Line 80) if (v.P_LoopMain[playerID] == 4)
            EUDEndIf()
            if EUDIf()(v.P_LoopMain[playerID] == 4):
                # (Line 81) {
                # (Line 82) trg.Shape_Square(playerID, 1, "60 + 1n Hydralisk", 100, 0);
                trg.Shape_Square(playerID, 1, "60 + 1n Hydralisk", 100, 0)
                # (Line 83) trg.Shape_Square(playerID, 1, "40 + 1n Mutalisk", 100, 0);
                trg.Shape_Square(playerID, 1, "40 + 1n Mutalisk", 100, 0)
                # (Line 85) trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 100, 0);
                trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 100, 0)
                # (Line 86) epic.Shape_Square(playerID, 1, "60 + 1n Archon", 100, 0, 1);
                epic.Shape_Square(playerID, 1, "60 + 1n Archon", 100, 0, 1)
                # (Line 88) trg.Shape_Square(playerID, 1, "50 + 1n Battlecruiser", 100, 100);
                trg.Shape_Square(playerID, 1, "50 + 1n Battlecruiser", 100, 100)
                # (Line 90) KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID);
                # (Line 91) KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID))
                # (Line 92) KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID))
                # (Line 94) MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
                DoActions(KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID))
                # (Line 95) MoveUnit(All, "60 + 1n Hydralisk", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
                DoActions(MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere"))
                # (Line 96) Order("60 + 1n Hydralisk", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                DoActions(MoveUnit(All, "60 + 1n Hydralisk", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]))
                # (Line 97) Order("40 + 1n Mutalisk", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                DoActions(Order("60 + 1n Hydralisk", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                # (Line 98) }
                DoActions(Order("40 + 1n Mutalisk", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                # (Line 100) trg.Main_Wait(80);
            EUDEndIf()
            trg.Main_Wait(80)
            # (Line 102) v.P_LoopMain[playerID] += 1;
            _ARRW(v.P_LoopMain, playerID).__iadd__(1)
            # (Line 104) if (v.P_LoopMain[playerID] == 19)
            if EUDIf()(v.P_LoopMain[playerID] == 19):
                # (Line 105) {
                # (Line 106) KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", playerID);
                # (Line 108) v.P_CountMain[playerID] += 1;
                DoActions(KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", playerID))
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 109) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 110) }
                # (Line 111) }
            EUDEndIf()
            # (Line 112) else if (v.P_CountMain[playerID] == 2)
        if EUDElseIf()(v.P_CountMain[playerID] == 2):
            # (Line 113) {
            # (Line 114) if (v.P_LoopMain[playerID] == 0)
            if EUDIf()(v.P_LoopMain[playerID] == 0):
                # (Line 115) {
                # (Line 116) trg.Shape_NxNSquare(playerID, 1, "40 + 1n Guardian", 9, 50);
                trg.Shape_NxNSquare(playerID, 1, "40 + 1n Guardian", 9, 50)
                # (Line 117) trg.Shape_Edge(playerID, 1, "Protoss Dark Templar", 45, 3, 150);
                trg.Shape_Edge(playerID, 1, "Protoss Dark Templar", 45, 3, 150)
                # (Line 118) trg.Shape_Edge(playerID, 1, "Protoss Dark Templar", 45, 5, 200);
                trg.Shape_Edge(playerID, 1, "Protoss Dark Templar", 45, 5, 200)
                # (Line 120) MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
                # (Line 121) Order("Protoss Dark Templar", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                DoActions(MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere"))
                # (Line 122) Order("40 + 3n Zeratul", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                DoActions(Order("Protoss Dark Templar", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                # (Line 124) KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID);
                DoActions(Order("40 + 3n Zeratul", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                # (Line 126) }
                DoActions(KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID))
                # (Line 127) if (v.P_LoopMain[playerID] == 9)
            EUDEndIf()
            if EUDIf()(v.P_LoopMain[playerID] == 9):
                # (Line 128) {
                # (Line 129) s.CharacterVoice(8);
                s.CharacterVoice(8)
                # (Line 130) }
                # (Line 133) trg.Main_Wait(80);
            EUDEndIf()
            trg.Main_Wait(80)
            # (Line 135) v.P_LoopMain[playerID] += 1;
            _ARRW(v.P_LoopMain, playerID).__iadd__(1)
            # (Line 137) if (v.P_LoopMain[playerID] == 32)
            if EUDIf()(v.P_LoopMain[playerID] == 32):
                # (Line 138) {
                # (Line 139) v.P_CountMain[playerID] += 1;
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 140) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 141) }
                # (Line 142) }
            EUDEndIf()
            # (Line 143) else if (v.P_CountMain[playerID] == 3)
        if EUDElseIf()(v.P_CountMain[playerID] == 3):
            # (Line 144) {
            # (Line 145) if (v.P_LoopMain[playerID] == 0)
            if EUDIf()(v.P_LoopMain[playerID] == 0):
                # (Line 146) {
                # (Line 147) trg.Shape_NxNSquare(playerID, 1, "40 + 1n Mutalisk", 3, 50);
                trg.Shape_NxNSquare(playerID, 1, "40 + 1n Mutalisk", 3, 50)
                # (Line 148) trg.Shape_NxNSquare(playerID, 1, "Protoss Dark Archon", 3, 50);
                trg.Shape_NxNSquare(playerID, 1, "Protoss Dark Archon", 3, 50)
                # (Line 149) KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID);
                # (Line 151) MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
                DoActions(KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID))
                # (Line 152) Order("40 + 1n Mutalisk", playerID, "Anywhere", Attack, "Anywhere");
                DoActions(MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere"))
                # (Line 153) }
                DoActions(Order("40 + 1n Mutalisk", playerID, "Anywhere", Attack, "Anywhere"))
                # (Line 154) if (v.P_LoopMain[playerID] == 3)
            EUDEndIf()
            if EUDIf()(v.P_LoopMain[playerID] == 3):
                # (Line 155) {
                # (Line 156) RemoveUnitAt(All, "40 + 1n Mutalisk", "Anywhere", playerID);
                # (Line 158) trg.Shape_NxNSquare(playerID, 1, "40 + 1n Mutalisk", 3, 50);
                DoActions(RemoveUnitAt(All, "40 + 1n Mutalisk", "Anywhere", playerID))
                trg.Shape_NxNSquare(playerID, 1, "40 + 1n Mutalisk", 3, 50)
                # (Line 159) trg.Shape_NxNSquare(playerID, 1, "Protoss Dark Archon", 3, 50);
                trg.Shape_NxNSquare(playerID, 1, "Protoss Dark Archon", 3, 50)
                # (Line 160) KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID);
                # (Line 162) MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
                DoActions(KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID))
                # (Line 163) Order("40 + 1n Mutalisk", playerID, "Anywhere", Attack, "Anywhere");
                DoActions(MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere"))
                # (Line 164) }
                DoActions(Order("40 + 1n Mutalisk", playerID, "Anywhere", Attack, "Anywhere"))
                # (Line 166) trg.Main_Wait(80);
            EUDEndIf()
            trg.Main_Wait(80)
            # (Line 168) v.P_LoopMain[playerID] += 1;
            _ARRW(v.P_LoopMain, playerID).__iadd__(1)
            # (Line 170) if (v.P_LoopMain[playerID] == 7)
            if EUDIf()(v.P_LoopMain[playerID] == 7):
                # (Line 171) {
                # (Line 172) KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", playerID);
                # (Line 174) v.P_CountMain[playerID] += 1;
                DoActions(KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", playerID))
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 175) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 176) }
                # (Line 177) }
            EUDEndIf()
            # (Line 178) else if (v.P_CountMain[playerID] == 4)
        if EUDElseIf()(v.P_CountMain[playerID] == 4):
            # (Line 179) {
            # (Line 180) if (Bring(playerID, AtLeast, 2, "Protoss Arbiter", "[Skill]UseSkill")
            _t19 = EUDIf()
            # (Line 181) )
            if _t19(Bring(playerID, AtLeast, 2, "Protoss Arbiter", "[Skill]UseSkill")):
                # (Line 182) {
                # (Line 183) s.CharacterVoice(9);
                s.CharacterVoice(9)
                # (Line 184) v.P_SkillDelay[playerID] = 0;
                _ARRW(v.P_SkillDelay, playerID) << (0)
                # (Line 185) v.P_CountMain[playerID] = 0;
                _ARRW(v.P_CountMain, playerID) << (0)
                # (Line 186) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 187) v.P_Step[playerID] = 230;
                _ARRW(v.P_Step, playerID) << (230)
                # (Line 188) KillUnitAt(2, "Protoss Arbiter", "[Skill]UseSkill", playerID);
                # (Line 189) }
                DoActions(KillUnitAt(2, "Protoss Arbiter", "[Skill]UseSkill", playerID))
                # (Line 190) else
                # (Line 191) {
            if EUDElse()():
                # (Line 192) KillUnitAt(All, "40 + 3n Zeratul", "Anywhere", playerID);
                # (Line 193) KillUnitAt(All, "Protoss Dark Templar", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "40 + 3n Zeratul", "Anywhere", playerID))
                # (Line 194) KillUnitAt(All, "40 + 1n Lurker", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "Protoss Dark Templar", "Anywhere", playerID))
                # (Line 195) KillUnitAt(All, "60 + 1n Hydralisk", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "40 + 1n Lurker", "Anywhere", playerID))
                # (Line 196) KillUnitAt(All, "Unclean One (Defiler)", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "60 + 1n Hydralisk", "Anywhere", playerID))
                # (Line 198) trg.SkillEnd();
                DoActions(KillUnitAt(All, "Unclean One (Defiler)", "Anywhere", playerID))
                trg.SkillEnd()
                # (Line 199) }
                # (Line 200) }
            EUDEndIf()
            # (Line 201) }
        EUDEndIf()
        # (Line 202) }
    EUDEndIf()