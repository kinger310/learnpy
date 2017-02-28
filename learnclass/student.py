# -*- coding: utf-8 -*-


class Student(object):
    """A simple example class"""
    i = 12345

    def f(self):
        return 'Hello, world'

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print("%s:%s" % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

# bart = Student('Bart Simpson', 59)

# %%
# Function defined outside the class


def f1(self, x, y):
    return min(x, x+y)


class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g

# %% Methods may call other methods by using method attributes
#    of the self argument


class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)

# %% Inheritance
"""
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
"""
issubclass(int, object)
issubclass(int, bool)
issubclass(int, int)
issubclass(bool, int)
"""
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
"""
# %% Private Variables


class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method


class MappingSubclass(Mapping):
    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)






