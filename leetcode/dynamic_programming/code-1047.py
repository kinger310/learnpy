# 1049. Last Stone Weight II
# We have a collection of rocks, each rock has a positive integer weight.

# Each turn, we choose any two rocks and smash them together.
# Suppose the stones have weights x and y with x <= y.  The result of this smash is:

# If x == y, both stones are totally destroyed;
# If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
# At the end, there is at most 1 stone left.
# Return the smallest possible weight of this stone (the weight is 0 if there are no stones left.)


# Example 1:

# Input: [2,7,4,1,8,1]
# Output: 1
# Explanation: 
# We can combine 2 and 4 to get 2 so the array converts to [2,7,1,8,1] then,
# we can combine 7 and 8 to get 1 so the array converts to [2,1,1,1] then,
# we can combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we can combine 1 and 1 to get 0 so the array converts to [1] then that's the optimal value.
 

# Note:

# 1 <= stones.length <= 30
# 1 <= stones[i] <= 100


def lastStoneWeightII2(stones: "List[int]") -> int:
    n = len(stones)
    dp = [0] * (2 ** (n+1))
    for k in range(n):
        for j in range(2**(k+1)-1, 2**(k+2)-1, 2):
            dp[j] = dp[j//2] + stones[k]
            dp[j+1] = dp[j//2] - stones[k]
    return min(x for x in dp[2**n-1:2**(n+1)-1] if x >= 0)

def lastStoneWeightII(stones: "List[int]") -> int:
    n = len(stones)
    if n == 0:
        return 0
    my_set = {stones[0]}
    for k in range(1, n):
        new_set = set()
        for j in my_set:
            new_set.add(abs(j + stones[k]))
            new_set.add(abs(j - stones[k]))
        my_set = new_set
    return min(my_set)

print(lastStoneWeightII([31,26,33,21,40]))
print(lastStoneWeightII([2,7,4]))
print(lastStoneWeightII([2,7,4,1]))
print(lastStoneWeightII([2,7,4,1,8]))
print(lastStoneWeightII([2,7,4,1,8,1]))