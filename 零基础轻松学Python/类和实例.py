# -*- coding:utf-8 -*-
class Student(object):
    def __init__(self, name, score, gender):
        self.__name = name
        self.__score = score
        self.__gender = gender

    def print_score(self):
        print('%s:%s' % (self.__name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender == 'female' or gender == 'male':
            self.__gender = gender
        else:
            raise ValueError('bad gender')


lisa = Student('Lisa', 99, 'female')
bart = Student('Bart', 59, 'male')

print(lisa.get_name(), lisa.get_grade())
print(bart.get_name(), bart.get_grade())

print(bart.get_gender())
print(lisa.get_gender())

lisa.set_gender('male')

print(lisa.get_gender())

