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
    # (Line 8) if (v.P_WaitMain[playerID] == 0)
    if EUDIf()(v.P_WaitMain[playerID] == 0):
        # (Line 9) {
        # (Line 10) if (v.P_CountMain[playerID] == 0)
        if EUDIf()(v.P_CountMain[playerID] == 0):
            # (Line 11) {
            # (Line 12) if (v.P_LoopMain[playerID] <= 5)
            if EUDIf()(v.P_LoopMain[playerID] <= 5):
                # (Line 13) {
                # (Line 14) trg.Shape_Double(playerID, 1, "50 + 1n Battlecruiser", 144 - (48 * v.P_LoopMain[playerID]), 144);
                trg.Shape_Double(playerID, 1, "50 + 1n Battlecruiser", 144 - (48 * v.P_LoopMain[playerID]), 144)
                # (Line 15) trg.Shape_Double(playerID, 1, "Protoss Dark Archon", 144 - (48 * v.P_LoopMain[playerID]), 144);
                trg.Shape_Double(playerID, 1, "Protoss Dark Archon", 144 - (48 * v.P_LoopMain[playerID]), 144)
                # (Line 16) KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID);
                # (Line 17) KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID))
                # (Line 18) trg.Main_Wait(0);
                DoActions(KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID))
                trg.Main_Wait(0)
                # (Line 19) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 20) }
                # (Line 21) else if (v.P_LoopMain[playerID] == 6)
            if EUDElseIf()(v.P_LoopMain[playerID] == 6):
                # (Line 22) {
                # (Line 23) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 24) v.P_CountMain[playerID] += 1;
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 25) }
                # (Line 26) }
            EUDEndIf()
            # (Line 27) else if (v.P_CountMain[playerID] == 1)
        if EUDElseIf()(v.P_CountMain[playerID] == 1):
            # (Line 28) {
            # (Line 29) if (v.P_LoopMain[playerID] <= 5)
            if EUDIf()(v.P_LoopMain[playerID] <= 5):
                # (Line 30) {
                # (Line 31) trg.Shape_Double(playerID, 1, "50 + 1n Battlecruiser", 144, -144 + (48 * v.P_LoopMain[playerID]));
                trg.Shape_Double(playerID, 1, "50 + 1n Battlecruiser", 144, -144 + (48 * v.P_LoopMain[playerID]))
                # (Line 32) trg.Shape_Double(playerID, 1, "Protoss Dark Archon", 144, -144 + (48 * v.P_LoopMain[playerID]));
                trg.Shape_Double(playerID, 1, "Protoss Dark Archon", 144, -144 + (48 * v.P_LoopMain[playerID]))
                # (Line 33) KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID);
                # (Line 34) KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID))
                # (Line 35) trg.Main_Wait(0);
                DoActions(KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID))
                trg.Main_Wait(0)
                # (Line 36) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 37) }
                # (Line 38) else if (v.P_LoopMain[playerID] == 6)
            if EUDElseIf()(v.P_LoopMain[playerID] == 6):
                # (Line 39) {
                # (Line 40) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 41) v.P_CountMain[playerID] += 1;
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 42) }
                # (Line 43) }
            EUDEndIf()
            # (Line 44) else if (v.P_CountMain[playerID] == 2)
        if EUDElseIf()(v.P_CountMain[playerID] == 2):
            # (Line 45) {
            # (Line 46) KillUnitAt(All, 2, "Anywhere", playerID);
            # (Line 47) KillUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID);
            DoActions(KillUnitAt(All, 2, "Anywhere", playerID))
            # (Line 48) KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID);
            DoActions(KillUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID))
            # (Line 50) if (v.P_LoopMain[playerID] == 0)
            DoActions(KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID))
            if EUDIf()(v.P_LoopMain[playerID] == 0):
                # (Line 51) {
                # (Line 52) trg.Shape_Square(playerID, 1, "50 + 1n Battlecruiser", 96, 96);
                trg.Shape_Square(playerID, 1, "50 + 1n Battlecruiser", 96, 96)
                # (Line 53) trg.Shape_Square(playerID, 1, "Protoss Dark Archon", 96, 96);
                trg.Shape_Square(playerID, 1, "Protoss Dark Archon", 96, 96)
                # (Line 54) KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID);
                # (Line 56) trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0);
                DoActions(KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID))
                trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0)
                # (Line 57) Order("50 + 1n Battlecruiser", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                # (Line 58) trg.Main_Wait(150);
                DoActions(Order("50 + 1n Battlecruiser", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                trg.Main_Wait(150)
                # (Line 59) }
                # (Line 60) else if (v.P_LoopMain[playerID] == 1 || v.P_LoopMain[playerID] == 3)
            if EUDElseIf()(EUDSCOr()(v.P_LoopMain[playerID] == 1)(v.P_LoopMain[playerID] == 3)()):
                # (Line 61) {
                # (Line 62) trg.Shape_Square(playerID, 1, "40 + 1n Mojo", 144, 0);
                trg.Shape_Square(playerID, 1, "40 + 1n Mojo", 144, 0)
                # (Line 63) trg.Shape_Square(playerID, 1, "40 + 1n Mojo", 96, 0);
                trg.Shape_Square(playerID, 1, "40 + 1n Mojo", 96, 0)
                # (Line 64) trg.Shape_Square(playerID, 1, "40 + 1n Mojo", 48, 0);
                trg.Shape_Square(playerID, 1, "40 + 1n Mojo", 48, 0)
                # (Line 65) trg.Shape_Square(playerID, 1, "60 + 1n Archon", 144, 0);
                trg.Shape_Square(playerID, 1, "60 + 1n Archon", 144, 0)
                # (Line 66) trg.Shape_Square(playerID, 1, "60 + 1n Archon", 96, 0);
                trg.Shape_Square(playerID, 1, "60 + 1n Archon", 96, 0)
                # (Line 67) trg.Shape_Square(playerID, 1, "60 + 1n Archon", 48, 0);
                trg.Shape_Square(playerID, 1, "60 + 1n Archon", 48, 0)
                # (Line 68) KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
                # (Line 70) trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0);
                DoActions(KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID))
                trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0)
                # (Line 71) Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                # (Line 72) trg.Main_Wait(40);
                DoActions(Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                trg.Main_Wait(40)
                # (Line 73) }
                # (Line 74) else if (v.P_LoopMain[playerID] == 2 || v.P_LoopMain[playerID] == 4)
            if EUDElseIf()(EUDSCOr()(v.P_LoopMain[playerID] == 2)(v.P_LoopMain[playerID] == 4)()):
                # (Line 75) {
                # (Line 76) trg.Main_Wait(0);
                trg.Main_Wait(0)
                # (Line 77) }
                # (Line 78) else if (v.P_LoopMain[playerID] == 5)
            if EUDElseIf()(v.P_LoopMain[playerID] == 5):
                # (Line 79) {
                # (Line 80) trg.Shape_Square(playerID, 1, "50 + 1n Battlecruiser", 192, 192);
                trg.Shape_Square(playerID, 1, "50 + 1n Battlecruiser", 192, 192)
                # (Line 81) trg.Shape_Square(playerID, 1, "60 + 1n Archon", 192, 192);
                trg.Shape_Square(playerID, 1, "60 + 1n Archon", 192, 192)
                # (Line 82) KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
                # (Line 84) trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0);
                DoActions(KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID))
                trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0)
                # (Line 85) Order("50 + 1n Battlecruiser", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                # (Line 86) trg.Main_Wait(0);
                DoActions(Order("50 + 1n Battlecruiser", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                trg.Main_Wait(0)
                # (Line 87) }
                # (Line 88) else if (v.P_LoopMain[playerID] >= 6 && v.P_LoopMain[playerID] <= 8)
            if EUDElseIf()(EUDSCAnd()(v.P_LoopMain[playerID] >= 6)(v.P_LoopMain[playerID] <= 8)()):
                # (Line 89) {
                # (Line 90) var pos = 144 - (48 * (v.P_LoopMain[playerID] - 6));
                pos = EUDVariable()
                pos << (144 - (48 * (v.P_LoopMain[playerID] - 6)))
                # (Line 91) trg.Shape_Square(playerID, 1, "40 + 1n Gantrithor", pos, pos);
                trg.Shape_Square(playerID, 1, "40 + 1n Gantrithor", pos, pos)
                # (Line 92) trg.Shape_Square(playerID, 1, "60 + 1n Archon", pos, pos);
                trg.Shape_Square(playerID, 1, "60 + 1n Archon", pos, pos)
                # (Line 93) KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", playerID);
                # (Line 94) KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", playerID))
                # (Line 95) trg.Main_Wait(0);
                DoActions(KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID))
                trg.Main_Wait(0)
                # (Line 96) }
                # (Line 97) else if (v.P_LoopMain[playerID] == 9)
            if EUDElseIf()(v.P_LoopMain[playerID] == 9):
                # (Line 98) {
                # (Line 99) trg.Shape_Square(playerID, 1, "50 + 1n Battlecruiser", 192, 0);
                trg.Shape_Square(playerID, 1, "50 + 1n Battlecruiser", 192, 0)
                # (Line 100) trg.Shape_Square(playerID, 1, "60 + 1n Archon", 192, 0);
                trg.Shape_Square(playerID, 1, "60 + 1n Archon", 192, 0)
                # (Line 101) KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
                # (Line 103) trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0);
                DoActions(KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID))
                trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0)
                # (Line 104) Order("50 + 1n Battlecruiser", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                # (Line 105) trg.Main_Wait(0);
                DoActions(Order("50 + 1n Battlecruiser", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                trg.Main_Wait(0)
                # (Line 106) }
                # (Line 107) else if (v.P_LoopMain[playerID] >= 10 && v.P_LoopMain[playerID] <= 12)
            if EUDElseIf()(EUDSCAnd()(v.P_LoopMain[playerID] >= 10)(v.P_LoopMain[playerID] <= 12)()):
                # (Line 108) {
                # (Line 109) var pos = 144 - (48 * (v.P_LoopMain[playerID] - 10));
                pos = EUDVariable()
                pos << (144 - (48 * (v.P_LoopMain[playerID] - 10)))
                # (Line 110) trg.Shape_Square(playerID, 1, "40 + 1n Gantrithor", pos, 0);
                trg.Shape_Square(playerID, 1, "40 + 1n Gantrithor", pos, 0)
                # (Line 111) trg.Shape_Square(playerID, 1, "60 + 1n Archon", pos, 0);
                trg.Shape_Square(playerID, 1, "60 + 1n Archon", pos, 0)
                # (Line 112) KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", playerID);
                # (Line 113) KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", playerID))
                # (Line 114) trg.Main_Wait(0);
                DoActions(KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID))
                trg.Main_Wait(0)
                # (Line 115) }
                # (Line 116) else if (v.P_LoopMain[playerID] == 12)
            if EUDElseIf()(v.P_LoopMain[playerID] == 12):
                # (Line 117) {
                # (Line 118) trg.Shape_Square(playerID, 1, 2, 96, 96);
                trg.Shape_Square(playerID, 1, 2, 96, 96)
                # (Line 119) trg.Shape_Square(playerID, 1, 2, 48, 48);
                trg.Shape_Square(playerID, 1, 2, 48, 48)
                # (Line 120) trg.Shape_Square(playerID, 1, 2, 128, 0);
                trg.Shape_Square(playerID, 1, 2, 128, 0)
                # (Line 121) trg.Shape_Square(playerID, 1, 2, 64, 0);
                trg.Shape_Square(playerID, 1, 2, 64, 0)
                # (Line 123) trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0);
                trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0)
                # (Line 124) Order(2, playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                # (Line 125) trg.Main_Wait(30);
                DoActions(Order(2, playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                trg.Main_Wait(30)
                # (Line 126) }
                # (Line 127) else if (v.P_LoopMain[playerID] == 13)
            if EUDElseIf()(v.P_LoopMain[playerID] == 13):
                # (Line 128) {
                # (Line 129) trg.Shape_Square(playerID, 1, "50 + 1n Battlecruiser", 144, 144);
                trg.Shape_Square(playerID, 1, "50 + 1n Battlecruiser", 144, 144)
                # (Line 130) trg.Shape_Square(playerID, 1, "Protoss Dark Archon", 144, 144);
                trg.Shape_Square(playerID, 1, "Protoss Dark Archon", 144, 144)
                # (Line 132) trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0);
                trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0)
                # (Line 133) Order(2, playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                # (Line 134) trg.Main_Wait(30);
                DoActions(Order(2, playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                trg.Main_Wait(30)
                # (Line 135) }
                # (Line 137) v.P_LoopMain[playerID] += 1;
            EUDEndIf()
            _ARRW(v.P_LoopMain, playerID).__iadd__(1)
            # (Line 139) if (v.P_LoopMain[playerID] == 13)
            if EUDIf()(v.P_LoopMain[playerID] == 13):
                # (Line 140) {
                # (Line 141) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 142) v.P_CountMain[playerID] += 1;
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 143) }
                # (Line 144) }
            EUDEndIf()
            # (Line 145) if (v.P_CountMain[playerID] == 3)
        EUDEndIf()
        if EUDIf()(v.P_CountMain[playerID] == 3):
            # (Line 146) {
            # (Line 147) if (v.P_LoopMain[playerID] <= 5)
            if EUDIf()(v.P_LoopMain[playerID] <= 5):
                # (Line 148) {
                # (Line 149) trg.Shape_Double(playerID, 1, "50 + 1n Battlecruiser", 144 - (48 * v.P_LoopMain[playerID]), 144);
                trg.Shape_Double(playerID, 1, "50 + 1n Battlecruiser", 144 - (48 * v.P_LoopMain[playerID]), 144)
                # (Line 150) trg.Shape_Double(playerID, 1, "Protoss Dark Archon", 144 - (48 * v.P_LoopMain[playerID]), 144);
                trg.Shape_Double(playerID, 1, "Protoss Dark Archon", 144 - (48 * v.P_LoopMain[playerID]), 144)
                # (Line 151) KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID);
                # (Line 152) KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID))
                # (Line 153) trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0);
                DoActions(KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID))
                trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0)
                # (Line 154) Order("50 + 1n Battlecruiser", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                # (Line 155) trg.Main_Wait(0);
                DoActions(Order("50 + 1n Battlecruiser", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                trg.Main_Wait(0)
                # (Line 156) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 157) }
                # (Line 158) else if (v.P_LoopMain[playerID] == 6)
            if EUDElseIf()(v.P_LoopMain[playerID] == 6):
                # (Line 159) {
                # (Line 160) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 161) v.P_CountMain[playerID] += 1;
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 162) }
                # (Line 163) }
            EUDEndIf()
            # (Line 164) else if (v.P_CountMain[playerID] == 4)
        if EUDElseIf()(v.P_CountMain[playerID] == 4):
            # (Line 165) {
            # (Line 166) if (v.P_LoopMain[playerID] <= 5)
            if EUDIf()(v.P_LoopMain[playerID] <= 5):
                # (Line 167) {
                # (Line 168) trg.Shape_Double(playerID, 1, "50 + 1n Battlecruiser", 144, -144 + (48 * v.P_LoopMain[playerID]));
                trg.Shape_Double(playerID, 1, "50 + 1n Battlecruiser", 144, -144 + (48 * v.P_LoopMain[playerID]))
                # (Line 169) trg.Shape_Double(playerID, 1, "Protoss Dark Archon", 144, -144 + (48 * v.P_LoopMain[playerID]));
                trg.Shape_Double(playerID, 1, "Protoss Dark Archon", 144, -144 + (48 * v.P_LoopMain[playerID]))
                # (Line 170) KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID);
                # (Line 171) KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID))
                # (Line 172) trg.Main_Wait(0);
                DoActions(KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID))
                trg.Main_Wait(0)
                # (Line 173) v.P_LoopMain[playerID] += 1;
                _ARRW(v.P_LoopMain, playerID).__iadd__(1)
                # (Line 174) }
                # (Line 175) else if (v.P_LoopMain[playerID] == 6)
            if EUDElseIf()(v.P_LoopMain[playerID] == 6):
                # (Line 176) {
                # (Line 177) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 178) v.P_CountMain[playerID] += 1;
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 179) }
                # (Line 180) }
            EUDEndIf()
            # (Line 181) else if (v.P_CountMain[playerID] == 5)
        if EUDElseIf()(v.P_CountMain[playerID] == 5):
            # (Line 182) {
            # (Line 183) KillUnitAt(All, 2, "Anywhere", playerID);
            # (Line 184) KillUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID);
            DoActions(KillUnitAt(All, 2, "Anywhere", playerID))
            # (Line 185) KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID);
            DoActions(KillUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID))
            # (Line 187) if (v.P_LoopMain[playerID] == 0)
            DoActions(KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID))
            if EUDIf()(v.P_LoopMain[playerID] == 0):
                # (Line 188) {
                # (Line 189) trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 192, 192);
                trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 192, 192)
                # (Line 190) trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 144, 192);
                trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 144, 192)
                # (Line 191) trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 192, 144);
                trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 192, 144)
                # (Line 192) KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID);
                # (Line 193) trg.Main_Wait(0);
                DoActions(KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID))
                trg.Main_Wait(0)
                # (Line 194) }
                # (Line 195) else if (v.P_LoopMain[playerID] == 1)
            if EUDElseIf()(v.P_LoopMain[playerID] == 1):
                # (Line 196) {
                # (Line 197) trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 144, 144);
                trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 144, 144)
                # (Line 198) trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 144, 96);
                trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 144, 96)
                # (Line 199) trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 96, 144);
                trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 96, 144)
                # (Line 200) KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID);
                # (Line 201) trg.Main_Wait(0);
                DoActions(KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID))
                trg.Main_Wait(0)
                # (Line 202) }
                # (Line 203) else if (v.P_LoopMain[playerID] == 2)
            if EUDElseIf()(v.P_LoopMain[playerID] == 2):
                # (Line 204) {
                # (Line 205) trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 96, 96);
                trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 96, 96)
                # (Line 206) trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 48, 96);
                trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 48, 96)
                # (Line 207) trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 96, 48);
                trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 96, 48)
                # (Line 208) KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID);
                # (Line 209) trg.Main_Wait(0);
                DoActions(KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID))
                trg.Main_Wait(0)
                # (Line 210) }
                # (Line 211) else if (v.P_LoopMain[playerID] == 3)
            if EUDElseIf()(v.P_LoopMain[playerID] == 3):
                # (Line 212) {
                # (Line 213) trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 48, 48);
                trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 48, 48)
                # (Line 214) trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 48, 0);
                trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 48, 0)
                # (Line 215) KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID);
                # (Line 216) trg.Main_Wait(0);
                DoActions(KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID))
                trg.Main_Wait(0)
                # (Line 217) }
                # (Line 218) else if (v.P_LoopMain[playerID] == 4)
            if EUDElseIf()(v.P_LoopMain[playerID] == 4):
                # (Line 219) {
                # (Line 220) trg.Shape_Square(playerID, 1, "50 + 1n Battlecruiser", 144, 96);
                trg.Shape_Square(playerID, 1, "50 + 1n Battlecruiser", 144, 96)
                # (Line 221) trg.Shape_Square(playerID, 1, "50 + 1n Battlecruiser", 144, 0);
                trg.Shape_Square(playerID, 1, "50 + 1n Battlecruiser", 144, 0)
                # (Line 222) trg.Shape_Square(playerID, 1, "50 + 1n Battlecruiser", 96, 144);
                trg.Shape_Square(playerID, 1, "50 + 1n Battlecruiser", 96, 144)
                # (Line 223) trg.Shape_Square(playerID, 1, "Protoss Dark Archon", 144, 96);
                trg.Shape_Square(playerID, 1, "Protoss Dark Archon", 144, 96)
                # (Line 224) trg.Shape_Square(playerID, 1, "Protoss Dark Archon", 144, 0);
                trg.Shape_Square(playerID, 1, "Protoss Dark Archon", 144, 0)
                # (Line 225) trg.Shape_Square(playerID, 1, "Protoss Dark Archon", 96, 144);
                trg.Shape_Square(playerID, 1, "Protoss Dark Archon", 96, 144)
                # (Line 226) KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID);
                # (Line 227) KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID))
                # (Line 228) trg.Main_Wait(0);
                DoActions(KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID))
                trg.Main_Wait(0)
                # (Line 229) }
                # (Line 230) else if (v.P_LoopMain[playerID] == 5)
            if EUDElseIf()(v.P_LoopMain[playerID] == 5):
                # (Line 231) {
                # (Line 232) trg.Shape_Square(playerID, 1, "40 + 1n Mojo", 0, 48);
                trg.Shape_Square(playerID, 1, "40 + 1n Mojo", 0, 48)
                # (Line 233) trg.Shape_Square(playerID, 1, "40 + 1n Mojo", 0, 96);
                trg.Shape_Square(playerID, 1, "40 + 1n Mojo", 0, 96)
                # (Line 234) trg.Shape_Square(playerID, 1, 2, 0, 48);
                trg.Shape_Square(playerID, 1, 2, 0, 48)
                # (Line 235) trg.Shape_Square(playerID, 1, 2, 0, 96);
                trg.Shape_Square(playerID, 1, 2, 0, 96)
                # (Line 237) trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0);
                trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0)
                # (Line 238) Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                # (Line 239) Order(2, playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                DoActions(Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                # (Line 240) trg.Main_Wait(230);
                DoActions(Order(2, playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                trg.Main_Wait(230)
                # (Line 241) }
                # (Line 242) else if (v.P_LoopMain[playerID] == 6)
            if EUDElseIf()(v.P_LoopMain[playerID] == 6):
                # (Line 243) {
                # (Line 244) trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 48, 48);
                trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 48, 48)
                # (Line 245) trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 48, 0);
                trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 48, 0)
                # (Line 246) KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID);
                # (Line 247) trg.Main_Wait(0);
                DoActions(KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID))
                trg.Main_Wait(0)
                # (Line 248) }
                # (Line 249) else if (v.P_LoopMain[playerID] == 7)
            if EUDElseIf()(v.P_LoopMain[playerID] == 7):
                # (Line 250) {
                # (Line 251) trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 96, 96);
                trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 96, 96)
                # (Line 252) trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 48, 96);
                trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 48, 96)
                # (Line 253) trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 96, 48);
                trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 96, 48)
                # (Line 254) KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID);
                # (Line 255) trg.Main_Wait(0);
                DoActions(KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID))
                trg.Main_Wait(0)
                # (Line 256) }
                # (Line 257) else if (v.P_LoopMain[playerID] == 8)
            if EUDElseIf()(v.P_LoopMain[playerID] == 8):
                # (Line 258) {
                # (Line 259) trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 144, 144);
                trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 144, 144)
                # (Line 260) trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 144, 96);
                trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 144, 96)
                # (Line 261) trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 96, 144);
                trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 96, 144)
                # (Line 262) KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID);
                # (Line 263) trg.Main_Wait(0);
                DoActions(KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID))
                trg.Main_Wait(0)
                # (Line 264) }
                # (Line 265) else if (v.P_LoopMain[playerID] == 9)
            if EUDElseIf()(v.P_LoopMain[playerID] == 9):
                # (Line 266) {
                # (Line 267) trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 192, 192);
                trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 192, 192)
                # (Line 268) trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 144, 192);
                trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 144, 192)
                # (Line 269) trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 192, 144);
                trg.Shape_Square(playerID, 1, "40 + 1n Guardian", 192, 144)
                # (Line 270) KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID);
                # (Line 271) trg.Main_Wait(0);
                DoActions(KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID))
                trg.Main_Wait(0)
                # (Line 272) }
                # (Line 273) else if (v.P_LoopMain[playerID] == 10)
            if EUDElseIf()(v.P_LoopMain[playerID] == 10):
                # (Line 274) {
                # (Line 275) trg.Shape_Square(playerID, 1, "40 + 1n Mojo", 0, 48);
                trg.Shape_Square(playerID, 1, "40 + 1n Mojo", 0, 48)
                # (Line 276) trg.Shape_Square(playerID, 1, "40 + 1n Mojo", 0, 96);
                trg.Shape_Square(playerID, 1, "40 + 1n Mojo", 0, 96)
                # (Line 277) trg.Shape_Square(playerID, 1, 2, 0, 48);
                trg.Shape_Square(playerID, 1, 2, 0, 48)
                # (Line 278) trg.Shape_Square(playerID, 1, 2, 0, 96);
                trg.Shape_Square(playerID, 1, 2, 0, 96)
                # (Line 280) trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0);
                trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0)
                # (Line 281) Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                # (Line 282) Order(2, playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                DoActions(Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                # (Line 283) trg.Main_Wait(90);
                DoActions(Order(2, playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                trg.Main_Wait(90)
                # (Line 284) }
                # (Line 285) else if (Bring(playerID, AtLeast, 2, "Protoss Arbiter", "[Skill]UseSkill")
            _t37 = EUDElseIf()
            # (Line 286) && v.P_LoopMain[playerID] == 11)
            if _t37(EUDSCAnd()(Bring(playerID, AtLeast, 2, "Protoss Arbiter", "[Skill]UseSkill"))(v.P_LoopMain[playerID] == 11)()):
                # (Line 287) {
                # (Line 288) s.CharacterVoice(4);
                s.CharacterVoice(4)
                # (Line 289) v.P_Step[playerID] = 220;
                _ARRW(v.P_Step, playerID) << (220)
                # (Line 290) v.P_CountMain[playerID] = 0;
                _ARRW(v.P_CountMain, playerID) << (0)
                # (Line 291) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 292) KillUnitAt(2, "Protoss Arbiter", "[Skill]UseSkill", playerID);
                # (Line 293) }
                DoActions(KillUnitAt(2, "Protoss Arbiter", "[Skill]UseSkill", playerID))
                # (Line 294) else if (v.P_LoopMain[playerID] == 11)
            if EUDElseIf()(v.P_LoopMain[playerID] == 11):
                # (Line 295) {
                # (Line 296) trg.SkillEnd();
                trg.SkillEnd()
                # (Line 297) }
                # (Line 299) v.P_LoopMain[playerID] += 1;
            EUDEndIf()
            _ARRW(v.P_LoopMain, playerID).__iadd__(1)
            # (Line 300) }
            # (Line 301) }
        EUDEndIf()
        # (Line 302) }
    EUDEndIf()