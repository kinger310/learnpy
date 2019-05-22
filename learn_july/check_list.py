def check_list(nums):
    if len(nums) < 2:
        return "wrong"
    if nums[0] < nums[1]:
        asc_flag = 1
    elif nums[0] == nums[1]:
        asc_flag = 0
    else:
        asc_flag = -1

    if asc_flag == 1:
        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return "wrong"
        return "asc"
    elif asc_flag == -1:
        for i in range(1, len(nums) - 1):
            if nums[i] < nums[i + 1]:
                return "wrong"
        return "desc"
    else:
        return check_list(nums[2:])


print(check_list([1,1,1]))
print(check_list([1,1]))

