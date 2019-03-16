def solveNQueens(n: int) -> 'List[List[str]]':
    def validate(board, i, j):
        for x in range(n):
            for y in range(0, j):
                if board[x][y] == "Q" and (x == i or x + j == y + i or x + y == i + j):
                    # 第一种情况是列剪枝，第二种情况是正斜线，第三种是反斜线（正反相对0,0点在左上角来说）
                    return False
        return True

    def backtrack(result, board, col):
        if col == n:
            new_board = ["".join(row) for row in board]
            result.append(new_board)
            return
        for i in range(n):
            if validate(board, i, col):
                board[i][col] = "Q"
                backtrack(result, board, col+1)
                board[i][col] = "."

    board = [["." for _ in range(n)] for _ in range(n)]
    result = []
    backtrack(result, board, 0)
    return result


print(solveNQueens(2))

# import bisect
#
# bisect.bisect_left([1, 2, 4], 3)
