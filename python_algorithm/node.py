import sys
sys.setrecursionlimit(100000)  # 例如这里设置为一百万


class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


class LinkList(object):
    def __init__(self):
        self.head = None

    # # 返回键对应的值
    # def __getitem__(self, key):
    #     if self.is_empty():
    #         print('linklist is empty.')
    #         return
    #     elif key < 0 or key > self.get_length():
    #         print('the given key is error')
    #         return
    #     else:
    #         return self.getitem(key)
    #
    # # 设置给定键的值
    def __len__(self):
        return self.get_length()

    def get_length(self):
        p = self.head
        length = 0
        while p:
            length += 1
            p = p.next
        return length

    def is_empty(self):
        return True if self.get_length() == 0 else False

    def init_list(self, data):
        self.head = Node(data[0])
        p = self.head
        for i in data[1:]:
            node = Node(i)
            p.next = node
            p = p.next


def print_linked_list(node):
    while node:
        print(node.value)
        node = node.next


# maximum recursion depth exceeded
def print_backward(node):
    if node is None:
        return
    head = node.value
    tail = node.next
    print_backward(tail)
    print(head)


def main():
    data = [i for i in range(1000)]
    l = LinkList()
    l.init_list(data)

    # linked_list = Node('a', Node('b', Node('c', Node('d'))))
    print_linked_list(l.head)
    print_backward(l.head)


if __name__ == '__main__':
    main()
