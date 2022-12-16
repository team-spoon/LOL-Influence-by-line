from pprint import pprint
import requests

api_key = "RGAPI-88ac3bfa-6138-474a-9fe0-83d835caaa57"
sohwan = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" +'hide on bush' +'?api_key=' + api_key
r = requests.get(sohwan).json()
pprint(r['name'])


tier_url = "https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/" + r['id'] +'?api_key=' + api_key
r2  = requests.get(tier_url).json()
pprint(r2)

challenger = 'https://kr.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5?api_key=' + api_key

r = requests.get(challenger)#챌데이터 호출
league_df = pd.DataFrame(r.json())

league_df.reset_index(inplace=True)#수집한 챌데이터 index정리
league_entries_df = pd.DataFrame(dict(league_df['entries'])).T #dict구조로 되어 있는 entries컬럼 풀어주기
league_df = pd.concat([league_df, league_entries_df], axis=1) #열끼리 결합

league_df = league_df.drop(['index', 'queue', 'name', 'leagueId', 'entries', 'rank'], axis=1)
league_df.info()
league_df.to_csv('챌데이터.csv',index=False,encoding = 'cp949')#중간저장