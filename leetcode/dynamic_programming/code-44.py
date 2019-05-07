# 44. Wildcard Matching
# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.
#
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).
#
# Note:
#
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like ? or *.
# Example 1:
#
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:
#
# Input:
# s = "aa"
# p = "*"
# Output: true
# Explanation: '*' matches any sequence.
# Example 3:
#
# Input:
# s = "cb"
# p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
# Example 4:
#
# Input:
# s = "adceb"
# p = "*a*b"
# Output: true
# Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
# Example 5:
#
# Input:
# s = "acdcb"
# p = "a*c?b"
# Output: false

def isMatch(s: str, p: str) -> bool:
    m = len(p)
    n = len(s)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    for i in range(m):
        if p[i] == "*":
            dp[i+1][0] = dp[i][0]   # 这个想不到

    for i in range(m):
        for j in range(n):
            if p[i] == "*":
                dp[i + 1][j + 1] = dp[i+1][j] or dp[i][j + 1]  # 这个很难想
            # elif p[i] == "*":
            #     dp[i + 1][j + 1] = dp[i + 1][j]
            elif p[i] == "?" or p[i] == s[j]:
                dp[i + 1][j + 1] = dp[i][j]

    # print(dp)
    return dp[m][n]


# print(isMatch(s="acdcb", p="a*c?b"))
# print(isMatch(s="aa", p="a"))
# print(isMatch(s="aa", p="*"))
# print(isMatch(s="cb", p="?a"))
# print(isMatch(s="adceb", p="*a*b"))
# print(isMatch(s="aa",p="*b*"))
# print(isMatch("aab","c*a*b"))
# print(isMatch(s="adceb", p="c*a*b"))
print(isMatch("abefcdgiescdfimde", "ab*cd?i*de"))
