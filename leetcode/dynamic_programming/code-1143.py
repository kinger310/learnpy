# 1143. Longest Common Subsequence
#
# Given two strings text1 and text2, return the length of their longest common subsequence.
# A subsequence of a string is a new string generated from the original string with
# some characters(can be none) deleted without changing the relative order of the remaining
# characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence
# of two strings is a subsequence that is common to both strings.
#
# If there is no common subsequence, return 0.


def longestCommonSubsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i, c1 in enumerate(text1):
        for j, c2 in enumerate(text2):
            if c1 == c2:
                dp[i+1][j+1] = dp[i][j]+1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

    return dp[-1][-1]


print(longestCommonSubsequence("bsbininm", "jmjkbkjkv"))