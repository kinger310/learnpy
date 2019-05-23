# 617. Merge Two Binary Trees
# Given two binary trees and imagine that when you put one of them to cover the other,
# some nodes of the two trees are overlapped while the others are not.
#
# You need to merge them into a new binary tree. The merge rule is that if two nodes overlap,
# then sum node values up as the new value of the merged node. Otherwise,
# the NOT null node will be used as the node of new tree.
#
# Example 1:
#
# Input:
# 	Tree 1                     Tree 2
#           1                         2
#          / \                       / \
#         3   2                     1   3
#        /                           \   \
#       5                             4   7
# Output:
# Merged tree:
# 	     3
# 	    / \
# 	   4   5
# 	  / \   \
# 	 5   4   7

from leetcode.tree import TreeNode, lstToTreeNode, treeNodeToLst


def mergeTrees(t1: TreeNode, t2: TreeNode) -> TreeNode:
    if t1 is None or t2 is None:
        return t1 or t2
    t1.val += t2.val
    t1.left = mergeTrees(t1.left, t2.left)
    t1.right = mergeTrees(t1.right, t2.right)
    return t1


root = mergeTrees(lstToTreeNode([1, 3, 2, 5]), lstToTreeNode([2, 1, 3, None, 4, None, 7]))

print(root)
print(treeNodeToLst(root))
