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
# (Line 4) const s = StringBuffer();
s = _CGFW(lambda: [StringBuffer()], 1)[0]
# (Line 6) function main(cp)
# (Line 7) {
@EUDFunc
def f_main(cp):
    # (Line 8) f.HoldPosition(cp);
    f.HoldPosition(cp)
    # (Line 9) ModifyUnitShields(All, f.heroID[cp], cp, "Anywhere", 1);
    # (Line 10) MoveUnit(All, "40 + 1n Marine", cp, "Anywhere", "[Skill]HoldPosition");
    DoActions(ModifyUnitShields(All, f.heroID[cp], cp, "Anywhere", 1))
    # (Line 11) MoveUnit(All, "40 + 1n Ghost", cp, "Anywhere", "[Skill]HoldPosition");
    DoActions(MoveUnit(All, "40 + 1n Marine", cp, "Anywhere", "[Skill]HoldPosition"))
    # (Line 13) if (f.delay[cp] == 0)
    DoActions(MoveUnit(All, "40 + 1n Ghost", cp, "Anywhere", "[Skill]HoldPosition"))
    if EUDIf()(f.delay[cp] == 0):
        # (Line 14) {
        # (Line 15) if (f.count[cp] == 0)
        if EUDIf()(f.count[cp] == 0):
            # (Line 16) {
            # (Line 17) if (f.loop[cp] < 4)
            if EUDIf()(f.loop[cp] >= 4, neg=True):
                # (Line 18) {
                # (Line 19) SetDeaths(cp, SetTo, 1, " `ShieldRecharge");
                # (Line 20) f.SquareShape(cp, 1, "Zerg Devourer", 50 * f.loop[cp] + 50, 0);
                DoActions(SetDeaths(cp, SetTo, 1, " `ShieldRecharge"))
                f.SquareShape(cp, 1, "Zerg Devourer", 50 * f.loop[cp] + 50, 0)
                # (Line 21) KillUnitAt(All, "Zerg Devourer", "Anywhere", cp);
                # (Line 23) f.SkillWait(cp, 80);
                DoActions(KillUnitAt(All, "Zerg Devourer", "Anywhere", cp))
                f.SkillWait(cp, 80)
                # (Line 25) f.loop[cp] += 1;
                _ARRW(f.loop, cp).__iadd__(1)
                # (Line 26) }
                # (Line 27) else if (f.loop[cp] < 12)
            if EUDElseIf()(f.loop[cp] >= 12, neg=True):
                # (Line 28) {
                # (Line 29) f.SquareShape(cp, 1, "Zerg Devourer", 200 - 25 * (f.loop[cp] - 4), 25 * (f.loop[cp] - 4));
                f.SquareShape(cp, 1, "Zerg Devourer", 200 - 25 * (f.loop[cp] - 4), 25 * (f.loop[cp] - 4))
                # (Line 30) KillUnitAt(All, "Zerg Devourer", "Anywhere", cp);
                # (Line 32) if (f.loop[cp] % 2 == 0)
                DoActions(KillUnitAt(All, "Zerg Devourer", "Anywhere", cp))
                if EUDIf()(f.loop[cp] % 2 == 0):
                    # (Line 33) {
                    # (Line 34) f.SquareShape(cp, 1, "40 + 1n Marine", 200 - 25 * (f.loop[cp] - 4), 25 * (f.loop[cp] - 4));
                    f.SquareShape(cp, 1, "40 + 1n Marine", 200 - 25 * (f.loop[cp] - 4), 25 * (f.loop[cp] - 4))
                    # (Line 35) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
                    # (Line 36) MoveUnit(All, "40 + 1n Marine", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
                    DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
                    # (Line 37) Order("40 + 1n Marine", cp, "Anywhere", Attack, f.location[cp]);
                    DoActions(MoveUnit(All, "40 + 1n Marine", cp, "[Skill]Unit_Wait_ALL", f.location[cp]))
                    # (Line 38) }
                    DoActions(Order("40 + 1n Marine", cp, "Anywhere", Attack, f.location[cp]))
                    # (Line 40) f.SkillWait(cp, 80);
                EUDEndIf()
                f.SkillWait(cp, 80)
                # (Line 42) f.loop[cp] += 1;
                _ARRW(f.loop, cp).__iadd__(1)
                # (Line 44) }
                # (Line 45) else if (f.loop[cp] < 16)
            if EUDElseIf()(f.loop[cp] >= 16, neg=True):
                # (Line 46) {
                # (Line 47) f.SquareShape(cp, 1, "Zerg Devourer", 0, 200 - 50 * (f.loop[cp] - 12));
                f.SquareShape(cp, 1, "Zerg Devourer", 0, 200 - 50 * (f.loop[cp] - 12))
                # (Line 48) KillUnitAt(All, "Zerg Devourer", "Anywhere", cp);
                # (Line 50) f.SkillWait(cp, 80);
                DoActions(KillUnitAt(All, "Zerg Devourer", "Anywhere", cp))
                f.SkillWait(cp, 80)
                # (Line 52) f.loop[cp] += 1;
                _ARRW(f.loop, cp).__iadd__(1)
                # (Line 53) }
                # (Line 54) else if (f.loop[cp] == 16)
            if EUDElseIf()(f.loop[cp] == 16):
                # (Line 55) {
                # (Line 56) f.SkillWait(cp, 1080);
                f.SkillWait(cp, 1080)
                # (Line 58) f.loop[cp] += 1;
                _ARRW(f.loop, cp).__iadd__(1)
                # (Line 59) }
                # (Line 60) else if (f.loop[cp] == 17)
            if EUDElseIf()(f.loop[cp] == 17):
                # (Line 61) {
                # (Line 62) f.Voice_Routine(cp, 6);
                f.Voice_Routine(cp, 6)
                # (Line 64) f.SkillWait(cp, 80);
                f.SkillWait(cp, 80)
                # (Line 66) f.count[cp] += 1;
                _ARRW(f.count, cp).__iadd__(1)
                # (Line 67) f.loop[cp] = 0;
                _ARRW(f.loop, cp) << (0)
                # (Line 68) }
                # (Line 70) }
            EUDEndIf()
            # (Line 71) else if (f.count[cp] == 1)
        if EUDElseIf()(f.count[cp] == 1):
            # (Line 72) {
            # (Line 73) if (f.loop[cp] < 4)
            if EUDIf()(f.loop[cp] >= 4, neg=True):
                # (Line 74) {
                # (Line 75) f.SquareShape(cp, 1, "Zerg Devourer", 50 * f.loop[cp] + 50, 0);
                f.SquareShape(cp, 1, "Zerg Devourer", 50 * f.loop[cp] + 50, 0)
                # (Line 76) KillUnitAt(All, "Zerg Devourer", "Anywhere", cp);
                # (Line 78) f.SkillWait(cp, 80);
                DoActions(KillUnitAt(All, "Zerg Devourer", "Anywhere", cp))
                f.SkillWait(cp, 80)
                # (Line 80) f.loop[cp] += 1;
                _ARRW(f.loop, cp).__iadd__(1)
                # (Line 81) }
                # (Line 82) else if (f.loop[cp] < 12)
            if EUDElseIf()(f.loop[cp] >= 12, neg=True):
                # (Line 83) {
                # (Line 84) f.SquareShape(cp, 1, "Zerg Devourer", 200 - 25 * (f.loop[cp] - 4), 25 * (f.loop[cp] - 4));
                f.SquareShape(cp, 1, "Zerg Devourer", 200 - 25 * (f.loop[cp] - 4), 25 * (f.loop[cp] - 4))
                # (Line 85) KillUnitAt(All, "Zerg Devourer", "Anywhere", cp);
                # (Line 87) if (f.loop[cp] % 2 == 1)
                DoActions(KillUnitAt(All, "Zerg Devourer", "Anywhere", cp))
                if EUDIf()(f.loop[cp] % 2 == 1):
                    # (Line 88) {
                    # (Line 89) f.SquareShape(cp, 1, "40 + 1n Ghost", 200 - 25 * (f.loop[cp] - 4), 25 * (f.loop[cp] - 4));
                    f.SquareShape(cp, 1, "40 + 1n Ghost", 200 - 25 * (f.loop[cp] - 4), 25 * (f.loop[cp] - 4))
                    # (Line 90) MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
                    # (Line 91) MoveUnit(All, "40 + 1n Ghost", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
                    DoActions(MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"))
                    # (Line 92) Order("40 + 1n Ghost", cp, "Anywhere", Attack, f.location[cp]);
                    DoActions(MoveUnit(All, "40 + 1n Ghost", cp, "[Skill]Unit_Wait_ALL", f.location[cp]))
                    # (Line 93) }
                    DoActions(Order("40 + 1n Ghost", cp, "Anywhere", Attack, f.location[cp]))
                    # (Line 95) f.SkillWait(cp, 80);
                EUDEndIf()
                f.SkillWait(cp, 80)
                # (Line 97) f.loop[cp] += 1;
                _ARRW(f.loop, cp).__iadd__(1)
                # (Line 99) }
                # (Line 100) else if (f.loop[cp] < 16)
            if EUDElseIf()(f.loop[cp] >= 16, neg=True):
                # (Line 101) {
                # (Line 102) f.SquareShape(cp, 1, "Zerg Devourer", 0, 200 - 50 * (f.loop[cp] - 12));
                f.SquareShape(cp, 1, "Zerg Devourer", 0, 200 - 50 * (f.loop[cp] - 12))
                # (Line 103) KillUnitAt(All, "Zerg Devourer", "Anywhere", cp);
                # (Line 105) f.SkillWait(cp, 80);
                DoActions(KillUnitAt(All, "Zerg Devourer", "Anywhere", cp))
                f.SkillWait(cp, 80)
                # (Line 107) f.loop[cp] += 1;
                _ARRW(f.loop, cp).__iadd__(1)
                # (Line 108) }
                # (Line 109) else if (f.loop[cp] == 16)
            if EUDElseIf()(f.loop[cp] == 16):
                # (Line 110) {
                # (Line 111) f.SkillWait(cp, 1080);
                f.SkillWait(cp, 1080)
                # (Line 113) f.loop[cp] += 1;
                _ARRW(f.loop, cp).__iadd__(1)
                # (Line 114) }
                # (Line 115) else if (f.loop[cp] == 17)
            if EUDElseIf()(f.loop[cp] == 17):
                # (Line 116) {
                # (Line 117) f.SkillWait(cp, 80);
                f.SkillWait(cp, 80)
                # (Line 119) f.count[cp] += 1;
                _ARRW(f.count, cp).__iadd__(1)
                # (Line 120) f.loop[cp] = 0;
                _ARRW(f.loop, cp) << (0)
                # (Line 121) }
                # (Line 122) }
            EUDEndIf()
            # (Line 123) else if (f.count[cp] == 2)
        if EUDElseIf()(f.count[cp] == 2):
            # (Line 124) {
            # (Line 125) if (Bring(cp, AtLeast, 1, "Protoss Scout", "[Skill]UseSkill")
            _t17 = EUDIf()
            # (Line 126) && Bring(cp, AtLeast, 1, "Protoss Arbiter", "[Skill]UseSkill")
            # (Line 127) && f.step[cp] == 210)
            if _t17(EUDSCAnd()(Bring(cp, AtLeast, 1, "Protoss Scout", "[Skill]UseSkill"))(Bring(cp, AtLeast, 1, "Protoss Arbiter", "[Skill]UseSkill"))(f.step[cp] == 210)()):
                # (Line 128) {
                # (Line 129) f.Voice_Routine(cp, 7);
                f.Voice_Routine(cp, 7)
                # (Line 130) f.wait[cp] = 0;
                _ARRW(f.wait, cp) << (0)
                # (Line 131) f.count[cp] = 0;
                _ARRW(f.count, cp) << (0)
                # (Line 132) f.loop[cp] = 0;
                _ARRW(f.loop, cp) << (0)
                # (Line 133) f.step[cp] = 220;
                _ARRW(f.step, cp) << (220)
                # (Line 134) KillUnitAt(1, "Protoss Arbiter", "[Skill]UseSkill", cp);
                # (Line 135) KillUnitAt(1, "Protoss Scout", "[Skill]UseSkill", cp);
                DoActions(KillUnitAt(1, "Protoss Arbiter", "[Skill]UseSkill", cp))
                # (Line 136) }
                DoActions(KillUnitAt(1, "Protoss Scout", "[Skill]UseSkill", cp))
                # (Line 137) else
                # (Line 138) {
            if EUDElse()():
                # (Line 139) KillUnitAt(All, "40 + 1n Ghost", "Anywhere", cp);
                # (Line 140) KillUnitAt(All, "40 + 1n Marine", "Anywhere", cp);
                DoActions(KillUnitAt(All, "40 + 1n Ghost", "Anywhere", cp))
                # (Line 142) SetDeaths(cp, SetTo, 0, " `ShieldRecharge");
                DoActions(KillUnitAt(All, "40 + 1n Marine", "Anywhere", cp))
                # (Line 144) f.SkillEnd(cp);
                DoActions(SetDeaths(cp, SetTo, 0, " `ShieldRecharge"))
                f.SkillEnd(cp)
                # (Line 145) }
                # (Line 149) }
            EUDEndIf()
            # (Line 150) }
        EUDEndIf()
        # (Line 151) if (f.delayB[cp] == 0)
    EUDEndIf()
    if EUDIf()(f.delayB[cp] == 0):
        # (Line 152) {
        # (Line 153) if ((f.count[cp] == 1) && (f.loop[cp] < 16))
        if EUDIf()(EUDSCAnd()((f.count[cp] == 1))((EUDNot(f.loop[cp] >= 16)))()):
            # (Line 154) {
            # (Line 155) if (f.loopB[cp] > 3) f.loopB[cp] = 0;
            if EUDIf()(f.loopB[cp] <= 3, neg=True):
                _ARRW(f.loopB, cp) << (0)
                # (Line 157) f.Table_Sin(cp, (45 * f.loopB[cp] + 22), 50 * f.loopB[cp] + 50);
            EUDEndIf()
            f.Table_Sin(cp, (45 * f.loopB[cp] + 22), 50 * f.loopB[cp] + 50)
            # (Line 158) f.Table_Cos(cp, (45 * f.loopB[cp] + 22), 50 * f.loopB[cp] + 50);
            f.Table_Cos(cp, (45 * f.loopB[cp] + 22), 50 * f.loopB[cp] + 50)
            # (Line 160) f.SquareShape(cp, 1, " Unit. Hoffnung 25000", f.CosAngle[cp], f.SinAngle[cp]);
            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", f.CosAngle[cp], f.SinAngle[cp])
            # (Line 162) KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
            # (Line 164) f.SkillWaitB(cp, 160);
            DoActions(KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp))
            f.SkillWaitB(cp, 160)
            # (Line 166) f.loopB[cp] += 1;
            _ARRW(f.loopB, cp).__iadd__(1)
            # (Line 167) }
            # (Line 168) }
        EUDEndIf()
        # (Line 169) if (f.delayC[cp] == 0)
    EUDEndIf()
    if EUDIf()(f.delayC[cp] == 0):
        # (Line 170) {
        # (Line 171) if ((f.count[cp] < 2) && (f.loop[cp] < 16))
        if EUDIf()(EUDSCAnd()((EUDNot(f.count[cp] >= 2)))((EUDNot(f.loop[cp] >= 16)))()):
            # (Line 172) {
            # (Line 173) if (f.loopC[cp] > 8) f.loopC[cp] = 0;
            if EUDIf()(f.loopC[cp] <= 8, neg=True):
                _ARRW(f.loopC, cp) << (0)
                # (Line 175) f.SquareShape(cp, 1, "40 + 1n Zealot", 240 - 30 * f.loopC[cp], 30 * f.loopC[cp]);
            EUDEndIf()
            f.SquareShape(cp, 1, "40 + 1n Zealot", 240 - 30 * f.loopC[cp], 30 * f.loopC[cp])
            # (Line 176) f.SquareShape(cp, 1, "Protoss Dark Templar", 160 - 20 * f.loopC[cp], 20 * f.loopC[cp]);
            f.SquareShape(cp, 1, "Protoss Dark Templar", 160 - 20 * f.loopC[cp], 20 * f.loopC[cp])
            # (Line 178) KillUnitAt(All, "40 + 1n Zealot", "Anywhere", cp);
            # (Line 179) KillUnitAt(All, "Protoss Dark Templar", "Anywhere", cp);
            DoActions(KillUnitAt(All, "40 + 1n Zealot", "Anywhere", cp))
            # (Line 181) f.SkillWaitC(cp, 80);
            DoActions(KillUnitAt(All, "Protoss Dark Templar", "Anywhere", cp))
            f.SkillWaitC(cp, 80)
            # (Line 183) f.loopC[cp] += 1;
            _ARRW(f.loopC, cp).__iadd__(1)
            # (Line 184) }
            # (Line 185) }
        EUDEndIf()
        # (Line 187) }
    EUDEndIf()