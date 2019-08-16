# 文件处理b模式
f = open('fi', 'rb')  # b模式下不能指定编码方式不然会报错
k = f.read()
print(k)
# 字符串-->encode-->bytes
# bytes-->decode-->字符串
print(k.decode('utf-8'))
f.flush()# 刷新保存
f.close()

# b'\xe5\x86\x99\xe5\x9c\xa8\xe6\x9c\x80\xe5\x90\x8e\r\n'
# 写在最后
