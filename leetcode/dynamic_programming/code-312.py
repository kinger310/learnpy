#
# 312. Burst Balloons
# Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.
#
# Find the maximum coins you can collect by bursting the balloons wisely.
#
# Note:
#
# You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
# 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
# Example:
#
# Input: [3,1,5,8]
# Output: 167
# Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
#              coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

# 最后一个气球爆炸，一定是1*N*1的。

def maxCoins(nums: 'List[int]') -> int:
    def search(left, right):
        if left + 1 == right:
            return 0
        if (left, right) in cache:
            return cache[(left, right)]
        ans = 0
        for i in range(left + 1, right):
            ans = max(ans, nums[left] * nums[i] * nums[right] + search(left, i) + search(i, right))
        cache[(left, right)] = ans
        return ans

    nums = [1] + nums + [1]
    n = len(nums)
    cache = {}
    return search(0, n - 1)


def maxCoins2(nums: 'List[int]') -> int:
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    # top-down的确定搜索顺序是一件很困难的事情，转换成递归时，需要认真思考
    for k in range(2, n):
        for left in range(0, n - k):
            right = left + k
            for i in range(left + 1, right):
                dp[left][right] = max(dp[left][right], nums[left]*nums[i]*nums[right] + dp[left][i]+ dp[i][right])
    print(dp)
    return dp[0][n - 1]

print(maxCoins([3, 1, 5, 8]))
print(maxCoins2([3, 1, 5, 8]))


import bisect

bisect.bisect([8,5,1,7,10,12], 8)