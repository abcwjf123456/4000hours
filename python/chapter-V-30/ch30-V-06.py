class A:
    def __init__(self, fun):
        print("hh")
        self.fun = fun

    def __get__(self, instance, owner):
        print(instance)
        print(owner)
        res = self.fun(instance)
        return res


class B:
    x = A("x")

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @A  # addj=A(addj)
    def addj(self):
        return self.width * self.height


r1 = B(1, 1)
print(r1.addj)
