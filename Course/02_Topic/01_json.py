import json
from urllib import response
data = {
    'name':'joe',
    'age':21,
    'student': True
}

print(data)

file = open("simple.json", 'w')

jsonString = json.dumps(data)
print(jsonString)