# 1122. Relative Sort Array
# Given two arrays arr1 and arr2, the elements of arr2 are distinct, 
# and all elements in arr2 are also in arr1.

# Sort the elements of arr1 such that the relative ordering of items 
# in arr1 are the same as in arr2.  Elements that don't appear in arr2 should 
# be placed at the end of arr1 in ascending order.

 

# Example 1:

# Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# Output: [2,2,2,1,4,3,3,9,6,7,19]

# Hint: Using a hashmap, we can map the values of arr2 to their position in arr2.

def relativeSortArray(arr1: 'List[int]', arr2: 'List[int]') -> 'List[int]':
    hashmap = {k:idx for idx , k in enumerate(arr2)}
    new_arr1 = []
    for n in arr1:
        if n in hashmap:
            new_arr1.append((n, hashmap[n]))
        else:
            new_arr1.append((n, len(arr2)))
    new_arr1 = sorted(new_arr1, key=lambda x:(x[1], x[0]))
    # print(new_arr1)
    return [x[0] for x in new_arr1]

print(relativeSortArray(arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]))
        