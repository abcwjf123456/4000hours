# 私有属性
class Da:
    _gg = 1
    __hh = 3

    def jj(self):
        print('jj')


r1 = Da()
print(dir(r1))
print(r1._gg)
print(r1._Da__hh)
