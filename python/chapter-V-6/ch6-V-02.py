# 深入理解for循环遵循迭代器协议工作方式
# 下面是模拟for循环工作方式
l = [1, 2, 3]
h = l.__iter__()  # 转换成迭代对象
while True:
    try:
        print(h.__next__())  # 当值取完捕捉异常
    except StopIteration:
        print('完成迭代')
        break
