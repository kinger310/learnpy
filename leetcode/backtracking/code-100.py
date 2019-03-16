from leetcode.tree import lstToTreeNode

def isSameTree(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    if p is None and q is None:
        return True
    elif p is None or q is None:
        return False
    if p.val == q.val:
        left = isSameTree(p.left, q.left)
        right = isSameTree(p.right, q.right)
        return left and right
    return False
    # stack = [(p, q)]
    # while stack:
    #     r1, r2 = stack.pop()
    #     if (r1 and not r2) or (not r1 and r2) or (r1 and r2 and r1.val != r2.val):
    #         return False
    #     if r1 and r2:
    #         stack.append((r1.left, r2.left))
    #         stack.append((r1.right, r2.right))
    # return True

p = lstToTreeNode([1,2,3,4])
q = lstToTreeNode([1,2,3,5])
print(isSameTree(p, q))

