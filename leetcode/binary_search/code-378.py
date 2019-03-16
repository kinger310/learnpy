# Given a n x n matrix where each of the rows and columns are sorted in ascending order,
# find the kth smallest element in the matrix.
#
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.
#
# Example:
#
# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,
#
# return 13.
# You may assume k is always valid, 1 ≤ k ≤ n^2.

def kthSmallest(matrix: 'List[List[int]]', k: int) -> int:
    def guess(mid):
        cnt = 0
        for row in matrix:
            for num in row:
                if num < mid:
                    cnt += 1
        return cnt >= k

    n = len(matrix)
    lo = matrix[0][0]
    hi = matrix[n-1][n-1]+1
    ans = 0
    while lo < hi:
        mid = (lo + hi) // 2
        if guess(mid):
            hi = mid
        else:
            ans = mid
            lo = mid + 1
    return ans

print(kthSmallest([[1,5,9],[10,11,13],[12,14,15]],8))
print(kthSmallest([[1,1],[1,1]],4))
print(kthSmallest([[-5]],1))

