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
# (Line 5) import character.group4.milim.common.skill1 as O;
from character.group4.milim.common import skill1 as O
# (Line 6) import character.group4.milim.common.skill2 as S;
from character.group4.milim.common import skill2 as S
# (Line 7) import character.group4.milim.common.skill3 as C;
from character.group4.milim.common import skill3 as C
# (Line 8) import character.group4.milim.common.skill4 as A;
from character.group4.milim.common import skill4 as A
# (Line 10) import character.group4.milim.combo.combo1 as SSS;
from character.group4.milim.combo import combo1 as SSS
# (Line 11) import character.group4.milim.combo.combo2 as CCAA;
from character.group4.milim.combo import combo2 as CCAA
# (Line 12) import character.group4.milim.combo.combo3 as CCC;
from character.group4.milim.combo import combo3 as CCC
# (Line 14) import character.group4.milim.ultimate.ultimate1 as AAAA;
from character.group4.milim.ultimate import ultimate1 as AAAA
# (Line 16) import character.group4.milim.text as text;
from character.group4.milim import text as text
# (Line 17) import character.group4.milim.commend as commend;
from character.group4.milim import commend as commend
# (Line 19) function SkillList(playerID);
# (Line 21) function main(playerID)
# (Line 22) {
@EUDFunc
def f_main(playerID):
    # (Line 23) v.P_HeroID[playerID] = 25;
    _ARRW(v.P_HeroID, playerID) << (25)
    # (Line 24) v.P_LocationID[playerID] = 188;
    _ARRW(v.P_LocationID, playerID) << (188)
    # (Line 25) v.P_UnitID[playerID] = 54;
    _ARRW(v.P_UnitID, playerID) << (54)
    # (Line 27) v.P_Ultimate1[playerID] = 650;
    _ARRW(v.P_Ultimate1, playerID) << (650)
    # (Line 29) SkillList(playerID);
    SkillList(playerID)
    # (Line 30) commend.main(playerID);
    commend.f_main(playerID)
    # (Line 32) if (v.P_SkillDelay[playerID] == 0)
    if EUDIf()(v.P_SkillDelay[playerID] == 0):
        # (Line 33) {
        # (Line 34) switch(v.P_Step[playerID])
        EUDSwitch(v.P_Step[playerID])
        # (Line 35) {
        # (Line 36) case 1:
        _t2 = EUDSwitchCase()
        # (Line 37) O.main(playerID);
        if _t2(1):
            O.f_main(playerID)
            # (Line 38) break;
            EUDBreak()
            # (Line 39) case 100:
        _t3 = EUDSwitchCase()
        # (Line 40) S.main(playerID);
        if _t3(100):
            S.f_main(playerID)
            # (Line 41) break;
            EUDBreak()
            # (Line 42) case 200:
        _t4 = EUDSwitchCase()
        # (Line 43) C.main(playerID);
        if _t4(200):
            C.f_main(playerID)
            # (Line 44) break;
            EUDBreak()
            # (Line 45) case 300:
        _t5 = EUDSwitchCase()
        # (Line 46) A.main(playerID);
        if _t5(300):
            A.f_main(playerID)
            # (Line 47) break;
            EUDBreak()
            # (Line 48) case 110:
        _t6 = EUDSwitchCase()
        # (Line 49) SSS.main(playerID);
        if _t6(110):
            SSS.f_main(playerID)
            # (Line 50) break;
            EUDBreak()
            # (Line 51) case 210:
        _t7 = EUDSwitchCase()
        # (Line 52) CCAA.main(playerID);
        if _t7(210):
            CCAA.f_main(playerID)
            # (Line 53) break;
            EUDBreak()
            # (Line 54) case 220:
        _t8 = EUDSwitchCase()
        # (Line 55) CCC.main(playerID);
        if _t8(220):
            CCC.f_main(playerID)
            # (Line 56) break;
            EUDBreak()
            # (Line 57) case 310:
        _t9 = EUDSwitchCase()
        # (Line 58) AAAA.main(playerID);
        if _t9(310):
            AAAA.f_main(playerID)
            # (Line 59) break;
            EUDBreak()
            # (Line 61) }
        # (Line 62) }
        EUDEndSwitch()
        # (Line 66) }
    EUDEndIf()
    # (Line 68) function SkillList(playerID)

# (Line 69) {
@EUDFunc
def SkillList(playerID):
    # (Line 70) if(Memory(0x00596A44, Exactly, 256)) 	// Insert key Pressed
    if EUDIf()(Memory(0x00596A44, Exactly, 256)):
        # (Line 71) {
        # (Line 72) v.stb.printAt(0, "\n");
        v.stb.printAt(0, "\n")
        # (Line 73) v.stb.printAt(1, "\x1F　＃\x1B- 밀림 나바　\x04[ 전생했더니 슬라임이었던 건에 대하여 ]");
        v.stb.printAt(1, "\x1F　＃\x1B- 밀림 나바　\x04[ 전생했더니 슬라임이었던 건에 대하여 ]")
        # (Line 74) v.stb.printAt(2, "　　\x1FA\x04ction List");
        v.stb.printAt(2, "　　\x1FA\x04ction List")
        # (Line 75) v.stb.printAt(3, "　　　\x18O \x04파괴의 폭군 \x19[ 순간딜 / 상대 건물에 닿을 때까지 일직선 대시 / 일반기 자리고정 해제 25초 ] \x052분");
        v.stb.printAt(3, "　　　\x18O \x04파괴의 폭군 \x19[ 순간딜 / 상대 건물에 닿을 때까지 일직선 대시 / 일반기 자리고정 해제 25초 ] \x052분")
        # (Line 76) v.stb.printAt(4, "　　　\x04\x1FSSS \x04즐거움 \x19[ 만능 ]");
        v.stb.printAt(4, "　　　\x04\x1FSSS \x04즐거움 \x19[ 만능 ]")
        # (Line 77) v.stb.printAt(5, "　　　\x04\x1FCCC \x04여유 \x19[ 공성 / 자리고정 ]");
        v.stb.printAt(5, "　　　\x04\x1FCCC \x04여유 \x19[ 공성 / 자리고정 ]")
        # (Line 78) v.stb.printAt(6, "　　　\x04\x1FCCAA \x04나의 차례! \x19[ 공성 / 자리고정 ]");
        v.stb.printAt(6, "　　　\x04\x1FCCAA \x04나의 차례! \x19[ 공성 / 자리고정 ]")
        # (Line 79) v.stb.printAt(7, "\n");
        v.stb.printAt(7, "\n")
        # (Line 80) v.stb.printAt(8, "　　　\x08AAAA \x04드래곤 버스트 \x19[ 공성 / 선딜 7초 / 자리고정 ] \x05", v.P_Ultimate1[playerID]);
        v.stb.printAt(8, "　　　\x08AAAA \x04드래곤 버스트 \x19[ 공성 / 선딜 7초 / 자리고정 ] \x05", v.P_Ultimate1[playerID])
        # (Line 81) v.stb.printAt(9, "\n");
        v.stb.printAt(9, "\n")
        # (Line 82) PlayWAV("sound\\Bullet\\LaserHit.wav");
        # (Line 83) }
        DoActions(PlayWAV("sound\\Bullet\\LaserHit.wav"))
        # (Line 84) }
    EUDEndIf()
