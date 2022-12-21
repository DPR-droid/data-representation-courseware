# Read json from a web
# 
import requests
import json
url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
data = response.json()
# print(data)

### Add to file
# with open("bitcoindump.json", "w") as fp:
#     json.dump(data, fp)

#  Get Euro rate of bitcoin

euroobject = data["bpi"]["EUR"]
rate = euroobject["rate"]
print(rate)