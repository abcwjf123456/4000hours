# [-]
import re

a = "qgytufrtderder"
b = "q8yftftyftyf"
print(re.findall("q[a-z]*", a))
print(re.findall("q[0-9]+", b))
# ['qgytufrtderder']
# ['q8']
