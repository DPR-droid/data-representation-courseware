# Assignment 03

# Write a program that retrieves the dataset for the "exchequer account (historical series)" from the CSO, and stores it into a file called "cso.json"

#     Upload this program to the same repository you used for the XML assignment
#     Save this assignment as "assignment03-cso.py"
#     This program should not be a long one
#         I don't need you to reformat or analyse the data in any way
#         It should be about 10ish lines long (I have not counted)
#     You will need to find the dataset in CSO.ie, try economic and then finance.

from ast import Pass
import requests
import json

urlBegining = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02"
urlEnd = "/JSON-stat/2.0/en"


def getAllAsFile():
    with open("cso.json", "wt") as fp:
        print(json.dumps(getAll()), file=fp)

def getAll():   
    url = urlBegining + urlEnd
    response = requests.get(url)
    return response.json()


if __name__ == "__main__":
    getAllAsFile()