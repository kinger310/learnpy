# Introduction to algorithms 3rd. Page 31

def mysort(A):
    n = len(A)
    mergesort(A, 0, n - 1)


def mergesort(A, p, r):
    if p < r:
        mid = (p + r) // 2
        mergesort(A, p, mid)
        mergesort(A, mid + 1, r)
        merge(A, p, mid, r)


def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)
    for i in range(n1):
        L[i] = A[p + i]
    for j in range(n2):
        R[j] = A[q + j + 1]
    L[n1] = float("inf")
    R[n2] = float("inf")
    i, j = 0, 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


A = [5, 2, 4, 7, 1, 3, 2, 6]
mysort(A)
print(A)
