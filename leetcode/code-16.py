def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    result = 0
    if not nums:
        return 0
    nums.sort()
    tmp = float("inf")
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        lo = i + 1
        hi = len(nums) - 1
        while lo < hi:
            s = nums[i] + nums[lo] + nums[hi]
            if abs(s - target) < tmp:
                result = s
                tmp = abs(s - target)
            if s < target:
                lo += 1
            elif s > target:
                hi -= 1
            else:
                return target
    return result


nums = [-1, 1, -4, 3, 0, 1]
print(threeSumClosest(nums, 1))
