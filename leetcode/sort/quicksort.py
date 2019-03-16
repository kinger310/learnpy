def quicksort(nums):
    def partition(nums, lo, hi):
        pivot = nums[hi]
        i = lo - 1
        for j in range(lo, hi):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[hi] = nums[hi], nums[i + 1]
        return i + 1

    def quick(nums, lo, hi):
        if lo < hi:
            p = partition(nums, lo, hi)
            quick(nums, lo, p - 1)
            quick(nums, p + 1, hi)

    lo = 0
    hi = len(nums) - 1
    quick(nums, lo, hi)
    return nums


print(quicksort([7, 1, 6, 5, 8, 9, 2, 3, 0, 4]))
