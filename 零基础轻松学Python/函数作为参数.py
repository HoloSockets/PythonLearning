# -*- coding:utf-8 -*-


def add(var1, var2):
    print('求%s与%s的和' % (var1, var2))
    return var1 + var2


def substract(var1, var2):
    print('求%s与%s的差' % (var1, var2))
    return var1 - var2


def multiplication(var1, var2):
    print('求%s与%s的积' % (var1, var2))
    return var1 * var2


def division(var1, var2):
    if var2 <= 0:
        raise TypeError('请输入正整数')
    print('求%s与%s的商' % (var1, var2))
    return var1 / var2


def arithmetic(op, op1, op2):
    result = op(op1, op2)
    return result


# 函数做参数
# print('\t', arithmetic(add, 300, 50))
# print('\t', arithmetic(substract, 300, 50))
# print('\t', arithmetic(multiplication, 300, 50))
# print('\t', arithmetic(division, 300, 50))

# 函数放在容器中
print('把四则运算放在列表中')

funcs = [add, substract, multiplication, division]

# print('使用列表的索引定位调用想要执行的函数')
# funcs[0](300, 50)
#
# print('-------------------------------')
# print('使用for循环求四则运算')
# for f in funcs:
#     print(f(300, 50))

# 使用字典存储数据集
data = {'300': 50, '400': 20, '700': 70}

print('使用函数求多个数的四则运算')


def do_func(data, ops):
    print('求下列数字的四则运算', data)
    for key, value in data.items():
        for fun in ops:
            print(fun(int(key), value))
        print('-----------------------------')


# 调用函数
do_func(data, funcs)
