# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
# find all unique combinations in candidates where the candidate numbers sums to target.
#
# The same repeated number may be chosen from candidates unlimited number of times.
#
# Note:
#
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:
#
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]
# Example 2:
#
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]


def combinationSum(candidates: 'List[int]', target: 'int') -> 'List[List[int]]':
    def backtrack(result, path, s):
        if s > target:
            return
        if s == target:
            result.append(path)
            return
        for n in candidates:
            if not path or (path and path[-1] <= n):
                backtrack(result, path + [n], s + n)
    candidates.sort()
    result = []
    backtrack(result, [], 0)
    return result

print(combinationSum([2,3,4,5], 8))
