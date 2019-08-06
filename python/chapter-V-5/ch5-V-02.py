# filter函数
# filter返回的是一个迭代器对象
mum_1 = ['li_gyftgy', 'li_jj', 'fgfg']


def filter_test(func, x):
    ret = []
    for i in x:
        if func(i):
            ret.append(i)
    return i


print(list(filter_test(lambda k: not k.startswith('li'), mum_1)))

print(list(filter(lambda k: not k.startswith('li'), mum_1)))

# ['f', 'g', 'f', 'g']
# ['fgfg']
