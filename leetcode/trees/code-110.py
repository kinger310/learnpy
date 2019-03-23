# 110. Balanced Binary Tree
# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as:
#
# a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
#
# Example 1:
#
# Given the following tree [3,9,20,None,None,15,7]:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Return true.
#
# Example 2:
#
# Given the following tree [1,2,2,3,3,None,None,4,4]:
#
#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
# Return false.

from leetcode.tree import lstToTreeNode


def isBalanced2(root: 'TreeNode') -> bool:
    def maxDepth(root):
        if not root:
            return 0
        left = maxDepth(root.left)
        right = maxDepth(root.right)
        if left < 0 or right < 0 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1

    h = maxDepth(root)
    return h >= 0

def isBalanced(root: 'TreeNode') -> bool:
    def maxDepth(root):
        if not root:
            return 0
        return max(maxDepth(root.left), maxDepth(root.right)) + 1

    if not root:
        return True
    left = maxDepth(root.left)
    right = maxDepth(root.right)

    return abs(left - right) <= 1 and isBalanced(root.left) and isBalanced(root.right)


root1 = lstToTreeNode([3, 9, 20, None, None, 15, 7])
root2 = lstToTreeNode([1, 2, 2, 3, 3, None, None, 4, 4])
root3 = lstToTreeNode([1, 2, 2, 3, None, None, 3, 4, None, None, 4])
# print(isBalanced(root1))
# print(isBalanced(root2))
print(isBalanced(root3))
