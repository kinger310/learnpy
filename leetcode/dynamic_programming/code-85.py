# 85. Maximal Rectangle
# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
#
# Example:
#
# Input:
# [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# Output: 6

# The DP solution proceeds row by row, starting from the first row.
# Let the maximal rectangle area at row i and column j be computed by [right(i,j) - left(i,j)]*height(i,j).


# S2:计数法
#
# 对于这样一个只包含'0','1'的二维数组，我们既然要求一个最大的只由'1'组成的矩形，
# 那么就需要关注'1'连续存在的情况，连续的'1'才能组成更大的矩形，并且一旦遇到'0'，矩形就必然不能成立了。所以如果将一个矩形作如下变换：
#
# 1 0 1 0 0		1 0 1 0 0
# 1 0 1 1 1	->	1 0 1 2 3
# 1 1 1 1 1		1 2 3 4 5
# 1 0 0 1 0		1 0 0 1 0
# 即将每一行连续的'1'的个数标志出来，那么所有的横向的矩形就解出来了。
# 那么怎么样根据这个计算多行能够合并的最大矩形呢？首先，使用二重遍历遍历到每一个元素，
# 而我们，通过上面的矩阵求出以这个元素结尾的最大的的矩形。那么，对于某一个元素，
# 我们只需要求出高度高度一定的时候宽度的最大值，便可以求出最大的矩形。这时连续的'1'的数量就派上用处了，
# 举个例子，对于上面变换过后的坐标[2,3]，元素值为 4 ，意味着在这一行（第三行），这个元素前面有 4 个连续的'1'，
# 那么当高度为 1 的时候，宽度最大必然就是 4 了，那么当高度为 2 的时候呢？我们看坐标[2,3]上面的坐标[1,3]值为 2 ，
# 意味着这一层只有 2 个连续的'1'，所以，以位置[2,3]为矩形的右下角，高度为 2 的时候宽度最大是 2 ，这个矩形的面积就求出来了，
# 当求高度为 3 的矩形面积的时候，再将第一行的数据加上来就行了。当高度逐渐增加，遇到一个'0'的时候，意味着这无法构成一个矩形了，
# 就可以结束这一点的求解了。
#
# 按照这样的方法，如果我们将每一个点的所有解都求出来，取其最大，必然能够求得最大的那个矩形的面积。代码如下：


def maximalRectangle(matrix: 'List[List[str]]'):
    m = len(matrix)
    n = len(matrix[0]) if m else 0
    for i in range(m):
        for j in range(1, n):
            if matrix[i][j] == "1":
                matrix[i][j] = chr(ord(matrix[i][j-1])+1)

    max_val = 0
    for i in range(m):
        for j in range(n):
            min_val = ord(matrix[i][j]) - ord('0')
            if min_val > 0:
                max_val = max(max_val, min_val)
                k = i-1
                while k >= 0 and matrix[k][j] != '0':
                    min_val = min(min_val, ord(matrix[k][j]) - ord('0'))
                    max_val = max(max_val, min_val * (i-k+1))
                    k -= 1

    return max_val


print(maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))

