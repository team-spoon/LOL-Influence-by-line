from pprint import pprint
import requests
import pandas as pd

from getPatchData import getItemPatchDataV1, getItemPatchDataV2

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
    if version == '12-17':
        data = getItemPatchDataV1(version)
    else:
        data = getItemPatchDataV2(version)
    pprint("-------"+version+"-------")
    pprint(data if data else "아이템 변경점이 존재하지 않습니다.")
