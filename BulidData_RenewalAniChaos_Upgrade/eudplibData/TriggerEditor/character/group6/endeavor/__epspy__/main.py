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
# (Line 4) import character.group6.endeavor.commend as commend;
from character.group6.endeavor import commend as commend
# (Line 6) import character.group6.endeavor.common.skill1 as O;
from character.group6.endeavor.common import skill1 as O
# (Line 7) import character.group6.endeavor.common.skill2 as S;
from character.group6.endeavor.common import skill2 as S
# (Line 8) import character.group6.endeavor.common.skill3 as C;
from character.group6.endeavor.common import skill3 as C
# (Line 9) import character.group6.endeavor.common.skill4 as A;
from character.group6.endeavor.common import skill4 as A
# (Line 11) import character.group6.endeavor.combo.combo1 as SSS;
from character.group6.endeavor.combo import combo1 as SSS
# (Line 12) import character.group6.endeavor.combo.combo2 as CCCC;
from character.group6.endeavor.combo import combo2 as CCCC
# (Line 13) import character.group6.endeavor.combo.combo3 as AACC;
from character.group6.endeavor.combo import combo3 as AACC
# (Line 14) import character.group6.endeavor.combo.combo4 as AACCCAAA;
from character.group6.endeavor.combo import combo4 as AACCCAAA
# (Line 16) import character.group6.endeavor.ultimate.ultimate1 as AAAA;
from character.group6.endeavor.ultimate import ultimate1 as AAAA
# (Line 17) function skillList(playerID)
# (Line 18) {
@EUDFunc
def f_skillList(playerID):
    # (Line 19) if(Memory(0x00596A44, Exactly, 256)) 	// Insert key Pressed
    if EUDIf()(Memory(0x00596A44, Exactly, 256)):
        # (Line 20) {
        # (Line 21) v.stb.printAt(0, "\n");
        v.stb.printAt(0, "\n")
        # (Line 22) v.stb.printAt(1, "\x1F　＃\x04- 엔데버　\x04[ 나의 히어로 아카데미아 ]");
        v.stb.printAt(1, "\x1F　＃\x04- 엔데버　\x04[ 나의 히어로 아카데미아 ]")
        # (Line 23) v.stb.printAt(2, "　　\x1FA\x04ction List");
        v.stb.printAt(2, "　　\x1FA\x04ction List")
        # (Line 24) v.stb.printAt(3, "　　　\x18O \x04혁작열권 \x19[ 15초 간 방어력 15 상승 ] \x051분 30초");
        v.stb.printAt(3, "　　　\x18O \x04혁작열권 \x19[ 15초 간 방어력 15 상승 ] \x051분 30초")
        # (Line 25) v.stb.printAt(4, "　　　\x04\x1FSSS \x04이상 \x19[ 공성 ]");
        v.stb.printAt(4, "　　　\x04\x1FSSS \x04이상 \x19[ 공성 ]")
        # (Line 26) v.stb.printAt(5, "　　　\x04\x1FCCC \x04강함 \x19[ 공성 / 자리고정 ]");
        v.stb.printAt(5, "　　　\x04\x1FCCC \x04강함 \x19[ 공성 / 자리고정 ]")
        # (Line 27) v.stb.printAt(6, "　　　\x04\x1FAACC + 200 Gas + CAAA \x04최대출력 \x19[ 공성 ] \x1F[1]");
        v.stb.printAt(6, "　　　\x04\x1FAACC + 200 Gas + CAAA \x04최대출력 \x19[ 공성 ] \x1F[1]")
        # (Line 28) v.stb.printAt(7, "\n");
        v.stb.printAt(7, "\n")
        # (Line 29) v.stb.printAt(8, "　　　\x08AAAA \x04교훈 \x19[ 공성 / 자리고정 / 쉴드 1고정] \x05", v.P_Ultimate1[playerID]);
        v.stb.printAt(8, "　　　\x08AAAA \x04교훈 \x19[ 공성 / 자리고정 / 쉴드 1고정] \x05", v.P_Ultimate1[playerID])
        # (Line 30) v.stb.printAt(9, "　　　\x08 \x1F[1] + \x08O \x04교훈 \x19[ 공성 / 장판형 / 쉴드 1고정 / 자리고정 ] \x05", v.P_Ultimate2[playerID]);
        v.stb.printAt(9, "　　　\x08 \x1F[1] + \x08O \x04교훈 \x19[ 공성 / 장판형 / 쉴드 1고정 / 자리고정 ] \x05", v.P_Ultimate2[playerID])
        # (Line 31) v.stb.printAt(10, "\n");
        v.stb.printAt(10, "\n")
        # (Line 32) PlayWAV("sound\\Bullet\\LaserHit.wav");
        # (Line 33) }
        DoActions(PlayWAV("sound\\Bullet\\LaserHit.wav"))
        # (Line 34) }
    EUDEndIf()
    # (Line 36) function main(playerID)

# (Line 37) {
@EUDFunc
def f_main(playerID):
    # (Line 38) v.P_HeroID[playerID] 		= 35;
    _ARRW(v.P_HeroID, playerID) << (35)
    # (Line 39) v.P_UnitID[playerID] 			= 10;
    _ARRW(v.P_UnitID, playerID) << (10)
    # (Line 40) v.P_LocationID[playerID] 		= 205;
    _ARRW(v.P_LocationID, playerID) << (205)
    # (Line 42) v.P_Ultimate1[playerID] = 650;
    _ARRW(v.P_Ultimate1, playerID) << (650)
    # (Line 43) v.P_Ultimate2[playerID] = 650;
    _ARRW(v.P_Ultimate2, playerID) << (650)
    # (Line 46) commend.main(playerID);
    commend.f_main(playerID)
    # (Line 47) skillList(playerID);
    f_skillList(playerID)
    # (Line 50) if (v.P_SkillDelay[playerID] == 0)
    if EUDIf()(v.P_SkillDelay[playerID] == 0):
        # (Line 51) {
        # (Line 52) switch(v.P_Step[playerID])
        EUDSwitch(v.P_Step[playerID])
        # (Line 53) {
        # (Line 54) case 1:
        _t2 = EUDSwitchCase()
        # (Line 55) O.main(playerID);
        if _t2(1):
            O.f_main(playerID)
            # (Line 56) break;
            EUDBreak()
            # (Line 57) case 100:
        _t3 = EUDSwitchCase()
        # (Line 58) S.main(playerID);
        if _t3(100):
            S.f_main(playerID)
            # (Line 59) break;
            EUDBreak()
            # (Line 60) case 200:
        _t4 = EUDSwitchCase()
        # (Line 61) C.main(playerID);
        if _t4(200):
            C.f_main(playerID)
            # (Line 62) break;
            EUDBreak()
            # (Line 63) case 300:
        _t5 = EUDSwitchCase()
        # (Line 64) A.main(playerID);
        if _t5(300):
            A.f_main(playerID)
            # (Line 65) break;
            EUDBreak()
            # (Line 66) case 110:
        _t6 = EUDSwitchCase()
        # (Line 67) SSS.main(playerID);
        if _t6(110):
            SSS.f_main(playerID)
            # (Line 68) break;
            EUDBreak()
            # (Line 69) case 210:
        _t7 = EUDSwitchCase()
        # (Line 70) CCCC.main(playerID);
        if _t7(210):
            CCCC.f_main(playerID)
            # (Line 71) break;
            EUDBreak()
            # (Line 72) case 310:
        _t8 = EUDSwitchCase()
        # (Line 73) AACC.main(playerID);
        if _t8(310):
            AACC.f_main(playerID)
            # (Line 74) break;
            EUDBreak()
            # (Line 75) case 320:
        _t9 = EUDSwitchCase()
        # (Line 76) AACCCAAA.main(playerID);
        if _t9(320):
            AACCCAAA.f_main(playerID)
            # (Line 77) break;
            EUDBreak()
            # (Line 78) case 330:
        _t10 = EUDSwitchCase()
        # (Line 79) AAAA.main(playerID);
        if _t10(330):
            AAAA.f_main(playerID)
            # (Line 80) break;
            EUDBreak()
            # (Line 81) }
        # (Line 82) }
        EUDEndSwitch()
        # (Line 84) }
    EUDEndIf()