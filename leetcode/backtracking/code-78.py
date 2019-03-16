def subsets(nums: 'List[int]') -> 'List[List[int]]':
    def search(idx, result, path):
        result.append(path)
        for i in range(idx, len(nums)):
            search(i + 1, result, path + [nums[i]])

    result = []
    search(0, result, [])
    return result

print(subsets([1,2,3]))
