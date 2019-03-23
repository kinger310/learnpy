# 104. Maximum Depth of Binary Tree
# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given binary tree [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its depth = 3.
import collections
from leetcode.tree import lstToTreeNode

def maxDepth(root: 'TreeNode') -> int:
    if not root:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right))+1


def maxDepth2(root: 'TreeNode') -> int:
    if not root:
        return 0
    dq = collections.deque([root])
    depth = 0
    while dq:
        n = len(dq)
        for i in range(n):
            node = dq.popleft()
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
        depth += 1
    return depth


root = lstToTreeNode([3,9,20,None,None,15,7])
print(maxDepth(root))
print(maxDepth2(root))

