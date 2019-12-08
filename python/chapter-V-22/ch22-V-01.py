class People:
    def __init__(self, name, age):
        print('开始')
        self.name = name
        self.age = age
        print('结束')


p1 = People("yt", 13)
print(p1.__dict__)
print(p1.name)
print()
# 实例化后__init__会自动运行自动return self

# print(p1.age)
# 开始
# 结束
# {'name': 'yt', 'age': 13}
