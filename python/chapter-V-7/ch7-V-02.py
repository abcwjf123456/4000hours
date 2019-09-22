# 三元表达式
# 列表表达式

name = 'wjf'
r = '帅哥' if name == 'wjf' else '去你的'
print(r)

rs = ['鸡蛋%s' % i for i in range(10) if i <= 4]  # 非常占内存
print(rs)
