
# 内置函数
print(chr(89))  # 数字找到ascii码对应字母
print(ord('a'))  # 字母找到ascii码对应数字
# Y
# 97
print(pow(2, 2))  # 2**2
print(pow(2, 2, 2))  # 2**2/2
# 4
# 0
l = [1, 2, 3]
print(list(reversed(l)))  # 反转不会保存
print(l)
# [3, 2, 1]
# [1, 2, 3]
l = 'hello'
s1 = slice(3, 5)  # slice提前做好切片
print(l[s1])
# lo

# sorted()排序与max一样
# str eval对立
