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
# (Line 3) import Function as f;
import Function as f
# (Line 4) import Character.Sound as s;
from Character import Sound as s
# (Line 6) import Character.Rusaruka.Main 		as rusarukaMain;
from Character.Rusaruka import Main as rusarukaMain
# (Line 7) import Character.Chtholly.Main 		as chthollyMain;
from Character.Chtholly import Main as chthollyMain
# (Line 8) import Character.Kiana.Main 			as kianaMain;
from Character.Kiana import Main as kianaMain
# (Line 9) import Character.Yuuna.Main 		as yuunaMain;
from Character.Yuuna import Main as yuunaMain
# (Line 10) import Character.Mayuri.Main 		as mayuriMain;
from Character.Mayuri import Main as mayuriMain
# (Line 11) import Character.Nanami.Main 		as nanamiMain;
from Character.Nanami import Main as nanamiMain
# (Line 12) import Character.Milim.Main 		as milimMain;
from Character.Milim import Main as milimMain
# (Line 13) import Character.Yume.Main 		as yumeMain;
from Character.Yume import Main as yumeMain
# (Line 14) import Character.Magane.Main 		as maganeMain;
from Character.Magane import Main as maganeMain
# (Line 15) import Character.Oda.Main 			as odaMain;
from Character.Oda import Main as odaMain
# (Line 16) import Character.Ekidona.Main 		as ekidonaMain;
from Character.Ekidona import Main as ekidonaMain
# (Line 17) import Character.Niwa.Main 			as niwaMain;
from Character.Niwa import Main as niwaMain
# (Line 18) import Character.Park.Main 			as parkMain;
from Character.Park import Main as parkMain
# (Line 20) const bgmWait		= PVariable();
bgmWait = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 22) function SetVoice(cp);
# (Line 23) function MargeSound(cp);
# (Line 24) function SkillWait(cp);
# (Line 25) function SkillDelay(cp);
# (Line 26) function BGMRoutine(cp);
# (Line 28) function main(cp)
# (Line 29) {
@EUDFunc
def f_main(cp):
    # (Line 30) switch(v.Hero_Num[cp])
    EUDSwitch(v.Hero_Num[cp])
    # (Line 31) {
    # (Line 32) case 1:
    _t1 = EUDSwitchCase()
    # (Line 33) rusarukaMain.main(cp);
    if _t1(1):
        rusarukaMain.f_main(cp)
        # (Line 34) break;
        EUDBreak()
        # (Line 35) case 2:
    _t2 = EUDSwitchCase()
    # (Line 36) chthollyMain.main(cp);
    if _t2(2):
        chthollyMain.f_main(cp)
        # (Line 37) break;
        EUDBreak()
        # (Line 38) case 17:
    _t3 = EUDSwitchCase()
    # (Line 39) kianaMain.main(cp);
    if _t3(17):
        kianaMain.f_main(cp)
        # (Line 40) break;
        EUDBreak()
        # (Line 41) case 22:
    _t4 = EUDSwitchCase()
    # (Line 42) yuunaMain.main(cp);
    if _t4(22):
        yuunaMain.f_main(cp)
        # (Line 43) break;
        EUDBreak()
        # (Line 44) case 23:
    _t5 = EUDSwitchCase()
    # (Line 45) mayuriMain.main(cp);
    if _t5(23):
        mayuriMain.f_main(cp)
        # (Line 46) break;
        EUDBreak()
        # (Line 47) case 24:
    _t6 = EUDSwitchCase()
    # (Line 48) nanamiMain.main(cp);
    if _t6(24):
        nanamiMain.f_main(cp)
        # (Line 49) break;
        EUDBreak()
        # (Line 50) case 25:
    _t7 = EUDSwitchCase()
    # (Line 51) milimMain.main(cp);
    if _t7(25):
        milimMain.f_main(cp)
        # (Line 52) break;
        EUDBreak()
        # (Line 53) case 26:
    _t8 = EUDSwitchCase()
    # (Line 54) yumeMain.main(cp);
    if _t8(26):
        yumeMain.f_main(cp)
        # (Line 55) break;
        EUDBreak()
        # (Line 56) case 27:
    _t9 = EUDSwitchCase()
    # (Line 57) maganeMain.main(cp);
    if _t9(27):
        maganeMain.f_main(cp)
        # (Line 58) break;
        EUDBreak()
        # (Line 59) case 28:
    _t10 = EUDSwitchCase()
    # (Line 60) odaMain.main(cp);
    if _t10(28):
        odaMain.f_main(cp)
        # (Line 61) break;
        EUDBreak()
        # (Line 62) case 29:
    _t11 = EUDSwitchCase()
    # (Line 63) ekidonaMain.main(cp);
    if _t11(29):
        ekidonaMain.f_main(cp)
        # (Line 64) break;
        EUDBreak()
        # (Line 65) case 30:
    _t12 = EUDSwitchCase()
    # (Line 66) niwaMain.main(cp);
    if _t12(30):
        niwaMain.f_main(cp)
        # (Line 67) break;
        EUDBreak()
        # (Line 68) case 31:
    _t13 = EUDSwitchCase()
    # (Line 69) parkMain.main(cp);
    if _t13(31):
        parkMain.f_main(cp)
        # (Line 70) break;
        EUDBreak()
        # (Line 71) }
    # (Line 73) SkillWait(cp);
    EUDEndSwitch()
    SkillWait(cp)
    # (Line 74) SkillDelay(cp);
    SkillDelay(cp)
    # (Line 76) SetVoice(cp);
    SetVoice(cp)
    # (Line 77) s.main(cp);
    s.f_main(cp)
    # (Line 78) BGMRoutine(cp);
    BGMRoutine(cp)
    # (Line 79) }
    # (Line 81) function SetVoice(cp)

# (Line 82) {
@EUDFunc
def SetVoice(cp):
    # (Line 83) if (cp < 6)
    if EUDIf()(cp >= 6, neg=True):
        # (Line 84) {
        # (Line 85) if (Deaths(cp, AtLeast, 1, (186)))
        if EUDIf()(Deaths(cp, AtLeast, 1, (186))):
            # (Line 86) {
            # (Line 87) v.Sound_Text1[cp] = dwread_epd(EPD(0x58A364 + 48 * 186 + 4 * cp));
            _ARRW(v.Sound_Text1, cp) << (f_dwread_epd(EPD(0x58A364 + 48 * 186 + 4 * cp)))
            # (Line 88) v.Sound_Text1[8 + cp] = v.Sound_Text1[cp];
            _ARRW(v.Sound_Text1, 8 + cp) << (v.Sound_Text1[cp])
            # (Line 89) SetDeaths(cp, SetTo, 0, (186));
            # (Line 90) }
            DoActions(SetDeaths(cp, SetTo, 0, (186)))
            # (Line 91) if (Deaths(cp, AtLeast, 1, (174)))
        EUDEndIf()
        if EUDIf()(Deaths(cp, AtLeast, 1, (174))):
            # (Line 92) {
            # (Line 93) v.Sound_Text2[cp] = dwread_epd(EPD(0x58A364 + 48 * 174 + 4 * cp));
            _ARRW(v.Sound_Text2, cp) << (f_dwread_epd(EPD(0x58A364 + 48 * 174 + 4 * cp)))
            # (Line 94) v.Sound_Text2[8 + cp] = v.Sound_Text2[cp];
            _ARRW(v.Sound_Text2, 8 + cp) << (v.Sound_Text2[cp])
            # (Line 95) SetDeaths(cp, SetTo, 0, (174));
            # (Line 96) }
            DoActions(SetDeaths(cp, SetTo, 0, (174)))
            # (Line 97) if (Deaths(cp, AtLeast, 1, (117)))
        EUDEndIf()
        if EUDIf()(Deaths(cp, AtLeast, 1, (117))):
            # (Line 98) {
            # (Line 99) v.Sound_Text3[cp] = dwread_epd(EPD(0x58A364 + 48 * 117 + 4 * cp));
            _ARRW(v.Sound_Text3, cp) << (f_dwread_epd(EPD(0x58A364 + 48 * 117 + 4 * cp)))
            # (Line 100) v.Sound_Text3[8 + cp] = v.Sound_Text3[cp];
            _ARRW(v.Sound_Text3, 8 + cp) << (v.Sound_Text3[cp])
            # (Line 101) SetDeaths(cp, SetTo, 0, (117));
            # (Line 102) }
            DoActions(SetDeaths(cp, SetTo, 0, (117)))
            # (Line 103) if (Deaths(cp, AtLeast, 1, (157)))
        EUDEndIf()
        if EUDIf()(Deaths(cp, AtLeast, 1, (157))):
            # (Line 104) {
            # (Line 105) v.Sound_Text4[cp] = dwread_epd(EPD(0x58A364 + 48 * 157 + 4 * cp));
            _ARRW(v.Sound_Text4, cp) << (f_dwread_epd(EPD(0x58A364 + 48 * 157 + 4 * cp)))
            # (Line 106) v.Sound_Text4[8 + cp] = v.Sound_Text4[cp];
            _ARRW(v.Sound_Text4, 8 + cp) << (v.Sound_Text4[cp])
            # (Line 107) SetDeaths(cp, SetTo, 0, (157));
            # (Line 108) }
            DoActions(SetDeaths(cp, SetTo, 0, (157)))
            # (Line 109) if (Deaths(cp, AtLeast, 1, (222)))
        EUDEndIf()
        if EUDIf()(Deaths(cp, AtLeast, 1, (222))):
            # (Line 110) {
            # (Line 111) v.Sound_Text_Uilti[cp] = dwread_epd(EPD(0x58A364 + 48 * 222 + 4 * cp));
            _ARRW(v.Sound_Text_Uilti, cp) << (f_dwread_epd(EPD(0x58A364 + 48 * 222 + 4 * cp)))
            # (Line 112) v.Sound_Text_Uilti[8 + cp] = v.Sound_Text_Uilti[cp];
            _ARRW(v.Sound_Text_Uilti, 8 + cp) << (v.Sound_Text_Uilti[cp])
            # (Line 113) SetDeaths(cp, SetTo, 0, (222));
            # (Line 114) }
            DoActions(SetDeaths(cp, SetTo, 0, (222)))
            # (Line 115) if (Deaths(cp, AtLeast, 1, (188)))
        EUDEndIf()
        if EUDIf()(Deaths(cp, AtLeast, 1, (188))):
            # (Line 116) {
            # (Line 117) v.Sound_Text_Uniq[cp] = dwread_epd(EPD(0x58A364 + 48 * 188 + 4 * cp));
            _ARRW(v.Sound_Text_Uniq, cp) << (f_dwread_epd(EPD(0x58A364 + 48 * 188 + 4 * cp)))
            # (Line 118) v.Sound_Text_Uniq[8 + cp] = v.Sound_Text_Uniq[cp];
            _ARRW(v.Sound_Text_Uniq, 8 + cp) << (v.Sound_Text_Uniq[cp])
            # (Line 119) SetDeaths(cp, SetTo, 0, (188));
            # (Line 120) }
            DoActions(SetDeaths(cp, SetTo, 0, (188)))
            # (Line 121) }
        EUDEndIf()
        # (Line 122) }
    EUDEndIf()
    # (Line 124) function BGMRoutine(cp)

# (Line 125) {
@EUDFunc
def BGMRoutine(cp):
    # (Line 126) if (Bring(cp, AtLeast, 1, "Terran SCV", "[BGM]ON"))
    if EUDIf()(Bring(cp, AtLeast, 1, "Terran SCV", "[BGM]ON")):
        # (Line 127) {
        # (Line 128) if (bgmWait[cp] == 0)
        if EUDIf()(bgmWait[cp] == 0):
            # (Line 129) {
            # (Line 130) f.stb.print("　　\x04\x1F# N\x04ow \x04Playing... ' \x08化\x02身の\x04獣 [ \x19십\x04이대전 ed ]\x04");
            f.stb.print("　　\x04\x1F# N\x04ow \x04Playing... ' \x08化\x02身の\x04獣 [ \x19십\x04이대전 ed ]\x04")
            # (Line 131) PlayWAV("BGM.ogg");
            # (Line 132) bgmWait[cp] = 2424;
            DoActions(PlayWAV("BGM.ogg"))
            _ARRW(bgmWait, cp) << (2424)
            # (Line 133) }
            # (Line 134) }
        EUDEndIf()
        # (Line 136) if (bgmWait[cp] > 0)
    EUDEndIf()
    if EUDIf()(bgmWait[cp] <= 0, neg=True):
        # (Line 137) {
        # (Line 138) bgmWait[cp] -= 1;
        _ARRW(bgmWait, cp).__isub__(1)
        # (Line 139) }
        # (Line 140) }
    EUDEndIf()
    # (Line 142) function SkillWait(cp)

# (Line 143) {
@EUDFunc
def SkillWait(cp):
    # (Line 144) if (f.delay[cp] == 0)
    if EUDIf()(f.delay[cp] == 0):
        # (Line 145) {
        # (Line 146) if (f.count[cp] == 999)
        if EUDIf()(f.count[cp] == 999):
            # (Line 147) {
            # (Line 148) f.SkillWait(cp, 500);
            f.SkillWait(cp, 500)
            # (Line 149) f.count[cp] = 1000;
            _ARRW(f.count, cp) << (1000)
            # (Line 150) }
            # (Line 151) else if (f.count[cp] == 1000)
        if EUDElseIf()(f.count[cp] == 1000):
            # (Line 152) {
            # (Line 153) f.count[cp] = 0;
            _ARRW(f.count, cp) << (0)
            # (Line 154) f.loop[cp] = 0;
            _ARRW(f.loop, cp) << (0)
            # (Line 155) f.wait[cp] = 12;
            _ARRW(f.wait, cp) << (12)
            # (Line 156) }
            # (Line 157) }
        EUDEndIf()
        # (Line 159) if (f.wait[cp] >= 2)
    EUDEndIf()
    if EUDIf()(f.wait[cp] >= 2):
        # (Line 160) {
        # (Line 161) f.wait[cp] -= 1;
        _ARRW(f.wait, cp).__isub__(1)
        # (Line 162) }
        # (Line 163) else if (f.wait[cp] == 1)
    if EUDElseIf()(f.wait[cp] == 1):
        # (Line 164) {
        # (Line 165) f.wait[cp] = 0;
        _ARRW(f.wait, cp) << (0)
        # (Line 166) f.step[cp] = 0;
        _ARRW(f.step, cp) << (0)
        # (Line 167) }
        # (Line 168) }
    EUDEndIf()
    # (Line 170) function SkillDelay(cp)

# (Line 171) {
@EUDFunc
def SkillDelay(cp):
    # (Line 172) if (f.delay[cp] >= 1) { f.delay[cp] -= 1; }
    if EUDIf()(f.delay[cp] >= 1):
        _ARRW(f.delay, cp).__isub__(1)
        # (Line 173) if (f.delayB[cp] >= 1) { f.delayB[cp] -= 1; }
    EUDEndIf()
    if EUDIf()(f.delayB[cp] >= 1):
        _ARRW(f.delayB, cp).__isub__(1)
        # (Line 174) if (f.delayC[cp] >= 1) { f.delayC[cp] -= 1; }
    EUDEndIf()
    if EUDIf()(f.delayC[cp] >= 1):
        _ARRW(f.delayC, cp).__isub__(1)
        # (Line 175) }
    EUDEndIf()