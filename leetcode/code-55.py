def canJump(nums):
    lens = len(nums)
    lim = 0
    for i in range(lens-1):
        lim = max(nums[i] + i, lim)
        print(i, lim)
        if lim >= lens-1:
            return True
        elif lim == i:
            return False
        else:
            pass



# print(canJump([2,4,1,0,1,1,4]))
print(canJump([2,3,1,1,4]))
# print(canJump([3,2,1,0,1,4]))