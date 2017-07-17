import pandas as pd
import numpy as np

df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
                         'foo', 'bar', 'foo', 'foo'],
                   'B': ['one', 'one', 'two', 'three',
                         'two', 'two', 'one', 'three'],
                   'C': np.random.randn(8),
                   'D': np.random.randn(8)})

grouped = df.groupby('A')
grouped = df.groupby(['A', 'B'])


def get_letter_type(letter):
    if letter.lower() in 'aeiou':
        return 'vowel'
    else:
        return 'consonant'


grouped = df.groupby(get_letter_type, axis=1)
grouped.first()
grouped.last()
grouped.sum()

lst = [1, 2, 3, 1, 2, 3]
s = pd.Series([1, 2, 3, 10, 20, 30], lst)
grouped = s.groupby(level=0)
grouped.first()
grouped.last()
grouped.sum()

#
#
from pandas.stats.moments import expanding_mean, expanding_count
#
# def handler(grouped):
#     se = grouped.set_index('Date')['Sale'].sort_index()
#     # se is the (ordered) time series of sales restricted to a single basket
#     # we can now create a dataframe by combining different metrics
#     # pandas has a function for each of the ones you are interested in!
#     return pd.concat(
#         {
#             'MeanToDate': expanding_mean(se), # cumulative mean
#             'MaxToDate': se.cummax(),         # cumulative max
#             'SaleCount': expanding_count(se), # cumulative count
#             'Sale': se,                       # simple copy
#             'PrevSale': se.shift(1)           # previous sale
#         },
#         axis=1
#      )
#
# # we then apply this handler to all the groups and pandas combines them
# # back into a single dataframe indexed by (Basket, Date)
# # we simply need to reset the index to get the shape you mention in your question
# new_df = df.groupby('Basket').apply(handler).reset_index()


def handle(grouped):
    se = grouped.set_index('date')['yield'].sort_index()
    # se is the (ordered) time series of sales restricted to a single basket
    # we can now create a dataframe by combining different metrics
    # pandas has a function for each of the ones you are interested in!
    return pd.concat(
        {
            'prev_yield': se.shift(1), # previous sale
            'diff': se - se.shift(1),
            'MeanToDate': se.expanding(min_periods=1).mean(), # cumulative mean
            'MaxToDate': se.cummax(),         # cumulative max
            'SaleCount': se.expanding(min_periods=1).count(), # cumulative count
        },
        axis=1
     )

# df = pd.DataFrame({'id': ['001', '002'] * 5,
#                    'yield': [5, 4, 6, 3, 7, 2, 8, 1, 9, 0],
#                    'date': ['2017-04-19', '2017-04-19', '2017-04-20', '2017-04-20', '2017-04-21',
#                             '2017-04-21', '2017-04-22', '2017-04-22', '2017-04-23', '2017-04-23']
#                    })
df = pd.DataFrame({'id': ['001', '002'] * 5,
                   'yield': [5, 4, 6, 3, 7, 2, 8, 1, 9, 0],
                   'date': ['2017-04-19', '2017-04-19', '2017-04-20', '2017-04-20', '2017-04-21',
                            '2017-04-21', '2017-04-22', '2017-04-22', '2017-04-23', '2017-04-23']
                   })
df = df.sort_values(by=['id', 'date'])

new_df = df.groupby('id').apply(handle).reset_index()




def longestForward(a_list):
    neg_longest = 1
    neg_count = 0
    pos_longest = 1
    pos_count = 0
    for i, x in enumerate(a_list):
        if x == 0:
            continue
        elif x < 0:
            neg_count += 1
            if neg_count > neg_longest:
                neg_longest = neg_count
            pos_count = 0
        else:
            pos_count += 1
            if pos_count > pos_longest:
                pos_longest = pos_count
            neg_count = 0
    return neg_longest, pos_longest

arr = [3, 6, 5, 1, 9, 3, 2, 3, 4, 5, 1]
arr = [np.nan, 3, -1, -4, -6, -1, 1, 1, 1, 1, -4]
longestForward(arr)

new_df.groupby('id').diff.apply(longestForward)

