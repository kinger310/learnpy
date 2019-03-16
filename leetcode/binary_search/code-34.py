def searchRange(nums: 'List[int]', target: 'int') -> 'List[int]':
    lo = 0
    hi = len(nums)
    target_flag = False
    tmp = -1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        elif nums[mid] > target:
            hi = mid
        else:
            target_flag = True
            tmp = mid
            break

    # this seems O(N). need O(logN)
    start = end = tmp
    if target_flag:
        while start >= 0 and nums[start] == nums[tmp]:
            start -= 1
        while end <= len(nums) - 1 and nums[end] == nums[tmp]:
            end += 1
        return start + 1, end - 1
    else:
        return -1, -1

import bisect
def searchRange2(nums, target):
    lo = bisect.bisect_left(nums, target)
    return [lo, bisect.bisect(nums, target)-1] if target in nums[lo:lo+1] else [-1, -1]

nums = [7,8,8,8,9,10]
print(searchRange(nums, 8))