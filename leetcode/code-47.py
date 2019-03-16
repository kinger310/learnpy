def permuteUnique(nums: 'List[int]') -> 'List[List[int]]':
    def backtrack(result, path):
        if len(path) == n:
            result.append(path.copy())
            return
        for i in range(n):
            if used[i]:
                continue
            if i > 0 and nums[i - 1] == nums[i] and (not used[i - 1]):
                continue

            path.append(nums[i])
            used[i] = True
            backtrack(result, path)
            used[i] = False
            path.pop()

    result = []
    nums.sort()
    n = len(nums)
    used = [False] * n
    backtrack(result, [])
    return result


print(permuteUnique([3,3,0,3]))
