# 让实参变成可选
# 可以将形参指定一个默认值--空字符
# 形参默认值需要放到最后
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

# Jimi Hendrix
# John Lee Hooker
