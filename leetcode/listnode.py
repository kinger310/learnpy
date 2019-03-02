import time
from functools import wraps

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def lst2link(lst):
    cur = dummy = ListNode(0)
    for e in lst:
        cur.next = ListNode(e)
        cur = cur.next
    return dummy.next


def cyclelink(lst, pos):
    cur = dummy = ListNode(0)
    cache = None
    for i, e in enumerate(lst):
        cur.next = ListNode(e)
        cur = cur.next
        if i == pos:
            cache = cur
    cur.next = cache
    return dummy.next


def print_link(head):
    cur = head
    result = []
    while cur:
        result.append(cur.val)
        cur = cur.next
    print(result)


# A simple decorator
def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print(end-start)
        return r
    return wrapper


if __name__ == '__main__':
    x = cyclelink([1, 2, 3, 4], 1)
    # x = lst2link([1,2,3])
    print_link(x)

    print("ok")
