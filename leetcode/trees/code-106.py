# 106. Construct Binary Tree from Inorder and Postorder Traversal
# Given inorder and postorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#
# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
# Return the following binary tree:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7


from leetcode.tree import treeNodeToLst, TreeNode


def buildTree(inorder: 'List[int]', postorder: 'List[int]') -> 'TreeNode':
    if not inorder:
        return None
    val = postorder[-1]
    root = TreeNode(val)
    p = inorder.index(val)
    root.left = buildTree(inorder[:p], postorder[:p])
    root.right = buildTree(inorder[p + 1:], postorder[p:-1])
    return root


print(treeNodeToLst(buildTree([6, 9, 3, 15, 20, 7], [6, 9, 15, 7, 20, 3])))
