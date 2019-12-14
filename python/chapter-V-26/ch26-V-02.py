# 授权:授权是包装的一个特性,包装一个类型通常是对已存在的类型的一些定制
# 这种方法,可以新建,修改或删除原有产品的功能,其他的则保持原样,授权的过程,及是所有更新的功能都是由新类
# 的某部分来处理,但已存在的功能就授权给对象的默认属性


# 实现授权的关键点是覆盖__getattr__方法
import time


class Filehandle():
    def __init__(self, filename, mode="r", encoding="utf-8"):
        self.mode = mode
        self.filename = open(filename, mode, encoding=encoding)
        self.encoding = encoding

    # def read(self):
    #     pass
    #
    # def write(self):
    #     pass

    def write(self,line):
        # print("----------->",line)
        t=time.strftime("%Y-%m-%d %X")
        self.filename.write(("%s %s"%(t,line) ))

    def __getattr__(self, item):
        print(item, type(item))
        return getattr(self.filename, item)  # self.filename 内存地址  item(read方法 str类型)


f1 = Filehandle("a.text", "w+", "utf-8")

# print(f1.filename)
# print(f1.__dict__)
# print(type(f1.read()))#触发__getattr__


f1.write("11\n")
f1.write("cpu负载过高\n")
f1.write("内存剩余不足\n")
f1.write("硬盘剩余不足\n")

f1.seek(0)
print(f1.read())

# sys_f=open("b.text","w")
# print(getattr(sys_f,"read"))
