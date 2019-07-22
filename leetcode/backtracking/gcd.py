# 辗转相除法，时间复杂度O(logN)
def gcd(x, y):
    return x if y == 0 else gcd(y, x%y)

print(gcd(60, 576))


# 扩展欧几里得算法
def exgcd(a, b):
    if b == 0:
        return 1, 0, a
    x, y, r = exgcd(b, a%b)
    x, y = y, x - a//b * y
    return x, y, r

print(exgcd(17, 3120))
