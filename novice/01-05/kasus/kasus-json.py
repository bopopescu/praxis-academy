# Reading JSON content from a file
import json
file_json = open("kasus.json")
data = json.loads(file_json.read())
print(data)

