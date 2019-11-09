# {}
import re

a = "weeeeee"
b = "wee"
print(re.findall("we{3}", a))
print(re.findall("we{0,4}", a))
print(re.findall("we{0,4}", b))
# ['weee']
# ['weeee']
# ['wee']
