f = open("fg", "r")
d = f.read()
print(d)
print(type(d))
h = eval(d)
print(type(h))

# {"name":"hhh"}
# <class 'str'>
# <class 'dict'>
