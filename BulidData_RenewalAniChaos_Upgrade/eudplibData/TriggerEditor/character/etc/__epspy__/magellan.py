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
    # (Line 43) case 3000:
    _t1 = EUDSwitchCase()
    # (Line 44) PlayWAV("Magellan_02.ogg");
    if _t1(3000):
        # (Line 45) v.stb.print("\n\n\x13\x19Magellan\n\x13\x04업데이트 완료\n\n");
        DoActions(PlayWAV("Magellan_02.ogg"))
        v.stb.print("\n\n\x13\x19Magellan\n\x13\x04업데이트 완료\n\n")
        # (Line 47) break;
        EUDBreak()
        # (Line 48) case 3001:
    _t2 = EUDSwitchCase()
    # (Line 49) PlayWAV("Magellan_01.ogg");
    if _t2(3001):
        # (Line 50) v.stb.print("\n\n\x13\x19Magellan\n\x13\x04효율 개선!\n\n");
        DoActions(PlayWAV("Magellan_01.ogg"))
        v.stb.print("\n\n\x13\x19Magellan\n\x13\x04효율 개선!\n\n")
        # (Line 52) break;
        EUDBreak()
        # (Line 53) case 3002:
    _t3 = EUDSwitchCase()
    # (Line 54) PlayWAV("Magellan_03.ogg");
    if _t3(3002):
        # (Line 55) v.stb.print("\n\n\x13\x19Magellan\n\x13\x04일 시작!\n\n");
        DoActions(PlayWAV("Magellan_03.ogg"))
        v.stb.print("\n\n\x13\x19Magellan\n\x13\x04일 시작!\n\n")
        # (Line 57) break;
        EUDBreak()
        # (Line 58) case 3003:
    _t4 = EUDSwitchCase()
    # (Line 59) PlayWAV("Magellan_04.ogg");
    if _t4(3003):
        # (Line 60) v.stb.print("\n\n\x13\x19Magellan\n\x13\x04시스템 올 그린!\n\n");
        DoActions(PlayWAV("Magellan_04.ogg"))
        v.stb.print("\n\n\x13\x19Magellan\n\x13\x04시스템 올 그린!\n\n")
        # (Line 62) break;
        EUDBreak()
        # (Line 63) case 3004:
    _t5 = EUDSwitchCase()
    # (Line 64) PlayWAV("Magellan_05.ogg");
    if _t5(3004):
        # (Line 65) v.stb.print("\n\n\x13\x19Magellan\n\x13\x04가라! 눈의 반사로 눈속임이야!\n\n");
        DoActions(PlayWAV("Magellan_05.ogg"))
        v.stb.print("\n\n\x13\x19Magellan\n\x13\x04가라! 눈의 반사로 눈속임이야!\n\n")
        # (Line 67) break;
        EUDBreak()
        # (Line 69) }
    # (Line 71) }
    EUDEndSwitch()
    # (Line 73) function Text3(num)

# (Line 74) {
@EUDFunc
def Text3(num):
    # (Line 75) switch (num)
    EUDSwitch(num)
    # (Line 76) {
    # (Line 77) case 21000:
    _t1 = EUDSwitchCase()
    # (Line 78) v.stb.print("\n\n\x13\x19Magellan\n\x13\x04좋아, 드론 기동!\n\n");
    if _t1(21000):
        v.stb.print("\n\n\x13\x19Magellan\n\x13\x04좋아, 드론 기동!\n\n")
        # (Line 79) PlayWAV("Magellan_O.ogg");
        # (Line 81) break;
        DoActions(PlayWAV("Magellan_O.ogg"))
        EUDBreak()
        # (Line 82) }
    # (Line 83) }
    EUDEndSwitch()
    # (Line 85) function Text2(num)

# (Line 86) {
@EUDFunc
def Text2(num):
    # (Line 87) switch (num)
    EUDSwitch(num)
    # (Line 88) {
    # (Line 89) case 21000:
    _t1 = EUDSwitchCase()
    # (Line 90) v.stb.print("\n\n\x13\x19Magellan\n\x13\x043... 2... 1...! 가라!\n\n");
    if _t1(21000):
        v.stb.print("\n\n\x13\x19Magellan\n\x13\x043... 2... 1...! 가라!\n\n")
        # (Line 91) PlayWAV("Magellan_Ult.ogg");
        # (Line 93) break;
        DoActions(PlayWAV("Magellan_Ult.ogg"))
        EUDBreak()
        # (Line 94) case 21001:
    _t2 = EUDSwitchCase()
    # (Line 95) v.stb.print("\n\n\x13\x19Magellan\n\x13\x04꽃들아, 피어나라!\n\n");
    if _t2(21001):
        v.stb.print("\n\n\x13\x19Magellan\n\x13\x04꽃들아, 피어나라!\n\n")
        # (Line 96) PlayWAV("Magellan_Ult2.ogg");
        # (Line 98) break;
        DoActions(PlayWAV("Magellan_Ult2.ogg"))
        EUDBreak()
        # (Line 100) }
    # (Line 102) }
    EUDEndSwitch()