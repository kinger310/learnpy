from itertools import combinations


def foo(height):
    i, j = 0, len(height)-1
    area = 0
    while i < j:
        area = max(area, (j - i) * min(height[i], height[j]))
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return area


height = [1, 1, 6, 2, 5, 4, 8, 3, 5]
print(foo(height))

err = []
try:
    for i in range(10, -2, -1):
        div = 10/i
        print(div)
except:
    err.append(i)
for x in err:
    print(x)

