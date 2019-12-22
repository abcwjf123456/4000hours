class A:
    pass


class B(A):
    pass


r1 = B()
print(isinstance(r1, B))
print(isinstance(r1, A))
