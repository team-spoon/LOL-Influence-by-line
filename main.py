KEY = "RGAPI-88ac3bfa-6138-474a-9fe0-83d835caaa57"
baseUrl = "https://kr.api.riotgames.com"

userName = input()
getUserDataUrl = baseUrl + f"/lol/summoner/v4/summoners/by-name/{userName}?api_key={KEY}"

print(getUserDataUrl)
