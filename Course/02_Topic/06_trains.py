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

retrieveTags=['TrainStatus',
            'TrainLatitude',
            'TrainLongitude',
            'TrainCode',
            'TrainDate',
            'PublicMessage',
            'Direction']

# I had an issue with blank lines in the file so found solution at
# https://stackoverflow.com/questions/3348460/csv-file-written-with-python-has-blank-lines-between-each-r
# adding the newline= '' parameter
#store this one property into a CSV
with open("06_train.csv","w", newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionsNode in objTrainPositionsNodes:
        dataList = []
        for retrieveTag in retrieveTags:
            if retrieveTag == "TrainCode":
                datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0)
                traincode = datanode.firstChild.nodeValue.strip()
                if "D" in traincode:
                    print(traincode)

                    datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0)
                    dataList.append(datanode.firstChild.nodeValue.strip())
                    train_writer.writerow(dataList)


