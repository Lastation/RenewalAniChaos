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
# (Line 5) import character.group6.park.common.skill1 as O;
from character.group6.park.common import skill1 as O
# (Line 6) import character.group6.park.common.skill2 as S;
from character.group6.park.common import skill2 as S
# (Line 7) import character.group6.park.common.skill3 as C;
from character.group6.park.common import skill3 as C
# (Line 8) import character.group6.park.common.skill4 as A;
from character.group6.park.common import skill4 as A
# (Line 10) import character.group6.park.combo.combo1 as SSS;
from character.group6.park.combo import combo1 as SSS
# (Line 11) import character.group6.park.combo.combo2 as CCA;
from character.group6.park.combo import combo2 as CCA
# (Line 12) import character.group6.park.combo.combo3 as CCAAC;
from character.group6.park.combo import combo3 as CCAAC
# (Line 13) import character.group6.park.combo.combo4 as CCAACCC;
from character.group6.park.combo import combo4 as CCAACCC
# (Line 14) import character.group6.park.combo.combo5 as AAC;
from character.group6.park.combo import combo5 as AAC
# (Line 16) import character.group6.park.ultimate.ultimate1 as AAA;
from character.group6.park.ultimate import ultimate1 as AAA
# (Line 17) import character.group6.park.ultimate.ultimate2 as AAAAA;
from character.group6.park.ultimate import ultimate2 as AAAAA
# (Line 19) import character.group6.park.text as text;
from character.group6.park import text as text
# (Line 20) import character.group6.park.commend as commend;
from character.group6.park import commend as commend
# (Line 22) var loop  = 0;
loop = EUDCreateVariables(1)
_IGVA([loop], lambda: [0])
# (Line 24) function SkillList(playerID)
# (Line 25) {
@EUDFunc
def SkillList(playerID):
    # (Line 26) if(Memory(0x00596A44, Exactly, 256)) 	// Insert key Pressed
    if EUDIf()(Memory(0x00596A44, Exactly, 256)):
        # (Line 27) {
        # (Line 28) v.stb.printAt(0, "\n");
        v.stb.printAt(0, "\n")
        # (Line 29) v.stb.printAt(1, "\x1F　＃\x1B- 박 일표　\x04[ 갓 오브 하이스쿨 ]");
        v.stb.printAt(1, "\x1F　＃\x1B- 박 일표　\x04[ 갓 오브 하이스쿨 ]")
        # (Line 30) v.stb.printAt(2, "　　\x1FA\x04ction List");
        v.stb.printAt(2, "　　\x1FA\x04ction List")
        # (Line 31) v.stb.printAt(3, "　　　\x18O \x04택견 - 무음신속 \x19[ 10초 간 첫 스킬에 한해 스킬 사용시 적에게 돌진 ] \x052분");
        v.stb.printAt(3, "　　　\x18O \x04택견 - 무음신속 \x19[ 10초 간 첫 스킬에 한해 스킬 사용시 적에게 돌진 ] \x052분")
        # (Line 32) v.stb.printAt(4, "　　　\x04\x1FSSS\x04 소용 \x19[ 대인 / 순간딜 ]");
        v.stb.printAt(4, "　　　\x04\x1FSSS\x04 소용 \x19[ 대인 / 순간딜 ]")
        # (Line 33) v.stb.printAt(5, "　　　\x04\x1FCCC + AC + CC\x04 약점 \x19[ 대인 / 순간딜 ]");
        v.stb.printAt(5, "　　　\x04\x1FCCC + AC + CC\x04 약점 \x19[ 대인 / 순간딜 ]")
        # (Line 34) v.stb.printAt(6, "　　　\x04\x1FAAC \x04도발 \x19[ 대인 / 순간딜 ]");
        v.stb.printAt(6, "　　　\x04\x1FAAC \x04도발 \x19[ 대인 / 순간딜 ]")
        # (Line 35) v.stb.printAt(7, "　　　\x08AAA \x04택견 오의 - 화축 \x19[ 대인 ] \x05", v.P_Ultimate1[playerID]);
        v.stb.printAt(7, "　　　\x08AAA \x04택견 오의 - 화축 \x19[ 대인 ] \x05", v.P_Ultimate1[playerID])
        # (Line 36) v.stb.printAt(8, "　　　\x08 + AA \x04 최종 오의 - 삼염멸도각 \x19[ 공성 ] \x05", v.P_Ultimate2[playerID]);
        v.stb.printAt(8, "　　　\x08 + AA \x04 최종 오의 - 삼염멸도각 \x19[ 공성 ] \x05", v.P_Ultimate2[playerID])
        # (Line 37) v.stb.printAt(9, "\n");
        v.stb.printAt(9, "\n")
        # (Line 38) PlayWAV("sound\\Bullet\\LaserHit.wav");
        # (Line 39) }
        DoActions(PlayWAV("sound\\Bullet\\LaserHit.wav"))
        # (Line 40) }
    EUDEndIf()
    # (Line 42) function main(playerID)

# (Line 43) {
@EUDFunc
def f_main(playerID):
    # (Line 44) v.P_HeroID[playerID] = 31;
    _ARRW(v.P_HeroID, playerID) << (31)
    # (Line 45) v.P_LocationID[playerID] = 199;
    _ARRW(v.P_LocationID, playerID) << (199)
    # (Line 46) v.P_UnitID[playerID] = 10;
    _ARRW(v.P_UnitID, playerID) << (10)
    # (Line 48) v.P_Ultimate1[playerID] = 500;
    _ARRW(v.P_Ultimate1, playerID) << (500)
    # (Line 49) v.P_Ultimate2[playerID] = 250;
    _ARRW(v.P_Ultimate2, playerID) << (250)
    # (Line 51) SkillList(playerID);
    SkillList(playerID)
    # (Line 52) commend.main(playerID);
    commend.f_main(playerID)
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
            # (Line 73) case 210:
        _t7 = EUDSwitchCase()
        # (Line 74) CCA.main(playerID);
        if _t7(210):
            CCA.f_main(playerID)
            # (Line 75) break;
            EUDBreak()
            # (Line 76) case 220:
        _t8 = EUDSwitchCase()
        # (Line 77) CCAAC.main(playerID);
        if _t8(220):
            CCAAC.f_main(playerID)
            # (Line 78) break;
            EUDBreak()
            # (Line 79) case 230:
        _t9 = EUDSwitchCase()
        # (Line 80) CCAACCC.main(playerID);
        if _t9(230):
            CCAACCC.f_main(playerID)
            # (Line 81) break;
            EUDBreak()
            # (Line 82) case 310:
        _t10 = EUDSwitchCase()
        # (Line 83) AAC.main(playerID);
        if _t10(310):
            AAC.f_main(playerID)
            # (Line 84) break;
            EUDBreak()
            # (Line 85) case 320:
        _t11 = EUDSwitchCase()
        # (Line 86) AAA.main(playerID);
        if _t11(320):
            AAA.f_main(playerID)
            # (Line 87) break;
            EUDBreak()
            # (Line 88) case 330:
        _t12 = EUDSwitchCase()
        # (Line 89) AAAAA.main(playerID);
        if _t12(330):
            AAAAA.f_main(playerID)
            # (Line 90) break;
            EUDBreak()
            # (Line 91) }
        # (Line 92) }
        EUDEndSwitch()
        # (Line 95) }
    EUDEndIf()