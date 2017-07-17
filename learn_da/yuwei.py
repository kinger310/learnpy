import pandas as pd
import numpy as np


file_path = r'D:\ProgramFiles\PycharmProjects\learnpy\learn_da\jones_model.xlsx'
df = pd.read_excel(file_path, sheetname='修改', header=1)

a = df.groupby('code').size().reset_index()
a.columns = ['code', 'count']
a = a[a['count'] == 16]

b = a.merge(df, how='inner', on='code')
b.to_excel('result.xlsx')
