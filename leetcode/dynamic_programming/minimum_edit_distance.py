# 72. Edit Distance
# Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
#
# You have the following 3 operations permitted on a word:
#
# Insert a character
# Delete a character
# Replace a character
# Example 1:
#
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation:
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# Example 2:
#
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation:
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')


def minDistance(word1: str, word2: str) -> int:
    m, n = len(word2), len(word1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        dp[i][0] = i
    for j in range(1, n + 1):
        dp[0][j] = j
    for i in range(m):
        for j in range(n):
            replace = dp[i][j]
            insert = dp[i][j + 1]
            delete = dp[i + 1][j]
            if word2[i] == word1[j]:
                dp[i + 1][j + 1] = min(replace, insert + 1, delete + 1)
            else:
                dp[i + 1][j + 1] = min(replace, insert, delete) + 1
    # print(dp)
    return dp[m][n]


print(minDistance(word1="horse", word2=""))
print(minDistance(word1="horse", word2="ros"))
print(minDistance(word1="intention", word2="execution"))
