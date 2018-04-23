# -*- coding: utf-8 -*-

import pandas as pd
import random
import math


def distance(item1, item2):
    h_unit = 5
    v_unit = 40
    w_unit = 3
    x1, y1, x2, y2 = item1[0], item1[1], item2[0], item2[1]
    if x1 != x2:
        return min(2 * v_unit - y1 - y2, y1 + y2) + (abs(x1 - x2) - 1) * w_unit + h_unit
    else:
        return abs(y1 - y2)


def path_dis(indexList, arr):
    sum = 0.0
    for i in range(len(indexList) - 1):
        sum += distance(arr[indexList[i]], arr[indexList[i + 1]])
    return sum


def s_shape_ini(df):
    aisle_lst = sorted(set(df['aisle']))
    df_lst = []
    for i in range(len(aisle_lst)):
        if i % 2 == 1:
            df_part = df[df['aisle'] == aisle_lst[i]].sort_values(['position'])
        else:
            df_part = df[df['aisle'] == aisle_lst[i]].sort_values(['position'], ascending=False)
        df_lst.append(df_part)
    df_result = pd.concat(df_lst)
    sol = list(df_result.index)
    sol.append(0)
    return sol


def update2opt(best_path, arr):
    count = 0
    if len(best_path) > 3:
        while count < 50:
            # print(calPathDist(best_path))
            # print(best_path.tolist())
            a, b = sorted(random.sample(range(1, len(best_path) - 1), 2))
            rev_path = best_path[:a] + best_path[b:a - 1:-1] + best_path[b + 1:]
            if path_dis(rev_path, arr) < path_dis(best_path, arr):
                count = 1
                best_path = rev_path
            else:
                count += 1
    return best_path


def sa_opt(best_path, arr):
    count = 0
    if len(best_path) > 3:
        at, T = 0.95, 10
        while count < 50:
            a, b = sorted(random.sample(range(1, len(best_path) - 1), 2))
            rev_path = best_path[:a] + best_path[b:a - 1:-1] + best_path[b + 1:]
            delta = path_dis(rev_path, arr) - path_dis(best_path, arr)
            if delta <= 0:
                count = 1
                best_path = rev_path
            elif math.exp(-delta / T) >= random.random():
                count = 1
                best_path = rev_path
            else:
                count += 1
            T *= at
    return best_path


def opt_best(df):
    df_new = df[['aisle', 'position']].drop_duplicates()
    df_new.loc[-1] = [0, 0]
    df_new.index += 1
    df_new = df_new.sort_index().reset_index(drop=True)
    arr = df_new.as_matrix()
    best_path = s_shape_ini(df_new)
    best_path = sa_opt(best_path, arr)
    # best_path = update2opt(best_path, arr)
    travel = path_dis(best_path, arr)
    return travel


if __name__ == '__main__':
    df = pd.DataFrame({'aisle':[3,2,3,2,3,1], 'position':[17,31,32,28,29,38]})
    t = opt_best(df)
