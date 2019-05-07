# 41. First Missing Positive
# Given an unsorted integer nums, find the smallest missing positive integer.
#
# Example 1:
#
# Input: [1,2,0]
# Output: 3
# Example 2:
#
# Input: [3,4,-1,1]
# Output: 2
# Example 3:
#
# Input: [7,8,9,11,12]
# Output: 1
# Note:
#
# Your algorithm should run in O(n) time and uses constant extra space.

def firstMissingPositive(nums: 'List[int]') -> 'int':
    # Pass 1, move every value to the position of its value
    if not nums:
        return 1
    nums.append(0)  # 神来之笔
    N = len(nums)
    for cursor in range(N):
        target = nums[cursor]
        while 0 <= target < N and target != nums[target]:
            new_target = nums[target]
            nums[target] = target
            target = new_target

    # Pass 2, find first location where the index doesn't match the value
    for cursor in range(N):
        if nums[cursor] != cursor:
            return cursor
    return N


print(firstMissingPositive([1, 2, 0]))
print(firstMissingPositive([3, 4, -1, 1]))
print(firstMissingPositive([7, 8, 9, 11, 12]))
