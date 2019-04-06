# 123. Best Time to Buy and Sell Stock III
# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most two transactions.
#
# Note: You may not engage in multiple transactions at the same time
# (i.e., you must sell the stock before you buy again).
#
# Example 1:
#
# Input: [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
#              Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
# Example 2:
#
# Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
#              Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
#              engaging multiple transactions at the same time. You must sell before buying again.
# Example 3:
#
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

# dp[k, i] = max(dp[k, i-1], prices[i] - prices[j] + dp[k-1, j-1]), j=[0..i-1]

def maxProfit(prices: 'List[int]') -> int:
    if not prices:
        return 0
    n = len(prices)
    dp = [[0]*n for _ in range(3)]
    for k in range(1, 3):
        min_buy = prices[0]
        for i in range(1, n):
            min_buy = min(min_buy, prices[i] - dp[k - 1][i - 1])
            dp[k][i] = max(dp[k][i-1], prices[i] - min_buy)
    return dp[2][n-1]

    # 与单个情形对比
    # n = len(prices)
    # max_profit = [0] * n
    # min_buy = float("inf")
    # for i in range(n):
    #     min_buy = min(min_buy， prices[i])
    #     max_profit[i] = max(max_profit[i-1], prices[i] - min_buy)
    # return max_profit[-1]





print(maxProfit([3,3,5,0,0,3,1,4]))



