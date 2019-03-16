# from itertools import  permutations

def permute(nums: 'List[int]') -> 'List[List[int]]':
    def backtrack(result, path):
        if len(path) == n:
            result.append(path.copy())
            return
        for i in range(n):
            if nums[i] in path:
                continue
            path.append(nums[i])
            backtrack(result, path)
            path.pop()

    result = []
    n = len(nums)
    backtrack(result, [])
    return result


print(permute([1, 2, 3]))
