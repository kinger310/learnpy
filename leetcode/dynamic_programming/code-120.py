# 120. Triangle
# Given a triangle, find the minimum path sum from top to bottom.
# Each step you may move to adjacent numbers on the row below.
#
# For example, given the following triangle
#
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
#
# Note:
#
# Bonus point if you are able to do this using only O(n) extra space,
# where n is the total number of rows in the triangle.



def minimumTotal(triangle: 'List[List[int]]') -> int:
    n = len(triangle)
    if n == 0:
        return 0
    dp = [[0] * (i + 1) for i in range(n)]
    dp[0][0] = triangle[0][0]
    for i in range(1, n):
        dp[i][0] = triangle[i][0] + dp[i - 1][0]
        dp[i][i] = triangle[i][i] + dp[i - 1][i - 1]
        for j in range(1, i):
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
    # print(dp)
    return min(dp[n - 1])

print(minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))


