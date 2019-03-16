def mySqrt(x: int) -> int:
    def guess(mid):
        return mid * mid <= x

    lo = 0
    hi = x + 1
    ans = 0
    while lo < hi:
        mid = (lo + hi) // 2
        if guess(mid):
            ans = mid
            lo = mid + 1
        else:
            hi = mid

    return ans

print(mySqrt(231234))
