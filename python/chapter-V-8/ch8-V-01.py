
# 生成器的应用

def producer():
    ret = []
    print('生产的包子')
    for i in range(100):
        ret.append(i)
    return ret


def counsumer(res):
    for index, baozi in enumerate(res):
        print('第%s包子,吃%s' % (index, baozi))


t = producer()
counsumer(t)
# 为顺序执行,无法并发.包子都先生产好了无法做到来一个人给他做一个包子
