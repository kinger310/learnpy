def solveNQueens(n: int) -> 'List[List[str]]':
    def check(i, j):
        for x in range(n):
            for y in range(j):
                # x + j == y + i 是左上到右下的正斜线， x+y == i +j 是反斜线
                if board[x][y] == "Q" and (i == x or x + j == y + i or x + y == i + j):
                    return False
        return True

    def backtrack(result, col):
        if col == n:
            board_str = ["".join(row) for row in board]
            result.append(board_str)
        for i in range(n):
            if check(i, col):
                board[i][col] = "Q"
                backtrack(result, col + 1)
                board[i][col] = "."

    result = []
    board = [["."] * n for _ in range(n)]
    backtrack(result, 0)
    return result


print(solveNQueens(6))
