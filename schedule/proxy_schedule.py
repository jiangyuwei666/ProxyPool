import time
from multiprocessing import Process
from api.proxy_api import app
from spider.proxy_getter import Getter
from spider.proxy_checker import ProxyChecker
from db.mongodb_client import MongodbClient
from util.settings import *


class Scheduler:
    def scheduler_checker(self, cycle=CHECK_CYCLE):
        """
        检测代理可用
        :return:
        """
        checker = ProxyChecker()
        while True:
            print('From Scheduler:Checker is running...')
            checker.run()
            time.sleep(cycle)

    def schedule_getter(self, cycle=GETTER_ENABLED):
        """
        定时获取代理
        :return:
        """
        getter = Getter()
        while True:
            print("From Scheduler:getter is running...")
            getter.run()
            time.sleep(cycle)

    def schedule_api(self):
        """
        打开api，挂起服务器
        :return:
        """
        print("From Scheduler:api is running")
        app.run()  # 这里可以添加服务器的ip地址，这样就可以访问服务器上的ip'host="10.0.117.116"'

    def run(self):
        """
        控制整个代理池启动，开三个进程
        :return:
        """
        if GETTER_ENABLED:
            print('From Schedule:getter is running')
            getter_process = Process(target=self.schedule_getter)
            getter_process.start()
        if CHECKER_ENABLED:
            checker_process = Process(target=self.scheduler_checker)
            checker_process.start()
        if API_ENABLED:
            print('From Schedule:api open')
            api_process = Process(target=self.schedule_api)
            api_process.start()



