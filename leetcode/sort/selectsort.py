def selectsort(nums):
    n = len(nums)
    for i in range(n-1):
        for j in range(i, n):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


print(selectsort([7, 1, 6, 5, 8, 9, 2, 3, 0, 4]))
