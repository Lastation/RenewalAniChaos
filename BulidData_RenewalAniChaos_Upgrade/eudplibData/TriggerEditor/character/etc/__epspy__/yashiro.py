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
    # (Line 43) case 2000:
    _t1 = EUDSwitchCase()
    # (Line 44) PlayWAV("yashiro_sss.ogg");
    if _t1(2000):
        # (Line 45) v.stb.print("\n\n\x13\x02Yashiro Gaku\n\x13\x04그것은 분에 넘치는 소망이다\n\n");
        DoActions(PlayWAV("yashiro_sss.ogg"))
        v.stb.print("\n\n\x13\x02Yashiro Gaku\n\x13\x04그것은 분에 넘치는 소망이다\n\n")
        # (Line 47) break;
        EUDBreak()
        # (Line 48) case 2002:
    _t2 = EUDSwitchCase()
    # (Line 49) v.stb.print("\n\n\x13\x02Yashiro Gaku\n\x13\x04네가 손에 넣는 것은 이 마을의 평화다\n\x13\x04네가 원한 것은 바로 그거잖아?\n\n");
    if _t2(2002):
        v.stb.print("\n\n\x13\x02Yashiro Gaku\n\x13\x04네가 손에 넣는 것은 이 마을의 평화다\n\x13\x04네가 원한 것은 바로 그거잖아?\n\n")
        # (Line 51) PlayWAV("yashiro_ccaa.ogg");
        # (Line 52) break;
        DoActions(PlayWAV("yashiro_ccaa.ogg"))
        EUDBreak()
        # (Line 53) case 2003:
    _t3 = EUDSwitchCase()
    # (Line 54) v.stb.print("\n\n\x13\x02Yashiro Gaku\n\x13\x04내가 손에 넣는 것은\n\x13\x04내 손에 의한, 나만을 위해 존재하는 죽음이다\n\n");
    if _t3(2003):
        v.stb.print("\n\n\x13\x02Yashiro Gaku\n\x13\x04내가 손에 넣는 것은\n\x13\x04내 손에 의한, 나만을 위해 존재하는 죽음이다\n\n")
        # (Line 56) break;
        EUDBreak()
        # (Line 57) case 2001:
    _t4 = EUDSwitchCase()
    # (Line 58) PlayWAV("yashiro_aac.ogg");
    if _t4(2001):
        # (Line 59) v.stb.print("\n\n\x13\x02Yashiro Gaku\n\x13\x04게임 오버다, 너도 나도\n\n");
        DoActions(PlayWAV("yashiro_aac.ogg"))
        v.stb.print("\n\n\x13\x02Yashiro Gaku\n\x13\x04게임 오버다, 너도 나도\n\n")
        # (Line 61) break;
        EUDBreak()
        # (Line 62) }
    # (Line 63) }
    EUDEndSwitch()
    # (Line 65) function Text2(num)

# (Line 66) {
@EUDFunc
def Text2(num):
    # (Line 67) switch (num)
    EUDSwitch(num)
    # (Line 68) {
    # (Line 69) case 14000:
    _t1 = EUDSwitchCase()
    # (Line 70) v.stb.print("\n\n\x13\x02Yashiro Gaku\n\x13\x04고마워 사토루, 하지만 사탕은 안 들어 있어\n\n");
    if _t1(14000):
        v.stb.print("\n\n\x13\x02Yashiro Gaku\n\x13\x04고마워 사토루, 하지만 사탕은 안 들어 있어\n\n")
        # (Line 71) PlayWAV("yashiro_aaaa.ogg");
        # (Line 73) break;
        DoActions(PlayWAV("yashiro_aaaa.ogg"))
        EUDBreak()
        # (Line 74) case 14001:
    _t2 = EUDSwitchCase()
    # (Line 75) v.stb.print("\n\n\x13\x02Yashiro Gaku\n\x13\x04왜냐면, 이거... \x08내 차가 아니야\n\n");
    if _t2(14001):
        v.stb.print("\n\n\x13\x02Yashiro Gaku\n\x13\x04왜냐면, 이거... \x08내 차가 아니야\n\n")
        # (Line 77) break;
        EUDBreak()
        # (Line 78) }
    # (Line 80) }
    EUDEndSwitch()
    # (Line 82) function Text3(num)

# (Line 83) {
@EUDFunc
def Text3(num):
    # (Line 84) switch (num)
    EUDSwitch(num)
    # (Line 85) {
    # (Line 86) case 14000:
    _t1 = EUDSwitchCase()
    # (Line 87) v.stb.printAt(3,"\x13\x02Yashiro Gaku\n\x13\x04이런 이야기를 믿어 줄 것 같진 않지만, 굳이 말하마.");
    if _t1(14000):
        v.stb.printAt(3, "\x13\x02Yashiro Gaku\n\x13\x04이런 이야기를 믿어 줄 것 같진 않지만, 굳이 말하마.")
        # (Line 88) PlayWAV("yashiro_u1.ogg");
        # (Line 90) break;
        DoActions(PlayWAV("yashiro_u1.ogg"))
        EUDBreak()
        # (Line 91) case 14001:
    _t2 = EUDSwitchCase()
    # (Line 92) v.stb.printAt(3,"\x13\x02Yashiro Gaku\n\x13\x04아니, 너라면 알아줄 지도 몰라.");
    if _t2(14001):
        v.stb.printAt(3, "\x13\x02Yashiro Gaku\n\x13\x04아니, 너라면 알아줄 지도 몰라.")
        # (Line 94) break;
        EUDBreak()
        # (Line 95) case 14002:
    _t3 = EUDSwitchCase()
    # (Line 96) v.stb.printAt(3,"\x13\x02Yashiro Gaku\n\x13\x03스파이스\x04랑 만난 이후로,");
    if _t3(14002):
        v.stb.printAt(3, "\x13\x02Yashiro Gaku\n\x13\x03스파이스\x04랑 만난 이후로,")
        # (Line 97) PlayWAV("yashiro_u2.ogg");
        # (Line 99) break;
        DoActions(PlayWAV("yashiro_u2.ogg"))
        EUDBreak()
        # (Line 100) case 14003:
    _t4 = EUDSwitchCase()
    # (Line 101) v.stb.printAt(3,"\x13\x02Yashiro Gaku\n\x13\x04나에게는 \x17거미줄\x04이 보이게 됐다.");
    if _t4(14003):
        v.stb.printAt(3, "\x13\x02Yashiro Gaku\n\x13\x04나에게는 \x17거미줄\x04이 보이게 됐다.")
        # (Line 103) break;
        EUDBreak()
        # (Line 104) case 14004:
    _t5 = EUDSwitchCase()
    # (Line 105) v.stb.printAt(3,"\x13\x02Yashiro Gaku\n\x13\x04그게 보인 인간을 죽여 왔다.");
    if _t5(14004):
        v.stb.printAt(3, "\x13\x02Yashiro Gaku\n\x13\x04그게 보인 인간을 죽여 왔다.")
        # (Line 106) PlayWAV("yashiro_u3.ogg");
        # (Line 108) break;
        DoActions(PlayWAV("yashiro_u3.ogg"))
        EUDBreak()
        # (Line 109) case 14005:
    _t6 = EUDSwitchCase()
    # (Line 110) v.stb.printAt(3,"\x13\x02Yashiro Gaku\n\x13\x04그러나 어느 날\n\x13\x04한 명의 소년이 내 계획을 저지했다.");
    if _t6(14005):
        v.stb.printAt(3, "\x13\x02Yashiro Gaku\n\x13\x04그러나 어느 날\n\x13\x04한 명의 소년이 내 계획을 저지했다.")
        # (Line 111) PlayWAV("yashiro_u4.ogg");
        # (Line 113) break;
        DoActions(PlayWAV("yashiro_u4.ogg"))
        EUDBreak()
        # (Line 114) case 14006:
    _t7 = EUDSwitchCase()
    # (Line 115) v.stb.printAt(3,"\x13\x02Yashiro Gaku\n\x13\x04그리고 그 소년의 머리 위에도\n\x13\x17거미줄\x04이 나타났다.");
    if _t7(14006):
        v.stb.printAt(3, "\x13\x02Yashiro Gaku\n\x13\x04그리고 그 소년의 머리 위에도\n\x13\x17거미줄\x04이 나타났다.")
        # (Line 116) PlayWAV("yashiro_u5.ogg");
        # (Line 118) break;
        DoActions(PlayWAV("yashiro_u5.ogg"))
        EUDBreak()
        # (Line 119) case 14007:
    _t8 = EUDSwitchCase()
    # (Line 120) v.stb.printAt(3,"\x13\x02Yashiro Gaku\n\x13\x04그러나 그는 죽지 않았다.");
    if _t8(14007):
        v.stb.printAt(3, "\x13\x02Yashiro Gaku\n\x13\x04그러나 그는 죽지 않았다.")
        # (Line 121) PlayWAV("yashiro_u6.ogg");
        # (Line 123) break;
        DoActions(PlayWAV("yashiro_u6.ogg"))
        EUDBreak()
        # (Line 124) case 14008:
    _t9 = EUDSwitchCase()
    # (Line 125) v.stb.printAt(3,"\x13\x02Yashiro Gaku\n\x13\x04나는 그 녀석을 \x03스파이스\x04라고 이름짓고\n\x13\x04관찰하기로 했다.");
    if _t9(14008):
        v.stb.printAt(3, "\x13\x02Yashiro Gaku\n\x13\x04나는 그 녀석을 \x03스파이스\x04라고 이름짓고\n\x13\x04관찰하기로 했다.")
        # (Line 126) PlayWAV("yashiro_u7.ogg");
        # (Line 128) break;
        DoActions(PlayWAV("yashiro_u7.ogg"))
        EUDBreak()
        # (Line 129) case 14009:
    _t10 = EUDSwitchCase()
    # (Line 130) PlayWAV("yashiro_u8.ogg");
    if _t10(14009):
        # (Line 131) v.stb.printAt(3,"\x13\x02Yashiro Gaku\n\x13\x08그게 너야...");
        DoActions(PlayWAV("yashiro_u8.ogg"))
        v.stb.printAt(3, "\x13\x02Yashiro Gaku\n\x13\x08그게 너야...")
        # (Line 133) break;
        EUDBreak()
        # (Line 134) case 14010:
    _t11 = EUDSwitchCase()
    # (Line 135) v.stb.printAt(4,"\x13\x02Yashiro Gaku\n\x13\x04그런 게 있을 리가 없잖냐");
    if _t11(14010):
        v.stb.printAt(4, "\x13\x02Yashiro Gaku\n\x13\x04그런 게 있을 리가 없잖냐")
        # (Line 136) PlayWAV("yashiro_o_active.ogg");
        # (Line 138) break;
        DoActions(PlayWAV("yashiro_o_active.ogg"))
        EUDBreak()
        # (Line 139) case 14012:
    _t12 = EUDSwitchCase()
    # (Line 140) PlayWAV("yashiro_o_end.ogg");
    if _t12(14012):
        # (Line 141) v.stb.printAt(3,"\x13\x02Yashiro Gaku\n\x13\x04이건 나에게도 이판사판의 도박이었다");
        DoActions(PlayWAV("yashiro_o_end.ogg"))
        v.stb.printAt(3, "\x13\x02Yashiro Gaku\n\x13\x04이건 나에게도 이판사판의 도박이었다")
        # (Line 143) break;
        EUDBreak()
        # (Line 144) }
    # (Line 145) }
    EUDEndSwitch()
