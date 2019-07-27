# 在字典中存储字典
user = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    }
}
for name, user_info in user.items():
    print(name)
    print(user_info['first'])
