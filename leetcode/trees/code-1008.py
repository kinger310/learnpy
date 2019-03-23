# 1008. Construct Binary Search Tree from Preorder Traversal
# Return the root node of a binary search tree that matches the given preorder traversal.
# (Recall that a binary search tree is a binary tree where for every node, 
# any descendant of node.left has a value < node.val, 
# and any descendant of node.right has a value > node.val.
# Also recall that a preorder traversal displays the value of the node first, 
# then traverses node.left, then traverses node.right.)
# Example 1:

# Input: [8, 5, 1, 7, 10, 12]
# Output: [8, 5, 10, 1, 7, null, 12]

import bisect
from leetcode.tree import treeNodeToLst, TreeNode


def bstFromPreorder(A: 'List[int]') -> 'TreeNode':
    if not A:
        return None
    p = bisect.bisect(A, A[0])
    root = TreeNode(A[0])
    root.left = bstFromPreorder(A[1:p])
    root.right = bstFromPreorder(A[p:])
    return root


print(treeNodeToLst(bstFromPreorder([8, 5, 1, 7, 10, 12])))
print(treeNodeToLst(bstFromPreorder([])))
