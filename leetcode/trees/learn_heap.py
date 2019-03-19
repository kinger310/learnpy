import heapq


# heapq.heapify([3,2,1,4,5,6,7])

def min_heapify(A, i, size):
    n = len(A[:size])
    while i < n:
        left = 2 * i + 1
        right = left + 1
        min_pos = i
        # 跟两个子节点比，跟最小的交换位置
        if left < n and A[left] < A[min_pos]:
            min_pos = left
        if right < n and A[right] < A[min_pos]:
            min_pos = right
        if min_pos != i:
            A[min_pos], A[i] = A[i], A[min_pos]
            i = min_pos
        else:
            break


def max_heapify(A, i, size):
    n = len(A[:size])
    while i < n:
        left = 2 * i + 1
        right = left + 1
        max_pos = i
        # 跟两个子节点比，跟最大的交换位置
        if left < n and A[left] > A[max_pos]:
            max_pos = left
        if right < n and A[right] > A[max_pos]:
            max_pos = right
        if max_pos != i:
            A[max_pos], A[i] = A[i], A[max_pos]
            i = max_pos
        else:
            break


def heapify(A):
    n = len(A)
    for i in reversed(range(n // 2)):
        # sift up
        max_heapify(A, i, n)


def heap_sort(A):
    n = len(A)
    heapify(A)
    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        max_heapify(A, 0, i)


B = [3, 2, 6, 4, 5, 7, 1]
# heapify(B)
heap_sort(B)
print(B)
