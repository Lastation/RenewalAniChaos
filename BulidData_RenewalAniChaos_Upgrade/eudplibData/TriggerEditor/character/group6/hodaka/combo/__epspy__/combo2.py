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
# (Line 3) import variable as v;
import variable as v
# (Line 4) import func.trig as trg;
from func import trig as trg
# (Line 5) import func.sound as s;
from func import sound as s
# (Line 7) var x = 0;
x = EUDCreateVariables(1)
_IGVA([x], lambda: [0])
# (Line 8) function main(playerID)
# (Line 9) {
@EUDFunc
def f_main(playerID):
    # (Line 10) trg.Debuff_Stop();
    trg.Debuff_Stop()
    # (Line 11) trg.Debuff_BanReturn();
    trg.Debuff_BanReturn()
    # (Line 13) if (v.P_WaitMain[playerID] == 0)
    if EUDIf()(v.P_WaitMain[playerID] == 0):
        # (Line 14) {
        # (Line 15) if (v.P_CountMain[playerID] == 0)
        if EUDIf()(v.P_CountMain[playerID] == 0):
            # (Line 16) {
            # (Line 17) if (v.P_LoopMain[playerID] <= 6)
            if EUDIf()(v.P_LoopMain[playerID] <= 6):
                # (Line 18) {
                # (Line 19) trg.Shape_Double(playerID,1,"60 + 1n Siege",192 - v.P_LoopMain[playerID] * 32, 0 + v.P_LoopMain[playerID] * 32);
                trg.Shape_Double(playerID, 1, "60 + 1n Siege", 192 - v.P_LoopMain[playerID] * 32, 0 + v.P_LoopMain[playerID] * 32)
                # (Line 20) trg.Shape_Double(playerID,1,"60 + 1n Siege",0 - v.P_LoopMain[playerID] * 32, 192 - v.P_LoopMain[playerID] * 32);
                trg.Shape_Double(playerID, 1, "60 + 1n Siege", 0 - v.P_LoopMain[playerID] * 32, 192 - v.P_LoopMain[playerID] * 32)
                # (Line 21) trg.Shape_Double(playerID,1,"Terran Science Vessel",192 - v.P_LoopMain[playerID] * 32, 0 + v.P_LoopMain[playerID] * 32);
                trg.Shape_Double(playerID, 1, "Terran Science Vessel", 192 - v.P_LoopMain[playerID] * 32, 0 + v.P_LoopMain[playerID] * 32)
                # (Line 22) trg.Shape_Double(playerID,1,"Terran Science Vessel",0 - v.P_LoopMain[playerID] * 32, 192 - v.P_LoopMain[playerID] * 32);
                trg.Shape_Double(playerID, 1, "Terran Science Vessel", 0 - v.P_LoopMain[playerID] * 32, 192 - v.P_LoopMain[playerID] * 32)
                # (Line 23) KillUnitAt(All,"Terran Science Vessel","Anywhere",playerID);
                # (Line 24) Order("60 + 1n Siege",playerID,"Anywhere",Attack,v.P_LocationID[playerID]);
                DoActions(KillUnitAt(All, "Terran Science Vessel", "Anywhere", playerID))
                # (Line 25) trg.Main_Wait(100);
                DoActions(Order("60 + 1n Siege", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                trg.Main_Wait(100)
                # (Line 26) }
                # (Line 27) else if (v.P_LoopMain[playerID] == 7)
            if EUDElseIf()(v.P_LoopMain[playerID] == 7):
                # (Line 28) {
                # (Line 29) trg.Main_Wait(800);
                trg.Main_Wait(800)
                # (Line 30) }
                # (Line 32) else if(v.P_LoopMain[playerID] <= 11)
            if EUDElseIf()(v.P_LoopMain[playerID] <= 11):
                # (Line 33) {
                # (Line 34) trg.Shape_Square(playerID,1,"40 + 1n Mojo", 96 ,96 - x *32);
                trg.Shape_Square(playerID, 1, "40 + 1n Mojo", 96, 96 - x * 32)
                # (Line 35) KillUnitAt(All,"40 + 1n Mojo","Anywhere",playerID);
                # (Line 36) trg.Main_Wait(10);
                DoActions(KillUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID))
                trg.Main_Wait(10)
                # (Line 37) x +=1;
                x.__iadd__(1)
                # (Line 39) }
                # (Line 40) else if(v.P_LoopMain[playerID] == 12)
            if EUDElseIf()(v.P_LoopMain[playerID] == 12):
                # (Line 41) {
                # (Line 42) trg.Shape_Square(playerID,1,"50 + 1n Battlecruiser",128, 96);
                trg.Shape_Square(playerID, 1, "50 + 1n Battlecruiser", 128, 96)
                # (Line 43) trg.Shape_Square(playerID,1,"50 + 1n Battlecruiser",96, 128);
                trg.Shape_Square(playerID, 1, "50 + 1n Battlecruiser", 96, 128)
                # (Line 44) trg.MoveLoc(v.P_UnitID[playerID],playerID,0,0);
                trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0)
                # (Line 45) Order("50 + 1n Battlecruiser",playerID,"Anywhere",Attack,v.P_LocationID[playerID]);
                # (Line 46) trg.Main_Wait(1000);
                DoActions(Order("50 + 1n Battlecruiser", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                trg.Main_Wait(1000)
                # (Line 47) }
                # (Line 48) else if(v.P_LoopMain[playerID] == 13)
            if EUDElseIf()(v.P_LoopMain[playerID] == 13):
                # (Line 49) {
                # (Line 50) trg.Shape_Double(playerID,1,"40 + 1n Wraith",64,0);
                trg.Shape_Double(playerID, 1, "40 + 1n Wraith", 64, 0)
                # (Line 51) trg.Shape_Double(playerID,1,"40 + 1n Wraith",0,64);
                trg.Shape_Double(playerID, 1, "40 + 1n Wraith", 0, 64)
                # (Line 52) trg.Shape_Dot(playerID,1,"40 + 1n Wraith",0,0);
                trg.Shape_Dot(playerID, 1, "40 + 1n Wraith", 0, 0)
                # (Line 53) trg.MoveLoc(v.P_UnitID[playerID],playerID,0,0);
                trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0)
                # (Line 54) Order("40 + 1n Wraith",playerID,"Anywhere",Attack,v.P_LocationID[playerID]);
                # (Line 55) trg.Main_Wait(300);
                DoActions(Order("40 + 1n Wraith", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                trg.Main_Wait(300)
                # (Line 56) }
                # (Line 57) else if(v.P_LoopMain[playerID] == 14)
            if EUDElseIf()(v.P_LoopMain[playerID] == 14):
                # (Line 58) {
                # (Line 59) KillUnitAt(All,"40 + 1n Wraith","Anywhere",playerID);
                # (Line 60) trg.Main_Wait(500);
                DoActions(KillUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID))
                trg.Main_Wait(500)
                # (Line 61) }
                # (Line 63) else if(v.P_LoopMain[playerID] == 15)
            if EUDElseIf()(v.P_LoopMain[playerID] == 15):
                # (Line 64) {
                # (Line 65) KillUnitAt(All,"50 + 1n Battlecruiser","Anywhere",playerID);
                # (Line 66) KillUnitAt(All,"60 + 1n Siege","Anywhere",playerID);
                DoActions(KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID))
                # (Line 67) trg.Main_Wait(0);
                DoActions(KillUnitAt(All, "60 + 1n Siege", "Anywhere", playerID))
                trg.Main_Wait(0)
                # (Line 68) }
                # (Line 69) else if(v.P_LoopMain[playerID] == 16)
            if EUDElseIf()(v.P_LoopMain[playerID] == 16):
                # (Line 70) {
                # (Line 71) trg.Shape_Double(playerID,1,"50 + 1n Battlecruiser",192,0);
                trg.Shape_Double(playerID, 1, "50 + 1n Battlecruiser", 192, 0)
                # (Line 72) trg.Shape_Double(playerID,1,"50 + 1n Battlecruiser",160,32);
                trg.Shape_Double(playerID, 1, "50 + 1n Battlecruiser", 160, 32)
                # (Line 73) trg.Shape_Double(playerID,1,"50 + 1n Battlecruiser",128,64);
                trg.Shape_Double(playerID, 1, "50 + 1n Battlecruiser", 128, 64)
                # (Line 74) trg.Shape_Double(playerID,1,"50 + 1n Battlecruiser",96,96);
                trg.Shape_Double(playerID, 1, "50 + 1n Battlecruiser", 96, 96)
                # (Line 75) trg.Shape_Double(playerID,1,"50 + 1n Battlecruiser",64,128);
                trg.Shape_Double(playerID, 1, "50 + 1n Battlecruiser", 64, 128)
                # (Line 76) trg.Shape_Double(playerID,1,"50 + 1n Battlecruiser",32,160);
                trg.Shape_Double(playerID, 1, "50 + 1n Battlecruiser", 32, 160)
                # (Line 77) trg.Shape_Double(playerID,1,"50 + 1n Battlecruiser",0,192);
                trg.Shape_Double(playerID, 1, "50 + 1n Battlecruiser", 0, 192)
                # (Line 78) trg.Shape_Double(playerID,1,"50 + 1n Battlecruiser",-32,160);
                trg.Shape_Double(playerID, 1, "50 + 1n Battlecruiser", -32, 160)
                # (Line 79) trg.Shape_Double(playerID,1,"50 + 1n Battlecruiser",-64,128);
                trg.Shape_Double(playerID, 1, "50 + 1n Battlecruiser", -64, 128)
                # (Line 80) trg.Shape_Double(playerID,1,"50 + 1n Battlecruiser",-96,96);
                trg.Shape_Double(playerID, 1, "50 + 1n Battlecruiser", -96, 96)
                # (Line 81) trg.Shape_Double(playerID,1,"50 + 1n Battlecruiser",-128,64);
                trg.Shape_Double(playerID, 1, "50 + 1n Battlecruiser", -128, 64)
                # (Line 82) trg.Shape_Double(playerID,1,"50 + 1n Battlecruiser",-160,32);
                trg.Shape_Double(playerID, 1, "50 + 1n Battlecruiser", -160, 32)
                # (Line 83) trg.MoveLoc(v.P_UnitID[playerID],playerID,0,0);
                trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0)
                # (Line 84) Order("50 + 1n Battlecruiser",playerID,"Anywhere",Attack,v.P_LocationID[playerID]);
                # (Line 85) trg.Main_Wait(300);
                DoActions(Order("50 + 1n Battlecruiser", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                trg.Main_Wait(300)
                # (Line 86) }
                # (Line 88) else if(v.P_LoopMain[playerID] == 17)
            if EUDElseIf()(v.P_LoopMain[playerID] == 17):
                # (Line 89) {
                # (Line 90) KillUnitAt(All,"50 + 1n Battlecruiser","Anywhere",playerID);
                # (Line 91) trg.Main_Wait(1700);
                DoActions(KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID))
                trg.Main_Wait(1700)
                # (Line 92) }
                # (Line 93) else if(v.P_LoopMain[playerID] == 18)
            if EUDElseIf()(v.P_LoopMain[playerID] == 18):
                # (Line 94) {
                # (Line 95) trg.Shape_Square(playerID,1,"50 + 1n Tank",192,0);
                trg.Shape_Square(playerID, 1, "50 + 1n Tank", 192, 0)
                # (Line 96) trg.Shape_Square(playerID,1,"50 + 1n Tank",96,96);
                trg.Shape_Square(playerID, 1, "50 + 1n Tank", 96, 96)
                # (Line 97) trg.Shape_Square(playerID,1,"60 + 1n Dragoon",144,48);
                trg.Shape_Square(playerID, 1, "60 + 1n Dragoon", 144, 48)
                # (Line 98) trg.Shape_Square(playerID,1,"60 + 1n Dragoon",48,144);
                trg.Shape_Square(playerID, 1, "60 + 1n Dragoon", 48, 144)
                # (Line 99) trg.Shape_Square(playerID,1,"60 + 1n Archon",96,96);
                trg.Shape_Square(playerID, 1, "60 + 1n Archon", 96, 96)
                # (Line 100) trg.Shape_Square(playerID,1,"60 + 1n Archon",192,0);
                trg.Shape_Square(playerID, 1, "60 + 1n Archon", 192, 0)
                # (Line 101) trg.Shape_Square(playerID,1,"60 + 1n High Templar",144,48);
                trg.Shape_Square(playerID, 1, "60 + 1n High Templar", 144, 48)
                # (Line 102) trg.Shape_Square(playerID,1,"60 + 1n High Templar",48,144);
                trg.Shape_Square(playerID, 1, "60 + 1n High Templar", 48, 144)
                # (Line 103) KillUnitAt(All,"60 + 1n High Templar","Anywhere",playerID);
                # (Line 104) KillUnitAt(All,"60 + 1n Archon","Anywhere",playerID);
                DoActions(KillUnitAt(All, "60 + 1n High Templar", "Anywhere", playerID))
                # (Line 105) trg.MoveLoc(v.P_UnitID[playerID],playerID,0,0);
                DoActions(KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID))
                trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0)
                # (Line 106) Order("50 + 1n Tank",playerID,"Anywhere",Attack,v.P_LocationID[playerID]);
                # (Line 107) Order("60 + 1n Dragoon",playerID,"Anywhere",Attack,v.P_LocationID[playerID]);
                DoActions(Order("50 + 1n Tank", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                # (Line 108) trg.Main_Wait(1500);
                DoActions(Order("60 + 1n Dragoon", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                trg.Main_Wait(1500)
                # (Line 109) }
                # (Line 110) else if(v.P_LoopMain[playerID] == 19)
            if EUDElseIf()(v.P_LoopMain[playerID] == 19):
                # (Line 111) {
                # (Line 112) trg.Shape_NxNSquare(playerID,1,"60 + 1n Danimoth",3,64);
                trg.Shape_NxNSquare(playerID, 1, "60 + 1n Danimoth", 3, 64)
                # (Line 113) trg.MoveLoc(v.P_UnitID[playerID],playerID,0,0);
                trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0)
                # (Line 114) Order("60 + 1n Danimoth",playerID,"Anywhere",Attack,v.P_LocationID[playerID]);
                # (Line 115) trg.Main_Wait(200);
                DoActions(Order("60 + 1n Danimoth", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                trg.Main_Wait(200)
                # (Line 116) }
                # (Line 117) else if(v.P_LoopMain[playerID] == 20)
            if EUDElseIf()(v.P_LoopMain[playerID] == 20):
                # (Line 118) {
                # (Line 119) KillUnitAt(All,"60 + 1n Danimoth","Anywhere",playerID);
                # (Line 120) trg.Main_Wait(100);
                DoActions(KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", playerID))
                trg.Main_Wait(100)
                # (Line 121) }
                # (Line 122) else if(v.P_LoopMain[playerID] == 21)
            if EUDElseIf()(v.P_LoopMain[playerID] == 21):
                # (Line 123) {
                # (Line 124) trg.Shape_NxNSquare(playerID,1,"50 + 1n Battlecruiser",3,64);
                trg.Shape_NxNSquare(playerID, 1, "50 + 1n Battlecruiser", 3, 64)
                # (Line 125) trg.MoveLoc(v.P_UnitID[playerID],playerID,0,0);
                trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0)
                # (Line 126) Order("50 + 1n Battlecruiser",playerID,"Anywhere",Attack,v.P_LocationID[playerID]);
                # (Line 127) trg.Main_Wait(200);
                DoActions(Order("50 + 1n Battlecruiser", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                trg.Main_Wait(200)
                # (Line 129) }
                # (Line 130) else if(v.P_LoopMain[playerID] == 22)
            if EUDElseIf()(v.P_LoopMain[playerID] == 22):
                # (Line 131) {
                # (Line 133) KillUnitAt(All,"50 + 1n Battlecruiser","Anywhere",playerID);
                # (Line 134) KillUnitAt(All,"50 + 1n Tank","Anywhere",playerID);
                DoActions(KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID))
                # (Line 135) KillUnitAt(All,"60 + 1n Dragoon","Anywhere",playerID);
                DoActions(KillUnitAt(All, "50 + 1n Tank", "Anywhere", playerID))
                # (Line 136) x = 0;
                DoActions(KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", playerID))
                x << (0)
                # (Line 137) trg.SkillEnd();
                trg.SkillEnd()
                # (Line 138) }
                # (Line 140) v.P_LoopMain[playerID] += 1;
            EUDEndIf()
            _ARRW(v.P_LoopMain, playerID).__iadd__(1)
            # (Line 141) }
            # (Line 142) }
        EUDEndIf()
        # (Line 143) }
    EUDEndIf()