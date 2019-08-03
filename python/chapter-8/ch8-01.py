# 从文件中读取数据
# 读取整个文件
# 删除空格 Python rstrip() 删除 string 字符串末尾的指定字符（默认为空格）
with open('E:\4000hours\python\chapter-8\pi') as fill_object:
    contents=fill_object.read()
    print(contents.rstrip())

