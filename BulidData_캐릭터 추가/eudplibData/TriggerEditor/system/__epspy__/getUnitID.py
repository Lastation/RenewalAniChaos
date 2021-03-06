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
# (Line 4) const NowIndex = PVariable();
NowIndex = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 5) const PrevIndex 	= PVariable();
PrevIndex = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 6) const PlayerID 	= PVariable();
PlayerID = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 7) const UnitID 	= PVariable();
UnitID = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 8) const UnitHP 	= PVariable();
UnitHP = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 10) function getUnitID(playerID)
# (Line 11) {
@EUDFunc
def f_getUnitID(playerID):
    # (Line 12) if (MemoryEPD(EPD(0x6284E8) + 12 *playerID, AtLeast, 1))
    if EUDIf()(MemoryEPD(EPD(0x6284E8) + 12 * playerID, AtLeast, 1)):
        # (Line 13) {
        # (Line 14) const selectedUnit = EPD(0x6284E8) + 12 * playerID;
        selectedUnit = EPD(0x6284E8) + 12 * playerID
        # (Line 15) NowIndex[playerID] = epdread_epd(selectedUnit);
        _ARRW(NowIndex, playerID) << (f_epdread_epd(selectedUnit))
        # (Line 16) PlayerID[playerID] = bread_epd(NowIndex[playerID] + 0x4C/4, 0);
        _ARRW(PlayerID, playerID) << (f_bread_epd(NowIndex[playerID] + 0x4C // 4, 0))
        # (Line 18) if(NowIndex[playerID] != PrevIndex[playerID] )
        if EUDIf()(NowIndex[playerID] == PrevIndex[playerID], neg=True):
            # (Line 19) {
            # (Line 20) PrevIndex[playerID] = NowIndex[playerID];
            _ARRW(PrevIndex, playerID) << (NowIndex[playerID])
            # (Line 21) UnitID[playerID] = bread_epd(NowIndex[playerID] + 0x64/4, 0);
            _ARRW(UnitID, playerID) << (f_bread_epd(NowIndex[playerID] + 0x64 // 4, 0))
            # (Line 22) UnitHP[playerID] = dwread_epd(NowIndex[playerID] + 0x008 / 4);
            _ARRW(UnitHP, playerID) << (f_dwread_epd(NowIndex[playerID] + 0x008 // 4))
            # (Line 23) UnitHP[playerID] = UnitHP[playerID] / 256;
            _ARRW(UnitHP, playerID) << (UnitHP[playerID] // 256)
            # (Line 24) }
            # (Line 25) }
        EUDEndIf()
        # (Line 26) }
    EUDEndIf()
