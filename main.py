from pprint import pprint
import requests
import pandas as pd
import urllib
import time
import csv

api_key = "RGAPI-88ac3bfa-6138-474a-9fe0-83d835caaa57"
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
            
#         account_id = r.json()['accountId']
#         league_df.iloc[i, -1] = account_id

#     except:
#         pass

# league_df.to_csv("챌데이터.csv", index=False, encoding="utf-8")  # 중간저장

f = open('챌데이터.csv','r')
rdr = csv.reader(f)

league_df3 = pd.DataFrame(rdr)

match_info_df = pd.DataFrame()
season = str(13)

print(league_df3)

for i in range(len(league_df3)):
    print(league_df3['accountId'].iloc[i])
    
    # match0 = 'https://kr.api.riotgames.com/lol/match/v4/matchlists/by-account/' + league_df3['accountId'].iloc[i]  +'?season=' + season + '&api_key=' + api_key
    # print(match0)
    
    # try:
    #     r = requests.get(match0)
        
    #     while r.status_code == 429:
    #         time.sleep(5)
    #         match0 = 'https://kr.api.riotgames.com/lol/match/v4/matchlists/by-account/' + league_df3['account_id'].iloc[i]  +'?season=' + season + '&api_key=' + api_key
    #         r = requests.get(match0)
        
    #     match_info_df = pd.concat([match_info_df, pd.DataFrame(r.json()['matches'])])
    
    # except:
    #     print(i)



f.close()