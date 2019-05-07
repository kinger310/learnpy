# 97. Interleaving String
# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
#
# Example 1:
#
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
## Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbca"
## return False
# Example 2:
#
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false


def isInterleave(s1: str, s2: str, s3: str) -> bool:
    m, n = len(s1), len(s2)
    if len(s3) != m + n:
        return False
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    # dp[0][0] = True
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 and j == 0:
                dp[i][j] = True
            elif i == 0:
                dp[i][j] = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
            elif j == 0:
                dp[i][j] = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j] and s1[i - 1] == s3[i + j - 1], dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
    # print(dp)
    return dp[m][n]


print(isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac"))

print(isInterleave(s1="a", s2="b", s3="a"))
