from functools import wraps
def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print('Calling decorated function')
        return f(*args, **kwds)
    return wrapper

@my_decorator
def example():
    """Docstring"""
    print('Called example function')

example()


example.__name__
'''
when remove @wraps(f), 
example.__name__ returns 'wrapper'
example.__doc__ returns None
'''

example.__doc__