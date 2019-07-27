# 遍历字典
# Python 字典 items() 方法以列表返回可遍历的(键, 值) 元组数组。


user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for k, v in user_0.items():
    # 没有items()会报错
    print(k)
    print(v)


# username
# efermi
# first
# enrico
# last
# fermi