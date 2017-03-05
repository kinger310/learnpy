# -*- coding: utf-8 -*-
"""
Given a string, find the length of the longest substring without repeating characters.
Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        j = m = 0
        for i, c in enumerate(s):
            if c in dic:
                j = max(j, dic[c]+1)
            dic[c] = i
            m = max(m, i-j+1)
        return m


def main():
    my_str = 'aaaaaaaaaaaaaaabcaaaaaaaaaaaaaa'
    s = Solution()
    print(s.lengthOfLongestSubstring(my_str))

if __name__ == '__main__':
    main()




