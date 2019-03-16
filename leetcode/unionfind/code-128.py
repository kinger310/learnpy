# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
#
# Your algorithm should run in O(n) complexity.
#
# Example:
#
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# brute force
def longestConsecutive1(nums: 'List[int]') -> 'int':
    max_ans = 0
    for num in nums:
        cur_num = num
        ans = 1
        while cur_num + 1 in nums:
            cur_num += 1
            ans += 1
        max_ans = max(ans, max_ans)
    return max_ans

def longestConsecutive2(nums: 'List[int]') -> 'int':
    max_ans = 0
    nums.sort()
    ans = 1
    for i in range(1, len(nums)):
        cur_num = nums[i-1]
        if cur_num == nums[i] - 1:
            cur_num += 1
            ans += 1
        else:
            ans = 1
        max_ans = max(ans, max_ans)
    return max_ans

# HashSet and Intelligent Sequence Building
def longestConsecutive3(nums: 'List[int]') -> 'int':
    max_ans = 0
    num_set = set(nums)
    for num in num_set:
        if num - 1 not in num_set:
            cur_num = num
            ans = 1
            while cur_num + 1 in nums:
                cur_num += 1
                ans += 1
            max_ans = max(ans, max_ans)
    return max_ans

# Time complexity : O(n).
#
# Although the time complexity appears to be quadratic due to the while loop nested within the for loop,
# closer inspection reveals it to be linear.
# Because the while loop is reached only when currentNum marks the beginning of a sequence
# (i.e. currentNum-1 is not present in nums),
# the while loop can only run for nn iterations throughout the entire runtime of the algorithm.
# This means that despite looking like O(n⋅n) complexity,
# the nested loops actually run in O(n + n) = O(n)O(n+n)=O(n) time.
# All other computations occur in constant time, so the overall runtime is linear.


# Using union find
def longestConsecutive4(nums):
    uf = UF(len(nums))
    dct ={}
    for i in range(len(nums)):
        if nums[i] in dct:
            continue
        dct[nums[i]] = i
        if nums[i] + 1 in dct:
            uf.union(i, dct[nums[i]+1])
        if nums[i] - 1 in dct:
            uf.union(i, dct[nums[i]-1])

    return uf.maxUnion()


class UF:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.count = [1 for _ in range(n)]

    def root(self, i):
        # iterative
        # while i != self.par[i]:
        #     self.par[i] = self.par[self.par[i]]
        #     i = self.par[i]
        # return i

        # recursion
        if i == self.par[i]:
            return i
        p = self.root(self.par[i])
        self.par[i] = p  # path compression, i's parent is p
        return p

    def connected(self, i, j):
        return self.root(i) == self.root(j)

    # union by size
    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        newCount = self.count[i] + self.count[j]
        if self.count[i] <= self.count[j]:
            self.par[i] = j
            self.count[j] = newCount
        else:
            self.par[j] = i
            self.count[i] = newCount

    # returns the maxium size of union
    def maxUnion(self):
        # cnt = [0] * len(self.par)
        # m = 0
        # for i in range(len(self.par)):
        #     cnt[self.root(i)] += 1
        #     m = max(m, cnt[self.root(i)])
        # return m
        return max(self.count)


print(longestConsecutive4([100, 4, 200, 1, 3, 2]))
# print(longestConsecutive4([9,1,4,7,3,-1,0, 5,8,-1,6]))

# def root(i, lst):
#     print(i, lst[i])
#     while i != lst[i]:
#         lst[i] = lst[lst[i]]
#         i = lst[i]
#         print(i, lst[i])
#     return i

#
# def root(i):
#     # recursion
#     if i == lst[i]:
#         return i
#     p = root(lst[i])
#     lst[i] = p
#     return p

# lst = [0, 3, 2, 3, 1, 1]
# print(root(4))
