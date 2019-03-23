# 112. Path Sum
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such
# that adding up all the values along the path equals the given sum.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given the below binary tree and sum = 22,
#
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

from leetcode.tree import lstToTreeNode, treeNodeToLst

# not success
def hasPathSum(root: 'TreeNode', n: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None and root.val == n:
            return True
        return hasPathSum(root.left, n - root.val) or hasPathSum(root.right, n - root.val)


def hasPathSum1(root: 'TreeNode', n: int) -> bool:
    if not root:
        return False
    stack = [(root, n)]
    while stack:
        r, s = stack.pop()
        if r.left is None and r.right is None and r.val == s:
            return True
        if r.left:
            stack.append((r.left, s - r.val))
        if r.right:
            stack.append((r.right, s - r.val))
    return False


# root1 = lstToTreeNode([5,4,8,11,None,13,4,7,2,None,None,None,1])
root = lstToTreeNode([5,4,8,None,11])

print(hasPathSum1(root, 9))

print(treeNodeToLst(root))