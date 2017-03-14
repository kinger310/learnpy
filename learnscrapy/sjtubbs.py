# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


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

import re
# 爬取BBS前100页笑话数据
with open('joke.txt', 'a', encoding='gb2312', errors='ignore') as file:
    for i in range(100):
        url = "https://bbs.sjtu.edu.cn/bbsdoc,board,joke,page," + str(i) + ".html"
        r, code = get_html(url)
        soup = BeautifulSoup(r, "html.parser")
        tags = [(tag.text, link(tag.get('href'))) for tag in soup.find_all('a')]
        print(code)

        for tag in tags:
            if re.search(r'board,joke,file', tag[1]):
                print("{0}, {1}".format(tag[0], tag[1]))
                strings = tag[0] + tag[1] + '\n'
                file.write(strings)




# bbscon,board,joke,file,M.1488980222.A.html


