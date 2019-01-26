# %%
import pandas as pd
import pickle

with open('question.pkl', 'rb') as f_:
    question = pickle.load(f_)



print('ok')

#%%
import gensim
import numpy as np
numpy_matrix = np.random.randint(10, size=[5,2])  # random matrix as an example
corpus = gensim.matutils.Dense2Corpus(numpy_matrix)
numpy_matrix = gensim.matutils.corpus2dense(corpus, num_terms=5)

#%%
from gensim import corpora, models, similarities
with open('word_embed.pkl', 'rb') as f_:
    word_embed = pickle.load(f_)

# word_embed['W00022']
corpus = []
for i in range(10):
    words = question.loc[i, 'words'].split()
    corp_tup = [tuple(word_embed[word]) for word in words]
    corpus.append(corp_tup)

#%%

corpora.MmCorpus.serialize('corpus.mm', corpus)
corpus = corpora.MmCorpus('corpus.mm')
print(corpus)

# tfidf = models.TfidfModel(corpus)
#
# test_words = question.loc[11, 'words'].split()
# vec = [tuple(word_embed[word]) for word in test_words]
#
# print(tfidf[vec])

