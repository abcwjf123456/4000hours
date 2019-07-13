# 元组(不可变的列表叫元组但给元组变量赋值是合法的)
dimensions = (20, 100)
print(dimensions[0])
dimensions = (10, 100)  # 赋值操作
for dimension in dimensions:  # 遍历
    print(dimension)

# 20
# 10
# 100
