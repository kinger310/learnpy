# -*- coding: utf-8 -*-

try:
    f = open(r'test.txt', 'r')
    print(f.read())
except IOError as e:
    print('IOError:', e)
finally:
    if f:
        f.close()

from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

import os
[x for x in os.listdir('.') if os.path.isdir(x)]
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']

# 序列化

import pickle
d = dict(name='Bob', age=20, score=88)
pickle.dumps(d)

f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()

import json
d = dict(name='Bob', age=20, score=88)
json_str = json.dumps(d)

json.loads(json_str)


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

s = Student('Bob', 20, 88)
print(json.dumps(s, default=student2dict))

print(json.dumps(s, default=lambda obj: obj.__dict__))

