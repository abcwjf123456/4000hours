# class Meta_Type(type):
#     def __call__(self, *args, **kwargs):
#         # self是Meta_Type的实例，也就是Foo
#         # 因为每个类都默认继承object，所以可以调用__new__(Foo)方法，来实例化一个对象f1 == object.__new__(Foo)  ==> f1
#         obj = object.__new__(self)
#
#         # 调用Foo的构造函数实例化对象 == Foo.__init__(f1,*args,**kwargs)
#
#        self.__init__(obj, *args, **kwargs)
#
#     # 最后要返回f1这个对象
#     return obj
#
# metaclass = Meta_Type  ====> 会触发Foo = Meta_Type(Foo,'Foo',(),{})   ===>会触发Meta_Type的 __init__
# class Foo(metaclass=Meta_Type):
#     def __init__(self, name):
#         self.name = name
#
#     # 当Foo()时，表示执行了Foo，则会调用元类的__call__,__call__中会生成对象f1，并且调用Foo下的__init__方法，最终完成实例化
#
#
# f1 = Foo('Menawey')
# # >>>我是元类
# print(f1.__dict__)
# # >>>{'name': 'Menawey'}
