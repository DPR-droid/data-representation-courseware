# Lab 2: Trains
# XML data from irishrail

import requests
import csv
from xml.dom.minidom import parseString

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)

doc = parseString(page.content)

# Print to see it working
# Make xml readable
# print(doc.toprettyxml())

# modify the program so that it prints out the latitudes
objTrainPositionNodes = doc.getElementsByTagName("objTrainPositions")
for objTrainPositionNode in objTrainPositionNodes:
    trainlatnode = objTrainPositionNode.getElementsByTagName("TrainLatitude").item(0)
    trainlat = trainlatnode.firstChild.nodeValue.strip()
    print(trainlat)


