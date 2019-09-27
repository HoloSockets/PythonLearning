# -*- coding:utf-8 -*-


def welcome_python(hope):
    def welcome(member_name):
        print('你好，%s，%s' % (member_name, hope))

    return welcome


name = welcome_python('希望你能坚持下去!')
print('name代表的函数是：', name)
name('Grace')

# del welcome_python

name('Kim')

print('-------------------------------------------')
print('创建另外一个场景，也就是不同的祝福语')

name_2 = welcome_python('希望你的Python之路越来越好')

print('name_2代表的是：', name_2)

name_2('Grace')
name_2('Kim')

# __closure__属性
print('===============================================================')
print('查看name的属性')
print('有以下属性：\n', dir(name))
print('如果是闭包则返回一个元组：', name.__closure__)
print('name_1保存的自由变量的值是：', name.__closure__[0].cell_contents)
print()
print('查看name_2的属性')
print(dir(name_2))
print(name_2.__closure__)
print('name_2保存的自由变量的值是：', name_2.__closure__[0].cell_contents)
print('', name_2.__name__)
print('', name_2.__class__)
