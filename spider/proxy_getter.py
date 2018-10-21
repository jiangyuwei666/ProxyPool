# -*- coding: utf-8 -*-

from spider.proxy_spider import Spider
from db.mongodb_client import MongodbClient
from util.settings import HOST, PORT
import sys

POOL_UP_LIMIT = 500


class Getter:
    def __init__(self):
        self.spider = Spider()
        self.db_client = MongodbClient('proxy', HOST, PORT)

    def is_excess(self):
        """
        判断是否超出容量上限
        :return:
        """
        if self.db_client.count() >= POOL_UP_LIMIT:
            return True
        else:
            return False

    def run(self):
        """
        控制爬虫启动，执行代理爬取,并放入数据库
        :return:
        """
        print("The Getter is running...")
        for callback_label in range(self.spider.__SpiderFuncCount__):
            callback = self.spider.__SpiderFunc__[callback_label]
            proxies = self.spider.get_proxys(callback)
            sys.stdout.flush()  # linux控制输出的快慢
            for proxy in proxies:
                self.db_client.add(proxy)




