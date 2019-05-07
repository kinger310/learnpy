# 343. Integer Break
# Given a positive integer n, break it into the sum of at least two positive integers
# and maximize the product of those integers. Return the maximum product you can get.
#
# Example 1:
#
# Input: 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.
# Example 2:
#
# Input: 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
# Note: You may assume that n is not less than 2 and not larger than 58.


def integerBreak(n: int) -> int:
    if n <= 2:
        return 1
    if n == 3:
        return 2
    p, q = divmod(n, 3)
    if q == 0:
        res = 3**p
    elif q== 1:
        res = (3**(p-1))*4
    else:
        res = (3**p)*2
    return res


print(integerBreak(58))