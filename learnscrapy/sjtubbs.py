# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re


def get_html(url):
    try:
        r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=30)
        r.raise_for_status()  # throw HTTPError if the status code is not 200
        # r.encoding = r.apparent_encoding  # handling encoding issue
        return r.text, r.encoding
    except:
        return "Error: something is Wrong!"


def link(tag):
    s = "https://bbs.sjtu.edu.cn"
    if tag.startswith('/'):
        return s + tag
    else:
        return s + '/' + tag


'''
import re
# 爬取BBS前100页笑话数据

    for i in range(10):
        # url = "https://bbs.sjtu.edu.cn/bbsdoc,board,joke,page," + str(i) + ".html"
        url = "https://bbs.sjtu.edu.cn/bbsdoc,board,joke,page,%d.html" % i
        r, code = get_html(url)
        # soup = BeautifulSoup(r, "html.parser")
        soup = BeautifulSoup(r, "lxml")
        tags = [(tag.text, link(tag.get('href'))) for tag in soup.find_all('a') if not tag.text.startswith('Re')]
        print(code)
        # print(tags)

        for tag in tags:
            if re.search(r'board,joke,file', tag[1]):
                print("{0}, {1}".format(tag[0], tag[1]))
                strings = tag[0] + tag[1] + '\n'
'''

# bbscon,board,joke,file,M.1488980222.A.html
posts = []
for page in range(5):
    print('crawling...%d' %page)
    url = "https://bbs.sjtu.edu.cn/bbsdoc,board,joke,page,%d.html" % page
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=30)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "lxml")
    tags = [(tag.text, link(tag.get('href'))) for tag in soup.find_all('a') if not tag.text.startswith('Re')]
    for tag in tags:
        if re.search(r'board,joke,file', tag[1]):
            print("{0}, {1}".format(tag[0], tag[1]))
            posts.append(tag)


with open('./learnscrapy/joke.csv', 'w', encoding='utf-8') as file:
    for post in posts:
        print(post)
        file.write('%s, %s\n' % (post[0], post[1]))



