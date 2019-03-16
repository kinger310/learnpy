def fourSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """

    def findNsum(l, r, target, N, result, results):
        if r - l + 1 < N or N < 2 or target < nums[l] * N or target > nums[r] * N:  # early termination
            return
        if N == 2:  # two pointers solve sorted 2-sum problem
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
        else:  # recursively reduce N
            for i in range(l, r + 1):
                if i == l or (i > l and nums[i - 1] != nums[i]):
                    findNsum(i + 1, r, target - nums[i], N - 1, result + [nums[i]], results)

    nums.sort()
    results = []
    findNsum(0, len(nums) - 1, target, 4, [], results)
    return results


print(fourSum([-3, -2, -1, 0, 0, 1, 2, 3], 0))
