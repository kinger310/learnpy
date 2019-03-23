# 102. Binary Tree Level Order Traversal
# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

from leetcode.tree import lstToTreeNode
import collections

def levelOrder(root: 'TreeNode') -> 'List[List[int]]':
    queue = collections.deque([root])
    cur = root
    new_que = collections.deque([])
    result = []
    while cur or queue:
        tmp = []
        while queue:
            cur = queue.popleft()
            if cur:
                tmp.append(cur.val)
                new_que.extend([cur.left, cur.right])
        if tmp:
            result.append(tmp)
        queue = new_que.copy()
        new_que = collections.deque([])
    return result


def levelOrder2(root: 'TreeNode') -> 'List[List[int]]':
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
    return result

def levelOrder3(root: 'TreeNode') -> 'List[List[int]]':
    result = []
    if not root:
        return result
    queue = collections.deque([root])
    level = 0
    while queue:
        result.append([])
        que_len = len(queue)
        for i in range(que_len):
            cur = queue.popleft()
            result[level].append(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        level += 1
    return result

root = lstToTreeNode([3,9,20,None,None,15,7])
# root = lstToTreeNode([])

print(levelOrder(root))
print(levelOrder2(root))
print(levelOrder3(root))

