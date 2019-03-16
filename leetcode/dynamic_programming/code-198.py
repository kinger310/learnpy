# 198. House Robber
# https://leetcode.com/problems/house-robber/


def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # f(x) = max(f(x-1), x + f(x-2))
    arr = [0 for _ in range(len(nums) + 2)]
    for i in range(len(nums)):
        arr[i + 2] = max(arr[i + 1], nums[i] + arr[i])
    return arr[-1]


print(rob([2, 7, 9, 3, 1]))
