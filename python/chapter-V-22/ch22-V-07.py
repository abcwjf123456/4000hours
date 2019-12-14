# 静态方法
# 静态方法不能调实例变量与类变量只是类的工具包
# 组合已经练习过有问题百度
class A():
    bar = 1

    def __init__(self, a):
        self.a = a

    def foo(self):
        print('foo')

    @staticmethod
    def static_foo():
        print('static_foo')
        print(A.bar)
        print(r1.a)

    @classmethod
    def class_foo(s):
        print('class_foo')
        print(s.bar)
        print(r1.a)

    def cl(a):
        print("ytft%s" % a)


# A.cl(2)
# A.class_foo()
# A.static_foo()
r1 = A(2)
r1.static_foo()
r1.class_foo()
