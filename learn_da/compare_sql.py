import pandas as pd
import numpy as np

url = 'https://raw.github.com/pandas-dev/pandas/master/pandas/tests/data/tips.csv'

tips = pd.read_csv(url)
# tips.to_csv('tips.csv')
tips.head()

# SELECT
'''
SELECT total_bill, tip, smoker, time
FROM tips
LIMIT 5;
'''
tips[['total_bill', 'tip', 'smoker', 'time']].head(5)

'''
SELECT *
FROM tips
WHERE time = 'Dinner'
LIMIT 5;
'''
tips[tips['time'] == 'Dinner'].head(5)
tips[tips.time == 'Dinner'].head(5)
is_dinner = tips['time'] == 'Dinner'
is_dinner.value_counts()
tips[is_dinner].head(5)

'''
-- tips of more than $5.00 at Dinner meals
SELECT *
FROM tips
WHERE time = 'Dinner' AND tip > 5.00;
'''
tips[(tips.time == 'Dinner') & (tips.tip > 5.00)].head()

frame = pd.DataFrame({'col1': ['A', 'B', np.NaN, 'C', 'D'],
                      'col2': ['F', np.NaN, 'G', 'H', 'I']})
'''
SELECT *
FROM frame
WHERE col1 IS NOT NULL;
'''
frame[frame['col2'].isnull()]
frame[frame['col2'].notnull()]

'''
SELECT sex, count(*)
FROM tips
GROUP BY sex;
'''
tips.groupby('sex').size()
# notice: use size not count
# count() applies the function to each column, returning the number of not null records within each.
tips.groupby('sex').count()
tips.groupby('sex')['total_bill'].count()

'''
SELECT day, AVG(tip), COUNT(*)
FROM tips
GROUP BY day;
'''
# agg() allows you to pass a dictionary to your grouped DataFrame,
# indicating which functions to apply to specific columns
tips.groupby('day').agg({'tip': np.mean, 'time': np.size})

'''
SELECT smoker, day, COUNT(*), AVG(tip)
FROM tips
GROUP BY smoker, day;
'''
tips.groupby(['day', 'smoker']).agg({'tip': np.mean, 'time': np.size})
tips.groupby(['smoker', 'day']).agg({'tip': [np.mean, np.size]})

# JOIN
df1 = pd.DataFrame({'key': ['A', 'B', 'C', 'D'],
                    'value': np.random.randn(4)})

df2 = pd.DataFrame({'key': ['B', 'D', 'D', 'E'],
                    'value': np.random.randn(4)})
'''
SELECT *
FROM df1
INNER JOIN df2
  ON df1.key = df2.key;
'''
# merge performs an INNER JOIN by default
pd.merge(df1, df2, on='key')
# merge() also offers parameters for cases when you’d like to join one
# DataFrame’s column with another DataFrame’s index.
indexed_df2 = df2.set_index('key')
pd.merge(df1, indexed_df2, left_on='key', right_index=True)
'''
-- show all records from df1
SELECT *
FROM df1
LEFT OUTER JOIN df2
  ON df1.key = df2.key;
'''
# show all records from df1
pd.merge(df1[['key', 'value']], df2, on='key', how='left')
# right join
pd.merge(df1, df2, on='key', how='right')

# full JOIN
'''
-- show all records from both tables
SELECT *
FROM df1
FULL OUTER JOIN df2
  ON df1.key = df2.key;
'''
pd.merge(df1, df2, on='key', how='outer')
pd.merge(df1, df2)


left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})


right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
pd.merge(left, right, on='key')

# a MORE complicated example
left2 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                      'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']})

right2 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                       'C': ['C0', 'C1', 'C2', 'C3'],
                       'D': ['D0', 'D1', 'D2', 'D3']})
pd.merge(left2, right2, on=['key1', 'key2'])
pd.merge(left2, right2, left_on='key1', right_on='key1')

'''
SELECT * FROM tips limit 3, 5
select * from tips LIMIT 5 offset 3
SELECT * FROM tips
ORDER BY tip DESC
LIMIT 10 OFFSET 5;
'''

# tips.ix[3:7, :]
tips.iloc[3:3+5, :]
tips.nlargest(10+5, columns='tip').tail(10)

# Top N rows per group
# 选出每天的total_bills最高的前两位
(tips.assign(rn=tips.sort_values(['total_bill'], ascending=False).groupby(['day']).cumcount() + 1)
     .query('rn < 3')
     .sort_values(['day', 'rn'])
)

import pandas.core.groupby.DataFrameGroupBy.rank

(tips.assign(rnk=tips.groupby(['day'])['total_bill'].rank(method='first', ascending=False))
     .query('rnk < 3')
     .sort_values(['day', 'rnk'])
)
# Let’s find tips with (rank < 3) per gender group for (tips < 2).
# Notice that when using rank(method='min') function rnk_min remains the same
# for the same tip (as Oracle’s RANK() function)

(tips[tips['tip'] < 2]
     .assign(rnk_min=tips.groupby(['sex'])['tip']
                         .rank(method='min'))
     .query('rnk_min < 3')
     .sort_values(['sex','rnk_min'])
)

