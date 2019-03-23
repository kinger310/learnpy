import collections
from leetcode.tree import lstToTreeNode

def zigzagLevelOrder(root: 'TreeNode') -> 'List[List[int]]':
    result = []
    if not root:
        return result
    queue = collections.deque([root])
    level = 0
    flag = 0
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
        if flag:
            result[level] = result[level][::-1]
        flag = 1 - flag
        level += 1
    return result

root = lstToTreeNode([3,9,20,None,None,15,7, 1,2])
print(zigzagLevelOrder(root))
