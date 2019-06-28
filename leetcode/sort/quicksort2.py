# divide-and-conquer.
# write in 2019年6月27日15:24:07

def conquer(nums, lo, hi):
    pivot = nums[hi]
    # j is fast, i is slow for it grows only when nums[j] < pivot
    # then i stands for the most right element that less than pivot, j-i stands for element bigger than pivot
    # Thus we divide the nums.
    i = lo - 1
    for j in range(lo, hi):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    # Finally exchange i + 1 with pivot
    nums[i + 1], nums[hi] = nums[hi], nums[i + 1]
    return i + 1


def quicksort(nums):
    # divide
    def divide(nums, lo, hi):
        if lo < hi:
            pos = conquer(nums, lo, hi)
            divide(nums, lo, pos - 1)
            divide(nums, pos + 1, hi)

    lo = 0
    hi = len(nums) - 1
    divide(nums, lo, hi)


nn = [7, 1, 6, 5, 8, 9, 2, 3, 0, 4]
quicksort(nn)
print(nn)
