# -*- coding: utf-8 -*-

from util.get_selector import get_page
from util.get_selector import get_page_no_header as gpnh  # 有的网址很贱，不加请求头反而还能让你用

class ProxyMetacalss(type):
    """
    自定义元类
    """
    def __new__(cls, name, bases, attrs):
        count = 0
        attrs['__SpiderFunc__'] = []
        for k, v in attrs.items():
            if 'spider_' in k:
                attrs['__SpiderFunc__'].append(k)
                count += 1
        attrs['__SpiderFuncCount__'] = count
        return type.__new__(cls, name, bases, attrs)

class Spider(metaclass=ProxyMetacalss):
    """
    具体的爬虫类，爬取很多的代理网站
    可以动态的添加*spider_*方法，爬去更多的网址
    """
    def get_proxys(self, callback):
        """
        用反射调用所有的“spider_xxxx”方法
        :return:一个列表，是所有的proxy
        """
        proxies = []
        for proxy in eval("self.{}()".format(callback)):
            print("get", proxy)
            proxies.append(proxy)
        return proxies

    def spider_daili66(self, page=3):
        """
        代理66：http://www.66ip.cn/areaindex_1/1.html
        :return:
        """
        for per_page in range(1, page):
            url = "http://www.66ip.cn/areaindex_{page}/1.html".format(page=per_page)
            s = gpnh(url)
            if s is not None:
                print("Crawling", url)
                ip = s.xpath('//tr[1]/following-sibling::*/td[1]/text()')
                port = s.xpath('//tr[1]/following-sibling::*/td[2]/text()')
                for i in range(len(ip)):
                    yield ip[i] + ':' + port[i]

    # def spider_xici(self):
    #     """
    #     西刺高匿代理:http://www.xicidaili.com/nn
    #     :return:
    #     """
    #     url = "http://www.xicidaili.com/nn"
    #     s = get_page(url)
    #     if s is not None:
    #         ip = s.xpath('//tr//td[2]/text()')
    #         port = s.xpath('//tr//td[3]/text()')
    #         print(ip, port)

    def spider_kuaidaili(self):
        """
        快代理：https://www.kuaidaili.com/free/inha/
        :return:
        """
        url = "https://www.kuaidaili.com/free/inha/"
        s = get_page(url)
        if s is not None:
            print("Crawling", url)
            ip = s.xpath('//td[@data-title="IP"]/text()')
            port = s.xpath('//td[@data-title="PORT"]/text()')
            for i in range(len(ip)):
                yield ip[i] + ':' + port[i]

    def spider_fake360daili(self):
        """
        假360代理:http://www.swei360.com/free/?page=1
        :return:
        """
        for per_page in range(2):
            url = "http://www.swei360.com/free/?page={page}".format(page=per_page + 1)
            s = get_page(url)
            if s is not None:
                ip = s.xpath('//tr/td[1]/text()')
                port = s.xpath('//tr/td[2]/text()')
                for i in range(len(ip)):
                    yield ip[i] + ':' + port[i]

    def spider_ip3366(self):
        """
        ip3366:http://www.ip3366.net/free/?stype=1&page=1
        :return:
        """
        for per_page in range(2):
            url = "http://www.ip3366.net/free/?stype=1&page={page}".format(page=per_page + 1)
            s = get_page(url)
            if s is not None:
                ip = s.xpath('//tr/td[1]/text()')
                port = s.xpath('//tr/td[2]/text()')
                for i in range(len(ip)):
                    yield ip[i] + ':' + port[i]



