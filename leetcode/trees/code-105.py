# 105. Construct Binary Tree from Preorder and Inorder Traversal
# Given preorder and inorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# Return the following binary tree:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7

from leetcode.tree import treeNodeToLst, TreeNode

def buildTree(preorder: 'List[int]', inorder: 'List[int]') -> 'TreeNode':
    if not preorder:
        return None
    val = preorder[0]
    root = TreeNode(val)
    p = inorder.index(val)
    root.left = buildTree(preorder[1:1+p], inorder[:p])
    root.right = buildTree(preorder[1+p:], inorder[p+1:])
    return root


print(treeNodeToLst(buildTree([3,9,6,20,15,7], [6,9,3,15,20,7])))

