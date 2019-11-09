# 通配符除了\n不能匹配其他的所有字符都能匹配
import re

a = "sssskkkkhghgffghh"
print(re.findall("f...h", a))
