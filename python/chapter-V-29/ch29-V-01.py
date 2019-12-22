class Desc(object):
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        print("__get__...")

        print(self.name)
        print('=' * 40, "\n")


class TestDesc(object):
    x = Desc('x')

    def __init__(self):
        self.y = Desc('y')


# 以下为测试代码
t = TestDesc()
t.x
t.y
