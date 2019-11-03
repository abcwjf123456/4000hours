import json

f = open("hh", "r")
g = json.loads(f.read())
print(g)
