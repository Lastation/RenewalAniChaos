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
# (Line 5) import func.sound as s;
from func import sound as s
# (Line 7) var x = 0;
x = EUDCreateVariables(1)
_IGVA([x], lambda: [0])
# (Line 8) function main(playerID)
# (Line 9) {
@EUDFunc
def f_main(playerID):
    # (Line 10) trg.Buff_ShieldFix(1);
    trg.Buff_ShieldFix(1)
    # (Line 11) trg.Debuff_BanReturn();
    trg.Debuff_BanReturn()
    # (Line 12) trg.Effect_Recall();
    trg.Effect_Recall()
    # (Line 14) if (v.P_LoopMain[playerID] >= 2)
    if EUDIf()(v.P_LoopMain[playerID] >= 2):
        # (Line 15) {
        # (Line 16) trg.Debuff_Stop();
        trg.Debuff_Stop()
        # (Line 17) }
        # (Line 19) if (v.P_WaitMain[playerID] == 0)
    EUDEndIf()
    if EUDIf()(v.P_WaitMain[playerID] == 0):
        # (Line 20) {
        # (Line 21) if (v.P_CountMain[playerID] == 0)
        if EUDIf()(v.P_CountMain[playerID] == 0):
            # (Line 22) {
            # (Line 23) if (v.P_LoopMain[playerID] == 0)
            if EUDIf()(v.P_LoopMain[playerID] == 0):
                # (Line 24) {
                # (Line 25) trg.Main_Wait(10000);
                trg.Main_Wait(10000)
                # (Line 26) }
                # (Line 28) else if (v.P_LoopMain[playerID] == 1)
            if EUDElseIf()(v.P_LoopMain[playerID] == 1):
                # (Line 29) {
                # (Line 30) s.CharacterVoice(10);
                s.CharacterVoice(10)
                # (Line 31) }
                # (Line 32) else if (v.P_LoopMain[playerID] <= 8)
            if EUDElseIf()(v.P_LoopMain[playerID] <= 8):
                # (Line 33) {
                # (Line 34) trg.Shape_Edge(playerID,1,"60 + 1n Siege",0,4+x,96+(x*64));
                trg.Shape_Edge(playerID, 1, "60 + 1n Siege", 0, 4 + x, 96 + (x * 64))
                # (Line 35) trg.Shape_Edge(playerID,1,"60 + 1n Siege",45,4+x,96+(x*64));
                trg.Shape_Edge(playerID, 1, "60 + 1n Siege", 45, 4 + x, 96 + (x * 64))
                # (Line 36) trg.Shape_Edge(playerID,1,"40 + 1n Gantrithor",0,4+x,96+(x*64));
                trg.Shape_Edge(playerID, 1, "40 + 1n Gantrithor", 0, 4 + x, 96 + (x * 64))
                # (Line 37) trg.Shape_Edge(playerID,1,"40 + 1n Gantrithor",45,4+x,96+(x*64));
                trg.Shape_Edge(playerID, 1, "40 + 1n Gantrithor", 45, 4 + x, 96 + (x * 64))
                # (Line 38) trg.Shape_Dot(playerID,1,"40 + 1n Gantrithor",0,0);
                trg.Shape_Dot(playerID, 1, "40 + 1n Gantrithor", 0, 0)
                # (Line 39) trg.MoveLoc(v.P_UnitID[playerID],playerID,0,0);
                trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0)
                # (Line 40) Order("60 + 1n Siege",playerID,"Anywhere",Attack,v.P_LocationID[playerID]);
                # (Line 41) KillUnitAt(All,"40 + 1n Gantrithor","Anywhere",playerID);
                DoActions(Order("60 + 1n Siege", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                # (Line 42) trg.Main_Wait(100);
                DoActions(KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", playerID))
                trg.Main_Wait(100)
                # (Line 43) x += 1;
                x.__iadd__(1)
                # (Line 44) }
                # (Line 45) else if(v.P_LoopMain[playerID] == 9)
            if EUDElseIf()(v.P_LoopMain[playerID] == 9):
                # (Line 46) {
                # (Line 47) trg.Main_Wait(5100);
                trg.Main_Wait(5100)
                # (Line 48) }
                # (Line 49) else if(v.P_LoopMain[playerID] == 10)
            if EUDElseIf()(v.P_LoopMain[playerID] == 10):
                # (Line 50) {
                # (Line 51) x = 0;
                x << (0)
                # (Line 52) KillUnitAt(All,"60 + 1n Siege","Anywhere",playerID);
                # (Line 53) trg.Main_Wait(0);
                DoActions(KillUnitAt(All, "60 + 1n Siege", "Anywhere", playerID))
                trg.Main_Wait(0)
                # (Line 54) }
                # (Line 55) else if(v.P_LoopMain[playerID] <= 21)
            if EUDElseIf()(v.P_LoopMain[playerID] <= 21):
                # (Line 56) {
                # (Line 58) trg.Table_Sin(playerID, 18 * x, 48 * (x + 1));
                trg.Table_Sin(playerID, 18 * x, 48 * (x + 1))
                # (Line 59) trg.Table_Cos(playerID, 18 * x, 48 * (x + 1));
                trg.Table_Cos(playerID, 18 * x, 48 * (x + 1))
                # (Line 60) trg.Shape_Square(playerID,1,"40 + 1n Wraith",v.P_AngleCos[playerID],v.P_AngleSin[playerID]);
                trg.Shape_Square(playerID, 1, "40 + 1n Wraith", v.P_AngleCos[playerID], v.P_AngleSin[playerID])
                # (Line 61) trg.Shape_Square(playerID,1,"Protoss Observer",v.P_AngleCos[playerID],v.P_AngleSin[playerID]);
                trg.Shape_Square(playerID, 1, "Protoss Observer", v.P_AngleCos[playerID], v.P_AngleSin[playerID])
                # (Line 63) trg.Table_Sin(playerID, 2 + 18 * x, 48 * (x + 1));
                trg.Table_Sin(playerID, 2 + 18 * x, 48 * (x + 1))
                # (Line 64) trg.Table_Cos(playerID, 2 + 18 * x, 48 * (x + 1));
                trg.Table_Cos(playerID, 2 + 18 * x, 48 * (x + 1))
                # (Line 65) trg.Shape_Square(playerID,1,"60 + 1n Siege",v.P_AngleCos[playerID],v.P_AngleSin[playerID]);
                trg.Shape_Square(playerID, 1, "60 + 1n Siege", v.P_AngleCos[playerID], v.P_AngleSin[playerID])
                # (Line 66) trg.Shape_Square(playerID,1,"Protoss Observer",v.P_AngleCos[playerID],v.P_AngleSin[playerID]);
                trg.Shape_Square(playerID, 1, "Protoss Observer", v.P_AngleCos[playerID], v.P_AngleSin[playerID])
                # (Line 68) trg.Table_Sin(playerID, 4 + 18 * x, 48 * (x + 1));
                trg.Table_Sin(playerID, 4 + 18 * x, 48 * (x + 1))
                # (Line 69) trg.Table_Cos(playerID, 4 + 18 * x, 48 * (x + 1));
                trg.Table_Cos(playerID, 4 + 18 * x, 48 * (x + 1))
                # (Line 70) trg.Shape_Square(playerID,1,"40 + 1n Mojo",v.P_AngleCos[playerID],v.P_AngleSin[playerID]);
                trg.Shape_Square(playerID, 1, "40 + 1n Mojo", v.P_AngleCos[playerID], v.P_AngleSin[playerID])
                # (Line 71) trg.Shape_Square(playerID,1,"Protoss Observer",v.P_AngleCos[playerID],v.P_AngleSin[playerID]);
                trg.Shape_Square(playerID, 1, "Protoss Observer", v.P_AngleCos[playerID], v.P_AngleSin[playerID])
                # (Line 73) trg.Table_Sin(playerID, 6 + 18 * x, 48 * (x + 1));
                trg.Table_Sin(playerID, 6 + 18 * x, 48 * (x + 1))
                # (Line 74) trg.Table_Cos(playerID, 6 + 18 * x, 48 * (x + 1));
                trg.Table_Cos(playerID, 6 + 18 * x, 48 * (x + 1))
                # (Line 75) trg.Shape_Square(playerID,1,"40 + 1n Wraith",v.P_AngleCos[playerID],v.P_AngleSin[playerID]);
                trg.Shape_Square(playerID, 1, "40 + 1n Wraith", v.P_AngleCos[playerID], v.P_AngleSin[playerID])
                # (Line 76) trg.Shape_Square(playerID,1,"Protoss Observer",v.P_AngleCos[playerID],v.P_AngleSin[playerID]);
                trg.Shape_Square(playerID, 1, "Protoss Observer", v.P_AngleCos[playerID], v.P_AngleSin[playerID])
                # (Line 78) trg.Table_Sin(playerID, 8 + 18 * x, 48 * (x + 1));
                trg.Table_Sin(playerID, 8 + 18 * x, 48 * (x + 1))
                # (Line 79) trg.Table_Cos(playerID, 8 + 18 * x, 48 * (x + 1));
                trg.Table_Cos(playerID, 8 + 18 * x, 48 * (x + 1))
                # (Line 80) trg.Shape_Square(playerID,1,"60 + 3n Siege",v.P_AngleCos[playerID],v.P_AngleSin[playerID]);
                trg.Shape_Square(playerID, 1, "60 + 3n Siege", v.P_AngleCos[playerID], v.P_AngleSin[playerID])
                # (Line 81) trg.Shape_Square(playerID,1,"Protoss Observer",v.P_AngleCos[playerID],v.P_AngleSin[playerID]);
                trg.Shape_Square(playerID, 1, "Protoss Observer", v.P_AngleCos[playerID], v.P_AngleSin[playerID])
                # (Line 83) trg.Table_Sin(playerID, 10 + 18 * x, 48 * (x + 1));
                trg.Table_Sin(playerID, 10 + 18 * x, 48 * (x + 1))
                # (Line 84) trg.Table_Cos(playerID, 10 + 18 * x, 48 * (x + 1));
                trg.Table_Cos(playerID, 10 + 18 * x, 48 * (x + 1))
                # (Line 85) trg.Shape_Square(playerID,1,"40 + 1n Mojo",v.P_AngleCos[playerID],v.P_AngleSin[playerID]);
                trg.Shape_Square(playerID, 1, "40 + 1n Mojo", v.P_AngleCos[playerID], v.P_AngleSin[playerID])
                # (Line 86) trg.Shape_Square(playerID,1,"Protoss Observer",v.P_AngleCos[playerID],v.P_AngleSin[playerID]);
                trg.Shape_Square(playerID, 1, "Protoss Observer", v.P_AngleCos[playerID], v.P_AngleSin[playerID])
                # (Line 88) trg.Table_Sin(playerID, 12 + 18 * x, 48 * (x + 1));
                trg.Table_Sin(playerID, 12 + 18 * x, 48 * (x + 1))
                # (Line 89) trg.Table_Cos(playerID, 12 + 18 * x, 48 * (x + 1));
                trg.Table_Cos(playerID, 12 + 18 * x, 48 * (x + 1))
                # (Line 90) trg.Shape_Square(playerID,1,"40 + 1n Wraith",v.P_AngleCos[playerID],v.P_AngleSin[playerID]);
                trg.Shape_Square(playerID, 1, "40 + 1n Wraith", v.P_AngleCos[playerID], v.P_AngleSin[playerID])
                # (Line 91) trg.Shape_Square(playerID,1,"Protoss Observer",v.P_AngleCos[playerID],v.P_AngleSin[playerID]);
                trg.Shape_Square(playerID, 1, "Protoss Observer", v.P_AngleCos[playerID], v.P_AngleSin[playerID])
                # (Line 93) trg.Table_Sin(playerID, 14 + 18 * x, 48 * (x + 1));
                trg.Table_Sin(playerID, 14 + 18 * x, 48 * (x + 1))
                # (Line 94) trg.Table_Cos(playerID, 14 + 18 * x, 48 * (x + 1));
                trg.Table_Cos(playerID, 14 + 18 * x, 48 * (x + 1))
                # (Line 95) trg.Shape_Square(playerID,1,"60 + 1n Siege",v.P_AngleCos[playerID],v.P_AngleSin[playerID]);
                trg.Shape_Square(playerID, 1, "60 + 1n Siege", v.P_AngleCos[playerID], v.P_AngleSin[playerID])
                # (Line 96) trg.Shape_Square(playerID,1,"Protoss Observer",v.P_AngleCos[playerID],v.P_AngleSin[playerID]);
                trg.Shape_Square(playerID, 1, "Protoss Observer", v.P_AngleCos[playerID], v.P_AngleSin[playerID])
                # (Line 98) trg.Table_Sin(playerID, 16 + 18 * x, 48 * (x + 1));
                trg.Table_Sin(playerID, 16 + 18 * x, 48 * (x + 1))
                # (Line 99) trg.Table_Cos(playerID, 16 + 18 * x, 48 * (x + 1));
                trg.Table_Cos(playerID, 16 + 18 * x, 48 * (x + 1))
                # (Line 100) trg.Shape_Square(playerID,1,"40 + 1n Mojo",v.P_AngleCos[playerID],v.P_AngleSin[playerID]);
                trg.Shape_Square(playerID, 1, "40 + 1n Mojo", v.P_AngleCos[playerID], v.P_AngleSin[playerID])
                # (Line 101) trg.Shape_Square(playerID,1,"Protoss Observer",v.P_AngleCos[playerID],v.P_AngleSin[playerID]);
                trg.Shape_Square(playerID, 1, "Protoss Observer", v.P_AngleCos[playerID], v.P_AngleSin[playerID])
                # (Line 103) KillUnitAt(All,"Protoss Observer","Anywhere",playerID);
                # (Line 104) trg.MoveLoc(v.P_UnitID[playerID],playerID,0,0);
                DoActions(KillUnitAt(All, "Protoss Observer", "Anywhere", playerID))
                trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0)
                # (Line 105) Order("40 + 1n Wraith",playerID,"Anywhere",Attack,v.P_LocationID[playerID]);
                # (Line 106) Order("40 + 1n Mojo",playerID,"Anywhere",Attack,v.P_LocationID[playerID]);
                DoActions(Order("40 + 1n Wraith", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                # (Line 107) trg.Main_Wait(100);
                DoActions(Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                trg.Main_Wait(100)
                # (Line 108) x += 1;
                x.__iadd__(1)
                # (Line 109) }
                # (Line 110) else if(v.P_LoopMain[playerID] == 22)
            if EUDElseIf()(v.P_LoopMain[playerID] == 22):
                # (Line 111) {
                # (Line 112) x = 0;
                x << (0)
                # (Line 113) trg.Main_Wait(3600);
                trg.Main_Wait(3600)
                # (Line 114) }
                # (Line 115) else if(v.P_LoopMain[playerID] == 23)
            if EUDElseIf()(v.P_LoopMain[playerID] == 23):
                # (Line 116) {
                # (Line 117) trg.Shape_NxNSquare(playerID,1,"130 + 1n Norad",6,96);
                trg.Shape_NxNSquare(playerID, 1, "130 + 1n Norad", 6, 96)
                # (Line 118) trg.MoveLoc(v.P_UnitID[playerID],playerID,0,0);
                trg.MoveLoc(v.P_UnitID[playerID], playerID, 0, 0)
                # (Line 119) Order("130 + 1n Norad",playerID,"Anywhere",Attack,v.P_LocationID[playerID]);
                # (Line 120) trg.Main_Wait(2000);
                DoActions(Order("130 + 1n Norad", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                trg.Main_Wait(2000)
                # (Line 121) }
                # (Line 122) else if(v.P_LoopMain[playerID] == 24)
            if EUDElseIf()(v.P_LoopMain[playerID] == 24):
                # (Line 123) {
                # (Line 124) KillUnitAt(All,"60 + 3n Siege","Anywhere",playerID);
                # (Line 125) KillUnitAt(All,"60 + 1n Siege","Anywhere",playerID);
                DoActions(KillUnitAt(All, "60 + 3n Siege", "Anywhere", playerID))
                # (Line 126) KillUnitAt(All,"40 + 1n Wraith","Anywhere",playerID);
                DoActions(KillUnitAt(All, "60 + 1n Siege", "Anywhere", playerID))
                # (Line 127) KillUnitAt(All,"40 + 1n Mojo","Anywhere",playerID);
                DoActions(KillUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID))
                # (Line 128) KillUnitAt(All,"130 + 1n Norad","Anywhere",playerID);
                DoActions(KillUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID))
                # (Line 129) SetSwitch("UiltimateSwitch", Clear);
                DoActions(KillUnitAt(All, "130 + 1n Norad", "Anywhere", playerID))
                # (Line 130) SetSwitch("Recall - MaiHime",Clear);
                DoActions(SetSwitch("UiltimateSwitch", Clear))
                # (Line 131) trg.SkillEnd();
                DoActions(SetSwitch("Recall - MaiHime", Clear))
                trg.SkillEnd()
                # (Line 132) }
                # (Line 133) v.P_LoopMain[playerID] += 1;
            EUDEndIf()
            _ARRW(v.P_LoopMain, playerID).__iadd__(1)
            # (Line 134) }
            # (Line 135) }
        EUDEndIf()
        # (Line 136) }
    EUDEndIf()