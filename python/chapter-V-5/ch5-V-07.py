# max mix简单玩法
# l = [1, 2, 3]
# print(max(l))
# print(min(l))
# 3
# 1
# max mix高端玩法
# 先比较第一个值第一个比较出来后直接出结果无须在比较，max会for循环遍历每个元素在比较
people = [
    {'name': 'fg', 'age': 1000},
    {'name': 'hh', 'age': 1000}
]
print(max(people, key=lambda item: item['age']))
# max(people)会对people进行for循环然后将值传给item，lambda将age值取出来进行比较
