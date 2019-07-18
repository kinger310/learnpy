# 967. Numbers With Same Consecutive Differences
# Return all non-negative integers of length N such that the absolute difference
#  between every two consecutive digits is K.

# Note that every number in the answer must not have leading zeros except for the number 0 itself. 
# For example, 01 has one leading zero and is invalid, but 0 is valid.

# You may return the answer in any order.

# Example 1:

# Input: N = 3, K = 7
# Output: [181,292,707,818,929]
# Explanation: Note that 070 is not a valid number, because it has leading zeroes.
# Example 2:

# Input: N = 2, K = 1
# Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
 

# Note:

# 1 <= N <= 9
# 0 <= K <= 9

def numsSameConsecDiff(N, K):
    """
    :type N: int
    :type K: int
    :rtype: List[int]
    """
    def search(result, i, number):
        if i == N:
            result.append(number)
            return
        if i == 0:
            for n in range(1, 10):
                search(result, 1, number*10+n)
        else:
            for n in range(10):
                if abs(number%10 - n) == K:
                    search(result, i+1, number*10+n)
    if N == 1:
        return list(range(10))

    result = []
    search(result, 0, 0)
    return result

print(numsSameConsecDiff(1, 0))
print(numsSameConsecDiff(2,1))
print(numsSameConsecDiff(3,7))
print(numsSameConsecDiff(3,1))

