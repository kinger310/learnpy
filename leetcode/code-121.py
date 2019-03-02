def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    buys = [float("inf")] * (len(prices) + 1)
    sells = [0] * (len(prices) + 1)
    max_p = 0
    for i, p in enumerate(prices):
        if p > buys[i]:
            sells[i + 1] = max(sells[i], p)
            buys[i + 1] = buys[i]
        else:
            buys[i+1] = p
        profit = sells[i + 1] - buys[i + 1]
        max_p = max(profit, max_p)
    return max_p

def maxProfit2(prices):
    maxCur = maxSoFar = 0
    for i in range(1, len(prices)):
        maxCur += prices[i] - prices[i-1]
        maxCur = max(0, maxCur)
        maxSoFar = max(maxCur, maxSoFar)
    return maxSoFar
# maxCur = current maximum value
# maxSoFar = maximum value found so far



# print(maxProfit2([7, 3, 5, 2, 6, 4, 1, 7]))
print(maxProfit2([7,5,4,3,1]))
# print(maxProfit2([2,4,1]))