def rob(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    def robSub(root, dct):
        if not root:
            return 0
        if root in dct:
            return dct[root]
        result = 0
        if root.left:
            result += robSub(root.left.left, dct) + robSub(root.left.right, dct)
        if root.right:
            result += robSub(root.right.left, dct) + robSub(root.right.right, dct)
        result = max(result + root.val, robSub(root.left, dct) + robSub(root.right, dct))
        dct[root] = result
    
    return robSub(root, {})

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def robSub(root):
            if not root:
                return [0, 0]

            left = robSub(root.left);
            right = robSub(root.right);
            res = [0, 0]

            res[0] = max(left[0], left[1]) + max(right[0], right[1])
            res[1] = root.val + left[0] + right[0]  # left[0] 表示left节点没有被rob，left[1] 表示left节点被rob
            return res
        
        res = robSub(root)
        return max(res[0], res[1])


lst = [53, 2, 3, 4, 3, 1, None, 67]

