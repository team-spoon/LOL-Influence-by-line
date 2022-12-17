from pprint import pprint
import requests
import pandas as pd

from getPatchData import getItemPatchData

versionList = [
    '12-17',
    '12-18',
    '12-19',
    '12-20',
    '12-21',
    '12-22',
    '12-23',
    '12-24',
]

for version in versionList:
    data = getItemPatchData(version)
    pprint("-------"+version+"-------")
    pprint(data if data else "아이템 변경점이 존재하지 않습니다.")
