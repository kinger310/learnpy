# 辗转相除法，时间复杂度O(logN)
def gcd(x, y):
    return x if y == 0 else gcd(y, x%y)

print(gcd(60, 576))