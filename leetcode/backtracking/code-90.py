def subsetsWithDup(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    # 如何选取一种好的方式去重？不要后置去重，搜索的过程中去掉答案
    def search(idx, result, path):
        result.append(path)
        for i in range(idx, n):
            if i > idx and nums[i] == nums[i-1]:
                continue
            search(i + 1, result, path + [nums[i]])

    nums.sort()
    n = len(nums)
    result = []
    search(0, result, [])
    return result

print(subsetsWithDup([2,1,2,3]))
