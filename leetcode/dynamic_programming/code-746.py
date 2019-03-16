def minCostClimbingStairs(cost: 'List[int]') -> 'int':
    # f1 = f2 = 0
    # for x in reversed(cost):
    #     tmp = x + min(f1, f2)
    #     f2 = f1
    #     f1 = tmp
    n = len(cost)
    dp = [0]*(n+2)
    for i in range(2, n+2):
        dp[i] = cost[i-2] + min(dp[i-1], dp[i-2])
    return min(dp[n+1], dp[n])


print(minCostClimbingStairs([10, 15]))
print(minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
