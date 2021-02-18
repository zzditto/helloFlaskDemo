# author:LWZ
# datetime:2021/2/14 19:40

"""
文件说明：

"""
from datetime import datetime
from sayhello import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    body = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
