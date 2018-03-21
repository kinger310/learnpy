#!/usr/bin/env/python
# coding=utf-8

cafe = bytes('café', encoding='utf_8')

city = 'São Paulo'
city.encode('cp437', errors='replace')

octets = b'Montr\xe9al'
octets.decode(encoding='utf-8')
octets.decode('cp1252')
octets.decode('utf-8', errors='replace')

u16 = 'El Niño'.encode('utf_16')


import unicodedata
def shave_marks(txt):
    """去掉全部变音符号"""
    norm_txt = unicodedata.normalize('NFD', txt)
    shaved = ''.join(c for c in norm_txt
                     if not unicodedata.combining(c))
    return unicodedata.normalize('NFC', shaved)

order = '“Herr Voß: • ½ cup of OEtker™ caffè latte • bowl of açaí.”'
shave_marks(order)

import locale
locale.setlocale(locale.LC_COLLATE, 'zh_CN.utf-8')
a = ['啊', '仨', '仁']
so = sorted(a, key=locale.strxfrm)

from bisect import bisect


def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect(breakpoints, score)
    return grades[i]

[grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]

import random
import bisect
SIZE = 7
random.seed(1)
my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE*2)
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)

l = [28, 14, '28', 5, '9', '1', 0, 6, '23', 19]
import collections
collections.UserDict()

class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]
    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default
    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()
a = StrKeyDict0()
a[1]

import collections
class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]
    def __contains__(self, key):
        return str(key) in self.data
    def __setitem__(self, key, item):
        self.data[str(key)] = item


from types import MappingProxyType
d = {1:'A'}
d_proxy = MappingProxyType(d)
d_proxy[2] = 'x'  # Error
d[2] = 'B'
d_proxy

