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
    # (Line 31) switch(num)
    EUDSwitch(num)
    # (Line 32) {
    # (Line 33) case 1:
    _t1 = EUDSwitchCase()
    # (Line 34) PlayWAV("staredit\\wav\\Hime_Unique01.ogg");
    if _t1(1):
        # (Line 35) v.stb.printAt(3, "\x13\x04Tenkawa \x07MaiHime\n");
        DoActions(PlayWAV("staredit\\wav\\Hime_Unique01.ogg"))
        v.stb.printAt(3, "\x13\x04Tenkawa \x07MaiHime\n")
        # (Line 36) v.stb.printAt(5, "\x13\x04제군 ! \x07광연\x04의 시간이다!");
        v.stb.printAt(5, "\x13\x04제군 ! \x07광연\x04의 시간이다!")
        # (Line 37) break;
        EUDBreak()
        # (Line 38) case 2:
    _t2 = EUDSwitchCase()
    # (Line 39) PlayWAV("Kurumi_01.ogg");
    if _t2(2):
        # (Line 40) v.stb.print("\x13\x08Tokisaki \x05Krumi");
        DoActions(PlayWAV("Kurumi_01.ogg"))
        v.stb.print("\x13\x08Tokisaki \x05Krumi")
        # (Line 41) v.stb.print("\x13\x04귀여우시군요, 당신");
        v.stb.print("\x13\x04귀여우시군요, 당신")
        # (Line 42) break;
        EUDBreak()
        # (Line 43) case 3:
    _t3 = EUDSwitchCase()
    # (Line 44) PlayWAV("Kurumi_02.ogg");
    if _t3(3):
        # (Line 45) v.stb.print("\x13\x08Tokisaki \x05Krumi");
        DoActions(PlayWAV("Kurumi_02.ogg"))
        v.stb.print("\x13\x08Tokisaki \x05Krumi")
        # (Line 46) v.stb.print("\x13\x04저는 한번 나눈 약속을 소홀히 할정도로 영혼이 썩진 않았답니다");
        v.stb.print("\x13\x04저는 한번 나눈 약속을 소홀히 할정도로 영혼이 썩진 않았답니다")
        # (Line 47) break;
        EUDBreak()
        # (Line 48) case 6:
    _t4 = EUDSwitchCase()
    # (Line 49) PlayWAV("Kurumi_03.ogg");
    if _t4(6):
        # (Line 50) v.stb.print("\x13\x08Tokisaki \x05Krumi");
        DoActions(PlayWAV("Kurumi_03.ogg"))
        v.stb.print("\x13\x08Tokisaki \x05Krumi")
        # (Line 51) v.stb.print("\x13\x07어머,어머\x04 난폭하시군요\n\x13\x04뭐 , 유치한 소원이랑 제법 잘 어울리는 방식인걸요");
        v.stb.print("\x13\x07어머,어머\x04 난폭하시군요\n\x13\x04뭐 , 유치한 소원이랑 제법 잘 어울리는 방식인걸요")
        # (Line 52) break;
        EUDBreak()
        # (Line 53) case 7:
    _t5 = EUDSwitchCase()
    # (Line 54) PlayWAV("Kurumi_04.ogg");
    if _t5(7):
        # (Line 55) v.stb.print("\x13\x08Tokisaki \x05Krumi");
        DoActions(PlayWAV("Kurumi_04.ogg"))
        v.stb.print("\x13\x08Tokisaki \x05Krumi")
        # (Line 56) v.stb.print("\x13\x04나는 다시 한번 그를 만나러 가겠어!");
        v.stb.print("\x13\x04나는 다시 한번 그를 만나러 가겠어!")
        # (Line 57) break;
        EUDBreak()
        # (Line 58) case 8:
    _t6 = EUDSwitchCase()
    # (Line 59) PlayWAV("Kurumi_05.ogg");
    if _t6(8):
        # (Line 60) break;
        DoActions(PlayWAV("Kurumi_05.ogg"))
        EUDBreak()
        # (Line 61) case 15:
    _t7 = EUDSwitchCase()
    # (Line 62) v.stb.print("\x13\x08Tokisaki \x05Krumi");
    if _t7(15):
        v.stb.print("\x13\x08Tokisaki \x05Krumi")
        # (Line 63) v.stb.print("\x13알레프");
        v.stb.print("\x13알레프")
        # (Line 64) break;
        EUDBreak()
        # (Line 65) case 9:
    _t8 = EUDSwitchCase()
    # (Line 66) PlayWAV("Kurumi_06.ogg");
    if _t8(9):
        # (Line 67) v.stb.printAt(3, "\x13\x08Tokisaki \x05Krumi");
        DoActions(PlayWAV("Kurumi_06.ogg"))
        v.stb.printAt(3, "\x13\x08Tokisaki \x05Krumi")
        # (Line 68) v.stb.printAt(5, "\x13\x04제가 어째서 여기에 있는가");
        v.stb.printAt(5, "\x13\x04제가 어째서 여기에 있는가")
        # (Line 69) break;
        EUDBreak()
        # (Line 70) case 10:
    _t9 = EUDSwitchCase()
    # (Line 71) v.stb.printAt(3, "\x13\x08Tokisaki \x05Krumi");
    if _t9(10):
        v.stb.printAt(3, "\x13\x08Tokisaki \x05Krumi")
        # (Line 72) v.stb.printAt(5, "\x13\x04어떻게 살아있는가");
        v.stb.printAt(5, "\x13\x04어떻게 살아있는가")
        # (Line 73) break;
        EUDBreak()
        # (Line 74) case 11:
    _t10 = EUDSwitchCase()
    # (Line 75) v.stb.printAt(3, "\x13\x08Tokisaki \x05Krumi");
    if _t10(11):
        v.stb.printAt(3, "\x13\x08Tokisaki \x05Krumi")
        # (Line 76) v.stb.printAt(5, "\x13\x19당신\x04께서는 누구시며");
        v.stb.printAt(5, "\x13\x19당신\x04께서는 누구시며")
        # (Line 77) break;
        EUDBreak()
        # (Line 78) case 12:
    _t11 = EUDSwitchCase()
    # (Line 79) v.stb.printAt(3, "\x13\x08Tokisaki \x05Krumi");
    if _t11(12):
        v.stb.printAt(3, "\x13\x08Tokisaki \x05Krumi")
        # (Line 80) v.stb.printAt(5, "\x13\x04고양이 씨는 어째서 저래 귀여운지");
        v.stb.printAt(5, "\x13\x04고양이 씨는 어째서 저래 귀여운지")
        # (Line 81) break;
        EUDBreak()
        # (Line 82) case 13:
    _t12 = EUDSwitchCase()
    # (Line 83) v.stb.printAt(3, "\x13\x08Tokisaki \x05Krumi");
    if _t12(13):
        v.stb.printAt(3, "\x13\x08Tokisaki \x05Krumi")
        # (Line 84) v.stb.printAt(5, "\x13\x04무엇하나 알지 못하겟지만");
        v.stb.printAt(5, "\x13\x04무엇하나 알지 못하겟지만")
        # (Line 85) break;
        EUDBreak()
        # (Line 86) case 14:
    _t13 = EUDSwitchCase()
    # (Line 87) v.stb.printAt(3, "\x13\x08Tokisaki \x05Krumi");
    if _t13(14):
        v.stb.printAt(3, "\x13\x08Tokisaki \x05Krumi")
        # (Line 88) v.stb.printAt(5, "\x13\x04제 앞을 가로막으시겠다면 쓰러뜨려드리겠어요");
        v.stb.printAt(5, "\x13\x04제 앞을 가로막으시겠다면 쓰러뜨려드리겠어요")
        # (Line 89) break;
        EUDBreak()
        # (Line 90) case 16:
    _t14 = EUDSwitchCase()
    # (Line 91) PlayWAV("Kurumi_Unique.ogg");
    if _t14(16):
        # (Line 92) break;
        DoActions(PlayWAV("Kurumi_Unique.ogg"))
        EUDBreak()
        # (Line 93) case 17:
    _t15 = EUDSwitchCase()
    # (Line 94) v.stb.printAt(3, "\x13\x08Tokisaki \x05Krumi");
    if _t15(17):
        v.stb.printAt(3, "\x13\x08Tokisaki \x05Krumi")
        # (Line 95) v.stb.printAt(5, "\x13\x04자인");
        v.stb.printAt(5, "\x13\x04자인")
        # (Line 96) break;
        EUDBreak()
        # (Line 97) }
    # (Line 98) }
    EUDEndSwitch()