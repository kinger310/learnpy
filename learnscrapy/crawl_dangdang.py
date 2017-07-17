import requests
import re

#  get html page using requests
def get_html(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    r = requests.get(url, headers=headers, timeout=30)
    r.raise_for_status()
    return r.text, r.encoding
    # pass # write your code here

# parse html page using regular expression
def parse_html(html):
    pattern = r'<a title="\s([^\"]*?)"\shref=.*?<span class="search_now_price">&yen;(\d+\.\d+)<\/span>'
    products = re.findall(pattern, html)
    return products
    pass  # write your code here


# print product information
def print_info(info_list):
    file_name = r'D:\ProgramFiles\PycharmProjects\learnpy\learnscrapy\dangdang.csv'
    with open(file_name, 'w', errors='ignore') as file:
        for info in info_list:
            for item in info:
                print(item)
                file.write('{0}, {1}\n'.format(item[0], item[1]))
    pass  # write your code here

# main function
def main():
    query = 'Python'
    pages = 5
    search_url = 'http://search.dangdang.com/?key=%s' % query
    info_list = []
    for page in range(1, pages+1):
        try:
            print('crawling...%s' % page)
            url = search_url + '&page_index=%s' % page
            html, encoding = get_html(url)
            info_page = parse_html(html)
            info_list.append(info_page)
            # for (name, price) in info_list:
            #     print(name, price)
            # pass  # write your code here
        except:
            pass  # write your code here
    print_info(info_list)

if __name__=='__main__':
    main()
