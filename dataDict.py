import json
from collections import namedtuple
from json import JSONEncoder



def custonDataDecoder(dataDict):
    return namedtuple('X', dataDict.keys())(*dataDict.values())

f = open("data.json", "r")
json_string = f.read()
f.close()

dataDict = json.loads(json_string, object_hook=custonDataDecoder)
print(dir(dataDict.students))


