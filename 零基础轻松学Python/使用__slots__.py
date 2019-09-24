# -*- coding:utf-8 -*-

from types import MethodType


class Student(object):
    __slots__ = ('name', 'age', 'score', 'set_age')


class GraduateStudent(Student):
    # 除非子类中也定义__slots__变量才能继承父类的__slots__的限制
    pass


def set_age(self, age):
    self.age = age


def set_score(self, score):
    self.score = score


# 实例绑定属性和方法
s = Student()
s.name = 'Michael'
print(s.name)

s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

# 类绑定方法
Student.set_score = set_score

s1 = Student()
s2 = Student()

s1.set_score(100)
print(s1.score)
s2.set_score(99)
print(s2.score)

# 使用__slots__
g = GraduateStudent()

g.score = 9999

print(g.score)
