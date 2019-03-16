def permuteUnique(nums: 'List[int]') -> 'List[List[int]]':
    def backtrack(result, path):
        if len(path) == n:
            result.append(path.copy())
            return
        for i in range(n):
            if used[i]:
                continue
            if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack(result, path)
            path.pop()
            used[i] = False

    result = []
    n = len(nums)
    used = [False] * n
    backtrack(result, [])
    return result

print(permuteUnique([1,1,2]))
