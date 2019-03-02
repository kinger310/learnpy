from leetcode.listnode import timethis


# This is intuitive recursion algorithm with no cache
@timethis
def coinChange(coins: 'List[int]', amount: 'int') -> 'int':
    def f(remain):
        if remain < 0:
            return -1
        if remain == 0:
            return 0
        min_val = amount + 1
        for coin in coins:
            res = f(remain - coin)
            if 0 <= res < min_val:
                min_val = res + 1
        if min_val > amount:
            min_val = -1
        return min_val

    if amount < 1:
        return 0
    return f(amount)


# This is recursion algorithm with cache(Top down algorithm)
@timethis
def coinChange2(coins: 'List[int]', amount: 'int') -> 'int':
    def f(remain):
        if remain < 0:
            return -1
        if remain == 0:
            return 0
        if remain in cache:
            return cache[remain]
        min_val = amount + 1
        for coin in coins:
            res = f(remain - coin)
            if 0 <= res < min_val:
                min_val = res + 1
        if min_val > amount:
            min_val = -1
        cache[remain] = min_val
        return min_val

    if amount < 1:
        return 0
    cache = {}
    return f(amount)


# This is dynamic programming algorithm. (Bottom up algorithm)
@timethis
def coinChange3(coins: 'List[int]', amount: 'int') -> 'int':
    # dp[]. INIT value should be bigger than amount. amount + 1
    # dp[0] = 0. For amount = 0, no coins change.
    INIT = amount + 1
    dp = [INIT] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:  # s.t. i(current amount) >= coin
                dp[i] = min(dp[i], dp[i - coin] + 1)
    if dp[amount] > amount:
        dp[amount] = -1
    return dp[amount]


# print(coinChange2([2, 5], 3))
print(coinChange2([1, 2, 5], 501))
print(coinChange3([1, 2, 5], 10000))

import  math

math.factorial(3)