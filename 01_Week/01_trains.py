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

# Store xml in a file.
with open("trainxml.xml","w") as xmlfp:
    doc.writexml(xmlfp)