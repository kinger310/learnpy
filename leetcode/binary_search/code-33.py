# 33. Search in Rotated Sorted Array
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#
# You are given a target value to search. If found in the array return its index, otherwise return -1.
#
# You may assume no duplicate exists in the array.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# Example 1:
#
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
#
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1


def search(nums: 'List[int]', target: 'int') -> 'int':
    lo = 0
    hi = len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if (target < nums[0]) == (nums[mid] < nums[0]):
            n = nums[mid]
        elif target < nums[0]:
            n = float("-inf")
        else:
            n = float("inf")
        if n < target:
            lo = mid + 1
        elif n > target:
            hi = mid
        else:
            return mid
    return -1


nums = [6,7,0,1,2,4,5]
print(search(nums, 3))
