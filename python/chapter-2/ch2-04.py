# 对列表就行排序
# 前提都是小写且为永久性排序
# sort()方法语法：
#
# list.sort(cmp=None, key=None, reverse=False)
# 参数
# cmp -- 可选参数, 如果指定了该参数会使用该参数的方法进行排序(python2.7)。
# key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
# reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。z
# 返回值
# 该方法没有返回值，但是会对列表的对象进行排序。
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# ['audi', 'bmw', 'subaru', 'toyota']
# ['toyota', 'subaru', 'bmw', 'audi']
