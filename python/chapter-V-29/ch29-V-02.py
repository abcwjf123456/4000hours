class MyDescriptor:
    def __get__(self, instance, owener):
        print('getting...', self, instance, owener)

    def __set__(self, instance, value):
        print('settiong...', self, instance, value)

    def __delete__(self, instance):
        print('deleting...', self, instance)


class Test:
    x = MyDescriptor()


test = Test()
print(test.x)
