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

# (Line 1) import Function as f;
import Function as f
# (Line 3) function main(cp)
# (Line 4) {
@EUDFunc
def f_main(cp):
    # (Line 5) if (f.delay[cp] == 0)
    if EUDIf()(f.delay[cp] == 0):
        # (Line 6) {
        # (Line 7) if (f.count[cp] == 0)
        if EUDIf()(f.count[cp] == 0):
            # (Line 8) {
            # (Line 9) if (f.loop[cp] == 0)
            if EUDIf()(f.loop[cp] == 0):
                # (Line 10) {
                # (Line 11) f.LineShape(cp, 1, "40 + 1n Wraith", 45, 4, 75, 0);
                f.LineShape(cp, 1, "40 + 1n Wraith", 45, 4, 75, 0)
                # (Line 12) f.LineShape(cp, 1, "40 + 1n Goliath", 45, 4, 75, 0);
                f.LineShape(cp, 1, "40 + 1n Goliath", 45, 4, 75, 0)
                # (Line 13) KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);
                # (Line 15) Order("40 + 1n Wraith", cp, "Anywhere", Attack, "Anywhere");
                DoActions(KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp))
                # (Line 16) }
                DoActions(Order("40 + 1n Wraith", cp, "Anywhere", Attack, "Anywhere"))
                # (Line 17) else if (f.loop[cp] == 1)
            if EUDElseIf()(f.loop[cp] == 1):
                # (Line 18) {
                # (Line 19) KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
                # (Line 20) }
                DoActions(KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp))
                # (Line 21) else if (f.loop[cp] == 2)
            if EUDElseIf()(f.loop[cp] == 2):
                # (Line 22) {
                # (Line 23) f.LineShape(cp, 1, "40 + 1n Wraith", 135, 4, 75, 0);
                f.LineShape(cp, 1, "40 + 1n Wraith", 135, 4, 75, 0)
                # (Line 24) f.LineShape(cp, 1, "40 + 1n Goliath", 135, 4, 75, 0);
                f.LineShape(cp, 1, "40 + 1n Goliath", 135, 4, 75, 0)
                # (Line 25) KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);
                # (Line 27) Order("40 + 1n Wraith", cp, "Anywhere", Attack, "Anywhere");
                DoActions(KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp))
                # (Line 28) }
                DoActions(Order("40 + 1n Wraith", cp, "Anywhere", Attack, "Anywhere"))
                # (Line 29) else if (f.loop[cp] == 3)
            if EUDElseIf()(f.loop[cp] == 3):
                # (Line 30) {
                # (Line 31) KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
                # (Line 32) }
                DoActions(KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp))
                # (Line 34) f.SkillWait(cp, 160);
            EUDEndIf()
            f.SkillWait(cp, 160)
            # (Line 36) f.loop[cp] += 1;
            _ARRW(f.loop, cp).__iadd__(1)
            # (Line 38) if (f.loop[cp] == 4)
            if EUDIf()(f.loop[cp] == 4):
                # (Line 39) {
                # (Line 40) f.count[cp] += 1;
                _ARRW(f.count, cp).__iadd__(1)
                # (Line 41) f.loop[cp] = 0;
                _ARRW(f.loop, cp) << (0)
                # (Line 42) }
                # (Line 43) }
            EUDEndIf()
            # (Line 44) else if (f.count[cp] == 1)
        if EUDElseIf()(f.count[cp] == 1):
            # (Line 45) {
            # (Line 46) if (f.loop[cp] == 0)
            if EUDIf()(f.loop[cp] == 0):
                # (Line 47) {
                # (Line 48) f.SquareShape(cp, 1, "50 + 1n Tank", 75, 0);
                f.SquareShape(cp, 1, "50 + 1n Tank", 75, 0)
                # (Line 49) KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
                # (Line 50) }
                DoActions(KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp))
                # (Line 51) else if (f.loop[cp] == 1)
            if EUDElseIf()(f.loop[cp] == 1):
                # (Line 52) {
                # (Line 53) f.SquareShape(cp, 1, "50 + 1n Tank", 125, 50);
                f.SquareShape(cp, 1, "50 + 1n Tank", 125, 50)
                # (Line 54) f.SquareShape(cp, 1, "50 + 1n Tank", 50, 125);
                f.SquareShape(cp, 1, "50 + 1n Tank", 50, 125)
                # (Line 55) KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
                # (Line 56) }
                DoActions(KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp))
                # (Line 57) else if (f.loop[cp] == 3)
            if EUDElseIf()(f.loop[cp] == 3):
                # (Line 58) {
                # (Line 59) f.LineShape(cp, 1, "40 + 1n Wraith", 45, 4, 75, 0);
                f.LineShape(cp, 1, "40 + 1n Wraith", 45, 4, 75, 0)
                # (Line 60) f.LineShape(cp, 1, "40 + 1n Goliath", 45, 4, 75, 0);
                f.LineShape(cp, 1, "40 + 1n Goliath", 45, 4, 75, 0)
                # (Line 61) f.LineShape(cp, 1, "40 + 1n Wraith", 135, 4, 75, 0);
                f.LineShape(cp, 1, "40 + 1n Wraith", 135, 4, 75, 0)
                # (Line 62) f.LineShape(cp, 1, "40 + 1n Goliath", 135, 4, 75, 0);
                f.LineShape(cp, 1, "40 + 1n Goliath", 135, 4, 75, 0)
                # (Line 63) KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);
                # (Line 64) Order("40 + 1n Wraith", cp, "Anywhere", Attack, "Anywhere");
                DoActions(KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp))
                # (Line 65) }
                DoActions(Order("40 + 1n Wraith", cp, "Anywhere", Attack, "Anywhere"))
                # (Line 66) else if (f.loop[cp] == 4)
            if EUDElseIf()(f.loop[cp] == 4):
                # (Line 67) {
                # (Line 68) f.SquareShape(cp, 1, " Unit. Hoffnung 25000", 75, 0);
                f.SquareShape(cp, 1, " Unit. Hoffnung 25000", 75, 0)
                # (Line 69) f.SquareShape(cp, 1, " Unit. Hoffnung 25000", 125, 50);
                f.SquareShape(cp, 1, " Unit. Hoffnung 25000", 125, 50)
                # (Line 70) f.SquareShape(cp, 1, " Unit. Hoffnung 25000", 50, 125);
                f.SquareShape(cp, 1, " Unit. Hoffnung 25000", 50, 125)
                # (Line 71) KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
                # (Line 72) KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
                DoActions(KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp))
                # (Line 73) }
                DoActions(KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp))
                # (Line 75) f.SkillWait(cp, 160);
            EUDEndIf()
            f.SkillWait(cp, 160)
            # (Line 77) f.loop[cp] += 1;
            _ARRW(f.loop, cp).__iadd__(1)
            # (Line 79) if (f.loop[cp] == 5)
            if EUDIf()(f.loop[cp] == 5):
                # (Line 80) {
                # (Line 81) f.count[cp] += 1;
                _ARRW(f.count, cp).__iadd__(1)
                # (Line 82) f.loop[cp] = 0;
                _ARRW(f.loop, cp) << (0)
                # (Line 83) }
                # (Line 84) }
            EUDEndIf()
            # (Line 85) else if (f.count[cp] == 2)
        if EUDElseIf()(f.count[cp] == 2):
            # (Line 86) {
            # (Line 87) f.SkillEnd(cp);
            f.SkillEnd(cp)
            # (Line 88) }
            # (Line 89) }
        EUDEndIf()
        # (Line 90) }
    EUDEndIf()