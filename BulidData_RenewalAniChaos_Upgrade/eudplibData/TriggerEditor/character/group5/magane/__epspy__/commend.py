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
        # (Line 12) && Deaths(CurrentPlayer, Exactly, 0, " `UniqueCoolTime")
        # (Line 13) && Switch("UiltimateSwitch", Cleared)
        # (Line 14) )
        if _t2(EUDSCAnd()(Bring(playerID, AtLeast, 1, "Protoss Corsair", "[Skill]UseSkill"))(Deaths(CurrentPlayer, AtLeast, 1, " `O Skill Condition"))(Deaths(CurrentPlayer, Exactly, 0, " `UniqueCoolTime"))(Switch("UiltimateSwitch", Cleared))()):
            # (Line 15) {
            # (Line 16) s.CharacterVoice(8);
            s.CharacterVoice(8)
            # (Line 17) v.P_Step[playerID] = 1;
            _ARRW(v.P_Step, playerID) << (1)
            # (Line 18) KillUnitAt(1, "Protoss Corsair", "[Skill]UseSkill", playerID);
            # (Line 19) }
            DoActions(KillUnitAt(1, "Protoss Corsair", "[Skill]UseSkill", playerID))
            # (Line 20) else if (Bring(playerID, AtLeast, 1, "Protoss Corsair", "[Skill]UseSkill"))
        if EUDElseIf()(Bring(playerID, AtLeast, 1, "Protoss Corsair", "[Skill]UseSkill")):
            # (Line 21) {
            # (Line 22) SetResources(CurrentPlayer, Add, 60, Gas);
            # (Line 23) KillUnitAt(1, "Protoss Corsair", "[Skill]UseSkill", playerID);
            DoActions(SetResources(CurrentPlayer, Add, 60, Gas))
            # (Line 24) }
            DoActions(KillUnitAt(1, "Protoss Corsair", "[Skill]UseSkill", playerID))
            # (Line 25) else if (Bring(playerID, AtLeast, 1, "Protoss Carrier", "[Skill]UseSkill"))
        if EUDElseIf()(Bring(playerID, AtLeast, 1, "Protoss Carrier", "[Skill]UseSkill")):
            # (Line 26) {
            # (Line 27) v.P_Step[playerID] = 200;
            _ARRW(v.P_Step, playerID) << (200)
            # (Line 28) KillUnitAt(1, "Protoss Carrier", "[Skill]UseSkill", playerID);
            # (Line 29) }
            DoActions(KillUnitAt(1, "Protoss Carrier", "[Skill]UseSkill", playerID))
            # (Line 30) else if (Bring(playerID, AtLeast, 1, "Protoss Arbiter", "[Skill]UseSkill"))
        if EUDElseIf()(Bring(playerID, AtLeast, 1, "Protoss Arbiter", "[Skill]UseSkill")):
            # (Line 31) {
            # (Line 32) v.P_Step[playerID] = 300;
            _ARRW(v.P_Step, playerID) << (300)
            # (Line 33) KillUnitAt(1, "Protoss Arbiter", "[Skill]UseSkill", playerID);
            # (Line 34) }
            DoActions(KillUnitAt(1, "Protoss Arbiter", "[Skill]UseSkill", playerID))
            # (Line 36) else if (Bring(playerID, AtLeast, 1, "Protoss Scout", "[Skill]UseSkill"))
        if EUDElseIf()(Bring(playerID, AtLeast, 1, "Protoss Scout", "[Skill]UseSkill")):
            # (Line 37) {
            # (Line 38) v.P_Step[playerID] = 100;
            _ARRW(v.P_Step, playerID) << (100)
            # (Line 39) KillUnitAt(1, "Protoss Scout", "[Skill]UseSkill", playerID);
            # (Line 40) }
            DoActions(KillUnitAt(1, "Protoss Scout", "[Skill]UseSkill", playerID))
            # (Line 42) }
        EUDEndIf()
        # (Line 45) if (v.P_SkillDelay[playerID] >= 2 && v.P_CountMain[playerID] == 0)
    EUDEndIf()
    if EUDIf()(EUDSCAnd()(v.P_SkillDelay[playerID] >= 2)(v.P_CountMain[playerID] == 0)()):
        # (Line 46) {
        # (Line 47) if (Bring(playerID, AtLeast, 2, "Protoss Scout", "[Skill]UseSkill") && v.P_Step[playerID] == 100)
        if EUDIf()(EUDSCAnd()(Bring(playerID, AtLeast, 2, "Protoss Scout", "[Skill]UseSkill"))(v.P_Step[playerID] == 100)()):
            # (Line 48) {
            # (Line 49) s.CharacterVoice(1);
            s.CharacterVoice(1)
            # (Line 50) v.P_SkillDelay[playerID] = 0;
            _ARRW(v.P_SkillDelay, playerID) << (0)
            # (Line 51) v.P_CountMain[playerID] = 0;
            _ARRW(v.P_CountMain, playerID) << (0)
            # (Line 52) v.P_LoopMain[playerID] = 0;
            _ARRW(v.P_LoopMain, playerID) << (0)
            # (Line 53) v.P_Step[playerID] = 110;
            _ARRW(v.P_Step, playerID) << (110)
            # (Line 54) KillUnitAt(2, "Protoss Scout", "[Skill]UseSkill", playerID);
            # (Line 55) }
            DoActions(KillUnitAt(2, "Protoss Scout", "[Skill]UseSkill", playerID))
            # (Line 56) else if (Bring(playerID, AtLeast, 1, "Protoss Arbiter", "[Skill]UseSkill")
        _t9 = EUDElseIf()
        # (Line 57) && Bring(playerID, AtLeast, 1, "Protoss Carrier", "[Skill]UseSkill")
        # (Line 58) && v.P_Step[playerID] == 300)
        if _t9(EUDSCAnd()(Bring(playerID, AtLeast, 1, "Protoss Arbiter", "[Skill]UseSkill"))(Bring(playerID, AtLeast, 1, "Protoss Carrier", "[Skill]UseSkill"))(v.P_Step[playerID] == 300)()):
            # (Line 59) {
            # (Line 60) s.CharacterVoice(2);
            s.CharacterVoice(2)
            # (Line 61) v.P_SkillDelay[playerID] = 0;
            _ARRW(v.P_SkillDelay, playerID) << (0)
            # (Line 62) v.P_CountMain[playerID] = 0;
            _ARRW(v.P_CountMain, playerID) << (0)
            # (Line 63) v.P_LoopMain[playerID] = 0;
            _ARRW(v.P_LoopMain, playerID) << (0)
            # (Line 64) v.P_Step[playerID] = 310;
            _ARRW(v.P_Step, playerID) << (310)
            # (Line 65) KillUnitAt(1, "Protoss Arbiter", "[Skill]UseSkill", playerID);
            # (Line 66) KillUnitAt(1, "Protoss Carrier", "[Skill]UseSkill", playerID);
            DoActions(KillUnitAt(1, "Protoss Arbiter", "[Skill]UseSkill", playerID))
            # (Line 67) }
            DoActions(KillUnitAt(1, "Protoss Carrier", "[Skill]UseSkill", playerID))
            # (Line 68) else if (Bring(playerID, AtLeast, 2, "Protoss Carrier", "[Skill]UseSkill")
        _t10 = EUDElseIf()
        # (Line 69) && v.P_Step[playerID] == 200)
        if _t10(EUDSCAnd()(Bring(playerID, AtLeast, 2, "Protoss Carrier", "[Skill]UseSkill"))(v.P_Step[playerID] == 200)()):
            # (Line 70) {
            # (Line 71) s.CharacterVoice(3);
            s.CharacterVoice(3)
            # (Line 72) v.P_SkillDelay[playerID] = 0;
            _ARRW(v.P_SkillDelay, playerID) << (0)
            # (Line 73) v.P_CountMain[playerID] = 0;
            _ARRW(v.P_CountMain, playerID) << (0)
            # (Line 74) v.P_LoopMain[playerID] = 0;
            _ARRW(v.P_LoopMain, playerID) << (0)
            # (Line 75) v.P_Step[playerID] = 210;
            _ARRW(v.P_Step, playerID) << (210)
            # (Line 76) KillUnitAt(2, "Protoss Carrier", "[Skill]UseSkill", playerID);
            # (Line 77) }
            DoActions(KillUnitAt(2, "Protoss Carrier", "[Skill]UseSkill", playerID))
            # (Line 78) else if (Bring(playerID, AtLeast, 2, "Protoss Arbiter", "[Skill]UseSkill") && v.P_Step[playerID] == 210)
        if EUDElseIf()(EUDSCAnd()(Bring(playerID, AtLeast, 2, "Protoss Arbiter", "[Skill]UseSkill"))(v.P_Step[playerID] == 210)()):
            # (Line 79) {
            # (Line 80) s.CharacterVoice(4);
            s.CharacterVoice(4)
            # (Line 81) v.P_SkillDelay[playerID] = 0;
            _ARRW(v.P_SkillDelay, playerID) << (0)
            # (Line 82) v.P_CountMain[playerID] = 0;
            _ARRW(v.P_CountMain, playerID) << (0)
            # (Line 83) v.P_LoopMain[playerID] = 0;
            _ARRW(v.P_LoopMain, playerID) << (0)
            # (Line 84) v.P_Step[playerID] = 220;
            _ARRW(v.P_Step, playerID) << (220)
            # (Line 85) KillUnitAt(2, "Protoss Arbiter", "[Skill]UseSkill", playerID);
            # (Line 86) }
            DoActions(KillUnitAt(2, "Protoss Arbiter", "[Skill]UseSkill", playerID))
            # (Line 89) else if (Bring(playerID, AtLeast, 2, "Protoss Arbiter", "[Skill]UseSkill")
        _t12 = EUDElseIf()
        # (Line 90) && v.P_Step[playerID] == 300
        # (Line 91) && v.P_UltimateGauge[playerID] >= v.P_Ultimate1[playerID])
        if _t12(EUDSCAnd()(Bring(playerID, AtLeast, 2, "Protoss Arbiter", "[Skill]UseSkill"))(v.P_Step[playerID] == 300)(v.P_UltimateGauge[playerID] >= v.P_Ultimate1[playerID])()):
            # (Line 92) {
            # (Line 93) s.CharacterVoice(5);
            s.CharacterVoice(5)
            # (Line 94) v.P_SkillDelay[playerID] = 0;
            _ARRW(v.P_SkillDelay, playerID) << (0)
            # (Line 95) v.P_CountMain[playerID] = 0;
            _ARRW(v.P_CountMain, playerID) << (0)
            # (Line 96) v.P_LoopMain[playerID] = 0;
            _ARRW(v.P_LoopMain, playerID) << (0)
            # (Line 97) v.P_Step[playerID] = 320;
            _ARRW(v.P_Step, playerID) << (320)
            # (Line 98) SetDeaths(playerID, Subtract, v.P_Ultimate1[playerID], " `UltimateCoolTime");
            # (Line 99) KillUnitAt(2, "Protoss Arbiter", "[Skill]UseSkill", playerID);
            DoActions(SetDeaths(playerID, Subtract, v.P_Ultimate1[playerID], " `UltimateCoolTime"))
            # (Line 101) }
            DoActions(KillUnitAt(2, "Protoss Arbiter", "[Skill]UseSkill", playerID))
            # (Line 103) }
        EUDEndIf()
        # (Line 104) }
    EUDEndIf()