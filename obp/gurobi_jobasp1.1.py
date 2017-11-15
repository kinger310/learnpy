# -*- coding: utf-8 -*-
# # http://examples.gurobi.com/traveling-salesman-problem/#demo

import pandas as pd
import math
import random
from gurobipy import Model, GRB, quicksum

from obp.batch import Batch
from obp.picker import Picker

# objective functions
def tard(df, jobs):
    # 计算Tardiness与tardy jobs
    tardiness = 0
    tardy_jobs = 0
    for job in jobs:
        print('Picker', job.p)
        count = 0
        for batch in job.batches:
            print('Batch' + str(count), batch.weight)
            count += 1
            ct = batch.sd + batch.pt
            for order in batch.orders:
                dt = df.loc[order, 'dt']
                weight = df.loc[order, 'weight']
                print(order, weight, ct, dt, max(0, ct - dt))
                if ct > dt:
                    tardiness += ct - dt
                    tardy_jobs += 1
    # return tardy_jobs, tardiness
    return tardiness, tardy_jobs


def add_ct(model, where):
    if where == GRB.callback.MIPSOL:
        selected = []
        for p in range(p_max):
            for k in range(K):
                sol = model.cbGetSolution([model._vars[j, p, k] for j in range(n)])
                selected += [(j, p, k) for j in range(n) if sol[j, p, k] > 0.5]


M = 1000000
n = 15
p_max = 2
K = 10
df_items = pd.read_csv(r'./data/orders15.csv')
df_orders = pd.read_csv('./data/due_dates0.7.csv', index_col=0)
C = 7

w, pt, dt = list(df_orders['weight']), list(df_orders['pt']), list(df_orders['dt'])

m = Model()

# Create variables

vars = {}
for p in range(p_max):
    for k in range(K):
        for j in range(n):
            vars[j, p, k] = m.addVar(vtype=GRB.BINARY, name='o(%d, %d, %d)' % (j, p, k))
# add taj
ta = {}
for j in range(n):
    ta[j] = m.addVar(lb=0, vtype=GRB.CONTINUOUS)
# add ctpk
ct = {}
for p in range(p_max):
    for k in range(-1, K):
        ct[p, k] = m.addVar(lb=0, vtype=GRB.CONTINUOUS)

m.update()

# TODO set objectives
# # Set objective
m.setObjective(quicksum(ta[j] for j in range(n)), GRB.MINIMIZE)

for j in range(n):
    m.addConstr(quicksum(vars[j, p, k] for p in range(p_max) for k in range(K)) == 1)
m.update()

for p in range(p_max):
    for k in range(K):
        m.addConstr(quicksum(w[j] * vars[j, p, k] for j in range(n)) <= C)
m.update()

for p in range(p_max):
    m.addConstr(ct[p, -1] == 0)
m.update()
for p in range(p_max):
    for k in range(K):
        for j in range(n):
            m.addConstr((ct[p, k - 1] + pt[j] - ct[p, k]) <= 0)
m.update()
for p in range(p_max):
    for k in range(K):
        for j in range(n):
            m.addConstr((ct[p, k] - dt[j] - M * (1 - vars[j, p, k]) - ta[j]) <= 0)
m.update()

# Optimize model
m._vars = vars
m.params.LazyConstraints = 1
m.optimize(add_ct)

solution = m.getAttr('x', vars)
selected = [(j, p, k) for p in range(p_max) for k in range(K) for j in range(n) if solution[j, p, k] > 0.5]
# assert len(subtour(selected)) == n
print('Optimal cost: %g' % m.objVal)

jobs = []
# sd_p = [0] * p_max
for p in range(p_max):
    jobs.append(Picker(p, batches=[]))
ans = {}
for j, p, k in selected:
    ans[p, k] = []
for j, p, k in selected:
    ans[p, k].append(list(df_orders.index)[j])
l = 0
for x, y in ans.items():
    w = 0
    for order in y:
        w += df_orders.loc[order, 'weight']
    jobs[x[0]].batches.append(Batch(b=l, weight=w, orders=y))

for job in jobs:
    job.re_routing(df_items)

pair = tard(df_orders, jobs)
print(pair)
print('ok')
