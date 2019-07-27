# 遍历字典的所有键值

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name in sorted(favorite_languages.keys()):
    # 使用for name in sorted(favorite_languages.key())输出结果是相同的但还是建议使用上因为可读性高
    # 遍历值为values()

    print(name)


# edward
# jen
# phil
# sarah