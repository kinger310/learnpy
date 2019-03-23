# 101. Symmetric Tree
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following [1,2,2,null,3,null,3] is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3
# Note:
# Bonus points if you could solve it both recursively and iteratively.

from leetcode.tree import lstToTreeNode
import copy

def isSymmetric1(root: 'TreeNode') -> bool:
    def invert(root):
        if not root:
            return None
        left = invert(root.left)
        right = invert(root.right)
        root.left = right
        root.right = left
        return root

    def isSame(p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        return p.val == q.val and isSame(p.left, q.left) and isSame(p.right, q.right)

    inv = invert(copy.deepcopy(root))
    return isSame(root, inv)


def isSymmetric2(root: 'TreeNode') -> bool:
    def isMirror(p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        return p.val == q.val and isMirror(p.left, q.right) and isMirror(p.right, q.left)
    return isMirror(root, root)


def isSymmetric(root: 'TreeNode') -> bool:
    stack = [(root, root)]
    while stack:
        r1, r2 = stack.pop()
        if (r1 and not r2) or (not r1 and r2) or (r1 and r2 and r1.val != r2.val):
            return False
        if r1 and r2:
            stack.append((r1.left, r2.right))
            stack.append((r1.right, r2.left))
    return True

r1 = lstToTreeNode([1, 2, 2, 3, 4, 4, 3])
print(isSymmetric(r1))
r2 = lstToTreeNode([1, 2, 2, None, 3, None, 3])
print(isSymmetric(r2))
