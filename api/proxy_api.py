from flask import Flask, g
from db.mongodb_client import MongodbClient
from util.settings import *

__all__ = ['app']
app = Flask(__name__)


def get_conn():
    """
    连接数据库
    :return:
    """
    # if not hasattr(g, 'mongodb'):
    #     g.mongodb = MongodbClient('proxy', HOST, PORT)
    # return g.mongodb
    connection = MongodbClient()
    return connection


@app.route('/')
def index():
    return "<h2>小蒋娃的代理池</h2>"


@app.route('/get_proxy/')
def get_proxy():
    conn = get_conn()
    return str(conn.get()['proxy'])


@app.route('/get_all/')
def get_all():
    conn = get_conn()
    return conn.get_all()


# if __name__ == '__main__':
#     app.run(host='10.0.117.116')
