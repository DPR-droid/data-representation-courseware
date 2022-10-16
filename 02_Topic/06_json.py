import json
from urllib import response
data = {
    'name':'joe',
    'age':21,
    'student': True
}

print(data)

file = open("simple.json", 'w')

jsonString = json.dumps(data)
print(jsonString)

######################################

# Read from a file 

import json
filename = "simple.json"
with open(filename, "r") as fp:
    jsonobject = json.load(fp)
# print(jsonobject)
for name in jsonobject["name"]:
    print(name)


######################################

# Read from a web
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