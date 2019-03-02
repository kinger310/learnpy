def maxSubArray(nums: 'List[int]') -> 'int':
    dp = [float("-inf")] * (len(nums) + 1)
    cache = [0] * (len(nums) + 1)
    for i, n in enumerate(nums):
        cache[i+1] = max(cache[i] + n, n)
        dp[i+1] = max(dp[i], cache[i+1])

    return dp[-1]

print(maxSubArray([-2,1,-3,4,-1,2,1,-2,7,-5]))
