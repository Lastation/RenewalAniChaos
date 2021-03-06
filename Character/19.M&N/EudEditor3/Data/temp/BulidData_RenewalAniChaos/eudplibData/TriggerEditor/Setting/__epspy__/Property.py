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
# (Line 3) const s = StringBuffer();
s = _CGFW(lambda: [StringBuffer()], 1)[0]
# (Line 5) function Property_S(cp);
# (Line 6) function Property_C(cp);
# (Line 7) function Property_A();
# (Line 9) function PropertyText()
# (Line 10) {
@EUDFunc
def PropertyText():
    # (Line 11) if (Deaths((13), (10), 10000, (223)))
    if EUDIf()(Deaths((13), (10), 10000, (223))):
        # (Line 12) {
        # (Line 13) s.printAt(0, "\x13\x1F[S] : \x1B원거리에서 업그레이드\x04가 가능해집니다.");
        s.printAt(0, "\x13\x1F[S] : \x1B원거리에서 업그레이드\x04가 가능해집니다.")
        # (Line 14) s.printAt(1, "\x13\x19레벨\x04당 영웅 방어력이 1 증가합니다.");
        s.printAt(1, "\x13\x19레벨\x04당 영웅 방어력이 1 증가합니다.")
        # (Line 15) s.printAt(2, "\x13\x19팀원포함 최대 업그레이드\x04가 공격력이 2, 방어력이 1 증가합니다. [\x17Max 1\x04]");
        s.printAt(2, "\x13\x19팀원포함 최대 업그레이드\x04가 공격력이 2, 방어력이 1 증가합니다. [\x17Max 1\x04]")
        # (Line 16) s.printAt(3, "\n");
        s.printAt(3, "\n")
        # (Line 17) s.printAt(4, "\x13\x1F[C] : \x1B마나디스크\x04를 하나 가지고 시작합니다.");
        s.printAt(4, "\x13\x1F[C] : \x1B마나디스크\x04를 하나 가지고 시작합니다.")
        # (Line 18) s.printAt(5, "\x13\x1915 레벨 \x04이후 1분마다 마나가 \x17200/300/400 \x04회복됩니다.");
        s.printAt(5, "\x13\x1915 레벨 \x04이후 1분마다 마나가 \x17200/300/400 \x04회복됩니다.")
        # (Line 19) s.printAt(6, "\n");
        s.printAt(6, "\n")
        # (Line 20) s.printAt(7, "\x13\x1F[A] : \x041분 마다 궁극기 게이지가 \x1910 \x04회복됩니다.");
        s.printAt(7, "\x13\x1F[A] : \x041분 마다 궁극기 게이지가 \x1910 \x04회복됩니다.")
        # (Line 21) s.printAt(8, "\x13\x1920 레벨 \x04이전 \x1B마나 최대치\x04가 레벨당 \x1710 \x04추가로 증가합니다.");
        s.printAt(8, "\x13\x1920 레벨 \x04이전 \x1B마나 최대치\x04가 레벨당 \x1710 \x04추가로 증가합니다.")
        # (Line 22) }
        # (Line 23) }
    EUDEndIf()
    # (Line 25) function Property(cp)

# (Line 26) {
@EUDFunc
def Property(cp):
    # (Line 27) Property_S(cp);
    Property_S(cp)
    # (Line 28) Property_C(cp);
    Property_C(cp)
    # (Line 29) Property_A();
    Property_A()
    # (Line 30) }
    # (Line 32) function Property_S(cp)

# (Line 33) {
@EUDFunc
def Property_S(cp):
    # (Line 34) if (cp >= 0 && cp <= 2 &&  bread(0x58D088 + 0x21F0 * ((0) / 46) + cp * (46 - 31 * ((0) / 46)) + ((0) % 46)) == 60)
    if EUDIf()(EUDSCAnd()(cp >= 0)(cp <= 2)(f_bread(0x58D088 + 0x21F0 * ((0) // 46) + cp * (46 - 31 * ((0) // 46)) + ((0) % 46)) == 60)()):
        # (Line 35) {
        # (Line 36) if (Deaths((0), (10), 1000, (223)) || Deaths((1), (10), 1000, (223)) || Deaths((2), (10), 1000, (223)))
        if EUDIf()(EUDSCOr()(Deaths((0), (10), 1000, (223)))(Deaths((1), (10), 1000, (223)))(Deaths((2), (10), 1000, (223)))()):
            # (Line 37) {
            # (Line 38) bwrite(0x58D088 + 0x21F0 * ((7) / 46) + (0) * (46 - 31 * ((7) / 46)) + ((7) % 46), 82);
            f_bwrite(0x58D088 + 0x21F0 * ((7) // 46) + (0) * (46 - 31 * ((7) // 46)) + ((7) % 46), 82)
            # (Line 39) bwrite(0x58D088 + 0x21F0 * ((7) / 46) + (1) * (46 - 31 * ((7) / 46)) + ((7) % 46), 82);
            f_bwrite(0x58D088 + 0x21F0 * ((7) // 46) + (1) * (46 - 31 * ((7) // 46)) + ((7) % 46), 82)
            # (Line 40) bwrite(0x58D088 + 0x21F0 * ((7) / 46) + (2) * (46 - 31 * ((7) / 46)) + ((7) % 46), 82);
            f_bwrite(0x58D088 + 0x21F0 * ((7) // 46) + (2) * (46 - 31 * ((7) // 46)) + ((7) % 46), 82)
            # (Line 41) bwrite(0x58D088 + 0x21F0 * ((0) / 46) + (0) * (46 - 31 * ((0) / 46)) + ((0) % 46), 61);
            f_bwrite(0x58D088 + 0x21F0 * ((0) // 46) + (0) * (46 - 31 * ((0) // 46)) + ((0) % 46), 61)
            # (Line 42) bwrite(0x58D088 + 0x21F0 * ((0) / 46) + (1) * (46 - 31 * ((0) / 46)) + ((0) % 46), 61);
            f_bwrite(0x58D088 + 0x21F0 * ((0) // 46) + (1) * (46 - 31 * ((0) // 46)) + ((0) % 46), 61)
            # (Line 43) bwrite(0x58D088 + 0x21F0 * ((0) / 46) + (2) * (46 - 31 * ((0) / 46)) + ((0) % 46), 61);
            f_bwrite(0x58D088 + 0x21F0 * ((0) // 46) + (2) * (46 - 31 * ((0) // 46)) + ((0) % 46), 61)
            # (Line 44) }
            # (Line 45) }
        EUDEndIf()
        # (Line 46) if (cp >= 3 && cp <= 5 &&  bread(0x58D088 + 0x21F0 * ((0) / 46) + cp * (46 - 31 * ((0) / 46)) + ((0) % 46)) == 60)
    EUDEndIf()
    if EUDIf()(EUDSCAnd()(cp >= 3)(cp <= 5)(f_bread(0x58D088 + 0x21F0 * ((0) // 46) + cp * (46 - 31 * ((0) // 46)) + ((0) % 46)) == 60)()):
        # (Line 47) {
        # (Line 48) if (Deaths((3), (10), 1000, (223)) || Deaths((4), (10), 1000, (223)) || Deaths((5), (10), 1000, (223)))
        if EUDIf()(EUDSCOr()(Deaths((3), (10), 1000, (223)))(Deaths((4), (10), 1000, (223)))(Deaths((5), (10), 1000, (223)))()):
            # (Line 49) {
            # (Line 50) bwrite(0x58D088 + 0x21F0 * ((7) / 46) + (3) * (46 - 31 * ((7) / 46)) + ((7) % 46), 82);
            f_bwrite(0x58D088 + 0x21F0 * ((7) // 46) + (3) * (46 - 31 * ((7) // 46)) + ((7) % 46), 82)
            # (Line 51) bwrite(0x58D088 + 0x21F0 * ((7) / 46) + (4) * (46 - 31 * ((7) / 46)) + ((7) % 46), 82);
            f_bwrite(0x58D088 + 0x21F0 * ((7) // 46) + (4) * (46 - 31 * ((7) // 46)) + ((7) % 46), 82)
            # (Line 52) bwrite(0x58D088 + 0x21F0 * ((7) / 46) + (5) * (46 - 31 * ((7) / 46)) + ((7) % 46), 82);
            f_bwrite(0x58D088 + 0x21F0 * ((7) // 46) + (5) * (46 - 31 * ((7) // 46)) + ((7) % 46), 82)
            # (Line 53) bwrite(0x58D088 + 0x21F0 * ((0) / 46) + (3) * (46 - 31 * ((0) / 46)) + ((0) % 46), 61);
            f_bwrite(0x58D088 + 0x21F0 * ((0) // 46) + (3) * (46 - 31 * ((0) // 46)) + ((0) % 46), 61)
            # (Line 54) bwrite(0x58D088 + 0x21F0 * ((0) / 46) + (4) * (46 - 31 * ((0) / 46)) + ((0) % 46), 61);
            f_bwrite(0x58D088 + 0x21F0 * ((0) // 46) + (4) * (46 - 31 * ((0) // 46)) + ((0) % 46), 61)
            # (Line 55) bwrite(0x58D088 + 0x21F0 * ((0) / 46) + (5) * (46 - 31 * ((0) / 46)) + ((0) % 46), 61);
            f_bwrite(0x58D088 + 0x21F0 * ((0) // 46) + (5) * (46 - 31 * ((0) // 46)) + ((0) % 46), 61)
            # (Line 56) }
            # (Line 57) }
        EUDEndIf()
        # (Line 59) if (Deaths(cp, Exactly, 1000, (223)))
    EUDEndIf()
    if EUDIf()(Deaths(cp, Exactly, 1000, (223))):
        # (Line 60) {
        # (Line 61) if (v.Level[cp] != dwread_epd(EPD(0x5822F4 + 4 * cp)))
        if EUDIf()(v.Level[cp] == f_dwread_epd(EPD(0x5822F4 + 4 * cp)), neg=True):
            # (Line 62) {
            # (Line 63) SetMemoryEPD(EPD(0x58D2B0 + 0x207C * ((0) / 46) + cp * (46 - 31 * ((0) / 46)) + ((0) % 46)), (8), bitlshift(1, 8 * (((cp) * (46 - 31 * ((0) / 46)) + ((0) % 46)) % 4)));
            # (Line 64) v.Level[cp] = dwread_epd(EPD(0x5822F4 + 4 * cp));
            DoActions(SetMemoryEPD(EPD(0x58D2B0 + 0x207C * ((0) // 46) + cp * (46 - 31 * ((0) // 46)) + ((0) % 46)), (8), f_bitlshift(1, 8 * (((cp) * (46 - 31 * ((0) // 46)) + ((0) % 46)) % 4))))
            _ARRW(v.Level, cp) << (f_dwread_epd(EPD(0x5822F4 + 4 * cp)))
            # (Line 65) }
            # (Line 66) if (Deaths((13), (10), 0, (204)) && bread(0x58D2B0 + 0x207C * ((0) / 46) + (cp) * (46 - 31 * ((0) / 46)) + ((0) % 46)) >= 62)
        EUDEndIf()
        if EUDIf()(EUDSCAnd()(Deaths((13), (10), 0, (204)))(f_bread(0x58D2B0 + 0x207C * ((0) // 46) + (cp) * (46 - 31 * ((0) // 46)) + ((0) % 46)) >= 62)()):
            # (Line 67) {
            # (Line 68) bwrite(0x58D2B0 + 0x207C * ((0) / 46) + (cp) * (46 - 31 * ((0) / 46)) + ((0) % 46), 61);
            f_bwrite(0x58D2B0 + 0x207C * ((0) // 46) + (cp) * (46 - 31 * ((0) // 46)) + ((0) % 46), 61)
            # (Line 69) }
            # (Line 70) }
        EUDEndIf()
        # (Line 71) else
        # (Line 72) {
    if EUDElse()():
        # (Line 73) v.Level[cp] = dwread_epd(EPD(0x5822F4 + 4 * cp));
        _ARRW(v.Level, cp) << (f_dwread_epd(EPD(0x5822F4 + 4 * cp)))
        # (Line 74) }
        # (Line 75) }
    EUDEndIf()
    # (Line 77) function Property_C(cp)

# (Line 78) {
@EUDFunc
def Property_C(cp):
    # (Line 79) if (Deaths((13), (10), 2720, (223)) && cp >= 0 && cp <= 2)
    if EUDIf()(EUDSCAnd()(Deaths((13), (10), 2720, (223)))(cp >= 0)(cp <= 2)()):
        # (Line 80) {
        # (Line 81) v.Mana_Property[cp] = 100;
        _ARRW(v.Mana_Property, cp) << (100)
        # (Line 83) if (Deaths((0), (0), 2000, (223)) && Deaths((0), (1), 3999, (223))) { v.Mana_Property[cp] += 100; }
        if EUDIf()(EUDSCAnd()(Deaths((0), (0), 2000, (223)))(Deaths((0), (1), 3999, (223)))()):
            _ARRW(v.Mana_Property, cp).__iadd__(100)
            # (Line 84) if (Deaths((1), (0), 2000, (223)) && Deaths((1), (1), 3999, (223))) { v.Mana_Property[cp] += 100; }
        EUDEndIf()
        if EUDIf()(EUDSCAnd()(Deaths((1), (0), 2000, (223)))(Deaths((1), (1), 3999, (223)))()):
            _ARRW(v.Mana_Property, cp).__iadd__(100)
            # (Line 85) if (Deaths((2), (0), 2000, (223)) && Deaths((2), (1), 3999, (223))) { v.Mana_Property[cp] += 100; }
        EUDEndIf()
        if EUDIf()(EUDSCAnd()(Deaths((2), (0), 2000, (223)))(Deaths((2), (1), 3999, (223)))()):
            _ARRW(v.Mana_Property, cp).__iadd__(100)
            # (Line 87) SetResources((13), (8), v.Mana_Property[cp], (1));
        EUDEndIf()
        # (Line 88) SetDeaths((13), (7), 2000, (223));
        DoActions(SetResources((13), (8), v.Mana_Property[cp], (1)))
        # (Line 89) s.print("\n\n\x13\x19C 특성 \x04효과 +", v.Mana_Property[cp], " \x07Gas\n\n");
        DoActions(SetDeaths((13), (7), 2000, (223)))
        s.print("\n\n\x13\x19C 특성 \x04효과 +", v.Mana_Property[cp], " \x07Gas\n\n")
        # (Line 90) }
        # (Line 92) if (Deaths((13), (10), 2720, (223)) && cp >= 3 && cp <= 5)
    EUDEndIf()
    if EUDIf()(EUDSCAnd()(Deaths((13), (10), 2720, (223)))(cp >= 3)(cp <= 5)()):
        # (Line 93) {
        # (Line 94) v.Mana_Property[cp] = 100;
        _ARRW(v.Mana_Property, cp) << (100)
        # (Line 96) if (Deaths((3), (0), 2000, (223)) && Deaths((3), (1), 3999, (223))) { v.Mana_Property[cp] += 100; }
        if EUDIf()(EUDSCAnd()(Deaths((3), (0), 2000, (223)))(Deaths((3), (1), 3999, (223)))()):
            _ARRW(v.Mana_Property, cp).__iadd__(100)
            # (Line 97) if (Deaths((4), (0), 2000, (223)) && Deaths((4), (1), 3999, (223))) { v.Mana_Property[cp] += 100; }
        EUDEndIf()
        if EUDIf()(EUDSCAnd()(Deaths((4), (0), 2000, (223)))(Deaths((4), (1), 3999, (223)))()):
            _ARRW(v.Mana_Property, cp).__iadd__(100)
            # (Line 98) if (Deaths((5), (0), 2000, (223)) && Deaths((5), (1), 3999, (223))) { v.Mana_Property[cp] += 100; }
        EUDEndIf()
        if EUDIf()(EUDSCAnd()(Deaths((5), (0), 2000, (223)))(Deaths((5), (1), 3999, (223)))()):
            _ARRW(v.Mana_Property, cp).__iadd__(100)
            # (Line 100) SetResources((13), (8), v.Mana_Property[cp], (1));
        EUDEndIf()
        # (Line 101) SetDeaths((13), (7), 2000, (223));
        DoActions(SetResources((13), (8), v.Mana_Property[cp], (1)))
        # (Line 102) s.print("\n\n\x13\x19C 특성 \x04효과 +", v.Mana_Property[cp], " \x07Gas\n\n");
        DoActions(SetDeaths((13), (7), 2000, (223)))
        s.print("\n\n\x13\x19C 특성 \x04효과 +", v.Mana_Property[cp], " \x07Gas\n\n")
        # (Line 103) }
        # (Line 104) }
    EUDEndIf()
    # (Line 106) function Property_A()

# (Line 107) {
@EUDFunc
def Property_A():
    # (Line 108) if (Deaths((13), (10), 3720, (223)))
    if EUDIf()(Deaths((13), (10), 3720, (223))):
        # (Line 109) {
        # (Line 110) SetDeaths((13), (8), 10, (205));
        # (Line 111) SetDeaths((13), (7), 3000, (223));
        DoActions(SetDeaths((13), (8), 10, (205)))
        # (Line 112) s.print("\x13\x19A 특성 \x04효과 +10 \x1FShield");
        DoActions(SetDeaths((13), (7), 3000, (223)))
        s.print("\x13\x19A 특성 \x04효과 +10 \x1FShield")
        # (Line 113) }
        # (Line 114) }
    EUDEndIf()
