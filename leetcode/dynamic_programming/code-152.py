
def maxProduct(nums: 'List[int]') -> int:
    max_val = min_val = max_prod = nums[0]
    for i in range(1, len(nums)):
        if nums[i] < 0:
            min_val, max_val = max_val, min_val
        min_val = min(nums[i] * min_val, nums[i])
        max_val = max(nums[i] * max_val, nums[i])
        max_prod = max(max_prod, max_val)
    return max_prod

# print(maxProduct([2,3,-2,4]))
# print(maxProduct([-2]))

print(maxProduct([-2,0,-1, -2, -3]))


