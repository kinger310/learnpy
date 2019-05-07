# 49. Group Anagrams
# Given an array of strings, group anagrams together.
#
# Example:
#
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:
#
# All inputs will be in lowercase.
# The order of your output does not matter.
import collections

def groupAnagrams(strs: 'List[str]') -> 'List[List[str]]':
    dct = collections.defaultdict(list)
    for word in strs:
        keyword = "".join(sorted(word))
        dct[keyword].append(word)
    return list(dct.values())




print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))