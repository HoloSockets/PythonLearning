# -*- coding:utf-8 -*-

from collections.abc import Iterable, Iterator

name_dictionary = {'皇妃': 300,
                   '皇后': 1000,
                   '皇贵妃': 800,
                   '贵妃': 600,
                   '嫔': 200}

print('  ')
print('各个级别的嫔妃是：')
for key in name_dictionary.keys():
    print(key)

print('使用isinstance()函数判断字典是不是可迭代对象', isinstance(name_dictionary, Iterable))
print('使用isinstance()函数判断字典是不是迭代器', isinstance(name_dictionary, Iterator))