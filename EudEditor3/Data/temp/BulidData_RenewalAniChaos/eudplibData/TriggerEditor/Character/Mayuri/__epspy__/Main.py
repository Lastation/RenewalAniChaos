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

# (Line 1) import Function as f;
import Function as f
# (Line 3) import Character.Mayuri.Skill_O as O;
from Character.Mayuri import Skill_O as O
# (Line 4) import Character.Mayuri.Skill_S as S;
from Character.Mayuri import Skill_S as S
# (Line 5) import Character.Mayuri.Skill_C as C;
from Character.Mayuri import Skill_C as C
# (Line 6) import Character.Mayuri.Skill_A as A;
from Character.Mayuri import Skill_A as A
# (Line 8) import Character.Mayuri.Skill_SSS as SSS;
from Character.Mayuri import Skill_SSS as SSS
# (Line 9) import Character.Mayuri.Skill_AAS as AAS;
from Character.Mayuri import Skill_AAS as AAS
# (Line 10) import Character.Mayuri.Skill_CCC as CCC;
from Character.Mayuri import Skill_CCC as CCC
# (Line 11) import Character.Mayuri.Skill_CCCAA as CCCAA;
from Character.Mayuri import Skill_CCCAA as CCCAA
# (Line 12) import Character.Mayuri.Skill_CCCAAAA as CCCAAAA;
from Character.Mayuri import Skill_CCCAAAA as CCCAAAA
# (Line 13) import Character.Mayuri.Skill_AAA as AAA;
from Character.Mayuri import Skill_AAA as AAA
# (Line 14) import Character.Mayuri.Skill_AAAAA as AAAAA;
from Character.Mayuri import Skill_AAAAA as AAAAA
# (Line 16) import Character.Mayuri.Text as text;
from Character.Mayuri import Text as text
# (Line 17) import Character.Mayuri.Commend as commend;
from Character.Mayuri import Commend as commend
# (Line 19) const stb = StringBuffer();
stb = _CGFW(lambda: [StringBuffer()], 1)[0]
# (Line 20) const s = StringBuffer();
s = _CGFW(lambda: [StringBuffer()], 1)[0]
# (Line 21) function SkillList(cp);
# (Line 23) function main(cp)
# (Line 24) {
@EUDFunc
def f_main(cp):
    # (Line 25) f.location[cp] = 183;
    _ARRW(f.location, cp) << (183)
    # (Line 26) f.heroID[cp] = 64;
    _ARRW(f.heroID, cp) << (64)
    # (Line 28) f.UltimateA[cp] = 500;
    _ARRW(f.UltimateA, cp) << (500)
    # (Line 29) f.UltimateB[cp] = 250;
    _ARRW(f.UltimateB, cp) << (250)
    # (Line 31) SkillList(cp);
    SkillList(cp)
    # (Line 32) commend.main(cp);
    commend.f_main(cp)
    # (Line 34) if (f.wait[cp] == 0)
    if EUDIf()(f.wait[cp] == 0):
        # (Line 35) {
        # (Line 36) switch(f.step[cp])
        EUDSwitch(f.step[cp])
        # (Line 37) {
        # (Line 38) case 1:
        _t2 = EUDSwitchCase()
        # (Line 39) O.main(cp);
        if _t2(1):
            O.f_main(cp)
            # (Line 40) break;
            EUDBreak()
            # (Line 41) case 100:
        _t3 = EUDSwitchCase()
        # (Line 42) S.main(cp);
        if _t3(100):
            S.f_main(cp)
            # (Line 43) break;
            EUDBreak()
            # (Line 44) case 200:
        _t4 = EUDSwitchCase()
        # (Line 45) C.main(cp);
        if _t4(200):
            C.f_main(cp)
            # (Line 46) break;
            EUDBreak()
            # (Line 47) case 300:
        _t5 = EUDSwitchCase()
        # (Line 48) A.main(cp);
        if _t5(300):
            A.f_main(cp)
            # (Line 49) break;
            EUDBreak()
            # (Line 50) case 110:
        _t6 = EUDSwitchCase()
        # (Line 51) SSS.main(cp);
        if _t6(110):
            SSS.f_main(cp)
            # (Line 52) break;
            EUDBreak()
            # (Line 53) case 310:
        _t7 = EUDSwitchCase()
        # (Line 54) AAS.main(cp);
        if _t7(310):
            AAS.f_main(cp)
            # (Line 55) break;
            EUDBreak()
            # (Line 56) case 210:
        _t8 = EUDSwitchCase()
        # (Line 57) CCC.main(cp);
        if _t8(210):
            CCC.f_main(cp)
            # (Line 58) break;
            EUDBreak()
            # (Line 59) case 220:
        _t9 = EUDSwitchCase()
        # (Line 60) CCCAA.main(cp);
        if _t9(220):
            CCCAA.f_main(cp)
            # (Line 61) break;
            EUDBreak()
            # (Line 62) case 230:
        _t10 = EUDSwitchCase()
        # (Line 63) CCCAAAA.main(cp);
        if _t10(230):
            CCCAAAA.f_main(cp)
            # (Line 64) break;
            EUDBreak()
            # (Line 65) case 320:
        _t11 = EUDSwitchCase()
        # (Line 66) AAA.main(cp);
        if _t11(320):
            AAA.f_main(cp)
            # (Line 67) break;
            EUDBreak()
            # (Line 68) case 330:
        _t12 = EUDSwitchCase()
        # (Line 69) AAAAA.main(cp);
        if _t12(330):
            AAAAA.f_main(cp)
            # (Line 70) break;
            EUDBreak()
            # (Line 72) }
        # (Line 73) }
        EUDEndSwitch()
        # (Line 77) }
    EUDEndIf()
    # (Line 80) function SkillVoice(cp)

# (Line 81) {
@EUDFunc
def SkillVoice(cp):
    # (Line 82) if (f.Mayuri_Voice[cp] != 0) { text.main(cp); }
    if EUDIf()(f.Mayuri_Voice[cp] == 0, neg=True):
        text.f_main(cp)
        # (Line 83) }
    EUDEndIf()
    # (Line 85) function SkillList(cp)

# (Line 86) {
@EUDFunc
def SkillList(cp):
    # (Line 87) if(f.INSERT_KEY[cp] == 1) 	// Insert key Pressed
    if EUDIf()(f.INSERT_KEY[cp] == 1):
        # (Line 88) {
        # (Line 89) stb.printAt(0, "\n");
        stb.printAt(0, "\n")
        # (Line 90) stb.printAt(1, "\x1F　＃\x04- 시이나 \x1B마유리　\x04[ 슈타인즈 게이트 ]");
        stb.printAt(1, "\x1F　＃\x04- 시이나 \x1B마유리　\x04[ 슈타인즈 게이트 ]")
        # (Line 91) stb.printAt(2, "　　\x1FA\x04ction List");
        stb.printAt(2, "　　\x1FA\x04ction List")
        # (Line 92) stb.printAt(3, "　　　\x18O \x04무한원점의 알타이르 \x19[ 15초 동안 팀 전체 마나 회복 + 20 ] \x051분 30초");
        stb.printAt(3, "　　　\x18O \x04무한원점의 알타이르 \x19[ 15초 동안 팀 전체 마나 회복 + 20 ] \x051분 30초")
        # (Line 93) stb.printAt(4, "　　　\x04\x1FSSS \x04뚯뚜루~ \x19[ 대인 / 순간딜 ]");
        stb.printAt(4, "　　　\x04\x1FSSS \x04뚯뚜루~ \x19[ 대인 / 순간딜 ]")
        # (Line 94) stb.printAt(5, "　　　\x04\x1FCCA + CC + CC \x04비익연리의 달링 \x19[ 대인 / 지속딜 / 자리고정 / 쉴드고정 1 ]");
        stb.printAt(5, "　　　\x04\x1FCCA + CC + CC \x04비익연리의 달링 \x19[ 대인 / 지속딜 / 자리고정 / 쉴드고정 1 ]")
        # (Line 95) stb.printAt(6, "　　　\x04\x1FAA \x04무한원점의 아크라이트 \x19[ 대인 / 순간딜 / 쉴드고정 1 ]");
        stb.printAt(6, "　　　\x04\x1FAA \x04무한원점의 아크라이트 \x19[ 대인 / 순간딜 / 쉴드고정 1 ]")
        # (Line 96) stb.printAt(7, "\n");
        stb.printAt(7, "\n")
        # (Line 97) stb.printAt(8, "　　　\x08CAA \x04교차좌표의 스타더스트 \x19[ 대인 / 자리고정 ] \x05", f.UltimateA[cp]);
        stb.printAt(8, "　　　\x08CAA \x04교차좌표의 스타더스트 \x19[ 대인 / 자리고정 ] \x05", f.UltimateA[cp])
        # (Line 98) stb.printAt(9, "　　　\x04+ \x08AA \x04슈타인즈 게이트 \x19[ 공성 / 자리고정 ] \x05", f.UltimateB[cp]);
        stb.printAt(9, "　　　\x04+ \x08AA \x04슈타인즈 게이트 \x19[ 공성 / 자리고정 ] \x05", f.UltimateB[cp])
        # (Line 99) stb.printAt(10, "\n");
        stb.printAt(10, "\n")
        # (Line 100) PlayWAV("sound\\Bullet\\LaserHit.wav");
        # (Line 101) f.INSERT_KEY[cp] = 0;
        DoActions(PlayWAV("sound\\Bullet\\LaserHit.wav"))
        _ARRW(f.INSERT_KEY, cp) << (0)
        # (Line 102) }
        # (Line 103) }
    EUDEndIf()