def bubblesort(nums):
    n = len(nums)
    for i in range(n - 1, -1, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


print(bubblesort([7, 1, 6, 5, 8, 9, 2, 3, 0, 4]))
