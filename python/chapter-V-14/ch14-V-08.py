# []
import re

a = "gfugdug,u"
print(re.findall("g[f,d]u", a))
# ['gfu', 'gdu', 'g,u']
