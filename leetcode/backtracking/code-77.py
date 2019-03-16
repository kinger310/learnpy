def combine(n: int, k: int) -> 'List[List[int]]':

    def backtrack(result, path, start):
        if len(path) == k:
            result.append(path)
            return
        for i in range(start + 1, n + 1):
            backtrack(result, path + [i], i)

    result = []
    backtrack(result, [], 0)
    return result


print(combine(4, 3))
