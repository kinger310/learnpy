from leetcode.listnode import cyclelink


def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast and fast.next is slow:
            return True

    return False

def detectCycle(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow is fast:
            i = 0
            while slow is not head:
                head = head.next
                slow = slow.next
                i += 1
            print("tail connects to node index %s" % i)
            return head
    print("no cycle")
    return None



head = cyclelink([1,2,3,4,5,6], 2)
print(detectCycle(head))
