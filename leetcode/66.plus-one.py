#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
# https://leetcode.com/problems/plus-one/description/
#
# algorithms
# Easy (41.65%)
# Likes:    980
# Dislikes: 1741
# Total Accepted:    441.4K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty array of digits representing a non-negative integer, plus
# one to the integer.
# 
# The digits are stored such that the most significant digit is at the head of
# the list, and each element in the array contain a single digit.
# 
# You may assume the integer does not contain any leading zero, except the
# number 0 itself.
# 
# Example 1:
# 
# 
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# 
# 
# Example 2:
# 
# 
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# 
#
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits) - 1
        adder = [0] * len(digits)
        adder[-1] = 1
        carry = 0
        while n >= 0 or carry:
            carry, digits[n] = divmod(digits[n]+adder[n]+carry, 10)
            n -= 1
        return digits

