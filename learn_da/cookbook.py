import pandas as pd
import numpy as np

df = pd.DataFrame({'AAA': [4, 5, 6, 7], 'BBB': [10, 20, 30, 40], 'CCC': [100, 50, -30, -50]})

# %timeit
df['logic'] = np.where(df['AAA'] > 5, 'high', 'low')
# %timeit
df['logic'] = ['high' if x > 5 else 'low' for x in df['AAA']]


df = pd.DataFrame({'id': [100, 100, 100, 101, 101, 101]*100, 'country': ['CN', 'CN', 'JP', 'KR', 'KR', 'KR']*100,
                   'date': ['2001', '2002', '2003', '2001', '2002', '2003']*100})
unstack_df = df.groupby(['id', 'country']).size().unstack()
unstack_df = unstack_df.reset_index()
unstack_df['flag'] = unstack_df.notnull().sum(axis=1) - 1
# if flag > 1, signal_value = 0 ,  if flag = 1 signal_value = 0
# 可以用np.where实现


import random
N = 1000000
uniques_keys = [pd.util.testing.rands(3) for i in range(200)]
keys = [random.choice(uniques_keys) for i in range(N)]
values = np.random.rand(N).tolist()
vs = pd.Series(values)
ks = pd.Series(keys)
# %timeit
vs.groupby(ks, sort=False).sum()