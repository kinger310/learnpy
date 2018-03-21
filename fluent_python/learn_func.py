import random


def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)
fac = factorial
[fac(n) for n in range(10)]

class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)
    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')
    def __call__(self):
        return self.pick()
# bingo.pick() 的快捷方式是 bingo()

def clip(text, max_len=80):
    """在max_len前面或后面的第一个空格处截断文本
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
        if space_after >= 0:
            end = space_after
    if end is None: # 没找到空格
        end = len(text)
    return text[:end].rstrip()
from inspect import signature
sig = signature(clip)
for name, para in sig.parameters.items():
    print(para.kind, name, '=', para.default)

from functools import reduce
def fact(n):
    return reduce(lambda a, b: a * b, range(1, n + 1))

def deco(func):
    def inner():
        print('running inner')
    return inner

@deco
def target():
    print('running target')


registry = []
def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func

@register
def f1():
    print('running f1()')
@register
def f2():
    print('running f2()')
def f3():
    print('running f3()')
def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()

if __name__=='__main__':
    main()


def make_averager():
    series = []

    def average(new_value):
        series.append(new_value)  # series是自由变量
        total = sum(series)
        return total / len(series)
    return average

avg = make_averager()
avg(10)
avg(11)
avg(12)

avg.__code__.co_freevars
avg.__code__.co_varnames
avg.__closure__
avg.__closure__[0].cell_contents

def make_averager():
    count = 0
    total = 0
    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager

from fluent_python.clockdeco import clock
import time

@clock
def snooze(sec):
    time.sleep(sec)

@clock
def fac(n):
    return 1 if n < 2 else n * fac(n-1)

if __name__ == '__main__':
    snooze(.123)
    print('6! = ', fac(6))


def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)

### 单分派泛函数 singledispatch
from functools import singledispatch
from collections import abc
import numbers
import html

@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)

# singledispatch 创建一个自定义的htmlize.register 装饰器，
# 把多个函数绑在一起组成一个泛函数
@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{0}</p>'.format(content)

@htmlize.register(numbers.Integral)
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)

@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n<ul>'




