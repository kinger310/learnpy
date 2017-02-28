# -*- coding: utf-8 -*-

# %% generator


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

for n in fib(6):
    print(n)

# %% map


def f(x):
    return x*x
a = range(1, 11)
r = map(f, a)
list(r)

list(map(str, a))

# %% filter


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)
# 打印100以内的素数:
for n in primes():
    if n < 200:
        print(n)
    else:
        break

# %% 回文数


def is_palindrome(n):
    a = list(str(n))
    return list(reversed(a)) == a
output = filter(is_palindrome, range(1, 1000))
print(list(output))

# %% sorted

sorted([36, 5, -12, 9, -21], key=abs)
sorted(['bob', 'about', 'Zoo', 'Credit'])
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
sorted(L, key=lambda x: x[0])
sorted(L, key=lambda x: x[1], reverse=True)

# %%


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print('2015-3-25')
