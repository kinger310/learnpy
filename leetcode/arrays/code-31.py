# 31. Next Permutation
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
#
# If such arrangement is not possible, it must rearrange it as the lowest possible order
# (ie, sorted in ascending order).
#
# The replacement must be in-place and use only constant extra memory.
#
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
#
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

import bisect


def nextPermutation(nums: 'List[int]') -> 'None':
    """
    Do not return anything, modify nums in-place instead.
    """
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    # lo = i + 1
    # hi = len(nums)
    # # if
    # while lo < hi:
    #     mid = (lo + hi) // 2
    #     if nums[mid] > nums[i]:
    #         lo = mid + 1
    #     else:
    #         hi = mid
    # nums[hi-1], nums[i] = nums[i], nums[hi-1]
    if i >= 0:
        j = len(nums) - 1
        while j >= 0 and nums[i] >= nums[j]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

    s = i + 1
    t = len(nums) - 1
    while s < t:
        nums[s], nums[t] = nums[t], nums[s]
        s += 1
        t -= 1
    return nums

print(nextPermutation([3,2,1]))
print(nextPermutation([2,3,1]))
print(nextPermutation([1, 4, 3, 2]))
print(nextPermutation([1, 5, 8, 4, 7, 6, 5, 3, 1]))
