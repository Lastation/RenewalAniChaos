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
# (Line 3) import Character.Ekidona.Skill_O as O;
from Character.Ekidona import Skill_O as O
# (Line 4) import Character.Ekidona.Skill_S as S;
from Character.Ekidona import Skill_S as S
# (Line 5) import Character.Ekidona.Skill_C as C;
from Character.Ekidona import Skill_C as C
# (Line 6) import Character.Ekidona.Skill_A as A;
from Character.Ekidona import Skill_A as A
# (Line 8) import Character.Ekidona.Skill_SSS as SSS;
from Character.Ekidona import Skill_SSS as SSS
# (Line 10) import Character.Ekidona.Text as text;
from Character.Ekidona import Text as text
# (Line 11) import Character.Ekidona.Commend as commend;
from Character.Ekidona import Commend as commend
# (Line 13) function SkillList(cp);
# (Line 15) function main(cp)
# (Line 16) {
@EUDFunc
def f_main(cp):
    # (Line 17) f.location[cp] = 195;
    _ARRW(f.location, cp) << (195)
    # (Line 18) f.heroID[cp] = 87;
    _ARRW(f.heroID, cp) << (87)
    # (Line 20) f.UltimateA[cp] = 650;
    _ARRW(f.UltimateA, cp) << (650)
    # (Line 22) SkillList(cp);
    SkillList(cp)
    # (Line 23) commend.main(cp);
    commend.f_main(cp)
    # (Line 25) if (f.wait[cp] == 0)
    if EUDIf()(f.wait[cp] == 0):
        # (Line 26) {
        # (Line 27) switch(f.step[cp])
        EUDSwitch(f.step[cp])
        # (Line 28) {
        # (Line 29) case 1:
        _t2 = EUDSwitchCase()
        # (Line 30) O.main(cp);
        if _t2(1):
            O.f_main(cp)
            # (Line 31) break;
            EUDBreak()
            # (Line 32) case 100:
        _t3 = EUDSwitchCase()
        # (Line 33) S.main(cp);
        if _t3(100):
            S.f_main(cp)
            # (Line 34) break;
            EUDBreak()
            # (Line 35) case 200:
        _t4 = EUDSwitchCase()
        # (Line 36) C.main(cp);
        if _t4(200):
            C.f_main(cp)
            # (Line 37) break;
            EUDBreak()
            # (Line 38) case 300:
        _t5 = EUDSwitchCase()
        # (Line 39) A.main(cp);
        if _t5(300):
            A.f_main(cp)
            # (Line 40) break;
            EUDBreak()
            # (Line 41) case 110:
        _t6 = EUDSwitchCase()
        # (Line 42) SSS.main(cp);
        if _t6(110):
            SSS.f_main(cp)
            # (Line 43) break;
            EUDBreak()
            # (Line 44) }
        # (Line 45) }
        EUDEndSwitch()
        # (Line 49) }
    EUDEndIf()
    # (Line 52) function SkillVoice(cp)

# (Line 53) {
@EUDFunc
def SkillVoice(cp):
    # (Line 54) if (f.Ekidona_Voice[cp] != 0) { text.main(cp); }
    if EUDIf()(f.Ekidona_Voice[cp] == 0, neg=True):
        text.f_main(cp)
        # (Line 55) }
    EUDEndIf()
    # (Line 57) function SkillList(cp)

# (Line 58) {
@EUDFunc
def SkillList(cp):
    # (Line 59) if(Memory(0x00596A44, Exactly, 256)) 	// Insert key Pressed
    if EUDIf()(Memory(0x00596A44, Exactly, 256)):
        # (Line 60) {
        # (Line 61) f.stb.printAt(0, "\n");
        f.stb.printAt(0, "\n")
        # (Line 62) f.stb.printAt(1, "\x1F　＃\x1B- 에키드나　\x04[ Re : 제로부터 시작하는 이세계 생활 ]");
        f.stb.printAt(1, "\x1F　＃\x1B- 에키드나　\x04[ Re : 제로부터 시작하는 이세계 생활 ]")
        # (Line 63) f.stb.printAt(2, "　　\x1FA\x04ction List");
        f.stb.printAt(2, "　　\x1FA\x04ction List")
        # (Line 64) f.stb.printAt(3, "　　　\x18O \x04계약 \x19[ 순간딜 / 상대 건물에 닿을 때까지 일직선 대시 / 일반기 자리고정 해제 1분 ] \x054분");
        f.stb.printAt(3, "　　　\x18O \x04계약 \x19[ 순간딜 / 상대 건물에 닿을 때까지 일직선 대시 / 일반기 자리고정 해제 1분 ] \x054분")
        # (Line 65) f.stb.printAt(4, "　　　\x04\x1FSSS \x04즐거움 \x19[ 만능 ]");
        f.stb.printAt(4, "　　　\x04\x1FSSS \x04즐거움 \x19[ 만능 ]")
        # (Line 66) f.stb.printAt(5, "　　　\x04\x1FCCC \x04여유 \x19[ 공성 / 자리고정 ]");
        f.stb.printAt(5, "　　　\x04\x1FCCC \x04여유 \x19[ 공성 / 자리고정 ]")
        # (Line 67) f.stb.printAt(6, "　　　\x04\x1FCCAA \x04나의 차례! \x19[ 공성 / 자리고정 ]");
        f.stb.printAt(6, "　　　\x04\x1FCCAA \x04나의 차례! \x19[ 공성 / 자리고정 ]")
        # (Line 68) f.stb.printAt(7, "\n");
        f.stb.printAt(7, "\n")
        # (Line 69) f.stb.printAt(8, "　　　\x08AAAA \x04드래곤 버스트 \x19[ 공성 / 선딜 7초 / 자리고정 ] \x05", f.UltimateA[cp]);
        f.stb.printAt(8, "　　　\x08AAAA \x04드래곤 버스트 \x19[ 공성 / 선딜 7초 / 자리고정 ] \x05", f.UltimateA[cp])
        # (Line 70) f.stb.printAt(9, "\n");
        f.stb.printAt(9, "\n")
        # (Line 71) PlayWAV("sound\\Bullet\\LaserHit.wav");
        # (Line 72) }
        DoActions(PlayWAV("sound\\Bullet\\LaserHit.wav"))
        # (Line 73) }
    EUDEndIf()