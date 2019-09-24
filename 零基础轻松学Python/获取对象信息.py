# -*- coding:utf-8 -*-

import types
import 继承和多态 as ss


class MyDog(object):
    def __len__(self):
        return 100


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


def fn():
    pass


# 使用type()
print('fn is types.FunctionType:', type(fn) == types.FunctionType)
print('abs is types.BuiltinFunctionType:', type(abs) == types.BuiltinFunctionType)
print('lambda x : x is types.LambdaType:', type(lambda x: x) == types.LambdaType)
print('x for x in range(10) is types.GeneratorType:', type(x for x in range(10)) == types.GeneratorType)

# 使用isinstance()
a = ss.Animal()
d = ss.Dog()
h = ss.Husky()

print('h is Husky:', isinstance(h, ss.Husky))
print('h is Dog:', isinstance(h, ss.Dog))
print('h is an Animal:', isinstance(h, ss.Animal))

print('d is a Dog and an Animal:', (isinstance(d, ss.Dog) and isinstance(d, ss.Animal)))

print('d is Husky:', isinstance(d, ss.Husky))

print('\'a\' is str:', isinstance('a', str))
print('123 is int', isinstance(123, int))
print('b\'a\' is bytes', isinstance(b'a', bytes))

print('[1,2,3] is list or tuple', isinstance([1, 2, 3], (list, tuple)))
print('(1,2,3) is list or tuple', isinstance((1, 2, 3), (list, tuple)))

# 使用dir()
print(dir('ABC'))

dog = MyDog()
print(len(dog))

print('ABC'.lower())

obj = MyObject()

print(hasattr(obj, 'x'))
print(hasattr(obj, 'y'))
setattr(obj, 'y', 19)
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))
print(obj.y)

print(getattr(obj, 'z', 404))

print(hasattr(obj, 'power'))
print(getattr(obj, 'power'))
fn = getattr(obj, 'power')
print(fn)
print(fn())
