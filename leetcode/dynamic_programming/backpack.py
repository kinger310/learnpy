def backPack(m, A):
    # write your code here
    dp = [0] * (m + 1)
    for item in A:
        for size in range(m, 0, -1):
            if size >= item:
                dp[size] = max(dp[size - item] + item, dp[size])
    # print(dp)
    return dp[-1]

print(backPack(m=10, A=[3,4,5,8]))
