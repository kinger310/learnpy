# %%

#%%
import pandas as pd
pd.set_option('display.max_columns', 500)
import zipfile

with zipfile.ZipFile(r'D:\ProgramFiles\PycharmProjects\learnpy\machine_learning\regression\KaggleCredit2.csv.zip', 'r') as z:
    with z.open("KaggleCredit2.csv") as file:
        data = pd.read_csv(file, index_col=0)
data.head()

#%%
data.shape

#%%
data.isnull().sum()

#%% Drop NA
data.dropna(inplace=True)
data.shape

#%%
y = data['SeriousDlqin2yrs']
X = data.drop('SeriousDlqin2yrs', axis=1)
y.mean()


#%% homework1
# 把数据切分成训练集和测试集
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


#%% 练习2
# 使用logistic regression/决策树/SVM/KNN...等sklearn分类算法进行分类，尝试查sklearn API了解模型参数含义，调整不同的参数。
import numpy as np
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

#%% 练习3。 在测试集上进行预测，计算准确度
accuracy = np.mean(y_test == y_pred) * 100
print(accuracy) # 93.3508116249233

#%% 练习4
# 查看sklearn的官方说明，了解分类问题的评估标准，并对此例进行评估。
# 评估指标(主要是准确率和召回率)
y_score = model.decision_function(X_test)
y_s = model.predict_proba(X_test)
from sklearn.metrics import average_precision_score
average_precision = average_precision_score(y_test, y_score)

print('Average precision-recall score: {0:0.2f}'.format(
      average_precision))

# precision = TP/(TP+FP)  recall = TP / (TP+FN)
from sklearn.metrics import precision_recall_curve
precision, recall, thresholds = precision_recall_curve(y_test, y_score)

#%%
# Plot the Precision-Recall curve¶
from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt
from sklearn.utils.fixes import signature

precision, recall, _ = precision_recall_curve(y_test, y_score)

# In matplotlib < 1.5, plt.fill_between does not have a 'step' argument
step_kwargs = ({'step': 'post'}
               if 'step' in signature(plt.fill_between).parameters
               else {})
plt.step(recall, precision, color='b', alpha=0.2,
         where='post')
plt.fill_between(recall, precision, alpha=0.2, color='b', **step_kwargs)

plt.xlabel('Recall')
plt.ylabel('Precision')
plt.ylim([0.0, 1.05])
plt.xlim([0.0, 1.0])
plt.title('2-class Precision-Recall curve: AP={0:0.2f}'.format(
          average_precision))

#%% 练习5
# #
# 银行通常会有更严格的要求，因为fraud带来的后果通常比较严重，一般我们会调整模型的标准。
# 比如在logistic regression当中，一般我们的概率判定边界为0.5，但是我们可以把阈值设定低一些
# ，来提高模型的“敏感度”，试试看把阈值设定为0.3，再看看这时的评估指标(主要是准确率和召回率)。
#
# tips:sklearn的很多分类模型，predict_prob可以拿到预估的概率，可以根据它和设定的阈值大小去判断最终结果(分类类别)


# 比如在logistic regression当中，一般我们的概率判定边界为0.5，但是我们可以把阈值设定低一些
# 这个怎么做?

