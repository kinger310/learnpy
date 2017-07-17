# -- Part 1: Processing text (Recap) --

# read review data
path = r'E:\研二下\CTA\week8\week8-lab3'
data_file = "/data/labeledTrainData.tsv"
lines = open(path + data_file, encoding="utf-8", mode="r").readlines()
print(lines[:2])

# read review data: split fields

lines = lines[1:]  # skip header line
lines_splitted = [line.strip().split('\t') for line in lines]

ids = [fields[0] for fields in lines_splitted]
tones = [fields[1] for fields in lines_splitted]
reviews = [fields[2] for fields in lines_splitted]

print("There are %d reviews." % len(reviews))
print(reviews[0])

# pre-processing review data
import re

# remove html <tags>
reviews = [re.sub(r'<.+?>', ' ', review) for review in reviews]
# convert to lowercase
reviews = [review.lower() for review in reviews]
# remove quotes
reviews = [review[1: -1] for review in reviews]

print(reviews[0])

# nlp: tokenization etc.
from textblob import TextBlob

save_file_path = "./data/reviews.csv"
with open(save_file_path, encoding="utf-8", mode="w") as fout:
    for idx, review in enumerate(reviews):
        if idx % 1000 == 0:
            print("processing review %d ..." % idx)
        review_tb = TextBlob(review)
        words = review_tb.words  # tokenize words
        words = words.lemmatize()  # lemmatize words
        words = [word for word in words if word.isalnum() and len(word) > 1]  # only retrain letters and digits
        fout.write("%s, %s\n" % (tones[idx], ' '.join(words)))  # save
print('Success!')

# --Part 2: Representing text--

# firstly, read processed review data

lines = open("./data/reviews.csv", encoding="utf-8", mode="r").readlines()
reviews = [line.strip().split(',')[1] for line in lines]
tones = [line.strip().split(',')[0] for line in lines]
print(reviews[0])
print(tones[:10])

# import and init CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()
# vectorizer # default parameters

# transform text into document-term matrix

X = vectorizer.fit_transform(reviews)
print(type(X))  # X is a sparse matrix
print(X)

print(X.shape)

# convert X to a dense matrix
X_dense = X.toarray()
print(type(X_dense))
print(X_dense)

# examine the fitted vocabulary
vocab = vectorizer.get_feature_names()
print(len(vocab))
print(vocab[:100])

# when new unseen documents come, use transform rather than fit_transform
new_docs = ['this is an unseen document',
            'new document again']
X_new = vectorizer.transform(new_docs)
print(X_new)

# put all together
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(max_features=5000)  # can set params here

X = vectorizer.fit_transform(reviews)
print(X.shape)

vocab = vectorizer.get_feature_names()
print(len(vocab))

# get both 1-grams and 2-grams using the parameter "ngram_range"

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(ngram_range=[1, 2])  # 1-grams and 2-grams

X_12grams = vectorizer.fit_transform(reviews)
print(X_12grams.shape)

vocab = vectorizer.get_feature_names()
print(vocab[:100])

# import and init CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()
# vectorizer
# transform text into document-term matrix, use tf-idf weightings

X = vectorizer.fit_transform(reviews)
print(X.shape)
print(X)

# exercise: represent all review documents using BOW
# use 1-grams, and tfidf for term weighting
from sklearn.feature_extraction.text import TfidfVectorizer

# read all review data
lines = open("./data/reviews.csv", encoding="utf-8", mode="r").readlines()
reviews = [line.strip().split(',')[1] for line in lines]
tones = [int(line.strip().split(',')[0]) for line in lines]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(reviews)
print(X.shape)
print(X)

# -- Part 3: Building and evaluating classification models --
# firstly, prepare the data (X,y) obtained in the previous exercise
import numpy as np

y = tones
print(type(y))

y = np.asarray(y) # convert list to array for scikit-learn
print(type(y))

# pipeline: split X and y into training and testing sets
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0) # 80% vs. 20%
print("Shape of X_train:", X_train.shape)
print("Shape of y_train:", y_train.shape)
print("Shape of X_test:", X_test.shape)
print("Shape of y_test:", y_test.shape)

# build a KNN model
from sklearn.neighbors import KNeighborsClassifier

# init model (KNN, k=10)
model_knn = KNeighborsClassifier(n_neighbors=10)

# fit model using training data (in place)
# model_knn.fit(X_train, y_train)
# %timeit
model_knn.fit(X_train, y_train) # %time is a magic feature of jupyter notebook

from sklearn import metrics

# predicted classes of testing data
# %time
y_pred_class = model_knn.predict(X_test)
# predicted probabilities for class 1 in testing data
# %time
y_pred_prob = model_knn.predict_proba(X_test)[:, 1]

# compute accuracy and auc metrics
accuracy = metrics.accuracy_score(y_test, y_pred_class)
auc = metrics.roc_auc_score(y_test, y_pred_prob)
print("accuracy:",accuracy)
print("AUC:",auc)

# 5-fold cross-validation with KNN (k=10)
from sklearn.model_selection import cross_val_score

model_knn = KNeighborsClassifier(n_neighbors=10)  # k=10
scores = cross_val_score(model_knn, X, y, cv=5, scoring='accuracy')  # 5 folds

for idx, score in enumerate(scores):
    print('accuracy in cv-fold-%d = %f'%(idx+1,score))
print('mean=',scores.mean())
print('std=',scores.std())

# How to tune the parameters? What is the best k for KNN?

for k in [1,10,20,50,100,200,300,400,500]:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    accuracy = metrics.accuracy_score(y_test, y_pred)
    print('testing accuracy of KNN (K=%d) = %f' % (k, accuracy))



from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier

model_knn = KNeighborsClassifier(n_neighbors=10) # KNN, k=10
model_lg = LogisticRegression() # logistic Regression
model_nb = MultinomialNB() # Naive Bayes
model_dt = DecisionTreeClassifier(random_state=0) # Decision Tree
model_rf = RandomForestClassifier(n_estimators=200, random_state=0) # Random Forest
model_ada = AdaBoostClassifier(n_estimators=200, random_state=0) # Adaboost

models = []
models.append(model_knn)
models.append(model_lg)
models.append(model_nb)
models.append(model_dt)
models.append(model_rf)
models.append(model_ada)

for model in models:
    print(model)
    # train model
    model.fit(X_train, y_train)
    # predicted classes of testing data
    y_pred_class = model.predict(X_test)
    # predicted probabilities for class 1 in testing data
    y_pred_prob = model.predict_proba(X_test)[:, 1]

    # compute accuracy and auc metrics
    accuracy = metrics.accuracy_score(y_test, y_pred_class)
    auc = metrics.roc_auc_score(y_test, y_pred_prob)
    print("accuracy:",accuracy)
    print("AUC:",auc)
    print()

#  --Part 4: Building and evaluating regression models--

# first, read and represent 10K MDA using tfidf bag-of-words
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def read_mda(filename):
    MDAs = []
    LogVols = []
    for line in open(filename,mode="r"):
        fid, logvol, mda_text = line.strip().split(',',maxsplit=2)
        logvol = float(logvol)
        mda_words = mda_text.split()
        mda_words = [word for word in mda_words if word.isalnum() and len(word)>1]
        LogVols.append(logvol)
        MDAs.append(mda_text)
    return MDAs,LogVols

# read mda data: 2012 as training year, 2013 as testing year
path = r'E:\研二下\CTA\week8\week8-lab3'
X_train, y_train = read_mda(path + "/data/mda_2012.csv")
X_test, y_test = read_mda(path + "/data/mda_2013.csv")

# represent documents using scikit-learn
vectorizer = TfidfVectorizer(ngram_range=[1,1], max_features=100000) # 1-grams, tfidf
X_train = vectorizer.fit_transform(X_train)  # vectorize training texts using .fit_transform()
X_test = vectorizer.transform(X_test)  # vectorize testing texts using .transform()
y_train = np.asarray(y_train)  # convert list to array
y_test = np.asarray(y_test)  # convert list to array

# exercise: what are the shapes of X_train, y_train, X_test, y_test

print("Shape of X_train:", X_train.shape)
print("Shape of y_train:", y_train.shape)
print("Shape of X_test:", X_test.shape)
print("Shape of y_test:", y_test.shape)


# build and evaluate linear regression model

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# init model
model_lr = LinearRegression()
print(model_lr)

# fit model using traning data
model_lr.fit(X_train, y_train)

# use fitted model to predict testing data
y_pred = model_lr.predict(X_test)

# compute MSE metric
mse = mean_squared_error(y_test, y_pred)
print("Mean Square Error (MSE) on testing data =",mse)





