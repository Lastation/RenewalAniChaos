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
    # (Line 34) PlayWAV("Chtholly_EX01.ogg");
    if _t1(1):
        # (Line 35) v.stb.print("\x13\x1CChtholly Nota Seniorious\r\n\x13\x04언제까지고 함께 있어주겠다고 맹세했지");
        DoActions(PlayWAV("Chtholly_EX01.ogg"))
        v.stb.print("\x13\x1CChtholly Nota Seniorious\r\n\x13\x04언제까지고 함께 있어주겠다고 맹세했지")
        # (Line 36) break;
        EUDBreak()
        # (Line 37) case 2:
    _t2 = EUDSwitchCase()
    # (Line 38) v.stb.print("\x13\x1BCh\x1Ctholly Nota Seniorious\r\n\x13\x04맹세할 수 있었단 사실이 너무도 행복했어");
    if _t2(2):
        v.stb.print("\x13\x1BCh\x1Ctholly Nota Seniorious\r\n\x13\x04맹세할 수 있었단 사실이 너무도 행복했어")
        # (Line 39) break;
        EUDBreak()
        # (Line 40) case 3:
    _t3 = EUDSwitchCase()
    # (Line 41) PlayWAV("Chtholly_EX02.ogg");
    if _t3(3):
        # (Line 42) v.stb.print("\x13\x06Ch\x1Btho\x1Clly Nota Seniorious\r\n\x13\x04이 사람을 좋아하는 거구나 싶었지");
        DoActions(PlayWAV("Chtholly_EX02.ogg"))
        v.stb.print("\x13\x06Ch\x1Btho\x1Clly Nota Seniorious\r\n\x13\x04이 사람을 좋아하는 거구나 싶었지")
        # (Line 43) break;
        EUDBreak()
        # (Line 44) case 4:
    _t4 = EUDSwitchCase()
    # (Line 45) v.stb.print("\x13\x06Chtho\x1Blly \x1CNota Seniorious\r\n\x13\x04이렇게 생각할 수 있었던 사실이 행복했어");
    if _t4(4):
        v.stb.print("\x13\x06Chtho\x1Blly \x1CNota Seniorious\r\n\x13\x04이렇게 생각할 수 있었던 사실이 행복했어")
        # (Line 46) break;
        EUDBreak()
        # (Line 47) case 5:
    _t5 = EUDSwitchCase()
    # (Line 48) PlayWAV("Chtholly_EX03.ogg");
    if _t5(5):
        # (Line 49) break;
        DoActions(PlayWAV("Chtholly_EX03.ogg"))
        EUDBreak()
        # (Line 50) case 6:
    _t6 = EUDSwitchCase()
    # (Line 51) v.stb.print("\x13\x06Chtholly \x1BNo\x1Cta Seniorious\r\n\x13\x04행복하게 만들어주겠다고 내게 말해주었어");
    if _t6(6):
        v.stb.print("\x13\x06Chtholly \x1BNo\x1Cta Seniorious\r\n\x13\x04행복하게 만들어주겠다고 내게 말해주었어")
        # (Line 52) break;
        EUDBreak()
        # (Line 53) case 7:
    _t7 = EUDSwitchCase()
    # (Line 54) v.stb.print("\x13\x06Chtholly No\x1Bta Se\x1Cniorious\r\n\x13\x04내게 그런 말을 해준 것이 행복했어");
    if _t7(7):
        v.stb.print("\x13\x06Chtholly No\x1Bta Se\x1Cniorious\r\n\x13\x04내게 그런 말을 해준 것이 행복했어")
        # (Line 55) break;
        EUDBreak()
        # (Line 56) case 8:
    _t8 = EUDSwitchCase()
    # (Line 57) v.stb.print("\x13\x06Chtholly Nota Se\x1Bnior\x1Cious\r\n\x13\x04이렇게나 많은 행복함을 그 사람에게 나눠받았어 ");
    if _t8(8):
        v.stb.print("\x13\x06Chtholly Nota Se\x1Bnior\x1Cious\r\n\x13\x04이렇게나 많은 행복함을 그 사람에게 나눠받았어 ")
        # (Line 58) break;
        EUDBreak()
        # (Line 59) case 9:
    _t9 = EUDSwitchCase()
    # (Line 60) PlayWAV("Chtholly_00.ogg");
    if _t9(9):
        # (Line 61) v.stb.print("\x13\x1CChtholly Nota Seniorious\r\n\x13\x04어쩔수없구나, \x05정말...");
        DoActions(PlayWAV("Chtholly_00.ogg"))
        v.stb.print("\x13\x1CChtholly Nota Seniorious\r\n\x13\x04어쩔수없구나, \x05정말...")
        # (Line 62) break;
        EUDBreak()
        # (Line 63) case 10:
    _t10 = EUDSwitchCase()
    # (Line 64) PlayWAV("Chtholly_Dead.ogg");
    if _t10(10):
        # (Line 65) v.stb.printAt(3, "\x13\x06Chtholly Nota Seniorious\r\n\x13\x05빌렘... 고마..워...");
        DoActions(PlayWAV("Chtholly_Dead.ogg"))
        v.stb.printAt(3, "\x13\x06Chtholly Nota Seniorious\r\n\x13\x05빌렘... 고마..워...")
        # (Line 66) break;
        EUDBreak()
        # (Line 67) case 11:
    _t11 = EUDSwitchCase()
    # (Line 68) PlayWAV("Chtholly_EX04.ogg");
    if _t11(11):
        # (Line 69) break;
        DoActions(PlayWAV("Chtholly_EX04.ogg"))
        EUDBreak()
        # (Line 70) case 12:
    _t12 = EUDSwitchCase()
    # (Line 71) v.stb.printAt(4, "\x13\x06Chtholly Nota Senior\x1Bio\x1Cus\r\n\x13\x04그러니까\n\n\n");
    if _t12(12):
        v.stb.printAt(4, "\x13\x06Chtholly Nota Senior\x1Bio\x1Cus\r\n\x13\x04그러니까\n\n\n")
        # (Line 72) break;
        EUDBreak()
        # (Line 73) case 13:
    _t13 = EUDSwitchCase()
    # (Line 74) v.stb.printAt(4, "\x13\x06Chtholly Nota Seniorio\x1Bu\x1Cs\r\n\x13\x04분명\n\n\n");
    if _t13(13):
        v.stb.printAt(4, "\x13\x06Chtholly Nota Seniorio\x1Bu\x1Cs\r\n\x13\x04분명\n\n\n")
        # (Line 75) break;
        EUDBreak()
        # (Line 76) case 14:
    _t14 = EUDSwitchCase()
    # (Line 77) v.stb.printAt(0, "\x13\x06Chtholly Nota Seniorious\n\x13\x04지금의 나는\n\x13\x04누가 뭐라 할지라도\n\x13\x04세상에서 제일 \x06행복한 여자아이\x04인 거야");
    if _t14(14):
        v.stb.printAt(0, "\x13\x06Chtholly Nota Seniorious\n\x13\x04지금의 나는\n\x13\x04누가 뭐라 할지라도\n\x13\x04세상에서 제일 \x06행복한 여자아이\x04인 거야")
        # (Line 78) break;
        EUDBreak()
        # (Line 79) }
    # (Line 80) }
    EUDEndSwitch()