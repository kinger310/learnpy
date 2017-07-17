#!/usr/bin/python
# Computational Text Analysis, 2017 Spring
# Lab 2: Crawling and Extracting 10K filings

import os
import re
import requests
from bs4 import BeautifulSoup


# Extract and save 10k URLs
def get_10k_urls(years=range(2010,2011), save_dir='./index'):
    print("Start to get 10K URLs...")
    base_url = "https://www.sec.gov/Archives/edgar/full-index/%d/QTR%d/form.idx"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    for year in years:
        # save 10k urls year by year
        index_10k = dict()
        save_file = "%s/10k-%d.index"%(save_dir,year)
        with open(save_file,'w') as fout:
            for qtr in [1,2,3,4]:
                index_url = base_url%(year,qtr)
                try:
                    print("Extracting %s"%index_url)
                    # download index file
                    r = requests.get(index_url,timeout=30)
                    # parse index file and extract 10k url
                    m = re.findall(r"^10-K\s+(.+?)\s+(\d+)\s+(\d{4}-\d{2}-\d{2})\s+(edgar/data/.+?txt)", r.text, re.M)
                    for fields in m:
                        # firm = fields[0]
                        # cik = fields[1]
                        # filing_date = fields[2]
                        url_10k = "https://www.sec.gov/Archives/" + fields[3]
                        fout.write('%s\n'%url_10k)
                except:
                    print("Error: something is wrong when extracting %s"%index_url)


# Extract and save Item 1A. Risk Factors
def extract_10k_item1a(urls, save_dir="./RiskFactors"):
    print("Start to extract Item 1A. 'Risk Factors' from 10Ks...")
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    for url in urls:
        try:
            r = requests.get(url,timeout=30)
            text = r.text
            soup = BeautifulSoup(text,'lxml')
            text = ' '.join(soup.strings) # remove html tags
            # extract item 1a
            m = re.search(r'Item[\s]*1.{,30}?Business.{30,}?Item[\s]*1A.{,30}?Risk[\s]*?Factors(.{30,}?)Item[\s]*1B',text,re.I|re.S)
            if not m:
                m = re.search(r'Item[\s]*1.{,30}?Business.{30,}?Item[\s]*1A.{,30}?Risk[\s]*?Factors(.{30,}?)Item[\s]*2', text, re.I | re.S)
            # here you can add more "if + re" for robustness
            if m:
                text_item1a = re.sub(r'\s{2,}',' ',m.group(1))
                save_file = re.split(r'data',url)[-1].replace('/','_')
                print('%s/RF%s'%(save_dir,save_file))
                # print(text_item1a)
                with open('%s/RF%s'%(save_dir,save_file),encoding='utf-8',mode='w') as fout:
                    fout.write('%s'%text_item1a)
            else:
                print("Error: found no item 1a 'Risk Factors' in %s" % url)
        except Exception as e:
            print("Error: something is wrong when extracting %s" % url)
            print(e)


# Extract and save Item 7. MD&A
def extract_10k_item7(urls, save_dir='./MDA'):
    print("Start to extract Item 7. 'MD&A' from 10Ks...")
    # write your code here


# Measure
def measure_competition(doc):
    compete_words = ['competition', 'competitor', 'competitive', 'compete', 'competing']
    doc_words = re.split(r'[\s,.?!;:|"\']+',doc.strip())
    doc_words = [word.lower() for word in doc_words if word.isalnum()]
    counter = 0
    # write your code here
    return counter


# Main function for lab2, run each step one by one
def main():
    # step 1: get 10k urls
    get_10k_urls(years=range(2015,2017), save_dir='./index')

    # # step 2-1: extract Item 1A. Risk Facotrs
    # urls = []
    # for year in range(2015, 2017):
    #     urls += [url.strip() for url in open('./index/10k-%d.index'%year, 'r').readlines()]
    # extract_10k_item1a(urls, save_dir='./RiskFactors')

    # # step 2-2: extract Item 7. MD&A
    # urls = []
    # for year in range(2015, 2017):
    #     urls += [url.strip() for url in open('./index/10k-%d.index' % year, 'r').readlines()]
    # extract_10k_item7(urls, save_dir='./MDA')

    # # step 3: dictionary-based text analysis
    # filenames = os.listdir('./RiskFactors')
    # for filename in filenames:
    #     doc = open('./RiskFactors/%s'%filename,encoding='utf-8',mode='r').read()
    #     compete_measure = measure_competition(doc)
    #     print('Doc "%s" --> %d'%(filename, compete_measure))


if __name__=='__main__':
    main()