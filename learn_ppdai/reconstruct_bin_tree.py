# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return "<" + repr(self.val) + "," + repr(self.left) + "," + repr(self.right) + ">"


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        else:
            flag = TreeNode(pre[0])
            flag.left = self.reConstructBinaryTree(pre[1:tin.index(pre[0]) + 1], tin[:tin.index(pre[0])])
            flag.right = self.reConstructBinaryTree(pre[tin.index(pre[0]) + 1:], tin[tin.index(pre[0]) + 1:])
        return flag


if __name__ == '__main__':
    pre = [1, 2, 4, 7, 3, 5, 6, 8]  # 前序遍历序列
    tin = [4, 7, 2, 1, 5, 3, 8, 6]  # 中序遍历序列
    bin_tree = Solution().reConstructBinaryTree(pre, tin)
    print(bin_tree)
