#%%
# import modules & set up logging
import gensim, logging
from gensim.models import Word2Vec

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

sentences = [["cat", "say", "meow"], ["dog", "say", "woof"]]
# train word2vec on the two sentences
model = Word2Vec(sentences, min_count=1, hs=1, negative=0)
# model = Word2Vec(sentences, size=100, window=5, min_count=5, workers=4)
model.save('ppd_contest/word2v.pkl')
model = Word2Vec.load('ppd_contest/word2v.pkl')

#%%
say_vector = model['say']

model.wv.similarity('cat', 'dog')
model.score(["The fox jumped over a lazy dog".split()])

#%%
model.score(["The fox say gigi".split()])
model.wv.most_similar(positive=['dog', 'woof'], negative=['cat'])
model.wv.most_similar_cosmul(positive=['dog', 'woof'], negative=['cat'])

