def splitArray(nums: 'List[int]', m: 'int') -> int:
    def guess(mid):
        s = 0
        mm = 1
        for num in nums:
            if num > mid:
                return False
            if s + num > mid:
                mm += 1
                s = num
            else:
                s += num
        return mm <= m

    lo = 0
    hi = sum(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if guess(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo

# print(splitArray([9, 7,8], 3))
print(splitArray([7,2,5,10,8], 2))


# 二分法与单调性有密切联系。
# 原题是当给定m时,求尽量最小的partition中的和的最大值.
# 我们可以先求当partition已经做好,m值最小是多少