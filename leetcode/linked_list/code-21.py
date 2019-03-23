# 21. Merge Two Sorted Lists
# Merge two sorted linked lists and return it as a new list. 
# The new list should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

from leetcode.listnode import lst2link, ListNode, print_link

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = cur = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next

l1 = lst2link([1,2,4])
l2 = lst2link([1,3,4])

print_link(mergeTwoLists(l1, l2))

