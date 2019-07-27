# while循环处理列表和字典
# pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
# 首先，创建一个待验证用户列表
# 和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# 验证每一个用户，直到没有未验证用户为止
# 将每一个经过验证的列表移到已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print('Verifying users: ' + current_user.title())
    confirmed_users.append(current_user)
# 显示所有已验证的用户
print("\nThe following users have been confirmed")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

    # Verifying users: Candace
    # Verifying users: Brian
    # Verifying users: Alice
    #
    # The following users have been confirmed
    # Candace
    # Brian
    # Alice
