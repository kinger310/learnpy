# 76. Minimum Window Substring
# Given a string S and a string T,
# find the minimum window in S which will contain all the characters in T in complexity O(n).
#
# Example:
#
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
# Note:
#
# If there is no such window in S that covers all characters in T, return the empty string "".
# If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

import collections


def minWindow(s: str, t: str) -> str:
    if not s or not t:
        return ""
    # Dictionary which keeps a count of all the unique characters in t.
    dict_t = collections.Counter(t)
    # Number of unique characters in t, which need to be present in the desired window.
    required = len(dict_t)

    left, right = 0, 0
    formed = 0
    # Dictionary which keeps a count of all the unique characters in the current window.
    window_counts = {}

    ans = float("inf"), None, None

    while right < len(s):
        c = s[right]
        window_counts[c] = window_counts.get(c, 0) + 1
        if c in dict_t and window_counts[c] == dict_t[c]:
            formed += 1
        while left <= right and formed == required:
            ch = s[left]
            if right - left + 1 < ans[0]:
                ans = right-left+1, left, right

            # The character at the position pointed by the `left` pointer is no longer a part of the window.
            window_counts[ch] -= 1
            if ch in dict_t and window_counts[ch] < dict_t[ch]:
                formed -= 1

            left += 1
        right += 1
    return "" if ans == float("inf") else s[ans[1]:ans[2]+1]


print(minWindow("ABAACBAB", "ABC"))
# print(minWindow("ADOBECODEBANC","ABC"))
