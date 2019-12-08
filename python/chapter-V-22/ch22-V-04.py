class Popff:
    cong = "预估费用"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def ff(self):
        print(self.cong)


p1 = Popff("与他", 13)
print(p1.cong)
p1.ff()
