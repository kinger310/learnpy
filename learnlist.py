# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 23:31:09 2017

@author: Wangdi
"""

# %%
'''5.1.3. List Comprehensions 列表推导式'''
[(x, y) for x in [1, 2, 3] for y in [2, 3, 4] if x != y]

vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
[x*2 for x in vec]
# Answer:[-8, -4, 0, 4, 8]
# filter the list to exclude negative numbers
[x for x in vec if x >= 0]
# Answer:[0, 2, 4]
# apply a function to all the elements
[abs(x) for x in vec]
# Answer:[4, 2, 0, 2, 4]
# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]
# Answer:['banana', 'loganberry', 'passion fruit']
# create a list of 2-tuples like (number, square)
[(x, x**2) for x in range(6)]
# Answer:[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
# flatten a list using a listcomp with two 'for'
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[num for elem in vec for num in elem]

# %%
'''5.1.4. Nested List Comprehensions'''
# 3 methods
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], ]
[[row[i] for row in matrix] for i in range(4)]

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

transposed

list(zip(*matrix))

