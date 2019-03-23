from leetcode.listnode import lst2link, link2Lst


def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    # if not head:
    #     return None
    tail = head
    prev = None
    while tail:
        temp = tail.next
        tail.next = prev
        prev = tail
        tail = temp
    return prev


def reverse_link(head):
    if head is None or head.next is None:
        return head
    p = reverse_link(head.next)
    head.next.next = head
    head.next = None
    return p


head = lst2link([1, 2, 3, 4, 5])
p = reverse_link(head)
print(link2Lst(p))
