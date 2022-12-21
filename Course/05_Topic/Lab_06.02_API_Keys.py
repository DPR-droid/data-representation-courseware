# In this lab we are going to use Python access APIs that need a key
# We are using the APIs as described by:
# • https://html2pdf.app/
# • https://developer.github.com/v3/guides/
# NOTE: You will have to get your own key from github

import requests
import urllib.parse
from config import config as cfg

targetUrl = "https://en.wikipedia.org"
#targetUrl = "https://www.atu.ie/"
#targetUrl = "https://www.google.com"


apiKey = cfg["htmltopdfkey"]
#api = "yourkey"
apiurl = 'https://api.html2pdf.app/v1/generate'

params = {'url': targetUrl,'apiKey': apiKey}
parsedparams = urllib.parse.urlencode(params)

requestUrl = apiurl +"?" + parsedparams 
print (requestUrl)

response = requests.get(requestUrl)

print (response.status_code)
result =response.content

with open("document.pdf", "wb") as handler:
    handler.write(result)