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
# (Line 8) const P_type 		= PVariable();
P_type = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 10) function Text1(num);
# (Line 11) function Text2(num);
# (Line 12) function Text3(num);
# (Line 14) function player(playerID)
# (Line 15) {
@EUDFunc
def f_player(playerID):
    # (Line 16) if (P_type[playerID] == 1) { Text1(P_player[playerID]); }
    if EUDIf()(P_type[playerID] == 1):
        Text1(P_player[playerID])
        # (Line 17) if (P_type[playerID] == 2) { Text2(P_player[playerID]); }
    EUDEndIf()
    if EUDIf()(P_type[playerID] == 2):
        Text2(P_player[playerID])
        # (Line 18) if (P_type[playerID] == 3) { Text3(P_player[playerID]); }
    EUDEndIf()
    if EUDIf()(P_type[playerID] == 3):
        Text3(P_player[playerID])
        # (Line 19) P_player[playerID] = 0;
    EUDEndIf()
    _ARRW(P_player, playerID) << (0)
    # (Line 20) }
    # (Line 22) function observer(playerID)

# (Line 23) {
@EUDFunc
def f_observer(playerID):
    # (Line 24) if (P_type[playerID] == 1) { Text1(P_observer[playerID - 128]); }
    if EUDIf()(P_type[playerID] == 1):
        Text1(P_observer[playerID - 128])
        # (Line 25) if (P_type[playerID] == 2) { Text2(P_observer[playerID - 128]); }
    EUDEndIf()
    if EUDIf()(P_type[playerID] == 2):
        Text2(P_observer[playerID - 128])
        # (Line 26) if (P_type[playerID] == 3) { Text3(P_observer[playerID - 128]); }
    EUDEndIf()
    if EUDIf()(P_type[playerID] == 3):
        Text3(P_observer[playerID - 128])
        # (Line 27) P_observer[playerID - 128] = 0;
    EUDEndIf()
    _ARRW(P_observer, playerID - 128) << (0)
    # (Line 28) }
    # (Line 30) function main(playerID)

# (Line 31) {
@EUDFunc
def f_main(playerID):
    # (Line 32) if (playerID < 6) 	{ player(playerID); 	}
    if EUDIf()(playerID >= 6, neg=True):
        f_player(playerID)
        # (Line 33) else  			{ observer(playerID); }
    if EUDElse()():
        f_observer(playerID)
        # (Line 34) }
    EUDEndIf()
    # (Line 39) function Text1(num)

# (Line 40) {
@EUDFunc
def Text1(num):
    # (Line 41) switch (num)
    EUDSwitch(num)
    # (Line 42) {
    # (Line 43) case 4100:
    _t1 = EUDSwitchCase()
    # (Line 44) PlayWAV("Alther_0.ogg");
    if _t1(4100):
        # (Line 45) v.stb.print("\n\x13\x1FAlther Ego Λ\n\x13\x04「　멜트 스트라이크!　\x04」\n");
        DoActions(PlayWAV("Alther_0.ogg"))
        v.stb.print("\n\x13\x1FAlther Ego Λ\n\x13\x04「　멜트 스트라이크!　\x04」\n")
        # (Line 47) break;
        EUDBreak()
        # (Line 48) case 4200:
    _t2 = EUDSwitchCase()
    # (Line 49) PlayWAV("Alther_1.ogg");
    if _t2(4200):
        # (Line 50) v.stb.print("\n\x13\x1FAlther Ego Λ\n\x13\x04「　작별이네,　\x04」\n");
        DoActions(PlayWAV("Alther_1.ogg"))
        v.stb.print("\n\x13\x1FAlther Ego Λ\n\x13\x04「　작별이네,　\x04」\n")
        # (Line 52) break;
        EUDBreak()
        # (Line 53) case 4201:
    _t3 = EUDSwitchCase()
    # (Line 54) v.stb.print("\n\x13\x1FAlther Ego Λ\n\x13\x04「　마지막으로 사랑을 가르쳐줄게.　\x04」\n");
    if _t3(4201):
        v.stb.print("\n\x13\x1FAlther Ego Λ\n\x13\x04「　마지막으로 사랑을 가르쳐줄게.　\x04」\n")
        # (Line 56) break;
        EUDBreak()
        # (Line 57) case 4202:
    _t4 = EUDSwitchCase()
    # (Line 58) v.stb.print("\n\x13\x1FAlther Ego Λ\n\x13\x04「　가엾고 비참한 물의 포로.　\x04」\n");
    if _t4(4202):
        v.stb.print("\n\x13\x1FAlther Ego Λ\n\x13\x04「　가엾고 비참한 물의 포로.　\x04」\n")
        # (Line 60) break;
        EUDBreak()
        # (Line 61) case 4300:
    _t5 = EUDSwitchCase()
    # (Line 62) PlayWAV("Alther_2.ogg");
    if _t5(4300):
        # (Line 64) break;
        DoActions(PlayWAV("Alther_2.ogg"))
        EUDBreak()
        # (Line 65) case 4301:
    _t6 = EUDSwitchCase()
    # (Line 66) v.stb.print("\n\x13\x1FAlther Ego Λ\n\x13\x04「　나의 가시로, 잘 가도록해!　\x04」\n");
    if _t6(4301):
        v.stb.print("\n\x13\x1FAlther Ego Λ\n\x13\x04「　나의 가시로, 잘 가도록해!　\x04」\n")
        # (Line 68) break;
        EUDBreak()
        # (Line 69) }
    # (Line 70) }
    EUDEndSwitch()
    # (Line 72) function Text2(num)

# (Line 73) {
@EUDFunc
def Text2(num):
    # (Line 74) switch (num)
    EUDSwitch(num)
    # (Line 75) {
    # (Line 76) case 10000:
    _t1 = EUDSwitchCase()
    # (Line 77) PlayWAV("Alther_EX1.ogg");
    if _t1(10000):
        # (Line 78) v.stb.printAt(3,"\x13\x1FAlther Ego Λ\n\x13\x04「　대청소로 가보실까.　\x04」");
        DoActions(PlayWAV("Alther_EX1.ogg"))
        v.stb.printAt(3, "\x13\x1FAlther Ego Λ\n\x13\x04「　대청소로 가보실까.　\x04」")
        # (Line 80) break;
        EUDBreak()
        # (Line 81) case 10001:
    _t2 = EUDSwitchCase()
    # (Line 82) v.stb.printAt(3,"\x13\x1FAlther Ego Λ\n\x13\x04「　이걸로 피니시!　\x04」");
    if _t2(10001):
        v.stb.printAt(3, "\x13\x1FAlther Ego Λ\n\x13\x04「　이걸로 피니시!　\x04」")
        # (Line 84) break;
        EUDBreak()
        # (Line 85) case 10010:
    _t3 = EUDSwitchCase()
    # (Line 86) PlayWAV("Alther_EX2.ogg");
    if _t3(10010):
        # (Line 87) v.stb.printAt(3,"\x13\x1FAlther Ego Λ\n\x13\x04「　어머, 너희들도 같이?　\x04」");
        DoActions(PlayWAV("Alther_EX2.ogg"))
        v.stb.printAt(3, "\x13\x1FAlther Ego Λ\n\x13\x04「　어머, 너희들도 같이?　\x04」")
        # (Line 89) break;
        EUDBreak()
        # (Line 90) case 10011:
    _t4 = EUDSwitchCase()
    # (Line 91) v.stb.printAt(3,"\x13\x1FAlther Ego Λ\n\x13\x04「　라스트 스트로크!　\x04」");
    if _t4(10011):
        v.stb.printAt(3, "\x13\x1FAlther Ego Λ\n\x13\x04「　라스트 스트로크!　\x04」")
        # (Line 93) break;
        EUDBreak()
        # (Line 94) case 10012:
    _t5 = EUDSwitchCase()
    # (Line 95) v.stb.printAt(3,"\x13\x1FAlther Ego Λ\n\n\x13\x04「　블루서머・팔라디온　\x04」");
    if _t5(10012):
        v.stb.printAt(3, "\x13\x1FAlther Ego Λ\n\n\x13\x04「　블루서머・팔라디온　\x04」")
        # (Line 97) break;
        EUDBreak()
        # (Line 98) }
    # (Line 99) }
    EUDEndSwitch()
    # (Line 101) function Text3(num)

# (Line 102) {
@EUDFunc
def Text3(num):
    # (Line 103) switch (num)
    EUDSwitch(num)
    # (Line 104) {
    # (Line 105) case 10000:
    _t1 = EUDSwitchCase()
    # (Line 106) PlayWAV("Alther_O.ogg");
    if _t1(10000):
        # (Line 107) v.stb.printAt(3,"\x13\x1FAlther Ego Λ\n\x13\x04「　도망칠 곳? 있을리가 없잖아.　\x04」");
        DoActions(PlayWAV("Alther_O.ogg"))
        v.stb.printAt(3, "\x13\x1FAlther Ego Λ\n\x13\x04「　도망칠 곳? 있을리가 없잖아.　\x04」")
        # (Line 109) break;
        EUDBreak()
        # (Line 110) }
    # (Line 111) }
    EUDEndSwitch()