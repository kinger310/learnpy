# 174. Dungeon Game

# The demons had captured the princess(P) and imprisoned her in the bottom - right corner of a dungeon.
# The dungeon consists of M x N rooms laid out in a 2 D grid.Our valiant knight(K) was initially positioned
#  in the top - left room and must fight his way through the dungeon to rescue the princess.

# The knight has an initial health point represented by a positive integer.If at any point his health point
#  drops to 0 or below, he dies immediately.

# Some of the rooms are guarded by demons, so the knight loses health(negative integers) upon entering these rooms; 
# other rooms are either empty(0 's) or contain magic orbs that increase the knight' s health(positive integers).

# In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

#     Write a function to determine the knight 's minimum initial health so that he is able to rescue the princess.

# For example, given the dungeon below, the initial health of the knight must be at least 7 
# if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.
# [
#     [-2,  -3,  3],
#     [-5, -10,  1],
#     [10,  30, -5]
# ]
# Note:

# The knight's health has no upper bound. Any room can contain threats or power - ups, 
# even the first room the knight enters and the bottom - right room where the princess is imprisoned.


def calculateMinimumHP1(dungeon: 'List[List[int]]') -> int:
    m = len(dungeon)
    n = len(dungeon[0])
    dp = [[0] * n for _ in range(m)]
    dp[-1][-1] = max(-dungeon[-1][-1]+1, 1)
    for i in range(m-2, -1, -1):
        dp[i][-1] = dp[i+1][-1] - dungeon[i][-1]
        if dp[i][-1] <= 0:
            dp[i][-1] = 1
    for j in range(n-2, -1, -1):
        dp[-1][j] = dp[-1][j+1] - dungeon[-1][j]
        if dp[-1][j] <= 0:
            dp[-1][j] = 1
    for i in range(m-2, -1, -1):
        for j in range(n-2, -1, -1):
            dp[i][j] = min(dp[i][j+1], dp[i+1][j]) - dungeon[i][j]
            if dp[i][j] <= 0:
                dp[i][j] = 1
    return dp[0][0]


def calculateMinimumHP(dungeon: 'List[List[int]]'):
    m = len(dungeon)
    n = len(dungeon[0])
    dp = [[float("inf")] * (n+1) for _ in range(m+1)]
    dp[m][n-1] = dp[m-1][n] = 1
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            dp[i][j] = max(min(dp[i][j + 1], dp[i + 1][j]) - dungeon[i][j], 1)
    return dp[0][0]

print(calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))
print(calculateMinimumHP([[0,0,0],[1,1,-1]]))