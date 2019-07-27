# 结合使用函数和while循环
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()


while True:
    print('输入你的名字')
    print('输入q退出')
    f_name = input('first_name')
    if f_name == 'q':
        break
    l_name = input('last_name')
    if l_name == 'q':
        break

    formatte_name = get_formatted_name(f_name, l_name)
    print(formatte_name)
