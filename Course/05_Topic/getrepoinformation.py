import requests
import json

filename = "repos-public-03.json"

#url = 'https://api.github.com/repos/DPR-droid/data-representation-courseware'
url = 'https://api.github.com/repos/DPR-droid/data-representation-courseware/contents/'
#url = 'https://api.github.com/repos/DPR-droid/aprivateone'

response = requests.get(url)
print (response.status_code)
repoJSON = response.json()
#print (response.json())

with  open(filename, 'w') as fp:
    json.dump(repoJSON, fp, indent=4)
