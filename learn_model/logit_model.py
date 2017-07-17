# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import log


import os

df = pd.read_csv(os.getcwd() + r'/learn_model/Ch3_logistic_ex1.csv')
X0 = df.iloc[:20, :3]; X0  # X0 = df.iloc[0:20, 0:3]
XE = df.iloc[:, :3]; XE
Y0 = df.iloc[:20, 3]; Y0

# 数据转化和参数回归
# n = Y0.shape[0]
# Y1 = []
# for i in range(n):
#     if int(Y0[i]) == 0:
#         Y1.append(0.25)
#     else:
#         Y1.append(0.75)
# 构建常数项系数
X0['X_chang'] = np.ones(X0.shape[0])
# Y = [log(y / (1 - y)) for y in Y1]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X0, Y0, random_state=14)

from sklearn.linear_model import LogisticRegression
estimator = LogisticRegression()

estimator.fit(X_train, y_train)
estimator.fit(X0, Y0)
print(estimator.coef_)

y_predicted = estimator.predict(X_test)
accuracy = np.mean(y_test == y_predicted) * 100

# To predict the value
X_new = df.iloc[20:, :3]
X_new['X_chang'] = np.ones(X_new.shape[0])
y_new_predicted = estimator.predict(X_new)

# to know about how logit model works
from math import exp
b = estimator.coef_[0]
for i in range(20):
    a = b.dot(X0.iloc[i, :])
    part = 1 / (1 + exp(-a))
    if part <= 0.5:
        print('pre = 0, true = {0}'.format(Y0[i]))
    else:
        print('pre = 1, true = {0}'.format(Y0[i]))

# For further understanding, you should know the Linear
from sklearn.linear_model import LinearRegression
estimator = LinearRegression()
estimator.fit(X0, Y0)

from scipy.sparse.linalg import lsqr
X1 = X0.as_matrix()
Y1 = np.zeros(Y0.size)
for i, x in enumerate(Y0):
    Y1[i] = int(x)

out = lsqr(X1, Y1, show=True)

'''
def many_return(x):
    return [x, x*2], x**2

out = many_return(1)

'''
