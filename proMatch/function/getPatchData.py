from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from pprint import pprint
import requests

item_list = ['장화',
             '요정의 부적',
             '원기 회복의 구슬',
             '거인의 허리띠',
             '민첩성의 망토',
             '방출의 마법봉',
             '사파이어 수정',
             '루비 수정',
             '천 갑옷',
             '쇠사슬 조끼',
             '마법무효화의 망토',
             '잉걸불 칼',
             '롱소드',
             '곡괭이',
             'B.F. 대검',
             '빗발칼날',
             '흑요석 검',
             '단검',
             '곡궁',
             '증폭의 고서',
             '흡혈의 낫',
             '도란의 방패',
             '도란의 검',
             '도란의 반지',
             '음전자 망토',
             '쓸데없이 큰 지팡이',
             '암흑의 인장',
             '수확의 낫',
             '체력 물약',
             '굳건한 의지의 완전한 비스킷',
             '키르히아이스의 파편',
             '충전형 물약',
             '부패 물약',
             '수호자의 뿔피리',
             '포로 간식',
             '제어 와드',
             '슈렐리아의 군가',
             '강철의 영약',
             '마법의 영약',
             '분노의 영약',
             '미니언 해체분석기',
             '초시계 키트',
             '초시계',
             '망가진 초시계',
             '약간 신비한 신발',
             '완벽한 초시계',
             '망가진 초시계',
             '저녁갑주',
             '대천사의 지팡이',
             '마나무네',
             '광전사의 군화',
             '신속의 장화',
             '화학공학 부패기',
             '마법사의 신발',
             '얼음 방패',
             '수호 천사',
             '무한의 대검',
             '필멸자의 운명',
             '최후의 속삭임',
             '도미닉 경의 인사',
             '대천사의 포옹',
             '메자이의 영혼약탈자',
             '무라마나',
             '탐식의 망치',
             '유령 무희',
             '판금 장화',
             '지크의 융합',
             '온기가 필요한 자의 도끼',
             '스테락의 도전',
             '광휘의 검',
             '정령의 형상',
             '비상의 월갑',
             '점화석',
             '태양불꽃 방패',
             '여신의 눈물',
             '칠흑의 양날 도끼',
             '피바라기',
             '굶주린 히드라',
             '가시 갑옷',
             '덤불 조끼',
             '티아맷',
             '삼위일체',
             '파수꾼의 갑옷',
             '워모그의 갑옷',
             '루난의 허리케인',
             '열정의 검',
             '라바돈의 죽음모자',
             '마법사의 최후',
             '고속 연사포',
             '폭풍갈퀴',
             '리치베인',
             '밴시의 장막',
             '군단의 방패',
             '구원',
             '악마의 마법서',
             '기사의 맹세',
             '얼어붙은 심장',
             '헤르메스의 발걸음',
             '수호자의 보주',
             '에테르 환영',
             '금지된 우상',
             '내셔의 이빨',
             '라일라이의 수정홀',
             '기동력의 장화',
             '혹한의 손길',
             '종말의 겨울',
             '처형인의 대검',
             '구인수의 격노검',
             '콜필드의 전투 망치',
             '톱날 단검',
             '공허의 지팡이',
             '헤르메스의 시미터',
             '수은 장식띠',
             '요우무의 유령검',
             '란두인의 예언',
             '마법공학 교류 발전기',
             '마법공학 로켓 벨트',
             '몰락한 왕의 검',
             '주문포식자',
             '맬모셔스의 아귀',
             '존야의 모래시계',
             '명석함의 아이오니아 장화',
             '모렐로노미콘',
             '수호자의 검',
             '그림자 검',
             '선체파괴자',
             '수호자의 망치',
             '강철의 솔라리 펜던트',
             '추적자의 팔목 보호대',
             '가고일 돌갑옷',
             '망령의 두건',
             '미카엘의 축복',
             '허수아비',
             '투명 와드',
             '망원형 개조',
             '예언자의 렌즈',
             '수당',
             '불타는 향로',
             '정수 약탈자',
             '전령의 눈',
             '칼리스타의 칠흑의 창',
             '칼리스타의 칠흑의 창',
             '망자의 갑옷',
             '거대한 히드라',
             '수정 팔 보호구',
             '사라진 양피지',
             '밤의 끝자락',
             '주문도둑의 검',
             '얼음 송곳니',
             '얼음 정수의 파편',
             '강철 어깨 보호대',
             '룬 강철 어깨 갑옷',
             '화이트록의 갑옷',
             '고대유물 방패',
             '타곤 산의 방패',
             '타곤 산의 방벽',
             '영혼의 낫',
             '해로윙 초승달낫',
             '검은 안개 낫',
             '망각의 구',
             '제국의 명령',
             '대자연의 힘',
             '황금 뒤집개',
             '지평선의 초점',
             '우주의 추진력',
             '역병의 보석',
             '신록의 장벽',
             '균열 생성기',
             '흡수의 시선',
             '밤의 수확자',
             '악마의 포옹',
             '감시하는 와드석',
             '밴들유리 거울',
             '경계의 와드석',
             '부서진 여왕의 왕관',
             '그림자불꽃',
             '강철가시 채찍',
             '은빛 여명',
             '죽음의 무도',
             '화공 펑크 사슬검',
             '흐르는 물의 지팡이',
             '월석 재생기',
             '선혈포식자',
             '발걸음 분쇄기',
             '신성한 파괴자',
             '리안드리의 고뇌',
             '루덴의 폭풍',
             '만년서리',
             '바미의 불씨',
             '서리불꽃 건틀릿',
             '터보 화공 탱크',
             '절정의 화살',
             '돌풍',
             '크라켄 학살자',
             '불멸의 철갑궁',
             '나보리 신속검',
             '징수의 총',
             '분노의 칼',
             '드락사르의 황혼검',
             '월식',
             '자객의 발톱',
             '세릴다의 원한',
             '독사의 송곳니',
             '원칙의 원형낫',
             '증오의 사슬',
             '심연의 가면']


def init(version):  # 초기화
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    driver = webdriver.Chrome('chromedriver')
    driver.implicitly_wait(1)
    driver.get(
        f"https://www.leagueoflegends.com/ko-kr/news/game-updates/patch-{version}-notes/")
    html = driver.page_source
    bs = BeautifulSoup(html, "html.parser")
    return bs.body \
        .find("div", {"id": "patch-notes-container"}) \
        .findAll("div", {"class": "content-border"}) \



def isItem(item_name: str):  # 해당 패치에서 변경된 항목 중 아이템인가?
    global result, item_list
    if item_name in item_list:
        return True
    return False


result = []


def getItemPatchDataV1(version):  # 패치 정보 웹사이트 접속해서 아이템의 변경점을 출력한다
    item_name = init(version)
    result = []
    for item in item_name:
        itemJson = {}
        newItem = item.find_all("h3", {"class", "change-title"})  # 아이템 목록들
        # print(newItem)
        for item2 in newItem:
            if isItem(item2.get_text()):
                itemJson = {}

                changeList = item.find_all(
                    "div", {"class", "attribute-change"})

                result2 = []

                for change in changeList:
                    result2.append(change.get_text().strip())

                itemJson['name'] = item2.get_text().strip()
                itemJson['changes'] = list(result2)

                result.append(itemJson)

    return result


def getItemPatchDataV2(version):  # 패치 정보 웹사이트 접속해서 아이템의 변경점을 출력한다
    item_name = init(version)
    result = []
    for item in item_name:
        itemJson = {}
        newItem = item.find_all("h3", {"class", "change-title"})  # 아이템 목록들
        # print(newItem)
        for item2 in newItem:
            if isItem(item2.get_text()):
                itemJson = {}

                # before 12-17
                # changeList = item.find_all(
                #     "div", {"class", "attribute-change"})

                # after 12-18
                changeList = item.find_all(
                    "li")

                result2 = []

                for change in changeList:
                    result2.append(change.get_text().strip())

                itemJson['name'] = item2.get_text().strip()
                itemJson['changes'] = list(result2)

                result.append(itemJson)

    return result

