# 109. Convert Sorted List to Binary Search Tree
# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
#
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more than 1.
#
# Example:
#
# Given the sorted linked list: [-10,-3,0,5,9],
#
# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
#
#       0
#      / \
#    -3   9
#    /   /
#  -10  5

from leetcode.listnode import lst2link
from leetcode.tree import treeNodeToLst, TreeNode

# 时间复杂度O(NlogN)
def sortedListToBST(head: 'ListNode') -> 'TreeNode':
    # 难点在于如何查找链表的中间结点
    # 思想，快慢指针
    def find_middle(head):
        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        # 但是有个问题，left怎么遍历到mid就结束。设置prev前驱结点，保存slow指针。
        # 并用下面两行代码解决这个问题，返回后的head被修改，链表被mid一分为二
        if prev:
            prev.next = None
        return slow

    if not head:
        return None
    mid = find_middle(head)
    root = TreeNode(mid.val)
    # Base case when there is just one element in the linked list
    if head == mid:
        return root
    # 但是有个问题，left怎么遍历到mid就结束
    root.left = sortedListToBST(head)
    root.right = sortedListToBST(mid.next)
    return root

# 链表查找中间点确实很难，把链表转化成数组可以把时间复杂度将为O(N)
def sortedListToBST1(head: 'ListNode') -> 'TreeNode':

    def link2Lst(head):
        cur = head
        result = []
        while cur:
            result.append(cur.val)
            cur = cur.next
        return result

    def sortedArrayToBST(nums: 'List[int]') -> 'TreeNode':
        if not nums:
            return None
        p = len(nums) // 2
        root = TreeNode(nums[p])
        root.left = sortedArrayToBST(nums[:p])
        root.right = sortedArrayToBST(nums[p + 1:])
        return root

    if not head:
        return None
    nums = link2Lst(head)
    return sortedArrayToBST(nums)



p = lst2link([-10, -3, 0, 5, 9])
print(treeNodeToLst(sortedListToBST(p)))
p = lst2link([-10, -3, 0, 5, 9])
print(treeNodeToLst(sortedListToBST1(p)))
