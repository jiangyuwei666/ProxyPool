# -*- coding: utf-8 -*-

import pymongo
from pymongo import MongoClient
from util.settings import HOST, PORT, MAX_SCORE, INIT_SCORE, MIN_SCORE


class MongodbClient:
    def __init__(self, name, host, port):
        self.name = name  # 集合名称
        self.client = MongoClient(host=host, port=port)
        self.db = self.client.proxy  # 指定数据库为proxy

    def change_table(self, name):
        """
        修改操作的集合
        :param name:
        :return:
        """
        self.name = name

    def add(self, proxy, score=INIT_SCORE):
        """
        先看看能不能找到这条代理，找到就不加，找不到就加
        :param proxy:
        :param score:
        :return:
        """
        if self.db[self.name].find_one({'proxy': proxy}) is not None:
            return None
        else:
            self.db[self.name].insert({'proxy': proxy, 'score': score})

    def get(self):
        """
        按照分数获取代理
        先找满分代理，如果找不到就找一个5分的，再找不到就找一个3分的，最后不行就随便找一个
        :return:
        """
        if self.db[self.name].find_one({'score': MAX_SCORE}) is not None:
            return self.db[self.name].find_one({'score': MAX_SCORE})
        elif self.db[self.name].find_one({'score': {'$gt': 5}}):
            return self.db[self.name].find({'score': {'$gt': 5}}).sort('score', pymongo.DESCENDING).limit(1)
        elif self.db[self.name].find_one({'score': {'$gt': 3}}):
            return self.db[self.name].find({'score': {'$gt': 3}}).sort('score', pymongo.DESCENDING).limit(1)
        else:
            return self.db[self.name].find().sort('score', pymongo.DESCENDING).limit(1)

    # def delete(self, proxy):
    #     """
    #     删除代理，当某个代理扣分扣到0就调用这个方法
    #     :param proxy:
    #     :return:
    #     """
    #     self.db[self.name].remove({'proxy': proxy})

    def reduce(self, proxy):
        """
        扣分，请求失败就扣一分，分数=0时调用delete方法删除
        :return:
        """
        condition = {'proxy': proxy}
        result = self.db[self.name].find_one(condition)
        if result['score'] <= 1:
            self.db[self.name].remove({'proxy': proxy})
        else:
            self.db[self.name].update_one(condition, {'$inc': {'score': -1}})

    def max(self, proxy):
        """
        如果代理一开始就能使用就调用这个方法记为10分
        :param proxy:
        :return:
        """
        condition = {'proxy': proxy}
        result = self.db[self.name].find_one(condition)
        result['score'] = 10
        self.db[self.name].update_one(condition, {'$set': result})

    def count(self):
        """
        :return: 总共多少条
        """
        return self.db[self.name].count()

    def get_id(self, proxy):
        """
        返回数据库里的id值
        """
        result = self.db[self.name].find_one({'proxy': proxy})
        return result['_id']


















# if __name__ == '__main__':
#     db = MongoClient('proxy_pool', HOST, PORT)
