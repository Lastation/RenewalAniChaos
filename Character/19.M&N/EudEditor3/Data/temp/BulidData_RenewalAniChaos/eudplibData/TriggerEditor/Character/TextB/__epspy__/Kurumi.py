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

# (Line 1) import getunitID as id;
import getunitID as id
# (Line 3) import System.Main as sym;
from System import Main as sym
# (Line 4) import Shop.Main as shm;
from Shop import Main as shm
# (Line 5) import Title.Main as tm;
from Title import Main as tm
# (Line 7) import Angel.Main as am;
from Angel import Main as am
# (Line 8) import Fairy.Main as fm;
from Fairy import Main as fm
# (Line 9) import Princess.Main as pm;
from Princess import Main as pm
# (Line 11) var cp;
cp = EUDVariable()
# (Line 12) var vTime;
vTime = EUDVariable()
# (Line 14) function onPluginStart();
# (Line 15) function beforeTriggerExec();
# (Line 16) function afterTriggerExec();
# (Line 18) function FixedUpdate();
# (Line 19) function PlayerUpdate(cp);
# (Line 21) function onPluginStart()
# (Line 22) {
@EUDFunc
def onPluginStart():
    # (Line 23) randomize();
    f_randomize()
    # (Line 25) am.Init();
    am.Init()
    # (Line 26) fm.Init();
    fm.Init()
    # (Line 27) pm.Init();
    pm.Init()
    # (Line 28) }
    # (Line 31) function beforeTriggerExec()

# (Line 32) {
@EUDFunc
def beforeTriggerExec():
    # (Line 33) EUDPlayerLoop()();
    EUDPlayerLoop()()
    # (Line 35) cp = getcurpl();
    cp << (f_getcurpl())
    # (Line 36) PlayerUpdate(cp);
    PlayerUpdate(cp)
    # (Line 38) EUDEndPlayerLoop();
    EUDEndPlayerLoop()
    # (Line 40) vTime += 1;
    vTime.__iadd__(1)
    # (Line 41) if (vTime >= 24)
    if EUDIf()(vTime >= 24):
        # (Line 42) {
        # (Line 43) FixedUpdate();
        FixedUpdate()
        # (Line 44) vTime = 0;
        vTime << (0)
        # (Line 45) }
        # (Line 46) }
    EUDEndIf()
    # (Line 48) function FixedUpdate()

# (Line 49) {
@EUDFunc
def FixedUpdate():
    # (Line 50) sym.FixedUpdate();
    sym.FixedUpdate()
    # (Line 51) shm.FixedUpdate();
    shm.FixedUpdate()
    # (Line 52) tm.FixedUpdate();
    tm.FixedUpdate()
    # (Line 54) am.FixedUpdate();
    am.FixedUpdate()
    # (Line 55) fm.FixedUpdate();
    fm.FixedUpdate()
    # (Line 56) pm.FixedUpdate();
    pm.FixedUpdate()
    # (Line 57) }
    # (Line 59) function PlayerUpdate(cp)

# (Line 60) {
@EUDFunc
def PlayerUpdate(cp_1):
    # (Line 61) id.Get_UnitID(cp);
    id.Get_UnitID(cp_1)
    # (Line 63) sym.PlayerUpdate(cp);
    sym.PlayerUpdate(cp_1)
    # (Line 64) shm.PlayerUpdate(cp);
    shm.PlayerUpdate(cp_1)
    # (Line 65) tm.PlayerUpdate(cp);
    tm.PlayerUpdate(cp_1)
    # (Line 66) }
