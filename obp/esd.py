# -*- coding: utf-8 -*-

# 生成一组订单，100个order，每个order仅含有一个item，并有item对应location数据
# 数据格式：【order#, aisle#, position#】
# 单区块仓库的布局：仓库是10*40（40 for each side，共800个储位）
# 共有10个aisle，采用ABC分类存储
# #1、2含有50%的demand items， #3,4,5含有35%的demand items, 剩余通道含有15%的demand items

import random
import pandas as pd
import numpy as np

from obp.picker import Picker
from obp.batch import Batch
from obp.opt_best import opt_best


def prod_order(n=100):
    a_aisles = [1, 2]
    b_aisles = [3, 4, 5]
    c_aisles = [6, 7, 8, 9, 10]
    a, b = 0.5, 0.35
    order_list = []
    random.seed(1)
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
    # df.to_csv('./data/orders15.csv', index=False)
    return df


def proc_time(df, para='s'):
    num_item = len(df)
    if para == 's':
        travel = s_shape(df)
    else:
        travel = opt_best(df)
    pt = 3 + num_item / 4 + travel / 20
    # center = (np.mean(df['aisle']), np.mean(df['position']))
    return pd.Series({'weight': num_item, 'pt': pt})


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



def prod_due_dates(df_items, mtcr, p_max):
    df_orders = df_items.groupby(by=['order'])[['aisle', 'position']] \
        .apply(lambda x: proc_time(x, para='o'))
    min_pt, sum_pt = min(df_orders['pt']), sum(df_orders['pt'])
    max_pt = (2 * (1 - mtcr) * sum_pt + min_pt) / p_max
    random.seed(1)
    df_orders['dt'] = [round(random.uniform(min_pt, max_pt), 2) for _ in range(len(df_orders))]
    # df_orders.to_csv('./data/due_dates0.7.csv', index=False)
    return df_orders


def run(p_max, N, C, mtcr):
    # N = 15
    # C = 7
    # # modified traffic congestion rates
    # p_max = 2
    # mtcr = 0.6
    df_items = prod_order(n=N)
    # df_items = pd.read_csv(r'./data/orders15.csv')
    # 采用不同的Routing strategy会产生不同的路径
    # 采用S-shape策略，分奇数通道与偶数通道两种情况处理
    df_orders = prod_due_dates(df_items, mtcr, p_max)
    # df_orders = pd.read_csv('./data/due_dates0.7.csv', index_col=0)
    df_orders = df_orders.sort_values(by=['dt'], ascending=True)

    # 采用Earliest Start Date方法生成初始解
    # 还要计算出Tardiness.
    jobs = init_solution(C, df_items, df_orders, p_max)

    # 计算Tardiness与tardy jobs
    tardy_pair = tard(df_orders, jobs)
    print(p_max, N, C, mtcr, tardy_pair)

def init_solution(C, df_items, df_orders, p_max):
    jobs = []
    sd_p = [0] * p_max
    for p in range(p_max):
        jobs.append(Picker(p, batches=[Batch(b=0, sd=0, pt=0, weight=0, orders=[])]))
    for row in df_orders.itertuples():
        order1, weight, pt = row.Index, row.weight, row.pt
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
            b = len(jobs[p_star].batches)
            jobs[p_star].batches.append(Batch(b=b, sd=sd, pt=0, weight=0, orders=[]))
        batch = jobs[p_star].batches[-1]
        batch.orders.append(order1)
        # 一个batch里的所有orders需要合并在一起计算routing time，而不是pt单纯地相加！
        batch.routing_time(df_items, para='o')
        batch.weight += weight
    return jobs


# objective functions
def tard(df, jobs):
    # 计算Tardiness与tardy jobs
    tardiness = 0
    tardy_jobs = 0
    for job in jobs:
        # print('Picker', job.p)
        # count = 0
        for batch in job.batches:
            # print('Batch' + str(count), batch.weight)
            # count += 1
            ct = batch.sd + batch.pt
            for order in batch.orders:
                dt = df.loc[order, 'dt']
                # weight = df.loc[order, 'weight']
                # print(order, weight, ct, dt, max(0, ct - dt))
                if ct > dt:
                    tardiness += ct - dt
                    tardy_jobs += 1
    # return tardy_jobs, tardiness
    return tardiness, tardy_jobs


def main():
    P_MAX = [2, 4]
    N = [50, 100]
    C = [10, 20]
    MTCR = [0.6, 0.7, 0.8]
    for p_max in P_MAX:
        for n in N:
            for c in C:
                for mtcr in MTCR:
                    run(p_max, n, c, mtcr)
    # run(1, 1, 1, 1)
    print('ok')


if __name__ == '__main__':
    main()
