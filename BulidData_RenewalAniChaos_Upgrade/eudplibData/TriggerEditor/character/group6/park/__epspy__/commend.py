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
    # (Line 8) if (v.P_SkillDelay[playerID] == 0 && v.P_Step[playerID] == 0)
    if EUDIf()(EUDSCAnd()(v.P_SkillDelay[playerID] == 0)(v.P_Step[playerID] == 0)()):
        # (Line 9) {
        # (Line 10) if (Bring(playerID, AtLeast, 1, "Protoss Corsair", "[Skill]UseSkill")
        _t2 = EUDIf()
        # (Line 11) && Deaths(CurrentPlayer, AtLeast, 1, " `O Skill Condition")
        # (Line 12) && Deaths(CurrentPlayer, Exactly, 0, " `UniqueCoolTime"))
        if _t2(EUDSCAnd()(Bring(playerID, AtLeast, 1, "Protoss Corsair", "[Skill]UseSkill"))(Deaths(CurrentPlayer, AtLeast, 1, " `O Skill Condition"))(Deaths(CurrentPlayer, Exactly, 0, " `UniqueCoolTime"))()):
            # (Line 13) {
            # (Line 14) s.CharacterVoice(9);
            s.CharacterVoice(9)
            # (Line 16) v.P_Step[playerID] = 1;
            _ARRW(v.P_Step, playerID) << (1)
            # (Line 17) KillUnitAt(1, "Protoss Corsair", "[Skill]UseSkill", playerID);
            # (Line 18) }
            DoActions(KillUnitAt(1, "Protoss Corsair", "[Skill]UseSkill", playerID))
            # (Line 19) else if (Bring(playerID, AtLeast, 1, "Protoss Corsair", "[Skill]UseSkill"))
        if EUDElseIf()(Bring(playerID, AtLeast, 1, "Protoss Corsair", "[Skill]UseSkill")):
            # (Line 20) {
            # (Line 21) SetResources(CurrentPlayer, Add, 60, Gas);
            # (Line 22) KillUnitAt(1, "Protoss Corsair", "[Skill]UseSkill", playerID);
            DoActions(SetResources(CurrentPlayer, Add, 60, Gas))
            # (Line 23) }
            DoActions(KillUnitAt(1, "Protoss Corsair", "[Skill]UseSkill", playerID))
            # (Line 24) else if (Bring(playerID, AtLeast, 1, "Protoss Arbiter", "[Skill]UseSkill"))
        if EUDElseIf()(Bring(playerID, AtLeast, 1, "Protoss Arbiter", "[Skill]UseSkill")):
            # (Line 25) {
            # (Line 26) v.P_Step[playerID] = 300;
            _ARRW(v.P_Step, playerID) << (300)
            # (Line 27) KillUnitAt(1, "Protoss Arbiter", "[Skill]UseSkill", playerID);
            # (Line 28) }
            DoActions(KillUnitAt(1, "Protoss Arbiter", "[Skill]UseSkill", playerID))
            # (Line 29) else if (Bring(playerID, AtLeast, 1, "Protoss Carrier", "[Skill]UseSkill"))
        if EUDElseIf()(Bring(playerID, AtLeast, 1, "Protoss Carrier", "[Skill]UseSkill")):
            # (Line 30) {
            # (Line 31) v.P_Step[playerID] = 200;
            _ARRW(v.P_Step, playerID) << (200)
            # (Line 32) KillUnitAt(1, "Protoss Carrier", "[Skill]UseSkill", playerID);
            # (Line 33) }
            DoActions(KillUnitAt(1, "Protoss Carrier", "[Skill]UseSkill", playerID))
            # (Line 34) else if (Bring(playerID, AtLeast, 1, "Protoss Scout", "[Skill]UseSkill"))
        if EUDElseIf()(Bring(playerID, AtLeast, 1, "Protoss Scout", "[Skill]UseSkill")):
            # (Line 35) {
            # (Line 36) v.P_Step[playerID] = 100;
            _ARRW(v.P_Step, playerID) << (100)
            # (Line 37) KillUnitAt(1, "Protoss Scout", "[Skill]UseSkill", playerID);
            # (Line 38) }
            DoActions(KillUnitAt(1, "Protoss Scout", "[Skill]UseSkill", playerID))
            # (Line 40) }
        EUDEndIf()
        # (Line 43) if (v.P_SkillDelay[playerID] >= 2 && v.P_CountMain[playerID] == 0)
    EUDEndIf()
    if EUDIf()(EUDSCAnd()(v.P_SkillDelay[playerID] >= 2)(v.P_CountMain[playerID] == 0)()):
        # (Line 44) {
        # (Line 45) if (Bring(playerID, AtLeast, 2, "Protoss Scout", "[Skill]UseSkill") && v.P_Step[playerID] == 100)
        if EUDIf()(EUDSCAnd()(Bring(playerID, AtLeast, 2, "Protoss Scout", "[Skill]UseSkill"))(v.P_Step[playerID] == 100)()):
            # (Line 46) {
            # (Line 47) s.CharacterVoice(4);
            s.CharacterVoice(4)
            # (Line 48) v.P_SkillDelay[playerID] = 0;
            _ARRW(v.P_SkillDelay, playerID) << (0)
            # (Line 49) v.P_CountMain[playerID] = 0;
            _ARRW(v.P_CountMain, playerID) << (0)
            # (Line 50) v.P_LoopMain[playerID] = 0;
            _ARRW(v.P_LoopMain, playerID) << (0)
            # (Line 51) v.P_Step[playerID] = 110;
            _ARRW(v.P_Step, playerID) << (110)
            # (Line 52) KillUnitAt(2, "Protoss Scout", "[Skill]UseSkill", playerID);
            # (Line 53) }
            DoActions(KillUnitAt(2, "Protoss Scout", "[Skill]UseSkill", playerID))
            # (Line 54) else if (Bring(playerID, AtLeast, 2, "Protoss Carrier", "[Skill]UseSkill") && v.P_Step[playerID] == 200)
        if EUDElseIf()(EUDSCAnd()(Bring(playerID, AtLeast, 2, "Protoss Carrier", "[Skill]UseSkill"))(v.P_Step[playerID] == 200)()):
            # (Line 55) {
            # (Line 56) s.CharacterVoice(6);
            s.CharacterVoice(6)
            # (Line 57) v.P_SkillDelay[playerID] = 0;
            _ARRW(v.P_SkillDelay, playerID) << (0)
            # (Line 58) v.P_CountMain[playerID] = 0;
            _ARRW(v.P_CountMain, playerID) << (0)
            # (Line 59) v.P_LoopMain[playerID] = 0;
            _ARRW(v.P_LoopMain, playerID) << (0)
            # (Line 60) v.P_Step[playerID] = 210;
            _ARRW(v.P_Step, playerID) << (210)
            # (Line 61) KillUnitAt(2, "Protoss Carrier", "[Skill]UseSkill", playerID);
            # (Line 62) }
            DoActions(KillUnitAt(2, "Protoss Carrier", "[Skill]UseSkill", playerID))
            # (Line 63) else if (Bring(playerID, AtLeast, 1, "Protoss Carrier", "[Skill]UseSkill") && v.P_Step[playerID] == 210
        _t10 = EUDElseIf()
        # (Line 64) && Bring(playerID, AtLeast, 1, "Protoss Arbiter", "[Skill]UseSkill"))
        if _t10(EUDSCAnd()(Bring(playerID, AtLeast, 1, "Protoss Carrier", "[Skill]UseSkill"))(v.P_Step[playerID] == 210)(Bring(playerID, AtLeast, 1, "Protoss Arbiter", "[Skill]UseSkill"))()):
            # (Line 65) {
            # (Line 66) s.CharacterVoice(7);
            s.CharacterVoice(7)
            # (Line 67) v.P_SkillDelay[playerID] = 0;
            _ARRW(v.P_SkillDelay, playerID) << (0)
            # (Line 68) v.P_CountMain[playerID] = 0;
            _ARRW(v.P_CountMain, playerID) << (0)
            # (Line 69) v.P_LoopMain[playerID] = 0;
            _ARRW(v.P_LoopMain, playerID) << (0)
            # (Line 70) v.P_Step[playerID] = 220;
            _ARRW(v.P_Step, playerID) << (220)
            # (Line 71) KillUnitAt(1, "Protoss Carrier", "[Skill]UseSkill", playerID);
            # (Line 72) KillUnitAt(1, "Protoss Arbiter", "[Skill]UseSkill", playerID);
            DoActions(KillUnitAt(1, "Protoss Carrier", "[Skill]UseSkill", playerID))
            # (Line 73) }
            DoActions(KillUnitAt(1, "Protoss Arbiter", "[Skill]UseSkill", playerID))
            # (Line 74) else if (Bring(playerID, AtLeast, 2, "Protoss Carrier", "[Skill]UseSkill") && v.P_Step[playerID] == 220)
        if EUDElseIf()(EUDSCAnd()(Bring(playerID, AtLeast, 2, "Protoss Carrier", "[Skill]UseSkill"))(v.P_Step[playerID] == 220)()):
            # (Line 75) {
            # (Line 76) s.CharacterVoice(8);
            s.CharacterVoice(8)
            # (Line 77) v.P_SkillDelay[playerID] = 0;
            _ARRW(v.P_SkillDelay, playerID) << (0)
            # (Line 78) v.P_CountMain[playerID] = 0;
            _ARRW(v.P_CountMain, playerID) << (0)
            # (Line 79) v.P_LoopMain[playerID] = 0;
            _ARRW(v.P_LoopMain, playerID) << (0)
            # (Line 80) v.P_Step[playerID] = 230;
            _ARRW(v.P_Step, playerID) << (230)
            # (Line 81) KillUnitAt(2, "Protoss Carrier", "[Skill]UseSkill", playerID);
            # (Line 82) }
            DoActions(KillUnitAt(2, "Protoss Carrier", "[Skill]UseSkill", playerID))
            # (Line 83) else if (Bring(playerID, AtLeast, 1, "Protoss Carrier", "[Skill]UseSkill") && v.P_Step[playerID] == 300
        _t12 = EUDElseIf()
        # (Line 84) && Bring(playerID, AtLeast, 1, "Protoss Arbiter", "[Skill]UseSkill"))
        if _t12(EUDSCAnd()(Bring(playerID, AtLeast, 1, "Protoss Carrier", "[Skill]UseSkill"))(v.P_Step[playerID] == 300)(Bring(playerID, AtLeast, 1, "Protoss Arbiter", "[Skill]UseSkill"))()):
            # (Line 85) {
            # (Line 86) s.CharacterVoice(5);
            s.CharacterVoice(5)
            # (Line 87) v.P_SkillDelay[playerID] = 0;
            _ARRW(v.P_SkillDelay, playerID) << (0)
            # (Line 88) v.P_CountMain[playerID] = 0;
            _ARRW(v.P_CountMain, playerID) << (0)
            # (Line 89) v.P_LoopMain[playerID] = 0;
            _ARRW(v.P_LoopMain, playerID) << (0)
            # (Line 90) v.P_Step[playerID] = 310;
            _ARRW(v.P_Step, playerID) << (310)
            # (Line 91) KillUnitAt(1, "Protoss Carrier", "[Skill]UseSkill", playerID);
            # (Line 92) KillUnitAt(1, "Protoss Arbiter", "[Skill]UseSkill", playerID);
            DoActions(KillUnitAt(1, "Protoss Carrier", "[Skill]UseSkill", playerID))
            # (Line 93) }
            DoActions(KillUnitAt(1, "Protoss Arbiter", "[Skill]UseSkill", playerID))
            # (Line 97) else if (Bring(playerID, AtLeast, 2, "Protoss Arbiter", "[Skill]UseSkill")
        _t13 = EUDElseIf()
        # (Line 98) && v.P_Step[playerID] == 300
        # (Line 99) && v.P_UltimateGauge[playerID] >= v.P_Ultimate1[playerID])
        if _t13(EUDSCAnd()(Bring(playerID, AtLeast, 2, "Protoss Arbiter", "[Skill]UseSkill"))(v.P_Step[playerID] == 300)(v.P_UltimateGauge[playerID] >= v.P_Ultimate1[playerID])()):
            # (Line 100) {
            # (Line 101) s.CharacterVoice(1);
            s.CharacterVoice(1)
            # (Line 102) v.P_SkillDelay[playerID] = 0;
            _ARRW(v.P_SkillDelay, playerID) << (0)
            # (Line 103) v.P_Step[playerID] = 320;
            _ARRW(v.P_Step, playerID) << (320)
            # (Line 104) SetDeaths(playerID, Subtract, v.P_Ultimate1[playerID], " `UltimateCoolTime");
            # (Line 105) KillUnitAt(2, "Protoss Arbiter", "[Skill]UseSkill", playerID);
            DoActions(SetDeaths(playerID, Subtract, v.P_Ultimate1[playerID], " `UltimateCoolTime"))
            # (Line 106) }
            DoActions(KillUnitAt(2, "Protoss Arbiter", "[Skill]UseSkill", playerID))
            # (Line 108) else if (Bring(playerID, AtLeast, 2, "Protoss Arbiter", "[Skill]UseSkill")
        _t14 = EUDElseIf()
        # (Line 109) && v.P_Step[playerID] == 320
        # (Line 110) && v.P_UltimateGauge[playerID] >= v.P_Ultimate2[playerID])
        if _t14(EUDSCAnd()(Bring(playerID, AtLeast, 2, "Protoss Arbiter", "[Skill]UseSkill"))(v.P_Step[playerID] == 320)(v.P_UltimateGauge[playerID] >= v.P_Ultimate2[playerID])()):
            # (Line 111) {
            # (Line 112) if (Switch("UiltimateSwitch", Cleared))
            if EUDIf()(Switch("UiltimateSwitch", Cleared)):
                # (Line 113) {
                # (Line 114) SetSwitch("UiltimateSwitch", Set);
                # (Line 115) CreateUnit(1, " Item. Flag", "[Uiltimate]Flag", CurrentPlayer);
                DoActions(SetSwitch("UiltimateSwitch", Set))
                # (Line 116) s.CharacterVoice(3);
                DoActions(CreateUnit(1, " Item. Flag", "[Uiltimate]Flag", CurrentPlayer))
                s.CharacterVoice(3)
                # (Line 117) v.P_SkillDelay[playerID] = 0;
                _ARRW(v.P_SkillDelay, playerID) << (0)
                # (Line 118) v.P_Step[playerID] = 330;
                _ARRW(v.P_Step, playerID) << (330)
                # (Line 119) SetDeaths(playerID, Subtract, v.P_Ultimate2[playerID], " `UltimateCoolTime");
                # (Line 120) KillUnitAt(2, "Protoss Arbiter", "[Skill]UseSkill", playerID);
                DoActions(SetDeaths(playerID, Subtract, v.P_Ultimate2[playerID], " `UltimateCoolTime"))
                # (Line 121) }
                DoActions(KillUnitAt(2, "Protoss Arbiter", "[Skill]UseSkill", playerID))
                # (Line 123) else
                # (Line 124) {
            if EUDElse()():
                # (Line 125) SetResources(CurrentPlayer, Add, 900, Gas);
                # (Line 126) KillUnitAt(3, "Protoss Arbiter", "[Skill]UseSkill", playerID);
                DoActions(SetResources(CurrentPlayer, Add, 900, Gas))
                # (Line 127) SetDeaths(CurrentPlayer, SetTo, 999, " `SYSTEMTEXT");
                DoActions(KillUnitAt(3, "Protoss Arbiter", "[Skill]UseSkill", playerID))
                # (Line 128) }
                DoActions(SetDeaths(CurrentPlayer, SetTo, 999, " `SYSTEMTEXT"))
                # (Line 129) }
            EUDEndIf()
            # (Line 130) }
        EUDEndIf()
        # (Line 131) }
    EUDEndIf()