from pprint import pprint
import requests
import pandas as pd
import urllib
import time
import csv

api_key = "RGAPI-936fbe44-a27a-4aaf-96c0-9a9ae3df5159"
# sohwan = (
#     "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/"
#     + "hide on bush"
#     + "?api_key="
#     + api_key
# )
# r = requests.get(sohwan).json()
# # pprint(r["name"])

# print(r)

# tier_url = (
#     "https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/"
#     + r["id"]
#     + "?api_key="
#     + api_key
# )
# r2 = requests.get(tier_url).json()
# print(r2)
# # pprint(r2)

# challenger = (
#     "https://kr.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5?api_key="
#     + api_key
# )

# r = requests.get(challenger)  # 챌데이터 호출
# league_df = pd.DataFrame(r.json())

# league_df.reset_index(inplace=True)  # 수집한 챌데이터 index정리
# league_entries_df = pd.DataFrame(
#     dict(league_df["entries"])
# ).T  # dict구조로 되어 있는 entries컬럼 풀어주기
# league_df = pd.concat([league_df, league_entries_df], axis=1)  # 열끼리 결합

# league_df = league_df.drop(
#     ["index", "queue", "name", "leagueId", "entries", "rank"], axis=1
# )
# league_df.info()

# for i in range(len(league_df)):
#     try:
#         nickname = urllib.parse.quote(league_df['summonerName'].iloc[i])
#         sohwan = 'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + nickname + '?api_key=' + api_key
#         r = requests.get(sohwan)
#         print(sohwan)
#         print(r.status_code)
#         while r.status_code == 429:
#             time.sleep(5)
#             sohwan = 'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + league_df['summonerName'].iloc[i] + '?api_key=' + api_key
#             r = requests.get(sohwan)

#         account_id = r.json()['puuid']
#         league_df.iloc[i, -1] = account_id

#     except:
#         pass

# league_df.to_csv("챌데이터.csv", index=False, encoding="utf-8")  # 중간저장


# TODO - 챌데이터 시간 단위 뭔지 알아보기
f = open('챌데이터.csv', 'r')
challengerData = pd.DataFrame(csv.reader(f))  # 챌유저 puuid 저장된 csv
puuid = challengerData[9]

match_info_df = pd.DataFrame()

result = {'matchId': []}
print(len(puuid))
print(puuid)
for i in range(1, len(puuid)):
    try:
        nowPuuid = puuid.iloc[i]
        print(nowPuuid)
        matchUrl = f'https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/{nowPuuid}/ids?count=100&api_key={api_key}'

        r = requests.get(matchUrl)
        json = list(r.json())  # matchId 100개를 받아와서 for loop
        for challengermatchId in json:
            result['matchId'].append(challengermatchId)  # matchId 행에 추가

        while r.status_code == 429:  # 호출 limit 예외처리
            time.sleep(5)
            sohwan = f'https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/{nowPuuid}/ids?count=100&api_key={api_key}'
            r = requests.get(sohwan)
    except:
        print('엄@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

match_info_df = pd.DataFrame(result)

match_info_df.to_csv('챌경기.csv', index=False, encoding="utf-8")


f.close()
