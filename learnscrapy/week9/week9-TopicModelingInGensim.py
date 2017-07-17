# firstly, read processed review data

lines = open(r"D:\ProgramFiles\PycharmProjects\learnpy\learnscrapy\week8\data\reviews.csv",encoding="utf-8",mode="r").readlines()
reviews = [line.strip().split(',')[1] for line in lines]
print(reviews[:2])

# prepare data for gensim
# preprocessing
from gensim.parsing.preprocessing import remove_stopwords

# remove stopwords
reviews = [remove_stopwords(review) for review in reviews]
# review doc: string to list
reviews = [review.split() for review in reviews]

# prepare data for gensim
# generate vocabulary dictionary
from gensim import corpora

# %time
vocabs = corpora.Dictionary(reviews)
# you can save the dictionary of vacabularies
vocabs.save('movie_reviews.dict')
print(vocabs)

# prepare data for gensim
# generate corpus for gensim models

# %time
corpus = [vocabs.doc2bow(review_doc) for review_doc in reviews]
# you can save the corpus for future use
corpora.MmCorpus.serialize('movie_reviews.mm', corpus)
print(corpus[0])


# train lda model
from gensim import models

# train a lda model
# %time
lda = models.ldamodel.LdaModel(corpus=corpus, id2word=vocabs, num_topics=100)

# you can save the trained model for future use
lda.save('reviews_lda_100.model')

# you can load saved model later as follows:
# lda = models.LdaModel.load('reviews_lda_100.model')


# represent documents using topic distributions

corpus_lda = lda[corpus]
print(corpus_lda[0])

# visualize lda model using pyLDAvis
import pyLDAvis
from pyLDAvis import gensim

# %time
vis_data = pyLDAvis.gensim.prepare(lda, corpus, vocabs)

pyLDAvis.display(vis_data)


# Uusing Gensim, you can also train a lda model using tfidf corpus
from gensim import models

# %time
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]
print(corpus_tfidf[0])

# train a lda model
# %time lda_tfidf = gensim.models.ldamodel.LdaModel(corpus=corpus_tfidf, id2word=vocabs, num_topics=100)

# train a lsi model using tfidf corpus
from gensim import models

# %time
lsi = models.LsiModel(corpus_tfidf, id2word=vocabs, num_topics=100)
corpus_lsi = lsi[corpus_tfidf]

lsi.print_topics(10)



