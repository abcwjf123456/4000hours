# 返回值
# return语句将返回值返回到调用函数的代码行

def get_formatted_name(first_name, last_name):
    """返回整洁的名字"""
    full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('gg', 'gk')
# 将返回值存储到变量musician
print(musician)


# Gg Gg
