# *
import re

a = "wkdeeeee"
b = "wkd"
print(re.findall("^w..e*", a))
print(re.findall("wkde*", b))
# ['wkdeeeee']
# ['wkd']
