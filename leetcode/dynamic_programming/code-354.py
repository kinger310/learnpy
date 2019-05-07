# 354. Russian Doll Envelopes
# You have a number of envelopes with widths and heights given as a pair of integers (w, h).
# One envelope can fit into another if and only if both the width and height of one envelope is
# greater than the width and height of the other envelope.
#
# What is the maximum number of envelopes can you Russian doll? (put one inside other)
#
# Note:
# Rotation is not allowed.
#
# Example:
#
# Input: [[5,4],[6,4],[6,7],[2,3]]
# Output: 3
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).


def maxEnvelopes(envelopes: 'List[List[int]]') -> int:
    envelopes.sort(key=lambda k: (k[0], -k[1]))
    heights = [x[1] for x in envelopes]
    return lengthOfLIS(heights)


def lengthOfLIS(nums: 'List[int]') -> int:
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
            mid = (lo + hi) // 2
            if nums[idx] > mins[mid]:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        dp = ans + 1
        mins[dp] = min(mins[dp], nums[idx])
        path = max(path, dp)
    return dp - 1


print(maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))

print(maxEnvelopes([]))


# The idea is to order the envelopes and then calculate the longest increasing subsequence (LISS).
# We first sort the envelopes by width, and we also make sure that when the width is the same,
# the envelope with greater height comes first. Why? This makes sure that when we calculate the LISS,
# we don't have a case such as [3, 4] [3, 5]
# (we could increase the LISS but this would be wrong as the width is the same.
# It can't happen when [3, 5] comes first in the ordering).
