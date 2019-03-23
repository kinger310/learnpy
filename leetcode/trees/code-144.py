# 145. Binary Tree Postorder Traversal
# Given a binary tree, return the postorder traversal of its nodes' values.
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
# Output: [3,2,1]
# Follow up: Recursive solution is trivial, could you do it iteratively?
#
from leetcode.tree import lstToTreeNode


def preorderTraversal(root: 'TreeNode') -> 'List[int]':
    def search(result, root):
        if not root:
            return None
        result.append(root.val)
        search(result, root.left)
        search(result, root.right)

    result = []
    search(result, root)
    return result


def preorderTraversal2(root: 'TreeNode') -> 'List[int]':
    result = []
    stack = []
    cur = root
    while cur or stack:
        while cur:
            result.append(cur.val)
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        cur = cur.right
    return result

def preorderTraversal3(root: 'TreeNode') -> 'List[int]':
    result = []
    stack = [root]
    while stack:
        cur = stack.pop()
        if cur:
            result.append(cur.val)
            stack.append(cur.right)
            stack.append(cur.left)
    return result


root = lstToTreeNode([1, None, 2, 3])
print(preorderTraversal(root))
print(preorderTraversal2(root))
print(preorderTraversal3(root))
