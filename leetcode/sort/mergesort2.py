
def msort(a, lo, mid, hi):
    n1 = mid - lo +1
    n2 = hi - mid 
    L = [0]*(n1+1)
    R = [0]*(n2+1)
    for i in range(n1):
        L[i] = a[i+lo]
    for j in range(n2):
        R[j] = a[j+mid+1]
    L[n1] = R[n2] = float("inf")
    i = j = 0
    for k in range(lo, hi+1):
        if L[i] < R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j+=1



def mergesort(a):
    def merge(a, lo, hi):
        if lo < hi:
            mid = (lo+ hi)//2
            merge(a, lo, mid)
            merge(a, mid+1, hi)
            msort(a, lo, mid, hi)
    
    merge(a, 0, len(a) - 1)


n = [8, 2, 1, 6, 4, 0, 7, 5, 9, 3]
mergesort(n)
print(n)