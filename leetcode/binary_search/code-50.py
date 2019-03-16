# # 快速幂
#
# Example 1:
#
# Input: 2.00000, 10
# Output: 1024.00000
# Example 2:
#
# Input: 2.10000, 3
# Output: 9.26100
# Example 3:
#
# Input: 2.00000, -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25
#

# when n 是自然数
# 倍增法， 快速幂
def myPow1(x: float, n: int) -> float:
    if n == 0:
        return 1
    A = myPow1(x, n // 2)
    if n % 2 == 0:
        return A*A
    else:
        return A*A*x


print(myPow1(2.0, 31))
