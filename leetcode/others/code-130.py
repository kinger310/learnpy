# 130. Surrounded Regions
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
#
# Example:
#
# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:
#
# X X X X
# X X X X
# X X X X
# X O X X
# Explanation:
#
# Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board
# are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the
# border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected
# horizontally or vertically.

# Phase 1: "Save" every O-region touching the border, changing its cells to 'S'.
# Phase 2: Change every 'S' on the board to 'O' and everything else to 'X'.

def solve(board: 'List[List[str]]') -> None:
    if not any(board): return

    m, n = len(board), len(board[0])
    save = [(i, j) for k in range(m + n) for i, j in ((0, k), (m - 1, k), (k, 0), (k, n - 1))]
    while save:
        i, j = save.pop()
        if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
            board[i][j] = 'S'
            save += (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)
    # phase 2
    for row in board:
        for i, c in enumerate(row):
            row[i] = 'XO'[c == 'S']

    return board

print(solve([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]))
print(solve([["X","X","X","X"],["X","O","O","X"],["X","O","O","X"],["X","O","X","X"]]))