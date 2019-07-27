# 使用用户输入来填充字典
resposes = {}
poling_active = True

while poling_active:
    # 提示被调查人的名字和回答
    name = input('输入名字')
    respose = input('跟谁去爬山')

    # 存储到字典
    resposes[name] = respose

    # 看看还有人想调查吗
    repeat = input('还有人要调查吗输入yes/no')
    if repeat == 'no':
        poling_active = False

# 调查结束，显示结果
for name, respose in resposes.items():
    print(name + '和' + respose + '爬山')
