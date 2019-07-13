# 创建数字列表
for value in range(5):
    print(value)
for value01 in range(1, 5):
    print(value01)
for value02 in range(1, 7, 3):
    print(value02)

# 转换成列表 list() 方法用于将元组或字符串转换为列表
numbers = list(range(5))
print(numbers)

# [0, 1, 2, 3, 4]

squares = []
for value03 in range(1, 11):
    square = value03 ** 2
    squares.append(square)
print(squares)

# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
