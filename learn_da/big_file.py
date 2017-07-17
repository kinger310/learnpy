# import csv
#
#
# def getstuff(filename):
#     with open(filename, "r") as csvfile:
#         datareader = csv.reader(csvfile)
#         for row in datareader:
#             flag = True
#             for i in range(1, 6):
#                 if row[-i] == '':
#                     flag = False
#                     continue
#             if not flag:
#                 yield row
#
#
# # def getdata(filename, criteria):
# #     for criterion in criteria:
# #         for row in getstuff(filename, criterion):
# #             yield row
#
#
# filename = r'D:\ProgramFiles\PycharmProjects\learnpy\learnscrapy\esp.csv'
# # sequence_of_criteria = ('')
# for row in getstuff(filename):
#     print(row)
#
# import pandas as pd
#
# a = pd.read_csv(filename, header=None, encoding='utf-8')
#
# chunksize = 10 ** 3
# for chunk in pd.read_csv(filename, header=None, encoding='utf-8', chunksize=chunksize):
#     print(chunk.shape)
#     print('hahha')

import requests
from bs4 import BeautifulSoup

link = 'http://search.bilibili.com/topic?keyword=周末放映室=&page={0}'
id = 1
movie_list = []
for i in range(7):
    url = link.format(id + i)
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=30)
    soup = BeautifulSoup(r.text, 'lxml')
    x = soup.find_all('a', class_='title')
    y = soup.find_all('div', class_='des')
    assert len(x) == len(y)
    for j in range(len(y)):
        title = ''.join(list(filter(str.isdigit, x[j].text)))
        href = x[j]['href']
        des = y[j].text
        movie_list.append((title, des, href))

with open('movie_list.csv', 'w', encoding='utf-8', errors='ignore') as file:
    for movie in movie_list:
        file.write("{0}, {1}, {2}\n".format(movie[0].strip(), movie[1].strip(), movie[2].strip()))


