# to use this install package
# pip install PyGithub
from github import Github
import requests
from config import config as cfg

apikey = cfg["githubkey"]
# use your own key
g = Github(apikey)


repo = g.get_repo("DPR-droid/aprivateone")
print(repo.clone_url)