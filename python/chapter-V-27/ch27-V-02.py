class A:
    def __init__(self, value, value1):
        self.value = value
        self.value1 = value1

    # def __format__(self, format_spec):
    #
    #     pass


r1 = A(5, 3)
print("值为:{0.value},第二个值为:{0.value1}".format(r1))
