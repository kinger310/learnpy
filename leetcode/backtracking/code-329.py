# 329. Longest Increasing Path in a Matrix
# Given an integer matrix, find the length of the longest increasing path.
#
# From each cell, you can either move to four directions: left, right, up or down.
# You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).
#
# Example 1:
#
# Input: nums =
# [
#   [9,9,4],
#   [6,6,8],
#   [2,1,1]
# ]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].
# Example 2:
#
# Input: nums =
# [
#   [3,4,5],
#   [3,2,6],
#   [2,2,1]
# ]
# Output: 4
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.


def longestIncreasingPath(matrix: 'List[List[int]]') -> int:
    def check(i, j, dx, dy):
        if 0 <= i + dx < r and 0 <= j + dy < c and matrix[i][j] > matrix[i + dx][j + dy]:
            return True
        else:
            return False

    def search(i, j):
        if i < 0 or i >= r or j < 0 or j >= c:
            return 0
        if (i, j) in cache:
            return cache[(i, j)]
        m = 0
        for (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if check(i, j, dx, dy):
                m = max(m, search(i + dx, j + dy))
        cache[(i, j)] = m+1
        return cache[(i, j)]

    r = len(matrix)
    c = len(matrix[0]) if r else 0
    ans = 0
    cache = {}
    for i in range(r):
        for j in range(c):
            ans = max(ans, search(i, j))
    return ans


def longestIncreasingPath2(matrix):
    mat = {i + j*1j: val
              for i, row in enumerate(matrix)
              for j, val in enumerate(row)}
    length = {}
    for z in sorted(mat, key=mat.get):
        tmp_lst = []
        for Z in [z + 1, z - 1, z + 1j, z - 1j]:
            if Z in mat and mat[z] > mat[Z]:
                tmp_lst.append(length[Z])
        length[z] = 1 + max(tmp_lst or [0])
    return max(length.values() or [0])


def longestIncreasingPath3(matrix: 'List[List[int]]') -> int:
    def check(i, j, dx, dy):
        return 0 <= i + dx < r and 0 <= j + dy < c and matrix[i][j] > matrix[i + dx][j + dy]

    r = len(matrix)
    c = len(matrix[0]) if r else 0
    ans = 0
    dp = {(i, j): 0 for i in range(r) for j in range(c)}
    for i in range(r):
        for j in range(c):
            for (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if check(i, j, dx, dy):
                    dp[i, j] = max(dp[i, j], dp[i + dx, j + dy])
            dp[(i, j)] += 1
            ans = max(ans, dp[i, j])
    return ans


# print(longestIncreasingPath([]))
# print(longestIncreasingPath3([[1]]))
#
# print(longestIncreasingPath([
#     [9, 9, 4],
#     [6, 6, 8],
#     [2, 1, 1]]))
#
# print(longestIncreasingPath([
#     [3, 4, 5],
#     [3, 3, 6],
#     [2, 2, 1]]))

# print(longestIncreasingPath2([
#     [3, 4, 5],
#     [3, 2, 6],
#     [2, 2, 1]]))
# print(longestIncreasingPath3([
#     [3, 4, 5],
#     [3, 2, 6],
#     [2, 2, 1]]))

print(longestIncreasingPath2([[9,9,4],[6,6,8],[2,1,1]]))
print(longestIncreasingPath3([[9,9,4],[6,6,8],[2,1,1]]))