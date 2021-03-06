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
# (Line 3) import system.getUnitID as unitid;
from system import getUnitID as unitid
# (Line 5) const  BuildingID = PVariable();
BuildingID = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 7) function BuildingText(playerID)
# (Line 8) {
@EUDFunc
def BuildingText(playerID):
    # (Line 9) BuildingID[playerID] = unitid.UnitID[playerID];
    _ARRW(BuildingID, playerID) << (unitid.UnitID[playerID])
    # (Line 11) switch(BuildingID[playerID])
    EUDSwitch(BuildingID[playerID])
    # (Line 12) {
    # (Line 13) case 81:
    _t1 = EUDSwitchCase()
    # (Line 14) unitid.UnitHP[playerID] = dwread_epd(unitid.NowIndex[playerID] + 0x008 / 4) / 256;
    if _t1(81):
        _ARRW(unitid.UnitHP, playerID) << (f_dwread_epd(unitid.NowIndex[playerID] + 0x008 // 4) // 256)
        # (Line 15) v.stb.printAt(0, "\x13\x19[ \x1FP\x04olarlicht \x19]\n\x13\x04\x1955초 \x04마다 Hoffnung [용병] 스텍이 5 추가로 증가합니다.\n\n\x13\x04남은 체력 : ", unitid.UnitHP[playerID], " / 20000");
        v.stb.printAt(0, "\x13\x19[ \x1FP\x04olarlicht \x19]\n\x13\x04\x1955초 \x04마다 Hoffnung [용병] 스텍이 5 추가로 증가합니다.\n\n\x13\x04남은 체력 : ", unitid.UnitHP[playerID], " / 20000")
        # (Line 16) BuildingID[playerID] = 0;
        _ARRW(BuildingID, playerID) << (0)
        # (Line 17) break;
        EUDBreak()
        # (Line 18) case 79:
    _t2 = EUDSwitchCase()
    # (Line 19) unitid.UnitHP[playerID] = dwread_epd(unitid.NowIndex[playerID] + 0x008 / 4) / 256;
    if _t2(79):
        _ARRW(unitid.UnitHP, playerID) << (f_dwread_epd(unitid.NowIndex[playerID] + 0x008 // 4) // 256)
        # (Line 20) v.stb.printAt(0, "\x13\x19[ \x1BS\x04chnee \x19]\n\x13\x04제거시 \x1B신전 \x04의 무적이 해제됩니다.\n\n\x13\x04남은 체력 : ", unitid.UnitHP[playerID], " / 70000");
        v.stb.printAt(0, "\x13\x19[ \x1BS\x04chnee \x19]\n\x13\x04제거시 \x1B신전 \x04의 무적이 해제됩니다.\n\n\x13\x04남은 체력 : ", unitid.UnitHP[playerID], " / 70000")
        # (Line 21) BuildingID[playerID] = 0;
        _ARRW(BuildingID, playerID) << (0)
        # (Line 22) break;
        EUDBreak()
        # (Line 23) case 160:
    _t3 = EUDSwitchCase()
    # (Line 24) unitid.UnitHP[playerID] = dwread_epd(unitid.NowIndex[playerID] + 0x008 / 4) / 256;
    if _t3(160):
        _ARRW(unitid.UnitHP, playerID) << (f_dwread_epd(unitid.NowIndex[playerID] + 0x008 // 4) // 256)
        # (Line 25) v.stb.printAt(0, "\x13\x19[ \x1BT\x04raum \x19]\n\x13\x04제거시 해당라인의 \x1BC\x04reep 이 더이상 생성되지 않습니다.\n\n\x13\x04남은 체력 : ", unitid.UnitHP[playerID], " / 30000");
        v.stb.printAt(0, "\x13\x19[ \x1BT\x04raum \x19]\n\x13\x04제거시 해당라인의 \x1BC\x04reep 이 더이상 생성되지 않습니다.\n\n\x13\x04남은 체력 : ", unitid.UnitHP[playerID], " / 30000")
        # (Line 26) BuildingID[playerID] = 0;
        _ARRW(BuildingID, playerID) << (0)
        # (Line 27) break;
        EUDBreak()
        # (Line 28) case 168:
    _t4 = EUDSwitchCase()
    # (Line 29) unitid.UnitHP[playerID] = dwread_epd(unitid.NowIndex[playerID] + 0x008 / 4) / 256;
    if _t4(168):
        _ARRW(unitid.UnitHP, playerID) << (f_dwread_epd(unitid.NowIndex[playerID] + 0x008 // 4) // 256)
        # (Line 30) v.stb.printAt(0, "\x13\x19[ \x1BB\x04runnen \x19]\n\x13\x04모두 제거시 \x1BS\x04chnee [수호자] 의 무적이 해제됩니다.\n\n\x13\x04남은 체력 : ", unitid.UnitHP[playerID], " / 50000");
        v.stb.printAt(0, "\x13\x19[ \x1BB\x04runnen \x19]\n\x13\x04모두 제거시 \x1BS\x04chnee [수호자] 의 무적이 해제됩니다.\n\n\x13\x04남은 체력 : ", unitid.UnitHP[playerID], " / 50000")
        # (Line 31) BuildingID[playerID] = 0;
        _ARRW(BuildingID, playerID) << (0)
        # (Line 32) break;
        EUDBreak()
        # (Line 33) case 175:
    _t5 = EUDSwitchCase()
    # (Line 34) unitid.UnitHP[playerID] = dwread_epd(unitid.NowIndex[playerID] + 0x008 / 4) / 256;
    if _t5(175):
        _ARRW(unitid.UnitHP, playerID) << (f_dwread_epd(unitid.NowIndex[playerID] + 0x008 // 4) // 256)
        # (Line 35) v.stb.printAt(0, "\x13\x19[ \x1BM\x04ond \x19]\n\n\x13\x04남은 체력 : ", unitid.UnitHP[playerID], " / 200000");
        v.stb.printAt(0, "\x13\x19[ \x1BM\x04ond \x19]\n\n\x13\x04남은 체력 : ", unitid.UnitHP[playerID], " / 200000")
        # (Line 36) BuildingID[playerID] = 0;
        _ARRW(BuildingID, playerID) << (0)
        # (Line 37) break;
        EUDBreak()
        # (Line 38) case 189:
    _t6 = EUDSwitchCase()
    # (Line 39) v.stb.printAt(0, "\x13\x19[ \x1BP\x04ortal \x19]\n\n\x13\x04상점에 들어가거나 원하는 라인으로 이동 해주는 건물입니다.");
    if _t6(189):
        v.stb.printAt(0, "\x13\x19[ \x1BP\x04ortal \x19]\n\n\x13\x04상점에 들어가거나 원하는 라인으로 이동 해주는 건물입니다.")
        # (Line 40) BuildingID[playerID] = 0;
        _ARRW(BuildingID, playerID) << (0)
        # (Line 41) break;
        EUDBreak()
        # (Line 42) case 200:
    _t7 = EUDSwitchCase()
    # (Line 43) unitid.UnitHP[playerID] = dwread_epd(unitid.NowIndex[playerID] + 0x008 / 4) / 256;
    if _t7(200):
        _ARRW(unitid.UnitHP, playerID) << (f_dwread_epd(unitid.NowIndex[playerID] + 0x008 // 4) // 256)
        # (Line 44) v.stb.printAt(0, "\x13\x19[ \x1BW\x04ald \x19]\n\x13\x04제거시 \x1B방어건물 \x04의 무적이 해제되며,\n\x13\x1B신전\x04의 방어력이 20 감소됩니다.\n\n\x13\x04남은 체력 : ", unitid.UnitHP[playerID], " / 50000");
        v.stb.printAt(0, "\x13\x19[ \x1BW\x04ald \x19]\n\x13\x04제거시 \x1B방어건물 \x04의 무적이 해제되며,\n\x13\x1B신전\x04의 방어력이 20 감소됩니다.\n\n\x13\x04남은 체력 : ", unitid.UnitHP[playerID], " / 50000")
        # (Line 45) BuildingID[playerID] = 0;
        _ARRW(BuildingID, playerID) << (0)
        # (Line 46) break;
        EUDBreak()
        # (Line 47) }
    # (Line 49) }
    EUDEndSwitch()
    # (Line 51) function ShopText(playerID)

# (Line 52) {
@EUDFunc
def ShopText(playerID):
    # (Line 53) if (unitid.UnitID[playerID] >= 1)
    if EUDIf()(unitid.UnitID[playerID] >= 1):
        # (Line 54) {
        # (Line 55) if (unitid.PlayerID[playerID] == 6 || unitid.PlayerID[playerID] == 7)
        if EUDIf()(EUDSCOr()(unitid.PlayerID[playerID] == 6)(unitid.PlayerID[playerID] == 7)()):
            # (Line 56) {
            # (Line 57) switch(unitid.UnitID[playerID])
            EUDSwitch(unitid.UnitID[playerID])
            # (Line 58) {
            # (Line 59) case 122:
            _t3 = EUDSwitchCase()
            # (Line 60) v.stb.printAt(0, "\n\n\x13\x19[ \x04Upgrade \x19]\n\n\x13\x04영웅의 능력을 업그레이드 하는 곳 입니다.\n\n");
            if _t3(122):
                v.stb.printAt(0, "\n\n\x13\x19[ \x04Upgrade \x19]\n\n\x13\x04영웅의 능력을 업그레이드 하는 곳 입니다.\n\n")
                # (Line 61) unitid.UnitID[playerID] = 0;
                _ARRW(unitid.UnitID, playerID) << (0)
                # (Line 62) break;
                EUDBreak()
                # (Line 63) case 125:
            _t4 = EUDSwitchCase()
            # (Line 64) v.stb.printAt(0, "\n\n\x13\x19[ \x04Shield \x19]\n\n\x13\x04- \x19수호자 사망\x04시 구입 가능합니다.\n\x13\x04- 신전의 쉴드량이 \x19100%\x04로 회복됩니다.\n\n\x13\x04- 무제한 구입 가능합니다.\n\n");
            if _t4(125):
                v.stb.printAt(0, "\n\n\x13\x19[ \x04Shield \x19]\n\n\x13\x04- \x19수호자 사망\x04시 구입 가능합니다.\n\x13\x04- 신전의 쉴드량이 \x19100%\x04로 회복됩니다.\n\n\x13\x04- 무제한 구입 가능합니다.\n\n")
                # (Line 65) unitid.UnitID[playerID] = 0;
                _ARRW(unitid.UnitID, playerID) << (0)
                # (Line 66) break;
                EUDBreak()
                # (Line 67) case 216:
            _t5 = EUDSwitchCase()
            # (Line 68) v.stb.printAt(0, "\n\n\x13\x19[ \x04Potion Discount \x19]\n\n\x13\x04- 포션 가격이 \x1920% \x04할인됩니다.\n\n\x13\x04- \x191 \x04회 구입 가능합니다.\n\n");
            if _t5(216):
                v.stb.printAt(0, "\n\n\x13\x19[ \x04Potion Discount \x19]\n\n\x13\x04- 포션 가격이 \x1920% \x04할인됩니다.\n\n\x13\x04- \x191 \x04회 구입 가능합니다.\n\n")
                # (Line 69) unitid.UnitID[playerID] = 0;
                _ARRW(unitid.UnitID, playerID) << (0)
                # (Line 70) break;
                EUDBreak()
                # (Line 71) case 217:
            _t6 = EUDSwitchCase()
            # (Line 72) v.stb.printAt(0, "\n\n\x13\x19[ \x04Mana Disk \x19]\n\n\x13\x04- 가스 회복량이 \x1950% \x04증가됩니다.\n\n\x13\x04- \x192 \x04회 구입 가능합니다.\n\n");
            if _t6(217):
                v.stb.printAt(0, "\n\n\x13\x19[ \x04Mana Disk \x19]\n\n\x13\x04- 가스 회복량이 \x1950% \x04증가됩니다.\n\n\x13\x04- \x192 \x04회 구입 가능합니다.\n\n")
                # (Line 73) unitid.UnitID[playerID] = 0;
                _ARRW(unitid.UnitID, playerID) << (0)
                # (Line 74) break;
                EUDBreak()
                # (Line 75) case 219:
            _t7 = EUDSwitchCase()
            # (Line 76) v.stb.printAt(0, "\n\n\x13\x19[ \x04Potion \x19]\n\n\x13\x04- \x19셔틀\x04 생산시 사용되는 아이템입니다.\n\x13\x04- 영웅의 체력을 \x19100%\x04로 회복시킵니다.\n\n\x13\x04- 최대 \x1915 \x04개 보유 가능합니다.\n\n");
            if _t7(219):
                v.stb.printAt(0, "\n\n\x13\x19[ \x04Potion \x19]\n\n\x13\x04- \x19셔틀\x04 생산시 사용되는 아이템입니다.\n\x13\x04- 영웅의 체력을 \x19100%\x04로 회복시킵니다.\n\n\x13\x04- 최대 \x1915 \x04개 보유 가능합니다.\n\n")
                # (Line 77) unitid.UnitID[playerID] = 0;
                _ARRW(unitid.UnitID, playerID) << (0)
                # (Line 78) break;
                EUDBreak()
                # (Line 79) }
            # (Line 80) }
            EUDEndSwitch()
            # (Line 82) if (unitid.PlayerID[playerID] == 10)
        EUDEndIf()
        if EUDIf()(unitid.PlayerID[playerID] == 10):
            # (Line 83) {
            # (Line 84) switch(unitid.UnitID[playerID])
            EUDSwitch(unitid.UnitID[playerID])
            # (Line 85) {
            # (Line 86) case 39:
            _t9 = EUDSwitchCase()
            # (Line 87) v.stb.printAt(0, "\n\n\x13\x19[ \x04Hoffnung \x19]\n\n\x13\x04- 아군 게이트가 \x19모두 파괴\x04되었을시 구입 가능합니다.\n\x13\x04- 맵상의 Hoffnung이 \x193마리 이하\x04일시 구입가능합니다.\n\n\x13\x04- \x19무제한 \x04구입 가능합니다.\n\n");
            if _t9(39):
                v.stb.printAt(0, "\n\n\x13\x19[ \x04Hoffnung \x19]\n\n\x13\x04- 아군 게이트가 \x19모두 파괴\x04되었을시 구입 가능합니다.\n\x13\x04- 맵상의 Hoffnung이 \x193마리 이하\x04일시 구입가능합니다.\n\n\x13\x04- \x19무제한 \x04구입 가능합니다.\n\n")
                # (Line 88) unitid.UnitID[playerID] = 0;
                _ARRW(unitid.UnitID, playerID) << (0)
                # (Line 89) break;
                EUDBreak()
                # (Line 90) case 169:
            _t10 = EUDSwitchCase()
            # (Line 91) v.stb.printAt(0, "\n\n\x13\x19[ \x04C Skill \x19]\n\n\x13\x04- \x19C Skill [ 캐리어 ] \x04를 사용할수 있게 됩니다.\n\n\x13\x04- \x191 \x04회 구입 가능합니다.\n\n");
            if _t10(169):
                v.stb.printAt(0, "\n\n\x13\x19[ \x04C Skill \x19]\n\n\x13\x04- \x19C Skill [ 캐리어 ] \x04를 사용할수 있게 됩니다.\n\n\x13\x04- \x191 \x04회 구입 가능합니다.\n\n")
                # (Line 92) unitid.UnitID[playerID] = 0;
                _ARRW(unitid.UnitID, playerID) << (0)
                # (Line 93) break;
                EUDBreak()
                # (Line 94) case 170:
            _t11 = EUDSwitchCase()
            # (Line 95) v.stb.printAt(0, "\n\n\x13\x19[ \x04A Skill \x19]\n\n\x13\x04- \x19A Skill [ 아비터 ] \x04를 사용할수 있게 됩니다.\n\n\x13\x04- \x191 \x04회 구입 가능합니다.\n\n");
            if _t11(170):
                v.stb.printAt(0, "\n\n\x13\x19[ \x04A Skill \x19]\n\n\x13\x04- \x19A Skill [ 아비터 ] \x04를 사용할수 있게 됩니다.\n\n\x13\x04- \x191 \x04회 구입 가능합니다.\n\n")
                # (Line 96) unitid.UnitID[playerID] = 0;
                _ARRW(unitid.UnitID, playerID) << (0)
                # (Line 97) break;
                EUDBreak()
                # (Line 98) }
            # (Line 99) }
            EUDEndSwitch()
            # (Line 100) }
        EUDEndIf()
        # (Line 101) }
    EUDEndIf()
