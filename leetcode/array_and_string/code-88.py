# 88. Merge Sorted Array
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
# Note:
#
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is greater or equal to m + n)
# to hold additional elements from nums2.
# Example:
#
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# Output: [1,2,2,3,5,6]


def merge2(nums1: 'List[int]', m: int, nums2: 'List[int]', n: int):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i, j = 0, 0
    while i < m and j < n:
        if nums1[i] > nums2[j]:
            nums1[i], nums2[j] = nums2[j], nums1[i]
            j += 1
        i += 1
    k = 0
    tj = j
    while j < n or k < tj:
        if nums2[k] > nums2[j]:
            nums1[m + k] = nums2[j]
            j += 1
        else:
            # nums1[m + ]
            pass

    return nums1


# Hint: What if you fill the longer array from the end instead of start ?
# 当正向困难时，逆向思维很奇妙
def merge(nums1: 'List[int]', m: int, nums2: 'List[int]', n: int):
    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
    if n > 0:
        nums1[:n] = nums2[:n]

    return nums1



# print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))
# print(merge([4,5,6,0,0,0], 3, [1,2,3], 3))
# print(merge([1], 1, [], 0))
# print(merge([4,5,0,0,0,0],2,[1,2,3,6],4))
print(merge([4,5,6,7,0,0],4,[1,2],2))