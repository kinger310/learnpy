# 种子填充法又称洪水填充法
# from collections import deque


def numIslands(grid: 'List[List[str]]') -> 'int':
    def check(x, y, t):
        if 0 <= x < r and 0 <= y < c and grid[x][y] == "1":
            grid[x][y] = "0"
            qx[t] = x
            qy[t] = y
            t += 1
        return t

    def bfs(x, y):
        h = 0  # head
        t = 1  # tail
        grid[x][y] = "0"
        qx[0], qy[0] = x, y
        while h < t:
            t = check(qx[h] - 1, qy[h], t)
            t = check(qx[h] + 1, qy[h], t)
            t = check(qx[h], qy[h] - 1, t)
            t = check(qx[h], qy[h] + 1, t)
            h += 1

    r = len(grid)
    c = len(grid[0]) if grid else 0

    if r == 0 or c == 0:
        return 0
    qx = [0] * (r * c + 1)
    qy = [0] * (r * c + 1)
    cnt = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] == "1":
                bfs(i, j)
                cnt += 1

    return cnt


print(numIslands(
    [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["0", "1", "0", "0", "1"], ["1", "0", "0", "1", "1"]]))
