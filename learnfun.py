# -*- coding: utf-8 -*-

# %% Defining functions


def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result

f100 = fib2(100)    # call it
f100                # write the result

# %% Default Argument Values


def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))


def f1(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


# %% Keyword Arguments


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# %% Arbitrary Argument Lists


def concat(*args, sep="/"):
    return sep.join(args)

concat("earth", "mars", "venus")
concat("earth", "mars", "venus", sep=".")

# %% Unpacking Argument Lists


def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "action": "VOOM",
     "state": "bleedin' demised"}
parrot(**d)

# %% Lambda Expressions


def make_incrementor(n):
    return lambda x: x + n
f = make_incrementor(42)
f(1)


pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
pairs

sorted([1, 2, 3, 4, 5, 6, 7, 8, 9], key=lambda x: abs(5-x))


# %% Documentation Strings


def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)

# %% Function Annotations


def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')
