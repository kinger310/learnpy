# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 18:37:05 2017

@author: Wangdi
"""


def hello():
    """Print "Hello world" and return None"""
    print("Hello World")

# main program starts here
hello()

"""
from __future__ import division
from sympy import symbols
from sympy import Function
x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)
expr = f(x)

"""
# %%


def hello(name):
    """Given an object 'name', print 'Hello' and the object."""
    print("Hello {}".format(name))


i = 42
if __name__ == "__main__":
    hello(i)

# %%


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
# %%


def calc(*numbers):
    s = 0
    for n in numbers:
        s = s + n * n * n
    return s

# %% for
words = ['cat', 'window', 'defenestrate']
for w in words[:]:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
