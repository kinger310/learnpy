from leetcode.listnode import lst2link, print_link, ListNode


def deleteDuplicates2(head):
    pre = dummy = ListNode(0)
    cur = dummy.next = head
    while cur:
        while cur.next and cur.val == cur.next.val:
            cur = cur.next
        if pre.next is cur:
            pre = cur
        else:
            pre.next = cur.next
        cur = cur.next

    return dummy.next

# leaving only distinct numbers from the original list.


def deleteDuplicates1(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    cur = head
    while cur:
        while cur.next and cur.val == cur.next.val:
            cur.next = cur.next.next
        cur = cur.next
    return head

p = lst2link([-1, 1,1,1,2,2,3,3,5])
q = deleteDuplicates2(p)
print_link(q)