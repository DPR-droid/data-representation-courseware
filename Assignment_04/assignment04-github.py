# Imports
from github import Github
import requests
import re

# Hide API key in config.py
# This is hidden by updating the gitignore file
from config import config as cfg


# get API key in config.py
apikey = cfg["githubkey"]
# Use API Key
g = Github(apikey)

# Get Text file from repo
repo = g.get_repo("DPR-droid/aprivateone")

# Get the Download URL of the file in this repository called test.txt 
fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
# print(urlOfFile)

# Use the download URL to make a http request to the file can output the contents of the file
response = requests.get(urlOfFile)
contentOfFile = response.text
#print(contentOfFile)

# Replace all the instances of the text "Andrew" with your David using re
newContents = re.sub('Andrew', 'David', contentOfFile)
# print(newContents)

# Update the contents of the test.txt on git.
gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",
newContents,fileInfo.sha)
print(gitHubResponse)


