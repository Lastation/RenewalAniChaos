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
# (Line 5) import character.group4.yuuna.common.skill1 as O;
from character.group4.yuuna.common import skill1 as O
# (Line 6) import character.group4.yuuna.common.skill2 as S;
from character.group4.yuuna.common import skill2 as S
# (Line 7) import character.group4.yuuna.common.skill3 as C;
from character.group4.yuuna.common import skill3 as C
# (Line 8) import character.group4.yuuna.common.skill4 as A;
from character.group4.yuuna.common import skill4 as A
# (Line 10) import character.group4.yuuna.combo.combo1 as SSS;
from character.group4.yuuna.combo import combo1 as SSS
# (Line 11) import character.group4.yuuna.combo.combo2 as SSSSS;
from character.group4.yuuna.combo import combo2 as SSSSS
# (Line 12) import character.group4.yuuna.combo.combo3 as CCC;
from character.group4.yuuna.combo import combo3 as CCC
# (Line 13) import character.group4.yuuna.combo.combo4 as CCCAA;
from character.group4.yuuna.combo import combo4 as CCCAA
# (Line 14) import character.group4.yuuna.combo.combo5 as CAAA;
from character.group4.yuuna.combo import combo5 as CAAA
# (Line 16) import character.group4.yuuna.ultimate.ultimate1 as AAA;
from character.group4.yuuna.ultimate import ultimate1 as AAA
# (Line 17) import character.group4.yuuna.ultimate.ultimate2 as AAAAAA;
from character.group4.yuuna.ultimate import ultimate2 as AAAAAA
# (Line 19) import character.group4.yuuna.text as text;
from character.group4.yuuna import text as text
# (Line 20) import character.group4.yuuna.commend as commend;
from character.group4.yuuna import commend as commend
# (Line 22) function SkillList(playerID)
# (Line 23) {
@EUDFunc
def SkillList(playerID):
    # (Line 24) if(Memory(0x00596A44, Exactly, 256)) 	// Insert key Pressed
    if EUDIf()(Memory(0x00596A44, Exactly, 256)):
        # (Line 25) {
        # (Line 26) v.stb.printAt(0, "\n");
        v.stb.printAt(0, "\n")
        # (Line 27) v.stb.printAt(1, "\x1F　＃\x04- 유우키 \x1B유우나　\x04[ 유우키 유우나는 용사다 ]");
        v.stb.printAt(1, "\x1F　＃\x04- 유우키 \x1B유우나　\x04[ 유우키 유우나는 용사다 ]")
        # (Line 28) v.stb.printAt(2, "　　\x1FA\x04ction List");
        v.stb.printAt(2, "　　\x1FA\x04ction List")
        # (Line 29) v.stb.printAt(3, "　　　\x18O \x04만개 \x19[ 공 3 업 방 3 다운 / 최대 3 중첩 가능 / 사망 시 해제 ] \x051분");
        v.stb.printAt(3, "　　　\x18O \x04만개 \x19[ 공 3 업 방 3 다운 / 최대 3 중첩 가능 / 사망 시 해제 ] \x051분")
        # (Line 30) v.stb.printAt(4, "　　　\x04\x1FSSS + AS \x04인간 \x19[ 대인 / 순간딜 / AS - 자리고정 ]");
        v.stb.printAt(4, "　　　\x04\x1FSSS + AS \x04인간 \x19[ 대인 / 순간딜 / AS - 자리고정 ]")
        # (Line 31) v.stb.printAt(5, "　　　\x04\x1FCCA \x04강인함 \x19[ 공성 / 순간딜 / 자리고정 ]");
        v.stb.printAt(5, "　　　\x04\x1FCCA \x04강인함 \x19[ 공성 / 순간딜 / 자리고정 ]")
        # (Line 32) v.stb.printAt(6, "　　　\x04\x1FCAAA + 100 Gas \x04희생 \x19[ 공성 / 지속딜 / 자리고정 ]");
        v.stb.printAt(6, "　　　\x04\x1FCAAA + 100 Gas \x04희생 \x19[ 공성 / 지속딜 / 자리고정 ]")
        # (Line 33) v.stb.printAt(7, "\n");
        v.stb.printAt(7, "\n")
        # (Line 34) v.stb.printAt(8, "　　　\x08AAAA \x04대만개 \x19[ 공성 ] \x05", v.P_Ultimate1[playerID]);
        v.stb.printAt(8, "　　　\x08AAAA \x04대만개 \x19[ 공성 ] \x05", v.P_Ultimate1[playerID])
        # (Line 35) v.stb.printAt(9, "　　　\x04+ \x08AAA \x04용사 펀치 \x19[ 만개 3 중첩 시 사용 가능 ] \x05", v.P_Ultimate2[playerID]);
        v.stb.printAt(9, "　　　\x04+ \x08AAA \x04용사 펀치 \x19[ 만개 3 중첩 시 사용 가능 ] \x05", v.P_Ultimate2[playerID])
        # (Line 36) v.stb.printAt(10, "\n");
        v.stb.printAt(10, "\n")
        # (Line 37) PlayWAV("sound\\Bullet\\LaserHit.wav");
        # (Line 38) }
        DoActions(PlayWAV("sound\\Bullet\\LaserHit.wav"))
        # (Line 39) }
    EUDEndIf()
    # (Line 41) function main(playerID)

# (Line 42) {
@EUDFunc
def f_main(playerID):
    # (Line 43) v.P_HeroID[playerID] = 22;
    _ARRW(v.P_HeroID, playerID) << (22)
    # (Line 44) v.P_LocationID[playerID] = 181;
    _ARRW(v.P_LocationID, playerID) << (181)
    # (Line 45) v.P_UnitID[playerID] = 54;
    _ARRW(v.P_UnitID, playerID) << (54)
    # (Line 47) v.P_Ultimate1[playerID] = 650;
    _ARRW(v.P_Ultimate1, playerID) << (650)
    # (Line 48) v.P_Ultimate2[playerID] = 300;
    _ARRW(v.P_Ultimate2, playerID) << (300)
    # (Line 51) commend.main(playerID);
    commend.f_main(playerID)
    # (Line 52) SkillList(playerID);
    SkillList(playerID)
    # (Line 54) if (v.P_SkillDelay[playerID] == 0)
    if EUDIf()(v.P_SkillDelay[playerID] == 0):
        # (Line 55) {
        # (Line 56) switch(v.P_Step[playerID])
        EUDSwitch(v.P_Step[playerID])
        # (Line 57) {
        # (Line 58) case 1:
        _t2 = EUDSwitchCase()
        # (Line 59) O.main(playerID);
        if _t2(1):
            O.f_main(playerID)
            # (Line 60) break;
            EUDBreak()
            # (Line 61) case 100:
        _t3 = EUDSwitchCase()
        # (Line 62) S.main(playerID);
        if _t3(100):
            S.f_main(playerID)
            # (Line 63) break;
            EUDBreak()
            # (Line 64) case 200:
        _t4 = EUDSwitchCase()
        # (Line 65) C.main(playerID);
        if _t4(200):
            C.f_main(playerID)
            # (Line 66) break;
            EUDBreak()
            # (Line 67) case 300:
        _t5 = EUDSwitchCase()
        # (Line 68) A.main(playerID);
        if _t5(300):
            A.f_main(playerID)
            # (Line 69) break;
            EUDBreak()
            # (Line 70) case 110:
        _t6 = EUDSwitchCase()
        # (Line 71) SSS.main(playerID);
        if _t6(110):
            SSS.f_main(playerID)
            # (Line 72) break;
            EUDBreak()
            # (Line 73) case 120:
        _t7 = EUDSwitchCase()
        # (Line 74) SSSSS.main(playerID);
        if _t7(120):
            SSSSS.f_main(playerID)
            # (Line 75) break;
            EUDBreak()
            # (Line 76) case 210:
        _t8 = EUDSwitchCase()
        # (Line 77) CCC.main(playerID);
        if _t8(210):
            CCC.f_main(playerID)
            # (Line 78) break;
            EUDBreak()
            # (Line 79) case 220:
        _t9 = EUDSwitchCase()
        # (Line 80) CCCAA.main(playerID);
        if _t9(220):
            CCCAA.f_main(playerID)
            # (Line 81) break;
            EUDBreak()
            # (Line 82) case 230:
        _t10 = EUDSwitchCase()
        # (Line 83) CAAA.main(playerID);
        if _t10(230):
            CAAA.f_main(playerID)
            # (Line 84) break;
            EUDBreak()
            # (Line 85) case 310:
        _t11 = EUDSwitchCase()
        # (Line 86) AAA.main(playerID);
        if _t11(310):
            AAA.f_main(playerID)
            # (Line 87) break;
            EUDBreak()
            # (Line 88) case 320:
        _t12 = EUDSwitchCase()
        # (Line 89) AAAAAA.main(playerID);
        if _t12(320):
            AAAAAA.f_main(playerID)
            # (Line 90) break;
            EUDBreak()
            # (Line 92) }
        # (Line 93) }
        EUDEndSwitch()
        # (Line 97) }
    EUDEndIf()
