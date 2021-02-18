# author:LWZ
# datetime:2021/2/12 18:19

"""
文件说明：

"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<p>hello flask!!</p>"
