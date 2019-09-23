# -*- coding:utf-8 -*-

class Animal(object):
    def run(self):
        print('Animal is running...')

    def run_twice(self):
        self.run()
        self.run()


class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')

    def eat(self):
        print('Eating fish...')


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')


class Timer(object):
    def run(self):
        print('Start...')


def run_twice(animal):
    animal.run()
    animal.run()

dog = Dog()
dog.run()

cat = Cat()
cat.run()

a = list()
b = Animal()
c = Dog()

print(isinstance(a, list))
print(isinstance(b, Animal))
print(isinstance(c, Dog))
print(isinstance(c, Animal))

dog.run_twice()
cat.run_twice()

tortoise = Tortoise()

tortoise.run_twice()

timer = Timer()

run_twice(timer)
