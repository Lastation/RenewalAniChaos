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
# (Line 3) import func.sound as s;
from func import sound as s
# (Line 5) function main(playerID)
# (Line 6) {
@EUDFunc
def f_main(playerID):
    # (Line 7) if (v.P_WaitMain[playerID] == 0 && v.P_Step[playerID] == 0)
    if EUDIf()(EUDSCAnd()(v.P_WaitMain[playerID] == 0)(v.P_Step[playerID] == 0)()):
        # (Line 8) {
        # (Line 9) if (Bring(playerID, AtLeast, 1, "Protoss Corsair", "[Skill]UseSkill")
        _t2 = EUDIf()
        # (Line 10) && v.P_UniqueCool[playerID] == 0
        # (Line 11) && v.P_UniqueCondition[playerID] == 1
        # (Line 12) && Bring(AllPlayers, Exactly, 0, 130, "Anywhere"))
        if _t2(EUDSCAnd()(Bring(playerID, AtLeast, 1, "Protoss Corsair", "[Skill]UseSkill"))(v.P_UniqueCool[playerID] == 0)(v.P_UniqueCondition[playerID] == 1)(Bring(AllPlayers, Exactly, 0, 130, "Anywhere"))()):
            # (Line 13) {
            # (Line 14) v.P_Step[playerID] = 1;
            _ARRW(v.P_Step, playerID) << (1)
            # (Line 15) KillUnitAt(1, "Protoss Corsair", "[Skill]UseSkill", playerID);
            # (Line 16) }
            DoActions(KillUnitAt(1, "Protoss Corsair", "[Skill]UseSkill", playerID))
            # (Line 17) else if (Bring(playerID, AtLeast, 1, "Protoss Corsair", "[Skill]UseSkill"))
        if EUDElseIf()(Bring(playerID, AtLeast, 1, "Protoss Corsair", "[Skill]UseSkill")):
            # (Line 18) {
            # (Line 19) SetResources(CurrentPlayer, Add, 60, Gas);
            # (Line 20) KillUnitAt(1, "Protoss Corsair", "[Skill]UseSkill", playerID);
            DoActions(SetResources(CurrentPlayer, Add, 60, Gas))
            # (Line 21) }
            DoActions(KillUnitAt(1, "Protoss Corsair", "[Skill]UseSkill", playerID))
            # (Line 22) else if (Bring(playerID, AtLeast, 1, "Protoss Scout", "[Skill]UseSkill"))
        if EUDElseIf()(Bring(playerID, AtLeast, 1, "Protoss Scout", "[Skill]UseSkill")):
            # (Line 23) {
            # (Line 24) v.P_Step[playerID] = 100;
            _ARRW(v.P_Step, playerID) << (100)
            # (Line 25) KillUnitAt(1, "Protoss Scout", "[Skill]UseSkill", playerID);
            # (Line 26) }
            DoActions(KillUnitAt(1, "Protoss Scout", "[Skill]UseSkill", playerID))
            # (Line 27) else if (Bring(playerID, AtLeast, 1, "Protoss Carrier", "[Skill]UseSkill"))
        if EUDElseIf()(Bring(playerID, AtLeast, 1, "Protoss Carrier", "[Skill]UseSkill")):
            # (Line 28) {
            # (Line 29) v.P_Step[playerID] = 200;
            _ARRW(v.P_Step, playerID) << (200)
            # (Line 30) KillUnitAt(1, "Protoss Carrier", "[Skill]UseSkill", playerID);
            # (Line 31) }
            DoActions(KillUnitAt(1, "Protoss Carrier", "[Skill]UseSkill", playerID))
            # (Line 32) else if (Bring(playerID, AtLeast, 1, "Protoss Arbiter", "[Skill]UseSkill"))
        if EUDElseIf()(Bring(playerID, AtLeast, 1, "Protoss Arbiter", "[Skill]UseSkill")):
            # (Line 33) {
            # (Line 34) v.P_Step[playerID] = 300;
            _ARRW(v.P_Step, playerID) << (300)
            # (Line 35) KillUnitAt(1, "Protoss Arbiter", "[Skill]UseSkill", playerID);
            # (Line 36) }
            DoActions(KillUnitAt(1, "Protoss Arbiter", "[Skill]UseSkill", playerID))
            # (Line 37) }
        EUDEndIf()
        # (Line 40) if (v.P_SkillDelay[playerID] >= 2 && v.P_CountMain[playerID] == 0)
    EUDEndIf()
    if EUDIf()(EUDSCAnd()(v.P_SkillDelay[playerID] >= 2)(v.P_CountMain[playerID] == 0)()):
        # (Line 41) {
        # (Line 42) if (Bring(playerID, AtLeast, 2, "Protoss Scout", "[Skill]UseSkill") &&  v.P_Step[playerID] == 100)
        if EUDIf()(EUDSCAnd()(Bring(playerID, AtLeast, 2, "Protoss Scout", "[Skill]UseSkill"))(v.P_Step[playerID] == 100)()):
            # (Line 43) {
            # (Line 44) s.CharacterVoice(4);
            s.CharacterVoice(4)
            # (Line 45) v.P_SkillDelay[playerID] = 0;
            _ARRW(v.P_SkillDelay, playerID) << (0)
            # (Line 46) v.P_Step[playerID] = 110;
            _ARRW(v.P_Step, playerID) << (110)
            # (Line 47) KillUnitAt(2, "Protoss Scout", "[Skill]UseSkill", playerID);
            # (Line 48) }
            DoActions(KillUnitAt(2, "Protoss Scout", "[Skill]UseSkill", playerID))
            # (Line 49) else if (Bring(playerID, AtLeast, 2, "Protoss Carrier", "[Skill]UseSkill") &&  v.P_Step[playerID] == 200)
        if EUDElseIf()(EUDSCAnd()(Bring(playerID, AtLeast, 2, "Protoss Carrier", "[Skill]UseSkill"))(v.P_Step[playerID] == 200)()):
            # (Line 50) {
            # (Line 51) s.CharacterVoice(2);
            s.CharacterVoice(2)
            # (Line 52) v.P_SkillDelay[playerID] = 0;
            _ARRW(v.P_SkillDelay, playerID) << (0)
            # (Line 53) v.P_Step[playerID] = 210;
            _ARRW(v.P_Step, playerID) << (210)
            # (Line 54) KillUnitAt(2, "Protoss Carrier", "[Skill]UseSkill", playerID);
            # (Line 55) SetSwitch("Recall - Rusalka", Set);
            DoActions(KillUnitAt(2, "Protoss Carrier", "[Skill]UseSkill", playerID))
            # (Line 56) }
            DoActions(SetSwitch("Recall - Rusalka", Set))
            # (Line 57) else if (Bring(playerID, AtLeast, 2, "Protoss Arbiter", "[Skill]UseSkill") && v.P_Step[playerID] == 210)
        if EUDElseIf()(EUDSCAnd()(Bring(playerID, AtLeast, 2, "Protoss Arbiter", "[Skill]UseSkill"))(v.P_Step[playerID] == 210)()):
            # (Line 58) {
            # (Line 59) s.CharacterVoice(3);
            s.CharacterVoice(3)
            # (Line 60) v.P_SkillDelay[playerID] = 0;
            _ARRW(v.P_SkillDelay, playerID) << (0)
            # (Line 61) v.P_Step[playerID] = 220;
            _ARRW(v.P_Step, playerID) << (220)
            # (Line 62) KillUnitAt(2, "Protoss Arbiter", "[Skill]UseSkill", playerID);
            # (Line 63) SetSwitch("Recall - Rusalka", Set);
            DoActions(KillUnitAt(2, "Protoss Arbiter", "[Skill]UseSkill", playerID))
            # (Line 64) }
            DoActions(SetSwitch("Recall - Rusalka", Set))
            # (Line 65) else if (Bring(playerID, AtLeast, 2, "Protoss Carrier", "[Skill]UseSkill") &&  v.P_Step[playerID] == 300)
        if EUDElseIf()(EUDSCAnd()(Bring(playerID, AtLeast, 2, "Protoss Carrier", "[Skill]UseSkill"))(v.P_Step[playerID] == 300)()):
            # (Line 66) {
            # (Line 67) s.CharacterVoice(1);
            s.CharacterVoice(1)
            # (Line 68) v.P_Step[playerID] = 310;
            _ARRW(v.P_Step, playerID) << (310)
            # (Line 69) v.P_SkillDelay[playerID] = 0;
            _ARRW(v.P_SkillDelay, playerID) << (0)
            # (Line 70) KillUnitAt(2, "Protoss Carrier", "[Skill]UseSkill", playerID);
            # (Line 71) }
            DoActions(KillUnitAt(2, "Protoss Carrier", "[Skill]UseSkill", playerID))
            # (Line 74) else if (Bring(playerID, AtLeast, 2, "Protoss Arbiter", "[Skill]UseSkill")
        _t12 = EUDElseIf()
        # (Line 75) && Bring(playerID, AtLeast, 1, "Protoss Carrier", "[Skill]UseSkill")
        # (Line 76) && v.P_UltimateGauge[playerID] >= v.P_Ultimate1[playerID]
        # (Line 77) && v.P_Step[playerID] == 300)
        if _t12(EUDSCAnd()(Bring(playerID, AtLeast, 2, "Protoss Arbiter", "[Skill]UseSkill"))(Bring(playerID, AtLeast, 1, "Protoss Carrier", "[Skill]UseSkill"))(v.P_UltimateGauge[playerID] >= v.P_Ultimate1[playerID])(v.P_Step[playerID] == 300)()):
            # (Line 78) {
            # (Line 79) if (Switch("UiltimateSwitch", Cleared))
            if EUDIf()(Switch("UiltimateSwitch", Cleared)):
                # (Line 80) {
                # (Line 81) s.CharacterVoice(5);
                s.CharacterVoice(5)
                # (Line 82) SetSwitch("UiltimateSwitch", Set);
                # (Line 83) CreateUnit(1, " Item. Flag", "[Uiltimate]Flag", CurrentPlayer);
                DoActions(SetSwitch("UiltimateSwitch", Set))
                # (Line 84) v.P_Step[playerID] = 320;
                DoActions(CreateUnit(1, " Item. Flag", "[Uiltimate]Flag", CurrentPlayer))
                _ARRW(v.P_Step, playerID) << (320)
                # (Line 85) v.P_SkillDelay[playerID] = 0;
                _ARRW(v.P_SkillDelay, playerID) << (0)
                # (Line 86) v.P_UltimateGauge[playerID] -= v.P_Ultimate1[playerID];
                _ARRW(v.P_UltimateGauge, playerID).__isub__(v.P_Ultimate1[playerID])
                # (Line 87) KillUnitAt(2, "Protoss Arbiter", "[Skill]UseSkill", playerID);
                # (Line 88) KillUnitAt(1, "Protoss Carrier", "[Skill]UseSkill", playerID);
                DoActions(KillUnitAt(2, "Protoss Arbiter", "[Skill]UseSkill", playerID))
                # (Line 89) }
                DoActions(KillUnitAt(1, "Protoss Carrier", "[Skill]UseSkill", playerID))
                # (Line 90) else
                # (Line 91) {
            if EUDElse()():
                # (Line 92) SetResources(CurrentPlayer, Add, 800, Gas);
                # (Line 93) KillUnitAt(2, "Protoss Arbiter", "[Skill]UseSkill", playerID);
                DoActions(SetResources(CurrentPlayer, Add, 800, Gas))
                # (Line 94) KillUnitAt(1, "Protoss Carrier", "[Skill]UseSkill", playerID);
                DoActions(KillUnitAt(2, "Protoss Arbiter", "[Skill]UseSkill", playerID))
                # (Line 95) SetDeaths(CurrentPlayer, SetTo, 999, " `SYSTEMTEXT");
                DoActions(KillUnitAt(1, "Protoss Carrier", "[Skill]UseSkill", playerID))
                # (Line 96) }
                DoActions(SetDeaths(CurrentPlayer, SetTo, 999, " `SYSTEMTEXT"))
                # (Line 97) }
            EUDEndIf()
            # (Line 98) }
        EUDEndIf()
        # (Line 99) }
    EUDEndIf()
