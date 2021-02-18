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


# 动态url
@app.route("/show/<name>")
def index2(name):
    return f"<p>hello,{name}!!</p>"


# 动态url，指定变量类型
@app.route("/show/<int:age>")
def index3(age):
    return f"hello,{age}!!"


# 动态url，默认变量[1]
@app.route("/show", defaults={'name': 'ls'})
@app.route("/show/<name>")
def index4(name):
    return f"<p>hello,{name}!!</p>"


# 动态url，默认变量[2]
@app.route("/show/<name>")
def index5(name="ls"):
    return f"<p>hello,{name}!!</p>"


import click


@app.cli.command()
def hello():
    click.echo("hello,Human!!")


