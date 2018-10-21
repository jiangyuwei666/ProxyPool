# -*- coding: utf-8 -*-
from db.mongodb_client import  MongodbClient
import asyncio
import aiohttp
import time
import sys
try:
    from aiohttp import ClientError
except:
    from aiohttp import ClientProxyConnectionError as ProxyConnectionError
from util.settings import *


class ProxyChecker:
    def __init__(self):
        self.db = MongodbClient('proxy', HOST, PORT)

    async def check_proxy(self, proxy):
        """
        用来异步检查代理是否可用
        :param proxy:
        :return:
        """
        conn = aiohttp.TCPConnector(verify_ssl=False)  # 创建连接，不适用ssl验证
        async with aiohttp.ClientSession(connector=conn) as session:  # 异步建立会话对象（类似requests）
            try:
                if not isinstance(proxy, str):
                    proxy = proxy.decode('utf-8')  # 避免遇到去出来的代理数据类型错误，将其编码成字串类型
                real_proxy = 'http://' + proxy  # 组装成可使用的IP地址
                print('checking...', real_proxy)
                # 用会话发送请求后获取响应response
                async with session.get(TEST_URL, proxy=real_proxy, timeout=15, allow_redirects=False) as response:
                    # 检查response的状态码有咩有有效的状态吗集合里
                    if response in VALID_STATUS_CODE:
                        self.db.max(proxy)  # 在就记为10分
                        print("useful IP", proxy)
                    else:
                        self.db.reduce(proxy)  # 不在就扣分
                        print("fail status code", proxy)
            # 或者因为连接异常，超时异常等，捕捉到并扣分
            except(ClientError, aiohttp.client_exceptions.ClientConnectionError, asyncio.TimeoutError, AttributeError):
                self.db.reduce(proxy)
                print("request fail, useless IP", proxy)

    def run(self):
        """
        控制检查的函数启动
        :return:
        """
        print("Checker is running")
        try:
            count = self.db.count()
            print("last", count, "IPs")
            proxies = self.db.get_all()
            for i in range(0, count, CHECK_SIZE):
                start = i
                stop = min(CHECK_SIZE, count)  # 如果余留数小于每次的检测数，那么就以余留数作为这一次的检测数量
                print("Checking", start + 1, '-', stop)
                test_proxies = proxies[start, stop]  # 获取对应的代理
                loop = asyncio.get_event_loop()  # 开启一个“事件池”，我们可以往里面加入事件，下面两行就是往池里加任务
                tasks = [self.check_proxy(proxy=proxy) for proxy in test_proxies]  # 制定任务：将每一条代理IP检查
                loop.run_until_complete(asyncio.wait(tasks))  # 执行任务
                sys.stdout.flush()
                time.sleep(5)
        except Exception as e:
            print('Checker has something wrong', e.args)


