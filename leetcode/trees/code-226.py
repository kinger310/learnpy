# 226. Invert Binary Tree
# Invert a binary tree.
#
# Example:
#
# Input:
#
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# Output:
#
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
# Trivia:
# This problem was inspired by this original tweet by Max Howell:
#
# Google: 90% of our engineers use the software you wrote (Homebrew),
# but you can’t invert a binary tree on a whiteboard so f*** off.
# from collections
from leetcode.tree import TreeNode, lstToTreeNode, treeNodeToLst
import collections


def invertTree(root: 'TreeNode') -> 'TreeNode':
    if not root:
        return None
    left = invertTree(root.left)
    right = invertTree(root.right)
    root.left = right
    root.right = left
    return root

def invertTree2(root: 'TreeNode') -> 'TreeNode':
    if not root:
        return None
    queue = collections.deque([root])
    while queue:
        cur = queue.popleft()
        cur.left, cur.right = cur.right, cur.left
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)
    return root

root = lstToTreeNode([4,2,7,1,3,6,9])
# print(treeNodeToLst(invertTree(root)))
print(treeNodeToLst(invertTree2(root)))

