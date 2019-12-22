class A:
    def __init__(self, a=0, b=1):
        self._a = a
        self._b = b

    def __next__(self):

        self._a, self._b = self._b, self._a + self._b
        return self._a


r1 = A()
print(r1.__next__())
print(r1.__next__())
print(r1.__next__())
print(r1.__next__())
print(r1.__next__())
print(r1.__next__())
print(r1.__next__())
