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
# (Line 2) import Variable as v;
import Variable as v
# (Line 3) import Status as s;
import Status as s
# (Line 4) import Function as f;
import Function as f
# (Line 5) function SetBuildingHP(cp)
# (Line 6) {
@EUDFunc
def SetBuildingHP(cp):
    # (Line 7) ModifyUnitHitPoints(1, (155), (13), (64), 100 - (v.Unique_Cool[cp] / 10));
    # (Line 8) ModifyUnitShields(1, (167), (13), (64), dwread_epd(EPD(0x58A364 + 48 * 205 + 4 * cp)) / 10);
    DoActions(ModifyUnitHitPoints(1, (155), (13), (64), 100 - (v.Unique_Cool[cp] // 10)))
    # (Line 9) }
    DoActions(ModifyUnitShields(1, (167), (13), (64), f_dwread_epd(EPD(0x58A364 + 48 * 205 + 4 * cp)) // 10))
    # (Line 11) function SetVariable(cp)

# (Line 12) {
@EUDFunc
def SetVariable(cp):
    # (Line 13) v.Potion[cp] = dwread_epd(EPD(0x58A364 + 48 * 219 + 4 * cp));
    _ARRW(v.Potion, cp) << (f_dwread_epd(EPD(0x58A364 + 48 * 219 + 4 * cp)))
    # (Line 14) v.EXP_Need[cp] = dwread_epd(EPD(0x58A364 + 48 * 225 + 4 * cp));
    _ARRW(v.EXP_Need, cp) << (f_dwread_epd(EPD(0x58A364 + 48 * 225 + 4 * cp)))
    # (Line 15) v.EXP_Now[cp] = dwread_epd(EPD(0x58A364 + 48 * 185 + 4 * cp));
    _ARRW(v.EXP_Now, cp) << (f_dwread_epd(EPD(0x58A364 + 48 * 185 + 4 * cp)))
    # (Line 17) v.CS_Player[cp] = dwread_epd(EPD(0x58A364 + 48 * 164 + 4 * cp));
    _ARRW(v.CS_Player, cp) << (f_dwread_epd(EPD(0x58A364 + 48 * 164 + 4 * cp)))
    # (Line 18) v.Exp_Player[cp] = dwread_epd(EPD(0x58A364 + 48 * 166 + 4 * cp));
    _ARRW(v.Exp_Player, cp) << (f_dwread_epd(EPD(0x58A364 + 48 * 166 + 4 * cp)))
    # (Line 20) v.DeathCount[cp] = dwread_epd(EPD(0x58A364 + 48 * 210 + 4 * cp))/12;
    _ARRW(v.DeathCount, cp) << (f_dwread_epd(EPD(0x58A364 + 48 * 210 + 4 * cp)) // 12)
    # (Line 21) v.Unique_Cool[cp] = dwread_epd(EPD(0x58A364 + 48 * 203 + 4 * cp))/12;
    _ARRW(v.Unique_Cool, cp) << (f_dwread_epd(EPD(0x58A364 + 48 * 203 + 4 * cp)) // 12)
    # (Line 23) if (bread(0x58D2B0 + 0x207C * ((7) / 46) + (cp) * (46 - 31 * ((7) / 46)) + ((7) % 46)) != bread(0x58D2B0 + 35 + 46 * cp))
    if EUDIf()(f_bread(0x58D2B0 + 0x207C * ((7) // 46) + (cp) * (46 - 31 * ((7) // 46)) + ((7) % 46)) == f_bread(0x58D2B0 + 35 + 46 * cp), neg=True):
        # (Line 24) { bwrite(0x58D2B0 + 0x207C * ((35) / 46) + (cp) * (46 - 31 * ((35) / 46)) + ((35) % 46), bread(0x58D2B0 + 7 + 46 * cp)); }
        f_bwrite(0x58D2B0 + 0x207C * ((35) // 46) + (cp) * (46 - 31 * ((35) // 46)) + ((35) % 46), f_bread(0x58D2B0 + 7 + 46 * cp))
        # (Line 25) v.Dfs[cp] = bread(0x58D2B0 + 0 + 46 * cp);
    EUDEndIf()
    _ARRW(v.Dfs, cp) << (f_bread(0x58D2B0 + 0 + 46 * cp))
    # (Line 26) v.Atk[cp] = bread(0x58D2B0 + 7 + 46 * cp);
    _ARRW(v.Atk, cp) << (f_bread(0x58D2B0 + 7 + 46 * cp))
    # (Line 28) switch (v.Hero_Num[cp])	// 방어력 관련
    EUDSwitch(v.Hero_Num[cp])
    # (Line 29) {
    # (Line 30) case 10:	//얼터
    _t2 = EUDSwitchCase()
    # (Line 31) if (Deaths((13), (0), 1, (204)))
    if _t2(10):
        if EUDIf()(Deaths((13), (0), 1, (204))):
            # (Line 32) {
            # (Line 33) v.Dfs[cp] += 10;
            _ARRW(v.Dfs, cp).__iadd__(10)
            # (Line 34) SetDeaths((13), (9), 1, (204));
            # (Line 35) }
            DoActions(SetDeaths((13), (9), 1, (204)))
            # (Line 36) break;
        EUDEndIf()
        EUDBreak()
        # (Line 37) case 18:	//텐케이
    _t4 = EUDSwitchCase()
    # (Line 38) if (Deaths(CurrentPlayer, Exactly, 320, " `SkillStep")) v.Dfs[cp] = 200;
    if _t4(18):
        if EUDIf()(Deaths(CurrentPlayer, Exactly, 320, " `SkillStep")):
            _ARRW(v.Dfs, cp) << (200)
            # (Line 39) break;
        EUDEndIf()
        EUDBreak()
        # (Line 40) case 22:	//유우나
    _t6 = EUDSwitchCase()
    # (Line 41) v.Dfs[cp] -= 3 * dwread_epd(204 * 12 + cp);
    if _t6(22):
        _ARRW(v.Dfs, cp).__isub__(3 * f_dwread_epd(204 * 12 + cp))
        # (Line 42) break;
        EUDBreak()
        # (Line 43) }
    # (Line 46) switch (v.Hero_Num[cp])	// 공격력 관련
    EUDEndSwitch()
    EUDSwitch(v.Hero_Num[cp])
    # (Line 47) {
    # (Line 48) case 14:
    _t7 = EUDSwitchCase()
    # (Line 49) v.Atk[cp] += 2 * dwread_epd(204 * 12 + cp);
    if _t7(14):
        _ARRW(v.Atk, cp).__iadd__(2 * f_dwread_epd(204 * 12 + cp))
        # (Line 50) break;
        EUDBreak()
        # (Line 51) case 22:
    _t8 = EUDSwitchCase()
    # (Line 52) v.Atk[cp] += 3 * dwread_epd(204 * 12 + cp);
    if _t8(22):
        _ARRW(v.Atk, cp).__iadd__(3 * f_dwread_epd(204 * 12 + cp))
        # (Line 53) break;
        EUDBreak()
        # (Line 54) case 30:
    _t9 = EUDSwitchCase()
    # (Line 55) if (Deaths(cp, AtLeast, 1, " `UniqueSkill"))
    if _t9(30):
        if EUDIf()(Deaths(cp, AtLeast, 1, " `UniqueSkill")):
            # (Line 56) v.Atk[cp] += 10;
            _ARRW(v.Atk, cp).__iadd__(10)
            # (Line 57) break;
        EUDEndIf()
        EUDBreak()
        # (Line 58) }
    # (Line 59) if (cp < 3 && Switch("Passive - Nanami1", Set) && Bring(cp, AtLeast, 1, "Any unit", "24.Nanami_Bozo")) { v.Atk[cp] += 5; v.Dfs[cp] += 5; }
    EUDEndSwitch()
    if EUDIf()(EUDSCAnd()(cp >= 3, neg=True)(Switch("Passive - Nanami1", Set))(Bring(cp, AtLeast, 1, "Any unit", "24.Nanami_Bozo"))()):
        _ARRW(v.Atk, cp).__iadd__(5)
        _ARRW(v.Dfs, cp).__iadd__(5)
        # (Line 60) else if (cp >= 3 && Switch("Passive - Nanami2", Set) && Bring(cp, AtLeast, 1, "Any unit", "24.Nanami_Bozo")) { v.Atk[cp] += 5; v.Dfs[cp] += 5; }
    if EUDElseIf()(EUDSCAnd()(cp >= 3)(Switch("Passive - Nanami2", Set))(Bring(cp, AtLeast, 1, "Any unit", "24.Nanami_Bozo"))()):
        _ARRW(v.Atk, cp).__iadd__(5)
        _ARRW(v.Dfs, cp).__iadd__(5)
        # (Line 62) if (cp < 3 && Switch("Unique - Nanami1", Set)) { v.Atk[cp] += 5; v.Dfs[cp] += 5; }
    EUDEndIf()
    if EUDIf()(EUDSCAnd()(cp >= 3, neg=True)(Switch("Unique - Nanami1", Set))()):
        _ARRW(v.Atk, cp).__iadd__(5)
        _ARRW(v.Dfs, cp).__iadd__(5)
        # (Line 63) else if (cp >= 3 && Switch("Unique - Nanami2", Set)) { v.Atk[cp] += 5; v.Dfs[cp] += 5; }
    if EUDElseIf()(EUDSCAnd()(cp >= 3)(Switch("Unique - Nanami2", Set))()):
        _ARRW(v.Atk, cp).__iadd__(5)
        _ARRW(v.Dfs, cp).__iadd__(5)
        # (Line 65) if (s.ekidonaDebuff[cp] >= 1) v.Atk[cp] -= 5 * s.ekidonaDebuff[cp];
    EUDEndIf()
    if EUDIf()(s.ekidonaDebuff[cp] >= 1):
        _ARRW(v.Atk, cp).__isub__(5 * s.ekidonaDebuff[cp])
        # (Line 67) bwrite(0x58D2B0 + 0x207C * ((2) / 46) + (cp) * (46 - 31 * ((2) / 46)) + ((2) % 46), v.Dfs[cp]); 	//방어력 최종 적용
    EUDEndIf()
    f_bwrite(0x58D2B0 + 0x207C * ((2) // 46) + (cp) * (46 - 31 * ((2) // 46)) + ((2) % 46), v.Dfs[cp])
    # (Line 68) bwrite(0x58D2B0 + 0x207C * ((9) / 46) + (cp) * (46 - 31 * ((9) / 46)) + ((9) % 46), v.Atk[cp]);	//공격력 최종 적용
    f_bwrite(0x58D2B0 + 0x207C * ((9) // 46) + (cp) * (46 - 31 * ((9) // 46)) + ((9) % 46), v.Atk[cp])
    # (Line 70) ModifyUnitShields(All, f.heroID[cp], cp, "Anywhere", v.Shield[cp]);			//쉴드 고정
    # (Line 71) }
    DoActions(ModifyUnitShields(All, f.heroID[cp], cp, "Anywhere", v.Shield[cp]))