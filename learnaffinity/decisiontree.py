# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 21:47:09 2016

@author: Wangdi
"""

import pandas as pd
import numpy as np
from sklearn import cross_validation
import csv

df = pd.read_csv('C:/Users/Wangdi/Desktop/titanic/train.csv',header=0)
df['FamilySize'] = df['SibSp'] + df['Parch']
df = df.drop(['Ticket','Name','Cabin','SibSp','Parch','Embarked'],axis=1) # 去除非数值
m = np.ma.masked_array(df['Age'], np.isnan(df['Age'])) # 将NAN值隐藏，以计算均值
mean = np.mean(m).astype(int)
df['Age'] = df['Age'].map(lambda x : mean if np.isnan(x) else x)
df['Sex'] = df['Sex'].map( {'female': 1, 'male': 0} ).astype(int)
df['Fare'] = df['Fare'].map(lambda x : 0 if np.isnan(x) else int(x)).astype(int)
X = df.values
y = df['Survived'].values
X = np.delete(X,1,axis=1)
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,y,test_size=0.3,random_state=0)

from sklearn import tree
from sklearn.metrics import precision_recall_curve
dt_model = tree.DecisionTreeClassifier(max_depth=3)
dt_model.fit(X_train, y_train)
print('Decision Tree')
print(dt_model.score(X_test,y_test)) # probable best score 0.82090
print(dt_model.feature_importances_)
precision, recall, thresholds = precision_recall_curve(y_train, dt_model.predict(X_train))
print [precision, recall, thresholds]

from sklearn.ensemble import RandomForestClassifier
rf_model = RandomForestClassifier(n_estimators=30)
rf_model.fit(X_train, y_train)
print('Random Forest')
print(rf_model.score(X_test, y_test)) # probable best score 0.83209,每次数据不稳定

from sklearn.neighbors import KNeighborsClassifier
knn_model = KNeighborsClassifier(n_neighbors=30) 
knn_model.fit(X_train, y_train)
print('KNN')
print(knn_model.score(X_test, y_test)) # probable best score 0.71268

from sklearn.ensemble import GradientBoostingClassifier
gbc_model = GradientBoostingClassifier(n_estimators=9)
gbc_model.fit(X_train, y_train)
print('GradientBoostingClassifier')
print(gbc_model.score(X_test, y_test)) # probable best score 0.83209

test = pd.read_csv('C:/Users/Wangdi/Desktop/titanic/test.csv',header=0)
test['FamilySize'] = test['SibSp'] + test['Parch']
tf = test.drop(['Ticket','Name','Cabin','SibSp','Parch','Embarked'],axis=1)
m = np.ma.masked_array(tf['Age'], np.isnan(tf['Age']))
mean = np.mean(m).astype(int)
tf['Age'] = tf['Age'].map(lambda x : mean if np.isnan(x) else int(x))
tf['Sex'] = tf['Sex'].map( {'female': 1, 'male': 0} ).astype(int)
tf['Fare'] = tf['Fare'].map(lambda x : 0 if np.isnan(x) else int(x)).astype(int)
predicts = dt_model.predict(tf)
ids = tf['PassengerId'].values
predictions_file = open("C:/Users/Wangdi/Desktop/titanic/my_submission.csv", "wb")
open_file_object = csv.writer(predictions_file)
open_file_object.writerow(["PassengerId","Survived"])
open_file_object.writerows(zip(ids, predicts))
predictions_file.close()
