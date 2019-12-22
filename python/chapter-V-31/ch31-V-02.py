class A:
    def __call__(self, *args, **kwargs):
        print("call")
        print(kwargs)
        print(args)


# r1 = A(1)
# r1(1)

