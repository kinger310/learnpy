from leetcode.listnode import timethis

@timethis
def f(N, M):
    def dfs(n, m):
        if m == 0 or n == 0:
            return 0
        if m == 1 or n == 1:
            return 1
        if (m, n) in cache:
            return cache[(m, n)]
        res = dfs(n - 1, m) + dfs(n, m - 1)
        cache[(m, n)] = res
        return res

    cache = {}
    result = dfs(N, M)
    return result


@timethis
def g(n, m):
    def dfs(n,m):
        if m == 0 or n == 0:
            return 0
        if m == 1 or n == 1:
            return 1
        return dfs(n - 1, m) + dfs(n, m - 1)
    result = dfs(n, m)
    return result



@timethis
def ff(grid):
    def dfs(n, m):
        if m == 0 or n == 0 or grid[n - 1][m - 1] == 1:
            return 0
        if m == 1 and n == 1:  # 这里更严格了
            return 1

        if (m, n) in cache:
            return cache[(m, n)]
        res = dfs(n - 1, m) + dfs(n, m - 1)
        cache[(m, n)] = res
        return res

    if not grid:
        return 0
    cache = {}
    N = len(grid)
    M = len(grid[0])
    result = dfs(N, M)
    return result


# print(f(100, 100))
# print(g(15, 15))

# print(ff([[0,0,0],[0,0,0],[0,1,0]]))
# print(ff([[1,0,0]]))
print(ff([[0,0],[1,1],[0,0]]))



