import requests
from pprint import pprint

KEY = "RGAPI-88ac3bfa-6138-474a-9fe0-83d835caaa57"
baseUrl = "https://kr.api.riotgames.com"

leagues = [
  "challengerleagues",
  "grandmasterleagues",
  # "masterleagues"
]
f = open("proNickname.txt", 'w')
result = []

for league in leagues:
  getProNicknameUrl = baseUrl + f"/lol/league/v4/{league}/by-queue/RANKED_SOLO_5x5?api_key={KEY}"
  r = requests.get(getProNicknameUrl).json()
  for response in r['entries']:
    if response['veteran']:
      f.write(response["summonerName"] + '\n')
      result.append(response["summonerName"])

pprint(result)
f.close()
