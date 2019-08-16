# 迭代器
# 迭代器对象必须提供一个next()方法
# （字符串，列表，字典，元组，集合，文件对象）这些都不是可迭代对象只不过for循环式，调用了他们内部的__iter__把他们变成了可迭代对象。
# 然后for循环调用可迭代对象的__next()__方法去取值,而且for循环会捕捉StopIteration异常,以终止迭代.

l = [1, 2, 3]
h = l.__iter__()  # 第一步调用__iter__()方法转换成可迭代对象
print(h.__next__())  # 转换成迭代对象后必有__next__()方法，调用__next__()方法去取值
print(h.__next__())
print(h.__next__())
print(h.__next__())  # 当没有值后会抛出StopIteration异常

# 1
# 2
# 3
# Traceback (most recent call last):
#   File "E:/4000hours/python/chapter-V-6/ch6-V-01.py", line 10, in <module>
#     print(h.__next__())
# StopIteration

# 上述展开等价于下面for循环工作方式
for h in l:
    print(h)