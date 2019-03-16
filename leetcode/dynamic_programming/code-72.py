def minDistance(word1: str, word2: str) -> int:
    def f(i, j):
        if j < 0:
            return i+1
        if i < 0:
            return j+1
        if i == 0 and j == 0 and word1[i] == word2[j]:
            return 0
        if i == 0 and j == 0 and word1[i] != word2[j]:
            return 1
        if (i,j) in cache:
            return cache[i,j]
        if word1[i] == word2[j]:
            res1 = f(i - 1, j - 1)
        else:
            res1 = f(i - 1, j - 1) + 1
        res2 = f(i - 1, j) + 1
        res3 = f(i, j - 1) + 1
        cache[i,j] = min(res1, res2, res3)
        return cache[i,j]

    m = len(word1)
    n = len(word2)
    cache = {}
    return f(m - 1, n - 1)


def minDistance2(word1: str, word2: str) -> int:
    m = len(word1)
    n = len(word2)
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(m+1):
        dp[0][i] = i
    for j in range(n+1):
        dp[j][0] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            dp[j][i] = min(
                dp[j-1][i]+1, dp[j][i-1]+1,
                dp[j-1][i-1] if word1[i-1] == word2[j-1] else dp[j-1][i-1]+1
            )
    return dp[n][m]


print(minDistance2("", "a"))
print(minDistance2("a", ""))
print(minDistance2("a", "a"))
print(minDistance2("horse", "ros"))
print(minDistance2("intention", "execution"))
