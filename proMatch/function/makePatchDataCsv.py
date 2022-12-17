from pprint import pprint
import requests
import pandas as pd

from getPatchData import getItemPatchData

pprint(getItemPatchData("12-17"))


pprint(getItemPatchData("12-18"))
pprint(getItemPatchData("12-19"))
pprint(getItemPatchData("12-20"))
pprint(getItemPatchData("12-21"))
pprint(getItemPatchData("12-22"))
pprint(getItemPatchData("12-23"))


print('404 test')
pprint(getItemPatchData("12-24"))
