# -*- coding: utf-8 -*-


def print_directory_contents(sPath):
    """
    太重要了！阿里面试跪在这里...T_T
    这个函数接受文件夹的名称作为输入参数，
    返回该文件夹中文件的路径，
    以及其包含文件夹中文件的路径。
    """
    import os
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath, sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)
print_directory_contents('.')

"""
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    if len(nums) <= 1:
        return [-1, -1]
    buff_dict = {}
    for i in range(len(nums)):
        if nums[i] not in buff_dict:
            buff_dict[target - nums[i]] = i
        else:
            return [buff_dict[nums[i]], i]
    return [-1, -1]


def two_sum(nums, target):
    d = {}
    for i, num in enumerate(nums):
        if target - num in d:
            return [d[target - num], i]
        d[num] = i

# Definition for singly-linked list.


class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)  # Return the tuple (x//y, x%y)
            n.next = ListNode(val)
            n = n.next
        return root.next





def main():
    """
    nums = [2, 7, 11, 15]
    target = 26
    two_sum(nums, target)
    """
    l1 = ListNode([2, 4, 3])
    l2 = ListNode([5, 6, 4])
    s = Solution()
    s.addTwoNumbers(l1, l2)


if __name__ == '__main__':
    main()
