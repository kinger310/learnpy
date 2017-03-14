# -*- coding: utf-8 -*-

# import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv


# import os
# print(os.path)

# df = pd.read_csv(r'./learnsklearn/ionosphere.data')
# X = df.iloc[1, 1]
X = np.zeros((351, 34), dtype='float')
y = np.zeros((351,), dtype='bool')
# ONLY runs on ipython
data_filename = r'./learnsklearn/ionosphere.data'
with open(data_filename, 'r') as input_file:
    reader = csv.reader(input_file)
    for i, row in enumerate(reader):
        print("{0},{1}".format(i, row))
        data = [float(datum) for datum in row[:-1]]
        X[i, :] = data  # X[i, :] = X[i]
        y[i] = row[-1] == 'g'

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=14)

from sklearn.neighbors import KNeighborsClassifier
estimator = KNeighborsClassifier(n_neighbors=5)
estimator.fit(X_train, y_train)

y_predicted = estimator.predict(X_test)
accuracy = np.mean(y_test == y_predicted) * 100
print("The accuracy is {0:.1f}%".format(accuracy))

from sklearn.model_selection import cross_val_score
# cross_val_score 默认使用Stratified K Fold方法切分数据集
scores = cross_val_score(estimator, X, y, scoring='accuracy')
average_accuracy = np.mean(scores) * 100
print("The average accuracy is {0:.1f}%".format(average_accuracy))







