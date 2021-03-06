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
    # (Line 43) case 1000:
    _t1 = EUDSwitchCase()
    # (Line 44) PlayWAV("Cecillia_01.ogg");
    if _t1(1000):
        # (Line 45) v.stb.print("\n\x13\x17Cecillia\n\x13\x04「　간다, \x17파동각!　\x04」\n");
        DoActions(PlayWAV("Cecillia_01.ogg"))
        v.stb.print("\n\x13\x17Cecillia\n\x13\x04「　간다, \x17파동각!　\x04」\n")
        # (Line 47) break;
        EUDBreak()
        # (Line 48) case 1010:
    _t2 = EUDSwitchCase()
    # (Line 49) PlayWAV("Cecillia_02.ogg");
    if _t2(1010):
        # (Line 50) v.stb.print("\n\x13\x17Cecillia\n\x13\x04「　받아라! \x17천추각!　\x04」\n");
        DoActions(PlayWAV("Cecillia_02.ogg"))
        v.stb.print("\n\x13\x17Cecillia\n\x13\x04「　받아라! \x17천추각!　\x04」\n")
        # (Line 52) break;
        EUDBreak()
        # (Line 53) case 1020:
    _t3 = EUDSwitchCase()
    # (Line 54) PlayWAV("Cecillia_03.ogg");
    if _t3(1020):
        # (Line 55) v.stb.print("\n\x13\x17Cecillia\n\x13\x04「　부셔져라, \x06폭렬각!!!　\x04」\n");
        DoActions(PlayWAV("Cecillia_03.ogg"))
        v.stb.print("\n\x13\x17Cecillia\n\x13\x04「　부셔져라, \x06폭렬각!!!　\x04」\n")
        # (Line 57) break;
        EUDBreak()
        # (Line 58) }
    # (Line 59) }
    EUDEndSwitch()
    # (Line 61) function Text2(num)

# (Line 62) {
@EUDFunc
def Text2(num):
    # (Line 63) switch (num)
    EUDSwitch(num)
    # (Line 64) {
    # (Line 65) case 7000:
    _t1 = EUDSwitchCase()
    # (Line 66) PlayWAV("Cecillia_Uiltimate.ogg");
    if _t1(7000):
        # (Line 67) v.stb.printAt(3,"\x13\x17Cecillia\n\n\x13\x04「　하아앗.. \x06필살 유성각!　\x04」");
        DoActions(PlayWAV("Cecillia_Uiltimate.ogg"))
        v.stb.printAt(3, "\x13\x17Cecillia\n\n\x13\x04「　하아앗.. \x06필살 유성각!　\x04」")
        # (Line 69) break;
        EUDBreak()
        # (Line 70) }
    # (Line 71) }
    EUDEndSwitch()
    # (Line 73) function Text3(num)

# (Line 74) {
@EUDFunc
def Text3(num):
    # (Line 75) switch (num)
    EUDSwitch(num)
    # (Line 76) {
    # (Line 77) case 7000:
    _t1 = EUDSwitchCase()
    # (Line 78) PlayWAV("Cecillia_Unique.ogg");
    if _t1(7000):
        # (Line 79) v.stb.printAt(3,"\x13\x17Cecillia\n\x13\x04「　괴로워도 포기하면 거기서 끝이라고? 용기란 포기하지 않는 걸 말하는거라고　\x04」");
        DoActions(PlayWAV("Cecillia_Unique.ogg"))
        v.stb.printAt(3, "\x13\x17Cecillia\n\x13\x04「　괴로워도 포기하면 거기서 끝이라고? 용기란 포기하지 않는 걸 말하는거라고　\x04」")
        # (Line 81) break;
        EUDBreak()
        # (Line 82) }
    # (Line 83) }
    EUDEndSwitch()
