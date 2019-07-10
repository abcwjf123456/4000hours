# 反转列表
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()  # 永久性但可恢复重新调用reverse()及可
print(cars)
cars.reverse()
print(cars)
lg = len(cars)
print(lg)

# ['bmw', 'audi', 'toyota', 'subaru']
# ['subaru', 'toyota', 'audi', 'bmw']
# ['bmw', 'audi', 'toyota', 'subaru']
# reversed 函数返回一个反转的迭代器。
#
# reversed我没尝试
# 语法
# 以下是 reversed 的语法:
#
# reversed(seq)
# 参数
# seq -- 要转换的序列，可以是 tuple, string, list 或 range。
# 返回值
# 返回一个反转的迭代器。
