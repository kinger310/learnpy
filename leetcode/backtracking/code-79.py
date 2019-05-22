# 79. Word Search
# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring.
# The same letter cell may not be used more than once.
#
# Example:
#
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.


def exist(board: 'List[List[str]]', word: str) -> bool:
    m = len(board)
    n = len(board[0]) if m else 0
    p = len(word)
    visited = [[False] * n for _ in range(m)]
    if (m == 0 or n == 0) and p==0:
        return True
    if m == 0 or n == 0:
        return False

    def search(i, j, k):
        if i < 0 or i >= m or j < 0 or j >= n or k >= len(word):
            return False
        print(i,j,k)
        if not visited[i][j] and board[i][j] == word[k] and k == len(word) - 1:
            return True
        if not visited[i][j] and board[i][j] == word[k]:
            visited[i][j] = True
            find_flag = search(i - 1, j, k + 1) or search(i + 1, j, k + 1) \
                        or search(i, j - 1, k + 1) or search(i, j + 1, k + 1)
            visited[i][j] = False
            return find_flag

    for i in range(m):
        for j in range(n):
            if search(i, j, 0):
                return True
    return False

# print(exist([], ""))
# print(exist([[]], ""))
# print(exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"))
# print(exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))
# print(exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"))

print(exist([["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]], "aaaaaaaaaaaaa"))