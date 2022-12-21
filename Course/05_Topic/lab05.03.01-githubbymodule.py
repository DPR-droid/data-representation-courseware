# to use this install package
# pip install PyGithub
from github import Github
import requests
from config import config as cfg

apikey = cfg["githubkey"]
# use your own key
g = Github(apikey)
for repo in g.get_user().get_repos():
    print(repo.name)