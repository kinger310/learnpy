# 279. Perfect Squares
# Given a positive integer n, find the least number of perfect square numbers
# (for example, 1, 4, 9, 16, ...) which sum to n.
#
# Example 1:
#
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
# Example 2:
#
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
import math

def numSquares(n: int) -> int:
    dp = [n] * (n+1)
    dp[0] = 0
    for i in range(1, n+1):
        # if i == n:
        #     print("ok")
        j = 1
        tmp = j*j
        while tmp <= i:
            dp[i] = min(dp[i-tmp]+1, dp[i])
            j += 1
            tmp = j * j
    # print(dp)
    return dp[n]

# print(numSquares(7929))
print(numSquares(25))
