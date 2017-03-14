# -*- coding: utf-8 -*-

import sys

if __name__ == "__main__":
    # 读取第一行的n
    for line in sys.stdin:
        a = line.split()
        str1 = a[0]
        str2 = a[1]
        gene = {'A', 'T', 'G', 'C'}
        n = 0
        if len(str1) == len(str2) <= 50 and set(str1).issubset(gene) and set(str2).issubset(gene):
            new_str2 = list(str2)
            for i, s in enumerate(str1):
                if s == 'A' and new_str2[i] != 'T':
                    new_str2[i] = 'T'
                    n += 1
                elif s == 'T' and new_str2[i] != 'A':
                    new_str2[i] = 'A'
                    n += 1
                elif s == 'G' and new_str2[i] != 'C':
                    new_str2[i] = 'C'
                    n += 1
                elif s == 'C' and new_str2[i] != 'G':
                    new_str2[i] = 'G'
                    n += 1
            print(n)
        else:
            print("Not good input!")
