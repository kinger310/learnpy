#!/usr/bin/python
# Computational Text Analysis, 2017 Spring
# Lab 2: Crawling and Extracting 10K filings

import os
import re
import requests
from bs4 import BeautifulSoup


# Extract and save 10k URLs
def get_10k_urls(years=range(2010, 2011), save_dir='./index'):
    print("Start to get 10K URLs...")
    base_url = "https://www.sec.gov/Archives/edgar/full-index/%d/QTR%d/form.idx"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    for year in years:
        # save 10k urls year by year
        # index_10k = dict()
        save_file = "%s/10k-%d.index" % (save_dir, year)
        with open(save_file, 'w') as file:
            for qtr in range(1, 5):
                index_url = base_url % (year, qtr)
                try:
                    print("Extracting %s" % index_url)
                    # complete your code here
                    r = requests.get(index_url, timeout=1000)
                    m = re.findall(r"^10-K\s+(.+?)\s+(\d+)\s+(\d{4}-\d{2}-\d{2})\s+(edgar/data/.+?txt)",
                                   r.text, re.I | re.M)
                    html_head = 'https://www.sec.gov/Archives/'
                    for url in m:
                        strings = html_head + url[3] + '\n'
                        file.write(strings)
                except:
                    print("Error: something is wrong when extracting %s" % index_url)


# Extract and save Item 1A. Risk Factors
def extract_10k_item1a(urls, save_dir="./RiskFactors"):
    print("Start to extract Item 1A. 'Risk Factors' from 10Ks...")
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    for i, url in enumerate(urls):
        try:
            r = requests.get(url, timeout=30)
            text = r.text
            soup = BeautifulSoup(text, 'lxml')
            text = ' '.join(soup.strings)  # remove html tags
            # extract item 1a
            pattern1 = r'Item[\s]*1.{0,30}?Business.{30,}?Item[\s]*1A.{0,30}?Risk[\s]*?Factors(.{500,}?Item[\s]*1B)'
            m = parse_text(text, pattern1)
            if not m:
                pattern2 = r'Item[\s]*1.{0,30}?Business.{30,}?Item[\s]*1A.{0,30}?Risk[\s]*?Factors(.{500,}?Item[\s]*2)'
                m = parse_text(text, pattern2)
            if m:
                text_item1a = re.sub(r'\s{2,}', ' ', m)
                save_file = re.split(r'data', url)[-1].replace('/', '_')
                print('%s/RF%s' % (save_dir, save_file))
                with open('%s/RF%s' % (save_dir, save_file), encoding='utf-8', mode='w') as file:
                    file.write('%s' % text_item1a)
            else:
                print("Error: found no item 1a 'Risk Factors' in %s" % url)
        except Exception as e:
            print("Error: something is wrong when extracting %s" % url)
            print(e)
        # if i > 100:
        #     break


# 例如，'Item 1A...Item 1A...Item 1B'，确保右端Item 1B仅和距离最近的Item 1A被匹配到
def parse_text(text, pattern):
    result = re.search(pattern, text, re.I | re.S)
    if result:
        return parse_text(result.group(1), pattern)
    else:
        return text


# Extract and save Item 7. MD&A
def extract_10k_item7(urls, save_dir='./MDA'):
    print("Start to extract Item 7. 'MD&A' from 10Ks...")
    # complete your code here
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    for i, url in enumerate(urls):
        try:
            r = requests.get(url, timeout=30)
            text = r.text
            soup = BeautifulSoup(text, 'lxml')
            text = ' '.join(soup.strings)  # remove html tags
            # extract item 7
            pattern1 = r'Item[\s]*1.{0,30}?Business.{30,}?Item[\s]*7.{0,30}?MANAGEMENT\'S(.{500,}?Item[\s]*7A)'
            m = parse_text(text, pattern1)
            if not m:
                pattern2 = r'Item[\s]*1.{0,30}?Business.{30,}?Item[\s]*7.{0,30}?MANAGEMENT\'S(.{500,}?Item[\s]*8)'
                m = parse_text(text, pattern2)
            if m:
                text_item1a = re.sub(r'\s{2,}', ' ', m)
                save_file = re.split(r'data', url)[-1].replace('/', '_')
                print('%s/MDA%s' % (save_dir, save_file))
                with open('%s/MDA%s' % (save_dir, save_file), encoding='utf-8', mode='w') as file:
                    file.write('%s' % text_item1a)
            else:
                print("Error: found no item 1a 'Risk Factors' in %s" % url)
        except Exception as e:
            print("Error: something is wrong when extracting %s" % url)
            print(e)
        # if i > 30:
        #     break


# Measure
def measure_competition(doc):
    compete_words = {'competition', 'competitor', 'competitive', 'compete', 'competing', 'competitors', 'competes'}
    doc_words = re.split(r'[\s,.?!;:|"\']+', doc.strip())
    doc_words = [word.lower() for word in doc_words if word.isalnum()]
    counter = 0
    for word in doc_words:
        if word in compete_words:
            counter += 1
    return counter


# Main function for lab2, run each step one by one
def main():
    print(os.getcwd())
    # step 1: get 10k urls
    get_10k_urls(years=range(2015, 2017), save_dir='./index')

    # step 2-1: extract Item 1A. Risk Facotrs
    urls = []
    for year in range(2015, 2017):
        urls += [url.strip() for url in open('./index/10k-%d.index' % year, 'r').readlines()]
    # urls = ['https://www.sec.gov/Archives/edgar/data/715579/0001047469-15-001759.txt']
    extract_10k_item1a(urls, save_dir='./RiskFactors')

    # # step 2-2: extract Item 7. MD&A
    urls = []
    for year in range(2015, 2017):
        urls += [url.strip() for url in open('./index/10k-%d.index' % year, 'r').readlines()]
    # urls = ['https://www.sec.gov/Archives/edgar/data/715579/0001047469-15-001759.txt']
    extract_10k_item7(urls, save_dir='./MDA')

    # # step 3: dictionary-based text analysis
    # file_names = os.listdir('./RiskFactors')
    file_names = os.listdir('./RiskFactors')
    for filename in file_names:
        doc = open('./RiskFactors/%s' % filename, encoding='utf-8', mode='r').read()
        compete_measure = measure_competition(doc)
        print('Doc "%s" --> %d' % (filename, compete_measure))


if __name__ == '__main__':
    main()
