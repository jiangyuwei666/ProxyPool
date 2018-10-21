# 数据库地址
HOST = 'localhost'

# 数据库端口
PORT = 27017

# Redis密码，如无填None
# PASSWORD = None

# KEY =

# 代理分数
MAX_SCORE = 10  # 最多10分
MIN_SCORE = 0  # 最少0分，就直接删除
INIT_SCORE = 2  # 刚加进来给2分，三次连接不上就干掉

# 测试API，建议抓哪个网站测哪个
# 选择百度是因为百度一般不会ban，防止有的时候某IP被别人使用后被有的网址ban了就用不了了
TEST_URL = 'http://www.baidu.com'

# 检查周期
TEST_CYCLE = 20
# 获取周期
GET_CYCLE = 300

# 能够正常使用的状态码集合
VALID_STATUS_CODE = [200]

# 每次检测的最大代理数量
CHECK_SIZE = 50

