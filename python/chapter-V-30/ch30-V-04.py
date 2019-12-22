def ff(**kwargs):
    def gg(func):
        for key, value in kwargs.items():
            setattr(func, key, value)
        return func

    return gg


@ff(name=str, age=int)
class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# r1 = A("ggh", 11)
# print(A.__dict__)
