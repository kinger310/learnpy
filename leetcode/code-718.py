
def findLength(A: 'List[int]', B: 'List[int]') -> 'int':

    def search(xi, yi, result):
        if xi < 0 or yi < 0:
            return 0

        if A[xi] == B[yi]:
            cache[xi][yi] = search(xi-1, yi-1, result)+1

        search(xi - 1, yi, result)
        search(xi, yi - 1, result)
        result[0] = max(result[0], cache[xi][yi])
        return cache[xi][yi]

    n = len(A)
    m = len(B)

    cache = [[0] * m for _ in range(n)]
    result = [0]
    search(n-1, m-1, result)
    return result[0]






def findLength2(A,B):
    memo = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
    for i in range(len(A) - 1, -1, -1):
        for j in range(len(B) - 1, -1, -1):
            if A[i] == B[j]:
                memo[i][j] = memo[i + 1][j + 1] + 1
    return max(max(row) for row in memo)

# 求连续最大公共子序列
print(findLength([1,2,3,2,1],[3,2,1,4,7]))
print(findLength([0,1,1,1,1], [1,0,1,0,1]))

