# 100. Same Tree
# Given two binary trees, write a function to check if they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
#
# Example 1:
#
# Input:     1         1
#           / \       / \
#          2   3     2   3
#
#         [1,2,3],   [1,2,3]
#
# Output: true
# Example 2:
#
# Input:     1         1
#           /           \
#          2             2
#
#         [1,2],     [1,null,2]
#
# Output: false

from leetcode.tree import lstToTreeNode

def isSameTree1(p, q):
    if not p and not q:
        return True
    if (p and not q) or (not p and q):
        return False
    return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


def isSameTree(p, q):
    stack = [(p, q)]
    while stack:
        r1, r2 = stack.pop()
        if (r1 and not r2) or (not r1 and r2) or (r1 and r2 and r1.val != r2.val):
            return False
        if r1 and r2:
            stack.append((r1.left, r2.left))
            stack.append((r1.right, r2.right))
    return True


r1 = lstToTreeNode([1,2])
r2 = lstToTreeNode([1,None,2])
r3 = lstToTreeNode([1,2,3])
r4 = lstToTreeNode([1,2,3])
print(isSameTree(r1, r2))
print(isSameTree(r3, r4))




