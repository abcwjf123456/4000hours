import json

dic = {"dsd": "dd"}
f = json.dumps(dic)
g = open("hh", "w")
g.write(f)
