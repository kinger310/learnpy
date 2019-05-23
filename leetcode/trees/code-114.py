# 114. Flatten Binary Tree to Linked List
# Given a binary tree, flatten it to a linked list in-place.
#
# For example, given the following tree:
#
#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
# The flattened tree should look like:
#
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6

from leetcode.tree import lstToTreeNode, treeNodeToLst
# from leetcode.listnode import link2Lst


class Solution:
    def __init__(self):
        self.prev = None

    def flatten(self, root: 'TreeNode') -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.prev
        root.left = None
        self.prev = root


s = Solution()
root = lstToTreeNode([1, 2, 5, 3, 4, None, 6])
s.flatten(root)
print(treeNodeToLst(root))
# print("ok")
