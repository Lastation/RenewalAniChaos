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
# (Line 5) const posX1 = PVariable();
posX1 = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 6) const posX2 = PVariable();
posX2 = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 8) const posY1 = PVariable();
posY1 = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 9) const posY2 = PVariable();
posY2 = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 11) var n = 0;
n = EUDCreateVariables(1)
_IGVA([n], lambda: [0])
# (Line 12) var max_n = 5;
max_n = EUDCreateVariables(1)
_IGVA([max_n], lambda: [5])
# (Line 14) function savePosRoutine(playerID)
# (Line 15) {
@EUDFunc
def f_savePosRoutine(playerID):
    # (Line 16) MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
    # (Line 18) var i = n;
    DoActions(MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere"))
    i = EUDVariable()
    i << (n)
    # (Line 20) for (; i > 0; i--)
    if EUDWhile()(i <= 0, neg=True):
        def _t2():
            i.__isub__(1)
        # (Line 21) {
        # (Line 22) posX1[i] = posX1[i - 1];
        _ARRW(posX1, i) << (posX1[i - 1])
        # (Line 23) posX2[i] = posX2[i - 1];
        _ARRW(posX2, i) << (posX2[i - 1])
        # (Line 24) posY1[i] = posY1[i - 1];
        _ARRW(posY1, i) << (posY1[i - 1])
        # (Line 25) posY2[i] = posY2[i - 1];
        _ARRW(posY2, i) << (posY2[i - 1])
        # (Line 26) }
        # (Line 28) posX1[0] = dwread_epd(EPD(0x58DC60 + (v.P_LocationID[playerID] - 1) * 20));
        EUDSetContinuePoint()
        _t2()
    EUDEndWhile()
    _ARRW(posX1, 0) << (f_dwread_epd(EPD(0x58DC60 + (v.P_LocationID[playerID] - 1) * 20)))
    # (Line 29) posX2[0] = dwread_epd(EPD(0x58DC60 + (v.P_LocationID[playerID] - 1) * 20 + 8));
    _ARRW(posX2, 0) << (f_dwread_epd(EPD(0x58DC60 + (v.P_LocationID[playerID] - 1) * 20 + 8)))
    # (Line 30) posY1[0] = dwread_epd(EPD(0x58DC60 + (v.P_LocationID[playerID] - 1) * 20 + 4));
    _ARRW(posY1, 0) << (f_dwread_epd(EPD(0x58DC60 + (v.P_LocationID[playerID] - 1) * 20 + 4)))
    # (Line 31) posY2[0] = dwread_epd(EPD(0x58DC60 + (v.P_LocationID[playerID] - 1) * 20 + 12));
    _ARRW(posY2, 0) << (f_dwread_epd(EPD(0x58DC60 + (v.P_LocationID[playerID] - 1) * 20 + 12)))
    # (Line 33) if (n < max_n) n++;
    if EUDIf()(n >= max_n, neg=True):
        n.__iadd__(1)
        # (Line 34) }
    EUDEndIf()
    # (Line 36) function main(playerID)

# (Line 37) {
@EUDFunc
def f_main(playerID):
    # (Line 38) if (v.P_WaitMain[playerID] == 0)
    if EUDIf()(v.P_WaitMain[playerID] == 0):
        # (Line 39) {
        # (Line 40) if (v.P_CountMain[playerID] == 0)
        if EUDIf()(v.P_CountMain[playerID] == 0):
            # (Line 41) {
            # (Line 42) if (v.P_LoopMain[playerID] == 0)
            if EUDIf()(v.P_LoopMain[playerID] == 0):
                # (Line 43) {
                # (Line 44) SetSwitch("Recall - Oda", Set);
                # (Line 45) MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
                DoActions(SetSwitch("Recall - Oda", Set))
                # (Line 46) }
                DoActions(MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere"))
                # (Line 48) if (v.P_LoopMain[playerID] == 1)
            EUDEndIf()
            if EUDIf()(v.P_LoopMain[playerID] == 1):
                # (Line 49) {
                # (Line 50) if (n == max_n)
                if EUDIf()(n == max_n):
                    # (Line 51) {
                    # (Line 52) dwwrite_epd(EPD(0x58DC60 + (v.P_LocationID[playerID] - 1) * 20), posX1[max_n]);
                    f_dwwrite_epd(EPD(0x58DC60 + (v.P_LocationID[playerID] - 1) * 20), posX1[max_n])
                    # (Line 53) dwwrite_epd(EPD(0x58DC60 + (v.P_LocationID[playerID] - 1) * 20 + 8), posX2[max_n]);
                    f_dwwrite_epd(EPD(0x58DC60 + (v.P_LocationID[playerID] - 1) * 20 + 8), posX2[max_n])
                    # (Line 54) dwwrite_epd(EPD(0x58DC60 + (v.P_LocationID[playerID] - 1) * 20 + 4), posY1[max_n]);
                    f_dwwrite_epd(EPD(0x58DC60 + (v.P_LocationID[playerID] - 1) * 20 + 4), posY1[max_n])
                    # (Line 55) dwwrite_epd(EPD(0x58DC60 + (v.P_LocationID[playerID] - 1) * 20 + 12), posY2[max_n]);
                    f_dwwrite_epd(EPD(0x58DC60 + (v.P_LocationID[playerID] - 1) * 20 + 12), posY2[max_n])
                    # (Line 57) MoveUnit(All, v.P_UnitID[playerID], playerID, "Anywhere", v.P_LocationID[playerID]);
                    # (Line 58) CenterView(v.P_LocationID[playerID]);
                    DoActions(MoveUnit(All, v.P_UnitID[playerID], playerID, "Anywhere", v.P_LocationID[playerID]))
                    # (Line 59) }
                    DoActions(CenterView(v.P_LocationID[playerID]))
                    # (Line 60) }
                EUDEndIf()
                # (Line 62) trg.Main_Wait(80);
            EUDEndIf()
            trg.Main_Wait(80)
            # (Line 64) v.P_LoopMain[playerID] += 1;
            _ARRW(v.P_LoopMain, playerID).__iadd__(1)
            # (Line 66) if (v.P_LoopMain[playerID] == 2)
            if EUDIf()(v.P_LoopMain[playerID] == 2):
                # (Line 67) {
                # (Line 68) v.P_CountMain[playerID] += 1;
                _ARRW(v.P_CountMain, playerID).__iadd__(1)
                # (Line 69) v.P_LoopMain[playerID] = 0;
                _ARRW(v.P_LoopMain, playerID) << (0)
                # (Line 70) }
                # (Line 71) }
            EUDEndIf()
            # (Line 72) else if (v.P_CountMain[playerID] == 1)
        if EUDElseIf()(v.P_CountMain[playerID] == 1):
            # (Line 73) {
            # (Line 74) SetSwitch("Recall - Oda", Clear);
            # (Line 75) SetDeaths(playerID, SetTo, 2160, " `UniqueCoolTime");
            DoActions(SetSwitch("Recall - Oda", Clear))
            # (Line 76) trg.SkillEnd();
            DoActions(SetDeaths(playerID, SetTo, 2160, " `UniqueCoolTime"))
            trg.SkillEnd()
            # (Line 77) }
            # (Line 78) }
        EUDEndIf()
        # (Line 79) MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
    EUDEndIf()
    # (Line 81) }
    DoActions(MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere"))