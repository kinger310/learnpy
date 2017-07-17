# 知识点一 Python的并行计算
import numexpr as ne


def f(a):
    ex = 'abs(cos(a)) **　0.5'
    ne.set_num_threads(8)
    return ne.evaluate(ex)


# 二、 去重的set的运用
import pandas as pd

user_id = [10, 15, 20, 25, 30, 32, 40, 45, 50]
df = pd.DataFrame({'user_id': [10, 20, 25, 30, 32], 'value': [45, 49, 19, 58, 48]})
list(set(user_id) - set(df['user_id']))

# 三、 Top N rows per group
# -- Oracle's RANK() analytic function
# SELECT * FROM (
#   SELECT
#     t.*,
#     RANK() OVER(PARTITION BY sex ORDER BY tip) AS rnk
#   FROM tips t
#   WHERE tip < 2
# )
# WHERE rnk < 3
# ORDER BY sex, rnk;
import pandas as pd
from sklearn.datasets import load_iris

# 取三组里 sepal_length(花萼长)最长的三个
data = load_iris()
df = pd.DataFrame(data=data['data'], columns=data['feature_names'])
df.columns = df.columns.str[:-5].str.replace(' ', '_')
df['target'] = pd.Series(data['target'])
empty_df = pd.DataFrame()

t = df.assign(rn=df.sort_values(['sepal_length'], ascending=False)
              .groupby('target')
              .cumcount() + 1) \
    .query('rn <= 3') \
    .sort_values(['target', 'rn'])

# 四、 冒泡排序
arr = [6, 5, 4, 3, 2, 1]
for i in range(len(arr) - 1, 0, -1):
    for j in range(i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(arr)

# 五、 Pandas IO 函数 create_engine
from sqlalchemy import create_engine

# engine = create_engine(r'sqlite:D:/ProgramFiles/SQLite/test.db')
engine = create_engine(r'sqlite:///D:\ProgramFiles\SQLite\test.db')
df_new = pd.read_sql_query(
    'SELECT * FROM tips', engine
)
# df_new = pd.read_clipboard()
# df_new.to_clipboard()

a = df.to_json(orient='records', date_format='iso')
df.to_sql('iris', engine, if_exists='replace', index=False)



