# author:LWZ
# datetime:2021/2/14 19:28

"""
文件说明：

"""
import os
from sayhello import app

# dev_db = "sqlite:///" + os.path.join(os.path.dirname(app.root_path), 'data_db')
dev_db = "mysql+pymysql://root:123456@localhost:3306/sayhello"
SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
"""
os.getenv(key, default=None)
如果存在，返回环境变量 key 的值，否则返回 default。
"""
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)
