# 荷兰科学家Dijkstra提出，被命名为荷兰旗问题（Dutch National Flag Problem）


def sortColors1(nums: 'List[int]'):
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    j = -1
    for i in range(n):
        if nums[i] == 0:
            j += 1
            if i != j:
                nums[i], nums[j] = nums[j], nums[i]
    for i in range(j+1, n):
        if nums[i] == 1:
            j += 1
            if i != j:
                nums[i], nums[j] = nums[j], nums[i]


# We keep a loop invariant that [0,i) [i, j) [j, k) are 0s, 1s and 2s sorted in place for [0,k).
# Just like the Lomuto partition algorithm usually used in quick sort
def sortColors(nums):
    i = j = 0
    for k in range(len(nums)):
        v = nums[k]
        nums[k] = 2
        if v < 2:
            nums[j] = 1
            j += 1
        if v == 0:
            nums[i] = 0
            i += 1

A = [1,0,2]
sortColors(A)
print(A)