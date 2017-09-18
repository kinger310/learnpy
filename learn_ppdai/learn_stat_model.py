# -*- coding: utf-8 -*-

# hasthags indicate notes about code; the code below imports a few packages we will need for this analysis
import pandas as pd
import statsmodels.api as sm
import pylab as pl
import numpy as np
from patsy import dmatrices

df = sm.datasets.get_rdataset("Guerry", "HistData").data
vars = ['Department', 'Lottery', 'Literacy', 'Wealth', 'Region']
df = df[vars]
df = df.dropna()

y0, X0 = dmatrices('Lottery ~ Literacy + Wealth + Region', data=df, return_type='dataframe')

mod = sm.OLS(y0, X0)
res = mod.fit()
print res.summary()  # Summarize model

# Diagnostics and specification tests
sm.stats.linear_rainbow(res)

sm.graphics.plot_partregress('Lottery', 'Wealth', ['Region', 'Literacy'], data=df, obs_labels=False)


# R-style formulas

import statsmodels.formula.api as smf
import numpy as np
import pandas as pd

df = sm.datasets.get_rdataset("Guerry", "HistData").data
df = df[['Lottery', 'Literacy', 'Wealth', 'Region']].dropna()
df.head()

mod = smf.ols(formula='Lottery ~ Literacy + Wealth + Region', data=df)
res = mod.fit()
print(res.params)

res = smf.ols(formula='Lottery ~ Literacy + Wealth + C(Region) -1 ', data=df).fit()
print(res.params)
# 变量相乘，不设常变量
res1 = smf.ols(formula='Lottery ~ Literacy : Wealth - 1', data=df).fit()
# y1, X1 = dmatrices('Lottery ~ Literacy : Wealth - 1', data=df, return_type='dataframe')
print(res1.params)

res = smf.ols(formula='Lottery ~ np.log(Literacy)', data=df).fit()

def log_plus_1(x):
    return np.log(x) + 1.
res = smf.ols(formula='Lottery ~ log_plus_1(Literacy)', data=df).fit()
print(res.params)
y0, X0 = dmatrices('Lottery ~ Literacy + Wealth + Region', data=df, return_type='dataframe')

df1 = pd.read_csv('hour_pass.csv')
res = smf.logit(formula='Pass ~ Hours', data=df1).fit()
print res.summary()


