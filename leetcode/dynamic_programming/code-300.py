# 300. Longest Increasing Subsequence
# Given an unsorted array of integers, find the length of longest increasing subsequence.
#
# Example:
#
# Input: [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Note:
#
# There may be more than one LIS combination, it is only necessary for you to return the length.
# Your algorithm should run in O(n2) complexity.
# Follow up: Could you improve it to O(n log n) time complexity?

# backtracking with cache(top-down)
def lengthOfLIS(nums: 'List[int]') -> int:
    def search(idx):
        if idx < 0:
            return 0
        if dp[idx] > 0:
            return dp[idx]
        ans = 0
        for i in range(idx):
            if nums[idx] > nums[i]:
                ans = max(ans, search(i))
        dp[idx] = ans + 1
        return dp[idx]

    nums.append(float("inf"))
    n = len(nums)
    dp = [0] * n
    result = search(n - 1) - 1  # 从后往前搜
    return result


# dynamic programming(bottom-up)
def lengthOfLIS2(nums: 'List[int]') -> int:
    nums.append(float("inf"))
    n = len(nums)
    dp = [0] * n
    for idx in range(1, n):
        ans = 0
        for i in range(idx):
            if nums[idx] > nums[i]:
                ans = max(ans, dp[i])
        dp[idx] = ans + 1
    return dp[n - 1] - 1


# dynamic programming improvement. (find search rules)
def lengthOfLIS3(nums: 'List[int]') -> int:
    nums.append(float("inf"))
    n = len(nums)
    dp = [0] * (n + 1)
    mins = [float("inf")] * (n + 1)
    path = 0
    for idx in range(n):
        ans = 0
        for i in range(1, path + 1):
            if nums[idx] > mins[i]:
                ans = max(ans, i)
        dp[idx] = ans + 1
        mins[dp[idx]] = min(mins[dp[idx]], nums[idx])
        path = max(path, dp[idx])
    return dp[n - 1] - 1


# dynamic programming improvement. (find search rules)
def lengthOfLIS4(nums: 'List[int]') -> int:
    nums.append(float("inf"))
    n = len(nums)
    dp = [0] * (n + 1)
    mins = [float("inf")] * (n + 1)
    path = 0
    for idx in range(n):
        ans = 0
        for i in range(path, 0, -1):
            if nums[idx] > mins[i]:
                ans = i
                break
        dp[idx] = ans + 1
        mins[dp[idx]] = min(mins[dp[idx]], nums[idx])
        path = max(path, dp[idx])
    return dp[n - 1] - 1


# dynamic programming improvement. (binary search)
# 视频54min 处
def lengthOfLIS5(nums: 'List[int]') -> int:
    nums.append(float("inf"))
    n = len(nums)
    # dp = [0] * (n + 1) # dp也可以优化
    dp = 0
    mins = [float("inf")] * (n + 1)
    path = 0
    for idx in range(n):
        ans = 0
        # for i in range(path, 0, -1):
        #     if nums[idx] > mins[i]:
        #         ans = i
        #         break
        # 分析mins是一个单调递增的序列，有单调性，就可以用binary search
        lo, hi = 1, path  # 左闭右闭区间
        while lo <= hi:  # 注意开闭
            mid = (lo+hi)//2
            if nums[idx] > mins[mid]:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        dp = ans + 1
        mins[dp] = min(mins[dp], nums[idx])
        path = max(path, dp)
    return dp - 1

# print(lengthOfLIS3([]))
# print(lengthOfLIS3([10,11]))
# print(lengthOfLIS3([10,9]))
# print(lengthOfLIS2([10,9,2,5,3,7,101,18]))
print(lengthOfLIS4([10, 9, 2, 5, 3, 7, 101, 18]))
print(lengthOfLIS4([4,10,4,3,8,9]))
print(lengthOfLIS5([10, 9, 2, 5, 3, 7, 101, 18]))
print(lengthOfLIS5([4,10,4,3,8,9]))
# # optimize: 2 5 3
# which LIS is better?
