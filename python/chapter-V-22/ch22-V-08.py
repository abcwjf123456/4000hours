# 继承
# 没有覆盖一说子类会先找自己的属性然后没有就去找父类的
class Da:
    money = 1

    def __init__(self, name):
        self.name = name

    def dd(self):
        print("yftft")


class Son(Da):
    money = 11

    def __init__(self):
        pass


r1 = Da("gg")
print(Son.money)
Son.dd(r1)
