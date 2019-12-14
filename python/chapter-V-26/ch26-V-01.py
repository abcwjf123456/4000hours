# List继承原生列表list
# 实现授权是包装的一个特性。包装一个类型通常是对已存在的类型进行一些自定义定制，
# 这种做法可以新建，修改，或删除原有产品的某些功能，而其他的保持不变。
# 授权的过程，其实也就是所有的更新功能都交给新类的自定义的某部分功能来处理，但已存在的功能就授权给对象的默认属性。
class List(list):
    def append(self, p):
        if type(p) == str:
            # 用父类添加
            # list.append(self, p)
            super().append(p)
        else:
            print('必须是字符串')

    def show_mid(self):
        l = int(len(self) / 2)
        print(self[l])


arr = List('hello')
print(arr)
arr.show_mid()
arr.append('911')
arr.append(110)
print(arr)
'''
['h', 'e', 'l', 'l', 'o']
l
必须是字符串
['h', 'e', 'l', 'l', 'o', '911']
'''
