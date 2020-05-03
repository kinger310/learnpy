
def partition(a, lo, hi):
    i = lo - 1
    pivot = a[hi]
    for j in range(lo, hi):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[hi] = a[hi], a[i+1]
    return i+1


def quicksort(a):
    def quick(a, lo, hi):
        if lo < hi:
            pos = partition(a, lo, hi)
            quick(a, lo, pos -1)
            quick(a, pos+1, hi)
    
    quick(a, 0, len(a) - 1)


n = [8, 2, 1, 6, 4, 0, 7, 5, 9, 3]
quicksort(n)
print(n)