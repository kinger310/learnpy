# coding=utf-8

import sys
from functools import reduce


class Tree:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


def map_tree(lst):
    node = Tree(lst[0])
    node.left = Tree(lst[1])
    node.right = Tree(lst[2])
    return node


def reduce_tree(a_tree, b_tree):
    if a_tree.left.value != '*' and a_tree.left.value == b_tree.value:
        a_tree.left = b_tree
    if a_tree.right.value != '*' and a_tree.right.value == b_tree.value:
        a_tree.right = b_tree
    return a_tree


# map-reduce
if __name__ == '__main__':
    m, n = [int(x) for x in sys.stdin.readline().strip().split()]

    ans = 0
    input_list = []
    for _ in range(m):
        line_list = sys.stdin.readline().strip().split()
        input_list.append(line_list)
    if len(input_list):
        node = Tree(input_list[0][0])
        node.left = Tree(input_list[0][1])
        node.right = Tree(input_list[0][j])
        for j in range(1, m):
            temp = input_list[j]




    # trees = map(map_tree, input_list)
    # result_tree = reduce(reduce_tree, trees)

    print(input_list)




