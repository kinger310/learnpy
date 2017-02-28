# -*- coding: utf-8 -*-


try:
    print('start...')
    r = 10 / int('2')
    print('result', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError', e)
else:
    print('No Error!')
finally:
    print('finally...')
print('End')

# %%
# err_logging.py

import logging


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')

# %%
# err_raise.py


class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n


foo('0')

