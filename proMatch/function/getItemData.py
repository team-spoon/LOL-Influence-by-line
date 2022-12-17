import requests
from pprint import pprint

f = open('data.txt', 'w')
getItemListUrl = 'https://ddragon.leagueoflegends.com/cdn/12.5.1/data/ko_KR/item.json'
r = requests.get(getItemListUrl)

pprint(r.json()['data'])

for i in r.json()['data']:
    pprint(r.json()['data'][i]['name'])


f.close()
