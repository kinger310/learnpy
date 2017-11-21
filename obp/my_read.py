# with open(r'E:\PycharmProjects\learnpy\obp\data\new2.txt') as file:
#     for line in file:
#         if line.startswith('t') or line.startswith('D'):
#             print(line)

import pandas as pd
import numpy as np

df = pd.read_csv(r'E:\PycharmProjects\learnpy\obp\data\res.csv')
df.columns = df.columns.str.lower()

df['vnd_imp'] = (df['esd'] - df['vnd']) / df['esd']
df['vns_imp'] = (df['esd'] - df['vns']) / df['esd']
df['vnd_seed_imp'] = (df['esd'] - df['vnd_seed']) / df['esd']
df['vns_seed_imp'] = (df['esd'] - df['vns_seed']) / df['esd']

df.groupby(['n'])[['vnd_imp', 'vns_imp', 'vnd_seed_imp', 'vns_seed_imp']].apply(np.mean).reset_index()
df.groupby(['c'])[['vnd_imp', 'vns_imp', 'vnd_seed_imp', 'vns_seed_imp']].apply(np.mean)
df.groupby(['mtcr'])[['vnd_imp', 'vns_imp', 'vnd_seed_imp', 'vns_seed_imp']].apply(np.mean).reset_index()



print('ok')


