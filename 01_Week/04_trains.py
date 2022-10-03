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

#store this one property into a CSV
with open("04_train.csv","w", newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)


    objTrainPositionNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionNode in objTrainPositionNodes:
        traincodenode = objTrainPositionNode.getElementsByTagName("TrainCode").item(0)
        traincode = traincodenode.firstChild.nodeValue.strip()
        dataList = []
        dataList.append(traincode)
        train_writer.writerow(dataList)


