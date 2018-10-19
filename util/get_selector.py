# -*- coding: utf-8 -*-

from lxml import etree
import requests
import time

base_header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9'
}

def get_page(url, options={}):
    """
    获取代理界面的selector
    :param url: 传入的代理网址
    :param options: 可选，默认为空字典，主要是为了方便在header中添加别的关键字，如cookie
    :return:
    """
    print("Crawling proxy", url)
    header = dict(base_header, **options)
    time.sleep(2)
    r = requests.get(url, header, timeout=15)
    r.encoding = r.apparent_encoding
    if r.status_code == 200:
        print("Selector OK")
        return etree.HTML(r.text)
    else:
        return None

def get_page_no_header(url):
    print("Crawling proxy", url)
    time.sleep(2)
    r = requests.get(url, timeout=10)
    r.encoding = r.apparent_encoding
    if r.status_code == 200:
        print("Selector OK")
        return etree.HTML(r.text)
    else:
        return None


