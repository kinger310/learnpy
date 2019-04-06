# 64. Minimum Path Sum
# Given a m x n grid filled with non-negative numbers, find a path from
# top left to bottom right which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# Example:

# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.


def minPathSum(grid: "List[List[int]]") -> int:
    # def search(i,j):
    #     if i == m-1 or j == n-1:
    #         return
    #     if i >= m or j >= n:
    #         return 0
    #     ans = 0
    #     ans += grid[i][j] + min(search(i+1, j), search(i, j+1))
    #     print(i,j,ans)
    #     return ans
    #
    m = len(grid)
    n = len(grid[0]) if m else 0
    if not m or not n:
        return 0
    dp = [[0] * n for _ in range(m)]

    dp[0][0] = grid[0][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
    return dp[m - 1][n - 1]


print(minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
