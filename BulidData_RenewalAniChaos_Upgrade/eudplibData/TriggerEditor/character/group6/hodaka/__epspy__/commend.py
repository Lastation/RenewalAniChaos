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
# (Line 4) import func.sound as s;
from func import sound as s
# (Line 5) import func.trig as trg;
from func import trig as trg
# (Line 7) function main(playerID)
# (Line 8) {
@EUDFunc
def f_main(playerID):
    # (Line 9) if (v.P_WaitMain[playerID] == 0 && v.P_Step[playerID] == 0)
    if EUDIf()(EUDSCAnd()(v.P_WaitMain[playerID] == 0)(v.P_Step[playerID] == 0)()):
        # (Line 10) {
        # (Line 11) if (Bring(playerID, AtLeast, 1, "Protoss Corsair", "[Skill]UseSkill")
        _t2 = EUDIf()
        # (Line 12) && Deaths(CurrentPlayer, AtLeast, 1, " `O Skill Condition")
        # (Line 13) && Deaths(CurrentPlayer, Exactly, 0, " `UniqueCoolTime"))
        if _t2(EUDSCAnd()(Bring(playerID, AtLeast, 1, "Protoss Corsair", "[Skill]UseSkill"))(Deaths(CurrentPlayer, AtLeast, 1, " `O Skill Condition"))(Deaths(CurrentPlayer, Exactly, 0, " `UniqueCoolTime"))()):
            # (Line 14) {
            # (Line 15) s.CharacterVoice(1);
            s.CharacterVoice(1)
            # (Line 16) v.P_Step[playerID] = 1;
            _ARRW(v.P_Step, playerID) << (1)
            # (Line 17) KillUnitAt(1, "Protoss Corsair", "[Skill]UseSkill", playerID);
            # (Line 18) }
            DoActions(KillUnitAt(1, "Protoss Corsair", "[Skill]UseSkill", playerID))
            # (Line 19) else if (Bring(playerID, AtLeast, 1, "Protoss Corsair", "[Skill]UseSkill"))
        if EUDElseIf()(Bring(playerID, AtLeast, 1, "Protoss Corsair", "[Skill]UseSkill")):
            # (Line 20) {
            # (Line 21) KillUnitAt(1, "Protoss Corsair", "[Skill]UseSkill", playerID);
            # (Line 22) SetResources(playerID, Add, 60, Gas);
            DoActions(KillUnitAt(1, "Protoss Corsair", "[Skill]UseSkill", playerID))
            # (Line 23) }
            DoActions(SetResources(playerID, Add, 60, Gas))
            # (Line 24) else if (Bring(playerID, AtLeast, 1, "Protoss Scout", "[Skill]UseSkill"))
        if EUDElseIf()(Bring(playerID, AtLeast, 1, "Protoss Scout", "[Skill]UseSkill")):
            # (Line 25) {
            # (Line 26) v.P_Step[playerID] = 100;
            _ARRW(v.P_Step, playerID) << (100)
            # (Line 27) KillUnitAt(1, "Protoss Scout", "[Skill]UseSkill", playerID);
            # (Line 28) }
            DoActions(KillUnitAt(1, "Protoss Scout", "[Skill]UseSkill", playerID))
            # (Line 29) else if (Bring(playerID, AtLeast, 1, "Protoss Arbiter", "[Skill]UseSkill"))
        if EUDElseIf()(Bring(playerID, AtLeast, 1, "Protoss Arbiter", "[Skill]UseSkill")):
            # (Line 30) {
            # (Line 31) v.P_Step[playerID] = 300;
            _ARRW(v.P_Step, playerID) << (300)
            # (Line 32) KillUnitAt(1, "Protoss Arbiter", "[Skill]UseSkill", playerID);
            # (Line 33) }
            DoActions(KillUnitAt(1, "Protoss Arbiter", "[Skill]UseSkill", playerID))
            # (Line 34) else if (Bring(playerID, AtLeast, 1, "Protoss Carrier", "[Skill]UseSkill"))
        if EUDElseIf()(Bring(playerID, AtLeast, 1, "Protoss Carrier", "[Skill]UseSkill")):
            # (Line 35) {
            # (Line 36) v.P_Step[playerID] = 200;
            _ARRW(v.P_Step, playerID) << (200)
            # (Line 37) KillUnitAt(1, "Protoss Carrier", "[Skill]UseSkill", playerID);
            # (Line 38) }
            DoActions(KillUnitAt(1, "Protoss Carrier", "[Skill]UseSkill", playerID))
            # (Line 39) }
        EUDEndIf()
        # (Line 42) if (v.P_SkillDelay[playerID] >= 2 && v.P_CountMain[playerID] == 0)
    EUDEndIf()
    if EUDIf()(EUDSCAnd()(v.P_SkillDelay[playerID] >= 2)(v.P_CountMain[playerID] == 0)()):
        # (Line 43) {
        # (Line 44) if (Bring(playerID, AtLeast, 2, "Protoss Scout", "[Skill]UseSkill")
        _t8 = EUDIf()
        # (Line 45) &&  v.P_Step[playerID] == 100)
        if _t8(EUDSCAnd()(Bring(playerID, AtLeast, 2, "Protoss Scout", "[Skill]UseSkill"))(v.P_Step[playerID] == 100)()):
            # (Line 46) {
            # (Line 47) s.CharacterVoice(2);
            s.CharacterVoice(2)
            # (Line 48) v.P_SkillDelay[playerID] = 0;
            _ARRW(v.P_SkillDelay, playerID) << (0)
            # (Line 49) v.P_Step[playerID] = 110;
            _ARRW(v.P_Step, playerID) << (110)
            # (Line 50) KillUnitAt(2, "Protoss Scout", "[Skill]UseSkill", playerID);
            # (Line 51) }
            DoActions(KillUnitAt(2, "Protoss Scout", "[Skill]UseSkill", playerID))
            # (Line 52) else if (Bring(playerID, AtLeast, 2, "Protoss Carrier", "[Skill]UseSkill")
        _t9 = EUDElseIf()
        # (Line 53) &&  v.P_Step[playerID] == 200)
        if _t9(EUDSCAnd()(Bring(playerID, AtLeast, 2, "Protoss Carrier", "[Skill]UseSkill"))(v.P_Step[playerID] == 200)()):
            # (Line 54) {
            # (Line 55) s.CharacterVoice(3);
            s.CharacterVoice(3)
            # (Line 56) v.P_SkillDelay[playerID] = 0;
            _ARRW(v.P_SkillDelay, playerID) << (0)
            # (Line 57) v.P_Step[playerID] = 210;
            _ARRW(v.P_Step, playerID) << (210)
            # (Line 58) KillUnitAt(2, "Protoss Carrier", "[Skill]UseSkill", playerID);
            # (Line 59) }
            DoActions(KillUnitAt(2, "Protoss Carrier", "[Skill]UseSkill", playerID))
            # (Line 60) else if (Bring(playerID, AtLeast, 1, "Protoss Arbiter", "[Skill]UseSkill")
        _t10 = EUDElseIf()
        # (Line 61) && Bring(playerID, AtLeast, 2, "Protoss Carrier", "[Skill]UseSkill")
        # (Line 62) && Accumulate(playerID, AtLeast, 200, Gas)
        # (Line 63) &&  v.P_Step[playerID] == 300)
        if _t10(EUDSCAnd()(Bring(playerID, AtLeast, 1, "Protoss Arbiter", "[Skill]UseSkill"))(Bring(playerID, AtLeast, 2, "Protoss Carrier", "[Skill]UseSkill"))(Accumulate(playerID, AtLeast, 200, Gas))(v.P_Step[playerID] == 300)()):
            # (Line 64) {
            # (Line 65) s.CharacterVoice(5);
            s.CharacterVoice(5)
            # (Line 66) v.P_Step[playerID] = 310;
            _ARRW(v.P_Step, playerID) << (310)
            # (Line 67) v.P_SkillDelay[playerID] = 0;
            _ARRW(v.P_SkillDelay, playerID) << (0)
            # (Line 68) SetResources(playerID, Subtract, 200, Gas);
            # (Line 69) KillUnitAt(1, "Protoss Arbiter", "[Skill]UseSkill", playerID);
            DoActions(SetResources(playerID, Subtract, 200, Gas))
            # (Line 70) KillUnitAt(2, "Protoss Carrier", "[Skill]UseSkill", playerID);
            DoActions(KillUnitAt(1, "Protoss Arbiter", "[Skill]UseSkill", playerID))
            # (Line 71) }
            DoActions(KillUnitAt(2, "Protoss Carrier", "[Skill]UseSkill", playerID))
            # (Line 74) else if (Bring(playerID, AtLeast, 3, "Protoss Arbiter", "[Skill]UseSkill")
        _t11 = EUDElseIf()
        # (Line 75) && v.P_UltimateGauge[playerID] >= v.P_Ultimate1[playerID]
        # (Line 76) && v.P_Step[playerID] == 300)
        if _t11(EUDSCAnd()(Bring(playerID, AtLeast, 3, "Protoss Arbiter", "[Skill]UseSkill"))(v.P_UltimateGauge[playerID] >= v.P_Ultimate1[playerID])(v.P_Step[playerID] == 300)()):
            # (Line 77) {
            # (Line 78) if (Switch("UiltimateSwitch", Cleared))
            if EUDIf()(Switch("UiltimateSwitch", Cleared)):
                # (Line 79) {
                # (Line 80) s.CharacterVoice(8);
                s.CharacterVoice(8)
                # (Line 81) v.P_Step[playerID] = 320;
                _ARRW(v.P_Step, playerID) << (320)
                # (Line 82) v.P_SkillDelay[playerID] = 0;
                _ARRW(v.P_SkillDelay, playerID) << (0)
                # (Line 83) SetDeaths(playerID, Subtract, v.P_Ultimate1[playerID], 205);
                # (Line 84) KillUnitAt(3, "Protoss Arbiter", "[Skill]UseSkill", playerID);
                DoActions(SetDeaths(playerID, Subtract, v.P_Ultimate1[playerID], 205))
                # (Line 85) SetSwitch("UiltimateSwitch", Set);
                DoActions(KillUnitAt(3, "Protoss Arbiter", "[Skill]UseSkill", playerID))
                # (Line 86) CreateUnit(1, " Item. Flag", "[Uiltimate]Flag", CurrentPlayer);
                DoActions(SetSwitch("UiltimateSwitch", Set))
                # (Line 87) }
                DoActions(CreateUnit(1, " Item. Flag", "[Uiltimate]Flag", CurrentPlayer))
                # (Line 89) else
                # (Line 90) {
            if EUDElse()():
                # (Line 91) SetResources(CurrentPlayer, Add, 900, Gas);
                # (Line 92) KillUnitAt(3, "Protoss Arbiter", "[Skill]UseSkill", playerID);
                DoActions(SetResources(CurrentPlayer, Add, 900, Gas))
                # (Line 93) SetDeaths(CurrentPlayer, SetTo, 999, " `SYSTEMTEXT");
                DoActions(KillUnitAt(3, "Protoss Arbiter", "[Skill]UseSkill", playerID))
                # (Line 94) }
                DoActions(SetDeaths(CurrentPlayer, SetTo, 999, " `SYSTEMTEXT"))
                # (Line 95) }
            EUDEndIf()
            # (Line 96) }
        EUDEndIf()
        # (Line 97) }
    EUDEndIf()
