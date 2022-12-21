# XML Minidoms
# for employees.xml


from xml.dom.minidom import parse
filename = "company.xml"

doc = parse(filename)

employeesNodeList = doc.getElementsByTagName("Employee")
print(len(employeesNodeList))
for employeeNode in employeesNodeList:
    # print("->")
    firstNameNode = employeeNode.getElementsByTagName("FirstName").item(0)
    firstName = firstNameNode.firstChild.nodeValue.strip()
    print(firstName)


