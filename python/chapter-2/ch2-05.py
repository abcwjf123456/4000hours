# sorted 语法：
# 临时排序
# sorted(iterable, key=None, reverse=False)
# 参数说明：
#
# iterable -- 可迭代对象。
# key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
# reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。
# 返回值
# 返回重新排序的列表。

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print(sorted(cars))
print(cars)

# ['bmw', 'audi', 'toyota', 'subaru']
# ['audi', 'bmw', 'subaru', 'toyota']
# ['bmw', 'audi', 'toyota', 'subaru']
