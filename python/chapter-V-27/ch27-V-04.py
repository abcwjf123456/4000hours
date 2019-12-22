# 斐波那契数列
# 递归方式实现斐波那契数列
# 前n项:
#
# 复制代码
# # 递归方式实现 生成前20项
lis = []
for i in range(20):
    if i == 0 or i == 1:  # 第1,2项 都为1
        lis.append(1)
    else:
        lis.append(lis[i - 2] + lis[i - 1])  # 从第3项开始每项值为前两项值之和
print(lis)
