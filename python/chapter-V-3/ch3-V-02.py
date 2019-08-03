# 返回的内存地址

def test01():
    print('jhhj')


def test():
    print('hgh')
    # 拿到的是test01的内存地址
    return test01


res = test()
print(res)


# hgh
# <function test01 at 0x02B02078>