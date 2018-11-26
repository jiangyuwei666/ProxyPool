from util.settings import *


class BaseDB(object):
    """
    base database
    """

    def __init__(self, host, port):
        self.__host = host
        self.__port = port

    def add(self, proxy, score=INIT_SCORE):
        pass

    def get(self):
        pass

    def reduce(self):
        pass

    def max(self, proxy):
        pass
