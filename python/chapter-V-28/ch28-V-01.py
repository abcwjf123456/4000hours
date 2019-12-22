class A:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print("enter执行")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit执行")


with A("a.txt") as f:
    print("tff")
    print(f.name)
