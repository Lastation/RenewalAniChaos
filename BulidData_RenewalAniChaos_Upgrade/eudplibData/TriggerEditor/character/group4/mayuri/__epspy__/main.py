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
# (Line 5) import character.group4.mayuri.common.skill1 as O;
from character.group4.mayuri.common import skill1 as O
# (Line 6) import character.group4.mayuri.common.skill2 as S;
from character.group4.mayuri.common import skill2 as S
# (Line 7) import character.group4.mayuri.common.skill3 as C;
from character.group4.mayuri.common import skill3 as C
# (Line 8) import character.group4.mayuri.common.skill4 as A;
from character.group4.mayuri.common import skill4 as A
# (Line 10) import character.group4.mayuri.combo.combo1 as SSS;
from character.group4.mayuri.combo import combo1 as SSS
# (Line 11) import character.group4.mayuri.combo.combo2 as AAS;
from character.group4.mayuri.combo import combo2 as AAS
# (Line 12) import character.group4.mayuri.combo.combo3 as CCC;
from character.group4.mayuri.combo import combo3 as CCC
# (Line 13) import character.group4.mayuri.combo.combo4 as CCCAS;
from character.group4.mayuri.combo import combo4 as CCCAS
# (Line 14) import character.group4.mayuri.combo.combo5 as CCCASCC;
from character.group4.mayuri.combo import combo5 as CCCASCC
# (Line 16) import character.group4.mayuri.ultimate.ultimate1 as AAA;
from character.group4.mayuri.ultimate import ultimate1 as AAA
# (Line 17) import character.group4.mayuri.ultimate.ultimate2 as AAAAA;
from character.group4.mayuri.ultimate import ultimate2 as AAAAA
# (Line 19) import character.group4.mayuri.text as text;
from character.group4.mayuri import text as text
# (Line 20) import character.group4.mayuri.commend as commend;
from character.group4.mayuri import commend as commend
# (Line 22) function SkillList(playerID);
# (Line 24) function main(playerID)
# (Line 25) {
@EUDFunc
def f_main(playerID):
    # (Line 26) v.P_LocationID[playerID] = 183;
    _ARRW(v.P_LocationID, playerID) << (183)
    # (Line 27) v.P_UnitID[playerID] = 64;
    _ARRW(v.P_UnitID, playerID) << (64)
    # (Line 29) v.P_Ultimate1[playerID] = 500;
    _ARRW(v.P_Ultimate1, playerID) << (500)
    # (Line 30) v.P_Ultimate2[playerID] = 250;
    _ARRW(v.P_Ultimate2, playerID) << (250)
    # (Line 32) SkillList(playerID);
    SkillList(playerID)
    # (Line 33) commend.main(playerID);
    commend.f_main(playerID)
    # (Line 35) if (v.P_SkillDelay[playerID] == 0)
    if EUDIf()(v.P_SkillDelay[playerID] == 0):
        # (Line 36) {
        # (Line 37) switch(v.P_Step[playerID])
        EUDSwitch(v.P_Step[playerID])
        # (Line 38) {
        # (Line 39) case 1:
        _t2 = EUDSwitchCase()
        # (Line 40) O.main(playerID);
        if _t2(1):
            O.f_main(playerID)
            # (Line 41) break;
            EUDBreak()
            # (Line 42) case 100:
        _t3 = EUDSwitchCase()
        # (Line 43) S.main(playerID);
        if _t3(100):
            S.f_main(playerID)
            # (Line 44) break;
            EUDBreak()
            # (Line 45) case 200:
        _t4 = EUDSwitchCase()
        # (Line 46) C.main(playerID);
        if _t4(200):
            C.f_main(playerID)
            # (Line 47) break;
            EUDBreak()
            # (Line 48) case 300:
        _t5 = EUDSwitchCase()
        # (Line 49) A.main(playerID);
        if _t5(300):
            A.f_main(playerID)
            # (Line 50) break;
            EUDBreak()
            # (Line 51) case 110:
        _t6 = EUDSwitchCase()
        # (Line 52) SSS.main(playerID);
        if _t6(110):
            SSS.f_main(playerID)
            # (Line 53) break;
            EUDBreak()
            # (Line 54) case 310:
        _t7 = EUDSwitchCase()
        # (Line 55) AAS.main(playerID);
        if _t7(310):
            AAS.f_main(playerID)
            # (Line 56) break;
            EUDBreak()
            # (Line 57) case 210:
        _t8 = EUDSwitchCase()
        # (Line 58) CCC.main(playerID);
        if _t8(210):
            CCC.f_main(playerID)
            # (Line 59) break;
            EUDBreak()
            # (Line 60) case 220:
        _t9 = EUDSwitchCase()
        # (Line 61) CCCAS.main(playerID);
        if _t9(220):
            CCCAS.f_main(playerID)
            # (Line 62) break;
            EUDBreak()
            # (Line 63) case 230:
        _t10 = EUDSwitchCase()
        # (Line 64) CCCASCC.main(playerID);
        if _t10(230):
            CCCASCC.f_main(playerID)
            # (Line 65) break;
            EUDBreak()
            # (Line 66) case 320:
        _t11 = EUDSwitchCase()
        # (Line 67) AAA.main(playerID);
        if _t11(320):
            AAA.f_main(playerID)
            # (Line 68) break;
            EUDBreak()
            # (Line 69) case 330:
        _t12 = EUDSwitchCase()
        # (Line 70) AAAAA.main(playerID);
        if _t12(330):
            AAAAA.f_main(playerID)
            # (Line 71) break;
            EUDBreak()
            # (Line 73) }
        # (Line 74) }
        EUDEndSwitch()
        # (Line 78) }
    EUDEndIf()
    # (Line 80) function SkillList(playerID)

# (Line 81) {
@EUDFunc
def SkillList(playerID):
    # (Line 82) if(Memory(0x00596A44, Exactly, 256)) 	// Insert key Pressed
    if EUDIf()(Memory(0x00596A44, Exactly, 256)):
        # (Line 83) {
        # (Line 84) v.stb.printAt(0, "\n");
        v.stb.printAt(0, "\n")
        # (Line 85) v.stb.printAt(1, "\x1F　＃\x1A- 시이나 마유리　\x04[ 슈타인즈 게이트 ]");
        v.stb.printAt(1, "\x1F　＃\x1A- 시이나 마유리　\x04[ 슈타인즈 게이트 ]")
        # (Line 86) v.stb.printAt(2, "　　\x1FA\x04ction List");
        v.stb.printAt(2, "　　\x1FA\x04ction List")
        # (Line 87) v.stb.printAt(3, "　　　\x18O \x04무한원점의 알타이르 \x19[ 15초 동안 팀 전체 마나 회복 + 20 ] \x051분 30초");
        v.stb.printAt(3, "　　　\x18O \x04무한원점의 알타이르 \x19[ 15초 동안 팀 전체 마나 회복 + 20 ] \x051분 30초")
        # (Line 88) v.stb.printAt(4, "　　　\x04\x1FSSS \x04뚯뚜루~ \x19[ 대인 / 순간딜 ]");
        v.stb.printAt(4, "　　　\x04\x1FSSS \x04뚯뚜루~ \x19[ 대인 / 순간딜 ]")
        # (Line 89) v.stb.printAt(5, "　　　\x04\x1FCCC + AS + CC \x04비익연리의 달링 \x19[ 대인 / 지속딜 / CCC + AS - 자리고정 / 쉴드고정 1 ]");
        v.stb.printAt(5, "　　　\x04\x1FCCC + AS + CC \x04비익연리의 달링 \x19[ 대인 / 지속딜 / CCC + AS - 자리고정 / 쉴드고정 1 ]")
        # (Line 90) v.stb.printAt(6, "　　　\x04\x1FAA \x04무한원점의 아크라이트 \x19[ 대인 / 순간딜 / 쉴드고정 1 ]");
        v.stb.printAt(6, "　　　\x04\x1FAA \x04무한원점의 아크라이트 \x19[ 대인 / 순간딜 / 쉴드고정 1 ]")
        # (Line 91) v.stb.printAt(7, "\n");
        v.stb.printAt(7, "\n")
        # (Line 92) v.stb.printAt(8, "　　　\x08CAA \x04교차좌표의 스타더스트 \x19[ 대인 / 자리고정 ] \x05", v.P_Ultimate1[playerID]);
        v.stb.printAt(8, "　　　\x08CAA \x04교차좌표의 스타더스트 \x19[ 대인 / 자리고정 ] \x05", v.P_Ultimate1[playerID])
        # (Line 93) v.stb.printAt(9, "　　　\x04+ \x08AA \x04슈타인즈 게이트 \x19[ 공성 / 자리고정 ] \x05", v.P_Ultimate2[playerID]);
        v.stb.printAt(9, "　　　\x04+ \x08AA \x04슈타인즈 게이트 \x19[ 공성 / 자리고정 ] \x05", v.P_Ultimate2[playerID])
        # (Line 94) v.stb.printAt(10, "\n");
        v.stb.printAt(10, "\n")
        # (Line 95) PlayWAV("sound\\Bullet\\LaserHit.wav");
        # (Line 96) }
        DoActions(PlayWAV("sound\\Bullet\\LaserHit.wav"))
        # (Line 97) }
    EUDEndIf()