# -*- coding: utf-8 -*-
"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
"""


class Solution(object):
    def findMedianSortedArrays(self, A, B):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError
        i_min, i_max, half_len = 0, m, (m + n + 1) // 2
        while i_min <= i_max:
            i = (i_min + i_max) // 2   # Detail 1，i,j must be int.
            j = half_len - i
            if i < m and B[j-1] > A[i]:  # Detail 2, i < m must be ahead.
                # i is too small, must increase it
                i_min = i + 1
            elif i > 0 and A[i-1] > B[j]:
                # i is too big, must decrease it
                i_max = i - 1
            else:
                # find i success!
                if i == 0:
                    max_of_left = B[j-1]
                elif j == 0:
                    max_of_left = A[i-1]
                else:
                    max_of_left = max(A[i-1], B[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = B[j]
                elif j == n:
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i], B[j])
                return (max_of_left + min_of_right) / 2.0


def main():
    s = Solution()
    nums1 = [1, 3, 5, 7]
    nums2 = [2]
    print(s.findMedianSortedArrays(nums1, nums2))

if __name__ == '__main__':
    main()




