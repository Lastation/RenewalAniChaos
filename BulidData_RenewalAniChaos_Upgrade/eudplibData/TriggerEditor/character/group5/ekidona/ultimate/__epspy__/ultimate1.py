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
# (Line 9) var flag = 0;
flag = EUDCreateVariables(1)
_IGVA([flag], lambda: [0])
# (Line 10) var pre_flag = 0;
pre_flag = EUDCreateVariables(1)
_IGVA([pre_flag], lambda: [0])
# (Line 12) function main(playerID)
# (Line 13) {
@EUDFunc
def f_main(playerID):
    # (Line 14) MoveUnit(All, "50 + 1n Tank", playerID, "Anywhere", "[Skill]HoldPosition");
    # (Line 15) MoveUnit(All, "60 + 1n Dragoon", playerID, "Anywhere", "[Skill]HoldPosition");
    DoActions(MoveUnit(All, "50 + 1n Tank", playerID, "Anywhere", "[Skill]HoldPosition"))
    # (Line 17) if (v.P_WaitMain[playerID] == 0)
    DoActions(MoveUnit(All, "60 + 1n Dragoon", playerID, "Anywhere", "[Skill]HoldPosition"))
    if EUDIf()(v.P_WaitMain[playerID] == 0):
        # (Line 18) {
        # (Line 19) if (v.P_CountMain[playerID] < 9)
        if EUDIf()(v.P_CountMain[playerID] >= 9, neg=True):
            # (Line 20) {
            # (Line 21) if (v.P_LoopMain[playerID] % 20 == 0)
            if EUDIf()(v.P_LoopMain[playerID] % 20 == 0):
                # (Line 22) {
                # (Line 23) flag = 2;
                flag << (2)
                # (Line 24) }
                # (Line 25) if (v.P_LoopMain[playerID] % 20 == 1)
            EUDEndIf()
            if EUDIf()(v.P_LoopMain[playerID] % 20 == 1):
                # (Line 26) {
                # (Line 27) trg.Shape_Dot(playerID, 8, "Zerg Devourer", 0, 0);
                trg.Shape_Dot(playerID, 8, "Zerg Devourer", 0, 0)
                # (Line 28) if (playerID < 3)
                if EUDIf()(playerID >= 3, neg=True):
                    # (Line 29) GiveUnits(All, "Zerg Devourer", playerID, "Anywhere", P7);
                    # (Line 30) else if (playerID >= 3)
                    DoActions(GiveUnits(All, "Zerg Devourer", playerID, "Anywhere", P7))
                if EUDElseIf()(playerID >= 3):
                    # (Line 31) GiveUnits(All, "Zerg Devourer", playerID, "Anywhere", P8);
                    # (Line 32) }
                    DoActions(GiveUnits(All, "Zerg Devourer", playerID, "Anywhere", P8))
                EUDEndIf()
                # (Line 33) }
            EUDEndIf()
            # (Line 35) if (v.P_CountMain[playerID] == 0)
        EUDEndIf()
        if EUDIf()(v.P_CountMain[playerID] == 0):
            # (Line 36) {
            # (Line 37) if (v.P_LoopMain[playerID] == 0)
            if EUDIf()(v.P_LoopMain[playerID] == 0):
                # (Line 38) {
                # (Line 39) SetSwitch("JunkYardDog - Ekidona", Set);
                # (Line 40) trg.Buff_ShieldFix(1);
                DoActions(SetSwitch("JunkYardDog - Ekidona", Set))
                trg.Buff_ShieldFix(1)
                # (Line 41) }
                # (Line 43) trg.Main_Wait(80);
            EUDEndIf()
            trg.Main_Wait(80)
            # (Line 45) v.P_LoopMain[playerID] += 1;
            _ARRW(v.P_LoopMain, playerID).__iadd__(1)
            # (Line 47) if (v.P_LoopMain[playerID] == 91)
            if EUDIf()(v.P_LoopMain[playerID] == 91):
                # (Line 48) {
                # (Line 49) s.CharacterVoice(3);
                s.CharacterVoice(3)
                # (Line 51) v.P_CountMain[playerID] += 1;
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 52) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 53) }
                # (Line 54) }
            EUDEndIf()
            # (Line 55) else if (v.P_CountMain[playerID] == 1)
        if EUDElseIf()(v.P_CountMain[playerID] == 1):
            # (Line 56) {
            # (Line 57) trg.Main_Wait(80);
            trg.Main_Wait(80)
            # (Line 59) v.P_LoopMain[playerID] += 1;
            _ARRW(v.P_LoopMain, playerID).__iadd__(1)
            # (Line 61) if (v.P_LoopMain[playerID] == 66)
            if EUDIf()(v.P_LoopMain[playerID] == 66):
                # (Line 62) {
                # (Line 63) s.CharacterVoice(4);
                s.CharacterVoice(4)
                # (Line 65) v.P_CountMain[playerID] += 1;
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 66) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 67) }
                # (Line 68) }
            EUDEndIf()
            # (Line 69) else if (v.P_CountMain[playerID] == 2)
        if EUDElseIf()(v.P_CountMain[playerID] == 2):
            # (Line 70) {
            # (Line 71) trg.Main_Wait(80);
            trg.Main_Wait(80)
            # (Line 73) v.P_LoopMain[playerID] += 1;
            _ARRW(v.P_LoopMain, playerID).__iadd__(1)
            # (Line 75) if (v.P_LoopMain[playerID] == 68)
            if EUDIf()(v.P_LoopMain[playerID] == 68):
                # (Line 76) {
                # (Line 77) s.CharacterVoice(5);
                s.CharacterVoice(5)
                # (Line 79) KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID);
                # (Line 80) KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID))
                # (Line 81) KillUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", playerID))
                # (Line 82) KillUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID))
                # (Line 83) KillUnitAt(All, "Zerg Devourer", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID))
                # (Line 84) KillUnitAt(All, "Zerg Devourer", "Anywhere", P7);
                DoActions(KillUnitAt(All, "Zerg Devourer", "Anywhere", playerID))
                # (Line 85) KillUnitAt(All, "Zerg Devourer", "Anywhere", P8);
                DoActions(KillUnitAt(All, "Zerg Devourer", "Anywhere", P7))
                # (Line 86) KillUnitAt(All, "Zerg Devourer", "Anywhere", P11);
                DoActions(KillUnitAt(All, "Zerg Devourer", "Anywhere", P8))
                # (Line 87) KillUnitAt(All, "Zerg Devourer", "Anywhere", P9);
                DoActions(KillUnitAt(All, "Zerg Devourer", "Anywhere", P11))
                # (Line 88) KillUnitAt(All, "Zerg Devourer", "Anywhere", P12);
                DoActions(KillUnitAt(All, "Zerg Devourer", "Anywhere", P9))
                # (Line 89) KillUnitAt(All, "Zerg Devourer", "Anywhere", P10);
                DoActions(KillUnitAt(All, "Zerg Devourer", "Anywhere", P12))
                # (Line 91) v.P_CountMain[playerID] += 1;
                DoActions(KillUnitAt(All, "Zerg Devourer", "Anywhere", P10))
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 92) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 93) }
                # (Line 94) }
            EUDEndIf()
            # (Line 95) else if (v.P_CountMain[playerID] == 3)
        if EUDElseIf()(v.P_CountMain[playerID] == 3):
            # (Line 96) {
            # (Line 97) trg.Main_Wait(80);
            trg.Main_Wait(80)
            # (Line 99) v.P_LoopMain[playerID] += 1;
            _ARRW(v.P_LoopMain, playerID).__iadd__(1)
            # (Line 101) if (v.P_LoopMain[playerID] == 57)
            if EUDIf()(v.P_LoopMain[playerID] == 57):
                # (Line 102) {
                # (Line 103) s.CharacterVoice(6);
                s.CharacterVoice(6)
                # (Line 105) v.P_CountMain[playerID] += 1;
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 106) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 107) }
                # (Line 108) }
            EUDEndIf()
            # (Line 109) else if (v.P_CountMain[playerID] == 4)
        if EUDElseIf()(v.P_CountMain[playerID] == 4):
            # (Line 110) {
            # (Line 111) trg.Main_Wait(80);
            trg.Main_Wait(80)
            # (Line 113) v.P_LoopMain[playerID] += 1;
            _ARRW(v.P_LoopMain, playerID).__iadd__(1)
            # (Line 115) if (v.P_LoopMain[playerID] == 68)
            if EUDIf()(v.P_LoopMain[playerID] == 68):
                # (Line 116) {
                # (Line 117) s.CharacterVoice(7);
                s.CharacterVoice(7)
                # (Line 119) v.P_CountMain[playerID] += 1;
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 120) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 121) }
                # (Line 122) }
            EUDEndIf()
            # (Line 123) else if (v.P_CountMain[playerID] == 5)
        if EUDElseIf()(v.P_CountMain[playerID] == 5):
            # (Line 124) {
            # (Line 125) trg.Main_Wait(80);
            trg.Main_Wait(80)
            # (Line 127) v.P_LoopMain[playerID] += 1;
            _ARRW(v.P_LoopMain, playerID).__iadd__(1)
            # (Line 129) if (v.P_LoopMain[playerID] == 20)
            if EUDIf()(v.P_LoopMain[playerID] == 20):
                # (Line 130) {
                # (Line 131) v.P_CountMain[playerID] += 1;
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 132) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 133) }
                # (Line 134) }
            EUDEndIf()
            # (Line 135) else if (v.P_CountMain[playerID] == 6)
        if EUDElseIf()(v.P_CountMain[playerID] == 6):
            # (Line 136) {
            # (Line 137) trg.Main_Wait(80);
            trg.Main_Wait(80)
            # (Line 139) v.P_LoopMain[playerID] += 1;
            _ARRW(v.P_LoopMain, playerID).__iadd__(1)
            # (Line 141) if (v.P_LoopMain[playerID] == 16)
            if EUDIf()(v.P_LoopMain[playerID] == 16):
                # (Line 142) {
                # (Line 143) s.CharacterVoice(8);
                s.CharacterVoice(8)
                # (Line 145) v.P_CountMain[playerID] += 1;
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 146) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 147) }
                # (Line 148) }
            EUDEndIf()
            # (Line 149) else if (v.P_CountMain[playerID] == 7)
        if EUDElseIf()(v.P_CountMain[playerID] == 7):
            # (Line 150) {
            # (Line 151) trg.Main_Wait(80);
            trg.Main_Wait(80)
            # (Line 153) v.P_LoopMain[playerID] += 1;
            _ARRW(v.P_LoopMain, playerID).__iadd__(1)
            # (Line 155) if (v.P_LoopMain[playerID] == 15)
            if EUDIf()(v.P_LoopMain[playerID] == 15):
                # (Line 156) {
                # (Line 157) s.CharacterVoice(9);
                s.CharacterVoice(9)
                # (Line 159) v.P_CountMain[playerID] += 1;
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 160) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 161) }
                # (Line 162) }
            EUDEndIf()
            # (Line 163) else if (v.P_CountMain[playerID] == 8)
        if EUDElseIf()(v.P_CountMain[playerID] == 8):
            # (Line 164) {
            # (Line 165) trg.Main_Wait(80);
            trg.Main_Wait(80)
            # (Line 167) v.P_LoopMain[playerID] += 1;
            _ARRW(v.P_LoopMain, playerID).__iadd__(1)
            # (Line 169) if (v.P_LoopMain[playerID] == 43)
            if EUDIf()(v.P_LoopMain[playerID] == 43):
                # (Line 170) {
                # (Line 171) s.CharacterVoice(10);
                s.CharacterVoice(10)
                # (Line 173) v.P_CountMain[playerID] += 1;
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 174) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 175) }
                # (Line 176) }
            EUDEndIf()
            # (Line 177) else if (v.P_CountMain[playerID] == 9)
        if EUDElseIf()(v.P_CountMain[playerID] == 9):
            # (Line 178) {
            # (Line 179) trg.Main_Wait(80);
            trg.Main_Wait(80)
            # (Line 181) v.P_LoopMain[playerID] += 1;
            _ARRW(v.P_LoopMain, playerID).__iadd__(1)
            # (Line 183) if (v.P_LoopMain[playerID] == 18)
            if EUDIf()(v.P_LoopMain[playerID] == 18):
                # (Line 184) {
                # (Line 185) v.P_CountMain[playerID] += 1;
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 186) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 187) }
                # (Line 188) }
            EUDEndIf()
            # (Line 189) else if (v.P_CountMain[playerID] == 10)
        if EUDElseIf()(v.P_CountMain[playerID] == 10):
            # (Line 190) {
            # (Line 191) if (Bring(playerID, AtLeast, 3, "Protoss Arbiter", "[Skill]UseSkill")
            _t29 = EUDIf()
            # (Line 192) && v.P_UltimateGauge[playerID] >= v.P_Ultimate2[playerID])
            if _t29(EUDSCAnd()(Bring(playerID, AtLeast, 3, "Protoss Arbiter", "[Skill]UseSkill"))(v.P_UltimateGauge[playerID] >= v.P_Ultimate2[playerID])()):
                # (Line 193) {
                # (Line 194) s.CharacterVoice(11);
                s.CharacterVoice(11)
                # (Line 195) v.P_SkillDelay[playerID] = 0;
                _ARRW(v.P_SkillDelay, playerID) << (0)
                # (Line 196) v.P_CountMain[playerID] = 0;
                _ARRW(v.P_CountMain, playerID) << (0)
                # (Line 197) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 198) v.P_Step[playerID] = 320;
                _ARRW(v.P_Step, playerID) << (320)
                # (Line 199) SetDeaths(playerID, Subtract, v.P_Ultimate2[playerID], " `UltimateCoolTime");
                # (Line 200) KillUnitAt(3, "Protoss Arbiter", "[Skill]UseSkill", playerID);
                DoActions(SetDeaths(playerID, Subtract, v.P_Ultimate2[playerID], " `UltimateCoolTime"))
                # (Line 201) }
                DoActions(KillUnitAt(3, "Protoss Arbiter", "[Skill]UseSkill", playerID))
                # (Line 202) else
                # (Line 203) {
            if EUDElse()():
                # (Line 204) KillUnitAt(All, "60 + 1n Siege", "Anywhere", playerID);
                # (Line 205) KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "60 + 1n Siege", "Anywhere", playerID))
                # (Line 206) KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID))
                # (Line 207) KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", playerID))
                # (Line 208) KillUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", playerID))
                # (Line 209) KillUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID))
                # (Line 210) KillUnitAt(All, "50 + 1n Tank", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID))
                # (Line 211) KillUnitAt(All, "Zerg Devourer", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "50 + 1n Tank", "Anywhere", playerID))
                # (Line 212) KillUnitAt(All, "Zerg Devourer", "Anywhere", P7);
                DoActions(KillUnitAt(All, "Zerg Devourer", "Anywhere", playerID))
                # (Line 213) KillUnitAt(All, "Zerg Devourer", "Anywhere", P8);
                DoActions(KillUnitAt(All, "Zerg Devourer", "Anywhere", P7))
                # (Line 214) KillUnitAt(All, "Zerg Devourer", "Anywhere", P11);
                DoActions(KillUnitAt(All, "Zerg Devourer", "Anywhere", P8))
                # (Line 215) KillUnitAt(All, "Zerg Devourer", "Anywhere", P9);
                DoActions(KillUnitAt(All, "Zerg Devourer", "Anywhere", P11))
                # (Line 216) KillUnitAt(All, "Zerg Devourer", "Anywhere", P12);
                DoActions(KillUnitAt(All, "Zerg Devourer", "Anywhere", P9))
                # (Line 217) KillUnitAt(All, "Zerg Devourer", "Anywhere", P10);
                DoActions(KillUnitAt(All, "Zerg Devourer", "Anywhere", P12))
                # (Line 219) SetSwitch("JunkYardDog - Ekidona", Clear);
                DoActions(KillUnitAt(All, "Zerg Devourer", "Anywhere", P10))
                # (Line 220) SetSwitch("UiltimateSwitch", Clear);
                DoActions(SetSwitch("JunkYardDog - Ekidona", Clear))
                # (Line 221) trg.SkillEnd();
                DoActions(SetSwitch("UiltimateSwitch", Clear))
                trg.SkillEnd()
                # (Line 222) }
                # (Line 223) }
            EUDEndIf()
            # (Line 225) if (playerID < 3)
        EUDEndIf()
        if EUDIf()(playerID >= 3, neg=True):
            # (Line 226) {
            # (Line 227) if (Bring(P7, AtLeast, 1, "Zerg Devourer", "Anywhere"))
            if EUDIf()(Bring(P7, AtLeast, 1, "Zerg Devourer", "Anywhere")):
                # (Line 228) {
                # (Line 229) for (var i = 0; i < 8; i++)
                i = EUDVariable()
                i << (0)
                if EUDWhile()(i >= 8, neg=True):
                    def _t33():
                        i.__iadd__(1)
                    # (Line 230) {
                    # (Line 231) MoveLocation(v.P_LocationID[playerID], "Zerg Devourer", P7, "Anywhere");
                    # (Line 232) GiveUnits(1, "Zerg Devourer", P7, "Anywhere", P9);
                    DoActions(MoveLocation(v.P_LocationID[playerID], "Zerg Devourer", P7, "Anywhere"))
                    # (Line 234) if (i % 2 == 0)
                    DoActions(GiveUnits(1, "Zerg Devourer", P7, "Anywhere", P9))
                    if EUDIf()(i % 2 == 0):
                        # (Line 235) {
                        # (Line 236) trg.SkillUnit(playerID, 1, "80 + 1n Tom Kazansky");
                        trg.SkillUnit(playerID, 1, "80 + 1n Tom Kazansky")
                        # (Line 237) trg.SkillUnit(playerID, 1, "Protoss Dark Archon");
                        trg.SkillUnit(playerID, 1, "Protoss Dark Archon")
                        # (Line 238) }
                        # (Line 239) else if (i % 2 == 1)
                    if EUDElseIf()(i % 2 == 1):
                        # (Line 240) {
                        # (Line 241) trg.SkillUnit(playerID, 1, "80 + 1n Artanis");
                        trg.SkillUnit(playerID, 1, "80 + 1n Artanis")
                        # (Line 242) trg.SkillUnit(playerID, 1, "60 + 1n Archon");
                        trg.SkillUnit(playerID, 1, "60 + 1n Archon")
                        # (Line 243) }
                        # (Line 244) }
                    EUDEndIf()
                    # (Line 246) KillUnitAt(All, "80 + 1n Artanis", "Anywhere", playerID);
                    EUDSetContinuePoint()
                    _t33()
                EUDEndWhile()
                # (Line 247) KillUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "80 + 1n Artanis", "Anywhere", playerID))
                # (Line 248) KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", playerID))
                # (Line 249) KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID))
                # (Line 250) }
                DoActions(KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID))
                # (Line 251) else
                # (Line 252) {
            if EUDElse()():
                # (Line 253) GiveUnits(All, "Zerg Devourer", P9, "Anywhere", P7);
                # (Line 254) }
                DoActions(GiveUnits(All, "Zerg Devourer", P9, "Anywhere", P7))
                # (Line 255) }
            EUDEndIf()
            # (Line 256) else if (playerID >= 3)
        if EUDElseIf()(playerID >= 3):
            # (Line 257) {
            # (Line 258) if (Bring(P8, AtLeast, 1, "Zerg Devourer", "Anywhere"))
            if EUDIf()(Bring(P8, AtLeast, 1, "Zerg Devourer", "Anywhere")):
                # (Line 259) {
                # (Line 260) for (var i = 0; i < 8; i++)
                i = EUDVariable()
                i << (0)
                if EUDWhile()(i >= 8, neg=True):
                    def _t39():
                        i.__iadd__(1)
                    # (Line 261) {
                    # (Line 262) MoveLocation(v.P_LocationID[playerID], "Zerg Devourer", P8, "Anywhere");
                    # (Line 263) GiveUnits(1, "Zerg Devourer", P8, "Anywhere", P9);
                    DoActions(MoveLocation(v.P_LocationID[playerID], "Zerg Devourer", P8, "Anywhere"))
                    # (Line 265) if (i % 2 == 0)
                    DoActions(GiveUnits(1, "Zerg Devourer", P8, "Anywhere", P9))
                    if EUDIf()(i % 2 == 0):
                        # (Line 266) {
                        # (Line 267) trg.SkillUnit(playerID, 1, "80 + 1n Tom Kazansky");
                        trg.SkillUnit(playerID, 1, "80 + 1n Tom Kazansky")
                        # (Line 268) trg.SkillUnit(playerID, 1, "Protoss Dark Archon");
                        trg.SkillUnit(playerID, 1, "Protoss Dark Archon")
                        # (Line 269) }
                        # (Line 270) else if (i % 2 == 1)
                    if EUDElseIf()(i % 2 == 1):
                        # (Line 271) {
                        # (Line 272) trg.SkillUnit(playerID, 1, "80 + 1n Artanis");
                        trg.SkillUnit(playerID, 1, "80 + 1n Artanis")
                        # (Line 273) trg.SkillUnit(playerID, 1, "60 + 1n Archon");
                        trg.SkillUnit(playerID, 1, "60 + 1n Archon")
                        # (Line 274) }
                        # (Line 275) }
                    EUDEndIf()
                    # (Line 277) KillUnitAt(All, "80 + 1n Artanis", "Anywhere", playerID);
                    EUDSetContinuePoint()
                    _t39()
                EUDEndWhile()
                # (Line 278) KillUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "80 + 1n Artanis", "Anywhere", playerID))
                # (Line 279) KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", playerID))
                # (Line 280) KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID))
                # (Line 281) }
                DoActions(KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID))
                # (Line 282) else
                # (Line 283) {
            if EUDElse()():
                # (Line 284) GiveUnits(All, "Zerg Devourer", P9, "Anywhere", P8);
                # (Line 285) }
                DoActions(GiveUnits(All, "Zerg Devourer", P9, "Anywhere", P8))
                # (Line 286) }
            EUDEndIf()
            # (Line 288) if (flag == 1)
        EUDEndIf()
        if EUDIf()(flag == 1):
            # (Line 289) {
            # (Line 290) if (pre_flag != flag)
            if EUDIf()(pre_flag == flag, neg=True):
                # (Line 291) {
                # (Line 292) GiveUnits(All, "Zerg Devourer", P11, "Anywhere", P10);
                # (Line 293) GiveUnits(All, "Zerg Devourer", playerID, "Anywhere", P10);
                DoActions(GiveUnits(All, "Zerg Devourer", P11, "Anywhere", P10))
                # (Line 295) pre_flag = flag;
                DoActions(GiveUnits(All, "Zerg Devourer", playerID, "Anywhere", P10))
                pre_flag << (flag)
                # (Line 296) }
                # (Line 297) if (Bring(P10, AtLeast, 1, "Zerg Devourer", "Anywhere"))
            EUDEndIf()
            if EUDIf()(Bring(P10, AtLeast, 1, "Zerg Devourer", "Anywhere")):
                # (Line 298) {
                # (Line 299) for (var i = 0; i < 8; i++)
                i = EUDVariable()
                i << (0)
                if EUDWhile()(i >= 8, neg=True):
                    def _t46():
                        i.__iadd__(1)
                    # (Line 300) {
                    # (Line 301) MoveLocation(v.P_LocationID[playerID], "Zerg Devourer", P10, "Anywhere");
                    # (Line 302) GiveUnits(1, "Zerg Devourer", P10, "Anywhere", P11);
                    DoActions(MoveLocation(v.P_LocationID[playerID], "Zerg Devourer", P10, "Anywhere"))
                    # (Line 304) if (i % 2 == 0)
                    DoActions(GiveUnits(1, "Zerg Devourer", P10, "Anywhere", P11))
                    if EUDIf()(i % 2 == 0):
                        # (Line 305) {
                        # (Line 306) trg.SkillUnit(playerID, 1, "80 + 1n Tom Kazansky");
                        trg.SkillUnit(playerID, 1, "80 + 1n Tom Kazansky")
                        # (Line 307) trg.SkillUnit(playerID, 1, "Protoss Dark Archon");
                        trg.SkillUnit(playerID, 1, "Protoss Dark Archon")
                        # (Line 308) }
                        # (Line 309) else if (i % 2 == 1)
                    if EUDElseIf()(i % 2 == 1):
                        # (Line 310) {
                        # (Line 311) trg.SkillUnit(playerID, 1, "80 + 1n Artanis");
                        trg.SkillUnit(playerID, 1, "80 + 1n Artanis")
                        # (Line 312) trg.SkillUnit(playerID, 1, "60 + 1n Archon");
                        trg.SkillUnit(playerID, 1, "60 + 1n Archon")
                        # (Line 313) }
                        # (Line 314) }
                    EUDEndIf()
                    # (Line 316) KillUnitAt(All, "80 + 1n Artanis", "Anywhere", playerID);
                    EUDSetContinuePoint()
                    _t46()
                EUDEndWhile()
                # (Line 317) KillUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "80 + 1n Artanis", "Anywhere", playerID))
                # (Line 318) KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", playerID))
                # (Line 319) KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID))
                # (Line 320) }
                DoActions(KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID))
                # (Line 321) else
                # (Line 322) {
            if EUDElse()():
                # (Line 323) GiveUnits(All, "Zerg Devourer", P11, "Anywhere", P10);
                # (Line 324) }
                DoActions(GiveUnits(All, "Zerg Devourer", P11, "Anywhere", P10))
                # (Line 325) }
            EUDEndIf()
            # (Line 326) else if (flag == 2)
        if EUDElseIf()(flag == 2):
            # (Line 327) {
            # (Line 328) if (pre_flag != flag)
            if EUDIf()(pre_flag == flag, neg=True):
                # (Line 329) {
                # (Line 330) GiveUnits(All, "Zerg Devourer", P9, "Anywhere", playerID);
                # (Line 331) GiveUnits(All, "Zerg Devourer", P7, "Anywhere", playerID);
                DoActions(GiveUnits(All, "Zerg Devourer", P9, "Anywhere", playerID))
                # (Line 332) GiveUnits(All, "Zerg Devourer", P8, "Anywhere", playerID);
                DoActions(GiveUnits(All, "Zerg Devourer", P7, "Anywhere", playerID))
                # (Line 334) MoveUnit(All, "Zerg Devourer", playerID, "Anywhere", "[Skill]HoldPosition");
                DoActions(GiveUnits(All, "Zerg Devourer", P8, "Anywhere", playerID))
                # (Line 336) pre_flag = flag;
                DoActions(MoveUnit(All, "Zerg Devourer", playerID, "Anywhere", "[Skill]HoldPosition"))
                pre_flag << (flag)
                # (Line 337) }
                # (Line 339) if (Bring(playerID, AtLeast, 1, "Zerg Devourer", "Anywhere"))
            EUDEndIf()
            if EUDIf()(Bring(playerID, AtLeast, 1, "Zerg Devourer", "Anywhere")):
                # (Line 340) {
                # (Line 341) for (var i = 0; i < 8; i++)
                i = EUDVariable()
                i << (0)
                if EUDWhile()(i >= 8, neg=True):
                    def _t53():
                        i.__iadd__(1)
                    # (Line 342) {
                    # (Line 343) MoveLocation(v.P_LocationID[playerID], "Zerg Devourer", playerID, "Anywhere");
                    # (Line 344) GiveUnits(1, "Zerg Devourer", playerID, "Anywhere", P11);
                    DoActions(MoveLocation(v.P_LocationID[playerID], "Zerg Devourer", playerID, "Anywhere"))
                    # (Line 346) if (i % 4 == 0)
                    DoActions(GiveUnits(1, "Zerg Devourer", playerID, "Anywhere", P11))
                    if EUDIf()(i % 4 == 0):
                        # (Line 347) {
                        # (Line 348) trg.SkillUnit(playerID, 1, "50 + 1n Battlecruiser");
                        trg.SkillUnit(playerID, 1, "50 + 1n Battlecruiser")
                        # (Line 349) trg.SkillUnit(playerID, 1, "60 + 1n Siege");
                        trg.SkillUnit(playerID, 1, "60 + 1n Siege")
                        # (Line 350) trg.SkillUnit(playerID, 1, "130 + 1n Norad");
                        trg.SkillUnit(playerID, 1, "130 + 1n Norad")
                        # (Line 351) }
                        # (Line 352) else if (i % 4 == 1)
                    if EUDElseIf()(i % 4 == 1):
                        # (Line 353) {
                        # (Line 354) trg.SkillUnit(playerID, 1, "60 + 1n Danimoth");
                        trg.SkillUnit(playerID, 1, "60 + 1n Danimoth")
                        # (Line 355) trg.SkillUnit(playerID, 1, "60 + 1n Siege");
                        trg.SkillUnit(playerID, 1, "60 + 1n Siege")
                        # (Line 356) trg.SkillUnit(playerID, 1, "40 + 1n Gantrithor");
                        trg.SkillUnit(playerID, 1, "40 + 1n Gantrithor")
                        # (Line 357) }
                        # (Line 358) else if (i % 4 == 2)
                    if EUDElseIf()(i % 4 == 2):
                        # (Line 359) {
                        # (Line 360) trg.SkillUnit(playerID, 1, "40 + 1n Wraith");
                        trg.SkillUnit(playerID, 1, "40 + 1n Wraith")
                        # (Line 361) trg.SkillUnit(playerID, 1, "50 + 1n Tank");
                        trg.SkillUnit(playerID, 1, "50 + 1n Tank")
                        # (Line 362) trg.SkillUnit(playerID, 1, "130 + 1n Norad");
                        trg.SkillUnit(playerID, 1, "130 + 1n Norad")
                        # (Line 363) }
                        # (Line 364) else if (i % 4 == 3)
                    if EUDElseIf()(i % 4 == 3):
                        # (Line 365) {
                        # (Line 366) trg.SkillUnit(playerID, 1, "40 + 1n Mojo");
                        trg.SkillUnit(playerID, 1, "40 + 1n Mojo")
                        # (Line 367) trg.SkillUnit(playerID, 1, "60 + 1n Dragoon");
                        trg.SkillUnit(playerID, 1, "60 + 1n Dragoon")
                        # (Line 368) trg.SkillUnit(playerID, 1, "40 + 1n Gantrithor");
                        trg.SkillUnit(playerID, 1, "40 + 1n Gantrithor")
                        # (Line 369) }
                        # (Line 370) }
                    EUDEndIf()
                    # (Line 372) KillUnitAt(All, "130 + 1n Norad", "Anywhere", playerID);
                    EUDSetContinuePoint()
                    _t53()
                EUDEndWhile()
                # (Line 373) KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", playerID);
                DoActions(KillUnitAt(All, "130 + 1n Norad", "Anywhere", playerID))
                # (Line 375) MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
                DoActions(KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", playerID))
                # (Line 376) Order("50 + 1n Tank", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                DoActions(MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere"))
                # (Line 377) Order("50 + 1n Battlecruiser", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                DoActions(Order("50 + 1n Tank", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                # (Line 378) Order("60 + 1n Dragoon", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                DoActions(Order("50 + 1n Battlecruiser", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                # (Line 379) Order("60 + 1n Danimoth", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                DoActions(Order("60 + 1n Dragoon", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                # (Line 380) Order("40 + 1n Wraith", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                DoActions(Order("60 + 1n Danimoth", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                # (Line 381) Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
                DoActions(Order("40 + 1n Wraith", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                # (Line 382) }
                DoActions(Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]))
                # (Line 383) else
                # (Line 384) {
            if EUDElse()():
                # (Line 385) flag = 1;
                flag << (1)
                # (Line 386) }
                # (Line 387) }
            EUDEndIf()
            # (Line 388) }
        EUDEndIf()
        # (Line 390) MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
    EUDEndIf()
    # (Line 391) }
    DoActions(MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere"))