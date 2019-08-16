# 一: read(3)：
#
# 　　1. 文件打开方式为文本模式时，代表读取3个字符
#
# 　　2. 文件打开方式为b模式时，代表读取3个字节
#
# 二: 其余的文件内光标移动都是以字节为单位如seek，tell，truncate
#
# 注意：
#
# 　　1. seek有三种移动方式0，1，2，其中1和2必须在b模式下进行，但无论哪种模式，都是以bytes为单位移动的
#
# 　　2. truncate是截断文件，所以文件的打开方式必须可写，但是不能用w或w+等方式打开，因为那样直接清空文件了，所以truncate要在r+或a或a+等模式下测试效果
import time
with open('fi','rb') as f:
    f.seek(0,2)
    while True:
        line=f.readline()
        if line:
            print(line.decode('utf-8'))
        else:
            time.sleep(0.2)

