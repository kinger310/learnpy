# -*- coding: utf-8 -*-

import sys


def sep_items(n, L):
    my_dict = {}
    my_list = []
    if n <= 2:
        return my_list
    is_exist = False
    for a1 in range(1, n//2 + 1):
        for a2 in range(a1 + 1, n + 1):
            if (a1 + a2) * (a2 - a1 + 1) == n * 2:
                is_exist = True
                my_dict[a2 - a1 + 1] = a1
    if is_exist:
        min_len = min(my_dict.keys())
        if min_len >= L:
            my_list = [my_dict[min_len]+i for i in range(min_len)]
        return my_list
    else:
        return my_list

if __name__ == "__main__":
    for line in sys.stdin:
        a = line.split()
        n = int(a[0])
        L = int(a[1])
        # n, L = 5, 1
        my = sep_items(n, L)
        if 0 < len(my) < n:
            print(my)
        else:
            print('No')
