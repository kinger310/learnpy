def lengthOfLIS(nums: 'List[int]') -> int:
    nums.append(float("inf"))
    n = len(nums)
    dp = [0] * n

    for idx in range(1, n):
        ans = 0
        for i in range(idx - 1, -1, -1):
            if nums[idx] > nums[i]:
                ans = max(ans, dp[i]+1)
        dp[idx] = ans
    return dp[-1]

print(lengthOfLIS([]))
print(lengthOfLIS([10]))
print(lengthOfLIS([10,11]))
print(lengthOfLIS([10,9,2,5,3,7,101,18]))

print(lengthOfLIS([4,10,4,3,8,9]))