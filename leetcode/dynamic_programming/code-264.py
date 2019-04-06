# 264. Ugly Number II
# Write a program to find the n-th ugly number.
#
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
#
# Example:
#
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
# Note:
#
# 1 is typically treated as an ugly number.
# n does not exceed 1690.

def nthUglyNumber(n: int) -> int:
    dp = [0] * n
    dp[0] = 1
    t2 = t3 = t5 = 0
    for i in range(1, n):
        f2, f3, f5 = dp[t2]*2, dp[t3]*3, dp[t5]*5
        dp[i] = min(f2, f3, f5)
        if dp[i] == f2:
            t2 += 1
        if dp[i] == f3:
            t3 += 1
        if dp[i] == f5:
            t5 += 1
    return dp[-1]


print(nthUglyNumber(10))

