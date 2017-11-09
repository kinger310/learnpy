# -*- coding: utf-8 -*-

# 生成一组订单，100个order，每个order仅含有一个item，并有item对应location数据
# 数据格式：【order#, aisle#, position#】
# 单区块仓库的布局：仓库是10*40（40 for each side，共800个储位）
# 共有10个aisle，采用ABC分类存储
# #1、2含有50%的demand items， #3,4,5含有35%的demand items, 剩余通道含有15%的demand items

import random
import pandas as pd
import numpy as np

class Picker(object):
    def __init__(self, p, batches=None):
        self.p = p
        self.batches = batches


class Batch(object):
    def __init__(self, sd=0, pt=0, weight=0, orders=None):
        self.sd = sd
        self.pt = pt
        self.weight = weight
        self.orders = orders

    def routing_time(self, df, strategy='s'):
        df_orders = df[df['order'].isin(self.orders)]
        num_item = len(df_orders)
        if strategy == 's':
            travel = s_shape(df_orders)
        else:
            travel = 0
        self.pt = 3 + num_item / 4 + travel / 20


def prod_order(n=100):
    a_aisles = [1, 2]
    b_aisles = [3, 4, 5]
    c_aisles = [6, 7, 8, 9, 10]
    a, b = 0.5, 0.35
    order_list = []
    for i in range(n):
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


def proc_time(df, para='s'):
    num_item = len(df)
    if para == 's':
        travel = s_shape(df)
    else:
        travel = large_gap(df)
    pt = 3 + num_item / 4 + travel / 20
    return pt


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


def run(p_max, N, C, mtcr):
    # N = 100
    # C = 10
    # # modified traffic congestion rates
    # p_max = 2
    # mtcr = 0.6
    df_orders = prod_order(n=N)
    # df_orders = pd.read_csv(r'./data/orders.csv')
    # 采用不同的Routing strategy会产生不同的路径
    # 采用S-shape策略，分奇数通道与偶数通道两种情况处理
    df_num = df_orders.groupby(by=['order']).apply(lambda x: len(x)).reset_index(name='weight')
    df_pt = df_orders.groupby(by=['order'])[['aisle', 'position']]\
        .apply(lambda x: proc_time(x, para='s')).reset_index(name='pt')
    df_pt = pd.merge(df_num, df_pt, how='inner', on=['order'])

    min_pt, sum_pt = min(df_pt['pt']), sum(df_pt['pt'])
    max_pt = (2 * (1 - mtcr) * sum_pt + min_pt) / p_max
    df_pt['dt'] = [round(random.uniform(min_pt, max_pt), 2) for _ in range(len(df_pt))]
    # df_pt.to_csv('./data/due_dates.csv', index=False)
    # df_pt = pd.read_csv('./data/due_dates.csv')
    df_pt = df_pt.sort_values(by=['dt'], ascending=True)

    # 采用Earliest Start Date方法生成初始解
    # 还要计算出Tardiness.

    jobs = []
    sd_p = [0] * p_max
    for p in range(p_max):
        jobs.append(Picker(p, batches=[Batch(sd=0, pt=0, weight=0, orders=[])]))
    for row in df_pt.itertuples():
        order, weight, pt = row.order, row.weight, row.pt
        for picker in jobs:
            batch = picker.batches[-1]
            # 如果可以分配给last position batch， sd_p就是last batch 的sd
            if batch.weight + weight <= C:
                # CASE 1
                sd_p[picker.p] = (batch.sd, 1)
            else:
                # CASE 2
                ct = batch.sd + batch.pt
                sd_p[picker.p] = (ct, 2)
        p_star = sd_p.index(min(sd_p))
        case = sd_p[p_star][1]
        if case == 2:
            prev = jobs[p_star].batches[-1]
            sd = prev.sd + prev.pt
            jobs[p_star].batches.append(Batch(sd=sd, pt=0, weight=0, orders=[]))
        batch = jobs[p_star].batches[-1]
        # TODO 不是那么简单的加和，而是要计算combine在一块的pt时间
        batch.orders.append(order)
        batch.routing_time(df_orders)
        batch.weight += weight
    # 计算Tardiness与tardy jobs
    tardiness = 0
    tardy_jobs = 0
    for job in jobs:
        for batch in job.batches:
            # 一个batch里的所有orders需要合并在一起，而不是pt单纯地相加
            ct = batch.sd + batch.pt
            for order in batch.orders:
                dt = float(df_pt.loc[df_pt['order'] == order, 'dt'])
                if ct > dt:
                    tardiness += ct - dt
                    tardy_jobs += 1
    print(p_max, N, C, mtcr, tardiness, tardy_jobs)



def main():
    P_MAX = [2, 3, 5, 8]
    N = [100, 200]
    C = [10, 20]
    MTCR = [0.6, 0.7, 0.8]
    for p_max in P_MAX:
        for n in N:
            for c in C:
                for mtcr in MTCR:
                    run(p_max, n, c, mtcr)
    print('ok')


if __name__ == '__main__':
    main()
