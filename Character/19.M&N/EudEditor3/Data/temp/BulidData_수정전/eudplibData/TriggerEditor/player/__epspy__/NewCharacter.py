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

# (Line 1) import Variable as v;
import Variable as v
# (Line 3) const s = StringBuffer(1000);
s = _CGFW(lambda: [StringBuffer(1000)], 1)[0]
# (Line 5) function NewCharacter();
# (Line 7) function NewCharacter()
# (Line 8) {
@EUDTracedFunc
def NewCharacter():
    # (Line 9) const cp = getcurpl();
    EUDTraceLog(9)
    cp = f_getcurpl()
    # (Line 11) v.userLevel[cp] = 1;
    EUDTraceLog(11)
    _ARRW(v.userLevel, cp) << (1)
    # (Line 12) v.userMaxHp[cp] = 320;
    EUDTraceLog(12)
    _ARRW(v.userMaxHp, cp) << (320)
    # (Line 13) v.userJob[cp] = 1;
    EUDTraceLog(13)
    _ARRW(v.userJob, cp) << (1)
    # (Line 14) v.userCharacter[cp] = epdread_epd(EPD(0x628438));
    EUDTraceLog(14)
    _ARRW(v.userCharacter, cp) << (f_epdread_epd(EPD(0x628438)))
    # (Line 16) switch(cp)
    EUDTraceLog(16)
    EUDSwitch(cp)
    # (Line 17) {
    # (Line 18) case 0:
    _t1 = EUDSwitchCase()
    # (Line 19) dwwrite(0x65FD00 + 9808 + 0 * 4, v.userMaxHp[getcurpl()] * 256);
    EUDTraceLog(18)
    if _t1(0):
        EUDTraceLog(19)
        f_dwwrite(0x65FD00 + 9808 + 0 * 4, v.userMaxHp[f_getcurpl()] * 256)
        # (Line 20) CreateUnit(1, "Terran Marine", "Start", CurrentPlayer);
        # (Line 21) break;
        EUDTraceLog(20)
        DoActions(CreateUnit(1, "Terran Marine", "Start", CurrentPlayer))
        EUDTraceLog(21)
        EUDBreak()
        # (Line 22) case 1:
    _t2 = EUDSwitchCase()
    # (Line 23) CreateUnit(1, "Terran Ghost", "Start", CurrentPlayer);
    EUDTraceLog(22)
    if _t2(1):
        # (Line 24) break;
        EUDTraceLog(23)
        DoActions(CreateUnit(1, "Terran Ghost", "Start", CurrentPlayer))
        EUDTraceLog(24)
        EUDBreak()
        # (Line 25) case 2:
    _t3 = EUDSwitchCase()
    # (Line 26) CreateUnit(1, "Sarah Kerrigan", "Start", CurrentPlayer);
    EUDTraceLog(25)
    if _t3(2):
        # (Line 27) break;
        EUDTraceLog(26)
        DoActions(CreateUnit(1, "Sarah Kerrigan", "Start", CurrentPlayer))
        EUDTraceLog(27)
        EUDBreak()
        # (Line 28) }
    # (Line 30) s.print("\x04플레이어들의 유닛을 생성합니다.");
    EUDEndSwitch()
    EUDTraceLog(30)
    s.print("\x04플레이어들의 유닛을 생성합니다.")
    # (Line 32) v.isAlive[cp] = 1;
    EUDTraceLog(32)
    _ARRW(v.isAlive, cp) << (1)
    # (Line 33) }
