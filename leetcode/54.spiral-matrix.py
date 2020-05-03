#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (31.36%)
# Likes:    1345
# Dislikes: 450
# Total Accepted:    264.2K
# Total Submissions: 842.4K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix of m x n elements (m rows, n columns), return all elements of
# the matrix in spiral order.
# 
# Example 1:
# 
# 
# Input:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# 
# 
# Example 2:
# 
# Input:
# [
# ⁠ [1, 2, 3, 4],
# ⁠ [5, 6, 7, 8],
# ⁠ [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
# 
#
# https://leetcode.com/problems/spiral-matrix/discuss/20571/1-liner-in-Python-%2B-Ruby
# 有详细分析
# 递归解法
# 去一行后，顺时针旋转矩阵。参考leetcode-48. 但是顺时针旋转应该先转置再倒置。
class Solution:
    def spiralOrder(self, matrix: 'List[List[int]]') -> 'List[int]':
        return matrix and list(matrix.pop(0)) + self.spiralOrder(list(zip(*matrix))[::-1])

