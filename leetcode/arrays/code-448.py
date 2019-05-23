# 448. Find All Numbers Disappeared in an Array
# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#
# Find all the elements of [1, n] inclusive that do not appear in this array.
#
# Could you do it without extra space and in O(n) runtime?
# You may assume the returned list does not count as extra space.
#
# Example:
#
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [5,6]

def findDisappearedNumbers(nums):
    n = len(nums)
    for i in range(n):
        idx = abs(nums[i]) - 1
        nums[idx] = -abs(nums[idx])
    return [i + 1 for i in range(n) if nums[i] > 0]

print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))


