# -*- coding:utf-8 -*-


class Student(object):
    name = 'Student'

    # def __init__(self, name):
    #     self.name = name


# s = Student('Bob')
# s.score = 90
# print(s.name, s.score)

s = Student()
print('s.name:', s.name)
print('Student.name:', s.name)

s.name = 'Michael'
print('s.name:', s.name)
print('Student.name:', Student.name)

del s.name
print('s.name:', s.name)
