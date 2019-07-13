# 复制列表

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods  # 注意
print(my_foods)
print(friend_foods)
my_foods.append('cannoli')
friend_foods.append('ice cream')
print(my_foods)
print(friend_foods)
# ['pizza', 'falafel', 'carrot cake']
# ['pizza', 'falafel', 'carrot cake']
# ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
# ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
# 由输出结果可知复制的是同一列表并没有重新复制到新列表


# 正确操作
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]  # 注意
print(my_foods)
print(friend_foods)
my_foods.append('cannoli')
friend_foods.append('ice cream')
print(my_foods)
print(friend_foods)

# ['pizza', 'falafel', 'carrot cake']
# ['pizza', 'falafel', 'carrot cake']
# ['pizza', 'falafel', 'carrot cake', 'cannoli']
# ['pizza', 'falafel', 'carrot cake', 'ice cream']
# 由输出可知复制了新的列表
