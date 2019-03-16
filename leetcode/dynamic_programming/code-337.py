from leetcode.tree import lstToTreeNode


def rob(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    def search(node, canRob):
        if node is None:
            return 0
        if (node, canRob) in cache:
            return cache[(node, canRob)]
        ans = 0
        if canRob:
            ans = max(ans, node.val + search(node.left, False) + search(node.right, False))
        ans = max(ans, search(node.left, True) + search(node.right, True))
        cache[(node, canRob)] = ans
        return cache[(node, canRob)]

    cache = {}
    return search(root, True)
    

# def rob(self, root):
#     """
#     :type root: TreeNode
#     :rtype: int
#     """
#     def robSub(root):
#         if not root:
#             return [0, 0]
#
#         left = robSub(root.left);
#         right = robSub(root.right);
#         res = [0, 0]
#
#         res[0] = max(left[0], left[1]) + max(right[0], right[1])
#         res[1] = root.val + left[0] + right[0]  # left[0] 表示left节点没有被rob，left[1] 表示left节点被rob
#         return res
#
#     res = robSub(root)
#     return max(res[0], res[1])


# lst = [53, 2, 3, 4, 3, 1, None, 67]
lst = [3,2,3,None,3,None,1]

lst2 = [3,4,5,1,3,None,1]
tree = lstToTreeNode(lst2)
print(rob(tree))
