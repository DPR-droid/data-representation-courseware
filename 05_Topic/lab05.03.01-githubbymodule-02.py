# to use this install package
# pip install PyGithub
from github import Github
import requests
from config import config as cfg

apikey = cfg["githubkey"]
# use your own key
g = Github(apikey)


repo = g.get_repo("DPR-droid/aprivateone")

# print(repo.clone_url)

fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
print(urlOfFile)

response = requests.get(urlOfFile)
contentOfFile = response.text
print(contentOfFile)

newContents = contentOfFile + "\nAndrew"
print(newContents)

gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",
newContents,fileInfo.sha)
print(gitHubResponse)