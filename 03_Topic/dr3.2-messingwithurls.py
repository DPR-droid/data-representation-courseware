import requests

url = "http://atu.ie"

response = requests.get(url)
print(response.headers)
print(response.status_code)