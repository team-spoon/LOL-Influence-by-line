import requests
from pprint import pprint

KEY = "RGAPI-936fbe44-a27a-4aaf-96c0-9a9ae3df5159"
baseUrl = "https://kr.api.riotgames.com"

leagues = [
    "challengerleagues",
    "grandmasterleagues",
    # "masterleagues"
]
f = open("proNickname.txt", 'w')
result = []

for league in leagues:
    getProNicknameUrl = f"{baseUrl}/lol/league/v4/{league}/by-queue/RANKED_SOLO_5x5?api_key={KEY}"
    r = requests.get(getProNicknameUrl).json()
    for response in r['entries']:
        if response['veteran']:
            f.write(response["summonerName"] + '\n')
            result.append(response["summonerName"])

pprint(result)
f.close()
