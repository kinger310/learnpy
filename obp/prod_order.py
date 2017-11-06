# -*- coding: utf-8 -*-

# 生成一组订单，100个order，每个order仅含有一个item，并有item对应location数据
# 数据格式：【order#, aisle#, position#】
# 单区块仓库的布局：仓库是10*40（40 for each side，共800个储位）
# 共有10个aisle，采用ABC分类存储
# #1、2含有50%的demand items， #3,4,5含有35%的demand items, 剩余通道含有15%的demand items

import random
import pandas as pd
import numpy as np


def prod_order():
    N = 100
    a_aisles = [1, 2]
    b_aisles = [3, 4, 5]
    c_aisles = [6, 7, 8, 9, 10]
    a, b = 0.5, 0.35
    order_list = []
    for i in range(N):
        m = random.randint(1, 5)
        for _ in range(m):
            p = random.random()
            if p <= a:
                aisle = random.choice(a_aisles)
            elif p <= a + b:
                aisle = random.choice(b_aisles)
            else:
                aisle = random.choice(c_aisles)
            position = random.randint(1, 40)
            order_data = ('o' + str(i + 1).zfill(3), aisle, position)
            order_list.append(order_data)
    df = pd.DataFrame(data=order_list, columns=['order', 'aisle', 'position'])
    # df.to_csv('./data/orders.csv', index=False)
    return df


def proc_time(df, para='s_shape'):
    num_item = len(df)
    if para == 's_shape':
        travel = s_shape(df)
    else:
        travel = large_gap(df)
    proc_time = 3 + num_item / 4 + travel / 20
    return proc_time


def s_shape(df):
    h_unit = 5
    v_unit = 40
    aisle_lst = sorted(set(df['aisle']))
    max_a = max(aisle_lst)
    num_a = len(aisle_lst)
    if num_a % 2 != 0:
        pos = max(df[df['aisle'] == max_a]['position'])
        travel = 2 + (max_a - 1) * h_unit * 2 + (num_a - 1) * v_unit + pos * 2
    else:
        travel = 2 + (max_a - 1) * h_unit * 2 + num_a * v_unit
    return travel


def large_gap(df):
    travel = 1
    return travel

def main():
    # df_orders = prod_order()
    df_orders = pd.read_csv(r'./data/orders.csv')
    # 采用不同的Routing strategy会产生不同的路径
    # 采用S-shape策略，分奇数通道与偶数通道两种情况处理
    df_pt = df_orders.groupby(by=['order'])[['aisle', 'position']]\
        .apply(lambda x: proc_time(x, para='s_shape')).reset_index(name='pt')
    # modified traffic congestion rates
    p_max, mtcr = 2, 0.6
    min_pt, sum_pt = min(df_pt['pt']), sum(df_pt['pt'])
    max_pt = (2 * (1 - mtcr) * sum_pt + min_pt) / p_max
    df_pt['dt'] = [round(random.uniform(min_pt, max_pt), 2) for _ in range(len(df_pt))]
    print('ok')





if __name__ == '__main__':
    main()
