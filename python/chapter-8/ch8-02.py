# 文件读,读模式只能读不能写
# readline()每次读一行而且会换行加入end=' '换行会去除
f = open('pi', 'r', encoding='utf-8')
# print(f.readline(),end=' ')
# print(f.readline())
# print(f.readline())
# print(f.readlines())

f.close()
