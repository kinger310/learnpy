# -*- coding: utf-8 -*-

## Demo: use urllib.request to open and read url links
import urllib.request 

url = "https://www.crummy.com/software/BeautifulSoup/"
response = urllib.request.urlopen(url)
print(response)

html = response.read()
print(html)

## Demo: encoding issue
import urllib.request

url = "https://www.douban.com"
response = urllib.request.urlopen(url)
html = response.read()
print(html)
html = html.decode('utf-8') # use decode() method to convert bytes to str
print(type(html))
print(html)

## Demo: encoding issue'
import urllib.request

url = "https://bbs.sjtu.edu.cn/php/bbsindex.html"
response = urllib.request.urlopen(url)
html = response.read()
html = html.decode('gb2312')  # how to find the encoding of the webpage?
print(html)



url = "https://www.crummy.com/software/BeautifulSoup/"
response = urllib.request.urlopen(url)
html = response.read()
html = html.decode('utf-8')  # how to find the encoding of the webpage?
print(html)

#
if 'HTML' in html:
    print('found')
else:
    print('NO')

count = 0
for word in html.split():
    if 'Soup' in word:
        print(word)
        count += 1
print(count)

html.count('Soup')

import chardet #自动检测编码, 安装：pip install chardet
import urllib.request

for url in ["http://www.crummy.com/software/BeautifulSoup",
            "https://www.douban.com",
            "https://bbs.sjtu.edu.cn/php/bbsindex.html"]:
    html = urllib.request.urlopen(url).read()
    mychar = chardet.detect(html)
    print(url,mychar,mychar['encoding'])
    # encoding = mychar['encoding']
    # print(html.decode(encoding)[:1000])


print(count)

## Demo: automatically detect encoding
import chardet
import urllib.request

url = "https://www.douban.com"
html = urllib.request.urlopen(url).read()
mychar = chardet.detect(html)
print(mychar)
print(html.decode(mychar['encoding'])) #自动解码


## Demo: URLError
from urllib.request import urlopen
from urllib.error import URLError

try:
    urlopen("https://www.youtube.com")
except URLError as e:
    print(e)

try:
    urlopen("http://blog.csdn.net/cqcre")
#     urllib.request.urlopen("http://www.sjtu.edu.cn/1234")
#     urllib.request.urlopen("http://www.baidu.com")
except urllib.error.HTTPError as e:
    print(e)
except urllib.error.URLError as e:
    print(e)
else:
    print("OK")

#
## Demo: set user-agent in header
import urllib.request
import urllib.error

try:
    # urllib.request.urlopen("http://blog.csdn.net/cqcre") # if not setting user-agent in hearder, will throw a 403 error
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
                            '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    request = urllib.request.Request(url='http://blog.csdn.net/cqcre', headers=headers)
    response = urllib.request.urlopen(request)
    # html = response.read()
    # print(html.decode('utf-8'))
except urllib.error.HTTPError as e:
    print(e)
except urllib.error.URLError as e:
    print(e)
else:
    print("OK")

## test requests to see if it is installed correctly
import requests

r = requests.get("http://www.douban.com")
print(r.status_code)
print(r.text[:1000])


import requests

r = requests.get("http://www.douban.com", timeout=1)  # 超时参数
print(r.status_code)
print(type(r))

## Demo: Response对象的属性和字符编码处理
import requests
r = requests.get("http://www.sjtu.edu.cn")
print(r.status_code)
print(r.encoding)
print(r.apparent_encoding)
# print(r.text)  # 乱码
r.encoding = r.apparent_encoding
print(r.text)

## Demo: requests handles exceptions
import requests
r = requests.get("http://www.sjtu.edu.cn/1234")
print(r.status_code)
# r.raise_for_status()

import requests
url = "https://item.jd.com/497227.html" #空气净化器
r = requests.get(url, timeout=30)
r.raise_for_status() # throw HTTPError if the status code is not 200
r.encoding = r.apparent_encoding # handling encoding issue
print(r.text[:1000])

import requests
# url = "https://www.amazon.cn/dp/B005GNM3SS/" #空气净化器
url = "https://www.amazon.cn/gp/product/B01ARKEV1G" # 机器学习西瓜书
r = requests.get(url, timeout=30)
print(r.status_code)
r.encoding = r.apparent_encoding  # handling encoding issue
print(r.text)
print(r.request.headers)

# 伪装一个浏览器
## Demo: set user-agnet using "headers"
import requests
url = "https://www.amazon.cn/dp/B005GNM3SS/" #空气净化器
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
# headers = {'User-Agent':'Mozilla/5.0'}
r = requests.get(url, timeout=30, headers=headers) # add header information for user-agent
print(r.status_code)
r.encoding = r.apparent_encoding # handling encoding issue
print(r.text)

## Demo: set keywords to submit using "params"
import requests

keywords={'wd':'python scrape'}
r = requests.get("http://www.baidu.com/s",params=keywords)
print(r.status_code)
print(r.request.url)
print(r.text[:1000])

# keywords = {}
import requests
r = requests.get("https://movie.douban.com/subject/1298250/")
print(r.status_code)
print(r.text[:1000])
print(r.request.url)


## Requests抓取网页的通用代码: 加入异常捕获，超时设定，编码设定，浏览器伪装
import requests

# define get_html() function
def get_html(url):
    try:
        r = requests.get(url, headers={'User-Agent':'Mozilla/5.0'}, timeout=30)
        r.raise_for_status()  # throw HTTPError if the status code is not 200
        r.encoding = r.apparent_encoding # handling encoding issue
        return r.text[:1000]
    except:
        return "Error: something is Wrong!"

# call get_html() function
url_bad = "www.baidu.com"
print(get_html(url_bad))
print()
url = "http://www.baidu.com"
print(get_html(url))

from IPython.display import HTML

htmlString = """<!DOCTYPE html>
<html>
  <head>
    <title>This is a title</title>
  </head>
  <body>
    <h2> Test </h2>
    <p>Hello world!</p>
    <p><a href="http://yangbao.org" target="_blank">My Website</a></p>

  </body>
</html>"""

htmlOutput = HTML(htmlString)
print(type(htmlOutput))


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

## test BeautifulSoup

htmlString = "<!DOCTYPE html><html><head><title>This is a title</title></head><body><h2>Test</h2><p>Hello world!</p></body></html>"

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, "html.parser")
print(html_doc)
print()
print(soup.prettify())  # 友好的输出：prettify()方法

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, "lxml")
print(html_doc)
print()
print(soup.prettify())

print(soup.get_text())



from bs4 import BeautifulSoup
import requests

url = "http://www.crummy.com/software/BeautifulSoup"
r = requests.get(url)

## get BeautifulSoup object
soup = BeautifulSoup(r.text, "html.parser")
print(type(soup))

## compare these print statements
print(soup)
print(soup.prettify())
print(soup.get_text()) # print text by removing tags

## show how to find all a tags
soup.find_all('a')

## ***Why does this not work? ***
# soup.find_all('Soup')

## get attribute value from an element:
## find tag: this only returns the first occurrence, not all tags in the string
first_tag = soup.find('a')
print(first_tag)

## get attribute `href`
print(first_tag.get('href'))
print(first_tag['href'])

## get text
print(first_tag.string)
print(first_tag.text)
print(first_tag.get_text())

## get all links in the page
link_list = [link.get('href') for link in soup.find_all('a')]
print(link_list)

## filter all external links
## create an empty list to collect the valid links
external_links = []

## write a loop to filter the links
## if it starts with 'http' we are happy
for l in link_list:
    if l[:4] == 'http':
        external_links.append(l)

## This throws an error! It says something about 'NoneType'
## lets investigate. Have a close look at the link_list:
# link_list

## Seems that there are None elements! Let's verify
print([link for link in link_list if link is None])

## So there are two elements in the list that are None!



