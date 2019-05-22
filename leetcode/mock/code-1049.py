def lastStoneWeightII(stones: 'List[int]') -> int:
    dp = {0}
    for stone in stones:
        new_set = set()
        for j in dp:
            new_set.add(abs(j + stone))
            new_set.add(abs(j - stone))
        dp = new_set
    return min(dp)

def lastStoneWeightII1(stones: 'List[int]') -> int:
    dp = {0}
    for a in stones:
        dp = {abs(a + x) for x in dp} | {abs(a - x) for x in dp}
    return min(dp)

print(lastStoneWeightII([2,7,4,1,8,1]))
print(lastStoneWeightII([22,30,36,83,26,20,23,73,25,22,42,55,29,3,31,19,12,32,2,13,14,27,24,26]))

