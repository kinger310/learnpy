# 107. Binary Tree Level Order Traversal II
# Given a binary tree, return the bottom-up level order traversal of its nodes' values.
# (ie, from left to right, level by level from leaf to root).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]

from leetcode.tree import lstToTreeNode
import collections


def levelOrderBottom(root: 'TreeNode') -> 'List[List[int]]':
    queue = collections.deque([root])
    cur = root
    result = []
    while cur and queue:
        level_res = []
        level_que = collections.deque([])
        while queue:
            cur = queue.popleft()
            level_res.append(cur.val)
            if cur.left:
                level_que.append(cur.left)
            if cur.right:
                level_que.append(cur.right)
        result.append(level_res)
        queue = level_que
    return result[::-1]


root = lstToTreeNode([3,9,20,None,None,15,7])
print(levelOrderBottom(root))


