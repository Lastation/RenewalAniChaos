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
# (Line 2) import Function as f;
import Function as f
# (Line 4) function main(cp)
# (Line 5) {
@EUDFunc
def f_main(cp):
    # (Line 6) if (f.delay[cp] == 0)
    if EUDIf()(f.delay[cp] == 0):
        # (Line 7) {
        # (Line 8) if (f.count[cp] == 0)
        if EUDIf()(f.count[cp] == 0):
            # (Line 9) {
            # (Line 10) if (f.loop[cp] < 2)
            if EUDIf()(f.loop[cp] >= 2, neg=True):
                # (Line 11) {
                # (Line 12) f.DotShape(cp, 1, "40 + 1n Wraith", 0, 0);
                f.DotShape(cp, 1, "40 + 1n Wraith", 0, 0)
                # (Line 14) KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
                # (Line 16) f.SkillWait(cp, 320);
                DoActions(KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp))
                f.SkillWait(cp, 320)
                # (Line 18) f.loop[cp] += 1;
                _ARRW(f.loop, cp).__iadd__(1)
                # (Line 19) }
                # (Line 20) else if (f.loop[cp] == 2)
            if EUDElseIf()(f.loop[cp] == 2):
                # (Line 21) {
                # (Line 22) f.SkillWait(cp, 80);
                f.SkillWait(cp, 80)
                # (Line 24) f.count[cp] += 1;
                _ARRW(f.count, cp).__iadd__(1)
                # (Line 25) f.loop[cp] = 0;
                _ARRW(f.loop, cp) << (0)
                # (Line 26) }
                # (Line 27) }
            EUDEndIf()
            # (Line 28) else if (f.count[cp] == 1)
        if EUDElseIf()(f.count[cp] == 1):
            # (Line 29) {
            # (Line 30) if (f.loop[cp] < 2)
            if EUDIf()(f.loop[cp] >= 2, neg=True):
                # (Line 31) {
                # (Line 32) f.DotShape(cp, 1, "40 + 1n Wraith", 0, 0);
                f.DotShape(cp, 1, "40 + 1n Wraith", 0, 0)
                # (Line 34) KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
                # (Line 36) f.SkillWait(cp, 320);
                DoActions(KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp))
                f.SkillWait(cp, 320)
                # (Line 38) f.loop[cp] += 1;
                _ARRW(f.loop, cp).__iadd__(1)
                # (Line 39) }
                # (Line 40) else if (f.loop[cp] == 2)
            if EUDElseIf()(f.loop[cp] == 2):
                # (Line 41) {
                # (Line 42) f.SkillWait(cp, 80);
                f.SkillWait(cp, 80)
                # (Line 44) f.count[cp] += 1;
                _ARRW(f.count, cp).__iadd__(1)
                # (Line 45) f.loop[cp] = 0;
                _ARRW(f.loop, cp) << (0)
                # (Line 46) }
                # (Line 47) }
            EUDEndIf()
            # (Line 48) else if (f.count[cp] == 2)
        if EUDElseIf()(f.count[cp] == 2):
            # (Line 49) {
            # (Line 50) if (f.loop[cp] < 4)
            if EUDIf()(f.loop[cp] >= 4, neg=True):
                # (Line 51) {
                # (Line 52) f.DotShape(cp, 8, "Bengalaas (Jungle)", 0, 0);
                f.DotShape(cp, 8, "Bengalaas (Jungle)", 0, 0)
                # (Line 53) f.DotShape(cp, 1, "40 + 1n Guardian", 0, 0);
                f.DotShape(cp, 1, "40 + 1n Guardian", 0, 0)
                # (Line 55) KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", cp);
                # (Line 56) KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
                DoActions(KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", cp))
                # (Line 58) f.SkillWait(cp, 80);
                DoActions(KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp))
                f.SkillWait(cp, 80)
                # (Line 60) f.loop[cp] += 1;
                _ARRW(f.loop, cp).__iadd__(1)
                # (Line 61) }
                # (Line 62) else if (f.loop[cp] == 4)
            if EUDElseIf()(f.loop[cp] == 4):
                # (Line 63) {
                # (Line 64) f.SkillWait(cp, 160);
                f.SkillWait(cp, 160)
                # (Line 66) f.loop[cp] += 1;
                _ARRW(f.loop, cp).__iadd__(1)
                # (Line 67) }
                # (Line 68) else if (f.loop[cp] == 5)
            if EUDElseIf()(f.loop[cp] == 5):
                # (Line 69) {
                # (Line 70) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
                # (Line 71) MoveLocation("26.Yume_Bozo", f.heroID[cp], cp, "Anywhere");
                DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
                # (Line 73) if (cp < 3)
                DoActions(MoveLocation("26.Yume_Bozo", f.heroID[cp], cp, "Anywhere"))
                if EUDIf()(cp >= 3, neg=True):
                    # (Line 74) {
                    # (Line 75) if (Bring(3, AtLeast, 1, f.heroID[3], "26.Yume_Bozo"))
                    if EUDIf()(Bring(3, AtLeast, 1, f.heroID[3], "26.Yume_Bozo")):
                        # (Line 76) {
                        # (Line 77) MoveLocation(f.location[cp], f.heroID[3], 3, "Anywhere");
                        # (Line 78) }
                        DoActions(MoveLocation(f.location[cp], f.heroID[3], 3, "Anywhere"))
                        # (Line 79) else if (Bring(4, AtLeast, 1, f.heroID[4], "26.Yume_Bozo"))
                    if EUDElseIf()(Bring(4, AtLeast, 1, f.heroID[4], "26.Yume_Bozo")):
                        # (Line 80) {
                        # (Line 81) MoveLocation(f.location[cp], f.heroID[4], 4, "Anywhere");
                        # (Line 82) }
                        DoActions(MoveLocation(f.location[cp], f.heroID[4], 4, "Anywhere"))
                        # (Line 83) else if (Bring(5, AtLeast, 1, f.heroID[5], "26.Yume_Bozo"))
                    if EUDElseIf()(Bring(5, AtLeast, 1, f.heroID[5], "26.Yume_Bozo")):
                        # (Line 84) {
                        # (Line 85) MoveLocation(f.location[cp], f.heroID[5], 5, "Anywhere");
                        # (Line 86) }
                        DoActions(MoveLocation(f.location[cp], f.heroID[5], 5, "Anywhere"))
                        # (Line 88) }
                    EUDEndIf()
                    # (Line 89) else if (cp >= 3)
                if EUDElseIf()(cp >= 3):
                    # (Line 90) {
                    # (Line 91) if (Bring(0, AtLeast, 1, f.heroID[0], "26.Yume_Bozo"))
                    if EUDIf()(Bring(0, AtLeast, 1, f.heroID[0], "26.Yume_Bozo")):
                        # (Line 92) {
                        # (Line 93) MoveLocation(f.location[cp], f.heroID[0], 0, "Anywhere");
                        # (Line 94) }
                        DoActions(MoveLocation(f.location[cp], f.heroID[0], 0, "Anywhere"))
                        # (Line 95) else if (Bring(1, AtLeast, 1, f.heroID[1], "26.Yume_Bozo"))
                    if EUDElseIf()(Bring(1, AtLeast, 1, f.heroID[1], "26.Yume_Bozo")):
                        # (Line 96) {
                        # (Line 97) MoveLocation(f.location[cp],f.heroID[1], 1, "Anywhere");
                        # (Line 98) }
                        DoActions(MoveLocation(f.location[cp], f.heroID[1], 1, "Anywhere"))
                        # (Line 99) else if (Bring(2, AtLeast, 1, f.heroID[2], "26.Yume_Bozo"))
                    if EUDElseIf()(Bring(2, AtLeast, 1, f.heroID[2], "26.Yume_Bozo")):
                        # (Line 100) {
                        # (Line 101) MoveLocation(f.location[cp], f.heroID[2], 2, "Anywhere");
                        # (Line 102) }
                        DoActions(MoveLocation(f.location[cp], f.heroID[2], 2, "Anywhere"))
                        # (Line 103) }
                    EUDEndIf()
                    # (Line 104) MoveUnit(All, f.heroID[cp], cp, "Anywhere", f.location[cp]);
                EUDEndIf()
                # (Line 106) f.SkillWait(cp, 80);
                DoActions(MoveUnit(All, f.heroID[cp], cp, "Anywhere", f.location[cp]))
                f.SkillWait(cp, 80)
                # (Line 108) f.count[cp] += 1;
                _ARRW(f.count, cp).__iadd__(1)
                # (Line 109) f.loop[cp] = 0;
                _ARRW(f.loop, cp) << (0)
                # (Line 110) }
                # (Line 112) }
            EUDEndIf()
            # (Line 113) else if (f.count[cp] == 3)
        if EUDElseIf()(f.count[cp] == 3):
            # (Line 114) {
            # (Line 115) if (f.loop[cp] < 4)
            if EUDIf()(f.loop[cp] >= 4, neg=True):
                # (Line 116) {
                # (Line 117) f.EdgeShape(cp, 1, "Kakaru (Twilight)", 0, 3 + 2 * f.loop[cp], 50 + 50 * f.loop[cp]);
                f.EdgeShape(cp, 1, "Kakaru (Twilight)", 0, 3 + 2 * f.loop[cp], 50 + 50 * f.loop[cp])
                # (Line 118) KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
                # (Line 120) if (f.loop[cp] % 2 == 0)
                DoActions(KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp))
                if EUDIf()(f.loop[cp] % 2 == 0):
                    # (Line 121) {
                    # (Line 122) f.EdgeShape(cp, 1, "40 + 1n Zealot", 0, 3 + 2 * f.loop[cp], 50 + 50 * f.loop[cp]);
                    f.EdgeShape(cp, 1, "40 + 1n Zealot", 0, 3 + 2 * f.loop[cp], 50 + 50 * f.loop[cp])
                    # (Line 123) KillUnitAt(All, "40 + 1n Zealot", "Anywhere", cp);
                    # (Line 124) }
                    DoActions(KillUnitAt(All, "40 + 1n Zealot", "Anywhere", cp))
                    # (Line 125) else
                    # (Line 126) {
                if EUDElse()():
                    # (Line 127) f.EdgeShape(cp, 1, "Protoss Dark Templar", 0, 3 + 2 * f.loop[cp], 50 + 50 * f.loop[cp]);
                    f.EdgeShape(cp, 1, "Protoss Dark Templar", 0, 3 + 2 * f.loop[cp], 50 + 50 * f.loop[cp])
                    # (Line 128) KillUnitAt(All, "Protoss Dark Templar", "Anywhere", cp);
                    # (Line 129) }
                    DoActions(KillUnitAt(All, "Protoss Dark Templar", "Anywhere", cp))
                    # (Line 131) f.SkillWait(cp, 80);
                EUDEndIf()
                f.SkillWait(cp, 80)
                # (Line 133) f.loop[cp] += 1;
                _ARRW(f.loop, cp).__iadd__(1)
                # (Line 134) }
                # (Line 135) else if (f.loop[cp] == 4)
            if EUDElseIf()(f.loop[cp] == 4):
                # (Line 136) {
                # (Line 137) f.LineShape(cp, 1, "Target", 45, 5, 75, 75);
                f.LineShape(cp, 1, "Target", 45, 5, 75, 75)
                # (Line 138) f.LineShape(cp, 1, "Target", 45, 5, 75, 0);
                f.LineShape(cp, 1, "Target", 45, 5, 75, 0)
                # (Line 139) f.LineShape(cp, 1, "Target", 225, 5, 75, 75);
                f.LineShape(cp, 1, "Target", 225, 5, 75, 75)
                # (Line 140) f.LineShape(cp, 1, "Protoss Dark Archon", 45, 5, 75, 75);
                f.LineShape(cp, 1, "Protoss Dark Archon", 45, 5, 75, 75)
                # (Line 141) f.LineShape(cp, 1, "Protoss Dark Archon", 45, 5, 75, 0);
                f.LineShape(cp, 1, "Protoss Dark Archon", 45, 5, 75, 0)
                # (Line 142) f.LineShape(cp, 1, "Protoss Dark Archon", 225, 5, 75, 75);
                f.LineShape(cp, 1, "Protoss Dark Archon", 225, 5, 75, 75)
                # (Line 143) KillUnitAt(All, "Target", "Anywhere", cp);
                # (Line 144) KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
                DoActions(KillUnitAt(All, "Target", "Anywhere", cp))
                # (Line 146) f.SkillWait(cp, 80);
                DoActions(KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp))
                f.SkillWait(cp, 80)
                # (Line 148) f.loop[cp] += 1;
                _ARRW(f.loop, cp).__iadd__(1)
                # (Line 149) }
                # (Line 150) else if (f.loop[cp] == 5)
            if EUDElseIf()(f.loop[cp] == 5):
                # (Line 151) {
                # (Line 152) f.LineShape(cp, 1, "80 + 1n Artanis", 135, 5, 75, 75);
                f.LineShape(cp, 1, "80 + 1n Artanis", 135, 5, 75, 75)
                # (Line 153) f.LineShape(cp, 1, "80 + 1n Artanis", 135, 5, 75, 0);
                f.LineShape(cp, 1, "80 + 1n Artanis", 135, 5, 75, 0)
                # (Line 154) f.LineShape(cp, 1, "80 + 1n Artanis", 315, 5, 75, 75);
                f.LineShape(cp, 1, "80 + 1n Artanis", 315, 5, 75, 75)
                # (Line 155) f.LineShape(cp, 1, " Unit. Hoffnung 25000", 135, 5, 75, 75);
                f.LineShape(cp, 1, " Unit. Hoffnung 25000", 135, 5, 75, 75)
                # (Line 156) f.LineShape(cp, 1, " Unit. Hoffnung 25000", 135, 5, 75, 0);
                f.LineShape(cp, 1, " Unit. Hoffnung 25000", 135, 5, 75, 0)
                # (Line 157) f.LineShape(cp, 1, " Unit. Hoffnung 25000", 315, 5, 75, 75);
                f.LineShape(cp, 1, " Unit. Hoffnung 25000", 315, 5, 75, 75)
                # (Line 158) KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
                # (Line 160) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
                DoActions(KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp))
                # (Line 161) Order("80 + 1n Artanis", cp, "Anywhere", Attack, f.location[cp]);
                DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
                # (Line 163) f.SkillWait(cp, 80);
                DoActions(Order("80 + 1n Artanis", cp, "Anywhere", Attack, f.location[cp]))
                f.SkillWait(cp, 80)
                # (Line 165) f.loop[cp] += 1;
                _ARRW(f.loop, cp).__iadd__(1)
                # (Line 166) }
                # (Line 167) else if (f.loop[cp] == 6)
            if EUDElseIf()(f.loop[cp] == 6):
                # (Line 168) {
                # (Line 169) RemoveUnitAt(All, "80 + 1n Artanis", "Anywhere", cp);
                # (Line 171) f.LineShape(cp, 1, "Kakaru (Twilight)", 135, 5, 75, 75);
                DoActions(RemoveUnitAt(All, "80 + 1n Artanis", "Anywhere", cp))
                f.LineShape(cp, 1, "Kakaru (Twilight)", 135, 5, 75, 75)
                # (Line 172) f.LineShape(cp, 1, "Kakaru (Twilight)", 135, 5, 75, 0);
                f.LineShape(cp, 1, "Kakaru (Twilight)", 135, 5, 75, 0)
                # (Line 173) f.LineShape(cp, 1, "Kakaru (Twilight)", 315, 5, 75, 75);
                f.LineShape(cp, 1, "Kakaru (Twilight)", 315, 5, 75, 75)
                # (Line 174) KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
                # (Line 176) f.SkillWait(cp, 80);
                DoActions(KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp))
                f.SkillWait(cp, 80)
                # (Line 178) f.loop[cp] += 1;
                _ARRW(f.loop, cp).__iadd__(1)
                # (Line 179) }
                # (Line 180) else if (f.loop[cp] == 7)
            if EUDElseIf()(f.loop[cp] == 7):
                # (Line 181) {
                # (Line 182) f.LineShape(cp, 1, "40 + 1n Wraith", 45, 5, 75, 75);
                f.LineShape(cp, 1, "40 + 1n Wraith", 45, 5, 75, 75)
                # (Line 183) f.LineShape(cp, 1, "40 + 1n Wraith", 45, 5, 75, 0);
                f.LineShape(cp, 1, "40 + 1n Wraith", 45, 5, 75, 0)
                # (Line 184) f.LineShape(cp, 1, "40 + 1n Wraith", 225, 5, 75, 75);
                f.LineShape(cp, 1, "40 + 1n Wraith", 225, 5, 75, 75)
                # (Line 185) f.LineShape(cp, 1, " Unit. Hoffnung 25000", 45, 5, 75, 75);
                f.LineShape(cp, 1, " Unit. Hoffnung 25000", 45, 5, 75, 75)
                # (Line 186) f.LineShape(cp, 1, " Unit. Hoffnung 25000", 45, 5, 75, 0);
                f.LineShape(cp, 1, " Unit. Hoffnung 25000", 45, 5, 75, 0)
                # (Line 187) f.LineShape(cp, 1, " Unit. Hoffnung 25000", 225, 5, 75, 75);
                f.LineShape(cp, 1, " Unit. Hoffnung 25000", 225, 5, 75, 75)
                # (Line 188) KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
                # (Line 190) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
                DoActions(KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp))
                # (Line 191) Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);
                DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
                # (Line 193) f.SkillWait(cp, 80);
                DoActions(Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]))
                f.SkillWait(cp, 80)
                # (Line 195) f.loop[cp] += 1;
                _ARRW(f.loop, cp).__iadd__(1)
                # (Line 196) }
                # (Line 197) else if (f.loop[cp] == 8)
            if EUDElseIf()(f.loop[cp] == 8):
                # (Line 198) {
                # (Line 199) RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
                # (Line 201) f.LineShape(cp, 1, "Kakaru (Twilight)", 45, 5, 75, 75);
                DoActions(RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp))
                f.LineShape(cp, 1, "Kakaru (Twilight)", 45, 5, 75, 75)
                # (Line 202) f.LineShape(cp, 1, "Kakaru (Twilight)", 45, 5, 75, 0);
                f.LineShape(cp, 1, "Kakaru (Twilight)", 45, 5, 75, 0)
                # (Line 203) f.LineShape(cp, 1, "Kakaru (Twilight)", 225, 5, 75, 75);
                f.LineShape(cp, 1, "Kakaru (Twilight)", 225, 5, 75, 75)
                # (Line 204) KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
                # (Line 206) f.SkillWait(cp, 80);
                DoActions(KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp))
                f.SkillWait(cp, 80)
                # (Line 208) f.loop[cp] += 1;
                _ARRW(f.loop, cp).__iadd__(1)
                # (Line 209) }
                # (Line 211) else if (f.loop[cp] == 9)
            if EUDElseIf()(f.loop[cp] == 9):
                # (Line 212) {
                # (Line 213) SetDeaths(cp, SetTo, 1080, " `UniqueCoolTime");
                # (Line 215) f.SkillWait(cp, 80);
                DoActions(SetDeaths(cp, SetTo, 1080, " `UniqueCoolTime"))
                f.SkillWait(cp, 80)
                # (Line 217) f.count[cp] += 1;
                _ARRW(f.count, cp).__iadd__(1)
                # (Line 218) f.loop[cp] = 0;
                _ARRW(f.loop, cp) << (0)
                # (Line 219) }
                # (Line 220) }
            EUDEndIf()
            # (Line 221) else if (f.count[cp] == 4)
        if EUDElseIf()(f.count[cp] == 4):
            # (Line 222) {
            # (Line 223) if (Bring(cp, AtLeast, 1, "Protoss Carrier", "[Skill]UseSkill"))
            if EUDIf()(Bring(cp, AtLeast, 1, "Protoss Carrier", "[Skill]UseSkill")):
                # (Line 224) {
                # (Line 225) f.wait[cp] = 0;
                _ARRW(f.wait, cp) << (0)
                # (Line 226) f.count[cp] = 0;
                _ARRW(f.count, cp) << (0)
                # (Line 227) f.loop[cp] = 0;
                _ARRW(f.loop, cp) << (0)
                # (Line 228) f.step[cp] = 200;
                _ARRW(f.step, cp) << (200)
                # (Line 229) KillUnitAt(1, "Protoss Carrier", "[Skill]UseSkill", cp);
                # (Line 230) }
                DoActions(KillUnitAt(1, "Protoss Carrier", "[Skill]UseSkill", cp))
                # (Line 231) else if (Bring(cp, AtLeast, 1, "Protoss Arbiter", "[Skill]UseSkill"))
            if EUDElseIf()(Bring(cp, AtLeast, 1, "Protoss Arbiter", "[Skill]UseSkill")):
                # (Line 232) {
                # (Line 233) f.wait[cp] = 0;
                _ARRW(f.wait, cp) << (0)
                # (Line 234) f.count[cp] = 0;
                _ARRW(f.count, cp) << (0)
                # (Line 235) f.loop[cp] = 0;
                _ARRW(f.loop, cp) << (0)
                # (Line 236) f.step[cp] = 300;
                _ARRW(f.step, cp) << (300)
                # (Line 237) KillUnitAt(1, "Protoss Arbiter", "[Skill]UseSkill", cp);
                # (Line 238) }
                DoActions(KillUnitAt(1, "Protoss Arbiter", "[Skill]UseSkill", cp))
                # (Line 240) else if (Bring(cp, AtLeast, 1, "Protoss Scout", "[Skill]UseSkill"))
            if EUDElseIf()(Bring(cp, AtLeast, 1, "Protoss Scout", "[Skill]UseSkill")):
                # (Line 241) {
                # (Line 242) f.wait[cp] = 0;
                _ARRW(f.wait, cp) << (0)
                # (Line 243) f.count[cp] = 0;
                _ARRW(f.count, cp) << (0)
                # (Line 244) f.loop[cp] = 0;
                _ARRW(f.loop, cp) << (0)
                # (Line 245) f.step[cp] = 100;
                _ARRW(f.step, cp) << (100)
                # (Line 246) KillUnitAt(1, "Protoss Scout", "[Skill]UseSkill", cp);
                # (Line 247) }
                DoActions(KillUnitAt(1, "Protoss Scout", "[Skill]UseSkill", cp))
                # (Line 248) else
                # (Line 249) {
            if EUDElse()():
                # (Line 250) f.SkillEnd(cp);
                f.SkillEnd(cp)
                # (Line 251) }
                # (Line 252) }
            EUDEndIf()
            # (Line 253) }
        EUDEndIf()
        # (Line 254) }
    EUDEndIf()