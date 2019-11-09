# 贪婪匹配变惰性匹配
import re

a = "rtkkkkk"
print(re.findall("rtk*?", a))
print(re.findall("rtk??", a))
print(re.findall("rtk+?", a))

# ['rt']
# ['rt']
# ['rtk']
