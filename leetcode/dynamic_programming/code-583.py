# 583. Delete Operation for Two Strings
# Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same,
# where in each step you can delete one character in either string.
#
# Example 1:
# Input: "sea", "eat"
# Output: 2
# Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
# Note:
# The length of given words won't exceed 500.
# Characters in given words can only be lower-case letters.


def minDistance2(word1: str, word2: str) -> int:
    # least common subsequence
    m, n = len(word1), len(word2)
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in range(m):
        for j in range(n):
            if word1[i] == word2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
    return m+n - 2*dp[m][n]


def minDistance(word1: str, word2: str) -> int:
    # least common subsequence
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(2)]
    for i in range(m):
        for j in range(n):
            if word1[i] == word2[j]:
                dp[(i + 1) % 2][j + 1] = dp[i % 2][j] + 1
            else:
                dp[(i + 1) % 2][j + 1] = max(dp[(i + 1) % 2][j], dp[i % 2][j + 1])
    return m + n - 2 * dp[m % 2][n]

# print(minDistance("eat", "sea"))
print(minDistance("eaa", "saa"))
