class Da:
    def __getattr__(self, item):
        print("你调用的属性不存在%s" % item)
        return 0


r1 = Da()
print(r1.cc)
