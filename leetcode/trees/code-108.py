# 108. Convert Sorted Array to Binary Search Tree
# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
#
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more than 1.
#
# Example:
#
# Given the sorted array: [-10,-3,0,5,9],
#
# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
#
#       0
#      / \
#    -3   9
#    /   /
#  -10  5

from leetcode.tree import treeNodeToLst, TreeNode


def sortedArrayToBST(nums: 'List[int]') -> 'TreeNode':
    if not nums:
        return None
    p = len(nums)//2
    root = TreeNode(nums[p])
    root.left = sortedArrayToBST(nums[:p])
    root.right = sortedArrayToBST(nums[p+1:])
    return root

tree = sortedArrayToBST([-10,-3,0,5, 9])
print(treeNodeToLst(tree))

