

def search(nums: 'List[int]', target: 'int') -> 'int':
    lo = 0
    hi = len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if (target < nums[0]) == (nums[mid] < nums[0]):
            n = nums[mid]
        elif target < nums[0]:
            n = float("-inf")
        else:
            n = float("inf")
        if n < target:
            lo = mid + 1
        elif n > target:
            hi = mid
        else:
            return mid
    return -1



nums = [6,7,0,1,2,4,5]
print(search(nums, 3))
