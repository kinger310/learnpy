# Description
#
# Tower of Hanoi problem, is a well-known problem. On the A, B, C three pillars,
# there are n disks of different sizes (radii 1-n), they are stacked in a start on A,
# your goal is to a minimum number of legal steps to move all the plates move from A to C tower tower.
# Each step in the rules of the game are as follows:
#
# Each step is only allowed to move a plate (from the top of one pillars to the top of another pillars)
# The process of moving, you must ensure that a large dish is not at the top of the small plates
# (small can be placed on top of a large, below the maximum plate size can not have any other dish)
# Example
# Example 1:
#
# Input:n = 2
# Output: ["from A to B","from A to C","from B to C"]
# Example 2:
#
# Input:n = 3
# Output:["from A to C","from A to B","from C to B","from A to C","from B to A","from B to C","from A to C"]

# 值得注意的是中间柱子的序号确定。int mid = 3-from-to; 柱子序号设置为0，1，2

def towerOfHanoi(n):
    def hanoi(num, start, end, result):
        if num == 1:
            result.append("from {} to {}".format(tower[start], tower[end]))
            return
        mid = 3 - start - end
        hanoi(num - 1, start, mid, result)
        hanoi(1, start, end, result)
        hanoi(num - 1, mid, end, result)

    result = []
    tower = ["A", "B", "C"]
    hanoi(n, 0, 2, result)
    return result

def towerOfHanoi2(self, n):
    # write your code here
    def hanoi(num, A, B, C, result):
        if num == 1:
            result.append("from {} to {}".format(A, C))
            return
        hanoi(num - 1, A, C, B, result)
        hanoi(1, A, B, C, result)
        hanoi(num - 1, B, A, C, result)

    result = []

    hanoi(n, "A", "B", "C", result)
    return result

print(towerOfHanoi(3))
