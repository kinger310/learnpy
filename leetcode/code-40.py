def combinationSum2(candidates: 'List[int]', target: 'int') -> 'List[List[int]]':
    def backtrack(result, path, s, i):
        if s > target:
            return
        if s == target:
            if path not in result:
                result.append(path)
            return
        while i < len(candidates):
            # if not path or (path and path[-1] <= candidates[i]):
            backtrack(result, path + [candidates[i]], s + candidates[i], i+1)
            i += 1

    candidates.sort()
    result = []
    backtrack(result, [], 0, 0)
    return result

print(combinationSum2([2,3,4,5], 8))
# print(combinationSum2([10,1,2,7,6,1,5], 8))
# print(combinationSum2([2,5,2,1,2], 5))

