# 132. Palindrome Partitioning II
# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return the minimum cuts needed for a palindrome partitioning of s.
#
# Example:
#
# Input: "aab"
# Output: 1
# Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.



#
# This can be solved by two points:
#
# cut[i] is the minimum of cut[j - 1] + 1 (j <= i), if [j, i] is palindrome.
# If [j, i] is palindrome, [j + 1, i - 1] is palindrome, and c[j] == c[i].

def minCut(s: str) -> int:
    n = len(s)
    cut = [0] * n
    pal = [[False] * n for _ in range(n)]

    for i in range(n):
        min_val = i
        for j in range(i + 1):
            if s[j] == s[i] and (j + 1 > i - 1 or pal[j + 1][i - 1]):
                pal[j][i] = True
                min_val = 0 if j == 0 else min(min_val, cut[j - 1] + 1)
        cut[i] = min_val
    return cut[n - 1]


print(minCut("abcbc"))
