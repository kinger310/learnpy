# 94. Binary Tree Inorder Traversal
# Given a binary tree, return the inorder traversal of its nodes' values.
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
# Output: [1,3,2]
# Follow up: Recursive solution is trivial, could you do it iteratively?
from leetcode.tree import lstToTreeNode


def inorderTraversal(root: 'TreeNode') -> 'List[int]':
    def search(result, root):
        if not root:
            return None
        search(result, root.left)
        result.append(root.val)
        search(result, root.right)

    result = []
    search(result, root)
    return result


def inorderTraversal2(root: 'TreeNode') -> 'List[int]':
    result = []
    stack = []
    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        result.append(cur.val)
        cur = cur.right
    return result


def inorderTraversal3(root: 'TreeNode') -> 'List[int]':
    result = []
    stack = [(root, False)]
    while stack:
        cur, visited = stack.pop()
        if cur:
            if visited:
                result.append(cur.val)
            else:
                stack.append((cur.right, False))
                stack.append((cur, True))
                stack.append((cur.left, False))
    return result


root = lstToTreeNode([1, None, 2, 3])
print(inorderTraversal(root))
print(inorderTraversal2(root))
print(inorderTraversal3(root))
