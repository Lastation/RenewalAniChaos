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
# (Line 4) const T_CharaterNum = PVariable();
T_CharaterNum = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 6) const T_CharacterName =
# (Line 7) [Db("#REF"),
# (Line 8) Db("루살카 슈베게린"),
# (Line 9) Db("크톨리 노타 세니오리스"),
# (Line 10) Db("텐카와 마이히메"),
# (Line 11) Db("히나나위 텐시"),
# (Line 12) Db("소네 미유키"),
# (Line 13) Db("네게브"),
# (Line 14) Db("세실리아"),
# (Line 15) Db("후타바 안즈"),
# (Line 16) Db("호토 모카"),
# (Line 17) Db("수수께끼의 얼터에고 Λ"),
# (Line 18) Db("류즈"),
# (Line 19) Db("토키사키 쿠루미"),
# (Line 20) Db("사쿠라"),
# (Line 21) Db("야시로 가쿠"),
# (Line 22) Db("린"),
# (Line 23) Db("세라핌"),
# (Line 24) Db("키아나 카스라나"),
# (Line 25) Db("이와후네 텐케이"),
# (Line 26) Db("마르고트 나이트 & 마르가 나르제"),
# (Line 27) Db("에메트셀크"),
# (Line 28) Db("마젤란"),
# (Line 29) Db("유우키 유우나"),
# (Line 30) Db("시이나 마유리"),
# (Line 31) Db("나나미 치아키"),
# (Line 32) Db("밀림 나바"),
# (Line 33) Db("츠바쿠로 유메"),
# (Line 34) Db("치쿠조인 마가네"),
# (Line 35) Db("오다 사쿠노스케"),
# (Line 36) Db("에키드나"),
# (Line 37) Db("니와 료카"),
# (Line 38) Db("박 일표"),
# (Line 39) Db("모리시마 호다카"),
# (Line 40) Db("아가츠마 젠이츠"),
# (Line 41) Db("유자키 츠카사"),
# (Line 42) Db("#REF")];
T_CharacterName = _CGFW(lambda: [_ARR(FlattenList([Db("#REF"), Db("루살카 슈베게린"), Db("크톨리 노타 세니오리스"), Db("텐카와 마이히메"), Db("히나나위 텐시"), Db("소네 미유키"), Db("네게브"), Db("세실리아"), Db("후타바 안즈"), Db("호토 모카"), Db("수수께끼의 얼터에고 Λ"), Db("류즈"), Db("토키사키 쿠루미"), Db("사쿠라"), Db("야시로 가쿠"), Db("린"), Db("세라핌"), Db("키아나 카스라나"), Db("이와후네 텐케이"), Db("마르고트 나이트 & 마르가 나르제"), Db("에메트셀크"), Db("마젤란"), Db("유우키 유우나"), Db("시이나 마유리"), Db("나나미 치아키"), Db("밀림 나바"), Db("츠바쿠로 유메"), Db("치쿠조인 마가네"), Db("오다 사쿠노스케"), Db("에키드나"), Db("니와 료카"), Db("박 일표"), Db("모리시마 호다카"), Db("아가츠마 젠이츠"), Db("유자키 츠카사"), Db("#REF")]))], 1)[0]
# (Line 44) const T_CharacterTitle =
# (Line 45) [Db("#REF"),
# (Line 46) Db("Dies irae"),
# (Line 47) Db("종말에 뭐 하세요? 바쁘세요? 구해 주실 수 있나요?"),
# (Line 48) Db("퀄리디아 코드"),
# (Line 49) Db("동방 스카이 아레나"),
# (Line 50) Db("당신과 그녀와 그녀의 사랑"),
# (Line 51) Db("소녀전선"),
# (Line 52) Db("킹스레이드"),
# (Line 53) Db("PROJECT iM@S CINDERELLA GIRLS"),
# (Line 54) Db("주문은 토끼입니까?"),
# (Line 55) Db("Fate Grand Order"),
# (Line 56) Db("클락워크 플레닛"),
# (Line 57) Db("DATE A LIVE"),
# (Line 58) Db("Fate/stay night"),
# (Line 59) Db("나만이 없는 거리"),
# (Line 60) Db("Shelter"),
# (Line 61) Db("영원한 7일의 도시"),
# (Line 62) Db("붕괴 3rd"),
# (Line 63) Db("K"),
# (Line 64) Db("경계선상의 호라이즌"),
# (Line 65) Db("Final Fantasy XIV"),
# (Line 66) Db("Arknights"),
# (Line 67) Db("유우키 유우나는 용사다"),
# (Line 68) Db("슈타인즈 게이트"),
# (Line 69) Db("단간론파"),
# (Line 70) Db("전생했더니 슬라임이었던 건에 대하여"),
# (Line 71) Db("도사의 무녀"),
# (Line 72) Db("Re : CREATORS"),
# (Line 73) Db("문호 스트레이독스"),
# (Line 74) Db("Re: 제로부터 시작하는 이세계 생활"),
# (Line 75) Db("십이대전"),
# (Line 76) Db("갓 오브 하이스쿨"),
# (Line 77) Db("날씨의 아이"),
# (Line 78) Db("귀멸의 칼날"),
# (Line 79) Db("어쨋든 귀여워"),
# (Line 80) Db("#REF")];
T_CharacterTitle = _CGFW(lambda: [_ARR(FlattenList([Db("#REF"), Db("Dies irae"), Db("종말에 뭐 하세요? 바쁘세요? 구해 주실 수 있나요?"), Db("퀄리디아 코드"), Db("동방 스카이 아레나"), Db("당신과 그녀와 그녀의 사랑"), Db("소녀전선"), Db("킹스레이드"), Db("PROJECT iM@S CINDERELLA GIRLS"), Db("주문은 토끼입니까?"), Db("Fate Grand Order"), Db("클락워크 플레닛"), Db("DATE A LIVE"), Db("Fate/stay night"), Db("나만이 없는 거리"), Db("Shelter"), Db("영원한 7일의 도시"), Db("붕괴 3rd"), Db("K"), Db("경계선상의 호라이즌"), Db("Final Fantasy XIV"), Db("Arknights"), Db("유우키 유우나는 용사다"), Db("슈타인즈 게이트"), Db("단간론파"), Db("전생했더니 슬라임이었던 건에 대하여"), Db("도사의 무녀"), Db("Re : CREATORS"), Db("문호 스트레이독스"), Db("Re: 제로부터 시작하는 이세계 생활"), Db("십이대전"), Db("갓 오브 하이스쿨"), Db("날씨의 아이"), Db("귀멸의 칼날"), Db("어쨋든 귀여워"), Db("#REF")]))], 1)[0]
# (Line 82) const T_CharacterType =
# (Line 83) [Db("#REF"),
# (Line 84) Db("공성전"),
# (Line 85) Db("공성전"),
# (Line 86) Db("대인전"),
# (Line 87) Db("모든전투"),
# (Line 88) Db("대인전"),
# (Line 89) Db("모든전투"),
# (Line 90) Db("대인전"),
# (Line 91) Db("공성전"),
# (Line 92) Db("공성전"),
# (Line 93) Db("공성전"),
# (Line 94) Db("대인전"),
# (Line 95) Db("모든전투"),
# (Line 96) Db("공성전"),
# (Line 97) Db("대인전"),
# (Line 98) Db("공성전"),
# (Line 99) Db("모든전투"),
# (Line 100) Db("모든전투"),
# (Line 101) Db("대인전"),
# (Line 102) Db("모든전투"),
# (Line 103) Db("공성전"),
# (Line 104) Db("공성전"),
# (Line 105) Db("모든전투"),
# (Line 106) Db("대인전"),
# (Line 107) Db("공성전"),
# (Line 108) Db("공성전"),
# (Line 110) Db("대인전"),
# (Line 111) Db("대인전"),
# (Line 112) Db("공성전"),
# (Line 113) Db("공성전"),
# (Line 114) Db("공성전"),
# (Line 116) Db("대인전"),
# (Line 117) Db("모든전투"),
# (Line 118) Db("대인전"),
# (Line 119) Db("공성전"),
# (Line 120) Db("#REF")];
T_CharacterType = _CGFW(lambda: [_ARR(FlattenList([Db("#REF"), Db("공성전"), Db("공성전"), Db("대인전"), Db("모든전투"), Db("대인전"), Db("모든전투"), Db("대인전"), Db("공성전"), Db("공성전"), Db("공성전"), Db("대인전"), Db("모든전투"), Db("공성전"), Db("대인전"), Db("공성전"), Db("모든전투"), Db("모든전투"), Db("대인전"), Db("모든전투"), Db("공성전"), Db("공성전"), Db("모든전투"), Db("대인전"), Db("공성전"), Db("공성전"), Db("대인전"), Db("대인전"), Db("공성전"), Db("공성전"), Db("공성전"), Db("대인전"), Db("모든전투"), Db("대인전"), Db("공성전"), Db("#REF")]))], 1)[0]
# (Line 122) const T_CharacterNeed =
# (Line 123) [Db("#REF"),
# (Line 124) Db("처음하는"),
# (Line 125) Db("적응된"),
# (Line 126) Db("숙련된"),
# (Line 127) Db("적응된"),
# (Line 128) Db("숙련된"),
# (Line 129) Db("처음하는"),
# (Line 130) Db("숙련된"),
# (Line 131) Db("처음하는"),
# (Line 132) Db("처음하는"),
# (Line 133) Db("적응된"),
# (Line 134) Db("숙련된"),
# (Line 135) Db("적응된"),
# (Line 136) Db("숙련된"),
# (Line 137) Db("숙련된"),
# (Line 138) Db("적응된"),
# (Line 139) Db("적응된"),
# (Line 140) Db("적응된"),
# (Line 141) Db("숙련된"),
# (Line 142) Db("숙련된"),
# (Line 143) Db("적응된"),
# (Line 145) Db("처음하는"),
# (Line 146) Db("숙련된"),
# (Line 147) Db("숙련된"),
# (Line 148) Db("숙련된"),
# (Line 149) Db("적응된"),
# (Line 151) Db("숙련된"),
# (Line 152) Db("숙련된"),
# (Line 153) Db("숙련된"),
# (Line 154) Db("적응된"),
# (Line 155) Db("적응된"),
# (Line 157) Db("숙련된"),
# (Line 158) Db("처음하는"),
# (Line 159) Db("적등된"),
# (Line 160) Db("적응된"),
# (Line 161) Db("#REF")];
T_CharacterNeed = _CGFW(lambda: [_ARR(FlattenList([Db("#REF"), Db("처음하는"), Db("적응된"), Db("숙련된"), Db("적응된"), Db("숙련된"), Db("처음하는"), Db("숙련된"), Db("처음하는"), Db("처음하는"), Db("적응된"), Db("숙련된"), Db("적응된"), Db("숙련된"), Db("숙련된"), Db("적응된"), Db("적응된"), Db("적응된"), Db("숙련된"), Db("숙련된"), Db("적응된"), Db("처음하는"), Db("숙련된"), Db("숙련된"), Db("숙련된"), Db("적응된"), Db("숙련된"), Db("숙련된"), Db("숙련된"), Db("적응된"), Db("적응된"), Db("숙련된"), Db("처음하는"), Db("적등된"), Db("적응된"), Db("#REF")]))], 1)[0]
# (Line 163) const T_CharacterTrait =
# (Line 164) [Db("#REF"),
# (Line 166) Db("\x1F#\x04공성특화 \x1F#\x04지속딜 \x1F#\x04설치 \x1F#\x04조작쉬움"),
# (Line 167) Db("\x1F#\x04공성특화 \x1F#\x04지속딜 \x1F#\x04전투속행 \x1F#\x04조작어려움"),
# (Line 168) Db("\x1F#\x04대인특화 \x1F#\x04지속딜 \x1F#\x04보조 \x1F#\x04조작보통"),
# (Line 169) Db("\x1F#\x04만능 \x1F#\x04순간딜 \x1F#\x04설치 \x1F#\x04조작보통"),
# (Line 170) Db("\x1F#\x04대인특화 \x1F#\x04순간딜 \x1F#\x04디버프 \x1F#\x04조작어려움"),
# (Line 172) Db("\x1F#\x04만능 \x1F#\x04순간딜 \x1F#\x04보조 \x1F#\x04조작보통"),
# (Line 173) Db("\x1F#\x04대인특화 \x1F#\x04순간딜 \x1F#\x04부활 \x1F#\x04조작어려움"),
# (Line 174) Db("\x1F#\x04공성특화 \x1F#\x04지속딜 \x1F#\x04보조 \x1F#\x04조작쉬움"),
# (Line 175) Db("\x1F#\x04공성특화 \x1F#\x04순간딜 \x1F#\x04보조 \x1F#\x04조작어려움"),
# (Line 176) Db("\x1F#\x04공성특화 \x1F#\x04지속딜 \x1F#\x04버프 \x1F#\x04조작어려움"),
# (Line 178) Db("\x1F#\x04대인특화 \x1F#\x04순간딜 \x1F#\x04디버프 \x1F#\x04조작쉬움"),
# (Line 179) Db("\x1F#\x04만능 \x1F#\x04순간딜 \x1F#\x04모드 \x1F#\x04조작어려움"),
# (Line 180) Db("\x1F#\x04공성특화 \x1F#\x04지속딜 \x1F#\x04디버프 \x1F#\x04조작어려움"),
# (Line 181) Db("\x1F#\x04대인특화 \x1F#\x04순간딜 \x1F#\x04스택 \x1F#\x04조작매우어려움"),
# (Line 182) Db("\x1F#\x04공성특화 \x1F#\x04지속딜 \x1F#\x04희생 \x1F#\x04조작어려움"),
# (Line 184) Db("\x1F#\x04만능 \x1F#\x04순간딜 \x1F#\x04영원한 7일 \x1F#\x04조작보통"),
# (Line 185) Db("\x1F#\x04만능 \x1F#\x04지속딜 \x1F#\x04특수 \x1F#\x04조작보통"),
# (Line 186) Db("\x1F#\x04대인특화 \x1F#\x04순간딜 \x1F#\x04무적의 사나이 \x1F#\x04조작보통"),
# (Line 187) Db("\x1F#\x04만능 \x1F#\x04지속딜 \x1F#\x04저격 \x1F#\x04조작보통"),
# (Line 188) Db("\x1F#\x04공성특화 \x1F#\x04지속딜 \x1F#\x04귀환 \x1F#\x04조작보통"),
# (Line 190) Db("\x1F#\x04공성특화 \x1F#\x04순간딜 \x1F#\x04드론 \x1F#\x04조작보통"),
# (Line 191) Db("\x1F#\x04만능 \x1F#\x04지속딜 \x1F#\x04하이리스크 \x1F#\x04하이리턴 \x1F#\x04조작어려움"),
# (Line 192) Db("\x1F#\x04대인특화 \x1F#\x04순간딜 \x1F#\x04고정 \x1F#\x04조작어려움"),
# (Line 193) Db("\x1F#\x04공성특화 \x1F#\x04지속딜 \x1F#\x04서포트 \x1F#\x04조작보통"),
# (Line 194) Db("\x1F#\x04공성특화 \x1F#\x04지속딜 \x1F#\x04기동성 \x1F#\x04조작보통"),
# (Line 196) Db("\x1F#\x04대인특화 \x1F#\x04순간딜 \x1F#\x04기동성 \x1F#\x04조작어려움"),
# (Line 197) Db("\x1F#\x04대인특화 \x1F#\x04순간딜 \x1F#\x04무효화 \x1F#\x04조작어려움"),
# (Line 198) Db("\x1F#\x04공성특화 \x1F#\x04지속딜 \x1F#\x04영구각성 \x1F#\x04조작어려움"),
# (Line 199) Db("\x1F#\x04공성특화 \x1F#\x04지속딜 \x1F#\x04계약 \x1F#\x04조작보통"),
# (Line 200) Db("\x1F#\x04공성특화 \x1F#\x04지속딜 \x1F#\x04버프 \x1F#\x04조작쉬움"),
# (Line 202) Db("\x1F#\x04대인특화 \x1F#\x04순간딜 \x1F#\x04기동성 \x1F#\x04조작어려움"),
# (Line 203) Db("\x1F#\x04만능 \x1F#\x04순간딜 \x1F#\x04디버프 \x1F#\x04조작쉬움"),
# (Line 204) Db("\x1F#\x04대인특화 \x1F#\x04순간딜 \x1F#\x04기동성 \x1F#\x04조작보통"),
# (Line 205) Db("\x1F#\x04공성특화 \x1F#\x04지속딜 \x1F#\x04조작쉬움"),
# (Line 206) Db("#REF")];
T_CharacterTrait = _CGFW(lambda: [_ARR(FlattenList([Db("#REF"), Db("\x1F#\x04공성특화 \x1F#\x04지속딜 \x1F#\x04설치 \x1F#\x04조작쉬움"), Db("\x1F#\x04공성특화 \x1F#\x04지속딜 \x1F#\x04전투속행 \x1F#\x04조작어려움"), Db("\x1F#\x04대인특화 \x1F#\x04지속딜 \x1F#\x04보조 \x1F#\x04조작보통"), Db("\x1F#\x04만능 \x1F#\x04순간딜 \x1F#\x04설치 \x1F#\x04조작보통"), Db("\x1F#\x04대인특화 \x1F#\x04순간딜 \x1F#\x04디버프 \x1F#\x04조작어려움"), Db("\x1F#\x04만능 \x1F#\x04순간딜 \x1F#\x04보조 \x1F#\x04조작보통"), Db("\x1F#\x04대인특화 \x1F#\x04순간딜 \x1F#\x04부활 \x1F#\x04조작어려움"), Db("\x1F#\x04공성특화 \x1F#\x04지속딜 \x1F#\x04보조 \x1F#\x04조작쉬움"), Db("\x1F#\x04공성특화 \x1F#\x04순간딜 \x1F#\x04보조 \x1F#\x04조작어려움"), Db("\x1F#\x04공성특화 \x1F#\x04지속딜 \x1F#\x04버프 \x1F#\x04조작어려움"), Db("\x1F#\x04대인특화 \x1F#\x04순간딜 \x1F#\x04디버프 \x1F#\x04조작쉬움"), Db("\x1F#\x04만능 \x1F#\x04순간딜 \x1F#\x04모드 \x1F#\x04조작어려움"), Db("\x1F#\x04공성특화 \x1F#\x04지속딜 \x1F#\x04디버프 \x1F#\x04조작어려움"), Db("\x1F#\x04대인특화 \x1F#\x04순간딜 \x1F#\x04스택 \x1F#\x04조작매우어려움"), Db("\x1F#\x04공성특화 \x1F#\x04지속딜 \x1F#\x04희생 \x1F#\x04조작어려움"), Db("\x1F#\x04만능 \x1F#\x04순간딜 \x1F#\x04영원한 7일 \x1F#\x04조작보통"), Db("\x1F#\x04만능 \x1F#\x04지속딜 \x1F#\x04특수 \x1F#\x04조작보통"), Db("\x1F#\x04대인특화 \x1F#\x04순간딜 \x1F#\x04무적의 사나이 \x1F#\x04조작보통"), Db("\x1F#\x04만능 \x1F#\x04지속딜 \x1F#\x04저격 \x1F#\x04조작보통"), Db("\x1F#\x04공성특화 \x1F#\x04지속딜 \x1F#\x04귀환 \x1F#\x04조작보통"), Db("\x1F#\x04공성특화 \x1F#\x04순간딜 \x1F#\x04드론 \x1F#\x04조작보통"), Db("\x1F#\x04만능 \x1F#\x04지속딜 \x1F#\x04하이리스크 \x1F#\x04하이리턴 \x1F#\x04조작어려움"), Db("\x1F#\x04대인특화 \x1F#\x04순간딜 \x1F#\x04고정 \x1F#\x04조작어려움"), Db("\x1F#\x04공성특화 \x1F#\x04지속딜 \x1F#\x04서포트 \x1F#\x04조작보통"), Db("\x1F#\x04공성특화 \x1F#\x04지속딜 \x1F#\x04기동성 \x1F#\x04조작보통"), Db("\x1F#\x04대인특화 \x1F#\x04순간딜 \x1F#\x04기동성 \x1F#\x04조작어려움"), Db("\x1F#\x04대인특화 \x1F#\x04순간딜 \x1F#\x04무효화 \x1F#\x04조작어려움"), Db("\x1F#\x04공성특화 \x1F#\x04지속딜 \x1F#\x04영구각성 \x1F#\x04조작어려움"), Db("\x1F#\x04공성특화 \x1F#\x04지속딜 \x1F#\x04계약 \x1F#\x04조작보통"), Db("\x1F#\x04공성특화 \x1F#\x04지속딜 \x1F#\x04버프 \x1F#\x04조작쉬움"), Db("\x1F#\x04대인특화 \x1F#\x04순간딜 \x1F#\x04기동성 \x1F#\x04조작어려움"), Db("\x1F#\x04만능 \x1F#\x04순간딜 \x1F#\x04디버프 \x1F#\x04조작쉬움"), Db("\x1F#\x04대인특화 \x1F#\x04순간딜 \x1F#\x04기동성 \x1F#\x04조작보통"), Db("\x1F#\x04공성특화 \x1F#\x04지속딜 \x1F#\x04조작쉬움"), Db("#REF")]))], 1)[0]
# (Line 208) const T_SubText =
# (Line 209) [Db("#REF"),
# (Line 210) Db("\x04에 특화 되어있습니다."),
# (Line 211) Db(" 플레이어에게 추천합니다.")];
T_SubText = _CGFW(lambda: [_ARR(FlattenList([Db("#REF"), Db("\x04에 특화 되어있습니다."), Db(" 플레이어에게 추천합니다.")]))], 1)[0]
