class Da:
    def __init__(self):
        pass

    def __setattr__(self, key, value):
        # 设置属性时会触发
        # self.key=value # 这个是错误的会出现无限循环
        self.__dict__[key] = value # 用操作底层字典的方式才不会出现无限循环

    def __getattr__(self, item):
        # 经常用这
        # 只在属性不存在会触发
        print("get")

    def __delattr__(self, item):
        # 删除某个属性会触发
        self.__dict__.pop(item)



r1 = Da()
print(r1.x)

# print(dir(r1))
# __setattr__
# __delattr__
# __getattr__
