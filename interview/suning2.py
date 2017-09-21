import copy

def print_seq(v, s, i, j):
    if i == 0 or j == 0:
        return
    if v[i][j] == 1:
        print_seq(v, s, i - 1, j - 1)
        print(s[i - 1], end='')
    # 2 向左
    elif v[i][j] == 2:
        print_seq(v, s, i, j -1)
    # 3 向上
    else:
        print_seq(v, s, i-1, j)


if __name__ == '__main__':
    str1 = 'abcdef'
    str2 = 'abfce'
    r = []
    for i in range(len(str1) + 1):
        new = list()
        r.append(new)
        for _ in range(len(str2) + 1):
            r[i].append(0)
    v = copy.deepcopy(r)
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                r[i + 1][j + 1] = r[i][j] + 1
                v[i + 1][j + 1] = 1
            # 2 向右走（取j增）
            elif r[i + 1][j] >= r[i][j + 1]:
                r[i + 1][j + 1] = r[i + 1][j]
                v[i + 1][j + 1] = 2
            # 3 向下走（取i增）
            else:
                r[i + 1][j + 1] = r[i][j + 1]
                v[i + 1][j + 1] = 3

    # 输出一个序列，递归输出
    print_seq(v, str1, len(str1), len(str2))



#
# def diff(w1, w2):
#     count = 0
#     for x, y in zip(w1, w2):
#         if x != y:
#             count += 1
#     return count
#
# def cnt_min_len(start, end, dct):
#     dct.append(end)
#     dict_set = set(dct)
#     res = start
#     count = 0
#     while res != end:
#         for word in dict_set:
#             if diff(res, word) == 1:
#                 res = word
#                 count += 1
#                 dict_set = dict_set - {word}
#                 print(word)
#                 break
#         else:
#             return 0
#     return count
#
# if __name__ == '__main__':
#     start = 'hit'
#     end = 'cog'
#
#     dct = ['hot', 'dog', 'dot', 'lot', 'log']
#     print(cnt_min_len(start, end, dct))
