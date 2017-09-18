# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)

    def pop(self):
        if not self.stack2:
            while self.stack1:
                a = self.stack1.pop()
                self.stack2.append(a)
        return self.stack2.pop()


COU = 0
def foo():
    global COU
    for i in range(5):
        COU += 1


if __name__ == '__main__':
    queue = Solution()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    foo()
    print(COU)
    print(queue.pop())

