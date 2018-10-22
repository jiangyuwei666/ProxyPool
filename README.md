# ProxyPool
搭建的一个代理IP池，支持windows和ubuntu。数据库目前采用的MongoDB，后台用的flask。后面会持续维护这个项目。
## 功能
爬取一些代理网站，然后将上面的代理拿下来，同时整理可用的代理，并保存在数据库中。最后通过调api的方式进行代理的调用。
## 模块介绍
这个项目目前有以下5个模块
* [api](https://github.com/jiangyuwei666/ProxyPool/tree/master/api)

    利用flask实现。使用的时候可以用requests请求，就能够返回代理IP。
* [db](https://github.com/jiangyuwei666/ProxyPool/tree/master/db)

    数据库，目前用的是mongodb，后面可能会封装得更好使其能够兼容更多种类得数据库。
* [schedule](https://github.com/jiangyuwei666/ProxyPool/tree/master/schedule)

    调度模块，调度使爬虫，检测器，服务端工作。
* [spider](https://github.com/jiangyuwei666/ProxyPool/tree/master/spider)

    爬取几个代理网址，然后读入数据库，并定时检测代理的可用性。
* [utils](https://github.com/jiangyuwei666/ProxyPool/tree/master/util)

    一些工具类。