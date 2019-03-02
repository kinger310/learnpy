cache = {}
def fib(n):
    if n in cache:
        return cache[n]
    if n < 2:
        return n

    result = fib(n-1)+fib(n-2)
    cache[n] = result

    return result

print(fib(7))
