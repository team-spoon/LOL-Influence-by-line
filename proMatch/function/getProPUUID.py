import json
import requests
from pprint import pprint

KEY = "RGAPI-936fbe44-a27a-4aaf-96c0-9a9ae3df5159"
baseUrl = "https://kr.api.riotgames.com"

proNickname = ['zhouyudagougou',  'haohaodayouxi',  'zika1',  '뭐라고번역하지',  '피그차이나',  '안 믿어 사람',  '동냥아치',  'KDF 불독',  'KDF 알빙고',  'peyzz',  'Route9',  'Academy T1',  '어쩌라고맞짱뜰까',  'FA Kingdom',  '수지타산 맞으면',  'rewkfopdsfk',  'Talon817',  'ZOEKlNG',  'Rich3',  '김민교 수제자',  '10일의전사',  'G1DEON',  '221124',  '저빵인데터졌어영',  'Shadow Patch',  '이니쉬',  'ArkRuHa',  '청포도욕포',  'KT Castle',  '광연44',  'fragiIe',  '연애꽃1',  '행복한 태윤이',  '담원기아 루시드',  'yinheyinheyinhe',  'Every Sec0nd',  'FA Peach',  '전설의롤1234',  '바람부는언덕위에',  '이렐아칼리',  '이야공',  '은가뉴',  '다없수질',  'KDF 태윤',  'KT Way',  'DK Thanatos',  'zuihouyinian1',  'pojang',  '시간의 숲',  '1111111188888888',  '족발집 막내아들',  '난화내',  'VicLa27',  'onlydie1234',  'Kariszz',  '쭌 베',  'Bulld0g1',  '존중겸손아닥집중',  '농심라면다내꺼야',  'Radiohead',  '버기해적단 버기',  '앙 맛있엉',  '케이티 기리',  'T1 Smash1',  'Shadow Howling',  'BRO Hena',  'small champ pool',  'Erilia',  'laji fuzhu',  '관 모',  'psavncav',  '강주연',  '아 좀 맛없네',  'DRX Piero',  'Jett0',  'Sangchu',  'kiin',  'BRO Morgan',  'hxqeyff',  'XdXFncyDml0',  '이기고싶댜아',  'DreammaerD',  'person to leave',  'hhhhbbbb',  '마마돈워링',  'yuezhihuxi',  '젠지 뚱러',  'aaw4',  '언니우기',  'qweqweqwerrr',  'GHJVGFJG',  'nihao hello hi',  'TPzhao727472857',  '갈과 배 음료',  '숨바꼭질',  'Cry Outt',  'Seven',  '호잇이',  'Na Xi Da qwq',  '용병배영준',  'insuleixun',  '기묘기묘',  '최강 EDGAR',  'MID Lava',  'real gankster',  'Enosh3',  'Shadow Nia',  '신을저주해',  'xtyx',  'Shadow 1234',  'Irene Irene',  'NekoL',  '이 차가 식기전에',  'K a e 1',  'KDF 영재',  'lIlIIIIllllII',  'C9 EMENES',  '화내기도지쳤어',  'wywq987',  'KPL AG menglei',  'plume33',  '하이빵깨루',  'FIORAKlNG',  'Croco',  '손목위재스민',  'Juhana',  '패기는곳기회',  'General Irel',  '로 망',  '결국우린끝난사이',  '너 죽이는 방법',  '크으리',  '달빛써서예성',  'rtdvxz',  'limit',  '토실토실한붕어',  'DK Loopy',  'yaojiayouyaonuli',  '김다미 팬보이',  'ywohS',  'myboo',  'HLE Lure',  '삐카삐카랄라',  '이런 매서운 버돌',  '규 보 리',  '큐 지',
               '내가 대격변이다 ',  'GOLDIE',  'baiyezzz',  'GukBo',  'shadow 1111',  '짜리몽땅 지우개',  'ben dan xiao you',  'NS HH',  'facover',  '토트 무지카',  '별사탕이좋아요',  'BLACKSMITHKING',  '나약할 민',  'cheon2',  'asdoihqwhdoqwd',  'Wakanda 4ever',  '햄쥐의 볼주머니',  '외롭게는하지마요',  '지도없는항해',  'HealthandAhn',  'Azhy',  '뚱뚱하다5',  'love수면',  '절대집중력',  'kaibaibaxdm',  '승승웅',  '05 RENGARKING',  '매 루',  'Swalla',  'mm1m',  'TL Bradley',  '연패 후 연승',  '04 12 2003',  'what3ver',  '분노의 쭈꾸미',  'wqeqweqwe',  '어흥 놀랐지',  'T1 Photon1',  '우주 럭스',  '북쪽의괴물1',  '현주입니다',  '971218',  '실우치구',  '저돌적인 포지션',  'jkjkjkjkk',  'love part1',  '무지성카정원툴',  'DRX JaeHK',  'dangyadangyadang',  '준승이',  '김새루',  'DF 깍는노인',  'Liquid Medic',  '온 재',  '마음이 피곤하다',  '운을 바꾸다',  '별을 보고 싶어요',  'yaoyao재비행',  'changhong',  '욕망의 신',  'One Last K1ss',  'eg0ist1',  '악마돌',  '메운디클하면닉변',  '잠원토박이 마타',  '연노랑색',  '푸쿠이',  'FiddleStick',  '지지크',  '할수없는걸까',  'TwitchTV Migung',  '순규박',  'Lovepanpan',  '전설이 될 남자',  '나만 잘하면 그만',  '꼉굴이',  'AlphaGo test 06',  '볼때마다잘하는놈',  '워워 도현',  'not want to fail',  'lao liu',  'hi its viper',  'kyeahoo',  'Imagine Legends',  'SBXG Willer',  'dsasfgsdf',  'dlrj',  '우치하 찬스케',  'Peter0',  '미쳤어찬바람',  'Lion King 1',  'DK Siwoo',  '순애거든',  'Jianguoqiangzz',  '양여명',  '크산테 클레드',  '국민의힘 갤러리',  'LPL JUG',  'kanwocaozuo',  'uiui1',  '교육잘받은도구',  'haoyunyuanyuan',  '너희는 늙어봤냐',  'Firework37',  '생배 원챔 카서스',  'Beau Voyage',  'haoeeeee',  'lifgfasdfa',  'care bad girl',  'Megalia',  'xiayibale',  'cikcik',  '송창근SONG',  '12Savage',  'sdaskdjaslkd',  '초이통통',  'Sonozakishoin',  '나도 행복하자',  '입영기다리는사람',  'LSB PlanB',  '어린벌꿀오소리',  '아프리카 강주찬 ',  '윈터는차가워',  'LSB Vincenzo',  '아이러니zz',  'TOPKING',  'BVOYOVB',  'mdsgbzgo5678',  'xxiaofang',  'asdasddsaf',  '리포포o',  'NS 탑',  'sadfadsfe',  'Iove Riven',  'motfe',  'shinim1',  '야이야이야이이야',  '진짜롤너무어렵다',  'xiaguang',  'CARFE3',  '장영인서준',  'LGDChovy',  '고등학생',  'Deft DK',]

f = open("proPUUID.txt", 'w')

for nickname in proNickname:
    getUserPUUIDUrl = f"{baseUrl}/lol/summoner/v4/summoners/by-name/{nickname}?api_key={KEY}"
    r = requests.get(getUserPUUIDUrl).json()
    try:
        f.write(r['puuid'] + ',\n ')
    except:
        print('data가 없습니다.')

f.close()
