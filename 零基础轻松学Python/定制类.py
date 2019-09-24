# -*- coding:utf-8 -*-


class Student(object):
    def __init__(self, name):
        self.name = name

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

    def __str__(self):
        return 'Student object (name:%s)' % self.name

    __repr__ = __str__

    def __call__(self):
        print('My name is %s' % self.name)


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration
        return self.a

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


s = Student('Michael')
print(s)

# for n in Fib():
#     print(n)

f = Fib()

# for i in range(10):
#     print(f[i])

print(f[:10:2])

print(s.score)
print(s.age())

print(Chain().status.user.timeline.list)

s()

print('Student is callable:', callable(Student('lisa')))
print('max is callable:', callable(max))
print('[1,2,3] is callable:', callable([1, 2, 3]))
print('None is callable:', callable(None))
print('\'str\' is callable:', callable('str'))

# __str__ print()函数调用时调用
# __repr__ 直接打印对象时调用
# __iter__  for in 中使用 迭代对象
# __getitem__ 可以通过索引访问 制作切片功能
# __getattr__ 当属性没有定义时，在这个方法下查找
# __call__ 让实例可以直接被调用，变成和函数一样

