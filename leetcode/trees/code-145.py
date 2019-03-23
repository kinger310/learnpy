# 144. Binary Tree Preorder Traversal
#
# Given a binary tree, return the preorder traversal of its nodes' values.
#
# Example:
#
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# Output: [1,2,3]
# Follow up: Recursive solution is trivial, could you do it iteratively?
#
from leetcode.tree import lstToTreeNode


def postorderTraversal(root: 'TreeNode') -> 'List[int]':
    def search(result, root):
        if not root:
            return None
        search(result, root.left)
        search(result, root.right)
        result.append(root.val)

    result = []
    search(result, root)
    return result


def postorderTraversal2(root: 'TreeNode') -> 'List[int]':
    result = []
    stack = [(root, False)]
    while stack:
        cur, visited = stack.pop()
        if cur:
            if visited:
                result.append(cur.val)
            else:
                stack.append((cur, True))
                stack.append((cur.right, False))
                stack.append((cur.left, False))
    return result


# The 3rd uses modified preorder (right subtree first). Then reverse the result.
def postorderTraversal3(root: 'TreeNode') -> 'List[int]':
    result = []
    stack = [root]
    while stack:
        cur = stack.pop()
        if cur:
            result.append(cur.val)
            stack.append(cur.left)
            stack.append(cur.right)
    return result[::-1]

root = lstToTreeNode([1, 2, 3, None, None, 4])
print(postorderTraversal(root))
print(postorderTraversal2(root))
print(postorderTraversal3(root))


import numpy as np
import matplotlib.pyplot as plt
