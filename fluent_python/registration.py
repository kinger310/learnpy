registry = set()


def register(active=True):
    def decorate(func):
        print('Running register(active=%s) -> decorate(%s)' % (active, func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)
        return func

    return decorate


@register(active=False)
def f1():
    print('running f1')


@register()
def f2():
    print('running f2')


def f3():
    print('running f3')


from fluent_python.registration import *
register()(f3)
print(registry)
register(active=False)(f2)
print(registry)

def make_averager():
    series = []
    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)
    return averager