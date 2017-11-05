
#!/bin/env python
#-*-coding:utf-8-*-
import sys

def prime(n):
    flag = [1]*(n+2)
    p=2
    p_list = []
    while p <= n:
        p_list.append(p)
        for i in range(2*p,n+1,p):
            flag[i] = 0
        while 1:
            p += 1
            if(flag[p]==1):
                break
    return p_list

if __name__ == "__main__":
    nn = input()
    n = int(nn)
    for k in range(1, 11):
        if n >> k == 0:
            break
    k -= 1
    p_list = prime(n)
    count = len(p_list)
    for i in range(2, k+1):
        for p in p_list:
            if p ** i <= n:
                count += 1
    print(count)
