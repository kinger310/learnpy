# read in a txt file

filename = "./data/10K-RiskFactors-Apple-2016.txt"
text = open(filename,encoding="utf-8",mode="r").read() # read all text
print(type(text))
print(text[:1000])


# jieba分词: 默认模式
import jieba

# text = "我来到上海交通大学"
text = "中共中央总书记、国家主席、中央军委主席习近平29日上午在参加首都义务植树活动时强调，植树造林，种下的既是绿色树苗，也是祖国的美好未来。"

words = jieba.lcut(text)
print("Default Mode:")
print(words)

# exercise: Chinese word segmentation
# use jieba to segment Chinese words for all files in the folder "./data/Prospectus_Zh/"
# print first 10 segmented words for each file
import os, jieba

fnames = os.listdir('./data/Prospectus_Zh/')
for fname in fnames:
    with open('./data/Prospectus_Zh/' + fname, encoding='utf-8') as file:
        doc = file.read()
        words = jieba.lcut(doc)
        print(words[:10])

# exercise: os.listdir()
# list all the file names in the directory "./data/Prospectus_Zh/"
import os

fdir = "./data/Prospectus_Zh/"  # . means current working directory
filenames = os.listdir(fdir)  # list all file names in the specified directory
print(filenames[:10])  # print first 10 file names
# exercise: read files in a folder
# read all txt files in the folder "./data/RiskFactors/"
# save the content of each file as an element in a list
import os

docs = []
for file_name in filenames:
    with open(fdir + file_name, encoding='utf-8') as file:
        docs.append(file.read())
print(docs[0][:1000])

text_example1 = 'Apple Inc. is an American multinational technology company headquartered in Cupertino, ' \
                'California, thatdesigns, develops, and sells consumer electronics, computer software, ' \
                'and online services. Its hardware products include the iPhone smartphone, the iPad tablet ' \
                'computer, the Mac personal computer, the iPod portable media player, and the Apple Watch smartwatch.'
print(text_example1)

from textblob import TextBlob

textTB = TextBlob(text_example1)  # first create a TextBlob
words = textTB.words  # word tokenization
print(words)

# exercise: word tokenization
# read text in the file "./data/10K-RiskFactors-Apple-2016.txt"
# and do word tokenization (how many word tokens?)
from textblob import TextBlob

with open('./data/10K-RiskFactors-Apple-2016.txt', encoding='utf-8') as file:
    text = file.read()
    textTB = TextBlob(text)
    words = textTB.words # word tokenization
    print(words)
print(len(words))

# exercise: simple processing after word tokenization
# we usually do some simple processing after word tokenization
# please do the following things for the tokenized words in the previous exercise
# (1) only retain words consisting of alphanumeric characters
# (2) only retain words with more than 1 characters
# (3) transform all word tokens to lower case
words = [word.lower() for word in words if word.isalnum() and len(word) > 1]
print(words)


# sentence split
from textblob import TextBlob

text_example1 = 'Apple Inc. is an American multinational technology company headquartered in Cupertino, ' \
                'California, that designs, develops, and sells consumer electronics, computer software, ' \
                'and online services. Its hardware products include the iPhone smartphone, the iPad tablet ' \
                'computer, the Mac personal computer, the iPod portable media player, and the Apple Watch smartwatch.'
textTB = TextBlob(text_example1)
sents = textTB.sentences # sentence split
for sent in sents:
    print(sent)
    print("--------------------")


# exercise: sentence split
# read text in the file "./data/10K-RiskFactors-Apple-2016.txt"
# and do sentence split (how many sentences are splitted?)
from textblob import TextBlob

with open("./data/10K-RiskFactors-Apple-2016.txt", encoding='UTF-8') as file:
    text_example1 = file.read()
    textTB = TextBlob(text_example1)
    sents = textTB.sentences  # sentence split
len(sents)




# jieba词性标注分词
# ictclas兼容的标记法：https://gist.github.com/luw2007/6016931
import jieba.posseg

words_and_tags = jieba.posseg.lcut("我来到上海交通大学")
print(words_and_tags)
words = [wt.word for wt in words_and_tags]
print(words)
tags = [wt.flag for wt in words_and_tags]
print(tags)




