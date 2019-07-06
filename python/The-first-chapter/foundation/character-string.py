# 字符串
# name="ada lovelace"
# print(name.title())
# 输出结果Ada Lovelace
# title()方法以首字母大写的方式显示每个单词


# name="ada Lovelace"
# print(name.upper())
# print(name.lower())
# upper()全部大写
# lower()全部小写
# 输出结果 ADA LOVELACE
# 输出结果 ada lovelace 存储数据时，lower()很有用


# 拼接字符串
# first_name="ada"
# last_name="lovelace"
# print(first_name+" "+last_name)

# print("ada"+" "+"lovelace")
# 输出ada lovelace

# first_name="ada"
# last_name="lovelace"
# full_name=first_name+" "+last_name
# print(full_name.title())
# 输出Ada Lovelace

# message= "Hello"+" "+full_name.title()
# print(message)
# 输出Hello Ada Lovelace


# 制表符\t 换行符\n 我百度了一下好像公认的先换行后制表并未有对此的解释
# print("\t python")
# print("languages:python javascript")
# print("languages:\n\t python\n\t javascript")
# print("languages:\t\n python\t\n javascript")
# 输出
# 	python

# languages:python javascript

# languages:
# 	python
# 	javascript

# languages:
# python
# javascript

# for i in range(5):
    # print(i)
    # print(i,end='')# 结束换行
    # print(i, end='\t')# 结束换行并且制表符
    # print(f'\t{i}')# 另一种输出方式
    # print(f'\n{i}')# 另一种输出方式
# 输出
# 0
# 1
# 2
# 3
# 4

# 01234

# 0	 1	2	3	4

#   0
#   1
#   2
#   3
#   4


# 0
#
# 1
#
# 2
#
# 3
#
# 4



# 删除空白
# 只能在python编译器中能清楚看到末尾空白被删除了并且删除不是永久的，如果要在pycharm中看到直接将鼠标放在输出面板中
# favorite_language='python '
# print(favorite_language)
# print(favorite_language.rstrip())

# 永久性删除 及将新值存放在原来的变量中
# favorite_language='python '
# favorite_language=favorite_language.rstrip()
# print(favorite_language)

# 删除开头空白lstrip(),同时两端空白strip()
# favorite_language=' python '
# favorite_language=favorite_language.lstrip()
# favorite_language=favorite_language.strip()
# print(favorite_language)

# 字符串语法错误 编译器会报错所以注意即可
# message="one of python's strengths"
# print(message)

# message='one of python's strengths'
# print(message)





