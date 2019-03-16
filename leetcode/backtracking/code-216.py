# Find all possible combinations of k numbers that add up to a number n,
# given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
#
# Note:
#
# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:
#
# Input: k = 3, n = 7
# Output: [[1,2,4]]
# Example 2:
#
# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]


def combinationSum3(k: int, n: int) -> 'List[List[int]]':
    def backtrack(result, path, s, start):
        if len(path) == k and s == n:
            result.append(path)
            return
        for i in range(start, 10):
            backtrack(result, path+[i], s+i, i+1)

    result = []
    backtrack(result, [], 0, 1)

    return result

print(combinationSum3(3,9))
print(combinationSum3(3,7))
print(combinationSum3(10,45))
print(combinationSum3(3,10))



