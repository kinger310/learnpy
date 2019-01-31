# def jump(nums):
#     jumps = curEnd = curFarthest = 0
#     for i, n in enumerate(nums):
#         curFarthest = max(curFarthest, i + n)
#         if i == curEnd:
#             jumps += 1
#             curEnd = curFarthest
#             if curFarthest >= len(nums) - 1:
#                 return jumps
#     return jumps

def jump(nums):
    n, start, end, step = len(nums), 0, 0, 0
    while end < n - 1:
        step += 1
        maxend = end + 1
        for i in range(start, end + 1):
            if i + nums[i] >= n - 1:
                return step
            maxend = max(maxend, i + nums[i])
        start, end = end + 1, maxend
    return step


print(jump([1]))
