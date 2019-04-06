

# This is a TLE solution.
def largestRectangleArea2(heights: 'List[int]') -> int:
    n = len(heights)
    max_val = 0
    for i in range(n):
        min_val = heights[i]
        max_val = max(max_val, min_val)
        for j in range(i-1, -1, -1):
            min_val = min(heights[j], min_val)
            max_val = max(max_val, min_val * (i - j + 1))
    return max_val

def largestRectangleArea(heights: 'List[int]') -> int:
    # The stack maintain the indexes of buildings with ascending height.
    n = len(heights)
    heights.append(0)
    stack = []
    ans = 0
    i = 0
    while i <= n:
        if not stack or heights[i] >= heights[stack[-1]]:
            stack.append(i)
        else:
            tp = stack.pop()
            if stack:
                ans = max(ans, heights[tp] * (i - stack[-1] - 1))
            else:
                ans = max(ans, heights[tp] * i)
            i -= 1
        i += 1

    return ans

# print(largestRectangleArea([2, 1, 5, 6, 2, 3]))  # expect 10 (2*5)
# print(largestRectangleArea([2, 1, 3, 6, 2, 3]))# expect 8 (4*2)
# print(largestRectangleArea([2,3]))
# print(largestRectangleArea([3]))
print(largestRectangleArea(list(range(10))))
