def insertsort(nums):
    # 插入排序
    n = len(nums)
    for i in range(1, n):
        for j in range(i):
            if nums[j] > nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


print(insertsort([7, 1, 6, 5, 8, 9, 2, 3, 0, 4]))
