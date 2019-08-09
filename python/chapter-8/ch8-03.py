# 文件写模式
f = open('piii', 'w', encoding='utf-8')
# print(f.readlines()) 无法读而且文件存在会清空不在会新建
# print(f.readlines())
# f.write('ww')
# f.writelines(['\nfttftf']) 只能写字符串
f.close()
