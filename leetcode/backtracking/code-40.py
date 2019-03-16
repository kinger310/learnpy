# Given a collection of candidate numbers (candidates) and a target number (target),
# find all unique combinations in candidates where the candidate numbers sums to target.
#
# Each number in candidates may only be used once in the combination.
#
# Note:
#
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:
#
# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
# Example 2:
#
# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
#   [1,2,2],
#   [5]
# ]
def combinationSum2(candidates: 'List[int]', target: 'int') -> 'List[List[int]]':
    def backtrack(result, path, s, i):
        if s > target:
            return
        if s == target:
            result.append(path)
            return
        while i < n:
            if path + [candidates[i]] not in result:  # This is not elegant
                backtrack(result, path + [candidates[i]], s + candidates[i], i+1)
            i += 1

    candidates.sort()
    n = len(candidates)
    result = []
    backtrack(result, [], 0, 0)
    return result


def combinationSum22(candidates: 'List[int]', target: 'int') -> 'List[List[int]]':
    def backtrack(result, path, s, idx):
        if s > target:
            return
        if s == target:
            result.append(path)
            return
        for i in range(idx, n):
            if i > idx and candidates[i] == candidates[i-1]:  # skip duplicates
                continue
            backtrack(result, path + [candidates[i]], s + candidates[i], i+1)

    candidates.sort()
    n = len(candidates)
    result = []
    backtrack(result, [], 0, 0)
    return result

# print(combinationSum2([2,3,4,5], 8))
print(combinationSum22([10,1,2,7,6,1,5], 8))
# print(combinationSum2([2,5,2,1,2], 5))

