# 206. Reverse Linked List

# Reverse a singly linked list.

# Example:

# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL


from leetcode.listnode import lst2link, link2Lst


def reverseList(head: 'ListNode') -> 'ListNode':
    cur = head
    pre = None
    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return pre
    



head = lst2link([1, 2, 3, 4, 5])
p = reverseList(head)
print(link2Lst(p))