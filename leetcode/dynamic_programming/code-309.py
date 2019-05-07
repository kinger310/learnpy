# 309. Best Time to Buy and Sell Stock with Cooldown
# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like
# (ie, buy one and sell one share of the stock multiple times) with the following restrictions:
#
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
# After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
# Example:
#
# Input: [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]

def maxProfit1(prices: 'List[int]') -> int:
    n = len(prices)
    buy = [-10000000] * n
    sell = [0] * n
    rest = [0] * n
    for i, price in enumerate(prices):
        buy[i] = max(rest[i - 1] - price, buy[i - 1])
        sell[i] = max(buy[i - 1] + price, sell[i - 1])
        rest[i] = max(sell[i - 1], buy[i - 1], rest[i - 1])
    return sell[n-1]

# Where price is the price of day i. All of these are very straightforward. They simply represents :
#
# (1) We have to `rest` before we `buy` and
# (2) we have to `buy` before we `sell`
# One tricky point is how do you make sure you sell before you buy,
# since from the equations it seems that [buy, rest, buy] is entirely possible.
#
# Well, the answer lies within the fact that buy[i] <= rest[i] which means rest[i] = max(sell[i-1], rest[i-1]).
# That made sure [buy, rest, buy] is never occurred.
#
# A further observation is that and rest[i] <= sell[i] is also true therefore


def maxProfit2(prices: 'List[int]') -> int:
    n = len(prices)
    buy = [-10000000] * n
    sell = [0] * n
    rest = [0] * n
    for i, price in enumerate(prices):
        buy[i] = max(rest[i - 1] - price, buy[i - 1])
        sell[i] = max(buy[i - 1] + price, sell[i - 1])
        rest[i] = sell[i - 1]
    return sell[n-1]


def maxProfit3(prices: 'List[int]') -> int:
    n = len(prices)
    buy = [-10000000] * n
    sell = [0] * n
    for i, price in enumerate(prices):
        buy[i] = max(sell[i - 2] - price, buy[i - 1])
        sell[i] = max(buy[i - 1] + price, sell[i - 1])

    return sell[n-1]

def maxProfit(prices: 'List[int]') -> int:
    sell = 0
    prev_sell = 0
    buy = float("-inf")
    for price in prices:
        prev_buy = buy
        buy = max(prev_sell - price, prev_buy)
        prev_sell = sell
        sell = max(prev_buy + price, prev_sell)
    return sell


print(maxProfit([1,2,3,0,2]))


