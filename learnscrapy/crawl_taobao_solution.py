import requests
import re

#  get html page using requests
def get_html(url):
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    html = r.text
    return html

# parse html page using regular expression
def parse_html(html):
    info_list = []
    if re.search(r'raw_title',html):
        products = re.findall(r'"raw_title":"(.*?)"', html)
    else:
        products = re.findall(r'"title":"(.*?)"',html)
    if re.search(r'view_price', html):
        prices = re.findall(r'"view_price":"(\d+[.]?\d*?)"', html)
    else:
        prices = re.findall(r'"price":"(\d+[.]?\d*?)"', html)
    assert len(products) == len(prices)
    for i in range(len(products)):
        info_list.append((products[i], float(prices[i])))
    return info_list


# print product information
def print_info(info_list):
    print('id\t\tprice\t\tproduct')
    for idx, (product, price) in enumerate(info_list):
        print('%d\t\t%.2f\t\t%s'%(idx, price, product))

# save product information into a file
def save_info(info_list,save_file='data.csv'):
    with open(save_file,encoding='utf-8', mode='w') as fout:
        fout.write('id, price, product\n')
        for idx, (product, price) in enumerate(info_list):
            fout.write('%d, %.2f, %s\n' % (idx, price, product))

# main function
def main():
    query = '空气净化器'
    pages = 2
    search_url = 'https://s.taobao.com/search?q=%s'%(query)
    info_list = []
    for page in range(pages):
        try:
            print('crawling page %d'%page)
            url = '%s&s=%d'%(search_url, page)
            html = get_html(url)
            info_list += parse_html(html)
        except:
            print('Error: something is wrong when crawling page %d'%page)
    print_info(info_list)
    save_info(info_list)

if __name__=='__main__':
    main()
