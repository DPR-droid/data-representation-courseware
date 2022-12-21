# XML Minidoms
#  for files

from xml.dom.minidom import parse
filename = "breakfast.xml"

# read file in two ways

doc = parse(filename)

# or 

with open(filename) as fp:
    doc2 = parse(fp)


print(doc.toprettyxml(), end='')

print(doc2.toprettyxml(), end='')