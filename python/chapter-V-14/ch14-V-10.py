# import re
#
# ret = re.findall("www\.(baidu|oldboy)\.com", "www.oldboy.com")
# print(ret)
# ['oldboy']
# 这是因为findall会优先把匹配结果组里内容返回，如果想要匹配结果，取消权限即可

import re

ret = re.findall("www\.(?:baidu|oldboy)\.com", "www.oldboy.com")
print(ret)
# ['www.oldboy.com']
