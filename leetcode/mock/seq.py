

def foo(N):
    a = [0] * 50
    a[0] = 1
    for i in range(1, 50):
        s = 0
        for j in range(i):
            s += a[j] * (j+1)
        a[i] = s % (i+1)
    for i in range(50):
        print(str(a[i]).zfill(3),end=",")
        if (i+1)%6 == 0:
            print()
    # A = [1,1,0,3,0,3,5,4]
    # if N < 9:
    #     return A[N-1]
    # x, y = divmod(N - 8, 6)
    # if y == 1 or y == 3:
    #     return x+1
    # elif y == 0 or y == 4:
    #     return N // 2
    # elif y == 2:
    #     return N - 1
    # else:
    #     return N - (x+2)*2

print(foo(37))