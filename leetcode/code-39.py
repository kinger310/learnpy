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
