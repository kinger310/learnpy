# -*- coding: utf-8 -*-


class Animal(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称

    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')

# %%


def run_twice(animal):
    animal.run()
    animal.run()

a = Animal()
d = Dog()
c = Cat()

run_twice(d)
run_twice(c)

isinstance(c, Animal)
isinstance(a, Cat)

a.sex = 'male'
d.sex = 'male'

# %% 动态语言
# 动态绑定属性
d.sex = 'male'
setattr(d, 'age', '2')  # setattr(x, 'y', v) is equivalent to ``x.y = v''
Dog.sex = None
d = Dog()
print(d.sex)

# 动态绑定方法


def walk(self):
    print("Animal is walking...")


Animal.walk = walk
import types
Animal.walk = types.MethodType(walk, Animal)

