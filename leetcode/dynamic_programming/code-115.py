# 115. Distinct Subsequences
# Given a string S and a string T, count the number of distinct subsequences of S which equals T.
#
# A subsequence of a string is a new string which is formed from the original string by
# deleting some (can be none) of the characters without disturbing the relative positions
# of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
#
# Example 1:
#
# Input: S = "rabbbit", T = "rabbit"
# Output: 3
# Explanation:
#
# As shown below, there are 3 ways you can generate "rabbit" from S.
# (The caret symbol ^ means the chosen letters)
#
# rabbbit
# ^^^^ ^^
# rabbbit
# ^^ ^^^^
# rabbbit
# ^^^ ^^^
# Example 2:
#
# Input: S = "babgbag", T = "bag"
# Output: 5
# Explanation:
#
# As shown below, there are 5 ways you can generate "bag" from S.
# (The caret symbol ^ means the chosen letters)
#
# babgbag
# ^^ ^
# babgbag
# ^^    ^
# babgbag
# ^    ^^
# babgbag
#   ^  ^^
# babgbag
#     ^^^

#  t in substr
def numDistinct(s: str, t: str) -> int:
    n = len(s)
    m = len(t)
    if n < m:
        return 0
    dp = [[0]*(n+1) for _ in range(m+1)]
    for j in range(n+1):
        dp[0][j] = 1
    for i in range(m):
        for j in range(i, n):
            if t[i] == s[j]:
                dp[i+1][j+1] = dp[i+1][j]+dp[i][j]
            else:
                dp[i+1][j+1] = dp[i+1][j]
    # print(dp)
    return dp[m][n]

print(numDistinct("aabb", "abb"))
print(numDistinct("babgbag","bag"))
print(numDistinct("rabbit", "rabbit"))
print(numDistinct("rabbbit", "rabbit"))

