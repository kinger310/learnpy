# 363. Max Sum of Rectangle No Larger Than K

# DP. sum(i, j) is 0->i, 0->j rectangle's area.
# sum(i, j) = sum(i-1, j)+sum(i, j-1)+A[i, j] - sum(i-1,j-1)

def maxSumSubmatrix(matrix: 'List[List[int]]', k: int) -> int:
    return -1


print(maxSumSubmatrix([[1,0,1],[0,-2,3]], 2))
