# import numpy as np
#
#
# def distance(item1, item2):
#     h_unit = 5
#     v_unit = 40
#     w_unit = 3
#     x1, y1, x2, y2 = item1[0], item1[1], item2[0], item2[1]
#     if x1 != x2:
#         return min(2 * v_unit - y1 - y2, y1 + y2) + (abs(x1 - x2) - 1) * w_unit + h_unit
#     else:
#         return abs(y1 - y2)
#
#
# def path_dis(indexList, arr):
#     sum = 0.0
#     for i in range(len(indexList) - 1):
#         sum += distance(arr[indexList[i]], arr[indexList[i + 1]])
#     return sum
#
#
# arr = np.array([[0, 0], [3, 17],
#                   [2, 31],
#                   [3, 32],
#                   [2, 28],
#                   [3, 29],
#                   [1, 38]])
#
# path = [0, 6, 2, 4, 1, 5, 3, 0]
#
# path_dis(path, arr)

with open(r'C:\Users\wangdi\Desktop\opt结果.txt', errors='ignore') as file:
    for line in file:
        if line.startswith('t') or line.startswith('D'):
            print(line)

