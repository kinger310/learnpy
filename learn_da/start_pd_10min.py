import pandas as pd
import numpy as np

# a = np.array([[1., 2., 3.], [4., 5., 6.]])

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ACBD'))
df.values
df.columns
df.index

df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train"] * 2),
                    'F': 'foo'
                    })
df2.dtypes
# Sorting by an axis
df.sort_index(axis=1, ascending=False)
# Sorting by values
df.sort_values(by='B')
df['A'];
df.A;
df[0:3]
df['20130102':'20130104']
# Selection by Label
df.loc[dates[0]];
df.loc[:, ['A', 'B']];
df.loc['20130102':'20130104', ['A', 'B']];
df.loc[dates[0], 'A'];
df.at[dates[0], 'A']

# Selection by Position
df.iloc[3]

df[df > 0]

df2 = df.copy()
df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
df2[df2['E'].isin(['two', 'four'])]
# Setting a new column automatically aligns the data by the indexes
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20130102', periods=6))
df['F'] = s1
# Setting values by label
df.at[dates[0], 'A'] = 0
df.loc[dates[0], 'A'] = 1
# Setting values by position
df.iat[0, 1] = 0

df.loc[:, 'D'] = np.array([5] * len(df))

df2 = df.copy()
df2[df2 > 0] = -df2

df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
df1.loc[dates[0]:dates[1], 'E'] = 1
df1.dropna(how='any')
df1.fillna(value=5)

# Operations in general exclude missing data.
df.mean(axis=1)

s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(periods=2)
df.sub(s, axis='index')

# Apply
df.apply(np.cumsum)
df.apply(lambda x: x.max() - x.min())

# Histogramming
s = pd.Series(np.random.randint(0, 7, size=10))
s.value_counts().sort_index()

# String Methods
s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
s.str.lower()

# Merge
# Concat
df = pd.DataFrame(np.random.randn(10, 4))
pieces = [df[:3], df[2:7], df[7:]]
pd.concat(pieces)  # 需要drop_duplicates

# TODO Concat parameters

# pivot tables
df = pd.DataFrame({'A': ['one', 'one', 'two', 'three'] * 6,
                   'B': ['A', 'B', 'C'] * 8,
                   'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 4,
                   'D': np.random.randn(24),
                   'E': np.random.randn(24)})
pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'], aggfunc='mean')

# Time Series
rng = pd.date_range('1/1/2012', periods=100, freq='T')  # also min
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
ts.resample(rule='5Min').sum()

rng = pd.date_range('3/6/2012 00:00', periods=5, freq='D')
ts = pd.Series(np.random.randn(len(rng)), rng)

rng = pd.date_range('3/6/2012 00:00', periods=5, freq='D')
ts = pd.Series(np.random.randn(len(rng)), rng)
ts_utc = ts.tz_localize('UTC')
ts_utc.tz_convert('US/Eastern')
ts_utc.tz_convert('Asia/Shanghai')

rng = pd.date_range('1/1/2012', periods=5, freq='M')
ts = pd.Series(np.random.randn(len(rng)), rng)
ps = ts.to_period()
ps.to_timestamp()

prng = pd.period_range('1990Q1', '2000Q4', freq='Q-NOV')
ts = pd.Series(np.random.randn(len(prng)), prng)
ts.index = (prng.asfreq('M', 'E') + 1).asfreq('D', 'E')

import matplotlib.pyplot as plt
plt.style.use('ggplot')
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()
plt.show()


df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=['A', 'B', 'C', 'D'])
df = df.cumsum()
df.plot()
plt.legend(loc='best')

# Excel
df.to_excel('foo.xlsx', sheet_name='Sheet1')
pd.read_excel('foo.xlsx', 'Sheet1', index_col=None, na_values=['NA'])

