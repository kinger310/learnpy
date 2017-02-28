# -*- coding: utf-8 -*-

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed

'orange' in basket                 # fast membership testing

'crabgrass' in basket


# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
a                                  # unique letters in a

a - b                              # letters in a but not in b

a | b                              # letters in either a or b

a & b                              # letters in both a and b

a ^ b                              # letters in a or b but not both

# set comprehesions

a = {x for x in 'abracadabra' if x not in 'abc'}
a


# %% dictionary
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel

tel['jack']

del tel['sape']
tel['irv'] = 4127
tel

list(tel.keys())

sorted(tel.keys())

'guido' in tel

'jack' not in tel
# dict() constructor builds dictionaries directly
# from sequences of key-value pairs
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

{x: x**2 for x in (2, 4, 6)}

dict(sape=4139, guido=4127, jack=4098)

# %% Looping Techniques
from collections import Iterable
isinstance('abc', Iterable)
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
# 对list实现类似Java那样的下标循环
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

for i in reversed(range(1, 10, 2)):
    print(i)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

filtered_data

import os
[d for d in os.listdir(path='.')]
