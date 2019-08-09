# zip返回为一个对象
print(list(zip(('a', 'b', 'c'), (1, 2, 3))))
# [('a', 1), ('b', 2), ('c', 3)]
l = {'a': 1, 'b': 2}
print(list(zip(l.keys(), l.values())))
# [('a', 1), ('b', 2)]
