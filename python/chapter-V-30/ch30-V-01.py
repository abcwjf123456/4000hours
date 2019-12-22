def gg(fun):
    print("函数")
    fun.name=1
    return fun


@gg  # A=gg(A)
class A:
    def __init__(self):
        pass


r1 = A()
print(r1.__dict__)
