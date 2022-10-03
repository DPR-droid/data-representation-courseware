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

# the program to print out each of the trainscodes. I.e. find the listings and
# iterate through them to print each traincode out.
objTrainPositionNodes = doc.getElementsByTagName("objTrainPositions")
for objTrainPositionNode in objTrainPositionNodes:
    traincodenode = objTrainPositionNode.getElementsByTagName("TrainCode").item(0)
    traincode = traincodenode.firstChild.nodeValue.strip()
    print(traincode)


