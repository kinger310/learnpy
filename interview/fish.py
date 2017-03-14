# -*- coding: utf-8 -*-
import sys


def num_of_fish(min_size, max_size, fish_size):
    ans = 0
    for j in range(min_size, max_size + 1):
        flag = 1
        for i in fish_size:
            if 2 * j <= i <= 10 * j or 2 * i <= j <= 10 * i:
                flag = 0
        if flag:
            ans += 1
    return ans

if __name__ == "__main__":
    line1 = sys.stdin.readline()
    a = line1.split()
    min_size = int(a[0])
    max_size = int(a[1])
    n = int(sys.stdin.readline())
    line3 = sys.stdin.readline()
    fish_size = [int(x) for x in line3.split()]
    assert n >= len(fish_size)
    res = num_of_fish(min_size, max_size, fish_size)
    print(res)

