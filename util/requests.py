# -*- coding: utf-8 -*-

from lxml import etree
import requests
import time
import random

"""
base_header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9'
}
"""


class Request:
    """
    发送请求的类
    """

    def __init__(self):
        pass

    @property
    def user_agent(self):
        user_agent_list = [
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
            'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
        ]
        return random.choice(user_agent_list)

    @property
    def header(self):
        return {
            'user_agent': self.user_agent,
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9'
        }

    def get_page(self, url, options={}):
        """
            获取代理界面的selector
            :param url: 传入的代理网址
            :param options: 可选，默认为空字典，主要是为了方便在header中添加别的关键字，如cookie
            :return:
            """
        print("Crawling proxy", url)
        header = dict(self.header, **options)
        time.sleep(2)
        r = requests.get(url, header, timeout=15)
        r.encoding = r.apparent_encoding
        if r.status_code == 200:
            print("Selector OK")
            return etree.HTML(r.text)
        else:
            return None

    def get_page_without_header(self, url):
        """
        不用header发送get请求
        :param url:
        :return:
        """
        print("Crawling proxy", url)
        time.sleep(2)
        r = requests.get(url, timeout=10)
        r.encoding = r.apparent_encoding
        if r.status_code == 200:
            print("Selector OK")
            return etree.HTML(r.text)
        else:
            return None

    def get_page_by_post(self, url, data, option={}):
        """
        发送post请求
        """
        header = dict(self.header, **option)
        r = requests.post(url=url, data=data, header=header)
        r.encoding = r.apparent_encoding
        if 200 == r.status_code:
            print('Selector Ok')
            return etree.HTML(r.text)
        else:
            return None
