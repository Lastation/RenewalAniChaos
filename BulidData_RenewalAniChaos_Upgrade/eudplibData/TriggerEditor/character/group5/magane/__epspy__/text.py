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
# (Line 6) const P_player		= PVariable();
P_player = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 7) const P_observer 	= PVariable();
P_observer = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 9) function Text(num);
# (Line 11) function player(playerID)
# (Line 12) {
@EUDFunc
def f_player(playerID):
    # (Line 13) Text(P_player[playerID]);
    Text(P_player[playerID])
    # (Line 14) P_player[playerID] = 0;
    _ARRW(P_player, playerID) << (0)
    # (Line 15) }
    # (Line 17) function observer(playerID)

# (Line 18) {
@EUDFunc
def f_observer(playerID):
    # (Line 19) Text(P_observer[playerID - 128]);
    Text(P_observer[playerID - 128])
    # (Line 20) P_observer[playerID - 128] = 0;
    _ARRW(P_observer, playerID - 128) << (0)
    # (Line 21) }
    # (Line 23) function main(playerID)

# (Line 24) {
@EUDFunc
def f_main(playerID):
    # (Line 25) if (playerID < 6) 	{ player(playerID); 	}
    if EUDIf()(playerID >= 6, neg=True):
        f_player(playerID)
        # (Line 26) else  			{ observer(playerID); }
    if EUDElse()():
        f_observer(playerID)
        # (Line 27) }
    EUDEndIf()
    # (Line 29) function Text(num)

# (Line 30) {
@EUDFunc
def Text(num):
    # (Line 31) switch (num)
    EUDSwitch(num)
    # (Line 32) {
    # (Line 33) case 1:
    _t1 = EUDSwitchCase()
    # (Line 34) PlayWAV("Magane_01.ogg");
    if _t1(1):
        # (Line 35) v.stb.print("\x13\x1BChikujoin Magane\n");
        DoActions(PlayWAV("Magane_01.ogg"))
        v.stb.print("\x13\x1BChikujoin Magane\n")
        # (Line 36) v.stb.print("\x13\x04거기에 쓰여져 있는 거, \x08거짓말이라고 생각해?\x04");
        v.stb.print("\x13\x04거기에 쓰여져 있는 거, \x08거짓말이라고 생각해?\x04")
        # (Line 37) break;
        EUDBreak()
        # (Line 38) case 2:
    _t2 = EUDSwitchCase()
    # (Line 39) PlayWAV("Magane_06.ogg");
    if _t2(2):
        # (Line 40) v.stb.print("\x13\x1BChikujoin Magane\n");
        DoActions(PlayWAV("Magane_06.ogg"))
        v.stb.print("\x13\x1BChikujoin Magane\n")
        # (Line 41) v.stb.print("\x13\x08머리 나쁜 걸 남 탓으로 돌리지 말아줄래?\x04");
        v.stb.print("\x13\x08머리 나쁜 걸 남 탓으로 돌리지 말아줄래?\x04")
        # (Line 42) break;
        EUDBreak()
        # (Line 43) case 3:
    _t3 = EUDSwitchCase()
    # (Line 44) PlayWAV("Magane_04.ogg");
    if _t3(3):
        # (Line 45) v.stb.print("\x13\x1BChikujoin Magane\n");
        DoActions(PlayWAV("Magane_04.ogg"))
        v.stb.print("\x13\x1BChikujoin Magane\n")
        # (Line 46) v.stb.print("\x13\x04여기는 좋은 세계인가 보네\x04");
        v.stb.print("\x13\x04여기는 좋은 세계인가 보네\x04")
        # (Line 47) break;
        EUDBreak()
        # (Line 48) case 4:
    _t4 = EUDSwitchCase()
    # (Line 49) PlayWAV("Magane_05.ogg");
    if _t4(4):
        # (Line 50) v.stb.print("\x13\x1BChikujoin Magane\n");
        DoActions(PlayWAV("Magane_05.ogg"))
        v.stb.print("\x13\x1BChikujoin Magane\n")
        # (Line 51) v.stb.print("\x13\x04이거 상당히... \x08놀아볼만 하겠는데?\x04");
        v.stb.print("\x13\x04이거 상당히... \x08놀아볼만 하겠는데?\x04")
        # (Line 52) break;
        EUDBreak()
        # (Line 53) case 5:
    _t5 = EUDSwitchCase()
    # (Line 54) PlayWAV("Magane_03.ogg");
    if _t5(5):
        # (Line 55) break;
        DoActions(PlayWAV("Magane_03.ogg"))
        EUDBreak()
        # (Line 56) case 6:
    _t6 = EUDSwitchCase()
    # (Line 57) v.stb.print("\x13\x1BChikujoin Magane\n");
    if _t6(6):
        v.stb.print("\x13\x1BChikujoin Magane\n")
        # (Line 58) v.stb.print("\x13\x04그것은 빙글 돌아\x04");
        v.stb.print("\x13\x04그것은 빙글 돌아\x04")
        # (Line 59) break;
        EUDBreak()
        # (Line 60) case 7:
    _t7 = EUDSwitchCase()
    # (Line 61) v.stb.print("\x13\x1BChikujoin Magane\n");
    if _t7(7):
        v.stb.print("\x13\x1BChikujoin Magane\n")
        # (Line 62) v.stb.print("\x13\x04뒤집힌다\x04");
        v.stb.print("\x13\x04뒤집힌다\x04")
        # (Line 63) break;
        EUDBreak()
        # (Line 64) case 8:
    _t8 = EUDSwitchCase()
    # (Line 65) PlayWAV("Magane_09.ogg");
    if _t8(8):
        # (Line 66) v.stb.print("\x13\x1BChikujoin Magane\n");
        DoActions(PlayWAV("Magane_09.ogg"))
        v.stb.print("\x13\x1BChikujoin Magane\n")
        # (Line 67) v.stb.print("\x13\x04걸렸다\x04");
        v.stb.print("\x13\x04걸렸다\x04")
        # (Line 68) break;
        EUDBreak()
        # (Line 69) case 9:
    _t9 = EUDSwitchCase()
    # (Line 70) PlayWAV("Magane_10.ogg");
    if _t9(9):
        # (Line 71) v.stb.print("\x13\x1BChikujoin Magane\n");
        DoActions(PlayWAV("Magane_10.ogg"))
        v.stb.print("\x13\x1BChikujoin Magane\n")
        # (Line 72) v.stb.print("\x13\x04거짓말의 거짓말\x04");
        v.stb.print("\x13\x04거짓말의 거짓말\x04")
        # (Line 73) break;
        EUDBreak()
        # (Line 74) case 10:
    _t10 = EUDSwitchCase()
    # (Line 75) PlayWAV("Magane_11.ogg");
    if _t10(10):
        # (Line 76) v.stb.print("\x13\x1BChikujoin Magane\n");
        DoActions(PlayWAV("Magane_11.ogg"))
        v.stb.print("\x13\x1BChikujoin Magane\n")
        # (Line 77) v.stb.print("\x13\x04그것은 빙글 돌아 뒤집힌다\x04");
        v.stb.print("\x13\x04그것은 빙글 돌아 뒤집힌다\x04")
        # (Line 78) break;
        EUDBreak()
        # (Line 79) case 11:
    _t11 = EUDSwitchCase()
    # (Line 80) v.stb.print("\x13\x1BChikujoin Magane\n");
    if _t11(11):
        v.stb.print("\x13\x1BChikujoin Magane\n")
        # (Line 81) v.stb.print("\x13\x04거짓말의 거짓말\x04");
        v.stb.print("\x13\x04거짓말의 거짓말\x04")
        # (Line 82) break;
        EUDBreak()
        # (Line 83) }
    # (Line 84) }
    EUDEndSwitch()
