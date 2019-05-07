# 98. Validate Binary Search Tree
# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# Example 1:
#
# Input:
#     2
#    / \
#   1   3
# Output: true
# Example 2:
#
#     5
#    / \
#   1   4
#      / \
#     3   6
# Output: false
# Explanation: The input is: [5,1,4,None,None,3,6]. The root node's value
#              is 5 but its right child's value is 4.

# The idea above could be implemented as a recursion. One compares the node value with its upper and lower
# limits if they are available. Then one repeats the same step recursively for left and right subtrees.

from leetcode.tree import lstToTreeNode


def isValidBST(root: 'TreeNode') -> bool:
    if root is None:
        return True

    def isValid(node, lo, hi):
        if lo is not None and node.val <= lo:
            return False
        if hi is not None and node.val >= hi:
            return False
        left = isValid(node.left, lo, node.val) if node.left else True
        if left:
            right = isValid(node.right, node.val, hi) if node.right else True
            return right
        else:
            return False

    return isValid(root, None, None)

#
# print(isValidBST(lstToTreeNode([2, 1, 3])))
# print(isValidBST(lstToTreeNode([5, 1, 4, None, None, 3, 6])))
# print(isValidBST(lstToTreeNode([10, 5, 15, None, None, 6, 20])))

print(isValidBST(lstToTreeNode([0,None,-1])))