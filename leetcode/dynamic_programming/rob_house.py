# 三个大盗的故事


def rob_with_search(nums):
    def search(result, n):
        if n < 0:
            return 0
        result = max(nums[n]+search(result, n-2), search(result, n-1))
        return result

    N = len(nums)
    return search(0, N-1)


def rob_with_cache(nums):
    def search(result, n):
        if n < 0:
            return 0
        if n in cache:
            return cache[n]
        result = max(nums[n]+search(result, n-2), search(result, n-1))
        cache[n] = result
        return result

    cache = {}
    N = len(nums)
    return search(0, N-1)


def rob_with_dp(nums):
    N = len(nums)
    dp = [0] * (N+2)
    for i in range(N):
        dp[i+2] = max(nums[i]+dp[i], dp[i+1])
    return dp[-1]


nums = [2, 7, 9, 3, 1]

print(rob_with_search(nums))
print(rob_with_cache(nums))
print(rob_with_dp(nums))