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
# (Line 5) import func.trigepic as epic;
from func import trigepic as epic
# (Line 6) import func.sound as s;
from func import sound as s
# (Line 8) function main(playerID)
# (Line 9) {
@EUDFunc
def f_main(playerID):
    # (Line 10) trg.Debuff_BanReturn();
    trg.Debuff_BanReturn()
    # (Line 11) trg.Debuff_Stop();
    trg.Debuff_Stop()
    # (Line 13) MoveUnit(All, "40 + 1n Drone", playerID, "Anywhere", "[Skill]HoldPosition");
    # (Line 15) if (v.P_WaitMain[playerID] == 0)
    DoActions(MoveUnit(All, "40 + 1n Drone", playerID, "Anywhere", "[Skill]HoldPosition"))
    if EUDIf()(v.P_WaitMain[playerID] == 0):
        # (Line 16) {
        # (Line 17) if (v.P_CountMain[playerID] == 0)
        if EUDIf()(v.P_CountMain[playerID] == 0):
            # (Line 18) {
            # (Line 19) RemoveUnitAt(All, "40 + 1n Mutalisk", "Anywhere", playerID);
            # (Line 21) if (v.P_LoopMain[playerID] < 3)
            DoActions(RemoveUnitAt(All, "40 + 1n Mutalisk", "Anywhere", playerID))
            if EUDIf()(v.P_LoopMain[playerID] >= 3, neg=True):
                # (Line 22) {
                # (Line 23) var d = 0;
                d = EUDVariable()
                d << (0)
                # (Line 24) var n = 8;
                n = EUDVariable()
                n << (8)
                # (Line 25) var r = 50 + 50 * v.P_LoopMain[playerID];
                r = EUDVariable()
                r << (50 + 50 * v.P_LoopMain[playerID])
                # (Line 26) trg.Shape_Circle(playerID, 1, "Protoss Dark Archon", d, n, r);
                trg.Shape_Circle(playerID, 1, "Protoss Dark Archon", d, n, r)
                # (Line 27) trg.Shape_Circle(playerID, 1, "40 + 1n Mutalisk", d, n, r);
                trg.Shape_Circle(playerID, 1, "40 + 1n Mutalisk", d, n, r)
                # (Line 28) epic.Shape_Circle(playerID, 1, "40 + 1n Lurker", d, n, r, 2);
                epic.Shape_Circle(playerID, 1, "40 + 1n Lurker", d, n, r, 2)
                # (Line 30) MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
                # (Line 31) MoveUnit(All, "40 + 1n Lurker", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
                DoActions(MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere"))
                # (Line 32) Order("40 + 1n Mutalisk", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                DoActions(MoveUnit(All, "40 + 1n Lurker", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]))
                # (Line 34) KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID);
                DoActions(Order("40 + 1n Mutalisk", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                # (Line 35) }
                DoActions(KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID))
                # (Line 36) else if (v.P_LoopMain[playerID] == 3)
            if EUDElseIf()(v.P_LoopMain[playerID] == 3):
                # (Line 37) {
                # (Line 38) var d = 0;
                d = EUDVariable()
                d << (0)
                # (Line 39) var n = 8;
                n = EUDVariable()
                n << (8)
                # (Line 40) var r = 50 + 50 * v.P_LoopMain[playerID];
                r = EUDVariable()
                r << (50 + 50 * v.P_LoopMain[playerID])
                # (Line 41) trg.Shape_Circle(playerID, 1, "Protoss Dark Archon", d, n, r);
                trg.Shape_Circle(playerID, 1, "Protoss Dark Archon", d, n, r)
                # (Line 42) trg.Shape_Circle(playerID, 1, "40 + 1n Mutalisk", d, n, r);
                trg.Shape_Circle(playerID, 1, "40 + 1n Mutalisk", d, n, r)
                # (Line 43) epic.Shape_Circle(playerID, 1, "40 + 1n Lurker", d, n, r, 0);
                epic.Shape_Circle(playerID, 1, "40 + 1n Lurker", d, n, r, 0)
                # (Line 45) CreateUnitWithProperties(1, "40 + 1n Lurker", "[Skill]Hallu_Bozo", playerID, UnitProperty(burrowed = true));
                # (Line 47) MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
                DoActions(CreateUnitWithProperties(1, "40 + 1n Lurker", "[Skill]Hallu_Bozo", playerID, UnitProperty(burrowed=True)))
                # (Line 48) MoveUnit(All, "40 + 1n Lurker", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
                DoActions(MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere"))
                # (Line 49) Order("40 + 1n Mutalisk", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                DoActions(MoveUnit(All, "40 + 1n Lurker", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]))
                # (Line 51) KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID);
                DoActions(Order("40 + 1n Mutalisk", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                # (Line 52) }
                DoActions(KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID))
                # (Line 54) if (v.P_LoopMain[playerID] > 3)
            EUDEndIf()
            if EUDIf()(v.P_LoopMain[playerID] <= 3, neg=True):
                # (Line 55) {
                # (Line 56) if (v.P_LoopMain[playerID] % 4 == 0)
                if EUDIf()(v.P_LoopMain[playerID] % 4 == 0):
                    # (Line 57) {
                    # (Line 58) var d = 0;
                    d = EUDVariable()
                    d << (0)
                    # (Line 59) var n = 8;
                    n = EUDVariable()
                    n << (8)
                    # (Line 60) var r = 200;
                    r = EUDVariable()
                    r << (200)
                    # (Line 61) trg.Shape_Circle(playerID, 1, "40 + 1n Guardian", d, n, r);
                    trg.Shape_Circle(playerID, 1, "40 + 1n Guardian", d, n, r)
                    # (Line 63) MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
                    # (Line 64) Order("40 + 1n Guardian", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                    DoActions(MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere"))
                    # (Line 65) }
                    DoActions(Order("40 + 1n Guardian", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                    # (Line 66) else if (v.P_LoopMain[playerID] % 4 == 1)
                if EUDElseIf()(v.P_LoopMain[playerID] % 4 == 1):
                    # (Line 67) {
                    # (Line 68) for (var i = 0; i < 8; i++)
                    i = EUDVariable()
                    i << (0)
                    if EUDWhile()(i >= 8, neg=True):
                        def _t9():
                            i.__iadd__(1)
                        # (Line 69) {
                        # (Line 70) adv.Shape_SquareAt(playerID, "40 + 1n Guardian", 1, "80 + 1n Guardian", 40, 0);
                        adv.Shape_SquareAt(playerID, "40 + 1n Guardian", 1, "80 + 1n Guardian", 40, 0)
                        # (Line 71) adv.Shape_SquareAt(playerID, "40 + 1n Guardian", 1, "80 + 1n Guardian", 32, 32);
                        adv.Shape_SquareAt(playerID, "40 + 1n Guardian", 1, "80 + 1n Guardian", 32, 32)
                        # (Line 73) RemoveUnitAt(1, "40 + 1n Guardian", "Anywhere", playerID);
                        # (Line 74) }
                        DoActions(RemoveUnitAt(1, "40 + 1n Guardian", "Anywhere", playerID))
                        # (Line 76) KillUnitAt(All, "80 + 1n Guardian", "Anywhere", playerID);
                        EUDSetContinuePoint()
                        _t9()
                    EUDEndWhile()
                    # (Line 77) }
                    DoActions(KillUnitAt(All, "80 + 1n Guardian", "Anywhere", playerID))
                    # (Line 78) }
                EUDEndIf()
                # (Line 80) trg.Main_Wait(80);
            EUDEndIf()
            trg.Main_Wait(80)
            # (Line 82) v.P_LoopMain[playerID] += 1;
            _ARRW(v.P_LoopMain, playerID).__iadd__(1)
            # (Line 84) if (v.P_LoopMain[playerID] == 48)
            if EUDIf()(v.P_LoopMain[playerID] == 48):
                # (Line 85) {
                # (Line 86) s.CharacterVoice(6);
                s.CharacterVoice(6)
                # (Line 88) v.P_CountMain[playerID] += 1;
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 89) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 90) }
                # (Line 91) }
            EUDEndIf()
            # (Line 92) else if (v.P_CountMain[playerID] == 1)
        if EUDElseIf()(v.P_CountMain[playerID] == 1):
            # (Line 93) {
            # (Line 94) if (v.P_LoopMain[playerID] % 4 == 0)
            if EUDIf()(v.P_LoopMain[playerID] % 4 == 0):
                # (Line 95) {
                # (Line 96) var d = 0;
                d = EUDVariable()
                d << (0)
                # (Line 97) var n = 8;
                n = EUDVariable()
                n << (8)
                # (Line 98) var r = 200;
                r = EUDVariable()
                r << (200)
                # (Line 99) trg.Shape_Circle(playerID, 1, "40 + 1n Guardian", d, n, r);
                trg.Shape_Circle(playerID, 1, "40 + 1n Guardian", d, n, r)
                # (Line 101) MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
                # (Line 102) Order("40 + 1n Guardian", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                DoActions(MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere"))
                # (Line 103) }
                DoActions(Order("40 + 1n Guardian", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                # (Line 104) else if (v.P_LoopMain[playerID] % 4 == 1)
            if EUDElseIf()(v.P_LoopMain[playerID] % 4 == 1):
                # (Line 105) {
                # (Line 106) for (var i = 0; i < 8; i++)
                i = EUDVariable()
                i << (0)
                if EUDWhile()(i >= 8, neg=True):
                    def _t15():
                        i.__iadd__(1)
                    # (Line 107) {
                    # (Line 108) adv.Shape_SquareAt(playerID, "40 + 1n Guardian", 1, "80 + 1n Guardian", 40, 0);
                    adv.Shape_SquareAt(playerID, "40 + 1n Guardian", 1, "80 + 1n Guardian", 40, 0)
                    # (Line 109) adv.Shape_SquareAt(playerID, "40 + 1n Guardian", 1, "80 + 1n Guardian", 32, 32);
                    adv.Shape_SquareAt(playerID, "40 + 1n Guardian", 1, "80 + 1n Guardian", 32, 32)
                    # (Line 111) RemoveUnitAt(1, "40 + 1n Guardian", "Anywhere", playerID);
                    # (Line 112) }
                    DoActions(RemoveUnitAt(1, "40 + 1n Guardian", "Anywhere", playerID))
                    # (Line 114) KillUnitAt(All, "80 + 1n Guardian", "Anywhere", playerID);
                    EUDSetContinuePoint()
                    _t15()
                EUDEndWhile()
                # (Line 115) }
                DoActions(KillUnitAt(All, "80 + 1n Guardian", "Anywhere", playerID))
                # (Line 117) if (Bring(playerID, AtLeast, 1, "40 + 1n Lurker", "Anywhere"))
            EUDEndIf()
            if EUDIf()(Bring(playerID, AtLeast, 1, "40 + 1n Lurker", "Anywhere")):
                # (Line 118) {
                # (Line 119) for (var i = 0; i < 2; i++)
                i = EUDVariable()
                i << (0)
                if EUDWhile()(i >= 2, neg=True):
                    def _t18():
                        i.__iadd__(1)
                    # (Line 120) {
                    # (Line 121) adv.Shape_SquareAt(playerID, "40 + 1n Lurker", 1, "80 + 1n Guardian", 16, 16);
                    adv.Shape_SquareAt(playerID, "40 + 1n Lurker", 1, "80 + 1n Guardian", 16, 16)
                    # (Line 122) adv.Shape_SquareAt(playerID, "40 + 1n Lurker", 1, "Protoss Dark Archon", 16, 16);
                    adv.Shape_SquareAt(playerID, "40 + 1n Lurker", 1, "Protoss Dark Archon", 16, 16)
                    # (Line 124) trg.MoveLoc("40 + 1n Lurker", playerID, 0, 0);
                    trg.MoveLoc("40 + 1n Lurker", playerID, 0, 0)
                    # (Line 125) RemoveUnitAt(1, "40 + 1n Lurker", "Anywhere", playerID);
                    # (Line 126) trg.SkillUnit(playerID, 1, "40 + 1n Drone");
                    DoActions(RemoveUnitAt(1, "40 + 1n Lurker", "Anywhere", playerID))
                    trg.SkillUnit(playerID, 1, "40 + 1n Drone")
                    # (Line 127) }
                    # (Line 129) MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
                    EUDSetContinuePoint()
                    _t18()
                EUDEndWhile()
                # (Line 130) Order("40 + 1n Guardian", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                DoActions(MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere"))
                # (Line 132) KillUnitAt(All, "80 + 1n Guardian", "Anywhere", playerID);
                DoActions(Order("40 + 1n Guardian", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                # (Line 133) KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "80 + 1n Guardian", "Anywhere", playerID))
                # (Line 134) }
                DoActions(KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID))
                # (Line 136) trg.Main_Wait(80);
            EUDEndIf()
            trg.Main_Wait(80)
            # (Line 138) v.P_LoopMain[playerID] += 1;
            _ARRW(v.P_LoopMain, playerID).__iadd__(1)
            # (Line 140) if (v.P_LoopMain[playerID] == 36)
            if EUDIf()(v.P_LoopMain[playerID] == 36):
                # (Line 141) {
                # (Line 142) v.P_CountMain[playerID] += 1;
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 143) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 144) }
                # (Line 145) }
            EUDEndIf()
            # (Line 146) else if (v.P_CountMain[playerID] == 2)
        if EUDElseIf()(v.P_CountMain[playerID] == 2):
            # (Line 147) {
            # (Line 148) KillUnitAt(All, "40 + 1n Drone", "Anywhere", playerID);
            # (Line 149) KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID);
            DoActions(KillUnitAt(All, "40 + 1n Drone", "Anywhere", playerID))
            # (Line 151) trg.SkillEnd();
            DoActions(KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID))
            trg.SkillEnd()
            # (Line 152) }
            # (Line 153) }
        EUDEndIf()
        # (Line 154) }
    EUDEndIf()