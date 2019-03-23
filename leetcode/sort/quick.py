
# 数组被划分为4个（可能有空的）区域，
# 最右边是主元 pivot = A[hi]
# 最左边A[lo..i]内所有值小于等于x
# 往右A[i+1..j-1]内所有值大于x
# 再往右是无限制区域
def partition(A, lo, hi):
    pivot = A[hi]
    i = lo - 1
    for j in range(lo, hi):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    return i+1


def quick(A, lo, hi):
    if lo < hi:
        p = partition(A, lo, hi)
        quick(A, lo, p-1)
        quick(A, p+1, hi)

A = [2,7,4,5,0,9,8,1,3,6]
n = len(A)-1
quick(A, 0, n)
print(A)