class People:
    def __init__(self, name, age):
        print('开始')
        self.name = name
        self.age = age
        print('结束')
    def uu(self):
        print(self)
        print("yugygy %s" %self.name)


p1 = People("yt", 13)
print(p1)
print(p1.uu())
# self就是实例本身
print(dir(p1))
print(p1.__dict__)