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
# (Line 3) import Character.Nanami.Skill_O as O;
from Character.Nanami import Skill_O as O
# (Line 4) import Character.Nanami.Skill_S as S;
from Character.Nanami import Skill_S as S
# (Line 5) import Character.Nanami.Skill_C as C;
from Character.Nanami import Skill_C as C
# (Line 6) import Character.Nanami.Skill_A as A;
from Character.Nanami import Skill_A as A
# (Line 7) import Character.Nanami.Skill_SSS as SSS;
from Character.Nanami import Skill_SSS as SSS
# (Line 8) import Character.Nanami.Skill_CCC as CCC;
from Character.Nanami import Skill_CCC as CCC
# (Line 9) import Character.Nanami.Skill_CCCAA as CCCAA;
from Character.Nanami import Skill_CCCAA as CCCAA
# (Line 10) import Character.Nanami.Skill_CCA as CCA;
from Character.Nanami import Skill_CCA as CCA
# (Line 11) import Character.Nanami.Skill_CCAAA as CCAAA;
from Character.Nanami import Skill_CCAAA as CCAAA
# (Line 12) import Character.Nanami.Skill_CCAAAAA as CCAAAAA;
from Character.Nanami import Skill_CCAAAAA as CCAAAAA
# (Line 13) import Character.Nanami.Skill_Ult1 as Ult1;
from Character.Nanami import Skill_Ult1 as Ult1
# (Line 14) import Character.Nanami.Skill_Ult2 as Ult2;
from Character.Nanami import Skill_Ult2 as Ult2
# (Line 16) import Character.Nanami.Text as text;
from Character.Nanami import Text as text
# (Line 17) import Character.Nanami.Commend as commend;
from Character.Nanami import Commend as commend
# (Line 19) const stb = StringBuffer();
stb = _CGFW(lambda: [StringBuffer()], 1)[0]
# (Line 20) const s = StringBuffer();
s = _CGFW(lambda: [StringBuffer()], 1)[0]
# (Line 21) function SkillList(cp);
# (Line 23) function main(cp)
# (Line 24) {
@EUDFunc
def f_main(cp):
    # (Line 25) f.location[cp] = 185;
    _ARRW(f.location, cp) << (185)
    # (Line 26) f.heroID[cp] = 64;
    _ARRW(f.heroID, cp) << (64)
    # (Line 28) f.UltimateA[cp] = 700;
    _ARRW(f.UltimateA, cp) << (700)
    # (Line 29) f.UltimateB[cp] = 500;
    _ARRW(f.UltimateB, cp) << (500)
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
            # (Line 53) case 210:
        _t7 = EUDSwitchCase()
        # (Line 54) CCC.main(cp);
        if _t7(210):
            CCC.f_main(cp)
            # (Line 55) break;
            EUDBreak()
            # (Line 56) case 220:
        _t8 = EUDSwitchCase()
        # (Line 57) CCCAA.main(cp);
        if _t8(220):
            CCCAA.f_main(cp)
            # (Line 58) break;
            EUDBreak()
            # (Line 59) case 230:
        _t9 = EUDSwitchCase()
        # (Line 60) CCA.main(cp);
        if _t9(230):
            CCA.f_main(cp)
            # (Line 61) break;
            EUDBreak()
            # (Line 62) case 240:
        _t10 = EUDSwitchCase()
        # (Line 63) CCAAA.main(cp);
        if _t10(240):
            CCAAA.f_main(cp)
            # (Line 64) break;
            EUDBreak()
            # (Line 65) case 250:
        _t11 = EUDSwitchCase()
        # (Line 66) CCAAAAA.main(cp);
        if _t11(250):
            CCAAAAA.f_main(cp)
            # (Line 67) break;
            EUDBreak()
            # (Line 68) case 260:
        _t12 = EUDSwitchCase()
        # (Line 69) Ult1.main(cp);
        if _t12(260):
            Ult1.f_main(cp)
            # (Line 70) break;
            EUDBreak()
            # (Line 71) case 310:
        _t13 = EUDSwitchCase()
        # (Line 72) Ult2.main(cp);
        if _t13(310):
            Ult2.f_main(cp)
            # (Line 73) break;
            EUDBreak()
            # (Line 74) }
        # (Line 75) }
        EUDEndSwitch()
        # (Line 79) }
    EUDEndIf()
    # (Line 82) function SkillVoice(cp)

# (Line 83) {
@EUDFunc
def SkillVoice(cp):
    # (Line 84) if (f.Nanami_Voice[cp] != 0) { text.main(cp); }
    if EUDIf()(f.Nanami_Voice[cp] == 0, neg=True):
        text.f_main(cp)
        # (Line 85) }
    EUDEndIf()
    # (Line 87) function SkillList(cp)

# (Line 88) {
@EUDFunc
def SkillList(cp):
    # (Line 89) if(f.INSERT_KEY[cp] == 1) 	// Insert key Pressed
    if EUDIf()(f.INSERT_KEY[cp] == 1):
        # (Line 90) {
        # (Line 91) stb.printAt(0, "\n");
        stb.printAt(0, "\n")
        # (Line 92) stb.printAt(1, "\x1F　＃\x1B- 나나미 치아키　\x04[ 단간론파 ]");
        stb.printAt(1, "\x1F　＃\x1B- 나나미 치아키　\x04[ 단간론파 ]")
        # (Line 93) stb.printAt(2, "　　\x1FA\x04ction List");
        stb.printAt(2, "　　\x1FA\x04ction List")
        # (Line 94) stb.printAt(3, "　　　\x17Passive \x04초고교급 게이머 \x19[ 아군 마나 회복 증가 +5 ]");
        stb.printAt(3, "　　　\x17Passive \x04초고교급 게이머 \x19[ 아군 마나 회복 증가 +5 ]")
        # (Line 95) stb.printAt(4, "　　　\x18O \x04모두의 힘 \x19[ 1분 간 아군 공 방 증가 +5 ] \x053분");
        stb.printAt(4, "　　　\x18O \x04모두의 힘 \x19[ 1분 간 아군 공 방 증가 +5 ] \x053분")
        # (Line 96) stb.printAt(5, "　　　\x04\x1FSSS \x04발상 \x19[ 만능 ]");
        stb.printAt(5, "　　　\x04\x1FSSS \x04발상 \x19[ 만능 ]")
        # (Line 97) stb.printAt(6, "　　　\x04\x1FACC+ CA \x04필살기 \x19[ 만능 / 자리고정 ]");
        stb.printAt(6, "　　　\x04\x1FACC+ CA \x04필살기 \x19[ 만능 / 자리고정 ]")
        # (Line 98) stb.printAt(7, "　　　\x04\x1FCCC + AA + AA \x04응원 \x19[ 공성 / 자리고정 / 15 x 15 아군 공 방 증가 +5 ] \x1F[1]");
        stb.printAt(7, "　　　\x04\x1FCCC + AA + AA \x04응원 \x19[ 공성 / 자리고정 / 15 x 15 아군 공 방 증가 +5 ] \x1F[1]")
        # (Line 99) stb.printAt(8, "\n");
        stb.printAt(8, "\n")
        # (Line 100) stb.printAt(9, "　　　\x1F[1] + \x08O \x04클래스메이트 \x19[ 공성 / 자리고정 ] \x05", f.UltimateA[cp]);
        stb.printAt(9, "　　　\x1F[1] + \x08O \x04클래스메이트 \x19[ 공성 / 자리고정 ] \x05", f.UltimateA[cp])
        # (Line 101) stb.printAt(10, "　　　\x08AAA \x04격려 \x19[ 서포트 / 아군 궁게이지 +250 ] \x05", f.UltimateB[cp]);
        stb.printAt(10, "　　　\x08AAA \x04격려 \x19[ 서포트 / 아군 궁게이지 +250 ] \x05", f.UltimateB[cp])
        # (Line 102) PlayWAV("sound\\Bullet\\LaserHit.wav");
        # (Line 103) f.INSERT_KEY[cp] = 0;
        DoActions(PlayWAV("sound\\Bullet\\LaserHit.wav"))
        _ARRW(f.INSERT_KEY, cp) << (0)
        # (Line 104) }
        # (Line 105) }
    EUDEndIf()