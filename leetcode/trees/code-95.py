# 95. Unique Binary Search Trees II
# Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.
#
# Example:
#
# Input: 3
# Output:
# [
#   [1,null,3,2],
#   [3,2,null,1],
#   [3,1,null,null,2],
#   [2,1,3],
#   [1,null,2,null,3]
# ]
# Explanation:
# The above output corresponds to the 5 unique BST's shown below:
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

from leetcode.tree import TreeNode, treeNodeToLst

def generateTrees(n: int) -> 'List[TreeNode]':
    def generate(first, last):
        result = []
        for root in range(first, last+1):
            for left in generate(first, root-1):
                for right in generate(root+1, last):
                    node = TreeNode(root)
                    node.left = left
                    node.right = right
                    result.append(node)
        return result or [None]

    return generate(1, n)

tr_lst = generateTrees(2)
print([treeNodeToLst(x) for x in tr_lst])
print(len(tr_lst))
