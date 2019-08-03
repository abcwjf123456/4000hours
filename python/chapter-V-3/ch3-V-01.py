# 作用域
# 为什么还会有None呢？
# 因为不指定return返回值的前提下return默认返回None
# 返回地址实例看ch3-v-02
def test01():
    print('test01')


def test():
    print('test')
    # 返回的为函数地址
    return test01


res = test()
print(res())

# test
# test01
# None
