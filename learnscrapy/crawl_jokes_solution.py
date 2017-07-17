import requests
from bs4 import BeautifulSoup

for page in range(5):
    print('crawling page %d...' % page)
    url = 'https://bbs.sjtu.edu.cn/bbsdoc,board,joke,page,%d.html' % page
    r = requests.get(url, timeout=5)
    html = r.text
    soup = BeautifulSoup(html, 'lxml')
    links = soup.find_all('a')
    links = [link for link in links if 'bbscon,board,joke,file,M' in link.get('href')]
    for link in links:
        post_title = link.get_text()
        post_url = 'https://bbs.sjtu.edu.cn/' + link.get('href')
        if 'Re:' in post_title:
            continue
        else:
            print('%s,%s' % (post_title, post_url))

